---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/PersonalizationSpec/
title: PersonalizationSpec \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:08.961735+00:00
---

# PersonalizationSpec  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/PersonalizationSpec/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  PersonalizationSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Mode



The specification for personalization.

JSON representation  
---  
      
    
    {
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/PersonalizationSpec#Mode))
    }  
  
Fields  
---  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/PersonalizationSpec#Mode)`)` The personalization mode of the search request. Defaults to `[Mode.AUTO](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/PersonalizationSpec#Mode.ENUM_VALUES.AUTO)`.  
  
## Mode

The personalization mode of each search request.

Enums  
---  
`MODE_UNSPECIFIED` | Default value. In this case, server behavior defaults to `[Mode.AUTO](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/PersonalizationSpec#Mode.ENUM_VALUES.AUTO)`.  
`AUTO` | Personalization is enabled if data quality requirements are met.  
`DISABLED` | Disable personalization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-08 UTC."],[],[]] 
