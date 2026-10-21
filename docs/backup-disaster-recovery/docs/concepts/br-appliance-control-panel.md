---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/br-appliance-control-panel/
title: Appliance control panel \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:09.947924+00:00
---

# Appliance control panel  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/br-appliance-control-panel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Appliance control panel Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

There are a few activities that are specific to individual backup/recovery appliances. You execute these actions from the backup/recovery appliance control panel.

## Shut down a backup/recovery appliance

Improperly shutting down a backup/recovery appliance can result in data loss.

Use these instructions to shut down the appliance in a controlled manner:

  1. Click **Manage** and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Go to **Configuration** > **Appliance Settings**.

  5. Click the **Control Panel** tab.

The corresponding panel opens.

  6. Click **Shutdown**. The complete shutdown could take several minutes.




## Enable or disable expirations and schedules

Expirations and schedules are enabled by default. This means backups expire depending on the policy configuration.

If you disable expiration at an appliance level, it takes precedence over the individual policy configuration in policy templates. For example, if you configure a policy to expire backups and then set **Enable Expirations** to **No** using the **Appliance Control Panel** the backups do not expire.

Use these instructions to enable or disable expiration and scheduled backup backups at an appliance level:

  1. Click **Manage** and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance.

  3. Click **Configure Appliance**.

The **Appliance Configuration** page opens.

  4. Go to **Configuration** > **Appliance Settings**.

  5. Click the **Control Panel** tab.

The corresponding panel opens.

  6. In the **Policy Manager** section under the **Appliance Control Panel** , click **Yes** or **No** to enable or disable expirations or enable or disable schedules.




## Configure backup preservation priority setting for backups

Image preservation preserves backups beyond their expiration dates to ensure that those backups are properly processed by the backup/recovery appliance. Image preservation in the control panel lets you modify or disable the application priority settings for preserved snapshots jobs.

See **Images** for information on the following:

  * Displaying a list of preserved or discarded backups in the **Images** section of **Manage**.
  * Viewing **Image Preservation** status for preserved backups in the dashboard.
  * Viewing alerts and warnings specific to preserved backups in the **Monitor**.



### Image preservation overview

Your backup/recovery appliance may encounter resource challenges that result in snapshot jobs failing to execute in a timely manner. To enhance the success rate in which the appliance can complete snapshot jobs, the appliance operates in a backup preservation mode. Image preservation enhances the scheduling features of the backup plan policy manager to be able to ride through periods of high change rates, reduced replication throughput, and other situations. Image preservation delays snapshot and expirations in order to catch up with the transient system resource constraints. Images due for expiration are held until they have been processed by the appliance as long as there is capacity to do so by the appliance.

When the backup/recovery appliance attempts to preserve backups, the appliance runs snapshot, backups beyond their expiration date, continuously within the allowed window in an attempt to catch up on all backup processing. In this case, the appliance processes the oldest unprocessed backups ahead of the latest backups. Once a backlogged backup is processed, the backup is expired per the backup plan schedule.

