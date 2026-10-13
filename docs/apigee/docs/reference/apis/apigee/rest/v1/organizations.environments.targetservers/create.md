---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers/create/
title: Method: organizations.environments.targetservers.create \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:00.931614+00:00
---

# Method: organizations.environments.targetservers.create  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.targetservers.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a `[TargetServer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers#TargetServer)` in the specified environment.

### HTTP request

`POST https://apigee.googleapis.com/v1/{parent=organizations/*/environments/*}/targetservers`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent environment name under which the TargetServer will be created. Must be of the form `organizations/{org}/environments/{env}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.targetservers.create`

  
  
### Query parameters

Parameters  
---  
`name` |  `string` Optional. The ID to give the TargetServer. This will overwrite the value in `[TargetServer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers#TargetServer)`.  
  
### Request body

The request body contains an instance of `[TargetServer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers#TargetServer)`.

### Response body

If successful, the response body contains a newly created instance of `[TargetServer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers#TargetServer)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
