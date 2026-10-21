---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-source-database-one-time/
title: Configure your source Oracle database for a one-time migration \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:46:11.167466+00:00
---

# Configure your source Oracle database for a one-time migration  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-source-database-one-time/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Configure your source Oracle database for a one-time migration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure your Oracle source database for a one-time migration with Database Migration Service. Before you can use Database Migration Service to pull data from your source Oracle database, you must grant the appropriate privileges to the user account that will be used to connect to your database and access schema and code objects.

By default, Database Migration Service attempts to access all your object definitions through [ `DBA_VIEWS`](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_VIEWS.html). Access to `DBA_VIEWS` is granted with the `SELECT ANY DICTIONARY` privilege. If DBA views aren't accessible to the migration user account, Database Migration Service falls back to [ `ALL_VIEWS`](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_VIEWS.html). This approach provides you with the greatest degree of flexibility with respect to defining a security model that best matches your requirements.

For the exact configuration steps, refer to the section for your source database:

  * Configure an Amazon RDS for Oracle database
  * Configure a self-managed Oracle database
  * Configure a self-managed Oracle pluggable database



## Configure an Amazon RDS for Oracle database

To configure your Amazon RDS source databases for a one-time migration, grant the user account that Database Migration Service will use the appropriate privileges

For each command, replace `USER_NAME` with the name of the user account you use for the migration. Running these commands grants privileges to read from `V$DATABASE` which is required for validation.
    
    
    GRANT CONNECT TO USER_NAME;
    GRANT CREATE SESSION TO USER_NAME;
    GRANT SELECT ANY TABLE TO USER_NAME;
    GRANT SELECT ANY DICTIONARY TO USER_NAME;
    exec rdsadmin.rdsadmin_util.grant_sys_object('V_$DATABASE','USER_NAME','SELECT');

## Configure an Oracle database

To configure your Oracle source databases for a one-time migration, grant the user account that Database Migration Service will use the appropriate privileges

For each command, replace `USER_NAME` with the name of the user account you use for the migration. Running these commands grants privileges to read from `V$DATABASE` which is required for validation.
    
    
    GRANT CONNECT TO USER_NAME;
    GRANT CREATE SESSION TO USER_NAME;
    GRANT SELECT ANY TABLE TO USER_NAME;
    GRANT SELECT ANY DICTIONARY TO USER_NAME;
    GRANT SELECT ON SYS.V_$DATABASE TO USER_NAME;

## Configure an Oracle pluggable database (PDB)

Database Migration Service supports Oracle multi-tenant architecture, where a single [ container database (CDB)](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/introduction-to-oracle-database.html#GUID-AB84D6C9-4BBE-4D36-992F-2BB85739329F) contains one or more pluggable databases (PDBs). Each pluggable database is a self-contained database with a unique ID and name, and can be managed independently.

To connect to a container in a multi-tenant architecture setup, or to switch between container sessions, use the following command:

`ALTER SESSION SET CONTAINER = CONTAINER_NAME;`

Replace CONTAINER_NAME with the name of your container, for example your pluggable database or the `CDB$ROOT` container.

To configure an Oracle pluggable database so that you can use it with Database Migration Service, perform the following steps:

  1. Create a [ common user](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/tables-and-table-clusters.html#GUID-19337B94-645B-45E8-842C-762BBC544B13). 

A common user has the same identity in the `CDB$ROOT` container and in the pluggable databases. A common user can connect to and perform operations within the root, and within any pluggable database in which it has privileges. The common username must start with `C##` or `c##`. 

  2. Grant the appropriate privileges to the common user that will be used to connect to your database. Different permissions are required at the `CDB$ROOT` container and pluggable database levels. 

For each command, replace `USER_NAME` with the name of the user account you use for the migration. Running these commands grants privileges to read from `V$DATABASE` which is required for validation.

     * Connect to the `CDB$ROOT` container and run the following commands: 
           
           GRANT CREATE SESSION TO USER_NAME;
           GRANT SET CONTAINER TO USER_NAME;
           GRANT SELECT ON SYS.V_$DATABASE TO USER_NAME;
           GRANT EXECUTE_CATALOG_ROLE TO USER_NAME;

     * Connect to the pluggable database and run the following commands: 
           
           GRANT CREATE SESSION TO USER_NAME;
           GRANT SET CONTAINER TO USER_NAME;
           GRANT SELECT ANY TABLE TO USER_NAME;
           GRANT SELECT ANY DICTIONARY TO USER_NAME;
           GRANT SELECT ON SYS.V_$DATABASE TO USER_NAME;




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
