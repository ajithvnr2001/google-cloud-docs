---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ConfigDelivery.ConfigDeliveryClient
title: Config Delivery v1 API - Class ConfigDelivery.ConfigDeliveryClient (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:50.587357+00:00
---

# Config Delivery v1 API - Class ConfigDelivery.ConfigDeliveryClient (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ConfigDelivery.ConfigDeliveryClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Config Delivery v1 API - Class ConfigDelivery.ConfigDeliveryClient (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public class ConfigDelivery.ConfigDeliveryClient : ClientBase<ConfigDelivery.ConfigDeliveryClient>

Reference documentation and code samples for the Config Delivery v1 API class ConfigDelivery.ConfigDeliveryClient.

Client for ConfigDelivery

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[ConfigDelivery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ConfigDelivery)[ConfigDeliveryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ConfigDelivery.ConfigDeliveryClient) > ConfigDelivery.ConfigDeliveryClient

## Inherited Members

[ClientBase<ConfigDelivery.ConfigDeliveryClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ConfigDelivery.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1)

## Assembly

Google.Cloud.ConfigDelivery.V1.dll

## Constructors 

### ConfigDeliveryClient()
    
    
    protected ConfigDeliveryClient()

Protected parameterless constructor to allow creation of test doubles.

### ConfigDeliveryClient(CallInvoker)
    
    
    public ConfigDeliveryClient(CallInvoker callInvoker)

Creates a new client for ConfigDelivery that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### ConfigDeliveryClient(ChannelBase)
    
    
    public ConfigDeliveryClient(ChannelBase channel)

Creates a new client for ConfigDelivery

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### ConfigDeliveryClient(ClientBaseConfiguration)
    
    
    protected ConfigDeliveryClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### AbortRollout(AbortRolloutRequest, CallOptions)
    
    
    public virtual Operation AbortRollout(AbortRolloutRequest request, CallOptions options)

Abort a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AbortRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.AbortRolloutRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### AbortRollout(AbortRolloutRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation AbortRollout(AbortRolloutRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Abort a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AbortRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.AbortRolloutRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### AbortRolloutAsync(AbortRolloutRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> AbortRolloutAsync(AbortRolloutRequest request, CallOptions options)

Abort a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AbortRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.AbortRolloutRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### AbortRolloutAsync(AbortRolloutRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> AbortRolloutAsync(AbortRolloutRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Abort a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AbortRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.AbortRolloutRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateFleetPackage(CreateFleetPackageRequest, CallOptions)
    
    
    public virtual Operation CreateFleetPackage(CreateFleetPackageRequest request, CallOptions options)

Creates a new FleetPackage in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateFleetPackageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateFleetPackage(CreateFleetPackageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateFleetPackage(CreateFleetPackageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new FleetPackage in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateFleetPackageRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateFleetPackageAsync(CreateFleetPackageRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateFleetPackageAsync(CreateFleetPackageRequest request, CallOptions options)

Creates a new FleetPackage in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateFleetPackageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateFleetPackageAsync(CreateFleetPackageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateFleetPackageAsync(CreateFleetPackageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new FleetPackage in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateFleetPackageRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateLocationsClient()
    
    
    public virtual Locations.LocationsClient CreateLocationsClient()

Creates a new instance of [Locations.LocationsClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Locations](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.html)[LocationsClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html)` | A new [Locations.LocationsClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) for the same target as this client.  
  
### CreateOperationsClient()
    
    
    public virtual Operations.OperationsClient CreateOperationsClient()

Creates a new instance of [Operations.OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### CreateRelease(CreateReleaseRequest, CallOptions)
    
    
    public virtual Operation CreateRelease(CreateReleaseRequest request, CallOptions options)

Creates a new Release in a given project, location and resource bundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateReleaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateRelease(CreateReleaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateRelease(CreateReleaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Release in a given project, location and resource bundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateReleaseRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateReleaseAsync(CreateReleaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateReleaseAsync(CreateReleaseRequest request, CallOptions options)

Creates a new Release in a given project, location and resource bundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateReleaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateReleaseAsync(CreateReleaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateReleaseAsync(CreateReleaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Release in a given project, location and resource bundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateReleaseRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateResourceBundle(CreateResourceBundleRequest, CallOptions)
    
    
    public virtual Operation CreateResourceBundle(CreateResourceBundleRequest request, CallOptions options)

Creates a new ResourceBundle in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateResourceBundleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateResourceBundle(CreateResourceBundleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateResourceBundle(CreateResourceBundleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ResourceBundle in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateResourceBundleRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateResourceBundleAsync(CreateResourceBundleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateResourceBundleAsync(CreateResourceBundleRequest request, CallOptions options)

Creates a new ResourceBundle in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateResourceBundleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateResourceBundleAsync(CreateResourceBundleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateResourceBundleAsync(CreateResourceBundleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ResourceBundle in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateResourceBundleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateVariant(CreateVariantRequest, CallOptions)
    
    
    public virtual Operation CreateVariant(CreateVariantRequest request, CallOptions options)

Creates a new Variant in a given project, location, resource bundle, and release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateVariantRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateVariant(CreateVariantRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateVariant(CreateVariantRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Variant in a given project, location, resource bundle, and release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateVariantRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateVariantAsync(CreateVariantRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateVariantAsync(CreateVariantRequest request, CallOptions options)

Creates a new Variant in a given project, location, resource bundle, and release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateVariantRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateVariantAsync(CreateVariantRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateVariantAsync(CreateVariantRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Variant in a given project, location, resource bundle, and release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.CreateVariantRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteFleetPackage(DeleteFleetPackageRequest, CallOptions)
    
    
    public virtual Operation DeleteFleetPackage(DeleteFleetPackageRequest request, CallOptions options)

Deletes a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteFleetPackageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteFleetPackage(DeleteFleetPackageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteFleetPackage(DeleteFleetPackageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteFleetPackageRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteFleetPackageAsync(DeleteFleetPackageRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFleetPackageAsync(DeleteFleetPackageRequest request, CallOptions options)

Deletes a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteFleetPackageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteFleetPackageAsync(DeleteFleetPackageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFleetPackageAsync(DeleteFleetPackageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteFleetPackageRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteRelease(DeleteReleaseRequest, CallOptions)
    
    
    public virtual Operation DeleteRelease(DeleteReleaseRequest request, CallOptions options)

Deletes a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteReleaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteRelease(DeleteReleaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteRelease(DeleteReleaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteReleaseRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteReleaseAsync(DeleteReleaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteReleaseAsync(DeleteReleaseRequest request, CallOptions options)

Deletes a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteReleaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteReleaseAsync(DeleteReleaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteReleaseAsync(DeleteReleaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteReleaseRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteResourceBundle(DeleteResourceBundleRequest, CallOptions)
    
    
    public virtual Operation DeleteResourceBundle(DeleteResourceBundleRequest request, CallOptions options)

Deletes a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteResourceBundleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteResourceBundle(DeleteResourceBundleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteResourceBundle(DeleteResourceBundleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteResourceBundleRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteResourceBundleAsync(DeleteResourceBundleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteResourceBundleAsync(DeleteResourceBundleRequest request, CallOptions options)

Deletes a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteResourceBundleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteResourceBundleAsync(DeleteResourceBundleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteResourceBundleAsync(DeleteResourceBundleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteResourceBundleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteVariant(DeleteVariantRequest, CallOptions)
    
    
    public virtual Operation DeleteVariant(DeleteVariantRequest request, CallOptions options)

Deletes a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteVariantRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteVariant(DeleteVariantRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteVariant(DeleteVariantRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteVariantRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteVariantAsync(DeleteVariantRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteVariantAsync(DeleteVariantRequest request, CallOptions options)

Deletes a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteVariantRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteVariantAsync(DeleteVariantRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteVariantAsync(DeleteVariantRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeleteVariantRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### GetFleetPackage(GetFleetPackageRequest, CallOptions)
    
    
    public virtual FleetPackage GetFleetPackage(GetFleetPackageRequest request, CallOptions options)

Gets details of a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetFleetPackageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)` | The response received from the server.  
  
### GetFleetPackage(GetFleetPackageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FleetPackage GetFleetPackage(GetFleetPackageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetFleetPackageRequest)`  
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
`[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)` | The response received from the server.  
  
### GetFleetPackageAsync(GetFleetPackageRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FleetPackage> GetFleetPackageAsync(GetFleetPackageRequest request, CallOptions options)

Gets details of a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetFleetPackageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)` | The call object.  
  
### GetFleetPackageAsync(GetFleetPackageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FleetPackage> GetFleetPackageAsync(GetFleetPackageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetFleetPackageRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)` | The call object.  
  
### GetRelease(GetReleaseRequest, CallOptions)
    
    
    public virtual Release GetRelease(GetReleaseRequest request, CallOptions options)

Gets details of a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetReleaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Release)` | The response received from the server.  
  
### GetRelease(GetReleaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Release GetRelease(GetReleaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetReleaseRequest)`  
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
`[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Release)` | The response received from the server.  
  
### GetReleaseAsync(GetReleaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Release> GetReleaseAsync(GetReleaseRequest request, CallOptions options)

Gets details of a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetReleaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Release)` | The call object.  
  
### GetReleaseAsync(GetReleaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Release> GetReleaseAsync(GetReleaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetReleaseRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Release](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Release)` | The call object.  
  
### GetResourceBundle(GetResourceBundleRequest, CallOptions)
    
    
    public virtual ResourceBundle GetResourceBundle(GetResourceBundleRequest request, CallOptions options)

Gets details of a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetResourceBundleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceBundle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundle)` | The response received from the server.  
  
### GetResourceBundle(GetResourceBundleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ResourceBundle GetResourceBundle(GetResourceBundleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetResourceBundleRequest)`  
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
`[ResourceBundle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundle)` | The response received from the server.  
  
### GetResourceBundleAsync(GetResourceBundleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ResourceBundle> GetResourceBundleAsync(GetResourceBundleRequest request, CallOptions options)

Gets details of a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetResourceBundleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ResourceBundle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundle)` | The call object.  
  
### GetResourceBundleAsync(GetResourceBundleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ResourceBundle> GetResourceBundleAsync(GetResourceBundleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetResourceBundleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ResourceBundle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundle)` | The call object.  
  
### GetRollout(GetRolloutRequest, CallOptions)
    
    
    public virtual Rollout GetRollout(GetRolloutRequest request, CallOptions options)

Gets details of a single Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetRolloutRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Rollout)` | The response received from the server.  
  
### GetRollout(GetRolloutRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Rollout GetRollout(GetRolloutRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetRolloutRequest)`  
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
`[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Rollout)` | The response received from the server.  
  
