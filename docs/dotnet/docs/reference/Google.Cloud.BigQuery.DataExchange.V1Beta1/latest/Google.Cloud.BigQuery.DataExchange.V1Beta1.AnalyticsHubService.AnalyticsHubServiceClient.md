---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService.AnalyticsHubServiceClient
title: Analytics Hub v1beta1 API - Class AnalyticsHubService.AnalyticsHubServiceClient (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:46.832335+00:00
---

# Analytics Hub v1beta1 API - Class AnalyticsHubService.AnalyticsHubServiceClient (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService.AnalyticsHubServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Analytics Hub v1beta1 API - Class AnalyticsHubService.AnalyticsHubServiceClient (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService.AnalyticsHubServiceClient)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/2.0.0-beta06/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService.AnalyticsHubServiceClient)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/1.0.0-beta01/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService.AnalyticsHubServiceClient)


    
    
    public class AnalyticsHubService.AnalyticsHubServiceClient : ClientBase<AnalyticsHubService.AnalyticsHubServiceClient>

Reference documentation and code samples for the Analytics Hub v1beta1 API class AnalyticsHubService.AnalyticsHubServiceClient.

Client for AnalyticsHubService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[AnalyticsHubService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService)[AnalyticsHubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService.AnalyticsHubServiceClient) > AnalyticsHubService.AnalyticsHubServiceClient

## Inherited Members

[ClientBase<AnalyticsHubService.AnalyticsHubServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.DataExchange.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1)

## Assembly

Google.Cloud.BigQuery.DataExchange.V1Beta1.dll

## Constructors 

### AnalyticsHubServiceClient()
    
    
    protected AnalyticsHubServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### AnalyticsHubServiceClient(CallInvoker)
    
    
    public AnalyticsHubServiceClient(CallInvoker callInvoker)

Creates a new client for AnalyticsHubService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### AnalyticsHubServiceClient(ChannelBase)
    
    
    public AnalyticsHubServiceClient(ChannelBase channel)

Creates a new client for AnalyticsHubService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### AnalyticsHubServiceClient(ClientBaseConfiguration)
    
    
    protected AnalyticsHubServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateDataExchange(CreateDataExchangeRequest, CallOptions)
    
    
    public virtual DataExchange CreateDataExchange(CreateDataExchangeRequest request, CallOptions options)

Creates a new data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.CreateDataExchangeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The response received from the server.  
  
### CreateDataExchange(CreateDataExchangeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataExchange CreateDataExchange(CreateDataExchangeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.CreateDataExchangeRequest)`  
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
`[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The response received from the server.  
  
### CreateDataExchangeAsync(CreateDataExchangeRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataExchange> CreateDataExchangeAsync(CreateDataExchangeRequest request, CallOptions options)

Creates a new data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.CreateDataExchangeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The call object.  
  
### CreateDataExchangeAsync(CreateDataExchangeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataExchange> CreateDataExchangeAsync(CreateDataExchangeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.CreateDataExchangeRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The call object.  
  
### CreateListing(CreateListingRequest, CallOptions)
    
    
    public virtual Listing CreateListing(CreateListingRequest request, CallOptions options)

Creates a new listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.CreateListingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The response received from the server.  
  
### CreateListing(CreateListingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Listing CreateListing(CreateListingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.CreateListingRequest)`  
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
`[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The response received from the server.  
  
### CreateListingAsync(CreateListingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Listing> CreateListingAsync(CreateListingRequest request, CallOptions options)

Creates a new listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.CreateListingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The call object.  
  
### CreateListingAsync(CreateListingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Listing> CreateListingAsync(CreateListingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.CreateListingRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The call object.  
  
### CreateLocationsClient()
    
    
    public virtual Locations.LocationsClient CreateLocationsClient()

Creates a new instance of [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Locations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.html)[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html)` | A new [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) for the same target as this client.  
  
### DeleteDataExchange(DeleteDataExchangeRequest, CallOptions)
    
    
    public virtual Empty DeleteDataExchange(DeleteDataExchangeRequest request, CallOptions options)

Deletes an existing data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteDataExchangeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteDataExchange(DeleteDataExchangeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteDataExchange(DeleteDataExchangeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes an existing data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteDataExchangeRequest)`  
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
  
### DeleteDataExchangeAsync(DeleteDataExchangeRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteDataExchangeAsync(DeleteDataExchangeRequest request, CallOptions options)

Deletes an existing data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteDataExchangeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteDataExchangeAsync(DeleteDataExchangeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteDataExchangeAsync(DeleteDataExchangeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes an existing data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteDataExchangeRequest)`  
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
  
### DeleteListing(DeleteListingRequest, CallOptions)
    
    
    public virtual Empty DeleteListing(DeleteListingRequest request, CallOptions options)

Deletes a listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteListing(DeleteListingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteListing(DeleteListingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest)`  
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
  
### DeleteListingAsync(DeleteListingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteListingAsync(DeleteListingRequest request, CallOptions options)

Deletes a listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteListingAsync(DeleteListingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteListingAsync(DeleteListingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest)`  
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
  
### GetDataExchange(GetDataExchangeRequest, CallOptions)
    
    
    public virtual DataExchange GetDataExchange(GetDataExchangeRequest request, CallOptions options)

Gets the details of a data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.GetDataExchangeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The response received from the server.  
  
### GetDataExchange(GetDataExchangeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataExchange GetDataExchange(GetDataExchangeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.GetDataExchangeRequest)`  
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
`[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The response received from the server.  
  
### GetDataExchangeAsync(GetDataExchangeRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataExchange> GetDataExchangeAsync(GetDataExchangeRequest request, CallOptions options)

Gets the details of a data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.GetDataExchangeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The call object.  
  
### GetDataExchangeAsync(GetDataExchangeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataExchange> GetDataExchangeAsync(GetDataExchangeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.GetDataExchangeRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The call object.  
  
### GetIamPolicy(GetIamPolicyRequest, CallOptions)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyRequest request, CallOptions options)

Gets the IAM policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The response received from the server.  
  
### GetIamPolicy(GetIamPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the IAM policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
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
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The response received from the server.  
  
### GetIamPolicyAsync(GetIamPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CallOptions options)

Gets the IAM policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The call object.  
  
### GetIamPolicyAsync(GetIamPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the IAM policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The call object.  
  
### GetListing(GetListingRequest, CallOptions)
    
    
    public virtual Listing GetListing(GetListingRequest request, CallOptions options)

Gets the details of a listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.GetListingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The response received from the server.  
  
### GetListing(GetListingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Listing GetListing(GetListingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.GetListingRequest)`  
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
`[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The response received from the server.  
  
### GetListingAsync(GetListingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Listing> GetListingAsync(GetListingRequest request, CallOptions options)

Gets the details of a listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.GetListingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The call object.  
  
### GetListingAsync(GetListingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Listing> GetListingAsync(GetListingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.GetListingRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The call object.  
  
### ListDataExchanges(ListDataExchangesRequest, CallOptions)
    
    
    public virtual ListDataExchangesResponse ListDataExchanges(ListDataExchangesRequest request, CallOptions options)

Lists all data exchanges in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataExchangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListDataExchangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListDataExchangesResponse)` | The response received from the server.  
  
### ListDataExchanges(ListDataExchangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDataExchangesResponse ListDataExchanges(ListDataExchangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all data exchanges in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataExchangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListDataExchangesRequest)`  
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
`[ListDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListDataExchangesResponse)` | The response received from the server.  
  
### ListDataExchangesAsync(ListDataExchangesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDataExchangesResponse> ListDataExchangesAsync(ListDataExchangesRequest request, CallOptions options)

Lists all data exchanges in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataExchangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListDataExchangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListDataExchangesResponse)` | The call object.  
  
### ListDataExchangesAsync(ListDataExchangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDataExchangesResponse> ListDataExchangesAsync(ListDataExchangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all data exchanges in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataExchangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListDataExchangesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListDataExchangesResponse)` | The call object.  
  
### ListListings(ListListingsRequest, CallOptions)
    
    
    public virtual ListListingsResponse ListListings(ListListingsRequest request, CallOptions options)

Lists all listings in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListListingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListListingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListListingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListListingsResponse)` | The response received from the server.  
  
### ListListings(ListListingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListListingsResponse ListListings(ListListingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all listings in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListListingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListListingsRequest)`  
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
`[ListListingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListListingsResponse)` | The response received from the server.  
  
### ListListingsAsync(ListListingsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListListingsResponse> ListListingsAsync(ListListingsRequest request, CallOptions options)

Lists all listings in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListListingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListListingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListListingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListListingsResponse)` | The call object.  
  
### ListListingsAsync(ListListingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListListingsResponse> ListListingsAsync(ListListingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all listings in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListListingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListListingsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListListingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListListingsResponse)` | The call object.  
  
