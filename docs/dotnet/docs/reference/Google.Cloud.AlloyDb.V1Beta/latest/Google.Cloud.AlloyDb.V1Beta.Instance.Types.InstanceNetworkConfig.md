---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceNetworkConfig
title: AlloyDB v1beta API - Class Instance.Types.InstanceNetworkConfig (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:08.980569+00:00
---

# AlloyDB v1beta API - Class Instance.Types.InstanceNetworkConfig (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceNetworkConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class Instance.Types.InstanceNetworkConfig (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class Instance.Types.InstanceNetworkConfig : IMessage<Instance.Types.InstanceNetworkConfig>, IEquatable<Instance.Types.InstanceNetworkConfig>, IDeepCloneable<Instance.Types.InstanceNetworkConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class Instance.Types.InstanceNetworkConfig.

Metadata related to instance-level network configuration.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Instance.Types.InstanceNetworkConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types)[InstanceNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceNetworkConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types)[InstanceNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceNetworkConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types)[InstanceNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceNetworkConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### InstanceNetworkConfig()
    
    
    public InstanceNetworkConfig()

### InstanceNetworkConfig(InstanceNetworkConfig)
    
    
    public InstanceNetworkConfig(Instance.Types.InstanceNetworkConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types)[InstanceNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceNetworkConfig)`  
  
  
## Properties 

### AllocatedIpRangeOverride
    
    
    public string AllocatedIpRangeOverride { get; set; }

Optional. Name of the allocated IP range for the private IP AlloyDB instance, for example: "google-managed-services-default". If set, the instance IPs will be created from this allocated range and will override the IP range used by the parent cluster. The range name must comply with [RFC 1035](http://datatracker.ietf.org/doc/html/rfc1035). Specifically, the name must be 1-63 characters long and match the regular expression [a-z](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/\[-a-z0-9\]*\[a-z0-9\])?.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AuthorizedExternalNetworks
    
    
    public RepeatedField<Instance.Types.InstanceNetworkConfig.Types.AuthorizedNetwork> AuthorizedExternalNetworks { get; }

Optional. A list of external network authorized to access this instance.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types)[InstanceNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceNetworkConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceNetworkConfig.Types)[AuthorizedNetwork](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceNetworkConfig.Types.AuthorizedNetwork)` |   
  
### EnableOutboundPublicIp
    
    
    public bool EnableOutboundPublicIp { get; set; }

Optional. Enabling an outbound public IP address to support a database server sending requests out into the internet.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnablePublicIp
    
    
    public bool EnablePublicIp { get; set; }

Optional. Enabling public ip for the instance.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Network
    
    
    public string Network { get; set; }

Output only. The resource link for the VPC network in which instance resources are created and from which they are accessible via Private IP. This will be the same value as the parent cluster's network. It is specified in the form: // `projects/{project_number}/global/networks/{network_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkAsNetworkName
    
    
    public NetworkName NetworkAsNetworkName { get; set; }

[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.NetworkName)-typed view over the [Network](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance.Types.InstanceNetworkConfig#Google_Cloud_AlloyDb_V1Beta_Instance_Types_InstanceNetworkConfig_Network) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.NetworkName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
