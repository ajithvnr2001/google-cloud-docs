---
url: https://docs.cloud.google.com/compute/docs/disks/default-backup/
title: Configure the default backup setting for the console \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:30.989940+00:00
---

# Configure the default backup setting for the console  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/default-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure the default backup setting for the console Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to choose, view, and change the option for a project's default backup setting. This page might also help you choose which backup setting you want to select when creating an instance.

When you create a Compute Engine instance in the Google Cloud console, you can specify the method that you want to use to back up your data. The _default backup setting_ is a project-wide Compute Engine setting that specifies which method is preselected by default when you create an instance in the Google Cloud console. For example, you can configure the default backup setting to help encourage a project to use your preferred method for automatically backing up data.

## Before you begin

  * To learn about the options that you can use to back up data, see [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection). Specifically, this page discusses options for automatically scheduled backups, especially [backup plans for backup vaults](https://docs.cloud.google.com/compute/docs/instances/create-instance-with-gcbdr-backup-plan) and [snapshot schedules](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules).




### Pricing

Some of the backup options incur additional costs when you create an instance. For more information, see the pricing for each option in Understand and choose the default backup setting in this document.

### Required roles

To get the permissions that you need to choose, view, and change the default backup setting, ask your administrator to grant you the following IAM roles on your project: 

  * View and change the default backup setting: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) 
  * If you want to use backup plans and need to enable the Backup and DR API: [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to choose, view, and change the default backup setting. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to choose, view, and change the default backup setting:

  * View and change the Compute Engine settings and metadata for the project: 
    * `compute.projects.setCommonInstanceMetadata`
    * `compute.projects.get`
  * Enable APIs: 
    * `serviceusage.services.enable`
    * `serviceusage.services.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Important:** Unless you configure your project to use the _no backups_ option by default, you need to also make sure each user that you want to be able to create instances has sufficient permissions to back up instances. For example, make sure each user has the Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`) role. For more information, see the requirements listed for each option in Understand and choose the default backup setting in this document.

## Understand and choose the default backup setting

