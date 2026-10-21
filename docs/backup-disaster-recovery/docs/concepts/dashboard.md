---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/dashboard/
title: Introduction to the backup/recovery appliance dashboard \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:07.075194+00:00
---

# Introduction to the backup/recovery appliance dashboard  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Introduction to the backup/recovery appliance dashboard Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The dashboard provides an aggregated view of appliance health and system resource utilization for all managed backup/recovery appliances. The information is presented through a variety of panels like the Applications panel, Job status panel, Events panel, Protected data panel, Appliances health panels, and Updates panel. When a situation requires attention, calls-to-action are prominently shown as red numbers with links to more information.

You can filter the appliance-related data displayed in the dashboard by appliance.

## The applications panel

The **Applications** panel shows you three categories of discovered applications data:

  * **Managed** : Identifies how many of your discovered applications are managed (backup plans assigned to applications and management enabled in the **App Manager**). Click the number to go to the **App Manager** list of applications, filtered to show managed applications.

**Note:** If there is an assigned management of the same applications to multiple backup/recovery appliances, and the application is in a managed state on one appliance and in an unmanaged state on another appliance, that application will be identified as **Managed** in the **Applications** window.
  * **Unmanaged** : Identifies how many of your discovered applications are unmanaged by a backup plan. Click the number to go to the **App Manager** list of applications, filtered to show unmanaged applications. From the **App Manager** , you can assign a backup plan.

  * **Unscheduled** : Identifies how many of your discovered applications have backup plans assigned to them but the backup plan management of those applications is disabled. Click the number to go to the **App Manager** list of applications, filtered to show applications with backup plan management disabled. From the **App Manager** , you can re-assign a backup plan.




The **Applications** panel polls for fresh data every two minutes.

**Note:** Application data is measured and tracked across all managed backup/recovery appliances. The appliance management console displays the applications and VMs captured by each appliance in the dashboard, but won't count duplicate applications if those applications are VMs or remote applications captured from multiple backup/recovery appliances. For example, if the same two VMs are managed by two different backup/recovery appliances, the appliance management console only counts two managed applications, not four.

## The job status panel

The **Job Status** panel provides information about jobs that have run over the past 24 hours (default).

  * **Current or Past Jobs** : A quick view of how many jobs have succeeded, failed, were retried or canceled, or are running.
  * **Job Types or Appliance** s: Links to the **Monitor** filtered to show the status of jobs by job type over the last 24 hours or by managed backup/recovery appliance.



In the past jobs section, you can also view the status of the last week or last month if needed. This panel fetches fresh data every two minutes.

## The events panel

The **Events** panel provides quick access to error and warning events that have occurred over the past 24 hours. It polls for fresh data every two minutes.

  * **Errors number** : Shows errors over the past 24 hours.
  * **Warnings number** : Shows warnings over the past 24 hours.



Click the **Errors** or **Warnings** number area to access the **Events View**.

## The appliances health panel

The **Appliances Health** panel provides an overview of resource usage and system health for all managed backup/recovery appliances. Each colored block in the different resource usage and system health areas of panel identifies the number of managed appliances.

It polls for fresh data every two minutes and shows the following information:

  * **Disk Usage** : Current percent utilization of the default pools (snapshot and primary pools) for the managed appliances. If you don't have access to that information, then you see no values.
  * **Hardware** : Status of VDisk utilization for the managed appliances.
  * **Software** : Status of local snapshot and remote management for the managed appliances.
  * **appliance management console Connections** : Status of the state of communication between the appliance management console and its managed backup/recovery appliances. This status is based on the last synchronization and whether the appliance is reachable by the appliance management console.



If the blocks in the **Appliances Health** panel are green then this means that everything is working normal within the set resource parameters for each managed appliance. If there are any other colors visible, then log a support call.

**Note:** See this table for a legend of different state colors of the different system health components in the dashboard.

