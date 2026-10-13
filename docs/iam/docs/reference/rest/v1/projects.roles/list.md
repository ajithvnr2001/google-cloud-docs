---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/list/
title: Method: projects.roles.list \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:04.863139+00:00
---

# Method: projects.roles.list  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.roles.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Lists every predefined `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)` that IAM supports, or every custom role that is defined for an organization or project.

### HTTP request

`GET https://iam.googleapis.com/v1/{parent=projects/*}/roles`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The `parent` parameter's value depends on the target resource for the request, namely [roles](https://cloud.google.com/iam/docs/reference/rest/v1/roles), [projects](https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles), or [organizations](https://cloud.google.com/iam/docs/reference/rest/v1/organizations.roles). Each resource type's `parent` value format is described below:

  * [roles.list](https://cloud.google.com/iam/docs/reference/rest/v1/roles/list): An empty string. This method doesn't require a resource; it simply returns all [predefined roles](https://cloud.google.com/iam/docs/understanding-roles#predefined_roles) in IAM. Example request URL: `https://iam.googleapis.com/v1/roles`
  * [projects.roles.list](https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles/list): `projects/{PROJECT_ID}`. This method lists all project-level [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles). Example request URL: `https://iam.googleapis.com/v1/projects/{PROJECT_ID}/roles`
  * [organizations.roles.list](https://cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/list): `organizations/{ORGANIZATION_ID}`. This method lists all organization-level [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles). Example request URL: `https://iam.googleapis.com/v1/organizations/{ORGANIZATION_ID}/roles`

Note: Wildcard (*) values are invalid; you must specify a complete project ID or organization ID. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `iam.roles.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional limit on the number of roles to include in the response.The default is 300, and the maximum is 1,000.  
`pageToken` |  `string` Optional pagination token returned in an earlier ListRolesResponse.  
`view` |  `enum (`[RoleView](https://docs.cloud.google.com/iam/docs/reference/rest/v1/RoleView)`)` Optional view for the returned Role objects. When `FULL` is specified, the `includedPermissions` field is returned, which includes a list of all permissions in the role. The default value is `BASIC`, which does not return the `includedPermissions` field.  
`showDeleted` |  `boolean` Include Roles that have been deleted.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListRolesResponse](https://docs.cloud.google.com/iam/docs/reference/rest/v1/ListRolesResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
