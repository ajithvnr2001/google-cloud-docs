---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/folders/getfoldermetadata/
title: Folder: get \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:50.754112+00:00
---

# Folder: get  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/folders/getfoldermetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Folder: get Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves [ metadata of a folder](https://docs.cloud.google.com/storage/docs/json_api/v1/folders#resource) within a bucket with hierarchical namespace enabled. 

## Required permissions

The authenticated user must have the `storage.folders.get` IAM permission to use this method. 

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/folders/folder

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  The parent bucket of the folder.   
`folder` | `string` |  The URL-encoded name of the folder. For example, `example-folder/` URL-encoded as `example-folder%2F`. If the folder is nested, for example, `example-folder1/example-folder2/`, then the URL-encoded name is `example-folder1%2Fexample-folder2%2F`.   
**Optional query parameters**  
`ifMetagenerationMatch` | `long` |  If set, the method returns the folder if its metageneration matches this value.   
`ifMetagenerationNotMatch` | `long` |  If set, the method returns the folder if its metageneration does not match this value.   
  
### Request body

Don't supply a request body with this method.

## Response

If successful, this method returns a [folder resource](https://docs.cloud.google.com/storage/docs/json_api/v1/folders#resource) in the response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
