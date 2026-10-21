---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning
title: Package google.longrunning \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:32.425726+00:00
---

# Package google.longrunning  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Package google.longrunning Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Operations](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operations)` (interface)
  * `[GetOperationRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.GetOperationRequest)` (message)
  * `[ListOperationsRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.ListOperationsRequest)` (message)
  * `[ListOperationsResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.ListOperationsResponse)` (message)
  * `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)` (message)
  * `[OperationInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.OperationInfo)` (message)
  * `[WaitOperationRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.WaitOperationRequest)` (message)



## Operations

Manages long-running operations with an API service.

When an API method normally takes long time to complete, it can be designed to return `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)` to the client, and the client can use this interface to receive the real response asynchronously by polling the operation resource, or pass the operation resource to another API (such as Google Cloud Pub/Sub API) to receive the response. Any API service that returns long-running operations should implement the `Operations` interface so developers can have a consistent client experience.

GetOperation  
---  
` rpc GetOperation(`[GetOperationRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.GetOperationRequest)`) returns (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListOperations  
---  
` rpc ListOperations(`[ListOperationsRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.ListOperationsRequest)`) returns (`[ListOperationsResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.ListOperationsResponse)`) ` Lists service operations that match the specified filter in the request.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
WaitOperation  
---  
` rpc WaitOperation(`[WaitOperationRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.WaitOperationRequest)`) returns (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state. If the operation is already done, the latest state is immediately returned. If the timeout specified is greater than the default HTTP/RPC timeout, the HTTP/RPC timeout is used. If the server does not support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Note that this method is on a best-effort basis. It may return the latest state before the specified timeout (including immediately), meaning even an immediate response is no guarantee that the operation is done.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## GetOperationRequest

The request message for `[Operations.GetOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`.

Fields  
---  
`name` |  `string` The name of the operation resource.  
  
## ListOperationsRequest

The request message for `[Operations.ListOperations](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`.

Fields  
---  
`name` |  `string` Not used.  
`filter` |  `string` A string for filtering `[Operations](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`. The following filter fields are supported:

  * serviceName: Required. Only `=` operator is allowed.
  * startTime: The time this job was started, in ISO 8601 format. Allowed operators are `>=`, `>`, `<=`, and `<`.
  * status: Can be `done`, `in_progress`, or `failed`. Allowed operators are `=`, and `!=`.

Filter expression supports conjunction (AND) and disjunction (OR) logical operators. However, the serviceName restriction must be at the top-level and can only be combined with other restrictions via the AND logical operator.Examples:

  * `serviceName={some-service}.googleapis.com`
  * `serviceName={some-service}.googleapis.com AND startTime>="2017-02-01"`
  * `serviceName={some-service}.googleapis.com AND status=done`
  * `serviceName={some-service}.googleapis.com AND (status=done OR startTime>="2017-02-01")`

  
`page_size` |  `int32` The maximum number of operations to return. If unspecified, defaults to 50. The maximum value is 100.  
`page_token` |  `string` The standard list page token.  
  
## ListOperationsResponse

The response message for `[Operations.ListOperations](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`.

Fields  
---  
`operations[]` |  ``[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`` A list of operations that matches the specified filter in the request.  
`next_page_token` |  `string` The standard List next-page token.  
  
## Operation

This resource represents a long-running operation that is the result of a network API call.

Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  ``[Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.  
`done` |  `bool` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` may be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  ``[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.rpc#google.rpc.Status)`` The error result of the operation in case of failure or cancellation.  
`response` |  ``[Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` The normal response of the operation in case of success. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.  
  
## OperationInfo

A message representing the message types used by a long-running operation.

Example:
    
    
    rpc Export(ExportRequest) returns (google.longrunning.Operation) {
      option (google.longrunning.operation_info) = {
        response_type: "ExportResponse"
        metadata_type: "ExportMetadata"
      };
    }
    

Fields  
---  
`response_type` |  `string` Required. The message name of the primary return type for this long-running operation. This type will be used to deserialize the LRO's response.If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. `google.protobuf.Struct`).Note: Altering this value constitutes a breaking change.  
`metadata_type` |  `string` Required. The message name of the metadata type for this long-running operation.If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. `google.protobuf.Struct`).Note: Altering this value constitutes a breaking change.  
  
## WaitOperationRequest

The request message for `[Operations.WaitOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operations.WaitOperation)`.

Fields  
---  
`name` |  `string` The name of the operation resource to wait on.  
`timeout` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` The maximum duration to wait before timing out. If left blank, the wait will be at most the time permitted by the underlying HTTP/RPC protocol. If RPC context deadline is also specified, the shorter one will be used.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
