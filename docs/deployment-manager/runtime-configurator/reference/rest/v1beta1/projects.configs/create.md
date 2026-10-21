---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/create/
title: Method: projects.configs.create \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:32.936446+00:00
---

# Method: projects.configs.create  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Method: projects.configs.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Creates a new RuntimeConfig resource. The configuration name must be unique within project.

### HTTP request

`POST https://runtimeconfig.googleapis.com/v1beta1/{parent=projects/*}/configs`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The [project ID](https://support.google.com/cloud/answer/6158840?hl=en&ref_topic=6158848) for this request, in the format `projects/[PROJECT_ID]`. Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource `parent`:

  * `runtimeconfig.configs.create`

  
  
### Query parameters

Parameters  
---  
`requestId` |  `string` An optional but recommended unique `requestId`. If the server receives two `create()` requests with the same `requestId`, then the second request will be ignored and the first resource created and stored in the backend is returned. Empty `requestId` fields are ignored.It is responsibility of the client to ensure uniqueness of the `requestId` strings.`requestId` strings are limited to 64 characters.  
  
### Request body

The request body contains an instance of `[RuntimeConfig](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs#RuntimeConfig)`.

### Response body

If successful, the response body contains a newly created instance of `[RuntimeConfig](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs#RuntimeConfig)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloudruntimeconfig`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Try it!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
