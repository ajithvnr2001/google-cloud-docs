---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/migrate-tables-without-primary-keys/
title: Migrate tables without primary keys \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:16.004046+00:00
---

# Migrate tables without primary keys  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/migrate-tables-without-primary-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Migrate tables without primary keys Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service migrates only tables that have primary keys. If your source database includes tables that don't have primary keys, you need to manually create primary key constraints in the converted tables in the destination database after you [ apply the converted schema](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/work-with-conversion-workspaces#apply-to-dest).

To migrate SQL Server tables without primary keys, do the following:

  1. [ Convert all your schema and apply it to the destination database](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/convert-sql). 
  2. [ Connect to your AlloyDB for PostgreSQL instance with the `psql` client](https://docs.cloud.google.com/alloydb/docs/connect-psql). 
  3. Create the missing primary key constraints for your tables. For more information about primary keys, see [ Primary Keys](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-PRIMARY-KEYS) in the PostgreSQL documentation. 

You can also expand the following sections to see sample SQL commands:

#### Create primary keys using existing columns

Your table might already have a logical primary key based on a column or a combination of columns. For example, there might be columns with a unique constraint or index configured. Use these columns to generate a new primary key for tables in your source database. For example: 
         
         ALTER TABLE TABLE_NAME
         ADD PRIMARY KEY (COLUMN_NAME);

#### Create a primary key using all columns

If you don't have a pre-existing constraint that could serve as a primary key, create primary keys using all columns of the table. Make sure that you don't exceed the maximum length of the primary key allowed by your PostgreSQL instance. For example: 
         
         ALTER TABLE TABLE_NAME
         ADD PRIMARY KEY (COLUMN_NAME_1, COLUMN_NAME_2, COLUMN_NAME_3, ...);

When creating a composite primary key like this, you need to explicitly list all column names you want to use. It's not possible to use a statement to retrieve all column names for this purpose. 




## What's next

  * Once all your converted tables have primary key constraints, you can proceed with your migration and [ create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-migration-job).

  * To get a complete, step-by-step migration walkthrough, see [ SQL Server to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
