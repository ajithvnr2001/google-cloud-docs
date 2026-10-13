---
url: https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Operation
title: Google LongRunning Client - Class Operation (0.8.5) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:32.488980+00:00
---

# Google LongRunning Client - Class Operation (0.8.5)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/longrunning/latest/LongRunning.Operation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google LongRunning Client - Class Operation (0.8.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.5 (latest)  0.7.1  0.6.0  0.5.0  0.4.7  0.3.0  0.2.6 

Reference documentation and code samples for the Google LongRunning Client class Operation.

This resource represents a long-running operation that is the result of a network API call.

Generated from protobuf message `google.longrunning.Operation`

## Namespace

Google \ LongRunning

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`↳ metadata` |  `Google\Protobuf\Any`   
Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.  
`↳ done` |  `bool`   
If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
`↳ error` |  `Google\Rpc\Status`   
The error result of the operation in case of failure or cancellation.  
`↳ response` |  `Google\Protobuf\Any`   
The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.  
  
### getName

The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetadata

Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time.

Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Any|null` |   
  
### hasMetadata

### clearMetadata

### setMetadata

Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time.

Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Any`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDone

If the value is `false`, it means the operation is still in progress.

If `true`, the operation is completed, and either `error` or `response` is available.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setDone

If the value is `false`, it means the operation is still in progress.

If `true`, the operation is completed, and either `error` or `response` is available.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getError

The error result of the operation in case of failure or cancellation.

**Returns**  
---  
**Type** | **Description**  
`Google\Rpc\Status|null` |   
  
### hasError

### setError

The error result of the operation in case of failure or cancellation.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Rpc\Status`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResponse

The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Any|null` |   
  
### hasResponse

### setResponse

The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Any`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResult

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
