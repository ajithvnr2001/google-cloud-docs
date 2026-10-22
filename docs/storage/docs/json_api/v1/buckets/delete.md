---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/delete/
title: Buckets: delete \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:44.246107+00:00
---

# Buckets: delete  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: delete Stay organized with collections  Save and categorize content based on your preferences. 

Deletes an empty bucket. The request fails if there are any live or noncurrent objects in the bucket, but the request succeeds if the bucket only contains soft-deleted objects or incomplete uploads, such as ongoing [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads). Does not delete [soft-deleted objects](https://docs.cloud.google.com/storage/docs/soft-delete).

When this API is used to delete a bucket with a [soft delete policy](https://docs.cloud.google.com/storage/docs/soft-delete), the bucket becomes soft-deleted and the `softDeleteTime` and `hardDeleteTime` properties are set on the bucket. Objects and multipart uploads that were in the bucket at the time of deletion are also retained for the specified retention duration. When a soft-deleted bucket reaches the end of its retention duration, it is permanently deleted. The `hardDeleteTime` of the bucket always equals or exceeds the expiration time of the last soft-deleted object in the bucket. 

## Required permissions

The authenticated user must have the `storage.buckets.delete` IAM permission to use this method.

## Request

### HTTP request
    
    
    DELETE https://storage.googleapis.com/storage/v1/b/bucket

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
**Optional query parameters**  
`ifMetagenerationMatch` | `long` |  If set, only deletes the bucket if its metageneration matches this value.   
`ifMetagenerationNotMatch` | `long` |  If set, only deletes the bucket if its metageneration does not match this value.   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
