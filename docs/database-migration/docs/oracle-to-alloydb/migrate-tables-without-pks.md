---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/migrate-tables-without-pks/
title: Migrate tables without primary keys \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:28.211343+00:00
---

# Migrate tables without primary keys  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/migrate-tables-without-pks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Migrate tables without primary keys Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to migrate Oracle tables that don't have primary keys.

  * Automatic primary key generation explains how Database Migration Service handles source tables with missing primary keys.

  * Add missing primary keys manually shows example queries that you can use to add missing primary keys in your converted schema.




## Automatic primary key generation overview

Tables without primary keys don't promise consistent replication. Database Migration Service only migrates tables that have primary keys. If your source database includes tables that don't have primary keys, Database Migration Service can handle that in the following ways:

  * When you [ convert your source code and schema](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/convert-sql), Database Migration Service can automatically create any missing primary keys by adding `ROWID` columns in the destination tables. This automated process requires that your source tables: 
    * Don't already have primary keys.
    * Don't have a `UNIQUE` constraint with no nullable columns.
    * Don't have a `UNIQUE` index with no nullable columns.
If your tables don't meet these requirements, you need to manually add missing primary keys to the tables in the converted PostgreSQL schema. 
  * In **legacy conversion workspaces** , Database Migration Service doesn't automatically create primary keys. If you use a legacy conversion workspace, you need to manually add missing primary keys to the tables in the converted PostgreSQL schema. 



## Add missing primary keys manually

To migrate Oracle tables without primary keys, do the following:

  1. Use a conversion workspace to convert your source code and schema. 
     * For standard conversion workspaces, see [ Convert your source code and schema](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/convert-sql). 
     * For legacy conversion workspaces, see [ Work with legacy conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/legacy-conversion-workspaces). 
  2. [ Connect to your AlloyDB for PostgreSQL cluster with the `psql` client](https://docs.cloud.google.com/alloydb/docs/connect-psql). 
  3. Create the missing primary key constraints for your tables. For more information about primary keys, see [ Primary Keys](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-PRIMARY-KEYS) in the PostgreSQL documentation. 

You can also expand the following sections to see sample SQL commands:

#### Create primary keys using existing columns

Your table might already have a logical primary key based on a column or a combination of columns. For example, there might be columns with a unique constraint or index configured. Use these columns to generate a new primary key for tables in your source database. For example: 
         
         ALTER TABLE TABLE_NAME
         ADD PRIMARY KEY (COLUMN_NAME);

Replace the following:

     * TABLE_NAME with the name of your table that doesn't have a primary key. 
     * COLUMN_NAME with the name of a column with unique constraint or index that you can use as the primary key. 

#### Create a primary key using all columns

If you don't have a pre-existing constraint that could serve as a primary key, create primary keys using all columns of the table. Make sure that you don't exceed the maximum length of the primary key allowed by your PostgreSQL instance. 

When you create a composite primary key this way, you need to explicitly list all column names you want to use. It's not possible to use a statement to retrieve all column names for this purpose. For example: 
    
    ALTER TABLE TABLE_NAME
    ADD PRIMARY KEY (COLUMN_NAME_1, COLUMN_NAME_2, COLUMN_NAME_3, ...);

Replace the following:

     * TABLE_NAME with the name of your table that doesn't have a primary key. 
     * COLUMN_NAME_1, COLUMN_NAME_2 etc. with the names of columns you want to use to create the primary key. 

#### Create a unique constraint with the `ROWID` pseudocolumn

Oracle databases use the [ `ROWID` pseudocolumn](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ROWID-Pseudocolumn.html) to store the location of each row in a table. To migrate Oracle tables that don't have primary keys, you can add a `ROWID` column in the destination PostgreSQL database. Database Migration Service populates the column with the corresponding numeric values from the source Oracle `ROWID` pseudocolumn. 

To add the column and to set it as the primary key, run the following:
    
    ALTER TABLE TABLE_NAME ADD COLUMN rowid numeric(33,0) NOT NULL;
    CREATE SEQUENCE TABLE_NAME_rowid_seq INCREMENT BY -1 START WITH -1 OWNED BY TABLE_NAME.rowid;
    ALTER TABLE TABLE_NAME ALTER COLUMN rowid SET DEFAULT nextval('TABLE_NAME_rowid_seq');
    ALTER TABLE TABLE_NAME ADD CONSTRAINT CONSTRAINT_DISPLAY_NAME PRIMARY KEY (rowid);

Replace the following:

     * TABLE_NAME with the name of the table in which you want to add the column.
     * CONSTRAINT_DISPLAY_NAME with the identifier for the `PRIMARY KEY` constraint.




## What's next

  * [ Continue working with conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/work-with-conversion-workspaces).
  * [ Learn more about Gemini-powered conversion features](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces#ai-conversion).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
