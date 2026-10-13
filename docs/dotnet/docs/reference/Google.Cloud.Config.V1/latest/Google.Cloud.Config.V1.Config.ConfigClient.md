---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Config.ConfigClient
title: Infrastructure Manager v1 API - Class Config.ConfigClient (1.13.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:55.211668+00:00
---

# Infrastructure Manager v1 API - Class Config.ConfigClient (1.13.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Config.ConfigClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Infrastructure Manager v1 API - Class Config.ConfigClient (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.0 (latest)  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public class Config.ConfigClient : ClientBase<Config.ConfigClient>

Reference documentation and code samples for the Infrastructure Manager v1 API class Config.ConfigClient.

Client for Config

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Config)[ConfigClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Config.ConfigClient) > Config.ConfigClient

## Inherited Members

[ClientBase<Config.ConfigClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Config.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1)

## Assembly

Google.Cloud.Config.V1.dll

## Constructors 

### ConfigClient()
    
    
    protected ConfigClient()

Protected parameterless constructor to allow creation of test doubles.

### ConfigClient(CallInvoker)
    
    
    public ConfigClient(CallInvoker callInvoker)

Creates a new client for Config that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### ConfigClient(ChannelBase)
    
    
    public ConfigClient(ChannelBase channel)

Creates a new client for Config

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### ConfigClient(ClientBaseConfiguration)
    
    
    protected ConfigClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateDeployment(CreateDeploymentRequest, CallOptions)
    
    
    public virtual Operation CreateDeployment(CreateDeploymentRequest request, CallOptions options)

Creates a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateDeployment(CreateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateDeployment(CreateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreateDeploymentRequest)`  
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
  
### CreateDeploymentAsync(CreateDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateDeploymentAsync(CreateDeploymentRequest request, CallOptions options)

Creates a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateDeploymentAsync(CreateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateDeploymentAsync(CreateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreateDeploymentRequest)`  
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
  
### CreateDeploymentGroup(CreateDeploymentGroupRequest, CallOptions)
    
    
    public virtual Operation CreateDeploymentGroup(CreateDeploymentGroupRequest request, CallOptions options)

Creates a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] The newly created DeploymentGroup will be in the `CREATING` state and can be retrieved via Get and List calls.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreateDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateDeploymentGroup(CreateDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateDeploymentGroup(CreateDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] The newly created DeploymentGroup will be in the `CREATING` state and can be retrieved via Get and List calls.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreateDeploymentGroupRequest)`  
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
  
### CreateDeploymentGroupAsync(CreateDeploymentGroupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateDeploymentGroupAsync(CreateDeploymentGroupRequest request, CallOptions options)

Creates a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] The newly created DeploymentGroup will be in the `CREATING` state and can be retrieved via Get and List calls.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreateDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateDeploymentGroupAsync(CreateDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateDeploymentGroupAsync(CreateDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] The newly created DeploymentGroup will be in the `CREATING` state and can be retrieved via Get and List calls.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreateDeploymentGroupRequest)`  
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
  
### CreatePreview(CreatePreviewRequest, CallOptions)
    
    
    public virtual Operation CreatePreview(CreatePreviewRequest request, CallOptions options)

