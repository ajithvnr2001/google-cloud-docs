---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePoolService.DeploymentResourcePoolServiceClient
title: Vertex AI v1 API - Class DeploymentResourcePoolService.DeploymentResourcePoolServiceClient (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:35.752862+00:00
---

# Vertex AI v1 API - Class DeploymentResourcePoolService.DeploymentResourcePoolServiceClient (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePoolService.DeploymentResourcePoolServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class DeploymentResourcePoolService.DeploymentResourcePoolServiceClient (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public class DeploymentResourcePoolService.DeploymentResourcePoolServiceClient : ClientBase<DeploymentResourcePoolService.DeploymentResourcePoolServiceClient>

Reference documentation and code samples for the Vertex AI v1 API class DeploymentResourcePoolService.DeploymentResourcePoolServiceClient.

Client for DeploymentResourcePoolService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[DeploymentResourcePoolService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePoolService)[DeploymentResourcePoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePoolService.DeploymentResourcePoolServiceClient) > DeploymentResourcePoolService.DeploymentResourcePoolServiceClient

## Inherited Members

[ClientBase<DeploymentResourcePoolService.DeploymentResourcePoolServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Constructors 

### DeploymentResourcePoolServiceClient()
    
    
    protected DeploymentResourcePoolServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### DeploymentResourcePoolServiceClient(CallInvoker)
    
    
    public DeploymentResourcePoolServiceClient(CallInvoker callInvoker)

Creates a new client for DeploymentResourcePoolService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### DeploymentResourcePoolServiceClient(ChannelBase)
    
    
    public DeploymentResourcePoolServiceClient(ChannelBase channel)

Creates a new client for DeploymentResourcePoolService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### DeploymentResourcePoolServiceClient(ClientBaseConfiguration)
    
    
    protected DeploymentResourcePoolServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateDeploymentResourcePool(CreateDeploymentResourcePoolRequest, CallOptions)
    
    
    public virtual Operation CreateDeploymentResourcePool(CreateDeploymentResourcePoolRequest request, CallOptions options)

Create a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateDeploymentResourcePoolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateDeploymentResourcePool(CreateDeploymentResourcePoolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateDeploymentResourcePool(CreateDeploymentResourcePoolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateDeploymentResourcePoolRequest)`  
The request to send to the server.  
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
  
### CreateDeploymentResourcePoolAsync(CreateDeploymentResourcePoolRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateDeploymentResourcePoolAsync(CreateDeploymentResourcePoolRequest request, CallOptions options)

Create a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateDeploymentResourcePoolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateDeploymentResourcePoolAsync(CreateDeploymentResourcePoolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateDeploymentResourcePoolAsync(CreateDeploymentResourcePoolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateDeploymentResourcePoolRequest)`  
The request to send to the server.  
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
  
### DeleteDeploymentResourcePool(DeleteDeploymentResourcePoolRequest, CallOptions)
    
    
    public virtual Operation DeleteDeploymentResourcePool(DeleteDeploymentResourcePoolRequest request, CallOptions options)

Delete a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteDeploymentResourcePoolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteDeploymentResourcePool(DeleteDeploymentResourcePoolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteDeploymentResourcePool(DeleteDeploymentResourcePoolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Delete a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteDeploymentResourcePoolRequest)`  
The request to send to the server.  
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
  
### DeleteDeploymentResourcePoolAsync(DeleteDeploymentResourcePoolRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteDeploymentResourcePoolAsync(DeleteDeploymentResourcePoolRequest request, CallOptions options)

Delete a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteDeploymentResourcePoolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteDeploymentResourcePoolAsync(DeleteDeploymentResourcePoolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteDeploymentResourcePoolAsync(DeleteDeploymentResourcePoolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Delete a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteDeploymentResourcePoolRequest)`  
The request to send to the server.  
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
  
### GetDeploymentResourcePool(GetDeploymentResourcePoolRequest, CallOptions)
    
    
    public virtual DeploymentResourcePool GetDeploymentResourcePool(GetDeploymentResourcePoolRequest request, CallOptions options)

Get a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetDeploymentResourcePoolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePool)` | The response received from the server.  
  
### GetDeploymentResourcePool(GetDeploymentResourcePoolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DeploymentResourcePool GetDeploymentResourcePool(GetDeploymentResourcePoolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetDeploymentResourcePoolRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePool)` | The response received from the server.  
  
### GetDeploymentResourcePoolAsync(GetDeploymentResourcePoolRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DeploymentResourcePool> GetDeploymentResourcePoolAsync(GetDeploymentResourcePoolRequest request, CallOptions options)

Get a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetDeploymentResourcePoolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeploymentResourcePool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePool)` | The call object.  
  
### GetDeploymentResourcePoolAsync(GetDeploymentResourcePoolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DeploymentResourcePool> GetDeploymentResourcePoolAsync(GetDeploymentResourcePoolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetDeploymentResourcePoolRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeploymentResourcePool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePool)` | The call object.  
  
### ListDeploymentResourcePools(ListDeploymentResourcePoolsRequest, CallOptions)
    
    
    public virtual ListDeploymentResourcePoolsResponse ListDeploymentResourcePools(ListDeploymentResourcePoolsRequest request, CallOptions options)

List DeploymentResourcePools in a location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentResourcePoolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListDeploymentResourcePoolsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeploymentResourcePoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListDeploymentResourcePoolsResponse)` | The response received from the server.  
  
### ListDeploymentResourcePools(ListDeploymentResourcePoolsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDeploymentResourcePoolsResponse ListDeploymentResourcePools(ListDeploymentResourcePoolsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List DeploymentResourcePools in a location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentResourcePoolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListDeploymentResourcePoolsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeploymentResourcePoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListDeploymentResourcePoolsResponse)` | The response received from the server.  
  
### ListDeploymentResourcePoolsAsync(ListDeploymentResourcePoolsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDeploymentResourcePoolsResponse> ListDeploymentResourcePoolsAsync(ListDeploymentResourcePoolsRequest request, CallOptions options)

List DeploymentResourcePools in a location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentResourcePoolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListDeploymentResourcePoolsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDeploymentResourcePoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListDeploymentResourcePoolsResponse)` | The call object.  
  
### ListDeploymentResourcePoolsAsync(ListDeploymentResourcePoolsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDeploymentResourcePoolsResponse> ListDeploymentResourcePoolsAsync(ListDeploymentResourcePoolsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List DeploymentResourcePools in a location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentResourcePoolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListDeploymentResourcePoolsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDeploymentResourcePoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListDeploymentResourcePoolsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override DeploymentResourcePoolService.DeploymentResourcePoolServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePoolService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePoolService)[DeploymentResourcePoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePoolService.DeploymentResourcePoolServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.AIPlatform.V1.DeploymentResourcePoolService.DeploymentResourcePoolServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### QueryDeployedModels(QueryDeployedModelsRequest, CallOptions)
    
    
    public virtual QueryDeployedModelsResponse QueryDeployedModels(QueryDeployedModelsRequest request, CallOptions options)

List DeployedModels that have been deployed on this DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDeployedModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QueryDeployedModelsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryDeployedModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QueryDeployedModelsResponse)` | The response received from the server.  
  
