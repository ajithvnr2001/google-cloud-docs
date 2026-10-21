---
url: https://docs.cloud.google.com/datastream/docs/configure-azure-sqlserver/
title: Configure an Azure SQL database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:50.592473+00:00
---

# Configure an Azure SQL database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-azure-sqlserver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure an Azure SQL database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure change data capture (CDC) to stream data from an Azure SQL database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage.

**Note:** Datastream supports Azure SQL Database only when you use the change tables CDC method.

To configure an Azure SQL database:

  1. Enable change data capture (CDC) for your source Azure SQL database. To do it, connect to the database using Azure Data Studio or SQL Server Management Studio and run the following command:
         
         EXEC sys.sp_cdc_enable_db;
         GO
         

  2. Enable CDC on the tables for which you need to capture changes:
         
         EXEC sys.sp_cdc_enable_table
         @source_schema = N'SCHEMA_NAME',
         @source_name = N'TABLE_NAME',
         @role_name = NULL
         GO
         

**Note:** You need to run the command for each table for which you want to enable CDC.

Replace the following:

     * `SCHEMA_NAME`: the name of the schema to which the tables belong
     * `TABLE_NAME`: the name of the table for which you want to enable CDC
  3. Enable snapshot isolation.

When you backfill data from your SQL Server database, it's important to ensure consistent snapshots. If you don't apply the settings described in this section, changes made to the database during the backfill process might lead to duplicates or incorrect results. Applying snapshot isolation settings is required if your stream includes tables without primary keys.

Enabling snapshot isolation creates a temporary view of your database at the start of the backfill process. This ensures that the data being copied remains consistent, even if other users are making changes to the live tables at the same time. Enabling snapshot isolation might have a slight performance impact, but it's essential for reliable data extraction.

To enable snapshot isolation:

     1. Connect to your database using a SQL Server client.
     2. Run the following command:
    
    ALTER DATABASE DATABASE_NAME SET ALLOW_SNAPSHOT_ISOLATION ON;
    

Replace DATABASE_NAME with the name of you database.

  4. Create a Datastream user:

     1. Connect to the `master` database and create a login:
            
            USE master;
            CREATE LOGIN YOUR_LOGIN WITH PASSWORD = 'PASSWORD';
            

     2. Connect to the source database and create a user for your login:
            
            USE DATABASE_NAME
            CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;
            

     3. Assign the `db_owner` and `db_denydatawriter` roles to your user:
            
            EXEC sp_addrolemember 'db_owner', 'USER_NAME';
            EXEC sp_addrolemember 'db_denydatawriter', 'USER_NAME';
            

     4. Grant the `VIEW DATABASE STATE` permission to your user:
            
            GRANT VIEW DATABASE STATE TO USER_NAME;
            




## What's next

  * Learn more about how Datastream works with [SQL Server sources](https://docs.cloud.google.com/datastream/docs/sources-sqlserver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
