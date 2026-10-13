---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2
title: Google Cloud Memorystore for Memcached v1beta2 API - Namespace Google.Cloud.Memcache.V1Beta2 (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:11.438161+00:00
---

# Google Cloud Memorystore for Memcached v1beta2 API - Namespace Google.Cloud.Memcache.V1Beta2 (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Memcached v1beta2 API - Namespace Google.Cloud.Memcache.V1Beta2 (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/2.0.0-beta06/Google.Cloud.Memcache.V1Beta2)
  * [ 1.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/1.0.0-beta05/Google.Cloud.Memcache.V1Beta2)



## Classes 

### [ApplyParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.ApplyParametersRequest)

Request for [ApplyParameters][google.cloud.memcache.v1beta2.CloudMemcache.ApplyParameters].

### [ApplySoftwareUpdateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.ApplySoftwareUpdateRequest)

Request for [ApplySoftwareUpdate][google.cloud.memcache.v1beta2.CloudMemcache.ApplySoftwareUpdate].

### [CloudMemcache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcache)

Configures and manages Cloud Memorystore for Memcached instances.

The `memcache.googleapis.com` service implements the Google Cloud Memorystore for Memcached API and defines the following resource model for managing Memorystore Memcached (also called Memcached below) instances:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Memcached instances, named: `/instances/*`
  * As such, Memcached instances are resources of the form: `/projects/{project_id}/locations/{location_id}/instances/{instance_id}`



Note that location_id must be a GCP `region`; for example:

  * `projects/my-memcached-project/locations/us-central1/instances/my-memcached`



### [CloudMemcache.CloudMemcacheBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcache.CloudMemcacheBase)

Base class for server-side implementations of CloudMemcache

### [CloudMemcache.CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcache.CloudMemcacheClient)

Client for CloudMemcache

### [CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcacheClient)

CloudMemcache client wrapper, for convenient use.

### [CloudMemcacheClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcacheClientBuilder)

Builder class for [CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcacheClient) to provide simple configuration of credentials, endpoint etc.

### [CloudMemcacheClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcacheClientImpl)

CloudMemcache client wrapper implementation, for convenient use.

### [CloudMemcacheSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcacheSettings)

Settings for [CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcacheClient) instances.

### [CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CreateInstanceRequest)

Request for [CreateInstance][google.cloud.memcache.v1beta2.CloudMemcache.CreateInstance].

### [DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.DeleteInstanceRequest)

Request for [DeleteInstance][google.cloud.memcache.v1beta2.CloudMemcache.DeleteInstance].

### [GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.GetInstanceRequest)

Request for [GetInstance][google.cloud.memcache.v1beta2.CloudMemcache.GetInstance].

### [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.Instance)

A Memorystore for Memcached instance

### [Instance.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.Instance.Types)

Container for nested types declared in the Instance message type.

### [Instance.Types.InstanceMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.Instance.Types.InstanceMessage)

### [Instance.Types.InstanceMessage.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.Instance.Types.InstanceMessage.Types)

Container for nested types declared in the InstanceMessage message type.

### [Instance.Types.Node](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.Instance.Types.Node)

### [Instance.Types.Node.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.Instance.Types.Node.Types)

Container for nested types declared in the Node message type.

### [Instance.Types.NodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.Instance.Types.NodeConfig)

Configuration for a Memcached Node.

### [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.InstanceName)

Resource name for the `Instance` resource.

### [ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.ListInstancesRequest)

Request for [ListInstances][google.cloud.memcache.v1beta2.CloudMemcache.ListInstances].

### [ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.ListInstancesResponse)

Response for [ListInstances][google.cloud.memcache.v1beta2.CloudMemcache.ListInstances].

### [LocationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.LocationMetadata)

Metadata for the given [google.cloud.location.Location][google.cloud.location.Location].

### [MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.MaintenancePolicy)

Maintenance policy per instance.

### [MaintenanceSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.MaintenanceSchedule)

Upcoming maintenance schedule.

### [MemcacheParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.MemcacheParameters)

### [OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.OperationMetadata)

Represents the metadata of a long-running operation.

### [RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.RescheduleMaintenanceRequest)

Request for [RescheduleMaintenance][google.cloud.memcache.v1beta2.CloudMemcache.RescheduleMaintenance].

### [RescheduleMaintenanceRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.RescheduleMaintenanceRequest.Types)

Container for nested types declared in the RescheduleMaintenanceRequest message type.

### [UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.UpdateInstanceRequest)

Request for [UpdateInstance][google.cloud.memcache.v1beta2.CloudMemcache.UpdateInstance].

### [UpdateParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.UpdateParametersRequest)

Request for [UpdateParameters][google.cloud.memcache.v1beta2.CloudMemcache.UpdateParameters].

### [WeeklyMaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.WeeklyMaintenanceWindow)

Time window specified for weekly operations.

### [ZoneMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.ZoneMetadata)

## Enums 

### [Instance.Types.InstanceMessage.Types.Code](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.Instance.Types.InstanceMessage.Types.Code)

### [Instance.Types.Node.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.Instance.Types.Node.Types.State)

Different states of a Memcached node.

### [Instance.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.Instance.Types.State)

Different states of a Memcached instance.

### [InstanceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.InstanceName.ResourceNameType)

The possible contents of [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.InstanceName).

### [MemcacheVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.MemcacheVersion)

Memcached versions supported by our service.

### [RescheduleMaintenanceRequest.Types.RescheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.RescheduleMaintenanceRequest.Types.RescheduleType)

Reschedule options.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
