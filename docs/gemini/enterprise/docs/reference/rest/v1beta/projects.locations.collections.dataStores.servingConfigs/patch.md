---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs/patch/
title: Method: projects.locations.collections.dataStores.servingConfigs.patch \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:39.341469+00:00
---

# Method: projects.locations.collections.dataStores.servingConfigs.patch  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs/patch/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.servingConfigs.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Updates a ServingConfig.

Returns a NOT_FOUND error if the ServingConfig does not exist.

### HTTP request

Choose an endpoint:

globalus

  
`PATCH https://discoveryengine.googleapis.com/v1beta/{servingConfig.name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`servingConfig.name` |  `string` Immutable. Fully qualified name `projects/{project}/locations/{location}/collections/{collectionId}/engines/{engineId}/servingConfigs/{servingConfigId}`  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Indicates which fields in the provided `[ServingConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs#ServingConfig)` to update. The following are NOT supported:

  * `[ServingConfig.name](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs#ServingConfig.FIELDS.name)`

If not set, all supported fields are updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[ServingConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs#ServingConfig)`.

### Response body

If successful, the response body contains an instance of `[ServingConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.servingConfigs#ServingConfig)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `discoveryengine.servingConfigs.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
