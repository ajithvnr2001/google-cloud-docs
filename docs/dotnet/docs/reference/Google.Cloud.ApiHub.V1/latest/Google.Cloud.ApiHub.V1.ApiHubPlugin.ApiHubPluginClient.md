---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubPlugin.ApiHubPluginClient
title: API hub v1 API - Class ApiHubPlugin.ApiHubPluginClient (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:46.852286+00:00
---

# API hub v1 API - Class ApiHubPlugin.ApiHubPluginClient (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubPlugin.ApiHubPluginClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API hub v1 API - Class ApiHubPlugin.ApiHubPluginClient (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubPlugin.ApiHubPluginClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.1.0/Google.Cloud.ApiHub.V1.ApiHubPlugin.ApiHubPluginClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.0.0/Google.Cloud.ApiHub.V1.ApiHubPlugin.ApiHubPluginClient)


    
    
    public class ApiHubPlugin.ApiHubPluginClient : ClientBase<ApiHubPlugin.ApiHubPluginClient>

Reference documentation and code samples for the API hub v1 API class ApiHubPlugin.ApiHubPluginClient.

Client for ApiHubPlugin

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[ApiHubPlugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubPlugin)[ApiHubPluginClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubPlugin.ApiHubPluginClient) > ApiHubPlugin.ApiHubPluginClient

## Inherited Members

[ClientBase<ApiHubPlugin.ApiHubPluginClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1)

## Assembly

Google.Cloud.ApiHub.V1.dll

## Constructors 

### ApiHubPluginClient()
    
    
    protected ApiHubPluginClient()

Protected parameterless constructor to allow creation of test doubles.

### ApiHubPluginClient(CallInvoker)
    
    
    public ApiHubPluginClient(CallInvoker callInvoker)

Creates a new client for ApiHubPlugin that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### ApiHubPluginClient(ChannelBase)
    
    
    public ApiHubPluginClient(ChannelBase channel)

Creates a new client for ApiHubPlugin

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### ApiHubPluginClient(ClientBaseConfiguration)
    
    
    protected ApiHubPluginClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

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
  
### CreatePlugin(CreatePluginRequest, CallOptions)
    
    
    public virtual Plugin CreatePlugin(CreatePluginRequest request, CallOptions options)

Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The response received from the server.  
  
### CreatePlugin(CreatePluginRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Plugin CreatePlugin(CreatePluginRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginRequest)`  
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
`[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The response received from the server.  
  
### CreatePluginAsync(CreatePluginRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Plugin> CreatePluginAsync(CreatePluginRequest request, CallOptions options)

Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The call object.  
  
### CreatePluginAsync(CreatePluginRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Plugin> CreatePluginAsync(CreatePluginRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The call object.  
  
### CreatePluginInstance(CreatePluginInstanceRequest, CallOptions)
    
    
    public virtual Operation CreatePluginInstance(CreatePluginInstanceRequest request, CallOptions options)

Creates a Plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreatePluginInstance(CreatePluginInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreatePluginInstance(CreatePluginInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a Plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest)`  
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
  
### CreatePluginInstanceAsync(CreatePluginInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreatePluginInstanceAsync(CreatePluginInstanceRequest request, CallOptions options)

Creates a Plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreatePluginInstanceAsync(CreatePluginInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreatePluginInstanceAsync(CreatePluginInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a Plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest)`  
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
  
### DeletePlugin(DeletePluginRequest, CallOptions)
    
    
    public virtual Operation DeletePlugin(DeletePluginRequest request, CallOptions options)

Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeletePlugin(DeletePluginRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeletePlugin(DeletePluginRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest)`  
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
  
### DeletePluginAsync(DeletePluginRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeletePluginAsync(DeletePluginRequest request, CallOptions options)

Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeletePluginAsync(DeletePluginRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeletePluginAsync(DeletePluginRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest)`  
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
  
### DeletePluginInstance(DeletePluginInstanceRequest, CallOptions)
    
    
    public virtual Operation DeletePluginInstance(DeletePluginInstanceRequest request, CallOptions options)

Deletes a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeletePluginInstance(DeletePluginInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeletePluginInstance(DeletePluginInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginInstanceRequest)`  
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
  
### DeletePluginInstanceAsync(DeletePluginInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeletePluginInstanceAsync(DeletePluginInstanceRequest request, CallOptions options)

Deletes a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeletePluginInstanceAsync(DeletePluginInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeletePluginInstanceAsync(DeletePluginInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginInstanceRequest)`  
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
  
### DisablePlugin(DisablePluginRequest, CallOptions)
    
    
    public virtual Plugin DisablePlugin(DisablePluginRequest request, CallOptions options)

Disables a plugin. The `state` of the plugin after disabling is `DISABLED`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisablePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DisablePluginRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The response received from the server.  
  
### DisablePlugin(DisablePluginRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Plugin DisablePlugin(DisablePluginRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Disables a plugin. The `state` of the plugin after disabling is `DISABLED`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisablePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DisablePluginRequest)`  
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
`[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The response received from the server.  
  
### DisablePluginAsync(DisablePluginRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Plugin> DisablePluginAsync(DisablePluginRequest request, CallOptions options)

Disables a plugin. The `state` of the plugin after disabling is `DISABLED`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisablePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DisablePluginRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The call object.  
  
### DisablePluginAsync(DisablePluginRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Plugin> DisablePluginAsync(DisablePluginRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Disables a plugin. The `state` of the plugin after disabling is `DISABLED`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisablePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DisablePluginRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The call object.  
  
### DisablePluginInstanceAction(DisablePluginInstanceActionRequest, CallOptions)
    
    
    public virtual Operation DisablePluginInstanceAction(DisablePluginInstanceActionRequest request, CallOptions options)

Disables a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisablePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DisablePluginInstanceActionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DisablePluginInstanceAction(DisablePluginInstanceActionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DisablePluginInstanceAction(DisablePluginInstanceActionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Disables a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisablePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DisablePluginInstanceActionRequest)`  
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
  
### DisablePluginInstanceActionAsync(DisablePluginInstanceActionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DisablePluginInstanceActionAsync(DisablePluginInstanceActionRequest request, CallOptions options)

Disables a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisablePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DisablePluginInstanceActionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DisablePluginInstanceActionAsync(DisablePluginInstanceActionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DisablePluginInstanceActionAsync(DisablePluginInstanceActionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Disables a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisablePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DisablePluginInstanceActionRequest)`  
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
  
### EnablePlugin(EnablePluginRequest, CallOptions)
    
    
    public virtual Plugin EnablePlugin(EnablePluginRequest request, CallOptions options)

Enables a plugin. The `state` of the plugin after enabling is `ENABLED`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnablePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.EnablePluginRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The response received from the server.  
  
### EnablePlugin(EnablePluginRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Plugin EnablePlugin(EnablePluginRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Enables a plugin. The `state` of the plugin after enabling is `ENABLED`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnablePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.EnablePluginRequest)`  
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
`[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The response received from the server.  
  
### EnablePluginAsync(EnablePluginRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Plugin> EnablePluginAsync(EnablePluginRequest request, CallOptions options)

Enables a plugin. The `state` of the plugin after enabling is `ENABLED`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnablePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.EnablePluginRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The call object.  
  
### EnablePluginAsync(EnablePluginRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Plugin> EnablePluginAsync(EnablePluginRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Enables a plugin. The `state` of the plugin after enabling is `ENABLED`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnablePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.EnablePluginRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The call object.  
  
### EnablePluginInstanceAction(EnablePluginInstanceActionRequest, CallOptions)
    
    
    public virtual Operation EnablePluginInstanceAction(EnablePluginInstanceActionRequest request, CallOptions options)

Enables a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnablePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.EnablePluginInstanceActionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### EnablePluginInstanceAction(EnablePluginInstanceActionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation EnablePluginInstanceAction(EnablePluginInstanceActionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Enables a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnablePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.EnablePluginInstanceActionRequest)`  
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
  
### EnablePluginInstanceActionAsync(EnablePluginInstanceActionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> EnablePluginInstanceActionAsync(EnablePluginInstanceActionRequest request, CallOptions options)

Enables a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnablePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.EnablePluginInstanceActionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### EnablePluginInstanceActionAsync(EnablePluginInstanceActionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> EnablePluginInstanceActionAsync(EnablePluginInstanceActionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Enables a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnablePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.EnablePluginInstanceActionRequest)`  
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
  
### ExecutePluginInstanceAction(ExecutePluginInstanceActionRequest, CallOptions)
    
    
    public virtual Operation ExecutePluginInstanceAction(ExecutePluginInstanceActionRequest request, CallOptions options)

Executes a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ExecutePluginInstanceActionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ExecutePluginInstanceAction(ExecutePluginInstanceActionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ExecutePluginInstanceAction(ExecutePluginInstanceActionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Executes a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ExecutePluginInstanceActionRequest)`  
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
  
### ExecutePluginInstanceActionAsync(ExecutePluginInstanceActionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ExecutePluginInstanceActionAsync(ExecutePluginInstanceActionRequest request, CallOptions options)

Executes a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ExecutePluginInstanceActionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ExecutePluginInstanceActionAsync(ExecutePluginInstanceActionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ExecutePluginInstanceActionAsync(ExecutePluginInstanceActionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Executes a plugin instance in the API hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ExecutePluginInstanceActionRequest)`  
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
  
### GetPlugin(GetPluginRequest, CallOptions)
    
    
    public virtual Plugin GetPlugin(GetPluginRequest request, CallOptions options)

Get an API Hub plugin.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetPluginRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The response received from the server.  
  
### GetPlugin(GetPluginRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Plugin GetPlugin(GetPluginRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get an API Hub plugin.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetPluginRequest)`  
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
`[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The response received from the server.  
  
### GetPluginAsync(GetPluginRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Plugin> GetPluginAsync(GetPluginRequest request, CallOptions options)

Get an API Hub plugin.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetPluginRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The call object.  
  
### GetPluginAsync(GetPluginRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Plugin> GetPluginAsync(GetPluginRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get an API Hub plugin.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetPluginRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Plugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Plugin)` | The call object.  
  
### GetPluginInstance(GetPluginInstanceRequest, CallOptions)
    
    
    public virtual PluginInstance GetPluginInstance(GetPluginInstanceRequest request, CallOptions options)

Get an API Hub plugin instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetPluginInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginInstance)` | The response received from the server.  
  
### GetPluginInstance(GetPluginInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual PluginInstance GetPluginInstance(GetPluginInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get an API Hub plugin instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetPluginInstanceRequest)`  
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
`[PluginInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginInstance)` | The response received from the server.  
  
### GetPluginInstanceAsync(GetPluginInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<PluginInstance> GetPluginInstanceAsync(GetPluginInstanceRequest request, CallOptions options)

Get an API Hub plugin instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetPluginInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PluginInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginInstance)` | The call object.  
  
### GetPluginInstanceAsync(GetPluginInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<PluginInstance> GetPluginInstanceAsync(GetPluginInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get an API Hub plugin instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetPluginInstanceRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PluginInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginInstance)` | The call object.  
  
### ListPluginInstances(ListPluginInstancesRequest, CallOptions)
    
    
    public virtual ListPluginInstancesResponse ListPluginInstances(ListPluginInstancesRequest request, CallOptions options)

List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluginInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPluginInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesResponse)` | The response received from the server.  
  
### ListPluginInstances(ListPluginInstancesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListPluginInstancesResponse ListPluginInstances(ListPluginInstancesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluginInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest)`  
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
`[ListPluginInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesResponse)` | The response received from the server.  
  
### ListPluginInstancesAsync(ListPluginInstancesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListPluginInstancesResponse> ListPluginInstancesAsync(ListPluginInstancesRequest request, CallOptions options)

List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluginInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPluginInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesResponse)` | The call object.  
  
### ListPluginInstancesAsync(ListPluginInstancesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListPluginInstancesResponse> ListPluginInstancesAsync(ListPluginInstancesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluginInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPluginInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesResponse)` | The call object.  
  
### ListPlugins(ListPluginsRequest, CallOptions)
    
    
    public virtual ListPluginsResponse ListPlugins(ListPluginsRequest request, CallOptions options)

List all the plugins in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluginsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPluginsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginsResponse)` | The response received from the server.  
  
### ListPlugins(ListPluginsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListPluginsResponse ListPlugins(ListPluginsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List all the plugins in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluginsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginsRequest)`  
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
`[ListPluginsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginsResponse)` | The response received from the server.  
  
### ListPluginsAsync(ListPluginsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListPluginsResponse> ListPluginsAsync(ListPluginsRequest request, CallOptions options)

List all the plugins in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluginsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPluginsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginsResponse)` | The call object.  
  
### ListPluginsAsync(ListPluginsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListPluginsResponse> ListPluginsAsync(ListPluginsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List all the plugins in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluginsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPluginsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override ApiHubPlugin.ApiHubPluginClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubPlugin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubPlugin)[ApiHubPluginClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubPlugin.ApiHubPluginClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.ApiHub.V1.ApiHubPlugin.ApiHubPluginClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdatePluginInstance(UpdatePluginInstanceRequest, CallOptions)
    
    
    public virtual PluginInstance UpdatePluginInstance(UpdatePluginInstanceRequest request, CallOptions options)

Updates a plugin instance in the API hub. The following fields in the [plugin_instance][google.cloud.apihub.v1.PluginInstance] can be updated currently:

  * [display_name][google.cloud.apihub.v1.PluginInstance.display_name]
  * [schedule_cron_expression][PluginInstance.actions.schedule_cron_expression]



The [update_mask][google.cloud.apihub.v1.UpdatePluginInstanceRequest.update_mask] should be used to specify the fields being updated.

To update the [auth_config][google.cloud.apihub.v1.PluginInstance.auth_config] and [additional_config][google.cloud.apihub.v1.PluginInstance.additional_config] of the plugin instance, use the [ApplyPluginInstanceConfig][google.cloud.apihub.v1.ApiHubPlugin.ApplyPluginInstanceConfig] method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.UpdatePluginInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginInstance)` | The response received from the server.  
  
