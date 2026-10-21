---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/
title: Fully-managed Llama models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:18.993715+00:00
---

# Fully-managed Llama models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Fully-managed Llama models Stay organized with collections  Save and categorize content based on your preferences. 

  


Llama models are available for use as managed APIs and self-deployed models on Gemini Enterprise Agent Platform. You can stream your responses to reduce the end-user latency perception. A streamed response uses _server-sent events_ (SSE) to incrementally stream the response.

## Managed Llama models

Llama models offer fully managed and serverless models as APIs. To use a Llama model on Agent Platform, send a request directly to the Agent Platform API endpoint. When using Llama models as a managed API, there's no need to provision or manage infrastructure.

The following models are available from Llama to use in Gemini Enterprise Agent Platform. To access a Llama model, go to its Model Garden model card.

[Llama 4 Maverick 17B-128E](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/llama4-maverick) The largest and most capable multimodal Llama 4 model (MoE 17B active / 400B total), optimized for coding, deep reasoning, sophisticated chat, and high-precision image understanding. [Llama 4 Scout 17B-16E](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/llama4-scout) High-efficiency MoE model (17B active / 109B total) delivering state-of-the-art results for long-context retrieval, document summarization, and reasoning across large codebases. block [Llama 3.3 70B](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/llama3-3) A text-only 70B instruction-tuned model that provides enhanced performance relative to Llama 3.1 70B and Llama 3.2 90B for text-only applications.

## Use Llama models

For managed models, you can use curl commands to send requests to the Gemini Enterprise Agent Platform endpoint using the following model names. To learn how to make streaming and non-streaming calls to Llama models, see [Call open model APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis).

To use a self-deployed Gemini Enterprise Agent Platform model:

  1. Navigate to the [Model Garden console](https://console.cloud.google.com/agent-platform/model-garden).
  2. Find the relevant Gemini Enterprise Agent Platform model.
  3. Click **Enable** and complete the provided form to get the necessary commercial use licenses.



For more information about deploying and using partner models, see [Deploy a partner model and make prediction requests](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/use-models#deploy_a_partner_model_and_make_prediction_requests).

## What's next

[Learn how to use Llama models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/use-llama).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
