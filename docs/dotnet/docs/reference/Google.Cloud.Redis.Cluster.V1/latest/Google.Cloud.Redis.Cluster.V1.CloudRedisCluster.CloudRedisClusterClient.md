---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CloudRedisCluster.CloudRedisClusterClient
title: Google Cloud Memorystore for Redis (cluster management) v1 API - Class CloudRedisCluster.CloudRedisClusterClient (1.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:51.427131+00:00
---

# Google Cloud Memorystore for Redis (cluster management) v1 API - Class CloudRedisCluster.CloudRedisClusterClient (1.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CloudRedisCluster.CloudRedisClusterClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis (cluster management) v1 API - Class CloudRedisCluster.CloudRedisClusterClient (1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public class CloudRedisCluster.CloudRedisClusterClient : ClientBase<CloudRedisCluster.CloudRedisClusterClient>

Reference documentation and code samples for the Google Cloud Memorystore for Redis (cluster management) v1 API class CloudRedisCluster.CloudRedisClusterClient.

Client for CloudRedisCluster

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[CloudRedisCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CloudRedisCluster)[CloudRedisClusterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CloudRedisCluster.CloudRedisClusterClient) > CloudRedisCluster.CloudRedisClusterClient

## Inherited Members

[ClientBase<CloudRedisCluster.CloudRedisClusterClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Redis.Cluster.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1)

## Assembly

Google.Cloud.Redis.Cluster.V1.dll

## Constructors 

### CloudRedisClusterClient()
    
    
    protected CloudRedisClusterClient()

Protected parameterless constructor to allow creation of test doubles.

### CloudRedisClusterClient(CallInvoker)
    
    
    public CloudRedisClusterClient(CallInvoker callInvoker)

Creates a new client for CloudRedisCluster that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### CloudRedisClusterClient(ChannelBase)
    
    
    public CloudRedisClusterClient(ChannelBase channel)

Creates a new client for CloudRedisCluster

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### CloudRedisClusterClient(ClientBaseConfiguration)
    
    
    protected CloudRedisClusterClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### BackupCluster(BackupClusterRequest, CallOptions)
    
    
    public virtual Operation BackupCluster(BackupClusterRequest request, CallOptions options)

Backup Redis Cluster. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the cluster's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BackupClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### BackupCluster(BackupClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation BackupCluster(BackupClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Backup Redis Cluster. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the cluster's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BackupClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupClusterRequest)`  
The request to send to the server.  
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
  
### BackupClusterAsync(BackupClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> BackupClusterAsync(BackupClusterRequest request, CallOptions options)

Backup Redis Cluster. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the cluster's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BackupClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### BackupClusterAsync(BackupClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> BackupClusterAsync(BackupClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Backup Redis Cluster. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the cluster's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BackupClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupClusterRequest)`  
The request to send to the server.  
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
  
### CreateAclPolicy(CreateAclPolicyRequest, CallOptions)
    
    
    public virtual AclPolicy CreateAclPolicy(CreateAclPolicyRequest request, CallOptions options)

Creates an ACL policy. The creation is executed synchronously and the policy is available for use immediately after the RPC returns.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CreateAclPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AclPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicy)` | The response received from the server.  
  
### CreateAclPolicy(CreateAclPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AclPolicy CreateAclPolicy(CreateAclPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates an ACL policy. The creation is executed synchronously and the policy is available for use immediately after the RPC returns.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CreateAclPolicyRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AclPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicy)` | The response received from the server.  
  
### CreateAclPolicyAsync(CreateAclPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AclPolicy> CreateAclPolicyAsync(CreateAclPolicyRequest request, CallOptions options)

Creates an ACL policy. The creation is executed synchronously and the policy is available for use immediately after the RPC returns.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CreateAclPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AclPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicy)` | The call object.  
  
### CreateAclPolicyAsync(CreateAclPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AclPolicy> CreateAclPolicyAsync(CreateAclPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates an ACL policy. The creation is executed synchronously and the policy is available for use immediately after the RPC returns.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CreateAclPolicyRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AclPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicy)` | The call object.  
  
### CreateCluster(CreateClusterRequest, CallOptions)
    
    
    public virtual Operation CreateCluster(CreateClusterRequest request, CallOptions options)

