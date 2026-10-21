---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate/
title: Mount and migrate Microsoft SQL Server databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:15:30.028763+00:00
---

# Mount and migrate Microsoft SQL Server databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Mount and migrate Microsoft SQL Server databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The Microsoft SQL Server mount and migrate feature is available for recovery of the following:

  * SQL databases—stand-alone and failover cluster
  * Consistency group of SQL databases
  * SQL instances
  * SQL AAGs



SQL Server mount and migrate is a three step process in the appliance management console that includes the following:

  1. **Mount or restore** : Perform either an application aware mount or a mount and migrate restore. For more information, see Mount or restore
  2. **Migrate** : Configure the migration schedule for an image from the **Active Mounts** page. Image migration follows the schedule defined and migrations jobs are run repeatedly at the frequency specified. For more information, see Configure migration schedule
  3. **Finalize** : Initiate the last and final stage of the image migration process. For more information, see Finalize

**Note:** When working with a SQL availability group, the finalize step cannot be performed on a database in a group that is on the primary node. To finalize migration on the primary node, a failover to another node must be performed first, that changes the node to be a secondary node.

**Note:** Mount and migrate is also available for logical volume manager file systems, but as a two-step process that supports clone and restore capabilities only. By contrast, SQL Server mount and migrate is a full three-step implementation involving mount or restore, configuring migration schedule, and finalize migration.

## Mount or restore

You can perform either an application aware mount or a mount and migrate restore on the chosen image.

For instructions on how to perform an application aware mount of SQL databases,see [Mount a SQL Server databases as virtual applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-access). For instructions on performing a mount and migrate restore, see Mount and migrate restore.

Multiple restores can be performed concurrently for a parent application like SQL instance, SQL availability group, or SQL consistency group, but they have to be on different databases.

### Mount and migrate restore

To perform a mount and migrate restore, follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the SQL application with the image that you want to restore using mount and migrate capability. Then select **Access** from the drop-down list at the bottom of the **Applications** page.

The **Access** page opens listing captured images appear in the timeline ramp view. For more information on the view, see [Access the timeline ramp view of an image](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time)

**Note:** Background differentiates snapshot images containing a SQL database with archive log files, and also illustrates the restore range time period for the logs.
  3. Select the image, then select **Restore** from the list of operations. The **Restore** page opens.

  4. Select the **Mount and Migrate** option.

  5. If the selected database does not have logs, the **Restore** page does not show roll forward options.

  6. If the source application is protected by a snapshot policy that has enabled database log backups, and logs are available with the image, you can use the logs to roll forward to a specific point in time by changing these options in the **Roll Forward Time** section:

     * The date field contains all possible dates that the database can be rolled forward to—through the application of database transaction logs. Select the date you want the database to be rolled forward to.
     * The time field contains a slider showing all possible times on the selected date that the database can be rolled forward to. If you select the latest possible date and then move the slider to the right most position, the restore job applies to all available logs. If you select the earliest possible date and move the slider to the left most position, the restore job applies no logs.
     * You can specify to roll forward using either **User Time** or **Host Time**. **User Time** is relative to the local time of the current user. **Host Time** is relative to the system that hosts the data to be restored.

When using an OnVault image as the source, the log range is visible when logs are available in either the OnVault pool for the source image or in the snapshot pool on the backup/recovery appliance for the selected target host. When dealing with imported OnVault images, this might result in different ranges of available logs based on the target host, or it might result in no roll forward time option appearing at all.

  7. In **Label** , optionally enter a name. The **Label** is pre-populated with the text `Restore - M&M - 04 June, 2019 06:52:29pm`, using date and current time, so if you don't update the property, the default value is used.

You are not be able to change the default selection for **Restore with Recovery** , as the property is disabled.

  8. For **SQL Server Instance Name** , select the target **SQL Server Instance**. The new database will be managed by the instance you specify. Similarly, for **Consistency Groups** , enter the name of the target **Consistency Group** in the **Enter Consistency Group Name** field.

  9. In **SQL Server Database Name** , enter the new SQL Server database to be provisioned.

  10. For **SQL Instances and Consistency Groups** , select the databases to be included in the restore job. The **Restore with Recovery** option is enabled by default and you cannot disable it.

  11. In **Username** , enter the name of the username for database provisioning. It is needed only when the account running the Backup and DR agent does not have the privileges to apply transaction logs or to dispatch a database.

  12. In **Password** , enter the password for the user you specified in step 10.

  13. Click **Submit**. A warning dialog opens. Read it and then enter **DATA LOSS** to confirm.

The selected databases are taken offline. A mount is performed to provide fast access to the databases with the selected point in time. After the mount completes, the migrate option becomes available as an action on the resulting active image.

