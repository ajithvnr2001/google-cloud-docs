---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-backup-data/
title: Access data in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:35.196787+00:00
---

# Access data in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-backup-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Access data in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Depending on the application type, how it is managed, and where it resides in the Backup and DR, the **Access** page lets you do the following:

  * **Mount** : This option provides instant access to data without moving it. Use standard mounts to mount an application's data, or an application aware mount to mount an entire application and its data as virtual applications. Mounting an active image is the fastest method. When you mount an image, you have full access to its data. Mounted images use a virtual copy that does not take additional storage. Captured copies of databases can be rolled forward using the appliance management console and mounted on any database server. For more information on mounting active images, see [Mount images](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-images).

  * **Clone** : This option is used to create an independent copy of a dataset. The most common uses include application development and testing, data audit for compliance, data warehousing, e-discovery, and user acceptance testing. Data sets can be copied to a separate storage location anywhere in your environment. For more information on clones, see [Clone](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone).

  * **LiveClone** : This option is similar to the clone function, but unlike a clone, a LiveClone can be updated on demand, or according to a schedule. When a refreshed copy of the data is available, LiveClone allows an independent copy of a dataset to be mounted, and then refreshes the primary data with the independent copy. This allows teams such as development and test to ensure they are working on the latest set of data without having to manually manage the data. The LiveClone image appears adjacent to the original data in the [ramp view](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-list-and-yaml#access-time) of the **Access** page. For more information on clones, see [LiveClone](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/liveclone).

  * **Restore.** This option initiates all copy data recovery options for a backup/recovery appliance and reverts the production data to a specified point in time. Restores and clones are the only data access operations that move data. Typically restore operations are performed to restore a database to a valid state after a massive data corruption. The amount of time required to complete a restore operation depends on the amount of data involved. For background information on restoring VMs and applications, see [Restore overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-overview).

  * **Test Failover, Failover, Syncback, and Fallback** : These replication options are unique to Backup and DR. They are used with StreamSnap managed applications to allow you to keep a remote copy of an application's storage and configuration up-to-date and ready to be used in a failover scenario, facilitating high-availability and redundancy. When a StreamSnap managed application fails for any reason, you can mount a failover image of the application from the remote site—remote snapshot. When the problem has been resolved, you can perform a restore to the local site with the syncback image for the latest changes and then failback the application to the production site. For detailed information on failover and failback, see [Failover and failback](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/failover-and-failback).

  * **Expire** : This option forces the expiration of an active image earlier than its scheduled time in order to gain storage space. For detailed information on expiring active images, see [Force expiration on active image](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-image-expiration).

  * **Mark Sensitive** : This option lets you mark an image as data sensitive. Only users with access to sensitive data are able to see this option. Sensitive images have a lock icon lock next to their name in the timeline ramp view and the sensitive data column set to **Yes** in the table view. For sensitive images, the actions drop-down provides you with the option of marking the image as non-sensitive.




## About data sensitivity

You can restrict access to sensitive data for certain users. This is necessary when dealing with patient data in the healthcare domain for example, or when using personal data in a test or development environment where confidential information must only be handled by a select group of users.

By default, administrators, and those with administrator privileges, have access to sensitive data. Your administrator can also give access to sensitive data to individual users or to all members belonging to a certain role.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