Creates a Redis cluster based on the specified properties. The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis cluster will be fully functional. The completed longrunning.Operation will contain the new cluster object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CreateClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateCluster(CreateClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateCluster(CreateClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a Redis cluster based on the specified properties. The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis cluster will be fully functional. The completed longrunning.Operation will contain the new cluster object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CreateClusterRequest)`  
The request to send to the server.  
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
  
### CreateClusterAsync(CreateClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateClusterAsync(CreateClusterRequest request, CallOptions options)

Creates a Redis cluster based on the specified properties. The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis cluster will be fully functional. The completed longrunning.Operation will contain the new cluster object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CreateClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateClusterAsync(CreateClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateClusterAsync(CreateClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a Redis cluster based on the specified properties. The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis cluster will be fully functional. The completed longrunning.Operation will contain the new cluster object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CreateClusterRequest)`  
The request to send to the server.  
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
  
### DeleteAclPolicy(DeleteAclPolicyRequest, CallOptions)
    
    
    public virtual Operation DeleteAclPolicy(DeleteAclPolicyRequest request, CallOptions options)

Deletes a specific ACL policy. This action will delete the ACL policy and all the rules associated with it. An ACL policy cannot be deleted if it is attached to a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteAclPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteAclPolicy(DeleteAclPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteAclPolicy(DeleteAclPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a specific ACL policy. This action will delete the ACL policy and all the rules associated with it. An ACL policy cannot be deleted if it is attached to a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteAclPolicyRequest)`  
The request to send to the server.  
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
  
### DeleteAclPolicyAsync(DeleteAclPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAclPolicyAsync(DeleteAclPolicyRequest request, CallOptions options)

Deletes a specific ACL policy. This action will delete the ACL policy and all the rules associated with it. An ACL policy cannot be deleted if it is attached to a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteAclPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteAclPolicyAsync(DeleteAclPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAclPolicyAsync(DeleteAclPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a specific ACL policy. This action will delete the ACL policy and all the rules associated with it. An ACL policy cannot be deleted if it is attached to a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteAclPolicyRequest)`  
The request to send to the server.  
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
  
### DeleteBackup(DeleteBackupRequest, CallOptions)
    
    
    public virtual Operation DeleteBackup(DeleteBackupRequest request, CallOptions options)

Deletes a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteBackupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteBackup(DeleteBackupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteBackup(DeleteBackupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteBackupRequest)`  
The request to send to the server.  
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
  
### DeleteBackupAsync(DeleteBackupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteBackupAsync(DeleteBackupRequest request, CallOptions options)

Deletes a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteBackupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteBackupAsync(DeleteBackupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteBackupAsync(DeleteBackupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteBackupRequest)`  
The request to send to the server.  
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
  
### DeleteCluster(DeleteClusterRequest, CallOptions)
    
    
    public virtual Operation DeleteCluster(DeleteClusterRequest request, CallOptions options)

Deletes a specific Redis cluster. Cluster stops serving and data is deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteCluster(DeleteClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteCluster(DeleteClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a specific Redis cluster. Cluster stops serving and data is deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteClusterRequest)`  
The request to send to the server.  
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
  
### DeleteClusterAsync(DeleteClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteClusterAsync(DeleteClusterRequest request, CallOptions options)

Deletes a specific Redis cluster. Cluster stops serving and data is deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteClusterAsync(DeleteClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteClusterAsync(DeleteClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a specific Redis cluster. Cluster stops serving and data is deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.DeleteClusterRequest)`  
The request to send to the server.  
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
  
### ExportBackup(ExportBackupRequest, CallOptions)
    
    
    public virtual Operation ExportBackup(ExportBackupRequest request, CallOptions options)

Exports a specific backup to a customer target Cloud Storage URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ExportBackupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ExportBackup(ExportBackupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ExportBackup(ExportBackupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Exports a specific backup to a customer target Cloud Storage URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ExportBackupRequest)`  
The request to send to the server.  
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
  
### ExportBackupAsync(ExportBackupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ExportBackupAsync(ExportBackupRequest request, CallOptions options)

Exports a specific backup to a customer target Cloud Storage URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ExportBackupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ExportBackupAsync(ExportBackupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ExportBackupAsync(ExportBackupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Exports a specific backup to a customer target Cloud Storage URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ExportBackupRequest)`  
The request to send to the server.  
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
  
### GetAclPolicy(GetAclPolicyRequest, CallOptions)
    
    
    public virtual AclPolicy GetAclPolicy(GetAclPolicyRequest request, CallOptions options)

Gets the details of a specific Redis Cluster ACL policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetAclPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AclPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicy)` | The response received from the server.  
  
### GetAclPolicy(GetAclPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AclPolicy GetAclPolicy(GetAclPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a specific Redis Cluster ACL policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetAclPolicyRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AclPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicy)` | The response received from the server.  
  
### GetAclPolicyAsync(GetAclPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AclPolicy> GetAclPolicyAsync(GetAclPolicyRequest request, CallOptions options)

Gets the details of a specific Redis Cluster ACL policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetAclPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AclPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicy)` | The call object.  
  
### GetAclPolicyAsync(GetAclPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AclPolicy> GetAclPolicyAsync(GetAclPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a specific Redis Cluster ACL policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetAclPolicyRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AclPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicy)` | The call object.  
  
### GetAclPolicyRevision(GetAclPolicyRevisionRequest, CallOptions)
    
    
    public virtual AclPolicyRevision GetAclPolicyRevision(GetAclPolicyRevisionRequest request, CallOptions options)

Gets details of a specific ACL policy revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclPolicyRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetAclPolicyRevisionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AclPolicyRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicyRevision)` | The response received from the server.  
  
### GetAclPolicyRevision(GetAclPolicyRevisionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AclPolicyRevision GetAclPolicyRevision(GetAclPolicyRevisionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a specific ACL policy revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclPolicyRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetAclPolicyRevisionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AclPolicyRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicyRevision)` | The response received from the server.  
  
### GetAclPolicyRevisionAsync(GetAclPolicyRevisionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AclPolicyRevision> GetAclPolicyRevisionAsync(GetAclPolicyRevisionRequest request, CallOptions options)

Gets details of a specific ACL policy revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclPolicyRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetAclPolicyRevisionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AclPolicyRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicyRevision)` | The call object.  
  
### GetAclPolicyRevisionAsync(GetAclPolicyRevisionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AclPolicyRevision> GetAclPolicyRevisionAsync(GetAclPolicyRevisionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a specific ACL policy revision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclPolicyRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetAclPolicyRevisionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AclPolicyRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.AclPolicyRevision)` | The call object.  
  
### GetBackup(GetBackupRequest, CallOptions)
    
    
    public virtual Backup GetBackup(GetBackupRequest request, CallOptions options)

Gets the details of a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetBackupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.Backup)` | The response received from the server.  
  
### GetBackup(GetBackupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Backup GetBackup(GetBackupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetBackupRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.Backup)` | The response received from the server.  
  
