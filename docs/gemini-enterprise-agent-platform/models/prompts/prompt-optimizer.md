---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-optimizer/
title: Optimize prompts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:21.975982+00:00
---

# Optimize prompts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-optimizer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Optimize prompts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the Gemini Enterprise Agent Platform prompt optimizer to automatically optimize prompt performance by improving the [system instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instructions) for a set of prompts.

The Agent Platform prompt optimizer can help you improve your prompts quickly at scale, without manually rewriting system instructions or individual prompts. This is useful when changing between models and you want to reuse system instructions and prompts.

The following approaches are available for optimizing prompts:

  * The [**zero-shot optimizer**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/zero-shot-optimizer) is a real-time low-latency optimizer that improves a single prompt or system instruction template. It is fast and requires no additional setup besides providing your original prompt or system instruction. The zero-shot optimizer is model-independent and can improve prompts for most Google models. Also, it provides a `gemini_nano` mode to specifically [optimize prompts for smaller models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/zero-shot-optimizer#optimizing_for_smaller_models), such as [Gemini Nano](https://developer.android.com/ai/gemini-nano) and [Gemma 3n E4B](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-gemma).
  * The [**few-shot optimizer**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/few-shot-optimizer) is a real-time low-latency optimizer that refines system instructions by analyzing examples where a model's response did not meet expectations. By providing specific examples of prompts, model responses, and feedback on those responses, you can systematically improve prompt performance.
  * The [**data-driven optimizer**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/data-driven-optimizer) is a batch task-level iterative optimizer that improves prompts by evaluating the model's response to sample labeled prompts against specified evaluation metrics for your selected target model. It's for more advanced optimization that lets you configure the optimization parameters and provide a few labeled samples. Also, the data-driven optimizer supports optimization for generally-available Gemini models, such as [Gemini Nano](https://developer.android.com/ai/gemini-nano) and [Gemma 3n E4B](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-gemma), and custom models deployed locally or from the Gemini Enterprise Agent Platform Model Garden.



These methods are available to users through the Google Cloud console or the Vertex AI SDK.

To see examples of Prompt Optimizer, run the following notebooks in the environment of your choice:

  * "Zero-shot optimizer":

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/prompt_optimizer/get_started_with_vertex_ai_prompt_optimizer.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fprompts%2Fprompt_optimizer%2Fget_started_with_vertex_ai_prompt_optimizer.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fprompts%2Fprompt_optimizer%2Fget_started_with_vertex_ai_prompt_optimizer.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/prompt_optimizer/get_started_with_vertex_ai_prompt_optimizer.ipynb)

  * "Data-driven optimizer":

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/prompt_optimizer/get_started_with_vertex_ai_prompt_optimizer.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fprompts%2Fprompt_optimizer%2Fget_started_with_vertex_ai_prompt_optimizer.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fprompts%2Fprompt_optimizer%2Fget_started_with_vertex_ai_prompt_optimizer.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/prompt_optimizer/get_started_with_vertex_ai_prompt_optimizer.ipynb)

  * "Data-driven optimizer for custom metrics":

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/prompt_optimizer/get_started_with_vertex_ai_prompt_optimizer_custom_metric.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fprompts%2Fprompt_optimizer%2Fget_started_with_vertex_ai_prompt_optimizer_custom_metric.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fprompts%2Fprompt_optimizer%2Fget_started_with_vertex_ai_prompt_optimizer_custom_metric.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/prompt_optimizer/get_started_with_vertex_ai_prompt_optimizer_custom_metric.ipynb)




**Important:** While Prompt Optimizer is [generally available](https://cloud.google.com/products#product-launch-stages), its SDK library is still experimental. This means that the SDK is subject to change at any time without notice. We are continuously working to improve and stabilize the SDK. You may encounter bugs or changes to APIs and functionality.

## What's next

  * Learn about [zero-shot optimizer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/zero-shot-optimizer)

  * Learn about [few-shot optimizer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/few-shot-optimizer)

  * Learn about [data-driven optimizer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/data-driven-optimizer)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
