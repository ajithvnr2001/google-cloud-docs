---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-dnfs/
title: Use Oracle Direct NFS with Backup and DR in the appliance management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:07:14.727933+00:00
---

# Use Oracle Direct NFS with Backup and DR in the appliance management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-dnfs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Use Oracle Direct NFS with Backup and DR in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

In order to use Oracle Direct NFS (dNFS) with a backup/recovery appliance, the following requirements must be met:

  * Sufficient network bandwidth between database server and backup/recovery appliance

  * Use all Oracle required or recommended patches. Oracle maintains a list of required or recommended patches in the Oracle Support documentation.




## Configure the appliance management console for protecting and mounting virtual Oracle databases over dNFS

To perform dNFS-based backup, you must set the backup/recovery appliance staging disk format (disk preference) to NFS.

Use these instructions to set the staging disk format (disk preference) to NFS:

  1. Go to **Manage** > **Hosts**.

  2. Right-click the host and select **Edit**.

  3. At staging disk format, select **NFS** and then click **Save**.




## Actions to be performed on the target host for dNFS to work

Perform these actions to ensure that dNFS is configured correctly:

  1. Check for the following message under **DB Alert.log** to confirm that dNFS is enabled:
         
         Oracle instance running with ODM: Oracle Direct NFS ODM Library Version 3.01.
         

If dNFS is not enabled, then enable it:

     * NFS client packages must exist on the database host for protection jobs, and on any Oracle host on which you might mount a captured Oracle database using dNFS. For example, for Linux, the `nfs-util` package should exist on the host. Check with the following:

rpm -qa |grep nfs-util

     * Enable dNFS on the Oracle host:

cd $ORACLE_HOME/rdbms/lib make -f ins_rdbms.mk dnfs_on

     * Restart the databases running on that **`ORACLE_HOME`** , then check for the following message under **DB Alert.log** to confirm that dNFS is enabled:

Oracle instance running with ODM: Oracle Direct NFS ODM Library Version 3.0

  2. During the backup job, run the following query to check dNFS usage:
         
         select * from gv$dnfs_servers;
         

You can see the **NFS read/write** stats for the happening I/O:
         
         select inst_id, PNUM, NFS_READ, NFS_WRITE, NFS_COMMIT, NFS_MOUNT from
         gv$dnfs_stats where NFS_READ>0 or NFS_WRITE>0 order by inst_id, PNUM;
         

We can see the dnfs channel process information.
         
         select c.inst_id, program, pid,pname, local, path from gv$process p,
         gv$dnfs_channels c where p.inst_id = c.inst_id and c.pnum = p.pid;
         




## Troubleshoot dNFS: Database issues

This includes:

  * Alert log

  * Database trace files

  * Database unresponsive

  * dNFS views

  * The Oracle dNFS monitor package




### Alert log

The first stop for any debug operation is to check the alert log for dNFS related messages. A common issue observed on databases with dNFS is with the socket buffer size being limited. Oracle tries to adjust the size, but this can be limited by the O/S. In this case, an error like this one is found in the alert log:
    
    
        Direct NFS: Failed to set socket buffer size.wtmax=[1048576]\
        rtmax=[1048576], errno=-1
    

Other items to look for in the alert log include if the correct network cards are being used to communicate with the filer. This can be determined by looking for a message similar to the following:
    
    
        Direct NFS: channel id [0] path [192.168.56.3] to filer [192.168.56.3] via local [] is UP
    

### Database trace files

If I/O issues are occurring, the following events can be set in the database to capture additional logging information. Set these events, wait for the incident to occur, then review to trace files.
    
    
        ALTER SYSTEM SET MAX_DUMP_FILE_SIZE =UNLIMITED;
        ALTER SYSTEM SET EVENTS '10298 trace name context forever, level 1'; # KSFD I/O tracing
        ALTER SYSTEM SET EVENTS '19392 trace name context forever, level 8'; # kgnfs tracing
        ALTER SYSTEM SET EVENTS '19394 trace name context forever, level 8'; # skgnfs tracing
        ALTER SYSTEM SET EVENTS '19396 trace name context forever, level 6'; # kgodm tracing
        ALTER SYSTEM SET EVENTS '19398 trace name context forever, level 128'; # mount tracing errors
    

