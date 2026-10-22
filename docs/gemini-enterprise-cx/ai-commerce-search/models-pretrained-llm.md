---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models-pretrained-llm/
title: Utilizing pretrained LLM \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:47.426590+00:00
---

# Utilizing pretrained LLM  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models-pretrained-llm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Utilizing pretrained LLM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use a textual large-language model (LLM) in the custom recommendation models. We train these models for you. You can enable the pretrained features in the [custom recommendation models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models).

Recommendations uses the product [`description`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.description) field to feed to LLMs and put them into your recommendations models.

**Note:** Creating and configuring models is only available for recommendations.

## New LLM textual features

While it's possible to get text embeddings by [manually configuring a Vertex AI generative model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings#get_text_embeddings_for_a_snippet_of_text), you might want to integrate the new LLM capabilities into your recommendations models to improve performance.

The text embeddings are more descriptive, longer, and are not repetitive, as well as have multilingual interpretation capabilities. This feature is based on an allowlist. Contact support for enabling this feature.

There's no charge for using the text embeddings and they are included in AI Commerce Search [pricing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/pricing).

The LLM-pretrained embeddings improve semantic understanding of long form text searches such as descriptions.

See the following resources for more information on how to use embeddings and generative AI alone in your own custom ML training:

  * [Vertex AI generative AI documentation](https://docs.cloud.google.com/gemini-enterprise-cx/generative-ai-app-builder/docs/about-checklists)
  * [Machine Learning Crash Course: Embeddings](https://developers.google.com/machine-learning/crash-course/embeddings)



## Model compatibility

The LLM feature is compatible with all ml model types and objectives, including:

  * OYML
  * FBT
  * and more.



For more information on the different types of recommendation models AI Commerce Search supports, see [About recommendations models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
