---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getStorageLayout/
title: Buckets: getStorageLayout \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:26.842146+00:00
---

# Buckets: getStorageLayout  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getStorageLayout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: getStorageLayout Stay organized with collections  Save and categorize content based on your preferences. 

Returns the storage layout of the specified bucket.

## Required permissions

The authenticated user must have the `storage.objects.list` IAM permission to use this method.

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/storageLayout

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
**Optional query parameters**  
`prefix` | `string` |  If set, the `storage.objects.list` permission is checked for the specified prefix.   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:
    
    
        {
          "kind": "storage#storageLayout",
          "bucket": string,
          "location": string,
          "locationType": string,
          "hierarchicalNamespace":
            {
            "enabled": boolean
            },
        }

Property name | Value | Description  
---|---|---  
`kind` | `string` | The kind of item this is. For buckets, this is always `storage#storageLayout`.  
`bucket` | `string` | The name of the bucket.  
`location` | `string` | The location of the bucket. Object data for objects in the bucket resides in physical storage within this location. See [Cloud Storage bucket locations](https://docs.cloud.google.com/storage/docs/locations) for the authoritative list.  
`locationType` | `string` | This property has a value of `region`.  
`hierarchicalNamespace.enabled` | `boolean` | Whether or not [ hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) is enabled for this bucket.  
  
For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
