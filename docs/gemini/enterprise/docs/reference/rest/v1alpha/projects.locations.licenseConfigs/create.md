---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs/create/
title: Method: projects.locations.licenseConfigs.create \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:45.844911+00:00
---

# Method: projects.locations.licenseConfigs.create  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs/create/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.licenseConfigs.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Creates a `[LicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs#LicenseConfig)` This method should only be used for creating NotebookLm licenses or Gemini Enterprise free trial licenses.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{parent=projects/*/locations/*}/licenseConfigs`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name, such as `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`licenseConfigId` |  `string` Optional. The ID to use for the `[LicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs#LicenseConfig)`, which will become the final component of the `[LicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs#LicenseConfig)`'s resource name. We are using the tier (product edition) name as the license config ID such as `search` or `search_and_assistant`.  
  
### Request body

The request body contains an instance of `[LicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs#LicenseConfig)`.

### Response body

If successful, the response body contains a newly created instance of `[LicenseConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.licenseConfigs#LicenseConfig)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.licenseConfigs.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
