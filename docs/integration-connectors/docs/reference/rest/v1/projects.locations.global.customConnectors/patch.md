---
url: https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.global.customConnectors/patch/
title: Method: projects.locations.global.customConnectors.patch \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:15.404703+00:00
---

# Method: projects.locations.global.customConnectors.patch  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.global.customConnectors/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Reference ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest)



Send feedback 

#  Method: projects.locations.global.customConnectors.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates the parameters of a CustomConnector.

### HTTP request

`PATCH https://connectors.googleapis.com/v1/{customConnector.name=projects/*/locations/global/customConnectors/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`customConnector.name` |  `string` Identifier. Resource name of the CustomConnector. Format: projects/{project}/locations/{location}/customConnectors/{connector}  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. Field mask is used to specify the fields to be overwritten in the Connector resource by the update. The fields specified in the updateMask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. Set the mask as "*" for full replacement, which means all fields will be overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[CustomConnector](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.global.customConnectors#CustomConnector)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
