---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs/
title: Monitor jobs in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:51.761371+00:00
---

# Monitor jobs in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Monitor jobs in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

From the **Monitor** tab, you can view and manage jobs (cancel active jobs or change the job priority of a queued job) from backup/recovery appliances managed by the appliance management console. You can also view events, which are information, warning, or error notifications raised by an appliance.

You can filter jobs by name, status, start or end time, type, host, and application.

**Note:** All jobs that display status as retry or failed are logged to Cloud Logging. To display these events see [Backup and DR event logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events) and to set up notification on these (or specific) events see [Configure a log-based alert](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).

## Job status panel

The appliance management console **Jobs** panel provides information about jobs that have run over the past 24 hours (default).

  * **Current or Past Jobs.** A quick view of how many jobs are running, have succeeded, failed, were retried, or were canceled.
  * **Job Types or Appliances.** Links to the monitor filtered to show the status of jobs by job type over the last 24 hours or by managed backup/recovery appliance.



In the past jobs section, you can also view the status of the last week or last month if needed. This panel fetches fresh data every two minutes.

## Monitor jobs

Use these instructions to monitor jobs:

  1. Click the **Monitor** tab and select **Jobs** from the drop-down menu to open the **Jobs** page where you can see a list of all jobs that are running. Select the **Running** filter to show all jobs that are being monitored.
  2. To modify the display of the fields in the table, you can do the following:

     * **Search By Keyword.** Filter by job name, host and application in the **Jobs** view or by event message in the **Events** view is now auto-submit. As you type the query it will update the result set. **Search By Keyword** is case insensitive.
     * **Started, Ended and Queued**. These filters have single radio style buttons to select date range spanning a day, week for month.
     * **Adjust Fields.** Options in the top right side of the toolbar allow you to set columns as visible or hidden and to set the number of rows to display.
     * **Adjust Column Width.** To adjust the width of a table column to show more content in the table, drag the column divider in a column header to the left or right to resize the column width. Column dividers are marked by a pair of thin gray lines.
     * **Auto-refresh.** Of the **Monitor** grid view every fifteen seconds.
     * The **Monitor** page shows the time of the last refresh and the time until the next refresh. You can perform a manual refresh at any time.
  3. To export the job list as a PDF, click the export icon.

  4. To modify the number of rows displayed in a table page, you can select from the drop-down list at the bottom of the table. Choices include: 10, 25, 50, 100, or 500 rows per table page.

  5. To filter the list of jobs to view only a subset, click **Open Filters** to open the filters panel. Make your filtering selections, then click **Update Filters**.

**Note:** To clear a single filter without clearing all filters, click the **x** beside the applied filter. To clear all filtering, click **Clear Filters** in the filters panel.
  6. To view the details for a specific job, select an item in the **Jobs** list and then either:

     * Click the status link for an associated job in the **Status** column.
     * Click **View Details** from the bottom right corner of the page.
**Note:** You can also right-click on a job in the list and select **View Details** from the menu.
  7. The **Job Details** page opens. On this page, you can review the following:

     * Details about the job
     * Volume information
     * Number of job retries
     * Job statistics

