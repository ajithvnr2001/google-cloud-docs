---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls/get/
title: BucketAccessControls: get \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:03.047419+00:00
---

# BucketAccessControls: get  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  BucketAccessControls: get Stay organized with collections  Save and categorize content based on your preferences. 

Returns the ACL entry for the specified entity on the specified bucket.

**Important:** This method fails with a `400 Bad Request` response for buckets with uniform bucket-level access enabled. Use [`storage.buckets.getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) and [`storage.buckets.setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) to control access instead.

## Required permissions

The authenticated user must have the following IAM permissions on the bucket to use this method: 

  * `storage.buckets.get`
  * `storage.buckets.getIamPolicy`

As an alternative to having IAM permissions, the authenticated user can use this method by having the `OWNER` ACL permission for the bucket. 

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/acl/entity

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of an existing [bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource).   
`entity` | `string` |  The entity holding the permission. Can be `user-emailAddress`, `group-groupId`, `group-emailAddress`, `allUsers`, or `allAuthenticatedUsers`.   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a [BucketAccessControls resource](https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls#resource) in the response body.

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
