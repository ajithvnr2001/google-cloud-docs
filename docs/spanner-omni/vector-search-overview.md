---
url: https://docs.cloud.google.com/spanner-omni/vector-search-overview/
title: Spanner Omni vector search overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:03.371720+00:00
---

# Spanner Omni vector search overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/vector-search-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Spanner Omni vector search overview Stay organized with collections  Save and categorize content based on your preferences. 

Vector search in Spanner Omni is a high-performance, built-in feature that enables semantic search and similarity matching on high-dimensional vector data. By storing and indexing vector embeddings directly within your transactional database, Spanner Omni eliminates separate vector databases and complex extract, transform, load (ETL) pipelines.

The topics in this document apply to Spanner Omni in the same way they apply to Spanner.

## How vector search works

Vector search lets you find semantically similar items by representing data as numerical vectors (embeddings). Spanner Omni supports two primary search methods:

  * **K-nearest neighbors (KNN)** : Performs an exact search by calculating the distance between the query and every vector in the dataset. It provides the highest recall but can be computationally expensive for large datasets.

  * **Approximate nearest neighbors (ANN)** : Uses a vector index to find matches fast across large datasets. It trades a small amount of accuracy (recall) for gains in speed and scalability.




Vector search is especially powerful when combined with other features:

Combination | Benefit  
---|---  
Vector search with SQL filtering | Efficiently combine vector search with filters (for example, "Find similar images where category = 'shoes' and price < 100").  
Vector search + full-text search | Combine semantic similarity with keyword precision using reciprocal rank fusion (RRF) for improved search relevance.  
Vector + graph | Use vector search to find relevant entry points (nodes) in a property graph and then traverse complex relationships.  
  
For more information, see [Spanner vector search overview](https://docs.cloud.google.com/spanner/docs/vector-search-overview) in the Spanner documentation.

## Perform K-nearest neighbors search

Spanner Omni supports K-nearest neighbors (KNN) search using built-in distance functions. You can provide a vector embedding as an input parameter to find the nearest vectors in N-dimensional space.

The following distance functions are available:

  * `COSINE_DISTANCE()`: Measures the cosine of the angle between two vectors

  * `EUCLIDEAN_DISTANCE()`: Measures the shortest straight-line distance between two vectors

  * `DOT_PRODUCT()`: Calculates the cosine of the angle multiplied by the product of vector magnitudes (ideal for normalized data)




For more information, see [Perform vector similarity search by finding the K-nearest neighbors](https://docs.cloud.google.com/spanner/docs/find-k-nearest-neighbors) in the Spanner documentation.

## Choose the best vector distance function

Selecting the appropriate distance function depends on your data and the model used to generate embeddings.

Function | Description | Relationship to increasing similarity  
---|---|---  
Dot product | Calculates the cosine of angle multiplied by the product of corresponding vector magnitudes. | Increases  
Cosine distance | Measures the cosine of the angle between two vectors (1 - cosine similarity). | Decreases  
Euclidean distance | Measures the straight line distance between two vectors. | Decreases  
  
If your embeddings are normalized (magnitude = 1.0), `DOT_PRODUCT()` is typically an efficient choice. For non-normalized data, experiment with `COSINE_DISTANCE()` or `EUCLIDEAN_DISTANCE()` to determine which produces better results for your use case.

For more information, see [Choose among vector distance functions](https://docs.cloud.google.com/spanner/docs/choose-vector-distance-function) in the Spanner documentation.

## Approximate nearest neighbors (ANN)

ANN search is designed for very large datasets where exact KNN search becomes too slow or expensive. It uses a vector index to provide fast results with a small tradeoff in recall.

Without dedicated compute workers, ANN search in Spanner Omni supports datasets of up to 1 million vectors for vectors up to 128 dimensions in length. If your vectors have more dimensions, then the supported number of vectors decreases proportionally. Spanner Omni supports larger tables when you deploy workers to build your vector indexes. For more information, see Create and manage vector indexes.

### Perform ANN search with vector indexes

To perform an ANN search, use approximate distance functions such as `APPROX_COSINE_DISTANCE()`, `APPROX_EUCLIDEAN_DISTANCE()`, or `APPROX_DOT_PRODUCT()`. These functions require:

  * An existing vector index on the embedding column.

  * An `ORDER BY` clause using the approximate distance function.

  * A `LIMIT` clause to specify the number of results.




For more information, see [Find approximate nearest neighbors (ANN) and query vector embeddings](https://docs.cloud.google.com/spanner/docs/find-approximate-nearest-neighbors) in the Spanner documentation.

### Create and manage vector indexes

When creating a vector index, specify the `vector_length` of your embedding column and use the `STORING` clause to include additional columns for faster filtering.

The following is an example of how to create a vector index:
    
    
    CREATE VECTOR INDEX INDEX_NAME
      ON TABLE_NAME(EMBEDDING_COLUMN)
      OPTIONS (distance_type = 'DISTANCE_TYPE', tree_depth = 2, num_leaves = 1000);
    

For more information, see [Create and manage vector indexes](https://docs.cloud.google.com/spanner/docs/vector-indexes) in the Spanner documentation.

Building vector indexes on large tables that exceed the limits in Approximate nearest neighbors (ANN) requires dedicated compute workers to offload processing from your Spanner Omni servers. For more information, see [Deploy and manage workers](https://docs.cloud.google.com/spanner-omni/manage-workers).

**Note:** If you create a vector index on a large table without an active worker, the index creation operation pauses without progress until a worker is available. Spanner Omni lets you create an index without an active worker so that you can deploy workers only when required and decommission them immediately after index creation completes. 

### Use sampling when creating a vector index

For large datasets—such as tables with tens of millions of rows or more—you can reduce vector index creation time by specifying a sampling percentage. Use the `clustering_sampling_percentage` option in the `CREATE VECTOR INDEX` statement to sample a subset of the dataset when you build the initial index tree.

As a general guideline, aim for at least 50 sampled rows per leaf. For example, for a 10-million-row dataset with 10,000 leaves, a 5% sampling rate (`clustering_sampling_percentage = 5`) samples 500,000 rows, or 50 rows per leaf, as the following example shows:
    
    
    CREATE VECTOR INDEX VectorIndex
      ON BaseTable(Embedding)
      WHERE Embedding IS NOT NULL
      OPTIONS (
        tree_depth = 3,
        num_leaves = 10000,
        num_branches = 100,
        leaf_scatter_factor = 32,
        distance_type = 'COSINE',
        min_branch_splits = 10,
        min_leaf_splits = 10,
        clustering_sampling_percentage = 5
      );
    

Compared to building an index on the full dataset without sampling, sampling increases query latency and CPU usage per query for the same target recall. Increasing the sampling percentage increases index creation time, but reduces query latency and CPU cost per query. Choose a sampling percentage that balances index creation time and query performance based on the compute resources that are available for index creation.

### Vector indexing best practices

To maintain high search performance and recall:

  * **Tune index options** : Adjust `num_leaves` and `num_leaves_to_search` based on your data size and performance requirements.

  * **Rebuild periodically** : Rebuild your index if the distribution of your vectors changes significantly over time.

  * **Use filtering effectively** : Store frequently filtered columns in the index to improve search efficiency.




For more information, see [Vector indexing best practices](https://docs.cloud.google.com/spanner/docs/vector-index-best-practices) in the Spanner documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
