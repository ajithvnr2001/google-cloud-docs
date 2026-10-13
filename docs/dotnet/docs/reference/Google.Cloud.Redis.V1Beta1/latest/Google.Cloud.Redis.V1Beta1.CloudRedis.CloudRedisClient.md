---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisClient
title: Google Cloud Memorystore for Redis v1beta1 API - Class CloudRedis.CloudRedisClient (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:57.687927+00:00
---

# Google Cloud Memorystore for Redis v1beta1 API - Class CloudRedis.CloudRedisClient (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis v1beta1 API - Class CloudRedis.CloudRedisClient (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisClient)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/3.0.0-beta05/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisClient)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/2.0.0-beta09/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisClient)


    
    
    public class CloudRedis.CloudRedisClient : ClientBase<CloudRedis.CloudRedisClient>

Reference documentation and code samples for the Google Cloud Memorystore for Redis v1beta1 API class CloudRedis.CloudRedisClient.

Client for CloudRedis

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[CloudRedis](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis)[CloudRedisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisClient) > CloudRedis.CloudRedisClient

## Inherited Members

[ClientBase<CloudRedis.CloudRedisClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Redis.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1)

## Assembly

Google.Cloud.Redis.V1Beta1.dll

## Constructors 

### CloudRedisClient()
    
    
    protected CloudRedisClient()

Protected parameterless constructor to allow creation of test doubles.

### CloudRedisClient(CallInvoker)
    
    
    public CloudRedisClient(CallInvoker callInvoker)

Creates a new client for CloudRedis that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### CloudRedisClient(ChannelBase)
    
    
    public CloudRedisClient(ChannelBase channel)

Creates a new client for CloudRedis

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### CloudRedisClient(ClientBaseConfiguration)
    
    
    protected CloudRedisClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateInstance(CreateInstanceRequest, CallOptions)
    
    
    public virtual Operation CreateInstance(CreateInstanceRequest request, CallOptions options)

Creates a Redis instance based on the specified tier and memory size.

By default, the instance is accessible from the project's [default network](https://cloud.google.com/vpc/docs/vpc).

The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis instance will be fully functional. The completed longrunning.Operation will contain the new instance object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CreateInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateInstance(CreateInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateInstance(CreateInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a Redis instance based on the specified tier and memory size.

By default, the instance is accessible from the project's [default network](https://cloud.google.com/vpc/docs/vpc).

The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis instance will be fully functional. The completed longrunning.Operation will contain the new instance object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CreateInstanceRequest)`  
The request to send to the server.  
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
  
### CreateInstanceAsync(CreateInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateInstanceAsync(CreateInstanceRequest request, CallOptions options)

Creates a Redis instance based on the specified tier and memory size.

By default, the instance is accessible from the project's [default network](https://cloud.google.com/vpc/docs/vpc).

The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis instance will be fully functional. The completed longrunning.Operation will contain the new instance object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CreateInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateInstanceAsync(CreateInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateInstanceAsync(CreateInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a Redis instance based on the specified tier and memory size.

By default, the instance is accessible from the project's [default network](https://cloud.google.com/vpc/docs/vpc).

The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis instance will be fully functional. The completed longrunning.Operation will contain the new instance object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CreateInstanceRequest)`  
The request to send to the server.  
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
  
### CreateOperationsClient()
    
    
    public virtual Operations.OperationsClient CreateOperationsClient()

Creates a new instance of [Operations.OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### DeleteInstance(DeleteInstanceRequest, CallOptions)
    
    
    public virtual Operation DeleteInstance(DeleteInstanceRequest request, CallOptions options)

Deletes a specific Redis instance. Instance stops serving and data is deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.DeleteInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteInstance(DeleteInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteInstance(DeleteInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a specific Redis instance. Instance stops serving and data is deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.DeleteInstanceRequest)`  
The request to send to the server.  
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
  
### DeleteInstanceAsync(DeleteInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteInstanceAsync(DeleteInstanceRequest request, CallOptions options)

Deletes a specific Redis instance. Instance stops serving and data is deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.DeleteInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteInstanceAsync(DeleteInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteInstanceAsync(DeleteInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a specific Redis instance. Instance stops serving and data is deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.DeleteInstanceRequest)`  
The request to send to the server.  
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
  
### ExportInstance(ExportInstanceRequest, CallOptions)
    
    
    public virtual Operation ExportInstance(ExportInstanceRequest request, CallOptions options)

Export Redis instance data into a Redis RDB format file in Cloud Storage.

Redis will continue serving during this operation.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ExportInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ExportInstance(ExportInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ExportInstance(ExportInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Export Redis instance data into a Redis RDB format file in Cloud Storage.

Redis will continue serving during this operation.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ExportInstanceRequest)`  
The request to send to the server.  
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
  
### ExportInstanceAsync(ExportInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ExportInstanceAsync(ExportInstanceRequest request, CallOptions options)

Export Redis instance data into a Redis RDB format file in Cloud Storage.

Redis will continue serving during this operation.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ExportInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ExportInstanceAsync(ExportInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ExportInstanceAsync(ExportInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Export Redis instance data into a Redis RDB format file in Cloud Storage.

Redis will continue serving during this operation.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ExportInstanceRequest)`  
The request to send to the server.  
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
  
### FailoverInstance(FailoverInstanceRequest, CallOptions)
    
    
    public virtual Operation FailoverInstance(FailoverInstanceRequest request, CallOptions options)

Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.FailoverInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### FailoverInstance(FailoverInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation FailoverInstance(FailoverInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.FailoverInstanceRequest)`  
The request to send to the server.  
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
  
### FailoverInstanceAsync(FailoverInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> FailoverInstanceAsync(FailoverInstanceRequest request, CallOptions options)

Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.FailoverInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### FailoverInstanceAsync(FailoverInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> FailoverInstanceAsync(FailoverInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.FailoverInstanceRequest)`  
The request to send to the server.  
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
  
### GetInstance(GetInstanceRequest, CallOptions)
    
    
    public virtual Instance GetInstance(GetInstanceRequest request, CallOptions options)

Gets the details of a specific Redis instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)` | The response received from the server.  
  
### GetInstance(GetInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Instance GetInstance(GetInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a specific Redis instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)` | The response received from the server.  
  
### GetInstanceAsync(GetInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Instance> GetInstanceAsync(GetInstanceRequest request, CallOptions options)

Gets the details of a specific Redis instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)` | The call object.  
  
### GetInstanceAsync(GetInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Instance> GetInstanceAsync(GetInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a specific Redis instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)` | The call object.  
  
### GetInstanceAuthString(GetInstanceAuthStringRequest, CallOptions)
    
    
    public virtual InstanceAuthString GetInstanceAuthString(GetInstanceAuthStringRequest request, CallOptions options)

Gets the AUTH string for a Redis instance. If AUTH is not enabled for the instance the response will be empty. This information is not included in the details returned to GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceAuthStringRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceAuthStringRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceAuthString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceAuthString)` | The response received from the server.  
  
### GetInstanceAuthString(GetInstanceAuthStringRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual InstanceAuthString GetInstanceAuthString(GetInstanceAuthStringRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the AUTH string for a Redis instance. If AUTH is not enabled for the instance the response will be empty. This information is not included in the details returned to GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceAuthStringRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceAuthStringRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceAuthString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceAuthString)` | The response received from the server.  
  
### GetInstanceAuthStringAsync(GetInstanceAuthStringRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<InstanceAuthString> GetInstanceAuthStringAsync(GetInstanceAuthStringRequest request, CallOptions options)

Gets the AUTH string for a Redis instance. If AUTH is not enabled for the instance the response will be empty. This information is not included in the details returned to GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceAuthStringRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceAuthStringRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[InstanceAuthString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceAuthString)` | The call object.  
  
### GetInstanceAuthStringAsync(GetInstanceAuthStringRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<InstanceAuthString> GetInstanceAuthStringAsync(GetInstanceAuthStringRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the AUTH string for a Redis instance. If AUTH is not enabled for the instance the response will be empty. This information is not included in the details returned to GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceAuthStringRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceAuthStringRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[InstanceAuthString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceAuthString)` | The call object.  
  
### ImportInstance(ImportInstanceRequest, CallOptions)
    
    
    public virtual Operation ImportInstance(ImportInstanceRequest request, CallOptions options)

Import a Redis RDB snapshot file from Cloud Storage into a Redis instance.

Redis may stop serving during this operation. Instance state will be IMPORTING for entire operation. When complete, the instance will contain only data from the imported file.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ImportInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ImportInstance(ImportInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ImportInstance(ImportInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Import a Redis RDB snapshot file from Cloud Storage into a Redis instance.

Redis may stop serving during this operation. Instance state will be IMPORTING for entire operation. When complete, the instance will contain only data from the imported file.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ImportInstanceRequest)`  
The request to send to the server.  
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
  
### ImportInstanceAsync(ImportInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ImportInstanceAsync(ImportInstanceRequest request, CallOptions options)

Import a Redis RDB snapshot file from Cloud Storage into a Redis instance.

Redis may stop serving during this operation. Instance state will be IMPORTING for entire operation. When complete, the instance will contain only data from the imported file.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ImportInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ImportInstanceAsync(ImportInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ImportInstanceAsync(ImportInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Import a Redis RDB snapshot file from Cloud Storage into a Redis instance.

Redis may stop serving during this operation. Instance state will be IMPORTING for entire operation. When complete, the instance will contain only data from the imported file.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ImportInstanceRequest)`  
The request to send to the server.  
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
  
### ListInstances(ListInstancesRequest, CallOptions)
    
    
    public virtual ListInstancesResponse ListInstances(ListInstancesRequest request, CallOptions options)

Lists all Redis instances owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesResponse)` | The response received from the server.  
  
### ListInstances(ListInstancesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListInstancesResponse ListInstances(ListInstancesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all Redis instances owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesResponse)` | The response received from the server.  
  
### ListInstancesAsync(ListInstancesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListInstancesResponse> ListInstancesAsync(ListInstancesRequest request, CallOptions options)

Lists all Redis instances owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesResponse)` | The call object.  
  
### ListInstancesAsync(ListInstancesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListInstancesResponse> ListInstancesAsync(ListInstancesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all Redis instances owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override CloudRedis.CloudRedisClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudRedis](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis)[CloudRedisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### RescheduleMaintenance(RescheduleMaintenanceRequest, CallOptions)
    
    
    public virtual Operation RescheduleMaintenance(RescheduleMaintenanceRequest request, CallOptions options)

Reschedule maintenance for a given instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.RescheduleMaintenanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RescheduleMaintenance(RescheduleMaintenanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RescheduleMaintenance(RescheduleMaintenanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Reschedule maintenance for a given instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.RescheduleMaintenanceRequest)`  
The request to send to the server.  
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
  
### RescheduleMaintenanceAsync(RescheduleMaintenanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RescheduleMaintenanceAsync(RescheduleMaintenanceRequest request, CallOptions options)

Reschedule maintenance for a given instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.RescheduleMaintenanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RescheduleMaintenanceAsync(RescheduleMaintenanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RescheduleMaintenanceAsync(RescheduleMaintenanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Reschedule maintenance for a given instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.RescheduleMaintenanceRequest)`  
The request to send to the server.  
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
  
### UpdateInstance(UpdateInstanceRequest, CallOptions)
    
    
    public virtual Operation UpdateInstance(UpdateInstanceRequest request, CallOptions options)

Updates the metadata and configuration of a specific Redis instance.

Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpdateInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateInstance(UpdateInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateInstance(UpdateInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the metadata and configuration of a specific Redis instance.

Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpdateInstanceRequest)`  
The request to send to the server.  
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
  
### UpdateInstanceAsync(UpdateInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateInstanceAsync(UpdateInstanceRequest request, CallOptions options)

Updates the metadata and configuration of a specific Redis instance.

Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpdateInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateInstanceAsync(UpdateInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateInstanceAsync(UpdateInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the metadata and configuration of a specific Redis instance.

Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpdateInstanceRequest)`  
The request to send to the server.  
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
  
### UpgradeInstance(UpgradeInstanceRequest, CallOptions)
    
    
    public virtual Operation UpgradeInstance(UpgradeInstanceRequest request, CallOptions options)

Upgrades Redis instance to the newer Redis version specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpgradeInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpgradeInstance(UpgradeInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpgradeInstance(UpgradeInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Upgrades Redis instance to the newer Redis version specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpgradeInstanceRequest)`  
The request to send to the server.  
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
  
### UpgradeInstanceAsync(UpgradeInstanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpgradeInstanceAsync(UpgradeInstanceRequest request, CallOptions options)

Upgrades Redis instance to the newer Redis version specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpgradeInstanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpgradeInstanceAsync(UpgradeInstanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpgradeInstanceAsync(UpgradeInstanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Upgrades Redis instance to the newer Redis version specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpgradeInstanceRequest)`  
The request to send to the server.  
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
