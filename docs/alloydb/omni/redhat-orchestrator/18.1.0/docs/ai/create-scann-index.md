---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/create-scann-index/
title: Create a ScaNN index \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:32:30.736812+00:00
---

# Create a ScaNN index  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/create-scann-index/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)



Send feedback 

#  Create a ScaNN index Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/ai/create-scann-index)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/ai/create-scann-index)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/create-scann-index)

Use [stored embeddings](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/store-embeddings) to generate ScaNN vector indexes and query embeddings with AlloyDB Omni. 

The [ScaNN index](https://github.com/google-research/google-research/blob/master/scann/docs/algorithms.md) is a Google-made, tree-based quantization index for approximate nearest neighbor search. It provides lower index building time and smaller memory footprint as compared to HNSW. In addition, it provides faster QPS in comparison to HNSW based on the workload.

## Before you begin

Before you can start creating indexes, you must complete the following prerequisites.

  * [Embedding vectors are added to a table](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/store-embeddings) in your AlloyDB Omni database.

If you try to generate a ScaNN index on an empty or partitioned table, then you might encounter some issues. For more information about the errors generated, see [Troubleshoot ScaNN index errors](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/troubleshoot-scann-indexes). To create an index on an empty or small table, see Deferred index creation for empty or nearly empty tables.

  * [`vector`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/extensions#pgvector) and [`alloydb_scann`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/extensions#alloydb_scann) extensions are installed:
        
        CREATE EXTENSION IF NOT EXISTS alloydb_scann CASCADE;
        

Installing the `alloydb_scann` extension automatically checks to see if the `vector` extension is installed and installs it if it isn't. You don't need to manually install `vector` separately.

  * If you want to create a four-level ScaNN index, you must first enable the [Preview](https://cloud.google.com/products#product-launch-stages) feature for your AlloyDB Omni instance. To enable the Preview feature, choose one of the following two methods:

    * Enable the [`scann.enable_preview_features`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/alloydb-flags#scann.enable_preview_features) database flag.

For more information on configuring database flags, see [Configure database parameters](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-database-parameters).

    * Set the [`scann.max_allowed_num_levels`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/alloydb-flags#scann.max_allowed_num_levels) database flag to `3` at the session or instance level. To set the flag at the session level, run the following command:
          
          SET scann.max_allowed_num_levels = 3;
          

For more information about setting the flag at the instance level, see [Configure database parameters](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-database-parameters).




## Create an automatically-tuned index

Automatically-tuned ScaNN indexes simplify index creation by letting AlloyDB Omni [manage](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/maintain-vector-indexes#maintain-index-automatically) and tune the index structure. If you need granular control over index tuning, create a manually-tuned ScaNN index.

Automatically-tuned indexes can be optimized in two ways:

  * (Default) Vector search recall and latency at the cost of index build time
  * Balance index build time and search performance

**Note:** To create an automatically-tuned ScaNN index on a table with fewer than 10,000 rows, you can use deferred index creation and explicitly specify `WITH (MODE='AUTO')`. The index build is deferred until the table reaches 10,000 rows.

To create an automatically-tuned ScaNN index, run the following command.
    
    
    CREATE INDEX INDEX_NAME ON TABLE
           USING scann (EMBEDDING_COLUMN DISTANCE_FUNCTION)
    WITH (MODE='AUTO');
    

Replace the following:

  * `INDEX_NAME`: name of the index that you want to create. For example, `my_scann_index`. Index names are shared across your database. Verify that each index name is unique to each table in your database.

  * `TABLE`: table to add the index to.

  * `EMBEDDING_COLUMN`: column that stores `vector` data.

  * `DISTANCE_FUNCTION`: distance function to use with this index. Choose one of the following:

    * L2 distance: `l2`

    * Dot product: `dot_product`

    * Cosine distance: `cosine`




This command creates a ScaNN index that is optimized for search performance. If you want to change this setting, run the following command:
    
    
    CREATE INDEX INDEX_NAME ON TABLE
           USING scann (EMBEDDING_COLUMN DISTANCE_FUNCTION)
    WITH (MODE='AUTO',
          OPTIMIZATION='OPTIMIZATION');
    

Replace the following:

  * `INDEX_NAME`: name of the index that you want to create. For example, `my_scann_index`. Index names are shared across your database. Verify that each index name is unique to each table in your database.

  * `TABLE`: table to add the index to.

  * `EMBEDDING_COLUMN`: column that stores `vector` data.

  * `DISTANCE_FUNCTION`: distance function to use with this index. Choose one of the following:

    * L2 distance: `l2`

    * Dot product: `dot_product`

    * Cosine distance: `cosine`

  * (Optional) `OPTIMIZATION`: set to one of the following:

    * (Default) `SEARCH_OPTIMIZED`: optimize both vector search recall and vector search latency at the cost of longer index build times.

    * `BALANCED`: balance index build time and search performance.

If `OPTIMIZATION` is set, `MODE='AUTO'` must also be included.




## Create a manually-tuned index

If your application has specific requirements for recall and index build times, you can manually create and tune the ScaNN index.

To manually create a ScaNN index for a column containing stored vector embeddings, see the following commands.

### Two-level tree index
    
    
    CREATE INDEX INDEX_NAME ON TABLE
           USING scann (EMBEDDING_COLUMN DISTANCE_FUNCTION)
    WITH (mode='MANUAL',
          num_leaves=NUM_LEAVES_VALUE,
          quantizer=QUANTIZER);

  * `INDEX_NAME`: name of the index you want to create. For example, `my_scann_index`. The index names are shared across your database. Ensure that each index name is unique to each table in your database. 
  * `TABLE`: table to add the index to. 
  * `EMBEDDING_COLUMN`: column that stores `vector` data. 
  * `DISTANCE_FUNCTION`: distance function to use with this index. Choose one of the following: 
    * L2 distance: `l2`
    * Dot product: `dot_product`
    * Cosine distance: `cosine`
  * `NUM_LEAVES_VALUE`: number of partitions to apply to this index. Set to any value between 1 and 100 million for PostgreSQL 17 and higher, or between 1 and 30 million for PostgreSQL 16 and lower. For more information about how to choose this value, see [Tune a `ScaNN` index](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/tune-indexes). 
  * `QUANTIZER`: type of quantizer to use. Note that the ScaNN index can be loaded into the [columnar engine](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/columnar-engine/overview) to further accelerate the vector search. Choose one of the following: 
    * (Default) `SQ8`: provides a balance of query performance with minimal recall loss. This is typically less than 1-2%. 
    * ([Preview](https://cloud.google.com/products#product-launch-stages)) `AH`: Asymmetric hashing (AH) is up to 4x compressed when compared with `SQ8`. For potentially better query performance when the columnar engine is [enabled](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/columnar-engine/configure#enable) and the index and table data are populated into the columnar engine, consider this for potentially better query performance. For more information, see [Best practices for tuning ScaNN](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/best-practices-tuning-scann). 
    * `FLAT`: provides the highest recall, 99% or higher, at the cost of search performance. 



### Three-level tree index
    
    
    CREATE INDEX INDEX_NAME ON TABLE
           USING scann (EMBEDDING_COLUMN DISTANCE_FUNCTION)
    WITH (mode='MANUAL',
          num_leaves=NUM_LEAVES_VALUE,
          quantizer=QUANTIZER,
          max_num_levels = 2);

  * `INDEX_NAME`: name of the index you want to create. For example, `my_scann_index`. The index names are shared across your database. Ensure that each index name is unique to each table in your database. 
  * `TABLE`: table to add the index to. 
  * `EMBEDDING_COLUMN`: column that stores `vector` data. 
  * `DISTANCE_FUNCTION`: distance function to use with this index. Choose one of the following: 
    * L2 distance: `l2`
    * Dot product: `dot_product`
    * Cosine distance: `cosine`
  * `NUM_LEAVES_VALUE`: number of partitions to apply to this index. Set to any value between 1 and 100 million for PostgreSQL 17 and higher, or between 1 and 30 million for PostgreSQL 16 and lower. For more information about how to choose this value, see [Tune a `ScaNN` index](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/tune-indexes). 
  * `QUANTIZER`: type of quantizer to use. Note that the ScaNN index can be loaded into the columnar engine to further accelerate the vector search. Choose one of the following: 
    * (Default) `SQ8`: provides a balance of query performance with minimal recall loss. This is typically less than 1-2%. 
    * ([Preview](https://cloud.google.com/products#product-launch-stages)) `AH`: Asymmetric hashing (AH) is up to 4x compressed when compared with `SQ8`. For potentially better query performance when the columnar engine is [enabled](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/columnar-engine/configure#enable) and the index and table data are populated into the columnar engine, consider this for potentially better query performance. For more information, see [Best practices for tuning ScaNN](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/best-practices-tuning-scann). 
    * `FLAT`: provides the highest recall, 99% or higher, at the cost of search performance. 
  * `max_num_levels = 2`: the maximum number of centroid levels of the K-means clustering tree. Set this parameter to `2` to create a three-level index. 



### Four-level tree index

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
    
    
    CREATE INDEX INDEX_NAME ON TABLE
           USING scann (EMBEDDING_COLUMN DISTANCE_FUNCTION)
    WITH (mode='MANUAL',
          num_leaves=NUM_LEAVES_VALUE,
          quantizer=QUANTIZER,
          auto_maintenance=AUTO_MAINTENANCE,
          max_num_levels = 3);

  * `INDEX_NAME`: name of the index you want to create. For example, `my_scann_index`. The index names are shared across your database. Ensure that each index name is unique to each table in your database. 
  * `TABLE`: table to add the index to. 
  * `EMBEDDING_COLUMN`: column that stores `vector` data. 
  * `DISTANCE_FUNCTION`: distance function to use with this index. Choose one of the following: 
    * L2 distance: `l2`
    * Dot product: `dot_product`
    * Cosine distance: `cosine`
  * `NUM_LEAVES_VALUE`: number of partitions to apply to this index. Set to any value between 1 and 100 million for PostgreSQL 17 and higher, or between 1 and 30 million for PostgreSQL 16 and lower. For more information about how to choose this value, see [Tune a `ScaNN` index](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/tune-indexes). 
  * `QUANTIZER`: type of quantizer to use. Note that the ScaNN index can be loaded into the columnar engine to further accelerate the vector search. Choose one of the following: 
    * (Default) `SQ8`: provides a balance of query performance with minimal recall loss. This is typically less than 1-2%. 
    * [Preview](https://cloud.google.com/products#product-launch-stages) `AH`: Asymmetric hashing (AH) is up to 4x compressed when compared with `SQ8`. For potentially better query performance when the columnar engine is [enabled](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/columnar-engine/configure#enable) and the index and table data are populated into the columnar engine, consider this for potentially better query performance. For more information, see [Best practices for tuning ScaNN](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/best-practices-tuning-scann). 
    * `FLAT`: provides the highest recall, 99% or higher, at the cost of search performance. 
  * (Optional) `AUTO_MAINTENANCE`: controls whether automatic maintenance on the index is enabled or disabled. For more information on automatic maintenance, see [Maintain vector indexes](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/maintain-vector-indexes#maintain-index-automatically). 
    * (Default) `ON`: AlloyDB Omni enables automatic maintenance on the index. 
    * `OFF`: AlloyDB Omni disables automatic maintenance on the index. 
  * `max_num_levels = 3`: the maximum number of centroid levels of the K-means clustering tree. Set this parameter to `3` to create a four-level index. 



## Convert a manually-tuned index to an automatically-tuned index

To convert a manually-tuned index to an automatically-tuned index, complete the following steps:

  1. Reset all query parameters defined for your manually-tuned index.
         
         ALTER INDEX INDEX_NAME RESET (PARAMETER_NAME);
         

Replace the following variables:

     * `INDEX_NAME`: name of the index that you want to convert. For example, `my_scann_index`. Index names are shared across your database. Verify that each index name is unique to each table in your database.

     * `PARAMETER_NAME`: comma-separated list containing the names of the query parameters you want to reset. For example, `num_leaves, quantization`.

Note that you must reset all other query parameters before resetting `num_leaves`.

  2. Reindex your manually-tuned index to convert it to an automatically-tuned index.
         
         REINDEX INDEX CONCURRENTLY INDEX_NAME;
         




## Create a ScaNN index for `real[]` data types

To create an index for an embedding column that uses the `real[]` data type instead of `vector`, cast the column into the `vector` data type:
    
    
    CREATE INDEX INDEX_NAME ON TABLE
    USING scann (CAST(EMBEDDING_COLUMN AS vector(DIMENSIONS)) DISTANCE_FUNCTION);
    

Replace the following:

  * `INDEX_NAME`: name of the index that you want to create. For example, `my_scann_index`. Index names are shared across your database. Verify that each index name is unique to each table in your database.

  * `TABLE`: table to add the index to.

  * `DIMENSIONS`: the number of dimensions that the model supports.

  * `EMBEDDING_COLUMN`: column that stores `vector` data.

  * `DISTANCE_FUNCTION`: distance function to use with this index. Choose one of the following:

    * L2 distance: `l2`

    * Dot product: `dot_product`

    * Cosine distance: `cosine`




## View indexing progress

To view the indexing progress, use the `pg_stat_progress_create_index` view:
    
    
    SELECT * FROM pg_stat_progress_create_index;
    

The `phase` column shows the current state of your index creation. After the index building phase is complete, the row for the index isn't visible.

## Create a deferred index for empty tables or tables with insufficient rows

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, you can't create a ScaNN index on a table that is empty or has fewer rows than the value of the `num_leaves` index option.

To bypass this limitation, enable deferred index creation to let AlloyDB Omni defer index creation until the number of rows in the table reaches the threshold that `num_leaves` defines. After the threshold is met, AlloyDB Omni starts the index build in the background.

This deferred operation is a non-blocking process, allowing other database operations like reads and writes to continue without interruption. Because the index rebuild happens in the background, deferred index creation is suitable when tables ingest data rows in small batches. The index rebuild is automatically triggered after the number of rows reaches the threshold.

However, if you are planning to insert large number of rows into the table in a single transaction, we recommend that you split the transaction into multiple transactions or that you generate a ScaNN index without enabling deferred index creation.

**Note:** To use deferred index creation on an empty or nearly empty table, make sure that the `scann.allow_blocked_operations` flag used to force index creation is set to `off` on the database. If this flag is enabled, it overrides the deferred index creation feature.

### Enable deferred index creation

To enable deferred index creation, follow these steps:

  1. Make sure that the `scann.enable_index_maintenance` flag and one of the following flags are enabled:

     * [`scann.enable_preview_features`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/alloydb-flags#scann.enable_preview_features): this flag also enables other preview features.
     * [`scann.enable_index_with_insufficient_data`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/alloydb-flags#scann.enable_index_with_insufficient_data): this flag explicitly enables only the deferred index creation feature.

For more information about configuring database flags on your AlloyDB Omni instance, see [Configure database parameters](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-database-parameters).

  2. Create a ScaNN index. If you create an index in automatic mode on a table with fewer than 10,000 rows, you must explicitly specify `WITH (MODE='AUTO')`. For more information, see Create an automatically-tuned index. If you create an index in manual mode, make sure that the `auto_maintenance` parameter is set to `on`. For more information, see Create a manually-tuned index.




### Limitations

  * The automatic index creation background process uses database-level flag values. Even if you set any session-level flags using the `SET LOCAL` command, the process considers the flag value set at the database-level.
  * If you plan to bulk insert a large amount of data into an empty table in a single transaction, we recommend that you run the single insert transaction and then create a ScaNN index.



## Force index creation on empty or small tables

AlloyDB Omni uses validations to prevent the creation of a ScaNN index on an empty table or a table with very few rows for the following reasons:

  * ScaNN index trains on insufficient data. This can result in poor recall for vector similarity searches.

  * Write performance to the database might degrade.




We recommend that you defer index creation in suboptimal performance.

However, in some development or testing scenarios, you might need to create an index on an empty or small table. In these cases, you can enforce index creation. Note that forcing index creation requires `SUPERUSER` privileges.

To force index creation, complete the following steps:

  1. Set the `scann.allow_blocked_operations` session-level parameter to `true` on the database:
         
         SET scann.allow_blocked_operations = true;
         

  2. If the user you're using to run these queries doesn't have `SUPERUSER` privileges, assign them:
         
         CREATE USER USERNAME WITH SUPERUSER PASSWORD PASSWORD;
         

Replace the following variables:

     * `USERNAME`: name of the user you want to grant `SUPERUSER` privileges to.

     * `PASSWORD`: user's password.




## Build indexes in parallel

To build your index faster, AlloyDB Omni might automatically spawn multiple parallel workers depending on your dataset and the type of index that you choose. This often triggers when creating a three or four-level ScaNN index or if your dataset exceeds 100 million rows.

Though AlloyDB Omni automatically optimizes the number of parallel workers, you can tune the parallel workers using the following PostgreSQL query planning parameters:

  * [`max_parallel_maintenance_workers`](https://www.postgresql.org/docs/18/runtime-config-resource.html#GUC-MAX-PARALLEL-MAINTENANCE-WORKERS)
  * [`max_parallel_workers`](https://www.postgresql.org/docs/18/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS)
  * [`min_parallel_table_scan_size`](https://www.postgresql.org/docs/18/runtime-config-query.html#GUC-MIN-PARALLEL-TABLE-SCAN-SIZE)



To avoid out-of-memory issues when you create the ScaNN index, ensure that the [`maintenance_work_mem`](https://www.postgresql.org/docs/18/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM) and [`shared_buffers`](https://www.postgresql.org/docs/18/runtime-config-resource.html#GUC-SHARED-BUFFERS) database flags are set to a value less than the total machine memory.

## Run a query

After you store and index the embeddings in your database, you can start querying your data. You cannot run bulk search queries using the `alloydb_scann` extension.

To find the nearest semantic neighbors for a text string, you can use the `google_ml.embedding()` function to translate the text into a vector.

Because `google_ml.embedding()` returns a real array, you must explicitly cast the function call to `vector` before applying it to one of the nearest-neighbor operators, for example, `<->` for L2 distance. These operators can then use the ScaNN index to find the database rows with the most semantically similar embeddings.
    
    
    SELECT * FROM TABLE
    ORDER BY EMBEDDING_COLUMN DISTANCE_FUNCTION_QUERY
      google_ml.embedding(
          model_id => 'MODEL_ID',
          content => 'CONTENT')::vector
    LIMIT ROW_COUNT;
    

Replace the following variables:

  * `TABLE`: table containing the embedding to compare the text to.

  * `EMBEDDING_COLUMN`: column containing the stored embeddings.

  * `DISTANCE_FUNCTION_QUERY`: distance function to use with this query. Choose the query equivalent for the distance function when you created the index:

    * L2 distance: `<->`

    * Inner product: `<#>`

    * Cosine distance: `<=>`

  * `MODEL_ID`: ID of the registered embedding model you want to use.

  * `CONTENT`: the text string you want to translate into an embedding and search for.

  * `ROW_COUNT`: number of rows to return. For example, specify `1` if you want the single, best match.




## What's next

* [Run vector similarity searches](/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/run-vector-similarity-search) 

  * [Tune vector query performance](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/tune-indexes)

* [Vector index metrics](/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/omni-metrics) 
  * [Learn how to build a smart shopping assistant with AlloyDB, pgvector, and model endpoint management](https://codelabs.developers.google.com/smart-shop-agent-alloydb#0).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