### GetBackupAsync(GetBackupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Backup> GetBackupAsync(GetBackupRequest request, CallOptions options)

Gets the details of a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetBackupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.Backup)` | The call object.  
  
### GetBackupAsync(GetBackupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Backup> GetBackupAsync(GetBackupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetBackupRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.Backup)` | The call object.  
  
### GetBackupCollection(GetBackupCollectionRequest, CallOptions)
    
    
    public virtual BackupCollection GetBackupCollection(GetBackupCollectionRequest request, CallOptions options)

Get a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetBackupCollectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection)` | The response received from the server.  
  
### GetBackupCollection(GetBackupCollectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BackupCollection GetBackupCollection(GetBackupCollectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetBackupCollectionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection)` | The response received from the server.  
  
### GetBackupCollectionAsync(GetBackupCollectionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BackupCollection> GetBackupCollectionAsync(GetBackupCollectionRequest request, CallOptions options)

Get a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetBackupCollectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BackupCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection)` | The call object.  
  
### GetBackupCollectionAsync(GetBackupCollectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BackupCollection> GetBackupCollectionAsync(GetBackupCollectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetBackupCollectionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BackupCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.BackupCollection)` | The call object.  
  
### GetCluster(GetClusterRequest, CallOptions)
    
    
    public virtual Cluster GetCluster(GetClusterRequest request, CallOptions options)

