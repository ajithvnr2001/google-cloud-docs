---
url: https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest/
title: Supported sources and versions \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:24.904767+00:00
---

# Supported sources and versions  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Supported sources and versions Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service supports continuous migrations from PostgreSQL source databases to Cloud SQL for PostgreSQL destination databases.

## Supported sources

  * Amazon RDS 9.6.10+, 10.5+, 11.1+, 12, 13, 14, 15, 16, 17, 18.
  * Amazon Aurora 10.11+, 11.6+, 12.4+, 13.3+, 14.6+, 15.2+, 16, 17, 18.
  * Self-managed PostgreSQL (on premises or on any cloud VM that you fully control) 9.4, 9.5, 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18.
  * Cloud SQL for PostgreSQL 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18.
  * Microsoft Azure Database for PostgreSQL Flexible Server Flexible Server: 11+



For all supported source database offerings, Database Migration Service can migrate the databases you select from your source server. Certain system schemas and tables cannot be migrated. For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations).

## Supported destinations

  * Cloud SQL for PostgreSQL 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18.



## Cross-version support

Database Migration Service supports PostgreSQL-to-Cloud SQL for PostgreSQL migrations where the destination database version is the same major version as the source database, or any higher supported major version.

  * **Standard migrations** : Migrating from a later major version to an earlier major version (for example, from PostgreSQL 16 to 15) is unsupported. Migrating from a later minor version to an earlier minor version isn't recommended.
  * **Quick-start migrations** : Migrating to an earlier major version is permitted. Database Migration Service displays a warning rather than blocking the operation.



## What's next

  * For more information on feature support and constraints, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations).

  * To review the end-to-end migration process, see the [ Scenario overview](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview).

  * To get started with a migration walkthrough, see [ Get started with Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
