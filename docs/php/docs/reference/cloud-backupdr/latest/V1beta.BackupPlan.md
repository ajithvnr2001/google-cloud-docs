---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan
title: Google Cloud Backup Dr V1beta Client - Class BackupPlan (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:07.308636+00:00
---

# Google Cloud Backup Dr V1beta Client - Class BackupPlan (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class BackupPlan (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class BackupPlan.

A `BackupPlan` specifies some common fields, such as `description` as well as one or more `BackupRule` messages. Each `BackupRule` has a retention policy and defines a schedule by which the system is to perform backup workloads.

Generated from protobuf message `google.cloud.backupdr.v1beta.BackupPlan`

## Namespace

Google \ Cloud \ BackupDR \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ disk_backup_plan_properties` |  `[DiskBackupPlanProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DiskBackupPlanProperties)`   
Optional. Defines optional properties specific to backups of disk-based resources, such as Compute Engine Persistent Disks. This includes settings like whether to perform a guest flush.  
`↳ compute_instance_backup_plan_properties` |  `[ComputeInstanceBackupPlanProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ComputeInstanceBackupPlanProperties)`   
Optional. Defines optional properties specific to backups of compute instance based resources, such as Compute Engine Instances. This includes settings like whether to perform a guest flush.  
`↳ name` |  `string`   
Output only. Identifier. The resource name of the `BackupPlan`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`  
`↳ description` |  `string`   
Optional. The description of the `BackupPlan` resource. The description allows for additional details about `BackupPlan` and its use cases to be provided. An example description is the following: "This is a backup plan that performs a daily backup at 6pm and retains data for 3 months". The description must be at most 2048 characters.  
`↳ labels` |  `array|Google\Protobuf\Internal\MapField`   
Optional. This collection of key/value pairs allows for custom labels to be supplied by the user. Example, {"tag": "Weekly"}.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. When the `BackupPlan` was created.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. When the `BackupPlan` was last updated.  
`↳ backup_rules` |  `array<[BackupRule](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupRule)>`   
Optional. The backup rules for this `BackupPlan`.  
`↳ max_custom_on_demand_retention_days` |  `int`   
Optional. Optional field to configure the maximum number of days for which a backup can be retained. This field is only applicable for on-demand backups taken with custom retention value.  
`↳ state` |  `int`   
Output only. The `State` for the `BackupPlan`.  
`↳ resource_type` |  `string`   
Required. The resource type to which the `BackupPlan` will be applied. Examples include, "compute.googleapis.com/Instance", "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster", "compute.googleapis.com/Disk".  
`↳ etag` |  `string`   
Optional. `etag` is returned from the service in the response. As a user of the service, you may provide an etag value in this field to prevent stale resources.  
`↳ backup_vault` |  `string`   
Required. Resource name of backup vault which will be used as storage location for backups. Format: projects/{project}/locations/{location}/backupVaults/{backupvault}  
`↳ backup_vault_service_account` |  `string`   
Output only. The Google Cloud service account to be used by the BackupVault for taking backups. Specify the email address of the Backup Vault Service Account.  
`↳ log_retention_days` |  `int|string`   
Optional. Applicable only for Cloud SQL resource_type. Configures how long logs will be stored. It is defined in “days”. This value should be greater than or equal to minimum enforced log retention duration of the backup vault.  
`↳ supported_resource_types` |  `string[]`   
Output only. All resource types to which backupPlan can be applied.  
`↳ revision_id` |  `string`   
Output only. The user friendly revision ID of the `BackupPlanRevision`. Example: v0, v1, v2, etc.  
`↳ revision_name` |  `string`   
Output only. The resource id of the `BackupPlanRevision`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`  
  
### getDiskBackupPlanProperties

Optional. Defines optional properties specific to backups of disk-based resources, such as Compute Engine Persistent Disks. This includes settings like whether to perform a guest flush.

**Returns**  
---  
**Type** | **Description**  
`[DiskBackupPlanProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DiskBackupPlanProperties)|null` |   
  
### hasDiskBackupPlanProperties

### setDiskBackupPlanProperties

Optional. Defines optional properties specific to backups of disk-based resources, such as Compute Engine Persistent Disks. This includes settings like whether to perform a guest flush.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DiskBackupPlanProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.DiskBackupPlanProperties)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getComputeInstanceBackupPlanProperties

Optional. Defines optional properties specific to backups of compute instance based resources, such as Compute Engine Instances. This includes settings like whether to perform a guest flush.

**Returns**  
---  
**Type** | **Description**  
`[ComputeInstanceBackupPlanProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ComputeInstanceBackupPlanProperties)|null` |   
  
### hasComputeInstanceBackupPlanProperties

### setComputeInstanceBackupPlanProperties

Optional. Defines optional properties specific to backups of compute instance based resources, such as Compute Engine Instances. This includes settings like whether to perform a guest flush.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ComputeInstanceBackupPlanProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ComputeInstanceBackupPlanProperties)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

Output only. Identifier. The resource name of the `BackupPlan`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Identifier. The resource name of the `BackupPlan`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Optional. The description of the `BackupPlan` resource.

The description allows for additional details about `BackupPlan` and its use cases to be provided. An example description is the following: "This is a backup plan that performs a daily backup at 6pm and retains data for 3 months". The description must be at most 2048 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Optional. The description of the `BackupPlan` resource.

The description allows for additional details about `BackupPlan` and its use cases to be provided. An example description is the following: "This is a backup plan that performs a daily backup at 6pm and retains data for 3 months". The description must be at most 2048 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLabels

Optional. This collection of key/value pairs allows for custom labels to be supplied by the user. Example, {"tag": "Weekly"}.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setLabels

Optional. This collection of key/value pairs allows for custom labels to be supplied by the user. Example, {"tag": "Weekly"}.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. When the `BackupPlan` was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. When the `BackupPlan` was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. When the `BackupPlan` was last updated.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. When the `BackupPlan` was last updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupRules

Optional. The backup rules for this `BackupPlan`.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[BackupRule](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupRule)>` |   
  
### setBackupRules

Optional. The backup rules for this `BackupPlan`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[BackupRule](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupRule)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMaxCustomOnDemandRetentionDays

Optional. Optional field to configure the maximum number of days for which a backup can be retained. This field is only applicable for on-demand backups taken with custom retention value.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setMaxCustomOnDemandRetentionDays

Optional. Optional field to configure the maximum number of days for which a backup can be retained. This field is only applicable for on-demand backups taken with custom retention value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The `State` for the `BackupPlan`.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan.State).  
  
