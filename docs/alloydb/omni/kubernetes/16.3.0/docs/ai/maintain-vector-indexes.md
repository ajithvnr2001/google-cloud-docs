---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/maintain-vector-indexes/
title: Maintain vector indexes \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:56:42.694530+00:00
---

# Maintain vector indexes  |  AlloyDB Omni for Kubernetes: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/maintain-vector-indexes/

This page documents AlloyDB Omni version **16.3.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/overview)



Send feedback 

#  Maintain vector indexes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/maintain-vector-indexes)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/maintain-vector-indexes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/maintain-vector-indexes)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/maintain-vector-indexes)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/ai/maintain-vector-indexes)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/maintain-vector-indexes)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/maintain-vector-indexes)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/maintain-vector-indexes)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/ai/maintain-vector-indexes)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/maintain-vector-indexes)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/maintain-vector-indexes)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/maintain-vector-indexes)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/maintain-vector-indexes)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/maintain-vector-indexes)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/ai/maintain-vector-indexes)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/maintain-vector-indexes)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/maintain-vector-indexes)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/maintain-vector-indexes)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/maintain-vector-indexes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/maintain-vector-indexes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/ai/maintain-vector-indexes)

This page describes options for maintaining your vector indexes. Maintaining indexes helps to ensure that the indexes adapt to data changes that might impact the accuracy of your search results. Use the strategies on this page to avoid degradation in query performance as your dataset grows. 

## View vector index metrics

If your table is prone to frequent updates or insertions, then we recommend periodically reindexing the existing ScaNN index in order to improve the recall accuracy for your index. You can monitor index metrics to view changes in vector distributions or vector mutations since the index was built, and then reindex accordingly.

For more information about metrics, see [View vector index metrics](https://docs.cloud.google.com/alloydb/omni/16.3.0/reference/vector-index-metrics).

## Maintain indexes automatically

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use the `scann.enable_index_maintenance` Grand Unified Configuration (GUC) database flag along with the index-level `auto_maintenance` parameter while creating a ScaNN index. Using these settings together lets AlloyDB incrementally manage the index and split large outlier partitions as your dataset grows. By splitting partitions, AlloyDB tries to provide better Queries per Second (QPS) and search results.

Auto-maintenance index updates persist until AlloyDB updates the index again.

To enable AlloyDB to maintain an index automatically, add the `alloydb_scann` extension into the `shared_preload_libraries` parameter, enable the `scann.enable_index_maintenance` database flag, and then load the `alloydb_scann` extension by restarting the database:

  1. Load the `alloydb_scann` extension to the `shared_preload_libraries` list:
         
         sudo sed -r -i "s|(shared_preload_libraries\s*=\s*)'(.*)'.*$|\1'\2,alloydb_scann'|" DATA_DIR/postgresql.conf

  2. Verify that the parameter's configuration is set properly:
         
         grep -iE 'shared_preload_libraries' DATA_DIR/postgresql.conf

  3. Enable the `scann.enable_index_maintenance` flag by setting the flag in the in the `postgresql.conf` file:
         
         scann.enable_index_maintenance = ON

  4. Restart AlloyDB Omni for the parameter change to take effect:

###  Docker 
         
         docker container restart CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you started it.

###  Podman 
         
         podman container restart CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you started it.




After you enable the `scann.enable_index_maintenance` flag, you can enable auto maintenance for indexes, or you can enable the `scann_index_maintenance` function to manually invoke maintenance.

### Enable auto-maintenance during index creation

To create a ScaNN index with auto maintenance enabled, run the following example command:
    
    
    CREATE INDEX INDEX_NAME ON TABLE
      USING scann (EMBEDDING_COLUMN DISTANCE_FUNCTION)
      WITH (num_leaves=NUM_LEAVES_VALUE, auto_maintenance=on);
    

Replace the following:

  * `INDEX_NAME`: the name of the index you want to create—for example, `my-scann-index`. The index names are shared across your database. Ensure that each index name is unique to each table in your database.

  * `TABLE`: the table to add the index to.

  * `EMBEDDING_COLUMN`: a column that stores `vector` data.

  * `DISTANCE_FUNCTION`: the distance function to use with this index. Choose one of the following:

    * **L2 distance:** `l2`

    * **Dot product:** `dot_product`

    * **Cosine distance:** `cosine`

  * `NUM_LEAVES_VALUE`: the number of partitions to apply to this index. Set to any value between 1 to 1048576. For more information about how to decide this value, see [Tune a `ScaNN` index](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/tune-indexes).




### Manually invoke maintenance

If you want to invoke maintenance on a particular index on-demand, then run the following command:
    
    
    SELECT scann_index_maintenance('INDEX_NAME');
    

### Manage leaves to search for split partitions automatically

If you have enabled automatic maintenance of indexes, then AlloyDB automatically splits partitions when the `num_leaves` threshold is reached. As the number of partitions grows due to these splits, you should adjust the number of leaves to search to maintain optimal performance.

To manage the number of leaves to search automatically, use `pct_leaves_to_search`. This parameter lets you specify a percentage of number of partitions to search. If you expect your dataset to grow significantly, then start by setting the `pct_leaves_to_search` value to 1. The parameter is disabled by default.

Set this value to the percentage of current number of partitions. For example, to search 1% of of current number of partitions, set this value to `1`.   
  
You can set this parameter to any value between `0` to `100`. The default value is `0`, which disables this parameter and uses the `scann.num_leaves_to_search` to calculate the number of leaves to search.

To set the `pct_leaves_to_search` flag on your database, run the following command:
    
    
    ALTER DATABASE DATABASE_NAME SET scann.pct_leaves_to_search = PERCENTAGE_LEAVES_TO_SEARCH;
    

Replace the following:

  * `DATABASE_NAME`: the name of the database.
  * `PERCENTAGE_LEAVES_TO_SEARCH`: the percentage of `num_leaves` to search.



## Manually rebuild your index

You can manually rebuild your index if you want to rebuild it with the configurations you specified when it was created.

To manually rebuild your index, run the following command:
    
    
    REINDEX INDEX CONCURRENTLY INDEX_NAME;
    

Replace `INDEX_NAME` with the name of the index you want to rebuild—for example, `my-scann-index`. The index names are shared across your database. Ensure that each index name is unique to each table in your database.

For more information about reindexing in PostgreSQL, see [REINDEX](https://www.postgresql.org/docs/16/sql-reindex.html).

## What's next

  * [Vector index metrics](https://docs.cloud.google.com/alloydb/omni/16.3.0/reference/vector-index-metrics)
  * [Optimize vector query performance for ScaNN](https://docs.cloud.google.com/alloydb/omni/16.3.0/ai/scann-vector-query-perf-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