If you click the number in each colored block, it will bring you to the **Storage Pools** window (disk usage) or to the **Appliances** window (hardware, software, and the appliance management console connections) as a means to help identify the backup/recovery appliance that is experiencing system health issues.

The following table outlines the different state colors of the different appliance health components in the dashboard for the managed backup/recovery appliances.

Appliance Health Component | Legend  
---|---  
**Disk Usage** |   
Snapshot Pool | **Green** : The pool usage is in accordance with user specifications.   
**Yellow** : The pool usage is over the specified warning limit.   
**Red** : The pool usage is over the specified safe limit.  
Primary Pool | **Green** : The pool usage is in accordance with user specifications.   
**Yellow** : The pool usage is over the specified warning limit.   
**Red** : The pool usage is over the specified safe limit.  
**Hardware** |   
VDisk Utilization | **Green** : The VDisk counts are below the specified warning limit.   
**Red** : The VDisk counts are above the specified warning limit.   
**Software** |   
Local Snapshot | **Green** : The snapshot software component is active.   
**Red** : The snapshot software component is off.  
Remote Manage | **Green** : The replication software component is in good condition.   
**Yellow** : One or more replication jobs are stalled.   
**Red** : The replication software component is offline.   
**Gray** : The replication software component is disabled.  
**Management Console Connections** |   
Appliances | **Green** : The backup/recovery appliance connections to the appliance management console are active and communication is successful.   
**Red** The backup/recovery appliance connections to the appliance management console is stale and not reachable based during the last synchronization between the appliance management console and the appliance.  
  
## Protected data

The protected data panel shows the measure of protected source data. This data is used in billing for Backup and DR. The data in the panel is represented in the stack bar chart in TeraBytes (TBs).

For Google Cloud VMware Engine, it displays the number of Google Cloud VMware Engine nodes being protected. Nodes can be ve1 nodes or storage-only nodes. Storage-only node count is displayed only if you protect at least one ve1 node, even though storage-only nodes are added to a cluster.

For workloads other than Google Cloud VMware Engine, such as VMs, file systems, and databases, the protected data is calculated based on the data size of protected applications. These protected applications are divided into three categories and pricing is calculated based on these categories.

The following table lists the application types that are supported in the appliance management console.

VM/File System | Tier-1 DB | Tier-2 DB  
---|---|---  
Compute Engine Instance | IBM Db2 | SAP ASE  
File System | Oracle | SAP IQ  
Generic LVM Volume | SAP HANA | SAP MaxDB  
NAS (NFS/SMB) | Microsoft SQL Server | PostgresQL  
VMware VM |  |   
  
## Appliance updates panel

This panel displays the number of appliances that are **Pending** and **Overdue** to update. Clicking the **Overdue** or **Pending** takes you to the **Appliances** page.

## Help and other resources

In the upper right corner of the dashboard and every page of the management console, the **?** icon opens a menu of help and other resources:

  * **Help** : The help brings you to the page in the product documentation that most closely reflects your location within the appliance management console. For example, if you click the **Help** from the dashboard, this page opens. If you click **Help** while editing a backup plan, the [Manage backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) page opens.
  * **API Documentation** : This opens the API reference documentation.
  * **Videos** : This selection brings you to the [How-to videos](https://docs.cloud.google.com/backup-disaster-recovery/docs/how-to-videos) page with six helpful overview videos.
  * **About** : This selection shows you the current version of the management console. It also includes a **Third Party Licenses** link to download a zipped file of the license information for third-party software used in the appliance management console.  
For the third party licenses in use by a backup/recovery appliance, go to **Manage Appliances** , select the appliance, and click **Configure Appliance**. In the lower left corner of the Appliance Configuration page, click the **gear icon** and select the **Third Party Licenses** link to download a zipped file of the license information for third-party software used in that specific backup/recovery appliance.
  * **Guided Tour** : The Guided Tour brings you on a 10-step graphic tour through the appliance management console.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
