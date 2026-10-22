---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup-admin/protection-summary/
title: Find unprotected resources using protection summary \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:24.955022+00:00
---

# Find unprotected resources using protection summary  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup-admin/protection-summary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Find unprotected resources using protection summary Stay organized with collections  Save and categorize content based on your preferences. 

Protection summary helps you manage and verify the data protection status of your Google Cloud resources. It provides a centralized, at-a-glance view of backup configurations for your Compute Engine instances and disks, Cloud SQL instances and Filestore instances across all supported regions. You can use protection summary to view backup configurations at the project, folder, or organization level.

## Benefits

When you utilize protection summary, you get the following benefits:

  * **Holistic protection visibility** : get a centralized overview of your entire backup configuration across all your supported workloads in one place.

  * **Find protection gaps** : pinpoint resources with missing or misconfigured backups and address deviations from your data protection policies.

  * **Seamless integration** : integrate seamlessly with your existing Google Cloud environment and running workloads, providing immediate value without requiring complex configurations or impacting performance.




## Supported resource types

Protection summary is supported for the following resource types:

  * Compute Engine instances

  * Compute Engine disks

  * Cloud SQL instances

  * Filestore instances




## Understanding the _Configured for backup_ status

Protection summary reports a resource as _configured for backup_ based on its association with built-in Google Cloud data protection tools. This view doesn't include data from any third-party backup tools.

A resource is considered configured in the following cases:

  * **Compute Engine instance** : the instance has a [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan) or at least one of its attached disks has a Google Cloud snapshot schedule.

  * **Compute Engine disk** : the disk meets any of the following conditions:

    * It has a Google Cloud snapshot schedule.

    * It is associated with a [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan).

    * It is attached to a virtual machine (VM) that has a backup plan which covers the disk.

  * **Cloud SQL instance** : the instance has a [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan) or built-in Cloud SQL automated backups.

  * **Filestore instance** : the instance has a [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan) or built-in Filestore automated backups.




## Before you begin

To view the protection summary for a project, enable the Backup and DR API in the project where you are viewing the protection summary. When viewing the protection summary at the folder or organization level, you don't need to enable the API to view the summary, but the API must be enabled on a project to schedule backups for its resources.

