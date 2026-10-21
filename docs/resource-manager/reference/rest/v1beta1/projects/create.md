---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/create/
title: Method: projects.create \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:22.751996+00:00
---

# Method: projects.create  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: projects.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a Project resource.

Initially, the Project resource is owned by its creator exclusively. The creator can later grant permission to others to read or update the Project.

Several APIs are activated automatically for the Project, including Google Cloud Storage. The parent is identified by a specified `[ResourceId](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects#ResourceId)`, which must include both an ID and a type, such as project, folder, or organization.

This method does not associate the new project with a billing account. You can set or update the billing account associated with a project using the [`projects.updateBillingInfo`](https://docs.cloud.google.com/billing/reference/rest/v1/projects/updateBillingInfo) method.

### HTTP request

`POST https://cloudresourcemanager.googleapis.com/v1beta1/projects`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`useLegacyStack` |  `boolean` A now unused experiment opt-out option.  
  
### Request body

The request body contains an instance of `[Project](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects#Project)`.

### Response body

If successful, the response body contains a newly created instance of `[Project](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects#Project)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloudplatformprojects`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
