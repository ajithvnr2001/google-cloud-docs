---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AddContextArtifactsAndExecutionsRequest
title: Vertex AI v1beta1 API - Class AddContextArtifactsAndExecutionsRequest (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:01.861143+00:00
---

# Vertex AI v1beta1 API - Class AddContextArtifactsAndExecutionsRequest (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AddContextArtifactsAndExecutionsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AddContextArtifactsAndExecutionsRequest (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AddContextArtifactsAndExecutionsRequest : IMessage<AddContextArtifactsAndExecutionsRequest>, IEquatable<AddContextArtifactsAndExecutionsRequest>, IDeepCloneable<AddContextArtifactsAndExecutionsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class AddContextArtifactsAndExecutionsRequest.

Request message for [MetadataService.AddContextArtifactsAndExecutions][google.cloud.aiplatform.v1beta1.MetadataService.AddContextArtifactsAndExecutions].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AddContextArtifactsAndExecutionsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AddContextArtifactsAndExecutionsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AddContextArtifactsAndExecutionsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AddContextArtifactsAndExecutionsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### AddContextArtifactsAndExecutionsRequest()
    
    
    public AddContextArtifactsAndExecutionsRequest()

### AddContextArtifactsAndExecutionsRequest(AddContextArtifactsAndExecutionsRequest)
    
    
    public AddContextArtifactsAndExecutionsRequest(AddContextArtifactsAndExecutionsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AddContextArtifactsAndExecutionsRequest)`  
  
  
## Properties 

### Artifacts
    
    
    public RepeatedField<string> Artifacts { get; }

The resource names of the Artifacts to attribute to the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ArtifactsAsArtifactNames
    
    
    public ResourceNameList<ArtifactName> ArtifactsAsArtifactNames { get; }

[ArtifactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ArtifactName)-typed view over the [Artifacts](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AddContextArtifactsAndExecutionsRequest#Google_Cloud_AIPlatform_V1Beta1_AddContextArtifactsAndExecutionsRequest_Artifacts) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceNameList](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNameList-1.html)[ArtifactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ArtifactName)` |   
  
### Context
    
    
    public string Context { get; set; }

Required. The resource name of the Context that the Artifacts and Executions belong to. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ContextAsContextName
    
    
    public ContextName ContextAsContextName { get; set; }

[ContextName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ContextName)-typed view over the [Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AddContextArtifactsAndExecutionsRequest#Google_Cloud_AIPlatform_V1Beta1_AddContextArtifactsAndExecutionsRequest_Context) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ContextName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ContextName)` |   
  
### Executions
    
    
    public RepeatedField<string> Executions { get; }

The resource names of the Executions to associate with the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExecutionsAsExecutionNames
    
    
    public ResourceNameList<ExecutionName> ExecutionsAsExecutionNames { get; }

[ExecutionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExecutionName)-typed view over the [Executions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AddContextArtifactsAndExecutionsRequest#Google_Cloud_AIPlatform_V1Beta1_AddContextArtifactsAndExecutionsRequest_Executions) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceNameList](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNameList-1.html)[ExecutionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExecutionName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
