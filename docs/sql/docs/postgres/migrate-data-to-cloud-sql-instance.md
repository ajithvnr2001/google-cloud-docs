---
url: https://docs.cloud.google.com/sql/docs/postgres/migrate-data-to-cloud-sql-instance/
title: About data migration in Cloud SQL \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:28.309301+00:00
---

# About data migration in Cloud SQL  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/migrate-data-to-cloud-sql-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  About data migration in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/migrate-data-to-cloud-sql-instance "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/migrate-data-to-cloud-sql-instance "View this page for the SQL Server database engine")

This page describes data migration options in Cloud SQL.

## Database Migration Service

Database Migration Service offers multiple migration paths to serve a wide variety of use cases:

  * [Homogeneous migrations](https://docs.cloud.google.com/database-migration/docs/homogeneous-migrations) let you move data without changing your database SQL engine from self-managed or cloud offerings. Database Migration Service can help you migrate from backup files, or take the snapshot for you.

  * [Heterogeneous migrations](https://docs.cloud.google.com/database-migration/docs/heterogeneous-migrations) from Oracle and SQL Server sources to Cloud SQL for PostgreSQL let you convert your database objects to PostgreSQL with the assistance of Gemini-powered conversion features. These features help ensure your database objects' consistency and quality in the converted PostgreSQL schemas.




### Database Migration Service in Cloud SQL for PostgreSQL

A special, lightweight migration flow called _quick-start migrations_ is integrated directly into Cloud SQL for PostgreSQL to help expedite homogeneous migrations from sources that have a private IP address in your Google Cloud Virtual Private Cloud (such as self-managed databases on Compute Engine, or Cloud SQL for PostgreSQL instances enabled for private networking).

In this flow, Database Migration Service can automatically manage all the networking requirements to connect to your source database. For more information on quick-start migrations in Cloud SQL for PostgreSQL, see [Quick-start migrations guide](https://docs.cloud.google.com/sql/docs/postgres/quick-start-migrations-guide).

## Replicate from an external server

Another option for migrating data from an external server into Cloud SQL is to use replication. Cloud SQL supports various replication modes to migrate data into your instance.

For more information, see [About replicating from an external server](https://docs.cloud.google.com/sql/docs/postgres/replication/external-server).

To set up Cloud SQL for data migration by using replication, see [Configure Cloud SQL and the external server for replication](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external).

## Limitations

  * If your instance has customized backup settings (for example, a [custom backup location](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backing-up#locationbackups)), then after you promote the instance, we recommend that you customize your backup settings again. During the promotion process, Cloud SQL resets your backup settings to their default values.
  * After you promote an instance, we recommend that you enable [point-in-time recovery](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
