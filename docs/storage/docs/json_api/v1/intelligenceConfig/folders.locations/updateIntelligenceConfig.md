---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/folders.locations/updateIntelligenceConfig/
title: Method: folders.locations.updateIntelligenceConfig \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:21.313356+00:00
---

# Method: folders.locations.updateIntelligenceConfig  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/folders.locations/updateIntelligenceConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Method: folders.locations.updateIntelligenceConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates the `IntelligenceConfig` resource associated with your folder.

**IAM Permissions** :

Requires `storage.intelligenceConfigs.update` [IAM](https://cloud.google.com/iam/docs/overview#permissions) permission on the folder.

### HTTP request

`PATCH https://storage.googleapis.com/v2/folders/folderId/locations/global/intelligenceConfig`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the `IntelligenceConfig` resource associated with your folder.Format: `folders/folderId/locations/global/intelligenceConfig`  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The `updateMask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.  
`requestId` |  `string` Optional. The ID that uniquely identifies the request, preventing duplicate processing.  
  
### Request body

The request body contains an instance of `[IntelligenceConfig](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig)`.

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
