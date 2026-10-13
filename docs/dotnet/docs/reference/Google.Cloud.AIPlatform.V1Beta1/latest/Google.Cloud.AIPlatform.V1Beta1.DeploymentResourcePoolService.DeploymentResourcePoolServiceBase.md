---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeploymentResourcePoolService.DeploymentResourcePoolServiceBase
title: Vertex AI v1beta1 API - Class DeploymentResourcePoolService.DeploymentResourcePoolServiceBase (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:19.336977+00:00
---

# Vertex AI v1beta1 API - Class DeploymentResourcePoolService.DeploymentResourcePoolServiceBase (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeploymentResourcePoolService.DeploymentResourcePoolServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class DeploymentResourcePoolService.DeploymentResourcePoolServiceBase (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    [BindServiceMethod(typeof(DeploymentResourcePoolService), "BindService")]
    public abstract class DeploymentResourcePoolService.DeploymentResourcePoolServiceBase

Reference documentation and code samples for the Vertex AI v1beta1 API class DeploymentResourcePoolService.DeploymentResourcePoolServiceBase.

Base class for server-side implementations of DeploymentResourcePoolService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeploymentResourcePoolService.DeploymentResourcePoolServiceBase

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

### CreateDeploymentResourcePool(CreateDeploymentResourcePoolRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateDeploymentResourcePool(CreateDeploymentResourcePoolRequest request, ServerCallContext context)

Create a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateDeploymentResourcePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteDeploymentResourcePool(DeleteDeploymentResourcePoolRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteDeploymentResourcePool(DeleteDeploymentResourcePoolRequest request, ServerCallContext context)

Delete a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteDeploymentResourcePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetDeploymentResourcePool(GetDeploymentResourcePoolRequest, ServerCallContext)
    
    
    public virtual Task<DeploymentResourcePool> GetDeploymentResourcePool(GetDeploymentResourcePoolRequest request, ServerCallContext context)

Get a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetDeploymentResourcePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DeploymentResourcePool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeploymentResourcePool)` | The response to send back to the client (wrapped by a task).  
  
### ListDeploymentResourcePools(ListDeploymentResourcePoolsRequest, ServerCallContext)
    
    
    public virtual Task<ListDeploymentResourcePoolsResponse> ListDeploymentResourcePools(ListDeploymentResourcePoolsRequest request, ServerCallContext context)

List DeploymentResourcePools in a location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentResourcePoolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListDeploymentResourcePoolsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListDeploymentResourcePoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListDeploymentResourcePoolsResponse)` | The response to send back to the client (wrapped by a task).  
  
### QueryDeployedModels(QueryDeployedModelsRequest, ServerCallContext)
    
    
    public virtual Task<QueryDeployedModelsResponse> QueryDeployedModels(QueryDeployedModelsRequest request, ServerCallContext context)

List DeployedModels that have been deployed on this DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDeployedModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.QueryDeployedModelsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QueryDeployedModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.QueryDeployedModelsResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateDeploymentResourcePool(UpdateDeploymentResourcePoolRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateDeploymentResourcePool(UpdateDeploymentResourcePoolRequest request, ServerCallContext context)

Update a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateDeploymentResourcePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