Creates a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreatePreviewRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreatePreview(CreatePreviewRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreatePreview(CreatePreviewRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreatePreviewRequest)`  
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
  
### CreatePreviewAsync(CreatePreviewRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreatePreviewAsync(CreatePreviewRequest request, CallOptions options)

Creates a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreatePreviewRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreatePreviewAsync(CreatePreviewRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreatePreviewAsync(CreatePreviewRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.CreatePreviewRequest)`  
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
  
### DeleteDeployment(DeleteDeploymentRequest, CallOptions)
    
    
    public virtual Operation DeleteDeployment(DeleteDeploymentRequest request, CallOptions options)

Deletes a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteDeployment(DeleteDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteDeployment(DeleteDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteDeploymentRequest)`  
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
  
### DeleteDeploymentAsync(DeleteDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteDeploymentAsync(DeleteDeploymentRequest request, CallOptions options)

Deletes a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteDeploymentAsync(DeleteDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteDeploymentAsync(DeleteDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteDeploymentRequest)`  
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
  
### DeleteDeploymentGroup(DeleteDeploymentGroupRequest, CallOptions)
    
    
    public virtual Operation DeleteDeploymentGroup(DeleteDeploymentGroupRequest request, CallOptions options)

Deletes a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteDeploymentGroup(DeleteDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteDeploymentGroup(DeleteDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteDeploymentGroupRequest)`  
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
  
### DeleteDeploymentGroupAsync(DeleteDeploymentGroupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteDeploymentGroupAsync(DeleteDeploymentGroupRequest request, CallOptions options)

Deletes a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteDeploymentGroupAsync(DeleteDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteDeploymentGroupAsync(DeleteDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteDeploymentGroupRequest)`  
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
  
### DeletePreview(DeletePreviewRequest, CallOptions)
    
    
    public virtual Operation DeletePreview(DeletePreviewRequest request, CallOptions options)

Deletes a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeletePreviewRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeletePreview(DeletePreviewRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeletePreview(DeletePreviewRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeletePreviewRequest)`  
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
  
### DeletePreviewAsync(DeletePreviewRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeletePreviewAsync(DeletePreviewRequest request, CallOptions options)

Deletes a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeletePreviewRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeletePreviewAsync(DeletePreviewRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeletePreviewAsync(DeletePreviewRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeletePreviewRequest)`  
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
  
### DeleteStatefile(DeleteStatefileRequest, CallOptions)
    
    
    public virtual Empty DeleteStatefile(DeleteStatefileRequest request, CallOptions options)

Deletes Terraform state file in a given deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteStatefile(DeleteStatefileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteStatefile(DeleteStatefileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes Terraform state file in a given deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest)`  
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
  
### DeleteStatefileAsync(DeleteStatefileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteStatefileAsync(DeleteStatefileRequest request, CallOptions options)

Deletes Terraform state file in a given deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteStatefileAsync(DeleteStatefileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteStatefileAsync(DeleteStatefileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes Terraform state file in a given deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest)`  
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
  
### DeprovisionDeploymentGroup(DeprovisionDeploymentGroupRequest, CallOptions)
    
    
    public virtual Operation DeprovisionDeploymentGroup(DeprovisionDeploymentGroupRequest request, CallOptions options)

Deprovisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision] but are _no longer_ included in the _current_ [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeprovisionDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeprovisionDeploymentGroup(DeprovisionDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeprovisionDeploymentGroup(DeprovisionDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deprovisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision] but are _no longer_ included in the _current_ [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeprovisionDeploymentGroupRequest)`  
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
  
### DeprovisionDeploymentGroupAsync(DeprovisionDeploymentGroupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeprovisionDeploymentGroupAsync(DeprovisionDeploymentGroupRequest request, CallOptions options)

Deprovisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision] but are _no longer_ included in the _current_ [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeprovisionDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeprovisionDeploymentGroupAsync(DeprovisionDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeprovisionDeploymentGroupAsync(DeprovisionDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deprovisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision] but are _no longer_ included in the _current_ [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeprovisionDeploymentGroupRequest)`  
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
  
### ExportDeploymentStatefile(ExportDeploymentStatefileRequest, CallOptions)
    
    
    public virtual Statefile ExportDeploymentStatefile(ExportDeploymentStatefileRequest request, CallOptions options)

Exports Terraform state file from a given deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDeploymentStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportDeploymentStatefileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The response received from the server.  
  
### ExportDeploymentStatefile(ExportDeploymentStatefileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Statefile ExportDeploymentStatefile(ExportDeploymentStatefileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Exports Terraform state file from a given deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDeploymentStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportDeploymentStatefileRequest)`  
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
`[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The response received from the server.  
  
### ExportDeploymentStatefileAsync(ExportDeploymentStatefileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Statefile> ExportDeploymentStatefileAsync(ExportDeploymentStatefileRequest request, CallOptions options)

Exports Terraform state file from a given deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDeploymentStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportDeploymentStatefileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The call object.  
  
### ExportDeploymentStatefileAsync(ExportDeploymentStatefileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Statefile> ExportDeploymentStatefileAsync(ExportDeploymentStatefileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Exports Terraform state file from a given deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDeploymentStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportDeploymentStatefileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The call object.  
  
### ExportLockInfo(ExportLockInfoRequest, CallOptions)
    
    
    public virtual LockInfo ExportLockInfo(ExportLockInfoRequest request, CallOptions options)

Exports the lock info on a locked deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportLockInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportLockInfoRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[LockInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.LockInfo)` | The response received from the server.  
  
### ExportLockInfo(ExportLockInfoRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual LockInfo ExportLockInfo(ExportLockInfoRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Exports the lock info on a locked deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportLockInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportLockInfoRequest)`  
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
`[LockInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.LockInfo)` | The response received from the server.  
  
### ExportLockInfoAsync(ExportLockInfoRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<LockInfo> ExportLockInfoAsync(ExportLockInfoRequest request, CallOptions options)

Exports the lock info on a locked deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportLockInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportLockInfoRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[LockInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.LockInfo)` | The call object.  
  
### ExportLockInfoAsync(ExportLockInfoRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<LockInfo> ExportLockInfoAsync(ExportLockInfoRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Exports the lock info on a locked deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportLockInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportLockInfoRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[LockInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.LockInfo)` | The call object.  
  
### ExportPreviewResult(ExportPreviewResultRequest, CallOptions)
    
    
    public virtual ExportPreviewResultResponse ExportPreviewResult(ExportPreviewResultRequest request, CallOptions options)

Export [Preview][google.cloud.config.v1.Preview] results.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportPreviewResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ExportPreviewResultResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultResponse)` | The response received from the server.  
  
### ExportPreviewResult(ExportPreviewResultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ExportPreviewResultResponse ExportPreviewResult(ExportPreviewResultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Export [Preview][google.cloud.config.v1.Preview] results.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportPreviewResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest)`  
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
`[ExportPreviewResultResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultResponse)` | The response received from the server.  
  
### ExportPreviewResultAsync(ExportPreviewResultRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ExportPreviewResultResponse> ExportPreviewResultAsync(ExportPreviewResultRequest request, CallOptions options)

Export [Preview][google.cloud.config.v1.Preview] results.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportPreviewResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ExportPreviewResultResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultResponse)` | The call object.  
  
### ExportPreviewResultAsync(ExportPreviewResultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ExportPreviewResultResponse> ExportPreviewResultAsync(ExportPreviewResultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Export [Preview][google.cloud.config.v1.Preview] results.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportPreviewResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ExportPreviewResultResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultResponse)` | The call object.  
  
### ExportRevisionStatefile(ExportRevisionStatefileRequest, CallOptions)
    
    
    public virtual Statefile ExportRevisionStatefile(ExportRevisionStatefileRequest request, CallOptions options)

Exports Terraform state file from a given revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportRevisionStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportRevisionStatefileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The response received from the server.  
  
### ExportRevisionStatefile(ExportRevisionStatefileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Statefile ExportRevisionStatefile(ExportRevisionStatefileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Exports Terraform state file from a given revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportRevisionStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportRevisionStatefileRequest)`  
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
`[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The response received from the server.  
  
### ExportRevisionStatefileAsync(ExportRevisionStatefileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Statefile> ExportRevisionStatefileAsync(ExportRevisionStatefileRequest request, CallOptions options)

Exports Terraform state file from a given revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportRevisionStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportRevisionStatefileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The call object.  
  
### ExportRevisionStatefileAsync(ExportRevisionStatefileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Statefile> ExportRevisionStatefileAsync(ExportRevisionStatefileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Exports Terraform state file from a given revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportRevisionStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportRevisionStatefileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The call object.  
  
### GetAutoMigrationConfig(GetAutoMigrationConfigRequest, CallOptions)
    
    
    public virtual AutoMigrationConfig GetAutoMigrationConfig(GetAutoMigrationConfigRequest request, CallOptions options)

Get the AutoMigrationConfig for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutoMigrationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetAutoMigrationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMigrationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.AutoMigrationConfig)` | The response received from the server.  
  
### GetAutoMigrationConfig(GetAutoMigrationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AutoMigrationConfig GetAutoMigrationConfig(GetAutoMigrationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get the AutoMigrationConfig for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutoMigrationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetAutoMigrationConfigRequest)`  
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
`[AutoMigrationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.AutoMigrationConfig)` | The response received from the server.  
  
### GetAutoMigrationConfigAsync(GetAutoMigrationConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AutoMigrationConfig> GetAutoMigrationConfigAsync(GetAutoMigrationConfigRequest request, CallOptions options)

Get the AutoMigrationConfig for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutoMigrationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetAutoMigrationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AutoMigrationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.AutoMigrationConfig)` | The call object.  
  
### GetAutoMigrationConfigAsync(GetAutoMigrationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AutoMigrationConfig> GetAutoMigrationConfigAsync(GetAutoMigrationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get the AutoMigrationConfig for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutoMigrationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetAutoMigrationConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AutoMigrationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.AutoMigrationConfig)` | The call object.  
  
### GetDeployment(GetDeploymentRequest, CallOptions)
    
    
    public virtual Deployment GetDeployment(GetDeploymentRequest request, CallOptions options)

Gets details about a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Deployment)` | The response received from the server.  
  
### GetDeployment(GetDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Deployment GetDeployment(GetDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentRequest)`  
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
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Deployment)` | The response received from the server.  
  
### GetDeploymentAsync(GetDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Deployment> GetDeploymentAsync(GetDeploymentRequest request, CallOptions options)

Gets details about a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Deployment)` | The call object.  
  
### GetDeploymentAsync(GetDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Deployment> GetDeploymentAsync(GetDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Deployment)` | The call object.  
  
### GetDeploymentGroup(GetDeploymentGroupRequest, CallOptions)
    
    
    public virtual DeploymentGroup GetDeploymentGroup(GetDeploymentGroupRequest request, CallOptions options)

Get a DeploymentGroup for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentGroup)` | The response received from the server.  
  
### GetDeploymentGroup(GetDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DeploymentGroup GetDeploymentGroup(GetDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a DeploymentGroup for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentGroupRequest)`  
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
`[DeploymentGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentGroup)` | The response received from the server.  
  
