---
url: https://docs.cloud.google.com/database-migration/docs/supported-databases/
title: Supported source and destination databases \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:01.765504+00:00
---

# Supported source and destination databases  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/supported-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/overview)



Send feedback 

#  Supported source and destination databases Stay organized with collections  Save and categorize content based on your preferences. 

You can use Database Migration Service to migrate your databases to Google Cloud. Database Migration Service supports both homogeneous migrations, such as MySQL to Cloud SQL for MySQL, and heterogeneous migrations, such as Oracle to Cloud SQL for PostgreSQL.

This page lists the versions of all source and destination databases that Database Migration Service supports in all migration scenarios. Use this information to choose the source and destination databases for your migration.

## Homogeneous migrations supported source and destination databases

Select your homogeneous migration scenario to view which source and destination databases the migration supports:

### MySQL to Cloud SQL for MySQL

**Supported source databases**

  * Amazon RDS 5.6, 5.7, 8.0, 8.4, 9.7
  * Self-managed MySQL (on premises or on any cloud VM that you fully control) 5.5, 5.6, 5.7, 8.0, 8.4, 9.7
  * Cloud SQL for MySQL 5.6, 5.7, 8.0, 8.4, 9.7
  * Amazon Aurora 5.6, 5.7, 8.0, 8.4, 9.7
  * Microsoft Azure Database for MySQL 5.7, 8.0, 8.4, 9.7



For MySQL 8.0 sources, Database Migration Service also supports the following minor versions: 8.0.18, 8.0.26, 8.0.27, 8.0.28, 8.0.30, 8.0.31, 8.0.32, 8.0.33, 8.0.34, 8.0.35, 8.0.36, 8.0.37, 8.0.39, 8.0.40, 8.0.41, 8.0.42, 8.0.43. 

**Supported destination databases**

  * Cloud SQL for MySQL 5.6 and 5.7
  * Cloud SQL for MySQL 8.0 including the following minor versions: 8.0.18, 8.0.26, 8.0.27, 8.0.28, 8.0.30, 8.0.31, 8.0.32, 8.0.33, 8.0.34, 8.0.35, 8.0.36, 8.0.37, 8.0.39, 8.0.40, 8.0.41, 8.0.42, 8.0.43. 
  * Cloud SQL for MySQL 8.4 and 9.7 with certain limitations. For example, migrations that use physical backup files are not supported for MySQL 8.4 or 9.7 destinations. For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations). 
  * Cloud SQL for MySQL 9.7

**Note:** Migrating from a later minor version to an earlier minor version is not recommended. 

For more information, see [ Migrate to Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest).

### PostgreSQL to Cloud SQL for PostgreSQL

**Supported source databases**

  * Amazon RDS 9.6.10+, 10.5+, 11.1+, 12, 13, 14, 15, 16, 17, 18.
  * Amazon Aurora 10.11+, 11.6+, 12.4+, 13.3+, 14.6+, 15.2+, 16, 17, 18.
  * Self-managed PostgreSQL (on premises or on any cloud VM that you fully control) 9.4, 9.5, 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18.
  * Cloud SQL for PostgreSQL 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18.
  * Microsoft Azure Database for PostgreSQL Flexible Server Flexible Server: 11+



**Supported destination databases**

  * Cloud SQL for PostgreSQL 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18.



For more information, see [ Migrate to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest).

### PostgreSQL to AlloyDB for PostgreSQL

**Supported source databases**

  * Amazon RDS 9.6.10+, 10.5+, 11.1+, 12, 13, 14, 15, 16, 17
  * Amazon Aurora 10.11+, 11.6+, 12.4+, 13.3+, 14, 15, 16, 17
  * Self-managed PostgreSQL (on premises or on any cloud VM that you fully control) 9.4, 9.5, 9.6, 10, 11, 12, 13, 14, 15, 16, 17
  * Cloud SQL 9.6, 10, 11, 12, 13, 14, 15, 16, 17



**Supported destination databases**

  * AlloyDB for PostgreSQL 14, 15, 16, 17, 18



For more information, see [ Migrate to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest).

### SQL Server to Cloud SQL for SQL Server

The following table lists all supported SQL Server source and destination databases: 

Source databases | Destination databases  
---|---  
Amazon RDS |  Cloud SQL for SQL Server versions 2025, 2022, 2019, 2017  
Self-managed SQL Server (on-premises or on any cloud VM that you fully control)  
  
