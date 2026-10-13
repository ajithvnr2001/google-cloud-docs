---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/undelete/
title: Method: projects.undelete \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:18.150409+00:00
---

# Method: projects.undelete  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/undelete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: projects.undelete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Restores the Project identified by the specified `projectId` (for example, `my-project-123`). You can only use this method for a Project that has a lifecycle state of `[DELETE_REQUESTED](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects#LifecycleState.ENUM_VALUES.DELETE_REQUESTED)`. After deletion starts, the Project cannot be restored.

The caller must have undelete permissions for this Project.

### HTTP request

`POST https://cloudresourcemanager.googleapis.com/v1/projects/{projectId}:undelete`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`projectId` |  `string` Required. The project ID (for example, `foo-bar-123`). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `projectId`:

  * `resourcemanager.projects.undelete`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloudplatformprojects`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
