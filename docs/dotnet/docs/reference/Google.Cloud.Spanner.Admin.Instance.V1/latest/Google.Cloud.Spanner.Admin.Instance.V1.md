---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1
title: Google Cloud Spanner Instance Administration v1 API - Namespace Google.Cloud.Spanner.Admin.Instance.V1 (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:20.324094+00:00
---

# Google Cloud Spanner Instance Administration v1 API - Namespace Google.Cloud.Spanner.Admin.Instance.V1 (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner Instance Administration v1 API - Namespace Google.Cloud.Spanner.Admin.Instance.V1 (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 

## Classes 

### [AutoscalingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig)

Autoscaling configuration for an instance.

### [AutoscalingConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types)

Container for nested types declared in the AutoscalingConfig message type.

### [AutoscalingConfig.Types.AsymmetricAutoscalingOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption)

AsymmetricAutoscalingOption specifies the scaling of replicas identified by the given selection.

### [AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types)

Container for nested types declared in the AsymmetricAutoscalingOption message type.

### [AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides)

Overrides the top-level autoscaling configuration for the replicas identified by `replica_selection`. All fields in this message are optional. Any unspecified fields will use the corresponding values from the top-level autoscaling configuration.

### [AutoscalingConfig.Types.AutoscalingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AutoscalingLimits)

The autoscaling limits for the instance. Users can define the minimum and maximum compute capacity allocated to the instance, and the autoscaler will only scale within that range. Users can either use nodes or processing units to specify the limits, but should use the same unit to set both the min_limit and max_limit.

### [AutoscalingConfig.Types.AutoscalingTargets](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AutoscalingTargets)

The autoscaling targets for an instance.

### [CreateInstanceConfigMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.CreateInstanceConfigMetadata)

Metadata type for the operation returned by [CreateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstanceConfig].

### [CreateInstanceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.CreateInstanceConfigRequest)

The request for [CreateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstanceConfig].

### [CreateInstanceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.CreateInstanceMetadata)

Metadata type for the operation returned by [CreateInstance][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstance].

### [CreateInstancePartitionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.CreateInstancePartitionMetadata)

Metadata type for the operation returned by [CreateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstancePartition].

### [CreateInstancePartitionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.CreateInstancePartitionRequest)

The request for [CreateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstancePartition].

### [CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.CreateInstanceRequest)

The request for [CreateInstance][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstance].

### [DeleteInstanceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.DeleteInstanceConfigRequest)

The request for [DeleteInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.DeleteInstanceConfig].

### [DeleteInstancePartitionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.DeleteInstancePartitionRequest)

The request for [DeleteInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.DeleteInstancePartition].

### [DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.DeleteInstanceRequest)

The request for [DeleteInstance][google.spanner.admin.instance.v1.InstanceAdmin.DeleteInstance].

### [FreeInstanceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.FreeInstanceMetadata)

Free instance specific metadata that is kept even after an instance has been upgraded for tracking purposes.

### [FreeInstanceMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.FreeInstanceMetadata.Types)

Container for nested types declared in the FreeInstanceMetadata message type.

### [GetInstanceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceConfigRequest)

The request for [GetInstanceConfigRequest][google.spanner.admin.instance.v1.InstanceAdmin.GetInstanceConfig].

### [GetInstancePartitionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstancePartitionRequest)

The request for [GetInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.GetInstancePartition].

### [GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceRequest)

The request for [GetInstance][google.spanner.admin.instance.v1.InstanceAdmin.GetInstance].

### [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance)

An isolated set of Cloud Spanner resources on which databases can be hosted.

### [Instance.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types)

Container for nested types declared in the Instance message type.

### [InstanceAdmin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdmin)

Cloud Spanner Instance Admin API

The Cloud Spanner Instance Admin API can be used to create, delete, modify and list instances. Instances are dedicated Cloud Spanner serving and storage resources to be used by Cloud Spanner databases.

Each instance has a "configuration", which dictates where the serving resources for the Cloud Spanner instance are located (e.g., US-central, Europe). Configurations are created by Google based on resource availability.

Cloud Spanner billing is based on the instances that exist and their sizes. After an instance exists, there are no additional per-database or per-operation charges for use of the instance (though there may be additional network bandwidth charges). Instances offer isolation: problems with databases in one instance will not affect other instances. However, within an instance databases can affect each other. For example, if one database in an instance receives a lot of requests and consumes most of the instance resources, fewer resources are available for other databases in that instance, and their performance may suffer.

### [InstanceAdmin.InstanceAdminBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdmin.InstanceAdminBase)

Base class for server-side implementations of InstanceAdmin

### [InstanceAdmin.InstanceAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdmin.InstanceAdminClient)

Client for InstanceAdmin

### [InstanceAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient)

InstanceAdmin client wrapper, for convenient use.

### [InstanceAdminClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClientBuilder)

Builder class for [InstanceAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient) to provide simple configuration of credentials, endpoint etc.

### [InstanceAdminClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClientImpl)

InstanceAdmin client wrapper implementation, for convenient use.

### [InstanceAdminSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminSettings)

Settings for [InstanceAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient) instances.

### [InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfig)

A possible configuration for a Cloud Spanner instance. Configurations define the geographic placement of nodes and their replication.

### [InstanceConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfig.Types)

Container for nested types declared in the InstanceConfig message type.

### [InstanceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfigName)

Resource name for the `InstanceConfig` resource.

### [InstancePartition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstancePartition)

An isolated set of Cloud Spanner resources that databases can define placements on.

### [InstancePartition.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstancePartition.Types)

Container for nested types declared in the InstancePartition message type.

### [InstancePartitionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstancePartitionName)

Resource name for the `InstancePartition` resource.

### [ListInstanceConfigOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigOperationsRequest)

The request for [ListInstanceConfigOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigOperations].

### [ListInstanceConfigOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigOperationsResponse)

The response for [ListInstanceConfigOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigOperations].

### [ListInstanceConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsRequest)

The request for [ListInstanceConfigs][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs].

### [ListInstanceConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsResponse)

The response for [ListInstanceConfigs][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs].

### [ListInstancePartitionOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancePartitionOperationsRequest)

The request for [ListInstancePartitionOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitionOperations].

### [ListInstancePartitionOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancePartitionOperationsResponse)

The response for [ListInstancePartitionOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitionOperations].

### [ListInstancePartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancePartitionsRequest)

The request for [ListInstancePartitions][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitions].

### [ListInstancePartitionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancePartitionsResponse)

The response for [ListInstancePartitions][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitions].

### [ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesRequest)

The request for [ListInstances][google.spanner.admin.instance.v1.InstanceAdmin.ListInstances].

### [ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesResponse)

The response for [ListInstances][google.spanner.admin.instance.v1.InstanceAdmin.ListInstances].

### [MoveInstanceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.MoveInstanceMetadata)

Metadata type for the operation returned by [MoveInstance][google.spanner.admin.instance.v1.InstanceAdmin.MoveInstance].

### [MoveInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.MoveInstanceRequest)

The request for [MoveInstance][google.spanner.admin.instance.v1.InstanceAdmin.MoveInstance].

### [MoveInstanceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.MoveInstanceResponse)

The response for [MoveInstance][google.spanner.admin.instance.v1.InstanceAdmin.MoveInstance].

### [OperationProgress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.OperationProgress)

Encapsulates progress related information for a Cloud Spanner long running instance operations.

### [ReplicaComputeCapacity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ReplicaComputeCapacity)

ReplicaComputeCapacity describes the amount of server resources that are allocated to each replica identified by the replica selection.

### [ReplicaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ReplicaInfo)

### [ReplicaInfo.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ReplicaInfo.Types)

Container for nested types declared in the ReplicaInfo message type.

### [ReplicaSelection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ReplicaSelection)

ReplicaSelection identifies replicas with common properties.

### [UpdateInstanceConfigMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.UpdateInstanceConfigMetadata)

Metadata type for the operation returned by [UpdateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstanceConfig].

### [UpdateInstanceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.UpdateInstanceConfigRequest)

The request for [UpdateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstanceConfig].

### [UpdateInstanceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.UpdateInstanceMetadata)

Metadata type for the operation returned by [UpdateInstance][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstance].

### [UpdateInstancePartitionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.UpdateInstancePartitionMetadata)

Metadata type for the operation returned by [UpdateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstancePartition].

### [UpdateInstancePartitionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.UpdateInstancePartitionRequest)

The request for [UpdateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstancePartition].

### [UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.UpdateInstanceRequest)

The request for [UpdateInstance][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstance].

## Enums 

### [AutoscalingConfig.Types.AutoscalingLimits.MaxLimitOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AutoscalingLimits.MaxLimitOneofCase)

Enum of possible cases for the "max_limit" oneof.

### [AutoscalingConfig.Types.AutoscalingLimits.MinLimitOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AutoscalingLimits.MinLimitOneofCase)

Enum of possible cases for the "min_limit" oneof.

### [FreeInstanceMetadata.Types.ExpireBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.FreeInstanceMetadata.Types.ExpireBehavior)

Allows users to change behavior when a free instance expires.

### [FulfillmentPeriod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.FulfillmentPeriod)

Indicates the expected fulfillment period of an operation.

### [Instance.Types.DefaultBackupScheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.DefaultBackupScheduleType)

Indicates the [default backup schedule](https://cloud.google.com/spanner/docs/backup#default-backup-schedules) behavior for new databases within the instance.

### [Instance.Types.Edition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.Edition)

The edition selected for this instance. Different editions provide different capabilities at different price points.

### [Instance.Types.InstanceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.InstanceType)

The type of this instance. The type can be used to distinguish product variants, that can affect aspects like: usage restrictions, quotas and billing. Currently this is used to distinguish FREE_INSTANCE vs PROVISIONED instances.

### [Instance.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.State)

Indicates the current state of the instance.

### [InstanceConfig.Types.FreeInstanceAvailability](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfig.Types.FreeInstanceAvailability)

Describes the availability for free instances to be created in an instance configuration.

### [InstanceConfig.Types.QuorumType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfig.Types.QuorumType)

Indicates the quorum type of this instance configuration.

### [InstanceConfig.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfig.Types.State)

Indicates the current state of the instance configuration.

### [InstanceConfig.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfig.Types.Type)

The type of this configuration.

### [InstanceConfigName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfigName.ResourceNameType)

The possible contents of [InstanceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfigName).

### [InstancePartition.ComputeCapacityOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstancePartition.ComputeCapacityOneofCase)

Enum of possible cases for the "compute_capacity" oneof.

### [InstancePartition.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstancePartition.Types.State)

Indicates the current state of the instance partition.

### [InstancePartitionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstancePartitionName.ResourceNameType)

The possible contents of [InstancePartitionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstancePartitionName).

### [ReplicaComputeCapacity.ComputeCapacityOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ReplicaComputeCapacity.ComputeCapacityOneofCase)

Enum of possible cases for the "compute_capacity" oneof.

### [ReplicaInfo.Types.ReplicaType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ReplicaInfo.Types.ReplicaType)

Indicates the type of replica. See the [replica types documentation](https://cloud.google.com/spanner/docs/replication#replica_types) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
