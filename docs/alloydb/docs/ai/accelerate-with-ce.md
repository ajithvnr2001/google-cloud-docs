---
url: https://docs.cloud.google.com/alloydb/docs/ai/accelerate-with-ce/
title: Accelerate vector search with the columnar engine \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:41.627300+00:00
---

# Accelerate vector search with the columnar engine  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/accelerate-with-ce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Accelerate vector search with the columnar engine Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Columnar engine acceleration for HNSW indexes is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Acceleration for ScaNN indexes remains in [Preview](https://cloud.google.com/products#product-launch-stages).

The AlloyDB for PostgreSQL columnar engine lets you accelerate vector searches that use Scalable Nearest Neighbors (ScaNN) or Hierarchical Navigable Small World (HNSW) indexes. By caching vector indexes in a read-optimized, in-memory representation, the columnar engine serves queries directly from memory and increases queries per second (QPS) for vector search workloads.

You can only use HNSW with columnar engine for AlloyDB clusters running PostgreSQL 17 or later. ScaNN with columnar engine has no such limitation.

## Before you begin

  * Set the `google_columnar_engine.enabled` and `google_columnar_engine.enable_index_caching` database flags to `on` to enable the columnar engine and its index caching feature.
        
        gcloud alloydb instances update INSTANCE_ID \
            --database-flags google_columnar_engine.enabled=on,google_columnar_engine.enable_index_caching=on \
            --region=REGION \
            --cluster=CLUSTER_ID \
            --project=PROJECT_ID

Replace the following:

    * `INSTANCE_ID`: the ID of the instance where you want to enable the columnar engine.
    * `REGION`: the region where your instance is located—for example, `us-central1`.
    * `CLUSTER_ID`: the ID of the cluster where your instance is located.
    * `PROJECT_ID`: the ID of the project where your cluster is located.

