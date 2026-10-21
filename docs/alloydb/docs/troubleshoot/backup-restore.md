---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/backup-restore/
title: Troubleshoot backups and restores \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:35.693910+00:00
---

# Troubleshoot backups and restores  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/backup-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot backups and restores Stay organized with collections  Save and categorize content based on your preferences. 

This troubleshooting guide addresses common issues that you might encounter with AlloyDB for PostgreSQL backups, recovery, and replication. Recommended fixes are provided.

## You want to restore a deleted cluster

**Description:** In AlloyDB, both on-demand and automated backups are independent of the cluster that you want to restore. You can restore data from a backup to a new AlloyDB cluster even if the cluster that you used to create the backup is deleted. The storage layer handles AlloyDB backups. Also, the database doesn't lock during the backup process, which ensures continuous availability.

Backup restoration in AlloyDB is _out of place_ , which means that you restore the backup to a new cluster rather than overwriting an existing cluster. After you restore the cluster, you can add new primary or read pool instances to the restored cluster.

When you restore a cluster using point-in-time recovery (PITR), you can only restore a cluster from a time that is in the configured recovery window. You must choose a timestamp for a time when the cluster had an instance.

**Recommended fix:** [Restore a cluster from a stored backup](https://docs.cloud.google.com/alloydb/docs/backup/restore).

By default, AlloyDB continuously backs up your data with a 14-day recovery window. If you reconfigure your backup plan, it might take up to 24 hours for continuous backups and recovery to create a backup and enable continuous recovery functionality.

If you need help with this issue, contact [Google Cloud Support](https://cloud.google.com/support).

## You don't know how to find your backups

**Description:** Backups are stored separately from cluster storage for security and accessibility reasons.

**Recommended fix:** Find your backups using the following interfaces:

**Interface** | **Find backups**  
---|---  
Google Cloud console | [View a list of backups](https://docs.cloud.google.com/alloydb/docs/backup/list) in a project.  
Google Cloud CLI | [View a list of backups](https://docs.cloud.google.com/alloydb/docs/backup/list) in a project.  
REST API | Use the `[projects.locations.backups.list](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.backups/list)` method, which lets you list all backups in a specified project and location.   
  
## You want to perform a PITR, but you can't select a time

**Description:** AlloyDB offers PITR as part of its continuous backup and recovery. Transaction logs, which are essential for PITR, are offloaded to Cloud Storage, which ensures that the logs don't impact the size or performance of your clusters.

You might be unable to select a specific time for PITR for the following reasons:

  * The cluster that you want to restore doesn't exist. You can't use PITR to restore a deleted cluster.
  * The continuous backup feature isn't enabled. PITR relies on write-ahead logs (WAL) that are only collected when the continuous backup feature is enabled.
  * The backup restoration point is earlier than the date of the earliest continuous backup.
  * You didn't select a timestamp for a time when the cluster had an instance.



**Recommended fix:** Select a specific time for PITR.

Try the following fixes:

  * Verify that the cluster you want to restore exists. If the cluster exists, then follow the steps in [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr).
  * Check if continuous backups are enabled on your cluster. If continuous backups are enabled, then follow the steps in [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr).
  * Check if the time that you want to restore the backup is in the configured recovery window. By default, AlloyDB continuously backs up your data with a 14-day recovery window. For more information, see [Configure continuous backup](https://docs.cloud.google.com/alloydb/docs/backup/configure#configure-continuous).



## Your backups are deleted unexpectedly

**Description:** Your AlloyDB backups aren't deleted automatically unless automatic backup deletion is required by your retention configuration. The retention period of a backup is determined when a backup plan creates the backup—the retention period is written into the backup metadata at the time of backup creation, and the field is immutable.

Backups are created by backup plans, such as continuous backup and recovery or automatic backups. Backups have a retention window that's defined in the configuration of the backup plan, which is either the default retention window of 14 days, or is a user-configured retention parameter. You can't choose a retention period directly. On-demand backups have a 365-day retention period.

**Recommended fix:** To avoid unexpected backup deletions, review your backup plan configurations.

## You need to restore a backup to a different region

**Description:** You can only restore backups in the region where the backup is located, unless you first create a new on-demand backup of the original cluster.

**Recommended fix:** Restore a cluster to a new region by creating a new on-demand backup of the original cluster:

  1. Create the new backup in the target region.
  2. Use the new backup to perform the restore in your preferred region.



AlloyDB also supports backups on cross-region replicas. If you have a cross-region replica, taking a backup from that replica can fulfill many cross-region backup requirements. For more information, see [Cross-region replication overview](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
