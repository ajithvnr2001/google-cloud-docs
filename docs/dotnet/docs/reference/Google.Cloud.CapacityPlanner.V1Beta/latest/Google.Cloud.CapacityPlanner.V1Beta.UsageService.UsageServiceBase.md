---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageService.UsageServiceBase
title: Capacity Planner v1beta API - Class UsageService.UsageServiceBase (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:58.042578+00:00
---

# Capacity Planner v1beta API - Class UsageService.UsageServiceBase (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageService.UsageServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Capacity Planner v1beta API - Class UsageService.UsageServiceBase (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta02 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageService.UsageServiceBase)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/1.0.0-beta01/Google.Cloud.CapacityPlanner.V1Beta.UsageService.UsageServiceBase)


    
    
    [BindServiceMethod(typeof(UsageService), "BindService")]
    public abstract class UsageService.UsageServiceBase

Reference documentation and code samples for the Capacity Planner v1beta API class UsageService.UsageServiceBase.

Base class for server-side implementations of UsageService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UsageService.UsageServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CapacityPlanner.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta)

## Assembly

Google.Cloud.CapacityPlanner.V1Beta.dll

## Methods 

### ExportForecasts(ExportForecastsRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ExportForecasts(ExportForecastsRequest request, ServerCallContext context)

Exports forecasted usage data requested by user into either an existing Cloud Storage bucket or a BigQuery table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportForecastsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportForecastsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ExportReservationsUsage(ExportReservationsUsageRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ExportReservationsUsage(ExportReservationsUsageRequest request, ServerCallContext context)

Exports reservations usage data requested by user into either an existing Cloud Storage bucket or a new/existing BigQuery table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportReservationsUsageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportReservationsUsageRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ExportUsageHistories(ExportUsageHistoriesRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ExportUsageHistories(ExportUsageHistoriesRequest request, ServerCallContext context)

Exports historical usage data requested by user into either an existing Cloud Storage bucket or a BigQuery table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportUsageHistoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportUsageHistoriesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### QueryForecasts(QueryForecastsRequest, ServerCallContext)
    
    
    public virtual Task<QueryForecastsResponse> QueryForecasts(QueryForecastsRequest request, ServerCallContext context)

Returns a list of the forecasts that are in the parent parameter and match your specified filters.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryForecastsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryForecastsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QueryForecastsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryForecastsResponse)` | The response to send back to the client (wrapped by a task).  
  
### QueryReservations(QueryReservationsRequest, ServerCallContext)
    
    
    public virtual Task<QueryReservationsResponse> QueryReservations(QueryReservationsRequest request, ServerCallContext context)

Returns a list of the reservations that are in the parent parameter and match your specified filters.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryReservationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryReservationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QueryReservationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryReservationsResponse)` | The response to send back to the client (wrapped by a task).  
  
### QueryUsageHistories(QueryUsageHistoriesRequest, ServerCallContext)
    
    
    public virtual Task<QueryUsageHistoriesResponse> QueryUsageHistories(QueryUsageHistoriesRequest request, ServerCallContext context)

Returns a list of the usage histories that are in the parent parameter and match your specified filters.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryUsageHistoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryUsageHistoriesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QueryUsageHistoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryUsageHistoriesResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
