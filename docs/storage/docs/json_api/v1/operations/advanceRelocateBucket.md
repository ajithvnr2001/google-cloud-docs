---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/operations/advanceRelocateBucket/
title: Operations: advanceRelocateBucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:15.071431+00:00
---

# Operations: advanceRelocateBucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/operations/advanceRelocateBucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Operations: advanceRelocateBucket Stay organized with collections  Save and categorize content based on your preferences. 

Initiates the [final synchronization](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#initiate-final-sync) of a [bucket relocation operation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) that requires a write downtime. The server makes a best effort to proceed with the operation, but success is not guaranteed.

Users can use `[Operations: get](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/get)` to check the status of the operation.

## Required permissions

You must have the `storage.buckets.relocate` IAM permission on the bucket to initiate the final synchronization step.

You might also need the following permissions on the bucket:

  * `storage.bucketOperations.get`   
You need this permission to view the status of the bucket relocation operation.
  * `storage.bucketOperations.list`   
You need this permission to view the list of bucket relocation operations.
  * `storage.bucketOperations.cancel`   
You need this permission to cancel the bucket relocation operation.
  * `storage.bucket.get`  
You need this permission to view the metadata of a bucket during the final synchronization of the bucket relocation operation. 
  * `storage.objects.list` and `storage.objects.get`  
You need these permissions to view the list of objects in a bucket that you want to relocate to another location. 



## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/operations/operationId/advanceRelocateBucket

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
`operationId` | `string` |  The ID of the [`Buckets: relocate`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/relocate) long-running operation that initiated the bucket relocation. For example, `AbCJYd8jKT1n-Ciw1LCNXIcubwvij_TdqO-ZFjuF2YntK0r74`  
  
### Request body

In the request body, supply any one of the following properties:

Property name | Value | Description | Notes  
---|---|---|---  
**Optional parameters**  
`ttl` | `string` |  The Time to live (TTL) for the write downtime phase during a relocation process. It is expressed as a string, such as `12h` for 12 hours. The `ttl` duration determines the maximum allowed duration for the write downtime phase. If the write downtime exceeds this limit, the relocation process automatically reverts to the initate bucket relocation step, and write operations to the bucket are re-enabled. The value must be within the range of `6h` (6 hours) to `48h` (48 hours). If not specified, the default value is `12h` (12 hours).  | Writable  
`expire_time` | `string` |  If the final synchronization fails, the `expire_time` determines how long the process tries before switching back to the initiate bucket relocation step. The format of `expire_time` is a string in RFC 3339 format, such as `2024-08-15T01:30:15.01Z`.  | Writable  
  
## Response

If successful, this method returns an empty response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
