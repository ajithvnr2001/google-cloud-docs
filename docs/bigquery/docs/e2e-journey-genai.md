---
url: https://docs.cloud.google.com/bigquery/docs/e2e-journey-genai/
title: End-to-end user journeys for generative AI models \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:25.181797+00:00
---

# End-to-end user journeys for generative AI models  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/e2e-journey-genai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# End-to-end user journeys for generative AI models

This document describes the user journeys for BigQuery ML remote models, including the statements and functions that you can use to work with remote models. BigQuery ML offers the following types of remote models:

  * [Fine-tuned Google Gemini models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-tuned)
  * [Google, partner, and open models as a service](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model)
  * [Google text embedding models as a service](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-embedding-maas)
  * [Self-deployed open models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-open)
  * [Cloud AI services](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-service)
  * [Custom models deployed to Gemini Enterprise Agent Platform](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-https)



## Remote model user journeys

The following table describes the statements and functions you can use to create, evaluate, and generate data from remote models:

Model category | Model type | Model creation | [Evaluation](https://docs.cloud.google.com/bigquery/docs/evaluate-overview) | [Inference](https://docs.cloud.google.com/bigquery/docs/inference-overview) | Tutorials  
---|---|---|---|---|---  
Generative AI remote models | Remote model over a Gemini text generation model1 |  [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model) | [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate) | 

  * [`AI.GENERATE_TEXT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-text)
  * [`AI.GENERATE_TABLE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-table)
  * [`AI.GENERATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate)2
  * [`AI.GENERATE_BOOL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-bool)2
  * [`AI.GENERATE_DOUBLE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-double)2
  * [`AI.GENERATE_INT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-int)2

| 

  * [Generate text using your data](https://docs.cloud.google.com/bigquery/docs/generate-text-tutorial)
  * [Generate structured data using your data](https://docs.cloud.google.com/bigquery/docs/generate-table)
  * [Generate text with Gemini and public data](https://docs.cloud.google.com/bigquery/docs/generate-text-tutorial-gemini)
  * [Handle quota errors by calling `ML.GENERATE_TEXT` iteratively](https://docs.cloud.google.com/bigquery/docs/iterate-generate-text-calls)
  * [Analyze images with a Gemini model](https://docs.cloud.google.com/bigquery/docs/image-analysis)
  * [Try model tuning using public data](https://docs.cloud.google.com/bigquery/docs/tune-evaluate)

  
Remote model over a partner text generation model |  [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model) | [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate) |  [`AI.GENERATE_TEXT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-text) |  N/A   
Remote model over an open text generation model3 |  [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-open) | [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate) |  [`AI.GENERATE_TEXT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-text) |  [Generate text with Gemma and public data](https://docs.cloud.google.com/bigquery/docs/generate-text-tutorial-gemma)  
Remote model over a Google embedding generation model |  [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-embedding-maas) | N/A |  [`AI.GENERATE_EMBEDDING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-embedding) | 

  * [Generate text embeddings using your data](https://docs.cloud.google.com/bigquery/docs/generate-text-embedding)
  * [Generate image embeddings using your data](https://docs.cloud.google.com/bigquery/docs/generate-visual-content-embedding)
  * [Generate video embeddings using your data](https://docs.cloud.google.com/bigquery/docs/generate-video-embedding)
  * [Handle quota errors by calling `ML.GENERATE_EMBEDDING` iteratively](https://docs.cloud.google.com/bigquery/docs/iterate-generate-embedding-calls)
  * [Generate and search multimodal embeddings using public data](https://docs.cloud.google.com/bigquery/docs/generate-multimodal-embeddings)

  
Remote model over an open embedding generation model3 |  [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-open) | N/A |  [`AI.GENERATE_EMBEDDING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-embedding) |  [Generate text embeddings by using an open model and the `AI.GENERATE_EMBEDDING` function](https://docs.cloud.google.com/bigquery/docs/generate-text-embedding-tutorial-open-models)  
Cloud AI remote models | Remote model over the Cloud Vision API |  [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-service) | N/A |  [`ML.ANNOTATE_IMAGE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-annotate-image) | [Annotate images](https://docs.cloud.google.com/bigquery/docs/annotate-image)  
Remote model over the Cloud Translation API |  [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-service) | N/A |  [`ML.TRANSLATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-translate) | [Translate text](https://docs.cloud.google.com/bigquery/docs/translate-text)  
Remote model over the Cloud Natural Language API |  [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-service) | N/A |  [`ML.UNDERSTAND_TEXT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-understand-text) | [Understand text](https://docs.cloud.google.com/bigquery/docs/understand-text)  
Remote model over the Document AI API |  [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-service) | N/A |  [`ML.PROCESS_DOCUMENT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-process-document) | 

  * [Process documents](https://docs.cloud.google.com/bigquery/docs/process-document)
  * [Parse PDFs in a RAG pipeline](https://docs.cloud.google.com/bigquery/docs/rag-pipeline-pdf)

  
Remote model over the Speech-to-Text API |  [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-service) | N/A |  [`ML.TRANSCRIBE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transcribe) | [Transcribe audio files](https://docs.cloud.google.com/bigquery/docs/transcribe)  
Remote model over a custom model deployed to Gemini Enterprise Agent Platform | Remote model over a custom model deployed to Gemini Enterprise Agent Platform | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-https) | [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate) | [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict) | [Make predictions with a custom model](https://docs.cloud.google.com/bigquery/docs/bigquery-ml-remote-model-tutorial)  
  
1 Some Gemini models support [supervised tuning](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-tuned#supervised_tuning).

2 This function calls a hosted Gemini model, and doesn't require you to create a model separately using the `CREATE MODEL` statement.

3 You can automatically deploy an open model when you create the BigQuery ML remote model by specifying the model's Hugging Face or Agent Platform Model Garden ID. BigQuery manages the Agent Platform resources of open models deployed in this way, and lets you interact with those Agent Platform resources by using the BigQuery ML `ALTER MODEL` and `DROP MODEL` statements. It also lets you configure automatic undeployment of the model. For more information, see [Automatically deployed models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-open#automatically_deployed_models).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
