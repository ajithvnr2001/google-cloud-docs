---
url: https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/
title: Overview of custom speech models \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:17.559249+00:00
---

# Overview of custom speech models  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Overview of custom speech models Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Custom Speech-to-Text models help you fine-tune speech recognition models to your specific needs. This service is designed to enhance the accuracy and relevance of speech recognition service in diverse environments and use cases, using your domain-specific audio and text data.

Accessible in both our Google Cloud console and API, Custom Speech-to-Text models allow to train, evaluate and deploy a dedicated speech model in a no-code integrated environment. For training you can provide audio data only that are representative of your audio conditions, without reference transcriptions as a training set. However, you need to provide audio data and their reference transcriptions as part of your evaluation set.

Creating and using a custom Cloud Speech-to-Text model involves the following steps:

  1. Prepare and upload training data in a Cloud Storage bucket.
  2. Train a new custom model.
  3. Deploy and manage your custom model using endpoints.
  4. Use and evaluate your custom model in your application.



## How does it work

You can use Custom Speech-to-Text models to augment a base transcription model to improve transcription recognition. Some audio conditions, including sirens, music, and excessive background noise can pose acoustic challenges. Certain accents or unusual vocabulary, such product names can as well.

Every Custom Speech-to-Text model uses pre-trained, Conformer-based architecture as a base model trained with proprietary data of commonly spoken language. During the training process, the base model is fine-tuned by adapting a significant percentage of the original weights to improve recognition of domain-specific vocabulary and audio conditions specific to your application.

For the effective training of a Custom Speech-to-Text model, you must provide:

  * Minimum 100 audio-hours of training data, either audio-only or audio with the corresponding text transcript as ground-truth. This data is crucial for the initial training phase, so the model comprehensively learns the nuances of the speech patterns and vocabulary. For details, see [Create a ground-truth dataset](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/prepare-data#ground-truth_annotation_guidelines). 
    * A separate dataset of at least 10 audio-hours of validation data, with the corresponding text transcript as ground-truth. You can learn more about the expected format and ground-truth conventions to be followed in our [data preparation instructions](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/prepare-data).



Following a successful training, you can deploy a Custom Speech-to-Text model in an endpoint with one click, and use it directly through the Cloud Cloud Speech-to-Text V2 API for inference and benchmarking.

## Supported models, languages and regions

Custom Speech-to-Text models support the following combinations of models and languages and locales for training:

Language | BCP-47 | Base model  
---|---|---  
German (Germany) |  de-DE |  `latest_long`  
English (Australia) |  en-AU |  `latest_long`  
English (United Kingdom) |  en-GB |  `latest_long`  
English (India) |  en-IN |  `latest_long`  
English (United States) |  en-US |  `latest_long`  
Spanish (United States) |  es-US |  `latest_long`  
Spanish (Spain) |  es-ES |  `latest_long`  
French (Canada) |  fr-CA |  `latest_long`  
French (France) |  fr-FR |  `latest_long`  
Hindi (India) |  hi-IN |  `latest_long`  
Italian (Italy) |  it-IT |  `latest_long`  
Japanese (Japan) |  ja-JP |  `latest_long`  
Korean (South Korea) |  ko-KR |  `latest_long`  
Dutch (Netherlands) |  nl-NL |  `latest_long`  
Portuguese (Brazil) |  pt-BR |  `latest_long`  
Portuguese (Portugal) |  pt-PT |  `latest_long`  
  
Additionally, to comply with your data residency requirements we offer training and deployment hardware in different regions. Dedicated hardware is supported in the following combinations of models and regions:

Base model | Google Cloud Region | Supported tasks  
---|---|---  
`latest_long` |  `us-east1` |  **Training** and **Deployment**  
`latest_long` |  `europe-west4` |  **Training** and **Deployment**  
  
## Quota

For Custom Speech-to-Text model training, each Google Cloud project should have enough default quota to run multiple training jobs concurrently and is intended to meet the needs of most projects without additional adjustments. However if you need to run a higher number of concurrent training jobs or require more extensive labeling or compute resources, then request additional quota.

For a Custom Speech-to-Text model serving an endpoint deployment, each endpoint has a theoretical limit of [20 queries per second (QPS)](https://docs.cloud.google.com/speech-to-text/quotas). If higher throughput is required, request additional serving quota.

## Pricing

Creating and using a Custom Speech-to-Text model involves certain costs which are primarily based on the resources used during the training and subsequent deployment of the model. Specifically, the Custom Speech-to-Text model will incur the following costs in a typical model lifecycle:

  * **Training** : You will be charged for the number of model-training hours. This time is proportional to the amount of audio-hours in the training dataset. As a rule, training takes a tenth of the number of audio-hours in the dataset.
  * **Deployment** : You will be charged for each hour that a model is deployed on an endpoint.
  * **Inference** : You will be charged for the number of streamed seconds of audio for transcription, in alignment with the general Cloud Speech-to-Text billing.



Understanding these costs is crucial for effective budgeting and resource allocation. For more information, in the Custom Speech-to-Text models section, see [Cloud Cloud Speech-to-Text pricing](https://cloud.google.com/speech-to-text/pricing).

## What's next

Follow the resources to take advantage of custom speech models in your application:

  * [Prepare your training data](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/prepare-data)
  * [Train and manage your custom models](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/train-model)
  * [Deploy and manage model endpoints ](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/deploy-model)
  * [Use your custom models](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/use-model)
  * [Evaluate your custom models](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/evaluate-model)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