### GetDeploymentGroupAsync(GetDeploymentGroupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DeploymentGroup> GetDeploymentGroupAsync(GetDeploymentGroupRequest request, CallOptions options)

Get a DeploymentGroup for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeploymentGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentGroup)` | The call object.  
  
### GetDeploymentGroupAsync(GetDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DeploymentGroup> GetDeploymentGroupAsync(GetDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a DeploymentGroup for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentGroupRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeploymentGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentGroup)` | The call object.  
  
### GetDeploymentGroupRevision(GetDeploymentGroupRevisionRequest, CallOptions)
    
    
    public virtual DeploymentGroupRevision GetDeploymentGroupRevision(GetDeploymentGroupRevisionRequest request, CallOptions options)

Gets details about a [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentGroupRevisionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentGroupRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentGroupRevision)` | The response received from the server.  
  
### GetDeploymentGroupRevision(GetDeploymentGroupRevisionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DeploymentGroupRevision GetDeploymentGroupRevision(GetDeploymentGroupRevisionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentGroupRevisionRequest)`  
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
`[DeploymentGroupRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentGroupRevision)` | The response received from the server.  
  
### GetDeploymentGroupRevisionAsync(GetDeploymentGroupRevisionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DeploymentGroupRevision> GetDeploymentGroupRevisionAsync(GetDeploymentGroupRevisionRequest request, CallOptions options)

