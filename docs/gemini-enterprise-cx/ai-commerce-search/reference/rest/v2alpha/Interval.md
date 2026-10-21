---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Interval/
title: Interval \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:07:10.340565+00:00
---

# Interval  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Interval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Interval Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A floating point interval.

JSON representation  
---  
      
    
    {
    
      // Union field min can be only one of the following:
      "minimum": number,
      "exclusiveMinimum": number
      // End of list of possible types for union field min.
    
      // Union field max can be only one of the following:
      "maximum": number,
      "exclusiveMaximum": number
      // End of list of possible types for union field max.
    }  
  
Fields  
---  
Union field `min`. The lower bound of the interval. If neither of the min fields are set, then the lower bound is negative infinity.This field must not be larger than max. Otherwise, an INVALID_ARGUMENT error is returned. `min` can be only one of the following:  
`minimum` |  `number` Inclusive lower bound.  
`exclusiveMinimum` |  `number` Exclusive lower bound.  
Union field `max`. The upper bound of the interval. If neither of the max fields are set, then the upper bound is positive infinity.This field must be not smaller than min. Otherwise, an INVALID_ARGUMENT error is returned. `max` can be only one of the following:  
`maximum` |  `number` Inclusive upper bound.  
`exclusiveMaximum` |  `number` Exclusive upper bound.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
