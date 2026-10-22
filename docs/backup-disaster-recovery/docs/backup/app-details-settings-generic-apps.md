---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/
title: Configure application details and settings for generic applications in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:58.331496+00:00
---

# Configure application details and settings for generic applications in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure application details and settings for generic applications in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

From the appliance management console **Application Details & Settings** page, you can modify application-specific settings for capturing **Generic Apps** —other LVM (logical volume manager) applications not listed in the appliance management console. Application settings may be useful or required in certain circumstances. After you configure your application settings, click **Save Changes**.

**Note:** To reset one or more application settings back to its default state, click the **Reset to Default** option beside the setting. To reset all settings, click **Reset All to Default**.

The following is a list of application settings with descriptions. 

  * **Backup and DR agent options** : Leave Backup and DR agent options blank unless you are working with support.
  * **Freeze and Thaw Script Name** : Location of the custom script on the host. Scripts are called to freeze or unfreeze an application before a job.
  * **Percentage of Reserve Space in Volume Group** : This is the space logical volume manager consumes to track changes to production volumes when an logical volume manager snapshot is in effect. By default it is 20%.
  * **Use Buffered Copy** : Select from **Yes** or **No** —default.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
