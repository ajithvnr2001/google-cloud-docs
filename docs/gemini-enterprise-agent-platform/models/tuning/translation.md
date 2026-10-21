---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/translation/
title: About supervised fine-tuning for Translation LLM models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:13.396522+00:00
---

# About supervised fine-tuning for Translation LLM models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  About supervised fine-tuning for Translation LLM models Stay organized with collections  Save and categorize content based on your preferences. 

Supervised fine-tuning is a good option when you have a translation task with available labeled text data. It's particularly effective for domain-specific applications where the translation significantly differs from the general data the large model was originally trained on.

Supervised fine-tuning adapts model behavior with a labeled dataset. This process adjusts the model's weights to minimize the difference between its inferences and the actual labels.

## Supported models

The following Translation LLM models support supervised tuning:

  * `translation-llm-002`



## Limitations

  * Maximum input and output tokens: 
    * Serving: 1,000 (~4000 characters)
  * Validation dataset size: 1024 examples
  * Training dataset file size: Up to 1GB for JSONL
  * Training example length: 1,000 (~4000 characters)
  * Adapter size: 
    * `Translation LLM V2`: Supported value is only 4. Using any other values (e.g., 1 or 8) will result in failure.



## Use cases for using supervised fine-tuning

General pretrained translation model works well when the text to be translated is based on general commonplace text structures that the model learned from. If you want a model to learn something niche or domain-specific that deviates from general translation, then you might want to consider tuning that model. For example, you can use model tuning to teach the model the following:

  * Specific content of an industry domain with jargon or style
  * Specific structures or formats for generating output.
  * Specific behaviors such as when to provide a terse or verbose output.
  * Specific customized outputs for specific types of inputs.



## Configure a tuning job region

User data, such as the transformed dataset and the tuned model, is stored in the tuning job region. The only supported region is `us-central1`.

  * If you use the Vertex AI SDK, you can specify the region at initialization. For example:
        
        import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
        [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project='myproject', location='us-central1')
        

  * If you create a supervised fine-tuning job by sending a POST request using the [`tuningJobs.create`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tuningJobs/create) method, then you use the URL to specify the region where the tuning job runs. For example, in the following URL, you specify a region by replacing both instances of `TUNING_JOB_REGION` with the region where the job runs.
        
        https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs
        

  * If you use the [Google Cloud console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning/use#create_a_text_model_supervised_tuning_job), you can select the region name in the **Region** drop down field on the **Model details** page. This is the same page where you select the base model and a tuned model name.




## Quota

Quota is enforced on the number of concurrent tuning jobs. Every project comes with a default quota to run at least one tuning job. This is a global quota, shared across all available regions and supported models. If you want to run more jobs concurrently, you need to [request additional quota](https://docs.cloud.google.com/docs/quota_detail/view_manage#requesting_higher_quota) for `Global concurrent tuning jobs`.

## Pricing

You are billed for tuning based on [pricing for Translation Model tuning](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#model-tuning).

You are also billed for related services, such as Cloud Storage and Translation LLM Prediction.

Learn about [Translation LLM pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#translation-text), [ Cloud Storage pricing](http://cloud.google.com/storage/pricing).

## What's next

  * Prepare a [supervised fine-tuning dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/translation/prepare-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
