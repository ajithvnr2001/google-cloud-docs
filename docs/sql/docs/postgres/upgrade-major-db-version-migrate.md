---
url: https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-migrate/
title: Upgrade the database major version by migrating data \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:30.609773+00:00
---

# Upgrade the database major version by migrating data  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Upgrade the database major version by migrating data Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-migrate "View this page for the SQL Server database engine")

This page describes how to migrate your data to an instance running a later version of PostgreSQL. Before proceeding with this method, consider [upgrading the database major version in-place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace).

There are two ways to upgrade the database major version of your Cloud SQL for PostgreSQL instance by migrating your data.

  * **Option 1**. Use the [Database Migration Service (DMS)](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database). DMS supports migrating from a Cloud SQL for PostgreSQL instance. You can also use it to upgrade your database version.
  * **Option 2**. Move your data from one version of PostgreSQL to another by _exporting_ data from the current instance and _importing_ that data into a new instance running the later version of PostgreSQL. This process involves downtime; you put the current instance into read-only mode before starting the export. 



The rest of this page discusses the second option.

## Plan a major version upgrade

  1. Choose a target major version.

See the [list of versions that Cloud SQL supports](https://docs.cloud.google.com/sql/docs/postgres/db-versions).

  2. Consider the features offered in each PostgreSQL version and address incompatibilities.

New major versions introduce incompatible changes that might require you to modify the application code, the schema, or the database settings before you can upgrade your database instance. Review the release notes of your target major version to determine the incompatibilities that you need to address. If you're skipping major versions, address the incompatibilities listed for each version that you're skipping.

     * [PostgreSQL 17](https://www.postgresql.org/docs/17/release-17.html)
     * [PostgreSQL 16](https://www.postgresql.org/docs/16/release-16.html)
     * [PostgreSQL 15](https://www.postgresql.org/docs/15/release-15.html)
     * [PostgreSQL 14](https://www.postgresql.org/docs/14/static/release-14.html)
     * [PostgreSQL 13](https://www.postgresql.org/docs/13/static/release-13.html)
     * [PostgreSQL 12](https://www.postgresql.org/docs/12/static/release-12.html)
     * [PostgreSQL 11](https://www.postgresql.org/docs/11/static/release-11.html)
     * [PostgreSQL 10](https://www.postgresql.org/docs/10/static/release-10.html)
  3. Test the upgrade with a dry run.

Perform a dry run of the end-to-end upgrade process with a test instance before you upgrade the production database. You might want to test the upgrade using a [clone](https://docs.cloud.google.com/sql/docs/postgres/clone-instance) instead of your production database to avoid any performance impact from the export on your production workload.

In addition to validating that the upgrade completes successfully, run tests to understand the expected downtime of the upgrade, confirm your upgrade workflow, and ensure that the application behaves as expected on the upgraded database. If you haven't enabled [automatic storage increases](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen), take note of the disk storage used by the upgraded dry run instance to determine whether you need to increase the storage capacity for the production instance before upgrading.

  4. Decide when you want to upgrade.

**Note:** Upgrades require the instance to become unavailable for a period of time. Be sure to schedule your upgrade when database activity is low.



## Migrate your data

Migrating entails using the [`pg_dump`](https://www.postgresql.org/docs/14/static/app-pgdump.html) command to [export the data](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp#export) from the source instance and the [`pg_restore`](https://www.postgresql.org/docs/14/static/app-pgrestore.html) command to [import the data](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp#import) into the target instance.

To migrate your data to a Cloud SQL instance running a more recent database version, follow these steps:

  1. Create the target instance with the desired PostgreSQL version.

Make sure the target instance has:

     * Sufficient storage to hold all of the current instance's data.
     * The same authorized networks as the current instance. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/configure-ip).
     * The same user accounts, with the same PostgreSQL privileges and passwords.

For more information, see [Creating an instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

  2. Confirm that you can [connect to the new instance](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip) with your local PostgreSQL tools and update them, if necessary.

  3. Export the current instance's data to a PostgreSQL dump file, following the instructions in [Exporting data for Import into Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp#external-server).

Do _not_ export the `postgres` system database. The `postgres` database is the default database you connect to before you have created any other databases. Once you create another database, switch to it in order to create tables and insert data. Don't use the `postgres` database for your application's data.

  4. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) if needed, and upload your SQL dump file to the bucket.

  5. Import the data to the target instance, following the instructions in [Importing PostgreSQL databases from Cloud Storage](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp#import_data_using_pg_restore_).

  6. Optional. After completing the upgrade process, set up replication between the source and target instances using `pglogical` to update the target with all changes that have occurred since the initial dump was started. Once the two instances are in sync, you can promote the target instance.

For information about using `pglogical` to implement continuous replication, see [Configure your source](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database).

  7. Update your applications to connect to the new instance.

  8. When you're confident that your new instance is operating successfully, delete the old instance.




## What's next

  * Learn about [importing and exporting data](https://docs.cloud.google.com/sql/docs/postgres/import-export).
  * Learn about [options for connecting to an instance](https://docs.cloud.google.com/sql/docs/postgres/external-connection-methods).
  * Learn more about [setting PostgreSQL flags](https://docs.cloud.google.com/sql/docs/postgres/flags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
