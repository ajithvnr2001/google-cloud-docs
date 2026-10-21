---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/list/
title: Method: folders.list \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:26.088228+00:00
---

# Method: folders.list  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: folders.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the Folders that are direct descendants of supplied parent resource. List provides a strongly consistent view of the Folders underneath the specified parent resource. List returns Folders sorted based upon the (ascending) lexical ordering of their displayName. The caller must have `resourcemanager.folders.list` permission on the identified parent.

### HTTP request

`GET https://cloudresourcemanager.googleapis.com/v2beta1/folders`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`parent` |  `string` The resource name of the Organization or Folder whose Folders are being listed. Must be of the form `folders/{folder_id}` or `organizations/{org_id}`. Access to this method is controlled by checking the `resourcemanager.folders.list` permission on the `parent`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `resourcemanager.folders.list`

  
`pageSize` |  `integer` The maximum number of Folders to return in the response. The server can return fewer folders than requested. If unspecified, server picks an appropriate default.  
`pageToken` |  `string` A pagination token returned from a previous call to `folders.list` that indicates where this listing should continue from. This field is optional.  
`showDeleted` |  `boolean` Controls whether Folders in the `[DELETE_REQUESTED](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders#LifecycleState.ENUM_VALUES.DELETE_REQUESTED)` state should be returned. Defaults to false. This field is optional.  
  
### Request body

The request body must be empty.

### Response body

The folders.list response message.

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
`folders[]` |  `object (`[Folder](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders#Folder)`)` A possibly paginated list of Folders that are direct descendants of the specified parent resource.  
`nextPageToken` |  `string` A pagination token returned from a previous call to `folders.list` that indicates from where listing should continue. This field is optional.  
  
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
