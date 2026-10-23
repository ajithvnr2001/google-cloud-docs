---
url: https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore/
title: Restore an instance overview \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:09.994648+00:00
---

# Restore an instance overview  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Restore an instance overview Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore "View this page for the SQL Server database engine")

Cloud SQL lets you restore your instances from a backup, or by performing point-in-time recovery (PITR). This lets you recover an instance to a specific period or time by either restoring the backup to an existing instance, or restoring the backup to a new instance. To restore, you can use the backup of a live or deleted instance. The restore operation takes the source instance's settings, databases, and users, and sets them in the target instance you choose.

When you restore to a new instance, the target instance can be in a different region or project from the source instance. The target instance can also use a different number of cores or amount of memory than the source instance.

Cloud SQL always sets the storage capacity of the target instance to the maximum value of the size of both the configured disk and the backup disk. The backup disk is the size of the disk when the backup is taken.

When performing a restore on an instance, consider the following:

  * The restore operation overwrites all data on the target instance.
  * The flags from the source instance aren't restored. Any flags previously set on the target instance are retained after the restore.
  * The target instance is unavailable for connections during the restore operation; existing connections are lost.
  * If you are restoring to an instance with read replicas, then you must delete all replicas and recreate them after the restore operation completes.
  * The restore operation restarts the instance.
  * After you restore from a backup, the target instance's backup configurations are set to default values. If your source instance had custom backup configurations or was using enhanced backups, then you'll need to update the backup configurations after restore is complete.



## Restore using a backup

