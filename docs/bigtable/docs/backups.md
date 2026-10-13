---
url: https://docs.cloud.google.com/bigtable/docs/backups/
title: Bigtable backups overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:19.246174+00:00
---

# Bigtable backups overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bigtable backups overview

**Note:** This page includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

This page provides an overview of Bigtable backups. The content presented here is intended for Bigtable administrators and developers.

Backups let you save a copy of a table's schema and data and then restore from the backup to a new table later. Bigtable offers the following types of backups that depend on your disaster recovery (DR) requirements, the type of storage (HDD or SSD) that your Bigtable cluster uses.

  * **Standard backups** are optimized for long-term retention. When you restore from a standard backup to an SSD cluster, the restore operation requires additional optimization by Bigtable to bring the table to production-level performance. For more information, see Performance when restoring.
  * **Hot backups** provide the most efficient restoration to production-level performance and low-latency serving. For more information, see Hot backups.



You can create backups in the following ways:

  * Enable **automated backup** to let Bigtable create daily backups for you.
  * Create a **backup on demand** by using the Google Cloud console, the gcloud CLI, or a Bigtable client library.
  * Create a **copy of a backup**.



Before you read this page, you should be familiar with the [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview) and [Manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables).

## Features

  * **Fully integrated** : Backups are handled entirely by the Bigtable service, with no need to import or export.
  * **Incremental** : A backup shares physical storage with the source table and other backups of the table.
  * **Cost effective** : Using Bigtable backups lets you avoid the costs associated with exporting, storing, and importing data using other services.
  * **Automatic expiration** : Each backup has a user-defined retention period. For more information, see the Retention section of this document.
  * **Flexible restore options** : You can restore from a backup to a table in a different instance from where the backup was created.
  * **Automated backup** : Enable automated backup to let Bigtable create daily backups.
  * **Hot backups** : Plan for disaster recovery with production-ready hot backups.



## Use cases

Backups are useful for the following use cases:

  * Business continuity
  * Regulatory compliance
  * Testing and development
  * Disaster recovery



Consider the following disaster recovery scenarios:

