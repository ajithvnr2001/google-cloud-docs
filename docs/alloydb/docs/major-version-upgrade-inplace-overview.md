---
url: https://docs.cloud.google.com/alloydb/docs/major-version-upgrade-inplace-overview/
title: Database in-place major version upgrade overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:58.097910+00:00
---

# Database in-place major version upgrade overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/major-version-upgrade-inplace-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Database in-place major version upgrade overview Stay organized with collections  Save and categorize content based on your preferences. 

To adopt new PostgreSQL features, performance improvements, and security enhancements without migrating data or changing application connection strings, you can perform an in-place major version upgrade on your AlloyDB for PostgreSQL cluster.

The PostgreSQL community periodically releases [new major versions](https://www.postgresql.org/support/versioning/) that contain new features, performance improvements, and security enhancements. After PostgreSQL releases a new major version, AlloyDB [adds support for the compatible version](https://docs.cloud.google.com/alloydb/docs/db-version-policies#support-table). To keep your database up to date, you can upgrade your AlloyDB cluster by upgrading to a higher major version. You can upgrade your cluster by using this in-place upgrade feature or by [migrating your data](https://docs.cloud.google.com/alloydb/docs/cluster-upgrade) to a new AlloyDB cluster.

For more information, see [Database version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies).

In-place major version upgrades are an efficient way to upgrade your cluster's major version for the following reasons:

  * AlloyDB retains cluster and instance details and database settings like the instance name, IP address, and database flags after the upgrade.
  * You don't need to change application connection strings.
  * All the cluster instances (primary and read pool) are upgraded as part of the same operation.

**Note:** To verify the upgrade process and to check for incompatibilities, we recommend that you verify the upgrade process on a cloned cluster before you upgrade your actual cluster.

Additionally, role memberships with non-existent grantors (orphaned memberships) aren't preserved. If any cluster contains orphaned memberships in the `pg_auth_members` catalog, these role memberships are lost after the upgrade. For more information, see [Prepare the cluster for a major version upgrade](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version#prepare-upgrade).

## In-place major version upgrade workflow

When you start an upgrade on your cluster, AlloyDB performs the following actions:

  1. Runs pre-upgrade checks to find incompatibilities that can impact the upgrade.
  2. Prepares for the major version upgrade, which includes creating an internal clone of the cluster.
  3. Makes the primary instance unavailable. Downtime starts. Reads can still be done through read pools.
  4. Initiates a pre-upgrade backup.
  5. Upgrades the primary instance.
  6. Makes the read pool instances unavailable.
  7. Makes the primary instance available. Downtime ends.
  8. Initiates a post-upgrade backup.
  9. Upgrades read pool instances.

**Note:** When you perform an in-place major version upgrade, version-specific default values of the database flags might change. For more information, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

After the pre-upgrade checks pass, your cluster is cloned to an internal cluster in the same project. The backup and restore needed to clone the cluster takes approximately 10 minutes per terabyte of data.

During the clone operation, you can continue to use your original cluster. After the clone operation is complete, the upgrade process starts. The primary instance is unavailable for both reads and writes until the primary instance is upgraded. Expected downtime is typically 20 minutes to one hour, and primarily depends on your database schema and the number of objects.

**Note:** You can continue to use the read pool instances while the primary instance is being upgraded.

After the primary instance is upgraded, read pool instances become unavailable. Upgrades are attempted on all read pool instances concurrently. Downtime is expected to last approximately 20 minutes.

If the major version upgrade fails at any step before the primary instance is upgraded, AlloyDB automatically rolls back all changes.

After the primary instance is upgraded, the cluster version is upgraded to the target version and no rollbacks are triggered for any failure after this point. For example, AlloyDB doesn't roll back the cluster if one or more read pool instance upgrades fail. In these situations, contact [Google Cloud Support](https://cloud.google.com/support).

The following table gives an approximate estimation of the time taken for the upgrade to complete for clusters of different database sizes:

Database Size | Pre-upgrade (no downtime) | Primary downtime | Read pool downtime | Total duration  
---|---|---|---|---  
100 GB | ~15 minutes | ~20 minutes | ~20 minutes | ~1 hour  
1 TB | ~30 minutes | ~20 minutes | ~20 minutes | ~1 hour 15 minutes  
4 TB | ~1 hour | ~20 minutes | ~20 minutes | ~1 hour 45 minutes  
16 TB | ~3 hours | ~20 minutes | ~20 minutes | ~3 hours 45 minutes  
32 TB | ~5 hours 30 minutes | ~20 minutes | ~20 minutes | ~6 hours 15 minutes  
64 TB | ~11 hours | ~20 minutes | ~20 minutes | ~12 hours  
128 TB | ~21 hours 30 minutes | ~20 minutes | ~20 minutes | ~22 hours 15 minutes  
  
For more information, see [Upgrade a database in-place major version](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version).

### Upgrade status

You can [monitor the status of an in-place database major version upgrade](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version#monitor-upgrade) operation while it's in progress.

The upgrade process includes the following stages:

  * `ALLOYDB_PRECHECK`
  * `PG_UPGRADE_CHECK`
  * `PREPARE_FOR_UPGRADE`
  * `PRIMARY_INSTANCE_UPGRADE`
  * `READ_POOL_INSTANCES_UPGRADE`
  * `ROLLBACK`(only in case of failure before read pool upgrades)
  * `CLEANUP`



The possible states of these stages include the following:

  * `NOT_STARTED`
  * `IN_PROGRESS`
  * `SUCCESS`
  * `FAILED`
  * `CANCEL_IN_PROGRESS`
  * `CANCELLED`



### Upgrade cancellations

You can [cancel the upgrade operation](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version#cancel-major-version-upgrade) until a certain point during the primary instance upgrade. Once that point is crossed, you can't cancel an upgrade.

In the Google Cloud console, the operation isn't cancelable if the **Cancel upgrade** button is grayed out. Using the Google Cloud CLI or the REST API, you can determine if you can [cancel the upgrade](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version#cancel-major-version-upgrade) by checking `upgradeClusterStatus` in the upgrade status:

  * If `cancellable` is `true`, you can cancel the upgrade.
  * If `cancellable` is `false` or is missing in the status, you can't cancel the upgrade.



## Automatic pre-upgrade and post-upgrade backups

When you perform a major version upgrade, AlloyDB automatically creates the following continuous backups, where `XX` is the source major version and `YY` is the target major version.

  * The _pre-upgrade backup_ is created immediately before the upgrade starts. This backup is named using the format `pre-upgrade-bkp-pgXX-pgYY-<uuid>`. You can use this backup to restore to the pre-upgrade state. Note that restore is not an in-place operation and that it creates a new cluster. 
  * The _post-upgrade backup_ is created after the primary instance is upgraded. This backup is named using the format `post-upgrade-bkp-pgXX-pgYY-<uuid>`.



A _continuous backup_ is incremental, which means that the backup stores only the data that changed relative to the previous continuous backup. This approach reduces the size and cost (in resources) of the backup, and speeds up the backup creation process. For more information, see [Data backup and recovery overview](https://docs.cloud.google.com/alloydb/docs/backup/overview).

When you view your list of backups, the upgrade backups are listed with type `CONTINUOUS`. For more information, see [View a list of backups](https://docs.cloud.google.com/alloydb/docs/backup/list).

Performing point-in-time recovery (PITR) requires that a backup of a version is available. Recovery isn't available on the upgraded cluster until the post-upgrade backup, or another backup that is kicked off after the primary instance is upgraded, completes.

## What's next

  * [Upgrade a database in-place major version](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
