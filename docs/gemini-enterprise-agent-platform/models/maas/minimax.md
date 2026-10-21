---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/minimax/
title: MiniMax models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:00:55.762066+00:00
---

# MiniMax models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/minimax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  MiniMax models Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** All MiniMax Model as a Service (MaaS) endpoints are either deprecated or retired. You can either [self-deploy your model from Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models) or migrate your workloads to alternative managed endpoints before the retirement date. For more information, see [Open model deprecations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/open-models). 

MiniMax models are available for use as managed APIs and self-deployed models on Gemini Enterprise Agent Platform. You can stream your responses to reduce the end-user latency perception. A streamed response uses _server-sent events_ (SSE) to incrementally stream the response.

## Managed MiniMax models

MiniMax models offer fully managed and serverless models as APIs. To use a MiniMax model on Agent Platform, send a request directly to the Agent Platform API endpoint. When using MiniMax models as a managed API, there's no need to provision or manage infrastructure.

The following models are available from MiniMax to use in Gemini Enterprise Agent Platform. To access a MiniMax model, go to its Model Garden model card.

### MiniMax M2

MiniMax M2 is a model from MiniMax that's designed for agentic and code-related tasks. It is built for end-to-end development workflows and has strong capabilities in planning and executing complex tool-calling tasks. The model is optimized to provide a balance of performance, cost, and inference speed. 

[ Go to the MiniMax M2 model card ](https://console.cloud.google.com/agent-platform/publishers/minimaxai/model-garden/minimax-m2-maas)

## Use MiniMax models

For managed models, you can use curl commands to send requests to the Gemini Enterprise Agent Platform endpoint using the following model names: 

  * For MiniMax M2, use `minimax-m2-maas`



To learn how to make streaming and non-streaming calls to MiniMax models, see [Call open model APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis). 

To use a self-deployed Gemini Enterprise Agent Platform model:

  1. Navigate to the [Model Garden console](https://console.cloud.google.com/agent-platform/model-garden).
  2. Find the relevant Gemini Enterprise Agent Platform model.
  3. Click **Enable** and complete the provided form to get the necessary commercial use licenses.



For more information about deploying and using partner models, see [ Deploy a partner model and make prediction requests ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/use-models#deploy_a_partner_model_and_make_prediction_requests). 

## MiniMax model region availability

MiniMax models are available in the following regions: 

Model | Regions  
---|---  
MiniMax M2 | 

  * `global`

  
  
## What's next

Learn how to [Call open model APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