### UpdatePluginInstance(UpdatePluginInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual PluginInstance UpdatePluginInstance(UpdatePluginInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a plugin instance in the API hub. The following fields in the [plugin_instance][google.cloud.apihub.v1.PluginInstance] can be updated currently:

  * [display_name][google.cloud.apihub.v1.PluginInstance.display_name]
  * [schedule_cron_expression][PluginInstance.actions.schedule_cron_expression]



The [update_mask][google.cloud.apihub.v1.UpdatePluginInstanceRequest.update_mask] should be used to specify the fields being updated.

To update the [auth_config][google.cloud.apihub.v1.PluginInstance.auth_config] and [additional_config][google.cloud.apihub.v1.PluginInstance.additional_config] of the plugin instance, use the [ApplyPluginInstanceConfig][google.cloud.apihub.v1.ApiHubPlugin.ApplyPluginInstanceConfig] method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.UpdatePluginInstanceRequest)`  
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
`[PluginInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginInstance)` | The response received from the server.  
  
### UpdatePluginInstanceAsync(UpdatePluginInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<PluginInstance> UpdatePluginInstanceAsync(UpdatePluginInstanceRequest request, CallOptions options)

Updates a plugin instance in the API hub. The following fields in the [plugin_instance][google.cloud.apihub.v1.PluginInstance] can be updated currently:

  * [display_name][google.cloud.apihub.v1.PluginInstance.display_name]
  * [schedule_cron_expression][PluginInstance.actions.schedule_cron_expression]



The [update_mask][google.cloud.apihub.v1.UpdatePluginInstanceRequest.update_mask] should be used to specify the fields being updated.

To update the [auth_config][google.cloud.apihub.v1.PluginInstance.auth_config] and [additional_config][google.cloud.apihub.v1.PluginInstance.additional_config] of the plugin instance, use the [ApplyPluginInstanceConfig][google.cloud.apihub.v1.ApiHubPlugin.ApplyPluginInstanceConfig] method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.UpdatePluginInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PluginInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginInstance)` | The call object.  
  
### UpdatePluginInstanceAsync(UpdatePluginInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<PluginInstance> UpdatePluginInstanceAsync(UpdatePluginInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a plugin instance in the API hub. The following fields in the [plugin_instance][google.cloud.apihub.v1.PluginInstance] can be updated currently:

  * [display_name][google.cloud.apihub.v1.PluginInstance.display_name]
  * [schedule_cron_expression][PluginInstance.actions.schedule_cron_expression]



The [update_mask][google.cloud.apihub.v1.UpdatePluginInstanceRequest.update_mask] should be used to specify the fields being updated.

To update the [auth_config][google.cloud.apihub.v1.PluginInstance.auth_config] and [additional_config][google.cloud.apihub.v1.PluginInstance.additional_config] of the plugin instance, use the [ApplyPluginInstanceConfig][google.cloud.apihub.v1.ApiHubPlugin.ApplyPluginInstanceConfig] method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.UpdatePluginInstanceRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PluginInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginInstance)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
