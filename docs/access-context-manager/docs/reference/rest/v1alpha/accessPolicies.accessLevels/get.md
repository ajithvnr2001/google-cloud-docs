---
url: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/get/
title: Method: accessPolicies.accessLevels.get \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:30.178391+00:00
---

# Method: accessPolicies.accessLevels.get  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  Method: accessPolicies.accessLevels.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets an `[access level](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` based on the resource name.

### HTTP request

`GET https://accesscontextmanager.googleapis.com/v1alpha/{name=accessPolicies/*/accessLevels/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Resource name for the `[Access Level](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)`.Format: `accessPolicies/{policyId}/accessLevels/{access_level_id}`  
  
### Query parameters

Parameters  
---  
`accessLevelFormat` |  `enum (`[LevelFormat](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/LevelFormat)`)` Whether to return `BasicLevels` in the Cloud Common Expression Language rather than as `BasicLevels`. Defaults to AS_DEFINED, where `[Access Levels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` are returned as `BasicLevels` or `CustomLevels` based on how they were created. If set to CEL, all `[Access Levels](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)` are returned as `CustomLevels`. In the CEL case, `BasicLevels` are translated to equivalent `CustomLevels`.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[AccessLevel](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-01 UTC."],[],[]] 
