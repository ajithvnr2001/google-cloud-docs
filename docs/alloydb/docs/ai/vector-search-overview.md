---
url: https://docs.cloud.google.com/alloydb/docs/ai/vector-search-overview/
title: AlloyDB AI Vector Search overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:35.836258+00:00
---

# AlloyDB AI Vector Search overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/vector-search-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)



Send feedback 

#  AlloyDB AI Vector Search overview Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB AI integrates vector processing and similarity search directly into AlloyDB for PostgreSQL, letting you query both structured relational data and unstructured data by semantic meaning. By combining standard SQL capabilities with Approximate Nearest Neighbor (ANN) indexing, AlloyDB AI supports semantic search and retrieval-augmented generation (RAG) workflows without requiring you to deploy and manage a separate vector database.

## Core architecture and performance

AlloyDB uses the pgvector extension of PostgreSQL for vector functionality. It supports the popular HNSW index, as well as the Scalable Nearest Neighbors (ScaNN) index, a state-of-the-art vector search algorithm derived from years of Google Search research. This deep integration into the PostgreSQL environment allows for high-speed, pgvector-compatible operations and advanced semantic querying.

### ScaNN index performance

The ScaNN index offers substantial speed advantages over the standard PostgreSQL HNSW (Hierarchical Navigable Small Worlds) index, providing rapid vector operations necessary for demanding AI workloads:

Operation | Performance Gain (vs. standard PostgreSQL HNSW Index) | Features  
---|---|---  
Index Creation | Up to 10x faster | Parallel index build  
Vector Search Queries | Up to 4x faster | Index auto-maintenance  
Filtered Vector Search Queries | Up to 10x faster | Enterprise-grade observability  
  
### Adaptive filtering and query optimization

The ScaNN index is deeply integrated with the PostgreSQL query planner to ensure optimal performance for hybrid queries involving both vector similarity and standard structured metadata filters:

  * **Adaptive filtering:** ensures optimal performance when filters, joins, and vector indexes are utilized concurrently. It functions by observing query execution statistics at runtime, learning the selectivity of filters, and adaptively adjusting the execution plan to determine the most efficient ordering of filter application and vector search.
  * **Inline filtering:** specific to the ScaNN algorithm, inline filtering is an optimization strategy that executes vector search and metadata filter evaluation in tandem. It leverages secondary PostgreSQL indexes (such as B-trees, GIN, or GiST) to create a shortlist (bitmap) of rows that satisfy the filter criteria. The subsequent vector scan only computes distances for vectors contained within that pre-filtered set, drastically reducing computational overhead, especially when filters are moderately selective.



## Seamless integration with Gemini Enterprise Agent Platform

AlloyDB AI is engineered for built-in integration with the Agent Platform ecosystem, enabling the transformation and enrichment of data directly within the database using SQL.

### Automated embedding generation

The platform supports automated embedding generation using the `google_ml_integration` extension. This capability lets operational data (text, images, and video) be converted into vector embeddings using Agent Platform models, such as `text-embedding-005`:

  * **Model registration:** Agent Platform models (embedding and generative) are registered within the database using the `google_ml.create_model` procedure.
  * **Virtual columns:** embeddings can be automatically generated and persisted in a generated column using the `embedding()` function, ensuring the vector data remains synchronized with the source column data:


    
    
    ALTER TABLE my_table
    ADD COLUMN embedding vector(768)
    GENERATED ALWAYS AS (embedding('text-embedding-005', source_column)) STORED;
    

### Querying and generative AI enrichment

With vector embeddings stored, developers can perform sophisticated semantic searches using the vector similarity operator (`<=>`) in standard SQL. Furthermore, the results of these searches can be passed directly to generative AI models, such as `gemini-3.5-flash-lite`, using functions like `ai.generate` or `google_ml.predict_row` for RAG-based query enrichment and user-friendly output generation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