### Database not responding

If a database running on dNFS is not responding, then sign in as SYSDBA using sqlplus and perform a 'hanganalyze' or a dump:
    
    
        ```oradebug
        oradebug setmypid
        oradebug unlimited
        oradebug hanganalyze 3
        oradebug dump systemstate 266
        ```
    

If database is a RAC database, then add a -g option to the last two oradebug commands.

### dNFS views

The dNFS client is actually in the database kernel. Therefore, several v$ views exist within the database to monitor and check the health of dNFS from within the database. Oracle provides a package that can be used to quickly monitor dNFS performance. This package is in the Oracle dNFS monitor package.

Once deployed, a DBA can perform the following to get information (parameters: dnfs_monitor(sleep time), dnfs_itermonitor (sleep time,number of times to check), sleep time is in seconds):
    
    
        SQL> set serveroutput on
        SQL> set lines 200
        SQL> exec dnfs_monitor(60);
        Started at  01/18/2017 10:09:46 AM
        Finished at 01/18/2017 10:10:46 AM
        READ IOPS:                 2
        WRITE IOPS:                3
        TOTAL IOPS:                5
        READ Throughput:           0 MB/s
        WRITE Throughput:          0 MB/s
        TOTAL Throughput:          0 MB/s
        SQL> exec dnfs_itermonitor(2,10)
        Started at 01/18/2017 10:20:18 AM
        TIMESTAMP              READ IOPS  WRITE IOPS  TOTAL IOPS  READ(MB/s)  WRITE (MB/s) TOTAL (MB/s)
    
        01/18/2017 10:20:20 AM  15         7          22           0            0           0
    
        01/18/2017 10:20:22 AM   2         3          5            0            0           0
    
        01/18/2017 10:20:24 AM   0         3          3            0            0           0
    
        01/18/2017 10:20:26 AM   2         2          4            0            0           0
    
        01/18/2017 10:20:28 AM   0         3          3            0            0           0
    
        01/18/2017 10:20:30 AM   2         3          5            0            0           0
    
        01/18/2017 10:20:32 AM   4         3          7            0            0           0
    
        01/18/2017 10:20:34 AM   0         3          3            0            0           0
    
        01/18/2017 10:20:36 AM   2         3          5            0            0           0
    
        01/18/2017 10:20:38 AM   2         3          5            0            0           0
    
        Finished at 01/18/2017 10:20:38 AM
    

The V$ views are:

  * V$DNFS_SERVER: Shows information for all NFS server connections (one for each NFS server). View is useful to verify connectivity and TCP socket settings.

  * V$DNFS_CHANNELS: Shows information for all network paths created to the NFS servers. Each dNFS client creates one channel per process per network path. If multiple paths exists (multiple NICs), the dNFS client load balances over all channels. Data reflects activity since last select.

  * V$DNFS_FILES: Shows files that are open using dNFS client.

  * V$DNFS_STAT: Performance metrics for dNFS client.


