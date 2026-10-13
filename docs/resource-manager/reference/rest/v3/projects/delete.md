---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/delete/
title: Method: projects.delete \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:38:51.761963+00:00
---

# Method: projects.delete  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: projects.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Marks the project identified by the specified `name` (for example, `projects/415104041262`) for deletion.

This method will only affect the project if it has a lifecycle state of `[ACTIVE](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#State.ENUM_VALUES.ACTIVE)`.

This method changes the Project's lifecycle state from `[ACTIVE](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#State.ENUM_VALUES.ACTIVE)` to `[DELETE_REQUESTED](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#State.ENUM_VALUES.DELETE_REQUESTED)`. The deletion starts at an unspecified time, at which point the Project is no longer accessible.

Until the deletion completes, you can check the lifecycle state checked by retrieving the project with `[projects.get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/get#google.cloud.resourcemanager.v3.Projects.GetProject)`, and the project remains visible to `[projects.list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list#google.cloud.resourcemanager.v3.Projects.ListProjects)`. However, you cannot update the project.

After the deletion completes, the project is not retrievable by the `[projects.get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/get#google.cloud.resourcemanager.v3.Projects.GetProject)`, `[projects.list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list#google.cloud.resourcemanager.v3.Projects.ListProjects)`, and `[projects.search](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/search#google.cloud.resourcemanager.v3.Projects.SearchProjects)` methods.

The caller must have `resourcemanager.projects.delete` permissions for this project.

### HTTP request

`DELETE https://cloudresourcemanager.googleapis.com/v3/{name=projects/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the Project (for example, `projects/415104041262`). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `resourcemanager.projects.delete`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloudplatformprojects`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
