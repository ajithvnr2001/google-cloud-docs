---
url: https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations/updateCmekConfig/
title: Method: projects.locations.updateCmekConfig \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:49.569099+00:00
---

# Method: projects.locations.updateCmekConfig  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations/updateCmekConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/tasks/docs/apis)



Send feedback 

#  Method: projects.locations.updateCmekConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates or Updates a CMEK config.

Updates the Customer Managed Encryption Key associated with the Cloud Tasks location (Creates if the key does not already exist). All new tasks created in the location will be encrypted at-rest with the KMS-key provided in the config.

### HTTP request

`PATCH https://cloudtasks.googleapis.com/v2/{cmekConfig.name=projects/*/locations/*/cmekConfig}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`cmekConfig.name` |  `string` Output only. The config resource name which includes the project and location and must end in 'cmekConfig', in the format projects/PROJECT_ID/locations/LOCATION_ID/cmekConfig`  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` List of fields to be updated in this request.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[CmekConfig](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/CmekConfig)`.

### Response body

If successful, the response body contains an instance of `[CmekConfig](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/CmekConfig)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-tasks`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
