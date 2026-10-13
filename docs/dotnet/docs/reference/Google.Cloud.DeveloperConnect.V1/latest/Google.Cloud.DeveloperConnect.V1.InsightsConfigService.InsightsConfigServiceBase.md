---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigService.InsightsConfigServiceBase
title: Developer Connect v1 API - Class InsightsConfigService.InsightsConfigServiceBase (1.0.0-beta04) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:31.737512+00:00
---

# Developer Connect v1 API - Class InsightsConfigService.InsightsConfigServiceBase (1.0.0-beta04)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigService.InsightsConfigServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Developer Connect v1 API - Class InsightsConfigService.InsightsConfigServiceBase (1.0.0-beta04) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta04 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigService.InsightsConfigServiceBase)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/1.0.0-beta03/Google.Cloud.DeveloperConnect.V1.InsightsConfigService.InsightsConfigServiceBase)


    
    
    [BindServiceMethod(typeof(InsightsConfigService), "BindService")]
    public abstract class InsightsConfigService.InsightsConfigServiceBase

Reference documentation and code samples for the Developer Connect v1 API class InsightsConfigService.InsightsConfigServiceBase.

Base class for server-side implementations of InsightsConfigService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InsightsConfigService.InsightsConfigServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DeveloperConnect.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1)

## Assembly

Google.Cloud.DeveloperConnect.V1.dll

## Methods 

### CreateInsightsConfig(CreateInsightsConfigRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateInsightsConfig(CreateInsightsConfigRequest request, ServerCallContext context)

Creates a new InsightsConfig in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInsightsConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.CreateInsightsConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteInsightsConfig(DeleteInsightsConfigRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteInsightsConfig(DeleteInsightsConfigRequest request, ServerCallContext context)

Deletes a single Insight.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInsightsConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.DeleteInsightsConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetDeploymentEvent(GetDeploymentEventRequest, ServerCallContext)
    
    
    public virtual Task<DeploymentEvent> GetDeploymentEvent(GetDeploymentEventRequest request, ServerCallContext context)

Gets a single Deployment Event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.GetDeploymentEventRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DeploymentEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.DeploymentEvent)` | The response to send back to the client (wrapped by a task).  
  
### GetInsightsConfig(GetInsightsConfigRequest, ServerCallContext)
    
    
    public virtual Task<InsightsConfig> GetInsightsConfig(GetInsightsConfigRequest request, ServerCallContext context)

Gets details of a single Insight.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInsightsConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.GetInsightsConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InsightsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfig)` | The response to send back to the client (wrapped by a task).  
  
### ListDeploymentEvents(ListDeploymentEventsRequest, ServerCallContext)
    
    
    public virtual Task<ListDeploymentEventsResponse> ListDeploymentEvents(ListDeploymentEventsRequest request, ServerCallContext context)

Lists Deployment Events in a given insights config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ListDeploymentEventsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListDeploymentEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ListDeploymentEventsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListInsightsConfigs(ListInsightsConfigsRequest, ServerCallContext)
    
    
    public virtual Task<ListInsightsConfigsResponse> ListInsightsConfigs(ListInsightsConfigsRequest request, ServerCallContext context)

Lists InsightsConfigs in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInsightsConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ListInsightsConfigsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListInsightsConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ListInsightsConfigsResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateInsightsConfig(UpdateInsightsConfigRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateInsightsConfig(UpdateInsightsConfigRequest request, ServerCallContext context)

Updates the parameters of a single InsightsConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInsightsConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.UpdateInsightsConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
