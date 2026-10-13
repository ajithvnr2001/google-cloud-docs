---
url: https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1alpha2/projects/getContinuousValidationConfig/
title: Method: projects.getContinuousValidationConfig \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:58.233228+00:00
---

# Method: projects.getContinuousValidationConfig  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1alpha2/projects/getContinuousValidationConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Reference ](https://docs.cloud.google.com/binary-authorization/docs/api)



Send feedback 

#  Method: projects.getContinuousValidationConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes



Deprecated: For more information, see [Legacy continuous validation deprecation and shutdown](https://cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy).

Gets the `[continuous validation config](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1alpha2/ContinuousValidationConfig)` for the project. Returns a default config if the project does not have one. The default config disables continuous validation on all policies.

### HTTP request

`GET https://binaryauthorization.googleapis.com/v1alpha2/{name=projects/*/continuousValidationConfig}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the continuous validation config. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `binaryauthorization.continuousValidationConfig.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ContinuousValidationConfig](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1alpha2/ContinuousValidationConfig)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
