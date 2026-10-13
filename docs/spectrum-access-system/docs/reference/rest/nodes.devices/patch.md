---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/nodes.devices/patch/
title: Method: nodes.devices.patch \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:22.933566+00:00
---

# Method: nodes.devices.patch  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/nodes.devices/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Reference ](https://docs.cloud.google.com/spectrum-access-system/docs/apis)



Send feedback 

#  Method: nodes.devices.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes



Updates a `[device](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices#Device)`.

### HTTP request

`PATCH https://sasportal.googleapis.com/v1alpha1/{device.name=nodes/*/devices/*}`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`device.name` |  `string` Output only. The resource path name.   
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://docs.cloud.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)` format)` Fields to be updated.A comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[Device](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices#Device)`.

### Response body

If successful, the response body contains an instance of `[Device](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices#Device)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/userinfo.email`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
