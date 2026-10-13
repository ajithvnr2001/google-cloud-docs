---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.common
title: Package google.cloud.common \u00a0|\u00a0 Google Distributed Cloud connected, version 1.6.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:23.354019+00:00
---

# Package google.cloud.common  |  Google Distributed Cloud connected, version 1.6.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.common

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
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/apis)



Send feedback 

#  Package google.cloud.common Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[OperationMetadata](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.cloud.common#google.cloud.common.OperationMetadata)` (message)



## OperationMetadata

Represents the metadata of the long-running operation.

Fields  
---  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time the operation was created.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The time the operation finished running.  
`target` |  `string` Output only. Server-defined resource path for the target of the operation.  
`verb` |  `string` Output only. Name of the verb executed by the operation.  
`status_detail` |  `string` Output only. Human-readable status of the operation, if any.  
`cancel_requested` |  `bool` Output only. Identifies whether the user has requested cancellation of the operation. Operations that have been cancelled successfully have [Operation.error][] value with a `[google.rpc.Status.code](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/container/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of 1, corresponding to `Code.CANCELLED`.  
`api_version` |  `string` Output only. API version used to start the operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
