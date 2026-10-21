---
url: https://docs.cloud.google.com/database-migration/docs/mysql/verify-migration/
title: Verify a migration \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:38.997794+00:00
---

# Verify a migration  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/verify-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Verify a migration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to confirm that your migrated data is complete and accurate. At a minimum, you should verify that your tables exist in the migrated Cloud SQL databases instance.

  1. Connect to your Cloud SQL instance with a tool where you can run SQL commands against your migrated databases. 

For more information on connecting to Cloud SQL instances, see [ Connection options](https://docs.cloud.google.com/sql/docs/mysql/connect-overview#tools_for_connecting_to) in Cloud SQL documentation.

  2. Run SQL commands to verify your migrated data. For example: 

#### List all databases

Run the following command to verify if your destination Cloud SQL contains all the source databases you wanted to migrate:
         
         SHOW databases;

#### List all tables in a database

Run the following command to check if your migrated database contains all the necessary tables:
         
         SHOW tables;

#### Check table content and definitions

Run the following commands to verify the correctness of a specific migrated table:

     1. View the table definition: 
            
            SHOW CREATE TABLE TABLE_NAME;

     2. Verify the table contents: 
            
            SELECT * FROM TABLE_NAME;




For automated, large-scale validation across your source and destination databases, you can also use the open-source [Data Validation Tool (DVT)](https://github.com/GoogleCloudPlatform/professional-services-data-validator). DVT is a Python CLI tool that compares schemas, row counts, column aggregations, and row-level hashes between source and destination MySQL instances to verify data completeness and accuracy before cutover.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
