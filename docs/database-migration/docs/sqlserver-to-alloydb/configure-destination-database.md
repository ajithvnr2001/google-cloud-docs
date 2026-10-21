---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-destination-database/
title: Create and configure your destination AlloyDB for PostgreSQL instance \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:25.311318+00:00
---

# Create and configure your destination AlloyDB for PostgreSQL instance  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-destination-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Create and configure your destination AlloyDB for PostgreSQL instance Stay organized with collections  Save and categorize content based on your preferences. 

For heterogeneous SQL Server migrations to AlloyDB for PostgreSQL, Database Migration Service requires that you first create and configure your AlloyDB for PostgreSQL destination cluster. Perform the following steps:

  1. Create your destination cluster. Make sure you configure enough compute and memory resources to cover your migration needs and follow the requirements listed in [ known limitations](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/known-limitations). **Note:** If you're migrating from a Cloud SQL for SQL Server instance, create the destination cluster in the same region as your source. 

We recommend that you create your destination cluster with settings specific to the [ destination networking method](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination) you want to use: 

If you want to use...| Then...  
---|---  
[ Public IP destination connectivity](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination#public-ip), | Create your destination cluster with public IP enabled for **inbound connections**. See [ Create an AlloyDB for PostgreSQL instance](https://docs.cloud.google.com/alloydb/docs/connect-public-ip#create-instance) in the AlloyDB for PostgreSQL documentation.  
[ Private IP destination connectivity](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination#private-ip), |  Determine if you can use a PSC-enabled AlloyDB for PostgreSQL instance as your migration destination. Carefully consider functionality limitations for PSC-enabled instances. See [ Private Service Connect limitations](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#limitations) in the AlloyDB for PostgreSQL documentation. 
     * For scenarios where you can use a PSC-enabled AlloyDB for PostgreSQL instance, create your destination cluster with Private Service Connect enabled. See [ Create a PSC-enabled AlloyDB for PostgreSQL instance](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#enable-psc) in the AlloyDB for PostgreSQL documentation. You don't have to create a Private Service Connect endpoint for your destination instance. Database Migration Service can automatically handle the endpoint creation in the background when you create the migration job. 
     * For scenarios where you can't use a PSC-enabled AlloyDB for PostgreSQL instance, create your destination cluster enabled with private services access. See [ Create an AlloyDB for PostgreSQL instance with private services access](https://docs.cloud.google.com/alloydb/docs/cluster-create#gcloud) in the AlloyDB for PostgreSQL documentation.   
  2. Create the following entities in your destination cluster: 
     * A [ database to migrate your data](https://docs.cloud.google.com/alloydb/docs/database-create). 
     * A [ dedicated migration user account](https://cloud.google.com/alloydb/docs/database-users/about#create). 

This user account must have the same name as your destination database. For example, if you use Database Migration Service to migrate your data into a database called `myapp`, then the name of the dedicated migration user should also be `myapp`. 

  3. Grant the required permissions to the dedicated migration user account. Do the following: 
     1. [ Connect to your AlloyDB for PostgreSQL instance with the `psql` client](https://docs.cloud.google.com/alloydb/docs/connect-psql). 
     2. Run the following commands on your destination database: 
            
            GRANT CREATE ON DATABASE DESTINATION_DB_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT CREATE ON SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT, INSERT, UPDATE, DELETE, TRUNCATE ON ALL TABLES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";

     3. Optional: Grant your migration user the `CREATEDB` permission for the purposes of testing converted schema. 

At a later point in the migration, after you [ convert the source schema](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/convert-sql), you can use Database Migration Service to test whether converted schema can be applied to a PostgreSQL database. To perform the test, Database Migration Service creates a temporary database to avoid impacting your destination database. If you want to [ test your converted schema](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/work-with-conversion-workspaces#test-apply-to-dest), grant your migration user the `CREATEDB` permission. Use the following command: 
            
            ALTER USER "MIGRATION_USER_ACCOUNT_NAME" WITH CREATEDB;

     4. **For source databases that contain foreign keys or triggers** : Skip replication for foreign keys and triggers by using the [ `REPLICATION`](https://www.postgresql.org/docs/current/role-attributes.html#id-1.6.9.6.2.1.5.1.1) option with the dedicated migration user account. Run the following command: 
            
            ALTER USER "MIGRATION_USER_ACCOUNT_NAME" WITH REPLICATION;

For more information about how Database Migration Service migrates foreign keys and triggers, see [ Considerations for foreign keys and triggers](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/known-limitations#foreign-keys-triggers-considerations). 




## What's next?

  * Learn about destination database network connectivity. See [ Destination database networking methods](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination).

  * Learn about migration jobs. See [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-migration-job)

  * To get a complete, step-by-step migration walkthrough, see [ SQL Server to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