### GetRolloutAsync(GetRolloutRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Rollout> GetRolloutAsync(GetRolloutRequest request, CallOptions options)

Gets details of a single Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetRolloutRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Rollout)` | The call object.  
  
### GetRolloutAsync(GetRolloutRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Rollout> GetRolloutAsync(GetRolloutRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetRolloutRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Rollout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Rollout)` | The call object.  
  
### GetVariant(GetVariantRequest, CallOptions)
    
    
    public virtual Variant GetVariant(GetVariantRequest request, CallOptions options)

Gets details of a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetVariantRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Variant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Variant)` | The response received from the server.  
  
### GetVariant(GetVariantRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Variant GetVariant(GetVariantRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetVariantRequest)`  
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
`[Variant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Variant)` | The response received from the server.  
  
### GetVariantAsync(GetVariantRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Variant> GetVariantAsync(GetVariantRequest request, CallOptions options)

Gets details of a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetVariantRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Variant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Variant)` | The call object.  
  
### GetVariantAsync(GetVariantRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Variant> GetVariantAsync(GetVariantRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.GetVariantRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Variant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.Variant)` | The call object.  
  
### ListFleetPackages(ListFleetPackagesRequest, CallOptions)
    
    
    public virtual ListFleetPackagesResponse ListFleetPackages(ListFleetPackagesRequest request, CallOptions options)

