---
url: https://docs.cloud.google.com/alloydb/docs/backup/overview/
title: Data backup and recovery overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:21.428598+00:00
---

# Data backup and recovery overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/backup/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Data backup and recovery overview Stay organized with collections  Save and categorize content based on your preferences. 

To protect your data in AlloyDB for PostgreSQL databases, you can use several features to back up and recover your data, and to manage your backups. To restore data to a cluster from a backup, see [Restore a cluster from a backup](https://docs.cloud.google.com/alloydb/docs/backup/restore).

AlloyDB provides the following ways to back up and recover your data:

  * _Continuous backup and recovery_ , enabled on all clusters by default, is an AlloyDB feature that lets you create a new cluster based on any recent state of another cluster in the same region as the source cluster, and it can be in a different Google Cloud project.
  * _On-demand and automated backups_ are file-based resources that contain complete copies of your cluster's databases. AlloyDB creates them on-demand, or according to a regular schedule that you define. You can restore any of these backups into new clusters.



AlloyDB offers the following backup services to manage your backups:

  * Enhanced backups: backups are managed and stored in a centralized backup management project that uses the Backup and DR Service, which provides the [Backup and DR Service backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault), enforced retention, granular scheduling, and monitoring. For more information, see the [Backup and DR overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).
  * Standard backups: backups are created, managed, and stored by AlloyDB.



For more information about each backup option and its features, see Backup options.

## Types of backups

AlloyDB offers different types of backups for your clusters. The following table provides an overview of each backup type:

**Backup type** | **Description**  
---|---  
Continuous backup and recovery | Lets you restore an existing cluster to any moment from its recent history, with microsecond granularity, using point-in-time recovery (PITR). This feature is enabled by default, with a configurable retention window of 1 to 35 days. As part of this process, AlloyDB creates daily incremental backups.  
On-demand backup | A full backup of your cluster that you initiate manually at any time. You can also take an on-demand backup of your cluster before you delete it.  
Automated backup | Incremental backups that AlloyDB creates automatically based on a schedule you define.  
System backups | Backups that AlloyDB automatically creates in specific situations. Examples include backups created during [cross-region failover](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#backup-on-failover) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) operations, and backups created before and after an [in-place major version upgrade](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version) to serve as a rollback point.  
  
### Continuous backup and recovery

AlloyDB lets you restore an existing cluster to any moment from its recent history, with microsecond granularity. By default, AlloyDB lets you choose any point in time up to 14 days into the past. You can [configure your cluster](https://docs.cloud.google.com/alloydb/docs/backup/configure#continuous) to resize this window to as long as 35 days, or as short as one day.

Continuous backup and recovery is especially useful for restoring a cluster after an accidental large-scale data deletion, or any other situation where you need to rapidly re-create a cluster's state based on some point in the recent past.

Continuous backup and recovery lets AlloyDB have a [recovery point objective (RPO)](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) of zero. In other words, you can restore your cluster to the state that it held moments before a catastrophic incident, without the permanent loss of any data.

You can also use continuous backup and recovery to [make an independent clone of a healthy cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create#clone), with all its data copied over from the present moment.

### On-demand or automated backups

In AlloyDB, a backup is a file-based resource containing a copy of a cluster's data from a particular moment in time.

AlloyDB has the following ways of creating backups:

  * AlloyDB always creates one backup every day as part of its continuous backup and recovery system, unless you disable this feature. Continuous backups are _incremental backups_ : AlloyDB stores only the data that changed relative to previous backups. This approach keeps the backup files as small as possible, which helps to reduce your backup storage costs. These backups vary in size, depending on factors such as how much data is written since the last backup. Full continuous backups are also taken periodically; the backup size is similar to the cluster size.
  * You can create an [on-demand backup](https://docs.cloud.google.com/alloydb/docs/backup/create-on-demand) at any time using the Google Cloud CLI, the Google Cloud console, or the Backup and DR Service API (if you're using enhanced backups). On-demand backups are _full backups_ : each backup includes all the data that was in its cluster's databases when the backup operation began.
  * If you enable an AlloyDB [automated backup](https://docs.cloud.google.com/alloydb/docs/backup/configure) schedule, then AlloyDB creates additional backups regularly, according to your preferences. Automated backups are incremental, similar to continuous backups. If you configure automated backups to use a retention window longer than 35 days, then AlloyDB might store multiple chains of incremental backups to cover the necessary time span.



As with your cluster's databases, AlloyDB encrypts backup data through either the default Google-managed encryption or [customer-managed encryption keys](https://docs.cloud.google.com/alloydb/docs/cmek). When you create a backup, its contents become immutable, which means that you can't change them.

## Backup options

AlloyDB offers two options of backup services to manage your cluster's backups: Standard and Enhanced backups. You can choose between the standard and enhanced backup options based on your cluster's requirements and needs. Although clusters can't use both backup options at the same time, AlloyDB lets you switch between these backup options as needed.

The following table provides an overview of the features available with each backup option:

**Feature** | **Standard backup tier**(managed by AlloyDB) | **Enhanced backup tier**(managed by Backup and DR)  
---|---|---  
Backups secured against unauthorized deletion and changes | Immutable backups through backup vault | Immutable and indelible backups through backup vault  
Automated backup frequency | Daily with continuous log archival (continuous backups and recovery)Hourly/daily/weekly (Automated backups) | Hourly, daily, weekly, monthly, or annually  
Backups protected against source project deletion | – | ✅  
Centralized backup management | – | ✅  
Backup protected against source cluster deletion | ✅ | ✅  
Point-in-time recovery (PITR) using logs | ✅ | ✅  
Cross-regional backup | ✅ | –  
On-demand backup retention | Can be retained up to 1 year | Can be retained up to 1 year; eligible for manual deletion or expiration after the retention period elapses  
  
### Standard backups

AlloyDB's standard backup capabilities are built-in data protection features available by default on all clusters. This system provides a foundational layer of protection through two primary mechanisms: continuous backups and on-demand or automated backups.

Continuous backup and recovery is enabled on all clusters by default. It lets you restore a new cluster to any moment from its recent history with microsecond granularity using point-in-time recovery (PITR). The PITR window defaults to 14 days, but you can configure the window between 1 and 35 days. AlloyDB creates one daily incremental backup as part of this system, which stores only the data that changed since the last backup.

On-demand or automated backups are file-based resources that contain complete copies of the cluster's data from a specific moment in time. On-demand backups are full backups that include all cluster data at the time of creation. Automated backups are incremental backups that are created according to a user-defined schedule. After a backup is created, the backup data is immutable, preventing alterations. Backups are stored in the same region as the cluster by default, but you can specify a custom cross-region location for on-demand backups.

### Enhanced backups

AlloyDB's enhanced backup capability integrates with the Backup and DR Service, Google Cloud's central, enterprise-class backup service. Enhanced backups are best suited for select and enterprise segments and highly regulated workloads, and they provide protection from ransomware for mission-critical applications. With enhanced backups, you get the following features, which are in addition to the standard backup capabilities:

  * Immutable storage: backups are stored in a Backup and DR-managed [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).
  * Enforced retention: policies prevent accidental or malicious deletion of backups.
  * Advanced scheduling: highly customized backup frequency and retention rules.
  * Centralized management: uniform monitoring and reporting across multiple Google Cloud workloads like AlloyDB, Cloud SQL, and Compute Engine.



## Backup retention and deletion

The files that AlloyDB creates to enable continuous backup and recovery have a default retention period of 14 days. You can adjust this period to any number of days between 1 and 35, or you can disable continuous backup to prevent AlloyDB from retaining these files at all.

On-demand and automated backups have a retention period of up to one year. If you enable automated backups on your cluster, you can either set a retention period, or use the default period of 14 days.

Backups older than their retention period might still appear when you [view your project's backups](https://docs.cloud.google.com/alloydb/docs/backup/list). Expired backups don't incur storage costs, but they are subject to automated deletion. If you need to delete backups before the system deletes them, you can [manually delete your backups](https://docs.cloud.google.com/alloydb/docs/backup/delete).

### Backup deletion protections

You can manually delete your backups, but AlloyDB provides strong protections to prevent you from accidentally or unintentionally deleting backups that are actively managed or have dependencies.

You can't delete AlloyDB backups under the following conditions:

  * Active continuous backup plan: you can't delete a continuous backup if an active continuous backup configuration manages it on the source cluster and the backup is still in the cluster's recovery window. To delete these continuous backups, first disable continuous backup or shorten its recovery window. You can delete on-demand or automated backups at any time.
  * Dependency chain: you can't delete a backup if a later one needs it for a restore operation. For example, in a chain of incremental backups, you must delete the most recent incremental backup before you can delete the one that came before it.
  * Enhanced backups are in a Backup and DR backup vault inside the [enforced retention period](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#enforced-retention). This compliance feature prevents accidental or malicious deletion. During this period, no one can delete the backup.



These protections ensure the integrity of your backup history and the ability to restore your cluster to any valid point in time.

## Backup creation requirements

AlloyDB prepares to create a new backup by checking that the cluster's state is Ready, and then AlloyDB starts a long-running operation to create the backup.

## Efficient and independent backups

Backups you create from your AlloyDB data are managed entirely by AlloyDB's storage layer. This means that backup and restore operations have no impact on the read and write performance of your AlloyDB cluster, because they are performed by resources that are separate from the resources that store and query that cluster's data.

This separation of storage resources also means that a backup exists independently from its original cluster. You can restore from that backup even if its source cluster is deleted.

To learn more about how AlloyDB's storage layer enables independent backups, see [AlloyDB for PostgreSQL under the hood: Intelligent, database-aware storage](https://cloud.google.com/blog/products/databases/alloydb-for-postgresql-intelligent-scalable-storage).

## On-demand backups locations

For [on-demand backups](https://docs.cloud.google.com/alloydb/docs/backup/overview#on-demand-or), AlloyDB backup locations include the following:

  * [Default location](https://docs.cloud.google.com/alloydb/docs/backup/overview#default-backup-location) that AlloyDB selects, based on the location of the original cluster.
  * [Cross-region location](https://docs.cloud.google.com/alloydb/docs/backup/overview#cross-region-backup-location) that you specify when you don't want to use the default location.

**Note:** Enhanced backups handle on-demand backups differently. For more information, see [Create an on-demand backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-backup#create_an_on-demand_backup).

### Default backup location

If you don't specify a storage location, your backups are stored in the location of your AlloyDB cluster. For example, if your AlloyDB instance is in `us-central1 (Iowa)`, your backups are stored in the `us-central1 (Iowa)` location by default.

### Cross-region backup location

AlloyDB lets you select a custom cross-region location for your backup data, which expands the set of regions where you can store your backups. This is useful for retaining the ability to restore if your cluster region becomes unavailable.

When selecting a cross-region location for a backup, consider the following:

  * **Cost** : pricing may differ between the regions.
  * **Proximity to your application server** : you might want to store the backup as close to your serving application as possible.



**Note** : If you change the location where backups are stored, existing backups remain in their original location.

## Cluster restoration

You can restore a cluster in AlloyDB by creating a new cluster that contains all of the original cluster's data from some point in the past. The two ways that you can specify this point correspond to the two general kinds of backups that AlloyDB supports:

  * To perform a point-in-time restore of a cluster's recent state, specify both a source cluster and a timestamp when creating a new cluster. The new cluster must be in the same region as the source cluster, but can be in a different Google Cloud project.
  * To restore a cluster from a backup, specify that backup when creating a new cluster. The new cluster must be in the same region as the backup, but can be in a different Google Cloud project.



In both cases, AlloyDB creates a new cluster and then initiates a long-running operation to load the backed-up data into that cluster's storage. After this operation completes, you create a primary instance in that cluster to access the data.

Cluster restores occur in the same region, but on-demand backups can be stored cross-region. Backups and restores are supported across different Google Cloud projects and organizations.

For more, see [Restore from a backup](https://docs.cloud.google.com/alloydb/docs/backup/restore).

## What's next

  * [Manage enhanced backups](https://docs.cloud.google.com/alloydb/docs/backup/manage-enhanced-backups).
  * [Restore a cluster](https://docs.cloud.google.com/alloydb/docs/backup/restore).
  * [Manually create an on-demand backup](https://docs.cloud.google.com/alloydb/docs/backup/create-on-demand).
  * [Configure backup plans](https://docs.cloud.google.com/alloydb/docs/backup/configure), including automated backups and continuous backups.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