See [View job details](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-backup-overview#capture-app-data) for specifics on each of these areas.

  8. When you are done reviewing job details, click **Return to Jobs** to return to the **Jobs** page.




## Job status

At any time a job can have one of the statuses described in the following list:

  * **Canceled.** The job was canceled by a user, or auto-canceled by the system because the target pool exceeded the safe limit.
  * **Failed.** The job failed to run to completion within the backup plan period. In case of job failure, an event is created with information about the job failure. If there is time in the backup plan period, the original job becomes retried and an identical new job is queued.
  * **Not Run.** The job couldn't run during its backup plan period due to some constraint, for example the scheduler is disabled, destination pool is full, source image is missing or unsuitable, connectivity issue, or there are no available job slots.
  * **Queued.** When a policy requires a job to be run, a job is created with a status of **queued**. If no constraints are present, it goes into the **running** state. If constraints prevent it from running, then it remains queued. If the constraints continue to be present until it is time to run the next instance of the same policy, the job is given **notrun** status, and a new job instance with the same job ID and a letter appended to it is added in the queued state.

**Note:** While a job is queued, you can change the job priority.

  * **Queued_Readiness.** The job status only applies to Onvault and Direct to OnVault jobs. It is displayed when a check is performed to see whether an OnVault pool is ready for the queued job. In case there is no OnVault pool that is available, the **Queued_Readiness** status is shown.
  * **Retried.** The job did not complete. The job goes into the retried state. If there is time in the backup plan period, the original job becomes retried and a new job instance with the same job ID and a letter appended to it is queued. There can be 3 retry attempts, at 4, 16, and 64 minutes after each job fails. When the backup plan time runs out or if another instance of the job begins, the original job is failed and a retry job is started in retry status. Retry jobs have letters appended to the job ID.
  * **Running.** The job is being processed. The job's percent completion is indicated in the status.
  * **Succeeded With Warnings.** The job has completed successfully according to the backup plan that invoked it, however a warning was also printed that can be viewed in **Monitor** > **Events**. A typical example is that a Compute Engine instance snapshot succeeded but the metadata upload to OnVault did not.
  * **Succeeded.** The job has completed successfully according to the backup plan that invoked it.



## View job details

From the **Job Details** window, you can review the following:

  * Details about the job
  * Volume information
  * Number of job retries
  * Job statistics



When you are done reviewing job details, click **Return to Jobs** to return to the **Jobs** page.

The following list provides a description of the job details.

  * **App Name.** Application name, not necessarily unique.
  * **App Type.** Application type, such as SQL Server, Oracle, file system, or an entire Virtual Machine.
  * **Capacity.** The capacity of each volume.
  * **Consistency Mode.** Crash-consistent or application consistent, indicates whether the application was quiesced during the job.
  * **Duration.** The time between the start date and end date.
  * **End Date.** The date and time when the job finished.
  * **Error Code.** Zero for no error, a non-zero value to indicate the error encountered when running the job.
  * **Event ID.** Any event ID that is associated with the job. If there is no event ID, value is zero.
  * **Message.** A message explaining the errors encountered when running the job.
  * **Expiration Date.** Date and time when this image is due to be expired.
  * **Host Name.** Name of the host where the application runs.
  * **Image Type.** Snapshot, cloud, the type of image created by the job.
  * **isbootvmdk.** Set to true for the volume within the image that is the boot volume, if any.
  * **Islvm.** For each volume, whether it is a Logical Volume Manager Volume.
  * **Job ID.** A unique number that identifies a job.
  * **Last Constraint Date.** Most recent date when a job was run.
  * **Log Truncated.** Set to true to indicate that logs were truncated for the application.
  * **logicalname.** The name of each volume as identified by the host system.
  * **Mounted Host.** For a mount failover job, the host where the image is mounted.
  * **Policy Name.** The name of the policy associated with the job.
  * **Priority.** Low, medium or high, set in the policy.
  * **Protected data.** Amount of data protected.
  * **Source Name.** Which specific copy of an image was the source for a job.
  * **Sourcemountpoint.** The name of the mount points for each of the volumes on the original host.
  * **Start Date.** The date and time that the job actually started running.
  * **Template Name.** The name of the service level template.
  * **Transport Medium.** How the data was transported during the job: over the SAN or LAN.
  * **Uniqueid.** An identifier that uniquely identifies each volume in the image.
  * **Volumekey.** A string that is used internally to identify the multiple volumes within the image.
  * **VolumeUID.** A unique identifier for each volume in the image.



**Volume Information**

The following list shows the volume information provided.

  * **Capacity.** Size of the volume that was backed up.
  * **Data Store.** For a virtual machine, the datastore where the volume was located.
  * **File Name.** VMware: Path to the VMDK file.
  * **HUID.** Host unique identifier, a string that uniquely identifies the volume.
  * **Label.** The volume label of the volume.
  * **Logical Name.** A human readable unique name for the volume. For VMware VMs, this is the filename.
  * **Source Mountpoint.** The mount point of the volume.
  * **Target.** The Backup and DR VDisk name for the copy of the volume.



**Retries**

You can read a description of the retry metadata in the following list.

  * **End Date.** The date and time when the job finished, whether successfully or in failure.
  * **Error Code.** Zero, or the error code returned by the job.
  * **Error Message.** A textual messages corresponding to the error code.
  * **Job Name.** The job name of the original job or retry attempt.
  * **Start Date.** The date and time when the job started running.



**Statistics**

The following list provides a description of the statistics.

  * **Application Freeze Time.** The total time for which the application was in a frozen state during a backup. The application was placed in a frozen state, during a backup (snapshot) so that all of the data was captured in a consistent state.
  * **Application size (GB).** The size of the application data on the staging disk.
  * **Number of volumes.** The number of volumes in the application that is the subject of the job.
  * **Data copied (GB).** Displays the amount of new application data that was found by this job.



## Job Types

Backup and DR protects and accesses data through these types of jobs:

Job type | Monitor label | Description  
---|---|---  
**Clean Up Mirroring** | cleanupmirroring | Removes a StreamSnap image from a remote appliance when a backup plan is removed from an application or changed to one that does not include the same type of replication.  
**Clone** | clone | Creates a copy of a source image to a destination, such as a server, database, or disk pool.  
**Clone (Migrate)** | Clone (Migrate) | Migrates data from mounted disks to server disks.  
**Clone (Mount)** | Clone (Mount) | Mounts an image to a server in preparation to perform a Clone (Migrate) job.  
**Delete** | delete | Deletes an image that was already unmounted from the host.   
**Delete Test** | deletetest | Performs an unmount and delete of an image created by a failover-test job.   
**Direct to OnVault** | DirectOnVault | Creates a point-in-time image of a VMware VM into the OnVault pool without first using the snapshot pool.   
**Expiration** | expiration | Expires/deletes an image once it reaches the end of its retention period, or when requested on-demand.  
**Failback** | failback | Performs an unmount and delete of an image created by a failover job, removes any syncback images for the application, and triggers a Failover Delete job on the remote appliance.  
**Failover** | failover | Performs a mount of an application from a replicated StreamSnap image, stopping new snapshot jobs at the source and tracking changes for reverse replication (Syncback).  
**Failover - Delete** | deletefailover | Auto-triggered to run on the remote appliance when the local appliance performs a failback job.  
**Failover - Test** | failovertest | Performs a mount of an application from a replicated StreamSnap image, but keeps forward replication active and does not enable syncback.  
**Finalize** | Finalize | Performs the final step in a SQL Server Mount and Migrate process, which includes a migrate job combined with an unmount delete.  
**Forget Active Mount** | ForgetActiveMount | Removes tracking of a Compute Engine instance mount without deleting the instance in Compute Engine.  
**Forget Imported OnVault Image** | Forget OnVault Images | Undoes an import operation of OnVault metadata in an OnVault pool from one appliance.  
**LiveClone** | liveclone | Creates a LiveClone image (full copy) from a snapshot image.  
**LogBackup** | LogBackup | Creates an image to capture logs for applications.  
**Log Replicate** | logreplicate | Uses StreamSnap technology to perform the replication between the local and remote appliances, meaning the log replication goes directly from the snapshot pool on the local appliance to the snapshot pool on the remote appliance.  
**Migrate** | Migrate | Performs a copy of data from a mount to a server's storage. For some application types, it will perform an online transition and remove the Backup and DR mounted disks. For other application types, migration jobs run repeatedly until the user initiates a Finalize job.  
**Migrate (Cancel)** | Migrate (Cancel) | Cancels an in-progress migration, disables future migration jobs for the mounted image, and cleans up any partially migrated/copied data.  
**Mount** | mount | Mounts an image to a selected host.  
**OnVault** | vault | Copies a snapshot image to an OnVault pool.  
**OnVault(Log)** |  | Replicates database logs to one or more OnVault pools.  
**OnVault Replication** | OnVaultReplicate | Replicates an image in one OnVault pool to another OnVault pool.  
**Oracle ASM Rebalance** | Restore (ASM switch) Restore (ASM Rebalance)  | ASM Switch mounts an Oracle database in place of its original source database. ASM Rebalance initiates a migration of the database from the mounted disks to the server disks, and then removes the mounted disks when finished.   
**Prep Mount** | prep-mount | Performs a mount of a LiveClone image in a way that allows direct modification to the LiveClone.   
**Prep Unmount** | prep-unmount | Unmounts a LiveClone that was mounted using prep-mount and optionally allows saving of changes made to the mount directly into the LiveClone.  
**Refresh LiveClone** | refreshliveclone | Incrementally refreshes a LiveClone image with data from a different source snapshot image.  
**Remote-Mount** | remote-mount | Mounts a remote image (from another appliance) to a local host. Reverse incremental replication is performed (if needed) to perform this task.  
**Reprovision** | reprovision | Takes an existing mount of a database application and refreshes it to a different point in time by performing an unmount delete and subsequent mount of the new image, defaulting to all the same options used in the previous mount.  
**Restore** | restore | Replaces production data with a selected backup image.  
**Restore (Cancel)** | Restore (Cancel) | Cancels an in-progress mount and migrate restore. Any migrated data will be deleted and the mount data will be removed.  
**Restore (Migrate)** | Restore (Migrate) | Performs a copy of data from a restore (mount) to a server's storage. For some application types, it will perform an online transition and remove the Backup and DR mounted disks. For other application types, migration jobs run repeatedly until the user initiates a finalize job.  
**Restore (Mount)** | Restore (Mount) | Mounts an image of a database in place of its original source database, to prepare for a subsequent restore (migrate).  
**Snapshot** | snapshot | Creates a point-in-time image of the application or VM into the snapshot pool.  
**StreamSnap** | streamsnap | Creates, or refreshes, a failover-ready StreamSnap image on a remote appliance.   
Note: A StreamSnap replication job is also tied to a specific snapshot policy. It uses the schedule and frequency settings of snapshot policy when performing replication.   
**Syncback** | syncback | Performs an incremental reverse replication after a failover, creating a syncback image on the local or source appliance that can later be used for a restore.  
**Unmount** | unmount | Unmounts an image previously mounted to a host, but keeps the image available for later mounting.  
**Unmount Delete** | unmount delete | Unmounts an image previously mounted to a host and discards all changes made in that mount.  
  
## Run an on-demand job

If you require a job to start right away, run an on-demand job. On-demand jobs include all types of restore, clone, mount jobs, and jobs created when policies are applied on-demand.

**Note:** You don't need to run an on-demand job for just-discovered applications. However, if the assigned backup plan is not scheduled to start for some time, an on-demand job can be run immediately.

Each backup/recovery appliance reserves a pool of slots for all various categories of jobs: data access, expiration, log replication, log OnVault, on-demand, OnVault, snapshot, streamsnap. Also, there is an unreserved pool of slots.

Before starting a job, each backup/recovery appliance checks whether a slot corresponding to the job's category is available to run the job. When a reserved slot is not available because all the slots of that category are running jobs, the backup/recovery appliance checks whether an unreserved slot is available. If an unreserved slot is available, the job is started. However, you can reserve the maximum number of slots that the jobs of a particular category can use from the unreserved pool. This measure limits the number of slots that jobs from a category can make use of from the unreserved pool.

**Note:** Restore operations (mount, clone, failover, test failover, prep-mount, and restore) use data access slots.

### Run an on-demand backup job from the appliance management console

To run an on-demand capture of a managed application from the **Manage Backup Plan** page:

  1. Click the **App Manager** tab and select the **Applications** option from the drop-down list. The **Applications** page opens.
  2. Select the application or VM and then click **Manage Backup Plan** from the drop-down list. The **Manage Backup Plan** page opens.
  3. Expand a template policy from the list of policies on the right.

If a database is managed with a log protection-enabled backup template and if backups are available, you have further log options for the type of job to submit. In this case, you select whether to capture the database (DB) or just the logs (Log).

**Note:** On-demand StreamSnap jobs can be run for DB and DB+Log types. To perform on-demand log replication of just the database log to a remote backup/recovery appliance, select the **Replicate Logs** menu command described in Running On-Demand Database Log Replication.
  4. Click **Run Now** and a confirmation message opens.

  5. Click **Yes** to confirm. A point-in-time image is created per the backup policy.




### Run on-demand database log replication

In some cases, you might need to manually initiate log replication to the remote backup/recovery appliance for a database image. For example, you might need to manually perform log replication if the log for a database image did not properly replicate to the backup/recovery appliance or if there is no log for the database image on the backup/recovery appliance. You can then use the transaction logs at the remote appliance to recover a database to a specified point-in-time.

**Note:** Manually replicated transaction logs won't be visible on the remote appliance until the Oracle or Microsoft SQL Server database image is replicated to the remote appliance. The recover range is only visible when the replicated database image appears on the remote appliance.

To manually initiate database logs replication to the remote backup/recovery appliance:

  1. Click the **App Manager** tab and select the **Applications** option from the drop-down list. The **Applications** page opens.
  2. Select the managed application or VM and then click **Replicate Logs** from the drop-down list at the bottom right corner of the page.
  3. Click **Confirm** in the confirmation dialog that opens. The database transaction logs are replicated to the remote appliance defined by the replication policy in the template.



## Monitor mount jobs to containers

To monitor a mount job to a container:

  1. Click the **Monitor** tab and select **Jobs** from the drop-down menu to open the **Jobs** page where you can see a list of all jobs that are running.
  2. Filter by **Mount** jobs.
  3. Identify the job you want to monitor by its **Label** or other details.
  4. If the job is running, you can monitor its progress. Once completed, select the job and click **View Details** to review:

     * Details about the job
     * Volume information
     * Number of job retries
     * Job statistics

See [Viewing Job Details](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#view_job_details) for specifics on each of these areas.




### Access container YAML code

The section **Container YAML** lists the YAML code snippet that was added to the container or pod's YAML configuration file. You can refer back to this code and use it at a later point of time as needed.

  1. When you are done reviewing job details, click **Return to Jobs** to return to the Jobs page.



## Cancel a running job

You can cancel jobs that are running or are queued to run.

To cancel an active job:

  1. Click the **Monitor** tab and select **Jobs** from the drop-down menu. The **Jobs** page opens listing all jobs that are running. You can clear this default filter to show all jobs that are being monitored.
  2. Select the job that you want to cancel, then click **Cancel Job** from the bottom right corner of the window.

**Note:** You can also right-click on a job in the list and select **Cancel Job** from the menu.
  3. Click **Confirm** in the **Cancel Job** dialog.




## Change job priority

You can change the priority of an in-process job based on how you want the backup/recovery appliance to allocate necessary resources.

To change the priority of a queued job:

  1. Click the **Monitor** tab and select **Jobs** from the drop-down menu. The **Jobs** page opens listing all jobs that are running. You can clear this default filter to show all jobs that are being monitored.
  2. Select the job that you want to change priority from the **Jobs** page and then click **View Details** and then **Change Priority** from the bottom right corner of the window.

**Note:** You can also right-click on a job in the list and select **Change Priority** from the menu.
  3. From the **Set Job Priority** dialog, select the job priority.

  4. Click **Confirm** to change priority selection.




## How uncompleted jobs are retried before failing

When a scheduled job fails, the scheduler will automatically retry the job up to three more times. The first time a job fails, the status of the first attempt will be marked as Retried and the scheduler will wait four minutes before queuing the job again. If it fails a second time, the next retry will be queued after 16 minutes. If it fails a third time, a final retry will be queued after a holdoff period of 64 minutes. After three failed retry attempts (for a total of four attempts), the final retry job will be marked as Failed (rather than **Retried**) and no further jobs are attempted for that application in that schedule period.

The scheduler will treat a job retry like any other available job. If there are more jobs queued than slots to accommodate them, then the queued retry job will need to wait for a slot. If the policy window closes before a retry job can start, then any queued retry jobs won't run and no further retries will be attempted.

Job retries are reported in **Monitor** > **Jobs**. To identify job retries all four jobs will have the same job number in the following format in this order:

  * Job_xxxxx (Status: Retried)
  * Job_xxxxxa (Status: Retried; queued after a 4 minute holdoff)
  * Job_xxxxxb (Status: Retried; queued after a 16 minute holdoff)
  * Job_xxxxxc (Status: Failed; queued after a 64 minute holdoff)



The next time a backup job for this application is attempted depends on the policy's schedule. So if the schedule calls for one snapshot per day in a window starting at 01:00, the next attempt will be the following day at 01:00.

## Timezone

By default, in the appliance management console, all time stamps shown in the jobs and events menus are in the user's local timezone as detected by the web browser. If you want to confirm which timezone is in use, on the dashboard menu bar, select the user icon in the top right hand corner. It displays both the auto-detected timezone as well as set the timezone if the detected timezone is not suitable.

Use the following instructions to change the timezone.

  1. On the dashboard, click the user icon that is on the top right corner.
  2. Select **Change Timezone**.
  3. From the **Timezone** drop-down, select the timezone to use when displaying jobs and events.
  4. Click **Save**.



## About scheduled jobs

Jobs run according to the schedule assigned in their backup template policies. If you try to run many resource-intensive jobs simultaneously, then some have to wait for the resources to come available. If the wait is too long, the window closes and a backup plan violation occurs.

It is better to stagger resource-intensive jobs like initial snapshot jobs over time rather than to have them all compete for resources at the same moment. For example, instead of snapping all VMs, file systems, and databases at 6:00 PM on weekdays, consider snapping one type of application on the hour, another type at 10 minutes after the hour, and another type at 20 minutes after the hour.

The initial snapshot of an application or a VM is the largest and most time-consuming snapshot because every bit of data is new. When you add a new large application or VM, perform an on-demand snapshot at an off-peak time for the first snapshot and then schedule a backup template policy for all future snaps.

## About on-demand jobs

Most jobs run on a schedule according to their backup plans, but for upcoming maintenance windows, software upgrades, and for the first snapshot of a new application, you want to ensure that you have a successful copy of the data created before you start your scheduled maintenance task. These cases call for an on-demand job.

### About job slots

Backup and DR manages jobs by assigning _job slots_. The appliance reserves a pool of slots for each category of jobs, plus a pool of unreserved slots.

Before starting a job, Backup and DR checks whether a slot corresponding to the job's category is available to run the job. When a reserved slot is not available because all the slots of that category are running jobs, the appliance checks whether an unreserved slot is available. If an unreserved slot is available, the job is started.

### Queue of on-demand backup jobs

Backup and DR supports queuing of on-demand jobs to provide the flexibility to create your images without concern for the number of on-demand job slots available to start the job. The queued on-demand job remains in the queued state until an on-demand job slot is available.

When an on-demand slot opens, the job progresses to the running state. This sequence occurs in the order that the job was submitted. If an on-demand job fails, the appliance will attempt to run the next job in the queue. On-demand jobs use different job slots than scheduled jobs, so scheduled jobs may run before queued jobs.

While an on-demand job is in a queued state you can change the job priority, cancel the job or cancel protection for the application. You can view the queued jobs by clicking **Monitor** then **Jobs**.

A canceled on-demand job appears in the job history table as a canceled job. The start time of the job and the end time of the job will be the time that the cancel request or the cancellation of application protection was acknowledged.

## Maintain performance when adding new applications

If your system has been performing acceptably and then you add new applications, performance might suffer for a short time. This is because change block tracking recognizes new data and protects it even when it is only a small part of a large application. This means the system is optimized to process many changed blocks every day.

A new application requires a lot more resources for the initial capture, because it is all new data to the system.

Use the following information for best results when adding new applications:

  * When you add a new application, protect it for the first time using an on-demand job during a period of light load. This prevents the resource-intensive initial ingest job from interfering with other jobs.

  * When adding multiple new applications or VMs, try to stagger the initial protection jobs for each new application over time, to prevent all of the new data from being ingested simultaneously. Do this by assigning backup plans that run at different times. You can also use the on-ramp job slots feature to minimize disruption.

  * Separate the initial protection job in time from the mirror job. Once an application snapshot has been taken, the mirror job can run some hours later when the system load is lighter.

  * Consistency groups can be an efficient way to protect multiple applications with similar needs; see [Capture application data in Backup and DR consistency groups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-backup-overview#capture-app-data).

  * Be aware of your existing backup plans and try not to schedule snapshot jobs simultaneously with the snapshot jobs for very large or dynamic applications.

You can choose from the list of preserved snapshot images from the **Manage** tab, and:

    * Select from the list of preserved images and navigate to that image in the **App Manager**.

    * Expire one or more selected snapshot images.

**Note:** When expiring snapshots, the amount of space reclaimed might be less than the amount of space consumed by that snapshot. This is due to the common block reference between snapshots. To ensure maximum space reclamation, expire the oldest snapshot first.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
