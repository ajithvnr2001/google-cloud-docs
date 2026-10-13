---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations/cancel/
title: Method: projects.locations.operations.cancel \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:12.697369+00:00
---

# Method: projects.locations.operations.cancel  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations/cancel/




#  Method: projects.locations.operations.cancel Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use `[Operations.GetOperation](https://docs.cloud.google.com/distributed-cloud/edge/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations/get#google.longrunning.Operations.GetOperation)` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an `[Operation.error](https://docs.cloud.google.com/distributed-cloud/edge/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations#Operation.FIELDS.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/distributed-cloud/edge/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations#Status.FIELDS.code)` of `1`, corresponding to `Code.CANCELLED`.

### HTTP request

`POST https://gdchardwaremanagement.googleapis.com/v1alpha/{name=projects/*/locations/*/operations/*}:cancel`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The name of the operation resource to be cancelled.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `gdchardwaremanagement.operations.cancel`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
