---
url: https://docs.cloud.google.com/sql/docs/sqlserver/features/
title: Cloud SQL for SQL Server features \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:21.171371+00:00
---

# Cloud SQL for SQL Server features  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Cloud SQL for SQL Server features Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/features "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/features "View this page for the PostgreSQL database engine") | SQL Server

This page describes the major features and capabilities of Cloud SQL for SQL Server. Cloud SQL is also available for [MySQL](https://docs.cloud.google.com/sql/docs/mysql/features) and [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/features). **Note:** For information about the supported versions of database engines, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions).

## SQL Server feature support for Cloud SQL

  * Fully managed SQL Server databases in the cloud.
  * Custom machine types with up to 624 GB of RAM and 96 CPUs.
  * Up to 64 TB of storage available, with the ability to automatically increase storage size as needed.
  * Create and manage instances in the [Google Cloud console](https://console.cloud.google.com/).
  * Instances available in the Americas, Europe, Asia or Australia. See [all locations where you can create Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/locations).
  * [Database Migration Service for SQL Server](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview).
  * Customer data encrypted on Google's internal networks and in database tables, temporary files, and backups.
  * Column- and cell-level encryption for user databases.
  * Support for secure external connections with the Cloud SQL Auth Proxy or with the SSL/TLS protocol.
  * Import databases using BAK and SQL files.
  * Export databases using BAK files.
  * Automated backups, on-demand backups, and point-in-time recovery.
  * Instance cloning.
  * Integration with Stackdriver logging and monitoring.
  * SQL Server Agent enabled to facilitate replication and other jobs.
  * Data replication between multiple regions.
  * Set a default collation for databases, when creating an instance.
  * High availability through a regional persistent disk.
  * Integration with customer-managed Active Directory (CMAD), including Windows Authentication.
  * Integration with Managed Service for Microsoft Active Directory, including Windows Authentication.
  * Integration with Microsoft Entra ID.
  * Change Data Capture (CDC).
  * Intelligent query processing.
  * Accelerated database recovery.
  * Enhanced data classification.
  * UTF-8 character encoding support.
  * Enhanced monitoring.
  * Dynamic Data Masking (DDM).
  * Processor affinity masking using [`affinity mask`](https://docs.cloud.google.com/sql/docs/sqlserver/flags#list-flags-sqlserver) and [`affinity I/O mask`](https://docs.cloud.google.com/sql/docs/sqlserver/flags#list-flags-sqlserver).
  * Linked Servers.
  * SQL Server Audit.
  * SQL Server Publisher.
  * SQL Server Subscriber.
  * SQL Server Integration Services (SSIS) that runs on a separate host and connects to Cloud SQL. You can't host SSIS packages on or execute them from Cloud SQL.
  * SQL Server Reporting Services (SSRS) that runs on a separate host and connects to Cloud SQL. You can't host SSRS packages on or execute them from Cloud SQL.
  * The bulk copy program (bcp) utility. To learn more about downloading and installing the bcp utility, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver16#download-the-latest-version-of-bcp-utility).
  * BACPAC file imports and exports by using SqlPackage. To learn more about downloading and installing SqlPackage, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage-download?view=sql-server-ver16).
  * Bulk insert for importing data. This feature is supported only on SQL Server 2022. You can use a stored procedure for performing bulk insert. For more information, see [Use bulk insert for importing data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#bulk-insert).
  * Transparent Data Encryption (TDE). For information, see [About TDE](https://docs.cloud.google.com/sql/docs/sqlserver/about-tde).
  * Always Encrypted without secure enclaves.
  * Extended Events (XEvents).
  * Custom time zone support at instance creation and post instance creation.
  * Temporal tables. For more information, see [Temporal tables](https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables?view=sql-server-ver16).
  * Support for read pools
  * Storage shrink. For more information, see [About storage shrink](https://docs.cloud.google.com/sql/docs/sqlserver/about-storage-shrink).



## SQL Server features unavailable for Cloud SQL

The following features are unavailable in Cloud SQL and Google Cloud doesn't support them:

### General SQL Server features unavailable for Cloud SQL

  * SQL Server Analysis Services (SSAS)
  * SP_Configure settings. For more information about this feature, see [Configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).
  * Stretch database
  * Backing up to Microsoft Azure Blob Storage
  * Buffer pool extension
  * The OPENROWSET feature
  * Data Quality Services
  * Database Log Shipping
  * Database Mail
  * Dedicated Administrator Connection (DAC)
  * Distribution Transaction Coordinator (MSDTC)
  * File tables
  * FILESTREAM support
  * Installing a server that requires a full server installation with specific authentication mechanisms such as Azure DevOps Server.
  * Maintenance Plans
  * Performance Data Collector
  * Policy-Based Management
  * Machine Learning and R Services
  * Resource Governor
  * Server-level triggers
  * Service Broker endpoints
  * T-SQL endpoints (all operations using `CREATE ENDPOINT` are unavailable)
  * WCF Data Services
  * The `sysadmin` role and system stored procedures that require it
  * Hybrid buffer pool
  * Memory-optimized tempdb metadata
  * In-memory OLTP support for database snapshots
  * Registering external languages
  * Row-level security
  * Object storage backup and restore
  * [Persistent Memory (PMEM)](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-configure-pmem?view=sql-server-ver16)
  * Real-time operational analytics
  * Integrated acceleration and offloading
  * Hybrid buffer pool with direct write
  * Multi-write replication
  * Link to Azure SQL Managed instance
  * Contained availability group
  * Always Encrypted with secure enclaves
  * Support for PFX certificates and other cryptographic improvements
  * MS-TDS 8.0 protocol and TLS 1.3

**Note:** Cloud SQL is a managed service so it restricts access to certain system procedures and tables that require advanced privileges; you can't create or have access to users with superuser permissions.

### Other SQL Server operations unavailable for Cloud SQL

  * ADMINISTER BULK OPERATIONS
  * ALTER ANY CREDENTIAL
  * ALTER ANY EVENT NOTIFICATION
  * ALTER ANY EVENT SESSION
  * ALTER RESOURCES
  * ALTER SETTINGS
  * AUTHENTICATE SERVER
  * CONTROL_SERVER
  * CREATE DDL EVENT NOTIFICATION
  * CREATE ENDPOINT
  * CREATE TRACE EVENT NOTIFICATION
  * EXTERNAL ACCESS ASSEMBLY
  * RESTORE
  * SHUTDOWN
  * CLR ASSEMBLIES



## Supported syntax for Cloud SQL for SQL Server 

Cloud SQL supports the [Transact-SQL syntax](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/transact-sql-syntax-conventions-transact-sql?view=sql-server-2017).

## Supported languages for Cloud SQL for SQL Server 

You can use Cloud SQL with App Engine applications running in the flexible environment that are written in:

  * C#
  * Go
  * Java
  * Node.js
  * PHP
  * Python
  * Ruby



## How you can connect to Cloud SQL for SQL Server instances

You can connect to a Cloud SQL instance from:

  * [SQL Server Management Studio (SSMS)](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-2017). 
    * A client. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip).
  * [The sqlcmd utility](https://docs.microsoft.com/en-us/sql/ssms/scripting/sqlcmd-use-the-utility?view=sql-server-2017).



Connecting to Cloud SQL with Private Google access isn't supported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
