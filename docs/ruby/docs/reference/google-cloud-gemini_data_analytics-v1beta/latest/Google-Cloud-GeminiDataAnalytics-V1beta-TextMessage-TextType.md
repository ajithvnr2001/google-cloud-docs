---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-TextMessage-TextType/
title: Data Analytics API with Gemini V1BETA API - Module Google::Cloud::GeminiDataAnalytics::V1beta::TextMessage::TextType (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:14.398987+00:00
---

# Data Analytics API with Gemini V1BETA API - Module Google::Cloud::GeminiDataAnalytics::V1beta::TextMessage::TextType (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-TextMessage-TextType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Module Google::Cloud::GeminiDataAnalytics::V1beta::TextMessage::TextType (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API module Google::Cloud::GeminiDataAnalytics::V1beta::TextMessage::TextType.

The type of the text message.

## Constants 

### TEXT_TYPE_UNSPECIFIED

**value:** 0  
The default text type.

### FINAL_RESPONSE

**value:** 1  
The text is a final response to the user question.

### THOUGHT

**value:** 2  
The text is a thought from the model.

### PROGRESS

**value:** 3  
The text is an informational message about the agent's progress, such as a tool being invoked. This is distinct from the agent's internal thought process (`THOUGHT`) and the final answer to the user (`FINAL_RESPONSE`). These messages provide insight into the agent's actions.

### FOLLOWUP_QUESTIONS

**value:** 4  
The text is a list of follow-up questions suggested. Each item in parts is a follow-up question.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
