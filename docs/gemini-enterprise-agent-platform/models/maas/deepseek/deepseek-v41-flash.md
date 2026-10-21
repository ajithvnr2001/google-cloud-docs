---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/deepseek/deepseek-v41-flash/
title: DeepSeek-V4.1-Flash \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:16:30.004373+00:00
---

# DeepSeek-V4.1-Flash  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/deepseek/deepseek-v41-flash/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  DeepSeek-V4.1-Flash Stay organized with collections  Save and categorize content based on your preferences. 

DeepSeek-V4.1-Flash is a multimodal Mixture-of-Experts (MoE) model from DeepSeek built for agentic and coding tasks. It accepts text and image input and has a context window of up to 1M tokens. It activates 8B of its 552B backbone parameters per token during prefill, which keeps input-heavy agentic workloads cost-efficient.

The `deepseek-v4.1-flash-maas` endpoint is available until at least November 28, 2026. Availability might be extended based on usage and demand. For more information, see [Minimum availability for Preview models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/open-models#minimum-availability).

## Managed API (MaaS) specifications

[Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `deepseek-v4.1-flash-maas`  
---|---  
Modalities |  description  Text   
Input and output  photo  Image   
Input only  mic_off  Audio   
Not supported  videocam_off  Video   
Not supported   
Capabilities | 

  * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/function-calling)   
Supported
  * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output)   
Supported
  * [Thinking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/capabilities/thinking)   
Supported

  
Consumption options | 

  * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)   
Not supported
  * [Batch inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference)   
Not supported
  * [Pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)   
Standard PayGo  
Supported
  * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)   
Not supported

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * Global: `global`

  
**[ML processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency) ** | 

  * Global: `global`

  
Quotas | 

  * **`global`** : 1,048,576 maximum output, 1,048,576 context length

  
Versions | 

  * `deepseek-v4.1-flash-maas`
    * Launch stage: Preview
    * Release date: October 14, 2026

  
  
## Deploy as a self-deployed model

To self-deploy the model, navigate to the [DeepSeek-V4.1-Flash model card](https://console.cloud.google.com/agent-platform/publishers/deepseek-ai/model-garden/deepseek-v4.1) in the Model Garden console and click **Deploy model**. For more information about deploying and using partner models, see [Deploy a partner model and make prediction requests](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/use-models#deploy_a_partner_model_and_make_prediction_requests).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
