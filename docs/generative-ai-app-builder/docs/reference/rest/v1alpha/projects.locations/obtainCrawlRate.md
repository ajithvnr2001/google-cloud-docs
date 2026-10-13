---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate/
title: Method: projects.locations.obtainCrawlRate \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:42.259727+00:00
---

# Method: projects.locations.obtainCrawlRate  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.obtainCrawlRate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * OrganicCrawlRateTimeSeries
    * JSON representation
  * CrawlRateTimeSeries
    * JSON representation
  * DedicatedCrawlRateTimeSeries
    * JSON representation
  * State



Obtains the time series data of organic or dedicated crawl rate for monitoring. When dedicated crawl rate is not set, it will return vertex AI's organic crawl rate time series. Organic crawl means Google automatically crawl the internet at its own convenience. When dedicated crawl rate is set, it will return vertex AI's dedicated crawl rate time series.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{location=projects/*/locations/*}:obtainCrawlRate`

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
      "crawlRateScope": string
    }  
  
Fields  
---  
`crawlRateScope` |  `string` Required. The scope of the crawl rate that the user wants to monitor. Currently, only domain and host name are supported. A domain name example: `example.com`. A host name example: `www.example.com`. Please do not include `/` in the domain or host name.  
  
### Response body

Response message for `[CrawlRateManagementService.ObtainCrawlRate](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#google.cloud.discoveryengine.v1alpha.CrawlRateManagementService.ObtainCrawlRate)` method. The response contains organcic or dedicated crawl rate time series data for monitoring, depending on whether dedicated crawl rate is set.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#State)),
      "error": {
        object ([Status](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "organicCrawlRateTimeSeries": {
        object ([OrganicCrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#OrganicCrawlRateTimeSeries))
      },
      "dedicatedCrawlRateTimeSeries": {
        object ([DedicatedCrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#DedicatedCrawlRateTimeSeries))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#State)`)` Output only. The state of the response.  
`error` |  `object (`[Status](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Errors from service when handling the request.  
Once the user sets the dedicated crawl rate, it will return the dedicated crawl rate time series, otherwise it will return the organic crawl rate time series. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`organicCrawlRateTimeSeries` |  `object (`[OrganicCrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#OrganicCrawlRateTimeSeries)`)` The historical organic crawl rate timeseries data, used for monitoring.  
`dedicatedCrawlRateTimeSeries` |  `object (`[DedicatedCrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#DedicatedCrawlRateTimeSeries)`)` The historical dedicated crawl rate timeseries data, used for monitoring.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## OrganicCrawlRateTimeSeries

The historical organic crawl rate timeseries data, used for monitoring. Organic crawl is auto-determined by Google to crawl the user's website when dedicate crawl is not set. Crawl rate is the QPS of crawl request Google sends to the user's website.

JSON representation  
---  
      
    
    {
      "googleOrganicCrawlRate": {
        object ([CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries))
      },
      "vertexAiOrganicCrawlRate": {
        object ([CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries))
      }
    }  
  
Fields  
---  
`googleOrganicCrawlRate` |  `object (`[CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries)`)` Google's organic crawl rate time series, which is the sum of all googlebots' crawl rate. Please refer to <https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers> for more details about googlebots.  
`vertexAiOrganicCrawlRate` |  `object (`[CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries)`)` Vertex AI's organic crawl rate time series, which is the crawl rate of Google-CloudVertexBot when dedicate crawl is not set. Please refer to <https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers#google-cloudvertexbot> for more details about Google-CloudVertexBot.  
  
## CrawlRateTimeSeries

The historical crawl rate timeseries data, used for monitoring.

JSON representation  
---  
      
    
    {
      "qpsTimeSeries": {
        object ([TimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/TimeSeries))
      }
    }  
  
Fields  
---  
`qpsTimeSeries` |  `object (`[TimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/TimeSeries)`)` The QPS of the crawl rate.  
  
## DedicatedCrawlRateTimeSeries

The historical dedicated crawl rate timeseries data, used for monitoring. Dedicated crawl is used by Vertex AI to crawl the user's website when dedicate crawl is set.

JSON representation  
---  
      
    
    {
      "userTriggeredCrawlRate": {
        object ([CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries))
      },
      "autoRefreshCrawlRate": {
        object ([CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries))
      },
      "userTriggeredCrawlErrorRate": {
        object ([CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries))
      },
      "autoRefreshCrawlErrorRate": {
        object ([CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries))
      }
    }  
  
Fields  
---  
`userTriggeredCrawlRate` |  `object (`[CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries)`)` Vertex AI's dedicated crawl rate time series of user triggered crawl, which is the crawl rate of Google-CloudVertexBot when dedicate crawl is set, and user triggered crawl rate is for deterministic use cases like crawling urls or sitemaps specified by users.  
`autoRefreshCrawlRate` |  `object (`[CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries)`)` Vertex AI's dedicated crawl rate time series of auto-refresh, which is the crawl rate of Google-CloudVertexBot when dedicate crawl is set, and the crawl rate is for best effort use cases like refreshing urls periodically.  
`userTriggeredCrawlErrorRate` |  `object (`[CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries)`)` Vertex AI's error rate time series of user triggered dedicated crawl.  
`autoRefreshCrawlErrorRate` |  `object (`[CrawlRateTimeSeries](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/obtainCrawlRate#CrawlRateTimeSeries)`)` Vertex AI's error rate time series of auto-refresh dedicated crawl.  
  
## State

Different states of the response.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unspecified.  
`SUCCEEDED` | The state is successful.  
`FAILED` | The state is failed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
