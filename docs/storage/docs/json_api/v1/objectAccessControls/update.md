---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls/update/
title: ObjectAccessControls: update \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:23.493980+00:00
---

# ObjectAccessControls: update  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  ObjectAccessControls: update Stay organized with collections  Save and categorize content based on your preferences. 

Updates an ACL entry on the specified [object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource).

**Important:** This method fails with a `400 Bad Request` response for buckets with uniform bucket-level access enabled. Use [`storage.buckets.getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) and [`storage.buckets.setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) to control access instead.

## Required permissions

The authenticated user must have one of the following permissions to use this method: 

  * The `storage.objects.setIamPolicy` IAM permission for the bucket containing the object
  * The `OWNER` ACL permission for the object



## Request

### HTTP request
    
    
    PUT https://storage.googleapis.com/storage/v1/b/bucket/o/object/acl/entity

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
`entity` | `string` |  The entity holding the permission. Can be `user-emailAddress`, `group-groupId`, `group-emailAddress`, `allUsers`, or `allAuthenticatedUsers`.   
`object` | `string` |  Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
**Optional query parameters**  
`generation` | `long` |  If present, selects a specific revision of this object (as opposed to the latest version, the default).   
  
### Request body

In the request body, supply an [ObjectAccessControls resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls#resource).

## Response

If successful, this method returns an [ObjectAccessControls resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls#resource) in the response body.

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
