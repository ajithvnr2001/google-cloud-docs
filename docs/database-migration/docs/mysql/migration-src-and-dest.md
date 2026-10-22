---
url: https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest/
title: Supported source and destination databases \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:03.431249+00:00
---

# Supported source and destination databases  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Supported source and destination databases Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service supports one-time and continuous migrations from source databases to Cloud SQL destination databases.

**Important:** Database Migration Service isn't compatible with MariaDB.

## Supported sources

  * Amazon RDS 5.6, 5.7, 8.0, 8.4, 9.7
  * Self-managed MySQL (on premises or on any cloud VM that you fully control) 5.5, 5.6, 5.7, 8.0, 8.4, 9.7
  * Cloud SQL for MySQL 5.6, 5.7, 8.0, 8.4, 9.7
  * Amazon Aurora 5.6, 5.7, 8.0, 8.4, 9.7
  * Microsoft Azure Database for MySQL 5.7, 8.0, 8.4, 9.7



For MySQL 8.0 sources, Database Migration Service also supports the following minor versions: 8.0.18, 8.0.26, 8.0.27, 8.0.28, 8.0.30, 8.0.31, 8.0.32, 8.0.33, 8.0.34, 8.0.35, 8.0.36, 8.0.37, 8.0.39, 8.0.40, 8.0.41, 8.0.42, 8.0.43. 

## Supported destinations

  * Cloud SQL for MySQL 5.6 and 5.7
  * Cloud SQL for MySQL 8.0 including the following minor versions: 8.0.18, 8.0.26, 8.0.27, 8.0.28, 8.0.30, 8.0.31, 8.0.32, 8.0.33, 8.0.34, 8.0.35, 8.0.36, 8.0.37, 8.0.39, 8.0.40, 8.0.41, 8.0.42, 8.0.43. 
  * Cloud SQL for MySQL 8.4 and 9.7 with certain limitations. For example, migrations that use physical backup files are not supported for MySQL 8.4 or 9.7 destinations. For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations). 
  * Cloud SQL for MySQL 9.7



## Cross-version support

Database Migration Service supports MySQL-to-Cloud SQL migrations where the destination is the same version or one version higher than the source database. For example, you can migrate a MySQL 5.6 source database to a Cloud SQL 5.6 or 5.7 destination, but you can't migrate from version 5.6 directly to 8.0. Migrating from a later minor version to an earlier minor version isn't recommended.

See the following table for the full version compatibility matrix.

Source  
database version | Destination database version  
---|---  
5.6 | 5.7 | 8.0 | 8.4 | 9.7  
5.5 |  Supported |  Unsupported |  Unsupported |  Unsupported |  Unsupported  
5.6 |  Supported |  Supported |  Unsupported |  Unsupported |  Unsupported  
5.7 |  Unsupported |  Supported |  Supported |  Unsupported |  Unsupported  
8.0 |  Unsupported |  Unsupported |  Supported**1** |  Supported  
|  Unsupported  
8.4 |  Unsupported |  Unsupported |  Unsupported |  Supported |  Supported  
9.7 |  Unsupported |  Unsupported |  Unsupported |  Unsupported |  Supported  
**1** Special limitations apply. For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
