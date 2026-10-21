---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-oracle/
title: Prepare Oracle databases for Backup and DR on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:52.008809+00:00
---

# Prepare Oracle databases for Backup and DR on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Prepare Oracle databases for Backup and DR on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Before you begin, it's a good idea to review [Backup and DR for Oracle](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro).

Before you can back up Oracle databases, you must add the Oracle server as a host to Backup and DR. For this to work, be sure to consult [Prerequisites for backing up an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites) and then follow these preparation steps.

Preparation procedures for Oracle databases Step | Preparation procedure  
---|---  
1  |  [Prepare Oracle databases in a Linux environment](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-oracle) or   
[Prepare Oracle databases in a Windows environment](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-oracle-windows)  
2  |  [Prepare to back up an Oracle database with data files on an ASM disk group](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#capture-db)  
3  |  [Prepare Oracle database authentication](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#authentication)   
[Enable database block change tracking (optional)](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#block-change)   
[Protect from an Oracle Data Guard node](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#data-guard)   
[Configure RAC transparent failover of RMAN backup to other nodes](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#rac-failover)   
[Oracle archive logs compression](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#archive-logs)   
[Configure Oracle database services for load balancing across multiple nodes](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#multiple-nodes)   
[Patch Oracle 12c](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#patch)  
  
  
## Prepare Oracle databases in a Linux environment

Before you protect an Oracle database, or if database protection jobs fail, make sure that the following settings are correct on the Oracle database server.

  * Each Oracle database to be protected must be up and running. For example:


    
    
    database: actdb
    ps -ef | grep pmon | grep -i actdb
    oracle   27688     1  0  2015 ?        00:26:24 ora_pmon_actdb
    

  * The database must be running in archive log mode. To verify that the database is running in archive log mode, sign in to the database server as Oracle OS user and set the database environment variable:


    
    
    export ORACLE_HOME=<oracle home path>
    # Get this from /etc/oratab
    export ORACLE_SID=<database instance name>
    export PATH=$ORACLE_HOME/bin:$PATH
    
    
    
     Login to sqlplus:
    
    
    
    sqlplus / as sysdba
    archive log list;
    Database log mode   Archive Mode
    Automatic archival        Enabled
    Archive destination        +FRA
    Oldest online log sequence     569
    Next log sequence to archive   570
    Current log sequence        570
    
    
    
     Note: If archive log mode is not enabled then get archive mode enabled
     before proceeding.
    

  * The database should be using `spfile`. Verify that the database is running with `spfile`:


    
    
    sqlplus / as sysdba
    show parameter spfile
    NAME      TYPE   VALUE
    ------------------ ----------- ------------
    spfile      string  +DATA/ctdb/spfilectdb.ora
    
    
    
     Note: If the value is `null_` then
     get the spfile set. Backup and DR supports backing up using pfile as well.
     pfile should be available in default location. For example, a
     Linux `pfile` should be located under `$ORACLE_HOME/dbs`.
    

  * For Oracle RAC database, the snapshot control file must be located under shared disks. For an Oracle RAC database under ASM, the snapshot control file must be located under shared disks.

To check this, connect to RMAN and run the `show all` command. Configure it if necessary:
        
        rman target /
        

Then in RMAN:
        
        show all
        

RMAN configuration parameters for database with db_unique_name CTDB are:



    
    
    CONFIGURE RETENTION POLICY TO REDUNDANCY 1; # default
    CONFIGURE BACKUP OPTIMIZATION OFF; # default
    CONFIGURE DEFAULT DEVICE TYPE TO DISK; # default
    CONFIGURE CONTROLFILE AUTOBACKUP OFF; # default
    CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '%F'; # default
    CONFIGURE DEVICE TYPE DISK PARALLELISM 1 BACKUP TYPE TO BACKUPSET; # default
    CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/mnt/ctdb/snapcf_ctdb.f';
    
    
    
     This example shows the configuration set to the local file system.
    
     In a RAC environment, this must be set to shared ASM Disk Group. To put it
     on the ASM Disk Group, use:
    
    ```bash
    CONFIGURE SNAPSHOT CONTROLFILE NAME TO '+(disk group name)/snap_(database name).f';
    ```
    

## Prepare to back up an Oracle database with data files on an ASM disk group

**Backup and DR staging disk on an ASM disk group**

The ASM diskstring parameter must be set and is not null. Sign in to the database server as ASM OS user and set the ASM environment variable:
    
    
    export ORACLE_HOME=(oracle ASM home path)
    # Get this from /etc/oratab
    export ORACLE_SID=(ASM instance name)
    export PATH=$ORACLE_HOME/bin:$PATH
    

Connect to `sqlplus`:
    
    
    sqlplus / as sysasm
    show parameter asm_diskstring
    NAME      TYPE   VALUE
    ------------------- ----------- ------------------------------
    asm_diskstring      string  ORCL:*, /dev/sdt1, /dev/sdu1
    

If the result of value is null, then get the correct ASM disk string value for existing ASM disks before proceeding with Backup and DR protection. The Backup and DR backup adds its disk string path (`/dev/Backup and DR/asm/*`) for its backup staging disk to map to ASM.

**Backup and DR staging disk on the file system**

If you are protecting an Oracle ASM database to a file system, then **Convert ASM to file system** must be set to **Yes** under **Application Details & Settings**. See [Application details & settings for Oracle Databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings).

## Prepare Oracle database authentication

The following additional preparation steps are required only if you plan to use database authentication. Oracle database authentication is described in [Backup and DR using database authentication](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites#oracle-db-auth).

**Note:** Backup and DR does not support database authentication to Oracle in Windows environments.

  1. Follow the steps in Prepare Oracle databases in a Linux environment.

  2. Create a database user account for Backup and DR backup, if not provided:



    
    
    create user act_rman_user identified by <password>;
    

  1. Grant `sysdba` access to all RAC nodes by logging into `sqlplus` to all nodes and running:


    
    
    grant create session, resource, sysdba to act_rman_user;
    

For Oracle 12c this role can be `sysbackup` instead `of sysdba`, and the database username starts with #.

  1. Verify that the `sysdba` role has been granted on all nodes in the RAC environment:


    
    
    sqlplus / as sysasm
    select * from gv$pwfile_users;
    INST_ID USERNAME SYSDB SYSOP SYSAS
    ---------- --------------  ----- ----- -----
    1 SYS TRUE TRUE FALSE
    2 SYS TRUE TRUE FALSE
    1 ACT_RMAN_USER TRUE TRUE FALSE
    2 ACT_RMAN_USER TRUE TRUE FALSE
    

  1. Test the service name based on your environment type using the following instructions:

     * Create and verify the Oracle servicename in a non-RAC environment

     * Create and verify the Oracle servicename in a RAC environment




### Create and verify the Oracle servicename in a non-RAC environment

The Oracle servicename is used for database authentication only. It is not needed for OS authentication.

Example: Database name: `dbstd`, Instance Name: `dbstd`

  1. If the Oracle servicename is not listed, then create the service name entry in the `tnsnames.ora` file at `$ORACLE_HOME/network/admin` or at `$GRID_HOME/network/admin` by adding the entry:


    
    
    act_svc_dbstd =
    (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = (IP of the database server))(PORT = 1521))
    (CONNECT_DATA =
    (SERVER = DEDICATED)
    (SERVICE_NAME = dbstd)
    ) )
    

If the `tnsnames.ora` file is in a non-standard location, then provide the absolute path to it under **Application Details & Settings** as described in [Application details & settings for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)

  1. Test the service name entry for the database to make sure it is configured:

Login as Oracle OS user and set the Oracle environment:



    
    
    TNS_ADMIN=(tnsnames.ora file location)
    tnsping act_svc_dbstd
    

  1. Check the database user account to be sure the Backup and DR backup can connect:


    
    
    sqlplus act_rman_user/act_rman_user@act_svc_dbstd as sysdba
    

  1. Provide the servicename created (act_svc_dbstd) under the Oracle Service Name setting under **Application Details & Settings** as described in [Application details & settings for Oracle Databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)



### Create and verify the Oracle servicename in a RAC environment

The Oracle servicename is used for database authentication only. It is not needed for OS authentication.

Example three-node RAC:

  * Database name: `dbrac`

  * Instance1 name: `dbrac1`

  * Instance2 name: `dbrac2`

  * Instance3 name: `dbrac3` with database protection being set from Node3 (Instance name `dbrac3`):



  1. Create a servicename entry in `tnsnames.ora` file at `$ORACLE_HOME/network/admin` or at `$GRID_HOME/network/admin` by adding the following entry:


    
    
    act_svc_dbrac3 =
    (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = (IP of the database server)(PORT = 1521))
    (CONNECT_DATA =
    (SERVER = DEDICATED)
    (INSTANCE_NAME = dbrac3)
    (SERVICE_NAME = dbrac)
    ) ) )
    
    
    
         Where:
         HOST = This can be SCAN IP in a RAC environment or VIP or IP of the node 3 database server.
        SERVICE_NAME = database name
        INSTANCE_NAME = database instance name on node3
    

  1. Test the servicename:

Login as Oracle OS user and set the Oracle environment:



    
    
    TNS_ADMIN=(tnsnames.ora file location)
    tnsping act_svc_dbrac3
    

  1. Check the database user account to be sure the Backup and DR backup can connect:


    
    
    sqlplus act_rman_user/act_rman_user@act_svc_dbrac3 as sysdba
    

  1. Provide the service name created (act_svc_dbrac3) under the Oracle Service name setting under **Application Details & Settings** described in [Application details & settings for Oracle Databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings).

If the tnsnames.ora file is in a non-standard location, then provide the absolute path to the tnsnames.ora file under the Oracle `TNS_Admin` Path setting udner **Application Details & Settings** described in [Application details & settings for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)




## Enable database block change tracking (optional)

Database change block tracking is described in [Oracle database block change tracking (BCT)](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro#bct)

To check if database block change tracking is enabled:
    
    
    sqlplus / as sysdba
    

On the sql prompt:
    
    
    select * from v$block_change_tracking;
    

**Note:** Tracking is optional. Oracle standard edition and Oracle express edition do not support tracking. Tracking is described in [Oracle Database Block Change Tracking (BCT)](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro#bct).

If database block change tracking is not enabled, then enable database block change tracking from sqlplus:

### Using ASM Disk Group
    
    
    sqlplus / as sysdba
    

On the sql prompt:
    
    
    alter database enable block change tracking using file '+<ASM Disk Group Name>/<database name>/<dbname>.bct';
    

### Using file system
    
    
    sqlplus / as sysdba
    

On the sql prompt:
    
    
    alter database enable block change tracking using file '$ORACLE_HOME/dbs/<dbname>.bct';
    

## Protect from an Oracle Data Guard node

You can protect an Oracle database from primary database nodes or from Oracle Data Guard standby nodes. If protection is set from an Oracle Data Guard node, then make sure to set the primary node credentials under Application Details & Settings in the appliance management console.

### For database authentication (Linux only)

  * **Username/Password** : The database user account credentials. In order for this user account to be available on the Data Guard node with sysdba access, this user must be created with sysdba privilege at the Primary node (see creating backup user account with sysdba access). Then the password file (under `$ORACLE_HOME/dbs/`) from the primary node must be copied over to the Data Guard node.

**Note:** Backup and DR does not support database authentication to Oracle in Windows environments.



### For OS authentication

  * **Username/Password** : Under OS Authentication, sysdba privilege is not required. This database user account needs the privilege `connect, alter system`. In order for this user account to be available on the Data Guard node, this user must be created at the primary node.



If the user does not have the sysdba role, then the user needs `grant connect, alter system, select on dba_tablespaces`.

To grant these privileges, on the sql prompt:
    
    
    grant connect, alter system, select on dba_tablespaces to act_rman_user;
    

  * **Oracle Data Guard Primary Node Servicename** : This is the servicename in the tnsnames.ora file configured on the Data Guard node to connect to the primary node from the standby node. Oracle Data Guard Primary Node Servicename is required for both OS and DB authentication if the backup is configured from the Data Guard standby node.



For full details on all details & settings, see [Application details & settings for Oracle Databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)

Database Node | OS Authentication | Database Authentication  
---|---|---  
Primary  |  No database credentials are needed.  |  Database credentials are needed. If no role is selected, then sysdba is used.   
Standby  |  Database credentials are needed even for OS Auth (to connect to primary to switch log). The database credentials don't need to have a sysdba/sysbackup role. If a sysdba/sysbackup account is used, then set the user role in **User Role in the Database** in the Application Details & Settings.  |  Database credentials are needed. The database credentials must be for either the sysdba or sysbackup role, and **User Role in the Database** must be set to sysdba or sysbackup in the [Application Details & Settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-oracle). To set up database authentication, see [Enabling Database Authentication for an Oracle Server](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites#oracle-db-auth).   
  
## Configure RAC transparent failover of RMAN backup to other nodes

The Backup and DR agent must be installed and running on all nodes that you plan to be part of the backup failover configuration. The protection is set up from one node only.

**Note:** In an Oracle One Node environment, both nodes must be discovered and protected with the same template and profile.

In Details & Settings, Cluster Nodes, specify the failover node choice in a Oracle RAC environment:
    
    
    <Failover choice>:<Node IP>:<Servicename>:<Role>
    

Where:

  * **Failover Choice:** the order of node in which to fail over.

  * **Node IP:** the IP address of the node where you want the backup to run

  * **Servicename:** the name of the service created and specified in the tnsnames.ora for Backup and DR RMAN backup. This can be a new dedicated service created for Backup and DR backup or the SID name (instance name) of the database on that node.

  * **Role:** F, indicating it is a failover node




To create a new servicename on failover node under tnsnames.ora file ($ORACLE_HOME/network/admin/tnsnames.ora or at $GRID_HOME/network/admin/tnsnames.ora)

### Example in an Oracle One Node environment

RAC One Node consists of two nodes:

172.15.157.200   
172.15.157.201

It has one database OneN running only at one of the nodes at any given time. OneN is protected from 172.15.157.200, with Cluster Node settings specified as 1:172.15.157.201:OneN:F

If OneN fails over to 172.15.157.201, Backup and DR backup follows it and starts the next backup job from 172.15.157.201 instead of 200. If failover occurs in the middle of a backup job, then the job fails and the next job uses the failover node to start new backup.

Example in an Oracle Environment, not One Node:

  * 2 node RAC (`dbrac1`, `dbrac2`)

  * Protection is set using database name "dbrac" from `dbrac1` and failover is to be set to `dbrac2`

  * Service name on node2: `act_svc_dbrac2`

  * Node2 IP or scan IP: `172.1.1.0`



    
    
    act_svc_node2 =
          (DESCRIPTION =
          (ADDRESS = (PROTOCOL = TCP)(HOST = 172.1.1.0)(PORT = 1521))
          (CONNECT_DATA =
          (SERVER = DEDICATED)
          (INSTANCE_NAME = dbrac2)
          (SERVICE_NAME = dbrac)
          ) )
    

Under **Application Details & Settings**, the cluster nodes entries are the following:
    
    
    1:172.1.1.1:act_svc_node2:F
    

### The behavior of cluster node entries F and M

**F** : Failover node, only participates when protecting node is not to perform the backup.

**M** : Maintenance node, replaces protecting node if validated to be able to perform the backup.

## Oracle archive logs compression

Backup and DR archive log backup supports Oracle log backup set compression. The type of compression you select depends on these RMAN configuration settings. Select an option based on your use case.

  * Lower compression ratios create the least impact on backup throughput. These are best suited for environments where CPU resources are the limiting factor.

  * Medium compression is recommended for most environments. These provide a good combination of compression ratios and speed.

  * High compression ratios are resource intensive and are best suited for backups over slower networks where the limiting factor is network speed.




The default setting is Basic. Basic does not require Oracle Advanced Compression.

To check the type of compression set in the environment, run the `show all` command from the RMAN prompt:
    
    
    rman target /
    
    
    
    show all
    

## Configure Oracle database services for load balancing across multiple nodes

This procedure applies only to Oracle ASM databases. In this example, assume a four-node RAC environment; nodes 3 and 4 are to be load-balanced for backup use.

See:

  * Configure parallel RMAN image copy from multiple nodes

  * Configure Oracle database services for load balancing across multiple nodes




Load balancing between Oracle RAC nodes requires Oracle database authentication.

### Configure parallel RMAN image copy from multiple nodes

In a RAC environment, you can configure backup to run in parallel from multiple nodes.

  1. Install the Backup and DR agent on all nodes.

  2. Setup the ASM disk group mapping to node 3 and node 4 using Application details & settings.

  3. Create a database service using srvctl to run from node 3 and node 4.

  4. Use this service to specify under **Application Details & Settings**. Choose Number of channels under Advanced Settings (# of channels). RMAN distributes the channels between node 3 and node 4.

  5. Set Oracle servicename and RAC Member Nodes.




### Configure Oracle Database Services for load balancing across multiple nodes

  1. Configure in **Application Details & Settings**, RAC Member Nodes: IP of node3 and IP of node 4.

  2. Create a database service for the maintenance node to be used by Backup and DR for backup:



    
    
    srvctl add service -d <dbname> -s act_service_<dbname> -r <dbinstance3>,<dbinstance4>
    srvctl start service -d <dbname> -s act_service_<dbname>
    

  1. Add the tns entry for the Oracle service name created on backup nodes (`dbinstance3`and `dbinstance4` node in this example) under tnsnames.ora file ($ORACLE_HOME/network/admin/tnsnames.ora or at $GRID_HOME/network/admin/tnsnames.ora)


    
    
    act_service_<dbname> =
    (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = <SCAN IP>)(PORT = 1521))
    (CONNECT_DATA =
    (SERVER = DEDICATED)
    (SERVICE_NAME = <DATABASE NAME>)
    ) )
    

  1. Test the created servicename created:


    
    
    tnsping act_service_<dbname>
    

  1. Test the servicename and user credentials:


    
    
    sqlplus act_rman_user/act_rman_user@act_service_<dbname> as sysdba
    

  1. Specify this service name under **Application Details & Settings** Oracle service name.

  2. Create a dedicated archive log backup service on a protected node (e.g. node 3) to be used for backup:



    
    
    srvctl add service -d <dbname> -s act_arc_service_<dbname> -r <dbinstance3>
    srvctl start service -d <dbname> -s act_arc_service_<dbname>
    

  1. Add the tns entry for the archive log backup service name created under `tnsnames.ora` file (`$ORACLE_HOME/network/admin/tnsnames.ora` or at `$GRID_HOME/network/admin/tnsnames.ora`)


    
    
    act_arc_service_<dbname> =
    (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = <SCAN IP>)(PORT = 1521))
    (CONNECT_DATA =
    (SERVER = DEDICATED)
    (INSTANCE_NAME = <node 3 instance>)
    (SERVICE_NAME = act_arc_service_<dbname>)
    ) )
    

  1. Test the service name:


    
    
    tnsping act_arch_service_<dbname>
    

  1. Specify this servicename under **Application Details & Settings** archive log backup servicename.

**Note:** Load balancing between Oracle RAC nodes requires Oracle database authentication.

### Patch Oracle 12c

Backup and DR application aware mounts may fail if your Oracle 12c installation does not include this patch, which can be downloaded from the Oracle support portal:

Oracle Database 12c Bug# 19404068 (ORA-1610 ON RECOVER DATABASE FOR CREATED CONTROLFILE)

  * (Patch 19404068) Linux x86-64 for Oracle 12.1.0.2.0



To see if the patch is installed, run:
    
    
    cd $ORACLE_HOME/OPatch
    ./opatch lsinventory -details
    ./opatch lsinventory -details | grep 19404068
    

## What's Next

Before adding the Oracle host, continue to:

  1. (Optional) [Use Oracle Direct NFS with Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-dnfs)
  2. [Oracle patches and known issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues)



## The Oracle DBA Guide

  * [Backup and DR for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro)
  * [Prerequisites for protecting an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites)
  * [Oracle patches and known issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues)
  * [Prepare Oracle databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare)
  * [Discover and protect an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-oracle)
  * [Details and settings for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)
  * [Use dNFS with Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-dnfs)
  * [Protect a discovered Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/oracle-db-protect)
  * [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount)
  * [Create an instant virtual copy of an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount-virtualdb)
  * [Restore and recover an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-oracle)
  * [Instant recovery of an Oracle database using Mount and Migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/oracle-mm)
  * [Provision an environment with a Backup and DR workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-workflow-oracle)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
