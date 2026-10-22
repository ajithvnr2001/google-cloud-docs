---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/db2-recover-dump-to-new/
title: Recover a Full+Incremental backup of a Db2 database to a new target in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:11.165436+00:00
---

# Recover a Full+Incremental backup of a Db2 database to a new target in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/db2-recover-dump-to-new/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Recover a Full+Incremental backup of a Db2 database to a new target in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The following sections include information on recovering IBM Db2 databases from a Full+Incremental backup image to a new target.

## Procedure

To restore a file-based backup image to a new target, follow these instructions:

  1. From the Backup and DR appliance management console **Back Up & Recover** menu, select **Recover**.

**Note:** You can use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select the database to restore and click **Next**.

  3. Select the snapshot to recover the database from and click **Restore**.

  4. If you want to restore to a new target, then select **Restore to a new target**.

**Note:** The source and target databases should have the similar storage paths
  5. From the **Target** drop-down list, select the node for the new target.

  6. (Optional) Enter a descriptive **Label** to use for this job.

  7. **Replace Original Application Identity**. This option is only available when the restore target is a new host on the same backup/recovery appliance where the backup was originally generated.

     * **Yes** : This replaces the original application and has the same application ID, jobhistory, backup images and backup plan as the original application.
     * **No** : This does not replace the original application. It creates a new application that is discovered but not yet protected.
  8. **Included Databases** : This is pre-populated with the list of Db2 databases that will be restored. Select the databases that you want to include in the recovery.

  9. **Application Options** : In the **Target Instance Name** field, enter the name of the new Db2 instance that will be created by the restore job.

  10. Run the **Pre-Flight Check**.

     * If the pre-flight check fails, fix the issue and resubmit the pre-flight check.
     * If the pre-flight check is successful, click **Submit** to submit the restore job.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
