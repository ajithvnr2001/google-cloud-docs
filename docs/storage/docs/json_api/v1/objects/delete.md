---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/delete/
title: Objects: delete \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:32.027874+00:00
---

# Objects: delete  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects: delete Stay organized with collections  Save and categorize content based on your preferences. 

Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the `generation` parameter is used.

When this API is used to delete an object from a bucket with a [soft delete policy](https://docs.cloud.google.com/storage/docs/soft-delete), the object becomes soft deleted, and the `softDeleteTime` and `hardDeleteTime` properties are set on the [object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource). This API cannot be used to permanently delete soft-deleted objects. Soft-deleted objects are permanently deleted according to their `hardDeleteTime`. Attempting to delete soft-deleted objects using this API results in a `404 Not Found` error with the reason `notFound`.

## Required permissions

The authenticated user must have the `storage.objects.delete` IAM permission to use this method.

## Request

### HTTP request
    
    
    DELETE https://storage.googleapis.com/storage/v1/b/bucket/o/object

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket in which the object resides.   
`object` | `string` |  Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
**Optional query parameters**  
`generation` | `long` |  If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default).   
`ifGenerationMatch` | `long` |  Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.   
`ifGenerationNotMatch` | `long` |  Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.   
`ifMetagenerationMatch` | `long` |  Makes the operation conditional on whether the object's current metageneration matches the given value.   
`ifMetagenerationNotMatch` | `long` |  Makes the operation conditional on whether the object's current metageneration does not match the given value.   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
