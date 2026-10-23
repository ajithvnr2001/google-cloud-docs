---
url: https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-manually/
title: Manage column store content manually \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T06:00:15.849740+00:00
---

# Manage column store content manually  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-manually/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Manage column store content manually Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manually manage the content of the columnar engine to accelerate query performance. It explains how to add and remove tables, materialized views, and vector indexes.

## Manage tables, materialized views, and vector indexes

Based on your workload, you can manually add columns to the column store or drop some or all of the columns of a table or a materialized view from the column store. Query evaluation automatically uses the stored columnar data to answer queries.

Similarly, you can manually add HNSW or ScaNN vector indexes to the columnar engine to speed up vector search. Columnar engine acceleration for HNSW indexes is generally available (GA), while acceleration for ScaNN indexes is in [Preview](https://cloud.google.com/products#product-launch-stages). This allows for efficient nearest neighbor searches on large datasets of vector embeddings.

When choosing which tables, materialized views and columns to add to the column store, consider both the size of the column store and the shape of the workload. Good candidates for selection include large tables or views that are frequently scanned. Within these tables or views, identify any large non-unique indexes used by the OLAP workload. You can add these indexes' columns to the column store and potentially drop the indexes, thereby eliminating the performance cost associated with their maintenance on the primary instance.

Use one of the following methods to manage the content of the columnar engine:

  * Manage column store content by updating database flags
  * Manage column store content using SQL functions



See [What data you can add to the column store](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about#limitations) for information about what data types and data sources you can use when adding tables, columns, and materialized views to the column store.

## Before you begin

  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Manage column store content by updating database flags

You can manage column store content manually by updating the `google_columnar_engine.relations` database flag. The flag has a single value that specifies all of your column store's data sources. During the restart, columns specified in this flag are automatically populated into the column store.

You can use this flag together with [auto-columnarization](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-recommendations). If the columnar engine has memory available after populating the columns you specify through the `google_columnar_engine.relations` flag, then auto-columnarization adds further columns to the column store, as needed.

For more information on setting an instance's database flags using either Google Cloud CLI or the Google Cloud console, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

### Add columns using flags

To add columns to the column store, define an instance's `google_columnar_engine.relations` flag. Set its value to a comma-separated list of items, with each item specifying a list of columns to include from a specific table, in this format:
    
    
    DATABASE_NAME.SCHEMA_NAME.TABLE_NAME(COLUMN_LIST)
    

Replace the following:

  * DATABASE_NAME: the database containing the columns to add to the column store.

  * SCHEMA_NAME: the schema identifying the tables or the materialized views to add to the column store—for example, `public`.

  * TABLE_NAME: the table or the materialized view containing the columns to add to the column store.

  * COLUMN_LIST: a comma-separated list of the columns to add to the column store.




To add all of one table's or one materialized view's columns, omit the column list:
    
    
    DATABASE_NAME.SCHEMA_NAME.TABLE_NAME
    

For more information on setting the database flags on an instance, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

#### gcloud CLI syntax when using `google_columnar_engine.relations`

If you use the Google Cloud CLI to set the `google_columnar_engine.relations` flag, then you must use [alternate delimiter syntax](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) to separate the database flags that you set. This is because the column list is comma-separated, requiring you to use a non-comma character when specifying flags within the same command-line argument.

The following example demonstrates using the gcloud CLI to add two columns in the `public` schema to the column store. The example sets a separate flag to enable the columnar engine, because using [the `gcloud alloydb instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) to set any database flag must also set all other database flags that you want to have non-default values, even if they're already set.

**Caution:** Running this example unsets all database flags from the instance except for the flags that it specifies.
    
    
    gcloud alloydb instances update INSTANCE_NAME \
        --database-flags=^:^\
    google_columnar_engine.relations='DATABASE_NAME.public.TABLE_NAME(COLUMN_1,COLUMN_2)'\
    :google_columnar_engine.enabled=on\
    [:FLAG_3=VALUE_3 ...] \
        --region=REGION_ID \
        --cluster=CLUSTER_ID

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `DATABASE_NAME`: the database containing the columns to add to the column store.
  * `TABLE_NAME`: the table or materialized view name.
  * `COLUMN_1, COLUMN_2`: the columns to add to the column store.
  * `REGION_ID`: the region of your instance.
  * `CLUSTER_ID`: the cluster ID.



### Drop columns using flags

To drop columns from the column store, set a new value for the `google_columnar_engine.relations` flag described in the previous section, leaving out the columns that you want to drop.

To drop all of the columns from the column store, unset the `google_columnar_engine.relations` flag from your instance.

For more information on setting database flags on an instance, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

## Manage column store content using SQL functions

You can manage column store content manually by using SQL functions.

### Estimate column store space requirements

Run the `google_columnar_engine_estimate` SQL function to estimate the total amount space needed for a relation in the columnar engine.

### psql Client
    
    
    SELECT google_columnar_engine_estimate(
        relation => 'TABLE_NAME',
        columns => 'COLUMN_LIST'
    );
    

Replace the following:

  * `TABLE_NAME`: a string containing the name of the table or the materialized view. If the table or the view is in a schema other than public, specify the name of the schema, a dot, and the name of the table or the view; for example, `'myschema.mytable'`.
  * `COLUMN_LIST`: a string containing a comma-separated, case-sensitive list of the names of the columns you want to add. If you want to add all of the table's or the materialized view's columns to the column store, omit this parameter.



### Add columns using SQL functions

Run the `google_columnar_engine_add` SQL function to add columns to the column store.

This method adds the specified columns to the column store and manages the columns in the connected node only. The new columns don't persist within the store across instance restarts.

This method doesn't change the `google_columnar_engine.relations` database flag. [Auto-columnarization](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-recommendations) does not consider columns added by this SQL function.

### psql Client
    
    
    SELECT google_columnar_engine_add(
        relation => 'TABLE_NAME',
        columns => 'COLUMN_LIST'
    );
    

Replace the following:

  * `TABLE_NAME`: a string containing the name of the table or the materialized view. If the table or the view is in a schema other than `public`, specify the name of the schema, a dot, and the name of the table or the view; for example, `'myschema.mytable'`.
  * `COLUMN_LIST`: a string containing a comma-separated, case-sensitive list of the names of the columns you want to add. If you want to add all of the table's or the materialized view's columns to the column store, omit this parameter.



### Drop columns using SQL functions

Run the `google_columnar_engine_drop` SQL function as follows:

### psql Client
    
    
    SELECT google_columnar_engine_drop(
        relation => 'TABLE_NAME',
        columns => 'COLUMN_LIST'
    );
    

Replace the following:

  * `TABLE_NAME`: a string containing the name of the table or the materialized view. If the table or the view is in a schema other than `public`, specify the name of the schema, a dot, and the name of the table or the view; for example, `'myschema.mytable'`.
  * `COLUMN_LIST`: a string containing a comma-separated, case-sensitive list of the names of the columns that you want to drop. If you want to drop all of the table's or the materialized view's columns from the column store, omit this parameter.



You can use the `google_columnar_engine_drop` function to remove columns added by editing the `google_columnar_engine.relations` database flag. However, when you do so, those columns are added back to the columnar store when the instance restarts.

## Manage vector indexes in the columnar engine

To accelerate vector search, you can load vector indexes to the columnar engine's index cache. Columnar engine acceleration for HNSW indexes is generally available (GA), while acceleration for ScaNN indexes is in [Preview](https://cloud.google.com/products#product-launch-stages).

### Add, remove, and verify vector indexes using SQL functions

You can manually add, remove, and verify vector indexes from the index cache using SQL functions. Adding an index to the cache can accelerate vector search queries.

#### Add a vector index

To add a specific index to the columnar engine's index cache, use the following SQL function:
    
    
    SELECT google_columnar_engine_add_index(index => 'INDEX_NAME');
    

Replace `INDEX_NAME` with the name of the HNSW or ScaNN vector index that you want to add to the columnar engine's index cache.

#### Remove a vector index

To drop a specific vector index from the columnar engine, use the following SQL function:
    
    
    SELECT google_columnar_engine_drop_index(index => 'INDEX_NAME');
    

Replace `INDEX_NAME` with the name of the vector index that you want to remove.

#### Verify columnar engine usage

To verify if your vector index scans use the columnar engine, execute the `EXPLAIN ANALYZE` command with the `COLUMNAR_ENGINE` option:
    
    
    EXPLAIN (ANALYZE TRUE, SCANN TRUE, COSTS FALSE, TIMING FALSE, SUMMARY FALSE, VERBOSE FALSE, COLUMNAR_ENGINE TRUE)
    SELECT * FROM t ORDER BY val <=> '[0.5,0.5,0.5,0.5]' LIMIT 100;
    

The command returns a query plan similar to the following:
    
    
    Index Scan using t_ix3 on t t_1 (actual rows=100 loops=1)
          Order By: (val <=> '[0.5,0.5,0.5,0.5]'::vector)
          Limit: 100
          ScaNN Info: (... columnar engine nodes hit=6...)
          Columnar Engine ScaNN Info: (index found=true)
    

The presence of `columnar engine nodes hit` and `Columnar Engine ScaNN Info: (index found=true)` in the output confirms that the columnar engine is used for the query.

## What's next

  * [Optimize queries with virtual columns for expressions](https://docs.cloud.google.com/alloydb/docs/columnar-engine/add-frequent-expressions).
  * [Accelerate vector search with the columnar engine](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-with-ce)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
