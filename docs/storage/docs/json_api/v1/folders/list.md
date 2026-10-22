---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/folders/list/
title: Folder: list \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:00.525996+00:00
---

# Folder: list  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/folders/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Folder: list Stay organized with collections  Save and categorize content based on your preferences. 

View the [ folders](https://docs.cloud.google.com/storage/docs/folders-overview) within a bucket with hierarchical namespace enabled. 

## Required permissions

The authenticated user must have the `storage.folders.list` IAM permission to use this method.

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/folders

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  The parent bucket of the folder.   
**Optional query parameters**  
`prefix` | `string` |  Filter results to folders whose names begin with this prefix. If not set or set to an empty string, the method lists all folders in the bucket. If set to a non-empty string, the value must end with a `/`.   
`maxResults` | `unsigned integer` |  The maximum number of folders to return in a single response. The service may return fewer results than `maxResults` so the presence of `nextPageToken` should always be checked.   
`pageToken` | `string` |  A previously-returned page token representing part of the larger set of results to view. The `pageToken` is an encoded field containing the name of the last item (a folder) in the returned list. In a subsequent request using the `pageToken`, items that come after the `pageToken` are shown (up to `maxResults`). If you start a listing and then create a folder before using a `pageToken` to continue listing, you will not see the new folder in subsequent listing results if it is in part of the folder namespace already listed.  
`delimiter` | `string` |  Returns results in a directory-like mode, with `/` being the only supported value for the delimiter. If set, the method returns folders that exactly match the prefix or are one level below the given prefix. The folder matching the prefix is also returned as part of the response.   
`startOffset` | `string` |  Filter results to folders whose names are lexicographically equal to or after `startOffset`. If `endOffset` is also set, the folders listed have names between `startOffset` (inclusive) and `endOffset` (exclusive).   
`endOffset` | `string` |  Filter results to folders whose names are lexicographically before `endOffset`. If `startOffset` is also set, the folders listed have names between `startOffset` (inclusive) and `endOffset` (exclusive).   
  
### Request body

Don't supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure, where the list of folders are included in the `items` attribute and sorted alphabetically by order:
    
    
    {
      "kind": "storage#folders"
      "nextPageToken": string,
      "items": [
        Folder resources
      ]
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. For lists of folders, this is always `storage#folders`. |   
`nextPageToken` | `string` | The continuation token. Provide this value as the `pageToken` of a subsequent request in order to return the next page of results. Note that the next page may be empty. If this is the last page of results, then no continuation token is returned. The presence of this parameter in the response should always be checked to ensure a complete listing of all the results.   
  
The `nextPageToken` is the name of the last folder in the returned list. In a subsequent list request using the `pageToken`, items that come after the token are shown (up to `maxResults`). |   
`items[]` | `list` | The list of [folders](https://docs.cloud.google.com/storage/docs/json_api/v1/folders). |   
  
For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
