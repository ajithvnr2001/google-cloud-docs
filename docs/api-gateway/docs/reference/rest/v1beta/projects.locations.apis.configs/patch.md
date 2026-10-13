---
url: https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1beta/projects.locations.apis.configs/patch/
title: Method: projects.locations.apis.configs.patch \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:17.281980+00:00
---

# Method: projects.locations.apis.configs.patch  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1beta/projects.locations.apis.configs/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Reference ](https://docs.cloud.google.com/api-gateway/docs/reference)



Send feedback 

#  Method: projects.locations.apis.configs.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Updates the parameters of a single ApiConfig.

### HTTP request

`PATCH https://apigateway.googleapis.com/v1beta/{apiConfig.name=projects/*/locations/*/apis/*/configs/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`apiConfig.name` |  `string` Output only. Resource name of the API Config. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig}  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Field mask is used to specify the fields to be overwritten in the ApiConfig resource by the update. The fields specified in the updateMask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[ApiConfig](https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1beta/projects.locations.apis.configs#ApiConfig)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/api-gateway/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-10 UTC."],[],[]] 
