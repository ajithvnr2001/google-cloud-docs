---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.KnowledgeBases.KnowledgeBasesBase
title: Google Cloud Dialogflow v2 API - Class KnowledgeBases.KnowledgeBasesBase (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:23.138130+00:00
---

# Google Cloud Dialogflow v2 API - Class KnowledgeBases.KnowledgeBasesBase (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.KnowledgeBases.KnowledgeBasesBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class KnowledgeBases.KnowledgeBasesBase (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    [BindServiceMethod(typeof(KnowledgeBases), "BindService")]
    public abstract class KnowledgeBases.KnowledgeBasesBase

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class KnowledgeBases.KnowledgeBasesBase.

Base class for server-side implementations of KnowledgeBases

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > KnowledgeBases.KnowledgeBasesBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Methods 

### CreateKnowledgeBase(CreateKnowledgeBaseRequest, ServerCallContext)
    
    
    public virtual Task<KnowledgeBase> CreateKnowledgeBase(CreateKnowledgeBaseRequest request, ServerCallContext context)

Creates a knowledge base.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateKnowledgeBaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CreateKnowledgeBaseRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[KnowledgeBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.KnowledgeBase)` | The response to send back to the client (wrapped by a task).  
  
### DeleteKnowledgeBase(DeleteKnowledgeBaseRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteKnowledgeBase(DeleteKnowledgeBaseRequest request, ServerCallContext context)

Deletes the specified knowledge base.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteKnowledgeBaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DeleteKnowledgeBaseRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetKnowledgeBase(GetKnowledgeBaseRequest, ServerCallContext)
    
    
    public virtual Task<KnowledgeBase> GetKnowledgeBase(GetKnowledgeBaseRequest request, ServerCallContext context)

Retrieves the specified knowledge base.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetKnowledgeBaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GetKnowledgeBaseRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[KnowledgeBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.KnowledgeBase)` | The response to send back to the client (wrapped by a task).  
  
### ListKnowledgeBases(ListKnowledgeBasesRequest, ServerCallContext)
    
    
    public virtual Task<ListKnowledgeBasesResponse> ListKnowledgeBases(ListKnowledgeBasesRequest request, ServerCallContext context)

Returns the list of all knowledge bases of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListKnowledgeBasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ListKnowledgeBasesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListKnowledgeBasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ListKnowledgeBasesResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateKnowledgeBase(UpdateKnowledgeBaseRequest, ServerCallContext)
    
    
    public virtual Task<KnowledgeBase> UpdateKnowledgeBase(UpdateKnowledgeBaseRequest request, ServerCallContext context)

Updates the specified knowledge base.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateKnowledgeBaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.UpdateKnowledgeBaseRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[KnowledgeBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.KnowledgeBase)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
