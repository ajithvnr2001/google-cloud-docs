---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig
title: Network Management v1 API - Class EffectiveVpcFlowLogsConfig (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:05.309757+00:00
---

# Network Management v1 API - Class EffectiveVpcFlowLogsConfig (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Management v1 API - Class EffectiveVpcFlowLogsConfig (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.1.0  1.0.0 
    
    
    public sealed class EffectiveVpcFlowLogsConfig : IMessage<EffectiveVpcFlowLogsConfig>, IEquatable<EffectiveVpcFlowLogsConfig>, IDeepCloneable<EffectiveVpcFlowLogsConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Management v1 API class EffectiveVpcFlowLogsConfig.

A configuration to generate a response for GetEffectiveVpcFlowLogsConfig request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EffectiveVpcFlowLogsConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1)

## Assembly

Google.Cloud.NetworkManagement.V1.dll

## Constructors 

### EffectiveVpcFlowLogsConfig()
    
    
    public EffectiveVpcFlowLogsConfig()

### EffectiveVpcFlowLogsConfig(EffectiveVpcFlowLogsConfig)
    
    
    public EffectiveVpcFlowLogsConfig(EffectiveVpcFlowLogsConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig)`  
  
  
## Properties 

### AggregationInterval
    
    
    public VpcFlowLogsConfig.Types.AggregationInterval AggregationInterval { get; set; }

The aggregation interval for the logs. Default value is INTERVAL_5_SEC.

**Property Value**  
---  
**Type** | **Description**  
`[VpcFlowLogsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig.Types)[AggregationInterval](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig.Types.AggregationInterval)` |   
  
### CrossProjectMetadata
    
    
    public VpcFlowLogsConfig.Types.CrossProjectMetadata CrossProjectMetadata { get; set; }

Determines whether to include cross project annotations in the logs. This field is available only for organization configurations. If not specified in org configs will be set to CROSS_PROJECT_METADATA_ENABLED.

**Property Value**  
---  
**Type** | **Description**  
`[VpcFlowLogsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig.Types)[CrossProjectMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig.Types.CrossProjectMetadata)` |   
  
### FilterExpr
    
    
    public string FilterExpr { get; set; }

Export filter used to define which VPC Flow Logs should be logged.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FlowSampling
    
    
    public float FlowSampling { get; set; }

The value of the field must be in (0, 1]. The sampling rate of VPC Flow Logs where 1.0 means all collected logs are reported. Setting the sampling rate to 0.0 is not allowed. If you want to disable VPC Flow Logs, use the state field instead. Default value is 1.0.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### HasAggregationInterval
    
    
    public bool HasAggregationInterval { get; }

Gets whether the "aggregation_interval" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCrossProjectMetadata
    
    
    public bool HasCrossProjectMetadata { get; }

Gets whether the "cross_project_metadata" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasFilterExpr
    
    
    public bool HasFilterExpr { get; }

Gets whether the "filter_expr" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasFlowSampling
    
    
    public bool HasFlowSampling { get; }

Gets whether the "flow_sampling" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasInterconnectAttachment
    
    
    public bool HasInterconnectAttachment { get; }

Gets whether the "interconnect_attachment" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMetadata
    
    
    public bool HasMetadata { get; }

Gets whether the "metadata" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasNetwork
    
    
    public bool HasNetwork { get; }

Gets whether the "network" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasScope
    
    
    public bool HasScope { get; }

Gets whether the "scope" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasState
    
    
    public bool HasState { get; }

Gets whether the "state" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSubnet
    
    
    public bool HasSubnet { get; }

Gets whether the "subnet" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasVpnTunnel
    
    
    public bool HasVpnTunnel { get; }

Gets whether the "vpn_tunnel" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InterconnectAttachment
    
    
    public string InterconnectAttachment { get; set; }

Traffic will be logged from the Interconnect Attachment. Format: projects/{project_id}/regions/{region}/interconnectAttachments/{name}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Metadata
    
    
    public VpcFlowLogsConfig.Types.Metadata Metadata { get; set; }

Configures whether all, none or a subset of metadata fields should be added to the reported VPC flow logs. Default value is INCLUDE_ALL_METADATA.

**Property Value**  
---  
**Type** | **Description**  
`[VpcFlowLogsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig.Types)[Metadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig.Types.Metadata)` |   
  
### MetadataFields
    
    
    public RepeatedField<string> MetadataFields { get; }

Custom metadata fields to include in the reported VPC flow logs. Can only be specified if "metadata" was set to CUSTOM_METADATA.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Unique name of the configuration. The name can have one of the following forms:

  * For project-level configurations: `projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}`

  * For organization-level configurations: `organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}`

  * For a Compute config, the name will be the path of the subnet: `projects/{project_id}/regions/{region}/subnetworks/{subnet_id}`




**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Network
    
    
    public string Network { get; set; }

Traffic will be logged from VMs, VPN tunnels and Interconnect Attachments within the network. Format: projects/{project_id}/global/networks/{name}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Scope
    
    
    public EffectiveVpcFlowLogsConfig.Types.Scope Scope { get; set; }

Specifies the scope of the config (e.g., SUBNET, NETWORK, ORGANIZATION..).

**Property Value**  
---  
**Type** | **Description**  
`[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig.Types)[Scope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig.Types.Scope)` |   
  
### State
    
    
    public VpcFlowLogsConfig.Types.State State { get; set; }

The state of the VPC Flow Log configuration. Default value is ENABLED. When creating a new configuration, it must be enabled. Setting state=DISABLED will pause the log generation for this config.

**Property Value**  
---  
**Type** | **Description**  
`[VpcFlowLogsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.VpcFlowLogsConfig.Types.State)` |   
  
### Subnet
    
    
    public string Subnet { get; set; }

Traffic will be logged from VMs within the subnetwork. Format: projects/{project_id}/regions/{region}/subnetworks/{name}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TargetResourceCase
    
    
    public EffectiveVpcFlowLogsConfig.TargetResourceOneofCase TargetResourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig)[TargetResourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.EffectiveVpcFlowLogsConfig.TargetResourceOneofCase)` |   
  
### VpnTunnel
    
    
    public string VpnTunnel { get; set; }

Traffic will be logged from the VPN Tunnel. Format: projects/{project_id}/regions/{region}/vpnTunnels/{name}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
