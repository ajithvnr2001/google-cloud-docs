---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/openai/
title: OpenAI models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:43:25.394032+00:00
---

# OpenAI models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/openai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  OpenAI models Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** OpenAI models are not a Google product, and its availability in Gemini Enterprise Agent Platform is subject to the terms for "Separate Offerings" in the AI/ML Services section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms), and separate terms found in the relevant model card.

OpenAI models are available for use as managed APIs and self-deployed models on Gemini Enterprise Agent Platform. You can stream your responses to reduce the end-user latency perception. A streamed response uses _server-sent events_ (SSE) to incrementally stream the response.

### gpt-oss 120B

OpenAI gpt-oss 120B is a 120B open-weight language model released under the Apache 2.0 license. It is well-suited for reasoning and function calling use cases. The model is optimized for deployment on consumer hardware. 

The 120B model achieves near-parity with OpenAI o4-mini on core reasoning benchmarks, while running on a single 80GB GPU. 

[ Go to the gpt-oss 120B model card ](https://console.cloud.google.com/agent-platform/publishers/openai/model-garden/gpt-oss-120b-maas)

### gpt-oss 20B

OpenAI gpt-oss 20B is a 20B open-weight language model released under the Apache 2.0 license. It is well-suited for reasoning and function calling use cases. The model is optimized for deployment on consumer hardware. 

The 20B model delivers similar results to OpenAI o3-mini on common benchmarks and can run on edge devices with 16GB of memory, making it ideal for on-device use cases, local inference, or rapid iteration without costly infrastructure. 

[ Go to the gpt-oss 20B model card ](https://console.cloud.google.com/agent-platform/publishers/openai/model-garden/gpt-oss-20b-maas)

## Use OpenAI models

For managed models, you can use curl commands to send requests to the Gemini Enterprise Agent Platform endpoint using the following model names: 

  * For gpt-oss 120B, use `gpt-oss-120b-maas`
  * For gpt-oss 20B, use `gpt-oss-20b-maas`



To learn how to make streaming and non-streaming calls to OpenAI models, see [Call open model APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis). 

To use a self-deployed Gemini Enterprise Agent Platform model:

  1. Navigate to the [Model Garden console](https://console.cloud.google.com/agent-platform/model-garden).
  2. Find the relevant Gemini Enterprise Agent Platform model.
  3. Click **Enable** and complete the provided form to get the necessary commercial use licenses.



For more information about deploying and using partner models, see [ Deploy a partner model and make prediction requests ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/use-models#deploy_a_partner_model_and_make_prediction_requests). 

## OpenAI model region availability

OpenAI models are available in the following regions: 

Model | Regions  
---|---  
gpt-oss 120B | 

  * `global`

  
gpt-oss 20B | 

  * `us-central1`

  
  
## What's next

Learn how to [Call open model APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