### setState

Output only. The `State` for the `BackupPlan`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResourceType

Required. The resource type to which the `BackupPlan` will be applied.

Examples include, "compute.googleapis.com/Instance", "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster", "compute.googleapis.com/Disk".

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setResourceType

Required. The resource type to which the `BackupPlan` will be applied.

Examples include, "compute.googleapis.com/Instance", "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster", "compute.googleapis.com/Disk".

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEtag

Optional. `etag` is returned from the service in the response. As a user of the service, you may provide an etag value in this field to prevent stale resources.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEtag

Optional. `etag` is returned from the service in the response. As a user of the service, you may provide an etag value in this field to prevent stale resources.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupVault

Required. Resource name of backup vault which will be used as storage location for backups. Format: projects/{project}/locations/{location}/backupVaults/{backupvault}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBackupVault

Required. Resource name of backup vault which will be used as storage location for backups. Format: projects/{project}/locations/{location}/backupVaults/{backupvault}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupVaultServiceAccount

Output only. The Google Cloud service account to be used by the BackupVault for taking backups. Specify the email address of the Backup Vault Service Account.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBackupVaultServiceAccount

Output only. The Google Cloud service account to be used by the BackupVault for taking backups. Specify the email address of the Backup Vault Service Account.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLogRetentionDays

Optional. Applicable only for Cloud SQL resource_type.

Configures how long logs will be stored. It is defined in “days”. This value should be greater than or equal to minimum enforced log retention duration of the backup vault.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setLogRetentionDays

Optional. Applicable only for Cloud SQL resource_type.

Configures how long logs will be stored. It is defined in “days”. This value should be greater than or equal to minimum enforced log retention duration of the backup vault.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSupportedResourceTypes

Output only. All resource types to which backupPlan can be applied.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setSupportedResourceTypes

Output only. All resource types to which backupPlan can be applied.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRevisionId

Output only. The user friendly revision ID of the `BackupPlanRevision`.

Example: v0, v1, v2, etc.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setRevisionId

Output only. The user friendly revision ID of the `BackupPlanRevision`.

Example: v0, v1, v2, etc.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRevisionName

Output only. The resource id of the `BackupPlanRevision`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setRevisionName

Output only. The resource id of the `BackupPlanRevision`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResourceProperties

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
