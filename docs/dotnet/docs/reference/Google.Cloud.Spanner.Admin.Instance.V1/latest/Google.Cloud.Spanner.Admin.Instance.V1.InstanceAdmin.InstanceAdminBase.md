---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdmin.InstanceAdminBase
title: Google Cloud Spanner Instance Administration v1 API - Class InstanceAdmin.InstanceAdminBase (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:10.397140+00:00
---

# Google Cloud Spanner Instance Administration v1 API - Class InstanceAdmin.InstanceAdminBase (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdmin.InstanceAdminBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner Instance Administration v1 API - Class InstanceAdmin.InstanceAdminBase (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    [BindServiceMethod(typeof(InstanceAdmin), "BindService")]
    public abstract class InstanceAdmin.InstanceAdminBase

Reference documentation and code samples for the Google Cloud Spanner Instance Administration v1 API class InstanceAdmin.InstanceAdminBase.

Base class for server-side implementations of InstanceAdmin

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InstanceAdmin.InstanceAdminBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.Admin.Instance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1)

## Assembly

Google.Cloud.Spanner.Admin.Instance.V1.dll

## Methods 

### CreateInstance(CreateInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateInstance(CreateInstanceRequest request, ServerCallContext context)

Creates an instance and begins preparing it to begin serving. The returned long-running operation can be used to track the progress of preparing the new instance. The instance name is assigned by the caller. If the named instance already exists, `CreateInstance` returns `ALREADY_EXISTS`.

Immediately upon completion of this request:

  * The instance is readable via the API, with all requested attributes but no allocated resources. Its state is `CREATING`.



Until completion of the returned operation:

  * Cancelling the operation renders the instance immediately unreadable via the API.
  * The instance can be deleted.
  * All other attempts to modify the instance are rejected.



Upon completion of the returned operation:

  * Billing for all successfully-allocated resources begins (some types may have lower than the requested levels).
  * Databases can be created in the instance.
  * The instance's allocated resource levels are readable via the API.
  * The instance's state becomes `READY`.



