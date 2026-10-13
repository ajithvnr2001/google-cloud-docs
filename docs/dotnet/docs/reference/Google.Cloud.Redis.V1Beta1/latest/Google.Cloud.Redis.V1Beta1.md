---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1
title: Google Cloud Memorystore for Redis v1beta1 API - Namespace Google.Cloud.Redis.V1Beta1 (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:57.259689+00:00
---

# Google Cloud Memorystore for Redis v1beta1 API - Namespace Google.Cloud.Redis.V1Beta1 (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis v1beta1 API - Namespace Google.Cloud.Redis.V1Beta1 (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/3.0.0-beta05/Google.Cloud.Redis.V1Beta1)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/2.0.0-beta09/Google.Cloud.Redis.V1Beta1)



## Classes 

### [CloudRedis](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis)

Configures and manages Cloud Memorystore for Redis instances

Google Cloud Memorystore for Redis v1beta1

The `redis.googleapis.com` service implements the Google Cloud Memorystore for Redis API and defines the following resource model for managing Redis instances:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Redis instances, named: `/instances/*`
  * As such, Redis instances are resources of the form: `/projects/{project_id}/locations/{location_id}/instances/{instance_id}`



Note that location_id must be referring to a GCP `region`; for example:

  * `projects/redpepper-1290/locations/us-central1/instances/my-redis`



### [CloudRedis.CloudRedisBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisBase)

Base class for server-side implementations of CloudRedis

### [CloudRedis.CloudRedisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisClient)

Client for CloudRedis

### [CloudRedisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisClient)

CloudRedis client wrapper, for convenient use.

### [CloudRedisClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisClientBuilder)

Builder class for [CloudRedisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisClient) to provide simple configuration of credentials, endpoint etc.

### [CloudRedisClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisClientImpl)

CloudRedis client wrapper implementation, for convenient use.

### [CloudRedisSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisSettings)

Settings for [CloudRedisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisClient) instances.

### [CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CreateInstanceRequest)

Request for [CreateInstance][google.cloud.redis.v1beta1.CloudRedis.CreateInstance].

### [DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.DeleteInstanceRequest)

Request for [DeleteInstance][google.cloud.redis.v1beta1.CloudRedis.DeleteInstance].

### [ExportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ExportInstanceRequest)

Request for [Export][google.cloud.redis.v1beta1.CloudRedis.ExportInstance].

### [FailoverInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.FailoverInstanceRequest)

Request for [Failover][google.cloud.redis.v1beta1.CloudRedis.FailoverInstance].

### [FailoverInstanceRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.FailoverInstanceRequest.Types)

Container for nested types declared in the FailoverInstanceRequest message type.

### [GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GcsDestination)

The Cloud Storage location for the output content

### [GcsSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GcsSource)

The Cloud Storage location for the input content

### [GetInstanceAuthStringRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceAuthStringRequest)

Request for [GetInstanceAuthString][google.cloud.redis.v1beta1.CloudRedis.GetInstanceAuthString].

### [GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceRequest)

Request for [GetInstance][google.cloud.redis.v1beta1.CloudRedis.GetInstance].

### [ImportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ImportInstanceRequest)

Request for [Import][google.cloud.redis.v1beta1.CloudRedis.ImportInstance].

### [InputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InputConfig)

The input content

### [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)

A Memorystore for Redis instance.

### [Instance.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types)

Container for nested types declared in the Instance message type.

### [InstanceAuthString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceAuthString)

Instance AUTH string details.

### [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceName)

Resource name for the `Instance` resource.

### [ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest)

Request for [ListInstances][google.cloud.redis.v1beta1.CloudRedis.ListInstances].

### [ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesResponse)

Response for [ListInstances][google.cloud.redis.v1beta1.CloudRedis.ListInstances].

### [LocationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.LocationMetadata)

This location metadata represents additional configuration options for a given location where a Redis instance may be created. All fields are output only. It is returned as content of the `google.cloud.location.Location.metadata` field.

### [MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenancePolicy)

Maintenance policy for an instance.

### [MaintenanceSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenanceSchedule)

Upcoming maintenance schedule. If no maintenance is scheduled, fields are not populated.

### [NodeInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.NodeInfo)

Node specific properties.

### [OutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.OutputConfig)

The output content

### [PersistenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.PersistenceConfig)

Configuration of the persistence functionality.

### [PersistenceConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.PersistenceConfig.Types)

Container for nested types declared in the PersistenceConfig message type.

### [RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.RescheduleMaintenanceRequest)

Request for [RescheduleMaintenance][google.cloud.redis.v1beta1.CloudRedis.RescheduleMaintenance].

### [RescheduleMaintenanceRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.RescheduleMaintenanceRequest.Types)

Container for nested types declared in the RescheduleMaintenanceRequest message type.

### [TlsCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.TlsCertificate)

TlsCertificate Resource

### [UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpdateInstanceRequest)

Request for [UpdateInstance][google.cloud.redis.v1beta1.CloudRedis.UpdateInstance].

### [UpgradeInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpgradeInstanceRequest)

Request for [UpgradeInstance][google.cloud.redis.v1beta1.CloudRedis.UpgradeInstance].

### [WeeklyMaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.WeeklyMaintenanceWindow)

Time window in which disruptive maintenance updates occur. Non-disruptive updates can occur inside or outside this window.

### [ZoneMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ZoneMetadata)

Defines specific information for a particular zone. Currently empty and reserved for future use only.

## Enums 

### [FailoverInstanceRequest.Types.DataProtectionMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.FailoverInstanceRequest.Types.DataProtectionMode)

Specifies different modes of operation in relation to the data retention.

### [InputConfig.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InputConfig.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [Instance.Types.ConnectMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types.ConnectMode)

Available connection modes.

### [Instance.Types.ReadReplicasMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types.ReadReplicasMode)

Read replicas mode.

### [Instance.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types.State)

Represents the different states of a Redis instance.

### [Instance.Types.Tier](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types.Tier)

Available service tiers to choose from

### [Instance.Types.TransitEncryptionMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types.TransitEncryptionMode)

Available TLS modes.

### [InstanceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceName.ResourceNameType)

The possible contents of [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceName).

### [OutputConfig.DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.OutputConfig.DestinationOneofCase)

Enum of possible cases for the "destination" oneof.

### [PersistenceConfig.Types.PersistenceMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.PersistenceConfig.Types.PersistenceMode)

Available Persistence modes.

### [PersistenceConfig.Types.SnapshotPeriod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.PersistenceConfig.Types.SnapshotPeriod)

Available snapshot periods for scheduling.

### [RescheduleMaintenanceRequest.Types.RescheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.RescheduleMaintenanceRequest.Types.RescheduleType)

Reschedule options.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
