---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-backup-overview/
title: How is a backup image created? \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:00:08.645935+00:00
---

# How is a backup image created?  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-backup-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  How is a backup image created? Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the stages in creating a backup and the available backup options for supported [application types](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr).

## Stages in creating a backup

To create backups of supported applications such as databases, filesystems, and VMs, you assign a backup plan to run on a schedule, then:

  1. According to the [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan) settings, Backup and DR takes a snapshot image of the source data and saves it in the targeted storage pools.

  2. (optional) Either immediately or at a later time according to the backup plan, Backup and DR copies the image from the targeted pool to an alternate storage pool to generate a second copy. Commonly this is from the snapshot pool to an OnVault pool.




### When application protection takes effect

Applying a backup plan does not immediately protect an application. Protection jobs run on a schedule, according to resource availability. You can also run the job immediately.

  * The backup plan includes a schedule of when to run the protection job for this application, such as daily between 18:00 and 06:00 UTC, every four hours. If you apply protection to an application at 13:00 UTC today, then the first protection operation will be scheduled for 18:00 UTC.

  * At the scheduled time, the job is assigned a **job slot** , which may be available when the job is scheduled, but not always. Job slots are detailed in [About job slots](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs).




### Change backup plan

You can change an application's backup plan at any time. Future backups occur based on the new template. Existing backups are retained according to the template in use when they were created.

### Change tracking mechanisms

A backup/recovery appliance backs up data by making an initial full copy of the data, then making copies of incremental changes. This capability requires the ability to track and backup the changes that occur between backup operations. To track those changes the backup/recovery appliance uses either Compute Engine APIs, the Backup and DR agent or Backup VMware VMs.

Backup and DR uses multiple methods to track changes in source data that include:

  * Agent based change block tracking for SQL Server
  * Agent based change tracking for Linux Logical Volumes (LVM)
  * Compute Engine snapshot change tracking
  * Oracle Block Change tracking
  * VMware based change tracking



#### Agent change tracking driver

The Backup and DR agent with its change tracking driver (sometimes called the filter driver) enables efficient incremental backups by tracking changes from the host side. After the first complete backup of a database, the backup/recovery appliance performs incremental backups by default. If your backups are still always full backups, then check for the following:

  * The change tracking driver is stopped. In this case, restart the change tracking driver service.

  * The Windows change tracking driver is not installed. In this case, uninstall and then make a full install of the Windows Backup and DR agent.

  * For Linux OS, the kernel version is not supported by the installed agent. See [Support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr) for the supported Linux OS versions.




### Full and incremental snapshots

A full snapshot backs up up all the required data in the application. Full snapshots, also called full backups, are taken the first time an application is backed up and in some uncommon situations. After the first full snapshot, Backup and DR takes incremental snapshots, which are much faster.

Incremental snapshots work as follows:

  1. The first full snapshot contains all the source data.

  2. The second and subsequent snapshots only contain new data or modified data. Data that hasn't changed since the full snapshot isn't included. Instead, the subsequent incremental snapshots contain references to the full snapshot image for the unchanged data from the original snapshot.

  3. The next snapshot contains any new or changed data since the second snapshot but no unchanged data from the earlier snapshots. Instead, this snapshot contains references to blocks in earlier snapshots for any unchanged data.




## Backup options

Backup and DR lets you:

  * Agent based backup

  * Backup application data in consistency groups

  * Backup generic applications (LVM)

  * Backup database logs

  * Backup Compute Engine instances

  * Backup VMware VMs




### Agent based backup

The Backup and DR agent is used to backup individual applications and groups of applications on virtual servers. Backup and DR agent is a small-footprint, operating system specific, lightweight service that can be installed on VMware VMs or Compute Engine instances. The Backup and DR agent provides a more granular data backup capability than what is provided by VMware API calls. It lets you:

  * Discover applications
  * Quiesce applications, for application consistency during backup
  * Enables change block tracking for incremental forever backup strategy
  * A single policy template can be applied to multiple applications that are resident on a server.
  * Avoids VMware VMs "stun" issues



Installing the Backup and DR agent on a physical server or VM lets you create a single policy template to backup all applications on the server or several policy templates to backup groups of applications.

### Back up application data in consistency groups

A consistency group is enabled by the Backup and DR agent. As the name implies, consistency groups ensure consistent point-in-time backup and recovery across multiple applications on the same host. To achieve application consistency, members of a consistency group are quiesced and backed up together using a single policy template.

If Backup and DR's database log backup option is enabled in a snapshot policy, then all databases backed up by the policy template in which the snapshot policy resides can be recovered to the same point-in-time. Recovery and rolling forward of the logs (for databases) in a group is performed using the appliance management console with a single action.

In addition to making backup and recovery operations fast, consistency groups consume fewer system resources (VDisks).

### Back up generic applications (LVM)

Most applications are discovered through the Backup and DR agent or through APIs built into Backup and DR. A generic application is an application that you define by pointing to a group of LVM volumes to be protected.

### Back up database logs

Database log backup is enabled in a Snapshot policy's Advanced Options. It enables a single Snapshot policy to backup logs for Microsoft SQL Server databases, Oracle databases, and consistency groups that contain Microsoft SQL Server databases or Oracle databases. The frequency at which database logs are backed up is defined separately from that of the database. For example, a database can be backed up every day and its logs backed up every hour.

The frequency of database log backup is set in minutes, and the frequency at which logs are backed up must not exceed the frequency at which its associated database is backed up. For example, if a database backup frequency is every 24 hours, the log file backup frequency must be less than every 24 hours. The smallest database log backup interval is 15 minutes.

Log retention is defined separately from the retention of the Snapshot policy. Having a separate retention period lets you use logs in conjunction with copies of the database stored in the Snapshot pool.

Regardless of how many logs are backed up during a specified log retention period, a database's backed up logs are staged to a single VDisk in the Backup and DR Snapshot pool. To conserve space in the Snapshot pool, you can use an advanced setting to instruct the database to compress its logs.

### Backup Compute Engine instances

To backup entire Compute Engine instances, the backup/recovery appliance uses Compute Engine APIs. Compute Engine provides change block tracking for Backup and DR's incremental forever backup strategy and can quiesce applications for application consistency during backup.

When an entire virtual server is backed up, a fully functional virtual server (operating system, applications, and their data) is backed up. Having a copy of the entire virtual server ensures that the data can be accessed quickly and without issues.

### Back up VMware VMs

Backup and DR uses VMware vSphere Storage APIs - Data Protection calls to back up an entire VMware virtual server (or specific disks allocated to that VM). These enable change block tracking for Backup and DR's incremental forever backup strategy and quiesce applications for application consistency during backup.

#### Back up a VMware VM's applications and boot volume

When managing applications on VMs you have the option of also backing up the VM's boot volume. When a VM's boot volume is backed up, an image can be presented as a bootable VM. The image can then be migrated to a new, permanent location, if needed.

#### Back up entire VMware VMs

When an entire virtual server is backed up, a fully functional virtual server (operating system, applications, and their data) is backed up. Having a copy of the entire virtual server ensures that the data can be accessed fast and without issues. Because the image presented is a fully functional virtual server, it can be migrated to a new, permanent location if needed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
