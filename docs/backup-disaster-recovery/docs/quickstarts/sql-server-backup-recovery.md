---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/sql-server-backup-recovery/
title: Protect and recover Microsoft SQL server databases from the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:46:11.367502+00:00
---

# Protect and recover Microsoft SQL server databases from the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/sql-server-backup-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Protect and recover Microsoft SQL server databases from the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an end-to-end overview about how to back up and restore Microsoft SQL Server database and monitor backups.

## Configure backup for Microsoft SQL Server

Microsoft SQL Server is a database system that runs on Windows Server. You can use SQL Server on Compute Engine as part of the backend for your applications, as a flexible development and test environment. If you haven't created a high-performance SQL Server instance, you must first create a VM instance with SQL Server. For details, see [Creating a high-performance SQL Server instance](https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance).

### Prerequisite to configure backup

Before you start backing up SQL server databases, the sections in this page must be completed in sequential order. This page assumes the following details about your project:

  * There will be either one or two VMs.

  * Source—production—VM hosting source databases.

  * Target—recovery, test, DR, or non-production—VM to mount virtual copies of the databases.

  * Backup and DR has already been deployed with the backup/recovery appliance installed and the network firewall is configured as directed to allow the required communications between appliance and the SQL Server VMs.




Regardless of whether you deploy new VMs or use existing ones, the following tasks must be performed in sequential order:

  1. The source and target VMs require the Backup and DR agent setup.

  2. The Windows server requires the iSCSI service to be set to started and set to automatic start.

  3. Microsoft SQL Server should be installed.

  4. You can add additional drives to your SQL servers if this is a normal operating procedure, and if you run databases and logs on alternate disk drives.




#### Set up the source Windows Microsoft SQL Server VM

**Note:** All tasks here are performed as a local administrator or equivalent user.

  1. Log into the source VM.

If this is a Compute Engine instance, you need to ensure the iSCSI initiator is started and also auto-start is placed on reboot. To do this, launch the **iSCSI initiator** application using the following steps:

     1. Click the **Start menu**.

     2. Type in **iSCSI initiator** to find the application.

     3. Launch the process.

     4. If you are prompted, click **Yes** to enable iSCSI and have it set to auto-start upon boot. Once this is complete, the **iSCSI Initiator** page appears. Click **Ok** to close.

  2. Open a browser and download the Windows Backup and DR agent from the appliance management console. To download the Backup and DR agent, complete the following steps:

     1. From the appliance management console click the **Manage** drop-down menu and click **Applications**.

     2. Right-click and select the appliance to perform the backup images and select **Configure appliance**.

     3. From the **Appliance configuration** page, go to **Agent management** and download the relevant agent. You might need to do this on a different host and then transfer the executable file to the relevant host.

     4. Click the Windows Backup and DR agent EXE, and select **Run**.

  3. Select **Yes** to begin the installation.

**Important:** You must be a local administrator for the installation to work.
  4. Select the option to install the **Backup and DR agent with change tracking driver**. This installs an additional Windows service that tracks changes for databases larger than 1GB in size.

  5. Click **Next** and agree to install the Backup and DR agent in the default location.

  6. Click **Install** to let the installation begin. When done, click **Finish**.

  7. Open the **Services** control panel and confirm there are two Backup and DR services running. If not, then reinstall the Backup and DR agent and enable **Change block tracking**.

  8. Open a Windows command prompt and change the directory to `C:\Program Files\Google Cloud Backup and DR>`.

  9. Run the following command:
         
         udsagent.exe secret --reset
         

