---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/restore/
title: Buckets: restore \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:40.504595+00:00
---

# Buckets: restore  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: restore Stay organized with collections  Save and categorize content based on your preferences. 

Restores a [soft-deleted bucket](https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets).

The original bucket metadata, including IAM policies, custom metadata, and tags, but excluding managed folders, is restored and the `softDeleteTime` and `hardDeleteTime` is cleared. No objects are restored. If a live bucket with the same name already exists, the bucket cannot be restored.

After the bucket is live again, the objects can be restored with the [`Objects: restore`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/restore) or [`Objects: bulkRestore`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/bulkRestore) APIs.

## Required permissions

The authenticated user must have the `storage.buckets.restore` IAM permission at the project level or above to use this method. To return access control lists (ACLs) as part of the response, the authenticated user must also have the `storage.buckets.getIamPolicy` permission.

## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/restore

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket to be restored.   
**Required query parameters**  
`generation` | `long` |  The specific version of the bucket to be restored.   
**Optional query parameters**  
`projection` | `string` |  Set of properties to return. Defaults to `full`. Acceptable values are: 

  * `full`: Include all properties.
  * `noAcl`: Omit `owner`, `acl`, and `defaultObjectAcl` properties.

  
  
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
