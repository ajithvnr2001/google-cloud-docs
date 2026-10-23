---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-to-generic-apps/
title: Back up a generic application in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:16.762865+00:00
---

# Back up a generic application in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-to-generic-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up a generic application in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Before you can manage a generic application, you must copy scripts to a specific folder on the database server. For details on those scripts, consult the database administrator's guide for the database to be protected.

Use these instructions to apply a backup template and manage:

  1. In the appliance management console, click the **App Manager** menu and select **Applications** from the drop-down menu. The **Applications** page opens.

  2. Select the **Generic** application (LVM) that you want to manage, and then **Manage Backup Plan** from the drop-down list at the bottom right corner of the page. The **Manage Backup Plan** page opens.

  3. From the **Manage Backup Plan** page, choose from the **Template** and **Profile** drop-down lists:

     * **Template.** An existing backup template that includes policies to define the local storage or replication of the application data.

     * **Profile.** An existing resource profile that defines the resources used to store the data of the application as local or replicated backups.

The **Manage Backup Plan** page shows a view of the policies assigned to the selected applications in the backup plan policy map. Data capture management comes from the template policies and profiles that you designed in the backup plans.

  4. Click **Apply Backup Plan**. The **Apply backup plan** page opens.

  5. Configure the database or instance details and settings or policy overrides settings.

     * **Application Settings** : Configure application-specific settings like backup data capture method (required). See [Configure application settings for generic application (LVM)](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-generic-apps) for details.

     * **Policy Override** : Override specific policy settings previously configured in the selected backup template. Advanced settings can be useful or required in certain circumstances. See [Configure advanced settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) for details.

**Note:** You can override policy settings only if the policy template **Allow Overrides on Policy Settings** parameter has been set to **Yes**.
  6. Click **Manage Volumes** to open the **Manage Volumes** dialog.

**Note:** The settings in the **Manage Volumes** dialog reflect the settings selected when the **Generic** application was created. In most cases you won't need to make any changes.
     1. Select the eligible volumes to protect.

     2. In case there are a large number of volumes, use the search box to find a specific volume.

     3. Verify that the **Generic LVM script name** is the `genlvmscript.sh` script.

     4. For **LVM snapshot reserve space** , change the reserve space as needed. By default it is 20%.

**Note:** **Generic Application** (LVM) leverages LVM snapshots along with the LVM script to achieve application consistency. This is the space LVM will consume to track changes to production volumes when an LVM snapshot is in effect. By default it is 20%.
     5. Click **Save** to save the manage membership configuration.

  7. Click **Apply Backup Plan** to apply the backup template and resource profile. A success message opens.

  8. Click **Okay**.

If you back up a workload to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back the data up to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.

The application might not get backed up until the scheduled job runs according to the hours of operations defined in the backup template. For example, if at 10:00 (UTC) you assign a template that has hours of operation from 02:00 to 05:00 (UTC), then the first job won't start until the appliance has an available job slot at 02:00 (UTC) of the following day. To run a job immediately, see [perform an on-demand capture](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).

**Note:** All policies start and end times are in UTC time zone.

**Note:** To reset one or more application settings back to its default state, click the **Reset to Default** checkbox to the right of the selection you want to reset, or click **Reset All to Default** to reset all application selections back to their default state.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