Gets details about a [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentGroupRevisionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeploymentGroupRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentGroupRevision)` | The call object.  
  
### GetDeploymentGroupRevisionAsync(GetDeploymentGroupRevisionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DeploymentGroupRevision> GetDeploymentGroupRevisionAsync(GetDeploymentGroupRevisionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetDeploymentGroupRevisionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeploymentGroupRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentGroupRevision)` | The call object.  
  
### GetPreview(GetPreviewRequest, CallOptions)
    
    
    public virtual Preview GetPreview(GetPreviewRequest request, CallOptions options)

Gets details about a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetPreviewRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)` | The response received from the server.  
  
### GetPreview(GetPreviewRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Preview GetPreview(GetPreviewRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetPreviewRequest)`  
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
`[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)` | The response received from the server.  
  
### GetPreviewAsync(GetPreviewRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Preview> GetPreviewAsync(GetPreviewRequest request, CallOptions options)

Gets details about a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetPreviewRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)` | The call object.  
  
### GetPreviewAsync(GetPreviewRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Preview> GetPreviewAsync(GetPreviewRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [Preview][google.cloud.config.v1.Preview].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetPreviewRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)` | The call object.  
  
### GetResource(GetResourceRequest, CallOptions)
    
    
    public virtual Resource GetResource(GetResourceRequest request, CallOptions options)

Gets details about a [Resource][google.cloud.config.v1.Resource] deployed by Infra Manager.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Resource)` | The response received from the server.  
  
### GetResource(GetResourceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Resource GetResource(GetResourceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [Resource][google.cloud.config.v1.Resource] deployed by Infra Manager.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceRequest)`  
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
`[Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Resource)` | The response received from the server.  
  
### GetResourceAsync(GetResourceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Resource> GetResourceAsync(GetResourceRequest request, CallOptions options)

Gets details about a [Resource][google.cloud.config.v1.Resource] deployed by Infra Manager.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Resource)` | The call object.  
  
### GetResourceAsync(GetResourceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Resource> GetResourceAsync(GetResourceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [Resource][google.cloud.config.v1.Resource] deployed by Infra Manager.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Resource)` | The call object.  
  
### GetResourceChange(GetResourceChangeRequest, CallOptions)
    
    
    public virtual ResourceChange GetResourceChange(GetResourceChangeRequest request, CallOptions options)

Get a ResourceChange for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceChangeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ResourceChange)` | The response received from the server.  
  
### GetResourceChange(GetResourceChangeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ResourceChange GetResourceChange(GetResourceChangeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a ResourceChange for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceChangeRequest)`  
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
`[ResourceChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ResourceChange)` | The response received from the server.  
  
### GetResourceChangeAsync(GetResourceChangeRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ResourceChange> GetResourceChangeAsync(GetResourceChangeRequest request, CallOptions options)

Get a ResourceChange for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceChangeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ResourceChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ResourceChange)` | The call object.  
  
### GetResourceChangeAsync(GetResourceChangeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ResourceChange> GetResourceChangeAsync(GetResourceChangeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a ResourceChange for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceChangeRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ResourceChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ResourceChange)` | The call object.  
  
### GetResourceDrift(GetResourceDriftRequest, CallOptions)
    
    
    public virtual ResourceDrift GetResourceDrift(GetResourceDriftRequest request, CallOptions options)

Get a ResourceDrift for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceDriftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceDriftRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceDrift](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ResourceDrift)` | The response received from the server.  
  
### GetResourceDrift(GetResourceDriftRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ResourceDrift GetResourceDrift(GetResourceDriftRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a ResourceDrift for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceDriftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceDriftRequest)`  
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
`[ResourceDrift](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ResourceDrift)` | The response received from the server.  
  
### GetResourceDriftAsync(GetResourceDriftRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ResourceDrift> GetResourceDriftAsync(GetResourceDriftRequest request, CallOptions options)

