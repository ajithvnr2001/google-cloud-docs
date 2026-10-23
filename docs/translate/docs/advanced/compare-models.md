---
url: https://docs.cloud.google.com/translate/docs/advanced/compare-models/
title: Choose the right model for your application \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:51.055057+00:00
---

# Choose the right model for your application  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/compare-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback 

#  Choose the right model for your application Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Translation - Basic API gives you straightforward access to Google's Neural Machine Translation (NMT) model without modified settings. It also supports the standard TLLM model if you specify its full resource name. Cloud Translation - Basic supports only standard models, not customized models. Cloud Translation - Advanced lets you choose between the default NMT model, a state-of-the-art LLM translation model that supports Adaptive Translation, and your own customized versions of the TLLM or NMT models.

Use this table to decide on the best model for your use case.

Model | Description | Model ID  
---|---|---  
[Translation LLM (TLLM)](https://docs.cloud.google.com/translate/docs/translation-llm) |  **Highest quality translation model** \- a Large language model (LLM) powered by Gemini and fine-tuned for translation to provide the highest quality translations at fast latencies (2x faster latency than Gemini 2.0 Flash).  | `general/translation-llm`  
[Neural Machine Translation (NMT) model](https://docs.cloud.google.com/translate/docs/advanced/nmt-model) |  **Fastest translation model** \- ideal for real time and latency critical use cases. This is an updated version of Google's original Neural Machine Translation, available through the Cloud Translation - Basic API using [v2 client libraries](/translate/docs/reference/libraries/v2/overview-v2). You can get going quickly using this model out of the box, without any customization. | `general/nmt`  
[Customized Translation LLM](https://docs.cloud.google.com/translate/docs/translation-llm#customization) |  Provides **high quality translation customization via fine-tuning** of the Translation LLM with domain-specific language-pair training data. It outperforms the NMT customization by offering faster model training and serving times, as well as more fluent translations. **This is a new feature of Cloud Translation - Advanced.** | `translation-llm-custom/{model-id}`  
[Adaptive Machine Translation model](https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation) |  This option involves **real-time, lightweight customization** of the Translation LLM using [Adaptive Translation](https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation) based on a limited dataset of translation examples. | `general/translation-llm-adaptive`  
[Customized NMT model](https://docs.cloud.google.com/translate/docs/advanced/nmt-customization) | You can train a new customized version of the NMT model using training data specific to your domain and use case. | The model ID is generated after model training completes.  
  
Note that each model supports its own set of languages. Refer to the [Supported languages guide](https://docs.cloud.google.com/translate/docs/languages) to ensure that your source and target languages are supported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
