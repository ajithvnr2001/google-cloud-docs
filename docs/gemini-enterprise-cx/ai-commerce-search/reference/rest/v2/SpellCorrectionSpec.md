---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SpellCorrectionSpec/
title: SpellCorrectionSpec \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:23.613770+00:00
---

# SpellCorrectionSpec  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SpellCorrectionSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  SpellCorrectionSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Mode



The specification for query spell correction.

JSON representation  
---  
      
    
    {
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SpellCorrectionSpec#Mode))
    }  
  
Fields  
---  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SpellCorrectionSpec#Mode)`)` The mode under which spell correction should take effect to replace the original search query. Default to `[Mode.AUTO](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SpellCorrectionSpec#Mode.ENUM_VALUES.AUTO)`.  
  
## Mode

Enum describing under which mode spell correction should occur.

Enums  
---  
`MODE_UNSPECIFIED` | Unspecified spell correction mode. In this case, server behavior defaults to `[Mode.AUTO](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SpellCorrectionSpec#Mode.ENUM_VALUES.AUTO)`.  
`SUGGESTION_ONLY` | Google Retail Search will try to find a spell suggestion if there is any and put in the `[SearchResponse.corrected_query](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#FIELDS.corrected_query)`. The spell suggestion will not be used as the search query.  
`AUTO` | Automatic spell correction built by Google Retail Search. Search will be based on the corrected query if found.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
