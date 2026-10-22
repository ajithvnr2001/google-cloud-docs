---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/deepseek/
title: DeepSeek models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:46.629861+00:00
---

# DeepSeek models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/deepseek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  DeepSeek models Stay organized with collections  Save and categorize content based on your preferences. 

DeepSeek models are available for use as managed APIs and self-deployed models on Gemini Enterprise Agent Platform. You can stream your responses to reduce the end-user latency perception. A streamed response uses _server-sent events_ (SSE) to incrementally stream the response.

## Managed DeepSeek models

**Note:** The DeepSeek R1 model is not a Google product, and its availability in Gemini Enterprise Agent Platform is subject to the terms for "Separate Offerings" in the AI/ML Services section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms), and separate terms found in the relevant model card.

DeepSeek models offer fully managed and serverless models as APIs. To use a DeepSeek model on Agent Platform, send a request directly to the Agent Platform API endpoint. When using DeepSeek models as a managed API, there's no need to provision or manage infrastructure.

The following models are available from DeepSeek to use in Gemini Enterprise Agent Platform. To access a DeepSeek model, go to its Model Garden model card.

### DeepSeek-V4.1-Flash

DeepSeek-V4.1-Flash is a multimodal Mixture-of-Experts (MoE) model from DeepSeek built for agentic and coding tasks. It accepts text and image input and has a context window of up to 1M tokens. 

[ Go to the DeepSeek-V4.1-Flash model card ](https://console.cloud.google.com/agent-platform/publishers/deepseek-ai/model-garden/deepseek-v4.1-flash-maas)

### DeepSeek-OCR

**Caution:** As of July 21, 2026, this model endpoint is deprecated and will be retired on October 21, 2026. For more information, see [Open model deprecations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/open-models).  DeepSeek-OCR is a comprehensive Optical Character Recognition (OCR) model that analyzes and understands complex documents. It excels at challenging OCR tasks, including recognizing mathematical formulas and processing text that is curved, rotated, or overlapping. 

[ Go to the DeepSeek-OCR model card ](https://console.cloud.google.com/agent-platform/publishers/deepseek-ai/model-garden/deepseek-ocr-maas)

### DeepSeek-V3.2

**Caution:** As of July 21, 2026, this model endpoint is deprecated and will be retired on October 21, 2026. For more information, see [Open model deprecations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/open-models).  DeepSeek-V3.2 is a model that harmonizes high computational efficiency with superior reasoning and agent performance. DeepSeek's approach is built upon three key technical breakthroughs: DeepSeek Sparse Attention (DSA), scalable reinforcement learning framework, and large scale agentic task synthesis pipeline. 

[ Go to the DeepSeek-V3.2 model card ](https://console.cloud.google.com/agent-platform/publishers/deepseek-ai/model-garden/deepseek-v3.2-maas)

### DeepSeek-V3.1

**Caution:** As of July 21, 2026, this model endpoint is deprecated and will be retired on October 21, 2026. For more information, see [Open model deprecations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/open-models).  DeepSeek-V3.1 is a hybrid model that supports both thinking mode and non-thinking mode. Compared to the previous version, this upgrade brings improvements in hybrid thinking modes, tool calling, and thinking efficiency. 

[ Go to the DeepSeek-V3.1 model card ](https://console.cloud.google.com/agent-platform/publishers/deepseek-ai/model-garden/deepseek-v3.1-maas)

### DeepSeek R1 (0528)

**Caution:** As of July 21, 2026, this model endpoint is deprecated and will be retired on October 21, 2026. For more information, see [Open model deprecations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/open-models). 

DeepSeek R1 (0528) is the latest version of the DeepSeek R1 model. Compared to DeepSeek-R1, it has significantly improved depth of reasoning and inference capabilities. DeepSeek R1 (0528) excels in wide range tasks, such as creative writing, general question answering, editing, and summarization.

#### Considerations

For production-ready safety, integrate DeepSeek R1 (0528) with [Model Armor](https://cloud.google.com/security-command-center/docs/model-armor-overview), which screens LLM prompts and responses for various security and safety risks. 

[ Go to the DeepSeek R1 (0528) model card ](https://console.cloud.google.com/agent-platform/publishers/deepseek-ai/model-garden/deepseek-r1-0528-maas)

## Use DeepSeek models

For managed models, you can use curl commands to send requests to the Gemini Enterprise Agent Platform endpoint using the following model names: 

  * For DeepSeek-V4.1-Flash, use `deepseek-v4.1-flash-maas`
  * For DeepSeek-OCR, use `deepseek-ocr-maas`
  * For DeepSeek-V3.2, use `deepseek-v3.2-maas`
  * For DeepSeek-V3.1, use `deepseek-v3.1-maas`
  * For DeepSeek R1 (0528), use `deepseek-r1-0528-maas`



To learn how to make streaming and non-streaming calls to DeepSeek models, see [Call open model APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis). 

To use a self-deployed Gemini Enterprise Agent Platform model:

  1. Navigate to the [Model Garden console](https://console.cloud.google.com/agent-platform/model-garden).
  2. Find the relevant Gemini Enterprise Agent Platform model.
  3. Click **Enable** and complete the provided form to get the necessary commercial use licenses.



For more information about deploying and using partner models, see [ Deploy a partner model and make prediction requests ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/use-models#deploy_a_partner_model_and_make_prediction_requests). 

## DeepSeek model region availability

DeepSeek models are available in the following regions: 

Model | Regions  
---|---  
DeepSeek-V4.1-Flash | 

  * `global`

  
DeepSeek-OCR | 

  * `us-central1`

  
DeepSeek-V3.2 | 

  * `global`

  
DeepSeek-V3.1 | 

  * `us-central1`

  
DeepSeek R1 (0528) | 

  * `us-central1`

  
  
## What's next

Learn how to [Call open model APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
