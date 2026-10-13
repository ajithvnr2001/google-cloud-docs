---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter.DatabaseCenterBase
title: Database Center v1beta API - Class DatabaseCenter.DatabaseCenterBase (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:52.828455+00:00
---

# Database Center v1beta API - Class DatabaseCenter.DatabaseCenterBase (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter.DatabaseCenterBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class DatabaseCenter.DatabaseCenterBase (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    [BindServiceMethod(typeof(DatabaseCenter), "BindService")]
    public abstract class DatabaseCenter.DatabaseCenterBase

Reference documentation and code samples for the Database Center v1beta API class DatabaseCenter.DatabaseCenterBase.

Base class for server-side implementations of DatabaseCenter

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DatabaseCenter.DatabaseCenterBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Methods 

### AggregateFleet(AggregateFleetRequest, ServerCallContext)
    
    
    public virtual Task<AggregateFleetResponse> AggregateFleet(AggregateFleetRequest request, ServerCallContext context)

AggregateFleet provides statistics about the fleet grouped by various fields.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse)` | The response to send back to the client (wrapped by a task).  
  
### AggregateIssueStats(AggregateIssueStatsRequest, ServerCallContext)
    
    
    public virtual Task<AggregateIssueStatsResponse> AggregateIssueStats(AggregateIssueStatsRequest request, ServerCallContext context)

AggregateIssueStats provides database resource issues statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AggregateIssueStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsResponse)` | The response to send back to the client (wrapped by a task).  
  
### AggregateQueryStats(AggregateQueryStatsRequest, ServerCallContext)
    
    
    public virtual Task<AggregateQueryStatsResponse> AggregateQueryStats(AggregateQueryStatsRequest request, ServerCallContext context)

AggregateQueryStats provides database resource query execution statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateQueryStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AggregateQueryStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsResponse)` | The response to send back to the client (wrapped by a task).  
  
### QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest, ServerCallContext)
    
    
    public virtual Task<QueryDatabaseResourceGroupsResponse> QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest request, ServerCallContext context)

QueryDatabaseResourceGroups returns paginated results of database groups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsResponse)` | The response to send back to the client (wrapped by a task).  
  
### QueryIssues(QueryIssuesRequest, ServerCallContext)
    
    
    public virtual Task<QueryIssuesResponse> QueryIssues(QueryIssuesRequest request, ServerCallContext context)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)` | The response to send back to the client (wrapped by a task).  
  
### QueryProducts(QueryProductsRequest, ServerCallContext)
    
    
    public virtual Task<QueryProductsResponse> QueryProducts(QueryProductsRequest request, ServerCallContext context)

QueryProducts provides a list of all possible products which can be used to filter database resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QueryProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
