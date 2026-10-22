---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/tune-indexes/
title: Tune vector query performance \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:56:13.479149+00:00
---

# Tune vector query performance  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/tune-indexes/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)



Send feedback 

#  Tune vector query performance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/ai/tune-indexes)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/ai/tune-indexes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/tune-indexes)



This document describes how to tune your indexes to achieve faster query performance and better recall in AlloyDB Omni.

ScaNN IVF IVFFlat HNSW

**Caution:** The `postgres_ann` extension is renamed to `alloydb_scann`. Before you upgrade to AlloyDB Omni, you must drop any indexes created using the older `postgres_ann` version. Next, upgrade AlloyDB Omni, and then create the indexes again using the `alloydb_scann` extension. This applies only to AlloyDB Omni.

## Before you begin

Before you build a `ScaNN` index, complete the following:

  * Make sure that a table with your data is already created.
  * To avoid issues while generating the index, make sure that the value you set for the `maintenance_work_mem` and the `shared_buffers` flag is less than total machine memory.
  * To use four-level indexes, you must first enable the [Preview](https://cloud.google.com/products#product-launch-stages) feature for your instance. To enable the Preview feature, choose one of the following two methods: 
    * Enable the [`scann.enable_preview_features`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/alloydb-flags#scann.enable_preview_features) database flag.
    * Set the session-level [`scann.max_allowed_num_levels`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/alloydb-flags#scann.max_allowed_num_levels) database flag to `3`. `sql SET scann.max_allowed_num_levels = 3;`



## Tune a `ScaNN` index

Use the following guidance to determine the number of levels needed for your ScaNN index:

  * For 0 to 10 million rows: Choose a two-level index.
  * For 10 million to 100 million rows: 
    * To prioritize search recall, choose a two-level index.
    * To prioritize index build time, choose a three-level index.
  * For 100 million to 1 billion rows: 
    * To prioritize search recall, choose a three-level index.
    * To prioritize index build time, choose a four-level index (in [Preview](https://cloud.google.com/products#product-launch-stages)).
  * For 1 billion to 10 billion rows: Choose a four-level index (in [Preview](https://cloud.google.com/products#product-launch-stages)).



Consider the following examples for two-level, three-level, and four-level `ScaNN` indexes that show how tuning parameters are set for a table with 1,000,000 rows:

### Two-level index

```sql \-- Setting num_leaves to 1000 as power(1000000, 1/2) for two-level index BEGIN; SET LOCAL maintenance_work_mem = '300MB'; CREATE INDEX my_scann_index ON my_table USING scann (vector_column cosine) WITH (num_leaves = 1000); END; ``` 

### Three-level index

```sql \-- Setting num_leaves to 10000 as power(1000000, 2/3) for three-level index BEGIN; SET LOCAL maintenance_work_mem = '3000MB'; CREATE INDEX my_scann_index ON my_table USING scann (vector_column cosine) WITH (num_leaves = 10000, max_num_levels = 2); END; ``` 

### Four-level index (Preview)

```sql \-- Setting num_leaves to 31623 as power(1000000, 3/4) for four-level index BEGIN; SET LOCAL maintenance_work_mem = '9300MB'; CREATE INDEX my_scann_index ON my_table USING scann (vector_column cosine) WITH (num_leaves = 31623, max_num_levels = 3); END; ``` 

### Handle DML invalidations due to acceleration with columnar engine

If you chose to [accelerate your vector searches with the columnar engine](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/accelerate-with-ce), be aware that DML and DDL invalidations on the base tables can impact vector query performance. In case of high DML throughput, consider tuning the `google_columnar_engine.refresh_threshold_percentage` database flag or manually refreshing the index using the `google_columnar_engine_refresh_index` command.

## Analyze your queries

Use the `EXPLAIN ANALYZE` command to analyze your query insights as shown in the following example SQL query.
    
    
      EXPLAIN ANALYZE SELECT result_column
      FROM my_table
      ORDER BY EMBEDDING_COLUMN <=> embedding('text-embedding-005', 'What is a database?')::vector
      LIMIT 1;
    

The example response `QUERY PLAN` includes information such as the time taken, the number of rows scanned or returned, and the resources used.
    
    
    Limit  (cost=0.42..15.27 rows=1 width=32) (actual time=0.106..0.132 rows=1 loops=1)
      ->  Index Scan using my_scann_index on my_table  (cost=0.42..858027.93 rows=100000 width=32) (actual time=0.105..0.129 rows=1 loops=1)
            Order By: (embedding_column <=> embedding('text-embedding-005', 'What is a database?')::vector(768))
            Limit value: 1
    Planning Time: 0.354 ms
    Execution Time: 0.141 ms
    

## View vector index metrics

You can use the vector index metrics to review performance of your vector index, identify areas for improvement, and tune your index based on the metrics, if needed.

To view all vector index metrics, run the following SQL query, which uses the `pg_stat_ann_indexes` view:
    
    
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
    

For more information about the complete list of metrics, see [Vector index metrics](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/vector-index-metrics).

## What's next

  * [Create a ScaNN index](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/create-scann-index)
  * [Best practices for tuning ScaNN indexes](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/best-practices-tuning-scann)
  * See [an example embedding workflow](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/example-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
