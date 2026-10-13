---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.AgentRegistry.AgentRegistryClient
title: Agent Registry v1 API - Class AgentRegistry.AgentRegistryClient (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:22.362536+00:00
---

# Agent Registry v1 API - Class AgentRegistry.AgentRegistryClient (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.AgentRegistry.AgentRegistryClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Agent Registry v1 API - Class AgentRegistry.AgentRegistryClient (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public class AgentRegistry.AgentRegistryClient : ClientBase<AgentRegistry.AgentRegistryClient>

Reference documentation and code samples for the Agent Registry v1 API class AgentRegistry.AgentRegistryClient.

Client for AgentRegistry

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[AgentRegistry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.AgentRegistry)[AgentRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.AgentRegistry.AgentRegistryClient) > AgentRegistry.AgentRegistryClient

## Inherited Members

[ClientBase<AgentRegistry.AgentRegistryClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AgentRegistry.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1)

## Assembly

Google.Cloud.AgentRegistry.V1.dll

## Constructors 

### AgentRegistryClient()
    
    
    protected AgentRegistryClient()

Protected parameterless constructor to allow creation of test doubles.

### AgentRegistryClient(CallInvoker)
    
    
    public AgentRegistryClient(CallInvoker callInvoker)

Creates a new client for AgentRegistry that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### AgentRegistryClient(ChannelBase)
    
    
    public AgentRegistryClient(ChannelBase channel)

Creates a new client for AgentRegistry

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### AgentRegistryClient(ClientBaseConfiguration)
    
    
    protected AgentRegistryClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateBinding(CreateBindingRequest, CallOptions)
    
    
    public virtual Operation CreateBinding(CreateBindingRequest request, CallOptions options)

Creates a new Binding in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.CreateBindingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateBinding(CreateBindingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateBinding(CreateBindingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Binding in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.CreateBindingRequest)`  
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
  
### CreateBindingAsync(CreateBindingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateBindingAsync(CreateBindingRequest request, CallOptions options)

Creates a new Binding in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.CreateBindingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateBindingAsync(CreateBindingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateBindingAsync(CreateBindingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Binding in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.CreateBindingRequest)`  
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
  
### CreateService(CreateServiceRequest, CallOptions)
    
    
    public virtual Operation CreateService(CreateServiceRequest request, CallOptions options)

Creates a new Service in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.CreateServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateService(CreateServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateService(CreateServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Service in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.CreateServiceRequest)`  
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
  
### CreateServiceAsync(CreateServiceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateServiceAsync(CreateServiceRequest request, CallOptions options)

Creates a new Service in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.CreateServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateServiceAsync(CreateServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateServiceAsync(CreateServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Service in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.CreateServiceRequest)`  
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
  
### DeleteBinding(DeleteBindingRequest, CallOptions)
    
    
    public virtual Operation DeleteBinding(DeleteBindingRequest request, CallOptions options)

Deletes a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteBinding(DeleteBindingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteBinding(DeleteBindingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest)`  
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
  
### DeleteBindingAsync(DeleteBindingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteBindingAsync(DeleteBindingRequest request, CallOptions options)

Deletes a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteBindingAsync(DeleteBindingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteBindingAsync(DeleteBindingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest)`  
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
  
### DeleteService(DeleteServiceRequest, CallOptions)
    
    
    public virtual Operation DeleteService(DeleteServiceRequest request, CallOptions options)

Deletes a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteService(DeleteServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteService(DeleteServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteServiceRequest)`  
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
  
### DeleteServiceAsync(DeleteServiceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteServiceAsync(DeleteServiceRequest request, CallOptions options)

Deletes a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteServiceAsync(DeleteServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteServiceAsync(DeleteServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteServiceRequest)`  
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
  
### FetchAvailableBindings(FetchAvailableBindingsRequest, CallOptions)
    
    
    public virtual FetchAvailableBindingsResponse FetchAvailableBindings(FetchAvailableBindingsRequest request, CallOptions options)

Fetches available Bindings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchAvailableBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.FetchAvailableBindingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchAvailableBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.FetchAvailableBindingsResponse)` | The response received from the server.  
  
### FetchAvailableBindings(FetchAvailableBindingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FetchAvailableBindingsResponse FetchAvailableBindings(FetchAvailableBindingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches available Bindings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchAvailableBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.FetchAvailableBindingsRequest)`  
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
`[FetchAvailableBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.FetchAvailableBindingsResponse)` | The response received from the server.  
  
### FetchAvailableBindingsAsync(FetchAvailableBindingsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FetchAvailableBindingsResponse> FetchAvailableBindingsAsync(FetchAvailableBindingsRequest request, CallOptions options)

Fetches available Bindings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchAvailableBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.FetchAvailableBindingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchAvailableBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.FetchAvailableBindingsResponse)` | The call object.  
  
### FetchAvailableBindingsAsync(FetchAvailableBindingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FetchAvailableBindingsResponse> FetchAvailableBindingsAsync(FetchAvailableBindingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches available Bindings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchAvailableBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.FetchAvailableBindingsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchAvailableBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.FetchAvailableBindingsResponse)` | The call object.  
  
### GetAgent(GetAgentRequest, CallOptions)
    
    
    public virtual Agent GetAgent(GetAgentRequest request, CallOptions options)

Gets details of a single Agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetAgentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Agent)` | The response received from the server.  
  
### GetAgent(GetAgentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Agent GetAgent(GetAgentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetAgentRequest)`  
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
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Agent)` | The response received from the server.  
  
### GetAgentAsync(GetAgentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Agent> GetAgentAsync(GetAgentRequest request, CallOptions options)

Gets details of a single Agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetAgentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Agent)` | The call object.  
  
### GetAgentAsync(GetAgentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Agent> GetAgentAsync(GetAgentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetAgentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Agent)` | The call object.  
  
### GetBinding(GetBindingRequest, CallOptions)
    
    
    public virtual Binding GetBinding(GetBindingRequest request, CallOptions options)

Gets details of a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetBindingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Binding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Binding)` | The response received from the server.  
  
### GetBinding(GetBindingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Binding GetBinding(GetBindingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetBindingRequest)`  
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
`[Binding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Binding)` | The response received from the server.  
  
