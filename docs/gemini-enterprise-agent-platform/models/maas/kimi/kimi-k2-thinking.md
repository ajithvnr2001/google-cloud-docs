---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/kimi/kimi-k2-thinking/
title: Kimi K2 Thinking \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:00:53.789186+00:00
---

# Kimi K2 Thinking  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/kimi/kimi-k2-thinking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Kimi K2 Thinking Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of July 21, 2026, the `kimi-k2-thinking-maas` endpoint is deprecated and will be retired on October 21, 2026. For more information, see [Open model deprecations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/open-models). 

Kimi K2 Thinking is an open-source model that operates as a "thinking agent," reasoning step-by-step while using tools to achieve state-of-the-art performance on various benchmarks. It is capable of executing up to 200-300 sequential tool calls without human intervention, allowing it to solve complex problems across a wide range of tasks. The model uses Quantization-Aware Training (QAT) to support INT4 inference, which provides a roughly 2x improvement in generation speed.

## Managed API (MaaS) specifications

[Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `kimi-k2-thinking-maas`  
---|---  
Modalities |  description  Text   
Input and output  hide_image  Image   
Not supported  mic_off  Audio   
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
Supported
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

  * Multi-region: `us`

  
Quotas | 

  * **`global`** : 262,144 maximum output, 262,144 context length

  
Versions | 

  * `Kimi K2 Thinking`
    * Launch stage: GA
    * Release date: Nov 13, 2025

  
  
## Deploy as a self-deployed model

To self-deploy the model, navigate to the [Kimi K2 Thinking model card](https://console.cloud.google.com/agent-platform/publishers/moonshotai/model-garden/kimi-k2) in the Model Garden console and click **Deploy model**. For more information about deploying and using partner models, see [Deploy a partner model and make prediction requests](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/use-models#deploy_a_partner_model_and_make_prediction_requests). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