Get a ResourceDrift for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceDriftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceDriftRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ResourceDrift](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ResourceDrift)` | The call object.  
  
### GetResourceDriftAsync(GetResourceDriftRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ResourceDrift> GetResourceDriftAsync(GetResourceDriftRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a ResourceDrift for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceDriftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetResourceDriftRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ResourceDrift](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ResourceDrift)` | The call object.  
  
### GetRevision(GetRevisionRequest, CallOptions)
    
    
    public virtual Revision GetRevision(GetRevisionRequest request, CallOptions options)

Gets details about a [Revision][google.cloud.config.v1.Revision].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetRevisionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Revision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Revision)` | The response received from the server.  
  
### GetRevision(GetRevisionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Revision GetRevision(GetRevisionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [Revision][google.cloud.config.v1.Revision].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetRevisionRequest)`  
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
`[Revision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Revision)` | The response received from the server.  
  
### GetRevisionAsync(GetRevisionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Revision> GetRevisionAsync(GetRevisionRequest request, CallOptions options)

Gets details about a [Revision][google.cloud.config.v1.Revision].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetRevisionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Revision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Revision)` | The call object.  
  
### GetRevisionAsync(GetRevisionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Revision> GetRevisionAsync(GetRevisionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [Revision][google.cloud.config.v1.Revision].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetRevisionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Revision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Revision)` | The call object.  
  
### GetTerraformVersion(GetTerraformVersionRequest, CallOptions)
    
    
    public virtual TerraformVersion GetTerraformVersion(GetTerraformVersionRequest request, CallOptions options)

Gets details about a [TerraformVersion][google.cloud.config.v1.TerraformVersion].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTerraformVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetTerraformVersionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[TerraformVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.TerraformVersion)` | The response received from the server.  
  
### GetTerraformVersion(GetTerraformVersionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual TerraformVersion GetTerraformVersion(GetTerraformVersionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [TerraformVersion][google.cloud.config.v1.TerraformVersion].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTerraformVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetTerraformVersionRequest)`  
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
`[TerraformVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.TerraformVersion)` | The response received from the server.  
  
### GetTerraformVersionAsync(GetTerraformVersionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<TerraformVersion> GetTerraformVersionAsync(GetTerraformVersionRequest request, CallOptions options)

Gets details about a [TerraformVersion][google.cloud.config.v1.TerraformVersion].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTerraformVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetTerraformVersionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TerraformVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.TerraformVersion)` | The call object.  
  
### GetTerraformVersionAsync(GetTerraformVersionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<TerraformVersion> GetTerraformVersionAsync(GetTerraformVersionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details about a [TerraformVersion][google.cloud.config.v1.TerraformVersion].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTerraformVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.GetTerraformVersionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TerraformVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.TerraformVersion)` | The call object.  
  
### ImportStatefile(ImportStatefileRequest, CallOptions)
    
    
    public virtual Statefile ImportStatefile(ImportStatefileRequest request, CallOptions options)

Imports Terraform state file in a given deployment. The state file does not take effect until the Deployment has been unlocked.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ImportStatefileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The response received from the server.  
  
### ImportStatefile(ImportStatefileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Statefile ImportStatefile(ImportStatefileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Imports Terraform state file in a given deployment. The state file does not take effect until the Deployment has been unlocked.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ImportStatefileRequest)`  
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
`[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The response received from the server.  
  
### ImportStatefileAsync(ImportStatefileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Statefile> ImportStatefileAsync(ImportStatefileRequest request, CallOptions options)

Imports Terraform state file in a given deployment. The state file does not take effect until the Deployment has been unlocked.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ImportStatefileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The call object.  
  
### ImportStatefileAsync(ImportStatefileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Statefile> ImportStatefileAsync(ImportStatefileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Imports Terraform state file in a given deployment. The state file does not take effect until the Deployment has been unlocked.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ImportStatefileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Statefile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Statefile)` | The call object.  
  
### ListDeploymentGroupRevisions(ListDeploymentGroupRevisionsRequest, CallOptions)
    
    
    public virtual ListDeploymentGroupRevisionsResponse ListDeploymentGroupRevisions(ListDeploymentGroupRevisionsRequest request, CallOptions options)

Lists [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision]s in a given [DeploymentGroup][google.cloud.config.v1.DeploymentGroup].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupRevisionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupRevisionsResponse)` | The response received from the server.  
  
### ListDeploymentGroupRevisions(ListDeploymentGroupRevisionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDeploymentGroupRevisionsResponse ListDeploymentGroupRevisions(ListDeploymentGroupRevisionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision]s in a given [DeploymentGroup][google.cloud.config.v1.DeploymentGroup].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupRevisionsRequest)`  
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
`[ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupRevisionsResponse)` | The response received from the server.  
  
### ListDeploymentGroupRevisionsAsync(ListDeploymentGroupRevisionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDeploymentGroupRevisionsResponse> ListDeploymentGroupRevisionsAsync(ListDeploymentGroupRevisionsRequest request, CallOptions options)

