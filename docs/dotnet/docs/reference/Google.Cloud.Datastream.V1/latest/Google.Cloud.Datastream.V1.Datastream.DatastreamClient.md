---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream.DatastreamClient
title: DataStream v1 API - Class Datastream.DatastreamClient (2.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:23.202900+00:00
---

# DataStream v1 API - Class Datastream.DatastreamClient (2.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream.DatastreamClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  DataStream v1 API - Class Datastream.DatastreamClient (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.12.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.11.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.10.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.9.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.8.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.7.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.6.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.5.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.4.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.3.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.2.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.1.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.0.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/1.0.0/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)


    
    
    public class Datastream.DatastreamClient : ClientBase<Datastream.DatastreamClient>

Reference documentation and code samples for the DataStream v1 API class Datastream.DatastreamClient.

Client for Datastream

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[Datastream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream)[DatastreamClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream.DatastreamClient) > Datastream.DatastreamClient

## Inherited Members

[ClientBase<Datastream.DatastreamClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1)

## Assembly

Google.Cloud.Datastream.V1.dll

## Constructors 

### DatastreamClient()
    
    
    protected DatastreamClient()

Protected parameterless constructor to allow creation of test doubles.

### DatastreamClient(CallInvoker)
    
    
    public DatastreamClient(CallInvoker callInvoker)

Creates a new client for Datastream that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### DatastreamClient(ChannelBase)
    
    
    public DatastreamClient(ChannelBase channel)

Creates a new client for Datastream

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### DatastreamClient(ClientBaseConfiguration)
    
    
    protected DatastreamClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateConnectionProfile(CreateConnectionProfileRequest, CallOptions)
    
    
    public virtual Operation CreateConnectionProfile(CreateConnectionProfileRequest request, CallOptions options)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateConnectionProfileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateConnectionProfile(CreateConnectionProfileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateConnectionProfile(CreateConnectionProfileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateConnectionProfileRequest)`  
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
  
### CreateConnectionProfileAsync(CreateConnectionProfileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateConnectionProfileAsync(CreateConnectionProfileRequest request, CallOptions options)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateConnectionProfileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateConnectionProfileAsync(CreateConnectionProfileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateConnectionProfileAsync(CreateConnectionProfileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateConnectionProfileRequest)`  
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
  
### CreateIAMPolicyClient()
    
    
    public virtual IAMPolicy.IAMPolicyClient CreateIAMPolicyClient()

Creates a new instance of [IAMPolicy.IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[IAMPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.html)[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html)` | A new [IAMPolicy.IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) for the same target as this client.  
  
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
  
### CreatePrivateConnection(CreatePrivateConnectionRequest, CallOptions)
    
    
    public virtual Operation CreatePrivateConnection(CreatePrivateConnectionRequest request, CallOptions options)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreatePrivateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreatePrivateConnection(CreatePrivateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreatePrivateConnection(CreatePrivateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreatePrivateConnectionRequest)`  
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
  
### CreatePrivateConnectionAsync(CreatePrivateConnectionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreatePrivateConnectionAsync(CreatePrivateConnectionRequest request, CallOptions options)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreatePrivateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreatePrivateConnectionAsync(CreatePrivateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreatePrivateConnectionAsync(CreatePrivateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreatePrivateConnectionRequest)`  
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
  
### CreateRoute(CreateRouteRequest, CallOptions)
    
    
    public virtual Operation CreateRoute(CreateRouteRequest request, CallOptions options)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateRouteRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateRoute(CreateRouteRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateRoute(CreateRouteRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateRouteRequest)`  
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
  
### CreateRouteAsync(CreateRouteRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateRouteAsync(CreateRouteRequest request, CallOptions options)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateRouteRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateRouteAsync(CreateRouteRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateRouteAsync(CreateRouteRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateRouteRequest)`  
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
  
### CreateStream(CreateStreamRequest, CallOptions)
    
    
    public virtual Operation CreateStream(CreateStreamRequest request, CallOptions options)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateStream(CreateStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateStream(CreateStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateStreamRequest)`  
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
  
### CreateStreamAsync(CreateStreamRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateStreamAsync(CreateStreamRequest request, CallOptions options)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateStreamAsync(CreateStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateStreamAsync(CreateStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateStreamRequest)`  
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
  
### DeleteConnectionProfile(DeleteConnectionProfileRequest, CallOptions)
    
    
    public virtual Operation DeleteConnectionProfile(DeleteConnectionProfileRequest request, CallOptions options)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteConnectionProfileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteConnectionProfile(DeleteConnectionProfileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteConnectionProfile(DeleteConnectionProfileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteConnectionProfileRequest)`  
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
  
### DeleteConnectionProfileAsync(DeleteConnectionProfileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteConnectionProfileAsync(DeleteConnectionProfileRequest request, CallOptions options)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteConnectionProfileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteConnectionProfileAsync(DeleteConnectionProfileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteConnectionProfileAsync(DeleteConnectionProfileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteConnectionProfileRequest)`  
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
  
### DeletePrivateConnection(DeletePrivateConnectionRequest, CallOptions)
    
    
    public virtual Operation DeletePrivateConnection(DeletePrivateConnectionRequest request, CallOptions options)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeletePrivateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeletePrivateConnection(DeletePrivateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeletePrivateConnection(DeletePrivateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeletePrivateConnectionRequest)`  
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
  
### DeletePrivateConnectionAsync(DeletePrivateConnectionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeletePrivateConnectionAsync(DeletePrivateConnectionRequest request, CallOptions options)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeletePrivateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeletePrivateConnectionAsync(DeletePrivateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeletePrivateConnectionAsync(DeletePrivateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeletePrivateConnectionRequest)`  
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
  
### DeleteRoute(DeleteRouteRequest, CallOptions)
    
    
    public virtual Operation DeleteRoute(DeleteRouteRequest request, CallOptions options)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteRouteRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteRoute(DeleteRouteRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteRoute(DeleteRouteRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteRouteRequest)`  
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
  
### DeleteRouteAsync(DeleteRouteRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteRouteAsync(DeleteRouteRequest request, CallOptions options)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteRouteRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteRouteAsync(DeleteRouteRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteRouteAsync(DeleteRouteRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteRouteRequest)`  
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
  
### DeleteStream(DeleteStreamRequest, CallOptions)
    
    
    public virtual Operation DeleteStream(DeleteStreamRequest request, CallOptions options)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteStream(DeleteStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteStream(DeleteStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteStreamRequest)`  
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
  
### DeleteStreamAsync(DeleteStreamRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteStreamAsync(DeleteStreamRequest request, CallOptions options)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteStreamAsync(DeleteStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteStreamAsync(DeleteStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteStreamRequest)`  
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
  
### DiscoverConnectionProfile(DiscoverConnectionProfileRequest, CallOptions)
    
    
    public virtual DiscoverConnectionProfileResponse DiscoverConnectionProfile(DiscoverConnectionProfileRequest request, CallOptions options)

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileResponse)` | The response received from the server.  
  
### DiscoverConnectionProfile(DiscoverConnectionProfileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DiscoverConnectionProfileResponse DiscoverConnectionProfile(DiscoverConnectionProfileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileRequest)`  
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
`[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileResponse)` | The response received from the server.  
  
### DiscoverConnectionProfileAsync(DiscoverConnectionProfileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DiscoverConnectionProfileResponse> DiscoverConnectionProfileAsync(DiscoverConnectionProfileRequest request, CallOptions options)

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileResponse)` | The call object.  
  
### DiscoverConnectionProfileAsync(DiscoverConnectionProfileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DiscoverConnectionProfileResponse> DiscoverConnectionProfileAsync(DiscoverConnectionProfileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileResponse)` | The call object.  
  
### FetchStaticIps(FetchStaticIpsRequest, CallOptions)
    
    
    public virtual FetchStaticIpsResponse FetchStaticIps(FetchStaticIpsRequest request, CallOptions options)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchStaticIpsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)` | The response received from the server.  
  
### FetchStaticIps(FetchStaticIpsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FetchStaticIpsResponse FetchStaticIps(FetchStaticIpsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchStaticIpsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsRequest)`  
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
`[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)` | The response received from the server.  
  
### FetchStaticIpsAsync(FetchStaticIpsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FetchStaticIpsResponse> FetchStaticIpsAsync(FetchStaticIpsRequest request, CallOptions options)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchStaticIpsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)` | The call object.  
  
### FetchStaticIpsAsync(FetchStaticIpsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FetchStaticIpsResponse> FetchStaticIpsAsync(FetchStaticIpsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchStaticIpsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)` | The call object.  
  
### GetConnectionProfile(GetConnectionProfileRequest, CallOptions)
    
    
    public virtual ConnectionProfile GetConnectionProfile(GetConnectionProfileRequest request, CallOptions options)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetConnectionProfileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | The response received from the server.  
  
### GetConnectionProfile(GetConnectionProfileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ConnectionProfile GetConnectionProfile(GetConnectionProfileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetConnectionProfileRequest)`  
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
`[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | The response received from the server.  
  
### GetConnectionProfileAsync(GetConnectionProfileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ConnectionProfile> GetConnectionProfileAsync(GetConnectionProfileRequest request, CallOptions options)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetConnectionProfileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | The call object.  
  
### GetConnectionProfileAsync(GetConnectionProfileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ConnectionProfile> GetConnectionProfileAsync(GetConnectionProfileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetConnectionProfileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | The call object.  
  
### GetPrivateConnection(GetPrivateConnectionRequest, CallOptions)
    
    
    public virtual PrivateConnection GetPrivateConnection(GetPrivateConnectionRequest request, CallOptions options)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetPrivateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | The response received from the server.  
  
### GetPrivateConnection(GetPrivateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual PrivateConnection GetPrivateConnection(GetPrivateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetPrivateConnectionRequest)`  
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
`[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | The response received from the server.  
  
### GetPrivateConnectionAsync(GetPrivateConnectionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<PrivateConnection> GetPrivateConnectionAsync(GetPrivateConnectionRequest request, CallOptions options)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetPrivateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | The call object.  
  
### GetPrivateConnectionAsync(GetPrivateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<PrivateConnection> GetPrivateConnectionAsync(GetPrivateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetPrivateConnectionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | The call object.  
  
### GetRoute(GetRouteRequest, CallOptions)
    
    
    public virtual Route GetRoute(GetRouteRequest request, CallOptions options)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetRouteRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | The response received from the server.  
  
### GetRoute(GetRouteRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Route GetRoute(GetRouteRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetRouteRequest)`  
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
`[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | The response received from the server.  
  
### GetRouteAsync(GetRouteRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Route> GetRouteAsync(GetRouteRequest request, CallOptions options)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetRouteRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | The call object.  
  
### GetRouteAsync(GetRouteRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Route> GetRouteAsync(GetRouteRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetRouteRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | The call object.  
  
### GetStream(GetStreamRequest, CallOptions)
    
    
    public virtual Stream GetStream(GetStreamRequest request, CallOptions options)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | The response received from the server.  
  
### GetStream(GetStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Stream GetStream(GetStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest)`  
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
`[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | The response received from the server.  
  
### GetStreamAsync(GetStreamRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Stream> GetStreamAsync(GetStreamRequest request, CallOptions options)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | The call object.  
  
### GetStreamAsync(GetStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Stream> GetStreamAsync(GetStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | The call object.  
  
### GetStreamObject(GetStreamObjectRequest, CallOptions)
    
    
    public virtual StreamObject GetStreamObject(GetStreamObjectRequest request, CallOptions options)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamObjectRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The response received from the server.  
  
### GetStreamObject(GetStreamObjectRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual StreamObject GetStreamObject(GetStreamObjectRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamObjectRequest)`  
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
`[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The response received from the server.  
  
### GetStreamObjectAsync(GetStreamObjectRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<StreamObject> GetStreamObjectAsync(GetStreamObjectRequest request, CallOptions options)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamObjectRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The call object.  
  
### GetStreamObjectAsync(GetStreamObjectRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<StreamObject> GetStreamObjectAsync(GetStreamObjectRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamObjectRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The call object.  
  
### ListConnectionProfiles(ListConnectionProfilesRequest, CallOptions)
    
    
    public virtual ListConnectionProfilesResponse ListConnectionProfiles(ListConnectionProfilesRequest request, CallOptions options)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)` | The response received from the server.  
  
### ListConnectionProfiles(ListConnectionProfilesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListConnectionProfilesResponse ListConnectionProfiles(ListConnectionProfilesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesRequest)`  
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
`[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)` | The response received from the server.  
  
### ListConnectionProfilesAsync(ListConnectionProfilesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListConnectionProfilesResponse> ListConnectionProfilesAsync(ListConnectionProfilesRequest request, CallOptions options)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)` | The call object.  
  
### ListConnectionProfilesAsync(ListConnectionProfilesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListConnectionProfilesResponse> ListConnectionProfilesAsync(ListConnectionProfilesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)` | The call object.  
  
### ListPrivateConnections(ListPrivateConnectionsRequest, CallOptions)
    
    
    public virtual ListPrivateConnectionsResponse ListPrivateConnections(ListPrivateConnectionsRequest request, CallOptions options)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)` | The response received from the server.  
  
### ListPrivateConnections(ListPrivateConnectionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListPrivateConnectionsResponse ListPrivateConnections(ListPrivateConnectionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsRequest)`  
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
`[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)` | The response received from the server.  
  
### ListPrivateConnectionsAsync(ListPrivateConnectionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListPrivateConnectionsResponse> ListPrivateConnectionsAsync(ListPrivateConnectionsRequest request, CallOptions options)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)` | The call object.  
  
### ListPrivateConnectionsAsync(ListPrivateConnectionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListPrivateConnectionsResponse> ListPrivateConnectionsAsync(ListPrivateConnectionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)` | The call object.  
  
### ListRoutes(ListRoutesRequest, CallOptions)
    
    
    public virtual ListRoutesResponse ListRoutes(ListRoutesRequest request, CallOptions options)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)` | The response received from the server.  
  
### ListRoutes(ListRoutesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListRoutesResponse ListRoutes(ListRoutesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesRequest)`  
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
`[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)` | The response received from the server.  
  
### ListRoutesAsync(ListRoutesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListRoutesResponse> ListRoutesAsync(ListRoutesRequest request, CallOptions options)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)` | The call object.  
  
### ListRoutesAsync(ListRoutesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListRoutesResponse> ListRoutesAsync(ListRoutesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)` | The call object.  
  
### ListStreamObjects(ListStreamObjectsRequest, CallOptions)
    
    
    public virtual ListStreamObjectsResponse ListStreamObjects(ListStreamObjectsRequest request, CallOptions options)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamObjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)` | The response received from the server.  
  
### ListStreamObjects(ListStreamObjectsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListStreamObjectsResponse ListStreamObjects(ListStreamObjectsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamObjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsRequest)`  
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
`[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)` | The response received from the server.  
  
### ListStreamObjectsAsync(ListStreamObjectsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListStreamObjectsResponse> ListStreamObjectsAsync(ListStreamObjectsRequest request, CallOptions options)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamObjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)` | The call object.  
  
### ListStreamObjectsAsync(ListStreamObjectsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListStreamObjectsResponse> ListStreamObjectsAsync(ListStreamObjectsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamObjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)` | The call object.  
  
### ListStreams(ListStreamsRequest, CallOptions)
    
    
    public virtual ListStreamsResponse ListStreams(ListStreamsRequest request, CallOptions options)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)` | The response received from the server.  
  
### ListStreams(ListStreamsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListStreamsResponse ListStreams(ListStreamsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsRequest)`  
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
`[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)` | The response received from the server.  
  
### ListStreamsAsync(ListStreamsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListStreamsResponse> ListStreamsAsync(ListStreamsRequest request, CallOptions options)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)` | The call object.  
  
### ListStreamsAsync(ListStreamsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListStreamsResponse> ListStreamsAsync(ListStreamsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)` | The call object.  
  
### LookupStreamObject(LookupStreamObjectRequest, CallOptions)
    
    
    public virtual StreamObject LookupStreamObject(LookupStreamObjectRequest request, CallOptions options)

Use this method to look up a stream object by its source object identifier.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.LookupStreamObjectRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The response received from the server.  
  
### LookupStreamObject(LookupStreamObjectRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual StreamObject LookupStreamObject(LookupStreamObjectRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to look up a stream object by its source object identifier.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.LookupStreamObjectRequest)`  
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
`[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The response received from the server.  
  
### LookupStreamObjectAsync(LookupStreamObjectRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<StreamObject> LookupStreamObjectAsync(LookupStreamObjectRequest request, CallOptions options)

Use this method to look up a stream object by its source object identifier.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.LookupStreamObjectRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The call object.  
  
### LookupStreamObjectAsync(LookupStreamObjectRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<StreamObject> LookupStreamObjectAsync(LookupStreamObjectRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to look up a stream object by its source object identifier.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.LookupStreamObjectRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override Datastream.DatastreamClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Datastream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream)[DatastreamClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Datastream.V1.Datastream.DatastreamClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### RunStream(RunStreamRequest, CallOptions)
    
    
    public virtual Operation RunStream(RunStreamRequest request, CallOptions options)

Use this method to start, resume or recover a stream with a non default CDC strategy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RunStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RunStream(RunStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RunStream(RunStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to start, resume or recover a stream with a non default CDC strategy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RunStreamRequest)`  
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
  
### RunStreamAsync(RunStreamRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RunStreamAsync(RunStreamRequest request, CallOptions options)

Use this method to start, resume or recover a stream with a non default CDC strategy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RunStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RunStreamAsync(RunStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RunStreamAsync(RunStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to start, resume or recover a stream with a non default CDC strategy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RunStreamRequest)`  
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
  
### StartBackfillJob(StartBackfillJobRequest, CallOptions)
    
    
    public virtual StartBackfillJobResponse StartBackfillJob(StartBackfillJobRequest request, CallOptions options)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | The response received from the server.  
  
### StartBackfillJob(StartBackfillJobRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual StartBackfillJobResponse StartBackfillJob(StartBackfillJobRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobRequest)`  
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
`[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | The response received from the server.  
  
### StartBackfillJobAsync(StartBackfillJobRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<StartBackfillJobResponse> StartBackfillJobAsync(StartBackfillJobRequest request, CallOptions options)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | The call object.  
  
### StartBackfillJobAsync(StartBackfillJobRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<StartBackfillJobResponse> StartBackfillJobAsync(StartBackfillJobRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | The call object.  
  
### StopBackfillJob(StopBackfillJobRequest, CallOptions)
    
    
    public virtual StopBackfillJobResponse StopBackfillJob(StopBackfillJobRequest request, CallOptions options)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | The response received from the server.  
  
### StopBackfillJob(StopBackfillJobRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual StopBackfillJobResponse StopBackfillJob(StopBackfillJobRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobRequest)`  
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
`[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | The response received from the server.  
  
### StopBackfillJobAsync(StopBackfillJobRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<StopBackfillJobResponse> StopBackfillJobAsync(StopBackfillJobRequest request, CallOptions options)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | The call object.  
  
### StopBackfillJobAsync(StopBackfillJobRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<StopBackfillJobResponse> StopBackfillJobAsync(StopBackfillJobRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | The call object.  
  
### UpdateConnectionProfile(UpdateConnectionProfileRequest, CallOptions)
    
    
    public virtual Operation UpdateConnectionProfile(UpdateConnectionProfileRequest request, CallOptions options)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateConnectionProfileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateConnectionProfile(UpdateConnectionProfileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateConnectionProfile(UpdateConnectionProfileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateConnectionProfileRequest)`  
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
  
### UpdateConnectionProfileAsync(UpdateConnectionProfileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateConnectionProfileAsync(UpdateConnectionProfileRequest request, CallOptions options)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateConnectionProfileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateConnectionProfileAsync(UpdateConnectionProfileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateConnectionProfileAsync(UpdateConnectionProfileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateConnectionProfileRequest)`  
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
  
### UpdateStream(UpdateStreamRequest, CallOptions)
    
    
    public virtual Operation UpdateStream(UpdateStreamRequest request, CallOptions options)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateStream(UpdateStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateStream(UpdateStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateStreamRequest)`  
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
  
### UpdateStreamAsync(UpdateStreamRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateStreamAsync(UpdateStreamRequest request, CallOptions options)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateStreamAsync(UpdateStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateStreamAsync(UpdateStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateStreamRequest)`  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