You can also use Database Migration Service to migrate from earlier versions of SQL Server to later versions supported in Cloud SQL, as long as you follow the version compatibility guidelines. For more information, see the supported version and edition upgrades for your SQL Server version in Microsoft documentation. For example, see [Supported version and edition upgrades (SQL Server 2025)](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/supported-version-and-edition-upgrades-2025?view=sql-server-ver17#upgrades-from-earlier-versions-to-sql-server-2025). 

For more information, see [ Migrate to Cloud SQL for SQL Server](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview).

## Heterogeneous migrations supported source and destination databases

Select your heterogeneous migration scenario to view which source and destination databases the migration supports:

### Oracle to Cloud SQL for PostgreSQL

**Supported source and destination databases**

Database Migration Service supports the following Oracle databases as migration sources:

  * Amazon RDS for Oracle
  * Self-hosted deployments, including: 
    * Oracle Single Instance Database Deployment
    * Oracle Exadata
    * Oracle Active Data Guard
    * Oracle Real Application Clusters (RAC)



Full support also depends on your source Oracle version. The following table lists all supported versions for heterogeneous Oracle migrations: 

Source databases | Destination databases  
---|---  
Oracle 11g, Version 11.2.0.4  |  Cloud SQL for PostgreSQL 12, 13, 14, 15, 16, 17, 18.  
Oracle 12c, Version 12.1.0.2  
Oracle 12c, Version 12.2.0.1  
Oracle 18c  
Oracle 19c  
Oracle 21c  
  
**Unsupported source databases**

Database Migration Service doesn't support migrating from Oracle Autonomous Database.

For more information, see [Migrate from Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview).

### Oracle to AlloyDB for PostgreSQL

**Supported source and destination databases**

Database Migration Service supports the following Oracle databases as migration sources:

  * Amazon RDS for Oracle
  * Self-hosted deployments, including: 
    * Oracle Single Instance Database Deployment
    * Oracle Exadata
    * Oracle Active Data Guard
    * Oracle Real Application Clusters (RAC)



Full support also depends on your source Oracle version. The following table lists all supported versions for heterogeneous Oracle migrations: 

Source databases | Destination databases  
---|---  
Oracle 11g, Version 11.2.0.4  |  AlloyDB for PostgreSQL 12, 13, 14, 15, 16, 17, 18.  
Oracle 12c, Version 12.1.0.2  
Oracle 12c, Version 12.2.0.1  
Oracle 18c  
Oracle 19c  
Oracle 21c  
  
**Unsupported source databases**

Database Migration Service doesn't support migrating from Oracle Autonomous Database.

For more information, see [Migrate from Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview).

### SQL Server to Cloud SQL for PostgreSQL

**Supported source and destination databases**

The following table lists all supported SQL Server source and destination databases:

Source databases | Destination databases  
---|---  
Amazon RDS for SQL Server |  Cloud SQL for PostgreSQL 12, 13, 14, 15, 16, 17, 18.  
Microsoft Azure SQL Managed Instance Microsoft Azure SQL Database tier S3 and above  
Cloud SQL for SQL Server   
Self-managed SQL Server versions: Enterprise 2008 and later, Standard 2016 SP1 and later, Developer 2008 and later (on premises or on any cloud VM that you fully control)  
  
**Unsupported source databases**

Database Migration Service doesn't support migrating from the following SQL Server versions:

  * SQL Server Standard edition versions from 2008 to 2014
  * SQL Server Express
  * SQL Server Web



For more information, see [ Migrate from SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview).

### SQL Server to AlloyDB for PostgreSQL

**Supported source and destination databases**

The following table lists all supported SQL Server source and destination databases:

Source databases | Destination databases  
---|---  
Amazon RDS for SQL Server |  AlloyDB for PostgreSQL 14, 15, 16, 17, 18.  
Microsoft Azure SQL Managed Instance Microsoft Azure SQL Database tier S3 and above  
Cloud SQL for SQL Server   
Self-managed SQL Server versions: Enterprise 2008 and later, Standard 2016 SP1 and later, Developer 2008 and later (on premises or on any cloud VM that you fully control)  
  
**Unsupported source databases**

Database Migration Service doesn't support migrating from the following SQL Server versions:

  * SQL Server Standard edition versions from 2008 to 2014
  * SQL Server Express
  * SQL Server Web



For more information, see [Migrate from SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
