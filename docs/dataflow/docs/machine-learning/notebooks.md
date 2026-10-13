---
url: https://docs.cloud.google.com/dataflow/docs/machine-learning/notebooks/
title: Dataflow ML notebooks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:45.207298+00:00
---

# Dataflow ML notebooks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/machine-learning/notebooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Dataflow ML notebooks Stay organized with collections  Save and categorize content based on your preferences. 

Explore Dataflow ML notebooks to integrate machine learning into your Apache Beam pipelines. These notebooks provide practical examples and guidance for common machine learning workflows.

Use these resources to:

  * **Preprocess data for ML models** : This includes tasks like scaling data, computing vocabularies, and using `MLTransform` for data preparation.
  * **Run inference with various models and frameworks** : Use the `RunInference` transform with PyTorch, TensorFlow, scikit-learn, Hugging Face models, Gemma models, and Gemini Enterprise Agent Platform, including on GPUs with vLLM.
  * **Generate and manage embeddings** : Create text embeddings using Agent Platform or Hugging Face, and ingest them into databases like AlloyDB and BigQuery for vector search.
  * **Implement advanced ML pipeline patterns** : This includes automatic model refresh in running pipelines, using multiple models, building ensemble models, and data enrichment using BigQuery, Bigtable, and Vertex AI Feature Store.
  * **Apply ML to specific use cases** : Examples include anomaly detection as well as sentiment analysis and summarization with Gemma.



## All tutorials

