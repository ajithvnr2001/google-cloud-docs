---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning
title: Package google.longrunning \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:11.847221+00:00
---

# Package google.longrunning  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Package google.longrunning Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Operations](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations)` (interface)
  * `[GetOperationRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.GetOperationRequest)` (message)
  * `[Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation)` (message)



## Operations

Manages long-running operations with an API service.

When an API method normally takes long time to complete, it can be designed to return `[Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation)` to the client, and the client can use this interface to receive the real response asynchronously by polling the operation resource, or pass the operation resource to another API (such as Pub/Sub API) to receive the response. Any API service that returns long-running operations should implement the `Operations` interface so developers can have a consistent client experience.

GetOperation  
---  
` rpc GetOperation(`[GetOperationRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.GetOperationRequest)`) returns (`[Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## GetOperationRequest

The request message for `[Operations.GetOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`.

Fields  
---  
`name` |  `string` The name of the operation resource.  
  
## Operation

This resource represents a long-running operation that is the result of a network API call.

Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.  
`done` |  `bool` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  `[Status](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Status)` The error result of the operation in case of failure or cancellation.  
`response` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