Lists [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision]s in a given [DeploymentGroup][google.cloud.config.v1.DeploymentGroup].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupRevisionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupRevisionsResponse)` | The call object.  
  
### ListDeploymentGroupRevisionsAsync(ListDeploymentGroupRevisionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDeploymentGroupRevisionsResponse> ListDeploymentGroupRevisionsAsync(ListDeploymentGroupRevisionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision]s in a given [DeploymentGroup][google.cloud.config.v1.DeploymentGroup].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupRevisionsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupRevisionsResponse)` | The call object.  
  
### ListDeploymentGroups(ListDeploymentGroupsRequest, CallOptions)
    
    
    public virtual ListDeploymentGroupsResponse ListDeploymentGroups(ListDeploymentGroupsRequest request, CallOptions options)

List DeploymentGroups for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeploymentGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupsResponse)` | The response received from the server.  
  
### ListDeploymentGroups(ListDeploymentGroupsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDeploymentGroupsResponse ListDeploymentGroups(ListDeploymentGroupsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List DeploymentGroups for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupsRequest)`  
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
`[ListDeploymentGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupsResponse)` | The response received from the server.  
  
### ListDeploymentGroupsAsync(ListDeploymentGroupsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDeploymentGroupsResponse> ListDeploymentGroupsAsync(ListDeploymentGroupsRequest request, CallOptions options)

List DeploymentGroups for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDeploymentGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupsResponse)` | The call object.  
  
### ListDeploymentGroupsAsync(ListDeploymentGroupsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDeploymentGroupsResponse> ListDeploymentGroupsAsync(ListDeploymentGroupsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List DeploymentGroups for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDeploymentGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentGroupsResponse)` | The call object.  
  
### ListDeployments(ListDeploymentsRequest, CallOptions)
    
    
    public virtual ListDeploymentsResponse ListDeployments(ListDeploymentsRequest request, CallOptions options)

Lists [Deployment][google.cloud.config.v1.Deployment]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentsResponse)` | The response received from the server.  
  
### ListDeployments(ListDeploymentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDeploymentsResponse ListDeployments(ListDeploymentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Deployment][google.cloud.config.v1.Deployment]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentsRequest)`  
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
`[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentsResponse)` | The response received from the server.  
  
### ListDeploymentsAsync(ListDeploymentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDeploymentsResponse> ListDeploymentsAsync(ListDeploymentsRequest request, CallOptions options)

Lists [Deployment][google.cloud.config.v1.Deployment]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentsResponse)` | The call object.  
  
### ListDeploymentsAsync(ListDeploymentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDeploymentsResponse> ListDeploymentsAsync(ListDeploymentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Deployment][google.cloud.config.v1.Deployment]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListDeploymentsResponse)` | The call object.  
  
### ListPreviews(ListPreviewsRequest, CallOptions)
    
    
    public virtual ListPreviewsResponse ListPreviews(ListPreviewsRequest request, CallOptions options)

Lists [Preview][google.cloud.config.v1.Preview]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPreviewsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPreviewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsResponse)` | The response received from the server.  
  
### ListPreviews(ListPreviewsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListPreviewsResponse ListPreviews(ListPreviewsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Preview][google.cloud.config.v1.Preview]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPreviewsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsRequest)`  
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
`[ListPreviewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsResponse)` | The response received from the server.  
  
### ListPreviewsAsync(ListPreviewsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListPreviewsResponse> ListPreviewsAsync(ListPreviewsRequest request, CallOptions options)

Lists [Preview][google.cloud.config.v1.Preview]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPreviewsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPreviewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsResponse)` | The call object.  
  
### ListPreviewsAsync(ListPreviewsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListPreviewsResponse> ListPreviewsAsync(ListPreviewsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Preview][google.cloud.config.v1.Preview]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPreviewsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPreviewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsResponse)` | The call object.  
  
### ListResourceChanges(ListResourceChangesRequest, CallOptions)
    
    
    public virtual ListResourceChangesResponse ListResourceChanges(ListResourceChangesRequest request, CallOptions options)

Lists ResourceChanges for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceChangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListResourceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceChangesResponse)` | The response received from the server.  
  
### ListResourceChanges(ListResourceChangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListResourceChangesResponse ListResourceChanges(ListResourceChangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ResourceChanges for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceChangesRequest)`  
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
`[ListResourceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceChangesResponse)` | The response received from the server.  
  
### ListResourceChangesAsync(ListResourceChangesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListResourceChangesResponse> ListResourceChangesAsync(ListResourceChangesRequest request, CallOptions options)

Lists ResourceChanges for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceChangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListResourceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceChangesResponse)` | The call object.  
  
### ListResourceChangesAsync(ListResourceChangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListResourceChangesResponse> ListResourceChangesAsync(ListResourceChangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ResourceChanges for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceChangesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListResourceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceChangesResponse)` | The call object.  
  