Lists FleetPackages in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFleetPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListFleetPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesResponse)` | The response received from the server.  
  
### ListFleetPackages(ListFleetPackagesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListFleetPackagesResponse ListFleetPackages(ListFleetPackagesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists FleetPackages in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFleetPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesRequest)`  
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
`[ListFleetPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesResponse)` | The response received from the server.  
  
### ListFleetPackagesAsync(ListFleetPackagesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListFleetPackagesResponse> ListFleetPackagesAsync(ListFleetPackagesRequest request, CallOptions options)

Lists FleetPackages in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFleetPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFleetPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesResponse)` | The call object.  
  
### ListFleetPackagesAsync(ListFleetPackagesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListFleetPackagesResponse> ListFleetPackagesAsync(ListFleetPackagesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists FleetPackages in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFleetPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFleetPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListFleetPackagesResponse)` | The call object.  
  
### ListReleases(ListReleasesRequest, CallOptions)
    
    
    public virtual ListReleasesResponse ListReleases(ListReleasesRequest request, CallOptions options)

Lists Releases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListReleasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListReleasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListReleasesResponse)` | The response received from the server.  
  
### ListReleases(ListReleasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListReleasesResponse ListReleases(ListReleasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Releases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListReleasesRequest)`  
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
`[ListReleasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListReleasesResponse)` | The response received from the server.  
  
