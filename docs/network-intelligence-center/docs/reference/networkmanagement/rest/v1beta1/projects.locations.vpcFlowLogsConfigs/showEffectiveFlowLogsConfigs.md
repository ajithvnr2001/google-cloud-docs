---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/showEffectiveFlowLogsConfigs/
title: Method: projects.locations.vpcFlowLogsConfigs.showEffectiveFlowLogsConfigs \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:40.713917+00:00
---

# Method: projects.locations.vpcFlowLogsConfigs.showEffectiveFlowLogsConfigs  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/showEffectiveFlowLogsConfigs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Method: projects.locations.vpcFlowLogsConfigs.showEffectiveFlowLogsConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * EffectiveVpcFlowLogsConfig
    * JSON representation
  * Scope
  * Try it!



vpcFlowLogsConfigs.showEffectiveFlowLogsConfigs returns a list of all VPC Flow Logs configurations applicable to a specified resource.

### HTTP request

`GET https://networkmanagement.googleapis.com/v1beta1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs:showEffectiveFlowLogsConfigs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the VpcFlowLogsConfig, specified in the following format: `projects/{projectId}/locations/global` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networkmanagement.vpcflowlogsconfigs.list`

  
  
### Query parameters

Parameters  
---  
`resource` |  `string` Required. The resource to get the effective VPC Flow Logs configuration for. The resource must belong to the same project as the parent. The resource must be a network, subnetwork, interconnect attachment, VPN tunnel, or a project.  
`pageSize` |  `integer` Optional. Number of `EffectiveVpcFlowLogsConfigs` to return. Default is 30.  
`pageToken` |  `string` Optional. Page token from an earlier query, as returned in `nextPageToken`.  
`filter` |  `string` Optional. Lists the `EffectiveVpcFlowLogsConfigs` that match the filter expression. A filter expression must use the supported [CEL logic operators](https://cloud.google.com/vpc/docs/about-flow-logs-records#supported_cel_logic_operators).  
  
### Request body

The request body must be empty.

### Response body

Response for the `vpcFlowLogsConfigs.showEffectiveFlowLogsConfigs` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "effectiveFlowLogsConfigs": [
        {
          object ([EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/showEffectiveFlowLogsConfigs#EffectiveVpcFlowLogsConfig))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`effectiveFlowLogsConfigs[]` |  `object (`[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/showEffectiveFlowLogsConfigs#EffectiveVpcFlowLogsConfig)`)` List of Effective Vpc Flow Logs configurations.  
`nextPageToken` |  `string` Page token to fetch the next set of configurations.  
`unreachable[]` |  `string` Locations that could not be reached (when querying all locations with `-`).  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## EffectiveVpcFlowLogsConfig

A configuration to generate a response for GetEffectiveVpcFlowLogsConfig request.

JSON representation  
---  
      
    
    {
      "name": string,
      "metadataFields": [
        string
      ],
      "state": enum ([State](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.State)),
      "aggregationInterval": enum ([AggregationInterval](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.AggregationInterval)),
      "flowSampling": number,
      "metadata": enum ([Metadata](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.Metadata)),
      "filterExpr": string,
      "crossProjectMetadata": enum ([CrossProjectMetadata](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.CrossProjectMetadata)),
    
      // Union field target_resource can be only one of the following:
      "network": string,
      "subnet": string,
      "interconnectAttachment": string,
      "vpnTunnel": string
      // End of list of possible types for union field target_resource.
      "scope": enum ([Scope](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/showEffectiveFlowLogsConfigs#Scope))
    }  
  
Fields  
---  
`name` |  `string` Unique name of the configuration. The name can have one of the following forms:

  * For project-level configurations: `projects/{projectId}/locations/global/vpcFlowLogsConfigs/{vpcFlowLogsConfigId}`
  * For organization-level configurations: `organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpcFlowLogsConfigId}`
  * For a Compute config, the name will be the path of the subnet: `projects/{projectId}/regions/{region}/subnetworks/{subnet_id}`

  
`metadataFields[]` |  `string` Custom metadata fields to include in the reported VPC flow logs. Can only be specified if "metadata" was set to CUSTOM_METADATA.  
`state` |  `enum (`[State](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.State)`)` The state of the VPC Flow Log configuration. Default value is ENABLED. When creating a new configuration, it must be enabled. Setting state=DISABLED will pause the log generation for this config.  
`aggregationInterval` |  `enum (`[AggregationInterval](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.AggregationInterval)`)` The aggregation interval for the logs. Default value is INTERVAL_5_SEC.  
`flowSampling` |  `number` The value of the field must be in (0, 1]. The sampling rate of VPC Flow Logs where 1.0 means all collected logs are reported. Setting the sampling rate to 0.0 is not allowed. If you want to disable VPC Flow Logs, use the state field instead. Default value is 1.0.  
`metadata` |  `enum (`[Metadata](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.Metadata)`)` Configures whether all, none or a subset of metadata fields should be added to the reported VPC flow logs. Default value is INCLUDE_ALL_METADATA.  
`filterExpr` |  `string` Export filter used to define which VPC Flow Logs should be logged.  
`crossProjectMetadata` |  `enum (`[CrossProjectMetadata](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig.CrossProjectMetadata)`)` Determines whether to include cross project annotations in the logs. This field is available only for organization configurations. If not specified in org configs will be set to CROSS_PROJECT_METADATA_ENABLED.  
Union field `target_resource`. Reference to the resource of the config scope. That is, the scope from which traffic is logged. The target resource must belong to the same project as the configuration. This field is not supported for organization level configurations. `target_resource` can be only one of the following:  
`network` |  `string` Traffic will be logged from VMs, VPN tunnels and Interconnect Attachments within the network. Format: projects/{projectId}/global/networks/{name}  
`subnet` |  `string` Traffic will be logged from VMs within the subnetwork. Format: projects/{projectId}/regions/{region}/subnetworks/{name}  
`interconnectAttachment` |  `string` Traffic will be logged from the Interconnect Attachment. Format: projects/{projectId}/regions/{region}/interconnectAttachments/{name}  
`vpnTunnel` |  `string` Traffic will be logged from the VPN Tunnel. Format: projects/{projectId}/regions/{region}/vpnTunnels/{name}  
`scope` |  `enum (`[Scope](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.vpcFlowLogsConfigs/showEffectiveFlowLogsConfigs#Scope)`)` Specifies the scope of the config (e.g., SUBNET, NETWORK, ORGANIZATION..).  
  
## Scope

The scope for this flow log configuration.

Enums  
---  
`SCOPE_UNSPECIFIED` | Scope is unspecified.  
`SUBNET` | Target resource is a subnet (Network Management API).  
`COMPUTE_API_SUBNET` | Target resource is a subnet, and the config originates from the Compute API.  
`NETWORK` | Target resource is a network.  
`VPN_TUNNEL` | Target resource is a VPN tunnel.  
`INTERCONNECT_ATTACHMENT` | Target resource is an interconnect attachment.  
`ORGANIZATION` | Configuration applies to an entire organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-01 UTC."],[],[]] 
