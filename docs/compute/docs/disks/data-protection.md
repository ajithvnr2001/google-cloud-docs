---
url: https://docs.cloud.google.com/compute/docs/disks/data-protection/
title: Data protection options for disks and instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:38.204460+00:00
---

# Data protection options for disks and instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/data-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Data protection options for disks and instances Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you choose the right option to protect your Compute Engine resources based on your [recovery time objective (RTO)](https://wikipedia.org/wiki/IT_disaster_recovery), [recovery point objective (RPO)](https://wikipedia.org/wiki/IT_disaster_recovery), use case, and cost requirements.

Compute Engine offers a variety of options to protect the following resources:

  * Compute Engine instances
  * Persistent Disk
  * Google Cloud Hyperdisk



Each data protection option is designed for specific use cases and recovery needs. To protect your critical data, we recommend implementing one of the following backup or replication solutions.

Goal | Recommended solution  
---|---  
Test, debug, or manage deployments | For disks, use instant snapshots, disk clones, or custom OS images.  
  
For instances, use machine images.  
Back up for disaster recovery | For disks, use standard or archive snapshots.  
  
For instances, use machine images or Backup and DR Service.  
High availability for disaster recovery | For disks, use synchronous or Asynchronous Replication.  
**Warning:** To protect your data, you must implement one of the strategies discussed in this document. Keep the following in mind:  


  * **No automatic backups:** Compute Engine doesn't automatically back up your resources, such as instances and disks, unless you configure a backup or replication option.
  * **Permanent deletion:** You can't recover a deleted instance, disk, or image, even if the deletion was accidental.



## Data protection options for instances

The following table summarizes data protection options for instances.

Data protection options for instances  
---  
Goal | Option | RPO | RTO | Use cases  
Testing or disaster recovery | Machine images | Minutes to hours | Minutes to hours | 

  * Stores an instance's configuration, metadata, permissions, and data from all attached disks.
  * Long term instance backup and restore.
  * Instance cloning and replication.

  
Disaster recovery | Backup and DR Service | Policy-defined | Minutes to hours | 

  * Defend against ransomware and improve cyber resilience with immutable and indelible backups.
  * Protect instances while retaining governance and oversight.
  * Comprehensive monitoring, auditing, and reporting for compliance.

  
  
### Instance testing and debugging

To clone an instance for testing or debugging, scaling instances, or system maintenance, use machine images.

#### Machine images

Machine images are ideal for cloning instances because they capture a comprehensive, point-in-time copy of your source instance, letting you clone your production environment without affecting it.

When you create a new instance from a machine image, the new instance is a clone of the source instance, including the full instance configuration and a crash-consistent copy of the data from all attached Persistent Disk and Hyperdisk volumes. To back up only your instance's disks, and not the full instance configuration, use standard or archive snapshots.

