---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations/setDedicatedCrawlRate/
title: Method: projects.locations.setDedicatedCrawlRate \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:44.404333+00:00
---

# Method: projects.locations.setDedicatedCrawlRate  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations/setDedicatedCrawlRate/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.setDedicatedCrawlRate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * CrawlType
  * Mode



Sets the dedicated crawl rate for a crawlRateScope. If the dedicated crawl rate was not set, this will enable vertex AI's crawl bot to use the new dedicated crawl rate for crawling. If the dedicated crawl rate was set, vertex AI's crawl bot will try to update the rate to the new value. If the new value is too high, the crawl bot may crawl at a lower rate to avoid overloading the user's website.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{location=projects/*/locations/*}:setDedicatedCrawlRate`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`location` |  `string` Required. The location resource where crawl rate management will be performed. Format: `projects/{project}/locations/{location}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "crawlRateScope": string,
      "crawlRate": integer,
      "crawlType": enum ([CrawlType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations/setDedicatedCrawlRate#CrawlType)),
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations/setDedicatedCrawlRate#Mode))
    }  
  
Fields  
---  
`crawlRateScope` |  `string` Required. The scope of the crawl rate that the user wants to config. Currently, only domain and host name are supported. A domain name example: `example.com`. A host name example: `www.example.com`. Please do not include `/` in the domain or host name.  
`crawlRate` |  `integer` Optional. The crawl QPS set by the user. It is not guaranteed that Vertex crawl bot will crawl at this QPS. If the crawl rate is too high, the real QPS may be lower than the value set by the user to avoid overloading the user's website.  
`crawlType` |  `enum (`[CrawlType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations/setDedicatedCrawlRate#CrawlType)`)` Optional. Whether it's the crawl rate of user-triggered or auto-refresh.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations/setDedicatedCrawlRate#Mode)`)` Optional. Whether the rate is explicitly set by users, or set by vertex AI.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## CrawlType

Crawl type is used to distinguish user-triggered and auto-refresh. User-triggered crawl rate is for deterministic use cases like crawling urls or sitemaps specified by users. Auto-refresh crawl rate is for best effort use cases like refreshing urls periodically.

Enums  
---  
`CRAWL_TYPE_UNSPECIFIED` | The crawl type is unspecified.  
`USER_TRIGGERED` | The crawl type is user-triggered.  
`AUTO_REFRESH` | The crawl type is auto-refresh.  
  
## Mode

Whether the rate is explicitly set by users, or set by vertex AI.

Enums  
---  
`MODE_UNSPECIFIED` | The mode is unspecified. If the user does not specify the mode, default to AUTOMATIC.  
`AUTOMATIC` | Vertex AI automatically splits crawlRate into user-triggered and auto-refresh. Users don't need to specify `[SetDedicatedCrawlRateRequest.CrawlType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations/setDedicatedCrawlRate#CrawlType)` if the mode is AUTOMATIC.  
`EXPLICIT` | Users explicitly set user-triggered or auto-refresh crawl rate.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
