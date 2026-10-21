---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/delete/
title: Method: projects.delete \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:20.284180+00:00
---

# Method: projects.delete  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/delete/

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



Marks the Project identified by the specified `projectId` (for example, `my-project-123`) for deletion. This method will only affect the Project if it has a lifecycle state of `[ACTIVE](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects#LifecycleState.ENUM_VALUES.ACTIVE)`.

This method changes the Project's lifecycle state from `[ACTIVE](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects#LifecycleState.ENUM_VALUES.ACTIVE)` to `[DELETE_REQUESTED](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects#LifecycleState.ENUM_VALUES.DELETE_REQUESTED)`. The deletion starts at an unspecified time, at which point the Project is no longer accessible.

Until the deletion completes, you can check the lifecycle state checked by retrieving the Project with `[projects.get](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/get#google.cloudresourcemanager.v1.Projects.GetProject)`, and the Project remains visible to `[projects.list](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/list#google.cloudresourcemanager.v1.Projects.ListProjects)`. However, you cannot update the project.

After the deletion completes, the Project is not retrievable by the `[projects.get](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/get#google.cloudresourcemanager.v1.Projects.GetProject)` and `[projects.list](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/list#google.cloudresourcemanager.v1.Projects.ListProjects)` methods.

The caller must have delete permissions for this Project.

### HTTP request

`DELETE https://cloudresourcemanager.googleapis.com/v1/projects/{projectId}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`projectId` |  `string` The Project ID (for example, `foo-bar-123`).Required. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `projectId`:

  * `resourcemanager.projects.delete`

  
  
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
