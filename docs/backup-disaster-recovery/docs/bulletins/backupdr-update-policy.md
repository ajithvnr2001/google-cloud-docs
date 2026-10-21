---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/bulletins/backupdr-update-policy/
title: Backup and DR update policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:01:52.001303+00:00
---

# Backup and DR update policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/bulletins/backupdr-update-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Backup and DR update policy Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the update policy for backup/recovery appliances.

Google Cloud Backup and DR regularly releases updates for backup/recovery appliances, which includes bug fixes, security patches, and enhancements. Most updates are automated and don't require user action. However, some updates require you to manually update backup/recovery appliances.

As described in the [Google Cloud Backup and DR Support Services Guide](https://cloud.google.com/terms/gcbdr-services-guide), Backup and DR only supports the current version (n) of the backup/recovery appliance and one version immediately preceding the current release (n-1) with bug fixes and patches. Backup/recovery appliances earlier than version (n-1) are not supported.

Backup and DR notifies you of available updates to backup/recovery appliances through in-product notifications in the management console. You can also check the update status of the appliances on the **Appliances** page in the **Update Status** column.

To keep your backup/recovery appliances current, update them to the latest available version when it is in **Pending** or **Overdue** status. If you don't update your backup/recovery appliances regularly, their status changes to **Out of support**. In this state, you are restricted from enabling backups on any new entities or applications until you install the update.

The following are the possible statuses:

  * **Up to date** : indicates the appliance is running on the latest version and no action is required.
  * **Pending** : indicates the appliance has a new available update to install. To install the update, go to **Manage** > **Appliance Updates**.
  * **Overdue** : indicates the appliance is running on an earlier version and must be updated immediately. To install the update, go to **Manage** > **Appliance Updates**.
  * **Out of support** : indicates that the appliance version is earlier than the supported version and needs to be updated immediately. You can't back up any new entities or applications until you update the backup/recovery appliance to the supported version. Existing backups continue to run according to schedule and existing backup images can be restored.



For instructions on how to update an appliance, see [Update backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
