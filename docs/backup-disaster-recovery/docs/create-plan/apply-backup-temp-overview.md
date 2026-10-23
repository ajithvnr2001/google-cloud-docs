---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-overview/
title: Apply a backup template using the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:52.271764+00:00
---

# Apply a backup template using the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Apply a backup template using the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

In the appliance management console, you protect an application by assigning a resource profile and a template to it. This defines a backup plan to back up the application data.

**Note:** This is an overview of the procedure in the appliance management console. When you are ready to protect an application, see the specific procedure for that application type.

To apply a backup template:

  1. In the appliance management console, click the **App Manager** tab and select the **Applications** option from the drop-down list. The **Applications** page opens.

  2. Select the application that you want to protect, and then choose **Manage Backup Plan** from the drop-down list at the bottom right corner of the page. The **Manage Backup Plan** page opens.

  3. Choose from the **Template** and **Profile** drop-down lists:

     * **Template.** An existing backup template that includes policies to define the snapshot or replication of the application data.
     * **Profile.** An existing resource profile that defines the resources used to store the data of the application as snapshot or replicated backups.

The **Manage Backup Plan** page shows a view of the policies assigned to the selected applications in the backup plan policy map. Data backup comes from the template policies and profiles that you designed in the backup plans.

  4. Click **Apply Backup Plan**. The **Apply Backup Plan** page opens.

  5. Configure the application's details and settings and policy overrides settings.

     * **Application Settings.** Apply application-specific settings. Application settings can be useful or required in certain circumstances.
     * **Policy Overrides.** Override specific policy settings previously configured in the selected backup template.
**Note:** You can override policy settings only if the policy template **Allow Overrides on Policy Settings** property has been set to **Yes**.
  6. Click **Apply backup plan** to apply the backup template and resource profile. A success message displays.

  7. Click **Okay**.

If you back up a workload to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back up the data to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.

The application might not get backed up until the scheduled job runs according to the hours of operations defined in the backup template. For example, if at 10:00 (UTC) you assign a template that has hours of operation from 02:00 to 05:00 (UTC), then the first job won't start until the appliance has an available job slot at 02:00 (UTC) of the following day. To run a job immediately, see [perform an on-demand capture](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).

**Note:** All policies start and end times are in UTC time zone.

To change backup plan settings for the application, see [Modify backup plan management of a managed application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application). To disable a backup plan, see [Removing backup plan management of an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application#remove).


**Note:** To reset one or more application settings back to its default state, click the **Reset to Default** checkbox to the right of the selection you want to reset, or click **Reset All to Default** to reset all application selections back to their default state.

## Disable or remove a backup plan from an application

You can disable a backup plan, temporarily suspending backup jobs, and you can remove a backup plan from an application entirely, while keeping it available for other applications.

To disable or remove a backup plan:

  1. Click the **App Manager** tab and select the **Applications** option from the drop-down list. The **Applications** page opens.

  2. Select the application that you want to unprotect, and then choose **Manage Backup Plan** from the drop-down list at the bottom right corner of the page. The **Manage Backup Plan** page opens, showing the template and profile that are applied to the application.

  3. Click the drop-down at **Apply**. The options to **Disable** and **Remove Backup Plan** appear.

     * Disabling the plan leaves it associated with the application but suspends all backup jobs until you re-enable protection in the same way that you disabled it (**Disable** now appears as **Enable** for the selected application).

     * Removing the plan removes it from the application but keeps it available for other applications.


**Note:** To delete a template from the system completely, see [Delete a backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template#del-temp).

## Application-types specific protection procedures

  * [Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery)
  * [VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)
  * [File systems and Filestore](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-plan-to-filesystem)
  * [Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)
  * [Microsoft SQL server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/sql-protect)
  * [SAP HANA databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/configure-sap-backupmethod)
  * [Other databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/otherdb-required-settings)
  * [Generic applications (LVM)](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-to-generic-apps)



## What's next

  * Get an overview of [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan)
  * Create a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * Create a [backup policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview)
  * Create a [resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles)
  * Configure [advanced policy settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) of an application backed up by the policy



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
