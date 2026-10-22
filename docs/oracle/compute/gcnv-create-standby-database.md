---
url: https://docs.cloud.google.com/oracle/compute/gcnv-create-standby-database/
title: Create the standby database \u00a0|\u00a0 Oracle on Google Cloud Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:53.203394+00:00
---

# Create the standby database  |  Oracle on Google Cloud Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/gcnv-create-standby-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback 

#  Create the standby database Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to provision the standby database (in this case, `oracdb2`).

To create the standby database `oracdb2`, complete the following steps:

  1. Configure listener and Oracle Data Guard parameters.
  2. Prepare the standby database password file and `NOMOUNT`.
  3. Initialize standby database storage with NetApp Volumes.
  4. Mount standby ASM disk groups.
  5. Finalize the standby instance.
  6. Register the standby database with Oracle Restart.



## Configure listener and Oracle Data Guard parameters

Configure the listener on both database hosts to support Data Guard connections, including the `_DGMGRL` service required for the Broker. Set up the password file and configure archive log parameters on the primary database.

  1. On the primary database `oracdb1`, as `oracle` user, configure the listener and the environment.
         
         sudo su - oracle
         . ~/.bash_profile        # ORACLE_SID=orcl, ORACLE_HOME set

  2. On the standby database `oracdb2`, configure the listener to include `orcls` and `orcls_DGMGRL` services.
         
         GRID_HOME=/u01/app/26ai/grid
         sudo -u grid tee "$GRID_HOME/network/admin/listener.ora" >/dev/null <<'EOF'
         LISTENER =
           (DESCRIPTION =
             (ADDRESS = (PROTOCOL = TCP)(HOST = oracdb2.example.internal)(PORT = 1521)))
         SID_LIST_LISTENER =
           (SID_LIST =
             (SID_DESC = (GLOBAL_DBNAME = orcls)        (ORACLE_HOME = /u01/app/oracle/product/26ai/db_1) (SID_NAME = orcls))
             (SID_DESC = (GLOBAL_DBNAME = orcls_DGMGRL) (ORACLE_HOME = /u01/app/oracle/product/26ai/db_1) (SID_NAME = orcls)))
         EOF

  3. On both the primary and standby databases, restart the listener through Oracle Restart and verify that the `_DGMGRL` service is registered.
         
         sudo -u grid bash -c '
         export GRID_HOME=/u01/app/26ai/grid
         export ORACLE_HOME=$GRID_HOME
         $GRID_HOME/bin/srvctl stop listener
         $GRID_HOME/bin/srvctl start listener
         $GRID_HOME/bin/lsnrctl status
         '

The `lsnrctl status` output must list `SID` and `_DGMGRL`.




## Prepare the standby database password file and `NOMOUNT`

  1. From the primary database, copy the password file to the standby database using Identity-Aware Proxy (IAP) and Google Cloud CLI command `gcloud compute scp`.
         
         PRIMARY_ZONE=us-west1-a       # zone of oracdb1
         STANDBY_ZONE=us-west1-b       # zone of oracdb2
         
         gcloud compute scp oracdb1:/u01/app/oracle/product/26ai/db_1/dbs/orapworcl ./orapworcl \
         --zone=$PRIMARY_ZONE --tunnel-through-iap
         gcloud compute scp ./orapworcl oracdb2:/u01/app/oracle/product/26ai/db_1/dbs/orapworcls \
         --zone=$STANDBY_ZONE --tunnel-through-iap
         

  2. From the primary database `oracdb1`, copy `*.compatible` parameter values.
         
         sudo -u oracle sqlplus -s / as sysdba <<<"SELECT value FROM v\$parameter WHERE name='compatible';"

  3. On the standby database `oracdb2`, set up audit directory and password file.

Replace COPY_FROM_PRIMARY with the value of the `compatible` parameter you copied in the previous step.
         
         sudo -u oracle mkdir -p /u01/app/oracle/admin/orcls/adump
         sudo chown oracle:oinstall /u01/app/oracle/product/26ai/db_1/dbs/orapworcls
         sudo chmod 0600 /u01/app/oracle/product/26ai/db_1/dbs/orapworcls

  4. Create standby `init` parameter file.
         
         sudo -u oracle tee /u01/app/oracle/product/26ai/db_1/dbs/initorcls.ora >/dev/null <<'EOF'
         *.db_name='orcl'
         *.db_unique_name='orcls'
         *.audit_file_dest='/u01/app/oracle/admin/orcls/adump'
         *.diagnostic_dest='/u01/app/oracle'
         *.compatible='<COPY_FROM_PRIMARY>'
         *.sga_target=3072m
         *.pga_aggregate_target=1024m
         *.processes=320
         *.remote_login_passwordfile='EXCLUSIVE'
         *.standby_file_management='AUTO'
         *.fal_server='orcl'
         *.log_archive_config='DG_CONFIG=(orcl,orcls)'
         *.log_archive_dest_1='LOCATION=+RECO VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME=orcls'
         *.log_archive_dest_2='SERVICE=orcl AFFIRM SYNC VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) DB_UNIQUE_NAME=orcl'
         *.log_archive_dest_state_2='DEFER'
         *.log_archive_format='%t_%s_%r.arc'
         *.dg_broker_start=TRUE
         *.undo_tablespace='UNDOTBS1'
         *.open_cursors=300
         *.db_create_file_dest='+DATA'
         *.db_create_online_log_dest_1='+DATA'
         *.db_recovery_file_dest='+FRA'
         *.db_recovery_file_dest_size=25000m
         EOF

  5. Register the standby database and start it in the `NOMOUNT` mode.
         
         echo "orcls:/u01/app/oracle/product/26ai/db_1:N" | sudo tee -a /etc/oratab
         sudo -u oracle bash -c '
         export ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         export ORACLE_SID=orcls
         sqlplus / as sysdba <<SQL
         STARTUP NOMOUNT PFILE=/u01/app/oracle/product/26ai/db_1/dbs/initorcls.ora;
         EXIT
         SQL
         '