Preserved backups automatically expire when pool space or VDisk count reaches the warning threshold levels set, see [Resource consumption by appliance](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report#app-consum). When the appliance reaches a warning threshold level, backups expire based on application priority and age. Backups for applications with lower priority expire ahead of applications with higher priority. Within a priority level, older backups expire before newer backups. However, the last backup of any application does not expire by this method. Rather than expiring, the most recent snapshot of any application, an older snapshot of a different application, or a snapshot of a higher priority application expires.

If you find that you need to limit the scope of backup preservation to exclude lower priority applications, you can change preserved snapshot settings in the **Control Panel** from the **Manage** tab.

In addition, if over a period of time you find that the appliance is unable to catch-up with backlogged local jobs, you can disable the ability to preserve backups.

### Modify backup preservation settings for backups

You can modify **Image Preservation** priority settings for preserved snapshots jobs from the **Control Panel** from the **Manage** tab—**Manage** to **Appliances** to **Configure Appliance** to **Configuration** to **Appliance Settings** to **Control Panel**.

Modifying backup preservation settings may be necessary when you need to do the following:

  * Change the global application priority of **Preserve Snapshots Images** settings to limit the scope excluding applications of a certain priority setting. You can instruct the appliance to preserve backups for only **Medium** and **High Priority** applications or to preserve backups for only **High Priority** applications.
  * Disable the **Image Preservation** function if the appliance is unable to catch-up with backlogged backups.



### Modify preserve snapshots settings

A backup would normally be removed by the backup/recovery appliance based on the frequency, retention, start time, and end time specified in the policy template for an application. At times, the appliance may lag behind in the snapshot to remove jobs due to resource constraints. When this lag occurs, the setting of the **Preserve Snapshots** parameter in the **Image Preservation** section of the **Control Panel** defines to the appliance how to preserve backups that are due for expiration but not yet successfully removed.

If necessary, you can change the application priority of **Preserve Snapshots** from **All** (the default setting) to **Medium and High Priority** applications or to **Only High Priority** applications. If you find that the appliance is unable to catch-up with backlogged local jobs, you can disable the **Preserve Snapshots** parameter by setting it to **None**.

Use these instructions to modify the **Image Preservation** settings for preserved snapshot jobs:

  1. Click **Manage** and select **Appliances** from the drop-down menu.

The **Applications** page opens.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Go to **Configuration** > **Appliance Settings**.

  5. Click the **Control Panel** tab.

The corresponding panel opens.

  6. Go to the bottom of the page to locate **Image Preservation**.

  7. Options for the **Preserve Snapshots** parameter include the following:

     * **All** : All applications — low, medium, and high priority—have their backups preserved. This is the default setting.
     * **Medium and High Priority** : High and medium priority applications have their backups preserved.
     * **Only High Priority** : Only high priority applications have their backups preserved.
     * **None** : No local backups are preserved even if the job has not run on those backups. When the backup reaches its expiration time, barring other dependencies, it expires.
  8. A confirmation dialog appears instructing you that changing the priority of the **Preserve Snapshots** parameter may result in additional or fewer backups being preserved beyond their expiration until those backups are processed into the snapshot pool. Click **OK** to proceed with the application priority change.




## Set priorities for the first new applications

This option lets you add special job scheduling slots that are used only to capture the first ingest of a new application. Turn this option off if you are adding a lot of new applications and want to get them protected quickly without regard for the impact on existing applications. Turn on this option at a low number of slots (for example, two slots) to limit the impact of the ingestion of new applications on existing applications; new applications are brought on-board more slowly.

Use these instructions to enable additional job slots for ingestion of new applications:

  1. Click **Manage** and select **Appliances** from the drop-down menu.
  2. Select an appliance.
  3. Click **Configure Appliance** to open the **Appliance Configuration** page.
  4. Go to **Configuration** > **Appliance Settings**.
  5. Click the **Control Panel** tab.

The corresponding panel opens.

  6. You can increase, decrease, or turn off slots dedicated to capturing new application data. You can select from one to 10 slots. However, there is a finite number of slots available, so slots assigned come at the expense of incremental job performance.

**Note:** Don't change the slot assignment values except under the guidance of support.



## Appliance manager

From the **Appliance Manager** , you can do the following:

  * Manage shared appliances
  * Use the appliance's [Control panel](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel)



Use these instructions to open the **Appliance Settings** :

  1. Click **Manage** and select **Appliances** from the drop-down menu.

The **Appliances page** opens.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Go to **System** > **Configuration** > **Appliance Settings**.

A list of appliances joined to the local appliance is displayed.

  5. If an appliance is the primary of a domain, it is listed as **Sharing**.




### Manage joined appliances

From the **Appliance Manager** , you can do the following:

  * Unjoin appliances that are joined with the selected appliance
  * Throttle [Streamsnap](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-appliance#replicate) replication
  * Select [storage](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/storage-pools-about) location for replicated snapshots and VMs
  * View bandwidth [statistics](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-appliance#stats).
  * Join appliances



## Configure joined appliances

Appliances can be joined to additional appliances for disaster recovery and business continuity purposes at the same site or at different sites. Appliances must be joined in non-sharing mode.

### Non-sharing mode

Use this mode when you want appliances to perform remote backups for each other and for failover. You can join the following:

  * One appliance with another appliance to enable replication from the former to the latter.
  * One appliance with two appliances to enable different applications to replicate to separate appliances.
  * Two appliances with one appliance to let the later act as a target for replication.



Non-sharing mode makes peers of the appliances that are joined. When two appliances join in the non-sharing mode, each appliance can be the destination for remote replication of data from the other appliance.

In non-sharing mode, each appliance uses its own users, policies, and templates, and protects only the applications assigned to it; peer appliances don't share users, policies, and templates.

Backup/recovery appliances support StreamSnap replication from the primary appliance to a remote appliance. For more information on Backup and DR replication, see [Replicate data using appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-replication).

### Join in non-sharing mode

The following are step-by-step instructions for joining appliances in non-sharing mode. For details, see Non-sharing mode.

Use these instructions to join the local appliance A and the remote appliance B:

  1. Click **Manage** and select **Appliances** from the drop-down menu.
  2. Select an appliance.
  3. Click **Configure Appliance** to open the **Appliance configuration** page.
  4. Go to **Appliance Settings** > **Join Appliance**.

The **Join A Remote Appliance** page opens.

  5. Enter the IP address of the remote appliance B in **Remote Appliance** IP address.

  6. (Optional) Click **Test Connection** to validate the IP of the joining appliance.

  7. Click **Join**. On successful configuration appliance B appears connected to the appliance A.

  8. If you want to configure the bandwidth throttling used to replicate StreamSnap backup data from one appliance to another so that the two paired appliances can share bandwidth.




### Unjoin appliances

Before deleting a joined appliance, ensure that running jobs are not using the remote appliance.

Use these instructions to delete a joined appliance:

  1. Click **Manage** and select **Appliances** from the drop-down menu.
  2. Select an appliance.
  3. Click **Configure Appliance** to open the **Appliance configuration** page.
  4. Go to **System** > **Configuration** > **Appliance Settings**.

A list of joined appliances is displayed.

  5. Click **Unjoin** against the appropriate appliance.

  6. If an appliance is in use in any resource profile, then the unjoin process will fail.




## Diagnostic tools

The tools in the **Diagnostics** section of the **Appliance Configuration** page lets you view a variety of charts to monitor the efficiency of your backup/recovery appliance. In addition, you can also view a **System Load Report** , and monitor the status of the backup/recovery appliance's SSD devices.

### Charts

The backup/recovery appliance includes a suite of diagnostic charts to help you keep your appliance running efficiently. Information from the diagnostic charts can help you to plan changes to your appliance and to identify problems and potential problems with your appliance.

Use these instructions to display the diagnostic charts:

  1. Click **Manage** and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance and click **Configure Appliance** to open the **Appliance Configuration** page.

  3. Go to **Diagnostics** then **Charts**.




### Select a graph

From the **Select a graph** drop-down list you can select from the following diagnostic information to display as a graph in the **Charts** window.

### Snapshot disk IOPS

The disk I/O per second required by snapshots—read and write activities. You can display data in the graph by Read IOPS, Write IOPS, or both selections.

### Snapshot disk throughput

The logical amount of data required for snapshots, in KBpsec. You can display data in the graph by read KBps, write KBps, or both selections.

### VDisk count

A count of the appliance VDisks every 15 minutes.

### Select a time period for the graph

From the **Select a time period** drop-down list you can select the past day, week, or month to display the data in the associated graph.

### Zoom an area in the graph

Use the zoom display below the selected graph to expand on a particular period of time. Use these instructions to zoom:

  * Click-drag within a time period in the zoom display to select the view area. You can repeat this process for different time intervals in the display.
  * To revert to the normal chart display, click anywhere within the zoom display.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
