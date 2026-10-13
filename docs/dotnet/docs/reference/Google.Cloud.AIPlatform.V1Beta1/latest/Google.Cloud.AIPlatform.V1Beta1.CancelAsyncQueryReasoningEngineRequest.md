---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CancelAsyncQueryReasoningEngineRequest
title: Vertex AI v1beta1 API - Class CancelAsyncQueryReasoningEngineRequest (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:28.708360+00:00
---

# Vertex AI v1beta1 API - Class CancelAsyncQueryReasoningEngineRequest (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CancelAsyncQueryReasoningEngineRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class CancelAsyncQueryReasoningEngineRequest (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class CancelAsyncQueryReasoningEngineRequest : IMessage<CancelAsyncQueryReasoningEngineRequest>, IEquatable<CancelAsyncQueryReasoningEngineRequest>, IDeepCloneable<CancelAsyncQueryReasoningEngineRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class CancelAsyncQueryReasoningEngineRequest.

Request message for [ReasoningEngineExecutionService.CancelAsyncQueryReasoningEngine][google.cloud.aiplatform.v1beta1.ReasoningEngineExecutionService.CancelAsyncQueryReasoningEngine].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CancelAsyncQueryReasoningEngineRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CancelAsyncQueryReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CancelAsyncQueryReasoningEngineRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CancelAsyncQueryReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CancelAsyncQueryReasoningEngineRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CancelAsyncQueryReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CancelAsyncQueryReasoningEngineRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### CancelAsyncQueryReasoningEngineRequest()
    
    
    public CancelAsyncQueryReasoningEngineRequest()

### CancelAsyncQueryReasoningEngineRequest(CancelAsyncQueryReasoningEngineRequest)
    
    
    public CancelAsyncQueryReasoningEngineRequest(CancelAsyncQueryReasoningEngineRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CancelAsyncQueryReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CancelAsyncQueryReasoningEngineRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The name of the ReasoningEngine resource to use. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OperationName
    
    
    public string OperationName { get; set; }

Required. The name of the longrunning operation returned from AsyncQueryReasoningEngine. Format: `projects/{project}/locations/{location}/operations/{operation}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReasoningEngineName
    
    
    public ReasoningEngineName ReasoningEngineName { get; set; }

[ReasoningEngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CancelAsyncQueryReasoningEngineRequest#Google_Cloud_AIPlatform_V1Beta1_CancelAsyncQueryReasoningEngineRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ReasoningEngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
