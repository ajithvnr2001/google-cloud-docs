---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/delete/
title: Method: folders.delete \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:25.418649+00:00
---

# Method: folders.delete  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: folders.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Requests deletion of a Folder. The Folder is moved into the `[DELETE_REQUESTED](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders#LifecycleState.ENUM_VALUES.DELETE_REQUESTED)` state immediately, and is deleted approximately 30 days later. This method may only be called on an empty Folder in the `[ACTIVE](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders#LifecycleState.ENUM_VALUES.ACTIVE)` state, where a Folder is empty if it doesn't contain any Folders or Projects in the `[ACTIVE](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders#LifecycleState.ENUM_VALUES.ACTIVE)` state. The caller must have `resourcemanager.folders.delete` permission on the identified folder.

### HTTP request

`DELETE https://cloudresourcemanager.googleapis.com/v2beta1/{name=folders/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` the resource name of the Folder to be deleted. Must be of the form `folders/{folder_id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `resourcemanager.folders.delete`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Folder](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders#Folder)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloudplatformfolders`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
