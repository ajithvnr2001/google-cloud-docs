---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ListTargetSitesResponse/
title: ListTargetSitesResponse \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:19.588313+00:00
---

# ListTargetSitesResponse  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ListTargetSitesResponse/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  ListTargetSitesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for `[SiteSearchEngineService.ListTargetSites](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.siteSearchEngine.targetSites/list#google.cloud.discoveryengine.v1beta.SiteSearchEngineService.ListTargetSites)` method.

JSON representation  
---  
      
    
    {
      "targetSites": [
        {
          object ([TargetSite](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`targetSites[]` |  `object (`[TargetSite](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite)`)` List of TargetSites.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` The total number of items matching the request. This will always be populated in the response.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
