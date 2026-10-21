---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-destination-database/
title: Create and configure your destination Cloud SQL instance \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:51.229463+00:00
---

# Create and configure your destination Cloud SQL instance  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-destination-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Create and configure your destination Cloud SQL instance Stay organized with collections  Save and categorize content based on your preferences. 

For heterogeneous Oracle migrations to Cloud SQL, Database Migration Service requires that you first create and configure your Cloud SQL destination instance. Perform the following steps:

  1. Create your destination instance. Make sure you configure enough compute and memory resources to cover your migration needs and follow the requirements listed in [ known limitations](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/known-limitations). 

We recommend that you create your destination instance with settings specific to the [ destination networking method](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-destination) you want to use: 

If you want to use...| Then...  
---|---  
[ Public IP destination connectivity](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-destination#public-ip), | Create your destination instance with public IP enabled. See [ Create a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance) in the Cloud SQL for PostgreSQL documentation.  
[ Private IP destination connectivity](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-destination#private-ip), |  Determine if you can use a PSC-enabled Cloud SQL instance as your migration destination. Carefully consider functionality limitations for PSC-enabled instances. See [ Private Service Connect limitations](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#limitations) in the Cloud SQL documentation. 
     * For scenarios where you can use a PSC-enabled Cloud SQL instance, create your destination instance with both private IP and Private Service Connect enabled. See [ Create a PSC-enabled Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-cloud-sql-instance-psc-enabled) in the Cloud SQL for PostgreSQL documentation. 
     * For scenarios where you can't use a PSC-enabled Cloud SQL instance, create your destination instance with private IP enabled. See [ Create a Cloud SQL instance with private IP enabled](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-cloud-sql-instance-psc-enabled) in the Cloud SQL for PostgreSQL documentation.   
  2. Create the following entities in your destination instance: 
     * A [ database to migrate your data](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases). 
     * A [ dedicated migration user account](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating). 
  3. Grant the required permissions to the dedicated migration user account. Do the following: 
     1. Connect to your Cloud SQL instance with a SQL client. You can use the following methods: 
        * [ `psql` client](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip). You can use this method to connect to your instance private IP, but it might require that you create a Compute Engine virtual machine. 
        * [ `gcloud sql connect`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/connect) command. This command works only for Cloud SQL instances that have a public IP address enabled. 
     2. Run the following command on your destination instance: 
            
            GRANT CREATE ON DATABASE DESTINATION_DB_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT CREATE ON SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";
            GRANT SELECT, INSERT, UPDATE, DELETE, TRUNCATE ON ALL TABLES IN SCHEMA SCHEMA_NAME TO "MIGRATION_USER_ACCOUNT_NAME";

     3. Optional: Grant your migration user the `CREATEDB` permission for the purposes of testing converted schema. 

At a later point in the migration, after you [ convert the source schema](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/convert-sql), you can use Database Migration Service to test whether converted schema can be applied to a PostgreSQL database. To perform the test, Database Migration Service creates a temporary database to avoid impacting your destination database. If you want to [ test your converted schema](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces#test-apply-to-dest), grant your migration user the `CREATEDB` permission. Use the following command: 
            
            ALTER USER "MIGRATION_USER_ACCOUNT_NAME" WITH CREATEDB;

     4. **For source databases that contain foreign keys or triggers** : Skip replication for foreign keys and triggers by using the [ `REPLICATION`](https://www.postgresql.org/docs/current/role-attributes.html#id-1.6.9.6.2.1.5.1.1) option with the dedicated migration user account. Run the following command: 
            
            ALTER USER "MIGRATION_USER_ACCOUNT_NAME" WITH REPLICATION;

For more information about how Database Migration Service migrates foreign keys and triggers, see [ Considerations for foreign keys and triggers](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/known-limitations#foreign-keys-triggers-considerations). 




## What's next?

  * Learn about destination database network connectivity. See [ Destination database networking methods](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-destination).

  * Learn about migration jobs. See [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-migration-job)

  * To get a complete, step-by-step migration walkthrough, see [ Oracle to Cloud SQL for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
