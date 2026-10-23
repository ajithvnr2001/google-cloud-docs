---
url: https://docs.cloud.google.com/spanner/docs/metrics/
title: Metrics \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:10.484384+00:00
---

# Metrics  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Metrics Stay organized with collections  Save and categorize content based on your preferences. 

The following Spanner metrics are provided to Cloud Monitoring. For the best performance debugging results, use server-side metrics with [client-side metrics](https://docs.cloud.google.com/spanner/docs/view-manage-client-side-metrics).

The "metric type" strings in this table must be prefixed with `spanner.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`api/adapter_request_count` GA ** _(project)_**   
Adapter API requests   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Cloud Spanner Adapter API requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`status`: Request call result, ok=success.   
`method`: Cloud Spanner Adapter API method.   
`protocol`: Adapter protocol.   
`message_type`: Adapter protocol message type.   
`adapter_status`: Adapter protocol request result.   
`op_type`: Operation type.   
`api/adapter_request_latencies` GA ** _(project)_**   
Adapter request latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of server request latencies for a database. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`method`: Cloud Spanner Adapter API method.   
`protocol`: Adapter protocol.   
`message_type`: Adapter protocol message type.   
`op_type`: Operation type.   
`api/api_request_count` GA ** _(project)_**   
API requests   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Cloud Spanner API requests. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`status`: Request call result, ok=success.   
`method`: Cloud Spanner API method.   
`api/mcp_request_count` GA ** _(project)_**   
MCP request rate   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Rate of Cloud Spanner MCP requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: Request call result, ok=success.   
`tool`: The name of the MCP tool.   
`database`: Target database.   
`api/mcp_request_latencies` GA ** _(project)_**   
MCP request latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of MCP request latencies. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`tool`: The name of the MCP tool.   
`database`: Target database.   
`api/read_request_count_by_serving_location` BETA ** _(project)_**   
Read API request by serving location   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Cloud Spanner Read API requests by serving location, whether it is a directed read query, and whether it is a change stream query. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`is_change_stream`: (BOOL) TRUE if it is a change stream query.   
`is_directed_read`: (BOOL) TRUE if it is a directed read query.   
`status`: Request call result, OK=success.   
`serving_location`: The location of serving replicas.   
`api/read_request_latencies_by_change_stream` GA ** _(project)_**   
Read request latencies by change stream   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of read request latencies by whether it is a change stream query. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`is_change_stream`: (BOOL) TRUE if it is a change stream query.   
`api/read_request_latencies_by_serving_location` BETA ** _(project)_**   
Read API request latencies by serving location   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of read request latencies by serving location, whether it is a directed read query, and whether it is a change stream query. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. This is a superset of spanner.googleapis.com/api/read_request_latencies_by_change_stream. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`is_change_stream`: (BOOL) TRUE if it is a change stream query.   
`is_directed_read`: (BOOL) TRUE if it is a directed read query.   
`serving_location`: The location of serving replicas.   
`api/received_bytes_count` GA ** _(project)_**   
Bytes received by Cloud Spanner   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Uncompressed request bytes received by Cloud Spanner. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`api/request_count` GA ** _(project)_**   
API request rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Rate of Cloud Spanner API requests. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`status`: Request call result, ok=success.   
`method`: Cloud Spanner API method.   
`api/request_count_per_protocol` GA ** _(project)_**   
API request rate per protocol   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Rate of Cloud Spanner API requests per protocol. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: Request call result, ok=success.   
`region`: The region where the request was served.   
`protocol`: Protocl used for this request.   
`method`: Cloud Spanner API method.   
`response_code`: (INT64) HTTP response code received, such as 200 or 500.   
`op_type`: Operation type.   
`database`: Target database.   
`api/request_count_per_transaction_options` GA ** _(project)_**   
API requests by transaction options   
`GAUGE`, `DOUBLE`, `1/s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Cloud Spanner API request rate by transaction options. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`status`: Request call result, ok=success.   
`op_type`: Operation type ("read", "write" or "other").   
`response_code`: HTTP response code received, such as 200 or 500.   
`lock_mode`: The read lock mode used if within a read-write transaction ("PESSIMISTIC" or "OPTIMISTIC").   
`isolation_level`: The isolation level used if within a read-write transaction ("SERIALIZABLE" or "REPEATABLE_READ").   
`region`: The region where the request was served.   
`transaction_type`: Transaction type ("READ_ONLY", "READ_WRITE", "PARTITIONED_DML" or "NONE").   
`api/request_latencies` GA ** _(project)_**   
Request latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of server request latencies for a database. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`api/request_latencies_by_transaction_type` GA ** _(project)_**   
Request latencies by transaction type   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of server request latencies by transaction types. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`transaction_type`: Transaction type ("READ_ONLY" or "READ_WRITE").   
`is_leader_involved`: (BOOL) TRUE if the leader roundtrip call is issued.   
`api/request_latencies_per_protocol` GA ** _(project)_**   
Request latencies per protocol   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of server request latencies for a database per protocol. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`region`: The region where the request was served.   
`protocol`: Protocl used for this request.   
`method`: Cloud Spanner API method.   
`op_type`: Operation type.   
`database`: Target database.   
`api/request_latencies_per_transaction_options` GA ** _(project)_**   
Request latencies by transaction options   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of server request latencies by transaction options for a database. This includes latency of request processing in Cloud Spanner backends and API layer. It does not include network or reverse-proxy overhead between clients and servers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`op_type`: Operation type ("read", "write" or "other").   
`lock_mode`: The read lock mode used if within a read-write transaction ("PESSIMISTIC" or "OPTIMISTIC").   
`isolation_level`: The isolation level used if within a read-write transaction ("SERIALIZABLE" or "REPEATABLE_READ").   
`is_leader_involved`: (BOOL) TRUE if the leader roundtrip call is issued.   
`region`: The region where the request was served.   
`transaction_type`: Transaction type ("READ_ONLY", "READ_WRITE", "PARTITIONED_DML" or "NONE").   
`api/sent_bytes_count` GA ** _(project)_**   
Bytes sent by Cloud Spanner   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Uncompressed response bytes sent by Cloud Spanner. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`method`: Cloud Spanner API method.   
`client/afe_connectivity_error_count` GA ** _(project)_**   
AFE Connectivity Error Count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of requests that failed to reach the Spanner API Frontend. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/afe_latencies` GA ** _(project)_**   
AFE Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Latency between Spanner API Frontend receiving an RPC and starting to write back the response. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/attempt_count` GA ** _(project)_**   
Attempt Count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _The total number of RPC attempt performed by the Spanner client. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner attempt status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/attempt_latencies` GA ** _(project)_**   
Attempt Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of the total end-to-end latency across a RPC attempt. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner attempt status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/gfe_connectivity_error_count` GA ** _(project)_**   
GFE Connectivity Error Count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of requests that failed to reach the Google network. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/gfe_latencies` GA ** _(project)_**   
GFE Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Latency between Google network(GFE) receiving an RPC and reading back the first byte of the response. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/operation_count` GA ** _(project)_**   
Operation Count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _The total number of operations performed by the Spanner client. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`client/operation_latencies` GA ** _(project)_**   
Operation Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of the total end-to-end latency across all RPC attempts associated with a Spanner operation. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`method`: Cloud Spanner API method.   
`database`: Target database.   
`status`: Cloud Spanner operation status.   
`client_name`: Cloud Spanner client name.   
`directpath_enabled`: (BOOL) True if directpath is enabled.   
`directpath_used`: (BOOL) True if directpath is used for the RPC request.   
`graph_algorithm_stat/total/execution_count` GA ** _(project)_**   
Graph algorithm execution count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total graph algorithm requests received by Cloud Spanner during the time interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`algorithm`: Graph algorithm executed.   
`graph_algorithm_stat/total/execution_durations` GA ** _(project)_**   
Graph algorithm durations   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of graph algorithm execution times (in seconds) within the database. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`algorithm`: Graph algorithm executed.   
`graph_algorithm_stat/total/failed_execution_count` GA ** _(project)_**   
Graph algorithm failed count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total failed graph algorithm requests in Cloud Spanner during the time interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`algorithm`: Graph algorithm executed.   
`status`: failed status, one of [cancelled, timeout, error].   
`graph_query_stat/total/bytes_returned_count` GA ** _(project)_**   
Graph query bytes returned count   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of data bytes that the graph queries returned, excluding transmission encoding overhead. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`graph_query_stat/total/execution_count` GA ** _(project)_**   
Graph query execution count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of times Cloud Spanner saw graph queries during the interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`graph_query_stat/total/failed_execution_count` GA ** _(project)_**   
Graph query failures   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of times graph queries failed during the interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`status`: failed status, one of [cancelled, timeout, error].   
`graph_query_stat/total/query_latencies` GA ** _(project)_**   
Graph query latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of total length of time, in seconds, for graph query executions within the database. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`graph_query_stat/total/returned_rows_count` GA ** _(project)_**   
Graph query rows returned count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows that the graph queries returned. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`graph_query_stat/total/scanned_rows_count` GA ** _(project)_**   
Graph query rows scanned count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows that the graph queries scanned excluding deleted values. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`instance/autoscaling/high_priority_cpu_utilization_target` GA ** _(project)_**   
Autoscaling high priority cpu utilization target   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _High priority CPU utilization target used for autoscaling. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/max_node_count` GA ** _(project)_**   
Autoscaling max nodes   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Maximum number of nodes autoscaler is allowed to allocate to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/max_processing_units` GA ** _(project)_**   
Autoscaling max processing units   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Maximum number of processing units autoscaler is allowed to allocate to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/min_node_count` GA ** _(project)_**   
Autoscaling min nodes   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Minimum number of nodes autoscaler is allowed to allocate to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/min_processing_units` GA ** _(project)_**   
Autoscaling min processing units   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Minimum number of processing units autoscaler is allowed to allocate to the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/storage_utilization_target` GA ** _(project)_**   
Autoscaling storage utilization target   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage utilization target used for autoscaling. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/autoscaling/total_cpu_utilization_target` GA ** _(project)_**   
Autoscaling total cpu utilization target   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total CPU utilization target used for autoscaling. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._  
`instance/backup/used_bytes` GA ** _(project)_**   
Backup storage used   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Backup storage used in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`backup`: Target backup.   
`instance/cpu/smoothed_utilization` GA ** _(project)_**   
Smoothed CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _24-hour smoothed utilization of provisioned CPU. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`instance/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Percent utilization of provisioned CPU. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`instance/cpu/utilization_by_operation_type` GA ** _(project)_**   
CPU utilization by operation type   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Percent utilization of provisioned CPU, by operation type. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). Currently, it does not include CPU utilization for system tasks. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`is_system`: (BOOL) TRUE if the number is system CPU utilization.   
`priority`: Task priority ("high" or "medium" or "low").   
`category`: Operation type ("read_readonly", "beginorcommit" etc).   
`instance/cpu/utilization_by_priority` GA ** _(project)_**   
CPU utilization by priority   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Percent utilization of provisioned CPU, by priority. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`is_system`: (BOOL) TRUE if the number is system CPU utilization.   
`priority`: Task priority ("high", "medium", or "low").   
`instance/cross_region_replicated_bytes_count` GA ** _(project)_**   
Cross region replicated bytes   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of bytes replicated from preferred leader to replicas across regions. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`source_region`: Preferred leader region.   
`destination_region`: Cloud Spanner region the data is replicated to.   
`tag`: Type of transaction contributing to replication.   
`instance/data_boost/processing_unit_second_count` GA ** _(project)_**   
Processing unit second   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total processing units used for DataBoost operations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`credential_id`: The IAM credential ID.   
`instance/disk_load` GA ** _(project)_**   
Disk load   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Percent utilization of HDD disk load in an instance. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`instance/dual_region_quorum_availability` GA ** _(project)_**   
Dual Region Quorum Availability   
`GAUGE`, `BOOL`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Quorum availability signal for dual region instance configs. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`quorum_availability`: Quorum availability level.   
`instance/edition/feature_usage` GA ** _(project)_**   
Feature usage   
`GAUGE`, `BOOL`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Indicates if an edition feature is being used by the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`feature`: Edition feature.   
`database`: Database using the feature, if any.   
`used_in_query_path`: (BOOL) Used in query path, or not.   
`instance/leader_percentage_by_region` GA ** _(project)_**   
Leader percentage by region   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Percentage of leaders by cloud region. Values are typically numbers between 0.0 and 1.0, charts display the values as a percentage between 0% and 100%. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`region`: Cloud region containing the leaders.   
`instance/node_count` GA ** _(project)_**   
Nodes   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total number of nodes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/peak_split_cpu_usage_score` GA ** _(project)_**   
Peak split cpu usage score   
`GAUGE`, `DOUBLE`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Maximum cpu usage score observed in a database across all splits. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`instance/placement_row_limit` GA ** _(project)_**   
Placement row limit   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Upper limit for placement rows. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`instance/placement_row_limit_per_processing_unit` GA ** _(project)_**   
Placement row limit per processing unit   
`GAUGE`, `DOUBLE`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Upper limit for placement rows per processing unit. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`instance/placement_rows` GA ** _(project)_**   
Placement row count by database   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of placement rows in a database. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`instance/processing_units` GA ** _(project)_**   
Processing units   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total number of processing units. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/replica/autoscaling/high_priority_cpu_utilization_target` GA ** _(project)_**   
Autoscaling high priority cpu utilization target for replica   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _High priority CPU utilization target used for autoscaling replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/autoscaling/max_node_count` GA ** _(project)_**   
Autoscaling max nodes for replica   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Maximum number of nodes autoscaler is allowed to allocate to the replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/autoscaling/max_processing_units` GA ** _(project)_**   
Autoscaling max processing units for replica   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Maximum number of processing units autoscaler is allowed to allocate to the replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/autoscaling/min_node_count` GA ** _(project)_**   
Autoscaling min nodes for replica   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Minimum number of nodes autoscaler is allowed to allocate to the replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/autoscaling/min_processing_units` GA ** _(project)_**   
Autoscaling min processing units for replica   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Minimum number of processing units autoscaler is allowed to allocate to the replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/autoscaling/total_cpu_utilization_target` GA ** _(project)_**   
Autoscaling total cpu utilization target for replica   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total CPU utilization target used for autoscaling replica. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/cmek/total_keys` BETA ** _(project)_**   
CMEK keys   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of CMEK keys identified by database and key revocation status. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`is_key_revoked`: (BOOL) True if the CloudKMS key is revoked.   
`instance/replica/node_count` GA ** _(project)_**   
Replica nodes   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of nodes allocated to each replica identified by location and replica type. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/replica/processing_units` GA ** _(project)_**   
Replica processing units.   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of processing units allocated to each replica identified by location and replica type. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`location`: Replica location.   
`replica_type`: Replica type.   
`instance/schema_object_count_limit` GA ** _(project)_**   
Schema objects count limit   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _The schema object count limit for the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`instance/schema_objects` GA ** _(project)_**   
Schema object count   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _The total count of schema objects in the database. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`instance/session_count` GA ** _(project)_**   
Sessions   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of sessions in use. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`instance/storage/columnar_used_bytes` BETA ** _(project)_**   
Storage used (logical) for columnar storage   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage used (logical) in bytes for columnar storage. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`storage_class`: Storage type.   
`instance/storage/columnar_used_bytes_by_region` BETA ** _(project)_**   
Storage used (logical) for columnar storage by region   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage used (logical) in bytes for columnar storage by cloud region. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`storage_class`: Storage type.   
`instance/storage/combined/limit_bytes` GA ** _(project)_**   
Storage limit (combined)   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage limit (combined) for instance in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/storage/combined/limit_bytes_per_processing_unit` GA ** _(project)_**   
Storage limit (combined) per processing unit   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage limit (combined) per processing unit in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/storage/combined/utilization` GA ** _(project)_**   
Storage utilization (combined)   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage used (combined) as a fraction of storage limit (combined). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`instance/storage/limit_bytes` GA ** _(project)_**   
Storage limit   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage limit for instance in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_class`: Storage type.   
`instance/storage/limit_bytes_per_processing_unit` GA ** _(project)_**   
Storage limit per processing unit   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage limit per processing unit in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_class`: Storage type.   
`instance/storage/used_bytes` GA ** _(project)_**   
Storage used   
`GAUGE`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage used in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Target database.   
`storage_class`: Storage type.   
`instance/storage/utilization` GA ** _(project)_**   
Storage utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Storage used as a fraction of storage limit. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`storage_class`: Storage type.   
`lock_stat/total/lock_wait_time` GA ** _(project)_**   
Lock wait time   
`DELTA`, `DOUBLE`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total lock wait time for lock conflicts recorded for the entire database. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`pending_restore_count` GA ** _(project)_**   
Pending restore count   
`GAUGE`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Limits number of pending restores per instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`query_count` GA ** _(project)_**   
Count of queries   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of queries by database name, status, query type, and used optimizer version. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`status`: Request call result, ok=success.   
`query_type`: Type of query.   
`optimizer_version`: (INT64) Optimizer version used by the query.   
`query_stat/total/bytes_returned_count` GA ** _(project)_**   
Bytes returned count   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of data bytes that the queries returned, excluding transmission encoding overhead. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`query_stat/total/cpu_time` GA ** _(project)_**   
Query cpu time   
`DELTA`, `DOUBLE`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of seconds of CPU time Cloud Spanner spent on operations to execute the queries. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`query_stat/total/execution_count` GA ** _(project)_**   
Query execution count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of times Cloud Spanner saw queries during the interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`query_stat/total/failed_execution_count` GA ** _(project)_**   
Query failures   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of times queries failed during the interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`status`: failed status, one of [cancelled, timeout, error].   
`query_stat/total/query_latencies` GA ** _(project)_**   
Query latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of total length of time, in seconds, for query executions within the database. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`query_stat/total/remote_service_calls_count` GA ** _(project)_**   
Remote service calls count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of remote service calls. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`service`: Target remote service.   
`response_code`: (INT64) HTTP response code received, such as 200 or 500.   
`query_stat/total/remote_service_calls_latencies` GA ** _(project)_**   
Remote service calls latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Latency of remote service calls. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`service`: Target remote service.   
`response_code`: (INT64) HTTP response code received, such as 200 or 500.   
`query_stat/total/remote_service_network_bytes_sizes` GA ** _(project)_**   
Remote service network bytes   
`DELTA`, `DISTRIBUTION`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Network bytes exchanged with remote service. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`service`: Target remote service.   
`direction`: Direction of traffic: sent or received.   
`query_stat/total/remote_service_processed_rows_count` GA ** _(project)_**   
Remote service rows count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of rows processed by a remote service. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`service`: Target remote service.   
`response_code`: (INT64) HTTP response code received, such as 200 or 500.   
`query_stat/total/remote_service_processed_rows_latencies` GA ** _(project)_**   
Remote service rows latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Latency of rows processed by a remote service. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`service`: Target remote service.   
`response_code`: (INT64) HTTP response code received, such as 200 or 500.   
`query_stat/total/returned_rows_count` GA ** _(project)_**   
Rows returned count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows that the queries returned. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`query_stat/total/scanned_rows_count` GA ** _(project)_**   
Rows scanned count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows that the queries scanned excluding deleted values. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`queue/active_receive_tvf_queries` BETA ** _(project)_**   
Active receive Table-Valued Function (TVF) queries   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of active receive table-valued function (TVF) queries in the queue. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/buffered_in_flight_messages` BETA ** _(project)_**   
Buffered in-flight messages   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of in-flight messages in the queue that are currently leased and buffered in memory. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/buffered_ready_messages` BETA ** _(project)_**   
Buffered ready messages   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of ready messages in the queue that are buffered in memory and available for delivery. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/lease_expiration_count` BETA ** _(project)_**   
Lease expirations   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of expired message leases. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/message_ack_count` BETA ** _(project)_**   
Messages acknowledged   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of messages acknowledged. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/message_payload_sizes` BETA ** _(project)_**   
Message payload sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of message payload sizes in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/message_send_count` BETA ** _(project)_**   
Messages sent   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of messages sent. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`queue/oldest_unacked_message_age` BETA ** _(project)_**   
Oldest unacked message age   
`GAUGE`, `INT64`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Age of the oldest unacknowledged message in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`database`: Target database.   
`queue`: Target queue.   
`quota/internal/instance_admin_update_instance_requests/exceeded` ALPHA ** _(project)_**   
Instance update requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Number of attempts to exceed the limit on quota metric spanner.googleapis.com/internal/instance_admin_update_instance_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal/instance_admin_update_instance_requests/limit` ALPHA ** _(project)_**   
Instance update requests quota limit   
`GAUGE`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Current limit on quota metric spanner.googleapis.com/internal/instance_admin_update_instance_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal/instance_admin_update_instance_requests/usage` ALPHA ** _(project)_**   
Instance update requests quota usage   
`DELTA`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Current usage on quota metric spanner.googleapis.com/internal/instance_admin_update_instance_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/pending_restore_count/exceeded` GA ** _(project)_**   
Pending restore count quota exceeded error   
`DELTA`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Number of attempts to exceed the limit on quota metric spanner.googleapis.com/pending_restore_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/pending_restore_count/limit` GA ** _(project)_**   
Pending restore count quota limit   
`GAUGE`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Current limit on quota metric spanner.googleapis.com/pending_restore_count. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/pending_restore_count/usage` GA ** _(project)_**   
Pending restore count quota usage   
`GAUGE`, `INT64`, `1`   
**[spanner.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner.googleapis.com/Instance)** |  _Current usage on quota metric spanner.googleapis.com/pending_restore_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`read_stat/total/bytes_returned_count` GA ** _(project)_**   
Bytes returned count   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Total number of data bytes that the reads returned excluding transmission encoding overhead. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/client_wait_time` GA ** _(project)_**   
Client wait time   
`DELTA`, `DOUBLE`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of seconds spent waiting due to throttling. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/cpu_time` GA ** _(project)_**   
Read cpu time   
`DELTA`, `DOUBLE`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of seconds of CPU time Cloud Spanner spent execute the reads excluding prefetch CPU and other overhead. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/execution_count` GA ** _(project)_**   
Read execution count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of times Cloud Spanner executed the read shapesduring the interval. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/leader_refresh_delay` GA ** _(project)_**   
Leader refresh delay   
`DELTA`, `DOUBLE`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of seconds spent coordinating reads across instances in multi-regionconfigurations. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/locking_delays` GA ** _(project)_**   
Locking delays   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of total time in seconds spent waiting due to locking. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`read_stat/total/returned_rows_count` GA ** _(project)_**   
Rows returned count   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows that the reads returned. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`row_deletion_policy/deleted_rows_count` GA ** _(project)_**   
Rows deleted   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Count of rows deleted by the policy since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`row_deletion_policy/processed_watermark_age` GA ** _(project)_**   
Processed watermark age   
`GAUGE`, `INT64`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Time between now and the read timestamp of the last successful execution. An execution happens as the background task deletes eligible data in batches and is successful even when there are rows that cannot be deleted. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`row_deletion_policy/undeletable_rows` GA ** _(project)_**   
Total number of undeletable rows   
`GAUGE`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of rows in all tables in the database that can't be deleted. A row can't be deleted if, for example, it has so many child rows that a delete would exceed the transaction limit. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`database`: Target database.   
`transaction_stat/total/bytes_written_count` GA ** _(project)_**   
Bytes written   
`DELTA`, `INT64`, `By`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of bytes written by transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`transaction_stat/total/commit_attempt_count` GA ** _(project)_**   
Transaction commit attempts   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of commit attempts for transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`status`: Commit status ("success", "abort", or "precondition_failure")   
`transaction_stat/total/commit_retry_count` GA ** _(project)_**   
Transaction commit retries   
`DELTA`, `INT64`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Number of commit attempts that are retries from previously aborted transaction attempts. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`transaction_stat/total/participants` GA ** _(project)_**   
Transaction participants   
`DELTA`, `DISTRIBUTION`, `1`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of total number of participants in each commit attempt. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
`transaction_stat/total/transaction_latencies` GA ** _(project)_**   
Transaction latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[spanner_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_spanner_instance)** |  _Distribution of total seconds takenfrom the first operation of the transaction to commit or abort. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`database`: Target database.   
  
Table generated at 2026-10-14 20:24:33 UTC.

## What's next

  * [View and manage client-side metrics](https://docs.cloud.google.com/spanner/docs/view-manage-client-side-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
