---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-otherdb/
title: Prepare other self-managed databases for Backup and DR on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:36.791104+00:00
---

# Prepare other self-managed databases for Backup and DR on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-otherdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Prepare other self-managed databases for Backup and DR on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Before you can back up the following self-managed database instances and data, you must add the database server as a host to Backup and DR. For this to work, most databases require some settings and other preparation steps. The procedures on this page are for most self-managed databases:

For | Review | Then use  
---|---|---  
IBM Db2 | [Backup and DR for IBM Db2](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-db2) | [Db2 database prerequisites](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-otherdb#db2-prerequisites)  
PostgreSQL | [Backup and DR for PostgreSQL](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-postgresql) | [PostgreSQL database prerequisites](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-otherdb#postgresql-prerequisites)  
SAP ASE | [Backup and DR for SAP ASE](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-ase) | [SAP ASE database prerequisites](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-otherdb#ase-prerequisites)  
SAP IQ | [Backup and DR for SAP IQ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq) | [SAP IQ database prerequisites](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-otherdb#iq-prerequisites)  
SAP MaxDB | [Backup and DR for SAP MaxDB](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-maxdb) | [SAP MaxDB database prerequisites](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-otherdb#maxdb-prerequisites)  
SAP HANA | [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana) | [Prepare SAP HANA databases for backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana)  
Microsoft SQL Server | [Backup and DR for SQL Server](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sql-server) | [Prepare SQL server databases for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sql-server)  
Oracle | [Backup and DR for Oracle](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-oracle) | [Prerequisites for backing up an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-oracle) and its following pages  
  
For all other Backup and DR supported databases, follow these procedures.

## Db2 database prerequisites

  * Each database must be using **Automatic storage mode** , or else only instances are discovered.

  * Each database must be in archive log mode, and LOGARCHMETH1 must be set to local disk. To learn if the database is in circular mode or archive log mode, run the command `db2 get db cfg for <database name>| grep LOGARCHMETH1`

  * If the database is in circular mode, then change the logging to archive mode before continuing. To set the `LOGARCHMETH1` parameter, use the following:  
`db2 update db cfg for <dbname> LOGARCHMETH1 using 'DISK:<location>'`

  * For HADR-standby database the **reads on standby** option must be enabled, that is the `DB2_HADR_ROS` parameter must be set to **ON**.

**Note:** Third-party log backup location is not supported. Log backup location (`LOGARCHMETH1`) must be set to **local disk** for backup and recovery to succeed.**Note:** If you are using Pacemaker HADR, then see [Configure Pacemaker-aware snapshots for IBM Db2 HADR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/configure-db2-pacemaker).



## PostgreSQL database prerequisites

This section includes information about the PostgreSQL database prerequisites.

### Protect PostgreSQL from the primary node

  1. Create a backup user:

`create user actuser;`

  2. Provide privilege for backup:
         
         alter user actuser with superuser;
         alter user actuser with Replication;
         

  3. PostgreSQL archive mode—archive_mode—must be set to ON to take log backups. To configure the archive log mode option, update the postgresql.conf file in the data directory of the instance and reload the PostgreSQL.
         
         archive_mode = on
          // Command to reload PostgreSQL
          pg_ctl reload -D <Postgres_datadir_path>
         




**Example** : `pg_ctl reload -D /pgdata`

### Protect PostgreSQL from a standby node

  1. Create a backup user:

`create user actuser;`

  2. Provide privilege for backup:
         
         alter user actuser with superuser;
         alter user actuser with Replication;
         

  3. PostgreSQL archive mode—WAL—setup on standby node:

Create the directory where we want to keep the WALs.  
_Example assumes`/pglog` is the directory. Run the following steps as root user._
         
         mkdir /pglog
         chown -R postgres:postgres /pglog
         

Configure the parameters for archiving.   
_Example assumes`$PGDATA` is `/pgdata/11/data`. Run these steps as postgres user._  
Add or update the parameters in the file `/pgdata/11/data/postgresql.conf`
         
         wal_level = replica
          archive_mode = always
          archive_command = 'test ! -f /pglog/%f && cp %p /pglog/%f'
         

Restart the PostgreSQL:
         
         /usr/pgsql-11/bin/pg_ctl stop -D /pgdata/11/data
          /usr/pgsql-11/bin/pg_ctl start -D /pgdata/11/data
         

Add or update entry in `pg_hba.conf` on Primary to accept database connection from standby.  

         
         host postgres <db-user> <standby-ip/32> <connection method>
         

Example: `host postgres postgres 10.128.0.29/32 trust`

Test the archive generation (as postgres user):
         
         ls -l /pglog/
         

Run this log switch command:
         
         /usr/pgsql-11/bin/psql -h 10.128.0.28 -p5432 -c "select pg_switch_wal();"
          sleep 5 # log shipping may take some time depending on network
          ls -l /pglog/
         




## SAP ASE database prerequisites

Before you begin, on the SAP ASE server complete the following:

  * A backup user account must be created with backup privilege—either `oper_role` or `sa_role`. A backup username and password must be configured with host configuration. Create the user with or without a password to run the quiesce command on the source with sa_role/or with quiesce privileges. To create the user with a password, run the following:
        
        isql -Usa -P<password> -S<SAP ASE_Server_Name>
        1>sp_addlogin actuser, '<password>'
        2go
        1grant role sa_role to actuser
        2>go
        

To configure the user login without a password requirement, set the password to null, then run the following command:
        
        1>sp_configure "minimum password length", 0
        2>go
        1> sp_modifylogin actuser, "min passwd length",
        "0"
        2> go
        3> exit
        isql -Uactuser -P'<password>' -S<server_name>
        > sp_password '<password>', NULL
        >go
        >sp_configure "minimum password length", 8
        >go
        

**Note:** If there are multiple SAP ASE instances running on a server, then the backup username and password must be common for all SAP ASE instance running on that server.
  * [Install the Backup and DR agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent) on the SAP ASE server.

  * To enable transaction log backup, `Truncate on chkpt false` must be set at the database level for each database of the SAP ASE instance.

  * The following is true for volume level backups:

    * The SAP ASE instance must reside under LVM and it must not be the boot volume.

    * The LVM volume from which the SAP ASE volumes are provisioned should have at least 20% free space.


**Note:** SAP ASE discovery and backup jobs may stop responding due to a known issue with sp_spaceused. The reasons and the resolution for long running sp_spaceused procedures are explained in the SAP note: "2443782 - execute sp_spaceused takes too long - SAP ASE". 

## SAP IQ database prerequisites

Before you begin, review the following on the SAP IQ server:

  * SAP IQ PITR logging must be ON to take log backup. To configure PITR log option, you need these SAP IQ API:

    * `ALTER DBSPACE IQ_SYSTEM_LOG RENAME /<pitr_log_location>`

    * SET OPTION `PUBLIC.IQ_POINT_IN_TIME_RECOVERY_LOGGING` = ON`

After enabling PITR logging, a database full backup is needed.

  * The utility database needs to start by specifying the username and password, and dbname should be `utility_db`. For example: `start_iq -n utility_db -su act,passwd`

  * The database backup username and password should be the same as the `utility_db` username and password and it must have DBA privileges. To create the backup user, for example:
        
        create user actuser identified by 'mypassword';
        grant dba to actuser;
        

**Note:** If there are multiple SAP IQ instances running on a server, then the backup username and password must be common for all SAP IQ instances running on that server.
    * [Install the Backup and DR agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent) on the SAP IQ server host.



## SAP MaxDB database prerequisites

Before you begin, on the SAP MaxDB server:

  * If there are multiple MaxDB instances running on a server, then the DB username and password must be common for all MaxDB instance running on that server.

  * Autolog backup must be enabled. Use the following command to enable auto log backup:
        
        dbmcli -d <DBSID> -u <DBM_USERNAME>,<DBM_PASSWD> autolog_on
        <autolog_backup_template_name>
        

  * For enabling the autolog backup, you need an autolog backup template.




To create a backup template, use the following command.
    
    
        dbmcli -d <DBSID> -u <DBM_USERNAME>,<DBM_PASSWD> backup_template_create
        <BACKUP_TEMPLATE_NAME> to file  <FULL_PATH_WITH_FILE_NAME> content log
    

  * Log Overwrite area must be deactivated to enable autolog backup enable.



To deactivate log overwrite, use the following command:
    
    
        dbmcli -d <DBSID> -u <DBM_USERNAME>,<DBM_PASSWD> db_execute SET LOG AUTO
        OVERWRITE OFF.
    

  * [Install the Backup and DR agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent) on the SAP MaxDB server host.



## What's next

After the database is prepared for Backup and DR, you can [add the host and discover the databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-add-host).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
