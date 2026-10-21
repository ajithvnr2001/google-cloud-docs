---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SafetySetting/
title: SafetySetting \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:22.220909+00:00
---

# SafetySetting  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SafetySetting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  SafetySetting Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * HarmCategory
  * HarmBlockThreshold
  * HarmBlockMethod



Safety settings.

JSON representation  
---  
      
    
    {
      "category": enum ([HarmCategory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SafetySetting#HarmCategory)),
      "threshold": enum ([HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SafetySetting#HarmBlockThreshold)),
      "method": enum ([HarmBlockMethod](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SafetySetting#HarmBlockMethod))
    }  
  
Fields  
---  
`category` |  `enum (`[HarmCategory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SafetySetting#HarmCategory)`)` Harm category.  
`threshold` |  `enum (`[HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SafetySetting#HarmBlockThreshold)`)` The harm block threshold.  
`method` |  `enum (`[HarmBlockMethod](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SafetySetting#HarmBlockMethod)`)` Optional. Specify if the threshold is used for probability or severity score. If not specified, the threshold is used for probability score.  
  
## HarmCategory

Harm categories that will block the content.

Enums  
---  
`HARM_CATEGORY_UNSPECIFIED` | The harm category is unspecified.  
`HARM_CATEGORY_HATE_SPEECH` | The harm category is hate speech.  
`HARM_CATEGORY_DANGEROUS_CONTENT` | The harm category is dangerous content.  
`HARM_CATEGORY_HARASSMENT` | The harm category is harassment.  
`HARM_CATEGORY_SEXUALLY_EXPLICIT` | The harm category is sexually explicit content.  
`HARM_CATEGORY_CIVIC_INTEGRITY` | The harm category is civic integrity.  
  
## HarmBlockThreshold

Probability based thresholds levels for blocking.

Enums  
---  
`HARM_BLOCK_THRESHOLD_UNSPECIFIED` | Unspecified harm block threshold.  
`BLOCK_LOW_AND_ABOVE` | Block low threshold and above (i.e. block more).  
`BLOCK_MEDIUM_AND_ABOVE` | Block medium threshold and above.  
`BLOCK_ONLY_HIGH` | Block only high threshold (i.e. block less).  
`BLOCK_NONE` | Block none.  
`OFF` | Turn off the safety filter.  
  
## HarmBlockMethod

Probability vs severity.

Enums  
---  
`HARM_BLOCK_METHOD_UNSPECIFIED` | The harm block method is unspecified.  
`SEVERITY` | The harm block method uses both probability and severity scores.  
`PROBABILITY` | The harm block method uses the probability score.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
