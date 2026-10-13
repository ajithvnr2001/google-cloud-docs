---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/TileNavigationSpec/
title: TileNavigationSpec \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:23.440401+00:00
---

# TileNavigationSpec  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/TileNavigationSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  TileNavigationSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



This field specifies tile navigation related parameters.

JSON representation  
---  
      
    
    {
      "tileNavigationRequested": boolean,
      "appliedTiles": [
        {
          object ([Tile](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/Tile))
        }
      ]
    }  
  
Fields  
---  
`tileNavigationRequested` |  `boolean` This field specifies whether the customer would like to request tile navigation.  
`appliedTiles[]` |  `object (`[Tile](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/Tile)`)` This optional field specifies the tiles which are already clicked in client side. While the feature works without this field set, particularly for an initial query, it is highly recommended to set this field because it can improve the quality of the search response and removes possible duplicate tiles.NOTE: This field is not being used for filtering search products. Client side should also put all the applied tiles in `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
