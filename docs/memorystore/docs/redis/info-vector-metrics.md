---
url: https://docs.cloud.google.com/memorystore/docs/redis/info-vector-metrics/
title: INFO command metrics \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:44.347076+00:00
---

# INFO command metrics  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/info-vector-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  INFO command metrics Stay organized with collections  Save and categorize content based on your preferences. 

On Memorystore for Redis, the Redis `INFO` command returns metrics for vector data and vector search. This page describes the metrics that are available by using the Redis `info`, `info modules`, and `info modules search` commands.

## Index statistic metrics

Metric | Value type | Description  
---|---|---  
search_total_indexed_hash_keys | Integer | Total count of HASH keys for all indexes  
search_number_of_indexes | Integer | Index schema total count  
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
  
## HNSW metrics

Metric | Value type | Description  
---|---|---  
search_hnsw_create_exceptions_count | Integer | Count of HNSW creation exceptions.  
search_hnsw_search_exceptions_count | Integer | Count of HNSW search exceptions  
search_hnsw_remove_exceptions_count | Integer | Count of HNSW removal exceptions.  
search_hnsw_add_exceptions_count | Integer | Count of HNSW addition exceptions.  
search_hnsw_modify_exceptions_count | Integer | Count of HNSW modification exceptions  
  
## Subscription metrics

Metric | Value type | Description  
---|---|---  
search_modify_subscription_skipped_count | Integer | Count of skipped subscription modifications  
search_remove_subscription_successful_count | Integer | Count of successful subscription removals  
search_remove_subscription_skipped_count | Integer | Count of skipped subscription removals  
search_remove_subscription_failure_count | Integer | Count of failed subscription removals  
search_add_subscription_successful_count | Integer | Count of successfully added subscriptions  
search_add_subscription_failure_count | Integer | Count of failures of adding subscriptions  
search_add_subscription_skipped_count | Integer | Count of skipped subscription adding processes  
search_modify_subscription_failure_count | Integer | Count of failed subscription modifications  
search_modify_subscription_successful_count | Integer | Count of successful subscription modifications  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
