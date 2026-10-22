---
url: https://docs.cloud.google.com/datastream/docs/configure-amazon-aurora-psql/
title: Configure an Amazon Aurora PostgreSQL database \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:17.877044+00:00
---

# Configure an Amazon Aurora PostgreSQL database  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-amazon-aurora-psql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure an Amazon Aurora PostgreSQL database Stay organized with collections  Save and categorize content based on your preferences. 

Streaming change data capture (CDC) updates from an Amazon Aurora PostgreSQL database to BigQuery, Cloud Storage, or another [supported destination](https://docs.cloud.google.com/datastream/docs/destinations) requires logical replication on your source cluster. To prepare your database for Datastream, you configure a cluster parameter group, create a publication and replication slot, and set up a Datastream user.

Before you begin, make sure that you have an existing Amazon Aurora cluster and are connected to the Writer endpoint of your primary database server.

## Create a parameter group

  1. Launch your Amazon RDS Dashboard.
  2. In the **Navigation Drawer** , click **Parameter Groups** , and then click **Create Parameter Group**. The **Create Parameter Group** page appears.
  3. Use the following table to populate the fields of this page, and then click **Create** : Field| Description  
---|---  
Parameter group family| Select the family that matches your database.  
Type| Select **DB Cluster Parameter Group**.  
Group name| Provide a name for the parameter group.  
Description| Provide a description for the parameter group.  
  4. Select the checkbox to the left of your newly created parameter group, and then, under **Parameter group actions** , click **Edit**.
  5. Change the value of the `rds.logical_replication` parameter to **1**.
  6. Click **Save Changes**.



## Assign the parameter group to the database instance

  1. Launch your Amazon RDS Dashboard.
  2. In the **Navigation Drawer** , click **Databases** , and then select your database instance.
  3. From the **Instance Actions** menu, select **Modify**. The **Modify DB Instance** dialog appears.
  4. In the **Additional configuration** section, select the database cluster parameter group that you created.
  5. Set the **Backup retention period** to **7 days**.
  6. Click **Continue**.
  7. In the **Scheduling of modifications** pane, select the **Apply immediately** option.



## Reboot the database instance

  1. Launch your Amazon RDS Dashboard.
  2. In the **Navigation Drawer** , click **Databases** , and then select your database instance.
  3. In the **Actions** drop-down menu, select **Reboot** and then **Confirm**.



## Create a publication and a replication slot

  1. Create a publication for the changes in the tables you want to replicate. We recommend that you create a publication only for the tables that you want to replicate. This allows Datastream to read-only the relevant data, and lowers the load on the database and Datastream:
         
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



## Create a Datastream user

  1. To create a Datastream user, enter the following PostgreSQL command: 
         
         CREATE USER USER_NAME WITH ENCRYPTED PASSWORD 'USER_PASSWORD';

Replace the following:

     * USER_NAME: The name of the Datastream user that you want to create.
     * USER_PASSWORD: The password for the Datastream user that you want to create.
  2. Grant the following privileges to the user you created: 
         
         GRANT RDS_REPLICATION TO USER_NAME;
         GRANT SELECT ON ALL TABLES IN SCHEMA SCHEMA_NAME TO USER_NAME;
         GRANT USAGE ON SCHEMA SCHEMA_NAME TO USER_NAME;
         ALTER DEFAULT PRIVILEGES IN SCHEMA SCHEMA_NAME
           GRANT SELECT ON TABLES TO USER_NAME;
         

Replace the following:

     * SCHEMA_NAME: The name of the schema to which you want to grant the privileges.
     * USER_NAME: The user to whom you want to grant the privileges.



## What's next

  * Learn more about how Datastream works with [PostgreSQL sources](https://docs.cloud.google.com/datastream/docs/sources-postgresql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
