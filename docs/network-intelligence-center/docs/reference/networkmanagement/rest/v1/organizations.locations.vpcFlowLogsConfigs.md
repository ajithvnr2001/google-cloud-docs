---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs
title: REST Resource: organizations.locations.vpcFlowLogsConfigs \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:24.131988+00:00
---

# REST Resource: organizations.locations.vpcFlowLogsConfigs  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  REST Resource: organizations.locations.vpcFlowLogsConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: VpcFlowLogsConfig
    * JSON representation
    * State
    * AggregationInterval
    * Metadata
    * CrossProjectMetadata
    * TargetResourceState
  * Methods



## Resource: VpcFlowLogsConfig

A configuration to generate VPC Flow Logs.

JSON representation  
---  
      
    
    {
      "name": string,
      "metadataFields": [
        string
      ],
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.State)),
      "aggregationInterval": enum ([AggregationInterval](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.AggregationInterval)),
      "flowSampling": number,
      "metadata": enum ([Metadata](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.Metadata)),
      "filterExpr": string,
      "crossProjectMetadata": enum ([CrossProjectMetadata](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.CrossProjectMetadata)),
      "targetResourceState": enum ([TargetResourceState](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.TargetResourceState)),
    
      // Union field target_resource can be only one of the following:
      "network": string,
      "subnet": string,
      "interconnectAttachment": string,
      "vpnTunnel": string
      // End of list of possible types for union field target_resource.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique name of the configuration. The name can have one of the following forms:

  * For project-level configurations: `projects/{projectId}/locations/global/vpcFlowLogsConfigs/{vpcFlowLogsConfigId}`
  * For organization-level configurations: `organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpcFlowLogsConfigId}`

  
`metadataFields[]` |  `string` Optional. Custom metadata fields to include in the reported VPC flow logs. Can only be specified if "metadata" was set to CUSTOM_METADATA.  
`labels` |  `map (key: string, value: string)` Optional. Resource labels to represent user-provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the config was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the config was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Optional. The user-supplied description of the VPC Flow Logs configuration. Maximum of 512 characters.  
`state` |  `enum (`[State](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.State)`)` Optional. The state of the VPC Flow Log configuration. Default value is ENABLED. When creating a new configuration, it must be enabled. Setting state=DISABLED will pause the log generation for this config.  
`aggregationInterval` |  `enum (`[AggregationInterval](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.AggregationInterval)`)` Optional. The aggregation interval for the logs. Default value is INTERVAL_5_SEC.  
`flowSampling` |  `number` Optional. The value of the field must be in (0, 1]. The sampling rate of VPC Flow Logs where 1.0 means all collected logs are reported. Setting the sampling rate to 0.0 is not allowed. If you want to disable VPC Flow Logs, use the state field instead. Default value is 1.0.  
`metadata` |  `enum (`[Metadata](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.Metadata)`)` Optional. Configures whether all, none or a subset of metadata fields should be added to the reported VPC flow logs. Default value is INCLUDE_ALL_METADATA.  
`filterExpr` |  `string` Optional. Export filter used to define which VPC Flow Logs should be logged.  
`crossProjectMetadata` |  `enum (`[CrossProjectMetadata](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.CrossProjectMetadata)`)` Optional. Determines whether to include cross project annotations in the logs. This field is available only for organization configurations. If not specified in org configs will be set to CROSS_PROJECT_METADATA_ENABLED.  
`targetResourceState` |  `enum (`[TargetResourceState](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.TargetResourceState)`)` Output only. Describes the state of the configured target resource for diagnostic purposes.  
Union field `target_resource`. Reference to the resource of the config scope. That is, the scope from which traffic is logged. The target resource must belong to the same project as the configuration. This field is not supported for organization level configurations. `target_resource` can be only one of the following:  
`network` |  `string` Traffic will be logged from VMs, VPN tunnels and Interconnect Attachments within the network. Format: projects/{projectId}/global/networks/{name}  
`subnet` |  `string` Traffic will be logged from VMs within the subnetwork. Format: projects/{projectId}/regions/{region}/subnetworks/{name}  
`interconnectAttachment` |  `string` Traffic will be logged from the Interconnect Attachment. Format: projects/{projectId}/regions/{region}/interconnectAttachments/{name}  
`vpnTunnel` |  `string` Traffic will be logged from the VPN Tunnel. Format: projects/{projectId}/regions/{region}/vpnTunnels/{name}  
  
### State

Determines whether this configuration will be generating logs.

Enums  
---  
`STATE_UNSPECIFIED` | If not specified, will default to ENABLED.  
`ENABLED` | When ENABLED, this configuration will generate logs.  
`DISABLED` | When DISABLED, this configuration will not generate logs.  
  
### AggregationInterval

Toggles the aggregation interval for collecting flow logs by 5-tuple.

Enums  
---  
`AGGREGATION_INTERVAL_UNSPECIFIED` | If not specified, will default to INTERVAL_5_SEC.  
`INTERVAL_5_SEC` | Aggregate logs in 5s intervals.  
`INTERVAL_30_SEC` | Aggregate logs in 30s intervals.  
`INTERVAL_1_MIN` | Aggregate logs in 1m intervals.  
`INTERVAL_5_MIN` | Aggregate logs in 5m intervals.  
`INTERVAL_10_MIN` | Aggregate logs in 10m intervals.  
`INTERVAL_15_MIN` | Aggregate logs in 15m intervals.  
  
### Metadata

Configures which log fields would be included.

Enums  
---  
`METADATA_UNSPECIFIED` | If not specified, will default to INCLUDE_ALL_METADATA.  
`INCLUDE_ALL_METADATA` | Include all metadata fields.  
`EXCLUDE_ALL_METADATA` | Exclude all metadata fields.  
`CUSTOM_METADATA` | Include only custom fields (specified in metadataFields).  
  
### CrossProjectMetadata

Determines whether to include cross project annotations in the logs. Project configurations will always have CROSS_PROJECT_METADATA_DISABLED.

Enums  
---  
`CROSS_PROJECT_METADATA_UNSPECIFIED` | If not specified, the default is CROSS_PROJECT_METADATA_ENABLED.  
`CROSS_PROJECT_METADATA_ENABLED` | When CROSS_PROJECT_METADATA_ENABLED, metadata from other projects will be included in the logs.  
`CROSS_PROJECT_METADATA_DISABLED` | When CROSS_PROJECT_METADATA_DISABLED, metadata from other projects will not be included in the logs.  
  
### TargetResourceState

Output only. Indicates whether the target resource exists, for diagnostic purposes.

Enums  
---  
`TARGET_RESOURCE_STATE_UNSPECIFIED` | Unspecified target resource state.  
`TARGET_RESOURCE_EXISTS` | Indicates that the target resource exists.  
`TARGET_RESOURCE_DOES_NOT_EXIST` | Indicates that the target resource does not exist.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs/create)`

|  Creates a new `VpcFlowLogsConfig`.  
  
### `[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs/delete)`

|  Deletes a specific `VpcFlowLogsConfig`.  
  
### `[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs/get)`

|  Gets the details of a specific `VpcFlowLogsConfig`.  
  
### `[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs/list)`

|  Lists all `VpcFlowLogsConfigs` in a given organization.  
  
### `[patch](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs/patch)`

|  Updates an existing `VpcFlowLogsConfig`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-01 UTC."],[],[]] 
