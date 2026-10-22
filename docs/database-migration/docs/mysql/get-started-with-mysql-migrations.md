---
url: https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations/
title: Get started with MySQL homogeneous migrations \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:04.850174+00:00
---

# Get started with MySQL homogeneous migrations  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Get started with MySQL homogeneous migrations Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service provides a lot of flexibility for your homogeneous MySQL migrations to Cloud SQL for MySQL. Depending on your database size, downtime requirements, and networking setup, there are different workflows available to best meet your scenario. Detailed networking and other prerequisites are described in each migration guide.

The following table provides an overview of each migration flow:

Migration workflow | Best suited for | Description  
---|---|---  
[Migrate to a new destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/guide-to-new-instance) | Standard migrations where you want Database Migration Service to create and configure the destination Cloud SQL instance for you. | Database Migration Service automatically provisions a new destination Cloud SQL instance using configuration options you select, and migrates your source schemas and data. Covers both continuous and one-time migrations using automatic or manual `mysqldump` files.  
[Migrate to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/guide-to-existing-instance) | Scenarios where you need to pre-create and customize your destination Cloud SQL instance outside of Database Migration Service (for example, by using Terraform, custom database flags, existing read replicas, or Private Service Connect interfaces). | Migrate data into a standalone Cloud SQL instance that you have already created and configured before setting up the migration job. Covers both continuous and one-time migrations.  
[Migrate by using a Percona XtraBackup physical file](https://docs.cloud.google.com/database-migration/docs/mysql/migrate-with-physical-xtrabackup) | Very large, multi-terabyte self-hosted databases where a logical `mysqldump` export would be too slow. | Perform a physical migration by creating physical backup files with the third-party Percona XtraBackup utility and uploading them to a Cloud Storage bucket.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
