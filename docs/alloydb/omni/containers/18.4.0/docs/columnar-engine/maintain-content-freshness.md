---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/columnar-engine/maintain-content-freshness/
title: Maintain freshness of in-memory column store data \u00a0|\u00a0 AlloyDB Omni using containers: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:13:08.114797+00:00
---

# Maintain freshness of in-memory column store data  |  AlloyDB Omni using containers: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/columnar-engine/maintain-content-freshness/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/overview)



Send feedback 

#  Maintain freshness of in-memory column store data Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/columnar-engine/maintain-content-freshness)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/columnar-engine/maintain-content-freshness)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/columnar-engine/maintain-content-freshness)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/columnar-engine/maintain-content-freshness)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/columnar-engine/maintain-content-freshness)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/columnar-engine/maintain-content-freshness)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/columnar-engine/maintain-content-freshness)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/columnar-engine/maintain-content-freshness)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/columnar-engine/maintain-content-freshness)

This page describes how to maintain the freshness of data in the columnar engine's column store in AlloyDB Omni in a container. 

As table rows are added, deleted, or updated, the columnar engine doesn't immediately update data in the column store. Instead, it marks affected content in the column store as invalid, and queries are planned and executed using both column-oriented data from the column store and row-oriented data from the row cache and database storage.

Over time, as more and more data blocks become invalid, query performance improvements provided by the columnar engine are reduced to the point where the columnar data needs to be refreshed to regain query performance improvements. When this _refresh threshold_ is reached, the columnar engine uses a background job to refresh the invalid data in the column store. By default, the columnar engine uses a refresh threshold of 50, indicating that given content in the column store gets marked for refresh when 50% of its content has become invalid. You can change this refresh threshold to adjust the overhead of the automatic refresh and potentially gain better ongoing query performance for your application workload.

Additionally, you can manually refresh tables and ScaNN indexes that are loaded in the columnar engine at any time. Usually, you perform a manual refresh when you want changes to a table to be reflected in the column store as soon as possible after making the changes.

## Check invalid data percentage

As your application adds, deletes, or updates rows in a table, the columnar engine marks the affected data in the column store as invalid. You can check the percentage of invalid data for your tables and materialized views by querying the `g_columnar_relations` view. This helps you decide if you need to perform a manual refresh or adjust the automatic refresh threshold.

To view the invalidation percentage for all relations in the columnar store, execute the following query:
    
    
    SELECT relation_name, invalid_percentage FROM g_columnar_relations;
    

To check the invalidation percentage for a specific table, add a `WHERE` clause to the query.
    
    
    SELECT   relation_name,
      CASE
        WHEN total_block_count > 0 THEN (invalid_block_count * 100.0 / total_block_count)
        ELSE 0.0
      END AS invalid_block_percentage
    FROM
      g_columnar_relations;
    WHERE
     relation_name =  TABLE_NAME
    

Replace `TABLE_NAME` with a string containing the name of the table or the materialized view. If the resource is in a schema other than `public`, specify the name of the schema using the format `SCHEMA_NAME.TABLE_NAME`—for example, `myschema.mytable`.

To check the invalidation percentage for a specific index, add a `WHERE` clause to the query.
    
    
    SELECT   index_name,
      CASE
        WHEN total_block_count > 0 THEN (invalid_block_count * 100.0 / total_block_count)
        ELSE 0.0
      END AS invalid_block_percentage
    FROM
      g_columnar_indexes;
    WHERE
      index_name = INDEX_NAME
    

## Change the refresh threshold of the columnar engine

To change the refresh threshold of the columnar engine, you must modify the value of the `google_columnar_engine.refresh_threshold_percentage` database flag.
    
    
    ALTER SYSTEM SET google_columnar_engine.refresh_threshold_percentage=THRESHOLD;
    

Replace `THRESHOLD` with an integer value between `1` and `100`. This value specifies the percentage of data blocks in content that must become invalid for the content to be marked for refresh.

## Manually refresh tables and vector indexes in the column store

You can manually refresh tables and vector indexes in the columnar engine at any time using dedicated SQL functions. The supported index types are ScaNN and HNSW.

**Note:** Refreshing columnar engine accelerated HNSW and ScaNN indexes (available in [Preview](https://cloud.google.com/products#product-launch-stages)) can temporarily consume memory up to two times the index size.

To refresh a table's data in the columnar engine, execute the `google_columnar_engine_refresh` function.
    
    
    SELECT google_columnar_engine_refresh(TABLE_NAME);
    

Replace `TABLE_NAME` with a string containing the name of the table or the materialized view. If the resource is in a schema other than `public`, specify the name of the schema using the format `SCHEMA_NAME.TABLE_NAME`—for example, `myschema.mytable`.

Similarly, to manually refresh a vector index in the columnar engine, execute the `google_columnar_engine_refresh_index` function.
    
    
    SELECT google_columnar_engine_refresh_index(index => INDEX_NAME);
    

Replace `INDEX_NAME` with a string containing the name of the index to refresh.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