### ListOrgDataExchanges(ListOrgDataExchangesRequest, CallOptions)
    
    
    public virtual ListOrgDataExchangesResponse ListOrgDataExchanges(ListOrgDataExchangesRequest request, CallOptions options)

Lists all data exchanges from projects in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOrgDataExchangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListOrgDataExchangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListOrgDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListOrgDataExchangesResponse)` | The response received from the server.  
  
### ListOrgDataExchanges(ListOrgDataExchangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListOrgDataExchangesResponse ListOrgDataExchanges(ListOrgDataExchangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all data exchanges from projects in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOrgDataExchangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListOrgDataExchangesRequest)`  
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
`[ListOrgDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListOrgDataExchangesResponse)` | The response received from the server.  
  
### ListOrgDataExchangesAsync(ListOrgDataExchangesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListOrgDataExchangesResponse> ListOrgDataExchangesAsync(ListOrgDataExchangesRequest request, CallOptions options)

Lists all data exchanges from projects in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOrgDataExchangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListOrgDataExchangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListOrgDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListOrgDataExchangesResponse)` | The call object.  
  
### ListOrgDataExchangesAsync(ListOrgDataExchangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListOrgDataExchangesResponse> ListOrgDataExchangesAsync(ListOrgDataExchangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all data exchanges from projects in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOrgDataExchangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListOrgDataExchangesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListOrgDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListOrgDataExchangesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override AnalyticsHubService.AnalyticsHubServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService)[AnalyticsHubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService.AnalyticsHubServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService.AnalyticsHubServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### SetIamPolicy(SetIamPolicyRequest, CallOptions)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyRequest request, CallOptions options)

Sets the IAM policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The response received from the server.  
  
### SetIamPolicy(SetIamPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sets the IAM policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
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
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The response received from the server.  
  
### SetIamPolicyAsync(SetIamPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CallOptions options)

Sets the IAM policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The call object.  
  
### SetIamPolicyAsync(SetIamPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sets the IAM policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The call object.  
  
### SubscribeListing(SubscribeListingRequest, CallOptions)
    
    
    public virtual SubscribeListingResponse SubscribeListing(SubscribeListingRequest request, CallOptions options)

Subscribes to a listing.

Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SubscribeListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.SubscribeListingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SubscribeListingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.SubscribeListingResponse)` | The response received from the server.  
  
