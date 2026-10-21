---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/RedactionConfig/
title: RedactionConfig \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:22:35.655374+00:00
---

# RedactionConfig  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/RedactionConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  RedactionConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



DLP resources used for redaction while ingesting conversations. DLP settings are applied to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversation coming from CCAI Platform. They are not applied to conversations ingested from the `CreateConversation` endpoint or the Dialogflow / Agent Assist runtime integrations. When using Dialogflow / Agent Assist runtime integrations, redaction should be performed in Dialogflow / Agent Assist.

JSON representation  
---  
      
    
    {
      "deidentifyTemplate": string,
      "inspectTemplate": string
    }  
  
Fields  
---  
`deidentifyTemplate` |  `string` The fully-qualified DLP deidentify template resource name. Format: `projects/{project}/deidentifyTemplates/{template}`  
`inspectTemplate` |  `string` The fully-qualified DLP inspect template resource name. Format: `projects/{project}/locations/{location}/inspectTemplates/{template}`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
