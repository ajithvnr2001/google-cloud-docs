---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchParams/
title: SearchParams \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:22.966921+00:00
---

# SearchParams  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchParams/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  SearchParams Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Search parameters.

JSON representation  
---  
      
    
    {
      "filter": string,
      "canonicalFilter": string,
      "sortBy": string,
      "boostSpec": {
        object ([BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BoostSpec))
      }
    }  
  
Fields  
---  
`filter` |  `string` Optional. The filter string to restrict search results.The syntax of the filter string is the same as `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)`.  
`canonicalFilter` |  `string` Optional. The canonical filter string to restrict search results.The syntax of the canonical filter string is the same as `[SearchRequest.canonical_filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.canonical_filter)`.  
`sortBy` |  `string` Optional. The sort string to specify the sorting of search results.The syntax of the sort string is the same as `[SearchRequest.order_by](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.order_by)`.  
`boostSpec` |  `object (`[BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BoostSpec)`)` Optional. The boost spec to specify the boosting of search results.The syntax of the boost spec is the same as `[SearchRequest.boost_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.boost_spec)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