Gets the details of a specific Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.Cluster)` | The response received from the server.  
  
### GetCluster(GetClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Cluster GetCluster(GetClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a specific Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.Cluster)` | The response received from the server.  
  
### GetClusterAsync(GetClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Cluster> GetClusterAsync(GetClusterRequest request, CallOptions options)

Gets the details of a specific Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.Cluster)` | The call object.  
  
### GetClusterAsync(GetClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Cluster> GetClusterAsync(GetClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a specific Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.Cluster)` | The call object.  
  
### GetClusterCertificateAuthority(GetClusterCertificateAuthorityRequest, CallOptions)
    
    
    public virtual CertificateAuthority GetClusterCertificateAuthority(GetClusterCertificateAuthorityRequest request, CallOptions options)

Gets the details of certificate authority information for Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetClusterCertificateAuthorityRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority)` | The response received from the server.  
  
### GetClusterCertificateAuthority(GetClusterCertificateAuthorityRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CertificateAuthority GetClusterCertificateAuthority(GetClusterCertificateAuthorityRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of certificate authority information for Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetClusterCertificateAuthorityRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority)` | The response received from the server.  
  
### GetClusterCertificateAuthorityAsync(GetClusterCertificateAuthorityRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CertificateAuthority> GetClusterCertificateAuthorityAsync(GetClusterCertificateAuthorityRequest request, CallOptions options)

Gets the details of certificate authority information for Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetClusterCertificateAuthorityRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority)` | The call object.  
  
### GetClusterCertificateAuthorityAsync(GetClusterCertificateAuthorityRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CertificateAuthority> GetClusterCertificateAuthorityAsync(GetClusterCertificateAuthorityRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of certificate authority information for Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetClusterCertificateAuthorityRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority)` | The call object.  
  
### GetSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest, CallOptions)
    
    
    public virtual SharedRegionalCertificateAuthority GetSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request, CallOptions options)

Gets the details of regional certificate authority information for Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetSharedRegionalCertificateAuthorityRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.SharedRegionalCertificateAuthority)` | The response received from the server.  
  
### GetSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SharedRegionalCertificateAuthority GetSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of regional certificate authority information for Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetSharedRegionalCertificateAuthorityRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.SharedRegionalCertificateAuthority)` | The response received from the server.  
  
### GetSharedRegionalCertificateAuthorityAsync(GetSharedRegionalCertificateAuthorityRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SharedRegionalCertificateAuthority> GetSharedRegionalCertificateAuthorityAsync(GetSharedRegionalCertificateAuthorityRequest request, CallOptions options)

Gets the details of regional certificate authority information for Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetSharedRegionalCertificateAuthorityRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.SharedRegionalCertificateAuthority)` | The call object.  
  
### GetSharedRegionalCertificateAuthorityAsync(GetSharedRegionalCertificateAuthorityRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SharedRegionalCertificateAuthority> GetSharedRegionalCertificateAuthorityAsync(GetSharedRegionalCertificateAuthorityRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of regional certificate authority information for Redis cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.GetSharedRegionalCertificateAuthorityRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.SharedRegionalCertificateAuthority)` | The call object.  
  
### ListAclPolicies(ListAclPoliciesRequest, CallOptions)
    
    
    public virtual ListAclPoliciesResponse ListAclPolicies(ListAclPoliciesRequest request, CallOptions options)

Lists all ACL policies owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAclPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPoliciesResponse)` | The response received from the server.  
  
### ListAclPolicies(ListAclPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAclPoliciesResponse ListAclPolicies(ListAclPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all ACL policies owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPoliciesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAclPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPoliciesResponse)` | The response received from the server.  
  
### ListAclPoliciesAsync(ListAclPoliciesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAclPoliciesResponse> ListAclPoliciesAsync(ListAclPoliciesRequest request, CallOptions options)

Lists all ACL policies owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAclPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPoliciesResponse)` | The call object.  
  
### ListAclPoliciesAsync(ListAclPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAclPoliciesResponse> ListAclPoliciesAsync(ListAclPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all ACL policies owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPoliciesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAclPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPoliciesResponse)` | The call object.  
  
### ListAclPolicyRevisions(ListAclPolicyRevisionsRequest, CallOptions)
    
    
    public virtual ListAclPolicyRevisionsResponse ListAclPolicyRevisions(ListAclPolicyRevisionsRequest request, CallOptions options)