### ListReleasesAsync(ListReleasesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListReleasesResponse> ListReleasesAsync(ListReleasesRequest request, CallOptions options)

Lists Releases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListReleasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListReleasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListReleasesResponse)` | The call object.  
  
### ListReleasesAsync(ListReleasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListReleasesResponse> ListReleasesAsync(ListReleasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Releases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListReleasesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListReleasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListReleasesResponse)` | The call object.  
  
### ListResourceBundles(ListResourceBundlesRequest, CallOptions)
    
    
    public virtual ListResourceBundlesResponse ListResourceBundles(ListResourceBundlesRequest request, CallOptions options)

Lists ResourceBundles in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceBundlesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListResourceBundlesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListResourceBundlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListResourceBundlesResponse)` | The response received from the server.  
  
### ListResourceBundles(ListResourceBundlesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListResourceBundlesResponse ListResourceBundles(ListResourceBundlesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ResourceBundles in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceBundlesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListResourceBundlesRequest)`  
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
`[ListResourceBundlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListResourceBundlesResponse)` | The response received from the server.  
  
### ListResourceBundlesAsync(ListResourceBundlesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListResourceBundlesResponse> ListResourceBundlesAsync(ListResourceBundlesRequest request, CallOptions options)

Lists ResourceBundles in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceBundlesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListResourceBundlesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListResourceBundlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListResourceBundlesResponse)` | The call object.  
  
### ListResourceBundlesAsync(ListResourceBundlesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListResourceBundlesResponse> ListResourceBundlesAsync(ListResourceBundlesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ResourceBundles in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceBundlesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListResourceBundlesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListResourceBundlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListResourceBundlesResponse)` | The call object.  
  
### ListRollouts(ListRolloutsRequest, CallOptions)
    
    
    public virtual ListRolloutsResponse ListRollouts(ListRolloutsRequest request, CallOptions options)

Lists Rollouts in a given project, location, and Fleet Package.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRolloutsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListRolloutsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRolloutsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListRolloutsResponse)` | The response received from the server.  
  
### ListRollouts(ListRolloutsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListRolloutsResponse ListRollouts(ListRolloutsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Rollouts in a given project, location, and Fleet Package.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRolloutsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListRolloutsRequest)`  
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
`[ListRolloutsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListRolloutsResponse)` | The response received from the server.  
  
### ListRolloutsAsync(ListRolloutsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListRolloutsResponse> ListRolloutsAsync(ListRolloutsRequest request, CallOptions options)

Lists Rollouts in a given project, location, and Fleet Package.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRolloutsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListRolloutsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRolloutsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListRolloutsResponse)` | The call object.  
  
### ListRolloutsAsync(ListRolloutsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListRolloutsResponse> ListRolloutsAsync(ListRolloutsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Rollouts in a given project, location, and Fleet Package.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRolloutsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListRolloutsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRolloutsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListRolloutsResponse)` | The call object.  
  
### ListVariants(ListVariantsRequest, CallOptions)
    
    
    public virtual ListVariantsResponse ListVariants(ListVariantsRequest request, CallOptions options)

Lists Variants in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVariantsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListVariantsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListVariantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListVariantsResponse)` | The response received from the server.  
  
### ListVariants(ListVariantsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListVariantsResponse ListVariants(ListVariantsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Variants in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVariantsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListVariantsRequest)`  
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
`[ListVariantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListVariantsResponse)` | The response received from the server.  
  
### ListVariantsAsync(ListVariantsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListVariantsResponse> ListVariantsAsync(ListVariantsRequest request, CallOptions options)

