---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs/
title: MCP Tools Reference: backupdr.googleapis.com \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:47.002035+00:00
---

# MCP Tools Reference: backupdr.googleapis.com  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Reference ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference)



Send feedback 

#  MCP Tools Reference: backupdr.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `ListResourceBackupConfigs`

Retrieves backup configuration summaries and protection status for resources with in the specified project and location. CRITICAL: Location is mandatory and must be sent in the request. Location must not be '-' or 'global'. Do NOT attempt to use other tools (like ListBackupVaults,ListBackupPlans,ListBackupPlanAssociations) to discover active locations. You MUST explicitly ask the user for the location and project before calling this tool.

The following sample demonstrate how to use `curl` to invoke the `ListResourceBackupConfigs` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://backupdr.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "ListResourceBackupConfigs",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for ListResourceBackupConfigs.

### ListResourceBackupConfigsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string,
      "orderBy": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The project and location for which to retrieve resource backup configs. Format: 'projects/{project_id}/locations/{location}'. In Google Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**.  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will use 100 as default. Maximum value is 500 and values above 500 will be coerced to 500.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results.  
`orderBy` |  `string` Optional. Hint for how to order the results.  
  
## Output Schema

Response for ListResourceBackupConfigs.

### ListResourceBackupConfigsResponse

