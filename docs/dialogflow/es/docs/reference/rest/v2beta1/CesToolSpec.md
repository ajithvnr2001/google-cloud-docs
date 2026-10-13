---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/CesToolSpec/
title: CesToolSpec \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:10.177336+00:00
---

# CesToolSpec  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/CesToolSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  CesToolSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Spec of CES tool that the generator can choose from.

JSON representation  
---  
      
    
    {
      "cesTool": string,
      "confirmationRequirement": enum ([ConfirmationRequirement](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ConfirmationRequirement))
    }  
  
Fields  
---  
`cesTool` |  `string` Optional. Format: `projects/<Project ID>/locations/<Location ID>/apps/<app ID>/tools/<tool ID>`.  
`confirmationRequirement` |  `enum (`[ConfirmationRequirement](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ConfirmationRequirement)`)` Optional. Indicates whether the tool requires human confirmation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
