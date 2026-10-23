---
url: https://docs.cloud.google.com/sql/docs/mysql/functions/
title: Cloud SQL functions \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:36.333437+00:00
---

# Cloud SQL functions  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Cloud SQL functions Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This pages describes Cloud SQL functions.

## Vector conversion functions

This following table lists the functions that you can use to manipulate vector information in a `SELECT` statement.

**Function** |  | **Description**  
---|---|---  
**vector_to_string** | Input: **VECTOR** Output: **STRING** | Converts an argument to a string in a human-readable vector format. **Input:** one argument of type `VECTOR` **Output:** a string Syntax: `vector_to_string(some_embedding)`  
**string_to_vector** | Input: **STRING** Output: **VECTOR** | Converts a string to a human-readable vector format. This lets you write the values you want represented in a vector. **Input:** a string Syntax: `string_to_vector('some_embedding')` **Output:** one value of type vector.  
  
## Search functions

This section describes Cloud SQL search functions.

### KNN functions

This following table lists the functions that you can use to calculate the KNN vector distance.

**Function** | **Data type** | **Description**  
---|---|---  
**vector_distance** | Input: **VECTOR** Output: **REAL** | Calculates the vector distance between two `VECTOR`s. The two `VECTOR`s must have the same dimensions. **Input** : required. Takes two vector values, An optional third string argument indicates the distance measure. Default is `l2_squared_distance. Other options include `cosine_distance` and `dot_product`.  **Output** : the distance between the two vectors. For example: ` SELECT vector_distance(string_to_vector('[1,-2,3]'), string_to_vector('[1,2,3]'), 'Distance_Measure=dot_product'); `  
**cosine_distance** | Input: **VECTOR** Output: **REAL** | Algorithm to calculate the cosine of the angle between two vectors. A smaller value indicates greater similarity between the vectors. **Input** : takes two vector values. These can be column names or constants. **Output** : the cosine distance between the two vectors. For example: `SELECT cosine_distance(string_to_vector('[1,2,3]'), string_to_vector('[1,1,1]'));` ` SELECT id FROM t1 ORDER BY cosine_distance(string_to_vector('[1,2,3]'), embedding_column_name) LIMIT 10;`  
**dot_product** | Input: **VECTOR** Output: **REAL** | Algorithm that performs the dot product operation between two input vectors to calculate and output a single scalar value. **Input** : takes two vector values. These can be column names or constants. **Output** : the dot product of the two vectors. For example: `SELECT dot_product(string_to_vector('[1,2,3]'), string_to_vector('[1,1,1]'));` `SELECT id FROM t1 ORDER BY dot_product(string_to_vector('[1,2,3]'), embbeding_column_name) LIMIT 10;`  
**l2_squared_distance** | Input: **VECTOR** Output: **REAL** | Algorithm that adds the squared distance on each dimension between two input vectors to measure the Euclidean distance between them. **Input** : takes two vector values. These can be column names or constants. **Output** : the L2 squared distance between the two vectors. For example: `SELECT l2_squared_distance(string_to_vector('[1,2,3]'), string_to_vector('[1,1,1]'));` ` SELECT id FROM t1 ORDER BY l2_squared_distance(string_to_vector('[1,2,3]'), embbeding_column_name) LIMIT 10;`  
  
### ANN function

This following table lists the function that you can use to calculate vector distance.

Function | Data Type | Description  
---|---|---  
**approx_distance** | Input: **VECTOR** Output: **REAL** | Finds the top K closest rows that satisfy the distance measure using the selected algorithm. This function queries the approximate nearest neighbors from a vector column to a constant value. The two embedding column's `VECTOR` type and the constant `VECTOR` must have the same dimensions. There are some cases when this function falls back to a KNN (exact search) search instead of ANN search. You must include a limit with queries that use this function. **Syntax:** `approx_distance(embedding_name,  
query_vector,  
'distance_measure=algorithm_name  
[, num_leaves_to_search=value]'` **Inputs:**

  1. embedding_name: A vector embedding column name from the base table.
  2. query_vector: A constant of type `VECTOR` which can be (but is not required to be) the output of `string_to_vector`.
  3. The comma-separated search string options include the following: 
     * distance_measure: required. Uses an algorithm to measure distance between vectors. It uses the following string literals: 
       * `L2_SQUARED`
       * `COSINE`
       * `DOT_PRODUCT`
For example: `distance_measure=cosine`
     * `num_leaves_to_search`: optional. Specifies the number of leaves to probe for an ANN vector similarity search. If you don't specify the number of leaves, CloudSQL for MySQL picks a computed value for num_leaves_to_search which can be viewed in `information_schema.innodb_vector_indexes`. The computed number is generally a good starting point with good search quality and performance. It's recommended that you tune `num_leaves_to_search` based on your workload and performance or quality trade off. 
For example: `'distance_measure=dot_product,  
num_leaves_to_search=100'` **Required LIMIT value:** The specified limit is used as the number of neighbors to return (also known as the top K).  **Output** : The approximate distance of the top K closest rows in the base table. This function can only be used in the `ORDER BY` or `SELECT` list. For example: `SELECT id, approx_distance(embedding_column_name   
string_to_vector('[1,1,1]'),   
'distance_measure=cosine') dist from t1   
ORDER BY dist LIMIT 10;` `SELECT id  
FROM t1  
ORDER BY  
approx_distance(  
embedding_column_name  
string_to_vector('[1,1,1]'),  
'distance_measure=dot_product,num_leaves_to_search=100) LIMIT 4;`

  
  
## What's next

  * Read the [overview about vector search on Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/vector-search).
  * Learn how to [enable and disable vector embeddings on your instance](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search).
  * Learn how to [generate vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings#generate_vector_embeddings_based_on_row_data).
  * Learn how to [create vector indexes](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes).
  * Learn how to [perform searches on vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