Lists all ACL policy revisions in a given ACL policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclPolicyRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPolicyRevisionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAclPolicyRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPolicyRevisionsResponse)` | The response received from the server.  
  
### ListAclPolicyRevisions(ListAclPolicyRevisionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAclPolicyRevisionsResponse ListAclPolicyRevisions(ListAclPolicyRevisionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all ACL policy revisions in a given ACL policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclPolicyRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPolicyRevisionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAclPolicyRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPolicyRevisionsResponse)` | The response received from the server.  
  
### ListAclPolicyRevisionsAsync(ListAclPolicyRevisionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAclPolicyRevisionsResponse> ListAclPolicyRevisionsAsync(ListAclPolicyRevisionsRequest request, CallOptions options)

Lists all ACL policy revisions in a given ACL policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclPolicyRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPolicyRevisionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAclPolicyRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPolicyRevisionsResponse)` | The call object.  
  
### ListAclPolicyRevisionsAsync(ListAclPolicyRevisionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAclPolicyRevisionsResponse> ListAclPolicyRevisionsAsync(ListAclPolicyRevisionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all ACL policy revisions in a given ACL policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclPolicyRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPolicyRevisionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAclPolicyRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListAclPolicyRevisionsResponse)` | The call object.  
  
### ListBackupCollections(ListBackupCollectionsRequest, CallOptions)
    
    
    public virtual ListBackupCollectionsResponse ListBackupCollections(ListBackupCollectionsRequest request, CallOptions options)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupCollectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupCollectionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupCollectionsResponse)` | The response received from the server.  
  
### ListBackupCollections(ListBackupCollectionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListBackupCollectionsResponse ListBackupCollections(ListBackupCollectionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupCollectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupCollectionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupCollectionsResponse)` | The response received from the server.  
  
### ListBackupCollectionsAsync(ListBackupCollectionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListBackupCollectionsResponse> ListBackupCollectionsAsync(ListBackupCollectionsRequest request, CallOptions options)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupCollectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupCollectionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListBackupCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupCollectionsResponse)` | The call object.  
  
### ListBackupCollectionsAsync(ListBackupCollectionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListBackupCollectionsResponse> ListBackupCollectionsAsync(ListBackupCollectionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupCollectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupCollectionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListBackupCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupCollectionsResponse)` | The call object.  
  
### ListBackups(ListBackupsRequest, CallOptions)
    
    
    public virtual ListBackupsResponse ListBackups(ListBackupsRequest request, CallOptions options)

Lists all backups owned by a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupsResponse)` | The response received from the server.  
  
### ListBackups(ListBackupsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListBackupsResponse ListBackups(ListBackupsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all backups owned by a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupsResponse)` | The response received from the server.  
  
### ListBackupsAsync(ListBackupsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListBackupsResponse> ListBackupsAsync(ListBackupsRequest request, CallOptions options)

Lists all backups owned by a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupsResponse)` | The call object.  
  
### ListBackupsAsync(ListBackupsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListBackupsResponse> ListBackupsAsync(ListBackupsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all backups owned by a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListBackupsResponse)` | The call object.  
  
### ListClusters(ListClustersRequest, CallOptions)
    
    
    public virtual ListClustersResponse ListClusters(ListClustersRequest request, CallOptions options)

Lists all Redis clusters owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListClustersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListClustersResponse)` | The response received from the server.  
  
### ListClusters(ListClustersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListClustersResponse ListClusters(ListClustersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all Redis clusters owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListClustersRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListClustersResponse)` | The response received from the server.  
  
### ListClustersAsync(ListClustersRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListClustersResponse> ListClustersAsync(ListClustersRequest request, CallOptions options)

