---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery/
title: Protect and recover a Compute Engine instance from the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:36.671556+00:00
---

# Protect and recover a Compute Engine instance from the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Protect and recover a Compute Engine instance from the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an end-to-end overview about how to back up and restore your Compute Engine instance and monitor backups.

## Configure backup for Compute Engine instances

A Compute Engine instance is a VM hosted on Google Cloud. Each instance stores data on persistent disks that are attached to the instance. You can [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) or [create a group of managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) by using the Google Cloud console, the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the Compute Engine API.

For more detailed information, see [Compute Engine](https://docs.cloud.google.com/compute).

## Prerequisites to configure backup

Before you start backing up Compute Engine instances, read the following procedures and deploy Backup and DR:

  * [Plan a Backup and DR deployment](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan)

  * [Prepare to deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-prep)

  * [Deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-guide)




After deploying the Backup and DR, you can create a backup plan template and protect Compute Engine instances by applying the backup plan template to the instance.

### Create a backup plan template

This section will help you in creating a backup plan template. Backup plan templates are composed of backup policies. In policies, you can define when to run a backup, how frequently to run a backup, and how long to retain the backup image for **Days** , **Weeks** , **Months** , or **Years**.

**Note:** You can only use snapshot policy in your backup plan template to backup Compute Engine instance. If your backup plan template includes OnVault or StreamSnap policies, then it can't be used to backup Compute Engine instance.

Use these instructions to create a backup plan template:

  1. In the appliance management console, click the **Backup Plans** drop-down menu and select **Templates**.

  2. Click **\+ Create Template**.

  3. In the **Template** field, enter a name for the backup template in the format of an alphanumeric text string. Spaces, underscores (_), and dashes (-) are allowed in a name. Don't include special characters.

  4. In the **Description** field, enter a brief description for the backup template.

  5. Add the production to snapshot backup policy in either ways:

     * Click the **Plus sign icon (+)** in the backup plan policy map.
     * Click **\+ Add** in the **Policies** dialog.
  6. In the **Production to Snapshot** policy page, do the following:

     1. In the **Policy name** field, enter a name for the policy.

     2. Select the **Scheduling** type as **Windowed** or **Continuous**. The default is **Windowed**.

        * **Windowed.** Defines a discrete snapshot backup schedule adhering to a specific frequency and time window —for example, perform a backup every 30 minutes, daily from 09:00 to 17:00 UTC. You can instruct the backup/recovery appliance to run multiple backup jobs at a specified frequency interval or once during a specified time window.

        * **Continuous.** Defines a continuous snapshot backup schedule—for example, perform a backup job every eight hours, starting the first job at 01:00 UTC. In this policy schedule, jobs run continuously (24/7) at the specified time interval.

Configure the policy frequency settings per the selected schedule type as outlined in the following lists:

### Windowed

        * **On these days:** Configures the frequency of the policy by defining an interval at which snapshot images are captured. Based on this interval setting, the snapshot job runs once every specified number of days, weeks, months, or years. Click the link of this parameter and modify the **Run** interval.

The schedule is displayed in a calendar view. From this view you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes accordingly based on your selection.

        * **Except:** Defines an exception to the **Run** schedule. You can specify an **Except** value of daily, weekly, monthly, or yearly. For example, to skip the daily snapshot schedule every Friday, select weekly and select Friday. Click the link of this parameter and modify the exception.

The schedule is displayed in a calendar view. From this view you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes accordingly based on your selection.

        * **Within this window:** Defines a start and end time window for capturing images.

        * **Run once per window:** Specifies that the frequency duration for capturing snapshot images is once during the specified **Run between** time window.

        * **Every:** Specifies a repeat frequency duration (minutes or hours) for capturing snapshot images during the specified **Run between** time window. For example, every two hours.

### Continuous

        * **Every:** Specifies the time period to repeat the snapshot image capture in.

        * **Starting at:** Specific the time of day to run the first job in the continuous cycle of image captures at.

     3. Leave remaining fields to the default and click **Create Policy**.

  7. Click **Save Template**. A backup plan template is created.




### Apply a backup plan template

To apply a backup plan to the Compute Engine, first you need to discover and add the Compute Engine to the appliance management console. After discovering a Compute Engine in a project, you can apply a backup plan template to it.

Use the following steps in the appliance management console **Onboarding Wizard** to discover Compute Engine instances and apply backup plan template.

  1. In the appliance management console, click the **Back up & Recover** drop-down menu and select **Back up**.

  2. Select **Compute Engine**.

  3. Select a **Cloud Credential**.

  4. Select an appliance from the **Appliance** drop-down, if the credential is created on multiple appliances, and click **Next**. If you aren't able to locate the appliance in the list, see [cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials).

  5. Select the **Project ID** and **Zone** then click **Search** to list the instances available in the project and zone. If you can't find your project in the **Project ID** drop-down, click **Don't see your project ID here** and it lists the missing permissions

  6. Click **Next**.

  7. Select an instance and select **Apply a Backup Template** from the **Action** drop-down. If no instances appear, then ensure that the zone selected matches with the zone where your Compute Engine instances are located and running. Only new instances are displayed by default. You can change the options from the drop-down to see previously discovered instances.

  8. Select a backup template from the **Backup Template** drop-down and click **Ok**.

  9. From the **Volume Options** , you can select for each VM whether to protect all disks or just the boot volume.

  10. Click **Next**.

  11. Review the summary screen. If everything is correct, select **Finish** to enable a backup plan for Compute Engine instances. The selected Compute Engine instances are backed up with the selected backup template.

  12. Click **Finish** in the confirm finish dialog.

  13. After the onboarding is complete, a dialog appears. Click **Finish** again.

After the backup plans are applied to Compute Engine instances, the status changes to a green check mark. The green check indicates that your instance is onboarded successfully. You can view your onboarded Compute Engine instance from **App Manager** > **Applications** to page.




Backup and DR ensures that the chosen Compute Engine instances get backed up per the frequency set in the backup policy.

## On-demand backups

On-demand backup is a type of backup that you can manually trigger at any time. On-demand backups are useful for situations where you need to backup your data before a specific event. For example, you might want to backup your VM before applying updates or patches to ensure that you can restore it to its previous state if any issues arise during the update process.

To run an on-demand backup of a managed application:

  1. Click the **App Manager** tab and select the **Applications** option from the drop-down list. The **Applications** page opens.
  2. Select an Compute Engine instance and then click **Manage Backup Configuration** from the drop-down list at the bottom right corner of the page.
  3. From the **Policies** that is on the right, select **Snapshot**.
  4. Enter a **Label** and click **Run Now**. An on-demand backup will be triggered for the selected policy.



## Restore a Compute Engine instance

You can restore the source Compute Engine instance using **Restore** operation and restore instance to an alternate location using the **Mount** operation.

### Restore a Compute Engine instance to source instance

Restore is the process of restoring data from a backup image. You can restore the instance to the source location, use the **Restore** operation. For instructions on how to restore a Compute Engine instance, see [Restore a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-compute-engine).

### Restore the Compute Engine instance to the alternate location

You can restore a Compute Engine instance to an alternate location, using the **Mount** operations.

Use the following instructions to perform the mount:

  1. From the appliance management console, go to **Back up & Recover** > **Recover**. Select the Compute Engine instance you want to recover and click **Next**.

  2. Select a point in time backup image from which you want to recover the Compute Engine instance and select **Mount**.

  3. Select **Mount As New Compute Engine Instance**.

  4. Review all the configuration options. There are at least two that you should change:

     * **Zone** : Change this to a different zone to simulate recovering to a different region in the Google Cloud.

     * **Instance Name** : Change the instance name by adding a suffix so it goes from centos-7 to centos-7-recovered.

  5. Click **Mount**.

A **Mount** job starts. You can monitor the job from from **Monitor** > **Jobs**. The job might take five minutes or longer depending on what region you selected.

The recovered VM is displayed in the Google Cloud console from the **Compute Engine** > **VM Instances**.

If you want to mount instance to an alternate region or to an alternate project, see [Mount Compute Engine instance backup image as a new instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances#new).




### Manage the active mount

As the backup/recovery appliance created this Compute Engine instance, even though it isn't managing the disks for this instance, it still tracks it. There are two options:

  * **Unmount and delete** : This deletes the Compute Engine instance and its disks removing the active mount.

  * **Forget the active mount** : This removes the mount record from Backup and DR but leaves the Compute Engine instance in place. A Compute Engine administrator needs to manage the lifecycle of this instance from now on.




#### Delete the instance

Delete the instance using the following instructions:

  1. In the appliance management console, click the **App Manager** drop-down menu and select **Active Mounts**.

The active mount with the name you gave your new Compute Engine instance appears.

  2. Right-click the mount and select **Unmount and Delete** , then click **Submit**. You can monitor it from **Monitor** > **Jobs** and the new Compute Engine instance is gone.




#### Forget the instance

Forget the instance using the following instructions:

  1. In the appliance management console, click the **App Manager** drop-down menu and select **Active Mounts**.

The active mount with the name you gave your new Compute Engine instance appears.

  2. Right-click the mount and select **Forget Active Mount** , then click **Submit**. You can monitor it from **Monitor** > **Jobs**.

The new Compute Engine instance isn't listed in the appliance management console **Active Mounts** panel, but is still be present in Compute Engine.




## Monitor

You can monitor the Compute Engine jobs, from the [monitor jobs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs) and [monitor events](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-events).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
