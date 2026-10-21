---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/disable/
title: AnywhereCaches: disable \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:44.065097+00:00
---

# AnywhereCaches: disable  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  AnywhereCaches: disable Stay organized with collections  Save and categorize content based on your preferences. 

Disables a [cache instance](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) in a specified bucket.

When you call this API, the time to live (TTL) of data entries stops resetting and data is evicted from the cache when the entry expires. During this time, new data entries cannot be written to the cache, but existing data entries can still be read from the cache. After being disabled for a 1-hour grace period, the cache is deleted.

The [`AnywhereCaches: resume` API](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/resume) can revoke the disablement during the 1-hour grace period.

## Required permissions

The authenticated user must have the `storage.anywhereCaches.disable` IAM permission on the bucket to use this method.

## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/anywhereCaches/anywhereCacheID/disable

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following parameters apply to this method.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
`anywhereCacheID` | `string` |  A value that, along with the bucket's name, uniquely identifies the cache.   
  
To see an example of how to include parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an [AnywhereCache resource](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache#resource-representation) in the response body.

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