**Note:** If the target is a VM, and the mount mode is not pRDM, the user will see the warning text after the **Data Loss** message: Warning: pRDM is not selected. This means that while the databases are running from the mount, backups can consume a full copy's worth of space in the snapshot pool, plus the changed-block changes. When the migrate begins, backups can stop until the migration is finalized.



## Configure migration schedule

You can configure the migration schedule from the [Active mounts](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts) page. Any application aware mounted image can be migrated at a later time. Images that were restored using the mount and migrate option can also be migrated. Mounted images show the image state of **Mounted** and images that were restored using the mount and migrate capability have the image state of **Restore (Mounted)**.

For instructions on how to configure migration schedule, see [Configure migration schedule for mount and migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate#configure-schedule). Image migration follows the schedule defined and migrations jobs are run repeatedly at the frequency specified.

Once migration starts, the image state changes to **Migrating** —in case the image is an application aware mount—or **Restore (Migrating** &mdash); if the image was created using the **Restore Mount and Migration** option. The image is in **Migrating** state until you initiated finalize migration in step three, when the last migration that is performed.

## Finalize

Finalize migration initiates the last and final stage of the image migration process. Once you begin the finalize stage, you cannot cancel the migration process.

Before you initiate the finalize stage, complete the following:

  * change the migration frequency specified for the image
  * perform an on-demand migration job
  * cancel image migration
  * cancel image restore



To begin the finalize stage, follow these steps:

  1. Go to the **Active Mounts** page and filter by **Image State** of **Migrating** or **Restore (Migrating)**.
  2. Select the image and then select **Finalize Restore** from the drop-down menu at the bottom of the page.
  3. You see a confirmation message. Read it carefully and then click **Proceed**. The databases are taken offline during final migration and then brought back up again on the target production database.
  4. Go to **Monitor & Jobs**, and filter by **Finalize** job type. Locate the job and view the job details.

You can also view images with the **Finalize** image state in the **Active Mounts** page.




### Change migration frequency

To change the migration schedule, follow these steps:

  1. Select an active image with **Image State** of **Mounted** or **Restore Mounted**.
  2. Select **Migrate** from the drop-down menu at the bottom of the page.

The **Update Migrate Frequency** page opens.

  3. For **Frequency** , use the slider to define the frequency with which to schedule migrate jobs from one to 24 hours.

  4. For **Copy Thread Count** , specify the number of parallel copy threads to use, per disk volume, during the migration. The default value is four.

  5. For mounted images, update the **File Locations** section using instructions in [Configure migration schedule for mount and migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate#configure-schedule).

  6. Click **Submit**. You see a success message.

  7. Click **Okay** to close the message and return to the **Active Mounts** page.




### Run an on-demand migration job

Once you have configured the migration schedule, image migration follows the schedule you specified and migration jobs run at the frequency you specified. However, you can run the migration on demand if needed.

To run an on-demand image migration, complete the following:

  1. Select an active image with an **Image State** of **Migrating**.
  2. Select **Run Migration Job Now** from the drop-down menu.



### Cancel a migration job

To cancel an image migration, follow these steps:

  1. Select an active image with an **Image State** of **Migrating**.
  2. Select **Cancel Migration** from the drop-down menu.
  3. At the warning message, click **Proceed** to cancel. Canceling stops the migration and deletes all data that was copied over during previous migrations.



### Cancel image restore

To cancel an image restore, follow these steps:

  1. Go to the **Active Mounts** page and filter by the **Image State** of **Restore (Migrating)**.
  2. Select the image and then select **Cancel Restore** from the drop-down menu at the bottom of the page.
  3. Click **Proceed** to cancel. This cancels all running and scheduled migration jobs for the image, deletes all data copied by prior migrations, takes the databases offline, and finally performs an unmount and delete of the mounted databases.



## The Backup and DR Microsoft SQL Server DBA guide

This page is one in a series of pages specific to protecting and recovering Microsoft SQL Server databases with Backup and DR. You can find additional information at:

  * [Backup and DR for Microsoft SQL Server Databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sql-server)
  * [Prepare SQL Server databases for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sql-server)
  * [Add a SQL Server database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sql-server)
  * [Configure backup plans for Microsoft SQL Server instances and databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sql-server)
  * [Application details and settings for Microsoft SQL Server instances and databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sql-server)
  * [Mount a SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sql-server)
  * [Mount databases into SQL Always On Availability Groups](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sql-server-aag)
  * [Manage an active mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts)
  * [Migrate a SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sql-server-2)
  * [Clone SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-sql-server)
  * [Recover SQL Server backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sql-server)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
