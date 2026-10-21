---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning
title: Package google.longrunning \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:50.332590+00:00
---

# Package google.longrunning  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Package google.longrunning Stay organized with collections  Save and categorize content based on your preferences. 

Important: To access the URL listed within parentheses, you must connect to the internet. The URL is provided to access outside of your air-gapped environment. 

## Operations

Manages long-running operations with an API service.

When an API method normally takes long time to complete, it can be designed to return `[Operation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operation)` to the client, and the client can use this interface to receive the real response asynchronously by polling the operation resource, or pass the operation resource to another API (such as Google Cloud Pub/Sub API) to receive the response. Any API service that returns long-running operations should implement the `Operations` interface so developers can have a consistent client experience.

GetOperation  
---  
` rpc GetOperation(`[GetOperationRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.GetOperationRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operation)`) ` Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.  
ListOperations  
---  
` rpc ListOperations(`[ListOperationsRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.ListOperationsRequest)`) returns (`[ListOperationsResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.ListOperationsResponse)`) ` Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.  
  
## GetOperationRequest

The request message for `[Operations.GetOperation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`.

Fields  
---  
`name` |  `string` The name of the operation resource.  
  
## ListOperationsRequest

The request message for `[Operations.ListOperations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`.

Fields  
---  
`name` |  `string` The name of the operation's parent resource.  
`filter` |  `string` The standard list filter.  
`page_size` |  `int32` The standard list page size.  
`page_token` |  `string` The standard list page token.  
  
## ListOperationsResponse

The response message for `[Operations.ListOperations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`.

Fields  
---  
`operations[]` |  ``[Operation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operation)`` A list of operations that matches the specified filter in the request.  
`next_page_token` |  `string` The standard List next-page token.  
  
## Operation

This resource represents a long-running operation that is the result of a network API call.

Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  ``Any (https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.  
`done` |  `bool` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` may be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  ``Status (/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.rpc#google.rpc.Status)`` The error result of the operation in case of failure or cancellation.  
`response` |  ``Any (https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` The normal response of the operation in case of success. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
