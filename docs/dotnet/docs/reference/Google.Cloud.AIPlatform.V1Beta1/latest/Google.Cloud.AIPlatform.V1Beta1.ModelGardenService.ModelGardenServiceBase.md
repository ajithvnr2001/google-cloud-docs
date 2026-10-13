---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenService.ModelGardenServiceBase
title: Vertex AI v1beta1 API - Class ModelGardenService.ModelGardenServiceBase (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:33.581753+00:00
---

# Vertex AI v1beta1 API - Class ModelGardenService.ModelGardenServiceBase (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenService.ModelGardenServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ModelGardenService.ModelGardenServiceBase (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    [BindServiceMethod(typeof(ModelGardenService), "BindService")]
    public abstract class ModelGardenService.ModelGardenServiceBase

Reference documentation and code samples for the Vertex AI v1beta1 API class ModelGardenService.ModelGardenServiceBase.

Base class for server-side implementations of ModelGardenService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ModelGardenService.ModelGardenServiceBase

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

### AcceptPublisherModelEula(AcceptPublisherModelEulaRequest, ServerCallContext)
    
    
    public virtual Task<PublisherModelEulaAcceptance> AcceptPublisherModelEula(AcceptPublisherModelEulaRequest request, ServerCallContext context)

Accepts the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptPublisherModelEulaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AcceptPublisherModelEulaRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | The response to send back to the client (wrapped by a task).  
  
### CheckPublisherModelEulaAcceptance(CheckPublisherModelEulaAcceptanceRequest, ServerCallContext)
    
    
    public virtual Task<PublisherModelEulaAcceptance> CheckPublisherModelEulaAcceptance(CheckPublisherModelEulaAcceptanceRequest request, ServerCallContext context)

Checks the EULA acceptance status of a publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckPublisherModelEulaAcceptanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CheckPublisherModelEulaAcceptanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModelEulaAcceptance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModelEulaAcceptance)` | The response to send back to the client (wrapped by a task).  
  
### Deploy(DeployRequest, ServerCallContext)
    
    
    public virtual Task<Operation> Deploy(DeployRequest request, ServerCallContext context)

Deploys a model to a new endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeployPublisherModel(DeployPublisherModelRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<Operation> DeployPublisherModel(DeployPublisherModelRequest request, ServerCallContext context)

Deploys publisher models.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ExportPublisherModel(ExportPublisherModelRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ExportPublisherModel(ExportPublisherModelRequest request, ServerCallContext context)

Exports a publisher model to a user provided Google Cloud Storage bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExportPublisherModelRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetPublisherModel(GetPublisherModelRequest, ServerCallContext)
    
    
    public virtual Task<PublisherModel> GetPublisherModel(GetPublisherModelRequest request, ServerCallContext context)

Gets a Model Garden publisher model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetPublisherModelRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PublisherModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PublisherModel)` | The response to send back to the client (wrapped by a task).  
  
### ListPublisherModels(ListPublisherModelsRequest, ServerCallContext)
    
    
    public virtual Task<ListPublisherModelsResponse> ListPublisherModels(ListPublisherModelsRequest request, ServerCallContext context)

Lists publisher models in Model Garden.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPublisherModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListPublisherModelsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPublisherModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListPublisherModelsResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
