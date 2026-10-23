---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/application-consistent-backups-for-self-managed-databases/
title: Configure application-consistent backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:02.897426+00:00
---

# Configure application-consistent backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/application-consistent-backups-for-self-managed-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure application-consistent backups Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to configure scheduled, application-consistent backups and point-in-time recovery (PITR) workflows for self-managed databases running on Compute Engine Linux virtual machine (VM) instances.

When you back up stateful database workloads—such as IBM Db2, SAP HANA, MySQL, or PostgreSQL—standard crash-consistent snapshots taken by Backup and DR can capture the database while transactions are still in progress. These incomplete transactions can corrupt data, leave tables in inconsistent states, and require lengthy database repair routines upon crash recovery. Application-consistent backups resolve these issues by integrating with the VM guest agent to quiesce the database and optionally freeze the file system before creating a snapshot.

## Before you begin

Complete the following tasks before configuring application-consistent backups.

### Required roles

To get the permissions that you need to configure application-consistent backups, ask your administrator to grant you the following IAM roles on your project: 

  * To configure and manage backup plans: [Backup and DR Backup User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`) 
  * To manage Compute Engine instances: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) 
  * To access Secret Manager secrets from scripts: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Prerequisites

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Verify that billing is enabled for your project.

[Learn how to confirm that billing is enabled](https://cloud.google.com/billing/docs/how-to/verify-project)

  3. Enable the Backup and DR and Secret Manager APIs.

[Enable the APIs](https://console.cloud.google.com/flows/enableapi?apiid=backupdr.googleapis.com,secretmanager.googleapis.com)

  4. Ensure that your database data and log files are stored on standard [Persistent Disks](https://docs.cloud.google.com/compute/docs/disks/persistent-disks). Google Cloud Hyperdisk volumes don't support guest-flush operations.

  5. If you plan to configure point-in-time recovery, configure your database to archive its transaction and redo logs to a dedicated, separate Persistent Disk—for example, mounted at `/db2/ACT/log_archive`.




## Use the bring-your-own-script (BYOS) guest-flush framework

Backup and DR uses the Bring-Your-Own-Script (BYOS) guest-flush framework to quiesce your database before a snapshot is taken. The guest environment relies on two scripts residing in the `/etc/google/snapshots/` directory on your Linux VM instance:

  * **Pre-snapshot script (`/etc/google/snapshots/pre.sh`):** Executes before the snapshot is taken. This script must quiesce database operations and can optionally freeze the file system.
  * **Post-snapshot script (`/etc/google/snapshots/post.sh`):** Executes after the snapshot is taken. This script must optionally unfreeze the file system and resume database operations.



To learn more about database-specific script templates, see Review sample scripts by database type.

### Optional: Freeze and unfreeze file systems

Freezing the file system using the standard Linux utility `fsfreeze` is optional and not mandatory. Quiescing your database ensures application-level transaction consistency. However, if you require additional file-system-level consistency, you can optionally include the following file system freeze and unfreeze commands in your scripts.

Ensure your `pre.sh` and `post.sh` scripts on the VM are configured to handle optional file system freezing for log volumes without suspending database operations.

#### Add file system freeze instructions to pre.sh

If you choose to freeze file systems, add the following discovery and freeze logic at the end of your `pre.sh` script after quiescing the database:
    
    
    # Discover local writeable mount points
    MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
    # FREEZE FILESYSTEMS (Optional)
    for mnt in $MOUNT_POINTS; do
        if ! sudo fsfreeze -f "$mnt"; then
            logger "Error: Failed to freeze $mnt. Cleaning up..."
            # Attempt emergency thaw
            for thaw_mnt in $MOUNT_POINTS; do sudo fsfreeze -u "$thaw_mnt" 2>/dev/null; done
            # Add your database-specific resume/cleanup commands here before exiting
            exit 1
        fi
        logger "Filesystem $mnt is frozen."
    done
    

#### Add file system unfreeze instructions to post.sh

If you freeze file systems in `pre.sh`, add the following unfreeze logic at the beginning of your `post.sh` script before resuming the database:
    
    
    # Discover local writeable mount points
    MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
    # UNFREEZE FILESYSTEMS (Optional)
    for mnt in $MOUNT_POINTS; do
        sudo fsfreeze -u "$mnt"
        logger "Filesystem $mnt is unfrozen."
    done
    

### Fetch credentials dynamically with Secret Manager

Avoid hardcoding static database credentials or passwords inside your shell scripts. Instead, use Secret Manager to fetch credentials dynamically at runtime. Replace static password variables in your scripts with the following logic:
    
    
    # Fetch the database password from Secret Manager dynamically
    DBPASSWORD=$(gcloud secrets versions access latest \
        --secret="SECRET_NAME" \
        --format='get(payload.data)' | tr -d '\n')
    
    if [ $? -ne 0 ]; then
        logger "Critical Error: Unable to fetch the password from Secret Manager."
        exit 1
    fi
    

Replace `SECRET_NAME` with the name of the secret in Secret Manager.

## Review sample scripts by database type

The following samples provide `pre.sh` and `post.sh` implementations for supported database engines running on Linux instances.

**Note:** For Microsoft SQL Server workloads, unlike Linux environments that rely on custom scripts, Windows leverages its built-in Volume Shadow Copy Service (VSS). Within Windows environments, the guest-flush workflow engages the Google Cloud VSS agent to interface with Windows system services. Before a snapshot is taken, VSS automatically flushes file system buffers and quiesces compliant SQL Server workloads, committing all in-memory data to disk to ensure robust application-level consistency. For more information, see [Create a Windows application consistent disk snapshot](/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot).

### IBM Db2

Pre-snapshot script (`/etc/google/snapshots/pre.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/pre.sh
     # 1. Define Mount Points for the Database
     MOUNT_POINTS=("DATA_MOUNT_POINT" "LOG_MOUNT_POINT")
     logger "BYOS Framework: Starting pre-snapshot script."
    
     # 2. QUIESCE DATABASE (Generic Hook)
     # Replace with DB-specific command (e.g., 'db2 set write suspend')
     logger "Suspending Database I/O..."
     # [INSERT DB QUIESCE COMMAND HERE]
    
     # 3. FREEZE FILESYSTEMS (Optional)
     for mnt in "${MOUNT_POINTS[@]}"; do
         if ! sudo fsfreeze -f "$mnt"; then
             logger "Error: Failed to freeze $mnt."
             # Attempt emergency thaw
             for thaw_mnt in "${MOUNT_POINTS[@]}"; do sudo fsfreeze -u "$thaw_mnt" 2>/dev/null; done
             # [INSERT DB RESUME COMMAND HERE]
             exit 1
         fi
         logger "Filesystem $mnt is frozen."
     done
    

Post-snapshot script (`/etc/google/snapshots/post.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/post.sh
     MOUNT_POINTS=("DATA_MOUNT_POINT" "LOG_MOUNT_POINT")
     logger "BYOS Framework: Starting post-snapshot script."
    
     # 1. UNFREEZE FILESYSTEMS (Optional)
     for mnt in "${MOUNT_POINTS[@]}"; do
         sudo fsfreeze -u "$mnt"
         logger "Filesystem $mnt is unfrozen."
     done
    
     # 2. RESUME DATABASE (Generic Hook)
     # Replace with DB-specific command (e.g., 'db2 set write resume')
     logger "Resuming Database I/O..."
     # [INSERT DB RESUME COMMAND HERE]
     logger "BYOS Framework: Cleanup complete."
    

### Oracle

Pre-snapshot script (`/etc/google/snapshots/pre.sh`)
    
    
     sudo mkdir -p /etc/google/snapshots
     sudo tee /etc/google/snapshots/pre.sh > /dev/null << 'EOF'
     #!/bin/bash
     # Place Oracle (ASM) into hot backup mode before Backup and DR captures disks
     su - oracle -c "sqlplus -s / as sysdba" << 'SQL'
     WHENEVER SQLERROR EXIT FAILURE;
     ALTER DATABASE BEGIN BACKUP;
     EXIT;
     SQL
    
     if [ $? -ne 0 ]; then
       echo "Error: Failed to place Oracle in backup mode. Aborting snapshot." >&2
       exit 1
     fi
     EOF
    
     sudo chmod 750 /etc/google/snapshots/pre.sh
    

Post-snapshot script (`/etc/google/snapshots/post.sh`)
    
    
     sudo tee /etc/google/snapshots/post.sh > /dev/null << 'EOF'
     #!/bin/bash
     # Release Oracle from backup mode and archive current redo log to +FRA
     su - oracle -c "sqlplus -s / as sysdba" << 'SQL'
     WHENEVER SQLERROR EXIT FAILURE;
     ALTER DATABASE END BACKUP;
     ALTER SYSTEM ARCHIVE LOG CURRENT;
     EXIT;
     SQL
    
     if [ $? -ne 0 ]; then
       echo "Warning: Failed to execute ALTER DATABASE END BACKUP." >&2
       exit 1
     fi
     EOF
    
     sudo chmod 750 /etc/google/snapshots/post.sh
    

### SAP HANA

**Note:** For SAP specifications, see [SAP Note 2039883 - FAQ: SAP HANA database and data snapshots](https://me.sap.com/notes/2039883).

Pre-snapshot script (`/etc/google/snapshots/pre.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/pre.sh
    
     DISK_ARG="$1"
    
     # 1. Configuration & Discovery
     DBSID="DBSID"
     DBADM="DBADM"
     ID_FILE="/tmp/hana_snapshot_id_$DBSID"
     HDB_KEY="HDB_KEY"
    
     if [[ "$DISK_ARG" == "," ]] || [[ "$DISK_ARG" == "1/0" ]] || [[ "$DISK_ARG" == "sda" ]]; then
         # Dynamically discover all local writeable mount points for full VM image consistency
         # Filters out pseudo, temporary, and read-only filesystems
         MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
         logger "SAP HANA Full VM BYOS: Starting pre-snapshot script for $DBSID."
    
         # 2. QUIESCE DATABASE (Create SAP HANA Snapshot)
         logger "SAP HANA Full VM BYOS: Creating database snapshot..."
    
         # Determine HANA Version
         # Versions 2.0+ use 'FOR FULL SYSTEM' syntax
         HANAVERSION=$(su - $DBADM -c "HDB version" | grep "version:" | awk '{print $2}' | cut -d'.' -f1)
    
         if [ "$HANAVERSION" = "1" ]; then
             SQL="BACKUP DATA CREATE SNAPSHOT COMMENT 'SNAPSHOT_$(date +%Y%m%d)'"
         else
             SQL="BACKUP DATA FOR FULL SYSTEM CREATE SNAPSHOT COMMENT 'SNAPSHOT_$(date +%Y%m%d)'"
         fi
    
         # Execute the snapshot command via hdbsql
         su - $DBADM -c "hdbsql -j -U $HDB_KEY \"$SQL\""
         if [ $? -ne 0 ]; then
             logger "Error: Failed to create SAP HANA snapshot."
             exit 1
         fi
    
         # Retrieve the BACKUP_ID for the prepared snapshot
         ID=$(su - $DBADM -c "hdbsql -j -t -U $HDB_KEY \"SELECT BACKUP_ID FROM M_BACKUP_CATALOG WHERE STATE_NAME = 'prepared' ORDER BY SYS_START_TIME DESC\"" | head -n 2 | tr -d '"' | tail -n 1)
    
         if [ -z "$ID" ]; then
             logger "Error: Could not retrieve BACKUP_ID for prepared snapshot."
             exit 1
         fi
    
         echo "$ID" > "$ID_FILE"
         logger "SAP HANA Full VM BYOS: Database snapshot prepared with ID $ID."
     fi
    

Post-snapshot script (`/etc/google/snapshots/post.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/post.sh
    
     DISK_ARG="$1"
    
     # 1. Configuration & Discovery
     DBSID="DBSID"
     DBADM="DBADM"
     ID_FILE="/tmp/hana_snapshot_id_$DBSID"
     HDB_KEY="HDB_KEY"
    
     if [[ "$DISK_ARG" == "," ]] || [[ "$DISK_ARG" == "1/0" ]] || [[ "$DISK_ARG" == "sda" ]]; then
         # Discover all local writeable mount points to perform unfreeze
         MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
         logger "SAP HANA Full VM BYOS: Starting post-snapshot script for $DBSID."
    
         # 3. RESUME DATABASE (Close SAP HANA Snapshot)
         if [ -f "$ID_FILE" ]; then
             ID=$(cat "$ID_FILE")
             logger "SAP HANA Full VM BYOS: Closing database snapshot ID $ID..."
    
             # Determine HANA version for correct syntax
             HANAVERSION=$(su - $DBADM -c "HDB version" | grep "version:" | awk '{print $2}' | cut -d'.' -f1)
    
             if [ "$HANAVERSION" = "1" ]; then
                 SQL="BACKUP DATA CLOSE SNAPSHOT BACKUP_ID $ID SUCCESSFUL 'SNAPSHOT_COMPLETED'"
             else
                 SQL="BACKUP DATA FOR FULL SYSTEM CLOSE SNAPSHOT BACKUP_ID $ID SUCCESSFUL 'SNAPSHOT_COMPLETED'"
             fi
    
             # Execute the close snapshot command
             RESULT=$(su - $DBADM -c "hdbsql -j -U $HDB_KEY \"$SQL\"")
             if [ $? -ne 0 ]; then
                 logger "Error: Failed to close SAP HANA snapshot. $RESULT"
             else
                 logger "SAP HANA Full VM BYOS: Database snapshot closed successfully."
             fi
    
             # Cleanup the temporary ID file
             rm -f "$ID_FILE"
         else
             logger "Error: Snapshot ID file not found. Manual intervention required to close HANA snapshot."
         fi
    
         logger "SAP HANA Full VM BYOS: Cleanup complete."
    
     else
         MOUNT_POINTS="/hanabackup"
    
         for mnt in $MOUNT_POINTS; do
             sudo fsfreeze -u "$mnt"
             logger "Filesystem $mnt is unfrozen."
         done
     fi
    

Replace the following:

  * `DBSID`: the SAP HANA system identifier (SID) in uppercase.
  * `DBADM`: the SAP HANA administrator OS user (such as `<sid>adm`).
  * `HDB_KEY`: the SAP HANA userstore key configured for database access.



### SAP ASE

Pre-snapshot script (`/etc/google/snapshots/pre.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/pre.sh
     # 1. Configuration
     OSUSER="OS_USER"
     SYB_SERVER="SYB_SERVER_NAME"
     SYB_USER="SYB_USER"
     SYB_PASS="SYB_PASSWORD"
     SYB_DBLIST="DATABASE_LIST"
     TAG_NAME="SNAPSHOT_$(date +%Y%m%d)"
     MANIFEST_DIR="/var/tmp/sybase_manifests" # Directory for manifest files
     # 2. Discovery
     # Dynamically discover local writeable mount points
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
     logger "Sybase Full VM BYOS: Starting pre-snapshot script."
     # 3. QUIESCE DATABASE
     mkdir -p "$MANIFEST_DIR"
     chown $OSUSER "$MANIFEST_DIR"
    
     logger "Sybase Full VM BYOS: Quiescing databases: $SYB_DBLIST..."
     # Command logic from act_sybase_pre.sh
     # We use 'hold' to suspend activity and create the manifest file
     su - $OSUSER -c "isql -U$SYB_USER -P$SYB_PASS -S$SYB_SERVER -X --retserverror" <<EOF
     quiesce database $TAG_NAME hold $SYB_DBLIST for external dump to '$MANIFEST_DIR/manifest_$TAG_NAME.dat' with override
     go
     exit
     EOF
     if [ $? -ne 0 ]; then
         logger "Error: Failed to quiesce Sybase databases."
         exit 1
     fi
     # 4. FREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         if ! sudo fsfreeze -f "$mnt"; then
             logger "Error: Failed to freeze $mnt."
             # Attempt emergency thaw
             for thaw_mnt in $MOUNT_POINTS; do sudo fsfreeze -u "$thaw_mnt" 2>/dev/null; done
             # Release the database quiesce
             su - $OSUSER -c "isql -U$SYB_USER -P$SYB_PASS -S$SYB_SERVER -X" <<EOF
             quiesce database $TAG_NAME release
             go
             exit
     EOF
             exit 1
         fi
         logger "Filesystem $mnt is frozen."
     done
    

Post-snapshot script (`/etc/google/snapshots/post.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/post.sh
    
     # 1. Configuration
     OSUSER="OS_USER"
     SYB_SERVER="SYB_SERVER_NAME"
     SYB_USER="SYB_USER"
     SYB_PASS="SYB_PASSWORD"
     TAG_NAME="SNAPSHOT_$(date +%Y%m%d)"
     MANIFEST_DIR="/var/tmp/sybase_manifests"
    
     # 2. Discovery
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
     logger "Sybase Full VM BYOS: Starting post-snapshot script."
    
     # 3. UNFREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         sudo fsfreeze -u "$mnt"
         logger "Filesystem $mnt is unfrozen."
     done
    
     # 4. RESUME DATABASE
     logger "Sybase Full VM BYOS: Releasing databases for tag $TAG_NAME..."
    
     # Command logic from act_sybase_post.sh
     su - $OSUSER -c "isql -U$SYB_USER -P$SYB_PASS -S$SYB_SERVER -X" <<EOF
     use master
     go
     quiesce database $TAG_NAME release
     go
     exit
     EOF
    
     if [ $? -ne 0 ]; then
         logger "Error: Failed to release Sybase databases."
     else
         logger "Sybase Full VM BYOS: Databases released successfully."
         # Cleanup manifest
         rm -f "$MANIFEST_DIR/manifest_$TAG_NAME.dat"
     fi
    
     logger "Sybase Full VM BYOS: Cleanup complete."
    

Replace the following:

  * `OS_USER`: the operating system user running SAP ASE (such as `sybase`).
  * `SYB_SERVER_NAME`: the SAP ASE server name.
  * `SYB_USER`: the database user with permissions to quiesce databases.
  * `SYB_PASSWORD`: the database user password (or fetch dynamically with Secret Manager).
  * `DATABASE_LIST`: a comma-separated list of databases to quiesce.



### SAP IQ

Pre-snapshot script (`/etc/google/snapshots/pre.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/pre.sh
    
     # 1. Configuration
     OSUSER="OS_USER"
     DB_NAME="DB_NAME"
     CONN_STR="uid=DB_USER;pwd=DB_PASSWORD;dbn=$DB_NAME;eng=ENGINE_NAME"
     BKP_DIR="/var/tmp/sybaseiq_bkp"
     FULL_BKP_FILE="$BKP_DIR/FULL_VIR_DEC"
    
     # 2. Discovery
     # Dynamically discover all local writeable mount points for full VM consistency
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
     logger "SybaseIQ Full VM BYOS: Starting pre-snapshot script."
    
     # 3. QUIESCE DATABASE (Virtual Decoupled Backup)
     mkdir -p "$BKP_DIR"
     chown $OSUSER "$BKP_DIR"
    
     logger "SybaseIQ Full VM BYOS: Preparing virtual decoupled backup..."
    
     # Execute the quiesce command logic from act_sybaseiq_pre.sh
     su -m $OSUSER -c "dbisql -nogui -c '$CONN_STR' \"BACKUP DATABASE FULL VIRTUAL DECOUPLED TO '$FULL_BKP_FILE'\""
    
     if [ $? -ne 0 ]; then
         logger "Error: Failed to freeze (not able to take full_vir_dec backup)."
         exit 1
     fi
    
     # 4. FREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         if ! sudo fsfreeze -f "$mnt"; then
             logger "Error: Failed to freeze $mnt."
             # Attempt emergency thaw
             for thaw_mnt in $MOUNT_POINTS; do sudo fsfreeze -u "$thaw_mnt" 2>/dev/null; done
             # Cleanup quiesce file as backup is invalid
             rm -f "$FULL_BKP_FILE"
             exit 1
         fi
         logger "Filesystem $mnt is frozen."
     done
    

Post-snapshot script (`/etc/google/snapshots/post.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/post.sh
     # 1. Configuration
     OSUSER="OS_USER"
     DB_NAME="DB_NAME"
     CONN_STR="uid=DB_USER;pwd=DB_PASSWORD;dbn=$DB_NAME;eng=ENGINE_NAME"
     BKP_DIR="/var/tmp/sybaseiq_bkp"
     FULL_BKP_FILE="$BKP_DIR/FULL_VIR_DEC"
     INC_BKP_FILE="$BKP_DIR/INC_BKP"
     # 2. Discovery
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
     logger "SybaseIQ Full VM BYOS: Starting post-snapshot script."
     # 3. UNFREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         sudo fsfreeze -u "$mnt"
         logger "Filesystem $mnt is unfrozen."
     done
     # 4. RESUME DATABASE (Post-Snapshot Cleanup)
     logger "SybaseIQ Full VM BYOS: Performing incremental since full backup..."
     # Logic from act_sybaseiq_post.sh to finish the decoupled sequence
     su -m $OSUSER -c "dbisql -nogui -c '$CONN_STR' \"BACKUP DATABASE INCREMENTAL SINCE FULL TO '$INC_BKP_FILE'\""
     if [ $? -ne 0 ]; then
         logger "Error: Failed post-quiesce incremental backup."
     fi
     # Remove temporary files created during quiesce
     rm -f "$FULL_BKP_FILE"*
     logger "SybaseIQ Full VM BYOS: Cleanup complete."
    

Replace the following:

  * `OS_USER`: the operating system user running SAP IQ (such as `sybiq`).
  * `DB_NAME`: the SAP IQ database name.
  * `DB_USER`: the database user with DBA privileges.
  * `DB_PASSWORD`: the database user password (or fetch dynamically with Secret Manager).
  * `ENGINE_NAME`: the SAP IQ database engine name.



### SAP MaxDB

Pre-snapshot script (`/etc/google/snapshots/pre.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/pre.sh
    
     # 1. Configuration
     DBSID="DBSID"
     OSUSER="OS_USER"
     MAXDB_KEY="-user DBM_USER,DBM_PASSWORD"
     AUTOLOG_TMPLT="LOG_BACKUP"
    
     # 2. Discovery
     # Dynamically discover all local writeable mount points for full VM consistency
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
     logger "MaxDB Full VM BYOS: Starting pre-snapshot script for $DBSID."
    
     # 3. QUIESCE DATABASE
     # Optional: Trigger a log backup first to ensure point-in-time recovery readiness
     logger "MaxDB Full VM BYOS: Triggering log backup..."
     su -m $OSUSER -c "dbmcli -d $DBSID $MAXDB_KEY -uUTL -c backup_start $AUTOLOG_TMPLT LOG"
    
     # Suspend logwriter to quiesce the database
     logger "MaxDB Full VM BYOS: Suspending logwriter..."
     su -m $OSUSER -c "dbmcli -d $DBSID $MAXDB_KEY -uUTL -c util_execute suspend logwriter"
     if [ $? -ne 0 ]; then
         logger "Error: Failed to suspend MaxDB logwriter."
         exit 1
     fi
    
     # 4. FREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         if ! sudo fsfreeze -f "$mnt"; then
             logger "Error: Failed to freeze $mnt."
             # Attempt emergency thaw
             for thaw_mnt in $MOUNT_POINTS; do sudo fsfreeze -u "$thaw_mnt" 2>/dev/null; done
             # Resume the logwriter as the backup is no longer consistent
             su -m $OSUSER -c "dbmcli -d $DBSID $MAXDB_KEY -uUTL -c util_execute resume logwriter"
             exit 1
         fi
         logger "Filesystem $mnt is frozen."
     done
    

Post-snapshot script (`/etc/google/snapshots/post.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/post.sh
    
     # 1. Configuration
     DBSID="DBSID"
     OSUSER="OS_USER"
     MAXDB_KEY="-user DBM_USER,DBM_PASSWORD"
    
     # 2. Discovery
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
     logger "MaxDB Full VM BYOS: Starting post-snapshot script for $DBSID."
    
     # 3. UNFREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         sudo fsfreeze -u "$mnt"
         logger "Filesystem $mnt is unfrozen."
     done
    
     # 4. RESUME DATABASE
     logger "MaxDB Full VM BYOS: Resuming logwriter..."
     su -m $OSUSER -c "dbmcli -d $DBSID $MAXDB_KEY -uUTL -c util_execute resume logwriter"
     if [ $? -ne 0 ]; then
         logger "Error: Failed to resume MaxDB logwriter."
     else
         logger "MaxDB Full VM BYOS: Logwriter resumed successfully."
     fi
    
     logger "MaxDB Full VM BYOS: Cleanup complete."
    

Replace the following:

  * `DBSID`: the SAP MaxDB system identifier (SID) in uppercase.
  * `OS_USER`: the operating system user running MaxDB (such as `sdba`).
  * `DBM_USER`: the Database Manager (DBM) user.
  * `DBM_PASSWORD`: the DBM user password (or use a stored DBM key: `-k KEY_NAME`).



### PostgreSQL

Pre-snapshot script (`/etc/google/snapshots/pre.sh`)
    
    
     #!/bin/bash
     # 1. Configuration
     OSUSER="OS_USER"
     PG_HOME="PG_HOME"
     DBUSER="DB_USER"
     PORT=PORT_NUMBER
     DBNAME="DB_NAME"
     FIFO="/tmp/pg_backup_fifo_$PORT"
     PID_FILE="/tmp/pg_backup_pid_$PORT"
     ACT_JOBNAME="SNAPSHOT_$(date +%Y%m%d%H%M%S)"
    
     # 2. Discovery
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
     export PATH=$PG_HOME/bin:$PATH
    
     logger "PostgreSQL Full VM BYOS: Starting pre-snapshot script."
    
     # 3. QUIESCE DATABASE (Session-Bound)
     rm -f "$FIFO"
     mkfifo "$FIFO"
     chown "$OSUSER" "$FIFO"
    
     su "$OSUSER" -c "psql -p $PORT -U $DBUSER -d $DBNAME -f $FIFO" > /tmp/pg_backup_output.log 2>&1 &
     echo $! > "$PID_FILE"
    
     psql_version=$(su "$OSUSER" -c "psql --version" | awk '{print $3}' | cut -d'.' -f1)
     if [ "$psql_version" -ge 15 ]; then
         CMD="SELECT pg_backup_start('$ACT_JOBNAME');"
     else
         CMD="SELECT pg_start_backup('$ACT_JOBNAME');"
     fi
    
     echo "$CMD" > "$FIFO"
     sleep 2
    
     # 4. FREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         if ! sudo fsfreeze -f "$mnt"; then
             logger "Error: Failed to freeze $mnt. Cleaning up..."
             for thaw_mnt in $MOUNT_POINTS; do sudo fsfreeze -u "$thaw_mnt" 2>/dev/null; done
             echo "SELECT pg_backup_stop(); exit;" > "$FIFO"
             rm -f "$FIFO" "$PID_FILE"
             exit 1
         fi
         logger "Filesystem $mnt is frozen."
     done
    

Post-snapshot script (`/etc/google/snapshots/post.sh`)
    
    
     #!/bin/bash
     PORT=PORT_NUMBER
     FIFO="/tmp/pg_backup_fifo_$PORT"
     PID_FILE="/tmp/pg_backup_pid_$PORT"
    
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
     logger "PostgreSQL Full VM BYOS: Starting post-snapshot script."
    
     # 1. UNFREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         sudo fsfreeze -u "$mnt"
         logger "Filesystem $mnt is unfrozen."
     done
    
     # 2. RESUME DATABASE (Close Session)
     if [ -p "$FIFO" ]; then
         logger "PostgreSQL Full VM BYOS: Closing backup session via FIFO..."
         echo "SELECT pg_backup_stop(); SELECT pg_stop_backup(); exit;" > "$FIFO"
         if [ -f "$PID_FILE" ]; then
             wait "$(cat "$PID_FILE")" 2>/dev/null
         fi
         rm -f "$FIFO" "$PID_FILE"
         logger "PostgreSQL Full VM BYOS: Database session closed."
     else
         logger "Error: FIFO not found. Session may have terminated unexpectedly."
     fi
     logger "PostgreSQL Full VM BYOS: Cleanup complete."
    

Replace the following:

  * `OS_USER`: the operating system user running PostgreSQL (such as `postgres`).
  * `PG_HOME`: the path to the PostgreSQL installation directory.
  * `DB_USER`: the PostgreSQL database user with superuser privileges.
  * `PORT_NUMBER`: the port number that PostgreSQL listens on (default: `5432`).
  * `DB_NAME`: the name of the database to connect to.



### MySQL

Pre-snapshot script (`/etc/google/snapshots/pre.sh`)
    
    
     #!/bin/bash
     # 1. Configuration
     DBUSER="DB_USER"
     DBPASSWORD="DB_PASSWORD"
     PORTNO=PORT_NUMBER
     SOCKET_FILE="/var/run/mysqld/mysqld.sock"
     MYSQL_PATH="/usr/bin/mysql"
     FIFO="/tmp/mysql_backup_fifo_$PORTNO"
     PID_FILE="/tmp/mysql_backup_pid_$PORTNO"
    
     # 2. Discovery
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
     logger "MySQL Full VM BYOS: Starting pre-snapshot script."
    
     # 3. QUIESCE DATABASE (Session-Bound Lock)
     rm -f "$FIFO"
     mkfifo "$FIFO"
    
     $MYSQL_PATH -u"$DBUSER" -p"$DBPASSWORD" -S"$SOCKET_FILE" -P"$PORTNO" < "$FIFO" > /tmp/mysql_backup_output.log 2>&1 &
     echo $! > "$PID_FILE"
    
     logger "MySQL Full VM BYOS: Issuing FLUSH TABLES WITH READ LOCK..."
     echo "FLUSH TABLES WITH READ LOCK; SELECT SLEEP(86400);" > "$FIFO"
     sleep 2
    
     # 4. FREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         if ! sudo fsfreeze -f "$mnt"; then
             logger "Error: Failed to freeze $mnt. Cleaning up..."
             for thaw_mnt in $MOUNT_POINTS; do sudo fsfreeze -u "$thaw_mnt" 2>/dev/null; done
             kill $(cat "$PID_FILE") 2>/dev/null
             rm -f "$FIFO" "$PID_FILE"
             exit 1
         fi
         logger "Filesystem $mnt is frozen."
     done
    

Post-snapshot script (`/etc/google/snapshots/post.sh`)
    
    
     #!/bin/bash
     PORTNO=PORT_NUMBER
     FIFO="/tmp/mysql_backup_fifo_$PORTNO"
     PID_FILE="/tmp/mysql_backup_pid_$PORTNO"
    
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
     logger "MySQL Full VM BYOS: Starting post-snapshot script."
    
     # 1. UNFREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         sudo fsfreeze -u "$mnt"
         logger "Filesystem $mnt is unfrozen."
     done
    
     # 2. RESUME DATABASE (Unlock)
     if [ -f "$PID_FILE" ]; then
         logger "MySQL Full VM BYOS: Releasing locks..."
         kill $(cat "$PID_FILE") 2>/dev/null
         rm -f "$FIFO" "$PID_FILE"
         logger "MySQL Full VM BYOS: Locks released and session closed."
     else
         logger "Error: PID file not found. Lock may have been lost prematurely."
     fi
     logger "MySQL Full VM BYOS: Cleanup complete."
    

Replace the following:

  * `DB_USER`: the MySQL database user with administrative privileges.
  * `DB_PASSWORD`: the MySQL database password (or fetch dynamically with Secret Manager).
  * `PORT_NUMBER`: the port number that MySQL listens on (default: `3306`).



### MariaDB

Pre-snapshot script (`/etc/google/snapshots/pre.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/pre.sh
    
     # 1. Configuration
     DBUSER="DB_USER"
     DBPASSWORD="DB_PASSWORD"
     PORTNO=PORT_NUMBER
     SOCKET_FILE="/var/run/mysqld/mysqld.sock"
     MARIADB_PATH="/usr/bin/mariadb" # or /usr/bin/mysql
     SRV_TYPE="Master" # Set to "Slave" for standby nodes
     FIFO="/tmp/mariadb_backup_fifo_$PORTNO"
     PID_FILE="/tmp/mariadb_backup_pid_$PORTNO"
     STARTPOS_FILE="/tmp/STARTPOS_FILE_$PORTNO.txt"
    
     # 2. Discovery
     # Dynamically discover all local writeable mount points for full VM consistency
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
    
     logger "MariaDB Full VM BYOS: Starting pre-snapshot script."
    
     # 3. QUIESCE DATABASE (Session-Bound)
     # Create a FIFO to hold the session open
     rm -f "$FIFO"
     mkfifo "$FIFO"
    
     # Start a background mariadb session that reads from the FIFO
     # This keeps the session (and locks) active until the process is killed
     $MARIADB_PATH -u"$DBUSER" -p"$DBPASSWORD" -S"$SOCKET_FILE" -P"$PORTNO" < "$FIFO" > /tmp/mariadb_backup_output.log 2>&1 &
     echo $! > "$PID_FILE"
    
     # Prepare quiesce query (Logic from act_mariadb_pre.sh)
     if [ "$SRV_TYPE" != "Slave" ]; then
         # Primary node: lock all tables
         logger "MariaDB Full VM BYOS: Issuing FLUSH TABLES WITH READ LOCK..."
         echo "FLUSH TABLES WITH READ LOCK; SELECT SLEEP(86400);" > "$FIFO"
    
         # Capture master status for PITR/replication info
         $MARIADB_PATH -u"$DBUSER" -p"$DBPASSWORD" -S"$SOCKET_FILE" -P"$PORTNO" -e "SHOW MASTER STATUS;" > "$STARTPOS_FILE"
     else
         # Replica node: stop the slave thread
         logger "MariaDB Full VM BYOS: Issuing STOP SLAVE..."
         echo "STOP SLAVE; SELECT SLEEP(86400);" > "$FIFO"
    
         # Capture slave status
         $MARIADB_PATH -u"$DBUSER" -p"$DBPASSWORD" -S"$SOCKET_FILE" -P"$PORTNO" -e "SHOW SLAVE STATUS \G;" > "$STARTPOS_FILE"
     fi
    
     # Wait a brief moment to ensure the command is processed
     sleep 2
     # 4. FREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         if ! sudo fsfreeze -f "$mnt"; then
             logger "Error: Failed to freeze $mnt. Cleaning up..."
             # Attempt emergency thaw
             for thaw_mnt in $MOUNT_POINTS; do sudo fsfreeze -u "$thaw_mnt" 2>/dev/null; done
             # Kill the background session to release locks
             kill $(cat "$PID_FILE") 2>/dev/null
             rm -f "$FIFO" "$PID_FILE"
             exit 1
         fi
         logger "Filesystem $mnt is frozen."
     done
    

Post-snapshot script (`/etc/google/snapshots/post.sh`)
    
    
     #!/bin/bash
     # Location: /etc/google/snapshots/post.sh
     # 1. Configuration
     PORTNO=PORT_NUMBER
     SRV_TYPE="Master"
     DBUSER="DB_USER"
     DBPASSWORD="DB_PASSWORD"
     SOCKET_FILE="/var/run/mysqld/mysqld.sock"
     MARIADB_PATH="/usr/bin/mariadb"
     FIFO="/tmp/mariadb_backup_fifo_$PORTNO"
     PID_FILE="/tmp/mariadb_backup_pid_$PORTNO"
     # 2. Discovery
     MOUNT_POINTS=$(findmnt -n -l -o TARGET -t xfs,ext4,ext3,ext2,btrfs)
     logger "MariaDB Full VM BYOS: Starting post-snapshot script."
     # 3. UNFREEZE FILESYSTEMS (Optional)
     for mnt in $MOUNT_POINTS; do
         sudo fsfreeze -u "$mnt"
         logger "Filesystem $mnt is unfrozen."
     done
     # 4. RESUME DATABASE
     if [ -f "$PID_FILE" ]; then
         logger "MariaDB Full VM BYOS: Resuming database operations..."
         # Kill the background sleep process to automatically release session-bound locks
         kill $(cat "$PID_FILE") 2>/dev/null
         # For slave nodes, explicitly ensure replication is started
         if [ "$SRV_TYPE" = "Slave" ]; then
             $MARIADB_PATH -u"$DBUSER" -p"$DBPASSWORD" -S"$SOCKET_FILE" -P"$PORTNO" -e "START SLAVE;"
         fi
         rm -f "$FIFO" "$PID_FILE"
         logger "MariaDB Full VM BYOS: Cleanup complete."
     else
         logger "Error: PID file not found. Database state might be inconsistent."
     fi
    

Replace the following:

  * `DB_USER`: the MariaDB database user with administrative privileges.
  * `DB_PASSWORD`: the MariaDB database password (or fetch dynamically with Secret Manager).
  * `PORT_NUMBER`: the port number that MariaDB listens on (default: `3306`).



## Deploy guest-flush scripts

After preparing your `pre.sh` and `post.sh` scripts for your database, deploy them to the Linux VM instance:

  1. Connect to the Linux VM instance running your self-managed database by using SSH.

  2. Create the `/etc/google/snapshots/` directory if it doesn't already exist:
         
         sudo mkdir -p /etc/google/snapshots
         

  3. Save your custom `pre.sh` and `post.sh` scripts to the `/etc/google/snapshots/` directory on the VM instance.

  4. Ensure that the scripts have execute permissions:
         
         sudo chmod 755 /etc/google/snapshots/pre.sh /etc/google/snapshots/post.sh
         




## Enable the guest agent for snapshots

To allow Backup and DR to run pre-snapshot and post-snapshot scripts, enable snapshot integration in the Compute Engine guest environment on your Linux VM instance:

  1. Connect to the Linux VM instance running your self-managed database by using SSH (if not already connected).

  2. Open the guest environment configuration file in a text editor:
         
         sudo nano /etc/default/instance_configs.cfg
         

  3. Add or modify the following settings under the `[Snapshots]` section to enable snapshots:
         
         [Snapshots]
         enabled = true
         timeout_in_seconds = 120
         

**Note:** The `timeout_in_seconds` parameter specifies the maximum time the guest agent waits for the `pre.sh` and `post.sh` scripts to finish. Adjust this value to accommodate the duration of your database quiesce or file system freeze operations.
  4. Restart the guest agent on the VM instance to apply the changes:
         
         sudo systemctl restart google-guest-agent
         




## Configure the backup plan

Now that the VM instance is configured with the guest-flush scripts and the guest agent is enabled for snapshots, configure a backup plan in the Google Cloud console:

  1. In the Google Cloud console, go to the **Backup and DR** page.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

  2. From the navigation menu, select **Backup Plans**.

  3. Click **Create Backup Plan** , or select an existing backup plan and click **Edit**.

  4. Under the **Instance Backup** configuration steps, locate the consistency options.

  5. Select the **Enable Application Consistency** option.

  6. Save and apply the backup plan to your VM instance. On schedule, the backup plan triggers the guest agent to run your `pre.sh` script, take the snapshot, and run the `post.sh` script.




## Configure the Persistent Disk backup for database point-in-time recovery

For self-managed databases such as Db2 and SAP HANA, you can configure standalone Persistent Disk backups to capture database archive logs, enabling point-in-time recovery. If you don't require point-in-time recovery, you can skip to Disable guest-flush scripts.

### Best practices for point-in-time recovery log backups

  * **Frequency:** Configure the backup plan schedule for this dedicated log disk to be equal to your point-in-time recovery log granularity, for example, every 15 minutes or hourly.

  * **Cost optimization:** Storing frequent snapshots can increase storage costs. To minimize overhead, configure the **minimum retention period** and the corresponding **immutability vault period** to the minimum allowable time that still satisfies your point-in-time recovery window.




## Recover a self-managed database to a specific point in time

If you have configured regular VM backups alongside dedicated Persistent Disk log backups, follow this procedure to restore your database to a specific point in time. If you didn't configure dedicated log backups or don't require point-in-time recovery, see [Restore a Compute Engine instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore) to restore your VM directly, and skip to Perform post-restore tasks.

### Recovery workflow

  1. **Restore the base VM** : Select the instance backup (machine image) from the backup vault that precedes your target recovery time. Restore it following standard Compute Engine restore procedures. For instructions, see [Restore a Compute Engine instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore).

If you didn't configure dedicated log backups or don't require point-in-time recovery, skip to step 4.

  2. **Attach log disks** : Identify and restore the relevant log disk snapshots captured up to your target recovery time. Attach these newly created disks to the restored instance.

**Note:** You can restore the persistent disk by using the Google Cloud console or by using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) during the roll-forward procedure. You might need to mount multiple log backup disks to ensure all essential archived logs are available.
  3. **Roll forward the database** : Connect to the restored instance by using SSH and execute the database-specific roll-forward command—such as `ROLLFORWARD DATABASE` in Db2—by using the logs located on the newly attached persistent disks.

  4. **Perform post-restore tasks** : Perform any database-specific steps required to bring the application online.

**Caution:** Ensure database configurations are updated if the name of the restored VM or the attached disk paths differ from the source environment.



## Disable guest-flush scripts

To remove the custom guest-flush scripts and disable application consistency:

  1. **Unassign the backup plan from your instance** : In the Google Cloud console, go to the **Backup and DR** page, locate your VM instance under **Protected Resources** , and unassign or delete the backup plan association.

  2. **Remove guest-flush scripts** : Connect to your Linux VM instance by using SSH and remove the custom guest-flush scripts:
         
         sudo rm -f /etc/google/snapshots/pre.sh /etc/google/snapshots/post.sh
         

  3. **Disable snapshot integration in the guest agent** : Open `/etc/default/instance_configs.cfg` on your VM instance, set `enabled = false` under `[Snapshots]`, and restart the guest agent:
         
         sudo systemctl restart google-guest-agent
         




## What's next

  * [Create and manage backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create)
  * [Monitor backup and recovery jobs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console)
  * [Back up Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup)
  * [Restore Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore)
  * [Back up Persistent Disks](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-backup)
  * [Restore Persistent Disks](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