### GetBindingAsync(GetBindingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Binding> GetBindingAsync(GetBindingRequest request, CallOptions options)

Gets details of a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetBindingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Binding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Binding)` | The call object.  
  
### GetBindingAsync(GetBindingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Binding> GetBindingAsync(GetBindingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetBindingRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Binding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Binding)` | The call object.  
  
### GetEndpoint(GetEndpointRequest, CallOptions)
    
    
    public virtual Endpoint GetEndpoint(GetEndpointRequest request, CallOptions options)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetEndpointRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint)` | The response received from the server.  
  
### GetEndpoint(GetEndpointRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Endpoint GetEndpoint(GetEndpointRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetEndpointRequest)`  
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
`[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint)` | The response received from the server.  
  
### GetEndpointAsync(GetEndpointRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Endpoint> GetEndpointAsync(GetEndpointRequest request, CallOptions options)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetEndpointRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint)` | The call object.  
  
### GetEndpointAsync(GetEndpointRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Endpoint> GetEndpointAsync(GetEndpointRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetEndpointRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint)` | The call object.  
  
### GetMcpServer(GetMcpServerRequest, CallOptions)
    
    
    public virtual McpServer GetMcpServer(GetMcpServerRequest request, CallOptions options)

Gets details of a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetMcpServerRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.McpServer)` | The response received from the server.  
  
### GetMcpServer(GetMcpServerRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual McpServer GetMcpServer(GetMcpServerRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetMcpServerRequest)`  
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
`[McpServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.McpServer)` | The response received from the server.  
  
### GetMcpServerAsync(GetMcpServerRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<McpServer> GetMcpServerAsync(GetMcpServerRequest request, CallOptions options)

Gets details of a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetMcpServerRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[McpServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.McpServer)` | The call object.  
  
### GetMcpServerAsync(GetMcpServerRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<McpServer> GetMcpServerAsync(GetMcpServerRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetMcpServerRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[McpServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.McpServer)` | The call object.  
  
