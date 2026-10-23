---
url: https://docs.cloud.google.com/memorystore/docs/valkey/info-vector-metrics/
title: INFO command metrics \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:11.415858+00:00
---

# INFO command metrics  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/info-vector-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  INFO command metrics Stay organized with collections  Save and categorize content based on your preferences. 

On Memorystore for Valkey, the `INFO` command returns metrics for vector data and vector search. This page describes the metrics that are available by using the `info`, `info modules`, and `info modules search` commands.

## Index statistic metrics

Metric | Value type | Description  
---|---|---  
search_total_indexed_hash_keys | Integer | Total count of HASH keys for all index partitions located on this node  
search_number_of_indexes | Integer | Total count of indexes  
search_number_of_attributes | Integer | Total count of attributes for all indexes  
  
## Query metrics

Metric | Value type | Description  
---|---|---  
search_failure_requests_count | Integer | A count of all failed requests  
search_successful_requests_count | Integer | A count of all successful requests  
  
## Memory metrics

Metric | Value type | Description  
---|---|---  
search_used_memory_human | Integer | A human-friendly readable version of the `search_used_memory_bytes` metric  
search_used_memory_bytes | Integer | The total bytes of memory that all indexes occupy  
  
## Index ingestion

Metric | Value type | Description  
---|---|---  
search_background_indexing_status | String | The status of the indexing process. `NO_ACTIVITY` indicates idle indexing.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
