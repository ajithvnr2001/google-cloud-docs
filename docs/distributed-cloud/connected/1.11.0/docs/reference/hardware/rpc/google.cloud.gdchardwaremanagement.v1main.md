---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rpc/google.cloud.gdchardwaremanagement.v1main
title: Package google.cloud.gdchardwaremanagement.v1main \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:19.804879+00:00
---

# Package google.cloud.gdchardwaremanagement.v1main  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rpc/google.cloud.gdchardwaremanagement.v1main




#  Package google.cloud.gdchardwaremanagement.v1main Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[OperationMetadata](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rpc/google.cloud.gdchardwaremanagement.v1main#google.cloud.gdchardwaremanagement.v1main.OperationMetadata)` (message)



## OperationMetadata

Represents the metadata of a long-running operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`target` |  `string` Output only. Server-defined resource path for the target of the operation.  
`verb` |  `string` Output only. The verb executed by the operation.  
`status_message` |  `string` Output only. Human-readable status of the operation, if any.  
`requested_cancellation` |  `bool` Output only. Identifies whether the user has requested cancellation of the operation. Operations that have been cancelled successfully have [Operation.error][] value with a `[google.rpc.Status.code](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of 1, corresponding to `Code.CANCELLED`.  
`api_version` |  `string` Output only. API version used to start the operation.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
