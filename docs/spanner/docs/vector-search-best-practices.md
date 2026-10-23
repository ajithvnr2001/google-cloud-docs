---
url: https://docs.cloud.google.com/spanner/docs/vector-search-best-practices/
title: Vector search best practices \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:43.751403+00:00
---

# Vector search best practices  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/vector-search-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Vector search best practices Stay organized with collections  Save and categorize content based on your preferences. 

This document provides recommendations to optimize performance for vector search in Spanner.

## Understand Spanner basics

To conduct effective Spanner vector search performance testing, understand Spanner basics. For example, re-executing the same query immediately can be faster due to caches. To test performance on an application that primarily uses warm data, perform a warm-up read first.

Consult the following guides:

  * [Performance overview](https://docs.cloud.google.com/spanner/docs/performance)
  * [SQL best practices](https://docs.cloud.google.com/spanner/docs/sql-best-practices)
  * [Perform K-nearest neighbors (KNN) search](https://docs.cloud.google.com/spanner/docs/find-k-nearest-neighbors)
  * [Perform approximate nearest neighbors (ANN) search with vector indexes](https://docs.cloud.google.com/spanner/docs/find-approximate-nearest-neighbors)
  * [Vector indexing best practices](https://docs.cloud.google.com/spanner/docs/vector-index-best-practices)



Spanner processes queries in parallel based on [database splits](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#database-splits). Testing with a sustained production query load can enable [load-based splitting](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#load-based_splitting), which improves query performance through increased parallelism. To increase parallelism for future load, consider [presplitting](https://docs.cloud.google.com/spanner/docs/pre-splitting-overview) your database, especially for KNN.

## Vector search best practices

This document describes the following vector search best practices:

  * Annotate the embedding column
  * Use a top-k query
  * Use SQL literals for the `LIMIT` clause
  * Use batch-oriented scan
  * Use KNN for small datasets
  * Use ANN for large datasets



### Annotate the embedding column

Annotate the embedding column with [`vector_length`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#arrays). This annotation enables performance optimizations for [K-nearest neighbor (KNN)](https://docs.cloud.google.com/spanner/docs/find-k-nearest-neighbors) search and is a prerequisite for [approximate nearest neighbor (ANN)](https://docs.cloud.google.com/spanner/docs/find-approximate-nearest-neighbors) search.

### Use a top-k query

To find the nearest neighbors, use an `ORDER BY` clause with `LIMIT`. Top-k queries are highly optimized for vector search. Avoid filtering by a distance threshold in a `WHERE` clause.

For example, the following is not recommended:
    
    
    SELECT d.DocId
    FROM Documents AS d
    WHERE COSINE_DISTANCE(d.DocEmbedding, @vector) < 1;
    

Instead, use:
    
    
    SELECT d.DocId
    FROM Documents AS d
    ORDER BY COSINE_DISTANCE(d.DocEmbedding, @vector)
    LIMIT 10;
    

Using a top-k query is not only simpler because it eliminates distance threshold tuning, but it also enables performance optimizations specialized for vector search.

### Use SQL literals for the `LIMIT` clause

If the top-k limit is fixed, use a SQL literal instead of a parameter. For example, use `LIMIT 10` instead of `LIMIT @limit`. This provides the Spanner [query optimizer](https://docs.cloud.google.com/spanner/docs/query-optimizer/overview) with more information to select the best [query execution plan](https://docs.cloud.google.com/spanner/docs/query-execution-plans).

### Use batch-oriented scan

Vector search queries are scan heavy. For KNN queries, consider using batch-oriented scan with the [`scan_method=batch` query hint](https://docs.cloud.google.com/spanner/docs/sql-best-practices#enforce-scan-method). This is the default scan method for ANN queries.

### Use KNN for small datasets

If KNN is sufficient for your latency budget, don't create a vector index. KNN is more accurate, avoids index creation and maintenance costs, and can perform better than ANN when the number of input rows after any filtering is small.

#### Accelerate filtered KNN with a secondary index

To improve the performance of a filtered KNN query, create a [secondary index](https://docs.cloud.google.com/spanner/docs/secondary-indexes) on the filtering column. For example, consider the following query:
    
    
    SELECT d.DocId
    FROM Documents AS d
    WHERE Category = 'toy'
    ORDER BY COSINE_DISTANCE(d.DocEmbedding, @vector)
    LIMIT 10;
    

If the number of documents per category is fewer than a few tens of thousands and your application can accept a query latency of 100 ms, create a secondary index on the `Category` column. Store the `DocEmbedding` column in the index:
    
    
    CREATE INDEX ON Documents(Category) STORING (DocEmbedding);
    

This index creation helps accelerate the filtered query.

### Use ANN for large datasets

If the number of rows is large after evaluating for filters, create a vector index and use ANN search. Several techniques can accelerate filtering with ANN:

  * **Store filtering columns** : To enable filtering while traversing the vector search, store filtering columns in the vector index. This allows unqualified rows to be removed early in the execution.
        
        CREATE VECTOR INDEX ON Documents(DocEmbedding) STORING(Category);
        

  * **Key filtering columns** : To speed up filtering for highly selective columns that remove many results, organize these columns as additional key columns in the vector index. Queries that specify exact equality (using the `=` operator) for these additional keys accelerate the most. Using the `IN` clause for any of these additional keys doesn't achieve the same level of acceleration.
        
        CREATE VECTOR INDEX ON Documents(DocEmbedding, Category);
        

  * **Avoid storing large columns or using them as keys** : Doing so might dilute the data blocks for embeddings, which might reduce read efficiency. As an alternative, consider using a hash column in the index, and use the original large column as a post-filter after top-k.

  * **Create a filtered (partial) vector index** :If you query only a subset of the dataset, and a filtering condition defines that subset, such as `Category = "Tech"`, create a [filtered or partial vector index](https://docs.cloud.google.com/spanner/docs/vector-indexes#filter-vector-index).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
