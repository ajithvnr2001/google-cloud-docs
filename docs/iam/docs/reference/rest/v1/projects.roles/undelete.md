---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/undelete/
title: Method: projects.roles.undelete \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:05.815226+00:00
---

# Method: projects.roles.undelete  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/undelete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.roles.undelete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Undeletes a custom `[Role](https://docs.cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role)`.

### HTTP request

`POST https://iam.googleapis.com/v1/{name=projects/*/roles/*}:undelete`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The `name` parameter's value depends on the target resource for the request, namely [projects](https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles) or [organizations](https://cloud.google.com/iam/docs/reference/rest/v1/organizations.roles). Each resource type's `name` value format is described below:

  * [projects.roles.undelete](https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles/undelete): `projects/{PROJECT_ID}/roles/{CUSTOM_ROLE_ID}`. This method undeletes only [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles) that have been created at the project level. Example request URL: `https://iam.googleapis.com/v1/projects/{PROJECT_ID}/roles/{CUSTOM_ROLE_ID}`
  * [organizations.roles.undelete](https://cloud.google.com/iam/docs/reference/rest/v1/organizations.roles/undelete): `organizations/{ORGANIZATION_ID}/roles/{CUSTOM_ROLE_ID}`. This method undeletes only [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles) that have been created at the organization level. Example request URL: `https://iam.googleapis.com/v1/organizations/{ORGANIZATION_ID}/roles/{CUSTOM_ROLE_ID}`

Note: Wildcard (*) values are invalid; you must specify a complete project ID or organization ID. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `iam.roles.undelete`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "etag": string
    }  
  
Fields  
---  
`etag` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Used to perform a consistent read-modify-write.A base64-encoded string.  
  
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
