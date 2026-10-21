---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-for-tuned-gemini/
title: Context Caching for Fine-tuned Gemini Models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:34.177292+00:00
---

# Context Caching for Fine-tuned Gemini Models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-for-tuned-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Context Caching for Fine-tuned Gemini Models Stay organized with collections  Save and categorize content based on your preferences. 

You can use context caching for your fine-tuned Gemini models to improve performance and reduce costs for prompts that include large amounts of context. By caching frequently used context, you avoid re-sending large amounts of data with each request to your fine-tuned model.

The management operations (`Read`, `Update`, `Delete`) of the context cache for tuned Gemini models remain consistent with base models. Only cached content creation and inference require specific adjustment, which is detailed in the following sections.

## Prerequisites

**Fine-tuning a Gemini Model:** You need a deployed fine-tuned Gemini model based on a supported base model (see [Context caching overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview#supported_models)). For details on how to fine-tune a Gemini model, see [Fine-tune a Gemini model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini-use-supervised-tuning). To get the endpoint for your deployed tuned model, see [Deploy a tuned model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/overview#deploy_a_tuned_model).

Make sure that you have the following information:

  * The ID and the version of the tuned Gemini model
  * The endpoint resource name for the deployed fine-tuned model



## Supported versions

Fine-tuned Gemini models support implicit caching for specific versions. For a list of supported models and their capabilities, see [Google models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models).

Explicit caching is not supported for fine-tuned models.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