[Enable the API](https://console.cloud.google.com/apis/library/backupdr.googleapis.com)

For information about protection summary in the Backup and DR API see [API Reference](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference).

### Required IAM permissions

To view the protection summary, you must have the following role or permissions at the project, folder, or organization level corresponding to the scope you want to view:

  * **IAM role** : **Backup and DR Backup Config Viewer**

  * **IAM permissions** :

    * `backupdr.resourceBackupConfigs.list`
    * `backupdr.resourceBackupConfigs.get`
    * `backupdr.resourceBackupConfigs.fetch`
    * `backupdr.locations.list`



## View protection summary across a project, folder, or organization

To view the protection summary for your data resources, do the following:

  1. In the Google Cloud console, go to the **Backup and DR** protection summary page.

[Go to protection summary unprotected resources page](https://console.cloud.google.com/backupdr/protection-summary/list)

  2. Select the scope for which you want to view the protection summary, either **Project** , **Folder** , or **Organization**.

  3. Select the **Resource type** from the drop-down menu, and then click **View**.

The **Unprotected resources** tab is the quickest way to identify unprotected resources.

Protected resources, which are displayed under the **Protected resources** tab, are categorized into two **Configuration states** :

     * **Vaulted** : Shows a list of resources being backed up in a backup vault.

     * **Not vaulted** : Shows a list of all resources that are backed up without a backup vault.




The following fields are displayed in the protection summary:

  * **Resource name** : the display name of the resource.

  * **Project** : the project associated with the resource.

  * **Resource type** : the type of resource—for example, a Compute Engine instance, Compute Engine disk, Compute Engine regional disk, Cloud SQL instance, or Filestore instance.

  * **Backup schedule type** : the type of backup schedule applied to a resource, such as a backup template or snapshot schedule.

  * **Backup plan name** : the name of the resource that provides the backup scheduling configuration. For automated, unnamed backup schedules, this field is empty.

  * **Configuration state** : the backup configuration state. The possible values are **Not configured** , **Not vaulted** , and **Vaulted**.

  * **Backup schedule state** : the status of the backup schedule. The possible values are **Active** and **Inactive**.

  * **Backup scope** : the scope of the specific resource considered for backup, either **Full instance** or **Disk name**.

  * **Backup location** : the zonal, regional, or multi-regional location where the backups are stored.

  * **Latest successful backup** : the timestamp of the latest successful backup—for example, `Mar 1, 2026, 8:45:18 PM`.

  * **Backup vault** : the name of the backup vault used for backups.

  * **PITR configuration** : the name of the point-in-time recovery configuration used for backups.

  * **Public IP address** : the public IP address assigned to the resource.

  * **Private IP address** : the private IP address assigned to the resource.


**Note:** The protection summary displays backup configuration data from both Backup and DR and workload backups. It does not include data from third-party backup providers.

For projects with the Backup and DR API enabled, you can use the **Schedule backup** option to enhance the resource protection using vaulted backups.

If the Backup and DR API is not enabled for a project, the **Schedule backup** option is unavailable. To enable the API, hover over the **Schedule backup** option and onboard to the Introductory Trial (if applicable). Once the Backup and DR API is enabled, you can enhance resource protection using vaulted backups.

## Protection summary supported regions

Protection summary is supported in the following regions.

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

## Limitations

  * Protection summary is only compatible with resources located in regions that have support for the Backup and DR management console. See [Supported regions](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-plan#mc-supported-regions) for a list of supported regions.

  * Data is periodically refreshed, usually within an hour, but in some cases it can take up to 24 hours.




## Programmatically retrieve protection summary information

You can retrieve resource backup configurations programmatically using the protection summary API calls based on your required scope. For more information, see [API Reference](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rpc/google.cloud.backupdr.v1#backupdrprotectionsummary).

  * **Project level** : use the `ListResourceBackupConfigs` API call to retrieve resource backup configurations for a project.

  * **Folder or organization level** : use the `FetchResourceBackupConfigs` API call to retrieve resource backup configurations across a folder or organization.




## Sort and filter protection summary backup configuration information

This section describes how you can sort and filter the backup configurations that are returned by the `ListResourceBackupConfigs` and `FetchResourceBackupConfigs` API calls in the protection summary service.

### Sorting support

Sort (`ASC`,`DESC`) is supported only for `target_resource_display_name`. By default, the API calls return the resource backup configurations ordered alphabetically by the resource name.

### Filtering support

The following fields can be used for filtering the resource backup configurations returned by the API calls:

Field name | Field type | Supported filtering operators  
---|---|---  
`target_resource_display_name` | `string` | Both `:` and `=`  
`target_resource_type` | `string` | `:`  
`backup_configs_details.backup_config_source_display_name` | `string` | `:`  
`backup_configs_details.type` | `string` | `:`  
`backup_configured` | `bool` | `=`  
`vaulted` | `bool` | `=`  
  
Wildcard matching (using `*`) is supported only for the `target_resource_display_name` field.

## Filtering syntax

The filtering syntax follows the API filtering guidance set in [AIP 160](https://google.aip.dev/160), with the following limitations:

  * Only the `AND` operator and nesting are supported. All other operators and combinations, including `OR` and `NOT`, are not supported.

**Examples**

Valid: The filter uses the `AND` operator: `target_resource_display_name="vm-instance1" AND target_resource_type=CLOUDSQL_INSTANCE`

Valid: The filter uses nesting and only the `AND` operator: `(target_resource_display_name="vm-instance1" AND target_resource_type=CLOUDSQL_INSTANCE) AND backup_configured=true`

Invalid: The filter uses the `OR` operator: `target_resource_display_name="vm-instance1" OR target_resource_type=CLOUDSQL_INSTANCE`

  * Prefix match is supported only for `target_resource_display_name`.

**Examples**

Valid: The filter uses a prefix match: `target_resource_display_name:"vm-instance1*"`

Invalid: The filter compares a suffix match: `target_resource_display_name:"*vm-instance1"`

Invalid: The filter compares a suffix match: `target_resource_display_name="vm-instance1*"`




## What's next

  * Read about best practices for defending against ransomware with Backup and DR.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