### GetService(GetServiceRequest, CallOptions)
    
    
    public virtual Service GetService(GetServiceRequest request, CallOptions options)

Gets details of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Service)` | The response received from the server.  
  
### GetService(GetServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Service GetService(GetServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetServiceRequest)`  
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
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Service)` | The response received from the server.  
  
### GetServiceAsync(GetServiceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Service> GetServiceAsync(GetServiceRequest request, CallOptions options)

Gets details of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Service)` | The call object.  
  
### GetServiceAsync(GetServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Service> GetServiceAsync(GetServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.GetServiceRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Service)` | The call object.  
  
### ListAgents(ListAgentsRequest, CallOptions)
    
    
    public virtual ListAgentsResponse ListAgents(ListAgentsRequest request, CallOptions options)

Lists Agents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListAgentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListAgentsResponse)` | The response received from the server.  
  
### ListAgents(ListAgentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAgentsResponse ListAgents(ListAgentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Agents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListAgentsRequest)`  
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
`[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListAgentsResponse)` | The response received from the server.  
  
### ListAgentsAsync(ListAgentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAgentsResponse> ListAgentsAsync(ListAgentsRequest request, CallOptions options)

Lists Agents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListAgentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListAgentsResponse)` | The call object.  
  
### ListAgentsAsync(ListAgentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAgentsResponse> ListAgentsAsync(ListAgentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Agents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListAgentsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListAgentsResponse)` | The call object.  
  
### ListBindings(ListBindingsRequest, CallOptions)
    
    
    public virtual ListBindingsResponse ListBindings(ListBindingsRequest request, CallOptions options)

Lists Bindings in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListBindingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListBindingsResponse)` | The response received from the server.  
  
### ListBindings(ListBindingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListBindingsResponse ListBindings(ListBindingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Bindings in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListBindingsRequest)`  
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
`[ListBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListBindingsResponse)` | The response received from the server.  
  
### ListBindingsAsync(ListBindingsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListBindingsResponse> ListBindingsAsync(ListBindingsRequest request, CallOptions options)

Lists Bindings in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListBindingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListBindingsResponse)` | The call object.  
  
### ListBindingsAsync(ListBindingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListBindingsResponse> ListBindingsAsync(ListBindingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Bindings in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListBindingsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListBindingsResponse)` | The call object.  
  
### ListEndpoints(ListEndpointsRequest, CallOptions)
    
    
    public virtual ListEndpointsResponse ListEndpoints(ListEndpointsRequest request, CallOptions options)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListEndpointsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListEndpointsResponse)` | The response received from the server.  
  
### ListEndpoints(ListEndpointsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListEndpointsResponse ListEndpoints(ListEndpointsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListEndpointsRequest)`  
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
`[ListEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListEndpointsResponse)` | The response received from the server.  
  
### ListEndpointsAsync(ListEndpointsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListEndpointsResponse> ListEndpointsAsync(ListEndpointsRequest request, CallOptions options)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListEndpointsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListEndpointsResponse)` | The call object.  
  
### ListEndpointsAsync(ListEndpointsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListEndpointsResponse> ListEndpointsAsync(ListEndpointsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListEndpointsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListEndpointsResponse)` | The call object.  
  
### ListMcpServers(ListMcpServersRequest, CallOptions)
    
    
    public virtual ListMcpServersResponse ListMcpServers(ListMcpServersRequest request, CallOptions options)

Lists McpServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListMcpServersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListMcpServersResponse)` | The response received from the server.  
  
### ListMcpServers(ListMcpServersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListMcpServersResponse ListMcpServers(ListMcpServersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists McpServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListMcpServersRequest)`  
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
`[ListMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListMcpServersResponse)` | The response received from the server.  
  
### ListMcpServersAsync(ListMcpServersRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListMcpServersResponse> ListMcpServersAsync(ListMcpServersRequest request, CallOptions options)

Lists McpServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListMcpServersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListMcpServersResponse)` | The call object.  
  
### ListMcpServersAsync(ListMcpServersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListMcpServersResponse> ListMcpServersAsync(ListMcpServersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists McpServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListMcpServersRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListMcpServersResponse)` | The call object.  
  
