---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-to-consistency-group/
title: Back up a consistency group in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:25.684764+00:00
---

# Back up a consistency group in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-to-consistency-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up a consistency group in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Use these instructions to apply a backup template and manage:

  1. In the appliance management console, click the **App Manager** tab and select **Applications** from the drop-down menu. The **Applications** page opens.

  2. Select a **Consistency Group** that you want to manage. Select **Manage Backup Plan** from the drop-down list at the bottom right corner of the page. The **Manage Backup Plan** page opens.

  3. Choose from the **Template** and **Profile** drop-down lists:

     * **Template.** An existing backup template that includes policies to define the local storage or replication of the application data.
     * **Profile.** An existing resource profile that defines the resources used to store the data of the application as local or replicated backups. See [Create a resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles#create-profile) for details.

The **Manage Backup Plan** page shows a view of the policies assigned to the selected applications in the backup plan policy map. Management comes from the template policies and profiles that you designed in the backup plans.

  4. Click **Apply Backup Plan**. The **Apply backup plan** page opens.

  5. Configure the database or instance details and settings or policy overrides settings.

     * **Application and Settings** : Apply application-specific settings when managing a consistency group application data capture. Application settings can be useful or required in certain circumstances. See [Configure application settings for capturing consistency groups](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-to-capture-consistency-groups) for details.

     * **Policy Overrides** : Override specific policy settings previously configured in the selected backup template. Advanced settings can be useful or required in certain circumstances. See [Configure policy overrides](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) for details.

**Note:** You can override policy settings only if the policy template **Allow Overrides on Policy Settings** property has been set to **Yes**.
  6. Click **Apply backup plan** to apply the backup template and resource profile. A success message opens.

  7. Click **Okay**.

If you back up a consistency group to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back the data up to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.

The application might not get backed up until the scheduled job runs according to the hours of operations defined in the backup template. For example, if at 10:00 (UTC) you assign a template that has hours of operation from 02:00 to 05:00 (UTC), then the first job won't start until the appliance has an available job slot at 02:00 (UTC) of the following day. To run a job immediately, see [perform an on-demand capture](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).

**Note:** All policies start and end times are in UTC time zone.

To change backup plan settings for the application, see [Modify backup plan management of a managed application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application). To disable a backup plan, see [Removing backup plan management of an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings).


**Note:** To reset one or more application settings back to its default state, click the **Reset to Default** checkbox to the right of the selection you want to reset, or click **Reset All to Default** to reset all application selections back to their default state.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
