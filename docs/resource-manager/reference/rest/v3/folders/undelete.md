---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/undelete/
title: Method: folders.undelete \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:28.189215+00:00
---

# Method: folders.undelete  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/undelete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: folders.undelete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Cancels the deletion request for a folder. This method may be called on a folder in any state. If the folder is in the `[ACTIVE](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders#State.ENUM_VALUES.ACTIVE)` state the result will be a no-op success. In order to succeed, the folder's parent must be in the `[ACTIVE](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders#State.ENUM_VALUES.ACTIVE)` state. In addition, reintroducing the folder into the tree must not violate folder naming, height, and fanout constraints described in the `[folders.create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/create#google.cloud.resourcemanager.v3.Folders.CreateFolder)` documentation. The caller must have `resourcemanager.folders.undelete` permission on the identified folder.

### HTTP request

`POST https://cloudresourcemanager.googleapis.com/v3/{name=folders/*}:undelete`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the folder to undelete. Must be of the form `folders/{folder_id}`.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloudplatformfolders`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
