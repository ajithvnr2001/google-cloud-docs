---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BoostSpec/
title: BoostSpec \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:20.209123+00:00
---

# BoostSpec  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BoostSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  BoostSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Boost specification to boost certain items.

JSON representation  
---  
      
    
    {
      "conditionBoostSpecs": [
        {
          object ([ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConditionBoostSpec))
        }
      ],
      "skipBoostSpecValidation": boolean
    }  
  
Fields  
---  
`conditionBoostSpecs[]` |  `object (`[ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConditionBoostSpec)`)` Condition boost specifications. If a product matches multiple conditions in the specifications, boost scores from these specifications are all applied and combined in a non-linear way. Maximum number of specifications is 20.  
`skipBoostSpecValidation` |  `boolean` Whether to skip boostspec validation. If this field is set to true, invalid `[BoostSpec.condition_boost_specs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BoostSpec#FIELDS.condition_boost_specs)` will be ignored and valid `[BoostSpec.condition_boost_specs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BoostSpec#FIELDS.condition_boost_specs)` will still be applied.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
