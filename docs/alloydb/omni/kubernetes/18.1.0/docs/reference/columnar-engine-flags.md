---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/columnar-engine-flags/
title: Columnar engine flags \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:47.723662+00:00
---

# Columnar engine flags  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/columnar-engine-flags/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  Columnar engine flags Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/columnar-engine-flags)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/columnar-engine-flags)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/columnar-engine-flags)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/columnar-engine-flags)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/columnar-engine-flags)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/columnar-engine-flags)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/columnar-engine-flags)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/columnar-engine-flags)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/columnar-engine-flags)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/columnar-engine-flags)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/columnar-engine-flags)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/columnar-engine-flags)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/columnar-engine-flags)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/columnar-engine-flags)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/columnar-engine-flags)



This page describes the database flags that AlloyDB Omni uses to enable and manage features specific to [its columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/overview). For a list of all database flags that AlloyDB Omni supports, see [Supported database flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/database-flags).

Flags marked with **Instance restarts** mean that you must restart an AlloyDB Omni instance whenever you set, remove, or modify this flag on that instance. The flag's value persists for the instance until you modify it again.

For instructions about how to set a database flag, see [Configure AlloyDB Omni database flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/configure-database-flags).

## Enablement

### `google_columnar_engine.enabled`

Type| `Boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
If `on`, enables the AlloyDB Omni [columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/overview).

## Auto-columnarization

### `google_columnar_engine.enable_auto_columnarization`

Type| `Boolean`  
---|---  
Default| `on`  
Instance restarts| No  
  
If `on`, enables the columnar engine's [auto-columnarization features](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/manage-content-recommendations).

### `google_columnar_engine.relations`

Type| `String`  
---|---  
Default| An empty string  
Instance restarts| No  
  
Specifies a list of columns for AlloyDB Omni to add to your cluster's column store, apart from the auto-columnarization process. These columns can come from any tables within your cluster.

The flag's value is formatted as a comma-separated list of items. Each item specifies one or more columns from a single table, expressed in this format:
    
    
    'DATABASE_NAME.SCHEMA_NAME.TABLE_NAME(COLUMN_LIST)'
    

For more information, see [Manage column store content manually](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/manage-content-manually).

### `google_columnar_engine.auto_columnarization_schedule`

Type| `String`  
---|---  
Default| An empty string  
Instance restarts| No  
Maximum allowed value| 2147483647  
  
Specifies the frequency that AlloyDB Omni runs its [auto-columnarization](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/manage-content-recommendations) process on the instance.

The value is a string in the following format:
    
    
    'EVERY NUMBER TIME_UNITS'
    

Replace the following:

  * NUMBER: A positive integer.

  * TIME_UNITS: Either `DAYS` or `HOURS`.




If not defined, then AlloyDB Omni runs the auto-columnarization process once every hour.

## Sizing and query processing

### `google_columnar_engine.memory_size_in_mb`

Type| `Integer`  
---|---  
Valid values| Between 128 to the value that represents 70% of instance memory  
Default| 1GB of instance memory  
Instance restarts| Yes  
  
The amount of instance memory, expressed in mebibytes (MiB), that AlloyDB Omni allocates to the column store.

If this flag isn't set, then AlloyDB Omni allocates 1GB of the instance's memory to the column store.

### `google_columnar_engine.enable_columnar_scan`

Type| `Boolean`  
---|---  
Default| `on`  
Instance restarts| No  
  
If `on`, allows AlloyDB Omni to access data in the column store when handling queries.

If this flag is `off` while `google_columnar_engine.enabled` is `on`, then the columnar engine remains enabled and keeps its column store, but AlloyDB Omni doesn't use columnar data when it handles queries.

### `google_columnar_engine.omni_storage_cache_directory`

This flag lets you specify a separate dedicated directory path for disk cache files for the columnar engine.

Type| `String`  
---|---  
Valid values| A single directory path where disk cache files are stored.  
Default| The total size of the dedicated Persistent Volume Claim (PVC) is allocated for the columnar spill-to-disk cache.  
Instance restarts| Yes  
  
### `google_columnar_engine.storage_cache_size`

If `google_columnar_engine.omni_storage_cache_directory` is not specified, to enable the storage cache size, you must enable [disk cache](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/configure-disk-cache#enable-cache).

Type| `Integer`  
---|---  
Valid values| `1024` ... `2147483647`  
Default| 5% of the disk cache is allocated to the columnar engine when `google_columnar_engine.omni_storage_cache_directory` is not specified.  
Instance restarts| Yes  
  
If `on`, lets AlloyDB Omni configure size of the storage cache for the columnar engine.

When `google_columnar_engine.omni_storage_cache_directory` is not specified, the maximum allowed value for this flag is 50% of the total disk cache. The 1000 * `google_columnar_engine.memory_size_in_mb` cap is also applicable.

## Maintenance activities

### `google_job_scheduler.maintenance_cpu_percentage`

**Note:** This flag uses the prefix `google_job_scheduler` and not `google_columnar_engine`.Type| `Integer`  
---|---  
Valid values| `0` ... `100`  
Default| `20`  
Instance restarts| No  
  
The maximum percentage of an instance's CPU capacity that the columnar engine can apply to background processing.

### `google_job_scheduler.max_parallel_workers_per_job`

**Note:** This flag uses the prefix `google_job_scheduler` and not `google_columnar_engine`.Type| `Integer`  
---|---  
Valid values| `0` ... `262143`  
Default| `2`  
Instance restarts| No  
  
The maximum number of parallel workers that the columnar engine can create to handle any single background processing operation.

### Auto refresh - event driven

#### `google_columnar_engine.refresh_threshold_percentage`

Type| `Integer`  
---|---  
Valid values| `1` ... `100`  
Default| `50`  
Instance restarts| No  
  
Specifies the column store's data-refresh threshold, expressed as a percentage.

AlloyDB Omni refreshes the data within a _columnar unit_ —a set of data blocks within a columnar table—when the following conditions are met:

  * The columnar unit's table has exceeded the scan-threshold defined by the separate `refresh_threshold_scan_count` flag.

  * The percentage of the columnar unit's underlying data blocks that have become _invalid_ exceeds the value of the `refresh_threshold_percentage` flag. Columnar data blocks become invalid due to changes in the row-based data that the columnar table draws upon.




#### `google_columnar_engine.refresh_threshold_scan_count`

Type| `Integer`  
---|---  
Valid values| `0` ... `2147483647`  
Default| `5`  
Instance restarts| No  
  
AlloyDB Omni keeps a running count of the table scans performed on each columnar table since that table's most recent DML query. The value of the `refresh_threshold_scan_count` flag specifies the minimum value of this counter on any columnar table before AlloyDB Omni can refresh its data. From there, AlloyDB Omni uses the invalid-block threshold defined by `refresh_threshold_percentage` to determine when to refresh the table's data.

If this flag's value is set to `0`, then AlloyDB Omni disregards table scans to determine when to refresh columnar data, using only `refresh_threshold_percentage` instead.

### Auto refresh - periodic and adaptive

#### `google_columnar_engine.adaptive_auto_refresh_schedule`

Type| `String`  
---|---  
Default| An empty string  
Instance restarts| No  
Maximum allowed value| 2147483647  
  
Specifies the frequency that AlloyDB Omni runs its Adaptive Auto Refresh process on the instance.

The value is a string in the following format:
    
    
    'EVERY NUMBER TIME_UNITS'
    

Replace the following:

  * NUMBER: a positive integer.

  * TIME_UNITS: either `DAYS` or `HOURS`.




If not defined, then AlloyDB Omni runs the Adaptive Auto Refresh process once every hour.

#### `google_columnar_engine.min_adaptive_auto_refresh_blocks`

Type| `Integer`  
---|---  
Valid values| `0` ... `2147483647`  
Default| `50`  
Instance restarts| No  
  
The number of the columnar unit's underlying data blocks that have become invalid exceeds the value of the `min_adaptive_auto_refresh_blocks` flag. Columnar data blocks become invalid due to changes in the row-based data that the columnar table draws upon.

## Vectorized join

### `google_columnar_engine.enable_vectorized_join`

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Type| `Boolean`  
---|---  
Default| `off`  
Restarts instance| `No`  
  
If `on`, then AlloyDB Omni automatically uses multithreaded vectorized operations to improve the performance of queries that join multiple tables.

For more information, see [Enable vectorized joins](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/configure#vectorized).

### `google_columnar_engine.vectorized_join_threads`

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Type| `Integer`  
---|---  
Valid values| Up to half of the instance's vCPU count  
Default| `1`  
Restarts instance| `No`  
  
Defines the maximum number of parallel threads available to the vectorized join operator, enabled by the `enable_vectorized_join` flag.

You can define a value as large as one-half of the instance's vCPUs. For example, on a 16 vCPU instance, this flag's maximum value is `8`.

## Preview features

### `google_columnar_engine.enable_json_support`

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Type| `Boolean`  
---|---  
Default| `off`  
Restarts instance| `No`  
  
If both this flag and `enable_raw_format` are set to `on`, then AlloyDB Omni allows [PostgreSQL JSON and JSONB data types](https://www.postgresql.org/docs/18/datatype-json.html) in the column store.

### `google_columnar_engine.enable_raw_format`

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Type| `Boolean`  
---|---  
Default| `off`  
Restarts instance| `No`  
  
If both this flag and `enable_json_support` are set to `on`, then AlloyDB Omni allows [PostgreSQL JSON and JSONB data types](https://www.postgresql.org/docs/18/datatype-json.html) in the column store.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
