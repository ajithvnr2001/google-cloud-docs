---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/create/
title: Method: organizations.environments.apis.revisions.debugsessions.create \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:48.594495+00:00
---

# Method: organizations.environments.apis.revisions.debugsessions.create  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.apis.revisions.debugsessions.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a debug session for a deployed API Proxy revision.

### HTTP request

`POST https://apigee.googleapis.com/v1/{parent=organizations/*/environments/*/apis/*/revisions/*}/debugsessions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the API Proxy revision deployment for which to create the `[DebugSession](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions#DebugSession)`. Must be of the form `organizations/{organization}/environments/{environment}/apis/{api}/revisions/{revision}`.If the API proxy resource has the `space` attribute set, IAM permissions are checked differently . To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.tracesessions.create`

  
  
### Query parameters

Parameters  
---  
`timeout` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The time in seconds after which this `[DebugSession](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions#DebugSession)` should end. A timeout specified in `[DebugSession](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions#DebugSession)` will overwrite this value.  
  
### Request body

The request body contains an instance of `[DebugSession](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions#DebugSession)`.

### Response body

If successful, the response body contains a newly created instance of `[DebugSession](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions#DebugSession)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
