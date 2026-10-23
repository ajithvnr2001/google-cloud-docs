---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/llama4-scout/
title: Llama 4 Scout 17B-16E \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:57.736170+00:00
---

# Llama 4 Scout 17B-16E  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama/llama4-scout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Llama 4 Scout 17B-16E Stay organized with collections  Save and categorize content based on your preferences. 

Llama 4 Scout 17B-16E delivers state-of-the-art results for its size class that outperforms previous Llama generations and other open and proprietary models on several benchmarks. It features MoE architecture with 17 billion active parameters out of the 109 billion total parameters and 16 experts.

Llama 4 Scout 17B-16E is suited for retrieval tasks within long contexts and tasks that demand reasoning over large amounts of information, such as summarizing multiple large documents, analyzing extensive user interaction logs for personalization, and reasoning across large codebases.

## Managed API (MaaS) specifications

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/generative/multimodal/create/text?model=llama-4-scout-17b-16e-instruct-maas) [View model card in Model Garden](https://console.cloud.google.com/agent-platform/publishers/meta/model-garden/llama-4-maverick-17b-128e-instruct-maas)

Model ID | `llama-4-scout-17b-16e-instruct-maas`  
---|---  
Launch stage | GA  
Supported inputs & outputs | 

  * Inputs: Text, Code, Images
  * Outputs: Text

  
Capabilities | 

  * Supported
    * [Batch predictions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/capabilities/batch-prediction)
    * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/capabilities/function-calling)
    * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/capabilities/structured-output)
  * Not supported
    * [Llama Guard](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama)

  
Usage types | 

  * Supported
    * [Standard pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo)
    * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)
  * Not supported
    * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)

  
Knowledge cutoff date | August 2024  
Versions | 

  * `llama-4-scout-17b-16e-instruct-maas`
    * **Launch stage:** GA
    * **Release date:** April 29, 2025

  
Supported regions  
Model availability | 

  * United States
    * `us-east5`

  
ML processing | 

  * United States
    * `Multi-region`

  
Quota limits |  us-east5: 

  * Max output: 8,192
  * Context length: 1,310,720

  
Pricing | See [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing).  
  
## Deploy as a self-deployed model

To self-deploy the model, navigate to the [Llama 4 Scout 17B-16E model card](https://console.cloud.google.com/agent-platform/publishers/meta/model-garden/llama4) in the Model Garden console and click **Deploy model**. For more information about deploying and using partner models, see [Deploy a partner model and make prediction requests](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/use-models#deploy_a_partner_model_and_make_prediction_requests).

## Considerations

  * You can include a maximum of three images per request.
  * The MaaS endpoint doesn't use Llama Guard, unlike previous versions. To use Llama Guard, deploy Llama Guard from Model Garden and then send the prompts and responses to that endpoint. However, compared to Llama 4, Llama Guard has a more limited context (128,000) and can only process requests with a single image at the beginning of the prompt.
  * Batch predictions aren't supported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
