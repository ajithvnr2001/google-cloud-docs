---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning
title: Package google.longrunning \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:30:28.729397+00:00
---

# Package google.longrunning  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Package google.longrunning Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Operations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operations)` (interface)
  * `[GetOperationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.GetOperationRequest)` (message)
  * `[ListOperationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.ListOperationsRequest)` (message)
  * `[ListOperationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.ListOperationsResponse)` (message)
  * `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operation)` (message)



## Operations

Manages long-running operations with an API service.

When an API method normally takes long time to complete, it can be designed to return `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operation)` to the client, and the client can use this interface to receive the real response asynchronously by polling the operation resource, or pass the operation resource to another API (such as Pub/Sub API) to receive the response. Any API service that returns long-running operations should implement the `Operations` interface so developers can have a consistent client experience.

GetOperation  
---  
` rpc GetOperation(`[GetOperationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.GetOperationRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `retail.operations.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListOperations  
---  
` rpc ListOperations(`[ListOperationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.ListOperationsRequest)`) returns (`[ListOperationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.ListOperationsResponse)`) ` Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `retail.operations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## GetOperationRequest

The request message for `[Operations.GetOperation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`.

Fields  
---  
`name` |  `string` The name of the operation resource.  
  
## ListOperationsRequest

The request message for `[Operations.ListOperations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`.

Fields  
---  
`name` |  `string` The name of the operation's parent resource.  
`filter` |  `string` The standard list filter.  
`page_size` |  `int32` The standard list page size.  
`page_token` |  `string` The standard list page token.  
`return_partial_success` |  `bool` When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the `[ListOperationsResponse.unreachable](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.ListOperationsResponse.FIELDS.repeated.string.google.longrunning.ListOperationsResponse.unreachable)` field.This can only be `true` when reading across collections. For example, when `parent` is set to `"projects/example/locations/-"`.This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.  
  
## ListOperationsResponse

The response message for `[Operations.ListOperations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`.

Fields  
---  
`operations[]` |  `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.longrunning#google.longrunning.Operation)` A list of operations that matches the specified filter in the request.  
`next_page_token` |  `string` The standard List next-page token.  
`unreachable[]` |  `string` Unordered list. Unreachable resources. Populated when the request sets `ListOperationsRequest.return_partial_success` and reads across collections. For example, when attempting to list all resources across all supported locations.  
  
## Operation

This resource represents a long-running operation that is the result of a network API call.

Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.  
`done` |  `bool` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.rpc#google.rpc.Status)` The error result of the operation in case of failure or cancellation.  
`response` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
