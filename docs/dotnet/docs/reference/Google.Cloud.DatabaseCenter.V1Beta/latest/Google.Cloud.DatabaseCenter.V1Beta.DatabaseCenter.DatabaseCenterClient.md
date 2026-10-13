---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter.DatabaseCenterClient
title: Database Center v1beta API - Class DatabaseCenter.DatabaseCenterClient (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:53.857866+00:00
---

# Database Center v1beta API - Class DatabaseCenter.DatabaseCenterClient (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter.DatabaseCenterClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class DatabaseCenter.DatabaseCenterClient (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public class DatabaseCenter.DatabaseCenterClient : ClientBase<DatabaseCenter.DatabaseCenterClient>

Reference documentation and code samples for the Database Center v1beta API class DatabaseCenter.DatabaseCenterClient.

Client for DatabaseCenter

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[DatabaseCenter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter)[DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter.DatabaseCenterClient) > DatabaseCenter.DatabaseCenterClient

## Inherited Members

[ClientBase<DatabaseCenter.DatabaseCenterClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### DatabaseCenterClient()
    
    
    protected DatabaseCenterClient()

Protected parameterless constructor to allow creation of test doubles.

### DatabaseCenterClient(CallInvoker)
    
    
    public DatabaseCenterClient(CallInvoker callInvoker)

Creates a new client for DatabaseCenter that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### DatabaseCenterClient(ChannelBase)
    
    
    public DatabaseCenterClient(ChannelBase channel)

Creates a new client for DatabaseCenter

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### DatabaseCenterClient(ClientBaseConfiguration)
    
    
    protected DatabaseCenterClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### AggregateFleet(AggregateFleetRequest, CallOptions)
    
    
    public virtual AggregateFleetResponse AggregateFleet(AggregateFleetRequest request, CallOptions options)

AggregateFleet provides statistics about the fleet grouped by various fields.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse)` | The response received from the server.  
  
### AggregateFleet(AggregateFleetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AggregateFleetResponse AggregateFleet(AggregateFleetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

AggregateFleet provides statistics about the fleet grouped by various fields.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse)` | The response received from the server.  
  
### AggregateFleetAsync(AggregateFleetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AggregateFleetResponse> AggregateFleetAsync(AggregateFleetRequest request, CallOptions options)

AggregateFleet provides statistics about the fleet grouped by various fields.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse)` | The call object.  
  
### AggregateFleetAsync(AggregateFleetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AggregateFleetResponse> AggregateFleetAsync(AggregateFleetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

AggregateFleet provides statistics about the fleet grouped by various fields.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse)` | The call object.  
  
### AggregateIssueStats(AggregateIssueStatsRequest, CallOptions)
    
    
    public virtual AggregateIssueStatsResponse AggregateIssueStats(AggregateIssueStatsRequest request, CallOptions options)

AggregateIssueStats provides database resource issues statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateIssueStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsResponse)` | The response received from the server.  
  
### AggregateIssueStats(AggregateIssueStatsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AggregateIssueStatsResponse AggregateIssueStats(AggregateIssueStatsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

AggregateIssueStats provides database resource issues statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateIssueStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsResponse)` | The response received from the server.  
  
### AggregateIssueStatsAsync(AggregateIssueStatsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AggregateIssueStatsResponse> AggregateIssueStatsAsync(AggregateIssueStatsRequest request, CallOptions options)

AggregateIssueStats provides database resource issues statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AggregateIssueStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsResponse)` | The call object.  
  
### AggregateIssueStatsAsync(AggregateIssueStatsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AggregateIssueStatsResponse> AggregateIssueStatsAsync(AggregateIssueStatsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

AggregateIssueStats provides database resource issues statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AggregateIssueStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsResponse)` | The call object.  
  
### AggregateQueryStats(AggregateQueryStatsRequest, CallOptions)
    
    
    public virtual AggregateQueryStatsResponse AggregateQueryStats(AggregateQueryStatsRequest request, CallOptions options)

AggregateQueryStats provides database resource query execution statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateQueryStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateQueryStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsResponse)` | The response received from the server.  
  
### AggregateQueryStats(AggregateQueryStatsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AggregateQueryStatsResponse AggregateQueryStats(AggregateQueryStatsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

AggregateQueryStats provides database resource query execution statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateQueryStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateQueryStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsResponse)` | The response received from the server.  
  
### AggregateQueryStatsAsync(AggregateQueryStatsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AggregateQueryStatsResponse> AggregateQueryStatsAsync(AggregateQueryStatsRequest request, CallOptions options)

AggregateQueryStats provides database resource query execution statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateQueryStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AggregateQueryStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsResponse)` | The call object.  
  
### AggregateQueryStatsAsync(AggregateQueryStatsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AggregateQueryStatsResponse> AggregateQueryStatsAsync(AggregateQueryStatsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

AggregateQueryStats provides database resource query execution statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateQueryStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AggregateQueryStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override DatabaseCenter.DatabaseCenterClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatabaseCenter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter)[DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter.DatabaseCenterClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter.DatabaseCenterClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest, CallOptions)
    
    
    public virtual QueryDatabaseResourceGroupsResponse QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest request, CallOptions options)

QueryDatabaseResourceGroups returns paginated results of database groups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsResponse)` | The response received from the server.  
  
### QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryDatabaseResourceGroupsResponse QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

QueryDatabaseResourceGroups returns paginated results of database groups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsResponse)` | The response received from the server.  
  
### QueryDatabaseResourceGroupsAsync(QueryDatabaseResourceGroupsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryDatabaseResourceGroupsResponse> QueryDatabaseResourceGroupsAsync(QueryDatabaseResourceGroupsRequest request, CallOptions options)

QueryDatabaseResourceGroups returns paginated results of database groups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsResponse)` | The call object.  
  
### QueryDatabaseResourceGroupsAsync(QueryDatabaseResourceGroupsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryDatabaseResourceGroupsResponse> QueryDatabaseResourceGroupsAsync(QueryDatabaseResourceGroupsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

QueryDatabaseResourceGroups returns paginated results of database groups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsResponse)` | The call object.  
  
### QueryIssues(QueryIssuesRequest, CallOptions)
    
    
    public virtual QueryIssuesResponse QueryIssues(QueryIssuesRequest request, CallOptions options)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)` | The response received from the server.  
  
### QueryIssues(QueryIssuesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryIssuesResponse QueryIssues(QueryIssuesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)` | The response received from the server.  
  
### QueryIssuesAsync(QueryIssuesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryIssuesResponse> QueryIssuesAsync(QueryIssuesRequest request, CallOptions options)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)` | The call object.  
  
### QueryIssuesAsync(QueryIssuesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryIssuesResponse> QueryIssuesAsync(QueryIssuesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)` | The call object.  
  
### QueryProducts(QueryProductsRequest, CallOptions)
    
    
    public virtual QueryProductsResponse QueryProducts(QueryProductsRequest request, CallOptions options)

QueryProducts provides a list of all possible products which can be used to filter database resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsResponse)` | The response received from the server.  
  
### QueryProducts(QueryProductsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryProductsResponse QueryProducts(QueryProductsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

QueryProducts provides a list of all possible products which can be used to filter database resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsResponse)` | The response received from the server.  
  
### QueryProductsAsync(QueryProductsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryProductsResponse> QueryProductsAsync(QueryProductsRequest request, CallOptions options)

QueryProducts provides a list of all possible products which can be used to filter database resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsResponse)` | The call object.  
  
### QueryProductsAsync(QueryProductsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryProductsResponse> QueryProductsAsync(QueryProductsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

QueryProducts provides a list of all possible products which can be used to filter database resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsResponse)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