The standby database is in `NOMOUNT` mode with no datafiles.

## Initialize standby database storage with NetApp Volumes

NetApp Volumes storage-layer seeding is the primary differentiator of this architecture over a standard Oracle Data Guard setup. Rather than running Oracle Recovery Manager (RMAN) active duplicate which consumes primary database I/O and network bandwidth proportional to database size, NetApp Volumes replicates blocks directly between storage pools. The primary database is unaware of the transfer. It continues serving production workload throughout.

Seed the standby volumes in `oracle-pool-b` using NetApp Volumes, attach them to the standby database `oracdb2`, mount ASM disk groups, and finalize the standby instance at `MOUNT` state.

Choose the standby seeding method based on your environment and recovery requirements.

  * For production: use the Replication path: create and sync replications and Replication path: cut over and attach standby volumes.

  * For labs: use Alternate path: seed from snapshot.




All paths rejoin at Mount standby ASM disk groups and Finalize the standby instance.

### Prerequisites

Make sure that the following prerequisites are met before seeding the standby volumes:

  * Enable the following NetApp Volumes APIs:

API | Use  
---|---  
`gcloud netapp storage-pools` | Create Default-mode Flex Unified pools (--mode=default)  
`gcloud netapp volumes` | iSCSI volumes, host groups, snapshots  
`gcloud netapp volumes replications` | Cross-location volume replication  
  * Two default-mode pools (`oracle-pool-a` and `oracle-pool-b`) in different locations.

  * Source volumes on primary pool attached to `oracdb1-hg`; destination volumes created by replication.

  * Run replication from Cloud Shell or workstation, but not from the database instances.

  * On `oracdb2`, complete iSCSI and ASM host setup.
        
        export PROJECT=PROJECT_ID
        export LOC_A=us-west1-a
        export LOC_B=us-west1-b
        export DEST_POOL="projects/${PROJECT}/locations/${LOC_B}/storagePools/oracle-pool-b"

  * Create a standby storage pool if needed.
        
        gcloud netapp storage-pools create oracle-pool-b \
        --project="${PROJECT}" --location="${LOC_B}" \
        --service-level=flex --type=unified --mode=default \
        --capacity=1024 --network=name=<your-vpc>
        




### Create and sync replications

Create replication relationships from primary database volumes to standby database volumes, and then wait for initial synchronization to finish.
    
    
      gcloud netapp volumes replications create repl-oracdb2-data \
      --project="${PROJECT}" --location="${LOC_A}" --volume=oracdb1_data \
      --replication-schedule=EVERY_10_MINUTES \
      --destination-volume-parameters="storage_pool=${DEST_POOL},volume_id=oracdb2_data,share_name=oracdb2_data"
    
    
    
      gcloud netapp volumes replications create repl-oracdb2-reco \
      --project="${PROJECT}" --location="${LOC_A}" --volume=oracdb1_reco \
      --replication-schedule=EVERY_10_MINUTES \
      --destination-volume-parameters="storage_pool=${DEST_POOL},volume_id=oracdb2_reco,share_name=oracdb2_reco"
    

Wait until `mirrorState` is `MIRRORED` and the initial sync is complete for each replication.

### Cut over and attach standby volumes

Quiesce the primary, stop replication after the final sync, and attach destination volumes to the standby host group.

  1. On the primary, quiesce writes and capture recovery metadata.
         
         ALTER DATABASE BEGIN BACKUP;
         SELECT CURRENT_SCN FROM V$DATABASE;
         ALTER DATABASE CREATE STANDBY CONTROLFILE AS '/tmp/orcls_stby.ctl';
         

  2. Allow one final replication cycle, and then stop the replications.
         
         gcloud netapp volumes replications stop repl-oracdb2-data \
         --project="${PROJECT}" --location="${LOC_A}" --volume=oracdb1_data --force
         
         
         gcloud netapp volumes replications stop repl-oracdb2-reco \
         --project="${PROJECT}" --location="${LOC_A}" --volume=oracdb1_reco --force
         

  3. Attach destination volumes to `oracdb2-hg`. Replicated LUN may keep source name. Use `name=oracdb1_data_lun` on update.
         
         HG=$(gcloud netapp host-groups describe oracdb2-hg --project="${PROJECT}" --location=us-west1 --format='value(name)')
         
         
         gcloud netapp volumes update oracdb2_data --project="${PROJECT}" --location="${LOC_B}" \
         --block-devices="name=oracdb1_data_lun,host-groups=${HG},os-type=LINUX"
         

  4. Copy the controlfile to `oracdb2`, then end backup mode on the primary.
         
         ALTER DATABASE END BACKUP;
         




