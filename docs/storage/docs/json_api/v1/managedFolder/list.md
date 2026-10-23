---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/list/
title: ManagedFolder: list \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:35.617728+00:00
---

# ManagedFolder: list  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  ManagedFolder: list Stay organized with collections  Save and categorize content based on your preferences. 

View the [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) within a bucket. 

## Required permissions

The authenticated user must have the `storage.managedfolders.list` IAM permission to use this method.

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/managedFolders

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Query parameters**  
`prefix` | `string` |  Filter results to managed folders whose names begin with this prefix.   
`maxResults` | `unsigned integer` |  Maximum number of managed folders to return in a single response. The service may return fewer results than `maxResults` so the presence of `nextPageToken` should always be checked.   
`pageToken` | `string` |  A previously-returned page token representing part of the larger set of results to view. The `pageToken` is an encoded field containing the name of the last item (managed folder) in the returned list. In a subsequent request using the `pageToken`, items that come after the `pageToken` are shown (up to `maxResults`). If you start a listing and then create a new managed folder before using a `pageToken` to continue listing, you will not see the new managed folder in subsequent listing results if it is in part of the managed folder namespace already listed.  
**Path parameters**  
`bucket` | `string` |  The parent bucket of the managed folder.   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure, where the list of managed folders are included in the `items` attribute and sorted alphabetically by order:
    
    
    {
      "kind": "storage#managedFolder"
      "nextPageToken": string,
      "items": [
        managedFolder resources
      ]
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. For lists of managed folders, this is always `"storage#managedFolders"`. |   
`nextPageToken` | `string` | The continuation token. Provide this value as the `pageToken` of a subsequent request in order to return the next page of results. Note that the next page may be empty. If this is the last page of results, then no continuation token is returned. The presence of this parameter in the response should always be checked to ensure a complete listing of all the results.   
  
The `nextPageToken` is the name of the last managed folder in the returned list. In a subsequent list request using the `pageToken`, items that come after the token are shown (up to `maxResults`). |   
`items[]` | `list` | The list of [managed folders](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder). |   
  
## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
