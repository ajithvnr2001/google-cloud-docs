---
url: https://docs.cloud.google.com/bigtable/docs/metrics/
title: Metrics \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:22.093780+00:00
---

# Metrics  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Metrics

The following Bigtable metrics are provided to Cloud Monitoring. For best results, always use server-side metrics in conjunction with [client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-descriptions) for performance debugging.

The "metric type" strings in this table must be prefixed with `bigtable.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`backup/bytes_used` GA ** _(project)_**   
Backup storage used.   
`GAUGE`, `INT64`, `By`   
**[bigtable_backup](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_backup)** |  _Backup storage used in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`source_table`: The source table of the backup.   
`storage_type`: Type of disk storage.   
`client/application_blocking_latencies` GA ** _(project)_**   
Application Blocking Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The total latency introduced by your application when Cloud Bigtable has available response data but your application has not consumed it. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`client_name`: Cloud Bigtable client name.   
`client/attempt_latencies` GA ** _(project)_**   
Attempt Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Client observed latency per RPC attempt. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`streaming`: (BOOL) Cloud Bigtable streaming method.   
`status`: Cloud Bigtable attempt status.   
`client_name`: Cloud Bigtable client name.   
`client/client_blocking_latencies` GA ** _(project)_**   
Client Blocking Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The latency introduced by the client by blocking on sending more requests to the server when there are too many pending requests in bulk operations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`client_name`: Cloud Bigtable client name.   
`client/connectivity_error_count` GA ** _(project)_**   
Connectivity Error Count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of requests that failed to reach the Google network. (Requests without google response headers). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`status`: Cloud Bigtable operation status.   
`client_name`: Cloud Bigtable client name.   
`client/first_response_latencies` GA ** _(project)_**   
First Response Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Latency from operation start until the response headers were received. The publishing of the measurement will be delayed until the attempt response has been received. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`status`: Cloud Bigtable operation status.   
`client_name`: Cloud Bigtable client name.   
`client/operation_latencies` GA ** _(project)_**   
Operation Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Distribution of the total end-to-end latency across all RPC attempts associated with a Bigtable operation. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`streaming`: (BOOL) Cloud Bigtable streaming method.   
`status`: Cloud Bigtable operation status.   
`client_name`: Cloud Bigtable client name.   
`client/retry_count` GA ** _(project)_**   
Retry Count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The number of additional RPCs sent after the initial attempt. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`status`: Cloud Bigtable operation status.   
`client_name`: Cloud Bigtable client name.   
`client/server_latencies` GA ** _(project)_**   
Server Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The latency measured between the time when Google frontend receives an RPC and sending back the first byte of the response. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`streaming`: (BOOL) Cloud Bigtable streaming method.   
`status`: Cloud Bigtable operation status.   
`client_name`: Cloud Bigtable client name.   
`cluster/autoscaling/max_node_count` GA ** _(project)_**   
Maximum nodes   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Maximum number of nodes in an autoscaled cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`storage_type`: Storage type for the cluster.   
`cluster/autoscaling/min_node_count` GA ** _(project)_**   
Minimum nodes   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Minimum number of nodes in an autoscaled cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`storage_type`: Storage type for the cluster.   
`cluster/autoscaling/recommended_node_count_for_cpu` GA ** _(project)_**   
Recommended nodes based on CPU   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Recommended number of nodes in an autoscaled cluster based on CPU usage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`cluster/autoscaling/recommended_node_count_for_storage` GA ** _(project)_**   
Recommended nodes based on storage   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Recommended number of nodes in an autoscaled cluster based on storage usage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`cluster/autoscaling/storage_utilization_at_max` GA ** _(project)_**   
Storage utilization at autoscaler max   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Storage utilization at autoscaling max, i.e., storage used as a fraction of total storage capacity if the cluster is scaled to maximum node count. Writes are blocked if this reaches 100%. For details, see https://docs.cloud.google.com/bigtable/docs/autoscaling#how-it-works. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_type`: Type of disk storage (ssd and ssd+infrequent_access for SSD clusters, hdd for HDD clusters).   
`cluster/cpu_load` GA ** _(project)_**   
CPU load   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _CPU load of a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`cluster/cpu_load_by_app_profile_by_method_by_table` GA ** _(project)_**   
CPU load by app profile, method, and table   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _CPU load of a cluster. Split by app profile, method, and table. Contains the same underlying data as bigtable.googleapis.com/cluster/cpu_load. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`app_profile`: Cloud Bigtable application profile.   
`method`: Cloud Bigtable API method.   
`table`: Cloud Bigtable table name.   
`cluster/cpu_load_hottest_node` GA ** _(project)_**   
CPU load (hottest node)   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _CPU load of the busiest node in a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`cluster/cpu_load_hottest_node_high_granularity` GA ** _(project)_**   
CPU load (hottest node) high granularity   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _CPU load of the busiest node in a cluster sampled at a high granularity. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._  
`cluster/disk_load` GA ** _(project)_**   
Disk load   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _For HDD clusters, the utilization of HDD disks. For SSD clusters with tiered storage enabled, the utilization of the infrequent access tier disks. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`cluster/node_count` GA ** _(project)_**   
Nodes   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Number of nodes in a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`storage_type`: Storage type for the cluster.   
`cluster/storage_utilization` GA ** _(project)_**   
Storage utilization   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Storage used as a fraction of total storage capacity. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_type`: Type of disk storage (ssd and ssd+infrequent_access for SSD clusters, hdd for HDD clusters).   
`disk/bytes_used` GA ** _(project)_**   
Data stored   
`GAUGE`, `INT64`, `By`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Amount of compressed data for tables stored in a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_type`: Type of disk storage (ssd, hdd, or infrequent_access).   
`disk/per_node_storage_capacity` GA ** _(project)_**   
Storage capacity per node   
`GAUGE`, `INT64`, `By`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Capacity of compressed data for tables that can be stored per node in the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`storage_type`: Type of disk storage (ssd and ssd+infrequent_access for SSD clusters, hdd for HDD clusters).   
`disk/storage_capacity` GA ** _(project)_**   
Storage capacity   
`GAUGE`, `INT64`, `By`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Capacity of compressed data for tables that can be stored in a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`storage_type`: Type of disk storage (ssd and ssd+infrequent_access for SSD clusters, hdd for HDD clusters).   
`materialized_view/intermediate_storage` GA ** _(project)_**   
Data for intermediate processing.   
`GAUGE`, `INT64`, `By`   
**[bigtable_materialized_view](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_materialized_view)** |  _Amount of data used by intermediate processing for the materialized view in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`storage_type`: Type of disk storage.   
`materialized_view/max_delay` GA ** _(project)_**   
Maximum processing delay   
`GAUGE`, `INT64`, `s`   
**[bigtable_materialized_view](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_materialized_view)** |  _Upper bound of processing delay for the materialized view. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`materialized_view/storage` GA ** _(project)_**   
Materialized view data.   
`GAUGE`, `INT64`, `By`   
**[bigtable_materialized_view](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_materialized_view)** |  _Amount of data used for the materialized view storage in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`storage_type`: Type of disk storage.   
`materialized_view/system_errors` GA ** _(project)_**   
System error count   
`DELTA`, `INT64`, `1`   
**[bigtable_materialized_view](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_materialized_view)** |  _Number of errors from system for the materialized view. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`canonical_status`: Canonical error status.   
`materialized_view/user_errors` GA ** _(project)_**   
User error count   
`DELTA`, `INT64`, `1`   
**[bigtable_materialized_view](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_materialized_view)** |  _Number of errors from user data for the materialized view. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`canonical_status`: Canonical error status.   
`memory_layer/hit_ratio` BETA ** _(project)_**   
Memory layer hit ratio   
`GAUGE`, `DOUBLE`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Ratio of number of read requests that successfully read from the memory layer compared to all memory eligible read requests. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`memory_layer/ineligible_reason_count` BETA ** _(project)_**   
Memory layer ineligible reason count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of requests that were ineligible for the memory layer, broken down by the reason. One request may be counted for multiple reasons. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`reason`: Reason that request is ineligible for the memory layer.   
`memory_layer/max_request_units` BETA ** _(project)_**   
Memory layer max request units   
`GAUGE`, `INT64`, `1`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Maximum number of Request-Units per second used in a 5 minute window. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`memory_layer/read_latencies` BETA ** _(project)_**   
Memory layer read request latencies   
`DELTA`, `DISTRIBUTION`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Distribution of server read request latencies for a table that attempted to reach the memory layer. The latency is measured between the time when Cloud Bigtable (behind the Google frontend) receives an RPC and the time when it sends back the last byte of the response. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`memory_access`: Whether the memory read was successful in this request.   
`memory_layer/read_request_count` BETA ** _(project)_**   
Memory layer read request count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of read requests for a table that went to the memory layer, broken down by whether the memory read was successful. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`memory_access`: Whether the memory read was successful in this request.   
`memory_layer/request_unit_count` BETA ** _(project)_**   
Memory layer request unit count   
`DELTA`, `DOUBLE`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The Request-Unit usage for read requests that attempt to use the memory layer. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`memory_access`: Whether the memory read was successful in this request.   
`memory_layer/storage_capacity` BETA ** _(project)_**   
Memory layer storage capacity   
`GAUGE`, `INT64`, `By`   
**[bigtable_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_cluster)** |  _Memory layer storage capacity in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`replication/latency` GA ** _(project)_**   
Replication latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Distribution of the replication latencies of mutations to a table, measured as the difference between the commit time at the source and destination clusters. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`source_cluster`: Source cluster of the replicated data.   
`source_zone`: Source zone of the replicated data.   
`replication/max_delay` GA ** _(project)_**   
Replication maximum delay   
`GAUGE`, `DOUBLE`, `s`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Upper bound for replication delay between clusters of a table. Indicates the time frame during which latency information may not be accurate. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`source_cluster`: Source cluster of the replicated data.   
`source_zone`: Source zone of the replicated data.   
`server/data_boost/eligibility_count` GA ** _(project)_**   
Data Boost traffic eligibility count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Current Bigtable requests that are eligible and ineligible for Data Boost. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`app_profile`: Cloud Bigtable application profile.   
`eligibility`: Whether request is eligible for Data Boost.   
`server/data_boost/ineligible_reasons` GA ** _(project)_**   
Data Boost traffic ineligible reasons   
`GAUGE`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Reasons that current traffic is ineligible for Data Boost. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`app_profile`: Cloud Bigtable application profile.   
`ineligible_reason`: Reason that request is ineligible for Data Boost.   
`server/data_boost/spu_usage` GA ** _(project)_**   
Data Boost SPU Usage   
`GAUGE`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _The Serverless-Processing-Units usage (in SPU-seconds) for Data Boost requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`app_profile`: Cloud Bigtable application profile.   
`method`: Cloud Bigtable API method.   
`server/error_count` GA ** _(project)_**   
Error count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of server requests for a table that failed with an error. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`error_code`: gRPC Error Code.   
`app_profile`: Cloud Bigtable application profile.   
`server/latencies` GA ** _(project)_**   
Server Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Distribution of server request latencies for a table. The latency is measured between the time when Cloud Bigtable (behind the Google frontend) receives an RPC and the time when it sends back the last byte of the response. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/modified_rows_count` GA ** _(project)_**   
Modified rows   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of rows modified by server requests for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/multi_cluster_failovers_count` GA ** _(project)_**   
Multi-cluster failovers   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of failovers during multi-cluster requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/read_latencies_by_storage_tier` BETA ** _(project)_**   
Server Read Latencies by Storage Tier   
`DELTA`, `DISTRIBUTION`, `ms`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Distribution of server read request latencies by storage tier for a table. The latency is measured between the time when Cloud Bigtable (behind the Google frontend) receives an RPC and the time when it sends back the last byte of the response. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`storage_tier`: Type of storage tier accessed in the request (ssd, infrequent_access, ssd+infrequent_access, or unknown).   
`server/read_request_count_by_storage_tier` BETA ** _(project)_**   
Read request count by Storage Tier   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of server read requests by storage tier for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`storage_tier`: Type of storage tier accessed in the request (ssd, infrequent_access, ssd+infrequent_access, or unknown).   
`server/received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of bytes of request data received by servers for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of server requests for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/request_max_per_minute_count` GA ** _(project)_**   
Five-second maximum requests per minute   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Maximum number of requests received in a five-second span per minute. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/returned_rows_count` GA ** _(project)_**   
Returned rows   
`DELTA`, `INT64`, `1`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of rows returned by server requests for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`server/sent_bytes_count` GA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Number of bytes of response data sent by servers for a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Bigtable API method.   
`app_profile`: Cloud Bigtable application profile.   
`table/bytes_transferred_to_infrequent_access` BETA ** _(project)_**   
Data moved to infrequent access storage   
`GAUGE`, `INT64`, `By`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Amount of uncompressed data moved to infrequent access storage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`table/bytes_used` GA ** _(project)_**   
Data stored   
`GAUGE`, `INT64`, `By`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Amount of compressed data stored in a table. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`storage_type`: Type of disk storage (ssd, hdd, or infrequent_access).   
`table/change_stream_log_used_bytes` GA ** _(project)_**   
Change stream data   
`GAUGE`, `INT64`, `By`   
**[bigtable_table](https://docs.cloud.google.com/monitoring/api/resources#tag_bigtable_table)** |  _Amount of disk storage used by the change stream logs. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`storage_type`: Type of disk storage.   
  
Table generated at 2026-10-08 15:22:12 UTC.

## What's next

  * [Learn more about Bigtable Monitoring.](https://docs.cloud.google.com/bigtable/docs/monitoring-instance)
  * [Explore metrics available in Key Visualizer.](https://docs.cloud.google.com/bigtable/docs/keyvis-overview)
  * [View the full list of Google Cloud metrics.](https://docs.cloud.google.com/monitoring/api/metrics_gcp)
  * [Learn about the kinds of metrics.](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types#metric-kinds)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
