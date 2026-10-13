---
url: https://docs.cloud.google.com/database-migration/docs/mysql/migration-fidelity/
title: Migration fidelity \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:40.198126+00:00
---

# Migration fidelity  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/migration-fidelity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Migration fidelity Stay organized with collections  Save and categorize content based on your preferences. 

When you're migrating your schema, data, and metadata from a source database to a destination database, you want to ensure that all of this information is migrated accurately. Database Migration Service provides a high-fidelity way to migrate database objects (including the schema, data, and metadata) from one database to another.

All of the following data, schema, and metadata components are migrated as part of the database migration:

## Data

  * All tables and schemas, excluding the following system databases: `sys`, `mysql`, `performance_schema`, and `information_schema`.



## Schema

  * Naming

  * Primary key

  * Data type

  * Ordinal position

  * Default value

  * Nullability

  * Auto-increment attributes

  * Secondary indexes




## Metadata

  * Stored procedures

  * Functions

  * Triggers

  * Views

  * Foreign key constraints




## Continuous migration

Data manipulation language (DML) and data definition language (DDL) changes to all data, schemas, and metadata listed earlier are updated during continuous migrations.

### What isn't migrated

  * To migrate encrypted databases you need to provide the encryption keys to Database Migration Service. Database Migration Service supports migrating data from encrypted Amazon Aurora or Amazon RDS databases because these databases handle decryption transparently in their services. For more information, see [ Encrypting Amazon Aurora resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html), [ Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html), and [ Configure customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek).

  * User accounts and logins aren't migrated.

MySQL system databases (`mysql`, `performance_schema`, `information_schema`, and `sys`) aren't migrated. These databases contain information about user accounts, logins, and privileges. User account login information must be managed in the destination Cloud SQL database instance directly.

Metadata objects (such as stored procedures, functions, views, events, and triggers) that use the [ `DEFINER` clause](https://dev.mysql.com/doc/refman/8.0/en/stored-objects-security.html) to reference a user account that doesn't exist on the destination instance will fail when invoked on the new Cloud SQL destination. You must either create the corresponding user accounts on the destination instance or update the `DEFINER` clauses before migrating. For more information, see [ Verify metadata with a `DEFINER` clause](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer).

To add users to the Cloud SQL destination instance, navigate to the instance and add users from the **Users** tab, or add them from the MySQL client. For more information about creating and managing database users in Cloud SQL for MySQL, see [ Create and manage users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users) in the Cloud SQL documentation.

  * Non-default flag settings aren't migrated to the Cloud SQL destination instance. Run [ SHOW VARIABLES](https://dev.mysql.com/doc/refman/8.0/en/show-variables.html) on your source database before migrating your schema, data, and metadata to the destination database, and then run it again on the Cloud SQL database. Update flag settings as needed on the Cloud SQL database to replicate the source settings.

**Note:** Some flags that apply to a primary database may not make sense on a replica. Not all MySQL flags are allowed on a Cloud SQL instance. For more information, see [ Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags) in the Cloud SQL documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
