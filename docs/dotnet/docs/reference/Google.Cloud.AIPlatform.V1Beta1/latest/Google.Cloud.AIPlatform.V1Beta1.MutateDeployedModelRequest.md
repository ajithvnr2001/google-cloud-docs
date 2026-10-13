---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MutateDeployedModelRequest
title: Vertex AI v1beta1 API - Class MutateDeployedModelRequest (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:00.456453+00:00
---

# Vertex AI v1beta1 API - Class MutateDeployedModelRequest (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MutateDeployedModelRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class MutateDeployedModelRequest (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class MutateDeployedModelRequest : IMessage<MutateDeployedModelRequest>, IEquatable<MutateDeployedModelRequest>, IDeepCloneable<MutateDeployedModelRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class MutateDeployedModelRequest.

Request message for [EndpointService.MutateDeployedModel][google.cloud.aiplatform.v1beta1.EndpointService.MutateDeployedModel].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MutateDeployedModelRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MutateDeployedModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MutateDeployedModelRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MutateDeployedModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MutateDeployedModelRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MutateDeployedModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MutateDeployedModelRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### MutateDeployedModelRequest()
    
    
    public MutateDeployedModelRequest()

### MutateDeployedModelRequest(MutateDeployedModelRequest)
    
    
    public MutateDeployedModelRequest(MutateDeployedModelRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MutateDeployedModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MutateDeployedModelRequest)`  
  
  
## Properties 

### DeployedModel
    
    
    public DeployedModel DeployedModel { get; set; }

Required. The DeployedModel to be mutated within the Endpoint. Only the following fields can be mutated:

  * `min_replica_count` in either [DedicatedResources][google.cloud.aiplatform.v1beta1.DedicatedResources] or [AutomaticResources][google.cloud.aiplatform.v1beta1.AutomaticResources]
  * `max_replica_count` in either [DedicatedResources][google.cloud.aiplatform.v1beta1.DedicatedResources] or [AutomaticResources][google.cloud.aiplatform.v1beta1.AutomaticResources]
  * `required_replica_count` in [DedicatedResources][google.cloud.aiplatform.v1beta1.DedicatedResources]
  * [autoscaling_metric_specs][google.cloud.aiplatform.v1beta1.DedicatedResources.autoscaling_metric_specs]
  * `disable_container_logging` (v1 only)
  * `enable_container_logging` (v1beta1 only)



**Property Value**  
---  
**Type** | **Description**  
`[DeployedModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployedModel)` |   
  
### Endpoint
    
    
    public string Endpoint { get; set; }

Required. The name of the Endpoint resource into which to mutate a DeployedModel. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EndpointAsEndpointName
    
    
    public EndpointName EndpointAsEndpointName { get; set; }

[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EndpointName)-typed view over the [Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MutateDeployedModelRequest#Google_Cloud_AIPlatform_V1Beta1_MutateDeployedModelRequest_Endpoint) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EndpointName)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. The update mask applies to the resource. See [google.protobuf.FieldMask][google.protobuf.FieldMask].

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
