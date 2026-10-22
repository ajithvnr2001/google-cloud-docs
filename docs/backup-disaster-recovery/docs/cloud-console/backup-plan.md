---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan/
title: Backup plans overview \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:41.657337+00:00
---

# Backup plans overview  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup plans overview Stay organized with collections  Save and categorize content based on your preferences. 

[Setup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create)

This page describes backup plans, which let you define advanced backup strategies to back up your resources. You can use backup plans to back up the following resources:

  * Cloud SQL instances

  * Compute Engine instances and disks

  * AlloyDB for PostgreSQL clusters

  * Filestore instances




In a backup plan, you can define when and how to back up a resource. You can include the backup frequency, the backup retention period, and the [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault) location to store backups. When you associate a backup plan to a resource, the Backup and DR automatically backs up and retains backups for those resources according to the configuration in the backup plan.

Before you create a backup plan, you must designate the storage location for your backups by creating a [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

**Note:** The backup vault and backup plan must be in the same project and in [compatible locations](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#workload-location-compatibility).

A backup plan includes one or more backup rules. Each backup rule defines the following parameters:

  * **Frequency** : You can schedule backups to run hourly, daily, weekly, monthly, or yearly.

    * **Hourly** : The available frequency depends on the resource type. For more information, see Frequency ranges for hourly backups.

    * **Weekly** : You can select a specific day of the week.

    * **Monthly** : You can select a specific day of the month (for example, the 15th).

  * **Backup type** : You can use rules for scheduled backups or initiate on-demand backups.

  * **Backup window** : You can define the timeframe when backup jobs can start. The backup window has the following requirements:

    * It must use a 24-hour clock format, with start and end times between 00 and 24.

    * It must be at least six hours long.




Constraint: A backup plan always includes the boot disk. If you select **Exclude boot disk** in the **Data protection** section of the **Machine configuration** , the backup plan still includes the boot disk. For more information, see [Create an instance with additional non-boot disks](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-additional-non-boot-disks).

## Frequency ranges for hourly backups

This section specifies the frequency for hourly backups. An hourly frequency of `1` means jobs run every hour from the start time until the end time.

  * If `recurrence_type` is set to `HOURLY`, then this setting is required.

  * If `recurrence_type` is not `HOURLY`, then this setting is not applicable.

  * If you supply a value for this setting and `recurrence_type` is not `HOURLY`, a validation error occurs.




The supported values for each resource type are as follows:

Resource Type | Hourly Frequency  
---|---  
Compute Engine instance | 1-23  
Compute Engine disk | 1-23  
Cloud SQL instance | 6-23  
AlloyDB for PostgreSQL cluster | 1-23  
Filestore instance | 1-23  
  
For Compute Engine instance resources, refer to [best practices for hourly backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cloud_best_practices).

## Database log backups

For database resources (like Cloud SQL or AlloyDB), you can enable log backups within the backup plan. This allows for Point-in-Time Recovery (PITR) by capturing transaction logs between full backup points.

## Overview of data retention in Backup and DR

Backup and DR manages backup lifecycles and security using two retention types:

  1. **Assigned retention period** : Defined in the backup plan using the **Delete backups after** setting.

     * Backups are retained for this period and expire at its end.

     * You can delete backups manually before this date unless enforced retention prevents it.

  2. **Enforced retention period** : Defined in the [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault) configuration using the **Prevent deletion for** setting.

     * This setting ensures backups cannot be deleted for the specified period.

     * If the enforced retention period is longer than the assigned retention period, backups are not deleted until the enforced retention period ends.

     * You can apply an enforced retention period to an entire backup vault, or you can configure the backup vault to enforce the assigned retention period (**Delete backups after**) for each protected resource.




## Maximum custom on-demand retention

This setting defines the maximum number of days an on-demand backup (created manually outside the automated schedule) can be retained. This prevents users from accidentally setting excessively long retention periods for manual snapshots.

## Backup storage consumption

Consider the following rules for backup storage in a backup plan:

  * **Automatic deletion** : Backups are automatically deleted when the defined backup retention period is reached.

  * **Minimum retention** : The backup retention period must be equal to or greater than the minimum retention period of the backup vault.

  * **Inherited default** : The default value for backup deletion is inherited from the minimum retention period of the backup vault.

  * **Immutability** : Backups created using a backup plan are immutable. They cannot be modified or deleted during the minimum enforced retention period of the backup vault.




### Backing up workloads to a CMEK-enabled backup vault

If you configure a backup vault with CMEK, backups stored in it are protected using your specified key. The following rules apply when associating a backup plan with a CMEK-enabled vault:

  * **CMEK-protected workloads** : If a source workload is protected by CMEK (for example, a Compute Engine instance with CMEK-encrypted disks), you **must** back it up to a CMEK-enabled backup vault. You cannot back up a CMEK-protected resource to a backup vault that uses Google-owned and Google-managed encryption keys.

  * **Workloads using Google-owned and Google-managed encryption keys** : If a source workload uses Google-owned and Google-managed encryption keys, you **must** back it up to a backup vault that uses Google-owned and Google-managed encryption keys.




## Backup job retries

When a scheduled job fails, the scheduler automatically retries the job up to three more times. 

  * **First failure** : Status marked "Retried"; waits 4 minutes.
  * **Second failure** : Next retry queued after 16 minutes.
  * **Third failure** : Final retry queued after 64 minutes.
  * **Final failure** : After 4 total attempts, status changes to "Failed". No further jobs are attempted for that schedule period.



Job retries are reported in **Monitor** > **Jobs**. To identify retries, all four jobs will share the same Job number with a unique suffix (e.g., `Job_12345`, `Job_12345a`, `Job_12345b`).

## Backup plan supported regions

Backup plans can be created only in regions where the Backup and DR is available and where the resources to be backed up are located. To create a backup plan, a backup vault must also be available in a [compatible location](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#workload-location-compatibility). If you need to create a backup plan in an unsupported region, use the [backup templates](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) in the appliance management console.

Backup plans are supported in the following regions.

Geographic Area | Region Name | Region Description |   
---|---|---|---  
**North America** |  |  |   
| `northamerica-northeast1` * | Montréal |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `northamerica-northeast2` | Toronto |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-central1` | Iowa |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-east1` | South Carolina |   
| `us-east4` | Northern Virginia |   
| `us-east5` | Columbus |   
| `us-south1` | Dallas |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-west1` | Oregon |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `us-west2` | Los Angeles |   
| `us-west3` | Salt Lake City |   
| `us-west4` | Las Vegas |   
| `northamerica-south1` * | Querétaro |   
**South America** |  |  |   
| `southamerica-east1` | São Paulo |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `southamerica-west1` | Santiago |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
**Europe** |  |  |   
| `europe-central2` | Warsaw |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-north1` | Finland |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-north2` | Stockholm |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-southwest1` | Madrid |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west1` | Belgium |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west2` | London |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west3` | Frankfurt |   
| `europe-west4` | Netherlands |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west6` | Zürich |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west8` | Milan |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west9` | Paris |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
| `europe-west10` | Berlin |   
| `europe-west12` | Turin |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
**Middle East** |  |  |   
| `me-central1` | Doha |   
| `me-central2` | Dammam |   
| `me-west1` | Israel |   
**Africa** |  |  |   
| `africa-south1` | Johannesburg |   
**Asia Pacific** |  |  |   
| `asia-east1` | Taiwan |   
| `asia-east2` | Hong Kong |   
| `asia-northeast1` | Tokyo |   
| `asia-northeast2` * | Osaka |   
| `asia-northeast3` | Seoul |   
| `asia-southeast1` | Singapore |   
| `asia-southeast2` | Jakarta |   
| `australia-southeast1` | Sydney |   
| `australia-southeast2` | Melbourne |   
**India** |  |  |   
| `asia-south1` | Mumbai |   
| `asia-south2` | Delhi |   
  
* Querétaro (northamerica-south1), Montréal (northamerica-northeast1), and Osaka (asia-northeast2) don't support zone separation. This means the multiple zones within each of these regions may not be located in physically separate data center campuses. Consequently, a single, localized physical disaster event could potentially impact multiple zones within the same region, increasing the risk of data loss compared to regions that support zone separation.

## Backup plan and rule names

Your backup plan names and rule names must meet the following requirements:

  * Contain lowercase letters, numeric characters, dashes (`-`), underscores (`_`), and periods (`.`), spaces are not allowed
  * Start and end with a number or letter
  * Maximum of 63 characters
  * Cannot be represented as an IP address in dotted-decimal notation. For example, `192.0.2.255`



## What's next

  * [Create and manage a backup plan for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
