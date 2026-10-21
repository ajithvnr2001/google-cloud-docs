---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/projects.locations/getIntelligenceConfig/
title: Method: projects.locations.getIntelligenceConfig \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:21.754175+00:00
---

# Method: projects.locations.getIntelligenceConfig  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/projects.locations/getIntelligenceConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Method: projects.locations.getIntelligenceConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets the `IntelligenceConfig` resource associated with your project.

**IAM Permissions** :

Requires `storage.intelligenceConfigs.get` [IAM](https://cloud.google.com/iam/docs/overview#permissions) permission on the project.

### HTTP request

`GET https://storage.googleapis.com/v2/projects/projectId/locations/global/intelligenceConfig`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the `IntelligenceConfig` resource associated with your project.Format: `projects/projectId/locations/global/intelligenceConfig`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[IntelligenceConfig](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/devstorage.full_control`
  * `https://www.googleapis.com/auth/devstorage.read_only`
  * `https://www.googleapis.com/auth/devstorage.read_write`
  * `https://www.googleapis.com/auth/devstorage.write_only`
  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
