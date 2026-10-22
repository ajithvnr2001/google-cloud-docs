---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-appliance/
title: Manage backup/recovery appliances \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:07.085090+00:00
---

# Manage backup/recovery appliances  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage backup/recovery appliances Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup/recovery appliances are centrally managed from the [appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/introduction). From the **Manage** > **Appliances** page, you can manage appliance capacity heath, configure appliance settings, manage Backup and DR agents, update appliances, configure appliance networking, and remove appliances.

## Overview of all backup/recovery appliances

From this page, you can see information for each managed backup/recovery appliance, such as the following:

  * The **Name** of the appliance.
  * The **Appliance ID**.
  * **Connectivity Status** : Whether the connection to the appliance management console is active or stale (not reachable based on the last synchronization). 
  * The **IP** address of the appliance management console appliance.
  * **Appliance Capacity Health** : Links to a dashboard that shows this appliance's data change rate and snap count over the last 24 hours compared to the appliance's recommended capacity limit. If the current value exceeds the recommended value, monitor it for a few days, and consider adding more disks or other resources if it is underprovisioned, or creating a new appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.
  * The **Machine Type** : e2-standard-4, e2-standard-16, or n2-standard-16.

  * The date and time that the appliances was **Last Synchronized** with the appliance management console. If the appliance management console and backup/recovery appliance's connectivity status shows red and the last synchronization time is less than 30 minutes from the current time, contact [customer support](https://docs.cloud.google.com/backup-disaster-recovery/docs/support) to resolve the issue. Due to networking changes, backup/recovery appliances connectivity status may be temporarily down. However, they will automatically re-establish connectivity and sync with the appliance management console.

  * The appliance **System Version**.

  * **Version** : The appliance version is the first two numbers in the system version, so you don't need to show this column if you show the **System Version** column.

  * **Error** : This only shows a value when there is a system error.

  * **Timezone** : The time zone that the appliances uses for scheduling jobs.

  * **Service Account** : The service account used in deploying the appliance.

  * **Zone** : The Google Cloud zone in which the backup/recovery appliance is deployed.

  * **Project ID** : The Google Cloud project in which the backup/recovery appliance is deployed.

  * **Region** : The Google Cloud region in which the backup/recovery appliance is deployed.

  * The **Update Status** of the appliance, as follows:

    * **Up to date** : This indicates the appliance is running on the latest version and no action is required.
    * **Pending** : This indicates the appliance has a new available update to apply. You can apply the update to the appliance from the **Manage** > **Appliance Updates**.
    * **Overdue** : This indicates the appliance is running on earlier versions and must be updated immediately. You can update the appliance from the **Manage** > **Appliance Updates**.
    * **Out of support** : This indicates the appliance is older than the supported version and needs to be updated immediately. You cannot back up any new entities or applications until you update the backup/recovery appliance to the supported version. You can apply the update to the appliance from the **Manage** > **Appliance Updates**.
**Warning:** Don't rename the backup/recovery appliance, as the resources generated during deployment, such as the service account, Google Cloud credentials, firewall rules, and managed appliance, are not renamed. Renaming of the appliance is not supported at this time.



To modify the display of fields that appear in the **Appliances** table, follow these steps.

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu. The **Appliances** page opens listing all appliances managed by the appliance management console.
  2. To modify the display, you can do the following:

     * **Adjust Fields** : To modify the fields that appear in the table, right-click within the table header row and click the checkboxes for the fields you want displayed–or clear them for fields you don't want to view.
     * **Sort Content** : To sort the content listed in a table column by alphanumeric order, select a column header and then click the **Up** or **Down** arrow to change the order.
     * **Adjust Column Width** : To adjust the width of a table column to show more content in the table, drag the column divider in a column header to the left or right to resize the column width. Column dividers are marked by a pair of thin gray lines.
     * **Filter By** : To filter the list, click **show filter**. Enter one or more filter criteria as appropriate. To clear a filter, click **x** to the right of the applied filter.
**Note:** Filters that are of type text, list, and date persist across different appliance management console sessions for the same user.
  3. To export the appliances list, click the **Export** icon. You can export the appliances list in PDF format.




## Filter by appliance

You can filter the appliance-related data shown in the appliance management console.

To filter data by appliance:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Click the **Filter** icon in the top right-hand corner of the **Appliances** page.