The default backup setting for a project determines which backup method, if any, is automatically selected when you use the [**Create an instance** page in the Google Cloud console](https://console.cloud.google.com/compute/instancesAdd). Specifically, the default backup setting determines the backup method that is automatically selected in **Back up your data** section in the **Data protection** pane.

For reference, the **Back up your data** section lets you select which backup method, if any, to use for your data as follows:

  * Back up the instance using a backup plan for a backup vault.
  * Back up the disks using a snapshot schedule.
  * Don't use automatically scheduled backups.



Optionally, you can select a different option than the automatic selection.

Regardless of the default backup setting, if a backup method is selected, Compute Engine automatically selects a specific backup plan or a specific snapshot schedule to use. Optionally, you can select a different backup plan or different snapshot schedule before you finish creating the instance.

**Note:** For more information about which backup plan or snapshot schedule is automatically selected, see Options for the default backup setting.

### Limitations for the default backup setting

The default backup setting has the following scope:

  * The setting doesn't prevent users from selecting a different backup option.
  * The setting affects the project; it's not user specific.
  * The setting affects only the **Create an instance** page in the Google Cloud console.

    * When you use any other method to create an instance, its data is automatically backed up only if you configure it to.
    * The setting doesn't affect existing instances.

**Note:** If you want to change how data is automatically backed up for existing instances, you can learn how to [configure backup plans for existing instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup) and [configure scheduled snapshots for existing disks](https://docs.cloud.google.com/compute/docs/disks/manage-snapshot-schedules#change_snapshot_schedule_replace) instead.
  * This setting specifies only the type of backup option that's selected by default. It's not possible to customize the specific backup plan or specific snapshot schedule that is selected by default. To use a specific backup plan or snapshot schedule that isn't selected by default, select a different option while you're creating the instance.




### Options for the default backup setting

The options that you can use for the default backup setting are explained in the following table. Specifically, you can directly choose _backup plan_ , _snapshot schedule_ , or _no backups_ , but until you choose a default backup setting, your project uses a _predefined_ behavior.

Options for the default backup setting  
---  
Predefined (No option is selected) | 

  * **Use case:** All projects use this behavior until you change the default backup setting for your project or restore this behavior. 
  * **Effect:** Compute Engine automatically selects a default backup behavior that the project has enabled by using the following logic:
    * If Backup and DR has already been enabled for the project, then the project uses the same behavior as selecting the _backup plan_ option.
    * Otherwise, the project uses the same behavior as selecting the _snapshot schedule_ option.
  * **Requirements:** See the requirements for the _backup plan_ and _snapshot schedule_ options respectively.
  * **Pricing:** See the pricing for the _backup plan_ and _snapshot schedule_ options respectively.

  
Backup plan | 

  * **Use case:** We recommend this option for most projects. Review the use cases for the other options to see if your project is an exception. **Caution:** If your project [automatically applies a backup plan to new instances by using tags](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/dynamic-protection), we recommend you use the _no backups_ option. Otherwise, when instances use the default backup plan, the tag-based backup plan won't be applied to prevent redundancy. 
  * **Effect:** When you're creating a new instance, backup plans are selected by default to back up data. Specifically, the backup plan that is automatically selected is the default backup plan for the region that contains the instance. When you create an instance, Compute Engine automatically creates a default backup plan and default backup vault for the region as needed and if they don't already exist.
    * The _default backup plan_ runs daily between midnight and 6:00 AM in the local timezone for the region, is stored in the default backup vault for the region, and each backup is retained for a maximum of 14 days. The default backup plan is named `default-compute-instance-plan-REGION`. Replace `REGION` with the region that contains the instance; for example, `us-central1`.
    * The _default backup vault_ has a minimum enforced retention period of 1 day. The default backup vault is named `default-vault-REGION`. Replace `REGION` with the region that contains the instance; for example, `us-central1`.
  * **Requirements:**
    * To use this option, the project must have the Backup and DR API enabled. **Roles required to enable APIs** To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). [Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com)
    * Make sure each user that you want to be able to create instances with this option has the [permissions required to apply a backup plan during instance creation](https://docs.cloud.google.com/compute/docs/instances/create-instance-with-gcbdr-backup-plan#required-roles).
    * Backup plans are applied to an instance and its disks only when your configuration supports it. Whenever a user creates an instance that uses this backup plan, make sure the user verifies that the configuration complies with the [limitations for applying backup plans during instance creation](https://docs.cloud.google.com/compute/docs/instances/create-instance-with-gcbdr-backup-plan#limitations).
  * **Pricing:** Backup plans and vaults incur additional costs. For more information, see [Backup and DR pricing](https://docs.cloud.google.com/backup-disaster-recovery/pricing).

  
Snapshot schedule | 

  * **Use case:** We recommend this option only if any of the following are true for your project:
    * You want to or already store backups in multi-regional locations. For more information about when to use multi-regional locations, see [Snapshot storage locations](https://docs.cloud.google.com/compute/docs/disks/snapshots#snapshot_storage_location).
    * You don't match the use case for the _no backups_ option and can't meet the requirements for _backup plan_ option.
  * **Effect:** When you're creating a new instance, snapshot schedules are selected by default to back up data. Specifically, the snapshot schedule that is selected by default varies. If the project already has compatible snapshot schedules, the automatic selection is the snapshot schedule that comes first in alphabetical order. Alternatively, if no compatible snapshot schedule exists, the automatic selection is a default snapshot schedule for the region that contains the instance. Compute Engine automatically creates the default snapshot schedule when needed.
    * The _default snapshot schedule_ runs daily at 6:00 PM UTC, is located in the region that contains the instance, stores snapshots in the [multi-region](https://docs.cloud.google.com/storage/docs/locations#location-mr) that contains the instance, and each snapshot is retained for a maximum of 14 days. The default snapshot schedule is named `default-schedule-1` for each region.
  * **Requirements:**
    * Make sure each user that you want to be able to create instances with this option has the [permissions required to attach a snapshot schedule to a disk](https://docs.cloud.google.com/compute/docs/disks/manage-snapshot-schedules#required_roles_and_permissions).
    * Snapshot schedules are applied to a disk only when your configuration supports it. Whenever a user creates an instance that uses snapshot schedules, make sure the user verifies that the configuration of the instance and each disk complies with the [limitations for snapshot schedules](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules#limitations).
  * **Pricing:** Snapshot schedules incur additional costs. For more information, see [Compute Engine disk snapshot pricing](https://cloud.google.com/compute/disks-image-pricing).

  
No backups | 

  * **Use case:** Use this option only when one or more of the following are true for your project:
    * You're confident that you will have other options to recover your data if it's lost due to unforeseen events. For example, you already use tags to automatically apply backup plans, or you maintain replicated data in a separate location.
    * You're confident that your data won't need to be recovered if it's lost. For example, you only use the project for experimental workloads.
    * You can't meet the requirements for the other options.
    * You can't incur the additional costs for the other options.
  * **Effect:** When you're creating a new instance, data is not automatically backed up by default. **Warning:** If you don't back up or replicate your data and your data is deleted or corrupted for any reason, then you won't be able to recover that data. 
  * **Requirements:** This option doesn't have any requirements.
  * **Pricing:** This option doesn't incur additional costs.

  
  
## View the default backup setting for a project

To view the default backup setting for a project, do the following:

  1. If you haven't already, open the project that you want to view settings for in the Google Cloud console.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the Google Cloud console, go to the **Settings** page for Compute Engine.

[Go to Settings](https://console.cloud.google.com/compute/settings)

The **Default data protection** section displays the option that your project uses for the default backup setting. If none of the radio buttons are selected, then your project uses the _predefined_ behavior.




## Change the default backup setting for a project

To change the default backup setting for a project, do the following in the Google Cloud console:

  1. Review the options for the default backup setting and decide which option you want to use. For the selected option, ensure that it matches your use case and that you meet the requirements.

  2. If you haven't already, open the project that you want to change settings for in the Google Cloud console.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Based on the option that you want to choose for the default backup setting, do one of the following:

     * If you want to choose the _backup plan_ , _snapshot schedule_ , or _no backups_ option, then complete the following steps:

       1. In the Google Cloud console, go to the **Settings** page for Compute Engine.

[Go to Settings](https://console.cloud.google.com/compute/settings)

       2. For **Default data protection** , choose the new option.

       3. Click **Save**.

     * If you want to revert to the _predefined_ behavior that Compute Engine had automatically selected for the project, complete the steps to [remove project metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#remove-custom-project-wide-metadata) for the `google-compute-default-data-protection` metadata entry.




## Update the default backup setting for all projects in an organization at once

If you want to set or update the default backup setting for all projects in an organization at once, then you can't use the Google Cloud console. Instead, you can use gcloud CLI to update the setting in the project metadata and automate this update across all projects in the organization. To perform this automation, follow these steps:

  1. Review the options for the default backup setting and decide which option you want to use. For the selected option, ensure that it matches your use case and that you meet the requirements.

  2. Create a script to automate running the [`gcloud compute project-info add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata) for all projects in the organization. Specify the `--metadata google-compute-default-data-protection` flag with the value of the option that you want to change the default backup setting to. Consider the following examples:

     * To set or update the default backup setting across all projects in the organization to **No backups** , use the following command in your script:
           
           gcloud compute project-info add-metadata \
           --project=PROJECT_NAME \
           --metadata=google-compute-default-data-protection=NONE
           

     * To set or update the default backup setting across all projects in the organization to **Backup plan** , use the following command in your script:
           
           gcloud compute project-info add-metadata \
           --project=PROJECT_NAME \
           --metadata=google-compute-default-data-protection=BACKUP
           

     * To set or update the default backup setting across all projects in the organization to **Snapshot schedule** , use the following command in your script:
           
           gcloud compute project-info add-metadata \
           --project=PROJECT_NAME \
           --metadata=google-compute-default-data-protection=SNAPSHOT_SCHEDULES
           

Replace `PROJECT_NAME` with the name of the project.

To learn more about setting and updating your project's metadata, see [Set and remove custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).




## What's next

  * Learn how to [create and start an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  * Learn how to [restore an instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore).
  * Learn how to [restore an instance from a snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
