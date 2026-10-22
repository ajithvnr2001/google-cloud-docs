---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/mistral/mistral-ocr/
title: Mistral OCR (25.05) \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:46:12.455509+00:00
---

# Mistral OCR (25.05)  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/mistral/mistral-ocr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Mistral OCR (25.05) Stay organized with collections  Save and categorize content based on your preferences. 

Mistral OCR (25.05) is an Optical Character Recognition API for document understanding. Mistral OCR (25.05) excels in understanding complex document elements, including interleaved imagery, mathematical expressions, tables, and advanced layouts such as LaTeX formatting. The model enables deeper understanding of rich documents such as scientific papers with charts, graphs, equations and figures.

Mistral OCR (25.05) is an ideal model to use in combination with a RAG system that takes multimodal documents (such as slides or complex PDFs) as input.

You can couple Mistral OCR (25.05) with other Mistral models to reformat the results. This combination ensures that the extracted content is not only accurate but also presented in a structured and coherent manner, making it suitable for various downstream applications and analyses.

[View model card in Model Garden](https://console.cloud.google.com/agent-platform/publishers/mistralai/model-garden/mistral-ocr-2505)

Model ID | `mistral-ocr-2505`  
---|---  
Launch stage | GA  
Supported inputs & outputs | 

  * Inputs: Documents
  * Outputs: Text

  
Usage types | 

  * Supported
    * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)
  * Not supported
    * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)

  
Versions | 

  * `Mistral OCR (25.05)`
    * **Launch stage:** GA
    * **Release date:** May 14, 2025

  
Supported regions  
Model availability | 

  * United States
    * `us-central1`
  * Europe
    * `europe-west4`

  
ML processing | 

  * United States
    * `Multi-region`
  * Europe
    * `Multi-region`

  
Quota limits |  us-central1: 

  * QPM: 30
  * Pages per request: 30 (1 page = 1 million input tokens and 1 million output tokens)
  * Context length: 30 pages
  * Max request size: 30MB for streaming, 10MB for unary

europe-west4: 

  * QPM: 30
  * Pages per request: 30 (1 page = 1 million input tokens and 1 million output tokens)
  * Context length: 30 pages
  * Max request size: 30MB for streaming, 10MB for unary

  
Pricing | See [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