Lists Variants in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVariantsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListVariantsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListVariantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListVariantsResponse)` | The call object.  
  
### ListVariantsAsync(ListVariantsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListVariantsResponse> ListVariantsAsync(ListVariantsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Variants in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVariantsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListVariantsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListVariantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ListVariantsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override ConfigDelivery.ConfigDeliveryClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConfigDelivery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ConfigDelivery)[ConfigDeliveryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ConfigDelivery.ConfigDeliveryClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.ConfigDelivery.V1.ConfigDelivery.ConfigDeliveryClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### ResumeRollout(ResumeRolloutRequest, CallOptions)
    
    
    public virtual Operation ResumeRollout(ResumeRolloutRequest request, CallOptions options)

Resume a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResumeRolloutRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ResumeRollout(ResumeRolloutRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ResumeRollout(ResumeRolloutRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Resume a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResumeRolloutRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ResumeRolloutAsync(ResumeRolloutRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ResumeRolloutAsync(ResumeRolloutRequest request, CallOptions options)

Resume a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResumeRolloutRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ResumeRolloutAsync(ResumeRolloutRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ResumeRolloutAsync(ResumeRolloutRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Resume a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResumeRolloutRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### SuspendRollout(SuspendRolloutRequest, CallOptions)
    
    
    public virtual Operation SuspendRollout(SuspendRolloutRequest request, CallOptions options)

Suspend a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuspendRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.SuspendRolloutRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### SuspendRollout(SuspendRolloutRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation SuspendRollout(SuspendRolloutRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Suspend a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuspendRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.SuspendRolloutRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### SuspendRolloutAsync(SuspendRolloutRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> SuspendRolloutAsync(SuspendRolloutRequest request, CallOptions options)

Suspend a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuspendRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.SuspendRolloutRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### SuspendRolloutAsync(SuspendRolloutRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> SuspendRolloutAsync(SuspendRolloutRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Suspend a Rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuspendRolloutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.SuspendRolloutRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateFleetPackage(UpdateFleetPackageRequest, CallOptions)
    
    
    public virtual Operation UpdateFleetPackage(UpdateFleetPackageRequest request, CallOptions options)

Updates the parameters of a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateFleetPackageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateFleetPackage(UpdateFleetPackageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateFleetPackage(UpdateFleetPackageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateFleetPackageRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateFleetPackageAsync(UpdateFleetPackageRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateFleetPackageAsync(UpdateFleetPackageRequest request, CallOptions options)

Updates the parameters of a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateFleetPackageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateFleetPackageAsync(UpdateFleetPackageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateFleetPackageAsync(UpdateFleetPackageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single FleetPackage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateFleetPackageRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateRelease(UpdateReleaseRequest, CallOptions)
    
    
    public virtual Operation UpdateRelease(UpdateReleaseRequest request, CallOptions options)

Updates the parameters of a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateReleaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateRelease(UpdateReleaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateRelease(UpdateReleaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateReleaseRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateReleaseAsync(UpdateReleaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateReleaseAsync(UpdateReleaseRequest request, CallOptions options)

Updates the parameters of a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateReleaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateReleaseAsync(UpdateReleaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateReleaseAsync(UpdateReleaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Release.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateReleaseRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateResourceBundle(UpdateResourceBundleRequest, CallOptions)
    
    
    public virtual Operation UpdateResourceBundle(UpdateResourceBundleRequest request, CallOptions options)

Updates the parameters of a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateResourceBundleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateResourceBundle(UpdateResourceBundleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateResourceBundle(UpdateResourceBundleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateResourceBundleRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateResourceBundleAsync(UpdateResourceBundleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateResourceBundleAsync(UpdateResourceBundleRequest request, CallOptions options)

Updates the parameters of a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateResourceBundleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateResourceBundleAsync(UpdateResourceBundleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateResourceBundleAsync(UpdateResourceBundleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single ResourceBundle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateResourceBundleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateResourceBundleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateVariant(UpdateVariantRequest, CallOptions)
    
    
    public virtual Operation UpdateVariant(UpdateVariantRequest request, CallOptions options)

Updates the parameters of a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateVariantRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateVariant(UpdateVariantRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateVariant(UpdateVariantRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateVariantRequest)`  
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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateVariantAsync(UpdateVariantRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateVariantAsync(UpdateVariantRequest request, CallOptions options)

Updates the parameters of a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateVariantRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateVariantAsync(UpdateVariantRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateVariantAsync(UpdateVariantRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Variant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.UpdateVariantRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
