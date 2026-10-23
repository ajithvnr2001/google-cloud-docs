---
url: https://docs.cloud.google.com/managed-lustre/docs/back-up-instance-data/
title: Back up instance data \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:30.472021+00:00
---

# Back up instance data  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/back-up-instance-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Back up instance data Stay organized with collections  Save and categorize content based on your preferences. 

If data on a Google Cloud Managed Lustre instance is accidentally deleted or corrupted, or if an instance is deleted, that data is not recoverable directly on the instance. Managed Lustre does not support undeleting files or recovering instances after deletion.

To protect against data loss, you should periodically back up your instance data by exporting it to a [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) bucket.

## Backup strategy with Cloud Storage

You can use Managed Lustre's built-in data transfer capability to export data from your instance directly to a Cloud Storage bucket.

For instructions, see [Transfer data to Cloud Storage](https://docs.cloud.google.com/managed-lustre/docs/transfer-data).

Key considerations for your backup strategy:

  * **Incremental exports** : Transfers from Managed Lustre to Cloud Storage are incremental. They only copy files that don't already exist in the destination bucket or that have changed since the last transfer.

  * **Deleted files** : Exports do not delete files in the destination bucket that have been deleted from the instance.

  * **Hierarchical namespace (HNS)** : For faster transfer speeds, consider using a Cloud Storage bucket with [hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/hns-overview).

  * **Storage classes** : To manage storage costs for long-term backups, consider using Cloud Storage [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes) (such as Nearline, Coldline, or Archive) or configuring [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) on your backup bucket. For details, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).

  * **Bucket location** : To avoid cross-region data transfer charges and minimize latency during backup and restore operations, create your backup bucket in the same region as your Managed Lustre instance.




## Automate periodic backups

To maintain regular backups, you can automate periodic data exports. For example, you can use:

  * **Cloud Scheduler** : Trigger exports on a recurring schedule by sending HTTP requests to the [`instances.exportData`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/exportData) REST API.
  * **Cron jobs** : Run scheduled scripts on a client Compute Engine VM or management instance using the [`gcloud lustre instances export-data`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/export-data) command.



## Restore data

To restore data from a Cloud Storage backup bucket, you import the data back into a Managed Lustre instance. Data import transfers are incremental, copying only files that don't already exist on the target instance or that have changed since the last transfer. If a file exists on both the instance and the backup bucket, the import overwrites the file on the instance with the backup version if the file has been modified.

For detailed transfer instructions and commands, see [Transfer data to or from Cloud Storage](https://docs.cloud.google.com/managed-lustre/docs/transfer-data).

Depending on your recovery scenario, you can restore data to an existing instance or recreate an instance from a backup:

  * **Restore data to an existing instance** :

    * Used to recover deleted or corrupted files, or to restore specific directories to an active instance.
    * You can restore an entire file system or specify a subdirectory path. If restoring to a subdirectory, that directory must already exist on the file system.
    * If a file on the instance has been modified or corrupted, importing the backup overwrites that file with the version from Cloud Storage.
    * To prevent write conflicts or data inconsistency during the import, pause client write activity or unmount clients from the target directory path.
  * **Recreate an instance from a backup** :

    * Used for disaster recovery or after an instance is accidentally deleted.
    * [Create a new Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance) with your chosen capacity, performance tier, and VPC network.
    * [Import the backup data](https://docs.cloud.google.com/managed-lustre/docs/transfer-data) from your Cloud Storage bucket into the root directory (`/`) of the new instance.
    * After the import operation completes, update your client mount configurations on [Compute Engine](https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine) or update your [Google Kubernetes Engine](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-existing-instance) `PersistentVolume` manifests with the new instance's IP address and file system name.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
