---
url: https://docs.cloud.google.com/datastream/docs/configure-self-managed-psql/
title: Configure a self-managed PostgreSQL database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:36.191795+00:00
---

# Configure a self-managed PostgreSQL database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-self-managed-psql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a self-managed PostgreSQL database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

Datastream lets you stream change data capture (CDC) updates from a self-managed PostgreSQL or AlloyDB Omni database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage. To prepare your source database, you enable logical replication, create a publication and replication slot, and configure a Datastream user with replication privileges.

## Enable logical replication on the database

  1. Set the `wal_level` parameter in your database by adding `wal_level=logical` to the `postgresql.conf` file.

  2. Restart the server.




## Create a publication and a replication slot

  1. Sign in to a PostgreSQL console as a superuser.

  2. Create a publication. We recommend that you create a publication only for the tables that you want to replicate. This allows Datastream to read-only the relevant data, and lowers the load on the database and Datastream:
         
         CREATE PUBLICATION PUBLICATION_NAME
         FOR TABLE SCHEMA1.TABLE1, SCHEMA2.TABLE2;

Replace the following:

     * PUBLICATION_NAME: The name of your publication. You'll need to provide this name when you create a stream in the Datastream stream creation wizard.
     * SCHEMA: The name of the schema that contains the table.
     * TABLE: The name of the table that you want to replicate.

You can create a publication for all tables in a schema. This approach lets you replicate changes for tables in the specified list of schemas, including tables that you create in the future:
    
    CREATE PUBLICATION PUBLICATION_NAME
    FOR TABLES IN SCHEMA SCHEMA1, SCHEMA2;

You can also create a publication for all tables in your database. Note that this approach increases the load on both the source database and Datastream:
    
    CREATE PUBLICATION PUBLICATION_NAME FOR ALL TABLES;
    

  3. Create a replication slot by entering the following SQL command: 
         
         SELECT PG_CREATE_LOGICAL_REPLICATION_SLOT('REPLICATION_SLOT_NAME', 'pgoutput');

Replace the following:

     * REPLICATION_SLOT_NAME: The name of your replication slot. You will need to provide this name when you create a stream in the Datastream stream creation wizard.
The replication slot name must be unique for each stream that's replicating from this database.



### Create a Datastream user

  1. To create a Datastream user, enter the following SQL commands: 
         
         CREATE USER USER_NAME WITH ENCRYPTED PASSWORD 'USER_PASSWORD';

Replace the following:

     * USER_NAME: The name of the Datastream user that you want to create.
     * USER_PASSWORD: The login password for the Datastream user that you want to create.
  2. Grant the following privileges to the user you created:
         
         ALTER ROLE USER_NAME WITH REPLICATION;
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
