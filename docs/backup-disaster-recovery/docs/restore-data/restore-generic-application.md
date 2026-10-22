---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-generic-application/
title: Restore and recover generic applications in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:16.446097+00:00
---

# Restore and recover generic applications in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-generic-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore and recover generic applications in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The Restore function reverts the production data to a specified point in time. You can restore a generic application to its original host or to a replacement host at the same IP address, overwriting the existing data.

Restoring replaces the original production application data with the specified point-in-time backup. This restoration results in the loss of all current application data as the application is restored to its status at the point-in-time when the backup was created. This operation cannot be undone.

Typically restore operations are performed to restore a database to a valid state after events such as unexpected data corruption. The amount of time required to complete a restore operation depends on the amount of data involved.

## Restore a generic application

To restore a generic application:

  1. Click the **App Manager** tab and select **Applications** from the drop-down menu. The **Applications** page opens.
  2. Select the generic application that has the backup that you want to restore, then choose **Access** from the drop-down list. The **Access** page opens listing captured backups in the timeline ramp view. For more information on the view, see [Access the timeline ramp view of a backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time). Snapshot backup type supports restore operation.
  3. Select the backup then select **Restore** from the list of access operations. The **Restore** page opens.
  4. Select a single volume or multiple volumes to restore. By default all volumes are selected.
  5. Click **Submit**. A warning dialog opens. 
  6. Read it and then enter `DATA LOSS` to confirm. A second warning appears.
  7. Enter `OVERWRITE OTHER APPS` to confirm the restore operation.

The restore job starts. You can verify that the restore operation is successful by viewing the job status in the **Monitor**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