### SubscribeListing(SubscribeListingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SubscribeListingResponse SubscribeListing(SubscribeListingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Subscribes to a listing.

Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SubscribeListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.SubscribeListingRequest)`  
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
`[SubscribeListingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.SubscribeListingResponse)` | The response received from the server.  
  
### SubscribeListingAsync(SubscribeListingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SubscribeListingResponse> SubscribeListingAsync(SubscribeListingRequest request, CallOptions options)

Subscribes to a listing.

Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SubscribeListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.SubscribeListingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SubscribeListingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.SubscribeListingResponse)` | The call object.  
  
### SubscribeListingAsync(SubscribeListingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SubscribeListingResponse> SubscribeListingAsync(SubscribeListingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Subscribes to a listing.

Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SubscribeListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.SubscribeListingRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SubscribeListingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.SubscribeListingResponse)` | The call object.  
  
### TestIamPermissions(TestIamPermissionsRequest, CallOptions)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(TestIamPermissionsRequest request, CallOptions options)

Returns the permissions that a caller has.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The response received from the server.  
  
### TestIamPermissions(TestIamPermissionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(TestIamPermissionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the permissions that a caller has.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
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
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The response received from the server.  
  
### TestIamPermissionsAsync(TestIamPermissionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, CallOptions options)

Returns the permissions that a caller has.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The call object.  
  
### TestIamPermissionsAsync(TestIamPermissionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the permissions that a caller has.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The call object.  
  
### UpdateDataExchange(UpdateDataExchangeRequest, CallOptions)
    
    
    public virtual DataExchange UpdateDataExchange(UpdateDataExchangeRequest request, CallOptions options)

Updates an existing data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.UpdateDataExchangeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The response received from the server.  
  
### UpdateDataExchange(UpdateDataExchangeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DataExchange UpdateDataExchange(UpdateDataExchangeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates an existing data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.UpdateDataExchangeRequest)`  
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
`[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The response received from the server.  
  
### UpdateDataExchangeAsync(UpdateDataExchangeRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DataExchange> UpdateDataExchangeAsync(UpdateDataExchangeRequest request, CallOptions options)

Updates an existing data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.UpdateDataExchangeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The call object.  
  
### UpdateDataExchangeAsync(UpdateDataExchangeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DataExchange> UpdateDataExchangeAsync(UpdateDataExchangeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates an existing data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataExchangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.UpdateDataExchangeRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchange)` | The call object.  
  
### UpdateListing(UpdateListingRequest, CallOptions)
    
    
    public virtual Listing UpdateListing(UpdateListingRequest request, CallOptions options)

Updates an existing listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.UpdateListingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The response received from the server.  
  
### UpdateListing(UpdateListingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Listing UpdateListing(UpdateListingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates an existing listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.UpdateListingRequest)`  
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
`[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The response received from the server.  
  
### UpdateListingAsync(UpdateListingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Listing> UpdateListingAsync(UpdateListingRequest request, CallOptions options)

Updates an existing listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.UpdateListingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The call object.  
  
### UpdateListingAsync(UpdateListingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Listing> UpdateListingAsync(UpdateListingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates an existing listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.UpdateListingRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Listing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.Listing)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
