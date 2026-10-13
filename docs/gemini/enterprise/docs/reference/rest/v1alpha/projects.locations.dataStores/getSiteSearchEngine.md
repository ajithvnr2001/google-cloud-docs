---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores/getSiteSearchEngine/
title: Method: projects.locations.dataStores.getSiteSearchEngine \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:36.719659+00:00
---

# Method: projects.locations.dataStores.getSiteSearchEngine  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores/getSiteSearchEngine/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.dataStores.getSiteSearchEngine Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Gets the `[SiteSearchEngine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/SiteSearchEngine)`.

### HTTP request

Choose an endpoint:

globalus

  
`GET https://discoveryengine.googleapis.com/v1alpha/{name=projects/*/locations/*/dataStores/*/siteSearchEngine}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Resource name of `[SiteSearchEngine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/SiteSearchEngine)`, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}/siteSearchEngine`.If the caller does not have permission to access the [SiteSearchEngine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[SiteSearchEngine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/SiteSearchEngine)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `discoveryengine.siteSearchEngines.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