**Filter by:** Core Dataflow & MLTransform ConceptsData enrichment & EmbeddingModel training & Data processingRun inferenceSpecialized use cases Core Dataflow & MLTransform Concepts |  **Preprocessing with the Apache Beam DataFrames API** Demonstrates the use of the Apache Beam DataFrames API to perform common data exploration and preprocessing steps. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/dataframe_api_preprocessing)  
---|---|---  
Core Dataflow & MLTransform Concepts |  **Preprocess data with MLTransform** A basic introduction to using MLTransform for preprocessing data for machine learning workflows. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/mltransform_basic)  
Data enrichment & Embedding |  **Vector Embedding Ingestion with Apache Beam and AlloyDB** Demonstrates how to generate embeddings from data and ingest them into AlloyDB using Apache Beam and Dataflow for scalable data processing. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/alloydb_product_catalog_embeddings)  
Data enrichment & Embedding |  **Use Apache Beam and BigQuery to enrich data** Shows how to enrich data by using the Apache Beam enrichment transform with BigQuery. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/bigquery_enrichment_transform)  
Data enrichment & Embedding |  **Embedding Ingestion and Vector Search with Apache Beam and BigQuery** Demonstrates how to use the Apache Beam RAG package to generate embeddings, ingest them into BigQuery, and perform vector similarity search. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/bigquery_vector_ingestion_and_search)  
Data enrichment & Embedding |  **Use Apache Beam and Bigtable to enrich data** Shows how to enrich data by using the Apache Beam enrichment transform with Bigtable. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/bigtable_enrichment_transform)  
Data enrichment & Embedding |  **Generate text embeddings by using Hugging Face Hub models** Uses MLTransform to generate embeddings from text data using Hugging Face's SentenceTransformers framework. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/huggingface_text_embeddings)  
Data enrichment & Embedding |  **Use Apache Beam and Vertex AI Feature Store to enrich data** Shows how to enrich data by using the Apache Beam enrichment transform with Vertex AI Feature Store. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/vertex_ai_feature_store_enrichment)  
Data enrichment & Embedding |  **Generate text embeddings by using the Vertex AI API** Uses the Vertex AI text-embeddings API to generate text embeddings that use Google’s large generative artificial intelligence (AI) models. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/vertex_ai_text_embeddings)  
Model training & Data processing |  **Update ML models in running pipelines** Demonstrates how to perform automatic model updates without stopping your Apache Beam pipeline by using side inputs. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/automatic_model_refresh)  
Model training & Data processing |  **Compute and apply vocabulary on a dataset** Shows how to use MLTransform to generate a vocabulary on input text and assign an index value to each token. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/compute_and_apply_vocab)  
Model training & Data processing |  **Run ML inference with multiple differently-trained models** Demonstrates how to use a KeyedModelHandler to run inference in an Apache Beam pipeline with multiple different models on a per-key basis. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/per_key_models)  
Model training & Data processing |  **Use MLTransform to scale data** Shows how to use MLTransform to scale data, an important preprocessing step for training machine learning (ML) models. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/scale_data)  
Model training & Data processing |  **TensorFlow Model Analysis in Beam** Shows how you can use TFMA to investigate and visualize the performance of a model as part of your Apache Beam pipeline by creating and comparing two models. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/tfma_beam)  
Run inference |  **Remote inference in Apache Beam** Demonstrates how to implement a custom inference call in Apache Beam by using the Google Cloud Vision API. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/custom_remote_inference)  
Run inference |  **Bring your own ML model to Beam RunInference** Illustrates how to use the spaCy package to load a machine learning (ML) model and perform inference in an Apache Beam pipeline using the RunInference PTransform. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_custom_inference)  
Run inference |  **Run inference with a Gemma open model** Demonstrates how to load the preconfigured Gemma 2B model and then use it in an Apache Beam inference pipeline. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_gemma)  
Run inference |  **Use RunInference for Generative AI** Shows how to use the Apache Beam RunInference transform for generative AI tasks with a large language model (LLM) from the Hugging Face Model Hub. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_generative_ai)  
Run inference |  **Apache Beam RunInference with Hugging Face** Shows how to use models from Hugging Face and Hugging Face pipeline in Apache Beam pipelines that uses the RunInference transform. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_huggingface)  
Run inference |  **Ensemble model using an image captioning and ranking example** Shows how to implement a cascade model in Apache Beam using the RunInference API for image captioning. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_multi_model)  
Run inference |  **Apache Beam RunInference for PyTorch** Demonstrates the use of the RunInference transform for PyTorch. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_pytorch)  
Run inference |  **Use RunInference in Apache Beam** Demonstrates how to use the RunInference API with three popular ML frameworks: PyTorch, TensorFlow, and scikit-learn. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_pytorch_tensorflow_sklearn)  
Run inference |  **Apache Beam RunInference for scikit-learn** Demonstrates the use of the RunInference transform for scikit-learn. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_sklearn)  
Run inference |  **Apache Beam RunInference with TensorFlow** Shows how to use the Apache Beam RunInference transform for TensorFlow. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_tensorflow)  
Run inference |  **Use RunInference with TFX Basic Shared Libraries** Demonstrates how to use the Apache Beam RunInference transform with TensorFlow and TFX Basic Shared Libraries (tfx-bsl). |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_tensorflow_with_tfx)  
Run inference |  **Apache Beam RunInference with TensorFlow and TensorFlow Hub** Shows how to use the Apache Beam RunInference transform for TensorFlow with a trained model from TensorFlow Hub. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_with_tensorflow_hub)  
Run inference |  **Apache Beam RunInference with Vertex AI** Shows how to use the Apache Beam RunInference transform for image classification with Vertex AI. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_vertex_ai)  
Run inference |  **Run ML inference by using vLLM on GPUs** Demonstrates how to run machine learning inference by using vLLM and GPUs. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_vllm)  
Run inference |  **Use TPUs in Dataflow** Demonstrates how to configure and execute two distinct Dataflow pipelines that leverage Tensor Processing Units (TPUs). The first pipeline performs a simple computation to confirm TPU access, while the second, more complex pipeline runs inference with the Gemma-3-27b-it model. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/dataflow_tpu_examples)  
Specialized use cases |  **Anomaly Detection on Batch and Streaming Data using Apache Beam (Z-Score Method)** Shows how to perform anomaly detection on both batch and streaming data using the AnomalyDetection PTransform with the Z-Score algorithm. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/anomaly_detection_zscore)  
Specialized use cases |  **Use Gemma to gauge sentiment and summarize conversations** Demonstrates how to use Gemma to gauge the sentiment of a conversation, summarize the conversation's content, and draft a reply. |  [View Notebook](https://docs.cloud.google.com/dataflow/docs/notebooks/gemma_2_sentiment_and_summarization)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