Lists all Redis clusters owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListClustersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListClustersResponse)` | The call object.  
  
### ListClustersAsync(ListClustersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListClustersResponse> ListClustersAsync(ListClustersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all Redis clusters owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListClustersRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.ListClustersResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override CloudRedisCluster.CloudRedisClusterClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudRedisCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CloudRedisCluster)[CloudRedisClusterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CloudRedisCluster.CloudRedisClusterClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Redis.Cluster.V1.CloudRedisCluster.CloudRedisClusterClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### RescheduleClusterMaintenance(RescheduleClusterMaintenanceRequest, CallOptions)
    
    
    public virtual Operation RescheduleClusterMaintenance(RescheduleClusterMaintenanceRequest request, CallOptions options)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleClusterMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.RescheduleClusterMaintenanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RescheduleClusterMaintenance(RescheduleClusterMaintenanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RescheduleClusterMaintenance(RescheduleClusterMaintenanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleClusterMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.RescheduleClusterMaintenanceRequest)`  
The request to send to the server.  
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
  
### RescheduleClusterMaintenanceAsync(RescheduleClusterMaintenanceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RescheduleClusterMaintenanceAsync(RescheduleClusterMaintenanceRequest request, CallOptions options)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleClusterMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.RescheduleClusterMaintenanceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RescheduleClusterMaintenanceAsync(RescheduleClusterMaintenanceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RescheduleClusterMaintenanceAsync(RescheduleClusterMaintenanceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleClusterMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.RescheduleClusterMaintenanceRequest)`  
The request to send to the server.  
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
  
### UpdateAclPolicy(UpdateAclPolicyRequest, CallOptions)
    
    
    public virtual Operation UpdateAclPolicy(UpdateAclPolicyRequest request, CallOptions options)

Updates the ACL policy.

The operation applies the updated ACL policy to all of the linked clusters. If Memorystore can apply the policy to all clusters, then the operation returns a SUCCESS status. If Memorystore can't apply the policy to all clusters, then to ensure eventual consistency, Memorystore uses reconciliation to apply the policy to the failed clusters.

Completed longrunning.Operation will contain the new ACL policy object in the response field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.UpdateAclPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateAclPolicy(UpdateAclPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateAclPolicy(UpdateAclPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the ACL policy.

The operation applies the updated ACL policy to all of the linked clusters. If Memorystore can apply the policy to all clusters, then the operation returns a SUCCESS status. If Memorystore can't apply the policy to all clusters, then to ensure eventual consistency, Memorystore uses reconciliation to apply the policy to the failed clusters.

Completed longrunning.Operation will contain the new ACL policy object in the response field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.UpdateAclPolicyRequest)`  
The request to send to the server.  
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
  
### UpdateAclPolicyAsync(UpdateAclPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAclPolicyAsync(UpdateAclPolicyRequest request, CallOptions options)

Updates the ACL policy.

The operation applies the updated ACL policy to all of the linked clusters. If Memorystore can apply the policy to all clusters, then the operation returns a SUCCESS status. If Memorystore can't apply the policy to all clusters, then to ensure eventual consistency, Memorystore uses reconciliation to apply the policy to the failed clusters.

Completed longrunning.Operation will contain the new ACL policy object in the response field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.UpdateAclPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateAclPolicyAsync(UpdateAclPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAclPolicyAsync(UpdateAclPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the ACL policy.

The operation applies the updated ACL policy to all of the linked clusters. If Memorystore can apply the policy to all clusters, then the operation returns a SUCCESS status. If Memorystore can't apply the policy to all clusters, then to ensure eventual consistency, Memorystore uses reconciliation to apply the policy to the failed clusters.

Completed longrunning.Operation will contain the new ACL policy object in the response field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.UpdateAclPolicyRequest)`  
The request to send to the server.  
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
  
### UpdateCluster(UpdateClusterRequest, CallOptions)
    
    
    public virtual Operation UpdateCluster(UpdateClusterRequest request, CallOptions options)

Updates the metadata and configuration of a specific Redis cluster.

Completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.UpdateClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateCluster(UpdateClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateCluster(UpdateClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the metadata and configuration of a specific Redis cluster.

Completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.UpdateClusterRequest)`  
The request to send to the server.  
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
  
### UpdateClusterAsync(UpdateClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateClusterAsync(UpdateClusterRequest request, CallOptions options)

Updates the metadata and configuration of a specific Redis cluster.

Completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.UpdateClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateClusterAsync(UpdateClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateClusterAsync(UpdateClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the metadata and configuration of a specific Redis cluster.

Completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.UpdateClusterRequest)`  
The request to send to the server.  
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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
