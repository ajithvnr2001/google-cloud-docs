---
url: https://docs.cloud.google.com/database-migration/docs/release-notes/
title: Database Migration Service release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:17.115146+00:00
---

# Database Migration Service release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Resources ](https://docs.cloud.google.com/database-migration/docs/release-notes)



Send feedback 

#  Database Migration Service release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Database Migration Service. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/dms-release-notes.xml) directly. 

## August 17, 2026

Announcement

Database Migration Service for MySQL homogeneous migrations now supports MySQL version 9.7. For more information, see [ Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/supported-databases).

## August 05, 2026

Feature

You can now manage your Database Migration Service migration jobs directly from the destination Cloud SQL instance or AlloyDB for PostgreSQL cluster pages in the Google Cloud console. For more information, see:

  * Manage homogeneous migration jobs: 
    * [ SQL Server to Cloud SQL for SQL Server](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs)
    * [ MySQL to Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-actions)
    * [ PostgreSQL to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions)
    * [ PostgreSQL to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions)
  * Manage heterogeneous migration jobs: 
    * [ Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/manage-migration-jobs)
    * [ Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/manage-migration-jobs)
    * [ SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/manage-migration-jobs)
    * [ SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/manage-migration-jobs)



## July 02, 2026

Change

MySQL version 9.7 support for MySQL homogeneous migrations is being rolled out across all regions. A new announcement will be published when MySQL version 9.7 for MySQL homogeneous migrations with Database Migration Service becomes available.

## June 23, 2026

Announcement

**Note:** MySQL version 9.7 version isn't yet available. For more information, see the release note from July 2nd, 2026. 

Database Migration Service for MySQL homogeneous migrations now supports MySQL version 9.7. For more information, see [ Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/supported-databases).

## May 22, 2026

Feature

Database Migration Service for homogeneous SQL Server migrations now provides dedicated support for Cloud SQL for SQL Server sources. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

