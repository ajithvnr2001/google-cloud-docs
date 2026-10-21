---
url: https://docs.cloud.google.com/datastream/docs/configure-amazon-rds-psql/
title: Configure an Amazon RDS PostgreSQL database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:50.035724+00:00
---

# Configure an Amazon RDS PostgreSQL database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-amazon-rds-psql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure an Amazon RDS PostgreSQL database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure change data capture (CDC) to stream data from an Amazon RDS for PostgreSQL database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage.

### Create a parameter group

  1. Launch your Amazon RDS Dashboard.

  2. In the **Navigation Drawer** , click **Parameter Groups** , and then click **Create Parameter Group**. The **Create Parameter Group** page appears.

  3. Select the database family that matches your database, provide a name and description for the parameter group, and then click **Create**.

  4. Select the checkbox to the left of your newly created parameter group, and then, under **Parameter group actions** , click **Edit**.

  5. Set the following parameter for your group.

Parameter| Value  
---|---  
rds.logical_replication| `1`  
  6. Click **Save Changes**.

For PostgreSQL 13 and later, it is recommended that you also set the `max_slot_wal_keep_size` parameter in the `postgresql.conf` file to limit the amount of storage used by replication slots. For more information, see [Work with PostgreSQL database WAL log files](https://docs.cloud.google.com/datastream/docs/work-with-postgresql-database-wal-log-files).



### Configure the source database

  1. Launch your Amazon RDS Dashboard.

  2. In the **Navigation Drawer** , click **Databases**.

  3. Select your source, and then click **Modify**.

  4. Go to the **Additional configuration** section.

  5. Select the parameter group that you created.

  6. Click **Continue**.

  7. Under **Scheduling of modifications** , select **Apply immediately**.

Because you modified your source, you must wait until the changes to your parameter group are applied before proceeding.



### Verify that the parameter group is assigned to the database instance

  1. Launch your Amazon RDS Dashboard.

  2. In the **Navigation Drawer** , click **Databases** , and then select your database instance.

  3. Click the **Configurations** tab.

  4. Verify that you see the parameter group that you created, and that its status is **pending-reboot**.

  5. Reboot your database instance to complete the configuration. To reboot the instance:

     1. In the **Navigation Drawer** , click **Instances**.
     2. Select your database instance.
     3. From the **Instance Actions** menu, select **Reboot**.
After you reboot your database instance, its status changes to **in-sync**.



### Create a publication and a replication slot

  1. Create a publication. We recommend that you create a publication only for the tables that you want to replicate. This allows Datastream to read-only the relevant data, and lowers the load on the database and Datastream:
         
         CREATE PUBLICATION PUBLICATION_NAME
         FOR TABLE SCHEMA1.TABLE1, SCHEMA2.TABLE2;

Replace the following:

     * PUBLICATION_NAME: The name of your publication. You'll need to provide this name when you create a stream in the Datastream stream creation wizard.
     * SCHEMA: The name of the schema that contains the table.
     * TABLE: The name of the table that you want to replicate.

You can also create a publication for all tables in your database. Note that this approach increases the load on both the source database and Datastream:
    
    CREATE PUBLICATION PUBLICATION_NAME FOR ALL TABLES;
    

For PostgreSQL 15 and later, you can create a publication for all tables in a schema. This approach lets you replicate changes for tables in the specified list of schemas, including tables that you create in the future: 
    
    CREATE PUBLICATION PUBLICATION_NAME
    FOR TABLES IN SCHEMA SCHEMA1, SCHEMA2;

  2. Create a replication slot by entering the following PostgreSQL command: 
         
         SELECT PG_CREATE_LOGICAL_REPLICATION_SLOT('REPLICATION_SLOT_NAME', 'pgoutput'); 

Replace the following:

     * REPLICATION_SLOT_NAME: The name of your replication slot. You'll need to provide this name when you create a stream in the Datastream stream creation wizard.
The replication slot must be unique for each stream that's replicating from this database.



### Create a Datastream user

  1. To create a Datastream user, enter the following PostgreSQL command:
         
         CREATE USER USER_NAME WITH ENCRYPTED PASSWORD 'USER_PASSWORD';
         

Replace the following:

     * USER_NAME: The name of the Datastream user that you want to create.
     * USER_PASSWORD: The login password for the Datastream user that you want to create.
  2. Grant the following privileges to the user you created:
         
         GRANT RDS_REPLICATION TO USER_NAME;
         GRANT SELECT ON ALL TABLES IN SCHEMA SCHEMA_NAME TO USER_NAME;
         GRANT USAGE ON SCHEMA SCHEMA_NAME TO USER_NAME;
         ALTER DEFAULT PRIVILEGES IN SCHEMA SCHEMA_NAME
           GRANT SELECT ON TABLES TO USER_NAME;
         

Replace the following:

     * USER_NAME: The user to whom you want to grant the privileges.
     * SCHEMA_NAME: The name of the schema to which you want to grant the privileges.



## What's next

  * Learn more about how Datastream works with [PostgreSQL sources](https://docs.cloud.google.com/datastream/docs/sources-postgresql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
