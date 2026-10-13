---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/BoostSpec/
title: BoostSpec \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:29.400908+00:00
---

# BoostSpec  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/BoostSpec/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  BoostSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ConditionBoostSpec
    * JSON representation



Specification to boost suggestions based on the condition of the suggestion.

JSON representation  
---  
      
    
    {
      "conditionBoostSpecs": [
        {
          object ([ConditionBoostSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/BoostSpec#ConditionBoostSpec))
        }
      ]
    }  
  
Fields  
---  
`conditionBoostSpecs[]` |  `object (`[ConditionBoostSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/BoostSpec#ConditionBoostSpec)`)` Condition boost specifications. If a suggestion matches multiple conditions in the specifications, boost values from these specifications are all applied and combined in a non-linear way. Maximum number of specifications is 20.Note: Currently only support language condition boost.  
  
## ConditionBoostSpec

Boost applies to suggestions which match a condition.

JSON representation  
---  
      
    
    {
      "condition": string,
      "boost": number
    }  
  
Fields  
---  
`condition` |  `string` An expression which specifies a boost condition. The syntax is the same as [filter expression syntax](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax). Currently, the only supported condition is a list of BCP-47 lang codes.Example:

  * To boost suggestions in languages `en` or `fr`: `(lang_code: ANY("en", "fr"))`

  
`boost` |  `number` Strength of the boost, which should be in [-1, 1]. Negative boost means demotion. Default is 0.0.Setting to 1.0 gives the suggestions a big promotion. However, it does not necessarily mean that the top result will be a boosted suggestion.Setting to -1.0 gives the suggestions a big demotion. However, other suggestions that are relevant might still be shown.Setting to 0.0 means no boost applied. The boosting condition is ignored.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-27 UTC."],[],[]] 
