---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/testIamPermissions/
title: Buckets: testIamPermissions \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:25.220507+00:00
---

# Buckets: testIamPermissions  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/testIamPermissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: testIamPermissions Stay organized with collections  Save and categorize content based on your preferences. 

Tests a set of permissions on the given bucket to see which, if any, are held by the caller.

## Required permissions

Permissions are not required for using this method.

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/iam/testPermissions

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
**Required query parameters**  
`permissions` | `string` |  Permissions to test.   
  
Note: Providing `storage.buckets.list` or `storage.buckets.create` returns an error, as these permissions apply to projects instead of buckets.   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:
    
    
    {
      "kind": "storage#testIamPermissionsResponse",
      "permissions": [
        string
      ]
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. |   
`permissions[]` | `list` | The permissions held by the caller. Permissions are always of the format `"storage.resource.capability"`, where `resource` is one of `buckets`, `objects`, or `managedFolders`. See [Cloud Storage IAM Permissions](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions) for a list of supported permissions. |   
  
For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
