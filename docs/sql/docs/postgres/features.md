---
url: https://docs.cloud.google.com/sql/docs/postgres/features/
title: Cloud SQL for PostgreSQL features \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:04.420119+00:00
---

# Cloud SQL for PostgreSQL features  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Cloud SQL for PostgreSQL features Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/features "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/features "View this page for the SQL Server database engine")

This page describes the major features and capabilities of Cloud SQL for PostgreSQL. Cloud SQL is also available for [MySQL](https://docs.cloud.google.com/sql/docs/mysql/features) and [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/features). **Note:** For information about the supported versions of database engines, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/postgres/db-versions).

## PostgreSQL features by Cloud SQL editions

For more information about the features for each edition of Cloud SQL for PostgreSQL, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro).

## PostgreSQL feature support for Cloud SQL

  * Fully managed PostgreSQL databases in the cloud.
  * Instances available in the Americas, EU, Asia, and Australia. See [all locations where you can create Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/locations).
  * Supports migration from source databases to Cloud SQL destination databases using [Database Migration Service (DMS)](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database).
  * Customer data encrypted on Google's internal networks and in database tables, temporary files, and backups.
  * Support for secure external connections with the Cloud SQL Auth Proxy or with the SSL/TLS protocol.
  * Data replication between multiple zones with automatic failover.
  * Import and export databases using SQL dump files.
  * Support for PostgreSQL client-server protocol and standard PostgreSQL connectors.
  * Automated backups, on-demand backups, and point-in-time recovery.
  * Instance cloning.
  * Integration with Google Cloud Observability logging and monitoring.
  * Support for multiple [PostgreSQL versions](https://docs.cloud.google.com/sql/docs/postgres/db-versions).
  * Logical replication
  * Support for read pools and read pool autoscaling
  * Storage shrink. For more information, see [About storage shrink](https://docs.cloud.google.com/sql/docs/postgres/about-storage-shrink).



## Supported PostgreSQL extensions for Cloud SQL

Cloud SQL supports many PostgreSQL extensions. For a complete list of these extensions, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

## Supported PostgreSQL procedural languages for Cloud SQL

Cloud SQL supports the [`PL/pgSQL` SQL procedural language](https://www.postgresql.org/docs/current/static/plpgsql.html).

## Supported languages for Cloud SQL for PostgreSQL

You can use Cloud SQL with App Engine applications running in the flexible environment that are written in:

  * C#
  * Go
  * Java
  * Node.js
  * PHP
  * Python
  * Ruby



You can also use Cloud SQL with external applications using the standard PostgreSQL client-server protocol.

## How you can connect to Cloud SQL for PostgreSQL instances

You can connect to a Cloud SQL instance from:

  * A `psql` client. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip).
  * Third-party tools that use the standard PostgreSQL client-server protocol.
  * External applications. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-external-app).
  * App Engine applications. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine).
  * Applications running on Compute Engine. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-compute-engine).
  * Applications running on Google Kubernetes Engine. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine).
  * Cloud Run functions. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-functions). 
    * Cloud Run. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/connect-run).



Connecting to Cloud SQL with Private Google access isn't supported.

## Differences between standard PostgreSQL and Cloud SQL for PostgreSQL

In general, the PostgreSQL functionality provided by a Cloud SQL instance is the same as the functionality provided by a locally-hosted PostgreSQL instance. However, there are a few differences between a standard PostgreSQL instance and a Cloud SQL instance.

### Unsupported features for Cloud SQL for PostgreSQL

  * Any feature that requires `SUPERUSER` privileges with the following exceptions:

    * You can use the `CREATE EXTENSION` statement only for supported extensions.

    * If you are assigned to the `cloudsqlsuperuser` role, then you can perform `CREATE CAST` and `DROP CAST` statements. For more information, see [Superuser restrictions and privileges](https://docs.cloud.google.com/sql/docs/postgres/users#superuser-restrictions-and-privileges).

  * The `WITHOUT FUNCTION` cast method.

  * Custom background workers.

  * The `psql` client in Cloud Shell doesn't support operations that require a reconnection, such as connecting to a different database using the `\c` command. 

  * Low-Level Virtual Machine (LLVM) Just-in-Time (JIT) compilation.




### Notable differences between PostgreSQL and Cloud SQL for PostgreSQL

  * Some PostgreSQL options and parameters aren't enabled for editing as [ Cloud SQL flags](https://docs.cloud.google.com/sql/docs/postgres/flags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
