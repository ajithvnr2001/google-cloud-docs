---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/GroundingSpec/
title: GroundingSpec \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:43.530203+00:00
---

# GroundingSpec  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/GroundingSpec/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  GroundingSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * FilteringLevel



Grounding specification.

JSON representation  
---  
      
    
    {
      "includeGroundingSupports": boolean,
      "filteringLevel": enum ([FilteringLevel](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/GroundingSpec#FilteringLevel))
    }  
  
Fields  
---  
`includeGroundingSupports` |  `boolean` Optional. Specifies whether to include groundingSupports in the answer. The default value is `false`.When this field is set to `true`, returned answer will have `groundingScore` and will contain GroundingSupports for each claim.  
`filteringLevel` |  `enum (`[FilteringLevel](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/GroundingSpec#FilteringLevel)`)` Optional. Specifies whether to enable the filtering based on grounding score and at what level.  
  
## FilteringLevel

Level to filter based on answer grounding.

Enums  
---  
`FILTERING_LEVEL_UNSPECIFIED` | Default is no filter  
`FILTERING_LEVEL_LOW` | Filter answers based on a low threshold.  
`FILTERING_LEVEL_HIGH` | Filter answers based on a high threshold.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
