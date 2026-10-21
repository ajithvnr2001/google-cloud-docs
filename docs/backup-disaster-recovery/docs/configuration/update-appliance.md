---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance/
title: Update backup/recovery appliances \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:21:37.452178+00:00
---

# Update backup/recovery appliances  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Update backup/recovery appliances Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains how you can update your backup/recovery appliance. Backup and DR requires you to be compliant with the [update policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/bulletins/backupdr-update-policy) in order to remain supported on your backup/recovery appliance.

Backup and DR provides two kinds of updates:

  * **Hotfix** : this includes system updates, security fixes, and critical bug fixes related to Backup and DR components. Backup and DR installs hotfixes automatically when they become available. You can check the status of the update on the **Installation Jobs** page. Sometimes, the automatic installation of a hotfix may fail even after multiple retries. In these cases, you need to install the hotfix manually.

  * **Patch** : this includes new features, enhancements, and bug fixes. There are two types of patch updates. 

    * **Auto-patch updates** : Most updates are automated. These updates don't require manual installation, reboot, or disruption to the backup/recovery appliance. Auto-patch updates are applied only on backup/recovery appliances that are in the "Out of support" state. For example, if N (11.0.17) is the latest version available, and a backup/recovery appliance is on unsupported version N-2 (11.0.15), then auto patch upgrades only move the appliances to N-1 (11.0.16), and not to the latest version (11.0.17).

By default, the auto update is set to update after two weeks from the date that the update is available. You can set the default time slot to automatically apply the auto updates to the appliances. You can also schedule the update for a specific date and time. All auto upgrades will be carried out during the selected default time window. Note that you must maintain at least a six-hour gap between the start time and end time to update the appliance. For more instructions on setting a default window, see Set a Default Window for Auto-patch Updates If the auto patch update fails to install automatically, it becomes visible on the **Available updates** page, where you can update the appliance manually. These updates are displayed as `AUTO_PATCH_NUMBER` on the **Available updates** page. However, you can reschedule the updates to one month. For instructions on updating the appliance, see Install updates.

    * **Manual updates** : these updates require manual installation. These are displayed as `PATCH_NUMBER` on the **Appliance updates** page. We recommend updating an appliance to the latest available version whenever an update is available. Before installing the patch, ensure all the prerequisites are met. If the **Install or schedule updates** page's **Reboot required** column is displayed as **Yes** , the appliance reboots automatically after the update. No manual reboot is required. You can schedule manual updates to be installed at a scheduled time. For instructions on updating the appliance, see Install updates.




## IAM roles and permissions

