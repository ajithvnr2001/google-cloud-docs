---
url: https://docs.cloud.google.com/sql/docs/mysql/data-definition-language/
title: Cloud SQL Data Definition Language (DDL) \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:04.594018+00:00
---

# Cloud SQL Data Definition Language (DDL)  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/data-definition-language/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Cloud SQL Data Definition Language (DDL) Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page defines the syntax for Cloud SQL extensions to the MySQL data definition language (DDL) statements.

## VECTOR statements

This section has information about `VECTOR` statements.

### CREATE VECTOR INDEX

Creates a vector index.
    
    
    CREATE VECTOR INDEX index_name
    [opt_index_type]
    ON table_name (column_name)
    [index_options]
    
    where opt_index_type is:
     | USING SCANN
    
    where index_option is :
     USING SCANN
     | [QUANTIZER=SQ8]
     | [NUM_LEAVES=int_value]
     | DISTANCE_MEASURE=L2_SQUARED|DOT_PRODUCT|COSINE
    

**Parameters**

  * **`USING SCANN`** : required. The index type to use when creating the vector index. This algorithm creates a [ScaNN index](https://research.google/blog/announcing-scann-efficient-vector-similarity-search/). `SCANN` is the only supported value. You can't modify this parameter.
  * **`QUANTIZER`** : optional. This parameter maps a high-dimensional vector to a compressed representation. `SQ8` is the only supported value. You can't modify this parameter.
  * **`NUM_LEAVES`** : optional. Specifies how many partitions (leaves) to build. Only change this setting from its default setting if you have a good understanding of ANN search and your dataset. The number specified can't be larger than the number of embeddings in the base table.
  * **`DISTANCE_MEASURE`** : required. A mathematical formula that calculates the similarity of two vectors. You must set the same distance measure in this parameter as the distance in the `approx_distance` search options. The supported laterals are: 
    * `L2_SQUARED`
    * `COSINE`
    * `DOT_PRODUCT`



**Example**

The following example shows how to create a vector index on the `table_name` table
    
    
    CREATE
      VECTOR INDEX index1
    ON table_name(vector_column_name)
    USING SCANN QUANTIZER = SQ8 DISTANCE_MEASURE = l2_squared;
    

### ALTER TABLE

Adds a vector index to an existing table. Vector searches require `SCANN` as the index option and the quantization type must be `SQ8`.
    
    
    ALTER TABLE table_name
      ADD VECTOR INDEX index_name(key_part)[index_option];
    
    WHERE key_part is:{ _col_name_[(_length_)] | (_expr_) }
    WHERE
      index_option
      is:USING
        SCANN
        | [QUANTIZER = SQ8]
        | [NUM_LEAVES = int_value]
        | DISTANCE_MEASURE
      = L2_SQUARED | DOT_PRODUCT | COSINE
    

**Parameters**

  * **`USING SCANN`** : required. The index type to use when creating the vector index. This algorithm creates a [ScaNN index](https://research.google/blog/announcing-scann-efficient-vector-similarity-search/). `SCANN` is the only supported value. You can't modify this parameter.
  * **`QUANTIZER`** : optional. This parameter maps a high-dimensional vector to a compressed representation. `SQ8` is the only supported value. You can't modify this parameter.
  * **`NUM_LEAVES`** : optional. Specifies how many partitions (leaves) to build. Only change this setting from its default setting if you have a good understanding of ANN search and your dataset. The number specified can't be larger than the number of embeddings in the base table.
  * **`DISTANCE_MEASURE`** : required. A mathematical formula that calculates the similarity of two vectors. You must set the same distance measure in this parameter as the distance in the `approx_distance` search options. The supported laterals are: 
    * `L2_SQUARED`
    * `COSINE`
    * `DOT_PRODUCT`



**Example**

The following example shows how to add a vector index on the `t1` table.
    
    
    ALTER TABLE t1 ADD VECTOR INDEX index1(j)
    USING SCANN QUANTIZER = SQ8 DISTANCE_MEASURE = l2_squared;
    

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
