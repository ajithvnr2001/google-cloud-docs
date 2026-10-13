---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableService.DataTableServiceClient
title: Chronicle v1 API - Class DataTableService.DataTableServiceClient (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:48.409957+00:00
---

# Chronicle v1 API - Class DataTableService.DataTableServiceClient (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableService.DataTableServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class DataTableService.DataTableServiceClient (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public class DataTableService.DataTableServiceClient : ClientBase<DataTableService.DataTableServiceClient>

Reference documentation and code samples for the Chronicle v1 API class DataTableService.DataTableServiceClient.

Client for DataTableService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[DataTableService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableService)[DataTableServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableService.DataTableServiceClient) > DataTableService.DataTableServiceClient

## Inherited Members

[ClientBase<DataTableService.DataTableServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### DataTableServiceClient()
    
    
    protected DataTableServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### DataTableServiceClient(CallInvoker)
    
    
    public DataTableServiceClient(CallInvoker callInvoker)

Creates a new client for DataTableService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### DataTableServiceClient(ChannelBase)
    
    
    public DataTableServiceClient(ChannelBase channel)

Creates a new client for DataTableService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### DataTableServiceClient(ClientBaseConfiguration)
    
    
    protected DataTableServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### BulkCreateDataTableRows(BulkCreateDataTableRowsRequest, CallOptions)
    
    
    public virtual BulkCreateDataTableRowsResponse BulkCreateDataTableRows(BulkCreateDataTableRowsRequest request, CallOptions options)

Create data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkCreateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BulkCreateDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsResponse)` | The response received from the server.  
  
### BulkCreateDataTableRows(BulkCreateDataTableRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BulkCreateDataTableRowsResponse BulkCreateDataTableRows(BulkCreateDataTableRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkCreateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest)`  
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
`[BulkCreateDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsResponse)` | The response received from the server.  
  
### BulkCreateDataTableRowsAsync(BulkCreateDataTableRowsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BulkCreateDataTableRowsResponse> BulkCreateDataTableRowsAsync(BulkCreateDataTableRowsRequest request, CallOptions options)

Create data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkCreateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BulkCreateDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsResponse)` | The call object.  
  
### BulkCreateDataTableRowsAsync(BulkCreateDataTableRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BulkCreateDataTableRowsResponse> BulkCreateDataTableRowsAsync(BulkCreateDataTableRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkCreateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BulkCreateDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsResponse)` | The call object.  
  
### BulkGetDataTableRows(BulkGetDataTableRowsRequest, CallOptions)
    
    
    public virtual BulkGetDataTableRowsResponse BulkGetDataTableRows(BulkGetDataTableRowsRequest request, CallOptions options)

Get data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkGetDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkGetDataTableRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BulkGetDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkGetDataTableRowsResponse)` | The response received from the server.  
  
### BulkGetDataTableRows(BulkGetDataTableRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BulkGetDataTableRowsResponse BulkGetDataTableRows(BulkGetDataTableRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkGetDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkGetDataTableRowsRequest)`  
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
`[BulkGetDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkGetDataTableRowsResponse)` | The response received from the server.  
  
### BulkGetDataTableRowsAsync(BulkGetDataTableRowsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BulkGetDataTableRowsResponse> BulkGetDataTableRowsAsync(BulkGetDataTableRowsRequest request, CallOptions options)

Get data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkGetDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkGetDataTableRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BulkGetDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkGetDataTableRowsResponse)` | The call object.  
  
### BulkGetDataTableRowsAsync(BulkGetDataTableRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BulkGetDataTableRowsResponse> BulkGetDataTableRowsAsync(BulkGetDataTableRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkGetDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkGetDataTableRowsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BulkGetDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkGetDataTableRowsResponse)` | The call object.  
  
### BulkReplaceDataTableRows(BulkReplaceDataTableRowsRequest, CallOptions)
    
    
    public virtual BulkReplaceDataTableRowsResponse BulkReplaceDataTableRows(BulkReplaceDataTableRowsRequest request, CallOptions options)

