---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rpc/google.longrunning
title: Package google.longrunning \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:38:14.949436+00:00
---

# Package google.longrunning  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rpc/google.longrunning

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Reference ](https://docs.cloud.google.com/spectrum-access-system/docs/apis)



Send feedback 

#  Package google.longrunning Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Operation](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rpc/google.longrunning#google.longrunning.Operation)` (message)



## Operation

This resource represents a long-running operation that is the result of a network API call.

Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  ``[Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.  
`done` |  `bool` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` is set. `result` can be only one of the following:  
`error` |  ``[Status](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rpc/google.rpc#google.rpc.Status)`` The error result of the operation in case of failure or cancellation.  
`response` |  ``[Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` The normal response of the operation in case of success. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