JSON representation  
---  
      
    
    {
      "resourceBackupConfigs": [
        {
          object ([ResourceBackupConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.ResourceBackupConfig))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`resourceBackupConfigs[]` |  `object (`[ResourceBackupConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.ResourceBackupConfig)`)` The list of ResourceBackupConfigs for the specified scope.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### ResourceBackupConfig

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "targetResource": string,
      "targetResourceDisplayName": string,
      "targetResourceType": enum ([ResourceType](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.ResourceType)),
      "targetResourceLabels": {
        string: string,
        ...
      },
      "backupConfigsDetails": [
        {
          object ([BackupConfigDetails](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.BackupConfigDetails))
        }
      ],
      "backupConfigured": boolean,
      "vaulted": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the ResourceBackupConfig. Format: projects/{project}/locations/{location}/resourceBackupConfigs/{uid}  
`uid` |  `string` Output only. The unique identifier of the resource backup config.  
`targetResource` |  `string` Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the cloud resource that this configuration applies to. Supported resource types are `[ResourceBackupConfig.ResourceType](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.ResourceType)`.  
`targetResourceDisplayName` |  `string` Output only. The human friendly name of the target resource.  
`targetResourceType` |  `enum (`[ResourceType](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.ResourceType)`)` Output only. The type of the target resource.  
`targetResourceLabels` |  `map (key: string, value: string)` Labels associated with the target resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`backupConfigsDetails[]` |  `object (`[BackupConfigDetails](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.BackupConfigDetails)`)` Backup configurations applying to the target resource, including those targeting its related/child resources. For example, backup configuration applicable to Compute Engine disks will be populated in this field for a Compute Engine VM which has the disk associated.  
`backupConfigured` |  `boolean` Output only. Whether the target resource is configured for backup. This is true if the backup_configs_details is not empty.  
`vaulted` |  `boolean` Output only. Whether the target resource is protected by a backup vault. This is true if the backup_configs_details is not empty and any of the `ResourceBackupConfig.backup_configs_details` has a backup configuration with `BackupConfigDetails.backup_vault` set.  
  
### TargetResourceLabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### BackupConfigDetails

JSON representation  
---  
      
    
    {
      "backupConfigSource": string,
      "backupConfigSourceDisplayName": string,
      "type": enum ([Type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.Type)),
      "state": enum ([State](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.State)),
      "pitrSettings": {
        object ([PitrSettings](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.PitrSettings))
      },
      "latestSuccessfulBackupTime": string,
      "applicableResource": string,
      "backupVault": string,
      "backupLocations": [
        {
          object ([BackupLocation](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.BackupLocation))
        }
      ],
    
      // Union field plan_specific_config can be only one of the following:
      "backupDrPlanConfig": {
        object ([BackupDrPlanConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.BackupDrPlanConfig))
      },
      "backupDrTemplateConfig": {
        object ([BackupDrTemplateConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.BackupDrTemplateConfig))
      }
      // End of list of possible types for union field plan_specific_config.
    }  
  
Fields  
---  
`backupConfigSource` |  `string` Output only. The full resource name of the backup config source resource. For example, "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPlans/{backupplanId}" or "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolicies/{resourcePolicyId}".  
`backupConfigSourceDisplayName` |  `string` Output only. The display name of the backup config source resource.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.Type)`)` Output only. The type of the backup config resource.  
`state` |  `enum (`[State](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.State)`)` Output only. The state of the backup config resource.  
`pitrSettings` |  `object (`[PitrSettings](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.PitrSettings)`)` Output only. Point in time recovery settings of the backup configuration resource.  
`latestSuccessfulBackupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of the latest successful backup created via this backup configuration.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`applicableResource` |  `string` Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource that is applicable for the backup configuration. Example: "//compute.googleapis.com/projects/{project}/zones/{zone}/instances/{instance}"  
`backupVault` |  `string` Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the backup vault that will store the backups generated through this backup configuration. Example: "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupVaults/{backupvaultId}"  
`backupLocations[]` |  `object (`[BackupLocation](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.BackupLocation)`)` The locations where the backups are to be stored.  
Union field `plan_specific_config`. The plan specific config. This depends on the value of `BackupConfigDetails.type`. For type=BACKUPDR_BACKUP_PLAN, backup_dr_plan_config would be populated to capture information related to Google Cloud Backup and DR's Backup Plans. For type=BACKUPDR_TEMPLATE, backup_dr_template_config would be populated to capture information related to Google Cloud Backup and DR's Template details. `plan_specific_config` can be only one of the following:  
`backupDrPlanConfig` |  `object (`[BackupDrPlanConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.BackupDrPlanConfig)`)` Google Cloud Backup and DR's Backup Plan specific data.  
`backupDrTemplateConfig` |  `object (`[BackupDrTemplateConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.BackupDrTemplateConfig)`)` Google Cloud Backup and DR's Template specific data.  
  
### PitrSettings

JSON representation  
---  
      
    
    {
      "retentionDays": integer
    }  
  
Fields  
---  
`retentionDays` |  `integer` Output only. Number of days to retain the backup.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### BackupLocation

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.Type_1)),
      "locationId": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.Type_1)`)` Output only. The type of the location.  
`locationId` |  `string` Output only. The id of the cloud location. Example: "us-central1"  
  
### BackupDrPlanConfig

JSON representation  
---  
      
    
    {
      "backupDrPlanRules": [
        {
          object ([BackupDrPlanRule](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.BackupDrPlanRule))
        }
      ]
    }  
  
Fields  
---  
`backupDrPlanRules[]` |  `object (`[BackupDrPlanRule](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListResourceBackupConfigs#Output.Schema.BackupDrPlanRule)`)` Backup rules of the backup plan resource.  
  
### BackupDrPlanRule

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
  
### BackupDrTemplateConfig

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
  
### ResourceType

The type of the cloud resource.

Enums  
---  
`RESOURCE_TYPE_UNSPECIFIED` | Resource type not set.  
`CLOUD_SQL_INSTANCE` | Cloud SQL instance.  
`COMPUTE_ENGINE_VM` | Compute Engine VM.  
`COMPUTE_ENGINE_DISK` | Compute Engine Disk.  
`COMPUTE_ENGINE_REGIONAL_DISK` | Compute Engine Regional Disk.  
`FILESTORE_INSTANCE` | Filestore Instance.  
  
### Type

Type of the backup configuration. This enum may receive new values in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Backup config type is unspecified.  
`CLOUD_SQL_INSTANCE_BACKUP_CONFIG` | Backup config is Cloud SQL instance's automated backup config.  
`COMPUTE_ENGINE_RESOURCE_POLICY` | Backup config is Compute Engine Resource Policy.  
`BACKUPDR_BACKUP_PLAN` | Backup config is Google Cloud Backup and DR's Backup Plan.  
`BACKUPDR_TEMPLATE` | Backup config is Google Cloud Backup and DR's Template.  
  
### State

The state tells whether the backup config is active or not.

Enums  
---  
`STATE_UNSPECIFIED` | Backup config state not set.  
`ACTIVE` | The config is in an active state protecting the resource  
`INACTIVE` | The config is currently not protecting the resource. Either because it is disabled or the owning project has been deleted without cleanup of the actual resource.  
`ERROR` | The config still exists but because of some error state it is not protecting the resource. Like the source project is deleted. For eg. PlanAssociation, BackupPlan is deleted.  
  
### Type

The type of the location.

Enums  
---  
`TYPE_UNSPECIFIED` | Location type is unspecified.  
`ZONAL` | Location type is zonal.  
`REGIONAL` | Location type is regional.  
`MULTI_REGIONAL` | Location type is multi regional.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
