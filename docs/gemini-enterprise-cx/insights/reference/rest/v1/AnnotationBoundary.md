---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/AnnotationBoundary/
title: AnnotationBoundary \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:33:39.974707+00:00
---

# AnnotationBoundary  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/AnnotationBoundary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  AnnotationBoundary Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A point in a conversation that marks the start or the end of an annotation.

JSON representation  
---  
      
    
    {
      "transcriptIndex": integer,
    
      // Union field detailed_boundary can be only one of the following:
      "wordIndex": integer
      // End of list of possible types for union field detailed_boundary.
    }  
  
Fields  
---  
`transcriptIndex` |  `integer` The index in the sequence of transcribed pieces of the conversation where the boundary is located. This index starts at zero.  
Union field `detailed_boundary`. A detailed boundary, which describes a more specific point. `detailed_boundary` can be only one of the following:  
`wordIndex` |  `integer` The word index of this boundary with respect to the first word in the transcript piece. This index starts at zero.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
