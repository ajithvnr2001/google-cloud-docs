---
url: https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs/patch/
title: Method: projects.locations.vodConfigs.patch \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:09.424488+00:00
---

# Method: projects.locations.vodConfigs.patch  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs/patch/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Reference ](https://docs.cloud.google.com/video-stitcher/docs/apis)



Send feedback 

#  Method: projects.locations.vodConfigs.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Updates the specified VOD config. Only updates fields specified in the call method body.

### HTTP request

`PATCH https://videostitcher.googleapis.com/v1/{vodConfig.name=projects/*/locations/*/vodConfigs/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`vodConfig.name` |  `string` Output only. The resource name of the VOD config, in the form of `projects/{project}/locations/{location}/vodConfigs/{id}`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[VodConfig](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs#VodConfig)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `videostitcher.vodConfigs.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
