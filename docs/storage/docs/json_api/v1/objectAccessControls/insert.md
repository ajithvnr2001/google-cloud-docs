---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls/insert/
title: ObjectAccessControls: insert \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:32.497610+00:00
---

# ObjectAccessControls: insert  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls/insert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  ObjectAccessControls: insert Stay organized with collections  Save and categorize content based on your preferences. 

Creates a new ACL entry on the specified [object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource).

**Important:** This method fails with a `400 Bad Request` response for buckets with uniform bucket-level access enabled. Use [`storage.buckets.getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) and [`storage.buckets.setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) to control access instead.

## Required permissions

The authenticated user must have one of the following permissions to use this method: 

  * The `storage.objects.setIamPolicy` IAM permission for the bucket containing the object
  * The `OWNER` ACL permission for the object



## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/o/object/acl

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
`object` | `string` |  Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
**Optional query parameters**  
`generation` | `long` |  If present, selects a specific revision of this object (as opposed to the latest version, the default).   
  
### Request body

In the request body, supply an [ObjectAccessControls resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls#resource) with the following properties:

Property name | Value | Description | Notes  
---|---|---|---  
**Required Properties**  
`entity` | `string` | The entity holding the permission, in one of the following forms: 

  * `user-email`
  * `group-groupId`
  * `group-email`
  * `domain-domain`
  * `project-team-projectId`
  * `allUsers`
  * `allAuthenticatedUsers`

Examples: 
  * The user `liz@example.com` would be `user-liz@example.com`.
  * The group `example@googlegroups.com` would be `group-example@googlegroups.com`.
  * To refer to all members of the domain `example.com`, the entity would be `domain-example.com`.

|  writable   
`role` | `string` | The access permission for the entity.   
  
Acceptable values are: 

  * "`OWNER`"
  * "`READER`"

|  writable   
  
## Response

If successful, this method returns an [ObjectAccessControls resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls#resource) in the response body.

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