**Note:** Save the secret key, you need to add this in Backup and DR agent section of [add host](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/ms-sql-server-backup-recovery#add-host). This secret key is valid for two hours.
  10. **Optional** : If you want transaction log backup, then you might need to change the **Recovery model** of your databases to _Full_. The default is **Simple** , which means that Backup and DR log backup images never find any logs to back up. This might be the selected setting for your configuration, in which case don't change it. Log into the Microsoft SQL Server Management Studio, then right-click the database and select **Properties**. Go to **Options** and change the **Recovery model** from **Simple** to **Full**.

  11. If you intend on backing up a SQL databases with transaction logs—**Full recovery model** —or if you want to avoid the need to enter credentials for a SQL server into the appliance management console interface when performing recoveries, there are two options available to achieve this.

Use one of these two approaches for the most seamless experience:

     * Option one: Use the `sysadmin` role.

Go to the SQL Instance Security **Login** menu. Right-click on the `NT AUTHORITY\SYSTEM` account and select properties. Then in **Server roles** , select the sysadmin role, and click **OK**. This allows the Backup and DR agent the elevated rights to run log backup images and log recoveries without requiring additional user authentication.

     * Option two: Create a new Windows Administrator account—domain or local OS:

       * Verify or grant the account permissions as follows:

         1. Allow the following rights in SQL: `dbcreator server` role, `db_backup operator database` role, `db_owner database` role

         2. Assign the following securables in SQL: View any database, Create any database, Alter any database, Connect SQL

       * Next, the account should be in the local Windows administrator group, to ensure access to scripts in `C:\Program Files\Google Cloud Backup and DR>` and to make OS calls and handle the staging disks where backup images are stored.

       * Finally, update the Google Cloud Backup and DR agent service to run as this account and restart the service.




#### Add a Microsoft SQL Server host and its databases to the appliance management console

To protect Microsoft SQL Server database, you must first add its host to the appliance management console and then discover the database.

**Note:** If you have added the Windows server to Backup and DR as a Compute Engine instance or as a VMware VM, then a host for this VM already exists and you don't need to add it again. Instead, find and edit that host.

  1. In the appliance management console, click the **Manage** drop-down menu and select **Hosts**.

  2. Click **\+ Add host**.

  3. Enter the name, IP address and click the **plus sign (+)** of your SQL Server VM.

  4. Select your backup/recovery appliance and click **Add**.

  5. In **Backup and DR agent settings** complete the following:

     * Backup and DR agent port is normally port 5106. If it is anything else, enter that port here.

     * Add credentials for the host only if you are backing up SMB shares.

     * You need to supply a secret key generated on [Windows](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-windows) and [Linux](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts) host servers by the Backup and DR agent, to initialize trusted communications between the host and Backup and DR agent. If you don't have a secret key that was generated in the last two hours, reset the key following the instructions in [Set up the source Windows Microsoft SQL Server VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/ms-sql-server-backup-recovery#setup-source) and paste the resulting key into this field. This only needs to be done once. You can use the secret key that was generated when you [Set up the source Windows Microsoft SQL Server VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/ms-sql-server-backup-recovery#setup-source).

  6. In the appliance management console, go to **Back up & Recover**, then **Back up** and choose **Microsoft SQL Server**. Select your newly added server and click **Next** to discover the SQL Instances on the server. This process can take a minute to complete. If it fails, then you might need to verify the correct firewall policy is in place, to allow the backup/recovery appliance access to the SQL server using TCP port 5106. Use the instructions to [Validate backup/recovery appliance to Backup and DR agent connectivity](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-network-settings#validate).

The SQL server instances on the VM is displayed.




### Create a backup plan

This section helps you in creating a backup plan template. Templates are composed of backup policies. In policies, you can define when to run a backup, how frequently to run a backup, how long to retain the backup image for—days, weeks, months, or years, and where they are restored.

  1. In the appliance management console, go to **Backup Plans** drop-down menu and click **Templates**.

  2. Click **Create Template**.

  3. Enter a name and description for your new template, then click the **plus sign (+)** associated with the icon that represents production data.

  4. Enter a policy name, daily window, and retention for the snapshots of your databases. This retention is typically short and it is stored in the snapshot pool on Persistent Disk storage to ensure recovery performance.

  5. Click **Advanced Policy Settings**.

  6. There are several options in the advanced policy settings, most of which should be left at the default values. For a SQL server, these are the most commonly changed settings and the recommended values for best practices:

     * **Truncate/purge log after backup.** Set this to **Truncate**.

     * **Enable database log backup.** Set this to **Yes**.

     * **Log backup retention.** Set this to **7 days**.

     * **Replicate logs.** Set this to **No**.

     * **Send logs to OnVault pool.** Set this to **Yes**.

  7. Click **Save changes**. After making the selections, click **Update policy**.

The snapshot icon appears colored.

  8. Click the **plus sign (+)** between the snapshot and OnVault icons to add an OnVault policy.

  9. Enter a policy name, daily window, and retention for the OnVault copies of your database backup images. The start time of the window should match the time specified in the snapshot policy. This retention is typically longer, ranging from 30 to 90 days, and the copies are stored in Cloud Storage to ensure the right balance of performance and cost. Click **Update policy** when done.

  10. Click **Save template** to save your policies and settings.

When you deploy the appliance management console and backup/recovery appliance, an OnVault pool and a matching resource profile are created automatically. This resource profile is used when protecting the databases.

  11. Add the databases to the appliance management console and protect them as needed. Continue to Add a Microsoft SQL server host and its databases.




### Apply backup plan

In this step, you apply the backup plan policy that you created in Configure a backup policy in the appliance management console to a database discovered in Add a Microsoft SQL server host and its databases to the appliance management console.

When you apply a template for the first time, the backup plan runs immediately and then according to schedule. It takes a snapshot of the database according to the snapshot policy and then copies it to the OnVault pool for longer storage according to the OnVault policy.

  1. Select the SQL Server instance that has the databases you want to back up and click **Next**.

  2. To apply a backup plan, select the instance, then choose **Apply backup plan** from the drop-down menu above the instance list. As you select options, more drop-down menus appears. Select the **Template** and **Profile** that were previously created, then click **OK**.

  3. If you want to select individual databases to include or exclude from backup images, you can click the **All databases** link to bring up the manage membership dialog.

You can choose an inclusion rule to suit your needs for inclusion or exclusion of databases for backup images. Auto-inclusion of new databases is controlled by this selection.

     * **Include all** , **Include user** , and **Exclude selected** result in new databases added to this instance to be backed up automatically.

     * **Include user** and **Include selected** result in a static list of databases to backup, and new databases aren't backed up without manual intervention.

The recommended selection is **Include all**.

  4. After optionally changing the database inclusion rule and saving your changes, click **Next**. You now have the option to modify application settings that determine Microsoft SQL Server specific behaviors during backup images. Keep the defaults and select **Next**.

  5. From the summary display, click **Finish** to initiate the discovery and protection of your SQL server databases. You are presented with a confirmation page reminding you to keep your browser window open, without refreshing, until the discovery is complete. Click **Finish** again.

Proceed after you see the **green checkbox**.

  6. After the backup plan is applied to the SQL instance, backup images begin automatically, based on the schedule within the **Template** policy.




The database should now be backed up successfully. After a few minutes of initiating the backup snapshot, return to the **App manager** , **Applications** menu.

### On-demand backups

On-demand backup is a type of backup that you can manually trigger at any time. On-demand backups are useful for situations where you need to back up your data before a specific event. For example, you might want to back up your VM before applying updates or patches to ensure that you can restore it to its previous state if any issues arise during the update process.

To run an on-demand backup of a managed application:

  1. Click the **App Manager** tab and select the **Applications** option from the drop-down list. The **Applications** page opens.
  2. Select an Google Cloud VMware Engine instance and then click **Manage Backup Configuration** from the drop-down list at the bottom right corner of the page.
  3. From the **Policies** that is on the right, select **Snapshot**.
  4. Enter a **Label** and click **Run Now**. An on-demand backup will be triggered for the selected policy.



## Recover the Microsoft SQL Server instance

Recover is the process of restoring data from a backup image using the **Mount** operation.

  1. In the appliance management console, navigate to the **App Manager** drop-down menu and click **Applications**.

  2. Find your backed up SQL instance or databases, right-click and select **Access**.

  3. Depending on the backup plan configured, You should be able to see captured images in the timeline ramp or table view. You might have images in the snapshot lane and additionally in the OnVault lane. Next, select one of the images and click **Mount**.

**Note:** If you see in the metadata fields on the right side you have a date and time for the recovery range then this is a strong indication that log backup images have succeeded in addition to the full backup.
  4. The **Mount** screen is where you select the target host you want to mount the databases to. This can be back to the source host (choose a new name for the DB), or a different target host. You can also optionally enter a label for the mount, which can be helpful when referring to the mount job later. You also must select the databases to be mounted in the **Select items** area.

Next, provide a name for the database you are mounting. The **User Name** and **Password** fields can be left blank if the Backup and DR UDS Host Agent service has the permissions specified in the section Set up the source Windows Microsoft SQL server VM. Otherwise, you need to enter credentials with those permissions on this screen. Lastly, click **Submit** to run the job. The mount job might take 1-5 minutes, depending on the environment. To monitor the job, go to the **Monitor** drop-down menu in the appliance management console and click **Jobs**.

**Note:** The target Microsoft SQL server must be running the same version or higher as the source server where the backup was run.

If all has succeeded, you can see your mount task using the appliance management console using the **App Manager** drop-down menu and clicking **Active Mounts**.

  5. Go back to the SQL Server instance, and refresh the instance to see your newly mounted database.

  6. Verify the database is available. Select **New query** and paste the following information, replacing `DevCRM` with the name of the mounted database:
         
         USE [DevCRM]
             SELECT * from [Customers];
           




### Mount and migrate your database

Mount and migrate lets you access a database quickly using the mount operation and then restore the database while it is running, with a small interruption at a later time to switch from the mounted disks to the server's attached disks.

  1. In the appliance management console, navigate to **App Manager** drop-down menu and click **Active Mounts**.

  2. Right-click on the database and select **Migrate**.

  3. Select the **Frequency** which is the duration in hours between incremental refreshes of the mounted database to the server's attached disks. This process repeats until the final switchover is done. Additionally you can configure the copy thread count—between 1-20— and optionally select the new file and folder location for the restored copy. Click **Submit** to start the process.

  4. During the migrate job, the database still runs as a mounted database hosted from the snapshot pool in the backup/recovery appliance. When the first migrate job is complete, a locally restored copy of the SQL database and log files are present on the target SQL server.

  5. Finalize the migration. This takes the database offline, performs a final sync of the current data to the server's attached disks, switches SQL server to reference the restored database files, and then brings the database back online. For many large databases, this process can run less than five minutes depending on the rate of change. From the **App Manager** drop-down menu in the appliance management console, click **Active Mounts** and select the database you want to finalize the migration for. Then, select **Finalize migration**.

  6. Confirm the finalize task, and click the **Proceed** option.

Finally, Backup and DR also cleans up the previous mounted disks as part of the finalize task. You don't need to perform clean-up tasks manually.




## Monitor

You can monitor the Microsoft SQL Server jobs, from the [monitor jobs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs) and [monitor events](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-events).

## What's next

This page is a quickstart to protect and recover Microsoft SQL server databases with Backup and DR. You can find additional information at:

  * [Backup and DR for Microsoft SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sql-intro)
  * [Prepare Microsoft SQL Server databases for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sql-server)
  * [Add Microsoft SQL Server database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sql-server)
  * [Configure backup plans for Microsoft SQL Server instances and databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/sql-protect)
  * [Mount Microsoft SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-access)
  * [Migrate Microsoft SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-server-mount-and-migrate)
  * [Clone Microsoft SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-cloning)
  * [Recover Microsoft SQL Server backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