### QueryDeployedModels(QueryDeployedModelsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryDeployedModelsResponse QueryDeployedModels(QueryDeployedModelsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List DeployedModels that have been deployed on this DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDeployedModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QueryDeployedModelsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryDeployedModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QueryDeployedModelsResponse)` | The response received from the server.  
  
### QueryDeployedModelsAsync(QueryDeployedModelsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryDeployedModelsResponse> QueryDeployedModelsAsync(QueryDeployedModelsRequest request, CallOptions options)

List DeployedModels that have been deployed on this DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDeployedModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QueryDeployedModelsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryDeployedModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QueryDeployedModelsResponse)` | The call object.  
  
### QueryDeployedModelsAsync(QueryDeployedModelsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryDeployedModelsResponse> QueryDeployedModelsAsync(QueryDeployedModelsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List DeployedModels that have been deployed on this DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDeployedModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QueryDeployedModelsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryDeployedModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.QueryDeployedModelsResponse)` | The call object.  
  
### UpdateDeploymentResourcePool(UpdateDeploymentResourcePoolRequest, CallOptions)
    
    
    public virtual Operation UpdateDeploymentResourcePool(UpdateDeploymentResourcePoolRequest request, CallOptions options)

Update a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateDeploymentResourcePoolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateDeploymentResourcePool(UpdateDeploymentResourcePoolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateDeploymentResourcePool(UpdateDeploymentResourcePoolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateDeploymentResourcePoolRequest)`  
The request to send to the server.  
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
  
### UpdateDeploymentResourcePoolAsync(UpdateDeploymentResourcePoolRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateDeploymentResourcePoolAsync(UpdateDeploymentResourcePoolRequest request, CallOptions options)

Update a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateDeploymentResourcePoolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateDeploymentResourcePoolAsync(UpdateDeploymentResourcePoolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateDeploymentResourcePoolAsync(UpdateDeploymentResourcePoolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update a DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentResourcePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateDeploymentResourcePoolRequest)`  
The request to send to the server.  
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

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
