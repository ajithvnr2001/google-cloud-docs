---
url: https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-migrate/
title: Upgrade the database major version by migrating data \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:27.078539+00:00
---

# Upgrade the database major version by migrating data  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Upgrade the database major version by migrating data Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-migrate "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to migrate your data to an instance running a later version of SQL Server. Before proceeding with this method, consider [upgrading the database major version in-place](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-inplace).

## Plan a major version upgrade

  1. Choose a target major version and edition.

See the [list of versions that Cloud SQL supports](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions).

  2. Consider the features offered in each SQL Server version and address incompatibilities.

New major versions introduce incompatible changes that might require you to modify the application code, the schema, or the database settings before you can upgrade your database instance. Review the release notes of your target major version to determine the incompatibilities that you need to address. If you're skipping major versions, address the incompatibilities listed for each version that you're skipping.

     * [SQL Server 2022](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?view=sql-server-ver16)
     * [SQL Server 2019](https://docs.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-ver15?view=sql-server-ver15)
     * [SQL Server 2017](https://docs.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2017?view=sql-server-ver15)
  3. Test the upgrade with a dry run.

Perform a dry run of the end-to-end upgrade process with a test instance before you upgrade the production database. You might want to test the upgrade using a [clone](https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance) instead of your production database to avoid any performance impact from the export on your production workload.

In addition to validating that the upgrade completes successfully, run tests to understand the expected downtime of the upgrade, confirm your upgrade workflow, and ensure that the application behaves as expected on the upgraded database. If you haven't enabled [automatic storage increases](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen), take note of the disk storage used by the upgraded dry run instance to determine whether you need to increase the storage capacity for the production instance before upgrading.

  4. Decide when you want to upgrade.

**Note:** Upgrades require the instance to become unavailable for a period of time. Be sure to schedule your upgrade when database activity is low.



## Migrate your data

Migrating entails [exporting the data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#export_data_to_a_bak_file) from the source instance to a BAK file and [importing the data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#import_data_from_a_bak_file) into the target instance.

To migrate your data to a Cloud SQL instance running a more recent database version, follow these steps:

  1. Create the target instance with the desired SQL Server version.

Make sure the target instance has:

     * Sufficient storage to hold all of the current instance's data.
     * The same authorized networks as the current instance. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip).
     * The same user accounts, with the same SQL Server privileges and passwords.

For more information, see [Creating an instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

  2. Confirm that you can [connect to the new instance](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip) with your local SQL Server tools and update them, if necessary.

  3. Export the current instance's data to a SQL Server BAK file by following the instructions in [Export data to a BAK file](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#export_data_to_a_bak_file).

Do _not_ export the `sqlserver` system database. The `sqlserver` database is the default database you connect to before you create any other databases. After you create another database, switch to the new database to create tables and insert data. Don't use the `sqlserver` database for your application's data.

  4. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) if needed, and upload your BAK file to the bucket.

  5. Import the data to the target instance by following the instructions in [Import from a BAK file](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#import_data_from_a_bak_file).

  6. Update your applications to connect to the new instance.

  7. Upgrade the [database compatibility level](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-inplace#db-compat).

  8. When you're confident that your new instance is operating successfully, delete the old instance.




## What's next

  * Learn about [importing and exporting data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export).
  * Learn about [options for connecting to an instance](https://docs.cloud.google.com/sql/docs/sqlserver/external-connection-methods).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
