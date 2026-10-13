---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main
title: Package google.cloud.edgecontainer.v1main \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:21.352084+00:00
---

# Package google.cloud.edgecontainer.v1main  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/apis)



Send feedback 

#  Package google.cloud.edgecontainer.v1main Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[ConfigData](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ConfigData)` (message)
  * `[LocationMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.LocationMetadata)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.OperationMetadata)` (message)
  * `[OperationMetadata.StatusReason](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.OperationMetadata.StatusReason)` (enum)
  * `[Quota](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.Quota)` (message)
  * `[ZonalService](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ZonalService)` (message)
  * `[ZonalService.ServiceSelector](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ZonalService.ServiceSelector)` (enum)
  * `[ZonalService.State](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ZonalService.State)` (enum)
  * `[ZoneMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ZoneMetadata)` (message)
  * `[ZoneMetadata.RackType](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ZoneMetadata.RackType)` (enum)



## ConfigData

Config data holds all the config related data for the zone.

Fields  
---  
`available_external_lb_pools_ipv4[]` |  `string` list of available v4 ip pools for external loadbalancer  
`available_external_lb_pools_ipv6[]` |  `string` list of available v6 ip pools for external loadbalancer  
  
## LocationMetadata

Metadata for a given `[google.cloud.location.Location](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.location#google.cloud.location.Location)`.

Fields  
---  
`available_zones` |  `map<string, `[ZoneMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ZoneMetadata)`>` The set of available Google Distributed Cloud Edge zones in the location. The map is keyed by the lowercase ID of each zone.  
  
## OperationMetadata

Long-running operation metadata for Edge Container API methods.

Fields  
---  
`create_time` |  ``[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`` The time the operation was created.  
`end_time` |  ``[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`` The time the operation finished running.  
`target` |  `string` Server-defined resource path for the target of the operation.  
`verb` |  `string` The verb executed by the operation.  
`status_message` |  `string` Human-readable status of the operation, if any.  
`requested_cancellation` |  `bool` Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have [Operation.error][] value with a `[google.rpc.Status.code](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of 1, corresponding to `Code.CANCELLED`.  
`api_version` |  `string` API version used to start the operation.  
`warnings[]` |  `string` Warnings that do not block the operation, but still hold relevant information for the end user to receive.  
`status_reason` |  ``[StatusReason](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.OperationMetadata.StatusReason)`` Machine-readable status of the operation, if any.  
  
## StatusReason

Indicates the reason for the status of the operation.

Enums  
---  
`STATUS_REASON_UNSPECIFIED` | Reason unknown.  
`UPGRADE_PAUSED` | The cluster upgrade is currently paused.  
  
## Quota

Represents quota for Edge Container resources.

Fields  
---  
`metric` |  `string` Name of the quota metric.  
`limit` |  `double` Quota limit for this metric.  
`usage` |  `double` Current usage of this metric.  
  
## ZonalService

Service enabled on the project.

Fields  
---  
`name` |  `string` Identifier. The resource name of the service.  
`service_selector` |  ``[ServiceSelector](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ZonalService.ServiceSelector)`` Required. The service to enable/disable.  
`state` |  ``[State](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ZonalService.State)`` Output only. The state of the service.  
`create_time` |  ``[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`` Output only. The time when the service was enabled.  
`update_time` |  ``[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`` Output only. The time when the service was last updated.  
`labels` |  `map<string, string>` Optional. Labels associated with this resource.  
Union field `zone_or_cluster`. The zone or cluster on which the service has to be enabled/disabled. `zone_or_cluster` can be only one of the following:  
`zone` |  `string` The zone on which the service has to be enabled/disabled.  
`cluster` |  `string` The fully qualified name of the cluster on which the service has to be enabled/disabled.  
  
## ServiceSelector

Services that can be enabled/disabled.

Enums  
---  
`SERVICE_SELECTOR_UNSPECIFIED` | Unspecified.  
`ALLOYDB` | AlloyDB service, alloydb.googleapis.com.  
`VMM` | VMM service, gdcvmmanager.googleapis.com.  
  
## State

The state of the service.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified.  
`STATE_ENABLED` | The service is enabled on the project.  
`STATE_DISABLED` | The service is disabled on the project.  
`STATE_ENABLING` | The service is being enabled on the project.  
`STATE_DISABLING` | The service is being disabled on the project.  
  
## ZoneMetadata

A Google Distributed Cloud Edge zone where edge machines are located.

Fields  
---  
`quota[]` |  ``[Quota](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.Quota)`` Quota for resources in this zone.  
`rack_types` |  `map<string, `[RackType](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ZoneMetadata.RackType)`>` The map keyed by rack name and has value of RackType.  
`config_data` |  ``[ConfigData](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1main#google.cloud.edgecontainer.v1main.ConfigData)`` Config data for the zone.  
  
## RackType

Type of the rack.

Enums  
---  
`RACK_TYPE_UNSPECIFIED` | Unspecified rack type, single rack also belongs to this type.  
`BASE` | Base rack type, a pair of two modified Config-1 racks containing Aggregation switches.  
`EXPANSION` | Expansion rack type, also known as standalone racks, added by customers on demand.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
