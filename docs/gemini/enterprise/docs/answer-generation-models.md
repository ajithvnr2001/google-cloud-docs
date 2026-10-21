---
url: https://docs.cloud.google.com/gemini/enterprise/docs/answer-generation-models/
title: Answer generation model versions and lifecycle for the Answer API (Legacy) \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:09.886714+00:00
---

# Answer generation model versions and lifecycle for the Answer API (Legacy)  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/answer-generation-models/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Developer guide ](https://docs.cloud.google.com/gemini/enterprise/docs/developer-guide)



Send feedback 

#  Answer generation model versions and lifecycle for the Answer API (Legacy) Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see [Get search results using StreamAssist](https://docs.cloud.google.com/gemini/enterprise/docs/get-answers-from-streamassist). 

Gemini Enterprise offers multiple model versions for you to choose when generating answers. You can choose the model versions when using [search summaries](https://docs.cloud.google.com/gemini/enterprise/docs/get-search-summaries) and [answers and follow-ups](https://docs.cloud.google.com/gemini/enterprise/docs/answer).

## Available models

Gemini Enterprise uses two types of models for question and answering use cases:

  * Gemini Enterprise Agent Platform LLM models that have been tested on question and answering tasks
  * Gemini Enterprise models that are based on Agent Platform LLM models and further trained to address question and answering tasks



Gemini Enterprise models share the same discontinuation date as their base Agent Platform LLM models. The base LLM model is available for six months after the release date of the next version of the model, according to the [Model versions and lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions). Leave enough time to migrate to new models before the discontinuation dates.

The following table lists model version specifications. When you set a model specification, the API uses the specified model to generate answers.

Model version1 | Description | Context window2 | Discontinuation date  
---|---|---|---  
`stable` |  The default model choice if the model version is not set.  The `stable` model specification points to `gemini-3.5-flash/answer_gen/v1`.  The model designated as `stable` changes periodically as new models and versions become available.  | 128K | N/A  
`gemini-3.1-pro-preview/answer_gen/v1` |  The [`gemini-3.1-pro-preview`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-pro) model.  | 128K | N/A  
`gemini-3-flash-preview/answer_gen/v1` |  The [`gemini-3-flash-preview`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-flash) model.  | 128K | N/A  
`gemini-3.5-flash/answer_gen/v1` |  The [`gemini-3.5-flash`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash) model.  | 128K | N/A  
  
1 The latest Gemini models might not be available for use with this API.

2 For quality and latency reasons, this context window is smaller than allowed elsewhere for these models.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
