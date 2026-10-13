---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1beta
title: Package google.cloud.edgecontainer.v1beta \u00a0|\u00a0 Google Distributed Cloud connected, version 1.6.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:33.969142+00:00
---

# Package google.cloud.edgecontainer.v1beta  |  Google Distributed Cloud connected, version 1.6.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1beta

Select versionkeyboard_arrow_down

  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
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
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/apis)



Send feedback 

#  Package google.cloud.edgecontainer.v1beta Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[LocationMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1beta#google.cloud.edgecontainer.v1beta.LocationMetadata)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1beta#google.cloud.edgecontainer.v1beta.OperationMetadata)` (message)
  * `[Quota](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1beta#google.cloud.edgecontainer.v1beta.Quota)` (message)
  * `[ZoneMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1beta#google.cloud.edgecontainer.v1beta.ZoneMetadata)` (message)



## LocationMetadata

Metadata for a given `[google.cloud.location.Location](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rpc/google.cloud.location#google.cloud.location.Location)`.

Fields  
---  
`available_zones` |  `map<string, `[ZoneMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1beta#google.cloud.edgecontainer.v1beta.ZoneMetadata)`>` The set of available Google Distributed Cloud Edge zones in the location. The map is keyed by the lowercase ID of each zone.  
  
## OperationMetadata

Long-running operation metadata for Edge Container API methods.

Fields  
---  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time the operation was created.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time the operation finished running.  
`target` |  `string` Server-defined resource path for the target of the operation.  
`verb` |  `string` The verb executed by the operation.  
`status_message` |  `string` Human-readable status of the operation, if any.  
`requested_cancellation` |  `bool` Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have [Operation.error][] value with a `[google.rpc.Status.code](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of 1, corresponding to `Code.CANCELLED`.  
`api_version` |  `string` API version used to start the operation.  
`warnings[]` |  `string` Warnings that do not block the operation, but still hold relevant information for the end user to receive.  
  
## Quota

Represents quota for Edge Container resources.

Fields  
---  
`metric` |  `string` Name of the quota metric.  
`limit` |  `double` Quota limit for this metric.  
`usage` |  `double` Current usage of this metric.  
  
## ZoneMetadata

A Google Distributed Cloud Edge zone where edge machines are located.

Fields  
---  
`quota[]` |  ``[Quota](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rpc/google.cloud.edgecontainer.v1beta#google.cloud.edgecontainer.v1beta.Quota)`` Quota for resources in this zone.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
