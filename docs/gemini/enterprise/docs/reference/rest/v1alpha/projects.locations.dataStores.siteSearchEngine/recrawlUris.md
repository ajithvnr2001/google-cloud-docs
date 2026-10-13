---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.siteSearchEngine/recrawlUris/
title: Method: projects.locations.dataStores.siteSearchEngine.recrawlUris \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:50.580044+00:00
---

# Method: projects.locations.dataStores.siteSearchEngine.recrawlUris  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.siteSearchEngine/recrawlUris/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.dataStores.siteSearchEngine.recrawlUris Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Request on-demand recrawl for a list of URIs.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{siteSearchEngine=projects/*/locations/*/dataStores/*/siteSearchEngine}:recrawlUris`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`siteSearchEngine` |  `string` Required. Full resource name of the `[SiteSearchEngine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/SiteSearchEngine)`, such as `projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "uris": [
        string
      ],
      "siteCredential": string
    }  
  
Fields  
---  
`uris[]` |  `string` Required. List of URIs to crawl. At most 10K URIs are supported, otherwise an INVALID_ARGUMENT error is thrown. Each URI should match at least one `[TargetSite](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite)` in `siteSearchEngine`.  
`siteCredential` |  `string` Optional. Credential ID to use for crawling.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `siteSearchEngine` resource:

  * `discoveryengine.siteSearchEngines.recrawlUris`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