### ListResourceDrifts(ListResourceDriftsRequest, CallOptions)
    
    
    public virtual ListResourceDriftsResponse ListResourceDrifts(ListResourceDriftsRequest request, CallOptions options)

List ResourceDrifts for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceDriftsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceDriftsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListResourceDriftsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceDriftsResponse)` | The response received from the server.  
  
### ListResourceDrifts(ListResourceDriftsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListResourceDriftsResponse ListResourceDrifts(ListResourceDriftsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List ResourceDrifts for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceDriftsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceDriftsRequest)`  
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
`[ListResourceDriftsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceDriftsResponse)` | The response received from the server.  
  
### ListResourceDriftsAsync(ListResourceDriftsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListResourceDriftsResponse> ListResourceDriftsAsync(ListResourceDriftsRequest request, CallOptions options)

List ResourceDrifts for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceDriftsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceDriftsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListResourceDriftsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceDriftsResponse)` | The call object.  
  
### ListResourceDriftsAsync(ListResourceDriftsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListResourceDriftsResponse> ListResourceDriftsAsync(ListResourceDriftsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List ResourceDrifts for a given preview.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceDriftsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceDriftsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListResourceDriftsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourceDriftsResponse)` | The call object.  
  
### ListResources(ListResourcesRequest, CallOptions)
    
    
    public virtual ListResourcesResponse ListResources(ListResourcesRequest request, CallOptions options)

Lists [Resources][google.cloud.config.v1.Resource] in a given revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourcesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourcesResponse)` | The response received from the server.  
  
### ListResources(ListResourcesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListResourcesResponse ListResources(ListResourcesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Resources][google.cloud.config.v1.Resource] in a given revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourcesRequest)`  
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
`[ListResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourcesResponse)` | The response received from the server.  
  
### ListResourcesAsync(ListResourcesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListResourcesResponse> ListResourcesAsync(ListResourcesRequest request, CallOptions options)

Lists [Resources][google.cloud.config.v1.Resource] in a given revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourcesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourcesResponse)` | The call object.  
  
### ListResourcesAsync(ListResourcesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListResourcesResponse> ListResourcesAsync(ListResourcesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Resources][google.cloud.config.v1.Resource] in a given revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourcesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListResourcesResponse)` | The call object.  
  
### ListRevisions(ListRevisionsRequest, CallOptions)
    
    
    public virtual ListRevisionsResponse ListRevisions(ListRevisionsRequest request, CallOptions options)

Lists [Revision][google.cloud.config.v1.Revision]s of a deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListRevisionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListRevisionsResponse)` | The response received from the server.  
  
### ListRevisions(ListRevisionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListRevisionsResponse ListRevisions(ListRevisionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Revision][google.cloud.config.v1.Revision]s of a deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListRevisionsRequest)`  
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
`[ListRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListRevisionsResponse)` | The response received from the server.  
  
### ListRevisionsAsync(ListRevisionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListRevisionsResponse> ListRevisionsAsync(ListRevisionsRequest request, CallOptions options)

Lists [Revision][google.cloud.config.v1.Revision]s of a deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListRevisionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListRevisionsResponse)` | The call object.  
  
### ListRevisionsAsync(ListRevisionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListRevisionsResponse> ListRevisionsAsync(ListRevisionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Revision][google.cloud.config.v1.Revision]s of a deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListRevisionsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListRevisionsResponse)` | The call object.  
  
### ListTerraformVersions(ListTerraformVersionsRequest, CallOptions)
    
    
    public virtual ListTerraformVersionsResponse ListTerraformVersions(ListTerraformVersionsRequest request, CallOptions options)

Lists [TerraformVersion][google.cloud.config.v1.TerraformVersion]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTerraformVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListTerraformVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListTerraformVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListTerraformVersionsResponse)` | The response received from the server.  
  
### ListTerraformVersions(ListTerraformVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListTerraformVersionsResponse ListTerraformVersions(ListTerraformVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [TerraformVersion][google.cloud.config.v1.TerraformVersion]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTerraformVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListTerraformVersionsRequest)`  
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
`[ListTerraformVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListTerraformVersionsResponse)` | The response received from the server.  
  
### ListTerraformVersionsAsync(ListTerraformVersionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListTerraformVersionsResponse> ListTerraformVersionsAsync(ListTerraformVersionsRequest request, CallOptions options)

Lists [TerraformVersion][google.cloud.config.v1.TerraformVersion]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTerraformVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListTerraformVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListTerraformVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListTerraformVersionsResponse)` | The call object.  
  
### ListTerraformVersionsAsync(ListTerraformVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListTerraformVersionsResponse> ListTerraformVersionsAsync(ListTerraformVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [TerraformVersion][google.cloud.config.v1.TerraformVersion]s in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTerraformVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListTerraformVersionsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListTerraformVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListTerraformVersionsResponse)` | The call object.  
  
