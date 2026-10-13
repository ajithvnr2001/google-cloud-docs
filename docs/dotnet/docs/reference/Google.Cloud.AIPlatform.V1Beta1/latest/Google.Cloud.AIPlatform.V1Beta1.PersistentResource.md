---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource
title: Vertex AI v1beta1 API - Class PersistentResource (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:22.425424+00:00
---

# Vertex AI v1beta1 API - Class PersistentResource (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class PersistentResource (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class PersistentResource : IMessage<PersistentResource>, IEquatable<PersistentResource>, IDeepCloneable<PersistentResource>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class PersistentResource.

Represents long-lasting resources that are dedicated to users to runs custom workloads. A PersistentResource can have multiple node pools and each node pool can have its own machine spec.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PersistentResource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PersistentResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PersistentResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PersistentResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### PersistentResource()
    
    
    public PersistentResource()

### PersistentResource(PersistentResource)
    
    
    public PersistentResource(PersistentResource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PersistentResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Time when the PersistentResource was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Optional. The display name of the PersistentResource. The name can be up to 128 characters long and can consist of any UTF-8 characters.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EncryptionSpec
    
    
    public EncryptionSpec EncryptionSpec { get; set; }

Optional. Customer-managed encryption key spec for a PersistentResource. If set, this PersistentResource and all sub-resources of this PersistentResource will be secured by this key.

**Property Value**  
---  
**Type** | **Description**  
`[EncryptionSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EncryptionSpec)` |   
  
### Error
    
    
    public Status Error { get; set; }

Output only. Only populated when persistent resource's state is `STOPPING` or `ERROR`.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. The labels with user-defined metadata to organize PersistentResource.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Immutable. Resource name of a PersistentResource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Network
    
    
    public string Network { get; set; }

Optional. The full name of the Compute Engine [network](https://docs.cloud.google.com/compute/docs/networks-and-firewalls#networks) to peered with Vertex AI to host the persistent resources. For example, `projects/12345/global/networks/myVPC`. [Format](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert) is of the form `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in `12345`, and {network} is a network name.

To specify this field, you must have already [configured VPC Network Peering for Vertex AI](https://cloud.google.com/vertex-ai/docs/general/vpc-peering).

If this field is left unspecified, the resources aren't peered with any network.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkAsNetworkName
    
    
    public NetworkName NetworkAsNetworkName { get; set; }

[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NetworkName)-typed view over the [Network](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource#Google_Cloud_AIPlatform_V1Beta1_PersistentResource_Network) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NetworkName)` |   
  
### PersistentResourceName
    
    
    public PersistentResourceName PersistentResourceName { get; set; }

[PersistentResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResourceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource#Google_Cloud_AIPlatform_V1Beta1_PersistentResource_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PersistentResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResourceName)` |   
  
### PscInterfaceConfig
    
    
    public PscInterfaceConfig PscInterfaceConfig { get; set; }

Optional. Configuration for PSC-I for PersistentResource.

**Property Value**  
---  
**Type** | **Description**  
`[PscInterfaceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PscInterfaceConfig)` |   
  
### ReservedIpRanges
    
    
    public RepeatedField<string> ReservedIpRanges { get; }

Optional. A list of names for the reserved IP ranges under the VPC network that can be used for this persistent resource.

If set, we will deploy the persistent resource within the provided IP ranges. Otherwise, the persistent resource is deployed to any IP ranges under the provided VPC network.

Example: ['vertex-ai-ip-range'].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourcePools
    
    
    public RepeatedField<ResourcePool> ResourcePools { get; }

Required. The spec of the pools of different resources.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ResourcePool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ResourcePool)` |   
  
### ResourceRuntime
    
    
    public ResourceRuntime ResourceRuntime { get; set; }

Output only. Runtime information of the Persistent Resource.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceRuntime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ResourceRuntime)` |   
  
### ResourceRuntimeSpec
    
    
    public ResourceRuntimeSpec ResourceRuntimeSpec { get; set; }

Optional. Persistent Resource runtime spec. For example, used for Ray cluster configuration.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceRuntimeSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ResourceRuntimeSpec)` |   
  
### SatisfiesPzi
    
    
    public bool SatisfiesPzi { get; set; }

Output only. Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SatisfiesPzs
    
    
    public bool SatisfiesPzs { get; set; }

Output only. Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

Output only. Time when the PersistentResource for the first time entered the `RUNNING` state.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### State
    
    
    public PersistentResource.Types.State State { get; set; }

Output only. The detailed state of a Study.

**Property Value**  
---  
**Type** | **Description**  
`[PersistentResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResource.Types.State)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Time when the PersistentResource was most recently updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
