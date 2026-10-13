---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionService.ReasoningEngineRuntimeRevisionServiceBase
title: Vertex AI v1beta1 API - Class ReasoningEngineRuntimeRevisionService.ReasoningEngineRuntimeRevisionServiceBase (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:18.991651+00:00
---

# Vertex AI v1beta1 API - Class ReasoningEngineRuntimeRevisionService.ReasoningEngineRuntimeRevisionServiceBase (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionService.ReasoningEngineRuntimeRevisionServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ReasoningEngineRuntimeRevisionService.ReasoningEngineRuntimeRevisionServiceBase (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    [BindServiceMethod(typeof(ReasoningEngineRuntimeRevisionService), "BindService")]
    public abstract class ReasoningEngineRuntimeRevisionService.ReasoningEngineRuntimeRevisionServiceBase

Reference documentation and code samples for the Vertex AI v1beta1 API class ReasoningEngineRuntimeRevisionService.ReasoningEngineRuntimeRevisionServiceBase.

Base class for server-side implementations of ReasoningEngineRuntimeRevisionService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReasoningEngineRuntimeRevisionService.ReasoningEngineRuntimeRevisionServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Methods 

### DeleteReasoningEngineRuntimeRevision(DeleteReasoningEngineRuntimeRevisionRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteReasoningEngineRuntimeRevision(DeleteReasoningEngineRuntimeRevisionRequest request, ServerCallContext context)

Deletes a reasoning engine revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReasoningEngineRuntimeRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteReasoningEngineRuntimeRevisionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetReasoningEngineRuntimeRevision(GetReasoningEngineRuntimeRevisionRequest, ServerCallContext)
    
    
    public virtual Task<ReasoningEngineRuntimeRevision> GetReasoningEngineRuntimeRevision(GetReasoningEngineRuntimeRevisionRequest request, ServerCallContext context)

Gets a reasoning engine runtime revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReasoningEngineRuntimeRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetReasoningEngineRuntimeRevisionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevision)` | The response to send back to the client (wrapped by a task).  
  
### ListReasoningEngineRuntimeRevisions(ListReasoningEngineRuntimeRevisionsRequest, ServerCallContext)
    
    
    public virtual Task<ListReasoningEngineRuntimeRevisionsResponse> ListReasoningEngineRuntimeRevisions(ListReasoningEngineRuntimeRevisionsRequest request, ServerCallContext context)

Lists runtime revisions in a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReasoningEngineRuntimeRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEngineRuntimeRevisionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListReasoningEngineRuntimeRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEngineRuntimeRevisionsResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
