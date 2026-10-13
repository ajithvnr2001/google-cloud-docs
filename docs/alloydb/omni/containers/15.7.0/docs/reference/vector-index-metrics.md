---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/reference/vector-index-metrics/
title: Vector index metrics \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:53.486221+00:00
---

# Vector index metrics  |  AlloyDB Omni for containers: 15.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/reference/vector-index-metrics/

This page documents AlloyDB Omni version **15.7.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/choose-compatible-versions)



Send feedback 

#  Vector index metrics Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/vector-index-metrics)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/reference/vector-index-metrics)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/reference/vector-index-metrics)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/reference/vector-index-metrics)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/reference/vector-index-metrics)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/vector-index-metrics)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/reference/vector-index-metrics)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/reference/vector-index-metrics)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/reference/vector-index-metrics)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/reference/vector-index-metrics)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/reference/vector-index-metrics)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/reference/vector-index-metrics)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/reference/vector-index-metrics)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/reference/vector-index-metrics)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/reference/vector-index-metrics)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/reference/vector-index-metrics)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/reference/vector-index-metrics)

This page lists the metrics related to the vector indexes that you generate in AlloyDB Omni. You can view these metrics using the `pg_stat_ann_indexes` view that is available when you install [the `alloydb_scann` extension](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/store-index-query-vectors). 

For more information about viewing the metrics, see [View vector index metrics](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/tune-indexes#vector-index-metrics).

## Usability metrics

The usability metrics include metrics that help you understand the state of index utilization with metrics, such as index configuration and number of index scans.

Metric name | Data type | Description  
---|---|---  
`relid` | `OID` | Unique identifier of the table that contains the vector index  
`indexrelid` | `OID` | Unique identifier of the vector index  
`schemaname` | `NAME` | Name of the schema that owns the index  
`relname` | `NAME` | Name of the table that contains the index  
`indexrelname` | `NAME` | Name of the index  
`indextype` | `NAME` | Type of the index. This value is always set to `alloydb_scann`  
`indexconfig` | `TEXT[]` | Configuration, such as leaves count and quantizer, defined for the index when it was created  
`indexsize` | `TEXT` | Size of the index  
`indexscan` | `BIGINT` | Number of index scans initiated on the index  
  
## Tuning metrics

Tuning metrics provide insights into your current index optimization, allowing you to apply recommendations for faster query performance.

Metric name | Data type | Description  
---|---|---  
`insertcount` | `BIGINT` | Number of insert operations on the index. This metric also includes the number of rows that existed before the index was created.  
`updatecount` | `BIGINT` | Number of update operations on the index. This metric doesn't take into account any HOT updates.  
`deletecount` | `BIGINT` | Number of delete operations on the index.  
`distribution` | `JSONB` | Vector distributions across all partitions for the index.  
  
The following fields show the distribution:  


  * `maximum (INT8)`: Maximum number of vectors across all partitions.
  * `minimum (INT8)`: Minimum number of vectors across all partitions.
  * `average (FLOAT)` : Average number of vectors across all partitions.
  * `outliers (INT8[])`: Top outliers across all partitions. This value shows the top 20 outliers.

  
**Note:** Due to the inherent characteristics of the K-means clustering algorithm, there will always be some degree of variance in the distribution of vectors across partitions, even when the index is initially created.  
  
### Tuning recommendation based on the metrics

Mutation
    The `insertcount`, `updatecount`, and `deletecount` metrics together show the changes or mutations in the vector for the index. 
    The index is created with a specific number of vectors and partitions. When operations such as insert, update, or delete are performed on the vector index, it only affects the initial set of partitions where the vectors reside. Consequently, the number of vectors in each partition fluctuates over time, potentially impacting recall, QPS, or both.
    If you encounter slowness or accuracy issues such as low QPS or poor recall, in your ANN search queries over time, then consider reviewing these metrics. A high number of mutations relative to the total number of vectors could indicate the need for reindexing. 
Distribution
    The `distribution` metric shows the vector distributions across all partitions.
    When you create an index, it is created with a specific number of vectors and fixed partitions. The partitioning process and subsequent distribution occurs based on this consideration. If additional vectors are added, they are partitioned among the existing partitions, resulting in a different distribution compared to the distribution when the index was created. Since the final distribution does not consider all vectors simultaneously, the recall, QPS, or both might be affected.
    If you observe a gradual decline in the performance of your ANN search queries, such as slower response times or reduced accuracy in the results (measured by QPS or recall), then consider checking this metric and reindexing.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
