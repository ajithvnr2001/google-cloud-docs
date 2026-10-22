---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/operations/
title: Operations \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:50.476671+00:00
---

# Operations  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Operations Stay organized with collections  Save and categorize content based on your preferences. 

The Operations resource represents a [long-running operation](https://docs.cloud.google.com/storage/docs/using-long-running-operations) within Cloud Storage.

## Resource representations
    
    
    {
        "name": string,
        "metadata": {
          "@type": string,
          field1: ...,
          ...
        },
        "done": boolean,
    
        // Union field result can include either an error or a response:
        "error": {
          "code": integer,
          "message": string,
          "details": [
            {
              "@type": string,
              field1: ...,
              ...
            }
          ]
        },
        "response": {
          "@type": string,
          field1: ...,
          ...
        }
      }

Property name | Value | Description | Notes  
---|---|---|---  
`name` | `string` | The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{operation_id}`. |   
`metadata` | `object` | Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`. |   
`done` | `boolean` | If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. |   
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` | `object` | The error result of the operation in case of failure or cancellation. |   
`error.code` | `integer` | The status code, which should be an enum value of `google.rpc.Code`. |   
`error.message` | `string` | A developer-facing error message, which should be in English. |   
`error.details[]` | `object` | A list of messages that carry the error details. There is a common set of message types for APIs to use. An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`. |   
`response` | `object` | The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`. |   
  
## Methods

The methods for working with long-running operations are as follows:

[cancel](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/cancel)
    Starts asynchronous cancellation on a long-running operation.
[get](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/get)
    Gets the latest state of a long-running operation.
[list](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/list)
    Lists service operations that match the specified filter in the request.
[advanceRelocateBucket](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/advanceRelocateBucket)
    Initiates the [final synchronization](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#initiate-final-sync) of a bucket relocation operation. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