Data related to only the selected appliance is shown. This information varies depending on the appliance selection.

  3. From the drop-down menu, select the **Appliances** that you want to filter.

  4. Click **Save**.




## Resources summary

The **Resources Summary** page provides an at-a-glance view of the status of an appliance. It includes usage information and the warning threshold for VDisks.

When usage of any of these resources reaches or exceeds the warning threshold, the appliance performance can suffer. To avoid this issue, [contact support](https://docs.cloud.google.com/backup-disaster-recovery/docs/support) for guidance and solutions.

## View and manage VDisk usage

A VDisk is a virtual disk on an appliance that imports the appliance's hosts, applications, users, and roles. The appliance is presented to the host as a unit of usable storage capacity.

You use VDisks for each LUN, VMDK, database, or file system protected, with each volume comprising a snapshot of an application, and each LUN comprising a mount or clone of an application.

To view the number of virtual disks on an appliance:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens. Select an appliance.

  2. Click **Configure Appliance**.

The **Appliance Configuration** page opens.

  3. Select **Resources** from the left navigation panel.

  4. Select the **VDisks** tab.

Under **VDisk Usage** , the following information is provided:

     * The number of VDisks in use
     * The number of available VDisks
     * The total VDisk capacity



### Top Ten VDisks list

The **Top Ten VDisks** list shows the ten applications that have the maximum number of virtual disk copies. These are usually snapshots, mounts, or clones.

### Change the warning threshold for VDisks

If the number of virtual disks created on an appliance exceeds the warning threshold, a warning is posted to the event log. You must reduce disk consumption or add another appliance to share the load.

The default warning threshold for VDisks usage is 90%. To change the warning value, drag the threshold value to the new value and click **Save**.

**Caution:** Change the warning threshold only if your usage requirements justify a different value. Consult support as they can help. Before changing the warning threshold, follow the steps in the next section to reduce disk consumption.

### Reduce VDisk consumption

Perform the following tasks to reduce VDisk consumption:

  * If you are not using one yet, deploy an E2-Standard-4 "Standard for Compute Engine VMs or SAP HANA databases" backup/recovery appliance and use that to protect up to 5,000 Compute Engine VMs, Cloud SQL instances, and SAP HANA and IBM Db2 databases that are backed up to Persistent Disk disks.

  * Reduce the number of snapshots kept for an application by changing the policy template or backup rule used by a backup plan to reduce the time that backups and logs are retained on the backup/recovery appliance before being replicated to OnVault storage.

  * Delete unneeded mounts, clones, and LiveClones.

  * Change VMware VMDKs that don't need to be protected to **Independent Mode** , as these cannot be protected by VMware snapshots.

  * Group Microsoft SQL Server databases from a single host together into a consistency group. For example, if a single host has 9 SQL databases, create one **Consistency Group** for that host and include all nine databases, then protect that group rather than the individual databases. In this example, VDisk consumption is reduced from nine to one.




## Replication

You can configure the bandwidth used to replicate StreamSnap backup data from one backup/recovery appliance to another so that two appliances can share the bandwidth available to your organization with other organizational resources. Throttling determines the amount of bandwidth you want to dedicate to an appliance for your data replication.

When two backup/recovery appliances are paired for replication (see [Data replication](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-replication)), you can choose to set the maximum bandwidth used for this replication. The bandwidth setting is made from the point-of-view of the originating appliance, called the A-side. When choosing this bandwidth setting, the bandwidth chosen represents the amount of traffic originating from this appliance to appliance B. If appliance A replicates to appliances B and C simultaneously, bandwidth throttling is set independently for appliance A to appliance B and appliance A to appliance C. For example, for paired appliances A and B bandwidth throttling can be 10Mbps while paired appliances A and C can be 100Mbps.

### Configure bandwidth throttling

Use the **Bandwidth Throttling** feature to limit the bandwidth used by the replication process between appliances.

  * **Enable Bandwidth Throttling** : Set Throttling to **On** if you plan to limit the maximum amount of bandwidth available for appliance replication (Steam Snap). You can restrict bandwidth usage by turning on bandwidth throttling and limiting the maximum amount of bandwidth that the appliance shouldn't exceed for each type of replication.

  * **Disable Bandwidth Throttling** : Set Throttling to **Off** if you don't want to restrict the amount of bandwidth used for appliance replication. This option lets you use the maximum available bandwidth.




Use these instructions to turn bandwidth throttling on or off with a bandwidth limit:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Setup** page.

  4. Go to **System** , then **Configuration** , then **Appliance Settings**.

  5. Click the **StreamSnap** tab if you have to turn bandwidth throttling on or off for StreamSnap replication.

  6. To enable bandwidth throttling, click **On**.

**Note:** If you choose not to restrict the maximum amount of bandwidth used for backup/recovery appliance replication, click the **Off** button to disable bandwidth throttling.
  7. Click **Yes** to override existing triggers or to configure a constant bandwidth value.

  8. Enter the new bandwidth in **Set bandwidth value to**. A value of zero means unlimited bandwidth.

  9. Click **Save** to update the bandwidth configuration settings.




### Schedule bandwidth throttling

During various times of the day or week you may want a backup/recovery appliance to use less bandwidth so that other priority services can use this bandwidth. You can customize the bandwidth throttle so that it runs automatically based on predefined schedules (triggers).

This section describes how to schedule bandwidth throttles. Each schedule specifies the amount of bandwidth that you want to allocate during the interval and time. You can create separate schedules for weekdays and weekends.

**Note:** You can create up to 10 different bandwidth triggers.

Use the instructions to create a custom schedule for bandwidth throttling:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Go to **System** , then **Configuration** , then **Appliance Settings**. This page lets you coordinate bandwidth throttling through the use of scheduled triggers.

  5. Click the **StreamSnap** subtab if you have to schedule bandwidth throttling for StreamSnap replication.

  6. Click the **On** button next to **Throttling** to enable throttling.

  7. Click the **No** button next to **Override Triggers**.

  8. Click the **Add New Trigger (+)** button to add a new trigger schedule.

  9. Enter the bandwidth value (in Mbps), day, and time for the new schedule.

  10. Click **Save** to update the changes.




### Activate a trigger schedule

To activate a trigger schedule, select the schedule and click **Set This Trigger**.

### Delete a trigger schedule

To delete an existing trigger schedule, select the schedule and click **Remove This Trigger (-)**.

## View bandwidth usage statistics

Use the **Statistics** tab to monitor bandwidth consumption for StreamSnap replication.

Use these instructions to view the bandwidth statistics for your appliances:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens. Select an appliance.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Go to **System** , then **Configuration** , then **Appliance Settings**.

  5. Click the **Statistics** tab.

  6. By default, **StreamSnap** is selected from the **Replication Type** drop-down list.

  7. A pair of charts appears displaying outgoing and incoming bandwidth consumption statistics for the selected appliance on a time scale that you select.

     * The **Incoming Bandwidth (All Sources)** graph depicts the incoming traffic reaching the local appliance from all joined appliances.
     * The **Outgoing Bandwidth** graph depicts the outgoing traffic from the local appliance to the selected appliance.

You can modify the scale by selecting a time unit, such as **Day** (bandwidth used during the last seven days), **Hour** (bandwidth used during the last 23 hours), and **Minute** (bandwidth used in the last 10 minutes). The bandwidth is measured in Mbps.




## Remove a backup/recovery appliance from the appliance management console

You can remove a backup/recovery appliance from management by the appliance management console through the **Manage** tab. All resources associated with this appliance will be removed from the appliance management console.

When you remove an appliance, the following process occurs:

  * De-schedules resource replication.
  * Removes everything related to the removed backup/recovery appliance from the appliance management console database except promoted backup templates, users, and roles.
  * Untags all promoted backup templates on the target backup/recovery appliance to return it to free-standing status.
  * Removes the management of the backup/recovery appliance by the appliance management console.



To remove a backup/recovery appliance from the management console:

  1. Click the **Manage** tab and select **Appliances** from the drop-down list.

The **Appliances** page opens listing all appliances managed by the appliance management console.

  2. Select the appliance you want to remove from the list, then click **Remove Appliance**.

**Note:** You can also right-click on the appliance and select **Remove Appliances**.
  3. Click **Confirm** in the confirmation dialog.


**Note:** A backup/recovery appliance runs forever, even if it is removed from the appliance management console, until the instance is [stopped or deleted](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
