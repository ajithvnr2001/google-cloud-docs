---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-consistency-group/
title: Restore and recover consistency groups in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:41.914644+00:00
---

# Restore and recover consistency groups in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-consistency-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore and recover consistency groups in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The Restore function reverts the production data to a specified point in time. Restoring replaces the original production application data with the specified point-in-time image. This restoration results in the loss of all current application data as the application is restored to its status at the point-in-time when the image was created. This operation cannot be undone.

Typically restore operations are performed to restore a database to event such as unexpected data corruption. The amount of time required to complete a restore operation depends on the amount of data involved.

Before you begin the consistency group restore process, note the following considerations:

  * Be very careful when restoring databases in a consistency group. When you restore databases that are in a consistency group, ALL databases in the consistency group are overwritten. If you don't want to overwrite all databases in the consistency group, first mount a single database, then use the manual VSSRESTORE command to copy the database files to the required location.
  * For a SQL Server failover instance, the database is always restored to the active node. The appliance management console mounts the backup image to the active node and performs the restore operation on the node. For SQL Server Availability Groups, the restore is also performed on the active node.



## Restore a consistency group

To restore a consistency group:

  1. Click the **App Manager** tab and select **Applications** from the drop-down menu. The **Applications** page opens.
  2. Select the **Consistency Group** that you want to restore, then choose **Access** from the drop-down list. The **Access** page opens listing backup images in the timeline ramp view. Image types that support a Restore operation include snapshot, and remote snapshot (StreamSnap images).

The timeline ramp view is a time-based visualization of backups for the selected application. Use your mouse to select a backup to restore. See [Access the Timeline Ramp View of an Image](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time) for details.

Background differentiates snapshot images containing database with transaction log files, and also illustrates the restore range time period for the logs.

  3. Select an image and then select **Restore** from the list of access operations. The **Restore** page opens.

  4. If the source application is protected by a snapshot policy that has enabled database log backups, and logs are available with the image, you can use them to roll forward to a specific point in time by changing these options in the **Roll Forward Time** section:

     * The **Date** field contains all possible dates that the database can be rolled forward to (through the application of database transaction logs). Select the date you need the database to be rolled forward to.
     * The **Time** field contains a slider showing all possible times on the selected date that the database can be rolled forward to. If you select the latest possible date and then move the slider to the right most position, the restore job applies to all available logs. If you select the earliest possible date and move the slider to the left most position, the restore job will apply no logs.
     * You can specify to roll forward using either **User Time** or **Host Time**. User Time is relative to the local time of the current user. Host time is relative to the system that hosts the data to be restored.
  5. Select a single volume or multiple volumes to restore. By default all the volumes are selected.

  6. For a consistency group with a database, check the **Restore With Recovery** checkbox if you don't intend to roll the database logs. Restore with recovery option brings the restored database online. Once the database is online, logs cannot be applied.

  7. Click **Submit** . The image is restored. If restoring a consistency group with a database, the backup/recovery appliance creates a new database image populated with data copied from the selected point-in-time image.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