### ListServices(ListServicesRequest, CallOptions)
    
    
    public virtual ListServicesResponse ListServices(ListServicesRequest request, CallOptions options)

Lists Services in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesResponse)` | The response received from the server.  
  
### ListServices(ListServicesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListServicesResponse ListServices(ListServicesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Services in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesRequest)`  
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
`[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesResponse)` | The response received from the server.  
  
### ListServicesAsync(ListServicesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListServicesResponse> ListServicesAsync(ListServicesRequest request, CallOptions options)

Lists Services in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesResponse)` | The call object.  
  
### ListServicesAsync(ListServicesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListServicesResponse> ListServicesAsync(ListServicesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Services in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override AgentRegistry.AgentRegistryClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.AgentRegistry)[AgentRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.AgentRegistry.AgentRegistryClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.AgentRegistry.V1.AgentRegistry.AgentRegistryClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### SearchAgents(SearchAgentsRequest, CallOptions)
    
    
    public virtual SearchAgentsResponse SearchAgents(SearchAgentsRequest request, CallOptions options)

Searches Agents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchAgentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchAgentsResponse)` | The response received from the server.  
  
### SearchAgents(SearchAgentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SearchAgentsResponse SearchAgents(SearchAgentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Searches Agents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchAgentsRequest)`  
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
`[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchAgentsResponse)` | The response received from the server.  
  
### SearchAgentsAsync(SearchAgentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SearchAgentsResponse> SearchAgentsAsync(SearchAgentsRequest request, CallOptions options)

Searches Agents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchAgentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchAgentsResponse)` | The call object.  
  
### SearchAgentsAsync(SearchAgentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SearchAgentsResponse> SearchAgentsAsync(SearchAgentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Searches Agents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchAgentsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchAgentsResponse)` | The call object.  
  
### SearchMcpServers(SearchMcpServersRequest, CallOptions)
    
    
    public virtual SearchMcpServersResponse SearchMcpServers(SearchMcpServersRequest request, CallOptions options)

Searches McpServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchMcpServersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchMcpServersResponse)` | The response received from the server.  
  
### SearchMcpServers(SearchMcpServersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SearchMcpServersResponse SearchMcpServers(SearchMcpServersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Searches McpServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchMcpServersRequest)`  
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
`[SearchMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchMcpServersResponse)` | The response received from the server.  
  
### SearchMcpServersAsync(SearchMcpServersRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SearchMcpServersResponse> SearchMcpServersAsync(SearchMcpServersRequest request, CallOptions options)

Searches McpServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchMcpServersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchMcpServersResponse)` | The call object.  
  
### SearchMcpServersAsync(SearchMcpServersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SearchMcpServersResponse> SearchMcpServersAsync(SearchMcpServersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Searches McpServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchMcpServersRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.SearchMcpServersResponse)` | The call object.  
  
### UpdateBinding(UpdateBindingRequest, CallOptions)
    
    
    public virtual Operation UpdateBinding(UpdateBindingRequest request, CallOptions options)

Updates the parameters of a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.UpdateBindingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateBinding(UpdateBindingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateBinding(UpdateBindingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.UpdateBindingRequest)`  
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
  
### UpdateBindingAsync(UpdateBindingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateBindingAsync(UpdateBindingRequest request, CallOptions options)

Updates the parameters of a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.UpdateBindingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateBindingAsync(UpdateBindingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateBindingAsync(UpdateBindingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.UpdateBindingRequest)`  
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
  
### UpdateService(UpdateServiceRequest, CallOptions)
    
    
    public virtual Operation UpdateService(UpdateServiceRequest request, CallOptions options)

Updates the parameters of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.UpdateServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateService(UpdateServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateService(UpdateServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.UpdateServiceRequest)`  
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
  
### UpdateServiceAsync(UpdateServiceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateServiceAsync(UpdateServiceRequest request, CallOptions options)

Updates the parameters of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.UpdateServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateServiceAsync(UpdateServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateServiceAsync(UpdateServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.UpdateServiceRequest)`  
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

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
