---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations
title: REST Resource: projects.locations.operations \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:38.541647+00:00
---

# REST Resource: projects.locations.operations  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  REST Resource: projects.locations.operations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Operation
    * JSON representation
  * Methods



## Resource: Operation

This resource represents a long-running operation that is the result of a network API call.

JSON representation  
---  
      
    
    {
      "name": string,
      "metadata": {
        "@type": string,
        field1: ...,
        ...
      },
      "done": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "error": {
        object ([Status](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "response": {
        "@type": string,
        field1: ...,
        ...
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{uniqueId}`.  
`metadata` |  `object` {`createTime`: The time the operation was created.`endTime`: The time the operation finished running.`target`: Server-defined resource path for the target of the operation.`verb`: Name of the verb executed by the operation.`statusDetail`: Human-readable status of the operation, if any.`cancelRequested`: Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have `[Operation.error](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/ListOperationsResponse#Status.FIELDS.code)` of 1, corresponding to `Code.CANCELLED`.`apiVersion`: API version used to start the operation.}  
`done` |  `boolean` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`error` |  `object (`[Status](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The error result of the operation in case of failure or cancellation.  
`response` |  `object` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations/cancel)`

|  Starts asynchronous cancellation on a long-running operation.  
  
### `[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations/delete)`

|  Deletes a long-running operation.  
  
### `[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations/get)`

|  Gets the latest state of a long-running operation.  
  
### `[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations/list)`

|  Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