### LockDeployment(LockDeploymentRequest, CallOptions)
    
    
    public virtual Operation LockDeployment(LockDeploymentRequest request, CallOptions options)

Locks a deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LockDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.LockDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### LockDeployment(LockDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation LockDeployment(LockDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Locks a deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LockDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.LockDeploymentRequest)`  
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
  
### LockDeploymentAsync(LockDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> LockDeploymentAsync(LockDeploymentRequest request, CallOptions options)

Locks a deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LockDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.LockDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### LockDeploymentAsync(LockDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> LockDeploymentAsync(LockDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Locks a deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LockDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.LockDeploymentRequest)`  
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
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override Config.ConfigClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Config)[ConfigClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Config.ConfigClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Config.V1.Config.ConfigClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### ProvisionDeploymentGroup(ProvisionDeploymentGroupRequest, CallOptions)
    
    
    public virtual Operation ProvisionDeploymentGroup(ProvisionDeploymentGroupRequest request, CallOptions options)

Provisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision] but are _no longer_ included in the _current_ [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ProvisionDeploymentGroup(ProvisionDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ProvisionDeploymentGroup(ProvisionDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Provisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision] but are _no longer_ included in the _current_ [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupRequest)`  
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
  
### ProvisionDeploymentGroupAsync(ProvisionDeploymentGroupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ProvisionDeploymentGroupAsync(ProvisionDeploymentGroupRequest request, CallOptions options)

Provisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision] but are _no longer_ included in the _current_ [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ProvisionDeploymentGroupAsync(ProvisionDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ProvisionDeploymentGroupAsync(ProvisionDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Provisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ [DeploymentGroupRevision][google.cloud.config.v1.DeploymentGroupRevision] but are _no longer_ included in the _current_ [DeploymentGroup][google.cloud.config.v1.DeploymentGroup] definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupRequest)`  
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
  
### UnlockDeployment(UnlockDeploymentRequest, CallOptions)
    
    
    public virtual Operation UnlockDeployment(UnlockDeploymentRequest request, CallOptions options)

Unlocks a locked deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UnlockDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UnlockDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UnlockDeployment(UnlockDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UnlockDeployment(UnlockDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Unlocks a locked deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UnlockDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UnlockDeploymentRequest)`  
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
  
### UnlockDeploymentAsync(UnlockDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UnlockDeploymentAsync(UnlockDeploymentRequest request, CallOptions options)

Unlocks a locked deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UnlockDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UnlockDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UnlockDeploymentAsync(UnlockDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UnlockDeploymentAsync(UnlockDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Unlocks a locked deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UnlockDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UnlockDeploymentRequest)`  
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
  
### UpdateAutoMigrationConfig(UpdateAutoMigrationConfigRequest, CallOptions)
    
    
    public virtual Operation UpdateAutoMigrationConfig(UpdateAutoMigrationConfigRequest request, CallOptions options)

Updates the AutoMigrationConfig for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateAutoMigrationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateAutoMigrationConfig(UpdateAutoMigrationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateAutoMigrationConfig(UpdateAutoMigrationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the AutoMigrationConfig for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateAutoMigrationConfigRequest)`  
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
  
### UpdateAutoMigrationConfigAsync(UpdateAutoMigrationConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAutoMigrationConfigAsync(UpdateAutoMigrationConfigRequest request, CallOptions options)

Updates the AutoMigrationConfig for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateAutoMigrationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateAutoMigrationConfigAsync(UpdateAutoMigrationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAutoMigrationConfigAsync(UpdateAutoMigrationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the AutoMigrationConfig for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateAutoMigrationConfigRequest)`  
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
  
### UpdateDeployment(UpdateDeploymentRequest, CallOptions)
    
    
    public virtual Operation UpdateDeployment(UpdateDeploymentRequest request, CallOptions options)

Updates a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateDeployment(UpdateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateDeployment(UpdateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateDeploymentRequest)`  
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
  
### UpdateDeploymentAsync(UpdateDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateDeploymentAsync(UpdateDeploymentRequest request, CallOptions options)

Updates a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateDeploymentAsync(UpdateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateDeploymentAsync(UpdateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a [Deployment][google.cloud.config.v1.Deployment].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateDeploymentRequest)`  
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
  
### UpdateDeploymentGroup(UpdateDeploymentGroupRequest, CallOptions)
    
    
    public virtual Operation UpdateDeploymentGroup(UpdateDeploymentGroupRequest request, CallOptions options)

Updates a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateDeploymentGroup(UpdateDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateDeploymentGroup(UpdateDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateDeploymentGroupRequest)`  
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
  
### UpdateDeploymentGroupAsync(UpdateDeploymentGroupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateDeploymentGroupAsync(UpdateDeploymentGroupRequest request, CallOptions options)

Updates a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateDeploymentGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateDeploymentGroupAsync(UpdateDeploymentGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateDeploymentGroupAsync(UpdateDeploymentGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.UpdateDeploymentGroupRequest)`  
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

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
