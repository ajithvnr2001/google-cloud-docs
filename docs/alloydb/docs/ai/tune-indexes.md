---
url: https://docs.cloud.google.com/alloydb/docs/ai/tune-indexes/
title: Tune vector query performance in AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:24:46.113994+00:00
---

# Tune vector query performance in AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/tune-indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Tune vector query performance in AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

Tuning your vector indexes in AlloyDB for PostgreSQL lets you optimize query execution speed and search recall for your vector search workloads. You can adjust index build and query parameters for ScaNN, IVF, IVFFlat, and HNSW indexes to match your dataset size and performance requirements.

ScaNN IVF IVFFlat HNSW

## Before you begin

Before you build a ScaNN index, complete the following:

  * [Create a table](https://docs.cloud.google.com/alloydb/docs/database-create) with your data.

  * To avoid out-of-memory issues when you create the ScaNN index, ensure that the [`maintenance_work_mem`](https://www.postgresql.org/docs/17/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM) and [`shared_buffers`](https://www.postgresql.org/docs/17/runtime-config-resource.html#GUC-SHARED-BUFFERS) database flags are set to a value less than the total machine memory.

  * To use four-level indexes, you must first enable the [Preview](https://cloud.google.com/products#product-launch-stages) feature for your AlloyDB instance. To enable the Preview feature, choose one of the following two methods:

    * Enable the [`scann.enable_preview_features`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#scann.enable_preview_features) database flag.

For more information on configuring database flags, see [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

    * Set the session-level [`scann.max_allowed_num_levels`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#scann.max_allowed_num_levels) database flag to `3`.
          
          SET scann.max_allowed_num_levels = 3;
          




## Tune a ScaNN index

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To determine the number of levels needed for your ScaNN index, see the following table.

Number of vector rows in your table | Number of levels for your ScaNN index  
---|---  
[0..10 million] | Two  
[10 million..100 million] |  Choose one of the following metrics to prioritize:

  * Search recall: two
  * Index build time: three

  
[100 million..1 billion] |  Choose one of the following metrics to prioritize:

  * Search recall: three
  * Index build time: four (in [Preview](https://cloud.google.com/products#product-launch-stages)) 

  
[1 billion..10 billion] |  Four (in [Preview](https://cloud.google.com/products#product-launch-stages))   
  
Use the following ScaNN indexes as examples for tuning parameters for a table with 1 million rows.

### Two-level tree index
    
    
    SET LOCAL scann.num_leaves_to_search = 1;
    SET LOCAL scann.pre_reordering_num_neighbors=50;
    
    CREATE INDEX my_scann_index ON my_table
           USING scann (vector_column cosine)
    WITH (num_leaves = [power(1000000, 1/2)]);

### Three-level tree index
    
    
    SET LOCAL scann.num_leaves_to_search = 10;
    SET LOCAL scann.pre_reordering_num_neighbors=50;
    
    CREATE INDEX my_scann_index ON my_table
           USING scann (vector_column cosine)
    WITH (num_leaves = [power(1000000, 2/3)], max_num_levels = 2);

### Four-level tree index
    
    
    SET LOCAL scann.num_leaves_to_search = 100;
    SET LOCAL scann.pre_reordering_num_neighbors=50;
    
    CREATE INDEX my-scann-index ON my-table
           USING scann (vector_column cosine)
    WITH (num_leaves = [power(1000000, 3/4)], max_num_levels = 3);

For more information about ScaNN indexes, see the following pages:

  * [Create a ScaNN index](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index)
  * [Best practices for tuning ScaNN indexes](https://docs.cloud.google.com/alloydb/docs/ai/best-practices-tuning-scann)



### Handle DML invalidations due to acceleration with columnar engine

If you chose to [accelerate your vector searches with the columnar engine](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-with-ce), be aware that DML and DDL invalidations on the base tables can impact vector query performance. In case of high DML throughput, consider tuning the `google_columnar_engine.refresh_threshold_percentage` database flag or manually refreshing the index using the `google_columnar_engine_refresh_index` command.

## Analyze your queries

Use the `EXPLAIN ANALYZE` command to analyze your query insights as shown in the following example SQL query.
    
    
      EXPLAIN ANALYZE SELECT result-column
      FROM my_table
      ORDER BY EMBEDDING_COLUMN <-> embedding('text-embedding-005', 'What is a database?')::vector
      LIMIT 1;
    

The example response `QUERY PLAN` includes information such as the time taken, the number of rows scanned or returned, and the resources used.
    
    
    Limit  (cost=0.42..15.27 rows=1 width=32) (actual time=0.106..0.132 rows=1 loops=1)
      ->  Index Scan using my_scann_index on my_table  (cost=0.42..858027.93 rows=100000 width=32) (actual time=0.105..0.129 rows=1 loops=1)
            Order By: (embedding_column <-> embedding('text-embedding-005', 'What is a database?')::vector(768))
            Limit value: 1
    Planning Time: 0.354 ms
    Execution Time: 0.141 ms
    

## View vector index metrics

You can use vector index metrics to review performance of your vector index, identify areas for improvement, and tune your index based on the metrics, if needed. The `pg_stat_ann_indexes` view helps you understand the state of index utilization while the `pg_stat_ann_index_creation` view provides information about rows created at the time of index creation.

To view index utilization metrics, run the following command:
    
    
    SELECT * FROM pg_stat_ann_indexes;
    

You see output similar to the following:
    
    
    -[ RECORD 1 ]----------+---------------------------------------------------------------------------
    relid                  | 271236
    indexrelid             | 271242
    schemaname             | public
    relname                | t1
    indexrelname           | t1_ix1
    indextype              | scann
    indexconfig            | {num_leaves=100,max_num_levels=1,quantizer=SQ8}
    indexsize              | 832 kB
    indexscan              | 0
    insertcount            | 250
    deletecount            | 0
    updatecount            | 0
    partitioncount         | 100
    distribution           | {"average": 3.54, "maximum": 37, "minimum": 0, "outliers": [37, 12, 11, 10, 10, 9, 9, 9, 9, 9]}
    distributionpercentile |{"10": { "num_vectors": 0, "num_partitions": 0 }, "25": { "num_vectors": 0, "num_partitions": 30 }, "50": { "num_vectors": 3, "num_partitions": 30 }, "75": { "num_vectors": 5, "num_partitions": 19 }, "90": { "num_vectors": 7, "num_partitions": 11 }, "95": { "num_vectors": 9, "num_partitions": 5 }, "99": { "num_vectors": 12, "num_partitions": 4 }, "100": { "num_vectors": 37, "num_partitions": 1 }}
    

To view number of rows created at the time of index creation, run the following command:
    
    
    SELECT * FROM pg_stat_ann_index_creation;
    

You see output similar to the following:
    
    
    -[ RECORD 1 ]----------+---------------------------------------------------------------------------
    relid                         | 271236
    indexrelid                    | 271242
    schemaname                    | public
    relname                       | t1
    indexrelname                  | t1_ix1
    index_rows_at_creation_time   | 262144
    

For more information about the complete list of metrics, see [Vector index metrics](https://docs.cloud.google.com/alloydb/docs/reference/vector-index-metrics).

## What's next

  * [Maintain vector indexes](https://docs.cloud.google.com/alloydb/docs/ai/maintain-vector-indexes).
  * Learn about an [example embedding workflow](https://docs.cloud.google.com/alloydb/docs/ai/example-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
