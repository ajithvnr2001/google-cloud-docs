---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/protect-data-using-backups/
title: Protect your data using backups \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:25:16.755298+00:00
---

# Protect your data using backups  |  AlloyDB Omni using the container orchestrator: 16.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/protect-data-using-backups/

This page documents AlloyDB Omni version **16.13.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/overview)



Send feedback 

#  Protect your data using backups Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.13.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/protect-data-using-backups)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/protect-data-using-backups)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/protect-data-using-backups)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/protect-data-using-backups)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/protect-data-using-backups)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/protect-data-using-backups)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/protect-data-using-backups)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/protect-data-using-backups)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/protect-data-using-backups)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/protect-data-using-backups)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/protect-data-using-backups)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/protect-data-using-backups)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/protect-data-using-backups)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/protect-data-using-backups)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/protect-data-using-backups)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/protect-data-using-backups)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/protect-data-using-backups)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/protect-data-using-backups)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/protect-data-using-backups)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/protect-data-using-backups)

This page describes the AlloyDB Omni Standard Availability reference architecture, which provides data protection using backups. 

## Use cases

This reference architecture supports the following scenarios:

  * You have databases that can tolerate some downtime and data loss since the last backup.
  * You want to protect your AlloyDB Omni database from user error, corruption, or physical failures at the database level, as opposed to server or VM image snapshots.
  * You want to recover your database in place or remotely, possibly up to a specific point in time.



## How the reference architecture works

The Standard Availability reference architecture covers the backup and recovery of your AlloyDB Omni databases.

