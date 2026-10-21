---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/Tile/
title: Tile \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:38:51.266322+00:00
---

# Tile  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/Tile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Tile Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



This field specifies the tile information including an attribute key, attribute value. More fields will be added in the future, eg: product id or product counts, etc.

JSON representation  
---  
      
    
    {
      "representativeProductId": string,
    
      // Union field product_attribute can be only one of the following:
      "productAttributeValue": {
        object ([ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ProductAttributeValue))
      },
      "productAttributeInterval": {
        object ([ProductAttributeInterval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ProductAttributeInterval))
      }
      // End of list of possible types for union field product_attribute.
    }  
  
Fields  
---  
`representativeProductId` |  `string` The representative product id for this tile.  
Union field `product_attribute`. The attribute key and value for the tile. `product_attribute` can be only one of the following:  
`productAttributeValue` |  `object (`[ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ProductAttributeValue)`)` The product attribute key-value.  
`productAttributeInterval` |  `object (`[ProductAttributeInterval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ProductAttributeInterval)`)` The product attribute key-numeric interval.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
