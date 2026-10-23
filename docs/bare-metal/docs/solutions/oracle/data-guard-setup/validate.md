---
url: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/validate/
title: Validate the Data Guard deployment \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:58.744752+00:00
---

# Validate the Data Guard deployment  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/validate/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Validate the Data Guard deployment

After you've [set up the Data Guard broker](https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/broker), you need to verify that redo was copied from the primary database and applied on the standby database. The following procedure can be used to check the Data Guard status from within the primary and standby databases.

The following examples are used throughout this guide:

Database unique name | Server hostnames | RAC instance names | Role  
---|---|---|---  
DBDG_SITE1 | site1db1, site1db2 | DBDG_SITE11, DBDG_SITE12 | Primary  
DBDG_SITE2 | site2db1, site2db2 | DBDG_SITE21, DBDG_SITE22 | Standby  
  
## Validate the Data Guard deployment

  1. Log in to the first Bare Metal Solution server that hosts the primary database, then set the `ORACLE_SID` environment variable so you can connect to the primary database:
         
         source oraenv <<< "DBDG_SITE11"
         

  2. Start SQL*Plus, then determine the latest sequence number for archived redo logs:
         
         sqlplus / as sysdba
         
         
         SELECT THREAD#, max(SEQUENCE#) "Last Primary Seq Archived"
         FROM V$ARCHIVED_LOG VAL, V$DATABASE VDB WHERE VAL.RESETLOGS_CHANGE# =
         VDB.RESETLOGS_CHANGE# GROUP BY THREAD# ORDER BY 1;
         

The following output has maximum sequence number of 40 for thread 1 and a maximum sequence number of 33 for thread 2:
         
         THREAD# Last Primary Seq Archived
         ---------- -------------------------
                  1                        40
                  2                        33
         

Record the results to compare with the standby database. Sequence numbers on the standby database are expected to match the primary database.

  3. Log in to the first Bare Metal Solution server that hosts the standby database, then set the `ORACLE_SID` environment variable so you can connect to the standby database:
         
         source oraenv <<< "DBDG_SITE21"
         

  4. Start SQL*Plus, then validate that the latest sequence number received and applied for archived redo logs matches the latest sequence number on the primary database:
         
         sqlplus / as sysdba
         
         
         SELECT THREAD#, max(SEQUENCE#) "Last Standby Seq Received"
         FROM V$ARCHIVED_LOG VAL, V$DATABASE VDB WHERE VAL.RESETLOGS_CHANGE# =
         VDB.RESETLOGS_CHANGE# GROUP BY THREAD# ORDER BY 1;
         
         
         SELECT THREAD#, max(SEQUENCE#) "Last Standby Seq Applied"
         FROM V$ARCHIVED_LOG VAL, V$DATABASE VDB WHERE VAL.RESETLOGS_CHANGE# =
         VDB.RESETLOGS_CHANGE# AND VAL.APPLIED IN ('YES','IN-MEMORY') GROUP BY
         THREAD# ORDER BY 1;
         

The following output has sequence numbers that match the prior query run against the standby database:
         
         THREAD# Last Standby Seq Received
         ---------- -------------------------
                  1                        40
                  2                        33
         
         
         THREAD# Last Standby Seq Applied
         ---------- ------------------------
                  1                       40
                  2                       33
         

  5. Check that the status of the managed recovery process is `APPLYING_LOG`:
         
         SELECT PROCESS, STATUS FROM V$MANAGED_STANDBY WHERE PROCESS LIKE '%MRP%';
         

The following example shows a single managed recovery process named `MRP0` with status of `APPLYING_LOG`:
         
         PROCESS   STATUS
         --------- ------------
         MRP0      APPLYING_LOG
         

  6. Check for any transport or apply lag on the standby database:
         
         COLUMN NAME FORMAT a20
         COLUMN VALUE FORMAT a30
         SELECT NAME, VALUE FROM V$DATAGUARD_STATS WHERE NAME LIKE '%lag%';
         

The following output shows no lag on the standby database:
         
         NAME                 VALUE
         -------------------- ------------------------------
         transport lag        +00 00:00:00
         apply lag            +00 00:00:00
         

If there is lag, consult Oracle's Data Guard troubleshooting [documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/haovw/tune-and-troubleshoot-oracle-data-guard.html#GUID-E8C27979-9D37-4899-9306-A5AE2B5CF6C0).




## Database switchover using the Data Guard broker

A switchover is a role reversal in which the primary database becomes a standby database, and vice versa. During the switchover process, database clients are disconnected from the primary database. Depending on how your application connects to the database, a switchover can disrupt application traffic. Oracle offers [options to maintain application continuity](https://docs.oracle.com/en/database/oracle/oracle-database/19/racad/ensuring-application-continuity.html) during role transitions. You can test your disaster recovery readiness by performing a database switchover with the following instructions:

  1. Log in to the Bare Metal Solution server that hosts the primary database.

  2. Launch the Data Guard command line interface, and connect to the standby database:
         
         dgmgrl
         
         
         CONNECT SYS@DBDG_SITE2
         

  3. When prompted for a password, enter your SYS remote login password for the database.

  4. Validate that the database is ready for a switchover.
         
         VALIDATE DATABASE DBDG_SITE2;
         

A successful result will report that the database is ready for switchover.

  5. If successful, perform the switchover command:
         
         SWITCHOVER TO DBDG_SITE2;
         

If the command succeeds, you'll receive a message that `DBDG_SITE2` is the new primary database in the configuration.

  6. Run the following command to confirm that the database roles are swapped:
         
         SHOW CONFIGURATION;
         

  7. Run the following command to return to the original configuration:
         
         SWITCHOVER TO DBDG_SITE1;
         


**Note:** Running the switchover command while connected to the primary database might result in the connection being dropped. This is due to the primary database being restarted during the switchover process.

## Database failover using Data Guard broker

A failover is a role transition in which one of the standby databases moves to the primary role due to a complete site outage. Redo will not be shipped to the standby database until the standby database has been reinstated.

**Warning:** A failover typically involves data loss.

### Perform the failover

  1. Log in to the first Bare Metal Solution server that hosts the standby database.

  2. Connect to the Data Guard command line interface, then failover the primary to the standby database:
         
         dgmgrl
         
         
         CONNECT SYS@DBDG_SITE2
         

  3. When prompted for a password, enter your SYS remote login password for the database.

  4. Initiate the failover:
         
         FAILOVER TO DBDG_SITE2
         

Run `show configuration;` to verify that `DBDG_SITE2` is now the primary database, and `DBDG_SITE1` needs to be reinstated.




### Reinstate the primary database

You can only reinstate the primary database after a failover if [`flashback database`](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/examples-of-using-oracle-data-guard.html#GUID-1163448F-6B18-4A44-AA8D-7CDF0D1360FB) is enabled. To reinstate the failed primary database:

  1. Log in to the first Bare Metal Solution server that hosts the primary database.

  2. Connect to the Data Guard command line interface, log in to the primary databases, then reinstate the failed database:
         
         dgmgrl
         
         
         CONNECT SYS@DBDG_SITE2
         

When prompted for a password, enter your SYS remote login password for the database.

  3. Reinstate the database:
         
         REINSTATE DATABASE DBDG_SITE1;
         EXIT;
         




## Next steps

Next, [set up a Data Guard observer on Compute Engine](https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/observer).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