The returned long-running operation will have a name of the format `<instance_name>/operations/<operation_id>` and can be used to track creation of the instance. The metadata field type is [CreateInstanceMetadata][google.spanner.admin.instance.v1.CreateInstanceMetadata]. The response field type is [Instance][google.spanner.admin.instance.v1.Instance], if successful.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.CreateInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateInstanceConfig(CreateInstanceConfigRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateInstanceConfig(CreateInstanceConfigRequest request, ServerCallContext context)

Creates an instance configuration and begins preparing it to be used. The returned long-running operation can be used to track the progress of preparing the new instance configuration. The instance configuration name is assigned by the caller. If the named instance configuration already exists, `CreateInstanceConfig` returns `ALREADY_EXISTS`.

Immediately after the request returns:

  * The instance configuration is readable via the API, with all requested attributes. The instance configuration's [reconciling][google.spanner.admin.instance.v1.InstanceConfig.reconciling] field is set to true. Its state is `CREATING`.



While the operation is pending:

  * Cancelling the operation renders the instance configuration immediately unreadable via the API.
  * Except for deleting the creating resource, all other attempts to modify the instance configuration are rejected.



Upon completion of the returned operation:

  * Instances can be created using the instance configuration.
  * The instance configuration's [reconciling][google.spanner.admin.instance.v1.InstanceConfig.reconciling] field becomes false. Its state becomes `READY`.



The returned long-running operation will have a name of the format `<instance_config_name>/operations/<operation_id>` and can be used to track creation of the instance configuration. The metadata field type is [CreateInstanceConfigMetadata][google.spanner.admin.instance.v1.CreateInstanceConfigMetadata]. The response field type is [InstanceConfig][google.spanner.admin.instance.v1.InstanceConfig], if successful.

Authorization requires `spanner.instanceConfigs.create` permission on the resource [parent][google.spanner.admin.instance.v1.CreateInstanceConfigRequest.parent].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.CreateInstanceConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateInstancePartition(CreateInstancePartitionRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateInstancePartition(CreateInstancePartitionRequest request, ServerCallContext context)

Creates an instance partition and begins preparing it to be used. The returned long-running operation can be used to track the progress of preparing the new instance partition. The instance partition name is assigned by the caller. If the named instance partition already exists, `CreateInstancePartition` returns `ALREADY_EXISTS`.

Immediately upon completion of this request:

  * The instance partition is readable via the API, with all requested attributes but no allocated resources. Its state is `CREATING`.



Until completion of the returned operation:

  * Cancelling the operation renders the instance partition immediately unreadable via the API.
  * The instance partition can be deleted.
  * All other attempts to modify the instance partition are rejected.



Upon completion of the returned operation:

  * Billing for all successfully-allocated resources begins (some types may have lower than the requested levels).
  * Databases can start using this instance partition.
  * The instance partition's allocated resource levels are readable via the API.
  * The instance partition's state becomes `READY`.



The returned long-running operation will have a name of the format `<instance_partition_name>/operations/<operation_id>` and can be used to track creation of the instance partition. The metadata field type is [CreateInstancePartitionMetadata][google.spanner.admin.instance.v1.CreateInstancePartitionMetadata]. The response field type is [InstancePartition][google.spanner.admin.instance.v1.InstancePartition], if successful.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstancePartitionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.CreateInstancePartitionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteInstance(DeleteInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteInstance(DeleteInstanceRequest request, ServerCallContext context)

Deletes an instance.

Immediately upon completion of the request:

  * Billing ceases for all of the instance's reserved resources.



Soon afterward:

  * The instance and _all of its databases_ immediately and irrevocably disappear from the API. All data in the databases is permanently deleted.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.DeleteInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteInstanceConfig(DeleteInstanceConfigRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteInstanceConfig(DeleteInstanceConfigRequest request, ServerCallContext context)

Deletes the instance configuration. Deletion is only allowed when no instances are using the configuration. If any instances are using the configuration, returns `FAILED_PRECONDITION`.

Only user-managed configurations can be deleted.

Authorization requires `spanner.instanceConfigs.delete` permission on the resource [name][google.spanner.admin.instance.v1.InstanceConfig.name].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.DeleteInstanceConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteInstancePartition(DeleteInstancePartitionRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteInstancePartition(DeleteInstancePartitionRequest request, ServerCallContext context)

Deletes an existing instance partition. Requires that the instance partition is not used by any database or backup and is not the default instance partition of an instance.

Authorization requires `spanner.instancePartitions.delete` permission on the resource [name][google.spanner.admin.instance.v1.InstancePartition.name].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstancePartitionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.DeleteInstancePartitionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetIamPolicy(GetIamPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Policy> GetIamPolicy(GetIamPolicyRequest request, ServerCallContext context)

Gets the access control policy for an instance resource. Returns an empty policy if an instance exists but does not have a policy set.

Authorization requires `spanner.instances.getIamPolicy` on [resource][google.iam.v1.GetIamPolicyRequest.resource].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The response to send back to the client (wrapped by a task).  
  
### GetInstance(GetInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Instance> GetInstance(GetInstanceRequest request, ServerCallContext context)

Gets information about a particular instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance)` | The response to send back to the client (wrapped by a task).  
  
### GetInstanceConfig(GetInstanceConfigRequest, ServerCallContext)
    
    
    public virtual Task<InstanceConfig> GetInstanceConfig(GetInstanceConfigRequest request, ServerCallContext context)

Gets information about a particular instance configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfig)` | The response to send back to the client (wrapped by a task).  
  
### GetInstancePartition(GetInstancePartitionRequest, ServerCallContext)
    
    
    public virtual Task<InstancePartition> GetInstancePartition(GetInstancePartitionRequest request, ServerCallContext context)

Gets information about a particular instance partition.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstancePartitionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstancePartitionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstancePartition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstancePartition)` | The response to send back to the client (wrapped by a task).  
  
### ListInstanceConfigOperations(ListInstanceConfigOperationsRequest, ServerCallContext)
    
    
    public virtual Task<ListInstanceConfigOperationsResponse> ListInstanceConfigOperations(ListInstanceConfigOperationsRequest request, ServerCallContext context)

Lists the user-managed instance configuration long-running operations in the given project. An instance configuration operation has a name of the form `projects/<project>/instanceConfigs/<instance_config>/operations/<operation>`. The long-running operation metadata field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations. Operations returned are ordered by `operation.metadata.value.start_time` in descending order starting from the most recently started operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstanceConfigOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigOperationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListInstanceConfigOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigOperationsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListInstanceConfigs(ListInstanceConfigsRequest, ServerCallContext)
    
    
    public virtual Task<ListInstanceConfigsResponse> ListInstanceConfigs(ListInstanceConfigsRequest request, ServerCallContext context)

Lists the supported instance configurations for a given project.

Returns both Google-managed configurations and user-managed configurations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstanceConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListInstanceConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListInstancePartitionOperations(ListInstancePartitionOperationsRequest, ServerCallContext)
    
    
    public virtual Task<ListInstancePartitionOperationsResponse> ListInstancePartitionOperations(ListInstancePartitionOperationsRequest request, ServerCallContext context)

Lists instance partition long-running operations in the given instance. An instance partition operation has a name of the form `projects/<project>/instances/<instance>/instancePartitions/<instance_partition>/operations/<operation>`. The long-running operation metadata field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations. Operations returned are ordered by `operation.metadata.value.start_time` in descending order starting from the most recently started operation.

Authorization requires `spanner.instancePartitionOperations.list` permission on the resource [parent][google.spanner.admin.instance.v1.ListInstancePartitionOperationsRequest.parent].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancePartitionOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancePartitionOperationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListInstancePartitionOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancePartitionOperationsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListInstancePartitions(ListInstancePartitionsRequest, ServerCallContext)
    
    
    public virtual Task<ListInstancePartitionsResponse> ListInstancePartitions(ListInstancePartitionsRequest request, ServerCallContext context)

Lists all instance partitions for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancePartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancePartitionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListInstancePartitionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancePartitionsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListInstances(ListInstancesRequest, ServerCallContext)
    
    
    public virtual Task<ListInstancesResponse> ListInstances(ListInstancesRequest request, ServerCallContext context)

Lists all instances in the given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesResponse)` | The response to send back to the client (wrapped by a task).  
  
### MoveInstance(MoveInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> MoveInstance(MoveInstanceRequest request, ServerCallContext context)

Moves an instance to the target instance configuration. You can use the returned long-running operation to track the progress of moving the instance.

`MoveInstance` returns `FAILED_PRECONDITION` if the instance meets any of the following criteria:

  * Is undergoing a move to a different instance configuration
  * Has backups
  * Has an ongoing update
  * Contains any CMEK-enabled databases
  * Is a free trial instance



While the operation is pending:

  * All other attempts to modify the instance, including changes to its compute capacity, are rejected.
  * The following database and backup admin operations are rejected:

    * `DatabaseAdmin.CreateDatabase`
    * `DatabaseAdmin.UpdateDatabaseDdl` (disabled if default_leader is specified in the request.)
    * `DatabaseAdmin.RestoreDatabase`
    * `DatabaseAdmin.CreateBackup`
    * `DatabaseAdmin.CopyBackup`
  * Both the source and target instance configurations are subject to hourly compute and storage charges.

  * The instance might experience higher read-write latencies and a higher transaction abort rate. However, moving an instance doesn't cause any downtime.



The returned long-running operation has a name of the format `<instance_name>/operations/<operation_id>` and can be used to track the move instance operation. The metadata field type is [MoveInstanceMetadata][google.spanner.admin.instance.v1.MoveInstanceMetadata]. The response field type is [Instance][google.spanner.admin.instance.v1.Instance], if successful. Cancelling the operation sets its metadata's [cancel_time][google.spanner.admin.instance.v1.MoveInstanceMetadata.cancel_time]. Cancellation is not immediate because it involves moving any data previously moved to the target instance configuration back to the original instance configuration. You can use this operation to track the progress of the cancellation. Upon successful completion of the cancellation, the operation terminates with `CANCELLED` status.

If not cancelled, upon completion of the returned operation:

  * The instance successfully moves to the target instance configuration.
  * You are billed for compute and storage in target instance configuration.



Authorization requires the `spanner.instances.update` permission on the resource [instance][google.spanner.admin.instance.v1.Instance].

For more details, see [Move an instance](https://cloud.google.com/spanner/docs/move-instance).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.MoveInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### SetIamPolicy(SetIamPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Policy> SetIamPolicy(SetIamPolicyRequest request, ServerCallContext context)

Sets the access control policy on an instance resource. Replaces any existing policy.

Authorization requires `spanner.instances.setIamPolicy` on [resource][google.iam.v1.SetIamPolicyRequest.resource].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The response to send back to the client (wrapped by a task).  
  
### TestIamPermissions(TestIamPermissionsRequest, ServerCallContext)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissions(TestIamPermissionsRequest request, ServerCallContext context)

Returns permissions that the caller has on the specified instance resource.

Attempting this RPC on a non-existent Cloud Spanner instance resource will result in a NOT_FOUND error if the user has `spanner.instances.list` permission on the containing Google Cloud Project. Otherwise returns an empty set of permissions.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateInstance(UpdateInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateInstance(UpdateInstanceRequest request, ServerCallContext context)

Updates an instance, and begins allocating or releasing resources as requested. The returned long-running operation can be used to track the progress of updating the instance. If the named instance does not exist, returns `NOT_FOUND`.

Immediately upon completion of this request:

  * For resource types for which a decrease in the instance's allocation has been requested, billing is based on the newly-requested level.



Until completion of the returned operation:

  * Cancelling the operation sets its metadata's [cancel_time][google.spanner.admin.instance.v1.UpdateInstanceMetadata.cancel_time], and begins restoring resources to their pre-request values. The operation is guaranteed to succeed at undoing all resource changes, after which point it terminates with a `CANCELLED` status.
  * All other attempts to modify the instance are rejected.
  * Reading the instance via the API continues to give the pre-request resource levels.



Upon completion of the returned operation:

  * Billing begins for all successfully-allocated resources (some types may have lower than the requested levels).
  * All newly-reserved resources are available for serving the instance's tables.
  * The instance's new resource levels are readable via the API.



The returned long-running operation will have a name of the format `<instance_name>/operations/<operation_id>` and can be used to track the instance modification. The metadata field type is [UpdateInstanceMetadata][google.spanner.admin.instance.v1.UpdateInstanceMetadata]. The response field type is [Instance][google.spanner.admin.instance.v1.Instance], if successful.

Authorization requires `spanner.instances.update` permission on the resource [name][google.spanner.admin.instance.v1.Instance.name].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.UpdateInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateInstanceConfig(UpdateInstanceConfigRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateInstanceConfig(UpdateInstanceConfigRequest request, ServerCallContext context)

Updates an instance configuration. The returned long-running operation can be used to track the progress of updating the instance. If the named instance configuration does not exist, returns `NOT_FOUND`.

Only user-managed configurations can be updated.

Immediately after the request returns:

  * The instance configuration's [reconciling][google.spanner.admin.instance.v1.InstanceConfig.reconciling] field is set to true.



While the operation is pending:

  * Cancelling the operation sets its metadata's [cancel_time][google.spanner.admin.instance.v1.UpdateInstanceConfigMetadata.cancel_time]. The operation is guaranteed to succeed at undoing all changes, after which point it terminates with a `CANCELLED` status.
  * All other attempts to modify the instance configuration are rejected.
  * Reading the instance configuration via the API continues to give the pre-request values.



Upon completion of the returned operation:

  * Creating instances using the instance configuration uses the new values.
  * The new values of the instance configuration are readable via the API.
  * The instance configuration's [reconciling][google.spanner.admin.instance.v1.InstanceConfig.reconciling] field becomes false.



The returned long-running operation will have a name of the format `<instance_config_name>/operations/<operation_id>` and can be used to track the instance configuration modification. The metadata field type is [UpdateInstanceConfigMetadata][google.spanner.admin.instance.v1.UpdateInstanceConfigMetadata]. The response field type is [InstanceConfig][google.spanner.admin.instance.v1.InstanceConfig], if successful.

Authorization requires `spanner.instanceConfigs.update` permission on the resource [name][google.spanner.admin.instance.v1.InstanceConfig.name].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.UpdateInstanceConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateInstancePartition(UpdateInstancePartitionRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateInstancePartition(UpdateInstancePartitionRequest request, ServerCallContext context)

Updates an instance partition, and begins allocating or releasing resources as requested. The returned long-running operation can be used to track the progress of updating the instance partition. If the named instance partition does not exist, returns `NOT_FOUND`.

Immediately upon completion of this request:

  * For resource types for which a decrease in the instance partition's allocation has been requested, billing is based on the newly-requested level.



Until completion of the returned operation:

  * Cancelling the operation sets its metadata's [cancel_time][google.spanner.admin.instance.v1.UpdateInstancePartitionMetadata.cancel_time], and begins restoring resources to their pre-request values. The operation is guaranteed to succeed at undoing all resource changes, after which point it terminates with a `CANCELLED` status.
  * All other attempts to modify the instance partition are rejected.
  * Reading the instance partition via the API continues to give the pre-request resource levels.



Upon completion of the returned operation:

  * Billing begins for all successfully-allocated resources (some types may have lower than the requested levels).
  * All newly-reserved resources are available for serving the instance partition's tables.
  * The instance partition's new resource levels are readable via the API.



The returned long-running operation will have a name of the format `<instance_partition_name>/operations/<operation_id>` and can be used to track the instance partition modification. The metadata field type is [UpdateInstancePartitionMetadata][google.spanner.admin.instance.v1.UpdateInstancePartitionMetadata]. The response field type is [InstancePartition][google.spanner.admin.instance.v1.InstancePartition], if successful.

Authorization requires `spanner.instancePartitions.update` permission on the resource [name][google.spanner.admin.instance.v1.InstancePartition.name].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstancePartitionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.UpdateInstancePartitionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
