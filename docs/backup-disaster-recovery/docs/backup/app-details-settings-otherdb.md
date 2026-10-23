---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-otherdb/
title: Configure application details and settings for other database types in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:31.268342+00:00
---

# Configure application details and settings for other database types in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-otherdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure application details and settings for other database types in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## Before you begin

After you configure the staging disk type on your host and configure your backup method, you need to configure application details and settings on your database.

## Common use cases

You can choose and apply settings for the following database types:

  * [IBM Db2](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/db2-intro)

  * [PostgreSQL](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/postgresql-intro)

  * [SAP ASE](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sap-ase-intro)

  * [SAP IQ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sap-iq-intro)

  * [SAP MaxDB](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/maxdb-intro)




## Set application details and settings for your database

Based on your application type and host, enter the settings you want to apply to your database backup plan:

  1. In the appliance management console, go to **App manager** and click **Applications**.

  2. Right-click the database and click **Manage backup plan**.

  3. Click **Details & settings**.

  4. In the **Application details & settings** window, configure database settings based on your host type.

Setting | Block | NFS  
---|---|---  
**Use staging disk granularity as minimum staging disk size** | Not applicable. | The default value is zero when you select **No**. If you select **Yes** , you must enter a value in GB in the **Staging disk granularity** field.   
  
This setting is for applications that are less than the size of the granularity setting and tend to grow periodically. This settings helps avoid frequent and costly full backups.   
  
There is no initial cost to use a staging disk that is larger than required for immediate use because the staging disk is thin-provisioned.  
**Staging disk granularity (GB)** | Not applicable. | Enter the maximum size of each staging disk when multiple staging disks are used for an application. The default value is **1000 GB**.  
**Last staging disk minimum size (GB)** | Not applicable. | Enter the minimum size of the last staging disk created for an application with multiple staging disks.   
  
This value is also used for additional disks allocated to accommodate growth. The default value is 250 GB.  
**Backup and DR agent options** | Use this only under the direction of support.  
**Percentage of reserve space in volume group** | We recommend **20%** for logical volume manager (LVM) snapshot temporary space.   
  
This option is not applicable for protecting virtual databases. | Not applicable.  
**Backup capture method** | Select **Use volume-level backup**. | Select Full+Incremental backup.   
  
Note: PostgreSQL databases always complete full backups with no increments.  
**Force Full Filesystem Backup**   
  
Not applicable for PostgreSQL databases which always take a full backup. | Not applicable. | To always get a full backup, set to **Yes**.  
**Database filesystem staging disk size in GB** | Not applicable. | Use the default calculation: _(Database size × 1.5) + 10%_.   
  
When you select this option, disks grow dynamically.  
**Log backup staging disk size in GB** | By default, Backup and DR calculates this as daily log generation multiplied by the retention of log backup plan with a 20% buffer.   
  
The default is recommended. When you provide a value, the default calculation is overridden and becomes a fixed size.  
**Retention of production DB logs in hours**   
  
Not applicable for ASE. | This value is used to purge the log backup from `basepath_logbackup` destination.   
  
Based on this setting, the last data backup ID is selected (`CURRENT_TIMESTAMP` subtracted by the number of days set) and the log that is older than the data backup ID is purged.   
  
The default value is zero days. When the default value is used, all logs prior to the last data backup are purged.  
**Script timeout** | The timeout value (in seconds) is applied to internal backup and recovery scripts called by Backup and DR agent.   
  
The default value is 172800 (48 hours).  
**Number of stripes**   
  
Applicable for ASE only.  | Striping means to read or write a single dump to multiple files. To increase I/O, increase the number of stripes used by the backup server.   
  
The default value is four.  
**Compression level**   
  
Applicable for ASE only. | Not applicable. | Enter a value of 100, 101, or between 0 and 9. Any other value is read as zero.  
**Use buffered block copy** * | Select **Yes** only under the direction of support.   
  
This option is not valid for NFS staging disks.  
  5. Click **Save changes**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
