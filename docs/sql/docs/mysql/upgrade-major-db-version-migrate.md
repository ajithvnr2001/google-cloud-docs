---
url: https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate/
title: Upgrade the database major version by migrating data \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:27.098851+00:00
---

# Upgrade the database major version by migrating data  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Upgrade the database major version by migrating data Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-migrate "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-migrate "View this page for the SQL Server database engine")

This page describes how to migrate your data to an instance running a later version of MySQL. Before proceeding with this method, consider [upgrading the database major version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace).

**Note:** To upgrade the minor version for MySQL 8.0, see [Upgrade the MySQL minor version for an instance](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

There are two ways to upgrade the database major version of your Cloud SQL for MySQL instance by migrating your data.

  * **Option 1**. Use the [Database Migration Service (DMS)](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database). DMS supports migrating from a Cloud SQL MySQL instance. You can also use it to upgrade your MySQL version.
  * **Option 2**. Move your data from one version of MySQL to another by _exporting_ data from the current instance and _importing_ that data into a new instance running the later version of MySQL. This process involves downtime; you put the current instance into read-only mode before starting the export. 



This page discusses the second option.

## Plan a major version upgrade

  1. Choose a target major version.

See the [list of versions that Cloud SQL supports](https://docs.cloud.google.com/sql/docs/mysql/db-versions).

  2. Consider the features offered in each MySQL version and address incompatibilities.

New major versions introduce incompatible changes that might require you to modify the application code, the schema, or the database settings before you can upgrade your database instance. Review the release notes of your target major version to determine the incompatibilities that you need to address. If you're skipping major versions, address the incompatibilities listed for each version that you're skipping.

     * [MySQL 9.7](https://dev.mysql.com/doc/refman/9.7/en/upgrading-from-previous-series.html)
     * [MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/upgrading-from-previous-series.html)
     * [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html)
     * [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/upgrading-from-previous-series.html)
  3. If you are upgrading from MySQL 5.7 to MySQL 8.0, then check for user grant changes in MySQL 8.0.

Cloud SQL for MySQL version 8.0 uses a new system flag called `partial_revokes`, which is set to `ON` by default. Unlike MySQL 5.7, this flag removes the ability to use wildcard characters in database `GRANT` commands. To ensure database users have access to the correct database schemas, modify database user privileges before upgrading to MySQL 8.0. Update the user's privileges to use the full name of the required database schemas instead of using wildcard characters.

For more information on how this flag works in MySQL 8.0, see [partial_revokes in MySQL 8.0](https://docs.cloud.google.com/sql/docs/mysql/flags#partial-revokes).

  4. Test the upgrade with a dry run.

Perform a dry run of the end-to-end upgrade process with a test instance before you upgrade the production database. You might want to test the upgrade using a [clone](https://docs.cloud.google.com/sql/docs/mysql/clone-instance) instead of your production database to avoid any performance impact from the export on your production workload.

In addition to validating that the upgrade completes successfully, run tests to ensure that the application behaves as expected on the upgraded database. If you haven't enabled [automatic storage increases](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen), take note of the disk storage used by the upgraded dry run instance to determine whether you need to increase the storage capacity for the production instance before upgrading.

  5. Decide when you want to upgrade.

**Note:** Upgrades require the instance to become unavailable for a period of time. Be sure to schedule your upgrade when database activity is low.



## Migrate your data

To migrate your data to a Cloud SQL instance running a more recent database version, follow these steps:

  1. Create the instance with the target database major version.

Make sure the target instance has:

     * Sufficient storage to hold all of the current instance's data.
     * The same authorized networks as the current instance. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/configure-ip).
     * The same user accounts, with the same MySQL privileges and passwords.

For more information, see [Creating an instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

  2. Confirm that you can [connect to the new instance](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip) with your local MySQL tools and update them if necessary.

  3. Put your current Cloud SQL instance into read-only mode by setting the `read_only` database flag to `On`.

For information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).

  4. Export the current instance's data to a SQL dump file, following the instructions in [Export data for import into Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql).

Do _not_ export the `mysql` system database.

  5. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) if needed, and upload your SQL dump file to the bucket.

  6. Import the data to the target instance, following the instructions in [Import MySQL databases from Cloud Storage](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql).

  7. Optional. After completing the upgrade process, set up replication between the source and target instances by using an external server to update the target with all changes that have occurred since the initial dump was started. Once the two instances are in sync, you can promote the target instance.

For information about using an external server to implement continuous replication, see [Replicating from an external server](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external_v1).

  8. Update your applications to connect to the new instance.

  9. When you're confident that your new instance is operating successfully, delete the old instance.




## What's next

  * Learn about [Changes affecting upgrades to MySQL 9.7](https://dev.mysql.com/doc/refman/9.7/en/upgrading-from-previous-series.html).
  * Learn about [Changes affecting upgrades to MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/upgrading-from-previous-series.html).
  * Learn about [Changes affecting upgrades to MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html).
  * Learn about [Changes affecting upgrades to MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/upgrading-from-previous-series.html).
  * Learn about the [Database Migration Service](https://docs.cloud.google.com/database-migration/docs).
  * Learn about [importing and exporting data](https://docs.cloud.google.com/sql/docs/mysql/import-export).
  * Learn about [options for connecting to an instance](https://docs.cloud.google.com/sql/docs/mysql/external-connection-methods).
  * Learn about [setting MySQL flags](https://docs.cloud.google.com/sql/docs/mysql/flags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
