---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/GenerativeQuestionConfig/
title: GenerativeQuestionConfig \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:21.313842+00:00
---

# GenerativeQuestionConfig  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/GenerativeQuestionConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  GenerativeQuestionConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Configuration for a single generated question.

JSON representation  
---  
      
    
    {
      "catalog": string,
      "facet": string,
      "generatedQuestion": string,
      "finalQuestion": string,
      "exampleValues": [
        string
      ],
      "frequency": number,
      "allowedInConversation": boolean
    }  
  
Fields  
---  
`catalog` |  `string` Required. Resource name of the catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog}  
`facet` |  `string` Required. The facet to which the question is associated.  
`generatedQuestion` |  `string` Output only. The LLM generated question.  
`finalQuestion` |  `string` Optional. The question that will be used at serving time. Question can have a max length of 300 bytes. When not populated, generatedQuestion should be used.  
`exampleValues[]` |  `string` Output only. Values that can be used to answer the question.  
`frequency` |  `number` Output only. The ratio of how often a question was asked.  
`allowedInConversation` |  `boolean` Optional. Whether the question is asked at serving time.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
