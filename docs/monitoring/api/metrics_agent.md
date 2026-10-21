---
url: https://docs.cloud.google.com/monitoring/api/metrics_agent/
title: Legacy Monitoring and Logging agent metrics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:27.245195+00:00
---

# Legacy Monitoring and Logging agent metrics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Legacy Monitoring and Logging agent metrics Stay organized with collections  Save and categorize content based on your preferences. 

When you install the legacy Cloud Monitoring and Cloud Logging agents on your VM instances, the agents transmit data for the metric types listed in this document to Monitoring. For information about choosing the right agent, see [Ops Agent overview](https://docs.cloud.google.com/monitoring/agent/ops-agent).

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

**Important:** You must install the legacy Monitoring agent to collect most of the metrics listed in this document. The Ops Agent collects similar metrics, with a few differences; see [Ops Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent) for the list of Ops Agent metrics, and Metrics from the Ops Agent and the legacy Monitoring agent for the list of differences. 

To collect the metrics labeled "logging agent" in the "agent" table, you must install the legacy Logging agent.

## About the tables of metrics

The tables of metrics provide formatted versions of the publicly available [metric descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor). This section provides additional information to help you interpret and use these descriptors.

  * For a general explanation of the entries in the tables, including information about values like `DELTA` and `GAUGE`, see [Metric types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

To chart or monitor metric types with values of type `STRING`, you must use Monitoring Query Language (MQL), and you must convert the value into a numeric value. For information about MQL string-conversion methods, see [`String`](https://docs.cloud.google.com/monitoring/mql/reference#string-group).

  * For information about the units used in the metric lists, see the [`unit` field](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.unit) in the `MetricDescriptor` reference.

  * For information about statements of the form “Sampled every _x_ seconds” and “After sampling, data is not visible for up to _y_ seconds”, see [Additional information: metadata](https://docs.cloud.google.com/monitoring/api/metrics#metadata).

  * The resource-hierarchy level tells you if the metric is written at the project, organization, or folder level(s). When the level is not specified in the metric descriptor, the metric writes at the project level by default.



  * The metric types in the table titled "agent" are free; the other types are chargeable. For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).


  * For information about the meaning of launch stages such as `GA` (General Availability) and `BETA` (Preview), see [Product launch stages](https://cloud.google.com/products#product-launch-stages).



## Metrics from the Ops Agent and the legacy Monitoring agent

The legacy Monitoring agent has two entirely different implementations, one for Linux VMs and one for Windows VMs. The Ops Agent runs on both Linux and Windows VMs.

### Differences in metric collection

**Note:** Metrics with a description that includes the statement _"Linux only"_ aren't collected by the legacy Monitoring agent for Windows VMs. However, the Ops Agent collects those metrics on both Linux and Windows VMs. The following table describes differences in the data ingested by the Ops Agent and the legacy Monitoring agent. Metric type, omitting  
`agent.googleapis.com` | Ops Agent (GA)† | Ops Agent (Preview)† | Legacy Monitoring agent  
---|---|---|---  
[ `cpu_state`](https://docs.cloud.google.com/monitoring/api/metrics_agent#cpu/utilization) | The possible values for Windows are `idle`, `interrupt,`   
`system` and `user`. | The possible values for Windows are `idle`, `interrupt,`   
`system` and `user`. | The possible values for Windows are `idle` and `used`.   
[ `disk/bytes_used`](https://docs.cloud.google.com/monitoring/api/metrics_agent#disk/bytes_used) and  
[ `disk/percent_used`](https://docs.cloud.google.com/monitoring/api/metrics_agent#disk/percent_used) | Ingested with the full path in the `device` label; for example, `/dev/sda15`.  
  
Not ingested for virtual devices like `tmpfs` and `udev`. | Ingested without `/dev` in the path in the `device` label; for example, `sda15`.  
  
Ingested for virtual devices like `tmpfs` and `udev`. | Ingested without `/dev` in the path in the `device` label; for example, `sda15`.  
  
Ingested for virtual devices like `tmpfs` and `udev`.  
†The **GA** column refers to Ops Agent versions 2.0.0 and higher. The **Preview** column refers to Ops Agent versions less than 2.0.0.

## Agent metrics

Metrics from the [Monitoring agent](https://docs.cloud.google.com/monitoring/agent) and from the [Logging agent](https://docs.cloud.google.com/logging/docs/agent) running on VM instances in Google Cloud and AWS.

The following list was last generated at 2026-05-14 16:07:40 UTC. For more information about this process, see [ About the lists](https://docs.cloud.google.com/monitoring/api/metrics#generated).

### agent

Metrics from the default configuration for the legacy Linux [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/agent/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`api_request_count` GA ** _(project)_**   
Monitoring Agent API Request Count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of API requests from the Monitoring agent. Linux only. Sampled every 60 seconds._   
`state`: Request state.   
`log_entry_count` GA ** _(project)_**   
Logging Agent Log Entry Count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of log entries written by the Logging agent. Linux only. Sampled every 60 seconds._   
`response_code`: Numeric response code from both the gRPC and HTTP error spaces.   
`log_entry_retry_count` GA ** _(project)_**   
Logging Agent Retried Log Entry Writes Count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of log-entry writes that were retried by the Logging agent. Linux only. Sampled every 60 seconds._   
`response_code`: Numeric response code from both the gRPC and HTTP error spaces.   
`memory_usage` GA ** _(project)_**   
Monitoring Agent Memory Usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Memory in use by the Monitoring agent. Linux only. Sampled every 60 seconds._  
`monitoring/point_count` GA ** _(project)_**   
Monitoring Agent Metric Point Count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of metric points written by the agent to Cloud Monitoring. Linux only. Sampled every 60 seconds._   
`status`: gRPC response code.   
`request_count` GA ** _(project)_**   
Logging Agent API Request Count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of API requests from the Logging agent. Linux only. Sampled every 60 seconds._   
`response_code`: Numeric response code from both the gRPC and HTTP error spaces.   
`streamspace_size` GA ** _(project)_**   
Monitoring Agent Process Labels Size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Estimated total size of process labels written by the Monitoring agent over a 24-hour window. Linux only. Sampled every 60 seconds._  
`streamspace_size_throttling` GA ** _(project)_**   
Monitoring Agent is Throttling Processes   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Whether the Monitoring agent is currently throttling process metrics. Linux only. Sampled every 60 seconds._  
`uptime` GA ** _(project)_**   
Monitoring/Logging Agent Uptime   
`CUMULATIVE`, `INT64`, `s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Uptime of Monitoring agent or Logging agent. Linux only. Sampled every 60 seconds._   
`version`: Agent version.   
  
### apache

Metrics from [apache](https://docs.cloud.google.com/monitoring/agent/plugins/apache). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/apache/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`connections` GA ** _(project)_**   
Open connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of active connections currently attached to the HTTP server. Sampled every 60 seconds._   
`server_name`: The name of the Apache HTTP server.   
`idle_workers` GA ** _(project)_**   
Idle workers   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of idle workers currently attached to the HTTP server. Sampled every 60 seconds._   
`server_name`: The name of the Apache HTTP server.   
`request_count` GA ** _(project)_**   
Requests   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total requests serviced by the HTTP server. Sampled every 60 seconds._   
`server_name`: The name of the Apache HTTP server.   
`scoreboard` GA ** _(project)_**   
Scoreboard   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Apache HTTP server scoreboard values. Sampled every 60 seconds._   
`server_name`: The name of the Apache HTTP server.   
`state`: The scoreboard state name.   
`traffic` GA ** _(project)_**   
Traffic   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total HTTP server traffic. Sampled every 60 seconds._   
`server_name`: The name of the Apache HTTP server.   
  
### cassandra

Metrics from [cassandra](https://docs.cloud.google.com/monitoring/agent/plugins/cassandra). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/cassandra/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`cache/hits` GA ** _(project)_**   
Hit count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Key cache hit count for the table. Sampled every 60 seconds._   
`cache`: The name of the cache.   
`client_request/latency/50p` GA ** _(project)_**   
Read latency   
`GAUGE`, `DOUBLE`, `us`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Latency of standard read requests. Sampled every 60 seconds._   
`operation`: The storage operation name.   
`client_request/latency/95p` GA ** _(project)_**   
Read latency   
`GAUGE`, `DOUBLE`, `us`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Latency of standard read requests. Sampled every 60 seconds._   
`operation`: The storage operation name.   
`client_request/latency/99p` GA ** _(project)_**   
Read latency   
`GAUGE`, `DOUBLE`, `us`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Latency of standard read requests. Sampled every 60 seconds._   
`operation`: The storage operation name.   
`client_request/latency/max` GA ** _(project)_**   
Read latency   
`GAUGE`, `DOUBLE`, `us`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Latency of standard read requests. Sampled every 60 seconds._   
`operation`: The storage operation name.   
`column_family/compression_ratio` GA ** _(project)_**   
Compression ratio   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current compression ratio for all SSTables. Sampled every 60 seconds._  
`column_family/max_row_size` GA ** _(project)_**   
Max row size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Size of the largest compacted row. Sampled every 60 seconds._  
`commitlog_total_size` GA ** _(project)_**   
Commit log size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current data size of all commit log segments. Sampled every 60 seconds._  
`completed_tasks` GA ** _(project)_**   
Completed tasks   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of completed tasks in queue. Sampled every 60 seconds._   
`stage_name`: The name of the queue stage.   
`current_tasks` GA ** _(project)_**   
Tasks   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of tasks in queue with the given task status. Sampled every 60 seconds._   
`stage_name`: The name of the queue stage.   
`task_status`: The status of the task (pending, active).   
`dropped_message/dropped_count` GA ** _(project)_**   
Dropped messages   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of dropped messages for the mutation. Sampled every 60 seconds._   
`operation`: The storage operation name.   
`storage_service_exception_count` GA ** _(project)_**   
Exceptions   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of exceptions thrown by the storage operations. Sampled every 60 seconds._  
`storage_service_load` GA ** _(project)_**   
Storage load   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total disk space used for this node. Sampled every 60 seconds._  
  
### couchdb

Metrics from [couchdb](https://docs.cloud.google.com/monitoring/agent/plugins/couchdb). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/couchdb/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`average_request_time` GA ** _(project)_**   
Request latency   
`GAUGE`, `DOUBLE`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Average request time. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
`httpd/bulk_request_count` GA ** _(project)_**   
Bulk requests   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Bulk requests count. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
`httpd/request_count` GA ** _(project)_**   
Requests   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Requests count. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
`httpd/request_method_count` GA ** _(project)_**   
Request methods   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _HTTP request method count. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
`http_method`: An HTTP request method.   
`httpd/response_code_count` GA ** _(project)_**   
Response codes   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _HTTP response status code count. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
`response_code`: An HTTP status code.   
`httpd/temporary_view_read_count` GA ** _(project)_**   
Temp view reads   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Temporary view reads count. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
`httpd/view_read_count` GA ** _(project)_**   
View reads   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _View reads count. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
`open_databases` GA ** _(project)_**   
Open databases   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of open databases. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
`open_files` GA ** _(project)_**   
Open files   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of open files. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
`read_count` GA ** _(project)_**   
Reads   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Database read count. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
`write_count` GA ** _(project)_**   
Writes   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Database write count. Sampled every 60 seconds._   
`server_name`: The couchdb server name.   
  
### cpu

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) and the legacy [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Compute Engine also reports [similar metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute), but those come from the hypervisor rather than from inside the VM. Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/cpu/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`load_15m` GA ** _(project)_**   
CPU load (15m)   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Load average over the last 15 minutes. Linux only. Sampled every 60 seconds._  
`load_1m` GA ** _(project)_**   
CPU load (1m)   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Load average over the last 1 minute. Linux only. Sampled every 60 seconds._  
`load_5m` GA ** _(project)_**   
CPU load (5m)   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Load average over the last 5 minutes. Linux only. Sampled every 60 seconds._  
`usage_time` GA ** _(project)_**   
CPU usage time (OS reported)   
`CUMULATIVE`, `INT64`, `s{CPU}`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total time the CPU spent in different states. This value is reported from inside the VM and can differ from `compute.googleapis.com/instance/cpu/usage_time`, which is reported by the hypervisor for the VM. Linux only. Sampled every 60 seconds._   
`cpu_number`: CPU number, for example, "0", "1", or "2". This label is only set with certain Monitoring configurations.   
`cpu_state`: CPU state, one of [idle, interrupt, nice, softirq, steal, system, user, wait].   
`utilization` GA ** _(project)_**   
CPU utilization (OS reported)   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Percentage of the total CPU capacity spent in different states. This value is reported from inside the VM and can differ from `compute.googleapis.com/instance/cpu/utilization`, which is reported by the hypervisor for the VM. Sampled every 60 seconds._   
`cpu_number`: CPU number, for example, "0", "1", or "2". This label is only set with certain Monitoring configurations. Linux only.   
`cpu_state`: CPU state, one of [idle, interrupt, nice, softirq, steal, system, user, wait] on Linux, or [idle, interrupt, system, user] from Windows Ops Agent, or [idle, used] from Windows Monitoring agent.   
  
### disk

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) and the legacy [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/disk/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`bytes_used` GA ** _(project)_**   
Disk bytes used   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current number of disk bytes used by state and by partition. Summing the values of all states yields the total available disk space. Linux only. Sampled every 60 seconds._   
`device`: Device name.   
`state`: Type of usage, one of [free, used, reserved].   
`io_time` GA ** _(project)_**   
Disk I/O time   
`CUMULATIVE`, `INT64`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cumulative time spent while I/O operations are in queue and when the disks are busy. The value of this metric increases when there is at least one I/O operation pending or in progress. This value corresponds to Field 10 in the https://www.kernel.org/doc/Documentation/iostats.txt documentation. Linux only. Sampled every 60 seconds._   
`device`: Device name.   
`merged_operations` GA ** _(project)_**   
Disk merged operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of merged disk operations by direction. Linux only. Sampled every 60 seconds._   
`device`: Device name.   
`direction`: Direction, one of [read, write].   
`operation_count` GA ** _(project)_**   
Disk operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of disk operations by direction. Linux only. Sampled every 60 seconds._   
`device`: Device name.   
`direction`: Direction, one of [read, write].   
`operation_time` GA ** _(project)_**   
Disk operation time   
`CUMULATIVE`, `INT64`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Average time to complete a disk operation multiplied by wall clock time. When aligned as a rate, the value is the average time to complete a disk operation. Linux only. Sampled every 60 seconds._   
`device`: Device name.   
`direction`: Direction, one of [read, write].   
`pending_operations` GA ** _(project)_**   
Disk pending operations   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current count of pending disk operations. Linux only. Sampled every 60 seconds._   
`device`: Device name.   
`percent_used` GA ** _(project)_**   
Disk utilization   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current percentage of the disk used by state and by partition. Represents the specific state value divided by the sum of all states; for example, 'used' represents (used / (free + used + reserved)). This differs from the Unix 'df' command, where 'used' means (used / (free + used)). The utilization is between 0.0 and 100.0. Sampled every 60 seconds._   
`device`: Device name.   
`state`: Type of usage, one of [free, used, reserved].   
`read_bytes_count` GA ** _(project)_**   
Disk bytes read   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of disk bytes that have been read. Linux only. Sampled every 60 seconds._   
`device`: Device name.   
`weighted_io_time` GA ** _(project)_**   
Disk weighted I/O time   
`CUMULATIVE`, `INT64`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total time spent on disk I/O operations weighted by the number of in-progress I/Os. This metric provides a measure of the I/O completion time and of the size of the backlog that might be accumulating. Linux only. Sampled every 60 seconds._   
`device`: Device name.   
`write_bytes_count` GA ** _(project)_**   
Disk bytes written   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of disk bytes that have been written. Linux only. Sampled every 60 seconds._   
`device`: Device name.   
  
### elasticsearch

Metrics from [elasticsearch](https://docs.cloud.google.com/monitoring/agent/plugins/elasticsearch). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/elasticsearch/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`cache_memory_usage` GA ** _(project)_**   
Cache size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Size in bytes of the caches. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`cache_name`: Cache name (either 'field' or 'filter').   
`field_eviction_count` GA ** _(project)_**   
Field evictions   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Evictions from field cache. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`filter_cache_eviction_count` GA ** _(project)_**   
Filter evictions   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Evictions from filter cache. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`gc_collection_count` GA ** _(project)_**   
GC count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Garbage collection count. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`type`: The type of the garbage collection.   
`memory_usage` GA ** _(project)_**   
Memory usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Size in bytes of memory. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`memory_type`: The memory type.   
`network` GA ** _(project)_**   
Network traffic   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of bytes transmitted and received on the network. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`direction`: Data direction, rx or tx.   
`num_current_documents` GA ** _(project)_**   
Documents   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of documents in the indexes on this node. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`document_type`: Document count type.   
`num_data_nodes` GA ** _(project)_**   
Data nodes   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of data nodes in the cluster. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`num_http_connections` GA ** _(project)_**   
Open connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of open HTTP connections to this node. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`num_nodes` GA ** _(project)_**   
Nodes   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of nodes in the cluster. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`num_open_files` GA ** _(project)_**   
Open files   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of open file descriptors held by the server process. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`num_server_connections` GA ** _(project)_**   
Open connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of open network connections to the server. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`num_shards` GA ** _(project)_**   
Shards   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of shards. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`shard_type`: State of the shard (active, relocating, initializing, unassigned).   
`operation_count` GA ** _(project)_**   
Completed operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of operations completed. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`operation`: The operation type.   
`operation_time` GA ** _(project)_**   
Operation time   
`CUMULATIVE`, `INT64`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Time in ms spent on operations. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`operation`: The operation type.   
`peak_threads` GA ** _(project)_**   
Max threads   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Maximum number of open threads that have been open concurrently in the server JVM process. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`storage_size` GA ** _(project)_**   
Storage size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Size in bytes of the document storage on this node. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
`threads` GA ** _(project)_**   
Threads   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of open threads in the server JVM process. Sampled every 60 seconds._   
`server_name`: The elasticsearch server name.   
  
### hbase

Metrics from [hbase](https://docs.cloud.google.com/monitoring/agent/plugins/hbase). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/hbase/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`ipc/connections` GA ** _(project)_**   
IPC connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of open connections. Sampled every 60 seconds._  
`ipc/queue_length` GA ** _(project)_**   
IPC queue size   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current size of the IPC queue. Sampled every 60 seconds._  
`ipc/traffic_count` GA ** _(project)_**   
IPC traffic   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of bytes transmitted and received via IPC. Sampled every 60 seconds._   
`direction`: Data direction, rx or tx.   
`master/average_load` GA ** _(project)_**   
Load   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The average master load. Sampled every 60 seconds._  
`master/dead_region_servers` GA ** _(project)_**   
Dead region servers   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of dead region servers. Sampled every 60 seconds._  
`master/live_region_servers` GA ** _(project)_**   
Live region servers   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of live region servers. Sampled every 60 seconds._  
`regionserver/block_cache/access_count` GA ** _(project)_**   
Block cache accesses   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of blocks of StoreFiles (HFiles) requested from the cache. Sampled every 60 seconds._   
`kind`: The cache access kind.   
`regionserver/block_cache/evicted_blocks_count` GA ** _(project)_**   
Evicted block count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of blocks that had to be evicted from the block cache due to heap size constraints. Sampled every 60 seconds._  
`regionserver/block_cache/hit_ratio_percent` GA ** _(project)_**   
Block cache hit ratio   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The running block cache hit ratio (0 to 100). Sampled every 60 seconds._  
`regionserver/block_cache/memory` GA ** _(project)_**   
Block cache size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Memory usage by the block cache. Sampled every 60 seconds._   
`usage_kind`: The kind of memory usage.   
`regionserver/block_cache/num_items` GA ** _(project)_**   
Block count   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of blocks of StoreFiles (HFiles) in the cache. Sampled every 60 seconds._  
`regionserver/call_queue/length` GA ** _(project)_**   
Call queue size   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The length of the call queue. Sampled every 60 seconds._  
`regionserver/compaction_queue/length` GA ** _(project)_**   
Compaction queue size   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The length of the compaction queue (the number of stores that have been targeted for compaction). Sampled every 60 seconds._  
`regionserver/flush_queue/length` GA ** _(project)_**   
Flush queue size   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of enqueued regions in the MemStore awaiting flush. Sampled every 60 seconds._  
`regionserver/memory/heap_usage` GA ** _(project)_**   
Heap usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Heap space used by the regionserver. Sampled every 60 seconds._  
`regionserver/memstore/files` GA ** _(project)_**   
Memstore files   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of store files on the regionserver. Sampled every 60 seconds._  
`regionserver/memstore/index_size` GA ** _(project)_**   
Memstore index size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The size of the store file index on the regionserver. Sampled every 60 seconds._  
`regionserver/memstore/open_stores` GA ** _(project)_**   
Memstore open stores   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of stores open on the regionserver. Sampled every 60 seconds._  
`regionserver/memstore/size` GA ** _(project)_**   
Memstore size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The sum of all the memstore sizes in the regionserver. Sampled every 60 seconds._  
`regionserver/online_regions` GA ** _(project)_**   
Online regions   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of active regions in the regionserver. Sampled every 60 seconds._  
`regionserver/request_count` GA ** _(project)_**   
Request count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of requests. Sampled every 60 seconds._   
`request_type`: The type of request.   
`regionserver/requests/total_rate` GA ** _(project)_**   
RPC request rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The point-in-time number of RegionServer RPC calls. Sampled every 60 seconds._   
`type`: The type of request.   
`regionserver/slow_operation_count` GA ** _(project)_**   
Slow operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of slow log operations. Sampled every 60 seconds._   
`operation`: The operation name (e.g., get, put).   
`thrift/batch_latency/average` GA ** _(project)_**   
Thrift average batch latency   
`GAUGE`, `DOUBLE`, `ns`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Thrift latency for batch operations. Sampled every 60 seconds._   
`operation`: The operation name (e.g., get, put).   
`thrift_id`: The id of the thrift instance.   
`thrift/call_latency/average` GA ** _(project)_**   
Thrift average call latency   
`GAUGE`, `DOUBLE`, `ns`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Thrift latency for all calls. Sampled every 60 seconds._   
`thrift_id`: The id of the thrift instance.   
`thrift/call_queue/length` GA ** _(project)_**   
Thrift call queue size   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Thrift call queue length. Sampled every 60 seconds._   
`thrift_id`: The id of the thrift instance.   
`thrift/slow_call_latency/average` GA ** _(project)_**   
Thrift average slow call latency   
`GAUGE`, `DOUBLE`, `ns`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Thrift latency for slow calls. Sampled every 60 seconds._   
`thrift_id`: The id of the thrift instance.   
`thrift/time_in_queue/average` GA ** _(project)_**   
Thrift average time in queue   
`GAUGE`, `DOUBLE`, `ns`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Thrift time spent in queue. Sampled every 60 seconds._   
`thrift_id`: The id of the thrift instance.   
  
### iis

**Microsoft Windows only**. Metrics from the default configuration for the Microsoft Windows [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) and the legacy Microsoft Windows [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/iis/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`current_connections` GA ** _(project)_**   
IIS open connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Currently open connections to IIS. Sampled every 60 seconds._  
`network/transferred_bytes_count` GA ** _(project)_**   
IIS transferred bytes   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Network bytes transferred by IIS. Sampled every 60 seconds._   
`direction`: Direction (sent, received)   
`new_connection_count` GA ** _(project)_**   
IIS connections   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Connections opened to IIS. Sampled every 60 seconds._  
`request_count` GA ** _(project)_**   
IIS requests   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Requests made to IIS. Sampled every 60 seconds._   
`http_method`: Http method (post, put, get, delete, option, trace, head)   
  
### interface

Network-interface metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) and the legacy Linux [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/interface/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`errors` GA ** _(project)_**   
Network errors   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of network errors. Linux only. Sampled every 60 seconds._   
`device`: Name of the network device.   
`direction`: Direction of the network traffic, one of [tx, rx].   
`packets` GA ** _(project)_**   
Network packets   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of packets sent over the network. Linux only. Sampled every 60 seconds._   
`device`: Name of the network device.   
`direction`: Direction of the network traffic, one of [tx, rx].   
`traffic` GA ** _(project)_**   
Network traffic   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of bytes sent over the network. Linux only. Sampled every 60 seconds._   
`device`: Name of the network device.   
`direction`: Direction of the network traffic, one of [tx, rx].   
  
### jvm

Metrics from [jvm](https://docs.cloud.google.com/monitoring/agent/plugins/jvm). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/jvm/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`gc/count` GA ** _(project)_**   
GC count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total number of collections that have occurred. Sampled every 60 seconds._   
`gc_name`: The name of the garbage collector involved.   
`gc/time` GA ** _(project)_**   
GC time   
`CUMULATIVE`, `INT64`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The accumulated collection elapsed time in milliseconds. Sampled every 60 seconds._   
`gc_name`: The name of the garbage collector involved.   
`memory/usage` GA ** _(project)_**   
Memory usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The memory usage. Sampled every 60 seconds._   
`memory_type`: The type of the memory.   
`usage_kind`: The kind of memory usage.   
`os/cpu_time` GA ** _(project)_**   
CPU time   
`CUMULATIVE`, `INT64`, `ns`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The CPU time used by the process on which the Java virtual machine is running. Sampled every 60 seconds._  
`os/open_files` GA ** _(project)_**   
Open files   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of open file descriptors. Sampled every 60 seconds._  
`thread/num_daemon` GA ** _(project)_**   
Daemon threads   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current number of live daemon threads. Sampled every 60 seconds._  
`thread/num_live` GA ** _(project)_**   
Threads   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current number of live threads. Sampled every 60 seconds._  
`thread/peak` GA ** _(project)_**   
Max threads   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The peak number of live threads. Sampled every 60 seconds._  
`uptime` GA ** _(project)_**   
Uptime   
`CUMULATIVE`, `INT64`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The uptime of the Java virtual machine. Sampled every 60 seconds._  
  
### kafka

Metrics from [kafka](https://docs.cloud.google.com/monitoring/agent/plugins/kafka). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/kafka/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`broker/topics/failed_request_count` GA ** _(project)_**   
Failed requests   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of failed requests. Sampled every 60 seconds._   
`request_type`: The type of the request, fetch or produce.   
`broker/topics/incoming_message_count` GA ** _(project)_**   
Incoming messages   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of incoming messages in all topics. Sampled every 60 seconds._  
`broker/topics/traffic` GA ** _(project)_**   
Traffic   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of bytes sent and received in all topics. Sampled every 60 seconds._   
`direction`: Data direction, in or out.   
`controller/kafka/active` GA ** _(project)_**   
Active controllers   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of active controllers in the cluster. Sampled every 60 seconds._  
`controller/kafka/offline_partitions` GA ** _(project)_**   
Offline partitions   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of partitions that don’t have an active leader and are hence not writable or readable. Sampled every 60 seconds._  
`controller/leader_elections/election_count` GA ** _(project)_**   
Leader elections   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total number of leader elections. Sampled every 60 seconds._  
`controller/leader_elections/unclean_count` GA ** _(project)_**   
Stale leader elections   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total number of leader elections where the leader is out-of-sync. Sampled every 60 seconds._  
`log/flush_count` GA ** _(project)_**   
Flushes   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of log flushes. Sampled every 60 seconds._  
`network/request_count` GA ** _(project)_**   
Requests   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of requests. Sampled every 60 seconds._   
`request_type`: The type of the request, fetch or produce.   
`purgatory/num_delayed_requests` GA ** _(project)_**   
Delayed purgatory requests   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current number of delayed requests in purgatory. Sampled every 60 seconds._   
`request_type`: The type of the request, fetch or produce.   
`purgatory/size` GA ** _(project)_**   
Purgatory requests   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current number of requests in purgatory. Sampled every 60 seconds._   
`request_type`: The type of the request, fetch or produce.   
`replica_fetcher/max_lag` GA ** _(project)_**   
Maximum lag   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The maximum lag in messages between the follower and leader replicas. Sampled every 60 seconds._  
`replica_fetcher/min_fetch_rate` GA ** _(project)_**   
Minimum fetch rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The minimum rate at which the follower replicas send fetch requests to the leaders. Sampled every 60 seconds._  
`replica_manager/isr/expand_count` GA ** _(project)_**   
Gaining replicas   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of replicas catching up (ISR = in-sync replica). Sampled every 60 seconds._  
`replica_manager/isr/shrink_count` GA ** _(project)_**   
Lagging replicas   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of replicas lagging behind (ISR = in-sync replica). Sampled every 60 seconds._  
`replica_manager/leaders` GA ** _(project)_**   
Leaders   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current number of leaders on this broker. Sampled every 60 seconds._  
`replica_manager/partitions` GA ** _(project)_**   
Partitions   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current number of partitions on this broker. Sampled every 60 seconds._  
`replica_manager/under_replicated_partitions` GA ** _(project)_**   
Unreliable partitions   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current number of under-replicated partitions. Sampled every 60 seconds._  
  
### memcached

Metrics from [memcached](https://docs.cloud.google.com/monitoring/agent/plugins/memcached). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/memcached/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`command_count` GA ** _(project)_**   
Commands   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Commands executed. Sampled every 60 seconds._   
`cache_name`: The memcache name.   
`command`: A memcached command name.   
`current_connections` GA ** _(project)_**   
Connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of current connections to the cache. Sampled every 60 seconds._   
`cache_name`: The memcache name.   
`current_items` GA ** _(project)_**   
Items   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of items currently stored in the cache. Sampled every 60 seconds._   
`cache_name`: The memcache name.   
`eviction_count` GA ** _(project)_**   
Evictions   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cache item evictions. Sampled every 60 seconds._   
`cache_name`: The memcache name.   
`memory` GA ** _(project)_**   
Memory usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Memory usage. Sampled every 60 seconds._   
`cache_name`: The memcache name.   
`mem_category`: Memory free or memory used.   
`network` GA ** _(project)_**   
Traffic   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Bytes transferred over the network. Sampled every 60 seconds._   
`cache_name`: The memcache name.   
`direction`: Data direction, rx or tx.   
`operation_count` GA ** _(project)_**   
Operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Memcached operation hit/miss counts. Sampled every 60 seconds._   
`cache_name`: The memcache name.   
`operation`: A memcached operation name (either 'incr', 'decr', or 'get').   
`type`: A memcached operation statistic (either 'hits' or 'misses')   
`operation_hitratio` GA ** _(project)_**   
Hit ratio   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Hit ratio for memcached operations, expressed as a percentage value between 0.0 and 100.0. Sampled every 60 seconds._   
`cache_name`: The memcache name.   
`operation`: A memcached operation name (either 'incr', 'decr', or 'get').   
`rusage` GA ** _(project)_**   
CPU time   
`CUMULATIVE`, `INT64`, `s{CPU}`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Accumulated user and system time. Sampled every 60 seconds._   
`cache_name`: The memcache name.   
`usage_type`: System utilization (either 'user' or 'syst').   
`threads` GA ** _(project)_**   
Threads   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of threads used by the memcached instance. Sampled every 60 seconds._   
`cache_name`: The memcache name.   
  
### memory

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) and the legacy [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/memory/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`bytes_used` GA ** _(project)_**   
Memory usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current memory usage by memory state. Summing the values of all states yields the total memory on the machine. Linux only. Sampled every 60 seconds._   
`state`: One of [buffered, cached, free, slab, used].   
`percent_used` GA ** _(project)_**   
Memory utilization   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current percentage of memory used by memory state. Summing percentages over all states yields 100 percent. Sampled every 60 seconds._   
`state`: One of [buffered, cached, free, slab, used].   
  
### mongodb

Metrics from [mongodb](https://docs.cloud.google.com/monitoring/agent/plugins/mongodb). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/mongodb/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`cache/hits` GA ** _(project)_**   
Cache hits   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of cache hits. Sampled every 60 seconds._  
`cache/misses` GA ** _(project)_**   
Cache misses   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of cache misses. Sampled every 60 seconds._  
`collections` GA ** _(project)_**   
Collections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of collections. Sampled every 60 seconds._   
`database_name`: The name of the MongoDB database.   
`connections` GA ** _(project)_**   
Connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of active server connections. Sampled every 60 seconds._   
`database_name`: The name of the MongoDB server.   
`data_size` GA ** _(project)_**   
Data size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The data size, in bytes. Sampled every 60 seconds._   
`database_name`: The name of the MongoDB database.   
`extents` GA ** _(project)_**   
Extents   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of extents. Sampled every 60 seconds._   
`database_name`: The name of the MongoDB database.   
`global_lock_hold_time` GA ** _(project)_**   
Global lock time   
`CUMULATIVE`, `INT64`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The time the global lock has been held. Sampled every 60 seconds._  
`index_size` GA ** _(project)_**   
Index size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The index size, in bytes. Sampled every 60 seconds._   
`database_name`: The name of the MongoDB database.   
`indexes` GA ** _(project)_**   
Indexes   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of indexes. Sampled every 60 seconds._   
`database_name`: The name of the MongoDB database.   
`memory_usage` GA ** _(project)_**   
Memory usage   
`GAUGE`, `DOUBLE`, `MiBy`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Mebibytes of memory used. Sampled every 60 seconds._   
`database_name`: The name of the MongoDB server.   
`memory_type`: Memory usage (mapped, resident, virtual).   
`objects` GA ** _(project)_**   
Objects   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of objects. Sampled every 60 seconds._   
`database_name`: The name of the MongoDB database.   
`operation_count` GA ** _(project)_**   
Operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of operations executed. Sampled every 60 seconds._   
`operation`: A database operation name.   
`storage_size` GA ** _(project)_**   
Storage size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The storage size, in bytes. Sampled every 60 seconds._   
`database_name`: The name of the MongoDB database.   
  
### mssql

**Microsoft Windows only**. Metrics from the default configuration for the Microsoft Windows [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) and the legacy Microsoft Windows [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/mssql/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`connections/user` GA ** _(project)_**   
SQL Server open connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Currently open connections to SQL server. Sampled every 60 seconds._  
`transaction_rate` GA ** _(project)_**   
SQL Server transaction rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _SQL server total transactions per second. Sampled every 60 seconds._  
`write_transaction_rate` GA ** _(project)_**   
SQL Server write transaction rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _SQL server write transactions per second. Sampled every 60 seconds._  
  
### mysql

Metrics from [mysql](https://docs.cloud.google.com/monitoring/agent/plugins/mysql). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/mysql/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`buffer_pool/num_pages` GA ** _(project)_**   
Buffer pool pages   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Buffer pool page count. Sampled every 60 seconds._   
`database`: The name of the database.   
`kind`: The buffer pool page kind.   
`buffer_pool/operation_count` GA ** _(project)_**   
Buffer pool operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Buffer pool operation count. Sampled every 60 seconds._   
`database`: The name of the database.   
`operation`: The buffer pool operation.   
`buffer_pool_size` GA ** _(project)_**   
Buffer pool size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Buffer pool size. Sampled every 60 seconds._   
`database`: The name of the database.   
`kind`: Buffer pool bytes kind.   
`command_count` GA ** _(project)_**   
Commands   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _MySQL command count. Sampled every 60 seconds._   
`database`: The name of the database.   
`command`: MySQL command.   
`handler_count` GA ** _(project)_**   
Handlers   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _MySQL handler count. Sampled every 60 seconds._   
`database`: The name of the database.   
`kind`: MySQL handler kind.   
`innodb/doublewrite_count` GA ** _(project)_**   
InnoDB doublewrite buffers   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _InnoDB doublewrite buffer count. Sampled every 60 seconds._   
`database`: The name of the database.   
`kind`: TODO.   
`innodb/log_operation_count` GA ** _(project)_**   
InnoDB log operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _InnoDB log operation count. Sampled every 60 seconds._   
`database`: The name of the database.   
`operation`: InnoDB log operation.   
`innodb/operation_count` GA ** _(project)_**   
InnoDB operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _InnoDB operation count. Sampled every 60 seconds._   
`database`: The name of the database.   
`operation`: InnoDB operation.   
`innodb/page_operation_count` GA ** _(project)_**   
InnoDB page operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _InnoDB page operation count. Sampled every 60 seconds._   
`database`: The name of the database.   
`operation`: InnoDB page operation.   
`innodb/row_lock_count` GA ** _(project)_**   
InnoDB locks   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _InnoDB row lock count. Sampled every 60 seconds._   
`database`: The name of the database.   
`kind`: InnoDB row lock kind.   
`innodb/row_operation_count` GA ** _(project)_**   
InnoDB row operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _InnoDB row operation count. Sampled every 60 seconds._   
`database`: The name of the database.   
`operation`: InnoDB row operation.   
`lock_count` GA ** _(project)_**   
Locks   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _MySQL lock count. Sampled every 60 seconds._   
`database`: The name of the database.   
`kind`: MySQL lock kind.   
`qcache/operation_count` GA ** _(project)_**   
QCache operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _QCache operation count. Sampled every 60 seconds._   
`database`: The name of the database.   
`operation`: QCache operation.   
`qcache/query_count` GA ** _(project)_**   
QCache queries   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _QCache query count. Sampled every 60 seconds._   
`database`: The name of the database.   
`slave_replication_lag` GA ** _(project)_**   
Replica lag   
`GAUGE`, `DOUBLE`, `s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Seconds behind master. Sampled every 60 seconds._   
`database`: The name of the database.   
`sort_count` GA ** _(project)_**   
Sorts   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _MySQL sort count. Sampled every 60 seconds._   
`database`: The name of the database.   
`kind`: MySQL sort kind.   
`thread_count` GA ** _(project)_**   
Threads   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Thread count. Sampled every 60 seconds._   
`database`: The name of the database.   
`kind`: Thread kind.   
  
### network

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) and the legacy [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/network/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`tcp_connections` GA ** _(project)_**   
TCP connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current count of TCP connections. Sampled every 60 seconds._   
`port`: TCP port number on the local or remote host, for example, "0-local", "0-remote", or "all".   
`tcp_state`: TCP state, for example, "ESTABLISHED" or "FIN_WAIT1".   
  
### nginx

Metrics from [nginx](https://docs.cloud.google.com/monitoring/agent/plugins/nginx). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/nginx/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`connections/accepted_count` GA ** _(project)_**   
Accepted connections   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total connections accepted. Sampled every 60 seconds._  
`connections/current` GA ** _(project)_**   
Active connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of connections currently attached to Nginx. Sampled every 60 seconds._   
`state`: The Nginx connection state.   
`connections/handled_count` GA ** _(project)_**   
Handled connections   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total connections handled. Sampled every 60 seconds._  
`request_count` GA ** _(project)_**   
Requests   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of requests Nginx has serviced. Sampled every 60 seconds._  
  
### pagefile

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) and the legacy Microsoft Windows [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/pagefile/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`percent_used` GA ** _(project)_**   
Pagefile utilization   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current percentage of pagefile used by state. Values are between 0.0 and 100.0. Windows only. Sampled every 60 seconds._   
`state`: Type of usage, one of [free, used].   
  
### postgresql

Metrics from [postgresql](https://docs.cloud.google.com/monitoring/agent/plugins/postgreSQL). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/postgresql/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`blocks_read_count` GA ** _(project)_**   
Blocks read   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of blocks read. Sampled every 60 seconds._   
`database`: The name of the database.   
`source`: The block read source.   
`table`: The name of the table.   
`commit_count` GA ** _(project)_**   
Commits   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of commits. Sampled every 60 seconds._   
`database`: The name of the database.   
`db_size` GA ** _(project)_**   
DB size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Database disk usage. Sampled every 60 seconds._   
`database`: The name of the database.   
`num_backends` GA ** _(project)_**   
Backends   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of backends. Sampled every 60 seconds._   
`database`: The name of the database.   
`num_tuples` GA ** _(project)_**   
DB rows   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of tuples (rows) in the database. Sampled every 60 seconds._   
`database`: The name of the database.   
`state`: Tuple (row) state (either 'dead' or 'live').   
`table`: The name of the table.   
`operation_count` GA ** _(project)_**   
Operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of db row operations. Sampled every 60 seconds._   
`database`: The name of the database.   
`operation`: The database operation.   
`table`: The name of the table.   
`rollback_count` GA ** _(project)_**   
Rollbacks   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of rollbacks. Sampled every 60 seconds._   
`database`: The name of the database.   
  
### processes

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) and the legacy [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Launch stages of these metrics: ALPHA GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/processes/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`count_by_state` GA ** _(project)_**   
Processes   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of processes in the given state. Linux only. Sampled every 60 seconds._   
`state`: Running, sleeping, zombie, etc.   
`cpu_time` GA ** _(project)_**   
Process CPU   
`CUMULATIVE`, `INT64`, `us{CPU}`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _CPU time of the given process. Sampled every 60 seconds._   
`process`: Process name.   
`user_or_syst`: Whether a user or system process.   
`command`: Process command.   
`command_line`: Process command line, 1024 characters maximum.   
`owner`: Process owner.   
`pid`: Process ID.   
`disk/read_bytes_count` GA ** _(project)_**   
Process disk read I/O   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Process disk read I/O. Linux only. Sampled every 60 seconds._   
`process`: Process name.   
`command`: Process command.   
`command_line`: Process command line, 1024 characters maximum.   
`owner`: Process owner.   
`pid`: Process ID.   
`disk/write_bytes_count` GA ** _(project)_**   
Process disk write I/O   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Process disk write I/O. Linux only. Sampled every 60 seconds._   
`process`: Process name.   
`command`: Process command.   
`command_line`: Process command line, 1024 characters maximum.   
`owner`: Process owner.   
`pid`: Process ID.   
`fork_count` GA ** _(project)_**   
Fork count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of processes forked. Linux only. Sampled every 60 seconds._  
`rss_usage` GA ** _(project)_**   
Process resident memory   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Resident memory usage of the given process. Linux only. Sampled every 60 seconds._   
`process`: Process name.   
`command`: Process command.   
`command_line`: Process command line, 1024 characters maximum.   
`owner`: Process owner.   
`pid`: Process ID.   
`vm_usage` GA ** _(project)_**   
Process virtual memory   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _VM Usage of the given process. Sampled every 60 seconds._   
`process`: Process name.   
`command`: Process command.   
`command_line`: Process command line, 1024 characters maximum.   
`owner`: Process owner.   
`pid`: Process ID.   
`windows/handles` ALPHA ** _(project)_**   
Process open handles (Windows)   
`GAUGE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Open handle count of the given process. Windows only. Sampled every 60 seconds._   
`process`: Process name.   
`command`: Process command.   
`command_line`: Process command line, 1024 characters maximum.   
`owner`: Process owner.   
`pid`: Process ID.   
  
### rabbitmq

Metrics from [rabbitmq](https://docs.cloud.google.com/monitoring/agent/plugins/rabbitMQ). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/rabbitmq/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`consumers` GA ** _(project)_**   
Consumers   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of consumers reading from the specified queue. Sampled every 60 seconds._   
`queue`: The rabbit queue name.   
`delivery_rate` GA ** _(project)_**   
Delivery rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The rate (per second) at which messages are being delivered. Sampled every 60 seconds._   
`queue`: The rabbit queue name.   
`num_messages` GA ** _(project)_**   
Messages   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of messages in a queue. Sampled every 60 seconds._   
`queue`: The rabbit queue name.   
`state`: The message state.   
`publish_rate` GA ** _(project)_**   
Publish rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The rate (per second) at which messages are being published. Sampled every 60 seconds._   
`queue`: The rabbit queue name.   
  
### redis

Metrics from [redis](https://docs.cloud.google.com/monitoring/agent/plugins/redis). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/redis/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`changes_since_last_save` GA ** _(project)_**   
Unsaved changes   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Change count since last save. Sampled every 60 seconds._   
`node`: Redis node name.   
`clients/blocked` GA ** _(project)_**   
Blocked clients   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of blocked clients. Sampled every 60 seconds._   
`node`: Redis node name.   
`clients/connected` GA ** _(project)_**   
Connected clients   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of client connections. Sampled every 60 seconds._   
`node`: Redis node name.   
`commands_processed` GA ** _(project)_**   
Commands   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total number of commands processed. Sampled every 60 seconds._   
`node`: Redis node name.   
`connections/slaves` GA ** _(project)_**   
Slave connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of slave connections. Sampled every 60 seconds._   
`node`: Redis node name.   
`connections/total` GA ** _(project)_**   
Connections   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total number of connections accepted. Sampled every 60 seconds._   
`node`: Redis node name.   
`expired_keys` GA ** _(project)_**   
Expired keys   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total number of key expirations. Sampled every 60 seconds._   
`node`: Redis node name.   
`memory/usage` GA ** _(project)_**   
Memory usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Memory usage in bytes. Sampled every 60 seconds._   
`node`: Redis node name.   
`memory/usage_lua` GA ** _(project)_**   
Lua memory usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Lua memory usage in bytes. Sampled every 60 seconds._   
`node`: Redis node name.   
`pubsub/channels` GA ** _(project)_**   
PubSub channels   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of global pub/sub channels with subscribed clients. Sampled every 60 seconds._   
`node`: Redis node name.   
`pubsub/patterns` GA ** _(project)_**   
PubSub patterns   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of global pub/sub patterns with subscribed clients. Sampled every 60 seconds._   
`node`: Redis node name.   
`uptime` GA ** _(project)_**   
Uptime   
`GAUGE`, `DOUBLE`, `s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Uptime in seconds. Sampled every 60 seconds._   
`node`: Redis node name.   
  
### riak

Metrics from [riak](https://docs.cloud.google.com/monitoring/agent/plugins/riak). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/riak/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`latency/95th_percentile` GA ** _(project)_**   
95% latency (1m)   
`GAUGE`, `DOUBLE`, `us`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Time between reception of client read request and subsequent response to client (95th percentile). Sampled every 60 seconds._   
`server_name`: The riak server name.   
`type`: An operation type with latency statistics (either 'get' or 'put').   
`latency/average` GA ** _(project)_**   
Average latency (1m)   
`GAUGE`, `DOUBLE`, `us`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Time between reception of client read request and subsequent response to client (mean). Sampled every 60 seconds._   
`server_name`: The riak server name.   
`type`: An operation type with latency statistics (either 'get' or 'put').   
`latency/maximum` GA ** _(project)_**   
Maximum latency (1m)   
`GAUGE`, `DOUBLE`, `us`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Time between reception of client read request and subsequent response to client (maximum). Sampled every 60 seconds._   
`server_name`: The riak server name.   
`type`: An operation type with latency statistics (either 'get' or 'put').   
`memory_usage` GA ** _(project)_**   
Memory usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Memory usage. Sampled every 60 seconds._   
`server_name`: The riak server name.   
`memory_type`: Memory usage type.   
`num_siblings/95th_percentile` GA ** _(project)_**   
95% siblings (1m)   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of siblings encountered during all GET operations by this node within the last minute (95th percentile). Sampled every 60 seconds._   
`server_name`: The riak server name.   
`num_siblings/average` GA ** _(project)_**   
Average siblings (1m)   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of siblings encountered during all GET operations by this node within the last minute (mean). Sampled every 60 seconds._   
`server_name`: The riak server name.   
`num_siblings/maximum` GA ** _(project)_**   
Maximum siblings (1m)   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of siblings encountered during all GET operations by this node within the last minute (maximum). Sampled every 60 seconds._   
`server_name`: The riak server name.   
`object_size/95th_percentile` GA ** _(project)_**   
95% object size (1m)   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Size of objects encountered by this node within the last minute (95th percentile). Sampled every 60 seconds._   
`server_name`: The riak server name.   
`object_size/average` GA ** _(project)_**   
Average object size (1m)   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Size of objects encountered by this node within the last minute (mean). Sampled every 60 seconds._   
`server_name`: The riak server name.   
`object_size/maximum` GA ** _(project)_**   
Maximum object size (1m)   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Size of objects encountered by this node within the last minute (maximum). Sampled every 60 seconds._   
`server_name`: The riak server name.   
`operation_count` GA ** _(project)_**   
Operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Coordinated operation count. Sampled every 60 seconds._   
`server_name`: The riak server name.   
`operation`: An operation name.   
  
### swap

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) and the legacy Linux [Monitoring agent](https://docs.cloud.google.com/monitoring/agent). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/swap/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`bytes_used` GA ** _(project)_**   
Swap usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current number of swap bytes used by state. For this metric to be available, swap must be enabled on the instance. Linux only. Sampled every 60 seconds._   
`device`: Swap device.   
`state`: One of [used, free, cached, reserved].   
`io` GA ** _(project)_**   
Swap I/O operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of swap I/O operations by direction. For this metric to be available, swap must be enabled on the instance. Linux only. Sampled every 60 seconds._   
`direction`: Swap I/O direction, one of [in, out].   
`percent_used` GA ** _(project)_**   
Swap utilization   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current percentage of swap used by state. Values are between 0.0 and 100.0. For this metric to be available, swap must be enabled on the instance. Linux only. Sampled every 60 seconds._   
`device`: Swap device.   
`state`: One of [used, free, cached, reserved].   
  
### tomcat

Metrics from [tomcat](https://docs.cloud.google.com/monitoring/agent/plugins/tomcat). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/tomcat/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`manager/sessions` GA ** _(project)_**   
Sessions   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of active sessions. Sampled every 60 seconds._   
`url_prefix`: The URL prefix for a given session.   
`request_processor/error_count` GA ** _(project)_**   
Errors   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of errors encountered. Sampled every 60 seconds._   
`proto_handler`: The protocol handler label.   
`request_processor/processing_time` GA ** _(project)_**   
Processing time   
`CUMULATIVE`, `INT64`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total processing time. Sampled every 60 seconds._   
`proto_handler`: The protocol handler label.   
`request_processor/request_count` GA ** _(project)_**   
Requests   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total number of requests. Sampled every 60 seconds._   
`proto_handler`: The protocol handler label.   
`request_processor/traffic_count` GA ** _(project)_**   
Traffic   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of bytes transmitted and received. Sampled every 60 seconds._   
`proto_handler`: The protocol handler label.   
`direction`: Data direction, rx or tx.   
`threads/busy` GA ** _(project)_**   
Busy threads   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current number of busy threads. Sampled every 60 seconds._   
`proto_handler`: The protocol handler label.   
`threads/current` GA ** _(project)_**   
Current threads   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current number of threads. Sampled every 60 seconds._   
`proto_handler`: The protocol handler label.   
  
### varnish

Metrics from [varnish](https://docs.cloud.google.com/monitoring/agent/plugins/varnish). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/varnish/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`backend_connection_count` GA ** _(project)_**   
Backend connection successes   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Backend connection success count. Sampled every 60 seconds._   
`cache_name`: The Varnish cache name suffixed with a metric category.   
`type`: The backend connection type (either 'failures', 'not-attempted', 'recycled', 'reuses', 'success', 'too-many', 'unused', or 'was-closed').   
`category`: The Varnish metric category.   
`cache_operation_count` GA ** _(project)_**   
Cache operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cache operation count. Sampled every 60 seconds._   
`cache_name`: The Varnish cache name suffixed with a metric category.   
`operation`: The cache operation type (either 'hit', 'miss', or 'hitpass').   
`category`: The Varnish metric category.   
`client_connection_count` GA ** _(project)_**   
Client connections   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Client connection count. Sampled every 60 seconds._   
`cache_name`: The Varnish cache name suffixed with a metric category.   
`category`: The Varnish metric category.   
`type`: The client connection type (either 'accepted', 'dropped', or 'received').   
  
### zookeeper

Metrics from [zookeeper](https://docs.cloud.google.com/monitoring/agent/plugins/zookeeper). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/zookeeper/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`connections_count` GA ** _(project)_**   
Open connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of connections currently alive. Sampled every 60 seconds._  
`data_size` GA ** _(project)_**   
Data size   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Bytes of data on this ZooKeeper server. Sampled every 60 seconds._  
`followers/count` GA ** _(project)_**   
Followers   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of followers. Sampled every 60 seconds._  
`followers/synced_count` GA ** _(project)_**   
Synced followers   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of synchronized followers. Sampled every 60 seconds._  
`network/received_packets_count` GA ** _(project)_**   
Packets received   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Packets received. Sampled every 60 seconds._  
`network/sent_packets_count` GA ** _(project)_**   
Packets sent   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Packets sent. Sampled every 60 seconds._  
`nodes/count` GA ** _(project)_**   
Nodes   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _ZooKeeper node count. Sampled every 60 seconds._  
`nodes/ephemeral_count` GA ** _(project)_**   
Ephemeral nodes   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of ephemeral nodes. Sampled every 60 seconds._  
`nodes/watches_count` GA ** _(project)_**   
Watches   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of watches on ZooKeeper nodes. Sampled every 60 seconds._  
`requests/latency/average` GA ** _(project)_**   
Average request latency   
`GAUGE`, `DOUBLE`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Average request latency. Sampled every 60 seconds._  
`requests/latency/maximum` GA ** _(project)_**   
Maximum request latency   
`GAUGE`, `DOUBLE`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Maximum request latency. Sampled every 60 seconds._  
`requests/latency/minimum` GA ** _(project)_**   
Minimum request latency   
`GAUGE`, `DOUBLE`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Minimum request latency. Sampled every 60 seconds._  
`requests/outstanding_count` GA ** _(project)_**   
Outstanding requests   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of outstanding requests. Sampled every 60 seconds._  
`sync_operations/pending_count` GA ** _(project)_**   
Pending syncs   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of pending synchronization operations. Sampled every 60 seconds._  
  
Generated at 2026-05-14 16:07:40 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