### Seed from snapshot

Use this path for one-time lab seeding when continuous replication is not required.

For a one-time lab seed, create a source snapshot and create standby volumes from that snapshot in `oracle-pool-b` (Google Cloud console or API). Attach created volumes to `oracdb2-hg`, and then continue with Mount standby ASM disk groups.

## Mount standby ASM disk groups

On the standby host, discover the attached storage paths and mount the ASM disk groups before database recovery.

On `oracdb2`, sign in to standby pool iSCSI portals and rescan multipath devices. If ASM disk headers match primary naming in a lab workflow, use primary-style multipath aliases (for example, `ora_oracdb1_data_01`, `ora_oracdb1_arch_01`), set `asm_diskstring='/dev/mapper/ora_oracdb1_*p*'`, and confirm partition ownership is `grid:asmadmin`, then mount disk groups:
    
    
    ALTER DISKGROUP DATA MOUNT FORCE;
    ALTER DISKGROUP RECO MOUNT FORCE;
    ALTER DISKGROUP FRA MOUNT FORCE;
    

### Finalize the standby instance

Restore the standby controlfile, recover to the captured SCN, convert to physical standby, and start managed recovery.
    
    
    STARTUP NOMOUNT;
    RESTORE STANDBY CONTROLFILE FROM '/tmp/orcls_stby.ctl';
    ALTER DATABASE MOUNT;
    RECOVER DATABASE UNTIL SCN <quiesce_scn>;
    ALTER DATABASE CONVERT TO PHYSICAL STANDBY;
    SHUTDOWN IMMEDIATE;
    STARTUP MOUNT;
    ALTER DATABASE RECOVER MANAGED STANDBY DATABASE DISCONNECT FROM SESSION;
    

At this point, the standby should be `PHYSICAL STANDBY` and `MOUNTED` with managed recovery started.

## Register the standby database with Oracle Restart

Register the standby with Oracle Restart so that reboots automatically recover ASM disk groups, mount the standby database, and restart managed recovery. Also, add the application service to both database resources.

  1. On `oracdb2`, capture the `spfile` location and register with Oracle Restart.

Replace STANDBY_SPFILE_PATH from the query (often under `+DATA`).
         
         sudo -u oracle bash -c '
         export ORACLE_SID=orcls
         sqlplus -s / as sysdba <<< "SHOW PARAMETER spfile;"
         '
         sudo -u oracle bash -c '
         export GRID_HOME=/u01/app/26ai/grid
         export ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         export PATH=$ORACLE_HOME/bin:$GRID_HOME/bin:$PATH
         srvctl add database \
           -db orcls \
           -dbname orcl \
           -oraclehome /u01/app/oracle/product/26ai/db_1 \
           -spfile <STANDBY_SPFILE_PATH> \
           -pwfile /u01/app/oracle/product/26ai/db_1/dbs/orapworcls \
           -role PHYSICAL_STANDBY \
           -startoption MOUNT \
           -stopoption IMMEDIATE \
           -diskgroup DATA,RECO,FRA
         srvctl config database -db orcls
         srvctl status database -db orcls
         '

  2. On `oracdb1`, verify and update the primary database resource to include all ASM disk group dependencies.
         
         sudo -u oracle bash -c '
         export GRID_HOME=/u01/app/26ai/grid
         export ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         export PATH=$ORACLE_HOME/bin:$GRID_HOME/bin:$PATH
         srvctl config database -db orcl
         srvctl modify database -db orcl -diskgroup DATA,RECO,FRA
         srvctl config database -db orcl
         '

  3. Add the application service on the standby database resource (`orcls` on `oracdb2`). Use role `PRIMARY` on both sides so that `orclapp` is available after switchover.
         
         sudo -u oracle bash -c '
         export GRID_HOME=/u01/app/26ai/grid
         export ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         export PATH=$ORACLE_HOME/bin:$GRID_HOME/bin:$PATH
         srvctl add service \
           -db orcls \
           -service orclapp \
           -pdb orclpdb \
           -role PRIMARY \
           -policy AUTOMATIC
         srvctl config service -db orcls -service orclapp
         '

  4. On `oracdb2`, verify the standby database resource.
         
         sudo -u oracle bash -c '
         export GRID_HOME=/u01/app/26ai/grid
         export ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         export PATH=$ORACLE_HOME/bin:$GRID_HOME/bin:$PATH
         srvctl status database -db orcls
         '




## What's next

  * [Finalize the standby database for Oracle Data Guard](https://docs.cloud.google.com/oracle/compute/gcnv-finalize-standby).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
