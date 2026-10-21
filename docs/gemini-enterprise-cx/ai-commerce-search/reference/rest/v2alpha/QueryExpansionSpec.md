---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/QueryExpansionSpec/
title: QueryExpansionSpec \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:59:45.498240+00:00
---

# QueryExpansionSpec  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/QueryExpansionSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  QueryExpansionSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Condition



Specification to determine under which conditions query expansion should occur.

JSON representation  
---  
      
    
    {
      "condition": enum ([Condition](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/QueryExpansionSpec#Condition)),
      "pinUnexpandedResults": boolean
    }  
  
Fields  
---  
`condition` |  `enum (`[Condition](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/QueryExpansionSpec#Condition)`)` The condition under which query expansion should occur. Default to `[Condition.DISABLED](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/QueryExpansionSpec#Condition.ENUM_VALUES.DISABLED)`.  
`pinUnexpandedResults` |  `boolean` Whether to pin unexpanded results. The default value is false. If this field is set to true, unexpanded products are always at the top of the search results, followed by the expanded results.  
  
## Condition

Enum describing under which condition query expansion should occur.

Enums  
---  
`CONDITION_UNSPECIFIED` | Unspecified query expansion condition. In this case, server behavior defaults to `[Condition.DISABLED](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/QueryExpansionSpec#Condition.ENUM_VALUES.DISABLED)`.  
`DISABLED` | Disabled query expansion. Only the exact search query is used, even if `[SearchResponse.total_size](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse#FIELDS.total_size)` is zero.  
`AUTO` | Automatic query expansion built by Google Retail Search.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
