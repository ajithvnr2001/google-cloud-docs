---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-oracle/
title: Restore and recover Oracle databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:17.876112+00:00
---

# Restore and recover Oracle databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore and recover Oracle databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Restoring to the original database replaces the original production application data with the specified point-in-time backup. This restoration results in the loss of all current application data as the application is restored to its status at the point-in-time when the backup was created. This operation cannot be undone. The amount of time required to complete a restore operation depends on the amount of data involved. You can also restore a database to another target.

## Limitations

  * You cannot perform mount operations on Oracle database backups stored in OnVault pools that point to backup vaults.

  * You cannot restore an Oracle database to a cloned virtual machine.

  * When you restore an Oracle database, Backup and DR disables its backup plan options (**Run Schedule** , **Expire Data**).




## Restore an Oracle database by using RMAN

Use the following instructions to restore an Oracle database from the appliance management console:

When the database is restored, it overwrites the original production database.

  1. Open the appliance management console to the **App Manager** and enter the database application name or use the filters to find the database backup that you need.

  2. Right-click the application, and then select **Access**.

  3. On the **Access** page, select a backup and click **Restore** under the **Mount** menu.

  4. On the **Restore** page, select **Traditional**.

  5. Use the **Restore Range** slider to select a specific point in time to restore the database. Slide the slider tool all the way to the left to restore only the database with no logs applied.

  6. In the **Username** field, enter the Oracle software owner on the selected target server.

  7. In the **Number of Channels** field, specify the number of RMAN channels to configure parallelism for database restore.

  8. Click **Submit**.

A warning dialog appears.

  9. Enter `DATA LOSS` to confirm that you want to overwrite the original production database and accept any potential data loss.

The job is queued for the next available job slot. You can view the progress of the queue in the **Jobs Monitor**.




## Restore a database to any target using the appliance management console

Restore an Oracle database to a new target by using RMAN from the appliance management console.

  1. From the **App Manager** , click **Applications**.

  2. Right-click the database and select **Access**.

  3. Select the backup to recover and choose **Restore**.

  4. On the **Restore** page, select **Traditional**.

     * **Target** : For all configurations, all eligible Oracle database servers are available to choose from the drop-down. Select the target server for the restore from the drop-down.
     * **Replace Original Application identity** : This option is only available when restoring to a new server on the same appliance where the backup was originally generated.
     * **Yes** : This replaces the original application and has the same application ID, job history, backups, and backup plan as the original application.
     * **No** : This does not replace the original application. The new database will be discovered as a new application as part of the Restore job.
     * **Rollforward time** : Choose a date and time for a database protected with logs to recover to the required point in time.
     * **Application Options** :

       * **DATABASESID** : This is pre-populated with the protected database SID name and is immutable.
       * **USERNAME** : This is pre-populated with source database Oracle software owner. Update the **USERNAME** if the Oracle software owner on the selected target server is different.
       * **ORAHOME** : This is pre-populated with source database Oracle Home path. Update the Oracle Home directory if the Oracle home is different on the selected target server.
       * **Advanced Options** : This is pre-populated and displays all the database parameter settings (from pfile) at the source at backup time. Make sure the parameter value is correct for the target database server (source or new target) for restore.
**Note:** Make sure to verify that path-specific parameters (audit file dest, db create file dest) are available on the target server.
  5. **Mapping Options** :

     * **Target Database Type** : Select the database target type (ASM diskgroup or file system) for the database from the drop-down list. File system target type is not supported for backups in ASM format.

Source Database | Backup format | Restore Target  
---|---|---  
ASM | ASM | ASM  
ASM | File system | ASM  
File system | File system | File system  
     * Select target ASM diskgroup and file system mappings for three file types: the data files, the control files and the redo files for the database from the drop-down list.

  6. Click **Pre-Flight Check**. If the pre-flight check fails, fix the issue and run the pre-flight check again.

  7. Click **Submit** to submit the restore job.