`V$DNFS_SERVER` Column | Description  
---|---  
`SRVNAME` | NFS Server Name   
`DIRNAME` | Volume exported by NFS server   
`MNTPORT` | Local mount port   
`NFSPORT` | NFS server port   
`WTMAX` | Max write size for NFS server   
`RTMAX` | Max read size for NFS server   
`V$DNFS_CHANNELS` Column | Description  
---|---  
`PNUM` | Oracle process number (link to PID in v$process)   
`SVRNAME` | NFS server name   
`PATH` | Network path to server   
`CH_ID` | dNFS channel ID   
`SVR_ID` | dNFS server ID   
`SENDS` | Send operations over channel **since last select**.   
`RECVS` | Receive operations over channel **since last select**.   
`PINGS` | Ping operations over channel **since last select**.   
`V$DNFS_FILES` Column | Description  
---|---  
`FILENAME` | Name of file.   
`FILESIZE` | Size of file.   
`PNUM` | Process ID (link to PID in v$process)   
`SRV_ID` | NFS server ID   
`V$DNFS_STAT` Column | Description  
---|---  
`PNUM` | Oracle process number (link to PID in `v$process`)   
`NFS_NULL` | `Null operations`  
`NFS_GETATTR` | Get attribute operations   
`NFS_SETATTR` | Set attribute operations   
`NFS_LOOKUP` | Lookup operations   
`NFS_ACCESS` | Access operations   
`NFS_READLINK` | Read link operations   
`NFS_READ` | Read operations   
`NFS_WRITE` | Write operations   
`NFS_CREATE` | Create operations   
`NFS_MKDIR` | Make directory operations   
`NFS_MKNOD` | Make node operations   
`NFS_SYMLINK` | Symbolic link operations   
`NFS_REMOVE` | Remove operations   
`NFS_RMDIR` | Remove directory operations   
`NFS_RENAME` | Rename operations   
`NFS_LINK` | Link operations   
`NFS_READDIR` | Read directory operations   
`NFS_READDIRPLUS` | Read directory plus operations   
`NFS_FSSTAT` | File system status operation   
`NFS_FSINFO` | File system information operations   
`NFS_PATHCONF` | Path configuration operations   
`NFS_COMMIT` | Commit operations   
`NFS_MOUNT` | Mount operations   
  
