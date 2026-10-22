---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/genai-models/
title: Available Generative AI models \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:22.301516+00:00
---

# Available Generative AI models  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/genai-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Available Generative AI models Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** This content applies to version 1.14.4 and later.

Vertex AI on Google Distributed Cloud (GDC) air-gapped features a growing list of foundation Generative AI models you can test, deploy, and implement for your air-gapped applications. Foundation models are fine-tuned for specific use cases and offered at different prices. This page summarizes the model families available in the Generative AI APIs on GDC and guides you on which models to choose by use case.

## Embeddings models

Embeddings convert textual data written in a natural language into numerical vectors. These vector representations are designed to capture the semantic meaning and context of the words they represent. Text embedding models can generate optimized embeddings for various task types, such as document retrieval, questions and answers, classification, and fact verification. For English text, use `text-embedding-004`. For multilingual text, use `text-multilingual-embedding-002`.

The following table summarizes the models available in the Embeddings API. For more information on embeddings, see [Text embeddings](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/text-embeddings-overview).

**Model** | **Description** | **Specifications**  
---|---|---  
**Text Embedding**  
  
(`text-embedding-004`) | Returns embeddings for English text inputs. | **Max token input:** 2,048.  
  
**Embedding dimensions:** less than 768.  
**Text Embedding Multilingual**  
  
(`text-multilingual-embedding-002`) | Returns embeddings for text inputs of [over 100 languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/supported-text-languages). | **Max token input:** 2,048.  
  
**Embedding dimensions:** less than 768.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