While Standard Availability is a basic implementation and minimizes required additional hardware or services, the Recovery Time Objective ([RTO](https://en.wikipedia.org/wiki/IT_disaster_recovery#Recovery_Time_Objective)) increases as the database gets larger. The more data there is to back up, the longer it takes to restore and recover the database. Data loss depends on the type of backup. If only data files are backed up periodically, then when you restore, you incur data loss since the last backup.

## Reducing RPO

The PostgreSQL [continuous archiving](https://www.postgresql.org/docs/current/continuous-archiving.html) feature lets you achieve a low Recovery Point Objective ([RPO](https://en.wikipedia.org/wiki/IT_disaster_recovery#Recovery_Point_Objective)) and enable point-in-time recovery through backups. This process involves archiving Write-Ahead Logging (WAL) files and streaming WAL data, potentially to a remote storage location.

If WAL files are archived only when full or at specific intervals, a complete database loss (including current WAL files) restricts recovery to the last archived WAL file, which means that your RPO must account for potential data loss. Conversely, continuous WAL data transfer minimizes potential data loss.

When you configure continuous backups, you can perform [recovery to a specific point in time](https://www.postgresql.org/docs/current/continuous-archiving.html). Point-in-time recovery lets you restore a database to a state before an error, such as accidental table deletion or incorrect batch updates. However, this recovery method affects both RPO and RTO unless you use a temporary auxiliary database. Restoring an entire database in place rolls back subsequent transactions on unaffected tables and takes the database offline, whereas restoring to a temporary auxiliary database lets you copy only the recovered data.

## Backup strategies

AlloyDB Omni supports data protection strategies such as periodic physical backups, point-in-time recovery, WAL archiving and streaming, and storing backups in different locations. Alternatively, for small databases, you can perform a logical backup by using [`pg_dump`](https://www.postgresql.org/docs/current/app-pgdump.html) for a single database or [`pg_dumpall`](https://www.postgresql.org/docs/current/app-pg-dumpall.html) for the entire cluster, and restore by using [`pg_restore`](https://www.postgresql.org/docs/current/app-pgrestore.html).

### Backup tools

For Kubernetes deployments, you can configure continuous backups using a backup plan (`BackupPlan`) managed by the AlloyDB Omni operator for each database cluster. For more information, see [Back up and restore in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/backup-kubernetes).

Depending on your deployment option, you can configure AlloyDB Omni to store backups on either local or remote storage, such as Cloud Storage or storage options provided by any cloud vendor. Although local storage might be faster to back up and recover from, remote storage is usually more robust for handling failures when an entire host or VM fails. For more information, see Figure 1, which shows potential backup destinations.

**Note:** While the illustrations in this document show Google Cloud physical location-related concepts and terminology such as "Zone" and "Region", AlloyDB Omni can be deployed in any cloud or any customer-managed environment. Consequently, terms such as "data center" or "city" might be more suitable to accurately represent your environments.

![AlloyDB Omni with backup options](https://docs.cloud.google.com/static/alloydb/omni/kubernetes/16.13.0/docs/images/alloydb-omni-ref-arch-standard.png)

**Figure 1.** AlloyDB Omni with backup options.

You can take backups to either local or remote storage options. Local backups tend to be quicker because they rely on only I/O throughput, whereas remote backups usually have a higher latency and lower network bandwidth. However, remote backups provide better protection against host and zonal failures than local backups.

You can also split local backups into local or shared storage. While local storage lacks disaster recovery options when a database host fails, shared storage lets you relocate that storage to another server and use it for recovery. This means that shared storage potentially offers a faster RTO.

For local, shared, and remote storage deployments, you can schedule the following types of backups or take them manually on demand:

  * **Full backups** : complete backups of all the database files needed for data recovery.
  * **Differential backups** : backups of only the file changes since the last full backup.
  * **Incremental backups** : backups of only the file changes since the last backup of any kind.



### Point-in-time recovery

Continuous backups of the PostgreSQL WAL files support point-in-time recovery. If, after a failure event, the WAL files are intact and usable, then you can use these files to recover to a specific point in time and help minimize data loss.

### Backup schedules

In most environments, backups are usually scheduled on a weekly basis. The following is a typical weekly schedule of backups:

  * Sunday: full backup
  * Monday, Tuesday: incremental backup
  * Wednesday: differential backup
  * Thursday, Friday: incremental backup
  * Saturday: differential backup



Using this typical schedule, a rolling recovery window of one week requires storage space for up to three full backups plus the required incremental or differential backups. This approach supports recovery for a failure that takes place during the full backup on Sunday, when the database recovery must extend to the previous Sunday before the backup started.

To minimize RTO with a potential for higher RPO, additional databases can operate in continuous recovery mode. This mode involves replaying backups and continuously updating the secondary environment by archiving and replaying new WAL files. The actual RPO, which reflects potential data loss, depends on transaction frequency, WAL file size, and the use of WAL streaming.

### Backup restoration

You can restore an AlloyDB Omni database from a stored backup or recover to a specific point in time within your retention window. Depending on your deployment environment and recovery needs, you can either restore data in place or restore the backup into a new database instance or cluster.

For Kubernetes deployments, the AlloyDB Omni operator supports recovering a database into the same Kubernetes cluster and namespace from a named backup or cloning from a point in time. For more information, see [Back up and restore in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/backup-kubernetes) and [Overview of manually cloning a database cluster from a Kubernetes backup](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/kubernetes-dr-backup-overview).

## Implementation

When you choose an availability reference architecture, keep in mind the following benefits, limitations, and alternatives.

### Benefits

  * Is straightforward to use and manage, and is suitable for non-critical databases with lenient RTO and RPO.
  * Requires minimal additional hardware.
  * Provides the foundational backups required for a disaster recovery plan.
  * Supports recovery to any point in time within the recovery window.



### Limitations

  * Can require more storage space than the database itself, depending on your retention requirements.
  * Can be slow to recover and might result in a higher RTO.
  * Can result in some data loss, depending on the availability of the current WAL data after a database failure, which might negatively affect RPO.



### Alternatives

Consider the [Enhanced Availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/protect-data-using-zonal-replication) or [Premium Availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/protect-data-using-zonal-regional-replication) reference architecture for improved availability and disaster recovery options.

## What's next

  * [AlloyDB Omni availability reference architecture overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/database-availability-reference-architecture-overview)
  * [AlloyDB Omni Enhanced Availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/protect-data-using-zonal-replication)
  * [AlloyDB Omni Premium Availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/protect-data-using-zonal-regional-replication)
  * [Back up and restore AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/backup-overview)
  * [Back up and restore in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/backup-kubernetes)
  * [Overview of manually cloning a database cluster from a Kubernetes backup](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/kubernetes-dr-backup-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