### The Oracle dNFS monitor package
    
    
        CREATE OR REPLACE PROCEDURE dnfs_monitor
           (sleepSecs IN NUMBER)
        IS
           startTime       DATE;
           startReadIOPS   NUMBER;
           startWriteIOPS  NUMBER;
           startReadBytes  NUMBER;
           startWriteBytes NUMBER;
           endTime         DATE;
           endReadIOPS     NUMBER;
           endWriteIOPS    NUMBER;
           endReadBytes    NUMBER;
           endWriteBytes   NUMBER;
           readThr         NUMBER;
           writeThr        NUMBER;
           readIOPS        NUMBER;
           writeIOPS       NUMBER;
           elapsedTime     NUMBER;
        BEGIN
    
           SELECT sysdate, SUM(stats.nfs_readbytes), SUM(stats.nfs_writebytes),
        SUM(stats.nfs_read), SUM(stats.nfs_write)
           INTO startTime, startReadBytes, startWriteBytes, startReadIOPS, startWriteIOPS
           FROM dual, v$dnfs_stats stats;
    
           DBMS_OUTPUT.PUT_LINE('Started at  ' || TO_CHAR(startTime,'MM/DD/YYYY HH:MI:SS AM'));
    
           DBMS_LOCK.SLEEP(sleepSecs);
    
           SELECT sysdate, SUM(stats.nfs_readbytes), SUM(stats.nfs_writebytes), SUM(stats.nfs_read), SUM(stats.nfs_write)
           INTO endTime, endReadBytes, endWriteBytes, endReadIOPS, endWriteIOPS
           FROM dual, v$dnfs_stats stats;
    
           DBMS_OUTPUT.PUT_LINE('Finished at ' || to_char(endTime,'MM/DD/YYYY HH:MI:SS AM'));
    
           elapsedTime := (endTime - startTime) * 86400;
           readThr := (endReadBytes - startReadBytes)/(1024 * 1024 * elapsedTime);
           writeThr := (endWriteBytes - startWriteBytes)/(1024 * 1024 * elapsedTime);
           readIOPS := (endReadIOPS - startReadIOPS)/elapsedTime;
           writeIOPS := (endWriteIOPS - startWriteIOPS)/elapsedTime;
    
           DBMS_OUTPUT.PUT_LINE('READ IOPS:        ' || LPAD(TO_CHAR(readIOPS, '999999999'), 10, ' '));
           DBMS_OUTPUT.PUT_LINE('WRITE IOPS:       ' || LPAD(TO_CHAR(writeIOPS,
           '999999999'), 10, ' '));
           DBMS_OUTPUT.PUT_LINE('TOTAL IOPS:       ' || LPAD(TO_CHAR(readIOPS + writeIOPS, '999999999'), 10, ' '));
           DBMS_OUTPUT.PUT_LINE('READ Throughput:  ' || LPAD(TO_CHAR(readThr, '999999999'), 10, ' ') || ' MB/s');
           DBMS_OUTPUT.PUT_LINE('WRITE Throughput: ' || LPAD(TO_CHAR(writeThr,
           '999999999'), 10, ' ') || ' MB/s');
           DBMS_OUTPUT.PUT_LINE('TOTAL Throughput: ' || LPAD(TO_CHAR(readThr + writeThr, '999999999'), 10, ' ') || ' MB/s');
           END;
        /
    
        CREATE OR REPLACE PROCEDURE dnfs_itermonitor
           (sleepSecs IN NUMBER,
            iter      IN NUMBER)
        IS
           startTime       DATE;
           startReadIOPS   NUMBER;
           startWriteIOPS  NUMBER;
           startReadBytes  NUMBER;
           startWriteBytes NUMBER;
           endTime         DATE;
           endReadIOPS     NUMBER;
           endWriteIOPS    NUMBER;
           endReadBytes    NUMBER;
           endWriteBytes   NUMBER;
           readThr         NUMBER;
           writeThr        NUMBER;
           readIOPS        NUMBER;
           writeIOPS       NUMBER;
           i               NUMBER;
           elapsedTime     NUMBER;
        BEGIN
    
           DBMS_OUTPUT.PUT_LINE('Started at ' || TO_CHAR(SYSDATE, 'MM/DD/YYYY HH:MI:SS AM'));
    
           DBMS_OUTPUT.PUT_LINE(
               LPAD('TIMESTAMP', 15, ' ')||
               LPAD('READ IOPS', 33, ' ')||
               LPAD('WRITE IOPS', 15, ' ')||
               LPAD('TOTAL IOPS', 15, ' ')||
               LPAD('READ (MB/s)', 15, ' ')||
               LPAD('WRITE (MB/s)', 15, ' ')||
               LPAD('TOTAL (MB/s)', 15, ' '));
    
           FOR i IN 1..iter
           LOOP
           SELECT sysdate, SUM(stats.nfs_readbytes), SUM(stats.nfs_writebytes), SUM(stats.nfs_read), SUM(stats.nfs_write)
           INTO startTime, startReadBytes, startWriteBytes, startReadIOPS, startWriteIOPS
           FROM dual, v$dnfs_stats stats;
    
           DBMS_LOCK.SLEEP(sleepSecs);
    
           SELECT sysdate, SUM(stats.nfs_readbytes), SUM(stats.nfs_writebytes), SUM(stats.nfs_read), SUM(stats.nfs_write)
           INTO endTime, endReadBytes, endWriteBytes, endReadIOPS, endWriteIOPS
           FROM dual, v$dnfs_stats stats;
    
           elapsedTime := (endTime - startTime) * 86400;
           readThr := (endReadBytes-startReadBytes)/(1024 * 1024 * elapsedTime);
           writeThr := (endWriteBytes-startWriteBytes)/(1024 * 1024 * elapsedTime);
           readIOPS := (endReadIOPS - startReadIOPS)/elapsedTime;
           writeIOPS := (endWriteIOPS - startWriteIOPS)/elapsedTime;
    
           DBMS_OUTPUT.PUT_LINE(
               TO_CHAR(endTime, 'MM/DD/YYYY HH:MI:SS AM')||
               LPAD(TO_CHAR(readIOPS, '999999999'), 15, '') ||
               LPAD(TO_CHAR(writeIOPS, '999999999'), 15,' ') ||
               LPAD(TO_CHAR(readIOPS + writeIOPS, '999999999'),15, ' ') ||
               LPAD(TO_CHAR(readThr, '999999999'), 15, '') ||LPAD(TO_CHAR(writeThr, '999999999'), 15, '
        ') ||
        LPAD(TO_CHAR(readThr + writeThr, '999999999'), 15, ' '));
        END LOOP;
        DBMS_OUTPUT.PUT_LINE('Finished at ' || to_char(endTime, 'MM/DD/YYYY HH:MI:SS AM'));
    
        END;
    

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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
