---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStoreService.DataStoreServiceClient
title: Discovery Engine v1beta API - Class DataStoreService.DataStoreServiceClient (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:08.887037+00:00
---

# Discovery Engine v1beta API - Class DataStoreService.DataStoreServiceClient (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStoreService.DataStoreServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class DataStoreService.DataStoreServiceClient (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public class DataStoreService.DataStoreServiceClient : ClientBase<DataStoreService.DataStoreServiceClient>

Reference documentation and code samples for the Discovery Engine v1beta API class DataStoreService.DataStoreServiceClient.

Client for DataStoreService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[DataStoreService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStoreService)[DataStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStoreService.DataStoreServiceClient) > DataStoreService.DataStoreServiceClient

## Inherited Members

[ClientBase<DataStoreService.DataStoreServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### DataStoreServiceClient()
    
    
    protected DataStoreServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### DataStoreServiceClient(CallInvoker)
    
    
    public DataStoreServiceClient(CallInvoker callInvoker)

Creates a new client for DataStoreService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### DataStoreServiceClient(ChannelBase)
    
    
    public DataStoreServiceClient(ChannelBase channel)

Creates a new client for DataStoreService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### DataStoreServiceClient(ClientBaseConfiguration)
    
    
    protected DataStoreServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateDataStore(CreateDataStoreRequest, CallOptions)
    
    
    public virtual Operation CreateDataStore(CreateDataStoreRequest request, CallOptions options)

Creates a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

DataStore is for storing [Documents][google.cloud.discoveryengine.v1beta.Document]. To serve these documents for Search, or Recommendation use case, an [Engine][google.cloud.discoveryengine.v1beta.Engine] needs to be created separately.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateDataStoreRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateDataStore(CreateDataStoreRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateDataStore(CreateDataStoreRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

DataStore is for storing [Documents][google.cloud.discoveryengine.v1beta.Document]. To serve these documents for Search, or Recommendation use case, an [Engine][google.cloud.discoveryengine.v1beta.Engine] needs to be created separately.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateDataStoreRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateDataStoreAsync(CreateDataStoreRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateDataStoreAsync(CreateDataStoreRequest request, CallOptions options)

Creates a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

DataStore is for storing [Documents][google.cloud.discoveryengine.v1beta.Document]. To serve these documents for Search, or Recommendation use case, an [Engine][google.cloud.discoveryengine.v1beta.Engine] needs to be created separately.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateDataStoreRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateDataStoreAsync(CreateDataStoreRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateDataStoreAsync(CreateDataStoreRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

DataStore is for storing [Documents][google.cloud.discoveryengine.v1beta.Document]. To serve these documents for Search, or Recommendation use case, an [Engine][google.cloud.discoveryengine.v1beta.Engine] needs to be created separately.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateDataStoreRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateLocationsClient()
    
    
    public virtual Locations.LocationsClient CreateLocationsClient()

Creates a new instance of [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Locations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.html)[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html)` | A new [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) for the same target as this client.  
  
### CreateOperationsClient()
    
    
    public virtual Operations.OperationsClient CreateOperationsClient()

Creates a new instance of [Operations.OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### DeleteDataStore(DeleteDataStoreRequest, CallOptions)
    
    
    public virtual Operation DeleteDataStore(DeleteDataStoreRequest request, CallOptions options)

Deletes a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteDataStoreRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteDataStore(DeleteDataStoreRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteDataStore(DeleteDataStoreRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteDataStoreRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteDataStoreAsync(DeleteDataStoreRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteDataStoreAsync(DeleteDataStoreRequest request, CallOptions options)

Deletes a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteDataStoreRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteDataStoreAsync(DeleteDataStoreRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteDataStoreAsync(DeleteDataStoreRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteDataStoreRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### GetDataStore(GetDataStoreRequest, CallOptions)
    
    
    public virtual DataStore GetDataStore(GetDataStoreRequest request, CallOptions options)

Gets a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetDataStoreRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStore)` | The response received from the server.  
  
### GetDataStore(GetDataStoreRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataStore GetDataStore(GetDataStoreRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetDataStoreRequest)`  
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
`[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStore)` | The response received from the server.  
  
### GetDataStoreAsync(GetDataStoreRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataStore> GetDataStoreAsync(GetDataStoreRequest request, CallOptions options)

Gets a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetDataStoreRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStore)` | The call object.  
  
### GetDataStoreAsync(GetDataStoreRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataStore> GetDataStoreAsync(GetDataStoreRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetDataStoreRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStore)` | The call object.  
  
### ListDataStores(ListDataStoresRequest, CallOptions)
    
    
    public virtual ListDataStoresResponse ListDataStores(ListDataStoresRequest request, CallOptions options)

Lists all the [DataStore][google.cloud.discoveryengine.v1beta.DataStore]s associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataStoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDataStoresRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDataStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDataStoresResponse)` | The response received from the server.  
  
### ListDataStores(ListDataStoresRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDataStoresResponse ListDataStores(ListDataStoresRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the [DataStore][google.cloud.discoveryengine.v1beta.DataStore]s associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataStoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDataStoresRequest)`  
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
`[ListDataStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDataStoresResponse)` | The response received from the server.  
  
### ListDataStoresAsync(ListDataStoresRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDataStoresResponse> ListDataStoresAsync(ListDataStoresRequest request, CallOptions options)

Lists all the [DataStore][google.cloud.discoveryengine.v1beta.DataStore]s associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataStoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDataStoresRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDataStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDataStoresResponse)` | The call object.  
  
### ListDataStoresAsync(ListDataStoresRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDataStoresResponse> ListDataStoresAsync(ListDataStoresRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the [DataStore][google.cloud.discoveryengine.v1beta.DataStore]s associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataStoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDataStoresRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDataStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDataStoresResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override DataStoreService.DataStoreServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStoreService)[DataStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStoreService.DataStoreServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.DiscoveryEngine.V1Beta.DataStoreService.DataStoreServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdateDataStore(UpdateDataStoreRequest, CallOptions)
    
    
    public virtual DataStore UpdateDataStore(UpdateDataStoreRequest request, CallOptions options)

Updates a [DataStore][google.cloud.discoveryengine.v1beta.DataStore]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateDataStoreRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStore)` | The response received from the server.  
  
### UpdateDataStore(UpdateDataStoreRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataStore UpdateDataStore(UpdateDataStoreRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a [DataStore][google.cloud.discoveryengine.v1beta.DataStore]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateDataStoreRequest)`  
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
`[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStore)` | The response received from the server.  
  
### UpdateDataStoreAsync(UpdateDataStoreRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataStore> UpdateDataStoreAsync(UpdateDataStoreRequest request, CallOptions options)

Updates a [DataStore][google.cloud.discoveryengine.v1beta.DataStore]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateDataStoreRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStore)` | The call object.  
  
### UpdateDataStoreAsync(UpdateDataStoreRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataStore> UpdateDataStoreAsync(UpdateDataStoreRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a [DataStore][google.cloud.discoveryengine.v1beta.DataStore]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateDataStoreRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DataStore)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
