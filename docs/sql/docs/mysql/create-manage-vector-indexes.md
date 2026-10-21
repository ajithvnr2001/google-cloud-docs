---
url: https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes/
title: Create and manage vector indexes \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:38.370655+00:00
---

# Create and manage vector indexes  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Create and manage vector indexes Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Note** : To use the general availability ([GA](https://cloud.google.com/products#product-launch-stages)) version of MySQL vector search, the maintenance version of your instance must be version `MYSQL_8_0_36.R20241208.01_00` or later. For information about how to upgrade your instance to a later version that supports GA vector embeddings, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).   
  
For information about the syntax and behavior of vector embeddings for the [Preview](https://cloud.google.com/products#product-launch-stages) version of this feature, see [Work with vector embeddings (Preview)](https://docs.cloud.google.com/sql/docs/mysql/work-with-vectors-preview).   
  
If you're already using the GA version of vector search in Cloud SQL for MySQL 8.0 or 8.4 and want to upgrade to Cloud SQL for MySQL 9.7, then review the [differences in MySQL vector support in Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/vector-search#version-differences) before you [perform the major version upgrade to Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace). 

This page describes how to configure memory for vector indexes, and create, tune, monitor, and drop vector indexes.

## Before you begin

Before you create a vector index, you must load data into the base table with vector embedding values. Your base table must have at least 1,000 rows. If you have more data points available, you can get better partitioning and training of the index.

[Enable the `cloudsql_vector` database flag](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search#enable-cloudsql-vector-flag) on your Cloud SQL instance.

For instances that use Cloud SQL for MySQL 9.7 or later, although you aren't required to enable the `cloudsql_vector` to create and store vector embeddings, you must [enable the `cloudsql_vector` database flag](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search#enable-cloudsql-vector-flag) on your Cloud SQL instance to create vector indexes.

## Configure memory allocation for vector indexes

The `cloudsql_vector_max_mem_size` database flag controls how much memory your Cloud SQL instance dedicates to vector indexes. This is a static flag that requires a restart of your instance. This memory serves two main purposes:

  1. **Storing the vector index structure:** the non-leaf portion of the vector index (the `TREE_MEMORY`) resides in this memory. The approximate size of this tree depends on the number of leaf nodes (`num_leaves`) and the dimensions of your vectors:
         
         Approximate TREE_MEMORY = num_leaves * vector dimensions * 4 * 2
         

For example, an index with 1000 leaves and 768 dimensions would have an approximate `TREE_MEMORY` of 1000 * 768 * 4 * 2 or 6144000 bytes. You can also check the actual `TREE_MEMORY` using the `information_schema.innodb_vector_indexes` table. Cloud SQL manages that memory. You don't need to allocate space for all vector indexes simultaneously, as inactive indexes are unloaded to make room for other requests.

  2. **Memory for index creation (training data):** during vector index creation, memory is needed to process a sample of the data from your base table to build the index. This memory is used only during the index creation process and is freed afterward. The approximate size of the memory needed for training is:
         
         approximate_training_memory = num_rows in base table * 0.1 * 4 * vector dimensions
         

For example, with a table of 1,000,000 rows and 768 dimensions, the `training_memory` would be 1000000 * 0.1 * 768 * 4 or 307,200,000 bytes. Only 10% of the base table data is sampled to compute the centroids for the tree.

When you enable the `cloudsql_vector` flag, Cloud SQL automatically sets a default `cloudsql_vector_max_mem_size` based on your VM size. This default usually suffices for typical workloads. Cloud SQL reduces the `innodb_buffer_pool_size` flag to allocate this memory. The default maximum value for `cloudsql_vector_max_mem_size` is 16GB. If you need to tune your memory size, then you can dynamically adjust `cloudsql_vector_max_mem_size` based on your vector index usage.

**Important:** If you increase `cloudsql_vector_max_mem_size`, then to avoid memory issues, you must decrease `innodb_buffer_pool_size` correspondingly.



### `cloudsql_vector_max_mem_size` values

**VM size** | **`cloudsql_vector_max_mem_size`**  
---|---  
4GB | 194MB  
8GB | 515MB  
16GB | 1.2GB  
32GB | 2.56GB  
64GB | 5.12GB  
128GB | 10.24GB  
256GB+ | 16GB  
  
The range of memory allocated for the vector index is the following:

  * 128MB minimum
  * 10% of the buffer pool
  * 16GB maximum



You can adjust the memory later, as needed.

For information about monitoring the size of your vector index, see [Monitor vector indexes](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes#monitor_vector_indexes).

To update the memory allocated for vector indexes on the instance, use the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
     --database-flags= cloudsql_vector_max_mem_size=NEW_MEMORY_VALUE;
    

Replace the following:

  * INSTANCE_NAME: the name of the instance on which you are changing the memory allocation.
  * NEW_MEMORY_VALUE: the updated memory allocation, in bytes, for your vector indexes.



This change takes effect immediately after a database restart.

## Create a vector index

There are two ways to create a vector index:

  * [`CREATE VECTOR INDEX`statement](https://docs.cloud.google.com/sql/docs/mysql/data-definition-language#create_vector_index), a Cloud SQL extension to standard MySQL syntax.
  * [`ALTER TABLE` statement](https://docs.cloud.google.com/sql/docs/mysql/data-definition-language#alter_table) with the Cloud SQL `ADD VECTOR INDEX` clause extension. You can't run this statement simultaneously with other DDL statements on thetable.

**Note:** The size of your base table is calculated by scanning the table for the number of rows with non-NULL entries in the vector embeddings column.

Use the following syntax to create a vector index using `CREATE VECTOR INDEX`:
    
    
    CREATE
      VECTOR INDEX INDEX_NAME
    ON TABLE_NAME(COLUMN_NAME)
    USING
      SCANN[QUANTIZER = SQ8]
        DISTANCE_MEASURE
      = L2_SQUARED | COSINE | DOT_PRODUCT[NUM_LEAVES = INT_VALUE ];
    

The following are the index options:

  * **`USING SCANN`** : optional. Indicates the index type to use. **SCANN** is the only supported value.
  * **`QUANTIZER`** : optional. Maps a high-dimensional vector to a compressed representation. **SQ8** is the only supported value.
  * **`DISTANCE_MEASURE`** : required. Specifies a mathematical formula to use to calculate the similarity of two vectors. You must set the same distance measure in this parameter as the distance you set in the `approx_distance` search options. The supported literals are: 
    * `L2_SQUARED`
    * `COSINE`
    * `DOT_PRODUCT`
  * **`NUM_LEAVES`** : optional. Specifies how many partitions (leaves) to build. Only change this setting from its default setting if you have a good understanding of ANN search and your dataset. The number specified can't be larger than the number of embeddings in the base table.



For example, to create a vector index, run the following:
    
    
    CREATE
      VECTOR INDEX vectorIndex
    ON dbname.books(embeddings) DISTANCE_MEASURE = L2_SQUARED;
    

While the `CREATE` statement is running, the base table is put into a read-only mode and no DMLs are allowed on the base table.

You can use the following syntax to create an index on an existing table:
    
    
    ALTER TABLE tbl_name
      ADD VECTOR INDEX index_name(key_part)[index_option];
    

For example, to create an index on an existing table:
    
    
    ALTER TABLE t1 ADD VECTOR INDEX index1(j)
    USING SCANN QUANTIZER = SQ8 DISTANCE_MEASURE = l2_squared NUM_LEAVES = 10;
    

## Tune the vector index

This section gives further information about the parameters that you use to build the vector index. To tune the vector index, use this information to determine how to influence the build process.

**Parameter** | **Description** | **Default** | **Scope** | **Impact**  
---|---|---|---|---  
`cloudsql_vector_max_mem_size` | Memory allocated for index training. | Varies | Instance | Insufficient memory can lead to build failures. See [Configure memory allocation for vector indexes](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes#configure_memory_allocation_for_vector_indexes).   
`innodb_ddl_threads` | Degree of parallelism for index training and build. | 4 | Session | Higher values reduce build time but increase CPU load. Set this value to the number of CPUs you can spare without adversely affecting database operations.  
  
Ensure `cloudsql_vector_max_mem_size` is configured appropriately for training. Adjust `innodb_ddl_threads` to balance build time and CPU load, considering the impact on concurrent database operations. Monitor CPU utilization during the build.

## Drop a vector index

To drop a vector index, use the SQL `DROP INDEX` or `ALTER TABLE` statements with the index name you want to drop, as shown in the following:
    
    
    DROP INDEX index_name ON books;
    
    ALTER TABLE table_name
    DROP INDEX index_name;
    

## Monitor vector indexes

Cloud SQL provides the following information schema tables with real-time information about vector indexes that are loaded in its memory:

  * `information_schema.innodb_vector_indexes` lists all the vector indexes that are opened in the memory after restart.
  * `information_schema.innodb_all_vector_indexes` lists all the vector indexes that exist on the instance (even if they aren't opened in the memory yet).
  * `information_schema.innodb_vector_indexes_memory` provides information about overall memory usage of vector indexes in the instance.



For more detailed information, see the [Information schema](https://docs.cloud.google.com/sql/docs/mysql/information-schema).

To view information in the `innodb_vector_indexes` table, run the following command:
    
    
    SELECT * FROM information_schema.innodb_vector_indexes \ G;
    

The output looks similar to the following:
    
    
     INDEX_NAME: t1_vec_index
     TABLE_NAME: test.t1
     INDEX_TYPE: TREE_SQ
     DIMENSION: 3
     DIST_MEASURE: COSINE
     STATUS: Ready
     STATE: INDEX_READY_TO_USE
     NUM_LEAVES: 10
     NUM_LEAVES_TO_SEARCH: 10
     QUERIES: 1
     MUTATIONS: 1
     TREE_MEMORY: 443
    

## Best practices for working with vector indexes

This section provides best practices for working with vector indexes. Every workload is different, and you might need to adjust accordingly.

  * After major data manipulation language (DML) operations, it's a good practice to rebuild the index.
  * Generally, it's acceptable to let Cloud SQL compute the number of leaves, or containers for embeddings, to use. The number of leaves determines how many partitions the vector index is divided into. If you have a use case where you want to specify the number of leaves, then it's recommended to have at least 100 vectors per leaf for the best recall. In the context of vector search, recall refers to the percentage of vectors that the index returns which are true nearest neighbors.



## What's next

  * Read the [overview about vector search on Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/vector-search).
  * Learn how to [enable and disable vector embeddings on your instance](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search).
  * Learn how to [generate vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings#generate_vector_embeddings_based_on_row_data).
  * Learn how to [perform searches on vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
