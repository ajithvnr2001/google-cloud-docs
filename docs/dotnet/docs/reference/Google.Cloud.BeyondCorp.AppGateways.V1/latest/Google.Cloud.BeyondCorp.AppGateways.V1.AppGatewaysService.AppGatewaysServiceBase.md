---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/latest/Google.Cloud.BeyondCorp.AppGateways.V1.AppGatewaysService.AppGatewaysServiceBase
title: BeyondCorp AppGateways v1 API - Class AppGatewaysService.AppGatewaysServiceBase (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:36.689255+00:00
---

# BeyondCorp AppGateways v1 API - Class AppGatewaysService.AppGatewaysServiceBase (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/latest/Google.Cloud.BeyondCorp.AppGateways.V1.AppGatewaysService.AppGatewaysServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  BeyondCorp AppGateways v1 API - Class AppGatewaysService.AppGatewaysServiceBase (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/latest/Google.Cloud.BeyondCorp.AppGateways.V1.AppGatewaysService.AppGatewaysServiceBase)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/1.3.0/Google.Cloud.BeyondCorp.AppGateways.V1.AppGatewaysService.AppGatewaysServiceBase)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/1.2.0/Google.Cloud.BeyondCorp.AppGateways.V1.AppGatewaysService.AppGatewaysServiceBase)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/1.1.0/Google.Cloud.BeyondCorp.AppGateways.V1.AppGatewaysService.AppGatewaysServiceBase)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/1.0.0/Google.Cloud.BeyondCorp.AppGateways.V1.AppGatewaysService.AppGatewaysServiceBase)


    
    
    [BindServiceMethod(typeof(AppGatewaysService), "BindService")]
    public abstract class AppGatewaysService.AppGatewaysServiceBase

Reference documentation and code samples for the BeyondCorp AppGateways v1 API class AppGatewaysService.AppGatewaysServiceBase.

Base class for server-side implementations of AppGatewaysService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AppGatewaysService.AppGatewaysServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BeyondCorp.AppGateways.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/latest/Google.Cloud.BeyondCorp.AppGateways.V1)

## Assembly

Google.Cloud.BeyondCorp.AppGateways.V1.dll

## Methods 

### CreateAppGateway(CreateAppGatewayRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateAppGateway(CreateAppGatewayRequest request, ServerCallContext context)

Creates a new AppGateway in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/latest/Google.Cloud.BeyondCorp.AppGateways.V1.CreateAppGatewayRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteAppGateway(DeleteAppGatewayRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteAppGateway(DeleteAppGatewayRequest request, ServerCallContext context)

Deletes a single AppGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/latest/Google.Cloud.BeyondCorp.AppGateways.V1.DeleteAppGatewayRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetAppGateway(GetAppGatewayRequest, ServerCallContext)
    
    
    public virtual Task<AppGateway> GetAppGateway(GetAppGatewayRequest request, ServerCallContext context)

Gets details of a single AppGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/latest/Google.Cloud.BeyondCorp.AppGateways.V1.GetAppGatewayRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/latest/Google.Cloud.BeyondCorp.AppGateways.V1.AppGateway)` | The response to send back to the client (wrapped by a task).  
  
### ListAppGateways(ListAppGatewaysRequest, ServerCallContext)
    
    
    public virtual Task<ListAppGatewaysResponse> ListAppGateways(ListAppGatewaysRequest request, ServerCallContext context)

Lists AppGateways in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppGatewaysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/latest/Google.Cloud.BeyondCorp.AppGateways.V1.ListAppGatewaysRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAppGatewaysResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.AppGateways.V1/latest/Google.Cloud.BeyondCorp.AppGateways.V1.ListAppGatewaysResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
