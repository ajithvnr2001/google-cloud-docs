---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ExistingNetworkConfig
title: Cluster Director v1 API - Class ExistingNetworkConfig (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:33.388774+00:00
---

# Cluster Director v1 API - Class ExistingNetworkConfig (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ExistingNetworkConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cluster Director v1 API - Class ExistingNetworkConfig (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class ExistingNetworkConfig : IMessage<ExistingNetworkConfig>, IEquatable<ExistingNetworkConfig>, IDeepCloneable<ExistingNetworkConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Cluster Director v1 API class ExistingNetworkConfig.

When set in a [NetworkResourceConfig][google.cloud.hypercomputecluster.v1.NetworkResourceConfig], indicates that an existing network should be imported.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExistingNetworkConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ExistingNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ExistingNetworkConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ExistingNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ExistingNetworkConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ExistingNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ExistingNetworkConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.HypercomputeCluster.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1)

## Assembly

Google.Cloud.HypercomputeCluster.V1.dll

## Constructors 

### ExistingNetworkConfig()
    
    
    public ExistingNetworkConfig()

### ExistingNetworkConfig(ExistingNetworkConfig)
    
    
    public ExistingNetworkConfig(ExistingNetworkConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ExistingNetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ExistingNetworkConfig)`  
  
  
## Properties 

### Network
    
    
    public string Network { get; set; }

Required. Immutable. Name of the network to import, in the format `projects/{project}/global/networks/{network}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkAsNetworkName
    
    
    public NetworkName NetworkAsNetworkName { get; set; }

[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.NetworkName)-typed view over the [Network](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ExistingNetworkConfig#Google_Cloud_HypercomputeCluster_V1_ExistingNetworkConfig_Network) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.NetworkName)` |   
  
### Subnetwork
    
    
    public string Subnetwork { get; set; }

Required. Immutable. Particular subnetwork to use, in the format `projects/{project}/regions/{region}/subnetworks/{subnetwork}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SubnetworkAsSubnetworkName
    
    
    public SubnetworkName SubnetworkAsSubnetworkName { get; set; }

[SubnetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.SubnetworkName)-typed view over the [Subnetwork](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.ExistingNetworkConfig#Google_Cloud_HypercomputeCluster_V1_ExistingNetworkConfig_Subnetwork) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SubnetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Google.Cloud.HypercomputeCluster.V1.SubnetworkName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
