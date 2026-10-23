---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/insert/
title: ManagedFolder: insert \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:34.381938+00:00
---

# ManagedFolder: insert  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/insert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  ManagedFolder: insert Stay organized with collections  Save and categorize content based on your preferences. 

Create a [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders) within a bucket. 

## Required permissions

The authenticated user must have the `storage.managedfolders.create` IAM permission to use this method.

## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/managedFolders

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  The parent bucket of the managed folder.   
  
### Request body

When creating a managed folder, provide the name of the managed folder in the request body.

Property name | Value | Description | Notes  
---|---|---|---  
**Required Properties**  
`name` | `string` | The name of the managed folder, expressed as a path. For example, `example-dir` or `example-dir/example-dir1`. |   
  
## Response

If successful, this method returns a [ManagedFolder resource](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder) in the response body.

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