## Recover an Oracle database manually using RMAN

To manually recover an Oracle database, refer to these procedures. 

### Non-RAC, Non-ASM, File System

**Recover an Oracle database with data file on file system and protected under file-based staging disk format**

  1. Mount the backup from the protected source database.

In the **Mount** window, **Mapping Options** , provide a mount location for the backup, for example: `/acttestdb`. For instructions on how to mount a database backup, see [Mount an Oracle database backup protected Under a file system for data access](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount#file-system).

The database backup is mounted at: `/acttestdb`

The protected archive log is mounted at: `/acttestdb_Log`

  2. Set the Oracle environment and use sqlplus to shut down the database:
         
         sqlplus / as sysdba
         sql> shutdown immediate;
         

Verify the database is shut down. End any remaining processes for the database.
         
         ps -ef | grep database sid
         

  3. Start the database in nomount state using the backup parameter file from the mounted volume. The backup parameter file is under top mounted folder, for example `/acttestdb`

  4. Set the Oracle environment and use sqlplus to start the database:
         
         sqlplus / as sysdba
         sql> startup nomount pfile='/acttestdb/database sid___backup.ora';
         

  5. Create a new spfile from the existing pfile and restart the database.

Create an spfile from the pfile:
         
         create spfile='$ORACLE_HOME/dbs/spfile_database sid.ora' from pfile='/acttestdb/database sid___backup.ora';
         

Restart the database with spfile in nomount state:
         
         shutdown immediate;
         startup nomount;
         

  6. Restore the control file using RMAN from the Backup and DR mounted archive log backup. Use the latest control file from the log mounted backup, for example:
         
         /acttestdb_Log/cf D_sid-id_Target SID.ctl
         

or if there is more than one log backup:

/acttestdb_Log_1/cf-D_sid-id_Target SID.ctl
         
         rman target /
            restore controlfile from '/acttestdb_Log_1/cf-D_<var>sid</var>-id_<var>id</var>.ctl' ;
         

  7. Mount the database:
         
         alter database mount;
         

  8. Catalog the datafile and archivelog folder from Backup and DR mounted database backup and archive log backup to RMAN:
         
         run {
              catalog start with '+acttestdg/db_name/datafile' noprompt;
              catalog start with '+acttestdg/db_namearchivelog' noprompt;
              catalog start with 'mountpoint_log' noprompt;
              }
         

  9. Restore and recover the database:
         
         run { restore database ; recover database; }
         

For a specific point in time recovery using the format yyyymmddhh24mi:
         
         run
             {
             restore database;
             recover database until time "to_date('timestamp','yyyymmddhh24mi')";
             }
         

  10. Open the database with the reset log option.

     * For primary database recovery:
           
           alter database open resetlogs;
           

     * For Data Guard standby database recovery, start the Data Guard managed recovery process:
           
           alter database recover managed standby database nodelay disconnect;
           

The database is available for read and write.




### RAC or Standalone ASM, File System

**Recover an Oracle database with data file on ASM disk group and protected under file-based staging disk format**

**Note:** You cannot perform mount operations on database backups stored in OnVault pools that point to backup vaults.

  1. Mount the backup from the protected source database.

In the Mount window under Mapping Options, provide a mount location for the backup, for example: `/acttestdb`. For instructions on how to mount a database backup, see [Mounting an Oracle Database backup Protected Under a File System for Data Access](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount#file-system).

The database backup is mounted at the mount location: `/acttestdb`

The protected archive log is mounted at:`/acttestdb_Log`

  2. Shut down the Oracle database. From node 1, su to Oracle OS user:

`su - oracle`

Set the Oracle environment and use srvctl to stop the database across all nodes:

`srvctl stop database -d <var>database_name</var>`

Verify the database is shutdown (all nodes). End any remaining processes for the database.

`ps -ef | grep <var>database_name</var>`

  3. Start the database in no-mount state using the backup parameter file from the mounted volume. The backup parameter file is under the top mounted folder, for example at `/acttestdb`

  4. Set the Oracle environment and use sqlplus to start the database:
         
         sqlplus / as sysdba
         startup nomount pfile='/acttestdb/<var>database_name</var>___backup.ora';
         

  5. Create a new spfile and restart the database.

To get the path of original spfile under disk group:

cat $ORACLE_HOME/dbs/init{database sid}.ora

For example: spfile=+{preferred disk group}/db_name/spfiledb_name.ora`
         
         create spfile='+{preferred disk group}/{db name}/spfile<var>db_name</var>.ora' from pfile='/acttestdb/<var>db_name</var>___backup.ora';
         

Restart the database with spfile in nomount state:
         
         shutdown immediate;
           startup nomount;
         

  6. Restore the control file using RMAN from the Backup and DR mounted archive log backup. Use the latest control file from the log mounted backup, for example:
         
         /acttestdb_Log/cf-D_<var>db_name</var>-id_<var>db_id</var>.ctl
         

or if you have more than one log backup:
         
         /acttestdb_Log_1/cf-D_<var>db_name</var>-id_<var>db_id</var>.ctl
         
         
         target /
            restore controlfile from '/acttestdb_Log_1/cf-D_<var>db_name</var>-id_<var>db_id</var>.ctl' ;
            ```
         

  7. Mount the database:
         
         alter database mount;
         

  8. Catalog the datafile and archivelog folder from Backup and DR mounted database backup and archive log backup to RMAN:
         
         run { catalog start with '/acttestdb/datafile' noprompt;
          catalog start with '/acttestdb/archivelog' noprompt;
          catalog start with '/acttestdb_Log' noprompt;}
         

  9. Restore and recover the database:
         
         run { restore database ; recover database; }
         

For a specific point in time recovery using the format yyyymmddhh24mi:
         
         run
          {
          restore database;
          recover database until time "to_date('<var>timestamp</var>','yyyymmddhh24mi')";
          }
         

  10. Open the database with the reset log option.

     * For primary database recovery:
    
    alter database open resetlogs;
    

RAC config requires another step after reset log: Shut down the database on node 1 and start the database across all nodes.

Use sqlplus to shut down the database:
    
    sqlplus / as sysdba
      shutdown immediate;
      ```
    Use srvctl to start the database across all nodes:
    
     ```srvctl
      srvctl start database -d <var>database_name</var>
      ```
    + For Data Guard standby database recovery:
    
      + For non-RAC config: Start the Data Guard managed recovery process
    
          ```rman
          alter database recover managed standby database nodelay disconnect;
          ```
    
      + For RAC config: Shut down the database on node 1 and start the
        database in mounted state across all nodes.
    
         1. Use sqlplus to shut down the database:
    
              ```sqlplus
              / as sysdba
              shutdown immediate;
              ```
    
         1. Use srvctl to start the database in a mount state across all
            nodes:
    
             ```srvctl
             srvctl start database -d <var>database_name</var> -o mount
             ```
    
         1. Start the Data Guard managed recovery process:
    
             ```rman
             alter database recover managed standby database nodelay disconnect;
             ```
    




The database is available for read and write.

### RAC or Standalone ASM, ASM Disk Group

**Recover an Oracle database with data file on ASM disk group and protected under ASM disk group staging disk format**

  1. Mount the backup from the protected source database. In the Mount window, provide a preferred disk group for the backup mount under ASM on RAC Node 1. For details on how to mount a database backup, see [Mounting an Oracle Database backup Protected Under an ASM Disk Group for Data Access](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount#asm-diskgroup).

**Note:** You cannot perform mount operations on database backups stored in OnVault pools that point to backup vaults.

For example, on the mount screen:

     * **Select Host** : RAC node 1 database server

     * **Preferred disk group** : acttestdg

     * **RAC node list** : IP of RAC node 1

The backup parameter file is copied under `/act/touch/<var>preferred_disk_group</var>/`, for example:

`/act/touch/acttestdg/<var>database_name</var>___backup.ora`

  2. Shut down the Oracle database.

From node 1, su to Oracle OS user:
         
         su - oracle
         

Set the Oracle environment. Use srvctl to stop database across all nodes:
         
         srvctl stop database -d <var>database_name</var>
         

Verify the database is shut down (on all nodes). End any remaining processes for the database.
         
         ps -ef | grep <var>db_name</var>
         

  3. Start the database in nomount state using the backup parameter file copied under /act/touch/acttestdg.

  4. Set the Oracle environment. Use sqlplus to start the database:
         
         ```sqlplus
         / as sysdba
         startup nomount pfile='/act/touch/acttestdg/<var>db_name</var>___backup.ora';
         ```
         

  5. Create a new spfile and restart the database.

To get the path of original spfile under disk group:
         
         ```sqlplus
          cat $ORACLE_HOME/dbs/init(database sid).ora
          ```
         

For example: spfile=+preferred disk group/db_name/spfiledb_name.ora
         
         create spfile='+<var>preferred disk group</var>/<var>db_name</var>/spfile<var>db_name</var>.ora' from pfile='/act/touch/acttestdg/<var>db_name</var>___backup.ora';
         

Restart the database with spfile in nomount state:
         
         ```sql
          shutdown immediate;
          startup nomount;
          ```
         

  6. Restore control file using RMAN from the Backup and DR mounted archive log backup. Use the latest control file from Log mounted backup, for example:  
`/acttestdb_Log/cf-D_<var>db_name</var>-id_<var>db_id</var>.ctl` or if more than one log backup exists:  
`/acttestdb_Log_1/cf-D_<var>db_name</var>-id_<var>db_id</var>.ctl`
         
         ```rman
          rman target /
          restore controlfile from '/acttestdg_Log_1/cf-D_<var>db_name</var>-id_<var>db_id</var>.ctl' ;
          ```
         

  7. Mount the database:
         
         ```rman
          alter database mount;
          ```
         

  8. Catalog the datafile and archivelog folder from Backup and DR mounted database backup and archive log backup to RMAN:
         
         ```rman
          run { catalog start with '+acttestdg/<var>db_name</var>/datafile' noprompt;
          catalog start with '+acttestdg/<var>db_name</var>/archivelog' noprompt;
          catalog start with '/acttestdg_Log' noprompt;}
          ```
         

  9. Restore and recover the database:
         
         ```rman
          run { restore database ; recover database ; }
          ```
         

For a specific point in time recovery run the recover command as under:
         
         ```rman
          run
          {
          restore database;
          recover database until time "to_date('<var>timestamp</var>','yyyymmddhh24mi')";
          }
          ```
         

  10. Open the database with the reset log option.

     * For primary database recovery:
           
           alter database open resetlogs;
           

RAC config requires another step: After reset log, shut down the database on node 1 and start the database across all nodes. Use sqlplus to shut down the database:
           
           / as sysdba
            shutdown immediate;
           

Use srvctl to start database across all nodes:
           
           start database -d <var>database_name</var>
           

     * For Data Guard standby database recovery:

       * For non-RAC config: Start the Data Guard managed recovery process:
             
             alter database recover managed standby database nodelay disconnect;
             

       * For RAC config: Shut down the database on node 1 and start the database in mounted state across all nodes.

         1. Use sqlplus to shut down the database:
                
                as sysdba
                shutdown immediate;
                

         2. Use srvctl to start the database in a mount state across all nodes:
                
                start database -d <var>database_name</var> -o mount
                

         3. Start the Data Guard managed recovery process:
                
                alter database recover managed standby database nodelay disconnect;
                

The database is available for read and write.




## Recover Oracle tablespace and data files

To recover a single tablespace data file, for example, due to data corruption:

  1. Mount the latest database snapshot from the backup/recovery appliance back to the Oracle server.

**Note:** You cannot perform mount operations on database backups stored in OnVault pools that point to backup vaults.
  2. Catalog the database backup snapshot to RMAN.

  3. Restore and recover the tablespace using the backup snapshot as detailed here.




### Recover a single tablespace of a production database on an ASM Disk Group

To recover a single tablespace of a production database to the primary node:

  1. Mount the database point-in-time snapshot as detailed in [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount).

  2. In the Mount window under Mapping Options, provide a mount location for the backup. For example, for a backup under ASM disk group provide a disk group name under Preferred Disk Group and for backup under file system provide a mount location such as `/acttestdb`.

**Note:** You cannot perform mount operations on database backups stored in OnVault pools that point to backup vaults.
     * For instructions on how to mount a database backup protected under file system, see [Mount an Oracle database backup protected under a file system for data access](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount#file-system).

     * For details on how to mount a database backup protected under ASM Disk Group, see [Mount an Oracle database backup protected under an ASM disk group for data access](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount#asm-diskgroup).

  3. From the primary node, log into the database server as Oracle OS user.

  4. Set the database environment and log into RMAN:
         
         rman target /
         

  5. At the RMAN prompt, catalog the backup data file and archive log folder:

Example: A database backup protected under ASM Disk Group: (Mounted ASM Disk Group name " + acttestdg"):
         
         ```rman
         catalog start with '+acttestdg/<var>db_name</var>/datafile' noprompt;
         catalog start with '+acttestdg/<var>db_name</var>/archivelog' noprompt;
         catalog start with &#8216;/<var>mountpoint_log</var>'; noprompt;
         (If archivelogs are protected by Backup and DR)
         ```
         

Example: A database backup protected under file system (mounted file system name "/acttestdb"):
         
         ```rman
         catalog start with '/acttestdb/datafile' noprompt;
         catalog start with '/acttestdb/archivelog'
         noprompt;
         catalog start with '/acttestdb_log/archivelog' noprompt;
         ```
         
         (If archivelogs are protected by Backup and DR)
         

Now you can run all RMAN recovery commands, such as:

     * Recover a tablespace
     * Recover a datafile
     * Recover a corrupt database block
     * Recover lost control files
     * Recover an Oracle pluggable database
  6. When finished, [unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) the backup.




### Recover a tablespace

To recover a tablespace:
    
    
        ```rman
        restore tablespace <var>tablespace name</var>;
        recover tablespace <var>tablespace name</var>;
        ```
    

### Recover a datafile

To recover a datafile:
    
    
        ```rman
        restore datafile <var>file#</var>;
        recover datafile <var>file#</var>;
        ```
    

### Recover a corrupt database block

To recover a corrupt database block:

  1. Mount the database point-in-time snapshot as detailed in [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount#file-system).

  2. In the **Mount** window, **Mapping Options** , provide a mount location for the backup. For example, for a backup in an ASM disk group provide a disk group name under Preferred Disk Group and for backup in a file system provide a mount location ex: /acttestdb.

     * For instructions on how to mount a database backup protected under file system, see [Mount an Oracle database backup protected under file system for data access](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount#asm-diskgroup).

     * For details on how to mount a database backup protected under an ASM Disk Group, see [Mount an Oracle database backup protected under an ASM disk group for data access](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount).

  3. From the primary node, log into the database server as Oracle OS user.

  4. Set the database environment and log into sqlplus, then query v$database_block_corruption to check the corrupt blocks:
         
         ```sh
         sqlplus / as sysdba
         sql> SELECT * FROM V$DATABASE_BLOCK_CORRUPTION;
         ```
         

  5. Login to RMAN to recover all corrupted blocks:
         
         ```rman
         rman target /
         RECOVER CORRUPTION LIST;
         ```
         

After the blocks are recovered, the database removes them from V$DATABASE_BLOCK_CORRUPTION.

  6. To recover an individual corrupt block (for example: datafile 8 and block 13):

From RMAN prompt
         
         ```rman
         recover datafile 8 block 13;
         ```
         




### Recover lost control files

To recover lost control files:

  1. Mount the database point-in-time snapshot as detailed in [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount#file-system).

  2. In the **Mount** window, **Mapping Options** , provide a mount location for the backup. For example, for a backup under ASM disk group provide a disk group name under Preferred Disk Group and for a backup under file system provide a mount location such as `/acttestdb`.

     * For instructions on how to mount a database backup protected under file system, see [Mount an Oracle database backup protected under a file system for data access](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount#asm-diskgroup).

     * For details on how to mount a database backup protected under ASM Disk Group: see [Mounting an Oracle Database backup Protected Under an ASM Disk Group for Data Access](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount).

  3. From the primary node, log into the database server as Oracle OS user.

  4. Set the database environment and log into sqlplus, then shut down the database and start in nomount state:

For standalone database:
         
         ```sql
         sqlplus / as sysdba
         sql> shutdown immediate;
         sql> startup nomount;
         ```
         

For RAC database from the mounted backup node shutdown the database across all nodes:
         
         ```sh
         srvctl stop database -d <var>db_name</var>
         sql> startup nomount;
         ```
         

  5. Restore the control file from Backup and DR mounted backup.

For example: `/acttestdb` (file system) and `+acttestdg` (for ASM)
         
         ```rman
         rman target /
         restore controlfile
         from '/acttestdb/cf-D_<var>db_name</var>-id_<var>db_id</var>.ctl' ; (Filesystem
         mount)
         restore controlfile
         from '+acttestdb/cf-D_<var>db_name</var>-id_<var>db_id</var>.ctl' ; (ASM
         mount)
         ```
         

  6. Mount and open the database from sqlplus:
         
         ```sql
         sqlplus / as sysdba
         sql> alter database mount;
         sql> recover database until cancel;
         sql> alter database open resetlogs;
         ```
         




### Recover an Oracle pluggable database

To recover an Oracle 12c or later pluggable database (PDB):

  1. Mount the backup from the source database server to recover. In the **Mount** window, provide a preferred disk group for the backup mount under ASM on RAC Node 1. For details on how to mount a database backup, see [Mount an Oracle database backup protected under ASM Disk Group for data access](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount).

**Note:** You cannot perform mount operations on database backups stored in OnVault pools that point to backup vaults.
  2. Close the pluggable database:

     1. From Node 1, `su` to Oracle User
            
            su - oracle
            

     2. Set the Oracle environment. Connect to the Oracle database as "sysdba" user:
            
            / as sysdba
               alter pluggable database <var>pluggable_db_name</var> close;
            

  3. Catalog the datafile and archivelog folder from Backup and DR mounted database backup and archive log backup to RMAN:
         
         run { catalog start with '+acttestdg/<var>db_name</var>/datafile' noprompt;
             catalog start with '+acttestdg/<var>db_name</var>/archivelog' noprompt;
             catalog start with '/acttestdg_Log' noprompt;
             }
         

  4. Restore and recover the pluggable database
         
         run
             {
             restore pluggable database <var>pluggable_db_name</var>;
             recover pluggable database <var>pluggable_db_name</var> until time "to_date('<var>required time stamp</var>>';,';yyyymmddhh24mi')";
             }
         

**Note:** These steps are applicable only for Oracle 12.1.0.2 version and later. If Oracle version is 12.1.0.1 or earlier 12.1.0.2, then recovery of all datafiles belonging to the pluggable database must be performed before you open the pluggable database in the next step. For example: `rman> recover datafile <PDB datafile number>;`
  5. Open the pluggable database:
         
         alter pluggable database <var>pluggable_db_name</var> open;
         




The pluggable database is open for read and write.

## The Oracle DBA guide

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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
