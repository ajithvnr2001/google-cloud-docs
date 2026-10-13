---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/create/
title: Method: projects.roles.create \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:04.702134+00:00
---

# Method: projects.roles.create  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.roles.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Creates a new custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.

### HTTP request

`POST https://iam.googleapis.com/v1/{parent=projects/*}/roles`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The `parent` parameter's value depends on the target resource for the request, namely [projects](https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles) or [organizations](https://cloud.google.com/iam/docs/reference/rest/v1/organizations.roles). Each resource type's `parent` value format is described below:

  * [projects.roles.create](https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles/create): `projects/{PROJECT_ID}`. This method creates project-level [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles). Example request URL: `https://iam.googleapis.com/v1/projects/{PROJECT_ID}/roles`
  * [organizations.roles.create](https://cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/create): `organizations/{ORGANIZATION_ID}`. This method creates organization-level [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles). Example request URL: `https://iam.googleapis.com/v1/organizations/{ORGANIZATION_ID}/roles`

Note: Wildcard (*) values are invalid; you must specify a complete project ID or organization ID. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `iam.roles.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "roleId": string,
      "role": {
        object ([Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role))
      }
    }  
  
Fields  
---  
`roleId` |  `string` The role ID to use for this role.A role ID may contain alphanumeric characters, underscores (`_`), and periods (`.`). It must contain a minimum of 3 characters and a maximum of 64 characters.  
`role` |  `object (`[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`)` The Role resource to create.  
  
### Response body

If successful, the response body contains a newly created instance of `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
