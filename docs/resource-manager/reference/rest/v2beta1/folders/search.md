---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/search/
title: Method: folders.search \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:26.156072+00:00
---

# Method: folders.search  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: folders.search Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Search for folders that match specific filter criteria. Search provides an eventually consistent view of the folders a user has access to which meet the specified filter criteria.

This will only return folders on which the caller has the permission `resourcemanager.folders.get`.

### HTTP request

`POST https://cloudresourcemanager.googleapis.com/v2beta1/folders:search`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "pageSize": integer,
      "pageToken": string,
      "query": string
    }  
  
Fields  
---  
`pageSize` |  `integer` The maximum number of folders to return in the response. The server can return fewer folders than requested. If unspecified, server picks an appropriate default.  
`pageToken` |  `string` A pagination token returned from a previous call to `folders.search` that indicates from where search should continue. This field is optional.  
`query` |  `string` Search criteria used to select the Folders to return. If no search criteria is specified then all accessible folders will be returned.Query expressions can be used to restrict results based upon displayName, lifecycleState and parent, where the operators `=`, `NOT`, `AND` and `OR` can be used along with the suffix wildcard symbol `*`.The displayName field in a query expression should use escaped quotes for values that include whitespace to prevent unexpected behavior.Some example queries are:

  * Query `displayName=Test*` returns Folder resources whose display name starts with "Test".
  * Query `lifecycleState=ACTIVE` returns Folder resources with `lifecycleState` set to `ACTIVE`.
  * Query `parent=folders/123` returns Folder resources that have `folders/123` as a parent resource.
  * Query `parent=folders/123 AND lifecycleState=ACTIVE` returns active Folder resources that have `folders/123` as a parent resource.
  * Query `displayName=\\"Test String\\"` returns Folder resources with display names that include both "Test" and "String".

  
  
### Response body

The response message for searching folders.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "folders": [
        {
          object ([Folder](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders#Folder))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`folders[]` |  `object (`[Folder](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders#Folder)`)` A possibly paginated folder search results. the specified parent resource.  
`nextPageToken` |  `string` A pagination token returned from a previous call to `folders.search` that indicates from where searching should continue. This field is optional.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/cloudplatformfolders`
  * `https://www.googleapis.com/auth/cloudplatformfolders.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