Replace all existing data table rows with new data table rows.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkReplaceDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkReplaceDataTableRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BulkReplaceDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkReplaceDataTableRowsResponse)` | The response received from the server.  
  
### BulkReplaceDataTableRows(BulkReplaceDataTableRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BulkReplaceDataTableRowsResponse BulkReplaceDataTableRows(BulkReplaceDataTableRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Replace all existing data table rows with new data table rows.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkReplaceDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkReplaceDataTableRowsRequest)`  
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
`[BulkReplaceDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkReplaceDataTableRowsResponse)` | The response received from the server.  
  
### BulkReplaceDataTableRowsAsync(BulkReplaceDataTableRowsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BulkReplaceDataTableRowsResponse> BulkReplaceDataTableRowsAsync(BulkReplaceDataTableRowsRequest request, CallOptions options)

Replace all existing data table rows with new data table rows.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkReplaceDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkReplaceDataTableRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BulkReplaceDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkReplaceDataTableRowsResponse)` | The call object.  
  
### BulkReplaceDataTableRowsAsync(BulkReplaceDataTableRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BulkReplaceDataTableRowsResponse> BulkReplaceDataTableRowsAsync(BulkReplaceDataTableRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Replace all existing data table rows with new data table rows.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkReplaceDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkReplaceDataTableRowsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BulkReplaceDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkReplaceDataTableRowsResponse)` | The call object.  
  
### BulkUpdateDataTableRows(BulkUpdateDataTableRowsRequest, CallOptions)
    
    
    public virtual BulkUpdateDataTableRowsResponse BulkUpdateDataTableRows(BulkUpdateDataTableRowsRequest request, CallOptions options)

Update data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkUpdateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkUpdateDataTableRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BulkUpdateDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkUpdateDataTableRowsResponse)` | The response received from the server.  
  
### BulkUpdateDataTableRows(BulkUpdateDataTableRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BulkUpdateDataTableRowsResponse BulkUpdateDataTableRows(BulkUpdateDataTableRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkUpdateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkUpdateDataTableRowsRequest)`  
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
`[BulkUpdateDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkUpdateDataTableRowsResponse)` | The response received from the server.  
  
### BulkUpdateDataTableRowsAsync(BulkUpdateDataTableRowsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BulkUpdateDataTableRowsResponse> BulkUpdateDataTableRowsAsync(BulkUpdateDataTableRowsRequest request, CallOptions options)

Update data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkUpdateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkUpdateDataTableRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BulkUpdateDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkUpdateDataTableRowsResponse)` | The call object.  
  
### BulkUpdateDataTableRowsAsync(BulkUpdateDataTableRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BulkUpdateDataTableRowsResponse> BulkUpdateDataTableRowsAsync(BulkUpdateDataTableRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update data table rows in bulk.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkUpdateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkUpdateDataTableRowsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BulkUpdateDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkUpdateDataTableRowsResponse)` | The call object.  
  
### CreateDataTable(CreateDataTableRequest, CallOptions)
    
    
    public virtual DataTable CreateDataTable(CreateDataTableRequest request, CallOptions options)

Create a new data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataTableRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The response received from the server.  
  
