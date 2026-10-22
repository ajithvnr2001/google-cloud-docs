---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/preference-tuning/
title: About preference tuning for Gemini models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:24.509896+00:00
---

# About preference tuning for Gemini models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/preference-tuning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  About preference tuning for Gemini models Stay organized with collections  Save and categorize content based on your preferences. 

To see an example of preference tuning, run the "Get Started with Gemini Preference Optimization" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/tuning/dpo_gemini_get_started.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Ftuning%2Fdpo_gemini_get_started.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Ftuning%2Fdpo_gemini_get_started.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/tuning/dpo_gemini_get_started.ipynb)

Gemini Enterprise Agent Platform preference tuning lets you tune your Gemini models with human feedback data.

Preference tuning enables the model to learn from subjective user preferences that are hard to define by using specific labels or through supervised fine-tuning alone.

The preference tuning input dataset contains examples consisting of a prompt and pair of responses indicating which one is preferred and which one is dispreferred. The model learns to generate preferred responses with higher probability and dispreferred responses with lower probability.

To learn how to prepare the dataset, see [Prepare preference tuning data for Gemini models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/preference-tuning/prepare-data).

## Supported models

The following Gemini models support preference tuning:

#### Click to expand supported models

  * [Gemini 2.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite)
  * [Gemini 2.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash)



## Limitations

Specification | Value  
---|---  
Modalities | Text  
File size of the training dataset | 1GB  
Maximum input and output tokens per training example | 131,072  
Maximum input and output serving tokens | Same as base Gemini model  
Maximum number of training examples in a training dataset | 10M text-only training examples  
Maximum validation dataset size | 5000 examples or 30% of the number of training examples if there are more than 1000 validation examples  
Adapter size | Supported values are 1, 2, 4, 8, and 16  
  
## Best practices

Before you apply the preference optimization algorithm to your model, we strongly recommend that you do the following:

  1. Tune the model using [supervised fine-tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning/prepare-data) on the preferred response data. This teaches the model to generate preferred responses during inference.
  2. [Continue tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/continuous-tuning) from the checkpoint produced from step 1 using preference tuning. This teaches the model to increase the likelihood gap between preferred and dispreferred responses.



For creating the supervised fine-tuning dataset, use the prompt and accepted response pairs in your preference dataset as prompt and target for your supervised fine-tuning dataset. Typically one or two epochs of supervised fine-tuning should be sufficient, although this can change based on the dataset size and how aligned your training dataset is with the Gemini model initially.

To use supervised fine-tuning to tune the model, follow the steps in [Tune Gemini models by using supervised fine-tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning/use).

## Quota

Quota is enforced on the number of concurrent tuning jobs. Every project comes with a default quota to run at least one tuning job. This is a global quota, shared across all available regions and supported models. If you want to run more jobs concurrently, you need to [request additional quota](https://docs.cloud.google.com/docs/quota_detail/view_manage#requesting_higher_quota) for `Global concurrent tuning jobs`.

## Pricing

Pricing for Gemini preference tuning can be found here: [Gemini Enterprise Agent Platform pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing#model-tuning).

For pricing purposes, the number of tokens for each tuning example is calculated by multiplying the number of tokens in the prompt by 2, and then adding the number of completion tokens.

## What's next

  * Prepare a [preference tuning dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/preference-tuning/prepare-data).
  * [Learn about deploying a tuned Gemini model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/overview#deploy_a_tuned_model).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
