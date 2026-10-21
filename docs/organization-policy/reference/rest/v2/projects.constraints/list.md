---
url: https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.constraints/list/
title: Method: projects.constraints.list \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:42.387414+00:00
---

# Method: projects.constraints.list  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.constraints/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  Method: projects.constraints.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists constraints that could be applied on the specified resource.

### HTTP request

`GET https://orgpolicy.googleapis.com/v2/{parent=projects/*}/constraints`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The Google Cloud resource that parents the constraint. Must be in one of the following forms:

  * `projects/{project_number}`
  * `projects/{projectId}`
  * `folders/{folder_number}`
  * `organizations/{organization_number}`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `orgpolicy.constraints.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Size of the pages to be returned. This is not used, but the server may at any point start using this field to limit page size.  
`pageToken` |  `string` Page token used to retrieve the next page. This is not used, but the server may at any point start using this field.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListConstraintsResponse](https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListConstraintsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/organizationpolicy`
  * `https://www.googleapis.com/auth/organizationpolicy.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
