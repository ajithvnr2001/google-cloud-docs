---
url: https://docs.cloud.google.com/vmware-engine/docs/update-center/
title: Update a private cloud \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:48.983856+00:00
---

# Update a private cloud  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/update-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update a private cloud

When new software becomes available from VMware, VMware Engine tests the software, then makes it available to you through the VMware Engine Update center.

You can use the Update center to perform the following updates:

  * **Version updates** : an update to a VMware component that introduces new features and upgrades the VMware stack version.
  * **Maintenance patches** : a patch that fixes a specific issue in a VMware component.
  * **Security patches** : a patch that fixes a security issue in a VMware component. Google runs security patches as soon as they are available, you can't schedule them in the Update center.



Version updates and maintenance patches are _schedulable updates_ , which means that you can plan for them and control when they run. Security patches are _non-schedulable updates_ , which means that you can't control when they run.

## Required permissions

To get the permissions that you need to use Update center, ask your administrator to grant you one of the following [IAM roles](https://docs.cloud.google.com/vmware-engine/docs/iam):

  * **VMware Engine Viewer** (`roles/vmwareengine.viewer`): view updates and announcements
  * **VMware Engine Admin** (`roles/vmwareengine.vmwareengineAdmin`): view and schedule updates



If you plan to use [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles), the role must include the following permissions:

  * To view updates and announcements: 
    * `vmwareengine.upgrades.list`
    * `vmwareengine.upgrades.get`
    * `vmwareengine.announcements.get`
    * `vmwareengine.announcements.list`
  * To schedule updates, you also need the following permission: 
    * `vmwareengine.upgrades.update`



## Update notifications

After an update becomes available, VMware Engine sends the following update notifications:

**Note:** Start date and time is shown in the Coordinated Universal Time (UTC) time zone.

  * **Update Announcement:** a notification sent to all users about a maintenance patch or a security patch that will become available within seven days, or within 30 days for any version updates.

  * **Scheduling Available:** a notification about the default update schedule of your private cloud. You can change the default schedule for version updates and maintenance patches up to 15 days before the default start date. You can change the schedule up to 15 days from the default start date of the update.

  * **Update Start:** a notification about the start of an update for your private cloud.




Notifications are shown on the Google Cloud console, vCenter UI, and NSX UI. Email notifications are sent to addresses listed in the **Technical** category in [Essential Contacts](https://docs.cloud.google.com/essential-contacts/docs/managing-contacts). If you don't specify any contacts in the **Technical** category, notifications are sent to users with project owner IAM roles.

## Schedule private cloud updates

After you receive a _scheduling available_ notification for your private cloud, you can view the default update schedule and daily window of updates, or update the schedule and daily update windows for version updates and maintenance patches. You can make changes to the update schedule, including its start date, until 15 days before the default start date.

If you don't make changes to the schedule, the update runs using the default schedule.

**Note:** You can't change the start date of the update beyond 15 days from the default start date.

  * **Scheduled Start Date:** the date and time when the update operations start. Start time defaults to the week of the day's start time window. For example if the start date is on a Wednesday, the start time of the update uses the start time of Wednesday's window start time.

  * **Daily Update Window:** updates are performed during this window on a daily basis on day of the week basis. 




### Preparation

Google recommends taking the following preparations before starting an update or upgrade:

  * **Check storage capacity:** Ensure your vSphere cluster's storage space utilization is lower than 80% to maintain the [SLA](https://docs.cloud.google.com/vmware-engine/sla). If the utilization is higher than 80%, upgrades might take longer than normal or fail completely. If your storage utilization is higher than 70%, [add a node](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#add-nodes) to expand the cluster and avoid any potential downtime during upgrades.
  * **Change vSAN storage policies with FTT of 0:** Change VMs configured with a vSAN storage policy for Failures to Tolerate (FTT) of 0 to a vSAN storage policy with FTT of 1 to maintain the SLA.
  * **Remove VM CD mounts:** Remove any CDs mounted on your workload VMs that are not compatible with vMotion.
  * **Complete VMware tool installations:** Complete any installations or upgrades of VMware tools before the scheduled upgrade begins.
  * **Remove SCSI bus sharing on VMs:** Remove SCSI bus sharing on VMs if you don't want the VMs to be powered off.
  * **Remove inaccessible VMs and datastores:** Remove unused and inaccessible VMs from the vCenter inventory. Remove any inaccessible external datastores.
  * **Disable Distributed Resource Scheduler (DRS) rules:** DRS rules that pin a VM to a host prevent a node from entering maintenance mode. You can disable the DRS rules before the upgrade and enable them after the upgrade is complete.
  * **Update VMware add-ons and third-party solutions:** Verify that VMware add-ons and third party solutions deployed on your private cloud vCenter are compatible with the post-upgrade versions mentioned previously. Examples of tools include those for backup, monitoring, disaster recovery orchestration, and other similar functions. Check with the solution vendor and update ahead of time if necessary to ensure compatibility after the upgrade.



### View or change the update schedule

When you schedule an update, you must provide an update window, which lets you to control when the update runs. Updates are performed only during this window and pause until the next window allows updates to continue. You must specify a minimum update window of 40 hours per week, spread across multiple days, with a minimum of 8 hours required for each selected day in the update window. For example, if you selected an update window of all day (24 hours) on Sunday, you would need to include a 16 hour window on another day of the week to meet the minimum hours per day requirement.

The more time you include in your weekly update window, the earlier your update is projected to end. As you adjust your update window, the Update center calculates an estimated end date and time, based on the total estimated update time. For example, if the total estimated update time is 120 hours and you select an update window of 40 hours per week, the update takes 3 weeks to complete and the Update center shows you an estimated end date and time which is 3 weeks from the start date.

To change an update schedule do the following:

  1. In the Google Cloud console, go to the **Update center** page.

[Go to Update center](https://console.cloud.google.com/vmwareengine/upgrades)

  2. From the list of private clouds, click the **More actions** more_vert button in the row of the private cloud that you want to update.

  3. Click **Review schedule**. The **Review update schedule** page opens.

  4. Review and optionally edit the following:

     1. In the **Start date** field, modify the start date for the update. The start date must be within 15 days of the default start date and must be on a day of the week that is included in the update window. You can make changes to the start date from when you receive the _scheduling available_ notification up to 15 days before the default start date.
     2. In the **Update window** section, edit the update window by selecting a combination of days and times that are permissible for the update to occur. A minimum of 40 hours is required, with a minimum of 8 hours per day.
  5. Review **Estimated end date and time** , then click **Schedule update**.




VMware Engine starts the update on the start date, at the start time specified for the day of the week that the start date falls on. VMware Engine pauses the update outside of the times specified in the maintenance window.

### View details or view update status

To view the status of an update, do the following:

  1. In the Google Cloud console, go to the **Update center** page.

[Go to Update center](https://console.cloud.google.com/vmwareengine/upgrades)

  2. Click **View details**.




Updates can be in one of the following states:

  * **Scheduled by default** : The update has a default schedule that you can review and edit until 7 days before the default start date.
  * **Scheduled by user** : The default update schedule was changed by a user.
  * **In progress** : The update is ongoing.
  * **Paused** : The update is paused and waiting for the next specified window, or an issue was found and the update will resume after it's fixed.
  * **Canceled** : The update was canceled by the system.
  * **Failed** : The update failed.
  * **Completed** : The update was completed and the private cloud is operational.



Additional information about the private cloud and update type are shown on this page.

**Note:** Components update and version information will show **-** for security updates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
