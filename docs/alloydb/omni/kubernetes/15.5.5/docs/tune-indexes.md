---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/tune-indexes/
title: Tune vector query performance \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:04.733227+00:00
---

# Tune vector query performance  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/tune-indexes/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  Tune vector query performance Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/tune-indexes)



This document shows you how to tune your indexes to achieve faster query performance and better recall.

**Caution:** The `postgres_ann` extension is renamed to `alloydb_scann`. Before you upgrade to AlloyDB Omni, you must drop any indexes created using the older `postgres_ann` version. Next, upgrade AlloyDB Omni, and then create the indexes again using the `alloydb_scann` extension. This applies only to AlloyDB Omni.

## Tune a `ScaNN` index

**Preview — AlloyDB ScaNN index**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

ScaNN index uses tree-quantization based indexing. In Tree-quantization techniques, indexes learn a search tree together with a quantization (or hashing) function. When you run a query, the search tree is used to prune the search space while quantization is used to compress the index size. This pruning speeds up the scoring of the similarity (i.e., distance) between the query vector and the database vectors.

To achieve both a high query-per-second rate (QPS) and a high recall with your nearest-neighbor queries, you must partition the tree of your `ScaNN` index in a way that is most appropriate to your data and your queries.

Before you build a `ScaNN` index, complete the following:

  * Make sure that a table with your data is already created.
  * Make sure that the value you set for the `maintenance_work_mem` and the `shared_buffers` flag is less than total machine memory to avoid issues while generating the index.



### Tuning parameters

The following index parameters and database flags are used together to find the right balance of recall and QPS. All the parameters apply to both `ScaNN` index types.

Parameter typeIndex creationQuery runtime

Tuning parameter | Description | Parameter type  
---|---|---  
`num_leaves` | The number of partitions to apply to this index. The number of partitions you apply to when creating an index affects the index performance. By increasing partitions for a set number of vectors, you create a more fine-grained index, which improves recall and query performance. However, this comes at the cost of longer index creation times.  
  
Since three-level trees build faster than two-level trees, you can increase the `num_leaves_value` when creating a three-level tree index to achieve better performance.  


  * **Two-level index** : Set this value to any value between `1` and `1048576`.  
  
If you are unsure about selecting the exact value, use `sqrt(ROWS)` as a starting point, where `ROWS` is the number of vector rows. The number of vectors that each partition holds is calculated by   
`ROWS/sqrt(ROWS) = sqrt(ROWS)`.  
  
Since a two-level tree index can be created on a dataset with less than 10 million vector rows, each partition will hold less than (`sqrt(10M)`) vectors, which is `3200` vectors. For optimal performance, it's recommended to minimize the number of vectors in each partition.
  * **Three-level index** : Set this value to any value between `1` and `1048576`.  
  
If you are unsure about selecting the exact value, use `power(ROWS, 2/3)` as a starting point, where `ROWS` is the number of vector rows. The number of vectors that each partition holds is calculated by   
`ROWS/power(ROWS, 2/3) = power(ROWS, 1/3)`.  
  
Since a three-level tree index can be created on a dataset with vector rows more than 100 million, each partition will hold more than   
(`power(100M, 1/3)`) vectors, which is `465` vectors. For optimal performance, it's recommended to minimize the number of vectors in each partition.

| Index creation  
`quantizer` | The type of quantizer you want to use for the K-means tree. The default value is `SQ8` for better query performance.  
  
Set it to `FLAT` for better recall. | Index creation  
`enable_pca` | Enables Principal Component Analysis (PCA), which is a dimension reduction technique used to automatically reduce the size of the embedding when possible. This option is enabled by default.  
  
Set to `false` if you observe deterioration in recall. | Index creation  
`scann.num_leaves_to_search` | The database flag controls the trade off between recall and QPS. The default value is 1% of the value set in `num_leaves`.   
  
Higher the value set, better is the recall, but results in lower QPS, and the other way around. | Query runtime  
`scann.max_top_neighbors_buffer_size` | The database flag specifies the size of cache used to improve the performance for filtered queries by scoring or ranking the scanned candidate neighbors in memory instead of the disk. The default value is `20000`.   
  
Higher the value set, better is the QPS under filtered queries, but results in higher memory usage, and the other way around. | Query runtime  
`scann.pre_reordering_num_neighbors` | The database flag when set, specifies the number of candidate neighbors to consider during the reordering stages after initial search identifies a set of candidates. Set this to a value higher than the number of neighbors you want the query to return.   
  
Higher value sets result in better recall, but this approach results in lower QPS. | Query runtime  
`max_num_levels` | The maximum number of levels of the K-means clustering tree.  


  * **Two-level tree index** : Set by default for two-level tree-based quantization.
  * **Three-level tree index** : Set to `2` explicitly for three-level tree-based quantization.

| Index creation  
  
