---
url: https://docs.cloud.google.com/dataflow/docs/guides/managed-io-iceberg/
title: Dataflow managed I/O for Apache Iceberg \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:28.469788+00:00
---

# Dataflow managed I/O for Apache Iceberg  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/managed-io-iceberg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow managed I/O for Apache Iceberg Stay organized with collections  Save and categorize content based on your preferences. 

[Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io) supports the following capabilities for Apache Iceberg:

Catalogs | 

  * Hadoop
  * Hive
  * REST-based catalogs
  * [BigQuery metastore](https://docs.cloud.google.com/bigquery/docs/about-bqms) (requires Apache Beam SDK 2.62.0 or later if not using the Portable Runner) 

  
---|---  
Read capabilities | Batch read  
Write capabilities | 

  * Batch write
  * Streaming write
  * [ Dynamic destinations](https://docs.cloud.google.com/dataflow/docs/guides/write-to-iceberg#dynamic-destinations)
  * Dynamic table creation

  
  
For [BigQuery tables for Apache Iceberg](https://docs.cloud.google.com/bigquery/docs/iceberg-tables), use the [`BigQueryIO` connector](https://beam.apache.org/documentation/io/built-in/google-bigquery/) with BigQuery Storage API. The table must already exist; dynamic table creation is not supported.

## Requirements

The following SDKs support managed I/O for Apache Iceberg:

  * Apache Beam SDK for Java version 2.58.0 or later
  * Apache Beam SDK for Python version 2.61.0 or later



## Configuration

Managed I/O for Apache Iceberg supports the following configuration parameters:

### `ICEBERG` Read

Configuration | Type | Description  
---|---|---  
**table** |  `str` |  Identifier of the Iceberg table.   
catalog_name  |  `str` |  Name of the catalog containing the table.   
catalog_properties  |  `map[str, str]` |  Properties used to set up the Iceberg catalog.   
config_properties  |  `map[str, str]` |  Properties passed to the Hadoop Configuration.   
drop  |  `list[str]` |  A subset of column names to exclude from reading. If null or empty, all columns will be read.   
filter  |  `str` |  SQL-like predicate to filter data at scan time. Example: "id > 5 AND status = 'ACTIVE'". Uses Apache Calcite syntax: https://calcite.apache.org/docs/reference.html   
keep  |  `list[str]` |  A subset of column names to read exclusively. If null or empty, all columns will be read.   
  
### `ICEBERG` Write

'). 

Configuration | Type | Description  
---|---|---  
**table** |  `str` |  A fully-qualified table identifier. You may also provide a template to write to multiple dynamic destinations, for example: `dataset.my_{col1}_{col2.nested}_table`.   
allowed_lateness_seconds  |  `int32` |  How long a late record may lag behind the watermark before it is dropped entirely, rather than routed to the dead_letter output. Defaults to 21600 (6 hours). Currently only supported in 'merge-on-read' mode.   
autosharding  |  `boolean` |  Enables dynamic sharding to automatically adjust the number of parallel writers based on data volume. It handles data skew by further sub-dividing partitions into multiple shards to prevent bottlenecks during high-throughput writes. Only available with 'hash' distribution mode.   
catalog_name  |  `str` |  Name of the catalog containing the table.   
catalog_properties  |  `map[str, str]` |  Properties used to set up the Iceberg catalog.   
change_type_column  |  `str` |  Merge-on-read only. The optional column name representing the row's change type (INSERT, UPDATE_BEFORE, UPDATE_AFTER, or DELETE). This column will be stripped from the data row before writing to Iceberg. If unset, the sink will use the element's native ValueKind   
change_type_map  |  `map[str, str]` |  Merge-on-read only. Optional map from a change_type_column value to the canonical change type name (see above).   
config_properties  |  `map[str, str]` |  Properties passed to the Hadoop Configuration.   
direct_write_byte_limit  |  `int32` |  For a streaming pipeline, sets the limit for lifting bundles into the direct write path.   
distribution_mode  |  `str` |  Defines distribution of write data. Supported distributions: \- none: don't shuffle rows (default) \- hash: shuffle rows by partition key before writing data   
drop  |  `list[str]` |  A list of field names to drop from the input record before writing. Is mutually exclusive with 'keep' and 'only'. In merge-on-read mode the control columns are always dropped.   
equality_columns  |  `list[str]` |  Columns defining row identity (equality-delete fields). Defaults to the destination table's identifier (primary-key) fields. Required if the table doesn't exist yet. Currently only supported in 'merge-on-read' mode.   
keep  |  `list[str]` |  A list of field names to keep in the input record. All other fields are dropped before writing. Is mutually exclusive with 'drop' and 'only'. In merge-on-read mode the control columns are dropped unless listed here.   
maximum_table_cache_size  |  `int32` |  For a batch pipeline, sets the maximum number of table metadata specs to cache in memory. Tables exceeding this limit fall back to worker-local catalog loading.   
mode  |  `str` |  Controls how rows are written. 'append' (default) appends every row as new data. 'merge-on-read' treats each row as a change (INSERT, UPDATE_BEFORE, UPDATE_AFTER, or DELETE) applied to the table by primary key.   
num_shards  |  `int32` |  The number of deterministic primary-key-hash shards per destination, i.e. the max write parallelism per destination. Too low may bottleneck writes, and too high may produce more files. Defaults to 16. Currently only supported in 'merge-on-read' mode.   
only  |  `str` |  The name of a single record field that should be written. Is mutually exclusive with 'keep' and 'drop'.   
partition_fields  |  `list[str]` |  Fields used to create a partition spec that is applied when tables are created. For a field 'foo', the available partition transforms are: 

  * `foo`
  * `truncate(foo, N)`
  * `bucket(foo, N)`
  * `hour(foo)`
  * `day(foo)`
  * `month(foo)`
  * `year(foo)`
  * `void(foo)`

For more information on partition transforms, please visit <https://iceberg.apache.org/spec/#partition-transforms>.   
sequence_number_column  |  `str` |  Merge-on-read only. The required column name representing the monotonic sequence number used to order a single key's changes. Defaults to '_commit_snapshot_sequence_number'. This column will be stripped from the data row before writing to Iceberg.   
shards_per_partition  |  `int32` |  Maximum number of shards a single partition's rows may occupy. Lower values write fewer files per commit, but also reduces per-partition write parallelism. A value of 1 pins each partition to one writer. Ignored for unpartitioned tables. Must be between 1 and `num_shards`; defaults to `num_shards`. Currently only supported in 'merge-on-read' mode.   
sink_id  |  `str` |  A stable identifier for this sink, used to namespace the idempotency tokens written to each commit's Iceberg snapshot summary. Defaults to a unique per-write UUID. Set it explicitly (and keep it stable across relaunches) for exactly-once commits across relaunches of a particular streaming write. A batch load with a stable sink_id commits only once (later batch loads with the same sink_id are skipped). Currently only supported in 'merge-on-read' mode.   
snapshot_properties  |  `map[str, str]` |  Extra key/value properties to add to every commit's Iceberg snapshot summary. Keys prefixed with 'beam.cdc.' are reserved and rejected. Currently only supported in 'merge-on-read' mode.   
sort_fields  |  `list[str]` |  Fields used to set the table's sort order, applied when the table is created. Each entry has the form `<term> [asc|desc] [nulls first|nulls last]`, where `<term>` is a field name or one of the partition transforms (e.g. `bucket(col, 4)`, `day(ts)`). Direction defaults to ascending; null order defaults to nulls-first for ascending and nulls-last for descending. Note: this sets the table's declared sort order as metadata; it does not cause Beam to physically sort records before writing. For more information on sort orders, please visit <https://iceberg.apache.org/spec/#sort-orders>.   
sorter_memory_mb  |  `int32` |  The in-memory buffer size (MB) for the pre-write sort; groups larger than this spill to disk. Must be >= 1. Defaults to 100. Currently only supported in 'merge-on-read' mode.   
table_cache_polling_buckets  |  `int32` |  Sets the number of parallel buckets/workers used to query the Iceberg catalog during refreshes. Defaults to 1.   
table_cache_refresh_interval_seconds  |  `int32` |  For a streaming pipeline, sets the interval in seconds at which table metadata is refreshed from the catalog.   
table_properties  |  `map[str, str]` |  Iceberg table properties to be set on the table when it is created. For more information on table properties, please visit <https://iceberg.apache.org/docs/latest/configuration/#table-properties>.   
token_heartbeat_seconds  |  `int32` |  Streaming only. If set, the sink will emit a periodic empty token-refresh commit while idle, so its thread of `sink_id` stamped snapshot stays recent and is less likely to be lost to `expire_snapshots`. Disabled by default. Currently only supported in 'merge-on-read' mode.   
triggering_frequency_seconds  |  `int32` |  For a streaming pipeline, sets the frequency at which snapshots are produced.   
upsert  |  `boolean` |  Merge-on-read only. If true, only the after-image of each change (INSERT/UPDATE_AFTER) is applied, as an upsert; UPDATE_BEFORE records are dropped. Default: false.   
use_side_input_table_cache  |  `boolean` |  Enables expirable side-input caching of Iceberg table metadata across workers to reduce catalog load.   
write_properties  |  `map[str, str]` |  Properties applied to the underlying file writer (e.g. Parquet write properties like 'write.parquet.bloom-filter-enabled.column.  
  
## What's next

For more information and code examples, see the following topics:

  * [Read from Apache Iceberg](https://docs.cloud.google.com/dataflow/docs/guides/read-from-iceberg)
  * [Read from Apache Iceberg (job builder UI)](https://docs.cloud.google.com/dataflow/docs/guides/iceberg-df-lakehouse-integration)
  * [Write to Apache Iceberg](https://docs.cloud.google.com/dataflow/docs/guides/write-to-iceberg)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
