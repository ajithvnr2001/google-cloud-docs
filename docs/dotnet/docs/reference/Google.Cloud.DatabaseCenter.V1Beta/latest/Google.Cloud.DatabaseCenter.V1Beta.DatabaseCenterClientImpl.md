---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClientImpl
title: Database Center v1beta API - Class DatabaseCenterClientImpl (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:54.209269+00:00
---

# Database Center v1beta API - Class DatabaseCenterClientImpl (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClientImpl

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class DatabaseCenterClientImpl (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class DatabaseCenterClientImpl : DatabaseCenterClient

Reference documentation and code samples for the Database Center v1beta API class DatabaseCenterClientImpl.

DatabaseCenter client wrapper implementation, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient) > DatabaseCenterClientImpl

## Inherited Members

[DatabaseCenterClient.DefaultEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_DefaultEndpoint)

[DatabaseCenterClient.DefaultScopes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_DefaultScopes)

[DatabaseCenterClient.ServiceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_ServiceMetadata)

[DatabaseCenterClient.CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_CreateAsync_System_Threading_CancellationToken_)

[DatabaseCenterClient.Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_Create)

[DatabaseCenterClient.ShutdownDefaultChannelsAsync()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_ShutdownDefaultChannelsAsync)

[DatabaseCenterClient.AggregateIssueStatsAsync(AggregateIssueStatsRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_AggregateIssueStatsAsync_Google_Cloud_DatabaseCenter_V1Beta_AggregateIssueStatsRequest_System_Threading_CancellationToken_)

[DatabaseCenterClient.QueryIssues(string, string, int?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_QueryIssues_System_String_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)

[DatabaseCenterClient.QueryIssuesAsync(string, string, int?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_QueryIssuesAsync_System_String_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Remarks

DatabaseCenter contains methods to query fleet view for database resources.

## Constructors 

### DatabaseCenterClientImpl(DatabaseCenterClient, DatabaseCenterSettings, ILogger)
    
    
    public DatabaseCenterClientImpl(DatabaseCenter.DatabaseCenterClient grpcClient, DatabaseCenterSettings settings, ILogger logger)

Constructs a client wrapper for the DatabaseCenter service, with the specified gRPC client and settings.

**Parameters**  
---  
**Name** | **Description**  
`grpcClient` | `[DatabaseCenter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter)[DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter.DatabaseCenterClient)`  
The underlying gRPC client.  
`settings` | `[DatabaseCenterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterSettings)`  
The base [DatabaseCenterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterSettings) used within this client.  
`logger` | `[ILogger](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.ilogger)`  
Optional [ILogger](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.ilogger) to use within this client.  
  
## Properties 

### GrpcClient
    
    
    public override DatabaseCenter.DatabaseCenterClient GrpcClient { get; }

The underlying gRPC DatabaseCenter client

**Property Value**  
---  
**Type** | **Description**  
`[DatabaseCenter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter)[DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter.DatabaseCenterClient)` |   
**Overrides**

[DatabaseCenterClient.GrpcClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_GrpcClient)

## Methods 

### AggregateFleet(AggregateFleetRequest, CallSettings)
    
    
    public override PagedEnumerable<AggregateFleetResponse, AggregateFleetRow> AggregateFleet(AggregateFleetRequest request, CallSettings callSettings = null)

AggregateFleet provides statistics about the fleet grouped by various fields.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse)[AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow)` | A pageable sequence of [AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow) resources.  
**Overrides**

[DatabaseCenterClient.AggregateFleet(AggregateFleetRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_AggregateFleet_Google_Cloud_DatabaseCenter_V1Beta_AggregateFleetRequest_Google_Api_Gax_Grpc_CallSettings_)

### AggregateFleetAsync(AggregateFleetRequest, CallSettings)
    
    
    public override PagedAsyncEnumerable<AggregateFleetResponse, AggregateFleetRow> AggregateFleetAsync(AggregateFleetRequest request, CallSettings callSettings = null)

AggregateFleet provides statistics about the fleet grouped by various fields.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse)[AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow)` | A pageable asynchronous sequence of [AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow) resources.  
**Overrides**

[DatabaseCenterClient.AggregateFleetAsync(AggregateFleetRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_AggregateFleetAsync_Google_Cloud_DatabaseCenter_V1Beta_AggregateFleetRequest_Google_Api_Gax_Grpc_CallSettings_)

### AggregateIssueStats(AggregateIssueStatsRequest, CallSettings)
    
    
    public override AggregateIssueStatsResponse AggregateIssueStats(AggregateIssueStatsRequest request, CallSettings callSettings = null)

AggregateIssueStats provides database resource issues statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateIssueStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsResponse)` | The RPC response.  
**Overrides**

[DatabaseCenterClient.AggregateIssueStats(AggregateIssueStatsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_AggregateIssueStats_Google_Cloud_DatabaseCenter_V1Beta_AggregateIssueStatsRequest_Google_Api_Gax_Grpc_CallSettings_)

### AggregateIssueStatsAsync(AggregateIssueStatsRequest, CallSettings)
    
    
    public override Task<AggregateIssueStatsResponse> AggregateIssueStatsAsync(AggregateIssueStatsRequest request, CallSettings callSettings = null)

AggregateIssueStats provides database resource issues statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AggregateIssueStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsResponse)` | A Task containing the RPC response.  
**Overrides**

[DatabaseCenterClient.AggregateIssueStatsAsync(AggregateIssueStatsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_AggregateIssueStatsAsync_Google_Cloud_DatabaseCenter_V1Beta_AggregateIssueStatsRequest_Google_Api_Gax_Grpc_CallSettings_)

### AggregateQueryStats(AggregateQueryStatsRequest, CallSettings)
    
    
    public override PagedEnumerable<AggregateQueryStatsResponse, QueryStatsInfo> AggregateQueryStats(AggregateQueryStatsRequest request, CallSettings callSettings = null)

AggregateQueryStats provides database resource query execution statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateQueryStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AggregateQueryStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsResponse)[QueryStatsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryStatsInfo)` | A pageable sequence of [QueryStatsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryStatsInfo) resources.  
**Overrides**

[DatabaseCenterClient.AggregateQueryStats(AggregateQueryStatsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_AggregateQueryStats_Google_Cloud_DatabaseCenter_V1Beta_AggregateQueryStatsRequest_Google_Api_Gax_Grpc_CallSettings_)

### AggregateQueryStatsAsync(AggregateQueryStatsRequest, CallSettings)
    
    
    public override PagedAsyncEnumerable<AggregateQueryStatsResponse, QueryStatsInfo> AggregateQueryStatsAsync(AggregateQueryStatsRequest request, CallSettings callSettings = null)

AggregateQueryStats provides database resource query execution statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateQueryStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AggregateQueryStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsResponse)[QueryStatsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryStatsInfo)` | A pageable asynchronous sequence of [QueryStatsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryStatsInfo) resources.  
**Overrides**

[DatabaseCenterClient.AggregateQueryStatsAsync(AggregateQueryStatsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_AggregateQueryStatsAsync_Google_Cloud_DatabaseCenter_V1Beta_AggregateQueryStatsRequest_Google_Api_Gax_Grpc_CallSettings_)

### QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest, CallSettings)
    
    
    public override PagedEnumerable<QueryDatabaseResourceGroupsResponse, DatabaseResourceGroup> QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest request, CallSettings callSettings = null)

QueryDatabaseResourceGroups returns paginated results of database groups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsResponse)[DatabaseResourceGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceGroup)` | A pageable sequence of [DatabaseResourceGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceGroup) resources.  
**Overrides**

[DatabaseCenterClient.QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_QueryDatabaseResourceGroups_Google_Cloud_DatabaseCenter_V1Beta_QueryDatabaseResourceGroupsRequest_Google_Api_Gax_Grpc_CallSettings_)

### QueryDatabaseResourceGroupsAsync(QueryDatabaseResourceGroupsRequest, CallSettings)
    
    
    public override PagedAsyncEnumerable<QueryDatabaseResourceGroupsResponse, DatabaseResourceGroup> QueryDatabaseResourceGroupsAsync(QueryDatabaseResourceGroupsRequest request, CallSettings callSettings = null)

QueryDatabaseResourceGroups returns paginated results of database groups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsResponse)[DatabaseResourceGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceGroup)` | A pageable asynchronous sequence of [DatabaseResourceGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceGroup) resources.  
**Overrides**

[DatabaseCenterClient.QueryDatabaseResourceGroupsAsync(QueryDatabaseResourceGroupsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_QueryDatabaseResourceGroupsAsync_Google_Cloud_DatabaseCenter_V1Beta_QueryDatabaseResourceGroupsRequest_Google_Api_Gax_Grpc_CallSettings_)

### QueryIssues(QueryIssuesRequest, CallSettings)
    
    
    public override PagedEnumerable<QueryIssuesResponse, DatabaseResourceIssue> QueryIssues(QueryIssuesRequest request, CallSettings callSettings = null)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)[DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue)` | A pageable sequence of [DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue) resources.  
**Overrides**

[DatabaseCenterClient.QueryIssues(QueryIssuesRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_QueryIssues_Google_Cloud_DatabaseCenter_V1Beta_QueryIssuesRequest_Google_Api_Gax_Grpc_CallSettings_)

### QueryIssuesAsync(QueryIssuesRequest, CallSettings)
    
    
    public override PagedAsyncEnumerable<QueryIssuesResponse, DatabaseResourceIssue> QueryIssuesAsync(QueryIssuesRequest request, CallSettings callSettings = null)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)[DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue)` | A pageable asynchronous sequence of [DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue) resources.  
**Overrides**

[DatabaseCenterClient.QueryIssuesAsync(QueryIssuesRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_QueryIssuesAsync_Google_Cloud_DatabaseCenter_V1Beta_QueryIssuesRequest_Google_Api_Gax_Grpc_CallSettings_)

### QueryProducts(QueryProductsRequest, CallSettings)
    
    
    public override PagedEnumerable<QueryProductsResponse, Product> QueryProducts(QueryProductsRequest request, CallSettings callSettings = null)

QueryProducts provides a list of all possible products which can be used to filter database resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[QueryProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsResponse)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Product)` | A pageable sequence of [Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Product) resources.  
**Overrides**

[DatabaseCenterClient.QueryProducts(QueryProductsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_QueryProducts_Google_Cloud_DatabaseCenter_V1Beta_QueryProductsRequest_Google_Api_Gax_Grpc_CallSettings_)

### QueryProductsAsync(QueryProductsRequest, CallSettings)
    
    
    public override PagedAsyncEnumerable<QueryProductsResponse, Product> QueryProductsAsync(QueryProductsRequest request, CallSettings callSettings = null)

QueryProducts provides a list of all possible products which can be used to filter database resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[QueryProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsResponse)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Product)` | A pageable asynchronous sequence of [Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Product) resources.  
**Overrides**

[DatabaseCenterClient.QueryProductsAsync(QueryProductsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_QueryProductsAsync_Google_Cloud_DatabaseCenter_V1Beta_QueryProductsRequest_Google_Api_Gax_Grpc_CallSettings_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