### CreateDataTable(CreateDataTableRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataTable CreateDataTable(CreateDataTableRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create a new data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataTableRequest)`  
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
`[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The response received from the server.  
  
### CreateDataTableAsync(CreateDataTableRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataTable> CreateDataTableAsync(CreateDataTableRequest request, CallOptions options)

Create a new data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataTableRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The call object.  
  
### CreateDataTableAsync(CreateDataTableRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataTable> CreateDataTableAsync(CreateDataTableRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create a new data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataTableRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The call object.  
  
### CreateDataTableRow(CreateDataTableRowRequest, CallOptions)
    
    
    public virtual DataTableRow CreateDataTableRow(CreateDataTableRowRequest request, CallOptions options)

Create a new data table row.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataTableRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The response received from the server.  
  
### CreateDataTableRow(CreateDataTableRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataTableRow CreateDataTableRow(CreateDataTableRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create a new data table row.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataTableRowRequest)`  
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
`[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The response received from the server.  
  
### CreateDataTableRowAsync(CreateDataTableRowRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataTableRow> CreateDataTableRowAsync(CreateDataTableRowRequest request, CallOptions options)

Create a new data table row.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataTableRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The call object.  
  
### CreateDataTableRowAsync(CreateDataTableRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataTableRow> CreateDataTableRowAsync(CreateDataTableRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create a new data table row.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataTableRowRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The call object.  
  
### DeleteDataTable(DeleteDataTableRequest, CallOptions)
    
    
    public virtual Empty DeleteDataTable(DeleteDataTableRequest request, CallOptions options)

Delete data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteDataTableRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteDataTable(DeleteDataTableRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteDataTable(DeleteDataTableRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Delete data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteDataTableRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteDataTableAsync(DeleteDataTableRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteDataTableAsync(DeleteDataTableRequest request, CallOptions options)

Delete data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteDataTableRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteDataTableAsync(DeleteDataTableRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteDataTableAsync(DeleteDataTableRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Delete data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteDataTableRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteDataTableRow(DeleteDataTableRowRequest, CallOptions)
    
    
    public virtual Empty DeleteDataTableRow(DeleteDataTableRowRequest request, CallOptions options)

Delete data table row.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteDataTableRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteDataTableRow(DeleteDataTableRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteDataTableRow(DeleteDataTableRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Delete data table row.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteDataTableRowRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteDataTableRowAsync(DeleteDataTableRowRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteDataTableRowAsync(DeleteDataTableRowRequest request, CallOptions options)

Delete data table row.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteDataTableRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteDataTableRowAsync(DeleteDataTableRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteDataTableRowAsync(DeleteDataTableRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Delete data table row.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteDataTableRowRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### GetDataTable(GetDataTableRequest, CallOptions)
    
    
    public virtual DataTable GetDataTable(GetDataTableRequest request, CallOptions options)

Get data table info.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The response received from the server.  
  
### GetDataTable(GetDataTableRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataTable GetDataTable(GetDataTableRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get data table info.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableRequest)`  
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
`[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The response received from the server.  
  
### GetDataTableAsync(GetDataTableRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataTable> GetDataTableAsync(GetDataTableRequest request, CallOptions options)

Get data table info.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The call object.  
  
### GetDataTableAsync(GetDataTableRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataTable> GetDataTableAsync(GetDataTableRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get data table info.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The call object.  
  
### GetDataTableOperationErrors(GetDataTableOperationErrorsRequest, CallOptions)
    
    
    public virtual DataTableOperationErrors GetDataTableOperationErrors(GetDataTableOperationErrorsRequest request, CallOptions options)

Get the error for a data table operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableOperationErrorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTableOperationErrors](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableOperationErrors)` | The response received from the server.  
  
### GetDataTableOperationErrors(GetDataTableOperationErrorsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataTableOperationErrors GetDataTableOperationErrors(GetDataTableOperationErrorsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get the error for a data table operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableOperationErrorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest)`  
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
`[DataTableOperationErrors](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableOperationErrors)` | The response received from the server.  
  
### GetDataTableOperationErrorsAsync(GetDataTableOperationErrorsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataTableOperationErrors> GetDataTableOperationErrorsAsync(GetDataTableOperationErrorsRequest request, CallOptions options)

Get the error for a data table operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableOperationErrorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTableOperationErrors](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableOperationErrors)` | The call object.  
  
### GetDataTableOperationErrorsAsync(GetDataTableOperationErrorsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataTableOperationErrors> GetDataTableOperationErrorsAsync(GetDataTableOperationErrorsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get the error for a data table operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableOperationErrorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTableOperationErrors](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableOperationErrors)` | The call object.  
  
### GetDataTableRow(GetDataTableRowRequest, CallOptions)
    
    
    public virtual DataTableRow GetDataTableRow(GetDataTableRowRequest request, CallOptions options)

Get data table row

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The response received from the server.  
  
