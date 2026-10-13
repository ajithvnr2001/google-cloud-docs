---
url: https://docs.cloud.google.com/sql/docs/mysql/vector-search/
title: Vector search in Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:01.099828+00:00
---

# Vector search in Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/vector-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Vector search in Cloud SQL for MySQL Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Note** : To use the general availability ([GA](https://cloud.google.com/products#product-launch-stages)) version of MySQL vector search, the maintenance version of your instance must be version `MYSQL_8_0_36.R20241208.01_00` or later. For information about how to upgrade your instance to a later version that supports GA vector embeddings, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).   
  
For information about the syntax and behavior of vector embeddings for the [Preview](https://cloud.google.com/products#product-launch-stages) version of this feature, see [Work with vector embeddings (Preview)](https://docs.cloud.google.com/sql/docs/mysql/work-with-vectors-preview).   
  
If you're already using the GA version of vector search in Cloud SQL for MySQL 8.0 or 8.4 and want to upgrade to Cloud SQL for MySQL 9.7, then review the [differences in MySQL vector support in Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/vector-search#version-differences) before you [perform the major version upgrade to Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace). 

This page describes how vector searches are implemented on Cloud SQL for MySQL instances. Cloud SQL lets you store vector embeddings, create vector indexes, and perform [vector searches](https://research.google/blog/announcing-scann-efficient-vector-similarity-search/) in conjunction with your other stored data.

## Vector embedding storage

You store vector embeddings in a table that's compliant with atomicity, consistency, isolation, and durability (ACID) properties. Like other relational data in the table, you can access the vector embeddings in the table with existing transactional semantics.

To establish mapping between table rows and vector representations, you need to create a column in your table to store your vector embeddings. The column must use the `VECTOR` data type. The vector embedding column can only store vector embeddings that use exactly the same dimensions that you specify when you define the column. There are no restrictions for the number of rows in the table where you store vector embeddings.

If you have enough storage and memory available on your Cloud SQL instance, then you can have multiple tables with their own vector embedding columns.

[Data replication](https://dev.mysql.com/doc/refman/8.4/en/innodb-and-mysql-replication.html) works the same way for the vector embedding column as it does for other MySQL InnoDB columns.

For a list of limitations and restrictions for vector embedding tables, columns, and DML statements, see [Limitations](https://docs.cloud.google.com/sql/docs/mysql/vector-search#limitations).

## Vector indexes

You must use a vector index to perform ANN similarity searches on your vector embeddings. Cloud SQL creates vector indexes using the [Scalable Nearest Neighbors (ScANN)](https://research.google/blog/announcing-scann-efficient-vector-similarity-search) algorithm.

Vector indexes have the following requirements:

  * You can only create one vector index per table.
  * If you have multiple tables with vector embeddings on your instance, then you can create vector indexes for each of them.
  * If you're creating a vector index, then you can't add a constraint to the primary key of the indexed table.



For better search quality, create a vector index only after loading the bulk of your data in the base table. If you have less than 1000 embeddings in the base table, then the index creation fails.

When deciding whether to create a vector index, if you have a small number of rows, consider whether you can perform a KNN search instead. The decision to use a KNN versus an ANN search also depends on the number of dimensions on the vector embedding. A larger number of embeddings might require a vector index.

For a list of limitations and restrictions for vector indexes, see [Limitations](https://docs.cloud.google.com/sql/docs/mysql/vector-search#limitations). For information on creating a vector index, see [Create and manage vector indexes](https://docs.cloud.google.com/sql/docs/mysql/vector-search#create_and_manage_vector_indexes).

### Vector index updates

Cloud SQL updates vector indexes in real time. Any transaction that performs data manipulation language (DML) operations on the base table also propagates changes to the associated vector indexes. Vector indexes behave in the same way as any other secondary index on the table. The vector indexes are fully transactionally consistent and ACID compliant. If you roll back a transaction, then the corresponding rollback changes also occur in the vector index.

### Replication of vector indexes

Cloud SQL replicates vector indexes to all read replicas, including for cascading replicas. When you create a new read replica from a primary instance that has vector embedding, the read replica inherits the vector embedding settings from the primary instance. For existing read replicas, you must enable vector embedding support on each one.

In terms of impact to replication lag, creating and maintaining vector indexes operate in the same way as regular MySQL indexes.

### Persistence, shutdown, and impact on maintenance

Vector indexes are persisted the same way as base tables, with full ACID support. Vector indexes are always in-sync with their base table data, and have the same visibility, isolation, and crash safety. There is no impact to the vector index when the instance is shut down or receives maintenance.

### Index maintenance

After extensive DML operations are performed on the base table, the vector index that you trained on the initial data (at the time of index creation) might not reflect the new state. This can impact search quality.

There are two parts to the index:

  * The index tree. This is built by training on existing data. It stays unchanged during the lifetime of the index.
  * The index leaves. These contain all the rows of data. The index leaves never go out of sync.



The index tree might become less efficient after a large number of DML statements are run because rows move from one leaf to another. To refresh the index tree, you need to rebuild the index.

### Unsupported DDL operations on tables with vector indexes

The following data definition language (DDL) operations are unsupported for tables that have vector indexes.

  * Alter table operations that require the copy algorithm
  * Alter table operations that require the table to be rebuilt
  * Drop or change the primary key
  * Move the table to a general tablespace



## Vector search

Cloud SQL provides vector distance functions that you use to perform approximate nearest neighbor (ANN) and K-nearest neighbors (KNN) vector similarity searches on your instance. When you run a query, the query vector is compared to vectors in your dataset. Distance functions calculate the distance between the vectors using a similarity metric such as cosine. The vectors with the shortest distance between them are the most similar and are returned in search results.

Cloud SQL uses the following functions to measure distance between vectors in vector searches when you perform ANN and KNN vector searches:

  * **[Cosine](https://en.wikipedia.org/wiki/Cosine_similarity#Cosine_distance)** : measures the cosine of the angle between two vectors. A smaller value indicates greater similarity between the vectors.
  * **[Dot product](https://mathworld.wolfram.com/DotProduct.html)** : calculates the cosine of the angle multiplied by the product of corresponding vector magnitudes.
  * **[L2 squared distance](https://en.wikipedia.org/wiki/Euclidean_distance#Squared_Euclidean_distance)** : measures the Euclidean distance between two vectors by adding the squared distance on each dimension.



### KNN search

A KNN vector search is the preferred search method when you need exact results or want to add selective filtering. KNN search performs a distance computation of the query vector with every embedding in the dataset to find the nearest neighbor. KNN searches in Cloud SQL provide perfect recall. KNN searches don't use a vector index so they're a good option when working with smaller datasets.

To perform a KNN search, you use the `vector_distance` function that takes two vectors as input: the query vector (what you're searching for) and a candidate vector from your dataset. It calculates the distance between these two vectors. You use vector_distance in a `SELECT` statement. For more information, See [Search K-nearest neighbors (KNN)](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings#search_k-nearest_neighbors_knn).

If you find that KNN isn't performing well, you can build a vector index later and continue to use `approx_distance` in your application for ANN searches.

### ANN search

An ANN vector search is the preferred search type when query efficiency is a concern. It speeds up similarity searches by calculating the distance between your query vector and only a portion of the vectors in your dataset. To do this, Cloud SQL organizes the data into clusters or partitions and then focuses the search on the clusters closest to the query. ANN searches require vector indexes. These indexes prioritize search speed over perfect recall. In Cloud SQL, the [TREE_SQ](https://docs.cloud.google.com/sql/docs/mysql/vector-search#vector_index_types) index type is used for ANN searches.

To perform an ANN search, you use the [`approx_distance`](https://docs.cloud.google.com/sql/docs/mysql/functions#ann_function) function with a distance measurement option. You use `approx_distance` in an `ORDER BY` or `SELECT` list and a `LIMIT` clause is permitted to limit search results. You can also add a `WHERE` clause to perform post-filtering of your search results. If you want to have more control over the number of results that are returned when you perform an ANN search with filters, then you can use [iterative filtering](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings#ann-iterative-filtering). With iterative filtering, your search query can return more search results by scanning more of the vector index until the preferred number of neighbors are found.

You can enable iterative filtering for your search query by setting the `cloudsql_vector_iterative_filtering` flag to `ON` at a session level for individual clients or a global level for all clients that connect to the instance.

For more information, see [Search approximate nearest neighbors (ANN)](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings#ann).

There are some cases when an ANN search falls back to a KNN search. For more information, see [Check the fallback status for ANN searches](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings#check_the_fallback_status_on_ann_searches).

## Vector support differences in Cloud SQL for MySQL versions

Cloud SQL for MySQL introduced support for vector search in version 8.0.36 and later. Starting in Cloud SQL for MySQL version 9.7, Cloud SQL has modified specific vector search capabilities to integrate better with community-developed vector support and storage functionalities introduced in community-developed MySQL 9.0.

The following table provides a comparison of Cloud SQL for MySQL versions that how the differences in version can affect the usage of vector search in Cloud for MySQL.

Support area | Cloud SQL for MySQL 8.4 and earlier | Cloud SQL for MySQL 9.7 and later  
---|---|---  
**Vector enablement** | To add vector embeddings to your MySQL database and use vector search, you must set the `cloudsql_vector` flag to `on` for your Cloud SQL instance.  | If you want to create vector indexes and perform ANN search, then you must set the `cloudsql_vector` flag to `on`.  
**Vector embedding columns in a table** |  A table can only have _one_ vector embedding column.  |  You are limited to one vector embedding column per table _only_ if you create an index on the table. If you don't create an index on the table, then the table can have multiple vector embedding columns.   
**Use of`COMMENT` and `CONSTRAINT` to identify vector embedding columns** |  To distinguish the vector embedding column from other columns, Cloud SQL adds a special `COMMENT` annotation and `CONSTRAINT` rule to the column. The constraint is required for input validation, and the vector embedding column annotation is visible as a comment. You can't modify or delete the comment or constraint.  |  The `COMMENT` annotation and `CONSTRAINT` rule are no longer used to identify vector embedding columns in Cloud SQL for MySQL 9.7.   
**Dimensions limit** | A vector embedding is restricted to 16,000 dimensions with no default.  | A vector embedding is restricted to 16,383 dimensions with a default of 2,048.   
**Vector storage format** |  `VARBINARY` format  | Community-based storage format   
**Syntax for declaring the[vector data type](https://dev.mysql.com/doc/refman/9.7/en/vector.html)** |  ` VECTOR(VECTOR_DIMENSIONS)  
USING VARBINARY ` |  ` VECTOR(VECTOR_DIMENSIONS)  
[USING VARBINARY] `  
**Conversion function differences** | The output of the `vector_to_string` function is printed as the entire value.  | The output of the [`vector_to_string`](https://dev.mysql.com/doc/refman/9.7/en/vector-functions.html#function_vector-to-string) function is rendered in scientific notation, which is the community standard.   
  
## Limitations

The following are limitations apply to all versions of Cloud SQL that support vectors:

  * There can only be one vector index per table.
  * The vector embedding column can't be a generated column.
  * Table-level partitioning on tables with vector embedding columns isn't supported.
  * Primary keys that use the `BIT`, `BINARY`, `VARBINARY`, `JSON`, `BLOB`, `TEXT` data types, or spatial data aren't supported for vector indexes. Composite primary keys also can't include any of these types.
  * If there's a vector index, then you can't add a constraint to the primary key of the base table.
  * When a vector index is present on a table, there are DDL operations that you can't perform. For more information, see [Unsupported DDL operations on tables with vector indexes](https://docs.cloud.google.com/sql/docs/mysql/vector-search#unsupported_ddl_operations_on_tables_with_vector_indexes).



The following restrictions are for vector search queries:

  * The `approx_distance` function can only be used in an `ORDER BY` or `SELECT` list.
  * Predicates involving the base table can be used in the `WHERE` condition in combination with `approx_distance` expressions in the `ORDER BY` or `SELECT` list. The `WHERE` condition predicates are evaluated after the `approx_distance` vector functions are evaluated.



## What's next

  * Read the [overview about vector search on Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/vector-search).
  * Learn how to [generate vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings#generate_vector_embeddings_based_on_row_data).
  * Learn how to [create vector indexes](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes).
  * Learn how to [perform searches on vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
