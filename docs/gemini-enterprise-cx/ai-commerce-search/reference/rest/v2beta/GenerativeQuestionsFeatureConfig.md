---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/GenerativeQuestionsFeatureConfig/
title: GenerativeQuestionsFeatureConfig \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:10:53.455992+00:00
---

# GenerativeQuestionsFeatureConfig  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/GenerativeQuestionsFeatureConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  GenerativeQuestionsFeatureConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Configuration for overall generative question feature state.

JSON representation  
---  
      
    
    {
      "catalog": string,
      "featureEnabled": boolean,
      "minimumProducts": integer
    }  
  
Fields  
---  
`catalog` |  `string` Required. Resource name of the affected catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog}  
`featureEnabled` |  `boolean` Optional. Determines whether questions will be used at serving time. Note: This feature cannot be enabled until initial data requirements are satisfied.  
`minimumProducts` |  `integer` Optional. Minimum number of products in the response to trigger follow-up questions. Value must be 0 or positive.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