To learn more about machine images, see [About machine images](https://docs.cloud.google.com/compute/docs/machine-images).

### Instance backups for disaster recovery

To back up instances and their attached disks for disaster recovery, use machine images or [Backup and DR Service](https://docs.cloud.google.com/compute/docs/instances/backup-plans-for-instances).

#### Backup and DR Service

Backup and DR Service lets you create backup plans that define automated backup schedules, data retention policies, and replication strategies. We recommend Backup and DR Service for workloads with the following requirements:

  * Manage backups across multiple projects.
  * Advanced, policy-based automation.
  * Support for Google Cloud services, including Compute Engine VMs and VMware Engine VMs.
  * Protection from accidental deletion or malicious attacks by storing backups in secure, isolated backup vaults that support immutability and indelibility.
  * Cost efficiency with incremental backups.
  * Low RTO with features that enable instant mounting and in-place access to data directly from backups.



To learn more about Backup and DR Service, see [About Backup and DR Service back up plans](https://docs.cloud.google.com/compute/docs/instances/backup-plans-for-instances).

### Default back up settings for instances created in the Console

When you create a new instance using the Google Cloud console, Compute Engine uses a predefined default backup method until you change it. This encourages consistent use of automated backups across your project. One of the following options is automatically selected in the **Data protection** tab:

  * **Backup plan** : We recommend this option for most projects as it offers centralized, policy-based backups. If the Backup and DR API is enabled for your project, this option is your predefined default backup method.
  * **Snapshot schedules** : This option is selected if the Backup and DR Service isn't enabled. Snapshot schedules automatically backs up the disks attached to your instance on a regular basis, but it doesn't back up the full instance configuration.
  * **No backups** : This option means no backup method is preselected. You should only choose this if you have another method for protecting your data, or if the data is transient and doesn't require backups.



Regardless of the default backup setting, you can choose a different backup method when you create the instance to best suit the needs of a specific workload. This setting doesn't affect existing instances.

For detailed instructions on how to view or change your project's default backup setting, see [Configure the default backup setting for the console](https://docs.cloud.google.com/compute/docs/disks/default-backup).

## Data protection options for disks

The following table summarizes data protection options for disks.

Data protection options for disks  
---  
Goal | Option | RPO | RTO | Use cases  
Testing | Disk clones | Zero | Seconds to minutes | 

  * Quickly create staging environments from production.
  * Copy a disk for backup verification or export offloading.
  * Perform malware scans without impacting source disk performance.

  
Testing | Instant snapshots | Seconds to minutes | Seconds to minutes | 

  * Create a backup of a disk's data at a particular point in time that's saved in the same location as the source disk.
  * Fast rollback for user errors or failed software upgrades.
  * Stored as differential copies for better performance and space efficiency.

  
Testing | OS images | N/A | N/A | 

  * Create multiple instances with identical boot disks.
  * Create standardized development and testing environments.

  
Disaster recovery | Standard and archive snapshots | Minutes to hours | Minutes to hours | 

  * Geo-redundant disk backups for disaster recovery.
  * Stored as differential copies for better performance and space efficiency.

  
Disaster recovery | Synchronous replication | Zero | Seconds to minutes | 

  * Replicates data synchronously across two zones in the same region to provide high availability in the rare event of a _zonal_ outage.
  * Not designed for data backup.

  
Disaster recovery | Asynchronous Replication | Seconds to minutes | Minutes | 

  * Replicates data asynchronously across two regions to provide high availability in the rare event of a _regional_ outage.
  * Not designed for data backup.

  
  
### Disk testing and debugging

You can use clones, instant snapshots, or custom OS images to back up a disk for testing and debugging.

#### Disk clones

To create a ready-to-use copy of a disk, use a disk clone instead of creating a snapshot. Disk cloning creates an instantly usable, independent duplicate of a disk, which lets you work with production data in an isolated environment without disturbing your production workloads.

Unlike a snapshot, which is a backup that needs to be restored to a new disk, a clone is a new, fully functional disk that contains all the data from the source disk at the time of creation.

To learn more about disk clones, see [Duplicate a disk with clones](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks).

#### Instant snapshots

To quickly back up a disk for operational purposes, such software upgrades or system testing, use an instant snapshot. Instant snapshots are in-place backups stored in the same zone or region as the source disk, which lets you restore data to a new disk in minutes. This rapid recovery helps minimize downtime and avoid long maintenance windows.

Instant snapshots are designed for fast, operational recovery, not disaster recovery. Instant snapshots are stored in the same location as the source disk and are automatically deleted when the source disk is deleted. For long-term storage or disaster recovery, use standard or archive snapshots instead of instant snapshots.

To learn more about instant snapshots, see [About instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots).

#### OS Images

To create multiple new instances with identical boot disks or to create disks at scale, use a custom operating system (OS) image. You can create a custom OS image from an existing boot disk. An OS image is a complete, bootable copy of your disk, including the operating system, custom configurations, and any installed software. Once created, you can use the OS image as a reusable template to provision new boot disks for many VMs.

To create disks at scale, use OS images instead of creating multiple disks from a snapshot. OS images are faster because Compute Engine uses local caching in the target zones to accelerate the creation process.

To learn more about custom images, see [About OS images](https://docs.cloud.google.com/compute/docs/images).

### Disk backups for disaster recovery

You can use standard and archive snapshots to back up a disk for disaster recovery. You can also use synchronous and Asynchronous Replication to protect your applications from zonal or regional outages.

#### Standard and archive snapshots

To protect your data from regional or zonal failures, or for long-term archival, use standard or archive snapshots. Standard and archive snapshots are remote, geo-redundant backups designed specifically for disaster recovery and long-term data retention. While both types provide durable, incremental backups, they're optimized for different use cases:

  * Use standard snapshots to protect production data that might need to be restored with a faster recovery time than archive snapshots.
  * Use archive snapshots as a lower-cost storage option for data that's rarely accessed, such as backups required for compliance, audits, or long-term cold storage.



We recommend [scheduling hourly standard snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots). If you require daily snapshots, consider scheduling snapshots every 6 hours.

To learn more about standard and archive snapshots, see [About archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots).

### Disk replication for disaster recovery

For business-critical workloads that require high availability or disaster recovery capabilities, use disk replication to protect your applications from zonal or regional outages. Replication protects against infrastructure failure by maintaining a continuously updated copy of your data in another location. However, replication doesn't protect against data corruption, user error, or malicious attacks.

You can replicate your disk data either synchronously within a region or asynchronously between regions.

#### Protect against zonal outages with synchronous replication

If your workload can't tolerate any data loss (an RPO of zero) in the event of a zonal outage, use Regional Persistent Disk or Hyperdisk Balanced High Availability. These disks provide synchronous replication that writes data to two zones in the same region simultaneously.

This option is best suited for stateful, high-availability workloads that require a very low RTO. If a zone fails, you can failover your workload to the other zone in the region and continue operations with minimal disruption.

To learn more, see [About synchronous disk replication](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk).

#### Protect against regional outages with Asynchronous Replication

To replicate disk data between two different regions, use Asynchronous Replication. This protects your workloads against a complete regional outage by letting you failover your application to a secondary region. Asynchronous Replication offers a low RPO and low RTO and is ideal for critical workloads that must be recoverable in the event of a large-scale disaster affecting an entire region. To ensure your disaster recovery plan is effective, you can use Asynchronous Replication with [consistency groups](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups) to perform disaster recovery testing and to manage application failover and failback between regions.

To learn more, see [About Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).

## What's next

  * [Configure the default backup setting](https://docs.cloud.google.com/compute/docs/disks/default-backup) for an instance created in the console.
  * Read [Best practices for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