For Cloud SQL for SQL Server sources, Database Migration Service automatically exports all required backup files and uploads them to a dedicated Cloud Storage bucket. For more information, see the [ Migration guide for Cloud SQL for SQL Server sources](https://docs.cloud.google.com/database-migration/docs/sqlserver/csql-sql-server-src-guide) in the Database Migration Service homogeneous SQL Server documentation.

## May 12, 2026

Feature

Gemini-powered conversion quality assessments for heterogeneous migrations in Database Migration Service are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information, see [ Convert SQL with Gemini in Database Migration Service](https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms#quality-assessments).

## April 30, 2026

Feature

Database Migration Service for heterogeneous migrations to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL now supports PostgreSQL version 18. For more information, see [ Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/supported-databases).

## April 22, 2026

Feature

You can now use [ quick-start migrations for homogeneous PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations) to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL.

Quick-start migrations are a lightweight continuous migration flow where Database Migration Service can automatically set up everything you need to migrate sources that have a private IP assigned in a VPC network, such as self-managed databases on Compute Engine or Cloud SQL for PostgreSQL instances. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 07, 2026

Feature

You can use the [ Database Migration Service MCP server](https://docs.cloud.google.com/database-migration/docs/use-database-migration-service-mcp) to enable agents and AI applications to view and manage running migration jobs. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 30, 2026

Feature

Database Migration Service for homogeneous MySQL migrations now lets you migrate individual databases from your source. You can select the databases when you [ create a migration job for homogeneous MySQL migrations](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-intro).

## March 18, 2026

Announcement

Database Migration Service for heterogeneous SQL Server migrations now supports failback migration jobs in [Preview](https://cloud.google.com/products#product-launch-stages). Failback migrations let you push CDC updates back to the original SQL Server source from the destination PostgreSQL database after you complete the standard migration. This feature keeps your original source database alive and up to date in case you need to switch your application back to the source SQL Server database. For more information, see the page relevant for your migration scenario:

  * [ Failback migration guide for SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide-failback-migration)
  * [ Failback migration guide for SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/guide-failback-migration)



## February 27, 2026

Feature

Database Migration Service for heterogeneous migrations now supports `RENAME-__`,`MOVE-`, `CASE_HANDLING` and `GENERATE_MISSING_PK` directives to provide improved control over converting Oracle and SQL Server objects to PostgreSQL. For more information, see the page relevant for your migration scenario:

  * [ Supported conversion directives for Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/about-conversion-workspaces#conversion-directives-reference)
  * [ Supported conversion directives for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces#conversion-directives-reference)
  * [ Supported conversion directives for SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#conversion-directives-reference)
  * [ Supported conversion directives for SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/about-conversion-workspaces#conversion-directives-reference)



## November 18, 2025

Feature

Database Migration Service for homogeneous PostgreSQL migrations to Cloud SQL for PostgreSQL now supports PostgreSQL version 18. For more information, see [ Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/supported-databases).

Feature

Database Migration Service now supports the one-time migration type for all heterogeneous migration scenarios. For more information, see the following pages:

  * [ Migration data flow for Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview#data-flow-migration-types)
  * [ Migration data flow for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview#data-flow-migration-types)
  * [ Migration data flow for SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview#data-flow-migration-types)
  * [ Migration data flow for SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview#data-flow-migration-types)



## November 05, 2025

Feature

Database Migration Service for homogeneous MySQL migrations to Cloud SQL for MySQL now supports MySQL version 8.0.43. For more information, see [ Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/supported-databases).

## October 30, 2025

Feature

Database Migration Service now supports Private Service Connect interfaces for source network connectivity in all heterogeneous migration scenarios.

For more information, see the following pages:

  * [ Source connectivity methods for Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source#private-connectivity-psci)
  * [ Source connectivity methods for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source#private-connectivity-psci)
  * [ Source connectivity methods for SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-methods-source#private-connectivity-psci)
  * [ Source connectivity methods for SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-source#private-connectivity-psci)



## September 15, 2025

Announcement

Gemini-powered conversion features for heterogeneous migrations in Database Migration Service are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information, see [Accelerate code and schema conversion with Gemini](https://cloud.google.com/database-migration/docs/convert-sql-with-dms#gemini-conversion).

## September 05, 2025

Feature

Database Migration Service for heterogeneous Oracle and SQL Server migrations now supports table-level observability features. In addition to metrics aggregated for the whole database, you can now monitor the migration progress individually for each table. For more information, see the monitoring pages for your scenario:

  * [Migration job metrics for Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/migration-job-metrics)
  * [Migration job metrics for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/migration-job-metrics)
  * [Migration job metrics for SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/migration-job-metrics)
  * [Migration job metrics for SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/migration-job-metrics)



## August 18, 2025

Feature

Database Migration Service for homogeneous PostgreSQL migrations to AlloyDB for PostgreSQL now supports PostgreSQL version 17. For more information, see [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/supported-databases).

## August 14, 2025

Feature

Database Migration Service now supports Private Service Connect interfaces for network connectivity in homogeneous Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and AlloyDB for PostgreSQL migrations. For more information, see the following pages:

  * [Networking methods in homogeneous Cloud SQL for MySQL migrations](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods)
  * [Networking methods in homogeneous Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods)
  * [Networking methods in homogeneous AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods)



## June 30, 2025

Announcement

Database Migration Service support for heterogeneous SQL Server to PostgreSQL migrations is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information, see:

  * [Database Migration Service for SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)
  * [Database Migration Service for SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



## June 16, 2025

Feature

Heterogeneous Oracle and SQL Server migrations now provide an improved experience with conversion overview dashboards and streamlined conversion issue grouping. To learn more about Database Migration Service conversion workspaces with Gemini-powered conversion features, see [Convert SQL with Database Migration Service ](https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms#conversion-workspaces).

## May 22, 2025

Feature

Database Migration Service now supports MySQL minor version 8.0.42 for homogeneous MySQL migrations. For more information, see [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) in Cloud SQL for MySQL migrations.

## May 08, 2025

Feature

You can now use additional concurrency settings for heterogeneous SQL Server migration jobs with Database Migration Service. This lets you adjust the migration process to better align with your scenario.

For information about creating migration jobs using the new full dump configuration and maximum concurrent connection settings, see:

  * [Create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-migration-job) in the SQL Server to Cloud SQL for PostgreSQL documentation
  * [Create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-migration-job) in the SQL Server to AlloyDB for PostgreSQL documentation



## April 24, 2025

Feature

Database Migration Service for heterogeneous migrations to PostgreSQL now supports migrating to PostgreSQL versions 16 and 17.

  * PostgreSQL versions 16 and 17 are supported for migrations from Oracle and SQL Server to Cloud SQL for PostgreSQL.
  * PostgreSQL version 16 is supported for migrations from Oracle and SQL Server to AlloyDB for PostgreSQL.



For more information, see [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/supported-databases).

## April 09, 2025

Feature

Gemini-powered auto-conversion is now available in [Preview](https://cloud.google.com/products#product-launch-stages) for all heterogeneous migration scenarios. You can use code and schema conversion enhancements automatically provided by Gemini to significantly reduce the time and complexity of your database migrations.

For more information about auto-conversion and other AI conversion features, such as conversion assistant or pattern matching, see [Accelerate code and schema conversion with Gemini](https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms#gemini-conversion).

Announcement

Database Migration Service support for heterogeneous SQL Server to PostgreSQL migrations is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see:

  * [Database Migration Service for SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)
  * [Database Migration Service for SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



## March 14, 2025

Feature

Database Migration Service now supports MySQL minor version 8.0.41 for homogeneous MySQL migrations. For more information, see [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) in Cloud SQL for MySQL migrations.

## February 26, 2025

Feature

Database Migration Service for homogeneous Cloud SQL for PostgreSQL migrations now lets you migrate specific databases from your source instance. You can view metrics, statuses, and errors separately for each database.

For more information about migrating specific databases, see:

  * [Create a migration job to a new destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job)
  * [Create a migration job to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance)
  * [Review a migration job](https://docs.cloud.google.com/database-migration/docs/postgres/review-migration-job)
  * [Manage migration jobs](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions)



## February 14, 2025

Feature

Database Migration Service for homogeneous AlloyDB for PostgreSQL migrations now lets you migrate specific databases from your source instance. You can view metrics, statuses, and errors separately for each database.

For more information about migrating specific databases, see: [Create a migration job to a new destination instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job) and [Create a migration job to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance).

Feature

Database Migration Service for homogeneous Cloud SQL for SQL Server migrations now lets you promote, restart, or view additional metrics for each database individually.

For more information, see: [Migration job metrics](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-metrics) and [Manage migration jobs](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs).

## January 13, 2025

Feature

Database Migration Service now supports Microsoft Azure sources for MySQL and PostgreSQL homogeneous migrations to Cloud SQL. 

For more information, see [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/supported-databases).

## January 09, 2025

Feature

Database Migration Service now supports public IP allowlist network connectivity for all homogeneous and heterogeneous migrations to AlloyDB for PostgreSQL. For more information, see:

  * [Configure IP allowlist connectivity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-ip-allowlists) in the PostgreSQL to AlloyDB for PostgreSQL documentation.
  * [Create destination connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-connection-profiles#create-alloydb-dest-connection-profile) in the Oracle to AlloyDB for PostgreSQL documentation.



## December 24, 2024

Feature

Database Migration Service for homogeneous PostgreSQL migrations to Cloud SQL for PostgreSQL now supports PostgreSQL version 17. For more information, see [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest) in Cloud SQL for PostgreSQL migrations.

## December 12, 2024

Feature

Database Migration Service now supports MySQL minor version 8.0.40 for homogeneous MySQL migrations. For more information, see [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) in Cloud SQL for MySQL migrations.

## November 18, 2024

Feature

Database Migration Service now lets you select if a connection profile is for a source or a destination database, based on your migration scenario. Database Migration Service shows configuration options applicable to your choice.

## November 07, 2024

Feature

Database Migration Service now supports MySQL minor version 8.0.39 for homogeneous MySQL migrations. For more information, see [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) in Cloud SQL for MySQL migrations.

## October 21, 2024

Feature

You can now use additional concurrency settings for heterogeneous Oracle migration jobs with Database Migration Service. This lets you adjust the migration process to better align with your scenario.

For information about creating migration jobs using the new full dump configuration and maximum concurrent connection settings, see:

  * [Create a migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-migration-job) in the Oracle to Cloud SQL for PostgreSQL documentation
  * [Create a migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-migration-job) in the Oracle to AlloyDB for PostgreSQL documentation



## October 10, 2024

Feature

Database Migration Service for homogeneous MySQL to Cloud SQL for MySQL migrations now supports MySQL version 8.4. See [Supported source and destination databases in Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) migrations.

## October 08, 2024

Announcement

Database Migration Service for homogeneous PostgreSQL migrations to Cloud SQL does not automatically enable point-in-time recovery (PITR) for the destination instance when you promote the migration job. You can enable PITR after the migration is complete. 

For more information, see [Promote a migration](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration) and [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations).

## September 24, 2024

Feature

Database Migration Service for homogeneous PostgreSQL migrations to AlloyDB for PostgreSQL now supports PostgreSQL version 16. See [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest) in AlloyDB for PostgreSQL migrations.

Announcement

Database Migration Service support for homogeneous SQL Server to Cloud SQL for SQL Server migrations is now generally available (GA). For more information, see [Database Migration Service for homogeneous SQL Server documentation](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview).

## September 18, 2024

Change

Database Migration Service for homogeneous PostgreSQL migrations to Cloud SQL now automatically enables point-in-time recovery (PITR) for the destination instance when you promote the migration job. Previously, you had to turn on PITR after you promoted an instance. 

For more information, see [Promote a migration](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration) and [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations).

Database Migration Service doesn't automatically enable PITR for homogeneous PostgreSQL migrations to Cloud SQL. For more information, see the release note entry for October 8, 2024.

## August 30, 2024

Feature

Database Migration Service for homogeneous migrations to Cloud SQL for SQL Server now supports differential backup files. For more information, see [Supported types of backup files](https://docs.cloud.google.com/database-migration/docs/sqlserver/supported-backup-files).

## August 13, 2024

Feature

Database Migration Service now supports migrations to MySQL minor version 8.0.37. See [Supported source and destination databases in Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) migrations.

## July 29, 2024

Feature

Database Migration Service support for homogeneous MySQL to Cloud SQL for MySQL migrations with physical backup files created by using the Percona XtraBackup utility is now Generally Available (GA).

For more information, see [Migrate your databases by using a Percona XtraBackup physical file](https://docs.cloud.google.com/database-migration/docs/mysql/migrate-with-physical-xtrabackup).

## July 25, 2024

Feature

Gemini conversion assistant for conversion workspaces is now available in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see:

  * [Convert Oracle code and schema with Gemini assistance for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini)
  * [Convert Oracle code and schema with Gemini assistance for Oracle to CloudSQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini)



## July 08, 2024

Change

Database Migration Service for heterogeneous Oracle migrations can now migrate tables without primary or unique constraints that have more than 500 million rows. The previous maximum row limitation for such tables is no longer in place. For more information on known limitations, see:

  * [Known limitations for Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/known-limitations)
  * [Known limitations for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/known-limitations)



## July 03, 2024

Feature

Database Migration Service for heterogeneous Oracle migrations to AlloyDB for PostgreSQL now supports network connectivity with Private Service Connect for AlloyDB clusters with Private Service Connect enabled. For more information, see [Configure Private Service Connect](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-private-service-connect).

## June 17, 2024

Feature

In Database Migration Service for heterogeneous Oracle migrations, you can now use the **Promote** action directly on the migration job details page to finalize your migration process. For more information, see [Finalize a migration in Oracle to AlloyDB](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/finalize-migration) and [Finalize a migration in Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/finalize-migration).

## June 10, 2024

Feature

Database Migration Service for homogeneous PostgreSQL migrations to Cloud SQL for PostgreSQL now supports PostgreSQL version 16. See [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest) in Cloud SQL for PostgreSQL migrations.

## June 06, 2024

Feature

Database Migration Service for heterogeneous Oracle migrations now features additional logging information that can help you better monitor the health and progress of your migration jobs. For more information, see [Logging for Oracle to AlloyDB](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/logging), and [Logging for Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/logging).

Feature

Database Migration Service for heterogeneous Oracle migrations can now skip foreign keys and triggers, so dropping them from the destination database is no longer required. For more information, see [Considerations for foreign keys and triggers for Oracle to AlloyDB](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-your-destination-postgresql-database#foreign-keys-triggers-considerations) and [Considerations for foreign keys and triggers for Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-your-destination-postgresql-database#foreign-keys-triggers-considerations).

## May 22, 2024

Feature

Database Migration Service now supports migrations to MySQL minor version 8.0.36. See [Supported source and destination databases in Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) migrations.

## April 19, 2024

Feature

Database Migration Service for homogeneous migrations to Cloud SQL for MySQL and homogeneous migrations to Cloud SQL for PostgreSQL now supports migrations to existing destination instances that have read replicas enabled.

For more information, see:

  * [Configure source database for MySQL to Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database)
  * [Configure source database for PostgreSQL to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database)



## April 09, 2024

Announcement

Database Migration Service support for code conversion with Gemini assistance is now available in preview. For more information, see:

  * [Code conversion with Gemini assistance for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini)
  * [Code conversion with Gemini assistance for Oracle to CloudSQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini)



Announcement

Database Migration service support for homogeneous SQL Server migrations to Cloud SQL for SQL Server is now available in preview. For more information, see [Database Migration Service for SQL Server](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview).

Announcement

Database Migration Service support for Oracle to AlloyDB for PostgreSQL migrations is now generally available. For more information, see [Database Migration Service for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/migration-src-and-dest).

Announcement

Database Migration Service conversion workspaces for heterogeneous migrations are now generally available (GA). For more information, see:

  * [Conversion workspaces for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-ws)
  * [Conversion workspaces for Oracle to CloudSQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/about-conversion-ws)



## April 05, 2024

Feature

Database Migration Service now supports physical backup files created by using the Percona XtraBackup utility for homogeneous MySQL to Cloud SQL for MySQL migrations. For more information, see [Migrate your databases by using a Percona XtraBackup physical file](https://docs.cloud.google.com/database-migration/docs/mysql/migrate-with-physical-xtrabackup).

## March 29, 2024

Feature

Database Migration Service now supports faster migrations of large PostgreSQL databases to AlloyDB for PostgreSQL.

For information about creating migration jobs using the high-performance parallelism settings, see [Create a migration job to a new destination instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job#specify-source-connection-profile-info) and [Create a migration job to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance#specify-source-connection-profile-info).

## March 27, 2024

Feature

A new migration job status called **Running with errors** is available for heterogeneous Oracle migrations in Database Migration Service. This status represents migration jobs that encounter errors, but continue replicating data for unaffected objects and attempt to retry faulty operations.

For more information, see [Migration job statuses for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/review-migration-job#migration_job_statuses) and [Migration job statuses for Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/review-migration-job#migration_job_statuses).

Feature

Database Migration Service now supports faster migrations of large PostgreSQL databases to Cloud SQL for PostgreSQL.

For information about creating migration jobs using the high-performance parallelism settings, see [Create a migration job to a new destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#specify-source-connection-profile-info) and [Create a migration job to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance#specify-source-connection-profile-info).

## January 17, 2024

Announcement

Database Migration Service support for Oracle to AlloyDB for PostgreSQL migrations is now available in Preview. For more information, see [Database Migration Service for Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/migration-src-and-dest) documentation.

## January 11, 2024

Feature

Database Migration Service for Oracle to Cloud SQL for PostgreSQL and Oracle to AlloyDB for PostgreSQL migrations now support row sizes of up to 30 MB. For more information, see [Known limitations in Oracle to Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/known-limitations) and [Known limitations in Oracle to AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/known-limitations).

## January 07, 2024

Feature

Database Migration Service now supports MySQL minor version 8.0.35. See [Supported source and destination databases in Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) migrations.

## December 14, 2023

Feature

You can now migrate MySQL and PostgreSQL databases to Cloud SQL instances or AlloyDB clusters created outside Database Migration Service. See [Migration jobs overview](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-intro).

## December 13, 2023

Feature

Database Migration Service now supports selecting PostgreSQL version 15 when migrating to AlloyDB for PostgreSQL. See [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest) in AlloyDB for PostgreSQL migrations.

## December 11, 2023

Feature

Database Migration Service now supports MySQL minor versions. See [Supported source and destination databases](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) in Cloud SQL for MySQL migrations.

## November 29, 2023

Change

Database Migration Service supports creating [Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job) and [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job) instances with customer-managed encryption keys (CMEK) enabled.

## November 10, 2023

Feature

Database Migration Service now supports data cache in Cloud SQL for PostgreSQL Enterprise Plus edition instance creation.

You can enable data cache in the destination database when you [create a migration job](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#dest). To learn more about data cache in Cloud SQL for PostgreSQL, see [Data cache overview](https://docs.cloud.google.com/sql/docs/postgres/data-cache).

## September 18, 2023

Feature

Database Migration Service now supports customer-managed encryption keys (CMEK) that are externally managed with Cloud External Key Manager. For more details on CMEK support for each migration scenario, see [CMEK integrations](https://docs.cloud.google.com/kms/docs/compatible-services#cmek_integrations).

## August 30, 2023

Feature

Integrated code and schema conversion for Oracle to Cloud SQL for PostgreSQL migrations is now available in Preview. With this feature, Database Migration Service [conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/about-conversion-ws) provide an inline editor to help make your schema conversions simple and seamless.

Announcement

Database Migration Service support for Oracle to Cloud SQL for PostgreSQL migrations is now generally available (GA). For more information, see [Database Migration Service for Oracle to PostgreSQL documentation](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql).

## July 27, 2023

Feature

Database Migration Service now supports faster migrations of large MySQL databases to Cloud SQL for MySQL. For information about creating migration jobs using the high-performance dump option, see [Create a migration job](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job#specify-source-connection-profile-info).

## June 20, 2023

Announcement

Database Migration Service support for PostgreSQL to AlloyDB for PostgreSQL migrations is now generally available (GA).

## May 02, 2023

Feature

Database Migration Service now supports faster migrations from PostgreSQL source databases to a destination Cloud SQL for PostgreSQL instance. The feature improves the performance of migrating data and constraints (including primary keys, foreign keys, and indexes).

## April 17, 2023

Feature

Database Migration Service now supports Oracle multi-tenant (CDB/PDB) architecture. For information about configuring pluggable databases for use with Database Migration Service, click [here](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-your-source-oracle-database#oraclepluggabledatabase).

## April 06, 2023

Feature

You can now set up cascading read replicas after you migrate data to a Cloud SQL destination instance using Database Migration Service. To find out how to set up cascading read replicas for a Cloud SQL for MySQL instance, click [here](https://docs.cloud.google.com/database-migration/docs/mysql/set-up-cascading-replica). To find out how to set up cascading read replicas for a Cloud SQL for PostgreSQL instance, click [here](https://docs.cloud.google.com/database-migration/docs/postgres/set-up-cascading-replica).

## January 19, 2023

Feature

Database Migration Service support for migrating Oracle workloads into Cloud SQL for PostgreSQL is now in Public Preview. Click [here](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql) to access the documentation.

## December 13, 2022

Feature

Database Migration Service now supports high availability (HA) instances for MySQL and PostgreSQL database migrations. To find out how to configure connectivity for a high availability instance, click [here](https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity-ip-allowlists). To learn how to configure a high availability instance when creating a migration job, click [here](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job#dest).

## September 15, 2022

Feature

Database Migration Service now supports migrating PostgreSQL workloads into AlloyDB for PostgreSQL. Click [here](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb) to access the documentation.

## June 24, 2022

Feature

Database Migration Service now supports the migration of tables without primary keys in PostgreSQL. For tables that don't have primary keys, Database Migration Service supports the migration of the **initial snapshot and`INSERT` statements during the change data capture (CDC) phase**. You should migrate `UPDATE` and `DELETE` statements manually. Click [here](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database) to access the documentation.

## April 04, 2022

Feature

Database Migration Service now supports migrating Oracle workloads into Cloud SQL for PostgreSQL. Click [here](https://docs.cloud.google.com/database-migration/docs) to access the documentation.

## March 16, 2022

Feature

Database Migration Service now supports version 14 of Cloud SQL for PostgreSQL. Click [here](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest) to access the documentation.

## March 10, 2022

Feature

Database Migration Service now supports adding dump flags for data dump customizations to migration jobs for Cloud SQL for MySQL instances. Click [here](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job) to access the documentation.

## December 16, 2021

Feature

Database Migration Service now supports creating [Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job), [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job), and Cloud SQL for SQL Server instances with customer-managed encryption keys (CMEK) enabled. Click [here](https://docs.cloud.google.com/database-migration/docs) to access the documentation. This note is incorrect. See entry for November 29, 2023.

## July 29, 2021

Feature

Database Migration Service now supports Cloud SQL for PostgreSQL as a source for PostgreSQL migrations. Click [here](https://docs.cloud.google.com/database-migration/docs) to access the documentation.

## March 31, 2021

Announcement

The GA version of Database Migration Service is now available for PostgreSQL. This version makes it easier for you to "lift and shift" your MySQL and PostgreSQL workloads into Cloud SQL. Click [here](https://docs.cloud.google.com/database-migration/docs) to access the documentation.

## November 10, 2020

Announcement

The Public Preview version of Database Migration Service is now available for MySQL. This version makes it easier for you to "lift and shift" your MySQL workloads into Cloud SQL. Click [here](https://docs.cloud.google.com/database-migration/docs) to access the documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
