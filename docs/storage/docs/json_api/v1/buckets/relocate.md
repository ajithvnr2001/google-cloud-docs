---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/relocate/
title: Buckets: relocate \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:52.862333+00:00
---

# Buckets: relocate  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/relocate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: relocate Stay organized with collections  Save and categorize content based on your preferences. 

Initiates the [dry run](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#dry-run) or the [relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#initiate-relocation) step of a [bucket relocation operation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview).

Users can use `[Operations: get](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/get)` to check the status of the operation.

## Required permissions

You must have the `storage.buckets.relocate` IAM permission on the bucket to initiate the dry run or the bucket relocation step.

You might also need the following permissions on the bucket:

  * `storage.bucketOperations.get`   
You need this permission to view the status of the bucket relocation operation.
  * `storage.bucketOperations.list`   
You need this permission to view the list of bucket relocation operations.
  * `storage.bucketOperations.cancel`   
You need this permission to cancel the bucket relocation operation.
  * `storage.bucket.get`  
You need this permission to view the metadata of a bucket during the [dry run](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#dry-run) and the [relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#initiate-relocation) step of the bucket relocation operation. 
  * `storage.objects.list` and `storage.objects.get`  
You need these permissions to view the list of objects in a bucket that you want to relocate to another location. 



## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/relocate

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket that you want to relocate.   
  
### Request body

In the request body, supply the following properties:

Property name | Value | Description | Notes  
---|---|---|---  
**Required parameters**  
`destinationLocation` | `string` |  The [destination location](https://docs.cloud.google.com/storage/docs/locations#available-locations) of the bucket.  | Writable  
**Optional parameters**  
`destinationCustomPlacementConfig` | `object` |  The bucket's destination placement configuration if relocating to a [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#configurable).  | Writable  
`destinationCustomPlacementConfig.dataLocations` | `list of strings` |  The list of configurable dual-region locations where you want to relocate the bucket.  | Writable  
`validateOnly` | `boolean` |  When set to `true`, the [dry run](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#dry-run) of the bucket relocation operation starts.  | Writable  
  
## Response

Initiating a bucket relocation process starts a long-running operation. You'll receive an operation ID and a description of the operation. To track the completion of the bucket relocation operation, you'll need to track its progress. For information about how to track the progress of the bucket relocation operation, see [Get details of a long-running operation](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/get).

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