### Tune a `ScaNN` index

Consider the following examples for two-level and three-level `ScaNN` indexes that show how tuning parameters are set:

### Two-level index
    
    
    SET LOCAL scann.num_leaves_to_search = 1;
    SET LOCAL scann.pre_reordering_num_neighbors=50;
    
    CREATE INDEX my-scann-index ON my-table
      USING scann (vector_column cosine)
      WITH (num_leaves = [power(1000000, 1/2)]);
    

### Three-level index
    
    
    SET LOCAL scann.num_leaves_to_search = 10;
    SET LOCAL scann.pre_reordering_num_neighbors=50;
    
    CREATE INDEX my-scann-index ON my-table
      USING scann (vector_column cosine)
      WITH (num_leaves = [power(1000000, 2/3)], max_num_levels = 2);
    

Any insert or update operation on a table where a `ScaNN` index is already generated impacts how the learned tree optimizes the index. If your table is prone to frequent updates or insertions, then we recommend periodically reindexing the existing `ScaNN` index to improve the recall accuracy.

You can monitor index metrics to determine the amount of mutations created since the index was built, and then reindex accordingly. For more information about metrics, see [Vector index metrics](https://docs.cloud.google.com/alloydb/docs/reference/vector-index-metrics).

### Best practices for tuning

Based on the type of `ScaNN` index you plan to use, the recommendations for tuning your index vary. This section provides recommendations about how to tune index parameters for optimal balance between recall and QPS.

#### Two-level tree index

To apply recommendations to help you find the optimal values of `num_leaves` and `num_leaves_to_search` for your dataset, follow these steps:

  1. Create the `ScaNN` index with `num_leaves` set to the square root of the indexed table's row count.
  2. Run your test queries, increasing the value of `scann.num_of_leaves_to_search`, until you achieve your target recall range–for example, 95%. For more information about analyzing your queries, see Analyze your queries.
  3. Take note of the ratio between `scann.num_leaves_to_search` and `num_leaves` that will be used in subsequent steps. This ratio provides approximation around the dataset that will help you achieve your target recall.  
  
If you are working with high dimension vectors (500 dimensions or higher) and want to improve recall, then try tuning the value of `scann.pre_reordering_num_neighbors`. As a starting point, set the value to `100 * sqrt(K)` where `K` is the limit that you set in your query.
  4. If your QPS is too low after your queries achieve a target recall, then follow these steps: 
     1. Recreate the index, increasing the value of `num_leaves` and `scann.num_leaves_to_search` according to the following guidance: 
        * Set `num_leaves` to a larger factor of the square root of your row count. For example, if the index has `num_leaves` set to the square root of your row count, try setting it to double the square root. If the value is already double, then try setting it to triple the square root.
        * Increase `scann.num_leaves_to_search` as needed to maintain its ratio with `num_leaves`, which you noted in Step 3.
        * Set `num_leaves` to a value less than or equal to the row count divided by 100.
     2. Run the test queries again. While you're running the test queries, experiment with reducing `scann.num_leaves_to_search`, finding a value that increases QPS while keeping your recall high. Try different values of `scann.num_leaves_to_search` without rebuilding the index.
  5. Repeat Step 4 until both the QPS and the recall range have reached acceptable values.



#### Three-level tree index

In addition to the recommendations for the two-level tree `ScaNN` index, use the following guidance and the steps to tune the index:

  * Increasing the `max_num_levels` from `1` for a two-level tree to `2` for a three-level tree significantly reduces the time to create an index, but at the expense of recall accuracy. Set `max_num_levels` using the following recommendation: 
    * Set the value to `2` if the number of vector rows exceeds 100 million rows.
    * Set the value to `1` if the number of vector rows are less than 10 million rows.
    * Set to either `1` or `2` if the number of vector rows lie between 10 million and 100 million rows, based on balance of index creation time and the recall accuracy you need.



To apply recommendations to find the optimal value of `num_leaves` and `max_num_levels` index parameters, follow these steps:

  1. Create the `ScaNN` index with the following `num_leaves` and `max_num_levels` combinations based on your dataset:

     * **vector rows greater than 100 million rows** : Set `max_num_levels` as `2` and `num_leaves` as `power(rows, ⅔)`.
     * **vector rows less than 100 million rows** : Set `max_num_levels` as `1` and `num_leaves` as `sqrt(rows)`.
     * **vector rows between 10 million and 100 million rows** : Start by setting `max_num_levels` as `1` and `num_leaves` as `sqrt(rows)`.
  2. Run your test queries. For more information about analyzing queries, see Analyze your queries.

If the index creation time is satisfactory, then retain the `max_num_levels` value, and experiment with the `num_leaves` value for optimal recall accuracy.

  3. If you aren't satisfied with the index creation time, then do the following:

     * If `max_num_levels` value is `1`, then drop the index. Rebuild the index with `max_num_levels` value set to `2`.

Run the queries and tune the `num_leaves` value for optimal recall accuracy.

     * If the `max_num_levels` value is `2`, then drop the index. Rebuild the index with the same `max_num_levels` value and tune the `num_leaves` value for optimal recall accuracy.




## Tune an `IVF` index

Tuning the values you set for the `lists`, `ivf.probes`, and the `quantizer` parameters might help optimize your application's performance:

Tuning parameter | Description | Parameter type  
---|---|---  
`lists` | The number of lists created during index building. The starting point for setting this value is `(rows)/1000` for up to one million rows, and `sqrt(rows)` for more than one million rows. | Index creation  
`quantizer` | The type of quantizer you want to use for the K-means tree. The default value is `SQ8` for better query performance. Set it to `FLAT` for better recall. | Index creation  
`ivf.probes` | the number of nearest lists to explore during search. The starting point for this value is   
`sqrt(lists)`. | Query runtime  
  
Consider the following example that shows an `IVF` index with the tuning parameters set:
    
    
    SET LOCAL ivf.probes = 10;
    
    CREATE INDEX my-ivf-index ON my-table
      USING ivf (vector_column cosine)
      WITH (lists = 100, quantizer = 'SQ8');
    

## Tune an `IVFFlat` index

Tuning the values you set for the `lists` and the`ivfflat.probes` parameters can help optimize application performance:

Tuning parameter | Description | Parameter type  
---|---|---  
`lists` | The number of lists created during index building. The starting point for setting this value is `(rows)/1000` for up to one million rows, and `sqrt(rows)` for more than one million rows. | Index creation  
`ivfflat.probes` | The number of nearest lists to explore during search. The starting point for this value is   
`sqrt(lists)`. | Query runtime  
  
Before you build an `IVFFlat` index, make sure that your database's `max_parallel_maintenance_workers` flag is set to a value sufficient to expedite the index creation on large tables.

Consider the following example that shows an `IVFFlat` index with the tuning parameters set:
    
    
    SET LOCAL ivfflat.probes = 10;
    
    CREATE INDEX my-ivfflat-index ON my-table
      USING ivfflat (vector_column cosine)
      WITH (lists = 100);
    

## Tune an `HNSW` index

Tuning the values you set for the `m`, `ef_construction`, and the `hnsw.ef_search` parameters can help optimize application performance.

Tuning parameter | Description | Parameter type  
---|---|---  
`m` | The maximum number of connections per from a node in the graph. You can start with the default value as `16`(default) and experiment with higher values based on the size of your dataset. | Index creation  
`ef_construction` | The size of the dynamic candidate list maintained during graph construction, which constantly updates the current best candidates for nearest neighbors for a node. Set this value to any value higher than twice of the `m` value—for example, `64`(default). | Index creation  
`ef_search` | The size of the dynamic candidate list used during search. You can start setting this value to either `m` or `ef_construction`, and then change it while observing the recall. The default value is `40`. | Query runtime  
  
Consider the following example that shows an `hnsw` index with the tuning parameters set:
    
    
    SET LOCAL hnsw.ef_search = 40;
    
    CREATE INDEX my-hnsw-index ON my-table
      USING hnsw (vector_column cosine)
      WITH (m = 16, ef_construction = 200);
    

## Analyze your queries

Use the `EXPLAIN ANALYZE` command to analyze your query insights as shown in the following example SQL query.
    
    
      EXPLAIN ANALYZE SELECT result-column FROM my-table
        ORDER BY EMBEDDING_COLUMN ::vector
        USING INDEX my-scann-index
        <-> embedding('textembedding-gecko@003', 'What is a database?')
        LIMIT 1;
    

The example response `QUERY PLAN` includes information such as the time taken, the number of rows scanned or returned, and the resources used.
    
    
    Limit  (cost=0.42..15.27 rows=1 width=32) (actual time=0.106..0.132 rows=1 loops=1)
      ->  Index Scan using my-scann-index on my-table  (cost=0.42..858027.93 rows=100000 width=32) (actual time=0.105..0.129 rows=1 loops=1)
            Order By: (embedding_column <-> embedding('textgecko@003', 'What is a database?')::vector(768))
            Limit value: 1
    Planning Time: 0.354 ms
    Execution Time: 0.141 ms
    

## View vector index metrics

You can use the vector index metrics to review performance of your vector index, identify areas for improvement, and tune your index based on the metrics, if needed.

To view all vector index metrics, run the following SQL query, which uses the `pg_stat_ann_indexes` view:
    
    
    SELECT * FROM pg_stat_ann_indexes;
    

For more information about the complete list of metrics, see [Vector index metrics](https://docs.cloud.google.com/alloydb/docs/reference/vector-index-metrics).

## What's next

  * [An example embedding workflow](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/example-embeddings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