### GetDataTableRow(GetDataTableRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataTableRow GetDataTableRow(GetDataTableRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get data table row

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableRowRequest)`  
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
`[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The response received from the server.  
  
### GetDataTableRowAsync(GetDataTableRowRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataTableRow> GetDataTableRowAsync(GetDataTableRowRequest request, CallOptions options)

Get data table row

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The call object.  
  
### GetDataTableRowAsync(GetDataTableRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataTableRow> GetDataTableRowAsync(GetDataTableRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get data table row

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableRowRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The call object.  
  
### ListDataTableRows(ListDataTableRowsRequest, CallOptions)
    
    
    public virtual ListDataTableRowsResponse ListDataTableRows(ListDataTableRowsRequest request, CallOptions options)

List data table rows.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTableRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTableRowsResponse)` | The response received from the server.  
  
### ListDataTableRows(ListDataTableRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDataTableRowsResponse ListDataTableRows(ListDataTableRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List data table rows.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTableRowsRequest)`  
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
`[ListDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTableRowsResponse)` | The response received from the server.  
  
### ListDataTableRowsAsync(ListDataTableRowsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDataTableRowsResponse> ListDataTableRowsAsync(ListDataTableRowsRequest request, CallOptions options)

List data table rows.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTableRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTableRowsResponse)` | The call object.  
  
### ListDataTableRowsAsync(ListDataTableRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDataTableRowsResponse> ListDataTableRowsAsync(ListDataTableRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List data table rows.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTableRowsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDataTableRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTableRowsResponse)` | The call object.  
  
### ListDataTables(ListDataTablesRequest, CallOptions)
    
    
    public virtual ListDataTablesResponse ListDataTables(ListDataTablesRequest request, CallOptions options)

List data tables.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataTablesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTablesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDataTablesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTablesResponse)` | The response received from the server.  
  
### ListDataTables(ListDataTablesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDataTablesResponse ListDataTables(ListDataTablesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List data tables.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataTablesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTablesRequest)`  
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
`[ListDataTablesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTablesResponse)` | The response received from the server.  
  
### ListDataTablesAsync(ListDataTablesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDataTablesResponse> ListDataTablesAsync(ListDataTablesRequest request, CallOptions options)

List data tables.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataTablesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTablesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDataTablesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTablesResponse)` | The call object.  
  
### ListDataTablesAsync(ListDataTablesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDataTablesResponse> ListDataTablesAsync(ListDataTablesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List data tables.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataTablesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTablesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDataTablesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListDataTablesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override DataTableService.DataTableServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataTableService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableService)[DataTableServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableService.DataTableServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Chronicle.V1.DataTableService.DataTableServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdateDataTable(UpdateDataTableRequest, CallOptions)
    
    
    public virtual DataTable UpdateDataTable(UpdateDataTableRequest request, CallOptions options)

Update data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateDataTableRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The response received from the server.  
  
### UpdateDataTable(UpdateDataTableRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataTable UpdateDataTable(UpdateDataTableRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateDataTableRequest)`  
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
`[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The response received from the server.  
  
### UpdateDataTableAsync(UpdateDataTableRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataTable> UpdateDataTableAsync(UpdateDataTableRequest request, CallOptions options)

Update data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateDataTableRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The call object.  
  
### UpdateDataTableAsync(UpdateDataTableRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataTable> UpdateDataTableAsync(UpdateDataTableRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update data table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataTableRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateDataTableRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTable)` | The call object.  
  
### UpdateDataTableRow(UpdateDataTableRowRequest, CallOptions)
    
    
    public virtual DataTableRow UpdateDataTableRow(UpdateDataTableRowRequest request, CallOptions options)

Update data table row

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateDataTableRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The response received from the server.  
  
### UpdateDataTableRow(UpdateDataTableRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataTableRow UpdateDataTableRow(UpdateDataTableRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update data table row

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateDataTableRowRequest)`  
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
`[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The response received from the server.  
  
### UpdateDataTableRowAsync(UpdateDataTableRowRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataTableRow> UpdateDataTableRowAsync(UpdateDataTableRowRequest request, CallOptions options)

Update data table row

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateDataTableRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The call object.  
  
### UpdateDataTableRowAsync(UpdateDataTableRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataTableRow> UpdateDataTableRowAsync(UpdateDataTableRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update data table row

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateDataTableRowRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableRow)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
