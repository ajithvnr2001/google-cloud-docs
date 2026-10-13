---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs
title: REST Resource: projects.locations.resourceBackupConfigs \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:57.554147+00:00
---

# REST Resource: projects.locations.resourceBackupConfigs  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  REST Resource: projects.locations.resourceBackupConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ResourceBackupConfig
    * JSON representation
  * ResourceType
  * BackupConfigDetails
    * JSON representation
  * BackupDrPlanConfig
    * JSON representation
  * BackupDrPlanRule
    * JSON representation
  * BackupDrTemplateConfig
    * JSON representation
  * Type
  * State
  * PitrSettings
    * JSON representation
  * BackupLocation
    * JSON representation
  * Type
  * Methods



## Resource: ResourceBackupConfig

ResourceBackupConfig represents a resource along with its backup configurations.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "targetResource": string,
      "targetResourceDisplayName": string,
      "targetResourceType": enum ([ResourceType](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#ResourceType)),
      "targetResourceLabels": {
        string: string,
        ...
      },
      "backupConfigsDetails": [
        {
          object ([BackupConfigDetails](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupConfigDetails))
        }
      ],
      "backupConfigured": boolean,
      "vaulted": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the ResourceBackupConfig. Format: projects/{project}/locations/{location}/resourceBackupConfigs/{uid}  
`uid` |  `string` Output only. The unique identifier of the resource backup config.  
`targetResource` |  `string` Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the cloud resource that this configuration applies to. Supported resource types are `[ResourceBackupConfig.ResourceType](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#ResourceType)`.  
`targetResourceDisplayName` |  `string` Output only. The human friendly name of the target resource.  
`targetResourceType` |  `enum (`[ResourceType](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#ResourceType)`)` Output only. The type of the target resource.  
`targetResourceLabels` |  `map (key: string, value: string)` Labels associated with the target resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`backupConfigsDetails[]` |  `object (`[BackupConfigDetails](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupConfigDetails)`)` Backup configurations applying to the target resource, including those targeting its related/child resources. For example, backup configuration applicable to Compute Engine disks will be populated in this field for a Compute Engine VM which has the disk associated.  
`backupConfigured` |  `boolean` Output only. Whether the target resource is configured for backup. This is true if the backupConfigsDetails is not empty.  
`vaulted` |  `boolean` Output only. Whether the target resource is protected by a backup vault. This is true if the backupConfigsDetails is not empty and any of the `[ResourceBackupConfig.backup_configs_details](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#ResourceBackupConfig.FIELDS.backup_configs_details)` has a backup configuration with `[BackupConfigDetails.backup_vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupConfigDetails.FIELDS.backup_vault)` set.  
  
## ResourceType

The type of the cloud resource.

Enums  
---  
`RESOURCE_TYPE_UNSPECIFIED` | Resource type not set.  
`CLOUD_SQL_INSTANCE` | Cloud SQL instance.  
`COMPUTE_ENGINE_VM` | Compute Engine VM.  
`COMPUTE_ENGINE_DISK` | Compute Engine Disk.  
`COMPUTE_ENGINE_REGIONAL_DISK` | Compute Engine Regional Disk.  
`FILESTORE_INSTANCE` | Filestore Instance.  
  
## BackupConfigDetails

BackupConfigDetails has information about how the resource is configured for backups and about the most recent backup taken for this configuration.

JSON representation  
---  
      
    
    {
      "backupConfigSource": string,
      "backupConfigSourceDisplayName": string,
      "type": enum ([Type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#Type)),
      "state": enum ([State](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#State)),
      "pitrSettings": {
        object ([PitrSettings](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#PitrSettings))
      },
      "latestSuccessfulBackupTime": string,
      "applicableResource": string,
      "backupVault": string,
      "backupLocations": [
        {
          object ([BackupLocation](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupLocation))
        }
      ],
    
      // Union field plan_specific_config can be only one of the following:
      "backupDrPlanConfig": {
        object ([BackupDrPlanConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupDrPlanConfig))
      },
      "backupDrTemplateConfig": {
        object ([BackupDrTemplateConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupDrTemplateConfig))
      }
      // End of list of possible types for union field plan_specific_config.
    }  
  
Fields  
---  
`backupConfigSource` |  `string` Output only. The full resource name of the backup config source resource. For example, "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPlans/{backupplanId}" or "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolicies/{resourcePolicyId}".  
`backupConfigSourceDisplayName` |  `string` Output only. The display name of the backup config source resource.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#Type)`)` Output only. The type of the backup config resource.  
`state` |  `enum (`[State](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#State)`)` Output only. The state of the backup config resource.  
`pitrSettings` |  `object (`[PitrSettings](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#PitrSettings)`)` Output only. Point in time recovery settings of the backup configuration resource.  
`latestSuccessfulBackupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of the latest successful backup created via this backup configuration.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`applicableResource` |  `string` Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource that is applicable for the backup configuration. Example: "//compute.googleapis.com/projects/{project}/zones/{zone}/instances/{instance}"  
`backupVault` |  `string` Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the backup vault that will store the backups generated through this backup configuration. Example: "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupVaults/{backupvaultId}"  
`backupLocations[]` |  `object (`[BackupLocation](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupLocation)`)` The locations where the backups are to be stored.  
Union field `plan_specific_config`. The plan specific config. This depends on the value of `[BackupConfigDetails.type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupConfigDetails.FIELDS.type)`. For type=BACKUPDR_BACKUP_PLAN, backup_dr_plan_config would be populated to capture information related to Google Cloud Backup and DR's Backup Plans. For type=BACKUPDR_TEMPLATE, backup_dr_template_config would be populated to capture information related to Google Cloud Backup and DR's Template details. `plan_specific_config` can be only one of the following:  
`backupDrPlanConfig` |  `object (`[BackupDrPlanConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupDrPlanConfig)`)` Google Cloud Backup and DR's Backup Plan specific data.  
`backupDrTemplateConfig` |  `object (`[BackupDrTemplateConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupDrTemplateConfig)`)` Google Cloud Backup and DR's Template specific data.  
  
## BackupDrPlanConfig

BackupDrPlanConfig has additional information about Google Cloud Backup and DR's Plan backup configuration.

JSON representation  
---  
      
    
    {
      "backupDrPlanRules": [
        {
          object ([BackupDrPlanRule](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupDrPlanRule))
        }
      ]
    }  
  
Fields  
---  
`backupDrPlanRules[]` |  `object (`[BackupDrPlanRule](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#BackupDrPlanRule)`)` Backup rules of the backup plan resource.  
  
## BackupDrPlanRule

BackupDrPlanRule has rule specific information of the backup plan resource.

JSON representation  
---  
      
    
    {
      "ruleId": string,
      "lastSuccessfulBackupTime": string
    }  
  
Fields  
---  
`ruleId` |  `string` Output only. Unique Id of the backup rule.  
`lastSuccessfulBackupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of the latest successful backup created via this backup rule.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## BackupDrTemplateConfig

Provides additional information about Google Cloud Backup and DR's Template backup configuration.

JSON representation  
---  
      
    
    {
      "firstPartyManagementUri": string,
      "thirdPartyManagementUri": string
    }  
  
Fields  
---  
`firstPartyManagementUri` |  `string` Output only. The URI of the BackupDr template resource for the first party identity users.  
`thirdPartyManagementUri` |  `string` Output only. The URI of the BackupDr template resource for the third party identity users.  
  
## Type

Type of the backup configuration. This enum may receive new values in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Backup config type is unspecified.  
`CLOUD_SQL_INSTANCE_BACKUP_CONFIG` | Backup config is Cloud SQL instance's automated backup config.  
`COMPUTE_ENGINE_RESOURCE_POLICY` | Backup config is Compute Engine Resource Policy.  
`BACKUPDR_BACKUP_PLAN` | Backup config is Google Cloud Backup and DR's Backup Plan.  
`BACKUPDR_TEMPLATE` | Backup config is Google Cloud Backup and DR's Template.  
  
## State

The state tells whether the backup config is active or not.

Enums  
---  
`STATE_UNSPECIFIED` | Backup config state not set.  
`ACTIVE` | The config is in an active state protecting the resource  
`INACTIVE` | The config is currently not protecting the resource. Either because it is disabled or the owning project has been deleted without cleanup of the actual resource.  
`ERROR` | The config still exists but because of some error state it is not protecting the resource. Like the source project is deleted. For eg. PlanAssociation, BackupPlan is deleted.  
  
## PitrSettings

Point in time recovery settings of the backup configuration resource.

JSON representation  
---  
      
    
    {
      "retentionDays": integer
    }  
  
Fields  
---  
`retentionDays` |  `integer` Output only. Number of days to retain the backup.  
  
## BackupLocation

BackupLocation represents a cloud location where a backup can be stored.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#Type_1)),
      "locationId": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#Type_1)`)` Output only. The type of the location.  
`locationId` |  `string` Output only. The id of the cloud location. Example: "us-central1"  
  
## Type

The type of the location.

Enums  
---  
`TYPE_UNSPECIFIED` | Location type is unspecified.  
`ZONAL` | Location type is zonal.  
`REGIONAL` | Location type is regional.  
`MULTI_REGIONAL` | Location type is multi regional.  
  
## Methods  
  
---  
  
### `[fetch](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs/fetch)`

|  Fetches ResourceBackupConfigs.  
  
### `[list](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs/list)`

|  Lists ResourceBackupConfigs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
