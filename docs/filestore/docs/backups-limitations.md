---
url: https://docs.cloud.google.com/filestore/docs/backups-limitations/
title: Backup limitations \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:41.011071+00:00
---

# Backup limitations  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/backups-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Backup limitations Stay organized with collections  Save and categorize content based on your preferences. 

The following sections cover limitations related to creating and managing backups.

## General limitations

Filestore backups can't be combined with the [Filestore multishares](https://docs.cloud.google.com/filestore/docs/multishares) feature.

## Performance

  * For highly utilized instances, the performance may be reduced by as much as 15% while a backup is uploaded. Basic tier instance performance is not affected by backup `create` operations.

  * Storing an instance's data to multiple backup chains does impact backup performance. Expect higher latency on backup `create` operations when alternating between backup chains.

  * Instance operations such as instance `restore` or instance `delete` may be delayed until a backup `create` operation completes.

  * In some cases, `delete` operations may take up to 24 hours to complete.




## Operations concurrency

  * Backup `delete` operations associated with the same source instance must be performed one at a time.

  * Bulk backup `delete` operations within a backup chain are not supported. While a `delete` operation is pending, any new `delete` operations within the same backup chain return a `RESOURCE_EXHAUSTED` error. This is regardless of whether the source instance has been deleted. If the source instance has been deleted, you receive a `FAILED_PRECONDITION` error.

**Note:** This limitation doesn't apply to basic SSD and basic HDD service tier instances.

Filestore supports concurrent backup `delete` operations when backups reference separate source instances.

For example, an instance labeled `Source1` has backup data referenced in `Backup1` and `Backup2`. `Source2` has backup data referenced in `Backup3` and `Backup4`. `Backup1` and `Backup2` can't be deleted in parallel, however, `Backup2` and `Backup3` can.

  * Backup `create` and backup `delete` operations initiated within the same backup chain _can_ run concurrently. When you've already started creating a new backup, you have to wait until the operation completes to delete the most recent existing backup. This is because the most recent backup contains the most critical data needed to successfully complete the backup `create` operation. If you try to delete the most recent backup, you will receive the `FAILED_PRECONDITION` error. 

For example, `Source1` has a backup chain composed of `Backup1` and `Backup2`. When you begin a `create` operation for `Backup3`, you can't delete `Backup2` until the `create` operation completes.

  * For more information about operation rate limits, see [Operation rate limits for backups](https://docs.cloud.google.com/filestore/docs/limits#rate-limits-backups).




## Storage

  * You can restore a backup of a basic instance to the source instance of the same service tier, an already existing instance, or a new instance. If you choose a new instance, you can choose between basic HDD and basic SSD instances regardless of the source instance tier.

  * You can't restore zonal, regional, and enterprise instances to a source or existing instance, only to a new instance. The new instance tier doesn't have to match the source instance tier. For example, you can restore a backup of a regional instance to a zonal instance. The provisioned capacity of the new instance must be equal to or exceed the provisioned capacity of the source instance.




## Capacity

  * Backups created for zonal, regional, and enterprise instances might consume instance capacity. This capacity varies relative to the scope of changes made to the data since the backup was created. More specifically, when a backup is created, Filestore creates an internal snapshot of the file system which also occupies a portion of available instance capacity.

  * Snapshot size is _also_ relative to the scope of changes made to data within the share since the last backup was created. This snapshot continues to exist until the next subsequent backup is created and uploaded.

  * All data referenced by the backup persists in the state as it was when captured and continues to take up capacity from the file system. So for example, if you were to delete data from the mounted file system, that action itself won't free up capacity. Instead, to do so, you would create a new backup after deleting or overwriting significant amounts of data.

  * To anticipate sufficient capacity for your workloads, consider applying one of the following:

    * Increase instance capacity for workloads with significant, frequent data changes or a high change rate.

    * Take frequent backups. If the last backup is stale, the internal snapshot might accumulate more changes and consume more instance capacity.




## Encryption

When using CMEK to encrypt your backup chains, the following limitations apply:

  * An entire backup chain is encrypted using the same CMEK.

  * When creating a backup with CMEK, CMEK must reside in the same region as the target backup.

  * If storing a backup chain in a region separate from the source instance, you might need to apply separate keys, one for the source and one for the backup chain.

    * All service tiers support multiple backup chains, or the ability to store an instance's backups in multiple regions. If electing to use CMEK for encryption, a CMEK key must reside in the same region as the resource it encrypts. If you're storing backups in a region separate from the source, and the CMEK is not a multiregion key, you must use separate CMEK keys. For more information, see [CMEK restrictions](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys#restrictions) and [Choosing the best CMEK location](https://docs.cloud.google.com/kms/docs/locations#choosing).
  * A single CMEK is applied to the Cloud Storage bucket where the backup chain is stored and cannot be combined or replaced.

  * CMEK support is not available for basic tier backups.




For more information, see [CMEK support for backup chains](https://docs.cloud.google.com/filestore/docs/cmek#cmek_support_for_backup_chains).

## Data migration

After you create a Filestore instance, you can't change its location or service tier. To migrate your data to another region, you can create a backup of it and use the backup to create a new Filestore instance or restore it to an existing instance.

## Protocols

When restoring a backup, the new instance must use the same [protocol](https://docs.cloud.google.com/filestore/docs/about-supported-protocols) as the source instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