To get the permissions that you need to update an appliance, ask your administrator to grant you the [Backup and DR Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set a default window for Auto-patch updates to install

  * Select one or multiple days of the week as default window.
  * Select a time slot within the day for the same.
  * The auto-patch updates will happen 2 weeks after discovery of the update in one of the day of the week selected and within the given time slot . 



## Update notifications

Backup and DR displays an update notification in the following scenarios:

  * When a new update is available for installation
  * When an update is scheduled for installation within the next 24 hours
  * When an update installation is in progress
  * When an update installation has succeeded or failed



You can view notification details by clicking the  notifications  icon.

If the update-type is auto-patch, two new notifications will be displayed:

  * When an update is scheduled for installation within the next 2 weeks
  * When an update is scheduled for installation within the next 1 week



## Appliance status

Appliance can have one of the following statues. You can check the status appliance from **Manage** > **Appliances**.

  * **Up to date** : This indicates the appliance is running on the latest version and no action is required.
  * **Pending** : This indicates the appliance has a new available update to apply. See Install updates to update the appliance.
  * **Overdue** : This indicates the appliance is running on earlier versions and must be updated immediately. See Install updates to update the appliance.
  * **Out of support** : This indicates the appliance is older than the supported version and needs to be updated immediately. You cannot back up any new entities or applications until you update the backup/recovery appliance to the supported version. See Install updates to update the appliance.



## View available updates

To view available updates, click **Manage** and select **Appliance Updates**.

The **Available Updates** page displays the following fields:

  * **Update name** : This field displays update name as `PATCH_NUMBER`, `AUTO_PATCH_NUMBER` for a patch, or `HF_NUMBER` for a hotfix. Click an update name to view [release notes](https://docs.cloud.google.com/backup-disaster-recovery/docs/release-notes) for a patch or a dialog listing details for a hotfix.
  * **Appliance status** : This field displays the status of an update as follows:

    * **Pending** : By default, whenever an update is available, it displays the status as **Pending**. When you install an update on demand, you are directed to the **Installation Jobs** page displaying the progress of the update.
    * **Scheduled** : If you schedule an update for installation at a particular time and date, it displays the status as **Scheduled**. See Install an update at a scheduled time for more information.
    * **Rollback available** : If the Backup and DR releases a rollback for the applied hotfix update, it displays the status as **Rollback available**.
  * **Expected duration** : This field displays the approximate time that it takes to update an appliance.

  * **Due date** : This field displays the date by when the update must be installed.

  * **Published on** : This field displays the date when the update was published.




## Install updates

You can apply updates in two ways—on demand or scheduled.

### Before you begin

The following are the prerequisites that must be met before you install an update:

  * Don't run or schedule any backup or restore jobs while installing an update.
  * Ensure that the utilization of snapshot and primary pools is less than 90%. To check the pool utilization, go to **Manage** > **Storage Pools** and check the **Used(%)** column for the snapshot and primary pools associated with the appliance. If **Used(%)** is more than 90%, add an extra disk to the [snapshot pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/snapshot-pool#disk) or [primary pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/primary-pool), and then continue with an update.
  * If you're installing a patch update:

    * You must handle active backups (mounts) to avoid preflight check failures: 
      * **For GCE workloads and agent-based workloads** : Use [Forget](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#forget) or [Unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete). The **Unmount** option is not available for these workloads.
      * **For Backup and DR snapshots** : Use [Unmount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount).
**Note:** Only the available options are shown in the appliance management console. For example, if you see `Forget mount` then you won't see `Active mounts`.**Caution:** Choosing **Unmount and delete** removes the backup from the appliance and deletes the data. This data cannot be reclaimed after the task has been performed.
    * Disable the scheduler before installing the update. You can enable it after the update, see [Enable or disable expirations and schedules](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#enable_or_disable_expirations_and_schedules).



### Install an update on demand

Use the following instructions to install an on-demand appliance update:

  1. Click **Manage** and select **Appliance Updates**.
  2. Right-click an update name—for example, `PATCH_NUMBER`, `AUTO_PATCH_NUMBER`, or `HF_NUMBER`— and select **Install or Schedule Updates**.
  3. Select the appliance that you want to apply the latest update to. You can also select multiple appliances to update all the appliances at the same time. By default, the **Install Now** is selected.

**Note:** The backup/recovery appliance reboots automatically after the update is applied if the **Reboot Required** column displays **Yes**. You don't need to manually reboot the appliance.
  4. Click **Apply**. When the update installation process starts, the **Installation Jobs** page opens. This is where you can [check the status of the update](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance#installation).




### Install an update at a scheduled time

Before scheduling an update, ensure that you have selected the correct time zone from the appliance management console. The scheduled updates run based on the selected timezone. For information on updating the timezone, see [change the timezone](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#timezone).

You can schedule updates only for Compute Engine and Google Cloud VMware Engine instances. You cannot schedule updates for backup/recovery appliances that protect agent-based workloads such as file systems and databases.

Use the following instructions to schedule updates.

  1. Click **Manage** and select **Appliance Updates**. The available updates appear. By default, the status of the update is **Pending**.
  2. Right-click an update name—for example, `PATCH_NUMBER` or `HF_NUMBER`or `AUTO_PATCH_NUMBER` —and select **Install or Schedule Updates**.
  3. Select the appliance that you want to apply the latest update to. If you want to update the appliances at the same time, then select multiple appliances.

**Note:** The backup/recovery appliance reboots automatically after the update is applied if the **Reboot Required** column displays **Yes**. You don't need to manually reboot the appliance.
  4. Select **Install Later**.

  5. Click the calendar icon to select when you want to install the update.

  6. Click **Apply**. The **Status** column of the update changes to **Scheduled**.

The installation process for the scheduled update starts within 15 minutes of the scheduled time.




### Edit a scheduled update

Use the following instructions to edit a scheduled update.

  1. Click **Manage** and select **Appliance Updates**.
  2. Right-click an update name—for example, `PATCH_NUMBER` or `HF_NUMBER`— and select **Edit Update Schedule**.
  3. Select the appliance you want to edit the existing schedule of. You can also select multiple appliances if you want to edit and schedule an update at the same time.
  4. Edit the schedule by changing the timestamp from the calendar.
  5. Click **Apply**.



### Cancel a scheduled update

Use the following instructions to cancel a scheduled update.

  1. Click **Manage** and select **Appliance Updates**.
  2. Right-click an update name —for example, `PATCH_NUMBER` or `HF_NUMBER`—and select **Cancel Scheduled Updates**.
  3. Select the appliance that you want to cancel applying the latest update to. You can also select multiple appliances if you want to cancel the update on multiple appliances at the same time.
  4. Click **Apply**.



## Monitor installation jobs

The **Installation Jobs** page displays the status of appliance updates.

Use the following instructions to view installation job updates.

  1. Click **Manage** and select **Appliance Updates**.
  2. Select **Installation Jobs**. This page displays the following fields:

     * **ID** : This field displays the unique ID of an update.
     * **Update name** : This field displays update name as `PATCH_NUMBER` for a patch, or `HF_NUMBER` for a hotfix. Click an update name to view [release notes](https://docs.cloud.google.com/backup-disaster-recovery/docs/release-notes) for a patch or a dialog listing details for a hotfix.
     * **Status** : This field displays the following statuses when an update is applied. Hold the pointer over a status field for more information about the update status.

       * **Downloading** : This status displays when an update is being downloaded onto the appliance.
       * **Checking** : This status displays when performing preflight checks.
       * **Installing** : This status displays when an update is being installed.
       * **Success** : This status displays when an update is installed successfully.
       * **Failed** : This status displays when an installation of the update fails. Review the logs and try to Install the update again.
       * **Skipped** : This status displays when you skip to install an update on an appliance.
       * **Rollback in progress** : This status displays when a rollback is in progress onto the appliance.
       * **Rollback success** : This status displays when an update is rolled back successfully.
       * **Rollback failed** : This status displays when the rollback of an update fails.
     * **Update type** : This field displays the type of update, such as `Manual` for manual patch updates and `Auto` for hotfixes and automatic patch updates.

     * **Appliance** : This field displays the name of the appliance you are installing the update on.

     * **Started** : This field displays the timestamp of when the installation of an update started.

     * **Ended** : This field displays the timestamp of when the installation of an update completed. This field is populated only when an update installation is successful or failed.

     * **Logs** : This field displays the logs of an update. If the installation of an update fails, view the update logs to debug the failed update and then Install the update again.

During installation, the **Installation Jobs** page displays the progress of an update. Based on the progress, the status of an update changes to **Success** or **Failed**.


**Note:** If the installation of an update fails, check the error message from the update logs and fix the underlying issue before attempting to Install the update again.

## View the update logs

Use the update logs to debug a failed update and fix the issue before attempting to install the update again.

Use the following instructions to view update logs.

  1. Click **Manage** and select **Appliance Updates**.
  2. Select **Installation Jobs**.
  3. Click **Logs**. The following log files are displayed for an appliance:

     * `patch-XXX-preflight-info.log`: This file contains the logs of the preflight checks that are executed on the appliance.
     * `patch-xxx-preflight-error.log`: This file contains the error logs of the preflight checks that are executed on the appliance.
     * `autoupdate-patch-xxx-updatelog`: This file contains the update installation logs for the appliance.



## After a successful update

After successfully updating an appliance, you must perform the following tasks to ensure that the updated appliance functions correctly.

  1. Navigate to the **Manage** > **Appliance Updates** > **Installation Jobs** page and ensure that the appliance update status is **Up to date**. The **Up to date** status displays only when all the relevant updates on the appliance are installed.
  2. Navigate to the **Manage** > **Appliances** page and check the appliance management console and backup/recovery appliance connection status in the **Connectivity Status** column. The **Green** tick mark indicates that the connectivity is successful.
  3. Enable the [schedules](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#enable_or_disable_expirations_and_schedules).
  4. [Remount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#remount) the unmounted backups.
  5. Run any [backup jobs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run) to validate if the backups are running as expected after updating the appliance.



## Rollback a hotfix update

If the Backup and DR detects an issue with an applied hotfix update, it may rollback the update automatically. However, if the Backup and DR is unable to rollback the update, then you need to rollback the update manually. You can view available rollbacks in the **Available Updates** page with the status **Rollback Available**.

Rollbacks don't lead to a downtime as appliances don't reboot during or post rollback.

Use the following instructions to rollback a hotfix update.

  1. Click **Manage** and select **Appliance Updates**.
  2. Right-click a hotfix update name—for example, `HF_NUMBER`—and select **Rollback**.
  3. Select any appliances that you want to rollback the update.
  4. Click **Apply**. When the update rollback process starts, the **Installation Jobs** page opens. This is where you can check the status of the rollback.

If rollback fails, contact Google Cloud Customer Care to resolve the issue.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
