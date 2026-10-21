---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get/
title: Buckets: get \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:41.433186+00:00
---

# Buckets: get  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: get Stay organized with collections  Save and categorize content based on your preferences. 

Returns metadata for the specified bucket.

## Required permissions

The authenticated user must have the `storage.buckets.get` IAM permission to use this method. Additionally, to return specific bucket metadata, the authenticated user must have the following permissions:

  * To return the IAM policies: `storage.buckets.getIamPolicy`
  * To return the bucket IP filtering rules: `storage.buckets.getIpFilter`



## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
**Optional query parameters**  
`generation` | `long` |  If present, selects a specific soft-deleted version of this bucket instead of the live version. This parameter is required if `softDeleted` is set to `true`.   
`ifMetagenerationMatch` | `long` |  Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.   
`ifMetagenerationNotMatch` | `long` |  Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.   
`projection` | `string` |  Set of properties to return. Defaults to `noAcl`. Acceptable values are: 

  * `full`: Include all properties.
  * `noAcl`: Omit `owner`, `acl`, and `defaultObjectAcl` properties.

  
`softDeleted` | `boolean` |  If `true`, returns the soft-deleted bucket. This parameter is required if `generation` is specified.   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a [bucket resource](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource) in the response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
