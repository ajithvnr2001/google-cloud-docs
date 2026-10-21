---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/verify-migration/
title: Verify a migration \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:33.718591+00:00
---

# Verify a migration  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/verify-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Verify a migration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to confirm that your migrated data is complete and accurate. At a minimum, you should run SQL statements to verify that your tables exist in the migrated Cloud SQL database. For a more precise data comparison between the source and destination database, you can  try using the open-source Data Validation Tool.

## Verify destination data with SQL statements

You can run SQL statements to verify that your tables exist in the migrated Cloud SQL database. Do the following:

  1. Connect to your Cloud SQL for PostgreSQL instance with a tool where you can run SQL commands against your migrated databases. 

For more information on connecting to Cloud SQL instances, see [Connection options](https://docs.cloud.google.com/sql/docs/postgres/connect-overview#tools_for_connecting_to) in Cloud SQL documentation.

  2. Run SQL commands to verify your migrated data. For example:

     * List all tables in the database: 
           
           SELECT * FROM pg_catalog.pg_tables;

     * Verify the table contents: 
           
           SELECT * FROM TABLE_NAME';




## Verify data with the Data Validation Tool

The [ open-source Data Validation Tool](https://github.com/GoogleCloudPlatform/professional-services-data-validator) lets you perform very precise data comparisons between two databases, but it requires creating network connections to your source and destination databases.

The following steps show a minimal example:

  1. Deploy or use a virtual machine with access to both the source and the destination.

  2. In the virtual machine, create a folder in which to install the Data Validation Tool.

  3. Navigate to this folder.

  4. Use [ `pip`](https://pip.pypa.io/en/stable/) to install the Data Validation Tool.
         
         pip install google-pso-data-validator
         

  5. Create connections to the source Oracle database and the destination Cloud SQL for PostgreSQL database:
         
         data-validation connections add -c source Oracle --host 'ip-address' --port port --user username --password pswd --database database-name
         data-validation connections add -c target Postgres --host 'ip-address' --port port --user username --password pswd --database database-name
         

For example:
         
         data-validation connections add -c source Oracle --host '10.10.10.11' --port 1521 --user system --password pswd --database XE
         data-validation connections add -c target Postgres --host '10.10.10.12' --port 5432 --user postgres --password pswd --database postgres
         

  6. Create or generate a list of tables to compare data between the source and destination databases:
         
         export TABLES_LIST=$(data-validation find-tables --source-conn source --target-conn target --allowed-schemas schema-name)
         

For example:
         
         export TABLES_LIST=$(data-validation find-tables --source-conn source --target-conn target --allowed-schemas public)
         

  7. Run full validation against all tables:
         
         data-validation validate column --source-conn source --target-conn target --tables-list "${TABLES_LIST}"
         




We suggest that you run this validation during replication to ensure relative consistency. Large table queries may take too long to run during a small promotion window. In such cases, use the Data Validation Tool to add filters to reduce runtime or prepare the table list to include a subset of tables for the final validation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