**Goal** | **Backup strategy** | **Restoration strategy**  
---|---|---  
**Protect against human error:** You want to always have a recent backup of your data ready in case of accidental deletion or corruption.  | Determine the backups creation schedule that's right for your business needs, such as daily. Optionally, create periodic copies of the backups and store them in a different project or region for increased isolation and protection. For even more protection, store the backup copies in a project or instance with restricted access permissions.  | Restore to a new table from the backup or copy, and then re-route requests to the new table.   
**Zone unavailability:** You need to make sure that in the unlikely event that a Google Cloud zone becomes unavailable, your data is still available.  | Enable automated backup to let Bigtable create a daily backup on every cluster in the instance. Alternatively, create backups on a regular basis and then periodically create a copy of the most recent backup and store it on one or more clusters in different zones (optionally in a different instance or project).  | If the zone where your serving cluster becomes unavailable, restore from the remote backup copy to a new table, and then re-route requests to the new table.   
**Data corruption:** Use a backup to recover some of a table's data, such as when part of the source table has become corrupted.  | Enable replication and automated backup to create daily backups in multiple regions, so that if a table becomes corrupted on one cluster, you have one or more backups that don't share storage on the corrupted cluster.  | Restore from the backup to a new table on the new cluster or instance. Then write an application using a Bigtable client library or [Dataflow](https://cloud.google.com/products/dataflow) that reads from the new table and then writes the data back to the source table. When the data has been copied to the original table, delete the new table.   
**Fast recovery:** Restore to full production performance levels quickly, minimizing downtime.  | Always maintain a recent hot backup of your table. | Restore to a new table from the hot backup, and then re-route requests to the new table.   
  
## Hot backups

A _hot backup_ is a production-ready backup that is optimized for speedy recovery, with lower latency when reading from the new table shortly after restoration. Restoring to production performance from a hot backup is faster than restoring from a standard backup.

When you create a hot backup, you can configure the hot-to-standard transition time. The hot backup then automatically transitions to a standard backup after a specific date and time. For more information, see [Create a hot backup](https://docs.cloud.google.com/bigtable/docs/managing-backups#create-hot-backup).

### Limitations for hot backups

Hot backups have the following limitations:

  * You can convert a hot backup to a standard backup, but you can't convert a standard backup to a hot backup.
  * You can't create hot backups using automated backup, and you can't create a hot backup on an HDD cluster.
  * A copy of a hot backup is always a standard backup. As such, the backup copy doesn't have the same efficient restoration to production-level performance and low-latency serving as the hot backup.



## Working with Bigtable backups

The following actions are available for Bigtable backups. In all cases, **the destination project, instance, and cluster must already exist**. You are not able to create these resources as part of a backup operation.

  1. You can't create a copy of a backup copy. 
  2. A copy of a backup is always a standard backup, even if the source is a hot backup. 

  
---  
**Action** | **Destination options**  
Create a standard backup | 

  * Any cluster in the same instance as the source table

  
Create a hot backup | 

  * Any cluster in the same instance as the source table. The instance must use SSD storage.

  
Restore from a standard or hot backup to a new table | 

  * Any instance


  * Any Bigtable region


  * Any project

  
Copy a backup1, 2 | 

  * Any instance


  * Any Bigtable region


  * Any project

  
  
See [Manage backups](https://docs.cloud.google.com/bigtable/docs/managing-backups) for **step-by-step instructions** on these actions as well as operations such as updating and deleting backups.

Use the following to work with Bigtable backups:

  * The Google Cloud console
  * The Google Cloud CLI
  * The Cloud Bigtable [client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries)



## Backup storage

A table backup that you create manually or programmatically is stored on a single cluster that you specify. When automated backup is enabled, Bigtable stores a backup on each cluster in the instance. In the Enterprise Plus edition, you can [select cluster locations where automated backup is enabled](https://docs.cloud.google.com/bigtable/docs/managing-backups#automated-backup-cluster-locations).

If your cluster exceeds the recommended limits for CPU or storage utilization when you create a backup, your backup creation might be delayed. For more information, see [Understand CPU and disk usage](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cpu-and-disk).

A backup of a table includes all the data that was in the table at the time the backup was created, on the cluster where the backup is created. A backup is never larger than the size of the source table at the time that the backup is created.

Bigtable backups are incremental. The amount of storage that a backup consumes depends on the size of the table and the extent to which it can share storage of unchanged data with the original table or other backups of the same table. For that reason, a backup's size depends on the amount of data divergence since the prior backup.

You can create up to 150 backups per table per cluster.

You can delete a table that has a backup. To protect your backups, you can't delete the following:

  * A cluster that contains one or more backups. To delete the cluster, you must delete those backups or wait for them to expire.
  * A cluster that is configured as a location in a table's automated backup policy. To delete the cluster, you must first update the automated backup policy to remove the cluster location or disable automated backup for the table.
  * An instance that has one or more backups in any cluster.



A backup still exists after you restore from it to a new table. You can delete it or let it expire when you no longer need it. Backup storage does not count toward the [node storage limit](https://docs.cloud.google.com/bigtable/quotas#nodes-per-project) for a project.

Data in backups is encrypted.

## Retention

Bigtable backups let you retain your data for a specified period. You can configure the retention period for individual backups or as part of an automated backup policy:

  * The retention period begins from the moment when the backup is created.
  * The default retention period for tables with enabled automated backup is seven days.
  * You can configure a custom retention period for an automated backup policy of up to 90 days in both Enterprise and Enterprise Plus editions. For individual on-demand backups or when you update a retention period of an existing backup, you can specify up to 90 days in the Enterprise edition or up to 365 days in the Enterprise Plus edition.
  * If you create a copy of a backup, the maximum retention period for the copy is 30 days from the time the copy is created.
  * When creating a backup, you can specify an _expiration date_ instead of a retention period. An expiration date is an absolute date and time, while a retention period specifies a duration. Both methods result in an expiration time that follows the same rules and limitations.
  * For hot backups, you can define an independent transition time that determines when the backup ceases to be hot and becomes standard. You can modify this time, but it must be at least 24 hours after you created the backup.



You can change the retention period for a backup or for an automated backup policy. For more information, see [Modify a backup or backup copy](https://docs.cloud.google.com/bigtable/docs/managing-backups#modify) and [Update an automated backup policy](https://docs.cloud.google.com/bigtable/docs/managing-backups#update-automated-backup).

## Post-restoration storage

The storage cost for a new table restored from a backup is the same as for any table.

A table restored from a backup might not consume the same amount of storage as the original table, and it might decrease in size after restoration. The size difference depends on how recently [compaction](https://docs.cloud.google.com/bigtable/docs/overview#compactions) has occurred on the source cluster and the destination cluster.

Because compaction occurs on a rolling basis, it's possible that compaction occurs as soon as the table is created. However, compaction can take up to a week to occur.

A new table restored from a backup doesn't inherit the garbage collection policies of the source table. Configure garbage collection policies in the new table before you begin writing new data to the table. For more information, see [Configure garbage collection](https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection).

## Costs

Standard network costs apply when working with backups. You are not charged for backup operations, including creating, copying, or restoring from a backup.

### Storage costs

Storage costs are different for standard backups and hot backups.

#### Standard backup storage costs

To store a standard backup or a copy of a backup, you're charged the [standard backup storage rate](https://docs.cloud.google.com/bigtable/pricing#backups) for the region that the cluster containing the backup or backup copy is in.

A standard backup is a complete logical copy of a table. Behind the scenes, Bigtable optimizes standard backup storage utilization. This optimization means that a standard backup is incremental — it shares physical storage with the original table or with other backups of the table whenever possible. Because of Bigtable's built-in storage optimizations, the cost to store a standard backup or a copy of a backup might sometimes be less than the cost of a full physical copy of the table backup.

In replicated instances where automated backup is enabled, the storage costs might be higher because a backup is created on each cluster daily. In the Enterprise Plus edition, you can reduce storage costs by enabling automated backups only for clusters in specific locations.

#### Hot backup storage costs

To store a hot backup, you're charged the [hot backup storage rate](https://cloud.google.com/skus?filter=Bigtable%20hot%20backup&currency=USD) for the region that the cluster that contains the hot backup is located.

Because a hot backup is stored in a ready state, optimized for quick restoration, you are charged for storage of the entire logical copy of the table, rather than for incremental portions, as you are with a standard backup.

### Costs when copying a backup

When you create a copy of a backup in a different region than the source backup, you are charged standard network rates for the cost of copying the data to the destination cluster. You are not charged for network traffic when you create a copy in the same region as the source backup.

### Costs when restoring

When you restore a new table from a backup, you are billed for the network cost of replication. If the new table is in an instance that uses replication, you are charged a [one-time replication cost](https://docs.cloud.google.com/bigtable/pricing#replication-initial) for the data to be copied to all clusters in the instance.

If you restore to a different instance than where the backup was created, and the backup's instance and the destination instance don't have at least one cluster in the same region, you are charged a one-time cost for the initial data copy to the destination cluster at the [standard network rates](https://docs.cloud.google.com/bigtable/pricing#network).

## CMEK

When you create a backup in a cluster that is protected by a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/bigtable/docs/cmek), the backup is pinned to the primary version of the cluster's CMEK key at the time it is taken. Once the backup is created, its key and key version cannot be modified, even if the KMS key is rotated.

When you restore from a backup, the key version that the backup is pinned to must be enabled for the backup decryption process to succeed. The new table is protected with the latest primary version of the CMEK key for each cluster in the destination instance. If you want to restore from a CMEK-protected backup to a different instance, the destination instance must be CMEK-protected as well but does not need to have the same CMEK configuration as the source instance.

## Replication considerations

This section describes additional concepts to understand when backing up and restoring a table in an instance that uses [replication](https://docs.cloud.google.com/bigtable/docs/replication-overview).

### Replication and backing up

When you take a backup of a table manually in a replicated instance, you choose the cluster where you want to create and store the backup. For tables with automated backup enabled, a daily backup is created on each cluster in the instance. In the Enterprise Plus edition, you can limit the automated backup to clusters only in specific locations.

You don't have to stop writing to the cluster that contains the backup, but you should understand how Bigtable handles replicated writes to the cluster.

A backup is a copy of the table in its state on the cluster where the backup is stored, at the time the backup is created. Table data that has not yet been replicated from another cluster in the instance is not included in the backup.

Each backup has a start and end time. Writes that are sent to the cluster shortly _before or_ _during_ the backup operation _might not_ be included in the backup. Two factors contribute to this uncertainty:

  * A write might be sent to a section of the table that the backup has already copied.
  * A write to another cluster might not have been replicated to the cluster that contains the backup.



In other words, there's a chance that some writes with timestamps before the time of the backup might not be included in the backup.

If this inconsistency is unacceptable for your business requirements, you can use a [consistency token](https://docs.cloud.google.com/bigtable/docs/writes#replication-consistency) with your write requests to ensure that all replicated writes are included in a backup.

Backups of replicated tables that are created as part of automated backup are not exact copies of each other, because backup times can vary from cluster to cluster.

### Replication and restoring

When you restore a backup to a new table, replication to and from the other clusters in the instance starts immediately after the restore operation has completed on the destination cluster.

## Performance

While creating backups, use the following best practices to ensure that your performance remains optimal.

### Performance when backing up

Creating a backup usually takes less than a minute, although it can take up to one hour. Under normal circumstances, backup creation does not affect serving performance.

For optimal performance, don't create a backup of a single table more than once every five minutes. Creating backups more frequently can potentially lead to an observable increase in serving latency.

### Performance when restoring

Restoring from a backup to a table in a single-cluster instance takes a few minutes. In replicated instances, restoration takes longer because the data has to be copied to all the clusters. Bigtable always chooses the most efficient route to copy data.

If you restore to a different instance from where the backup was created, the restore operation takes longer than if you restore to the same instance. This is especially true if the destination instance does not have a cluster in the same zone as the cluster where the backup was created.

A bigger table takes longer to restore than a smaller table.

If you have an SSD instance, you might initially experience higher read latency, even after a restore is complete, while the table is optimized. You can [check the status](https://docs.cloud.google.com/bigtable/docs/managing-backups#status-backup) at any time during the restore operation to see if optimization is still in process.

If you restore to a different instance from where the backup was created, the destination instance can use HDD or SSD storage. It does not need to use the same storage type as the source instance.

## Access control

[IAM permissions](https://docs.cloud.google.com/bigtable/docs/access-control#permissions) control access to backup and restore operations. Backup permissions are at the instance level and apply to all backups in the instance.

The account that you use to create a backup of a table must have permission to read the table and create backups in the instance that the table is in (the source instance).

The account that you use to copy a backup must have permission to read the source backup and to create a backup in the destination instance and project.

The account that you use to restore a new table from a backup must have permission to create a table in the instance that you are restoring to.

**Action** | **Required IAM permission**  
---|---  
Create a backup | bigtable.tables.readRows, bigtable.backups.create  
Get a backup | bigtable.backups.get  
List backups | bigtable.backups.list  
Delete a backup | bigtable.backups.delete  
Update a backup | bigtable.backups.update  
Copy a backup | bigtable.backups.read, bigtable.backups.create  
Restore from a backup to a new table | bigtable.tables.create, bigtable.backups.restore  
Get an operation | bigtable.instances.get  
List operations | bigtable.instances.get  
  
## Best practices

Before you create a backup strategy, consider the following best practices. For more information about disaster recovery planning, see the Bigtable section of [Architecting disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/architecture/disaster-recovery).

### Creating backups

  * Don't back up a table more frequently than once every five minutes.
  * When you back up a table that uses replication, choose the cluster to store the backup after considering the following factors: 
    * **Cost**. One cluster in your instance may be in a lower-cost region than the others.
    * **Proximity to your application server**. You might want to store the backup as close to your serving application as possible.
  * If you need to ensure that all replicated writes are included in a backup when you back up a table in an instance that uses replication, use a [consistency token](https://docs.cloud.google.com/bigtable/docs/writes#replication-consistency) with your write requests.



### Restoring from backups

  * Plan ahead what you will name the new table if you need to restore from a backup. The key point is to be prepared ahead of time so that you don't have to decide when you're dealing with a problem.
  * If you are restoring a table for a reason other than accidental deletion, make sure all reads and writes are going to the new table before you delete the original table.
  * If you plan to restore to a different instance, [create the destination instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) before you initiate the backup restore operation.
  * To avoid slow table restoration, wait for a restore operation to complete before you initiate another restoration for the same source table in the same zone.
  * Wait at least an hour after creation before you restore from a standard backup. If you need to restore more quickly, use a hot backup instead.



## Quotas and limits

Backup and restore requests and backup storage are subject to [ Bigtable quotas and limits](https://docs.cloud.google.com/bigtable/quotas).

## Limitations

The following limitations apply to Bigtable backups:

**General**

  * You can't read directly from a backup.
  * A backup is a version of a table in a single cluster at a specific time. Backups don't represent a consistent state. The same also applies to backups of the same table in different clusters.
  * You cannot back up more than one table in a single operation.
  * You cannot export, copy, or move a Bigtable backup to another service, such as Cloud Storage.
  * Bigtable backups contain only Bigtable data and are not integrated with or related to backups for other Google services.
  * You can't create a backup of a view.



**Restoring**

  * You can't restore from a backup to an existing table.
  * You can only restore to an instance that already exists. Bigtable does not create a new instance when restoring from a backup. If the destination instance specified in a restore request does not exist, the restore operation fails.
  * If you restore from a backup to a table in an SSD cluster and then delete the newly restored table, the table deletion might take a while to complete because Bigtable waits for table optimization to finish.



**Copying**

  * You can't create a copy of a backup that is within 24 hours of expiring.
  * You can't create a copy of a backup copy.



**CMEK**

  * A backup that is protected by CMEK must be restored to a new table in an instance that is CMEK-protected.
  * When you create a copy of a backup that is CMEK-protected, the destination cluster must also be CMEK-protected.



## What's next

  * [Learn how to back up and restore tables](https://docs.cloud.google.com/bigtable/docs/managing-backups).
  * [Learn how to enable automated backup](https://docs.cloud.google.com/bigtable/docs/managing-backups#enable-automated-backup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
