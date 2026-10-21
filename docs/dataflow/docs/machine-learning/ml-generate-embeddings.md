---
url: https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-generate-embeddings/
title: Generate embeddings with MLTransform \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:48.800879+00:00
---

# Generate embeddings with MLTransform  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-generate-embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Generate embeddings with MLTransform Stay organized with collections  Save and categorize content based on your preferences. 

This page explains why and how to use the [`MLTransform`](https://github.com/apache/beam/blob/3d501ee9dc208af2efef009daa98c49819b73ddc/sdks/python/apache_beam/ml/transforms/base.py#L112) feature to prepare your data for training machine learning (ML) models. Specifically, this page shows you how to process data by generating embeddings using `MLTransform`.

By combining multiple data processing transforms in one class, `MLTransform` streamlines the process of applying Apache Beam ML data processing operations to your workflow.

![Diagram of the Dataflow ML workflow with the data processing step highlighted.](https://docs.cloud.google.com/static/dataflow/images/dataflow-ml-preprocess.png)

**Figure 1.** The complete Dataflow ML workflow. Use `MLTransform` in the preprocessing step of the workflow. 

## Embeddings overview

Embeddings are essential for modern semantic search and Retrieval Augmented Generation (RAG) applications. Embeddings let systems understand and interact with information on a deeper, more conceptual level. In semantic search, embeddings transform queries and documents into vector representations. These representations capture their underlying meaning and relationships. Consequently, this lets you find relevant results even when keywords don't directly match. This is a significant leap beyond standard keyword-based search. You can also use embeddings for product recommendations. This includes multimodal searches that use images and text, log analytics, and for tasks such as deduplication.

Within RAG, embeddings play a crucial role in retrieving the most relevant context from a knowledge base to ground the responses of large language models (LLMs). By embedding both the user's query and the chunks of information in the knowledge base, RAG systems can efficiently identify and retrieve the most semantically similar pieces. This semantic matching ensures that the LLM has access to the necessary information to generate accurate and informative answers.

## Ingest and process data for embeddings

![Diagram of embedding knowledge ingestion with the data processing steps of
chunking and embedding generation
highlighted.](https://docs.cloud.google.com/static/dataflow/images/knowledge-ingestion-diagram_embeddings.png)

**Figure 2.** A knowledge ingestion diagram. This shows the input multimodal documents data and two processing steps: chunking and embedding generation. Chunking is a preprocessing step used for complex data before embedding generation. After the data is processed, the embeddings are stored in a vector database. 

For core embedding use cases, the key consideration is how to ingest and process knowledge. This ingestion can be either in a batch or streaming manner. The source of this knowledge can vary widely. For example, this information can come from files stored in Cloud Storage, or can come from streaming sources like Pub/Sub or Google Cloud Managed Service for Apache Kafka.

For streaming sources, the data itself might be the raw content (for example, plain text) or URIs pointing to documents. Regardless of the source, the first stage typically involves preprocessing the information. For raw text, this might be minimal, such as basic data cleaning. However, for larger documents or more complex content, a crucial step is _chunking_. Chunking involves breaking down the source material into smaller, manageable units. The optimal chunking strategy isn't standardized and depends on the specific data and application. Platforms like Dataflow offer built-in capabilities to handle diverse chunking needs, simplifying this essential preprocessing stage.

## Benefits

The `MLTransform` class provides the following benefits:

  * Generate embeddings that you can use to push data into vector databases or to run inference.
  * Transform your data without writing complex code or managing underlying libraries.
  * Efficiently chain multiple types of processing operations with one interface.



## Support and limitations

The `MLTransform` class has the following limitations:

  * Available for pipelines that use the Apache Beam Python SDK versions 2.53.0 and later.
  * Pipelines must use [default windows](https://beam.apache.org/documentation/programming-guide/#single-global-window).



**Text embedding transforms:**

  * Support Python 3.8, 3.9, 3.10, 3.11, and 3.12.
  * Support both batch and streaming pipelines.
  * Support the [Gemini Enterprise Agent Platform text-embeddings API](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/embeddings/get-text-embeddings) and the [Hugging Face Sentence Transformers module](https://huggingface.co/sentence-transformers).



## Use cases

The example notebooks demonstrate how to use `MLTransform` for specific use cases.

[I want to generate text embeddings for my LLM by using Agent Platform Pipelines](https://docs.cloud.google.com/dataflow/docs/notebooks/vertex_ai_text_embeddings)
    Use the Apache Beam `MLTransform` class with the [Agent Platform Pipelines text-embeddings API](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/embeddings/get-text-embeddings) to generate text embeddings. Text embeddings are a way to represent text as numerical vectors, which is necessary for many natural language processing (NLP) tasks.
[I want to generate text embeddings for my LLM by using Hugging Face](https://docs.cloud.google.com/dataflow/docs/notebooks/huggingface_text_embeddings)
    Use the Apache Beam `MLTransform` class with [Hugging Face Hub](https://huggingface.co/docs/hub/models-the-hub) models to generate text embeddings. The Hugging Face [`SentenceTransformers`](https://huggingface.co/sentence-transformers) framework uses Python to generate sentence, text, and image embeddings.
[I want to generate text embeddings and ingest them into AlloyDB for PostgreSQL](https://docs.cloud.google.com/dataflow/docs/notebooks/alloydb_product_catalog_embeddings)
    Use Apache Beam, specifically its `MLTransform` class with [Hugging Face Hub](https://huggingface.co/docs/hub/models-the-hub) models to generate text embeddings. Then, use the `VectorDatabaseWriteTransform` to load these embeddings and associated metadata into AlloyDB for PostgreSQL. This notebook demonstrates building scalable batch and streaming Beam data pipelines for populating an AlloyDB for PostgreSQL vector database. This includes handling data from various sources like Pub/Sub or existing database tables, making custom schemas, and updating data.
[I want to generate text embeddings and ingest them into BigQuery](https://docs.cloud.google.com/dataflow/docs/notebooks/bigquery_vector_ingestion_and_search)
    Use the Apache Beam `MLTransform` class with [Hugging Face Hub](https://huggingface.co/docs/hub/models-the-hub) models to generate text embeddings from application data, such as a product catalog. The Apache Beam `HuggingfaceTextEmbeddings` transform is used for this. This transform uses the Hugging Face [SentenceTransformers](https://huggingface.co/sentence-transformers) framework, which provides models for generating sentence and text embeddings. These generated embeddings and their metadata are then ingested into BigQuery using the Apache Beam `VectorDatabaseWriteTransform`. The notebook further demonstrates vector similarity searches in BigQuery using the Enrichment transform.

For a full list of available transforms, see [Transforms](https://beam.apache.org/documentation/ml/preprocess-data#transforms) in the Apache Beam documentation.

## Use MLTransform for embedding generation

To use the `MLTransform` class to chunk information and generate embeddings, include the following code in your pipeline:
    
    
      
      def create_chunk(product: Dict[str, Any]) -> Chunk:
        return Chunk(
            content=Content(
                text=f"{product['name']}: {product['description']}"
            ),
            id=product['id'],  # Use product ID as chunk ID
            metadata=product,  # Store all product info in metadata
        )
    
      [...]
      with beam.Pipeline() as p:
        _ = (
                p
                | 'Create Products' >> beam.Create(products)
                | 'Convert to Chunks' >> beam.Map(create_chunk)
                | 'Generate Embeddings' >> MLTransform(
      write_artifact_location=tempfile.mkdtemp())
      .with_transform(huggingface_embedder)
                | 'Write to AlloyDB' >> VectorDatabaseWriteTransform(alloydb_config)
            )
    

The previous example creates a single chunk per element, but you can also use LangChain for to create chunks instead:
    
    
    splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    provider = beam.ml.rag.chunking.langchain.LangChainChunker(
    document_field='content', metadata_fields=[], text_splitter=splitter)
    
    with beam.Pipeline() as p:
    _ = (
    p
    | 'Create Products' >> beam.io.textio.ReadFromText(products)
    | 'Convert to Chunks' >> provider.get_ptransform_for_processing()
    

## What's next

  * Read the blog post ["How to enable real time semantic search and RAG applications with Dataflow ML"](https://cloud.google.com/blog/topics/developers-practitioners/create-and-retrieve-embeddings-with-a-few-lines-of-dataflow-ml-code?content_ref=how+to+enable+real+time+semantic+search+and+rag+applications+with+dataflow+ml).
  * For more details about `MLTransform`, see [Preprocess data](https://beam.apache.org/documentation/ml/preprocess-data) in the Apache Beam documentation.
  * For more examples, see [`MLTransform` for data processing](https://beam.apache.org/documentation/transforms/python/elementwise/mltransform) in the Apache Beam transform catalog.
  * Run an [interactive notebook in Colab](https://colab.sandbox.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/mltransform_basic.ipynb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
