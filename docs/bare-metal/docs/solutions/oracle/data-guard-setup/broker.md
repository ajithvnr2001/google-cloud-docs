---
url: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/broker/
title: Configure and enable Data Guard broker \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:59.130846+00:00
---

# Configure and enable Data Guard broker  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/broker/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure and enable Data Guard broker

After you've set up the [primary](https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/db-setup-primary) and [standby](https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/db-setup-standby) databases for Data Guard, you need to set up its [broker](https://docs.oracle.com/en/database/oracle/oracle-database/19/dgbkr/oracle-data-guard-broker-concepts.html). The Data Guard broker manages creation, control, and monitoring of Data Guard configurations.

The following examples are used throughout this guide:

Database unique name | Server hostnames | RAC instance names | Role  
---|---|---|---  
Database unique name | Server hostnames | RAC instance names | Role  
DBDG_SITE1 | site1db1, site1db2 | DBDG_SITE11, DBDG_SITE12 | Primary  
DBDG_SITE2 | site2db1, site2db2 | DBDG_SITE21, DBDG_SITE22 | Standby  
  
## Set up the primary database

Start the Data Guard monitor process on the primary database:

  1. Log in to the first Bare Metal Solution server that hosts the primary database.

  2. In `/etc/oratab` check that an entry to enable environment variables for the primary database exists:
         
         DBDG_SITE11:/apps/oracle/19.0.0/db_home1:N
         

  3. Set the `ORACLE_SID` environment variable so you can connect to the primary database:
         
         source oraenv <<< "DBDG_SITE11"
         

You should receive the response `The Oracle base has been set to /apps/oracle/oracle_base`.

  4. Use Recovery Manager to check that archive logs are not automatically deleted until they have been applied on all standby databases:
         
         rman target /
         
         
         CONFIGURE ARCHIVELOG DELETION POLICY TO APPLIED ON ALL STANDBY;
         EXIT;
         

  5. Start SQL*Plus, then configure a location for the broker configuration files and start the broker. RAC databases require the broker configuration files to reside on shared storage, preferably in an ASM diskgroup:
         
         sqlplus / as sysdba
         
         
         ALTER SYSTEM SET DG_BROKER_CONFIG_FILE1='+DATA/DBDG_SITE1/dr1DBDG_SITE1.dat' SID='*' SCOPE=BOTH;
         ALTER SYSTEM SET DG_BROKER_CONFIG_FILE2='+DATA/DBDG_SITE1/dr2DBDG_SITE1.dat' SID='*' SCOPE=BOTH;
         ALTER SYSTEM SET DG_BROKER_START=true SID='*' SCOPE=BOTH;
         EXIT;
         




## Set up the standby database

Start the Data Guard monitor process on the standby database:

  1. Log in to the first Bare Metal Solution server that hosts the standby database.

  2. Set the `ORACLE_SID` environment variable, so you can connect to the standby database:
         
         source oraenv <<< "DBDG_SITE21"
         

You should receive the response `The Oracle base has been set to /apps/oracle/oracle_base`.

  3. Log in to SQL*Plus, then configure a location for broker configuration files and start the broker.
         
         sqlplus / as sysdba
         
         
         ALTER SYSTEM SET DG_BROKER_CONFIG_FILE1='+DATA/DBDG_SITE2/dr1DBDG_SITE2.dat' SID='*' SCOPE=BOTH;
         ALTER SYSTEM SET DG_BROKER_CONFIG_FILE2='+DATA/DBDG_SITE2/dr2DBDG_SITE2.dat' SID='*' SCOPE=BOTH;
         ALTER SYSTEM SET DG_BROKER_START=true SID='*' SCOPE=BOTH;
         EXIT;
         




## Create the broker configuration

  1. Log in to the first Bare Metal Solution server that hosts the primary database.

  2. Connect to the Data Guard command line interface, then to the primary database:
         
         dgmgrl
         
         
         CONNECT SYS@DBDG_SITE1
         

When prompted for a password, enter your SYS remote login password for the primary database.

  3. Create the broker configuration:
         
         CREATE CONFIGURATION 'DBDG' AS PRIMARY DATABASE IS 'DBDG_SITE1' CONNECT IDENTIFIER IS DBDG_SITE1;
         

  4. Add the standby database:
         
         ADD DATABASE DBDG_SITE2 AS CONNECT IDENTIFIER IS DBDG_SITE2 MAINTAINED AS PHYSICAL;
         

  5. Enable the configuration. Enabling this configuration directs the broker process to begin log shipping from the primary database, and apply the redo on the standby database as it is received:
         
         ENABLE CONFIGURATION;
         

  6. You can check if the configuration is successful with the following commands:
         
         SHOW CONFIGURATION;
         
         SHOW DATABASE  DBDG_SITE1;
         
         SHOW DATABASE DBDG_SITE2;
         
         VALIDATE DATABASE DBDG_SITE1;
         
         VALIDATE DATABASE DBDG_SITE2;
         

The `show configuration` command doesn't report a status of `SUCCESS` until the standby database is synchronized with the primary database. The amount of time required for the initial synchronization can vary, based on the amount of changes performed on the primary database or the latency between the primary and standby sites. Here is an example of a successful configuration:
         
         Configuration - DBDG
         
           Protection Mode: MaxPerformance
           Members:
           DBDG_SITE1 - Primary database
             DBDG_SITE2 - Physical standby database
         
         Fast-Start Failover:  Disabled
         
         Configuration Status:
         SUCCESS   (status updated 0 seconds ago)
         

  7. Enable flashback on the newly configured standby database:
         
         CONNECT SYS@DBDG_SITE2
         

When prompted for a password, enter your SYS remote login password for the standby database.
         
         EDIT DATABASE DBDG_SITE2 SET STATE=APPLY-OFF;
         SQL 'ALTER DATABASE FLASHBACK ON';
         EDIT DATABASE DBDG_SITE2 SET STATE=APPLY-ON;
         

  8. Exit the Data Guard command line interface:
         
         EXIT;
         




## Next steps

Next, [validate the Data Guard deployment](https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/validate).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