Cloud SQL lets you restore an instance using a backup. You can use a backup from a live or deleted instance, and use it to restore to a new or existing instance. You can use [any available backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#backup_request_types) to restore the instance. To learn more about how backups work at Cloud SQL, see [Backups overview](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups).

When you restore an instance using a backup, you can do the following:

  * Restore to a new instance
  * Restore to an existing instance
  * Restore to an instance in another project or region



In the event of an outage, you can still retrieve a [list of backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backing-up#backuplist) in a particular project to restore from.

To restore your instance using a backup, see [Restore an instance using a backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring).

## Restore a CMEK-enabled instance using enhanced backups

When you use CMEK-enabled instances with enhanced backups, your backups are protected by the same CMEK as the instance. This can be an important part of your backup plan for instances that require CMEK encryption because it maintains your CMEK-encrypted backups in a separate project where they can be successfully restored even if your original workload project is compromised or deleted.

When you restore an enhanced backup of a CMEK-enabled instance into a new instance, you can choose any of the following encryption options for the new instance:

  * Use the same Cloud KMS key as the original instance. This is the default behavior.
  * Select a different Cloud KMS key for the target instance. To select a different key, set the `--disk-encryption-key` flag in the restore command.
  * Revert to Google-owned and Google-managed encryption keys for the target instance. To use GMEK, set the `--clear-disk-encryption` flag in the restore command.



## Point-in-time recovery (PITR)

PITR lets you restore your instance to a specific time of the database. For example, if an error causes a loss of data, then you can recover a database to its state before the error occurred. Unlike restore using a backup, PITR always create a new instance. You can't perform a PITR to an existing instance. The new instance inherits the settings of the source instance, similar to when you [create a clone](https://docs.cloud.google.com/sql/docs/postgres/clone-instance).

If you create a Cloud SQL Enterprise Plus edition instance, then PITR is enabled by default. You have to manually [disable the feature](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/configure-pitr#disablingpitr) if you don't want it enabled.

If you create a Cloud SQL Enterprise edition instance in the Google Cloud console, then PITR is enabled by default. Otherwise, if you create the instance by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or the Cloud SQL Admin API, then PITR is disabled by default. To enable PITR for these instances, you have to manually enable it.

**Note:** To speed up instance creation when PITR is enabled, Cloud SQL uses an initial [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) for PITR instead of a [standard backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#backup-options). This snapshot is later converted to a standard backup in the background to support restore operations. 

For step-by-step instructions for performing PITR, see [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr).

### Log storage for PITR

PITR uses [write-ahead logging (WAL)](https://www.postgresql.org/docs/current/wal-intro.html) to archive logs. When you restore an existing instance using a backup, these archive logs are deleted and won't be available to perform a PITR. Only new logs generated after the restore is complete can be used for PITR.

On January 9, 2023 , we launched storing transaction logs for PITR in [Cloud Storage](https://docs.cloud.google.com/storage/docs). Since this launch, the following conditions apply:

  * All Cloud SQL Enterprise Plus edition instances store their write-ahead logs used for PITR in Cloud Storage. Only Cloud SQL Enterprise Plus edition instances that you upgraded from Cloud SQL Enterprise edition before April 1, 2024 and had PITR enabled before January 9, 2023 continue to store their logs for PITR _on disk_.

  * Cloud SQL Enterprise edition instances created with PITR enabled before January 9, 2023 continue to store their logs for PITR _on disk_.

**Note:** For instances that were created before January 9, 2023 , Cloud SQL switches the location of the transaction logs used for PITR automatically for you. You can use [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API to [check where transaction logs are stored for your instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#check-log-storage-location).
  * If you upgrade a Cloud SQL Enterprise edition instance after January 9, 2023 that stores transaction logs for PITR on disk to Cloud SQL Enterprise Plus edition, then the upgrade process switches the storage location of the transaction logs used for PITR to Cloud Storage for you. For more information, see [Upgrade an instance to Cloud SQL Enterprise Plus edition by using in-place upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).

  * All Cloud SQL Enterprise edition instances that you create with PITR enabled after January 9, 2023 store logs used for PITR in Cloud Storage.




If your instance uses Cloud Storage to store write-ahead logs, then the logs are stored in the same region as the primary instance. These logs are stored for up to 35 days for Cloud SQL Enterprise Plus edition and 7 days for Cloud SQL Enterprise edition and generate no additional cost per instance.

For more information about how to check the storage location of the transaction logs used for PITR, see [check where transaction logs are stored for your instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#check-log-storage-location).

For instances that store write-ahead logs only on disk, you can switch the storage location of the transaction logs used for PITR from disk to Cloud Storage by using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API. For more information, see [Switch transaction log storage to Cloud Storage](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#switch-to-gcs).

**Caution:** Moving transaction logs from disk to Cloud Storage results in both several minutes of downtime and a loss of the previous logs for PITR. The downtime is because the instances must be restarted, and the logs are cleared when you deactivate PITR.

To ensure that logs for your instance are stored in Cloud Storage instead of on disk, complete the following actions:

  * [Check the network architecture of the instance](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture#check-single-instance). If the instance is on the old network architecture, then [upgrade it to the new network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture#upgrade-network-architecture).
  * If the size of your logs on disk is causing performance issues for your instance, then deactivate PITR and re-enable it. This action ensures that new logs are stored in Cloud Storage instead of on disk.

**Caution:** If you deactivate and re-enable PITR, then any existing logs are deleted, and you won't be able to perform PITR earlier than the time that you re-enabled it. Enabling and deactivating PITR requires restarting the database.



#### Log retention period

Cloud SQL retains transaction logs in Cloud Storage for up to the value set in the [`transactionLogRetentionDays`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances) PITR configuration setting. This value can range from 1 to 35 days for Cloud SQL Enterprise Plus edition and 1 to 7 days for Cloud SQL Enterprise edition. If a value for this parameter isn't set, then the default transaction log retention period is 14 days for Cloud SQL Enterprise Plus edition instances and 7 days for Cloud SQL Enterprise edition instances. For more information on how to set the transaction log retention days, see [Set transaction log retention](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#set-retention).

Although an instance stores the write-ahead logs used for PITR in Cloud Storage, the instance also keeps a smaller number of duplicate write-ahead logs on disk to allow for replication of the logs to Cloud Storage. By default, when you create an instance with PITR enabled, the instance stores its write-ahead logs for PITR in Cloud Storage. Cloud SQL also sets the value of the `expire_logs_days` and `binlog_expire_logs_seconds` flags to the equivalent of one day automatically. This translates to one day of logs on disk.

For PITR write-ahead logs that are stored _on disk_ , that are being switched to Cloud Storage, or that are already switched to Cloud Storage, Cloud SQL retains the logs for the minimum value set for one of the following configurations:

  * The `transactionLogRetentionDays` backup configuration setting
  * The `expire_logs_days` or the `binlog_expire_logs_seconds` flag



Cloud SQL doesn't set any values for these flags if the write-ahead logs are stored on disk, are being switched to Cloud Storage, or have already been switched to Cloud Storage. When logs are stored on disk, modifying the values of these flags can affect the behavior of PITR recovery and how many days worth of logs are stored on disk. While the log storage location is being switched to Cloud Storage, you can't modify the flag values. We also don't recommend that you configure either flag value to `0`. For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-expire-logs).

**Note:** If your instance has a large number of write-ahead logs on disk and you want to save disk space, then we recommend that you slowly reduce the value of the following:

  * `transactionLogRetentionDays` configuration setting
  * `expire_logs_days` database flag
  * `binlog_expire_logs_seconds` database flag



For example, to prevent performance issues, reduce the value of the flags by one day, each day, over several days. As a result, Cloud SQL doesn't purge all of the write-ahead logs simultaneously.

For [customer-managed encryption key (CMEK)-enabled instances](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek), write-ahead logs are encrypted using the latest version of the CMEK. To perform a restore, the latest key version is required for all days retained as part of the `retained-transaction-log-days` parameter.

### PITR limitations

The following limitations are associated with your instance having PITR enabled and the size of your transaction logs on disk causing an issue for your instance:

  * You can deactivate PITR and re-enable it to ensure that Cloud SQL stores logs in Cloud Storage in the same region as the instance. However, Cloud SQL deletes any existing logs so you can't perform a PITR operation earlier than the time that you re-enabled PITR.
  * You can increase the instance storage size, but the transaction log size increase in disk usage might be temporary.
  * To avoid unexpected storage issues, we recommend enabling [automatic storage increases](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen). This recommendation applies only if your instance has PITR enabled and your logs are stored on disk.



For step-by-step instructions for performing PITR, see [Use point-in-time recovery (PITR)][perform-pitr].

### Restore an unavailable instance

You can use PITR to restore a Cloud SQL instance that isn't available. PITR typically offers a recovery point objective (RPO) of five minutes or less.

If the instance is unavailable, then you can use the API to get the [earliest and latest recovery time](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#get-the-latest-recovery-time) to which you can restore the instance and perform the recovery to that time. If the zone in which the instance is configured isn't accessible, then you can [restore the instance to a different primary or secondary zone](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#perform-PITR-unavailable-instance) by providing values for the preferred zones.

Suppose a Cloud SQL instance becomes unavailable at 4 PM EST. If the latest recovery time is at 3:55 PM EST, then you can recover the instance up to this time.

### Restore a deleted instance using PITR

You can use PITR to restore a Cloud SQL instance after deletion. To use this feature, your instance must have [PITR](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#enablingpitr) and [retained backs](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#retained-backups) enabled before the instance is deleted. When enabled, PITR logs are retained after you delete the instance.

After an instance is deleted, the PITR logs continue to follow the retention settings defined by the instance when it was live. The PITR logs expire based on the retention settings on a rolling basis after the instance is deleted. The rolling period is defined based on the [PITR retention period](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#log-retention-period) set on the instance prior to deletion. For example, if your Cloud SQL Enterprise Plus edition instance has PITR retention set to 14 days, then the latest PITR log will be deleted 14 days after instance deletion. When a PITR log expires, it can't be recovered.

Since instance names can be reused after an instance is deleted in Cloud SQL, retained PITR logs can be identified in Google Cloud with the following fields:

  * `instance_deletion_time`
  * `log_retention_days`



These fields allow you to identify if a PITR log belongs to a deleted instance.

The PITR recovery window is defined as the earliest and latest recovery times available to restore your instance using PITR. To find your deleted instance's earliest and latest recovery times, see [Get the earliest and latest recovery time](https://docs.cloud.google.com/sql/docs/postgres/pitr#get-the-earliest-recovery-time).

To restore an instance using PITR after instance deletion, see [Perform PITR on a deleted instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#perform-PITR-deleted-instance).

## Requirements for restoring to a new instance

When you restore your instance to a new instance, note the following requirements:

  * The target instance must have the same database version as the instance from which the backup was taken.
  * When creating a new instance, the `storageAutoResize` feature is enabled by default. Any subsequently created backup inherits the same `storageAutoResize` setting. This means that whether restoring a backup to a new or existing instance, the instance will auto resize storage capacity as needed. Legacy instances don't have this feature enabled. To check your instance settings, see [View instance settings](https://docs.cloud.google.com/sql/docs/postgres/instance-info). 

  * The target instance must be in the `RUNNABLE` state.




## Restore rate limitations

You are allowed a maximum of three restore operations every 30 minutes per instance per region per project. If a restore operation fails, then it isn't counted towards this quota. If you reach the limit, then the operation fails with an error message that tells you when you can run the operation again.

Cloud SQL uses tokens from a bucket to determine how many restore operations are available at any one time. For each backup, there's a bucket for each target project and target region. The target instances from the same project share one bucket if they are in the same region. There's a maximum of three tokens in each bucket that you can use for restore operations. Every 10 minutes, a new token is added to the bucket. If the bucket is full, then the token overflows.

Each time you issue a restore operation, a token is granted from the bucket. If the operation succeeds, the token is removed from the bucket. If it fails, the token is returned to the bucket. The following diagram shows how this works:

![How tokens work](https://docs.cloud.google.com/static/sql/images/restore-rate-tokens.png)

For example, in the following figure, Backup1, Backup2, and Backup3 are the backups from the same source instance.

![Tokens for restore operation rate limiting](https://docs.cloud.google.com/static/sql/images/restore-rate-limiting.png)

  * Each backup (Backup1, Backup2, and Backup3) has its own bucket of tokens for restore operations that target different instances in Project 1 in Region A (Bucket11A, Bucket21A, and Bucket31A). Because each backup has its own bucket, you can restore each backup to the same instance three times every thirty minutes.
  * Each backup has a bucket for a separate project and for a separate region. For example, if there are five projects in a region, there are five buckets for that backup in that region, one in each project. In the previous figure, we have two projects in region A: Project 1 and Project n. 
    * Backup1 has two buckets of tokens for restore operations in Region A. One bucket for Project 1 (Bucket11A), and one bucket for Project n (Bucket1nA).
    * Similarly, Backup3 has two buckets for restore operations in Region A. One for Project 1 (Bucket31A) and one for Project n (Bucket3nA).
  * Backup3 has one bucket in Region B, for Project1, because all instances in the same target project and the same target region share one bucket.



## What's next

  * [Perform a restore from a backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring#restorebackups)
  * [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
