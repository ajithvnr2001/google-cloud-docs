---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/UrlContextResult/
title: UrlContextResult \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:44:29.414826+00:00
---

# UrlContextResult  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/UrlContextResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  UrlContextResult Stay organized with collections  Save and categorize content based on your preferences. 

The result of the URL context.

Fields  
  
`url` `string` The URL that was fetched. | `status` `enum (`[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/UrlContextResult#Status)`)` The status of the URL retrieval. | JSON representation  
---  
      
    
    {
      "url": string,
      "status": enum ([Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/UrlContextResult#Status))
    }  
  
## Status

The status of the URL retrieval.

Enums  
---  
`STATUS_UNSPECIFIED` | Unspecified status. This value should not be used.  
`SUCCESS` | url retrieval is successful.  
`ERROR` | url retrieval is failed due to error.  
`PAYWALL` | url retrieval is failed because the content is behind paywall.  
`UNSAFE` | url retrieval is failed because the content is unsafe.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
