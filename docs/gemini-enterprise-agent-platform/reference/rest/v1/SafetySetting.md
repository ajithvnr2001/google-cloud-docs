---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/SafetySetting/
title: SafetySetting \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:35:22.092961+00:00
---

# SafetySetting  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/SafetySetting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  SafetySetting Stay organized with collections  Save and categorize content based on your preferences. 

A safety setting that affects the safety-blocking behavior.

A `SafetySetting` consists of a harm `category` and a `threshold` for that category.

Fields  
  
`category` `enum (`[HarmCategory](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/HarmCategory)`)` Required. The harm category to be blocked. | `threshold` `enum (`[HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/HarmBlockThreshold)`)` Required. The threshold for blocking content. If the harm probability exceeds this threshold, the content will be blocked. | `method` `enum (`[HarmBlockMethod](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/SafetySetting#HarmBlockMethod)`)` Optional. The method for blocking content. If not specified, the default behavior is to use the probability score. | JSON representation  
---  
      
    
    {
      "category": enum ([HarmCategory](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/HarmCategory)),
      "threshold": enum ([HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/HarmBlockThreshold)),
      "method": enum ([HarmBlockMethod](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/SafetySetting#HarmBlockMethod))
    }  
  
## HarmBlockMethod

The method for blocking content.

Enums  
---  
`HARM_BLOCK_METHOD_UNSPECIFIED` | The harm block method is unspecified.  
`SEVERITY` | The harm block method uses both probability and severity scores.  
`PROBABILITY` | The harm block method uses the probability score.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-07 UTC."],[],[]] 
