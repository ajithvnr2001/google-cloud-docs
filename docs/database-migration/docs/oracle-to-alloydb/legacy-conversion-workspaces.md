---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/legacy-conversion-workspaces/
title: About legacy conversion workspaces \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:29.524709+00:00
---

# About legacy conversion workspaces  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/legacy-conversion-workspaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  About legacy conversion workspaces Stay organized with collections  Save and categorize content based on your preferences. 

Legacy conversion workspaces are an older, more limited type of conversion workspaces. Legacy conversion workspaces don't support Gemini-enhanced conversion features or the interactive SQL editor. You can only use them to convert your source schema with the Ora2Pg migration tool.

**Important:** Database Migration Service supports Ora2Pg versions `21.1` \- `23.2`.

We don't recommend using the legacy type of conversion workspaces for your migrations as they present multiple other limitations to the conversion workflow:

Interactive conversion workspace| Legacy conversion workspace  
---|---  
Schema and code object conversion happens in Database Migration Service. | You perform schema and code object conversions outside Database Migration Service by using the Ora2Pg migration tool.   
You can apply converted sources to the destination database directly in Database Migration Service. | You are responsible for applying the converted schema to the destination database in your AlloyDB for PostgreSQL destination cluster.  
You can test your draft schema and code directly in Database Migration Service to ensure they can be successfully applied to your destination cluster. | You can't test your draft schema and code without affecting the destination cluster.  
Automatically adds missing `rowid` columns for tables that don't have primary keys and unique constraints. | You must add missing primary keys to destination tables after you apply the schema.  
**Table 1** : Conversion workspace feature comparison

## Use legacy conversion workspaces

If your scenario requires the use of legacy conversion workspaces, modify the migration process with the following actions:

  1. Write an Ora2Pg configuration file.

Refer to the [ Ora2Pg documentation](https://ora2pg.darold.net/documentation.html#CONFIGURATION) for guidance on how to use the Ora2Pg conversion tool. Expand the following sections for the full list of directives supported in Database Migration Service. 

####  Ora2Pg configuration supported in Database Migration Service

Database Migration Service uses supported the following configuration for Ora2Pg files:

     * `BOOLEAN_VALUES`
     * `DATA_TYPE`
     * `DEFAULT_NUMERIC`
     * `ENABLE_MICROSECOND`
     * `EXPORT_SCHEMA`
     * `MODIFY_STRUCT`
     * `MODIFY_TYPE`
     * `PG_INTEGER_TYPE`
     * `PG_NUMERIC_TYPE`
     * `PG_SCHEMA`
     * `PRESERVE_CASE`
     * `REPLACE_AS_BOOLEAN`
     * `REPLACE_COLS`
     * `REPLACE_TABLES`
     * `REPLACE_ZERO_DATE`
     * `SCHEMA`

Database Migration Service uses connection profiles to define connectivity details, so you don't need to define the following information in your Or2Pg configuration file:

     * `ORACLE_DSN`
     * `ORACLE_HOME`
     * `ORACLE_PWD`
     * `ORACLE_USER`
     * `PG_DSN`
     * `PG_PWD`
     * `PG_USER`

Additionally, Database Migration Service doesn't use the `WHERE` configuration directive to limit the records to migrate.

  2. [ Create a legacy conversion workspace and convert schema](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-conversion-workspace#legacy-ws). 
  3. Manually apply converted schema to the destination database.

After you create the Ora2Pg configuration and create the workspace, you must apply the generated code by yourself directly on the destination database. 

**Important:** With legacy conversion workspaces, you can't test the schema before you migrate. If you encounter any issues when you apply the converted schema, you need to clear the faulty schema from the destination database, adjust your Ora2Pg file, and re-create the legacy conversion workspace with the Ora2Pg file. 
  4. Migrate tables without primary keys.

Database Migration Service migrates only tables that have primary keys. If your source database includes tables that don't have primary keys, you need to manually create primary keys or unique constraints in the converted tables in the destination database after you apply the converted schema. For more information and detailed steps, see [ Add primary key constraints in the destination database](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/migrate-tables-without-pks#add-keys-manually). 




## What's next

After you perform the conversion workflow with the legacy workspace, you can proceed with the standard migration procedures. See [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-migration-job).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
