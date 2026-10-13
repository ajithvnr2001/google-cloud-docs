---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/delete/
title: Method: projects.roles.delete \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:03.922680+00:00
---

# Method: projects.roles.delete  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.roles.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Deletes a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.

When you delete a custom role, the following changes occur immediately:

  * You cannot bind a principal to the custom role in an IAM `[Policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy)`.
  * Existing bindings to the custom role are not changed, but they have no effect.
  * By default, the response from `[roles.list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles/list#google.iam.admin.v1.IAM.ListRoles)` does not include the custom role.



A deleted custom role still counts toward the [custom role limit](https://cloud.google.com/iam/help/limits) until it is permanently deleted. You have 7 days to undelete the custom role. After 7 days, the following changes occur:

  * The custom role is permanently deleted and cannot be recovered.
  * If an IAM policy contains a binding to the custom role, the binding is permanently removed.
  * The custom role no longer counts toward your custom role limit.



### HTTP request

`DELETE https://iam.googleapis.com/v1/{name=projects/*/roles/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The `name` parameter's value depends on the target resource for the request, namely [projects](https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles) or [organizations](https://cloud.google.com/iam/docs/reference/rest/v1/organizations.roles). Each resource type's `name` value format is described below:

  * [projects.roles.delete](https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles/delete): `projects/{PROJECT_ID}/roles/{CUSTOM_ROLE_ID}`. This method deletes only [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles) that have been created at the project level. Example request URL: `https://iam.googleapis.com/v1/projects/{PROJECT_ID}/roles/{CUSTOM_ROLE_ID}`
  * [organizations.roles.delete](https://cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/delete): `organizations/{ORGANIZATION_ID}/roles/{CUSTOM_ROLE_ID}`. This method deletes only [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles) that have been created at the organization level. Example request URL: `https://iam.googleapis.com/v1/organizations/{ORGANIZATION_ID}/roles/{CUSTOM_ROLE_ID}`

Note: Wildcard (*) values are invalid; you must specify a complete project ID or organization ID. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `iam.roles.delete`

  
  
### Query parameters

Parameters  
---  
`etag` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Used to perform a consistent read-modify-write.A base64-encoded string.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
