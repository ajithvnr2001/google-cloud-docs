---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/process-blocked-responses/
title: Process blocked responses \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:45:34.545064+00:00
---

# Process blocked responses  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/process-blocked-responses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Process blocked responses Stay organized with collections  Save and categorize content based on your preferences. 

When interacting with Gemini on Gemini Enterprise Agent Platform, your requests (prompts) or the generated responses might be blocked by content filters. This document provides guidance on how to identify and process these blocked responses.

## When is content blocked?

There are two scenarios for content filters blocking content:

  * The input prompt is blocked.
  * The model's response is blocked.



The sections that follow describe how to process each scenario.

### The input prompt is blocked

If your input prompt is blocked by content filters before it is sent to the model, the API response exhibits the following characteristics:

  * The [`promptFeedback`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GenerateContentResponse#PromptFeedback) field is populated. This field contains information about why the prompt is blocked.
  * The [`candidates`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GenerateContentResponse) field isn't set.



### The model's response is blocked

If the model generates a response but that response is blocked by content filters, the API response exhibits the following characteristics:

  * The [`promptFeedback`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GenerateContentResponse#PromptFeedback) field isn't set.
  * The [`candidates`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GenerateContentResponse) field is set with the following characteristics: 
    * The [`content`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Content) field isn't set.
    * The [`finishReason`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GenerateContentResponse#FinishReason) field is set and indicates why response generation stopped.



You can determine why the content was blocked by inspecting these fields in the API response.

## What's next

  * Learn how to [configure content filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
