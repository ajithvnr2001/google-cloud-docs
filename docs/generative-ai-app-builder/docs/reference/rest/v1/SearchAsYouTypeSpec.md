---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SearchAsYouTypeSpec/
title: SearchAsYouTypeSpec \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:25.669846+00:00
---

# SearchAsYouTypeSpec  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SearchAsYouTypeSpec/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  SearchAsYouTypeSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Condition
  * Field
    * JSON representation



Specification for search as you type in search requests.

JSON representation  
---  
      
    
    {
      "condition": enum ([Condition](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SearchAsYouTypeSpec#Condition)),
      "fields": [
        {
          object ([Field](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SearchAsYouTypeSpec#Field))
        }
      ],
      "scoreThreshold": number
    }  
  
Fields  
---  
`condition` |  `enum (`[Condition](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SearchAsYouTypeSpec#Condition)`)` The condition under which search as you type should occur. Default to `[Condition.DISABLED](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SearchAsYouTypeSpec#Condition.ENUM_VALUES.DISABLED)`.  
`fields[]` |  `object (`[Field](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SearchAsYouTypeSpec#Field)`)` Optional. The list of fields to be used for Search As You type scoring.  
`scoreThreshold` |  `number` Optional. Search As You type score threshold for filtering purpose. We keep the result if `score` >= `scoreThreshold`.  
  
## Condition

Enum describing under which condition search as you type should occur.

Enums  
---  
`CONDITION_UNSPECIFIED` | Server behavior defaults to `[Condition.DISABLED](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SearchAsYouTypeSpec#Condition.ENUM_VALUES.DISABLED)`.  
`DISABLED` | Disables Search As You Type.  
`ENABLED` | Enables Search As You Type.  
`AUTO` | Automatic switching between search-as-you-type and standard search modes, ideal for single-API implementations (e.g., debouncing).  
  
## Field

A schema field to be used for Search As You type scoring on this request. Overrides any data-store-level Search As You type field configuration for the duration of the request.

JSON representation  
---  
      
    
    {
      "key": string,
      "weight": number
    }  
  
Fields  
---  
`key` |  `string` Required. A field key that has been indexed for Search As You type.  
`weight` |  `number` Optional. weight for scores from this field. Defaults to 1.0 if not specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-14 UTC."],[],[]] 