For more information on setting flags, see [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

  * [Create a ScaNN index (Preview)](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index) or [Create an HNSW index](https://docs.cloud.google.com/alloydb/docs/ai/create-hnsw-index) in your database.




## Add an index to the columnar engine

After enabling the columnar engine, you can add an existing index to the cache using the `google_columnar_engine_add_index()` SQL function.

To add an index to the columnar engine, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. To display the cluster **Overview** page, click the name of the AlloyDB cluster in the **Resource name** column.

  3. In the navigation pane, click **AlloyDB Studio**.

  4. Sign in to **AlloyDB Studio** using the name of your database, username, and password.

  5. In the **Editor 1** tab, enter the following query:
         
         SELECT google_columnar_engine_add_index('INDEX_NAME');
         

Replace `INDEX_NAME` with the name of your vector index.

     1. Click **Run**.

**Note:** Adding an index to the columnar engine can be a long-running operation, depending on the size of the index. If this operation times out in **AlloyDB Studio** , then we recommend running this command from a [`psql` client session](https://docs.cloud.google.com/alloydb/docs/connect-psql) instead.

After you add an index to the columnar engine, all queries that use this index are automatically accelerated by the columnar engine. You can verify that your vector queries are being accelerated by the columnar engine by using the `EXPLAIN (ANALYZE, COLUMNAR_ENGINE)` plan on your query.

## Verify cache usage

To verify that your vector queries are being accelerated by the columnar engine, you can use the `EXPLAIN (ANALYZE, COLUMNAR_ENGINE)` plan on your query.

### Example ScaNN execution plan (Preview)

The following is an example of an execution plan for a query that uses an ScaNN index that has been added to the columnar engine:
    
    
    EXPLAIN (ANALYZE TRUE, SCANN TRUE, COSTS FALSE, TIMING FALSE, SUMMARY FALSE, VERBOSE FALSE, COLUMNAR_ENGINE TRUE)
    SELECT * FROM t ORDER BY val <=> '[0.5,0.5,0.5,0.5]' LIMIT 100;
    
    --This contains details about ScaNN's usage from the columnar engine. Example:
    ------------------------------------------------------------------------------------------------------
     Index Scan using scann_idx on t t_1 (actual rows=100 loops=1)
          Order By: (val <=> '[0.5,0.5,0.5,0.5]'::vector)
          Limit: 100
          ScaNN Info: (... columnar engine nodes hit=6...)
          Columnar Engine ScaNN Info: (index found=true)
    (5 rows)
    

The presence of `columnar engine nodes hit` and `Columnar Engine ScaNN Info: (index found=true)` in the output confirms that the columnar engine is used for the query.

### Example HNSW execution plan

The execution plan displays the **Columnar Engine HNSW Info** section for the respective index that shows metrics such as the ratio of elements retrieved from the columnar engine (`elements_from_ce`) and from the disk (`elements_from_disk`).

The following is an example of an execution plan for a query that uses an HNSW index that has been added to the columnar engine:
    
    
    EXPLAIN (ANALYZE, COLUMNAR_ENGINE) SELECT * FROM documents ORDER BY embedding <=> '[0.1, 0.2, 0.3, 0.4, 0.5]'::vector LIMIT 5;
    
    --This contains details about HNSW's usage from the columnar engine. Example:
    ------------------------------------------------------------------------------------------------------
     Limit (actual rows=5 loops=1)
       ->  Index Scan using hnsw_idx on documents (actual rows=5 loops=1)
             Order By: (embedding '[0.1, 0.2, 0.3, 0.4, 0.5]'::vector)
             Columnar Engine HNSW Info: (index found=true elements_from_ce=385 elements_from_disk=0)
             Columnar Check: table is not in the columnar store
    (5 rows)
    

The response shows that the index is being accelerated by the columnar engine, as all the elements were retrieved from the columnar engine (`elements_from_ce=385`) and none were retrieved from the disk (`elements_from_disk=0`).

When data modifications such as `INSERT`, `UPDATE`, or `DELETE` statements invalidate cache entries, the columnar engine uses a hybrid approach to maintain accuracy and performance. It reads valid, cached vectors directly from memory, and fetches only the modified or new vectors from disk.

If you modify a large amount of data, you might temporarily see an increase in elements_from_disk and a drop in performance until the cache refreshes.

## Manage the cached index

To manage the lifecycle of your cached indexes, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. To display the cluster **Overview** page, click the name of the AlloyDB cluster in the **Resource name** column.

  3. In the navigation pane, click **AlloyDB Studio**.

  4. Sign in to **AlloyDB Studio** using the name of your database, username, and password.

  5. In the **Editor 1** tab, enter the SQL command for your selected task:

     * To refresh the cache manually, run the following command:
           
           SELECT google_columnar_engine_refresh_index('INDEX_NAME');
           

     * To verify index status, run the following command:
           
           SELECT google_columnar_engine_verify('INDEX_NAME');
           

     * To drop the index from the cache, run the following command:
           
           SELECT google_columnar_engine_drop_index('INDEX_NAME');
           

     * To view active indexes, run the following command:
           
           SELECT * FROM g_columnar_indexes;
           

     * To view partitioned indexes, run the following command:
           
           SELECT * FROM g_columnar_index_partitions;
           

Replace `INDEX_NAME` with the name of your index.

  6. Click **Run**.




## Limitations

Refreshing columnar engine accelerated HNSW indexes can temporarily consume memory up to two times the index size.

## What's next

  * [Create an HNSW index](https://docs.cloud.google.com/alloydb/docs/ai/create-hnsw-index)
  * [Create a ScaNN index (Preview)](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index)
  * [Columnar engine overview](https://docs.cloud.google.com/alloydb/docs/ai/columnar-engine-overview)
  * [Manage ScaNN indexes in the columnar engine (Preview)](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-manually)
  * [Perform vector search](https://docs.cloud.google.com/alloydb/docs/ai/perform-vector-search#accelerate-filtered-vector-search)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
