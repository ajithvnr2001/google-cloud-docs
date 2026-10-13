---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SafetySpec/
title: SafetySpec \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:44.492803+00:00
---

# SafetySpec  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SafetySpec/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  SafetySpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SafetySetting
    * JSON representation
  * HarmBlockThreshold



Safety specification. There are two use cases: 1. when only safetySpec.enable is set, the BLOCK_LOW_AND_ABOVE threshold will be applied for all categories. 2. when safetySpec.enable is set and some safetySettings are set, only specified safetySettings are applied.

JSON representation  
---  
      
    
    {
      "enable": boolean,
      "safetySettings": [
        {
          object ([SafetySetting](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SafetySpec#SafetySetting))
        }
      ]
    }  
  
Fields  
---  
`enable` |  `boolean` Enable the safety filtering on the answer response. It is false by default.  
`safetySettings[]` |  `object (`[SafetySetting](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SafetySpec#SafetySetting)`)` Optional. Safety settings. This settings are effective only when the safetySpec.enable is true.  
  
## SafetySetting

Safety settings.

JSON representation  
---  
      
    
    {
      "category": enum ([HarmCategory](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.HarmCategory)),
      "threshold": enum ([HarmBlockThreshold](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SafetySpec#HarmBlockThreshold))
    }  
  
Fields  
---  
`category` |  `enum (`[HarmCategory](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.HarmCategory)`)` Required. Harm category.  
`threshold` |  `enum (`[HarmBlockThreshold](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SafetySpec#HarmBlockThreshold)`)` Required. The harm block threshold.  
  
## HarmBlockThreshold

Probability-based thresholds levels for blocking.

Enums  
---  
`HARM_BLOCK_THRESHOLD_UNSPECIFIED` | Unspecified harm block threshold.  
`BLOCK_LOW_AND_ABOVE` | Block low threshold and above (i.e. block more).  
`BLOCK_MEDIUM_AND_ABOVE` | Block medium threshold and above.  
`BLOCK_ONLY_HIGH` | Block only high threshold (i.e. block less).  
`BLOCK_NONE` | Block none.  
`OFF` | Turn off the safety filter.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
