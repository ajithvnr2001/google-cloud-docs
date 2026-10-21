---
url: https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings/
title: Search and filter with vector embeddings \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:32.770696+00:00
---

# Search and filter with vector embeddings  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Search and filter with vector embeddings Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Note** : To use the general availability ([GA](https://cloud.google.com/products#product-launch-stages)) version of MySQL vector search, the maintenance version of your instance must be version `MYSQL_8_0_36.R20241208.01_00` or later. For information about how to upgrade your instance to a later version that supports GA vector embeddings, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).   
  
For information about the syntax and behavior of vector embeddings for the [Preview](https://cloud.google.com/products#product-launch-stages) version of this feature, see [Work with vector embeddings (Preview)](https://docs.cloud.google.com/sql/docs/mysql/work-with-vectors-preview).   
  
If you're already using the GA version of vector search in Cloud SQL for MySQL 8.0 or 8.4 and want to upgrade to Cloud SQL for MySQL 9.7, then review the [differences in MySQL vector support in Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/vector-search#version-differences) before you [perform the major version upgrade to Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace). 

This page describes the different ways that you can query vector embeddings. For an overview of ANN and KNN similarity searches, see [vector searches](https://docs.cloud.google.com/sql/docs/mysql/vector-search#vector_similarity_search_2).

## Before you begin

[Enable the `cloudsql_vector` database flag](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search#enable-cloudsql-vector-flag) on your Cloud SQL instance.

For instances that use Cloud SQL for MySQL 9.7 or later, although you aren't required to enable the `cloudsql_vector` to create and store vector embeddings, you must [enable the `cloudsql_vector` database flag](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search#enable-cloudsql-vector-flag) on your Cloud SQL instance to create vector indexes and perform ANN searches on your vector data.

## Search approximate nearest neighbors (ANN)

To perform an ANN search, use the [`approx_distance` function](https://docs.cloud.google.com/sql/docs/mysql/functions#ann_function) in a `SELECT` and `ORDER BY` clause. You must use a `LIMIT` clause in an ANN search. You can also get the distance value by putting `approx_distance` in a `SELECT` list.

Use the following syntax for ANN queries:
    
    
    # Ordering by distance
    SELECT title
    FROM books
    ORDER BY approx_distance(embedding, string_to_vector('[1,2,3]'), 'distance_measure=l2_squared')
    LIMIT 4;
    
    # Selecting the distance value
    SELECT
      approx_distance(
        embedding_name,
        string_to_vector('[1,2,3]'),
        'distance_measure=cosine,num_leaves_to_search=3')
        dist
    FROM table
    ORDER BY dist
    LIMIT limit_value;
    

The `approx_distance` function uses the following options:

  * **`embedding`** : uses the vector embedding column name from the base table.
  * **`string_to_vector`** or **`vector_to_string`** : converts a vector to a string and a string to a vector to make the vector human readable.
  * **`distance_measure`** : specify the distance measure to use for a vector similarity search. This value must match the value you set in the `distance_measure` parameter when you created the index. This parameter is required. Possible values for this parameter are: 
    * `COSINE`
    * `L2_SQUARED`
    * `DOT_PRODUCT`
  * **`num_leaves_to_search`** : optional. specifies the number of leaves to probe for an ANN vector similarity search. If you don't specify the number of leaves, then Cloud SQL uses a value generated based on the size of the table, number of leaves in the vector index, and other factors. You can view this value in `information_schema.innodb_vector_indexes`. We recommend that you fine-tune `num_leaves_to_search` to achieve the best balance between search quality and performance for your specific workload. If increased, it impacts performance but improves recall.



The following example shows how to use `approx_distance` to find the top K closest rows using the `l2_squared` distance measure and order the results by distance.
    
    
    # Ordering by distance
    SELECT title
    FROM books
    ORDER BY approx_distance(embedding, string_to_vector('[1,2,3]'),
                             'distance_measure=l2_squared')
    LIMIT 4;
    
    # Selecting the distance value
    SELECT
        approx_distance
            (embedding, string_to_vector('[1,2,3]'),
             'distance_measure=l2_squared') dist
    FROM table
    ORDER BY dist
    LIMIT 4;
    

### Filter results from approx_distance queries

You can use the `approx_distance` function with `WHERE` conditions that filter query results with a non-vector predicate to perform post filtering. The `approx_distance` function is evaluated before applying the filter which means that the number of results returned are nondeterministic.

For example, for the following query:
    
    
    SELECT id FROM products WHERE price < 100
    ORDER BY approx_distance(embedding, @query_vector,'distance_measure=cosine')
    LIMIT 11;
    

The `approx_distance` function returns the 11 nearest neighbors to the query vector regardless of price. In post filtering, the products with a price < 100 are selected. It's possible that all of the nearest neighbors have a price < 100, so there are 11 results to the query. Alternatively, if none of the nearest neighbors have a price < 100, there are 0 rows returned.

If you anticipate that your filter in the `WHERE` condition is very selective, an exact search (KNN) is one option to help ensure that a sufficient number of rows are returned.

Another option is to use iterative filtering to scan more of the ANN search index.

### Use iterative filtering to increase ANN search results

You can use iterative filtering when the selective filters of the `WHERE` clause in your ANN search query are producing fewer results than the number of results specified in your `LIMIT` clause.

For example, in the following query, when you enable iterative filtering, the query scans more of the vector index minus the first set of filtered results.
    
    
    EXPLAIN FORMAT=TREE
    SELECT * FROM t1 WHERE next_id BETWEEN 15 AND 100
    ORDER BY approx_distance(embedding, string_to_vector('[1,2,3]'), 'distance_measure=l2_squared')
    LIMIT 10;
    
    EXPLAIN
    -> Limit: 10 row(s)  (rows=10)
       -> Vector index loop with iterative filtering
          -> Vector index scan on t1
          -> Filter: (t1.next_id between 15 and 100)
             -> Single-row index lookup on t1 using PRIMARY (id=t1.id)
    

You fetch more neighbors from the search vector index iteratively until the configured maximum (`cloudsql_vector_iterative_filtering_max_neighbors`) is reached. Any filter matches are counted toward the `LIMIT` and removed from the additional vector index scans.

#### Enable iterative filtering

By default, iterative filtering is turned off for all sessions and Cloud SQL instances.

To enable iterative filtering for an existing session, use the following SQL statement.
    
    
    SET SESSION cloudsql_vector_iterative_filtering=on;
    

You can also enable iterative filtering globally for all client sessions that connect to the instance by setting the flag on the instance. To set a flag for an instance, see [Set a database flag](https://docs.cloud.google.com/sql/docs/mysql/flags#set_a_database_flag).

For more information about setting system variables at the session or global level, see [Using System Variables](https://dev.mysql.com/doc/refman/8.4/en/using-system-variables.html) in the MySQL documentation.

#### Tune iterative filtering

To control how many nearest neighbors are returned for an ANN search query with iterative filtering enabled, you can use the `cloudsql_vector_iterative_filtering_max_neighbors` session or global system variable. You can use this configuration to increase the number of nearest neighbors that are requested. However, to avoid storing too many results in memory, the maximum for this variable is `1000`.

To set this variable for a session, use the following SQL statement:
    
    
    SET cloudsql_vector_iterative_filtering_max_neighbors=600;
    

The default is `500`, and the minimum number is `10`.

#### Limitations

The following are limitations with using iterative filtering:

  * **Not a guarantee** : when you use iterative filtering, Cloud SQL attempts to find the number of results specified in the `LIMIT` clause, but doesn't guarantee that the number is found. This can happen if the maximum number of neighbors (`cloudsql_vector_iterative_filtering_max_neighbors`) is reached before the `LIMIT` is satisfied, or if there aren't enough rows that match the filter in the table.

  * **Complex queries** : iterative filtering works only when filter predicates are pushed down to the base table's access path. It isn't supported for filters on top of temporary tables; for example, tables that use a `HAVING` clause. In subqueries, only filters on the base table within the subquery itself are considered for iterative filtering.




### Check the fallback status on ANN searches

There are certain cases where an ANN search falls back to a KNN search. These include the following:

  * There's no vector index on the base table.
  * There's a vector index on the base table, but it uses a different distance measure from the `distance_measure` parameter in the `approx_distance` search options.
  * The vector index is corrupt or invisible to the current transaction.
  * The `LIMIT` specified is greater than 10000.
  * There is no `LIMIT` specified.
  * The current query involves more than one `approx_distance` call on the same base table.
  * The optimizer calculates that it's more efficient to use KNN.



All of these cases push a warning to the client indicating that exact search was performed and the reason why.

Use the following command in the mysql client to view the fallback status:
    
    
    SHOW global status LIKE '%cloudsql_vector_knn_fallback%';
    

If you want to use ANN and it's falling back to KNN, the query might run slower. You should find the reason it's falling back and assess whether to make changes so that ANN is used instead.

### Example: Create a vector index and run an ANN query

The following example walkthrough provides steps to create a vector index and run an ANN query in Cloud SQL.

  1. Generate vector embeddings. You can create vector embeddings manually or use a text embedding API of your choice. For an example that uses Vertex AI, see [Generate vector embeddings based on row data](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings#generate_vector_embeddings_based_on_row_data).
  2. Create a table in Cloud SQL that contains a vector embedding column with three dimensions.
         
         CREATE TABLE books(
         id INTEGER PRIMARY KEY AUTO_INCREMENT, title VARCHAR(60), embedding VECTOR(3) USING VARBINARY);
         

  3. Insert a vector embedding into the column.
         
         INSERT INTO books VALUES ((1, 'book title', string_to_vector('[1,2,3]')));
         

  4. Commit the changes.
         
         commit;
         

  5. Create the vector index using the `L2_squared` function to measure distance.
         
         CREATE
           VECTOR INDEX vectorIndex
         ON dbname.books(embeddings)
         USING SCANN QUANTIZER = SQ8 DISTANCE_MEASURE = l2_squared;
         

  6. Use the following syntax to perform an ANN search with a `LIMIT` of 4 search results:
         
         SELECT title
         FROM books
         ORDER BY approx_distance(embedding, string_to_vector('[1,2,3]'), 'distance_measure=l2_squared')
         LIMIT 4;
         
         SELECT approx_distance(embedding, string_to_vector('[1,2,3]'), 'distance_measure=cosine') dist
         FROM books
         ORDER BY dist
         LIMIT 4;
         




## Search K-nearest neighbors (KNN)

To perform a K-nearest neighbor search, use the [`vector_distance` function](https://docs.cloud.google.com/sql/docs/mysql/functions#knn_functions) with a distance measure option and a vector conversion function (`string_to_vector` or `vector_to_string`) in a `SELECT` statement. Use the following syntax:
    
    
    SELECT vector_distance(string_to_vector('[1,2,3]'),
                          string_to_vector('[1,2,3]'),
                          'Distance_Measure=dot_product');
    

Replace the values [1,2,3] with the embedding values of your data.

The following example shows how to use this query with the `cosine_distance` function and the `string_to_vector` vector conversion function.
    
    
    SELECT id,cosine_distance(embedding, string_to_vector('[1,2,3]')) dist
    FROM books
    ORDER BY distance
    LIMIT 10;
    

### Get the Cosine distance in a KNN query

Use the Cloud SQL [`cosine_distance` function](https://docs.cloud.google.com/sql/docs/mysql/functions#knn_functions) to calculate the distance using cosine.
    
    
    SELECT cosine_distance(embedding, string_to_vector('[3,1,2]')) AS distance FROM books WHERE id = 10;
    

### Get the Dot Product distance in a KNN query

Use the Cloud SQL [`dot_product` function](https://docs.cloud.google.com/sql/docs/mysql/functions#dot_product) to calculate the distance using the dot product.
    
    
    SELECT dot_product(embedding, string_to_vector('[3,1,2]')) AS distance FROM books WHERE id = 10;
    

### Get the L2-squared distance in a KNN query

Use the Cloud SQL [`l2_squared_distance` function](https://docs.cloud.google.com/sql/docs/mysql/functions#knn_functions) to calculate the distance using L2 squared.
    
    
    SELECT
      l2_squared_distance(embedding, string_to_vector('[3,1,2]'))
        AS distance
    FROM books
    WHERE id = 10;
    

## What's next

  * Read the [overview about vector search on Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/vector-search).
  * Learn how to [enable and disable vector embeddings on your instance](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search).
  * Learn how to [generate vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings#generate_vector_embeddings_based_on_row_data).
  * Learn how to [create vector indexes](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes).
  * Learn how to [perform searches on vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
