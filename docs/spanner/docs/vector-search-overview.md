---
url: https://docs.cloud.google.com/spanner/docs/vector-search-overview/
title: Spanner vector search overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:15.054318+00:00
---

# Spanner vector search overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/vector-search-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Spanner vector search overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes vector search and how it works in Spanner.

Vector search is a high-performance, built-in capability that enables semantic search and similarity matching on high-dimensional vector data. By storing and indexing vector embeddings directly within your transactional database, Spanner eliminates the need for separate vector databases and complex ETL pipelines.

## Key concepts

This section introduces the following key concepts of vector search:

  * Vector embeddings
  * Search methods (KNN and ANN)
  * Distance functions



### Vector embeddings

Vector embeddings are high-dimensional, numerical representations of unstructured data. They are generated from the unstructured data using machine learning models. For example, you can use the Gemini Enterprise Agent Platform text embedding API to [generate, store, and update text embeddings](https://docs.cloud.google.com/spanner/docs/ml-tutorial-embeddings) for data stored in Spanner.

### Search methods

Spanner supports two methods for finding similar vectors:

  * **[K-nearest neighbors (KNN)](https://docs.cloud.google.com/spanner/docs/find-k-nearest-neighbors)** : Performs an exact search by calculating the distance between the query and every vector in the dataset. It provides more accurate recall, but is computationally expensive for massive datasets.

  * **[Approximate nearest neighbor (ANN)](https://docs.cloud.google.com/spanner/docs/find-approximate-nearest-neighbors)** : Uses a [vector index](https://docs.cloud.google.com/spanner/docs/vector-indexes) (based on Google's ScaNN algorithm) to find matches quickly across a large number of vectors. It trades a small amount of accuracy (recall) for gains in speed and scalability.




## Key capabilities

  * **Scalability** : Supports billions of vectors for unpartitioned ANN search, or trillions of vectors for partitioned KNN workloads.

  * **Unified AI database and engine** : Use the [GoogleSQL `ML.PREDICT`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/ml-functions#mlpredict) or [PostgreSQL `spanner.ML_PREDICT_ROW`](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions#ml) function to generate embeddings from Agent Platform models directly within your query flow.

  * **Inline filtering** : Efficiently combine vector search with structured metadata filters (for example, "Find similar images where category = 'shoes' and price < 100") without losing performance.

  * **LangChain integration** : Built-in support for [LangChain](https://docs.cloud.google.com/spanner/docs/langchain) lets you build [retrieval-augmented generation (RAG)](https://cloud.google.com/use-cases/retrieval-augmented-generation) applications using Spanner as the vector store.




### Hybrid search capabilities

Vector search is most powerful when combined with Spanner's other data features:

Combination | Benefit  
---|---  
Vector search with SQL filtering | Efficiently combine vector search with filters (for example, "Find similar images where category = 'shoes' and price < 100").  
[Vector search + full-text search](https://docs.cloud.google.com/spanner/docs/hybrid-full-text-vector-search) | Combine semantic similarity with keyword precision using reciprocal rank fusion (RRF) for superior search relevance.  
[Vector + graph](https://docs.cloud.google.com/spanner/docs/graph/perform-vector-similarity-search) | Use vector search to find relevant entry points (nodes) in a property graph and then traverse complex relationships.  
  
## What's next

  * Learn more about [Spanner AI](https://docs.cloud.google.com/spanner/docs/spanner-ai-overview).
  * Learn more about how to [get Agent Platform text embeddings](https://docs.cloud.google.com/spanner/docs/ml-tutorial-embeddings).
  * Learn more about how to [perform K-nearest neighbors (KNN) search](https://docs.cloud.google.com/spanner/docs/find-k-nearest-neighbors).
  * Learn more about how to [perform approximate nearest neighbors (ANN) search](https://docs.cloud.google.com/spanner/docs/find-approximate-nearest-neighbors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
