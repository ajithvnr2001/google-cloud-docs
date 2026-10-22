---
url: https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure/
title: Configure the columnar engine \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:55.667364+00:00
---

# Configure the columnar engine  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Configure the columnar engine Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable or disable the columnar engine on an AlloyDB for PostgreSQL instance. It also covers how to configure an appropriate initial size for its column store, as well as memory and storage cache settings for optimal performance.

To use the columnar engine when using AlloyDB Omni, see [Enable the columnar engine in AlloyDB Omni](https://docs.cloud.google.com/alloydb/docs/omni/columnar-engine/configure).

Each of these actions involves changing the value of a database flag on one of your AlloyDB instances. For more information about setting database flags, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags). 

For a conceptual overview of the AlloyDB columnar engine, see [About the AlloyDB columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about).

## Enable the columnar engine

To use columnar engine on an instance, set the instance's [`google_columnar_engine.enabled`](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#enabled) flag to `on`.

After you set this flag, the instance automatically restarts. 

For more information about setting database flags in AlloyDB, see [Configure an instance's database flags](https://cloud.google.com/alloydb/docs/instance-configure-database-flags).

## Configure the size of the column store

While the columnar engine is enabled on an instance, AlloyDB allocates a portion of the instance's memory to store its columnar data. Dedicating high-speed RAM to your column store ensures that AlloyDB can access the columnar data as rapidly as possible.

Memory and storage cache together represent the overall capacity of the columnar engine.

### Configure memory for the columnar engine

If the column store becomes larger than the allocated portion of your instance's memory, AlloyDB automatically uses the instance's underlying cache layer to store the additional columnar data. 

In AlloyDB, you can load both relations, materialized views, and ScaNN indexes into the columnar engine to accelerate query performance.

By default, AlloyDB allocates 30% of the instance's memory to the column store, and automatically adjusts the total allocation if you resize the instance. You can modify the instance's memory to a recommended maximum of 50%, although 70% is allowed. To find the recommended columnar engine memory size for your instance, see [Recommend column store memory size](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-recommendations#recommend-populate). 

You can also set the allocation to a fixed and specific size using the [`google_columnar_engine.memory_size_in_mb`](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#memory-size-in-mb) flag. To have AlloyDB return to the default allocation, [remove the flag from the instance](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

For more information on setting or deleting flags, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags). 

### Configure the loading of ScaNN indexes into the columnar engine

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The columnar engine accelerates vector search when ScaNN indexes are populated into it.

To enable the columnar index cache, set the [`google_columnar_engine.enable_index_caching`](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#enable_index_caching) flag to `on`.

To disable this feature, set the flag to `off`.

### Configure storage cache for the columnar engine

You must size the `google_columnar_engine.storage_cache_size` relative to the `google_columnar_engine.memory_size_in_mb` setting because the columnar engine memory is used for in-memory metadata for the storage cache. The recommended sizing ratio is approximately 100 to 1000 times the memory size. For example, with a `google_columnar_engine.memory_size_in_mb` of 1024 (1 GB), you must set `google_columnar_engine.storage_cache_size` between 100 GB and 1000 GB.

The columnar engine's storage cache is provisioned according to the instance tier.

**Note:** 1 vCPU instance tiers don't have SSDs and can't use storage cache for the columnar engine. Their columnar engine storage cache size is 0.Instance tier | Default columnar engine cache size  
---|---  
N2 | C4A  
Primary | Read pool | Primary or read pool  
1 vCPU | N/A | N/A | 0  
2 vCPU | 18.75 GB | 37.5 GB | 18.75 GB  
4 vCPU | 18.75 GB | 37.5 GB | 18.75 GB  
8 vCPU | 18.75 GB | 37.5 GB | 37.5 GB  
16 vCPU | 37.5 GB | 37.5 GB | 75 GB  
32 vCPU | 75 GB | 75 GB | 112.5 GB  
48 vCPU | N/A | N/A | 187.5 GB  
64 vCPU | 150 GB | 150 GB | 262.5 GB  
72 vCPU | N/A | N/A | 300 GB  
96 vCPU | 300 GB | 300 GB | N/A  
128 vCPU | 450 GB | 450 GB | N/A  
  
The `google_columnar_engine.storage_cache_size` flag lets you adjust the columnar engine storage cache, with the limitations of the minimum and maximum values listed in the following table:

Instance tier | Minimum columnar engine cache size | Maximum columnar engine cache size  
---|---|---  
N2 | C4A  
Primary | Read pool | Primary or read pool  
1 vCPU | N/A | N/A | N/A | 0  
2 vCPU | 0 | 187.5 GB | 375 GB | 187.5 GB  
4 vCPU | 0 | 187.5 GB | 375 GB | 187.5 GB  
8 vCPU | 0 | 187.5 GB | 375 GB | 375 GB  
16 vCPU | 0 | 375 GB | 375 GB | 750 GB  
32 vCPU | 0 | 750 GB | 750 GB | 1125 GB  
48 vCPU | 0 | N/A | N/A | 1875 GB  
64 vCPU | 0 | 1500 GB | 1500 GB | 2625 GB  
72 vCPU | 0 | N/A | N/A | 3000 GB  
96 vCPU | 0 | 3000 GB | 3000 GB | N/A  
128 vCPU | 0 | 4500 GB | 4500 GB | N/A  
  
## Monitor storage cache data for the columnar engine

To view and monitor data about the storage cache of the columnar engine, you can use the following commands:

Command | Description  
---|---  
`SELECT google_columnar_engine_storage_cache_used();` | Returns the size of the used columnar engine storage cache.  
`SELECT google_columnar_engine_storage_cache_available();` | Returns the size of the unused columnar engine storage cache.  
`SHOW google_columnar_engine.storage_cache_size;` | Returns the total amount of the configured size of storage cache for the columnar engine.  
  
## Enable vectorized join

The columnar engine has a _vectorized join_ feature that can improve the performance of joins by applying vectorized processing to qualifying queries.

After you enable the vectorized join, the AlloyDB query planner has the option to apply the vectorized join operator instead of the standard PostgreSQL hash join operator. The planner makes this decision by comparing the cost of executing the query using either method.

To enable vectorized join on an instance, set the instance's [`google_columnar_engine.enable_vectorized_join`](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#enable-vectorized-join) flag to `on`.

For more information about setting database flags, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags). 

AlloyDB allocates one thread to the vectorized join feature by default. You can increase the number of threads available to this feature by setting the [`google_columnar_engine.vectorized_join_threads`](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#vectorized-join-threads) flag to a larger value.

## Manually refresh your columnar engine

By default, when you enable the columnar engine, it is set to automatically refresh the column store in the background.

**Note:** In [preview](https://cloud.google.com/products#product-launch-stages), ScaNN indexes aren't automatically refreshed in the columnar engine.

For workloads with a high rate of data modifications such as frequent `INSERT`, `UPDATE`, or `DELETE` operations, you may manually refresh the columnar store after these changes to keep the index up-to-date.

To manually refresh the column engine, run the following SQL query:
    
    
    SELECT google_columnar_engine_refresh('TABLE_NAME');
    

Replace `TABLE_NAME` with the name of the table or the materialized view you want to manually refresh.

## Disable the columnar engine

To disable the columbar engine on an instance, set the `google_columnar_engine.enabled` flag to `off`.

For more information about setting database flags in AlloyDB, see [Configure an instance's database flags](https://cloud.google.com/alloydb/docs/instance-configure-database-flags). 

After you set this flag, the instance automatically restarts. 

## Troubleshoot the columnar engine

If columns don't populate in the columnar engine, then one of the following situations might be true:

  * The columns you want to add include an unsupported data type.

  * The requirements of the columnar engine aren't met.




To find the cause of this issue, try the following:

  * Review your instance's [audit logs](https://docs.cloud.google.com/alloydb/docs/audit-logging#viewing_logs). 

  * [Confirm](https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune#relations-view) that the tables or materialized views in your query are in the columnar engine.

  * Verify the usage of the columnar engine using the [`EXPLAIN`](https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune) statement.




## What's next

  * See the [full list of columnar engine database flags](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags).

  * Learn about [auto-columnarization](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-recommendations).

  * Learn how to [accelerate analytical queries using the AlloyDB columnar engine](https://www.cloudskillsboost.google/paths/22/course_templates/642/labs/501234).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
