---
url: https://docs.cloud.google.com/monitoring/api/metrics_gcp_c/
title: Google Cloud metrics: API prefix is C \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:17.578628+00:00
---

# Google Cloud metrics: API prefix is C  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_gcp_c/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Google Cloud metrics: API prefix is C Stay organized with collections  Save and categorize content based on your preferences. 

These tables list the Google Cloud metric types whose service domain name begins with the letter `c`, such as `compute.googleapis.com`. For information about other metric types, see [Google Cloud metrics overview](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

## About the tables of metrics

The tables of metrics provide formatted versions of the publicly available [metric descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor). This section provides additional information to help you interpret and use these descriptors.

  * For a general explanation of the entries in the tables, including information about values like `DELTA` and `GAUGE`, see [Metric types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

To chart or monitor metric types with values of type `STRING`, you must use Monitoring Query Language (MQL), and you must convert the value into a numeric value. For information about MQL string-conversion methods, see [`String`](https://docs.cloud.google.com/monitoring/mql/reference#string-group).

  * For information about the units used in the metric lists, see the [`unit` field](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.unit) in the `MetricDescriptor` reference.

  * For information about statements of the form “Sampled every _x_ seconds” and “After sampling, data is not visible for up to _y_ seconds”, see [Additional information: metadata](https://docs.cloud.google.com/monitoring/api/metrics#metadata).

  * The resource-hierarchy level tells you if the metric is written at the project, organization, or folder level(s). When the level is not specified in the metric descriptor, the metric writes at the project level by default.



  * For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).


  * For information about the meaning of launch stages such as `GA` (General Availability) and `BETA` (Preview), see [Product launch stages](https://cloud.google.com/products#product-launch-stages).



**Cloud Endpoints** : APIs managed by Cloud Endpoints write [ `serviceruntime`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime) metrics against the [`api`](https://docs.cloud.google.com/monitoring/api/resources#tag_api) monitored-resource type.

**Note:** To monitor the availability of a service, create an uptime check. These checks create [`monitoring.googleapis.com/uptime_check/check_passed`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/uptime_check/check_passed) metric data. Don't configure an alerting policy to track a metric type such as `compute.googleapis.com/instance/uptime` if your goal is to monitor the availability of a service. For information about why such alerting policies might not function as you expect, see [Uptime policy doesn't create expected alerts](https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications#use-uptime-check). For information about how to create an uptime check, see [Managing uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks).

## Google Cloud metrics

Metrics from [Google Cloud](https://docs.cloud.google.com/docs).

The following list was last generated at 2026-10-14 20:24:33 UTC. For more information about this process, see [ About the lists](https://docs.cloud.google.com/monitoring/api/metrics#generated).

### certificatemanager

Metrics from [ Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `certificatemanager.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`map/entries` GA ** _(project)_**   
Certificate map entries   
`GAUGE`, `INT64`, `1`   
**[certificatemanager.googleapis.com/CertificateMap](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com/CertificateMap)** |  _Current number of map entries inside certificate map. Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._   
`is_primary`: Shows whether map entry is configured as primary.   
`project/certificates` GA ** _(project)_**   
Certificates   
`GAUGE`, `INT64`, `1`   
**[certificatemanager.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com/Project)** |  _Current number of certificates. Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._   
`scope`: Certificate scope, one of [DEFAULT, EDGE_CACHE].   
`type`: Certificate type, one of [MANAGED, SELF_MANAGED].   
`is_active`: Shows whether certificate is used in serving.   
`project/v2/active_certificates` BETA ** _(project)_**   
Active Certificates   
`GAUGE`, `INT64`, `1`   
**[certificatemanager.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com/Project)** |  _Current number of active certificates. For this metric, the sampling period is a reporting period, not a measurement period. Measurements are initiated every 3600 seconds. Measurements that take longer than 3600 seconds to complete will delay the start of the next measurement attempt. The last measured value is repeated until the next measurement completes. Sampled every 3600 seconds._   
`authority_type`: The type of CA that issued the certificate, one of [Private, Public].   
`key_algorithm`: The algorithm of the key used to sign the certificate.   
`key_usage_profile`: The use case based on the key usages of the certificate.   
`resource_types`: Shows the associated GCP resource types.   
`project/v2/certificate_expiration` BETA ** _(project)_**   
Certificate Expiration   
`GAUGE`, `DISTRIBUTION`, `s`   
**[certificatemanager.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com/Project)** |  _The distribution of the seconds left until the notAfter time of long-lived certificates with lifetime greater than 72 hours. For this metric, the sampling period is a reporting period, not a measurement period. Measurements are initiated every 3600 seconds. Measurements that take longer than 3600 seconds to complete will delay the start of the next measurement attempt. The last measured value is repeated until the next measurement completes. Sampled every 3600 seconds._  
`project/v2/certificate_observance_event_count` BETA ** _(project)_**   
Certificate Observance Event Count   
`DELTA`, `INT64`, `1`   
**[certificatemanager.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com/Project)** |  _Count of times a new certificate is observed._   
`authority_type`: The type of CA that issued the certificate, one of [Private, Public].   
`key_algorithm`: The algorithm of the key used to sign the certificate.   
`key_usage_profile`: The use case based on the key usages of the certificate.   
  
### ces

Metrics from [Gemini Enterprise for Customer Experience](https://docs.cloud.google.com/customer-engagement-ai). Launch stages of these metrics: ALPHA BETA

The "metric type" strings in this table must be prefixed with `ces.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`app/session_count` BETA ** _(project)_**   
CES session count.   
`DELTA`, `INT64`, `1`   
**[ces.googleapis.com/App](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/App)** |  _The total number of text and voice conversations received by the app._   
`modality`: The modality of the session (TEXT or VOICE).   
`outcome`: The outcome of the session (SUCCESS, FAILURE, ABANDONED, or ESCALATED).   
`error_code`: The error code if the session failed.   
`app_version`: The version of the app.   
`app/token_consumption_count` BETA ** _(project)_**   
CES tokens consumption.   
`DELTA`, `INT64`, `1`   
**[ces.googleapis.com/App](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/App)** |  _The total number of LLM tokens used by the app._   
`token_type`: The type of token (PROMPT or COMPLETION).   
`modality`: The modality of the session (TEXT or VOICE).   
`model_name`: The name of the LLM model.   
`app_version`: The version of the app.   
`app/voice_call_audio_duration_count` BETA ** _(project)_**   
CES voice call audio duration. (Seconds)   
`DELTA`, `DOUBLE`, `s`   
**[ces.googleapis.com/App](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/App)** |  _The total number of seconds for all voice conversations received by the app._   
`outcome`: The outcome of the session (SUCCESS, FAILURE, ABANDONED, or ESCALATED).   
`error_code`: The error code if the session failed.   
`app_version`: The version of the app.   
`quota/concurrent/concurrent_bidi_run_session_operations/exceeded` BETA ** _(project)_**   
Concurrent BidiRunSession Operations concurrent quota exceeded   
`DELTA`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Concurrent exceeded on quota metric ces.googleapis.com/concurrent_bidi_run_session_operations. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`base_model`: The base model custom dimension.   
`quota/concurrent/concurrent_bidi_run_session_operations/limit` BETA ** _(project)_**   
Concurrent BidiRunSession Operations concurrent quota limit   
`GAUGE`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Concurrent limit on quota metric ces.googleapis.com/concurrent_bidi_run_session_operations. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`base_model`: The base model custom dimension.   
`quota/concurrent/concurrent_bidi_run_session_operations/usage` ALPHA ** _(project)_**   
concurrent_bidi_run_session_operations usage   
`GAUGE`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _The concurrent usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`time_window`: The window size for concurrent operation limits.   
`base_model`: The number of base_model items.   
`quota/evaluation_llm_token_consumption/exceeded` BETA ** _(project)_**   
Evaluation LLM tokens quota exceeded error   
`DELTA`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric ces.googleapis.com/evaluation_llm_token_consumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/evaluation_llm_token_consumption/limit` BETA ** _(project)_**   
Evaluation LLM tokens quota limit   
`GAUGE`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Current limit on quota metric ces.googleapis.com/evaluation_llm_token_consumption. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/evaluation_llm_token_consumption/usage` BETA ** _(project)_**   
Evaluation LLM tokens quota usage   
`DELTA`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Current usage on quota metric ces.googleapis.com/evaluation_llm_token_consumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/run_session_llm_token_consumption/exceeded` BETA ** _(project)_**   
RunSession LLM tokens quota exceeded error   
`DELTA`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric ces.googleapis.com/run_session_llm_token_consumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/run_session_llm_token_consumption/limit` BETA ** _(project)_**   
RunSession LLM tokens quota limit   
`GAUGE`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Current limit on quota metric ces.googleapis.com/run_session_llm_token_consumption. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/run_session_llm_token_consumption/usage` BETA ** _(project)_**   
RunSession LLM tokens quota usage   
`DELTA`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Current usage on quota metric ces.googleapis.com/run_session_llm_token_consumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/run_session_requests/exceeded` DEPRECATED ** _(project)_**   
RunSession requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric ces.googleapis.com/run_session_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/run_session_requests/limit` DEPRECATED ** _(project)_**   
RunSession requests quota limit   
`GAUGE`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Current limit on quota metric ces.googleapis.com/run_session_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/run_session_requests/usage` DEPRECATED ** _(project)_**   
RunSession requests quota usage   
`DELTA`, `INT64`, `1`   
**[ces.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_ces.googleapis.com/Location)** |  _Current usage on quota metric ces.googleapis.com/run_session_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
  
### chronicle

Metrics from [Google Security Operations](https://docs.cloud.google.com/chronicle/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `chronicle.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`agent/cpu_seconds` GA ** _(project)_**   
Agent CPU Seconds   
`GAUGE`, `INT64`, `s`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Total CPU time consumed by the Chronicle agent process in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._  
`agent/exporter_accepted_spans_count` GA ** _(project)_**   
Exporter Accepted Spans Count   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The number of spans accepted by the exporter. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the name of the exporter.   
`agent/exporter_queue_capacity` GA ** _(project)_**   
Exporter Queue Capacity   
`GAUGE`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Current capacity of the exporter queue. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the name of the exporter.   
`agent/exporter_queue_size` GA ** _(project)_**   
Exporter Queue Size   
`GAUGE`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Current size of the exporter queue. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the name of the exporter.   
`agent/exporter_refused_spans_count` GA ** _(project)_**   
Exporter Refused Spans Count   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The number of spans refused by the exporter. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the name of the exporter.   
`agent/memory_used` GA ** _(project)_**   
Agent Memory Used   
`GAUGE`, `INT64`, `By`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Memory used by the Collection agent process. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._  
`agent/process_uptime` GA ** _(project)_**   
Agent Process Uptime   
`GAUGE`, `INT64`, `s`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The uptime of the Chronicle agent process. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._  
`agent/processor_accepted_spans_count` GA ** _(project)_**   
Processor Accepted Spans Count   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The number of spans accepted by the processor. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the name of the processor.   
`agent/processor_refused_spans_count` GA ** _(project)_**   
Processor Refused Spans Count   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The number of spans refused by the processor. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the name of the processor.   
`agent/receiver_accepted_spans_count` GA ** _(project)_**   
Receiver Accepted Spans Count   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The number of spans accepted by the receiver. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the name of the receiver.   
`agent/receiver_refused_spans_count` GA ** _(project)_**   
Receiver Refused Spans Count   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The number of spans refused by the receiver. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the name of the receiver.   
`azure_event_hub/bytes_count` GA ** _(project)_**   
Total Ingested Log Size (Azure Event Hub Feeds)   
`DELTA`, `INT64`, `By`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Total Size of logs ingested by azure event hub feeds. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`feed_name`: The identifier of the feed which is the google defined unique feed id.   
`azure_event_hub/is_unhealthy` GA ** _(project)_**   
Azure Event Hub Health Status   
`GAUGE`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The status of each Azure Event Hub ingestion source. State value describes the type of status for unhealthy sources. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`feed_name`: The identifier of the feed which is the google defined unique feed id.   
`state`: Indicates the health of the Azure Event Hub ingestion.   
`azure_event_hub/record_count` GA ** _(project)_**   
Total Ingested Log Count (Azure Event Hub Feeds)   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The total number of logs ingested by azure event hub feeds. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`feed_name`: The identifier of the feed which is the google defined unique feed id.   
`compliance/cmek/instance_healthy` BETA ** _(project)_**   
Chronicle CMEK Health Status   
`GAUGE`, `BOOL`, `1`   
**[chronicle.googleapis.com/Compliance](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Compliance)** |  _Indicates if the Customer Managed Encryption Key (CMEK) for the Chronicle instance is healthy and accessible. This is only for CMEK customers. For non-CMEK customers, this metric will always be true._   
`key_disabled_reason`: The specific reason for the CMEK health status interruption.   
`key_id`: The identifier of the Customer Managed Encryption Key (CMEK).   
`troubleshooting_doc`: The troubleshooting document reference message for the CMEK health status interruption.   
`forwarder/buffer_used` GA ** _(project)_**   
Buffer Used   
`GAUGE`, `DOUBLE`, `%`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Percentage of buffer used by the forwarder. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the input type used by the forwarder. (Eg: kafka, pcap, splunk, syslog etc.)   
`buffer_type`: Indicates the buffer type of the forwarder. Eg: memory, file etc.   
`forwarder/container/cpu_used` GA ** _(project)_**   
CPU Used   
`GAUGE`, `DOUBLE`, `%`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Percentage of cpu used by the forwarder container. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._  
`forwarder/container/disk_used` GA ** _(project)_**   
Disk Used   
`GAUGE`, `DOUBLE`, `%`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Percentage of disk used by the forwarder container. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._  
`forwarder/container/memory_used` GA ** _(project)_**   
Memory Used   
`GAUGE`, `DOUBLE`, `%`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Percentage of memory used by the forwarder container. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._  
`forwarder/last_heartbeat` GA ** _(project)_**   
Last Heartbeat   
`GAUGE`, `INT64`, `s`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Timestamp for last heartbeat of the forwarder (in seconds of UTC time since Unix epoch). Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the input type used by the forwarder. (Eg: kafka, pcap, splunk, syslog etc.)   
`forwarder/log/drop_count` GA ** _(project)_**   
Total Logs Dropped   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Number of logs dropped by the forwarder. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`input_type`: Indicates the input type used by the forwarder. (Eg: kafka, pcap, splunk, syslog etc.)   
`reason`: Indicates the reason why logs were dropped by the forwarder. Eg: regex, invalid_config, backlog etc.   
`gcp/is_unhealthy` GA ** _(project)_**   
Native GCP Health Status   
`GAUGE`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The status of each Native GCP ingestion logtype. State value describes the type of status for unhealthy sources. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`state`: Indicates the health of the Native GCP ingestion.   
`https_push/bytes_count` GA ** _(project)_**   
Total Ingested Log Size (HTTPS Push Feeds)   
`DELTA`, `INT64`, `By`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Total Size of logs ingested by https push ingestion source. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`feed_name`: The identifier of the feed which is the google defined unique feed id.   
`https_push/is_unhealthy` GA ** _(project)_**   
HTTPS Push Health Status   
`GAUGE`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The status of each HTTPS push ingestion source. State value describes the type of status for unhealthy sources. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`feed_name`: The identifier of the feed which is the google defined unique feed id.   
`state`: Indicates the health of the HTTPS Push ingestion.   
`https_push/record_count` GA ** _(project)_**   
Total Ingested Log Count (HTTPS Push Feeds)   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The total number of logs ingested by https push feeds. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`feed_name`: The identifier of the feed which is the google defined unique feed id.   
`ingestion/is_unhealthy` GA ** _(project)_**   
Ingestion Health Status   
`GAUGE`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The status of each source of ingestion. State value describes the type of status for unhealthy sources. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`state`: Indicates the health of the ingestion.   
`ingestion/log/bytes_count` GA ** _(project)_**   
Total Ingested Log Size   
`DELTA`, `INT64`, `By`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The total size of logs ingested. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`namespace`: The namespace of the log.   
`ingestion_source`: The source from where the log was ingested.   
`ingestion/log/quota_rejected_bytes_count` GA ** _(project)_**   
Total Quota Rejected Log Size   
`DELTA`, `INT64`, `By`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The total size of logs rejected due to insufficient quota. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`namespace`: The namespace of the log.   
`quota_type`: The type of quota (SHORT_TERM_DATA_RATE/LONG_TERM_DAILY_LIMIT).   
`ingestion/log/record_count` GA ** _(project)_**   
Total Ingested Log Count   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The total number of logs ingested. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`namespace`: The namespace of the log.   
`ingestion_source`: The source from where the log was ingested.   
`ingestion/quota_limit` GA ** _(project)_**   
Quota Limit   
`GAUGE`, `INT64`, `By`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Quota limits for the customer. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`quota_type`: The type of quota (SHORT_TERM/LONG_TERM).   
`log_processing_pipeline/emitted_bytes_count` GA ** _(project)_**   
Total Emitted Log Size   
`DELTA`, `INT64`, `By`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Total size of logs in bytes emitted by log processing pipeline. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`pipeline_id`: Pipeline id of the log processing pipeline.   
`processor_id`: Processor id of the log processing pipeline.   
`log_processing_pipeline/emitted_log_count` GA ** _(project)_**   
Total Emitted Log Count   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Total count of logs emitted by log processing pipeline. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`pipeline_id`: Pipeline id of the log processing pipeline.   
`processor_id`: Processor id of the log processing pipeline.   
`log_processing_pipeline/ingested_bytes_count` GA ** _(project)_**   
Total Ingested Log Size   
`DELTA`, `INT64`, `By`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Total size of logs in bytes received by log processing pipeline. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`pipeline_id`: Pipeline id of the log processing pipeline.   
`processor_id`: Processor id of the log processing pipeline.   
`log_processing_pipeline/ingested_log_count` GA ** _(project)_**   
Total Ingested Log Count   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Total count of logs received by log processing pipeline. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`pipeline_id`: Pipeline id of the log processing pipeline.   
`processor_id`: Processor id of the log processing pipeline.   
`log_processing_pipeline/processing_latencies` GA ** _(project)_**   
Processing Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _Latencies of logs processed by log processing pipeline. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`pipeline_id`: Pipeline id of the log processing pipeline.   
`processor_id`: Processor id of the log processing pipeline.   
`normalizer/event/record_count` GA ** _(project)_**   
Total Event Count (Parsing)   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The total number of events generated after parsing. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`state`: Indicates the final state for a log/event. Eg: failed_validation, validated etc.   
`event_type`: The event type determines which fields are included with the event. The event type includes values such as PROCESS_OPEN, FILE_CREATION, USER_CREATION, NETWORK_DNS.   
`normalizer/is_unhealthy` GA ** _(project)_**   
Parsing Health Status   
`GAUGE`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The status of log parsing ratio per logtype. State value describes the type of status for unhealthy sources. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`state`: Indicates the health of log parsing.   
`normalizer/log/record_count` GA ** _(project)_**   
Total Log Count (Parsing)   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The total number of log entries received for parsing. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`state`: If the log was parsed or failed parsing.   
`drop_reason`: Reason for the log to be dropped when it fails parsing.   
`namespace`: The namespace of the log.   
`ingestion_source`: The source from where the log was ingested.   
`outofband/log/bytes_count` GA ** _(project)_**   
Total Ingested Log Size (Feeds)   
`DELTA`, `INT64`, `By`   
**[chronicle.googleapis.com/LogType](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/LogType)** |  _The total size of logs ingested for feeds created using Feed management API. Sampled every 60 seconds. After sampling, data is not visible for up to 660 seconds._   
`feed_name`: The name of the feed.   
`outofband/log/is_unhealthy` GA ** _(project)_**   
OutOfBand Health Status   
`GAUGE`, `INT64`, `1`   
**[chronicle.googleapis.com/LogType](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/LogType)** |  _The status of each feed based ingestion source. State value describes the type of status for unhealthy sources. Sampled every 60 seconds. After sampling, data is not visible for up to 660 seconds._   
`feed_name`: The identifier of the feed which is the google defined unique feed id.   
`state`: Indicates the health of the feed based ingestion.   
`outofband/log/record_count` GA ** _(project)_**   
Total Ingested Log Count (Feeds)   
`DELTA`, `INT64`, `1`   
**[chronicle.googleapis.com/LogType](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/LogType)** |  _The total number of logs ingested for feeds created using Feed management API. Sampled every 60 seconds. After sampling, data is not visible for up to 660 seconds._   
`feed_name`: The name of the feed.   
`workspace/is_unhealthy` GA ** _(project)_**   
Native Workspace Health Status   
`GAUGE`, `INT64`, `1`   
**[chronicle.googleapis.com/Collector](https://docs.cloud.google.com/monitoring/api/resources#tag_chronicle.googleapis.com/Collector)** |  _The status of the Native Workspace ingestion source. State value describes the type of status for unhealthy sources. Sampled every 60 seconds. After sampling, data is not visible for up to 720 seconds._   
`state`: Indicates the health of the Native Workspace ingestion.   
  
### cloudaicompanion

Metrics from [Gemini](https://docs.cloud.google.com/gemini/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `cloudaicompanion.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`code_assist/chat_responses_count` GA ** _(project)_**   
Chat Response Count   
`DELTA`, `INT64`, `{response}`   
**[cloudaicompanion.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudaicompanion.googleapis.com/Instance)** |  _Count of chat responses viewed by Code Assist users since the last sample. Sampled every 3600 seconds. After sampling, data is not visible for up to 7200 seconds._   
`client_name`: Gemini Client, for example, geminicli.   
`programming_language`: The programming language of the request, for example, python.   
`initiation_method`: The method used to initiate the conversation.   
`code_assist/code_lines_accepted_count` GA ** _(project)_**   
Code Lines Accepted Count   
`DELTA`, `INT64`, `{line_of_code}`   
**[cloudaicompanion.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudaicompanion.googleapis.com/Instance)** |  _Total count of lines of code accepted by Code Assist users. Sampled every 3600 seconds. After sampling, data is not visible for up to 7200 seconds._   
`programming_language`: The programming language of the request, for example, python.   
`client_name`: Gemini Client, for example, geminicli.   
`code_assist/code_suggestions_accepted_count` GA ** _(project)_**   
Code Suggestions Accepted Count   
`DELTA`, `INT64`, `{suggestion}`   
**[cloudaicompanion.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudaicompanion.googleapis.com/Instance)** |  _Total count of code suggestions accepted by Code Assist users. Sampled every 3600 seconds. After sampling, data is not visible for up to 7200 seconds._   
`programming_language`: The programming language of the request, for example, python.   
`client_name`: Gemini Client, for example, geminicli.   
`code_assist/code_suggestions_count` GA ** _(project)_**   
Code Suggestions Count   
`DELTA`, `INT64`, `{suggestion}`   
**[cloudaicompanion.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudaicompanion.googleapis.com/Instance)** |  _Total count of code suggestions offered to Code Assist users. Sampled every 3600 seconds. After sampling, data is not visible for up to 7200 seconds._   
`programming_language`: The programming language of the request, for example, python.   
`client_name`: Gemini Client, for example, geminicli.   
`code_assist/daily_active_user_count` GA ** _(project)_**   
Daily Active User Count   
`GAUGE`, `INT64`, `{user}`   
**[cloudaicompanion.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudaicompanion.googleapis.com/Instance)** |  _Total count of Code Assist users active for the previous 24 hour period. Sampled every 86400 seconds. After sampling, data is not visible for up to 86400 seconds._   
`client_name`: Gemini Client, for example, geminicli.   
`code_assist/twenty_eight_day_active_user_count` GA ** _(project)_**   
Twenty-eight Day Active User Count   
`GAUGE`, `INT64`, `{user}`   
**[cloudaicompanion.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudaicompanion.googleapis.com/Instance)** |  _Total count of Code Assist users active for the previous 28 day period. Sampled every 86400 seconds. After sampling, data is not visible for up to 86400 seconds._   
`client_name`: Gemini Client, for example, geminicli.   
`usage/response_count` GA ** _(project)_**   
Response count   
`DELTA`, `INT64`, `{request}`   
**[cloudaicompanion.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudaicompanion.googleapis.com/Instance)** |  _Number of responses sent from a Gemini for Google Cloud service. Some responses, particularly duplicates, may be hidden from the user for usability. Sampled every 3600 seconds. After sampling, data is not visible for up to 7200 seconds._   
`method`: The backend service method that received or generated this message, one of [GenerateChat, GenerateCode, CompleteTask, GenerateText].   
`client_name`: Gemini Client, for example, VSCODE.   
`programming_language`: The programming language of the request, for example, Python.   
`product`: The product that the request is associated with, for example, CODEASSIST, DATABASE.   
`usage/responses/daily_active_users` GA ** _(project)_**   
Daily Active User Responses   
`GAUGE`, `INT64`, `{user}`   
**[cloudaicompanion.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudaicompanion.googleapis.com/Instance)** |  _Daily active users, defined as users who have been sent a response from a Gemini for Google Cloud service. Sampled every 86400 seconds. After sampling, data is not visible for up to 86400 seconds._  
`usage/responses/seven_day_active_users` GA ** _(project)_**   
Seven day Active User Responses   
`GAUGE`, `INT64`, `{user}`   
**[cloudaicompanion.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudaicompanion.googleapis.com/Instance)** |  _Seven day active users, defined as users who have been sent a response from a Gemini for Google Cloud service. Sampled every 86400 seconds. After sampling, data is not visible for up to 86400 seconds._  
`usage/responses/twenty_eight_day_active_users` GA ** _(project)_**   
Twenty-eight day Active User Responses   
`GAUGE`, `INT64`, `{user}`   
**[cloudaicompanion.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudaicompanion.googleapis.com/Instance)** |  _Twenty-eight day active users, defined as users who have been sent a response from a Gemini for Google Cloud service. Sampled every 86400 seconds. After sampling, data is not visible for up to 86400 seconds._  
  
### cloudbuild

Metrics from [Cloud Build](https://docs.cloud.google.com/build/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `cloudbuild.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`quota/concurrent_private_pool_build_cpus/exceeded` GA ** _(project)_**   
Concurrent Private Pool Build CPUs quota exceeded error   
`DELTA`, `INT64`, `1`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric cloudbuild.googleapis.com/concurrent_private_pool_build_cpus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_private_pool_build_cpus/limit` GA ** _(project)_**   
Concurrent Private Pool Build CPUs quota limit   
`GAUGE`, `INT64`, `1{CPU}`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Current limit on quota metric cloudbuild.googleapis.com/concurrent_private_pool_build_cpus. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_private_pool_build_cpus/usage` GA ** _(project)_**   
Concurrent Private Pool Build CPUs quota usage   
`GAUGE`, `INT64`, `1{CPU}`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Current usage on quota metric cloudbuild.googleapis.com/concurrent_private_pool_build_cpus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_private_pool_c3_build_cpus/exceeded` GA ** _(project)_**   
Concurrent Private Pool C3 Build CPUs quota exceeded error   
`DELTA`, `INT64`, `1`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric cloudbuild.googleapis.com/concurrent_private_pool_c3_build_cpus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_private_pool_c3_build_cpus/limit` GA ** _(project)_**   
Concurrent Private Pool C3 Build CPUs quota limit   
`GAUGE`, `INT64`, `1{CPU}`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Current limit on quota metric cloudbuild.googleapis.com/concurrent_private_pool_c3_build_cpus. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_private_pool_c3_build_cpus/usage` GA ** _(project)_**   
Concurrent Private Pool C3 Build CPUs quota usage   
`GAUGE`, `INT64`, `1{CPU}`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Current usage on quota metric cloudbuild.googleapis.com/concurrent_private_pool_c3_build_cpus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_private_pool_n2d_build_cpus/exceeded` GA ** _(project)_**   
Concurrent Private Pool N2D Build CPUs quota exceeded error   
`DELTA`, `INT64`, `1`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric cloudbuild.googleapis.com/concurrent_private_pool_n2d_build_cpus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_private_pool_n2d_build_cpus/limit` GA ** _(project)_**   
Concurrent Private Pool N2D Build CPUs quota limit   
`GAUGE`, `INT64`, `1{CPU}`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Current limit on quota metric cloudbuild.googleapis.com/concurrent_private_pool_n2d_build_cpus. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_private_pool_n2d_build_cpus/usage` GA ** _(project)_**   
Concurrent Private Pool N2D Build CPUs quota usage   
`GAUGE`, `INT64`, `1{CPU}`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Current usage on quota metric cloudbuild.googleapis.com/concurrent_private_pool_n2d_build_cpus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_public_pool_build_cpus/exceeded` GA ** _(project)_**   
Concurrent Build CPUs (Regional Default Pool) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric cloudbuild.googleapis.com/concurrent_public_pool_build_cpus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_public_pool_build_cpus/limit` GA ** _(project)_**   
Concurrent Build CPUs (Regional Default Pool) quota limit   
`GAUGE`, `INT64`, `1{CPU}`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Current limit on quota metric cloudbuild.googleapis.com/concurrent_public_pool_build_cpus. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
`quota/concurrent_public_pool_build_cpus/usage` GA ** _(project)_**   
Concurrent Build CPUs (Regional Default Pool) quota usage   
`GAUGE`, `INT64`, `1{CPU}`   
**[cloudbuild.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudbuild.googleapis.com/Location)** |  _Current usage on quota metric cloudbuild.googleapis.com/concurrent_public_pool_build_cpus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`build_origin`: The source on which the build was submitted (e.g. platform such as Cloud Functions).   
  
### clouddeploy

Metrics from [Cloud Deploy](https://docs.cloud.google.com/deploy/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `clouddeploy.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`quota/deployment_time/exceeded` GA ** _(project)_**   
Deployment Time quota exceeded error   
`DELTA`, `INT64`, `1`   
**[clouddeploy.googleapis.com/DeliveryPipeline](https://docs.cloud.google.com/monitoring/api/resources#tag_clouddeploy.googleapis.com/DeliveryPipeline)** |  _Number of attempts to exceed the limit on quota metric clouddeploy.googleapis.com/deployment_time. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/deployment_time/limit` GA ** _(project)_**   
Deployment Time quota limit   
`GAUGE`, `INT64`, `s`   
**[clouddeploy.googleapis.com/DeliveryPipeline](https://docs.cloud.google.com/monitoring/api/resources#tag_clouddeploy.googleapis.com/DeliveryPipeline)** |  _Current limit on quota metric clouddeploy.googleapis.com/deployment_time. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/deployment_time/usage` GA ** _(project)_**   
Deployment Time quota usage   
`DELTA`, `INT64`, `s`   
**[clouddeploy.googleapis.com/DeliveryPipeline](https://docs.cloud.google.com/monitoring/api/resources#tag_clouddeploy.googleapis.com/DeliveryPipeline)** |  _Current usage on quota metric clouddeploy.googleapis.com/deployment_time. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
  
### cloudfunctions

Metrics from [Cloud Run functions](https://docs.cloud.google.com/functions/docs) that use the `cloudfunctions.googleapis.com` API (v1 or v2). (For functions that use the `run.googleapis.com` API, see the table of metrics at [`run`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-run).) Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `cloudfunctions.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`function/active_instances` BETA ** _(project)_**   
Active instances   
`GAUGE`, `INT64`, `1`   
**[cloud_function](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_function)** |  _The number of active function instances. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`function/execution_count` GA ** _(project)_**   
Executions   
`DELTA`, `INT64`, `1`   
**[cloud_function](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_function)** |  _Count of function executions broken down by status. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`memory`: Memory assigned to function in MB.   
`status`: Execution status of the function: 'ok', 'timeout', 'error', 'crash', 'out of memory', 'out of quota', 'load error', 'load timeout', 'connection error', 'invalid header', 'request too large', 'system error', 'response error', 'invalid message'.   
`trigger_type`: Function's trigger type.   
`function/execution_times` GA ** _(project)_**   
Execution times   
`DELTA`, `DISTRIBUTION`, `ns`   
**[cloud_function](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_function)** |  _Distribution of functions execution times in nanoseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`memory`: Memory assigned to function in MB.   
`status`: Execution status of the function: 'ok', 'timeout', 'error', 'crash', 'out of memory', 'out of quota', 'load error', 'load timeout', 'connection error', 'invalid header', 'request too large', 'system error', 'response error', 'invalid message'.   
`trigger_type`: Function's trigger type.   
`function/instance_count` GA ** _(project)_**   
Instance Count   
`GAUGE`, `INT64`, `1`   
**[cloud_function](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_function)** |  _The number of function instances, broken down by state. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`state`: Whether a container is "active" or "idle".   
`function/network_egress` GA ** _(project)_**   
Network egress   
`DELTA`, `INT64`, `By`   
**[cloud_function](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_function)** |  _Outgoing network traffic of function, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`memory`: Memory assigned to function in MB.   
`trigger_type`: Function's trigger type.   
`function/user_memory_bytes` GA ** _(project)_**   
Memory usage   
`DELTA`, `DISTRIBUTION`, `By`   
**[cloud_function](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_function)** |  _Distribution of maximum function's memory usage during execution, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`memory`: Memory assigned to function in MB.   
`trigger_type`: Function's trigger type.   
`pending_queue/pending_requests` ALPHA ** _(project)_**   
Pending Requests   
`GAUGE`, `INT64`, `1`   
**[cloud_function](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_function)** |  _Number of pending requests. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`memory`: Memory assigned to function in MB.   
`trigger_type`: Function's trigger type.   
  
### cloudkms

Metrics from [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `cloudkms.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`ekm/external/request_count` GA ** _(project)_**   
Requests to the EKM service   
`DELTA`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Requests to the External Key Manager service since the last sample._   
`ekm_service_region`: The Google Cloud region from which latency to the EKM is measured, for example, "us-east1". For Cloud KMS keys in a multi-region location, latency is measured separately for each region in the multi-region.   
`method`: The name of the RPC method on the EKM, such as "wrap" and "unwrap".   
`final`: (BOOL) Indicates whether this is the last request to the EKM for a given Cloud KMS request.   
`response_code`: (INT64) HTTP response status code from the EKM service. Invalid status codes (>599 or <100) are set to -1. Non-HTTP errors, for example, DNS errors are set to 0.   
`status`: Cloud EKM response status that supplements the "response_code". For example, if the EKM fails to return an HTTP response, then "response_code" is 0 and the "status" indicates whether the cause is a timeout, DNS or TLS issue, etc. "OK" indicates a successful response from the EKM.   
`ekm/external/request_latencies` GA ** _(project)_**   
Latencies to the EKM service   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Distribution of latencies to the External Key Manager service, in milliseconds._   
`ekm_service_region`: The Google Cloud region from which latency to the EKM is measured, for example, "us-east1". For Cloud KMS keys in a multi-region location, latency is measured separately for each region in the multi-region.   
`method`: The name of the RPC method on the EKM, such as "wrap" and "unwrap".   
`final`: (BOOL) Indicates whether this is the last request to the EKM for a given Cloud KMS request.   
`peak_qps` GA ** _(project)_**   
Peak crypto ops   
`GAUGE`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _The project's maximum per-second crypto request count. The period must be one minute or longer. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`crypto_op`: Type of cryptographic operation of the request, corresponding to the KMS quotas.   
`quota/external_kms_multiregion_requests/exceeded` GA ** _(project)_**   
External KMS cryptographic requests Multiregions quota exceeded error   
`DELTA`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Number of attempts to exceed the limit on quota metric cloudkms.googleapis.com/external_kms_multiregion_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multiregion`: The region the quota applies to, only dual or multiregions.   
`quota/external_kms_multiregion_requests/limit` GA ** _(project)_**   
External KMS cryptographic requests Multiregions quota limit   
`GAUGE`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Current limit on quota metric cloudkms.googleapis.com/external_kms_multiregion_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multiregion`: The region the quota applies to, only dual or multiregions.   
`quota/external_kms_multiregion_requests/usage` GA ** _(project)_**   
External KMS cryptographic requests Multiregions quota usage   
`DELTA`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Current usage on quota metric cloudkms.googleapis.com/external_kms_multiregion_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`multiregion`: The region the quota applies to, only dual or multiregions.   
`quota/hsm_multiregion_asymmetric_requests/exceeded` GA ** _(project)_**   
HSM asymmetric cryptographic requests Multiregions quota exceeded error   
`DELTA`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Number of attempts to exceed the limit on quota metric cloudkms.googleapis.com/hsm_multiregion_asymmetric_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multiregion`: The region the quota applies to, only dual or multiregions.   
`quota/hsm_multiregion_asymmetric_requests/limit` GA ** _(project)_**   
HSM asymmetric cryptographic requests Multiregions quota limit   
`GAUGE`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Current limit on quota metric cloudkms.googleapis.com/hsm_multiregion_asymmetric_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multiregion`: The region the quota applies to, only dual or multiregions.   
`quota/hsm_multiregion_asymmetric_requests/usage` GA ** _(project)_**   
HSM asymmetric cryptographic requests Multiregions quota usage   
`DELTA`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Current usage on quota metric cloudkms.googleapis.com/hsm_multiregion_asymmetric_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`multiregion`: The region the quota applies to, only dual or multiregions.   
`quota/hsm_multiregion_symmetric_requests/exceeded` GA ** _(project)_**   
HSM symmetric cryptographic requests Multiregions quota exceeded error   
`DELTA`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Number of attempts to exceed the limit on quota metric cloudkms.googleapis.com/hsm_multiregion_symmetric_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multiregion`: The region the quota applies to, only dual or multiregions.   
`quota/hsm_multiregion_symmetric_requests/limit` GA ** _(project)_**   
HSM symmetric cryptographic requests Multiregions quota limit   
`GAUGE`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Current limit on quota metric cloudkms.googleapis.com/hsm_multiregion_symmetric_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multiregion`: The region the quota applies to, only dual or multiregions.   
`quota/hsm_multiregion_symmetric_requests/usage` GA ** _(project)_**   
HSM symmetric cryptographic requests Multiregions quota usage   
`DELTA`, `INT64`, `1`   
**[cloudkms.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudkms.googleapis.com/Project)** |  _Current usage on quota metric cloudkms.googleapis.com/hsm_multiregion_symmetric_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`multiregion`: The region the quota applies to, only dual or multiregions.   
  
### cloudsql

Metrics from [Cloud SQL](https://docs.cloud.google.com/sql/docs). Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `cloudsql.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`client/connector/closed_connection_count` BETA ** _(project)_**   
Connectors Closed Connections   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql.googleapis.com/InstanceClient](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql.googleapis.com/InstanceClient)** |  _The total number of closed connections to Cloud SQL instances._   
`instance_auth_type`: Authentication type used, one of [built_in, iam].   
`instance_ip_type`: IP address type of the connection, one of [public, psa, psc].   
`status`: Close connections status [success, error].   
`client/connector/connect_latencies` BETA ** _(project)_**   
Connectors Connect Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[cloudsql.googleapis.com/InstanceClient](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql.googleapis.com/InstanceClient)** |  _Distribution of the Cloud SQL connector connect latencies._   
`instance_auth_type`: Authentication type used, one of [built_in, iam].   
`instance_ip_type`: IP address type of the connection, one of [public, psa, psc].   
`client/connector/connection_durations` BETA ** _(project)_**   
Connectors Connection Duration   
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**[cloudsql.googleapis.com/InstanceClient](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql.googleapis.com/InstanceClient)** |  _Distribution of connection duration in seconds between connection open and close._   
`instance_auth_type`: Authentication type used, one of [built_in, iam].   
`instance_ip_type`: IP address type of the connection, one of [public, psa, psc].   
`client/connector/open_connection_count` BETA ** _(project)_**   
Connectors Connection Attempt Count   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql.googleapis.com/InstanceClient](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql.googleapis.com/InstanceClient)** |  _Total count of connection attempts made by the connector._   
`instance_auth_type`: Authentication type used, one of [built_in, iam].   
`instance_ip_type`: IP address type of the connection, one of [public, psa, psc].   
`connection_part`: If status is not success, which part of the connection errors out, one of [client_to_proxy, proxy_to_server].   
`status`: Status of the dial attempt, one of [success, user_error, cache_error, tcp_error, tls_error, auth_error, refresh_failed_error, refresh_expired_error, dns_lookup_error, unkown_error].   
`client/connector/open_connections` BETA ** _(project)_**   
Connectors Open Connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql.googleapis.com/InstanceClient](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql.googleapis.com/InstanceClient)** |  _Number of currently open connections per language connector client instance._   
`instance_auth_type`: Authentication type used, one of [built_in, iam].   
`instance_ip_type`: IP address type of the connection, one of [public, psa, psc].   
`database/active_directory/domain_reachable` GA ** _(project)_**   
Active Directory domain reachable   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the instance is able to ping a domain controller from the connected Managed Active Directory domain. If false, Windows Authentication may not work as expected. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/active_directory/instance_available` GA ** _(project)_**   
Windows Authentication available   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the instance is currently available using Windows Authentication. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/auto_failover_request_count` GA ** _(project)_**   
Auto-failover Requests   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta of number of instance auto-failover requests. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/available_for_failover` GA ** _(project)_**   
Available for failover   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _This is > 0 if the failover operation is available on the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/cpu/reserved_cores` GA ** _(project)_**   
CPU reserved cores   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of cores reserved for the database. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/cpu/usage_time` GA ** _(project)_**   
CPU usage   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Cumulative CPU usage time in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current CPU utilization represented as a percentage of the reserved CPU that is currently in use. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0). Charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/data_cache/bytes_used` GA ** _(project)_**   
Data cache used   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Data cache usage in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/data_cache/quota` GA ** _(project)_**   
Data cache quota   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Maximum data cache size in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/bytes_used` GA ** _(project)_**   
Bytes used   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Data utilization in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/bytes_used_by_data_type` GA ** _(project)_**   
Bytes used   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Data utilization in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`data_type`: A breakdown of instance disk usage per data_type, for example, 'data', 'tmp_data' or 'slow_log'.   
`database/disk/provisioning/iops` GA ** _(project)_**   
Provisioned IOPS   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Provisioned IOPS for the data disk. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/provisioning/throughput` GA ** _(project)_**   
Provisioned throughput   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Provisioned throughput for the data disk. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`io_type`: Direction of the throughput.   
`database/disk/quota` GA ** _(project)_**   
Disk quota   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Maximum data disk size in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/read_bytes_count` GA ** _(project)_**   
Disk read bytes   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk read IO bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/read_ops_count` GA ** _(project)_**   
Disk read IO   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk read IO operations. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/utilization` GA ** _(project)_**   
Disk utilization   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The fraction of the disk quota that is currently in use. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/write_bytes_count` GA ** _(project)_**   
Disk write bytes   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk write IO bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/write_ops_count` GA ** _(project)_**   
Disk write IO   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk write IO operations. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/instance_state` GA ** _(project)_**   
Instance state   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The current serving state of the Cloud SQL instance. Because there are seven possible states, seven data points are returned. Each of them has a different field value representing each state. Only the one that matches the current state of the instance is TRUE. All the others are FALSE. The state can be one of the following: RUNNING: The instance is running, or is ready to run when accessed. SUSPENDED: The instance is not available, for example due to problems with billing. RUNNABLE: The instance has been stopped by owner. It is not currently running, but it's ready to be restarted. PENDING_CREATE: The instance is being created. MAINTENANCE: The instance is down for maintenance. FAILED: The instance creation failed. UNKNOWN_STATE: The state of the instance is unknown. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: The state of the instance.   
`database/memory/components` BETA ** _(project)_**   
Memory components   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Memory stats components in percentage as usage, cache and free memory for the database. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`component`: Name of the component, one of [usage, cache and free].   
`database/memory/quota` GA ** _(project)_**   
Memory quota   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Maximum RAM size in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/memory/total_usage` GA ** _(project)_**   
Total memory usage   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total RAM usage in bytes. This metric reports the RAM usage of the database process, including the buffer/cache. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/memory/usage` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _RAM usage in bytes. This metric reports the RAM usage of the server, excluding the buffer/cache. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/memory/utilization` GA ** _(project)_**   
Memory utilization   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The fraction of the memory quota that is currently in use. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/aborted_clients_count` GA ** _(project)_**   
MySQL Aborted Clients Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Connections that were aborted because the client died without closing the connection properly, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/aborted_connects_count` GA ** _(project)_**   
MySQL Aborted Connects Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Failed attempts to connect to the MySQL server, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/conn_pool/avg_wait_time` GA ** _(project)_**   
MySQL Connection Pool Average Wait Time   
`GAUGE`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Average time spent by the connection on the work queue in milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/conn_pool/pending_connections` GA ** _(project)_**   
MySQL Connection Pool Pending Connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections presently enqueued in the work queue. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/conn_pool/threads` GA ** _(project)_**   
MySQL Connection Pool Threads   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of threads in the connection pool. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`status`: Status of the connection pool threads e.g. 'active' or 'idle'.   
`database/mysql/connections_count` GA ** _(project)_**   
MySQL Connections Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Connection attempts (successful or not) to the MySQL server, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/ddl_operations_count` GA ** _(project)_**   
MySQL DDL Operations Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _MySQL DDL operations, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of DDL operations, one of [create_table, drop_table, alter_table, rename_table, truncate_table].   
`database/mysql/dml_operations_count` GA ** _(project)_**   
MySQL DML Operations Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _MySQL DML operations, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of DML operations, one of [insert, insert_select, update, delete, replace, replace_select].   
`database/mysql/external_sync/replica_lag` GA ** _(project)_**   
Replica lag   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _An approximation of the lag (seconds behind primary) between the Cloud SQL MySQL external replica and its primary. Only applicable to Cloud SQL MySQL external replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`channel_name`: Name of the channel on which the replica is connected to the external server.   
`database/mysql/handler_operations_count` GA ** _(project)_**   
MySQL Handler Operations Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _MySQL handler operations, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of operation handler type, one of [delete, read_first, read_key, read_last, read_next, read_prev, read_rnd, read_rnd_next, update, write].   
`database/mysql/innodb/active_transactions` GA ** _(project)_**   
InnoDB Active Transactions   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of active Transaction details(trx which are in progress), Values in bracket are meant for innodb_transaction_state (Total/running/lock_wait/rolling_back/committing). Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: Values in bracket are meant for innodb_transaction_state, one of [Total, running, lock_wait, rolling_back, committing].   
`database/mysql/innodb/active_trx_longest_time` GA ** _(project)_**   
InnoDB Active TRX Longest Time   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Largest transaction time from currently active innodb transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/active_trx_rows_locked` GA ** _(project)_**   
InnoDB Active TRX Rows Locked   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of rows locked by currently active innodb transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/active_trx_rows_modified` GA ** _(project)_**   
InnoDB Active TRX Rows Modified   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of rows modified by currently active innodb transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/active_trx_total_time` GA ** _(project)_**   
InnoDB Active TRX Total Time   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Duration of currently active innodb transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/adaptive_hash_operation_count` GA ** _(project)_**   
Innodb AHI operations   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total internal row operations (rows added, updated, removed) performed to maintain the AHI since last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: AHI operation type.   
`database/mysql/innodb/ahi_search_count` GA ** _(project)_**   
AHI or Btree searches   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total search operations on the InnoDB AHI and its efficiency since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Operation type.   
`database/mysql/innodb/buffer_flush_sync_waits_count` GA ** _(project)_**   
Innodb sync flushing waits   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of times InnoDB has performed synchronous buffer flush operations and blocking the user transactions since last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/buffer_pool_pages` GA ** _(project)_**   
InnoDB Buffer Pool Pages   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of InnoDB buffer pool pages, innodb_page_type field stores count of InnoDB pages in each state. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`innodb_page_type`: Kind of InnoDB page, one of [dirty, free, Total]   
`database/mysql/innodb/buffer_pool_read_requests_count` GA ** _(project)_**   
Innodb Buffer Pool Read Requests Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Logical read requests from InnoDB buffer pool, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/buffer_pool_reads_count` GA ** _(project)_**   
Innodb Buffer Pool Reads Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Logical reads that InnoDB could not satisfy from the buffer pool, and had to read directly from disk, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/buffer_pool_write_requests_count` GA ** _(project)_**   
InnoDB Buffer Pool Write Requests Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Writes done to the InnoDB buffer pool, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_cache/cache_hit_count` GA ** _(project)_**   
MySQL data cache hit count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache hit read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_cache/cache_miss_count` GA ** _(project)_**   
MySQL data cache miss count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache miss read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_cache/pages` GA ** _(project)_**   
Innodb Pages in Data Cache   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of Innodb pages in Mysqls E+ Data cache feature. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`page_type`: Page types in data cache.   
`database/mysql/innodb/data_fsyncs_count` GA ** _(project)_**   
Innodb Data Fsyncs Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _InnoDB fsync() calls, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_pending_fsyncs` GA ** _(project)_**   
InnoDB Data Pending Fsyncs   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of pending fsync() operations in the MySQL server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_pending_reads` GA ** _(project)_**   
InnoDB Data Pending Reads   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of pending reads in the MySQL Server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_pending_writes` GA ** _(project)_**   
InnoDB Data Pending Writes   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of pending writes in the MySQL Server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/deadlocks_count` GA ** _(project)_**   
InnoDB Deadlocks Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Deadlocks, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/dictionary_memory` GA ** _(project)_**   
MySQL InnoDB dictionary cache   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Memory allocated for InnoDB dictionary cache. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/history_list_length` GA ** _(project)_**   
InnoDB History List Length   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates the size of undo logs which are used to store modifications made to older versions of rows. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/ibuf_merge_operation_count` GA ** _(project)_**   
InnoDB merged records operation wise   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of records type merged by the change buffering operation since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of merge operation. One of ibuf_merges_insert,ibuf_merges_delete_mark,ibuf_merges_delete.   
`database/mysql/innodb/ibuf_merges_count` GA ** _(project)_**   
InnoDB change buffer merges.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of change buffer merges since the last sample. This shows the efficiency of all change buffer operations. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/innodb_log_waits_count` GA ** _(project)_**   
Transaction waits for Innodb logbuffer flush   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of transactions wait for space to become available in the InnoDB log buffer, to help tune innodb_log_buffer_size configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/lock_timeout_count` GA ** _(project)_**   
Innodb Row Lock Wait Timeout Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Row lock wait timeouts, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/lsn` GA ** _(project)_**   
InnoDB LSN   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Value of Innodb current/flushed/last_checkpoint log sequence number. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`lsn_type`: Type of LSN being reported out of current/flushed/last_checkpoint.   
`database/mysql/innodb/operation_disk_io_count` GA ** _(project)_**   
Disk IO performed by InnoDB.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Disk IO operations performed by InnoDB since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of Disk IO operation. One of innodb_data_reads, innodb_data_writes, innodb_log_writes, innodb_dblwr_writes.   
`database/mysql/innodb/os_log_fsyncs_count` GA ** _(project)_**   
Innodb OS Log Fsyncs Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _InnoDB fsync() calls to the log file, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/os_log_pending_fsyncs` GA ** _(project)_**   
InnoDB OS Log Pending Fsyncs   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of pending fsync() operations for the InnoDB redo log files in the MySQL server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/os_log_pending_writes` GA ** _(project)_**   
InnoDB OS Log Pending Writes   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of pending writes to the InnoDB redo log files in the MySQL server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/pages_read_count` GA ** _(project)_**   
Innodb Pages Read Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _InnoDB pages read, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/pages_written_count` GA ** _(project)_**   
Innodb Pages Written Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _DInnoDB pages written, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/row_lock_time` GA ** _(project)_**   
InnoDB Row Lock Time   
`GAUGE`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The total time spent in acquiring row locks for InnoDB tables. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/row_lock_waits_count` GA ** _(project)_**   
InnoDB Row Lock Waits Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Times operations on InnoDB tables had to wait for a row lock, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/row_operations_count` GA ** _(project)_**   
InnoDB Row Operations Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _InnoDB row operations, operation_type field stores the count of InnoDB row operations, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of InnoDB row operations, one of [delete, insert, read, update]   
`database/mysql/innodb_buffer_pool_pages_dirty` GA ** _(project)_**   
InnoDB dirty pages   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of unflushed pages in the InnoDB buffer pool. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_buffer_pool_pages_free` GA ** _(project)_**   
InnoDB free pages   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of unused pages in the InnoDB buffer pool. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_buffer_pool_pages_total` GA ** _(project)_**   
InnoDB total pages   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of pages in the InnoDB buffer pool. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_data_fsyncs` GA ** _(project)_**   
InnoDB fsync calls   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of InnoDB fsync() calls. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_os_log_fsyncs` GA ** _(project)_**   
InnoDB log fsync calls   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of InnoDB fsync() calls to the log file. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_pages_read` GA ** _(project)_**   
InnoDB pages read   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of InnoDB pages read. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_pages_written` GA ** _(project)_**   
InnoDB pages written   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of InnoDB pages written. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/max_connections` GA ** _(project)_**   
MySQL Max Connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Value of the MySQL max_connections configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/memory/by_code_area` GA ** _(project)_**   
Memory allocated by code area   
`GAUGE`, `DOUBLE`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Memory allocated to each code area, reported by mysql performance_schema. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`code_area_group`: Kind of Mysql code area, one of [innodb_engine,sql,performance_schema,temptable_engine,memory_engine,mysys]   
`database/mysql/memory/by_event` GA ** _(project)_**   
Memory allocated by events   
`GAUGE`, `DOUBLE`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Memory allocated by each event, reported by performance_schema. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`event_type`: Kind of Mysql event, one of [innodb_hash0hash,innodb_memory,innodb_row0sel,sql_table,sql_thd_main,sql_dd,sql_string,mysys_iocache]   
`database/mysql/memory/global` GA ** _(project)_**   
Global memory allocated   
`GAUGE`, `DOUBLE`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The total allocated memory, reported by performance_schema. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/open_table_definitions` GA ** _(project)_**   
MySQL open table definitions   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of table definitions that are currently cached. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/open_tables` GA ** _(project)_**   
MySQL open tables   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of tables that are currently open. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/opened_table_count` GA ** _(project)_**   
MySQL opened table count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of tables that have been opened since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/opened_table_definitions_count` GA ** _(project)_**   
MySQL opened table definitions count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of table definitions that have been cached since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/queries` GA ** _(project)_**   
Queries   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of statements executed by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/questions` GA ** _(project)_**   
Questions   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of statements executed by the server sent by the client. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/received_bytes_count` GA ** _(project)_**   
Network bytes received by MySQL   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of bytes received by MySQL process. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/available_for_failover` DEPRECATED ** _(project)_**   
Available for failover (Deprecated)   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _This is > 0 if the failover operation is available on the master instance.master. The metric is deprecated. Please use cloudsql.googleapis.com/database/available_for_failover instead. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/last_io_errno` GA ** _(project)_**   
Last I/O thread error number.   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The error number of the most recent error that caused the I/O thread to stop. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/last_sql_errno` GA ** _(project)_**   
Last SQL thread error number.   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The error number of the most recent error that caused the SQL thread to stop. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/seconds_behind_master` GA ** _(project)_**   
Replication lag   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of seconds the read replica is behind its primary (approximation). A negative value indicates that replication is inactive. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/slave_io_running` GA ** _(project)_**   
Slave I/O thread running   
`GAUGE`, `STRING`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the I/O thread for reading the primary's binary log is running. Possible values are Yes, No and Connecting. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/slave_io_running_state` GA ** _(project)_**   
Slave I/O thread running state   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the I/O thread for reading the primary's binary log is running. Possible values are Yes, No and Connecting, and the values are exposed through the 'state' field. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: The slave_io_running state of the slave.   
`database/mysql/replication/slave_sql_running` GA ** _(project)_**   
Slave SQL thread running   
`GAUGE`, `STRING`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the SQL thread for executing events in the relay log is running. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/slave_sql_running_state` GA ** _(project)_**   
Slave SQL thread running state   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the SQL thread for executing events in the relay log is running. Possible values are Yes / No, and the values are exposed through the 'state' field. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: The slave_sql_running state of the slave.   
`database/mysql/sent_bytes_count` GA ** _(project)_**   
Network bytes sent by MySQL   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of bytes sent by MySQL process. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/slow_queries_count` GA ** _(project)_**   
MySQL slow queries count.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The total number of queries that took longer than long_query_time seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/thread_cache_size` GA ** _(project)_**   
MySQL Thread Cache Size   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Value of the MySQL thread_cache_size configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/thread_state` GA ** _(project)_**   
MySQL threads state   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The state of running threads by querying information_schema.processlist table, this information helps to understand the locking or contention issues. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: Thread state.   
`database/mysql/threads` GA ** _(project)_**   
MySQL Thread   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of Threads. threads_cached indicates threads in the thread cache, threads_connected indicates currently open connections, threads_running indicates threads that are not sleeping. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`thread_kind`: Kind of the threads counted (threads_cached, threads_connected, threads_running).   
`database/mysql/threads_created_count` GA ** _(project)_**   
MySQL Threads Created Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Threads created to handle connections, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/tmp_disk_tables_created_count` GA ** _(project)_**   
MySQL Temporary Disk Tables Created Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Internal on-disk temporary tables created by the MySQL server while executing statements, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/tmp_files_created_count` GA ** _(project)_**   
MySQL Temporary Files Created Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Temporary files created by the MySQL server, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/tmp_tables_created_count` GA ** _(project)_**   
MySQL Temporary Tables Created Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _MySQL temporary tables created, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/network/connection_attempt_count` GA ** _(project)_**   
Cloud SQL Connection Attempts   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of connection attempts to the Cloud SQL instance, with information about anomaly detection. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`login_status`: Login status, one of [succeeded, failed].   
`anomaly_detected`: Connection related anomaly, for example, "no anomaly detected", "brute-force login".   
`anomalous_connection_throttled`: (BOOL) Whether the connection is throttled if it's anomalous.   
`database/network/connections` GA ** _(project)_**   
Cloud SQL Connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections to databases on the Cloud SQL instance. Only applicable to MySQL and SQL Server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/network/received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of bytes received through the network. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/network/sent_bytes_count` GA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of bytes sent through the network. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`destination`: Deprecated and not populated.   
`database/postgresql/backends_in_wait` GA ** _(project)_**   
PostgreSQL backends in wait   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of backends in wait in postgres instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`backend_type`: Type of the backend, one of [autovacuum launcher, autovacuum worker, logical replication launcher, logical replication worker, parallel worker, background writer, client backend, checkpointer, archiver, startup, walreceiver, walsender, walwriter].   
`wait_event`: Name of the wait event, such as AutoVacuumMain, ClientRead.   
`wait_event_type`: Type of wait event, one of [Activity, BufferPin, Extension, IO, IPC, Lock, LWLock, Timeout].   
`database/postgresql/blocks_read_count` GA ** _(project)_**   
Number of disk blocks read.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of disk blocks read by this database. The source field distingushes actual reads from disk versus reads from buffer cache. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`source`: Type of data block, one of [disk, buffer_cache].   
`database/postgresql/checkpoint_count` GA ** _(project)_**   
Checkpoint count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total checkpoints occurred. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`checkpoint_type`: Type of checkpoint, can be one of [scheduled, requested].   
`database/postgresql/data_cache/hit_count` GA ** _(project)_**   
PostgreSQL data cache hit count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache hit read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/data_cache/hit_ratio` GA ** _(project)_**   
PostgreSQL data cache hit ratio   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Ratio of data cache hit read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/data_cache/miss_count` GA ** _(project)_**   
PostgreSQL data cache miss count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache miss read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/deadlock_count` GA ** _(project)_**   
Deadlocks count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of deadlocks detected for this database. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/disk/read_bytes_count` GA ** _(project)_**   
Bytes read by PostgreSQL   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta number of bytes read by PostgreSQL. Only available for PostgreSQL 16 and higher. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`backend_type`: Type of backend.   
`object`: Target object of the read operation.   
`context`: The context of the read operation.   
`database/postgresql/disk/write_bytes_count` GA ** _(project)_**   
Bytes written by PostgreSQL   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta number of bytes written by PostgreSQL. Only available for PostgreSQL 16 and higher. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`backend_type`: Type of backend.   
`object`: Target object of the write operation.   
`context`: The context of the write operation.   
`database/postgresql/external_sync/initial_sync_complete` ALPHA ** _(project)_**   
Initial sync complete   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Whether all databases on the Postgres External Server (ES) replica have completed the initial sync and are replicating changes from the source. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/external_sync/max_replica_byte_lag` ALPHA ** _(project)_**   
Max lag bytes   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Replication lag in bytes for Postgres External Server (ES) replicas. Aggregated across all DBs on the replica. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/insights/aggregate/execution_time` GA ** _(project)_**   
Execution time   
`CUMULATIVE`, `INT64`, `us{CPU}`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated query execution time per user per database. This is the sum of cpu time, io wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`database/postgresql/insights/aggregate/io_time` GA ** _(project)_**   
IO time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated IO time per user per database._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`io_type`: The IO type (read/write).   
`database/postgresql/insights/aggregate/latencies` GA ** _(project)_**   
Latency   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Query latency distribution per user per database._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`database/postgresql/insights/aggregate/lock_time` GA ** _(project)_**   
Aggregated lock time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated lock wait time per user per database._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`lock_type`: The lock type (lw/hw/buffer_pin).   
`database/postgresql/insights/aggregate/row_count` GA ** _(project)_**   
Affected rows   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of rows affected during query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`database/postgresql/insights/aggregate/shared_blk_access_count` GA ** _(project)_**   
Shared blocks cache access.   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Shared blocks (regular tables & indexed) accessed by statement execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`access_type`: The block access type (hit/miss).   
`database/postgresql/insights/perquery/execution_time` GA ** _(project)_**   
Per query execution times   
`CUMULATIVE`, `INT64`, `us{CPU}`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated execution times per user per database per query.This is the sum of cpu time, io wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/io_time` GA ** _(project)_**   
Per query IO time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated IO time per user per database per query._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`io_type`: The IO type (read/write).   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/latencies` GA ** _(project)_**   
Per query latency   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Query latency distribution per user per database per query._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/lock_time` GA ** _(project)_**   
Per query lock time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated lock wait time per user per database per query._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`lock_type`: The lock type (lw/hw/buffer_pin).   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/row_count` GA ** _(project)_**   
Per query affected rows   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of rows affected during query execution._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/shared_blk_access_count` GA ** _(project)_**   
Per query Shared blocks cache access   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Shared blocks (regular tables & indexed) accesssed by statement execution._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`access_type`: The block access type (hit/miss).   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/pertag/execution_time` GA ** _(project)_**   
Per tag execution time   
`CUMULATIVE`, `INT64`, `us{CPU}`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated execution times per user per database per tag.This is the sum of cpu time, io wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/io_time` GA ** _(project)_**   
Per tag IO time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated IO write time per user per database per tag._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`io_type`: The IO type (read/write).   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/latencies` GA ** _(project)_**   
Per tag latency   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Query latency distribution per user per database per tag._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/lock_time` GA ** _(project)_**   
Per tag lock time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated lock wait time per user per database per tag._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`lock_type`: The lock type (lw/hw/buffer_pin).   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/row_count` GA ** _(project)_**   
Per tag affected rows   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of rows affected during query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/shared_blk_access_count` GA ** _(project)_**   
Per tag shared blocks cache accessed   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Shared blocks (regular tables & indexed) accessed by statement execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`access_type`: The block access type (hit/miss).   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/new_connection_count` GA ** _(project)_**   
PostgreSQL new connections count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Count of new connections added to the postgres instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database, such as testdb.   
`database/postgresql/num_backends` GA ** _(project)_**   
PostgreSQL Connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections to the Cloud SQL PostgreSQL instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/num_backends_by_application` GA ** _(project)_**   
PostgreSQL connections by application   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections to the Cloud SQL PostgreSQL instance, grouped by applications. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`application`: Name of the application.   
`database/postgresql/num_backends_by_state` GA ** _(project)_**   
PostgreSQL Connections by State   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections to the Cloud SQL PostgreSQL instance, grouped by its state. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`state`: Connection state, one of [idle, active, idle_in_transaction, idle_in_transaction_aborted, disabled or fastpath_function_call].   
`database/postgresql/replication/replica_byte_lag` GA ** _(project)_**   
Lag bytes   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Replication lag in bytes. Reported from the master per replica. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`replica_name`: Name of the replica.   
`replica_lag_type`: Type of lag. This can be either replay_location, flush_location, write_location or sent_location.   
`database/postgresql/statements_executed_count` GA ** _(project)_**   
Statements executed count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total count of statements executed in postgresql instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`operation_type`: Type of the operation performed.   
`database/postgresql/temp_bytes_written_count` GA ** _(project)_**   
Data (in bytes) written to temporary   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total amount of data (in bytes) written to temporary files by the queries per database. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/temp_files_written_count` GA ** _(project)_**   
Temporary files used for writing data   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of temporary files used for writing data while performing algorithms such as join and sort. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/transaction_count` GA ** _(project)_**   
Number of transactions   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of number of transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`transaction_type`: transaction_type can be commit or rollback.   
`database/postgresql/transaction_id_count` GA ** _(project)_**   
Transaction ID count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of transaction ID. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`action`: Type of action, one of ["assigned" - count of transaction IDs assigned and consumed by the instance; "frozen" - count of transaction IDs replenished by the VACUUM`s freeze operation].   
`database/postgresql/transaction_id_utilization` GA ** _(project)_**   
Transaction ID utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current utilization represented as a percentage of transaction IDs consumed by the Cloud SQL PostgreSQL instance. Values are typically numbers between 0.0 and 1.0. Charts display the values as a percentage between 0% and 100%. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/tuple_size` GA ** _(project)_**   
Number of tuples (rows) in the database.   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of tuples (rows) in the database. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`tuple_state`: Type of tuple state, one of [live, dead].   
`database/postgresql/tuples_fetched_count` GA ** _(project)_**   
Number of tuples fetched   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of rows fetched as a result of queries per database in the PostgreSQL instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/tuples_processed_count` GA ** _(project)_**   
Number of rows processed   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of tuples(rows) processed for a given database for operations like insert, update or delete. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Type of database operation, one of [insert, update, delete].   
`database`: Name of the database.   
`database/postgresql/tuples_returned_count` GA ** _(project)_**   
Number of tuples returned   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of rows scanned while processing the queries per database in the PostgreSQL instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/vacuum/oldest_transaction_age` GA ** _(project)_**   
Oldest transaction age   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Age of the oldest transaction yet to be vacuumed in the Cloud SQL PostgreSQL instance, measured in number of transactions that have happened since the oldest transaction. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`oldest_transaction_type`: oldest transaction type can be one of [running, prepared, replication_slot, replica].   
`database/postgresql/write_ahead_log/flushed_bytes_count` GA ** _(project)_**   
PostgreSQL WAL flushed bytes count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total size (bytes) of WAL flushed for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/write_ahead_log/inserted_bytes_count` GA ** _(project)_**   
PostgreSQL WAL inserted bytes count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total size (bytes) of WAL inserted for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/write_ahead_log/redo_size` GA ** _(project)_**   
PostgreSQL redo size metric   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The size (bytes) of WAL to redo in case of recovery. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/write_ahead_log/written_bytes_count` GA ** _(project)_**   
PostgreSQL WAL written bytes count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total size (bytes) of WAL written for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/readpool/expected_pool_nodes` GA ** _(project)_**   
Expected Read Pool Nodes   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of nodes in the read pool. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/replication/log_archive_failure_count` GA ** _(project)_**   
Number of log archival failures.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of failed attempts for archiving replication log files. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/replication/log_archive_success_count` GA ** _(project)_**   
Number of log archival successes.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of successful attempts for archiving replication log files. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/replication/network_lag` GA ** _(project)_**   
Network lag   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates time taken from primary binary log to IO thread on replica. Only applicable to replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/replication/replica_lag` GA ** _(project)_**   
Replication lag   
`GAUGE`, `DOUBLE`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of seconds the read replica is behind its primary (approximation). A negative value indicates that replication is inactive. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/replication/state` BETA ** _(project)_**   
Replication state   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The current serving state of replication. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: State of replication:"Running" - Replication is active and running;"Stopped" - Replication is inactive and stopped;"Error" - There is an error happening and replication is stopped.   
`database/sqlserver/audits_size` GA ** _(project)_**   
Size of stored audit files.   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Tracks the size in bytes of stored SQLServer audit files on an instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/audits_upload_count` GA ** _(project)_**   
Total number of successfully uploaded audits.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Counts total number of SQLServer audit file uploads to a GCS bucket and whether or not an upload was successful. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`upload_status`: Upload status of latest audit file.   
`database/sqlserver/connections/connection_reset_count` GA ** _(project)_**   
Connection resets   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of logins started from the connection pool since the last restart of SQL Server service. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/connections/login_attempt_count` GA ** _(project)_**   
Login attempts   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of login attempts since the last restart of SQL Server service. This does not include pooled connections. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/connections/logout_count` GA ** _(project)_**   
Logouts   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of logout operations since the last restart of SQL Server service. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/connections/processes_blocked` GA ** _(project)_**   
Processes blocked   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of blocked processes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/data_cache/hit_count` GA ** _(project)_**   
SQL Server data cache hit count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache hit read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/data_cache/hit_ratio` GA ** _(project)_**   
SQL Server data cache hit ratio   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Ratio of successful data cache hit read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/data_cache/miss_count` GA ** _(project)_**   
SQL Server data cache miss count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache miss read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/databases` GA ** _(project)_**   
SQL Server Databases   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of databases on the instance excluding system databases. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: Database state, for example, 'ONLINE' or 'SUSPECT'.   
`recovery_model`: Database recovery model, one of [FULL, BULK_LOGGED, SIMPLE].   
`is_cdc_enabled`: (BOOL) Indicates whether CDC is enabled.   
`is_published`: (BOOL) Indicates whether a database is published.   
`auto_close`: (BOOL) Indicates whether auto-close is enabled on a database.   
`database/sqlserver/memory/buffer_cache_hit_ratio` GA ** _(project)_**   
Buffer cache hit ratio   
`GAUGE`, `DOUBLE`, `%`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current percentage of pages found in the buffer cache without having to read from disk. The ratio is the total number of cache hits divided by the total number of cache lookups. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/checkpoint_page_count` GA ** _(project)_**   
Checkpoint pages   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of pages flushed to disk by a checkpoint or other operation that requires all dirty pages to be flushed. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/committed_kb` GA ** _(project)_**   
SQL Server committed memory   
`GAUGE`, `INT64`, `kBy`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Represents the actual amount of memory committed in the memory manager. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/committed_target_kb` GA ** _(project)_**   
SQL Server committed target memory   
`GAUGE`, `INT64`, `kBy`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Represents the desired amount of memory SQL Server wants to have available. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/free_list_stall_count` GA ** _(project)_**   
Free list stalls   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of requests that had to wait for a free page. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/lazy_write_count` GA ** _(project)_**   
Lazy writes   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of buffers written by the buffer manager's lazy writer. The lazy writer is a system process that flushes out batches of dirty, aged buffers (buffers that contain changes that must be written back to disk before the buffer can be reused for a different page) and makes them available to user processes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/memory_clerk` GA ** _(project)_**   
SQL Server memory clerk allocations   
`GAUGE`, `INT64`, `MiBy`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Specifies the amount of page memory allocated for each memory clerk. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`clerk_type`: The memory clerk type.   
`clerk_name`: The name of the memory clerk.   
`database/sqlserver/memory/memory_grants_pending` GA ** _(project)_**   
Memory grants pending   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of processes waiting for a workspace memory grant. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/page_life_expectancy` GA ** _(project)_**   
Page life expectancy   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of seconds a page will stay in the buffer pool without references. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/page_operation_count` GA ** _(project)_**   
Page operations   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of physical database page reads or writes. This statistic counts physical page reads or writes across all databases. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation`: Page operation, one of [Read, Write].   
`database/sqlserver/replication/bytes_sent_to_replica_count` GA ** _(project)_**   
Bytes sent to replica   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of bytes sent to the remote availability replica. Before compression for async replica. Actual number of bytes for sync replica which has no compression. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`database/sqlserver/replication/log_apply_pending_queue` GA ** _(project)_**   
Log apply pending queue   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of log blocks that are waiting to be applied to all database replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/replication/log_bytes_received_count` GA ** _(project)_**   
Log bytes received   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total amount of log records received by the secondary replica for all databases. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/replication/recovery_queue` GA ** _(project)_**   
Recovery queue   
`GAUGE`, `INT64`, `kBy`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current amount of log records in kilobytes in the log files of the secondary replica that have not been redone. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/replication/redone_bytes_count` GA ** _(project)_**   
Redone bytes   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total amount of log records redone on all secondary databases. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/replication/resent_message_count` GA ** _(project)_**   
Resent messages   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of Always On messages resent. A resent message is a message that was attempted to be sent but was unable to complete and must be attempted to be sent again. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`database/sqlserver/schedulers/active_workers` GA ** _(project)_**   
Number of active workers per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of workers that are active. An active worker is never preemptive, must have an associated task, and is either running, runnable, or suspended. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/schedulers/by_status` GA ** _(project)_**   
Number of schedulers   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of schedulers reporting a particular status. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`status`: Scheduler status, one of [HIDDEN ONLINE, HIDDEN OFFLINE, VISIBLE ONLINE, VISIBLE OFFLINE, VISIBLE ONLINE (DAC), HOT_ADDED].   
`is_internal`: (BOOL) Indicates whether the scheduler is internal.   
`database/sqlserver/schedulers/current_tasks` GA ** _(project)_**   
Number of current tasks per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of current tasks that are associated with a scheduler. This count includes tasks that are waiting for a worker to execute them and tasks that are currently waiting or running (in SUSPENDED or RUNNABLE state). Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/schedulers/current_workers` GA ** _(project)_**   
Number of workers per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of workers that are associated with a scheduler. It includes workers that are not assigned any task. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/schedulers/pending_disk_io` GA ** _(project)_**   
Number of pending I/O operations per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of pending I/Os that are waiting to be completed. Each scheduler has a list of pending I/Os that are checked to determine whether they have been completed every time there is a context switch. The count is incremented when the request is inserted. This count is decremented when the request is completed. This number does not indicate the state of the I/Os. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/schedulers/runnable_tasks` GA ** _(project)_**   
Number of workers with assigned tasks per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of workers, with tasks assigned to them, that are waiting to be scheduled on the runnable queue. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/schedulers/work_queue` GA ** _(project)_**   
Number of pending tasks per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of tasks in the pending queue. These tasks are waiting for a worker to pick them up. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/server_principals` GA ** _(project)_**   
Server principals   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of server principals on the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`type`: Server principal type, one of [SQL_LOGIN, WINDOWS_LOGIN, WINDOWS_GROUP, SERVER_ROLE, CERTIFICATE_MAPPED_LOGIN, EXTERNAL_LOGIN, EXTERNAL_GROUP, ASYMMETRIC_KEY_MAPPED_LOGIN].   
`is_enabled`: (BOOL) Indicates whether a server principal is enabled.   
`database/sqlserver/sql_agent/jobs` GA ** _(project)_**   
SQL Server agent jobs   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of SQL Server agent jobs on the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`is_enabled`: (BOOL) Indicates whether a job is enabled.   
`last_run_outcome`: Last outcome of a job run, one of [Fail, Succeed, Retry, Cancel, In progress, Unknown].   
`database/sqlserver/transactions/batch_request_count` GA ** _(project)_**   
Batch requests   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of Transact-SQL command batches received. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/batch_requests_cpu_time` GA ** _(project)_**   
SQL Server batch requests CPU time   
`DELTA`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total CPU time for completed batch requests, bucketed by CPU time. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`bucket`: Bucket.   
`database/sqlserver/transactions/batch_requests_cpu_time_count` GA ** _(project)_**   
SQL Server batch requests CPU time count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Count of completed batch requests, bucketed by CPU time. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`bucket`: Bucket.   
`database/sqlserver/transactions/batch_requests_elapsed_time` GA ** _(project)_**   
SQL Server batch requests elapsed time   
`DELTA`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total elapsed time for completed batch requests, bucketed by the elapsed time of each batch statement. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`bucket`: Bucket.   
`database/sqlserver/transactions/batch_requests_elapsed_time_count` GA ** _(project)_**   
SQL Server batch requests elapsed time count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Count of completed batch requests bucketed by elapsed time. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`bucket`: Bucket.   
`database/sqlserver/transactions/deadlock_count` GA ** _(project)_**   
Deadlocks   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of lock requests that resulted in a deadlock. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`database/sqlserver/transactions/forwarded_record_count` GA ** _(project)_**   
Forwarded records   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of records fetched through forwarded record pointers. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/full_scan_count` GA ** _(project)_**   
Full scans   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of unrestricted full scans. These can be either base-table or full-index scans. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/lock_wait_count` GA ** _(project)_**   
Lock waits   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of lock requests that required the caller to wait. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`database/sqlserver/transactions/lock_wait_time` GA ** _(project)_**   
Lock wait time   
`DELTA`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total time lock requests were waiting for locks. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`database/sqlserver/transactions/log_bytes_flushed_count` GA ** _(project)_**   
Log bytes flushed   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of log bytes flushed. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Database name, one of [tempdb, model, msdb, mssqlsystemresource, master, other].   
`database/sqlserver/transactions/page_split_count` GA ** _(project)_**   
Page splits   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of page splits that occur as the result of overflowing index pages. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/probe_scan_count` GA ** _(project)_**   
Probe scans   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of probe scans that are used to find at most one single qualified row in an index or base table directly. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/sql_compilation_count` GA ** _(project)_**   
SQL compilations   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of SQL compilations. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/sql_recompilation_count` GA ** _(project)_**   
SQL recompilations   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of SQL recompilations. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/transaction_count` GA ** _(project)_**   
Transactions started   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of transactions started. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Database name, one of [tempdb, model, msdb, mssqlsystemresource, master, other].   
`database/sqlserver/wait_count` GA ** _(project)_**   
SQL Server wait count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of waits for each wait type. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`wait_type`: Wait type.   
`wait_category`: Wait category.   
`database/sqlserver/wait_time` GA ** _(project)_**   
SQL Server wait time   
`DELTA`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The accumulated wait time for each wait type. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`wait_type`: Wait type.   
`wait_category`: Wait category.   
`database/sqlserver/xevents_size` GA ** _(project)_**   
Size of stored XEvents files.   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Tracks the size in bytes of stored SQLServer XEvents files on an instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/xevents_upload_count` GA ** _(project)_**   
Total number of successfully uploaded XEvents.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Counts total number of SQLServer XEvents file uploads to a GCS bucket and whether or not an upload was successful. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`upload_status`: Upload status of latest XEvents file.   
`database/state` DEPRECATED ** _(project)_**   
State   
`GAUGE`, `STRING`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The current serving state of the Cloud SQL instance. This can be one of the following: RUNNING: The instance is *expected* to be running. If an instance experiences unplanned (non-maintenance) downtime, the state will still be RUNNING, but the database/up metric will report 0. SUSPENDED: The instance is not available, for example due to problems with billing. RUNNABLE: The instance has been stopped by owner. It is not currently running, but it's ready to be restarted. PENDING_CREATE: The instance is being created. MAINTENANCE: The instance is down for maintenance. FAILED: The instance creation failed or an operation left the instance in an unknown bad state. UNKNOWN_STATE: The state of the instance is unknown. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/swap/bytes_used` GA ** _(project)_**   
Swap space usage   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Swap space used by the database container. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/swap/pages_swapped_in_count` GA ** _(project)_**   
Pages Swapped In Count   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total count of pages swapped in of disk since the system was booted. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/swap/pages_swapped_out_count` GA ** _(project)_**   
Pages Swapped Out Count   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total count of pages swapped out of disk since the system was booted. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/up` GA ** _(project)_**   
Server up   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates if the server is up or not. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/uptime` GA ** _(project)_**   
Uptime   
`DELTA`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of the time in seconds the instance has been running. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`per_database/conn_pool/client_connections` GA ** _(project)_**   
Client connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Number of client connections per database grouped by status._   
`status`: Status of the client connection e.g. 'active' or 'waiting'.   
`per_database/conn_pool/client_connections_attempts_count` GA ** _(project)_**   
Client connection attempts count   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Number of client connection attempts received per database._  
`per_database/conn_pool/client_connections_avg_wait_time` GA ** _(project)_**   
Average wait time   
`GAUGE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Average wait time spent by clients waiting for a server connection per database in microseconds._  
`per_database/conn_pool/client_connections_error_count` GA ** _(project)_**   
Error count   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Count of errors that cause client disconnection including auth error, client connection setup error, server connection error and timeout errors._  
`per_database/conn_pool/num_pools` GA ** _(project)_**   
Number of connection pools   
`GAUGE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Number of connection pools per database._  
`per_database/conn_pool/server_connections` GA ** _(project)_**   
Server connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Number of server connections per database grouped by status._   
`status`: Status of the server connection e.g. 'active' or 'idle'.   
`per_database/postgresql/external_sync/initial_sync_complete` GA ** _(project)_**   
External server migration phase   
`GAUGE`, `BOOL`, ``   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Migration phase of each database on the external server (ES) replica. This only applies to instances that are replicating from an external server._  
`per_database/postgresql/external_sync/replication_byte_lag` GA ** _(project)_**   
Exernal server replication byte lag   
`GAUGE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Replication lag in bytes of each database on the external server (ES) replica. This only applies to instances that are replicating from an external server._  
`per_database/sqlserver/replication/delay` GA ** _(project)_**   
SQL Server replication delay   
`GAUGE`, `INT64`, `s`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _The time difference in seconds between the most recent transaction committed on the primary replica and the commit time of the most recent transaction redone on the secondary replica._   
`replica_instance_name`: Instance name of the replica.   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`availability_mode`: Availability mode of the replica.   
`per_database/sqlserver/replication/logsend_queue_size` GA ** _(project)_**   
SQL Server logsend queue size   
`GAUGE`, `INT64`, `By`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total size of log records in the log files of the primary database that haven't been sent to the secondary replica._   
`replica_instance_name`: Instance name of the replica.   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`per_database/sqlserver/replication/redo_queue_size` GA ** _(project)_**   
SQL Server redo queue size   
`GAUGE`, `INT64`, `By`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _The number of log records in the log files of the secondary replica that aren't yet redone._   
`replica_instance_name`: Instance name of the replica.   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`per_database/sqlserver/replication/seconds_behind_master` GA ** _(project)_**   
SQL Server seconds behind primary   
`GAUGE`, `INT64`, `s`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _The number of seconds since the hardening of the earliest hardened LSN on the primary replica that is yet to be hardened on the secondary replica._   
`replica_instance_name`: Instance name of the replica.   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`semi_managed/database/cpu/utilization` GA ** _(project)_**   
CPU utilization (Semi-managed)   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current CPU utilization represented as a percentage ' + 'of the reserved CPU that is currently in use. Values ' + 'are typically numbers between 0.0 and 1.0 (but ' + 'might exceed 1.0). Charts display the values as a ' + 'percentage between 0% and 100% (or more)._  
`semi_managed/database/disk/bytes_used` GA ** _(project)_**   
Bytes used (Semi-managed)   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Data utilization in bytes._   
`data_type`: A breakdown of disk usage by type of usage.   
`semi_managed/database/disk/quota` GA ** _(project)_**   
Disk quota (Semi-managed)   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Maximum data disk size in bytes._  
`semi_managed/database/disk/read_ops_count` GA ** _(project)_**   
Disk read IO (Semi-managed)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk read IO operations._  
`semi_managed/database/disk/write_ops_count` GA ** _(project)_**   
Disk write IO (Semi-managed)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk write IO operations._  
`semi_managed/database/memory/total_usage` GA ** _(project)_**   
Total memory usage (Semi-managed)   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total RAM usage in bytes including buffer cache._  
`semi_managed/database/memory/usage` GA ** _(project)_**   
Memory usage (Semi-managed)   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _RAM usage in bytes._  
`semi_managed/database/network/connections` GA ** _(project)_**   
Cloud SQL Connections (Semi-managed)   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections to databases on the Cloud SQL instance._  
`semi_managed/database/network/received_bytes_count` GA ** _(project)_**   
Received bytes (Semi-managed)   
`CUMULATIVE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Cumulative count of bytes received through the network._  
`semi_managed/database/network/sent_bytes_count` GA ** _(project)_**   
Sent bytes (Semi-managed)   
`CUMULATIVE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Cumulative count of bytes sent through the network._  
`semi_managed/database/sqlserver/connections/connection_reset_count` GA ** _(project)_**   
Connection resets (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of logins started from the connection pool since the last restart of SQL Server service._  
`semi_managed/database/sqlserver/connections/login_attempt_count` GA ** _(project)_**   
Login attempts (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of login attempts since the last restart of SQL Server service. This does not include pooled connections._  
`semi_managed/database/sqlserver/connections/logout_count` GA ** _(project)_**   
Logouts (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of logout operations since the last restart of SQL Server service._  
`semi_managed/database/sqlserver/connections/processes_blocked` GA ** _(project)_**   
Processes blocked (Semi-managed SQL Server)   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of blocked processes._  
`semi_managed/database/sqlserver/memory/buffer_cache_hit_ratio` GA ** _(project)_**   
Buffer cache hit ratio (Semi-managed SQL Server)   
`GAUGE`, `DOUBLE`, `%`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current percentage of pages found in the buffer cache without having to read from disk. The ratio is the total number of cache hits divided by the total number of cache lookups._  
`semi_managed/database/sqlserver/memory/checkpoint_page_count` GA ** _(project)_**   
Checkpoint pages (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of pages flushed to disk by a checkpoint or other operation that requires all dirty pages to be flushed._  
`semi_managed/database/sqlserver/memory/free_list_stall_count` GA ** _(project)_**   
Free list stalls (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of requests that had to wait for a free page._  
`semi_managed/database/sqlserver/memory/lazy_write_count` GA ** _(project)_**   
Lazy writes (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of buffers written by the buffer manager's lazy writer. The lazy writer is a system process that flushes out batches of dirty, aged buffers (buffers that contain changes that must be written back to disk before the buffer can be reused for a different page) and makes them available to user processes._  
`semi_managed/database/sqlserver/memory/memory_grants_pending` GA ** _(project)_**   
Memory grants pending (Semi-managed SQL Server)   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of processes waiting for a workspace memory grant._  
`semi_managed/database/sqlserver/memory/page_life_expectancy` GA ** _(project)_**   
Page life expectancy (Semi-managed SQL Server)   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of seconds a page will stay in the buffer pool without references._  
`semi_managed/database/sqlserver/memory/page_operation_count` GA ** _(project)_**   
Page operations (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of physical database page reads or writes. This statistic counts physical page reads or writes across all databases._   
`operation`: Page operation, one of [Read, Write].   
`semi_managed/database/sqlserver/transactions/batch_request_count` GA ** _(project)_**   
Batch requests (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of Transact-SQL command batches received._  
`semi_managed/database/sqlserver/transactions/deadlock_count` GA ** _(project)_**   
Deadlocks (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of lock requests that resulted in a deadlock._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`semi_managed/database/sqlserver/transactions/full_scan_count` GA ** _(project)_**   
Full scans (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of unrestricted full scans. These can be either base-table or full-index scans._  
`semi_managed/database/sqlserver/transactions/lock_wait_count` GA ** _(project)_**   
Lock waits (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of lock requests that required the caller to wait._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`semi_managed/database/sqlserver/transactions/lock_wait_time` GA ** _(project)_**   
Lock wait time (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total time lock requests were waiting for locks._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`semi_managed/database/sqlserver/transactions/page_split_count` GA ** _(project)_**   
Page splits (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of page splits that occur as the result of overflowing index pages._  
`semi_managed/database/sqlserver/transactions/sql_compilation_count` GA ** _(project)_**   
SQL compilations (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of SQL compilations._  
`semi_managed/database/sqlserver/transactions/sql_recompilation_count` GA ** _(project)_**   
SQL recompilations (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of SQL recompilations._  
`semi_managed/database/sqlserver/transactions/transaction_count` GA ** _(project)_**   
Transactions started (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of transactions started._   
`database`: Database name, one of [tempdb, model, msdb, mssqlsystemresource, master, other].   
`database_names_hash`: Unique identifier hash of the databases that are part of the database metric field.   
`semi_managed/database/swap/pages_swapped_in_count` GA ** _(project)_**   
Pages Swapped In Count (Semi-managed)   
`CUMULATIVE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total count of pages swapped in of disk since the system was booted._  
`semi_managed/database/swap/pages_swapped_out_count` GA ** _(project)_**   
Pages Swapped Out Count (Semi-managed)   
`CUMULATIVE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total count of pages swapped out of disk since the system was booted._  
  
### cloudtasks

Metrics from [Cloud Tasks](https://docs.cloud.google.com/tasks/docs) (formerly App Engine Task Queue). **Note:** This service was previously called “App Engine Task Queue”, and some of the metrics were published with the prefix `taskqueue.googleapis.com`. Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `cloudtasks.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`api/request_count` GA ** _(project)_**   
API requests   
`DELTA`, `INT64`, `1`   
**[cloud_tasks_queue](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_tasks_queue)** |  _Count of Cloud Tasks API calls. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`api_method`: The API method called (e.g. CreateTask).   
`response_code`: Canonical response code as string (e.g. 'ok').   
`queue/depth` GA ** _(project)_**   
Queue depth   
`GAUGE`, `INT64`, `1`   
**[cloud_tasks_queue](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_tasks_queue)** |  _The number of tasks in the queue. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`queue/task_attempt_count` GA ** _(project)_**   
Task attempt count   
`DELTA`, `INT64`, `1`   
**[cloud_tasks_queue](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_tasks_queue)** |  _Count of task attempts broken down by response code. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`response_code`: Canonical response code as string (e.g. 'ok').   
`queue/task_attempt_delays` GA ** _(project)_**   
Task attempt delays   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_tasks_queue](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_tasks_queue)** |  _Delay between each scheduled attempt time and actual attempt time. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
  
### cloudtrace

Metrics from [Cloud Trace](https://docs.cloud.google.com/trace/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `cloudtrace.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`bigquery_export/exported_span_count` BETA ** _(project)_**   
Spans Exported to BigQuery   
`DELTA`, `INT64`, `1`   
**[cloudtrace.googleapis.com/CloudtraceProject](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudtrace.googleapis.com/CloudtraceProject)** |  _Counts per status of attempts to export spans to BigQuery via a TraceSink. Note that spans will be counted for each configured TraceSink that they match._   
`status`: The status of an attempt to export spans to BigQuery via a TraceSink.   
`billing/monthly_spans_ingested` GA ** _(project)_**   
Monthly trace spans ingested   
`GAUGE`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Month-to-date trace spans ingested. Sampled every 1800 seconds. After sampling, data is not visible for up to 6000 seconds._   
`service`: Google Cloud service that produced the span.   
`chargeable`: (BOOL) Whether the span is chargeable.   
`billing/spans_ingested` GA ** _(project)_**   
Trace spans ingested   
`DELTA`, `INT64`, `1`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Trace spans ingested. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`service`: Google Cloud service that produced the span.   
`chargeable`: (BOOL) Whether the span is chargeable.   
  
### composer

Metrics from [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `composer.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`environment/active_dag_processors` GA ** _(project)_**   
Active Dag Processor instances   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of active dag processor instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/active_schedulers` GA ** _(project)_**   
Active Scheduler instances   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of active scheduler instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/active_triggerers` GA ** _(project)_**   
Active Triggerers instances   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of active triggerers instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/active_webservers` GA ** _(project)_**   
Active Webserver instances   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of active webserver instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/api/request_count` GA ** _(project)_**   
API Requests   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)** |  _Number of Composer API requests seen so far. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: The status code of the API call.   
`api_version`: The version of the Composer API, e.g., v1beta1.   
`api_method`: The name of the Composer API call, e.g., CreateEnvironment.   
`environment/api/request_latencies` GA ** _(project)_**   
API Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)** |  _Distribution of Composer API call latencies. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: The status code of the API call.   
`api_version`: The version of the Composer API, e.g., v1beta1.   
`api_method`: The name of the Composer API call, e.g., CreateEnvironment.   
`environment/celery/execute_command_failure_count` GA ** _(project)_**   
Celery task non-zero exit codes   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of non-zero exit codes from Celery task (corresponds to "celery.execute_command.failure" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/celery/task_timeout_error_count` GA ** _(project)_**   
Celery task publish timeouts   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of AirflowTaskTimeout errors raised when publishing Task to Celery Broker (corresponds to "celery.task_timeout_error" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/collect_db_dag_duration` GA ** _(project)_**   
Serialized DAG fetch duration   
`GAUGE`, `DOUBLE`, `ms`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Time taken for fetching all serialized DAGs from DB (corresponds to "collect_db_dags" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/dag_callback/exception_count` GA ** _(project)_**   
DAG callback exceptions   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of exceptions raised from DAG callbacks (corresponds to "dag.callback_exceptions" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/dag_file/refresh_error_count` GA ** _(project)_**   
DAG refresh errors   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of failures loading any DAG files (corresponds to "dag_file_refresh_error" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/dag_processing/last_duration` GA ** _(project)_**   
DAG file load time   
`GAUGE`, `DOUBLE`, `ms`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Time taken to load the given DAG file (corresponds to "dag_processing.last_duration. <dag_file>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`dag_file`: DAG file name.   
`environment/dag_processing/last_run_elapsed_time` GA ** _(project)_**   
Time since DAG processing   
`GAUGE`, `DOUBLE`, `s`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Time since the DAG file was last processed (corresponds to "dag_processing.last_run.seconds_ago. <dag_file>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`dag_file`: DAG file name.   
`environment/dag_processing/manager_stall_count` GA ** _(project)_**   
DagFileProcessorManager stall count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of DagFileProcessorManager stalls (corresponds to "dag_processing.manager_stalls" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/dag_processing/parse_error_count` GA ** _(project)_**   
Parse Error Count   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of errors raised during parsing DAG files. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/dag_processing/processes` GA ** _(project)_**   
DAG parsing processes   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of currently running DAG parsing processes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/dag_processing/processor_timeout_count` GA ** _(project)_**   
Processors Timeout Count   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of file processors terminated due to processing timeout. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/dag_processing/total_parse_time` GA ** _(project)_**   
Total Parse Time   
`GAUGE`, `DOUBLE`, `s`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of seconds taken to scan and import all DAG files once. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/dagbag_size` GA ** _(project)_**   
Dag Bag Size   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _The current dag bag size. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/database/airflow/size` GA ** _(project)_**   
Airflow metadata database size   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Size of the Airflow metadata database. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/database/auto_failover_request_count` BETA ** _(project)_**   
Auto-failover request count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of instance auto-failover requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/database/available_for_failover` BETA ** _(project)_**   
Available for failover   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _True (value > 0) if Cloud SQL instance is enabled with HA and is ready for failover. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/database/cpu/reserved_cores` GA ** _(project)_**   
Database CPU reserved cores   
`GAUGE`, `DOUBLE`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of cores reserved for the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/cpu/usage_time` GA ** _(project)_**   
Database CPU usage time   
`DELTA`, `DOUBLE`, `s`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _CPU usage time of the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/cpu/utilization` GA ** _(project)_**   
Database CPU utilization   
`GAUGE`, `DOUBLE`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _CPU utilization ratio (from 0.0 to 1.0) of the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/disk/bytes_used` GA ** _(project)_**   
Database disk usage   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Used disk space in bytes on the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/disk/quota` GA ** _(project)_**   
Database disk quota   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Maximum data disk size in bytes of the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/disk/utilization` GA ** _(project)_**   
Database disk utilization   
`GAUGE`, `DOUBLE`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Disk quota usage ratio (from 0.0 to 1.0) of the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/memory/bytes_used` GA ** _(project)_**   
Database memory usage   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Memory usage of the database instance in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/memory/quota` GA ** _(project)_**   
Database memory quota   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Maximum RAM size in bytes of the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/memory/utilization` GA ** _(project)_**   
Database memory utilization   
`GAUGE`, `DOUBLE`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Memory utilization ratio (from 0.0 to 1.0) of the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/network/connections` GA ** _(project)_**   
Database connections   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of concurrent connections to the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/network/max_connections` GA ** _(project)_**   
Database connections limit   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Maximum permitted number of concurrent connections to the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/network/received_bytes_count` GA ** _(project)_**   
Database received bytes   
`DELTA`, `INT64`, `By`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of bytes received by the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database/network/sent_bytes_count` GA ** _(project)_**   
Database sent bytes   
`DELTA`, `INT64`, `By`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of bytes sent by the database instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`environment/database_health` GA ** _(project)_**   
Database Healthy   
`GAUGE`, `BOOL`, ``   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Healthiness of Composer airflow database. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment_type`: Environment type, e.g. private_ip.   
`environment/database_retention/execution_durations` GA ** _(project)_**   
Database retention operation durations   
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Distribution of database retention operation durations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/database_retention/finished_execution_count` GA ** _(project)_**   
Database retention operation executions   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of database retention operation executions. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`status`: The status of the execution. Possible values are INTERRUPTED, INCOMPLETE, SUCCEEDED, FAILED.   
`environment/database_retention/retention_gap` GA ** _(project)_**   
Database retention period gap   
`GAUGE`, `INT64`, `h`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _The time gap between the database retention period and the age of the oldest retained data that is eligible for removal and is still present in the database. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/email/sla_notification_failure_count` GA ** _(project)_**   
Failed SLA miss email notifications   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of failed SLA miss email notification attempts. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/executor/open_slots` GA ** _(project)_**   
Executor Open Slots   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of open slots on executor. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`executor`: Executor name.   
`environment/executor/queued_tasks` GA ** _(project)_**   
Executor Queued Tasks   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of queued tasks on executor. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`executor`: Executor name.   
`environment/executor/running_tasks` GA ** _(project)_**   
Executor Running Tasks   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of running tasks on executor. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`executor`: Executor name.   
`environment/finished_task_instance_count` GA ** _(project)_**   
Finished Task Instance Count   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Overall task instances in finished state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of task instance, one of [success, failed].   
`image_version`: Version of Composer image.   
`environment/health/airflow_api_check_count` GA ** _(project)_**   
Airflow api checks count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of Airflow api checks. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`request_status`: Airflow api request status, one of [OK, TIMEOUT, CONNECTION_ERROR, REQUEST_ERROR].   
`node_name`: Node name.   
`environment/health/autoscaling_check_count` GA ** _(project)_**   
Autoscaling components checks count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of autoscaling components checks. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`component`: Composer autoscaling component name, one of [airflow-worker-set-controller, custom-stackdriver-adapter, horizontal pod autoscaler].   
`status`: Autoscaling component check status, one of [OK, NotFound, FailedGetResourceMetric, FailedGetExternalMetric, MinimumReplicasUnavailable, ProgressDeadlineExceeded, FailedComputeMetricsReplicas, ScalingLimitedTooManyReplicas].   
`error`: Autoscaling component error.   
`environment/health/cmek_encryption_check_count` GA ** _(project)_**   
CMEK encryption checks count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of CMEK encryption checks. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`status`: CMEK encryption check status, one of [OK, BROKEN_KMS_KEY].   
`environment/health/container_restart_count` GA ** _(project)_**   
Container restarts count.   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of container restarts. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workload_type`: Composer workload type.   
`reason`: Container restart reason, one of [CrashLoopBackOff, ImagePullBackOff, OOMKilled, Running, NotRunning].   
`container_name`: Container name.   
`environment/health/dependency_check_count` GA ** _(project)_**   
Dependency checks count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of dependency checks. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`dependency`: Composer dependency name, one of [ARTIFACT_REGISTRY, CLOUD_LOGGING, CLOUD_MONITORING, INVERTING_PROXY].   
`status`: Dependency check status, one of [OK, CONNECTION_ERROR, TIMEOUT, REQUEST_EXCEPTION].   
`node_name`: Node name.   
`environment/health/dependency_permissions_check_count` GA ** _(project)_**   
Dependency permissions checks count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of dependency permissions checks. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`status`: Permissions check status, one of [OK, TIMEOUT, MISSING_PERMISSION, PERMISSION_DENIED].   
`permission`: IAM permission name.   
`environment/health/pod_event_count` GA ** _(project)_**   
Pod event count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of pod events. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workload_type`: Composer workload type.   
`event_type`: Pod event type, one of [Evicted, BackOff, CrashLoopBackOff, Unhealthy].   
`environment/health/redis_queue_check_count` GA ** _(project)_**   
Redis queue checks count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of redis queue checks. Sampled every 600 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`status`: Redis queue check status, one of [NO_VALUE, NO_PERMISSION, TIMEOUT, CONNECTION_ERROR,OK].   
`node_name`: Node name.   
`environment/healthy` GA ** _(project)_**   
Healthy   
`GAUGE`, `BOOL`, ``   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Healthiness of Composer environment. Sampled every 300 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/job/count` GA ** _(project)_**   
Job count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of started jobs, e.g. SchedulerJob, LocalTaskJob (corresponds to " <job_name>_start", "<job_name>_end" Airflow metrics). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`status`: Status of the Job, one of [start, end]   
`job_name`: Name of the Job.   
`environment/job/heartbeat_failure_count` GA ** _(project)_**   
Failed Job heartbeats   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of failed heartbeats for a job (corresponds to " <job_name>_heartbeat_failure" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`job_name`: Name of the Job.   
`environment/maintenance_operation` GA ** _(project)_**   
Maintenance operation   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Information whether there is a maintenance operation of a given type. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`type`: The type of the maintenance operation, one of [INFRASTRUCTURE, COMPOSER].   
`environment/num_celery_workers` GA ** _(project)_**   
Celery Workers   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of Celery workers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/operator/created_task_instance_count` GA ** _(project)_**   
Tasks created per operator   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of created task instances per operator (corresponds to "task_instance_created- <operator_name>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`operator`: Operator name, for example "BashOperator" or "PythonOperator".   
`environment/operator/finished_task_instance_count` GA ** _(project)_**   
Operator executions   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of finished task instances per operator (corresponds to "operator_successes_ <operator_name>", "operator_failures_<operator_name>" Airflow metrics). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`operator`: Operator name, for example "BashOperator" or "PythonOperator".   
`status`: Whether the operator finished successfully, one of [success, failed].   
`environment/pool/open_slots` GA ** _(project)_**   
Open slots in the pool   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of open slots in the pool. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`pool_name`: Name of the Airflow pool.   
`environment/pool/queued_slots` GA ** _(project)_**   
Queued slots in the pool   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of queued slots in the pool (corresponds to "pool.queued_slots. <pool_name>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`pool_name`: Name of the Airflow pool.   
`environment/pool/running_slots` GA ** _(project)_**   
Running slots in the pool   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of running slots in the pool. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`pool_name`: Name of the Airflow pool.   
`environment/pool/starving_tasks` GA ** _(project)_**   
Starving tasks in the pool   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of starving tasks in the pool. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`pool_name`: Name of the Airflow pool.   
`environment/scheduler/critical_section_duration` GA ** _(project)_**   
Critical section duration   
`GAUGE`, `DOUBLE`, `ms`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Time spent in the critical section of the scheduler loop - only a single scheduler can enter this loop at a time (corresponds to "scheduler.critical_section_duration" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/scheduler/critical_section_lock_failure_count` GA ** _(project)_**   
Critical section lock failures   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of times a scheduler process tried to get a lock on the critical section - in order to send tasks to the executor - and found it locked by another process (corresponds to "scheduler.critical_section_busy" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/scheduler/pod_eviction_count` GA ** _(project)_**   
Scheduler Pod Eviction Count   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _The number of Airflow scheduler pod evictions. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/scheduler/task/externally_killed_count` GA ** _(project)_**   
Externally killed tasks   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of tasks killed externally (corresponds to "scheduler.tasks.killed_externally" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/scheduler/task/orphan_count` GA ** _(project)_**   
Orphaned task count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of cleared/adopted orphaned tasks (corresponds to "scheduler.orphaned_tasks.cleared", "scheduler.orphaned_tasks.adopted" Airflow metrics). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`status`: Status of the orphaned task, one of [cleared, adopted].   
`environment/scheduler/tasks` GA ** _(project)_**   
Scheduler managed tasks   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of tasks managed by scheduler (corresponds to "scheduler.tasks.running", "scheduler.tasks.starving", "scheduler.tasks.executable" Airflow metrics). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`status`: Status of the task, one of [running, starving, executable]   
`environment/scheduler_heartbeat_count` GA ** _(project)_**   
Scheduler Heartbeats   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Scheduler heartbeats. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/sla_callback_notification_failure_count` GA ** _(project)_**   
Failed SLA callback notifications   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of failed SLA miss callback notification attempts (corresponds to "sla_callback_notification_failure" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/smart_sensor/exception_failures` DEPRECATED ** _(project)_**   
Smart sensor poking exception failures   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of failures caused by exception in the previous smart sensor poking loop. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/smart_sensor/infra_failures` DEPRECATED ** _(project)_**   
Smart sensor poking infrastructure failures   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of infrastructure failures in the previous smart sensor poking loop. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/smart_sensor/poked_exception` DEPRECATED ** _(project)_**   
Smart sensor poking exceptions   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of exceptions in the previous smart sensor poking loop. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/smart_sensor/poked_success` DEPRECATED ** _(project)_**   
Smart sensor successfully poked tasks   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of newly succeeded tasks poked by the smart sensor in the previous poking loop. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/smart_sensor/poked_tasks` DEPRECATED ** _(project)_**   
Smart sensor poked tasks   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of tasks poked by the smart sensor in the previous poking loop. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/snapshot/creation_count` GA ** _(project)_**   
Snapshot creation count   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of created scheduled snapshots. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`result`: Snapshot creation result, one of [SUCCEEDED, FAILED].   
`environment/snapshot/creation_elapsed_time` GA ** _(project)_**   
Snapshot creation elapsed time   
`GAUGE`, `DOUBLE`, `s`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Time elapsed of the last scheduled snapshot creation. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/snapshot/size` GA ** _(project)_**   
Snapshot size   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Size of last scheduled snapshot in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/task_instance/previously_succeeded_count` GA ** _(project)_**   
Previously succeeded task instances   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of times a task instance was already in SUCCESS state before execution (corresponds to "previously_succeeded" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/task_queue_length` GA ** _(project)_**   
Task Queue Length   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of tasks in queue. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`queue_name`: Name of task queue.   
`environment/trigger/blocking_count` GA ** _(project)_**   
Blocking triggers   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of triggers that blocked the main thread of a triggerer. Sampled every 60 seconds._   
`image_version`: Version of Composer image.   
`environment/trigger/failed_count` GA ** _(project)_**   
Failed triggers   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of triggers that failed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/trigger/succeeded_count` GA ** _(project)_**   
Succeeded triggers   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Total number of triggers that succeeded. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/unfinished_task_instances` GA ** _(project)_**   
Unfinished Task Instances   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Overall task instances in not finished state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of task instance, one of [queued, running, scheduled, deferred].   
`image_version`: Version of Composer image.   
`environment/web_server/cpu/reserved_cores` DEPRECATED ** _(project)_**   
Web server CPU reserved cores   
`GAUGE`, `DOUBLE`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of cores reserved for the web server instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`instance_id`: Numeric ID of the Compute Engine instance running the web server.   
`environment/web_server/cpu/usage_time` DEPRECATED ** _(project)_**   
Web server CPU usage time   
`DELTA`, `DOUBLE`, `s`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _CPU usage time of the web server instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`instance_id`: Numeric ID of the Compute Engine instance running the web server.   
`environment/web_server/health` GA ** _(project)_**   
Web server health   
`GAUGE`, `BOOL`, ``   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Healthiness of Airflow web server. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/web_server/memory/bytes_used` DEPRECATED ** _(project)_**   
Web server memory usage   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Memory usage of the web server instance in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`instance_id`: Name of the Compute Engine instance running the web server.   
`environment/web_server/memory/quota` DEPRECATED ** _(project)_**   
Web server memory quota   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Maximum RAM size in bytes of the web server instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`image_version`: Version of Composer image.   
`instance_id`: Name of the Compute Engine instance running the web server.   
`environment/worker/max_workers` GA ** _(project)_**   
Maximum Airflow workers   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Maximum number of Airflow workers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/worker/min_workers` GA ** _(project)_**   
Minimum Airflow workers   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Minimum number of Airflow workers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/worker/pod_eviction_count` GA ** _(project)_**   
Worker Pod Eviction Count   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _The number of Airflow worker pods evictions. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/worker/scale_factor_target` GA ** _(project)_**   
Workers scale factor target   
`GAUGE`, `DOUBLE`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Scale factor for Airflow workers count. Sampled every 30 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`queue_name`: Name of the Airflow queue. See https://airflow.apache.org/docs/stable/concepts.html#queues.   
`environment/workloads_cpu_quota` GA ** _(project)_**   
Workloads CPU quota   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _CPU quota limit for Composer workloads. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/workloads_cpu_quota_usage` GA ** _(project)_**   
Workloads CPU quota usage   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _CPU quota usage for Composer workloads. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`environment/zombie_task_killed_count` GA ** _(project)_**   
Zombie Tasks Killed   
`DELTA`, `INT64`, `1`   
**[cloud_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_environment)**   
**[internal_composer_environment](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_environment)** |  _Number of zombie tasks killed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workflow/dag/run_duration` GA ** _(project)_**   
DAG run duration   
`GAUGE`, `DOUBLE`, `ms`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Time taken for a DAG run to reach terminal state (corresponds to "dagrun.duration.success. <dag_id>", "dagrun.duration.failed.<dag_id>" Airflow metrics). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`status`: DAG run status, one of [success, failed].   
`workflow/dependency_check_duration` GA ** _(project)_**   
DAG dependency check duration   
`GAUGE`, `DOUBLE`, `ms`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Time taken to check DAG dependencies (corresponds to "dagrun.dependency-check. <dag_id>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workflow/run_count` GA ** _(project)_**   
Workflow Runs   
`DELTA`, `INT64`, `1`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Number of workflow runs completed so far. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of workflow run, one of [success, shutdown, skipped, failed, running].   
`image_version`: Version of Composer image.   
`workflow/run_duration` GA ** _(project)_**   
Workflow Run Duration   
`GAUGE`, `DOUBLE`, `s`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Duration of workflow run completion. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of workflow run, one of [success, shutdown, skipped, failed].   
`image_version`: Version of Composer image.   
`workflow/schedule_delay` GA ** _(project)_**   
DAG run schedule delay   
`GAUGE`, `DOUBLE`, `ms`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Delay between the scheduled DagRun start date and the actual DagRun start date (corresponds to "dagrun.schedule_delay. <dag_id>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workflow/task/cpu_usage` GA ** _(project)_**   
Task CPU usage   
`GAUGE`, `DOUBLE`, `%`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Percentage of CPU used by a task (corresponds to "task.cpu_usage. <dag_id>.<task_id>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`task_id`: ID of the task.   
`workflow/task/log_file_size` GA ** _(project)_**   
Workflow Task Log Size   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Size of log file generated by workflow task in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of task, one of [success, shutdown, skipped, failed].   
`image_version`: Version of Composer image.   
`task_name`: Name of task.   
`operator`: Operator of task.   
`workflow/task/mem_usage` GA ** _(project)_**   
Task memory usage   
`GAUGE`, `DOUBLE`, `%`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Percentage of memory used by a task (corresponds to "task.mem_usage. <dag_id>.<task_id>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`task_id`: ID of the task.   
`workflow/task/removed_from_dag_count` GA ** _(project)_**   
Tasks removed from DAG   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Total number of tasks removed for a given DAG, i.e. task no longer exists in DAG (corresponds to "task_removed_from_dag. <dag_id>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workflow/task/restored_to_dag_count` GA ** _(project)_**   
Tasks restored to DAG   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Total number of tasks restored for a given DAG, i.e. task instance which was previously in REMOVED state in the DB is added to DAG file (corresponds to "task_restored_to_dag. <dag_id>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workflow/task/run_count` GA ** _(project)_**   
Tasks   
`DELTA`, `INT64`, `1`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Number of workflow tasks completed so far. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of task, one of [success, shutdown, skipped, failed].   
`image_version`: Version of Composer image.   
`queue`: The queue used by a task.   
`task_name`: Name of task.   
`operator`: Operator of task.   
`workflow/task/run_duration` GA ** _(project)_**   
Task Duration   
`GAUGE`, `DOUBLE`, `s`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Duration of task completion. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: State of task, one of [success, shutdown, skipped, failed].   
`image_version`: Version of Composer image.   
`task_name`: Name of task.   
`operator`: Operator of task.   
`workflow/task/schedule_delay` GA ** _(project)_**   
Task schedule delay   
`GAUGE`, `DOUBLE`, `ms`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Time elapsed between the first task start_date and DagRun expected start (corresponds to "dagrun. <dag_id>.first_task_scheduling_delay" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workflow/task_instance/finished_count` GA ** _(project)_**   
Completed task instances   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Total number of finished task instances (corresponds to "ti.finish. <dag_id>.<task_id>.<state>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`task_id`: ID of the task.   
`status`: Task instance status, such as "skipped" or "success".   
`workflow/task_instance/queued_duration` GA ** _(project)_**   
Task instance queued duration   
`GAUGE`, `DOUBLE`, `ms`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Time taken in queued state (corresponds to "dag. <dag_id>.<task_id>.queued_duration" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`task_id`: ID of the task.   
`workflow/task_instance/run_duration` GA ** _(project)_**   
Task instance run duration   
`GAUGE`, `DOUBLE`, `ms`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Time taken to finish a task (corresponds to "dag. <dag_id>.<task_id>.duration" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`task_id`: ID of the task.   
`workflow/task_instance/started_count` GA ** _(project)_**   
Started tasks   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Total number of tasks started in a given DAG (corresponds to "ti.start. <dag_id>.<task_id>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`task_id`: ID of the task.   
`workflow/task_runner/terminated_count` GA ** _(project)_**   
Task runner termination count   
`DELTA`, `INT64`, `1`   
**[cloud_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workflow)**   
**[internal_composer_workflow](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workflow)** |  _Number of workflow tasks where the task runner got terminated with a return code. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`task_id`: ID of the task.   
`return_code`: Signed return code of the process, one of [-9 (SIGKILL), -16 (SIGTERM), 0, 1].   
`workload/cpu/reserved_cores` GA ** _(project)_**   
Workload CPU reserved cores   
`GAUGE`, `DOUBLE`, `1`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Number of cores reserved for the workload instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workload/cpu/usage_time` GA ** _(project)_**   
Workload CPU usage time   
`DELTA`, `DOUBLE`, `s`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _CPU usage time of the workload instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workload/dags_sync_duration` GA ** _(project)_**   
DAGs sync duration   
`GAUGE`, `INT64`, `s`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _DAGs directory sync duration in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`initial_sync`: (BOOL) Whether the sync is an initial or a periodic one.   
`workload/disk/bytes_used` GA ** _(project)_**   
Workload disk usage   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Used disk space in bytes on the workload instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workload/disk/quota` GA ** _(project)_**   
Workload disk quota   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Maximum data disk size in bytes of the workload instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workload/log_entry_count` GA ** _(project)_**   
Log entries   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Total number of log occurrences with a specified severity level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`severity`: Severity of log entry, one of [ERROR, WARNING, INFO].   
`workload/memory/bytes_used` GA ** _(project)_**   
Workload memory usage   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Memory usage of the workload instance in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workload/memory/quota` GA ** _(project)_**   
Workload memory quota   
`GAUGE`, `INT64`, `By`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Maximum RAM size in bytes of the workload instance. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workload/plugins_sync_duration` GA ** _(project)_**   
Plugins sync duration   
`GAUGE`, `INT64`, `s`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Plugins directory sync duration in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`initial_sync`: (BOOL) Whether the sync is an initial or a periodic one.   
`workload/restart_count` GA ** _(project)_**   
Workload restarts count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Total number of workload restarts. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`type`: Type of workload restart, one of [PROCESS, CONTAINER, POD].   
`workload/scheduler/loop_duration` BETA ** _(project)_**   
Scheduler loop duration   
`GAUGE`, `DOUBLE`, `ms`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Time spent running one scheduler loop (corresponds to "scheduler.scheduler_loop_duration. <hostname>" Airflow metric). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`hostname`: The hostname of the scheduler instance (e.g., "airflow-scheduler-0" or "airflow-scheduler-1").   
`workload/trigger/num_running` GA ** _(project)_**   
Running triggers   
`GAUGE`, `INT64`, `1`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Number of running triggers in a triggerer. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
`workload/uptime` GA ** _(project)_**   
Workload uptime in seconds   
`GAUGE`, `INT64`, `s`   
**[cloud_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_composer_workload)**   
**[internal_composer_workload](https://docs.cloud.google.com/monitoring/api/resources#tag_internal_composer_workload)** |  _Time since workload created. Metric is supported only for Redis workload. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`image_version`: Version of Composer image.   
  
### compute

Metrics from [Compute Engine](https://docs.cloud.google.com/compute/docs). These metrics do not require installation of the Monitoring or Logging agent, but to collect the `compute.googleapis.com/guest` metrics, you must enable the [Container-Optimized OS Health Monitoring](https://docs.cloud.google.com/container-optimized-os/docs/how-to/monitoring) feature; for more information, see [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs).**Note:** To monitor the availability of a service, [create an uptime check](https://docs.cloud.google.com/monitoring/uptime-checks). These checks create `monitoring.googleapis.com/uptime_check/check_passed` metric data. Do not monitor the `instance/uptime` or `instance/uptime_total` metric types. Launch stages of these metrics: ALPHA BETA GA

The "metric type" strings in this table must be prefixed with `compute.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`capacity/slices` BETA ** _(project)_**   
Capacity State   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/AcceleratorSlice](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/AcceleratorSlice)** |  _The state of capacity per topology of an accelerator slice. The value indicates the count of topologies in that state at a given instant in time._   
`accelerator_type`: Accelerator type and generation.   
`topology`: Accelerator network topology.   
`state`: The state of the capacity.   
`cluster_id`: The cluster where the slice is located.   
`parent_slice_id`: The ID of the parent slice.   
`reservation_id`: The ID of the reservation.   
`block_id`: The block ID of the slice.   
`subblock_id`: The subblock ID of the slice.   
`disk/async_replication/async_replication_state` GA ** _(project)_**   
Async replication state   
`GAUGE`, `INT64`, `1`   
**[gce_disk](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_disk)** |  _Async replication disk pair's state. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`async_replication_state`: State of the async replication pair.   
`secondary_disk_id`: The ID of the secondary disk.   
`secondary_location`: The zone or region where the secondary disk resides.   
`secondary_project_number`: Project number to which the secondary disk belongs.   
`disk/async_replication/replication_network_compression_ratio` GA ** _(project)_**   
Async replication network compression ratio   
`GAUGE`, `DOUBLE`, `1`   
**[gce_disk](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_disk)** |  _Ratio of bytes transferred over the network to the bytes written to the disk. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`secondary_disk_id`: The ID of the secondary disk.   
`secondary_location`: The zone or region where the secondary disk resides.   
`secondary_project_number`: Project number to which the secondary disk belongs.   
`disk/async_replication/sent_bytes_count` GA ** _(project)_**   
Async replication sent bytes count   
`DELTA`, `INT64`, `By`   
**[gce_disk](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_disk)** |  _Delta count of bytes sent through the cross-region network. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`secondary_disk_id`: The ID of the secondary disk.   
`secondary_location`: The zone or region where the secondary disk resides.   
`secondary_project_number`: Project number to which the secondary disk belongs.   
`disk/async_replication/time_since_last_replication` GA ** _(project)_**   
Async replication time since last replication   
`GAUGE`, `INT64`, `s`   
**[gce_disk](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_disk)** |  _Seconds since the last replication was done. Also known as recovery point objective (RPO). Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`secondary_disk_id`: The ID of the secondary disk.   
`secondary_location`: The zone or region where the secondary disk resides.   
`secondary_project_number`: Project number to which the secondary disk belongs.   
`disk/regional/replica_state` GA ** _(project)_**   
Regional disk replica state   
`GAUGE`, `INT64`, `1`   
**[gce_disk](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_disk)** |  _Regional disk's replica state. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`state`: Disk replica state, one of [Synced, CatchingUp, OutOfSync].   
`replica_zone`: The zone where the disk replica is located.   
`storage_type`: Storage type, one of [pd-standard, PD-Balanced, pd-ssd, PD-Extreme, Hyperdisk-Extreme, Hyperdisk-Throughput].   
`firewall/dropped_bytes_count` GA ** _(project)_**   
Dropped bytes   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of incoming bytes dropped by the firewall. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`firewall/dropped_packets_count` GA ** _(project)_**   
Dropped packets   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of incoming packets dropped by the firewall. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`global_concurrent_operations` ALPHA ** _(project)_**   
Concurrent global operations per project   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/OperationType](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/OperationType)** |  _Concurrent quota for global operations._  
`global_dns/request_count` GA ** _(project)_**   
GCE Project Global DNS Request Count   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _The number of global internal DNS requests in a GCE project. After sampling, data is not visible for up to 1020 seconds._   
`zonal_dns_readiness`: Classification of request as ready or risky for migration to zonal DNS.   
`guest/cpu/load_15m` ALPHA ** _(project)_**   
CPU load average (15m)   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _CPU Load (15 minute intervals). For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`guest/cpu/load_1m` ALPHA ** _(project)_**   
CPU load average (1m)   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _CPU Load (1 minute intervals). For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`guest/cpu/load_5m` ALPHA ** _(project)_**   
CPU load average (5m)   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _CPU Load (5 minute intervals). For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`guest/cpu/runnable_task_count` BETA ** _(project)_**   
Runnable task count.   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The average number of runnable tasks in the run-queue. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`guest/cpu/usage_time` BETA ** _(project)_**   
CPU usage   
`CUMULATIVE`, `DOUBLE`, `s{CPU}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _CPU usage, in seconds. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`state`: One of the following: idle, interrupt, nice, softirq, steal, system, user, wait.   
`guest/disk/bytes_used` BETA ** _(project)_**   
Disk usage   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of bytes used on disk for file systems. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`mountoption`: Mount options on the disk device.   
`mount_option`: Mount options on the disk device.   
`device_name`: The name of the disk device.   
`state`: Type of usage (free, used, reserved)   
`fstype`: File system type of the disk device.   
`fs_type`: File system type of the disk device.   
`guest/disk/io_time` GA ** _(project)_**   
IO Time   
`CUMULATIVE`, `INT64`, `ms`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The cumulative time spent on the I/O operations that are in progress; that is, the actual time in queue and when disks were busy. Requests issued in parallel are counted as a single one. For Container-Optimized OS, or Ubuntu running GKE. Sampled every 60 seconds._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`guest/disk/merged_operation_count` BETA ** _(project)_**   
Merged disk operations   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Merged disk operations count. Disk operations which are adjacent to each other may be merged by the kernel for efficiency. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`direction`: Direction (read, write).   
`guest/disk/operation_bytes_count` BETA ** _(project)_**   
Disk bytes transferred   
`CUMULATIVE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Bytes transferred in disk operations. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`direction`: Direction (read, write).   
`guest/disk/operation_count` BETA ** _(project)_**   
Disk operations   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Disk operations count. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`direction`: Direction (read, write).   
`guest/disk/operation_time` BETA ** _(project)_**   
Disk operation time   
`CUMULATIVE`, `INT64`, `ms`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Amount of time spent on the disk operations, by direction. This metric only includes time spent on completed operations. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`direction`: Direction (read, write).   
`guest/disk/percent_used` BETA ** _(project)_**   
Percent Used   
`GAUGE`, `DOUBLE`, `percent`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Percentage of total disk capacity currently in use._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`guest/disk/queue_length` GA ** _(project)_**   
Queue Length   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The queue length on the disk averaged over the last 60 seconds. For Container-Optimized OS, or Ubuntu running GKE. Sampled every 60 seconds._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`guest/disk/weighted_io_time` GA ** _(project)_**   
IO Time   
`CUMULATIVE`, `INT64`, `ms`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The cumulative weighted IO time spent on the disk. For Container-Optimized OS, or Ubuntu running GKE. Sampled every 60 seconds._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`guest/memory/anonymous_used` BETA ** _(project)_**   
Anonymous memory usage in Bytes   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Anonymous memory usage, in Bytes. Summing values of all states yields the total anonymous memory used. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`state`: One of the following: active, inactive. Active means the memory has been used more recently.   
`guest/memory/bytes_used` BETA ** _(project)_**   
Memory usage in Bytes   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Memory usage by each memory state, in Bytes. Summing values of all states yields the total memory on the machine. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`state`: One of the following: buffered, cached, free, slab, used. Buffered consists of temporary storage for raw disk blocks. Cached consists of the pagecache and tmpfs usage. Free consists of total free memory. Slab consists of memory used for caching in-kernel data structures. Used is calculated by subtracting the values for the other states from the total available memory.   
`guest/memory/dirty_used` BETA ** _(project)_**   
Dirty pages usage in Bytes.   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Dirty pages usage, in Bytes. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`state`: One of the following: dirty, writeback. Dirty means the memory is waiting to be written back to disk, and writeback means the memory is actively being written back to disk.   
`guest/memory/page_cache_used` BETA ** _(project)_**   
Page cache memory usage in Bytes   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Page cache memory usage, in Bytes. Summing values of all states yields the total anonymous memory used. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`state`: One of the following: active, inactive. Active means the memory has been used more recently and usually not reclaimed until needed.   
`guest/memory/percent_used` BETA ** _(project)_**   
Percent Used   
`GAUGE`, `DOUBLE`, `percent`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Percentage of total system memory actively in use. Calculated as (Total Memory - Free Memory - Buffers - Cached - Slab) / Total Memory * 100._   
`instance_name`: The name of the VM instance.   
`state`: One of the following: used.   
`guest/memory/unevictable_used` BETA ** _(project)_**   
Unevictable memory usage in Bytes   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Unevictable memory usage, in Bytes. For Container-Optimized OS, or Ubuntu running GKE._   
`instance_name`: The name of the VM instance.   
`guest/memory/zswap/bytes_used` GA ** _(project)_**   
Zswap Bytes Used   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Zswap usage in bytes. Sampled every 60 seconds._   
`instance_name`: The name of the VM instance.   
`guest/memory/zswap/compression_efficiency` GA ** _(project)_**   
Zswap Compression Efficiency   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Zswap compression efficiency ratio. Sampled every 60 seconds._   
`instance_name`: The name of the VM instance.   
`guest/system/os_feature_enabled` BETA ** _(project)_**   
OS Feature   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _OS Features like GPU support, KTD kernel, third party modules as unknown modules. 1 if the feature is enabled and 0, if disabled. For Container-Optimized OS, or Ubuntu running GKE. Sampled every 60 seconds._   
`instance_name`: The name of the VM instance.   
`value`: Value for the features of the guest os system if present.   
`os_feature`: Features of the guest OS system.   
`guest/system/problem_count` GA ** _(project)_**   
Problem Count   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of times a machine problem has happened. For Container-Optimized OS, or Ubuntu running GKE. Sampled every 60 seconds._   
`instance_name`: The name of the VM instance.   
`reason`: Description of the type of the problem.   
`guest/system/problem_state` GA ** _(project)_**   
Problem State   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Whether a problem is affecting the system or not. The problem is affecting the system when set to 1 and is not affecting the system when set to 0. For Container-Optimized OS, or Ubuntu running GKE. Sampled every 60 seconds._   
`instance_name`: The name of the VM instance.   
`reason`: Description of the cause of the problem.   
`type`: Description of the type of the problem.   
`guest/system/uptime` GA ** _(project)_**   
Uptime   
`GAUGE`, `INT64`, `s`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of seconds that the operating system has been running for. For Container-Optimized OS, or Ubuntu running GKE. Sampled every 60 seconds._   
`instance_name`: The name of the VM instance.   
`kernel_version`: The version of the operating system kernel.   
`os_version`: The version of the operating system.   
`instance/clock_accuracy/ptp_kvm/nanosecond_accuracy` GA ** _(project)_**   
Clock Accuracy   
`GAUGE`, `INT64`, `ns`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Accuracy of the host clock in nanoseconds. Sampled every 60 seconds._   
`instance_name`: The name of the VM instance.   
`instance/cpu/guest_visible_vcpus` BETA ** _(project)_**   
Guest Visible vCPUs   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of vCPUs visible inside the guest. For many GCE machine types, the number of vCPUs visible inside the guest is equal to the `compute.googleapis.com/instance/cpu/reserved_cores` metric. For shared-core machine types, the number of guest-visible vCPUs differs from the number of resereved cores. For example, e2-small instances have two vCPUs visible inside the guest and 0.5 fractional vCPUs reserved. Therefore, for an e2-small instance, `compute.googleapis.com/instance/cpu/guest_visible_vcpus` has a value of 2 and `compute.googleapis.com/instance/cpu/reserved_cores` has a value of 0.5. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`instance/cpu/reserved_cores` GA ** _(project)_**   
Reserved vCPUs   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of vCPUs reserved on the host of the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`instance/cpu/scheduler_wait_time` GA ** _(project)_**   
Scheduler Wait Time   
`DELTA`, `DOUBLE`, `s{idle}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Wait time is the time a vCPU is ready to run, but unexpectedly not scheduled to run. The wait time returned here is the accumulated value for all vCPUs. The time interval for which the value was measured is returned by Monitoring in whole seconds as start_time and end_time. This metric is only available for VMs that belong to the e2 family or to overcommitted VMs on sole-tenant nodes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`instance/cpu/usage_time` GA ** _(project)_**   
CPU usage   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Delta vCPU usage for all vCPUs, in vCPU-seconds. To compute the per-vCPU utilization fraction, divide this value by (end-start)*N, where end and start define this value's time interval and N is `compute.googleapis.com/instance/cpu/reserved_cores` at the end of the interval. This value is reported by the hypervisor for the VM and can differ from `agent.googleapis.com/cpu/usage_time`, which is reported from inside the VM. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`instance/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Fractional utilization of allocated CPU on this instance. Values are typically numbers between 0.0 and 1.0 (but some machine types allow bursting above 1.0). Charts display the values as a percentage between 0% and 100% (or more). This metric is reported by the hypervisor for the VM and can differ from `agent.googleapis.com/cpu/utilization`, which is reported from inside the VM. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`instance/disk/average_io_latency` GA ** _(project)_**   
Disk average latency   
`GAUGE`, `DOUBLE`, `us`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Disk's average io latency in the last 60s. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, hyperdisk-extreme, hyperdisk-throughput].   
`instance/disk/average_io_queue_depth` GA ** _(project)_**   
Disk average io queue depth   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Disk's average io queue depth in the last 60s. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, hyperdisk-extreme, hyperdisk-throughput].   
`instance/disk/max_read_bytes_count` GA ** _(project)_**   
Peak disk read bytes   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Disk's maximum per-second read throughput over a period of time specified by the user. The period must be one minute or longer. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, PD-Balanced, pd-ssd, PD-Extreme, Hyperdisk-Extreme, Hyperdisk-Throughput].   
`device_type`: Disk type, one of [ephemeral, permanent].   
`instance/disk/max_read_ops_count` GA ** _(project)_**   
Peak disk read ops   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Disk's maximum per-second read requests count over a period of time specified by the user. The period must be one minute or longer. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-ssd, PD-Balanced, PD-Extreme, Hyperdisk-Extreme, Hyperdisk-Throughput].   
`device_type`: Disk type, one of [ephemeral, permanent].   
`instance/disk/max_write_bytes_count` GA ** _(project)_**   
Peak disk write bytes   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Disk's maximum per-second write throughput over a period of time specified by the user. The period must be one minute or longer. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, PD-Balanced, pd-ssd, PD-Extreme, Hyperdisk-Extreme, Hyperdisk-Throughput].   
`device_type`: Disk type, one of [ephemeral, permanent].   
`instance/disk/max_write_ops_count` GA ** _(project)_**   
Peak disk write ops   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Disk's maximum per-second write requests count over a period of time specified by the user. The period must be one minute or longer. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, PD-Balanced, pd-ssd, PD-Extreme, Hyperdisk-Extreme, Hyperdisk-Throughput].   
`device_type`: Disk type, one of [ephemeral, permanent].   
`instance/disk/performance_status` GA ** _(project)_**   
Disk performance status   
`GAUGE`, `BOOL`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Whether the disk performance is normal or could potentially be impacted by an issue within Compute Engine during the period of time specified by the user. The period must be one minute or longer. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, hyperdisk-extreme, hyperdisk-throughput, hyperdisk-balanced].   
`performance_status`: One of ["Healthy", "Degraded" or "Severely Degraded"].   
`instance/disk/provisioning/iops` GA ** _(project)_**   
Provisioned disk IOPS   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Disk's provisioned IOPS specified by the user. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, hyperdisk-balanced, hyperdisk-extreme, hyperdisk-throughput].   
`instance/disk/provisioning/size` GA ** _(project)_**   
Provisioned disk size   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Disk's provisioned size specified by the user. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, hyperdisk-balanced, hyperdisk-extreme, hyperdisk-throughput].   
`instance/disk/provisioning/throughput` GA ** _(project)_**   
Provisioned disk throughput (bytes/sec)   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Disk's provisioned throughput (bytes/sec) specified by the user. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, hyperdisk-balanced, hyperdisk-extreme, hyperdisk-throughput].   
`instance/disk/read_bytes_count` GA ** _(project)_**   
Disk read bytes   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of bytes read from disk. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, local-ssd, hyperdisk-extreme, hyperdisk-throughput].   
`device_type`: Disk type, one of [ephemeral, permanent].   
`instance/disk/read_ops_count` GA ** _(project)_**   
Disk read operations   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of disk read IO operations. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, local-ssd, hyperdisk-extreme, hyperdisk-throughput].   
`device_type`: Disk type, one of [ephemeral, permanent].   
`instance/disk/write_bytes_count` GA ** _(project)_**   
Disk write bytes   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of bytes written to disk. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, local-ssd, hyperdisk-extreme, hyperdisk-throughput].   
`device_type`: Disk type, one of [ephemeral, permanent].   
`instance/disk/write_ops_count` GA ** _(project)_**   
Disk write operations   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of disk write IO operations. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`device_name`: The name of the disk device.   
`storage_type`: Storage type, one of [pd-standard, pd-balanced, pd-ssd, pd-extreme, local-ssd, hyperdisk-extreme, hyperdisk-throughput].   
`device_type`: Disk type, one of [ephemeral, permanent].   
`instance/gpu/accumulated_context_utilization_seconds` BETA ** _(project)_**   
Accumulated Context Utilization Seconds   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Accumulated context utilization time (in seconds)._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/cache_correctable_ecc_error_count` BETA ** _(project)_**   
Correctable Cache ECC Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of correctable ECC errors in cache memory._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/cache_uncorrectable_ecc_error_count` BETA ** _(project)_**   
Uncorrectable Cache ECC Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of uncorrectable ECC errors in cache memory._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/dram_correctable_ecc_error_count` BETA ** _(project)_**   
Correctable DRAM ECC Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of correctable ECC errors in GPU DRAMs._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/dram_correctable_row_remapping_count` BETA ** _(project)_**   
Correctable DRAM Row Remapping Count   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of row remappings from correctable errors in GPU DRAMs._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/dram_row_remapping_failed` BETA ** _(project)_**   
DRAM Row Remapping Failed   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Whether row remapping failed previously. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`Value`: Whether row remapping failed previously. Possible values are "true" and "false".   
`instance/gpu/dram_row_remapping_pending` BETA ** _(project)_**   
DRAM Row Remapping Pending   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Whether row remapping is set to occur at the next GPU reset. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`Value`: Whether row remapping is set to occur at the next GPU reset. Possible values are "true" and "false".   
`instance/gpu/dram_uncorrectable_ecc_error_count` BETA ** _(project)_**   
Uncorrectable DRAM ECC Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of uncorrectable ECC errors in GPU DRAMs._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/dram_uncorrectable_row_remapping_count` BETA ** _(project)_**   
Uncorrectable DRAM Row Remapping Count   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of row remappings from uncorrectable errors in GPU DRAMs._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/failure_prediction_status` BETA ** _(project)_**   
VM Degradation Status   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric indicates the probability of a VM entering a degraded state within the next 5 hours as predicted by our proprietary algorithm. Value label for this metric would be NO_DEGRADATION_PREDICTED, DEGRADATION_PREDICTED, POSSIBLE_DEGRADATION_PREDICTED. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`Value`: The status of a VM entering a degraded state within the next 5 hours as predicted by our proprietary algorithm. Possible values are "NO_DEGRADATION_PREDICTED", "DEGRADATION_PREDICTED", "POSSIBLE_DEGRADATION_PREDICTED".   
`instance/gpu/fe_nic_fec_ccw_count` BETA ** _(project)_**   
FE NIC FEC Correctable Errors   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total count of correctable forward error correction code words across all instance front end NICs in a 1-minute window._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`nic_id`: The ID of the network interface card.   
`interface_name`: Name of the network interface.   
`instance/gpu/fe_nic_fec_ucw_count` BETA ** _(project)_**   
FE NIC FEC Uncorrectable Errors   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total count of uncorrectable forward error correction code words across all instance front end NICs in a 1-minute window._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`nic_id`: The ID of the network interface card.   
`interface_name`: Name of the network interface.   
`instance/gpu/fe_nic_link_status` BETA ** _(project)_**   
FE NIC Link Status   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The link operational status across instance frontend (FE) NICs, reported per NIC per interface where 1 indicates link UP and 0 indicates link DOWN._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`nic_id`: The ID of the network interface card.   
`interface_name`: Name of the network interface.   
`instance/gpu/gpu_nvlink_active_speed` BETA ** _(project)_**   
GPU NVLink Port Active Speed   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current NVLink port speed in Gbps. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`port_nvlink_status`: The LinkStatus of the NVLink port.   
`instance/gpu/gpu_nvlink_effective_ber` BETA ** _(project)_**   
GPU NVLink Effective BER   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Effective bit error rate (BER) is the error rate of the port after a forward error correction (FEC). The value indicates the overall average BER since the last counter reset. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`instance/gpu/gpu_nvlink_link_downed_counter` BETA ** _(project)_**   
GPU NVLink Port Link Downed Counter   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of link-down events on the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`instance/gpu/gpu_nvlink_link_error_recovery_count` BETA ** _(project)_**   
GPU NVLink Port Link Error Recovery Counter   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of successful link recovery processes. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`instance/gpu/gpu_nvlink_physical_effective_errors` BETA ** _(project)_**   
GPU NVLink Port Physical Effective Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Effective error count is the number of bit errors that the port receives post-Forward Error Correction (FEC). Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`instance/gpu/gpu_nvlink_port_rcv_data` BETA ** _(project)_**   
GPU NVLink Port Rcv Data   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of bytes received, measured as bps. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`instance/gpu/gpu_nvlink_port_rcv_errors` BETA ** _(project)_**   
GPU NVLink Port RCV Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of packets containing an error that were received on the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`instance/gpu/gpu_nvlink_port_xmit_data` BETA ** _(project)_**   
GPU NVLink Port Xmit Data   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of bytes transmitted, measured as bps. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`instance/gpu/gpu_nvlink_port_xmit_discards` BETA ** _(project)_**   
GPU NVLink Port Xmit Discards   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of outbound packets that were discarded by the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`instance/gpu/gpu_nvlink_port_xmit_wait` BETA ** _(project)_**   
GPU NVLink Port Xmit Wait   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of transmitted packets incurred transmit wait. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`instance/gpu/gpu_nvlink_vl15_dropped` BETA ** _(project)_**   
GPU NVLink Port VL15 Dropped   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of management (VL15) packets that were dropped due to a lack of resources on the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The model of GPUs that are attached to the VM.   
`gpu_id`: A single-digit value (such as GPU_0 or GPU_1) that represents the GPU's index within a machine with multiple GPUs attached. This number may not be consistent across reboots. To reference a specific GPU, we recommend that you instead use a GPU’s universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`gpu_nvlink_port_id`: The NVLink Port name on the GPU.   
`instance/gpu/infra_health` BETA ** _(project)_**   
VM Infra Health   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric captures the infrastructure health of the VM as a string. This metric is available for all GPU VM machine types starting with A3 mega, A3 edge, A3 high and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`unhealthy_category`: Explanation for the unhealthy VM status. This label is populated only when the value of the metric is `Unhealthy`.   
`Value`: The health status of the VM. Possible values are `Healthy`, `Unhealthy`, or `Unknown`. See the `unhealthy_category` label for details if unhealthy.   
`instance/gpu/inter_block_tx` BETA ** _(project)_**   
Network Traffic at Inter-Block   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric represents network traffic at the inter-block level as an INT64 value, calculated as the delta of observed traffic within a one-minute interval. This metric is available for GPU VM machine types starting with A3 mega and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/inter_subblock_tx` BETA ** _(project)_**   
Network Traffic at Inter-Subblock   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric represents network traffic at the inter-subblock level as an INT64 value, calculated as the delta of observed traffic within a one-minute interval. This metric is available for GPU VM machine types starting with A3 mega and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/intra_subblock_tx` BETA ** _(project)_**   
Network Traffic at Intra-Subblock   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric represents network traffic at the intra-subblock level as an INT64 value, calculated as the delta of observed traffic within a one-minute interval. This metric is available for GPU VM machine types starting with A3 mega and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/link_carrier_changes` BETA ** _(project)_**   
Link Carrier Changes   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric captures the network link carrier change as delta value computed at 1 minute granularity. This metric is available for all GPU VM machine types starting with A3 mega, A3 ultra, A4 and all future GPU VM families._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`nic_type`: The NIC type. (Frontend or Backend)   
`nic_id`: The ID of the network interface card.   
`interface_name`: Name of the network interface.   
`instance/gpu/nccl/latency_tx` BETA ** _(project)_**   
NCCL Send Latency   
`CUMULATIVE`, `DISTRIBUTION`, `nanoseconds`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The metric measures the latency distribution of NCCL send operations._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The reservation ID.   
`instance/gpu/nccl/latency_variance` BETA ** _(project)_**   
NCCL Send Latency Variance   
`CUMULATIVE`, `DISTRIBUTION`, `nanoseconds`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The metric measures the latency variance distribution of NCCL send operations._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The reservation ID.   
`instance/gpu/nccl/message_size_tx` BETA ** _(project)_**   
NCCL Send Message Size   
`CUMULATIVE`, `DISTRIBUTION`, `bytes`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The metric measures the message size distribution of NCCL send operations._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The reservation ID.   
`instance/gpu/nccl_hang` BETA ** _(project)_**   
NCCL Hang Issues   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of NCCL (NVIDIA Collective Communication Library) hang (or crash) issues detected on this VM instance. A value greater than 0 indicates a detected issue._   
`hang_reason`: A string value denoting the suspected reason for the NCCL hang or crash. Possible values: MissingHeartbeatIssue (process or node may have crashed), StalledRankIssue (GPU ranks not progressing as expected), NoHangIssue (No Hang Issue detected).   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`reservation_id`: The reservation ID.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`instance/gpu/network_cc_rate` BETA ** _(project)_**   
Network CC Rate   
`CUMULATIVE`, `DISTRIBUTION`, `bps`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric measures the distribution of the transmission rates set by RTTCC on the network interfaces in your GPU VMs. This metric is available for GPU VM machine types starting with A3 Ultra, A4, and all future GPU VM families._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/network_rtt` BETA ** _(project)_**   
Network RTT   
`CUMULATIVE`, `DISTRIBUTION`, `microseconds`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric measures network round-trip time in your GPU VMs. This metric is available for GPU VM machine types starting with A3 mega, A3 ultra, A4 and all future GPU VM families._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/nvlink_active_speed` BETA ** _(project)_**   
NVLink Active Speed   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current access link port speed in Gb/s. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`width`: Infiniband NVLink width.   
`instance/gpu/nvlink_port_state` BETA ** _(project)_**   
NVLink Port State   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Logical and Physical port states for NVswitch ports as defined in the OpenConfig YANG model. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`physical_port_state`: Physical state of the port as defined in the OpenConfig YANG model.   
`logical_port_state`: Logical state of the port as defined in the OpenConfig YANG model.   
`instance/gpu/nvlink_runtime_error` BETA ** _(project)_**   
NVLink Runtime Error   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Whether an NVLink Runtime Error occurred. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`Value`: Whether an NVLink Runtime Error occurred. Possible values are "true" and "false".   
`instance/gpu/nvswitch_effective_ber` BETA ** _(project)_**   
NVSwitch Effective BER   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Effective BER (Bit Error Rate) is the error rate of the port after FEC (Forward Error Correction). The value indicates the overall average BER since the last counter reset. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_effective_errors` BETA ** _(project)_**   
NVSwitch Effective Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Effective error count is the number of bit errors that the port receives after FEC (Forward Error Correction). Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_link_downed_counter` BETA ** _(project)_**   
NVSwitch Link Downed Counter   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The count of link-down events on the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_link_error_recovery_counter` BETA ** _(project)_**   
NVSwitch Link Error Recovery Counter   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The count of successful link recovery processes on the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_port_rcv_data` BETA ** _(project)_**   
NVSwitch Port Rcv Data   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of bytes received, measured as bps. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_port_rcv_errors` BETA ** _(project)_**   
NVSwitch Port Rcv Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of packets containing an error that were received on the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_port_xmit_constraint_errors` BETA ** _(project)_**   
NVSwitch Port Xmit Constraint Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of packets not transmitted from the switch physical port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_port_xmit_data` BETA ** _(project)_**   
NVSwitch Port Xmit Data   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of bytes transmitted, measured as bps. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_port_xmit_discards` BETA ** _(project)_**   
NVSwitch Port Xmit Discards   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of outbound packets that were discarded by the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_port_xmit_wait` BETA ** _(project)_**   
NVSwitch Port Xmit Wait   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of transmitted packets incurred transmit wait. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_status` BETA ** _(project)_**   
NV Switch Status   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric represents the health of an individual NV Switch on the host as a string. If a machine has multiple NV Switches attached, the metric provides each NV Switch health status on the host. The possible values for this metric are provided by NVIDIA BMC. This metric is available for all GPU VM machine types starting with A3 mega, A3 edge, A3 high and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`nvswitch_id`: (INT64) The ID of the NV Switches used on the host.   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`Value`: The status of the NV Switch as a string. The possible values are `OK`, `Warning`, or `Critical`.   
`instance/gpu/nvswitch_symbol_errors` BETA ** _(project)_**   
NVSwitch Symbol Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Symbol error count is the number of bit errors that the port receives after FEC (Forward Error Correction) and PLR (Physical Layer Retransmission). Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_vl15_dropped` BETA ** _(project)_**   
NVSwitch VL15 Dropped   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of management (VL15) packets that were dropped due to a lack of resources on the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/nvswitch_zero_hist` BETA ** _(project)_**   
NVSwitch Zero Histogram FEC   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _First FEC histogram bin with value of 0. Monitor max of bits errors in the FEC block occurred up to the time of measurement. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/packet_retransmission_count` BETA ** _(project)_**   
TCPXO Total Packet Retransmission Count   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric, representing the packet retransmission count observed by network interface cards (NICs) attached to GPUs on the host, is a single INT64 value per timestamp. This metric is available for GPU VM machine types starting with A3 mega. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/packets_sent_count` BETA ** _(project)_**   
Packets Sent Count   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total number of packets sent for a specific GPU NIC port in a 1-minute window._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`pf_bdf`: The PCI address of the NIC.   
`port_number`: (INT64) The port number of the NIC.   
`instance/gpu/pcie_correctable_error_count` BETA ** _(project)_**   
Correctable PCIe Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of correctable PCIe errors._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/pcie_fatal_error_count` BETA ** _(project)_**   
Fatal PCIe Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of fatal PCIe errors._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/pcie_l0_to_recovery_count` BETA ** _(project)_**   
PCIe L0 To Recovery Count   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of times the PCIe link entered the recovery state from the L0 state._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/pcie_nak_received_count` BETA ** _(project)_**   
PCIe NAK Received Count   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of NAKs the host root complex issued on the PCIe link._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/pcie_nak_sent_count` BETA ** _(project)_**   
PCIe NAK Sent Count   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of NAKs the GPU issued on the PCIe link._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/pcie_non_fatal_error_count` BETA ** _(project)_**   
Non Fatal PCIe Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of non-fatal PCIe errors._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/pcie_replay_count` BETA ** _(project)_**   
PCIe Replays   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of replays the GPU issued on the PCIe link._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/pcie_replay_rollover_count` BETA ** _(project)_**   
PCIe Replay Rollovers   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of replay rollovers the GPU issued on the PCIe link._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`gpu_model`: The GPU type attached to the VM.   
`gpu_id`: The number of GPUs that matches the CUDA device index. This number may not be consistent across reboots. To reference a specific GPU, we recommend using the universally unique identifier (UUID) label.   
`gpu_uuid`: The UUID of your GPU.   
`instance/gpu/port_excessive_buffer_overrun` BETA ** _(project)_**   
NVLink Port Excessive Buffer Overrun   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of excessive buffer overruns on the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/port_local_link_integrity_errors` BETA ** _(project)_**   
NVLink Port Local Link Integrity Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of local link integrity errors on the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/port_plr_bw_loss_percent` BETA ** _(project)_**   
NVLink Port PLR Bandwidth Loss Percent   
`GAUGE`, `DOUBLE`, `%`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Bandwidth loss percentage of the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/port_plr_rcv_uncorrectable_code` BETA ** _(project)_**   
NVLink Port PLR RCV Uncorrectable Code   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of received uncorrectable codes on the port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/port_plr_xmit_codes` BETA ** _(project)_**   
NVLink Port PLR Xmit Codes   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of transmitted PLR codewords. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/port_rcv_constraints_errors` BETA ** _(project)_**   
NVLink Port RCV Constraints Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of packets dropped on receive due to partition mismatch. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/port_rcv_remote_physical_errors` BETA ** _(project)_**   
NVLink Port RCV Remote Physical Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of packets received with remote physical error indications. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/port_rcv_switch_relay_errors` BETA ** _(project)_**   
NVLink Port RCV Switch Relay Errors   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of received packets dropped due to switch relay errors. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`instance/gpu/power_consumption` BETA ** _(project)_**   
GPU Power Consumption   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric represents power consumption observed on individual GPUs on the host as a double value. If a machine has multiple GPUs attached, the metric provides each GPU power consumption on the host. This metric is available for all GPU VM machine types starting with A3 mega, A3 edge, A3 high and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`gpu_id`: (INT64) The ID of the GPU running on the host.   
`gpu_uuid`: The UUID of the GPU.   
`gpu_model`: The model name of the GPU.   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/raw_bit_error_rate_per_channel` BETA ** _(project)_**   
NVLink Port Raw Bit Error Rate Per Channel   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Raw bit error rate per channel on the access link port. Supported for A4X VMs only._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated NVLink domain name hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`nvswitch_id`: The obfuscated NVSwitch ID to which machine is connected to.   
`nvswitch_port_id`: The access link port_id on the nvswitch to which machine is connected to.   
`channel_num`: A single digit [1-8] representing the channel number on the access link port.   
`instance/gpu/retransmit_packet_count` BETA ** _(project)_**   
Per GPU NIC Retransmit Packet Count   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _For ConnectX (Cx) NIC based VMs. The number of adaptively retransmitted packets for a specific GPU NIC port in a 1-minute window._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`pf_bdf`: The PCI address of the NIC.   
`port_number`: (INT64) The port number of the NIC.   
`instance/gpu/retransmit_percentage` BETA ** _(project)_**   
GPU NIC Retransmit Percentage   
`GAUGE`, `DOUBLE`, `%`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The percentage of packets retransmitted by the GPU NIC. This is calculated as the ratio of adaptive retransmits to total RDMA unicast packets sent, multiplied by 100. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`pf_bdf`: The PCI address of the NIC.   
`port_number`: (INT64) The port number of the NIC.   
`instance/gpu/sm_utilization` BETA ** _(project)_**   
SM Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric represents the Streaming Multiprocessor (SM) utilization of an individual GPU on the host as a percentage value. if a machine has multiple GPUs attached, the metric provides each GPU SM utilization on the host. This metric is available for all GPU VM machine types starting with A3 mega, A3 edge, A3 high and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`gpu_id`: (INT64) The ID of the GPU running on the host.   
`gpu_uuid`: The UUID of the GPU.   
`gpu_model`: The model name of the GPU.   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/straggler_status` BETA ** _(project)_**   
Straggler Status   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Indicates whether an instance is identified as a straggler. This metric is supported for the A3 Mega, A3 Ultra, and A4 machine types. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`Value`: The reporting value for the metric. Possible values are "true" and "false".   
`instance/gpu/tcpxo_receive_chunk_latency` BETA ** _(project)_**   
TCPXO Receive Chunk Latency   
`CUMULATIVE`, `DISTRIBUTION`, `nanoseconds`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The metric measures TCPXO received chunk latency in VM. This metric is available only for A3 mega VMs._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/tcpxo_send_chunk_latency` BETA ** _(project)_**   
TCPXO Send Chunk Latency   
`CUMULATIVE`, `DISTRIBUTION`, `nanoseconds`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The metric measures TCPXO send chunk latency in VM. This metric is available only for A3 mega VMs._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/temperature` BETA ** _(project)_**   
GPU Temperature   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric represents the temperature of an individual GPU on the host, as a double value. If a machine has multiple GPUs attached, the metric provides each GPU temperature on the host. This metric is available for all GPU VM machine types starting with A3 mega, A3 edge, A3 high and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`gpu_id`: (INT64) The ID of the GPU running on the host.   
`gpu_uuid`: The UUID of the GPU.   
`gpu_model`: The model name of the GPU.   
`units`: The unit of measurement of the GPU's temperature.   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/throughput_rx_bytes` BETA ** _(project)_**   
Throughput Rx Bytes   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric represents network throughput as an INT64 value, calculated as the delta of received bytes at a one-minute interval. This metric is available for GPU VM machine types starting with A3 mega and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/throughput_tx_bytes` BETA ** _(project)_**   
Throughput Tx Bytes   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric represents network throughput as an INT64 value, calculated as the delta of transferred bytes at a one-minute interval. This metric is available for GPU VM machine types starting with A3 mega and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/gpu/tlimit` BETA ** _(project)_**   
GPU Thermal Margin   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Represents the thermal margin of an individual GPU on the host. This metric represents the temperature in C from a software slowdown event for an individual GPU on the host as a double value. For an `n-GPU` machine, each timestamp we will have `n` values representing the thermal margin of each GPU on the host. This metric is available for all GPU VM machine types starting with A3 mega, A3 edge, A3 high and all future GPU VM families. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`gpu_id`: (INT64) The ID of the GPU running on the host.   
`gpu_uuid`: The UUID of the GPU.   
`gpu_model`: The model name of the GPU.   
`units`: The unit of measurement of the GPU's temperature.   
`cluster_id`: The ID of the cluster hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`machine_id`: The ID of the physical machine hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`instance/integrity/early_boot_validation_status` GA ** _(project)_**   
Early Boot Validation   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The validation status of early boot integrity policy. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`status`: One of "passed", "failed", or "unknown".   
`instance/integrity/late_boot_validation_status` GA ** _(project)_**   
Late Boot Validation   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The validation status of late boot integrity policy. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`status`: One of "passed", "failed", or "unknown".   
`instance/interruption_count` GA ** _(project)_**   
Interruption Count   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Interruptions are system evictions of infrastructure while the customer is in control of that infrastructure. This metric is the current count of interruptions by type and reason. The stream is often undefined when the count is zero. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`instance_name`: The name of the VM instance.   
`interruption_type`: The top-level interruption type.   
`interruption_reason`: The reason for the interruption.   
`instance/memory/balloon/ram_size` GA ** _(project)_**   
VM Memory Total   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total amount of memory in the VM. This metric is only available for VMs that belong to the e2 family. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`instance/memory/balloon/ram_used` GA ** _(project)_**   
VM Memory Used   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Memory currently used in the VM. This metric is only available for VMs that belong to the e2 family. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`instance/memory/balloon/swap_in_bytes_count` GA ** _(project)_**   
VM Swap In   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The amount of memory read into the guest from its own swap space. This metric is only available for VMs that belong to the e2 family. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`instance/memory/balloon/swap_out_bytes_count` GA ** _(project)_**   
VM Swap Out   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The amount of memory written from the guest to its own swap space. This metric is only available for VMs that belong to the e2 family. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`instance/network/received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of bytes received from the network. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`loadbalanced`: (BOOL) Whether traffic was received by an L3 loadbalanced IP address assigned to the VM. Traffic that is externally routed to the VM's standard internal or external IP address, such as L7 loadbalanced traffic, is not considered to be loadbalanced in this metric.   
`instance/network/received_packets_count` GA ** _(project)_**   
Received packets   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of packets received from the network. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`loadbalanced`: (BOOL) Whether traffic was received by an L3 loadbalanced IP address assigned to the VM. Traffic that is externally routed to the VM's standard internal or external IP address, such as L7 loadbalanced traffic, is not considered to be loadbalanced in this metric.   
`instance/network/sent_bytes_count` GA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of bytes sent over the network. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`loadbalanced`: (BOOL) Whether traffic was sent from an L3 loadbalanced IP address assigned to the VM. Traffic that is externally routed from the VM's standard internal or external IP address, such as L7 loadbalanced traffic, is not considered to be loadbalanced in this metric.   
`instance/network/sent_packets_count` GA ** _(project)_**   
Sent packets   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of packets sent over the network. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`loadbalanced`: (BOOL) Whether traffic was sent from an L3 loadbalanced IP address assigned to the VM. Traffic that is externally routed from the VM's standard internal or external IP address, such as L7 loadbalanced traffic, is not considered to be loadbalanced in this metric.   
`instance/tpu/accelerator/core_temperature` BETA ** _(project)_**   
Core Temperature   
`GAUGE`, `DOUBLE`, `Cel`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Core Temperature of the TPU._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/accelerator/core_throttling_indicator` BETA ** _(project)_**   
Core Throttling Indicator   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of clock cycles skipped per second over the total clock cycles per TPU core._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`reason`: Top reason for core throttling, for example: thermal_throttle_clocks_skipped.   
`instance/tpu/accelerator/duty_cycle` BETA ** _(project)_**   
Accelerator Duty Cycle   
`GAUGE`, `DOUBLE`, `%`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Percentage of time over the sample period during which the accelerator was actively processing. Values are in the range of [0,100]._   
`accelerator_id`: Device Id of Accelerator.   
`instance/tpu/accelerator/hbm_power_draw` BETA ** _(project)_**   
HBM Power Draw   
`GAUGE`, `DOUBLE`, `W`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Sum of power on the HBM module in watts (W)._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/accelerator/hbm_temperature` BETA ** _(project)_**   
HBM Temperature   
`GAUGE`, `DOUBLE`, `Cel`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _High Bandwidth Memory (HBM) Temperature of the TPU._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`hbm_id`: High Bandwidth Memory (HBM) module identifier. Usually has only top value, for example: hbm_0.   
`instance/tpu/accelerator/hbm_uncorrectable_count` BETA ** _(project)_**   
HBM Uncorrectable Count   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of uncorrectable errors at HBM (fatal)._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/accelerator/memory_bandwidth_utilization` BETA ** _(project)_**   
Accelerator Memory Bandwidth Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current percentage of the accelerator memory bandwidth that is being used. Computed by dividing the memory bandwidth used over a sample period by the maximum supported bandwidth over the same sample period._   
`accelerator_id`: Device Id of Accelerator.   
`instance/tpu/accelerator/memory_total` BETA ** _(project)_**   
Accelerator Memory Total   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total accelerator memory currently allocated in bytes._   
`accelerator_id`: Device Id of Accelerator.   
`instance/tpu/accelerator/memory_used` BETA ** _(project)_**   
Accelerator Memory Used   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total accelerator memory currently used in bytes._   
`accelerator_id`: Device Id of Accelerator.   
`instance/tpu/accelerator/mxu_temperature` BETA ** _(project)_**   
MXU Temperature   
`GAUGE`, `DOUBLE`, `Cel`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Matrix Multiply Unit (MXU) Temperature of the TPU._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`die_id`: Slot index for the accelerator. Usually has only top value, for example: die_0.   
`instance/tpu/accelerator/network/ici_link_flaps` BETA ** _(project)_**   
ICI Link Flaps   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Frequency of state changes between up and down states on an ICI link._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/accelerator/network/ici_link_health` BETA ** _(project)_**   
ICI Link Health   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _A numerical indicator (0–10) representing ICI link health. Higher values indicate increasing levels of link instability—from minor, temporary flapping (1–5) to persistent degraded performance (6–9). A value of 10 represents a fatal link failure that automatically evicts active workloads._   
`port_id`: Port Id.   
`instance/tpu/accelerator/network/ici_packets_received_count` BETA ** _(project)_**   
ICI Packets Received Count   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of packets received by the TPU accelerator over its Inter-Chip Interconnect (ICI) links._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/accelerator/network/ici_packets_sent_count` BETA ** _(project)_**   
ICI Packets Sent Count   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of packets transmitted by the TPU accelerator over its Inter-Chip Interconnect (ICI) links._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/accelerator/pcie_fatal_error_count` BETA ** _(project)_**   
PCIe Fatal Error Count   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of fatal PCIe errors occurring at PCIe interface._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/accelerator/pcie_nonfatal_error_count` BETA ** _(project)_**   
PCIe Nonfatal Error Count   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of non-fatal PCIe errors occurring at PCIe interface._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/accelerator/power_draw` BETA ** _(project)_**   
Power Draw   
`GAUGE`, `DOUBLE`, `W`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Accelerator power draw measured in watts (W)._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/accelerator/tensorcore_utilization` BETA ** _(project)_**   
Accelerator TensorCore Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current percentage of the Tensorcore that is utilized. Computed by dividing the Tensorcore operations that were performed over a sample period by the supported number of Tensorcore operations over the same sample period._   
`accelerator_id`: Device Id of Accelerator.   
`instance/tpu/accelerator/tray_power` BETA ** _(project)_**   
Tray Power   
`GAUGE`, `DOUBLE`, `W`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total power drawn at the TPU tray._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/accelerator/tray_temperature` BETA ** _(project)_**   
Tray Temperature   
`GAUGE`, `DOUBLE`, `Cel`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Tray Temperature of the TPU._   
`accelerator_id`: The device ID of the accelerator. Valid values are 0, 1, 2, 3.   
`instance/tpu/active_chips` GA ** _(project)_**   
Active TPU Chips Count   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current count of chips that are actively being utilized (i.e) not idle._   
`accelerator_type`: Accelerator type and generation.   
`reservation_id`: The ID of the physical machine reservation.   
`provisioning_model`: The associated provisioning model.   
`protection_tier`: The associated protection model.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`is_exr`: (BOOL) Indicates if the chip is part of an extended reservation.   
`instance/tpu/chip_state` BETA ** _(project)_**   
TPU Chip State Count   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The count of TPU chips in various states like Healthy, Unhealthy and Unknown._   
`state`: The state of the chip.   
`accelerator_type`: Accelerator type and generation.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`is_exr`: (BOOL) Indicates if the chip is part of an extended reservation.   
`instance/tpu/failure_prediction_score` BETA ** _(project)_**   
TPU Degradation Score   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric indicates the probability of a TPU machine entering an unhealthy state._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`model_id`: The model ID.   
`prediction_window`: The prediction window.   
`instance/tpu/failure_prediction_status` BETA ** _(project)_**   
TPU Degradation Status   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _This metric indicates the probability of a TPU machine entering a degraded state within the next 5 hours as predicted by our proprietary algorithm. The value label for this metric is NO_DEGRADATION_PREDICTED, DEGRADATION_PREDICTED, POSSIBLE_DEGRADATION_PREDICTED. Sampled every 60 seconds. After sampling, data is not visible for up to 540 seconds._   
`cluster_id`: The obfuscated cluster ID of the cluster hosting the VM.   
`block_id`: The obfuscated block ID within the cluster hosting the VM.   
`subblock_id`: The obfuscated sub-block ID hosting the VM.   
`machine_id`: The obfuscated machine name hosting the VM.   
`reservation_id`: The reservation ID.   
`Value`: The status of a TPU machine entering a degraded state within the next 5 hours as predicted by our proprietary algorithm. Possible values are "NO_DEGRADATION_PREDICTED", "DEGRADATION_PREDICTED", "POSSIBLE_DEGRADATION_PREDICTED".   
`instance/tpu/infra_health` BETA ** _(project)_**   
TPU Instance Health   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Indicates the overall health status of a TPU instance. The metric labels help identify the specific health status and reasons for issues on degraded or unhealthy TPU instances, primarily focusing on TPU hardware and system health. Health status changes may take several minutes to be reflected in this metric. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`health_status`: The overall health state of the TPU instance. Possible values: HEALTHY (operating as expected), UNHEALTHY (critical issue detected), DEGRADED (performance impacting issue), UNKNOWN (status cannot be determined).   
`unhealthy_category`: Explanation for the unhealthy VM status. This label is populated only when the value of the metric is Unhealthy.   
`machine_type`: The machine type of the instance (e.g., ct6e-standard-4t-tpu).   
`machine_id`: The ID of the physical machine hosting the VM.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`cluster_id`: The ID of the cluster hosting the VM.   
`reservation_id`: The ID of the physical machine reservation.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`instance/tpu/runtime/uptime` BETA ** _(project)_**   
Runtime Uptime   
`GAUGE`, `INT64`, `s`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Uptime of the ML Runtime since the initialization of the runtime library (libtpu.so) by the ML job. During this period the runtime library blocks the TPU devices for use by the ML job._   
`ml_framework_name`: Name of the ML framework.   
`ml_framework_version`: Version of the ML framework.   
`instance/tpu/scheduled_chips` GA ** _(project)_**   
Scheduled TPU Chips Count   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current count of chips that are allocated to a VM which is HEALTHY and is NOT DISABLED for maintenance._   
`accelerator_type`: Accelerator type and generation.   
`reservation_id`: The ID of the physical machine reservation.   
`provisioning_model`: The associated provisioning model.   
`protection_tier`: The associated protection model.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`is_exr`: (BOOL) Indicates if the chip is part of an extended reservation.   
`instance/tpu/utilized_chips` BETA ** _(project)_**   
Utilized TPU Chips   
`GAUGE`, `DOUBLE`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The current aggregate utilized capacity expressed as an effective number of active chips. It is equivalent to the sum of the fractional utilization (0.0 to 1.0) of all active chips._   
`accelerator_type`: Accelerator type and generation.   
`reservation_id`: The ID of the physical machine reservation.   
`provisioning_model`: The associated provisioning model.   
`protection_tier`: The associated protection model.   
`block_id`: The ID of the block within the cluster hosting the VM.   
`subblock_id`: The ID of the sub-block hosting the VM.   
`is_exr`: (BOOL) Indicates if the chip is part of an extended reservation.   
`instance/uptime` GA ** _(project)_**   
Uptime   
`DELTA`, `DOUBLE`, `s{uptime}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Delta of how long the VM has been running, in seconds. Note: to get the total number of seconds since VM start, use compute.googleapis.com/instance/uptime_total. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`instance_name`: The name of the VM instance.   
`instance/uptime_total` GA ** _(project)_**   
Uptime Total   
`GAUGE`, `INT64`, `s`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Elapsed time since the VM was started, in seconds. After sampling, data is not visible for up to 120 seconds. When VM is Stopped (https://cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm-google-cloud), the time is not calculated. On starting the VM again, the timer will reset to 0 for that VM. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`instance_name`: The name of the VM instance.   
`instance_group/predicted_capacity` GA ** _(project)_**   
Instance group capacity as predicted   
`GAUGE`, `DOUBLE`, `1`   
**[instance_group](https://docs.cloud.google.com/monitoring/api/resources#tag_instance_group)** |  _Estimated capacity that the instance group will have if predictive autoscaling is enabled. Currently available only for autoscaled instance groups and equal to the predicted number of serving VMs multiplied by utilization target. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`metric_type`: Metric for which utilization target is used, e.g., cpu.   
`instance_group/predicted_size` GA ** _(project)_**   
Instance group size as predicted   
`GAUGE`, `INT64`, `1`   
**[instance_group](https://docs.cloud.google.com/monitoring/api/resources#tag_instance_group)** |  _Estimated number of VMs that the instance group will have if predictive autoscaling is enabled. Currently available only for autoscaled instance groups. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`metric_type`: Metric for which utilization target is used, e.g., cpu.   
`instance_group/predicted_utilization` GA ** _(project)_**   
Instance group utilization as predicted   
`GAUGE`, `DOUBLE`, `1`   
**[instance_group](https://docs.cloud.google.com/monitoring/api/resources#tag_instance_group)** |  _The sum of the estimated values of the scaling metric for all serving VMs if predictive autoscaling is enabled. Currently available only for autoscaled instance groups. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`metric_type`: Metric for which utilization is predicted, e.g., cpu.   
`instance_group/size` GA ** _(project)_**   
Instance group size   
`GAUGE`, `INT64`, `1`   
**[instance_group](https://docs.cloud.google.com/monitoring/api/resources#tag_instance_group)** |  _The number of VMs in the instance group. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`inter_region_egress_bandwidth` GA ** _(project)_**   
Inter-Region Network Egress Bandwidth (bps) from Compute instances   
`DELTA`, `INT64`, `Mbit`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Inter-Region Network Egress Bandwidth (bps) from Compute instances. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`remote_location`: Cloud Region.   
`intercept/intercepted_bytes_count` BETA ** _(project)_**   
Intercepted bytes   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of intercepted bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`ip_protocol`: The ip protocol of the intercepted bytes, one of [IPv4, IPv6].   
`intercept/intercepted_packets_count` BETA ** _(project)_**   
Intercepted packets   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The number of intercepted packets. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`ip_protocol`: The ip protocol of the intercepted packets, one of [IPv4, IPv6].   
`machine/machine_status` BETA ** _(project)_**   
Machine Status   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Machine)** |  _This metric captures the machine health status and utilization status of a GCE Machine._   
`subblock_id`: ID of the subblock that the machine belongs to.   
`block_id`: ID of the block that the machine belongs to.   
`reservation_id`: ID of the reservation that the machine belongs to.   
`cluster_id`: The ID of the cluster where the machine is located.   
`machine_health`: The health status of the machine.   
`machine_utilization`: The utilization state of the machine.   
`unhealthy_category`: Explanation for the unhealthy machine status. This label is populated only when the value of the machine_health is `UNHEALTHY`.   
`mirroring/dropped_packets_count` GA ** _(project)_**   
Dropped packets   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of dropped mirrored packets. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`reason`: The reason for the packet drop.   
`mirroring/mirrored_bytes_count` GA ** _(project)_**   
Mirrored bytes   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of mirrored bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`ip_protocol`: The ip protocol of the mirrored bytes, one of [IPv4, IPv6].   
`mirroring/mirrored_packets_count` GA ** _(project)_**   
Mirrored packets   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of mirrored packets. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`ip_protocol`: The ip protocol of the mirrored packets, one of [IPv4, IPv6].   
`mrdma_nic/alerts` BETA ** _(project)_**   
Alerts   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _ASAPd-lite daemon alerts. Sampled every 60 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`reason`: Reason for the alert.   
`mrdma_nic/asapd_lite_uptime` BETA ** _(project)_**   
Asapd-lite Daemon Uptime   
`CUMULATIVE`, `INT64`, `s`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _Uptime of the Asapd-lite Daemon. Sampled every 60 seconds._  
`mrdma_nic/build_label` BETA ** _(project)_**   
Build Label   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _Build label of the running Asapd-lite Daemon in the format of doca_ <doca_version>_commit_<commit_hash>. Sampled every 300 seconds._   
`build_label`: Build label of the running Asapd-lite Daemon.   
`mrdma_nic/doca_telemetry_counters` BETA ** _(project)_**   
DOCA Telemetry Counters   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _Counters from DOCA telemetry library. Sampled every 60 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`metric_name`: Name of the metric.   
`mrdma_nic/doca_telemetry_statistics` BETA ** _(project)_**   
DOCA Telemetry Histograms   
`CUMULATIVE`, `DISTRIBUTION`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _Histograms from DOCA telemetry library. Sampled every 60 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`metric_name`: Name of the metric.   
`mrdma_nic/ethtool_counters` BETA ** _(project)_**   
Ethtool Counters   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _Driver specific counters from ethtool CLI. Sampled every 60 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`metric_name`: Name of the metric.   
`interface_name`: Name of the network interface.   
`mrdma_nic/ethtool_link_settings` BETA ** _(project)_**   
Ethtool Link Settings   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _CX NIC Ethtool Link Settings. Sampled every 60 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`interface_name`: Name of the network interface.   
`metric_name`: Name of the metric.   
`mrdma_nic/linkup` BETA ** _(project)_**   
Link in Up State   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _Count of MRDMA NICs with the given address in the up state. Sampled every 60 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`mrdma_nic/nic_configs` BETA ** _(project)_**   
NIC Configuration   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _CX NIC configuration. Sampled every 300 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`config_name`: Name of the configuration.   
`config_value`: Value of the configuration.   
`mrdma_nic/nic_states` BETA ** _(project)_**   
NIC States   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _CX NIC State. Sampled every 60 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`state_name`: Name of the state.   
`state_value`: Value of the state.   
`mrdma_nic/rttcc_counters` BETA ** _(project)_**   
RTTCC Counters   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _Counters for congestion control. Sampled every 60 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`metric_name`: Name of the metric.   
`mrdma_nic/rttcc_statistics` BETA ** _(project)_**   
RTTCC Histograms   
`CUMULATIVE`, `DISTRIBUTION`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _Histograms for Congestion Control. Sampled every 60 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`metric_name`: Name of the metric.   
`mrdma_nic/sysfs_counters` BETA ** _(project)_**   
Sysfs Counters   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/MrdmaNic](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/MrdmaNic)** |  _Counters from sysfs files, including infiniband counters and debugfs counters. Sampled every 60 seconds._   
`pci_address`: PCI address of the NIC in the format of domain:bus:device.function.   
`metric_name`: Name of the metric.   
`nat/allocated_ports` GA ** _(project)_**   
Allocated ports   
`GAUGE`, `INT64`, `{port}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of ports allocated to a VM by the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`nat_ip`: The NAT IP allocated to the NAT gateway.   
`nat/closed_connections_count` GA ** _(project)_**   
Closed connections count   
`DELTA`, `INT64`, `{connection}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of connections closed over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/dropped_received_packets_count` GA ** _(project)_**   
Received packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of received packets dropped by the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/dropped_sent_packets_count` GA ** _(project)_**   
Sent packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of sent packets dropped by the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`reason`: The reason for the packet drop. Possible values are OUT_OF_RESOURCES, ENDPOINT_INDEPENDENCE_CONFLICT.   
`nat/new_connections_count` GA ** _(project)_**   
New connections count   
`DELTA`, `INT64`, `{connection}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of new connections created over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/open_connections` GA ** _(project)_**   
Open connections   
`GAUGE`, `INT64`, `{connection}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of connections currently open on the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/port_usage` GA ** _(project)_**   
Port usage   
`GAUGE`, `INT64`, `{port}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Maximum number of connections from a VM to a single internet endpoint (IP:port). Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/received_bytes_count` GA ** _(project)_**   
Received bytes count   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of bytes received (destination - > VM) via the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/received_packets_count` GA ** _(project)_**   
Received packets count   
`DELTA`, `INT64`, `{packet}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of packets received (destination - > VM) via the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/sent_bytes_count` GA ** _(project)_**   
Sent bytes count   
`DELTA`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of bytes sent (VM - > destination) over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`nat/sent_packets_count` GA ** _(project)_**   
Sent packets count   
`DELTA`, `INT64`, `{packet}`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Count of packets sent (VM - > destination) over the NAT gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`nat_project_number`: The project number to which the NAT gateway belongs.   
`router_id`: The Cloud Router ID to which the NAT gateway belongs.   
`nat_gateway_name`: The name of the NAT gateway.   
`ip_protocol`: The protocol of the connection. Can be TCP, UDP or ICMP.   
`network/dropped_packets/no_vm_receive_buffers_count` GA ** _(project)_**   
No VM Receive Buffers Drop Count   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of packets dropped due to the VM not posting buffers fast enough to receive incoming packets from the host switch. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`network_switch/baseline_capacity_kbps` BETA ** _(project)_**   
Baseline Capacity   
`GAUGE`, `INT64`, `kbit/s`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The total potential capacity of a ToR's connection to the superblock._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`network_switch/boot_time_in_ns` BETA ** _(project)_**   
Boot Time   
`GAUGE`, `INT64`, `ns`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The boot time of the network switch in nanoseconds._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`network_switch/cpu_utilization` BETA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The CPU utilization of the network switch._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`network_switch/ecn_marked_packets_count` BETA ** _(project)_**   
ECN Marked Packets   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of ECN marked packets._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`network_switch/effective_capacity_kbps` BETA ** _(project)_**   
Effective Capacity   
`GAUGE`, `INT64`, `kbit/s`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The most realistic view of usable capacity of a ToR's connection to the superblock._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`network_switch/egress_max_queue_depth` BETA ** _(project)_**   
Egress Max Queue Depth   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The maximum queue depth during the most recent measurement cycle._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`queue_name`: The name of the queue.   
`network_switch/egress_queue_drops_count` BETA ** _(project)_**   
Egress Queue Drops   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of egress queue drops._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`queue_name`: The name of the queue.   
`network_switch/fec_word_error_count` BETA ** _(project)_**   
FEC Word Errors   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of FEC word errors._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`correctable`: (BOOL) Whether the error is correctable.   
`network_switch/in_buffer_discards` BETA ** _(project)_**   
In Buffer Discards   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of packets dropped at the ingress due to running out of the ingress buffer._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`peer_target_identifier`: The identifier of the peer machine or switch.   
`peer_port_identifier`: Index of NIC on the peer machine, or logical name of the port on the peer switch.   
`network_switch/in_bytes_count` BETA ** _(project)_**   
Incoming Bytes Count   
`CUMULATIVE`, `INT64`, `By`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The total number of incoming bytes received on the port._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`network_switch/in_discards` BETA ** _(project)_**   
In Discards   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of incoming packets that were discarded._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`peer_target_identifier`: The identifier of the peer machine or switch.   
`peer_port_identifier`: Index of NIC on the peer machine, or logical name of the port on the peer switch.   
`network_switch/in_errors` BETA ** _(project)_**   
In Errors   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of incoming packets that were received with errors._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`peer_target_identifier`: The identifier of the peer machine or switch.   
`peer_port_identifier`: Index of NIC on the peer machine, or logical name of the port on the peer switch.   
`network_switch/in_packets_count` BETA ** _(project)_**   
In Packets Count   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The total number of incoming packets received on the port._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`network_switch/interface_flaps_count` BETA ** _(project)_**   
Interface Flaps   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of times the interface has flapped._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`network_switch/memory_used` BETA ** _(project)_**   
Memory Used   
`GAUGE`, `INT64`, `By`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The memory used by the network switch._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`network_switch/out_bytes_count` BETA ** _(project)_**   
Outbound Bytes Count   
`CUMULATIVE`, `INT64`, `By`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The total number of outgoing bytes transmitted out of the port._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`queue_name`: The name of the queue.   
`network_switch/out_discards` BETA ** _(project)_**   
Out Discards   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of outbound packets that were intended to be sent, but ultimately dropped._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`peer_target_identifier`: The identifier of the peer machine or switch.   
`peer_port_identifier`: Index of NIC on the peer machine, or logical name of the port on the peer switch.   
`network_switch/out_errors` BETA ** _(project)_**   
Out Errors   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of outbound packets that were intended to be sent, but resulted in errors during transmission._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`peer_target_identifier`: The identifier of the peer machine or switch.   
`peer_port_identifier`: Index of NIC on the peer machine, or logical name of the port on the peer switch.   
`network_switch/pfc_rx_packets_count` BETA ** _(project)_**   
PFC RX Packets   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of PFC RX packets._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`priority_index`: The priority index.   
`network_switch/pfc_tx_packets_count` BETA ** _(project)_**   
PFC TX Packets   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of PFC TX packets._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`queue_name`: The name of the queue.   
`network_switch/port_high_micro_utilization_fraction` BETA ** _(project)_**   
Port High Micro Utilization Fraction   
`GAUGE`, `DOUBLE`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The fraction of measurements where the physical interface (port) micro-utilization exceeded 95% during the most recent measurement cycle._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`network_switch/port_status` BETA ** _(project)_**   
Port Status   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _Indicates the status of the ports on the network switch. Value is always 1 for easier aggregation. The actual status is provided as a metric label._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`peer_target_identifier`: The identifier of the peer machine or switch.   
`peer_port_identifier`: Index of NIC on the peer machine, or logical name of the port on the peer switch.   
`status`: The port status.   
`network_switch/qos_tx_packets` BETA ** _(project)_**   
QoS TX Packets   
`CUMULATIVE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The number of QoS TX packets._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`port_identifier`: The logical name of the port on the network switch.   
`queue_name`: The name of the queue.   
`network_switch/total_memory_bytes` BETA ** _(project)_**   
Total Memory   
`GAUGE`, `INT64`, `By`   
**[compute.googleapis.com/NetworkSwitch](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkSwitch)** |  _The total memory of the network switch._   
`subblock_id`: The ID of the sub-block that the network switch belongs to.   
`block_id`: The ID of the block that the network switch belongs to.   
`reservation_id`: The ID of the reservation.   
`switch_type`: The network switch type.   
`node_group/cpu/scheduled` GA ** _(project)_**   
CPU Scheduled   
`GAUGE`, `INT64`, `cores`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the scheduled CPU for a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`node_group/cpu/total` GA ** _(project)_**   
CPU Total   
`GAUGE`, `INT64`, `cores`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the total CPU reserved for a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`node_group/cpu/utilization` GA ** _(project)_**   
CPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the CPU utilization of a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`node_group/instances` GA ** _(project)_**   
Instance Count   
`GAUGE`, `INT64`, `1`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the count of instances in a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`instance_name`: The name of the instance.   
`status`: The status of the instance.   
`node_group/memory/bandwidth_utilization` GA ** _(project)_**   
Memory Bandwidth Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the memory bandwidth utilization of a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`node_group/memory/scheduled` GA ** _(project)_**   
Memory Scheduled   
`GAUGE`, `INT64`, `GB`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the scheduled memory reserved for a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`node_group/memory/total` GA ** _(project)_**   
Memory Total   
`GAUGE`, `INT64`, `GB`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the total memory reserved for a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`node_group/memory/utilization` GA ** _(project)_**   
Memory Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the memory utilization of a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`node_group/network/bandwidth_limit` GA ** _(project)_**   
Network Bandwidth Limit   
`GAUGE`, `DOUBLE`, `Gbps`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the network bandwidth limit of a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`node_group/network/bandwidth_utilization` GA ** _(project)_**   
Network Bandwidth Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the network bandwidth utilization of a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`node_group/nodes` GA ** _(project)_**   
Node Count   
`GAUGE`, `INT64`, `1`   
**[gce_node_group](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_node_group)** |  _This metric represents the count of nodes in a node group. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`node_name`: The name of the node.   
`node_group_name`: The name of the node group.   
`status`: The status of the node.   
`private_service_connect/consumer/closed_connections_count` GA ** _(project)_**   
Closed connections count   
`DELTA`, `INT64`, `{connection}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of TCP/UDP connections closed over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/dropped_received_packets_count` GA ** _(project)_**   
Received packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of received packets dropped by a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/dropped_sent_packets_count` GA ** _(project)_**   
Sent packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of sent packets dropped by a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/new_connections_count` GA ** _(project)_**   
New connections count   
`DELTA`, `INT64`, `{connection}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of new TCP/UDP connections created over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/open_connections` GA ** _(project)_**   
Open connections   
`GAUGE`, `INT64`, `{connection}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Number of TCP/UDP connections currently open on a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/received_bytes_count` GA ** _(project)_**   
Received bytes count   
`DELTA`, `INT64`, `By`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of bytes received (PSC - > Clients) over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/received_packets_count` GA ** _(project)_**   
Received packets count   
`DELTA`, `INT64`, `{packet}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of packets received (PSC - > Clients) over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/sent_bytes_count` GA ** _(project)_**   
Sent bytes count   
`DELTA`, `INT64`, `By`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of bytes sent (Clients - > PSC) over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/consumer/sent_packets_count` GA ** _(project)_**   
Sent packets count   
`DELTA`, `INT64`, `{packet}`   
**[compute.googleapis.com/PrivateServiceConnectEndpoint](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/PrivateServiceConnectEndpoint)** |  _Count of packets sent (Clients - > PSC) over a PSC connection ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`private_service_connect/producer/closed_connections_count` GA ** _(project)_**   
Closed connections count   
`DELTA`, `INT64`, `{connection}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of TCP/UDP connections closed over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/connected_consumer_forwarding_rules` GA ** _(project)_**   
Connected consumer forwarding rules   
`GAUGE`, `INT64`, `1`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Number of Consumer Forwarding Rules connected to a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`private_service_connect/producer/dropped_received_packets_count` GA ** _(project)_**   
Received packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of received packets dropped by a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/dropped_sent_packets_count` GA ** _(project)_**   
Sent packets dropped count   
`DELTA`, `INT64`, `{packet}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of sent packets dropped by a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/nat_ip_address_capacity` GA ** _(project)_**   
Nat ip address capacity   
`GAUGE`, `INT64`, `1`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Number of total IP addresses of a PSC Service Attachment resource ID. (Value -1 means the number is larger than the max value of INT64.) Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`private_service_connect/producer/new_connections_count` GA ** _(project)_**   
New connections count   
`DELTA`, `INT64`, `{connection}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of new TCP/UDP connections created over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/open_connections` GA ** _(project)_**   
Open connections   
`GAUGE`, `INT64`, `{connection}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Number of TCP/UDP connections currently open on a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/received_bytes_count` GA ** _(project)_**   
Received bytes count   
`DELTA`, `INT64`, `By`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of bytes received (PSC - > Service) over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/received_packets_count` GA ** _(project)_**   
Received packets count   
`DELTA`, `INT64`, `{packet}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of packets received (PSC - > Service) over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/sent_bytes_count` GA ** _(project)_**   
Sent bytes count   
`DELTA`, `INT64`, `By`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of bytes sent (Service - > PSC) over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/sent_packets_count` GA ** _(project)_**   
Sent packets count   
`DELTA`, `INT64`, `{packet}`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _Count of packets sent (Service - > PSC) over a PSC Service Attachment resource ID. Sampled every 60 seconds. After sampling, data is not visible for up to 345 seconds._   
`ip_protocol`: The protocol of the connection. Can be TCP or UDP.   
`psc_connection_id`: The Private Service Connect connection ID of the Private Service Connect Forwarding Rule.   
`private_service_connect/producer/used_nat_ip_addresses` GA ** _(project)_**   
Used nat ip addresses   
`GAUGE`, `INT64`, `1`   
**[gce_service_attachment](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_service_attachment)** |  _IP usage of the monitored service attachment. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`quota/asynchronously_replicating_disk_pairs_per_project_region_pair/exceeded` GA ** _(project)_**   
Asynchronously replicating disk pairs per project and region pair quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/asynchronously_replicating_disk_pairs_per_project_region_pair. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`paired_region`: Asynchronously replicating disk pairs custom dimension.   
`quota/asynchronously_replicating_disk_pairs_per_project_region_pair/limit` GA ** _(project)_**   
Asynchronously replicating disk pairs per project and region pair quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current limit on quota metric compute.googleapis.com/asynchronously_replicating_disk_pairs_per_project_region_pair. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`paired_region`: Asynchronously replicating disk pairs custom dimension.   
`quota/asynchronously_replicating_disk_pairs_per_project_region_pair/usage` GA ** _(project)_**   
Asynchronously replicating disk pairs per project and region pair quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current usage on quota metric compute.googleapis.com/asynchronously_replicating_disk_pairs_per_project_region_pair. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`paired_region`: Asynchronously replicating disk pairs custom dimension.   
`quota/broadcast_subnetworks_per_region_per_vpc_network/exceeded` GA ** _(project)_**   
Broadcast subnetworks per region per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/broadcast_subnetworks_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/broadcast_subnetworks_per_region_per_vpc_network/limit` GA ** _(project)_**   
Broadcast subnetworks per region per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/broadcast_subnetworks_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/broadcast_subnetworks_per_region_per_vpc_network/usage` GA ** _(project)_**   
Broadcast subnetworks per region per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/broadcast_subnetworks_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_router_prefixes_from_other_regions_per_region_per_vpc_network/limit` GA ** _(project)_**   
Unique Cloud Router dynamic route prefixes from other regions per region per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/cloud_router_prefixes_from_other_regions_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_router_prefixes_from_other_regions_per_region_per_vpc_network/usage` GA ** _(project)_**   
Unique Cloud Router dynamic route prefixes from other regions per region per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/cloud_router_prefixes_from_other_regions_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_router_prefixes_from_own_region_per_region_per_vpc_network/limit` GA ** _(project)_**   
Unique Cloud Router dynamic route prefixes from own region per region per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/cloud_router_prefixes_from_own_region_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cloud_router_prefixes_from_own_region_per_region_per_vpc_network/usage` GA ** _(project)_**   
Unique Cloud Router dynamic route prefixes from own region per region per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/cloud_router_prefixes_from_own_region_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/concurrent/global_concurrent_operations/exceeded` ALPHA ** _(project)_**   
Concurrent global operations per project concurrent quota exceeded   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/OperationType](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/OperationType)** |  _Concurrent exceeded on quota metric compute.googleapis.com/global_concurrent_operations. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`quota/concurrent/global_concurrent_operations/limit` ALPHA ** _(project)_**   
Concurrent global operations per project concurrent quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/OperationType](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/OperationType)** |  _Concurrent limit on quota metric compute.googleapis.com/global_concurrent_operations. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`quota/concurrent/global_concurrent_operations/usage` ALPHA ** _(project)_**   
global_concurrent_operations usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/OperationType](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/OperationType)** |  _The concurrent usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`time_window`: The window size for concurrent operation limits.   
`quota/concurrent/regional_concurrent_operations/exceeded` ALPHA ** _(project)_**   
Concurrent regional operations per project concurrent quota exceeded   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/OperationType](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/OperationType)** |  _Concurrent exceeded on quota metric compute.googleapis.com/regional_concurrent_operations. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`quota/concurrent/regional_concurrent_operations/limit` ALPHA ** _(project)_**   
Concurrent regional operations per project concurrent quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/OperationType](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/OperationType)** |  _Concurrent limit on quota metric compute.googleapis.com/regional_concurrent_operations. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`time_window`: time_window.   
`quota/concurrent/regional_concurrent_operations/usage` ALPHA ** _(project)_**   
regional_concurrent_operations usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/OperationType](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/OperationType)** |  _The concurrent usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`time_window`: The window size for concurrent operation limits.   
`quota/cpus_per_vm_family/exceeded` ALPHA ** _(project)_**   
CPU count per VM family. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/cpus_per_vm_family. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`vm_family`: VM family custom dimension.   
`quota/cpus_per_vm_family/limit` ALPHA ** _(project)_**   
CPU count per VM family. quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current limit on quota metric compute.googleapis.com/cpus_per_vm_family. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`vm_family`: VM family custom dimension.   
`quota/cpus_per_vm_family/usage` ALPHA ** _(project)_**   
CPU count per VM family. quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current usage on quota metric compute.googleapis.com/cpus_per_vm_family. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`vm_family`: VM family custom dimension.   
`quota/cross_regional_internal_proxy_lb_config_per_region_per_vpc_network/exceeded` BETA ** _(project)_**   
Cross regional internal proxy LB config size per region per VPC network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/cross_regional_internal_proxy_lb_config_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cross_regional_internal_proxy_lb_config_per_region_per_vpc_network/limit` BETA ** _(project)_**   
Cross regional internal proxy LB config size per region per VPC network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/cross_regional_internal_proxy_lb_config_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cross_regional_internal_proxy_lb_config_per_region_per_vpc_network/usage` BETA ** _(project)_**   
Cross regional internal proxy LB config size per region per VPC network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/cross_regional_internal_proxy_lb_config_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disks_per_consistency_group/exceeded` GA ** _(project)_**   
Disk count per consistency group quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/ResourcePolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/ResourcePolicy)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/disks_per_consistency_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disks_per_consistency_group/limit` GA ** _(project)_**   
Disk count per consistency group quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/ResourcePolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/ResourcePolicy)** |  _Current limit on quota metric compute.googleapis.com/disks_per_consistency_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disks_per_consistency_group/usage` GA ** _(project)_**   
Disk count per consistency group quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/ResourcePolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/ResourcePolicy)** |  _Current usage on quota metric compute.googleapis.com/disks_per_consistency_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disks_per_snapshot_schedule/exceeded` GA ** _(project)_**   
Disk count per snapshot schedule quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/ResourcePolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/ResourcePolicy)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/disks_per_snapshot_schedule. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disks_per_snapshot_schedule/limit` GA ** _(project)_**   
Disk count per snapshot schedule quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/ResourcePolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/ResourcePolicy)** |  _Current limit on quota metric compute.googleapis.com/disks_per_snapshot_schedule. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disks_per_snapshot_schedule/usage` GA ** _(project)_**   
Disk count per snapshot schedule quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/ResourcePolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/ResourcePolicy)** |  _Current usage on quota metric compute.googleapis.com/disks_per_snapshot_schedule. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disks_per_storage_pool/exceeded` GA ** _(project)_**   
Disk count per storage pool quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/disks_per_storage_pool. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disks_per_storage_pool/limit` GA ** _(project)_**   
Disk count per storage pool quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Current limit on quota metric compute.googleapis.com/disks_per_storage_pool. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/disks_per_storage_pool/usage` GA ** _(project)_**   
Disk count per storage pool quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Current usage on quota metric compute.googleapis.com/disks_per_storage_pool. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/dynamic_routes_per_region_per_peering_group/limit` GA ** _(project)_**   
Dynamic routes per region per peering group quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/dynamic_routes_per_region_per_peering_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/dynamic_routes_per_region_per_peering_group/usage` GA ** _(project)_**   
Dynamic routes per region per peering group quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/dynamic_routes_per_region_per_peering_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/firewall_rule_attributes_per_region_per_vpc_network/exceeded` GA ** _(project)_**   
Firewall Rule attributes per region per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/firewall_rule_attributes_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/firewall_rule_attributes_per_region_per_vpc_network/limit` GA ** _(project)_**   
Firewall Rule attributes per region per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/firewall_rule_attributes_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/firewall_rule_attributes_per_region_per_vpc_network/usage` GA ** _(project)_**   
Firewall Rule attributes per region per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/firewall_rule_attributes_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/firewall_rule_fqdns_per_region_per_vpc_network/exceeded` GA ** _(project)_**   
Firewall Rule FQDNs per region per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/firewall_rule_fqdns_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/firewall_rule_fqdns_per_region_per_vpc_network/limit` GA ** _(project)_**   
Firewall Rule FQDNs per region per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/firewall_rule_fqdns_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/firewall_rule_fqdns_per_region_per_vpc_network/usage` GA ** _(project)_**   
Firewall Rule FQDNs per region per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/firewall_rule_fqdns_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/fqdns_per_global_network_firewall_policy/exceeded` GA ** _(project)_**   
FQDN per global network firewall policy quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/fqdns_per_global_network_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/fqdns_per_global_network_firewall_policy/limit` GA ** _(project)_**   
FQDN per global network firewall policy quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current limit on quota metric compute.googleapis.com/fqdns_per_global_network_firewall_policy. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/fqdns_per_global_network_firewall_policy/usage` GA ** _(project)_**   
FQDN per global network firewall policy quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current usage on quota metric compute.googleapis.com/fqdns_per_global_network_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/fqdns_per_hierarchical_firewall_policy/exceeded` GA ** _(project)_**   
Hierarchical firewall policy FQDN objects per firewall policy. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/fqdns_per_hierarchical_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/fqdns_per_hierarchical_firewall_policy/limit` GA ** _(project)_**   
Hierarchical firewall policy FQDN objects per firewall policy. quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current limit on quota metric compute.googleapis.com/fqdns_per_hierarchical_firewall_policy. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/fqdns_per_hierarchical_firewall_policy/usage` GA ** _(project)_**   
Hierarchical firewall policy FQDN objects per firewall policy. quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current usage on quota metric compute.googleapis.com/fqdns_per_hierarchical_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/fqdns_per_regional_network_firewall_policy/exceeded` GA ** _(project)_**   
FQDN per regional network firewall policy quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/fqdns_per_regional_network_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/fqdns_per_regional_network_firewall_policy/limit` GA ** _(project)_**   
FQDN per regional network firewall policy quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current limit on quota metric compute.googleapis.com/fqdns_per_regional_network_firewall_policy. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/fqdns_per_regional_network_firewall_policy/usage` GA ** _(project)_**   
FQDN per regional network firewall policy quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current usage on quota metric compute.googleapis.com/fqdns_per_regional_network_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_firewall_programmed_secure_tag_values_per_vpc_network/exceeded` GA ** _(project)_**   
GCE Firewall programmed Secure Tag Values per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/gce_firewall_programmed_secure_tag_values_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_firewall_programmed_secure_tag_values_per_vpc_network/limit` GA ** _(project)_**   
GCE Firewall programmed Secure Tag Values per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/gce_firewall_programmed_secure_tag_values_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gce_firewall_programmed_secure_tag_values_per_vpc_network/usage` GA ** _(project)_**   
GCE Firewall programmed Secure Tag Values per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/gce_firewall_programmed_secure_tag_values_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/global_internal_managed_forwarding_rules_per_region_per_vpc_network/exceeded` GA ** _(project)_**   
Cross Regional Internal Managed Load Balancer Forwarding Rules per region per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/global_internal_managed_forwarding_rules_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/global_internal_managed_forwarding_rules_per_region_per_vpc_network/limit` GA ** _(project)_**   
Cross Regional Internal Managed Load Balancer Forwarding Rules per region per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/global_internal_managed_forwarding_rules_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/global_internal_managed_forwarding_rules_per_region_per_vpc_network/usage` GA ** _(project)_**   
Cross Regional Internal Managed Load Balancer Forwarding Rules per region per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/global_internal_managed_forwarding_rules_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/gpus_per_gpu_family/exceeded` GA ** _(project)_**   
GPU count per GPU family. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/gpus_per_gpu_family. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`gpu_family`: GPU family custom dimension.   
`quota/gpus_per_gpu_family/limit` GA ** _(project)_**   
GPU count per GPU family. quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current limit on quota metric compute.googleapis.com/gpus_per_gpu_family. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`gpu_family`: GPU family custom dimension.   
`quota/gpus_per_gpu_family/usage` GA ** _(project)_**   
GPU count per GPU family. quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current usage on quota metric compute.googleapis.com/gpus_per_gpu_family. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`gpu_family`: GPU family custom dimension.   
`quota/instances_per_peering_group/limit` GA ** _(project)_**   
Instances Per peering group quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/instances_per_peering_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/instances_per_peering_group/usage` GA ** _(project)_**   
Instances Per peering group quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/instances_per_peering_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/instances_per_vpc_network/exceeded` GA ** _(project)_**   
Instances Per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/instances_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/instances_per_vpc_network/limit` GA ** _(project)_**   
Instances Per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/instances_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/instances_per_vpc_network/usage` GA ** _(project)_**   
Instances Per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/instances_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/inter_region_egress_bandwidth/exceeded` GA ** _(project)_**   
Inter-Region Network Egress Bandwidth (bps) from Compute instances quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/inter_region_egress_bandwidth. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`remote_location`: Cloud Region.   
`quota/inter_region_egress_bandwidth/limit` GA ** _(project)_**   
Inter-Region Network Egress Bandwidth (bps) from Compute instances quota limit   
`GAUGE`, `INT64`, `Mbit`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current limit on quota metric compute.googleapis.com/inter_region_egress_bandwidth. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`remote_location`: Cloud Region.   
`quota/inter_region_egress_bandwidth/usage` GA ** _(project)_**   
Inter-Region Network Egress Bandwidth (bps) from Compute instances quota usage   
`DELTA`, `INT64`, `Mbit`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current usage on quota metric compute.googleapis.com/inter_region_egress_bandwidth. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`remote_location`: Cloud Region.   
`quota/interconnect_attachments_per_interconnect/exceeded` GA ** _(project)_**   
Interconnect attachments per Interconnect quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/Interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Interconnect)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/interconnect_attachments_per_interconnect. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/interconnect_attachments_per_interconnect/limit` GA ** _(project)_**   
Interconnect attachments per Interconnect quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Interconnect)** |  _Current limit on quota metric compute.googleapis.com/interconnect_attachments_per_interconnect. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/interconnect_attachments_per_interconnect/usage` GA ** _(project)_**   
Interconnect attachments per Interconnect quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Interconnect)** |  _Current usage on quota metric compute.googleapis.com/interconnect_attachments_per_interconnect. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_lb_forwarding_rules_per_peering_group/limit` GA ** _(project)_**   
Internal passthrough Network Load Balancer forwarding rules per peering group quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/internal_lb_forwarding_rules_per_peering_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_lb_forwarding_rules_per_peering_group/usage` GA ** _(project)_**   
Internal passthrough Network Load Balancer forwarding rules per peering group quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/internal_lb_forwarding_rules_per_peering_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_lb_forwarding_rules_per_vpc_network/exceeded` GA ** _(project)_**   
Internal passthrough Network Load Balancer forwarding rules per VPC network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/internal_lb_forwarding_rules_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_lb_forwarding_rules_per_vpc_network/limit` GA ** _(project)_**   
Internal passthrough Network Load Balancer forwarding rules per VPC network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/internal_lb_forwarding_rules_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_lb_forwarding_rules_per_vpc_network/usage` GA ** _(project)_**   
Internal passthrough Network Load Balancer forwarding rules per VPC network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/internal_lb_forwarding_rules_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_managed_forwarding_rules_per_peering_group/limit` GA ** _(project)_**   
Internal Managed Forwarding Rules per peering group quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/internal_managed_forwarding_rules_per_peering_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_managed_forwarding_rules_per_peering_group/usage` GA ** _(project)_**   
Internal Managed Forwarding Rules per peering group quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/internal_managed_forwarding_rules_per_peering_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_managed_forwarding_rules_per_vpc_network/exceeded` GA ** _(project)_**   
Internal Managed Forwarding Rules per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/internal_managed_forwarding_rules_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_managed_forwarding_rules_per_vpc_network/limit` GA ** _(project)_**   
Internal Managed Forwarding Rules per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/internal_managed_forwarding_rules_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_managed_forwarding_rules_per_vpc_network/usage` GA ** _(project)_**   
Internal Managed Forwarding Rules per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/internal_managed_forwarding_rules_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_protocol_forwarding_ha_rules_per_vpc_network/exceeded` GA ** _(project)_**   
Internal Protocol Forwarding HA Rules per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/internal_protocol_forwarding_ha_rules_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_protocol_forwarding_ha_rules_per_vpc_network/limit` GA ** _(project)_**   
Internal Protocol Forwarding HA Rules per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/internal_protocol_forwarding_ha_rules_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_protocol_forwarding_ha_rules_per_vpc_network/usage` GA ** _(project)_**   
Internal Protocol Forwarding HA Rules per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/internal_protocol_forwarding_ha_rules_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_protocol_forwarding_rules_per_peering_group/limit` GA ** _(project)_**   
Internal protocol forwarding rules per peering group quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/internal_protocol_forwarding_rules_per_peering_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_protocol_forwarding_rules_per_peering_group/usage` GA ** _(project)_**   
Internal protocol forwarding rules per peering group quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/internal_protocol_forwarding_rules_per_peering_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_protocol_forwarding_rules_per_vpc_network/exceeded` GA ** _(project)_**   
Internal protocol forwarding rules per VPC network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/internal_protocol_forwarding_rules_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_protocol_forwarding_rules_per_vpc_network/limit` GA ** _(project)_**   
Internal protocol forwarding rules per VPC network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/internal_protocol_forwarding_rules_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/internal_protocol_forwarding_rules_per_vpc_network/usage` GA ** _(project)_**   
Internal protocol forwarding rules per VPC network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/internal_protocol_forwarding_rules_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/ip_aliases_per_peering_group/limit` GA ** _(project)_**   
IP Aliases per peering group quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/ip_aliases_per_peering_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/ip_aliases_per_peering_group/usage` GA ** _(project)_**   
IP Aliases per peering group quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/ip_aliases_per_peering_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/ip_aliases_per_vpc_network/exceeded` GA ** _(project)_**   
IP Aliases per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/ip_aliases_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/ip_aliases_per_vpc_network/limit` GA ** _(project)_**   
IP Aliases per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/ip_aliases_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/ip_aliases_per_vpc_network/usage` GA ** _(project)_**   
IP Aliases per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/ip_aliases_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/local_ssd_total_storage_per_vm_family/exceeded` BETA ** _(project)_**   
Local SSD disk per VM family (GB). quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/local_ssd_total_storage_per_vm_family. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`vm_family`: VM family custom dimension.   
`quota/local_ssd_total_storage_per_vm_family/limit` BETA ** _(project)_**   
Local SSD disk per VM family (GB). quota limit   
`GAUGE`, `INT64`, `GBy`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current limit on quota metric compute.googleapis.com/local_ssd_total_storage_per_vm_family. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`vm_family`: VM family custom dimension.   
`quota/local_ssd_total_storage_per_vm_family/usage` BETA ** _(project)_**   
Local SSD disk per VM family (GB). quota usage   
`GAUGE`, `INT64`, `GBy`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current usage on quota metric compute.googleapis.com/local_ssd_total_storage_per_vm_family. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`vm_family`: VM family custom dimension.   
`quota/multicast_consumers_per_zone_per_vpc_network/exceeded` GA ** _(project)_**   
Multicast consumers per zone per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/multicast_consumers_per_zone_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/multicast_consumers_per_zone_per_vpc_network/limit` GA ** _(project)_**   
Multicast consumers per zone per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/multicast_consumers_per_zone_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/multicast_consumers_per_zone_per_vpc_network/usage` GA ** _(project)_**   
Multicast consumers per zone per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/multicast_consumers_per_zone_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/peerings_per_vpc_network/exceeded` GA ** _(project)_**   
Peerings Per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/peerings_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/peerings_per_vpc_network/limit` GA ** _(project)_**   
Peerings Per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/peerings_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/peerings_per_vpc_network/usage` GA ** _(project)_**   
Peerings Per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/peerings_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/psc_google_apis_forwarding_rules_per_vpc_network/exceeded` GA ** _(project)_**   
PSC Google APIs Forwarding Rules per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/psc_google_apis_forwarding_rules_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/psc_google_apis_forwarding_rules_per_vpc_network/limit` GA ** _(project)_**   
PSC Google APIs Forwarding Rules per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/psc_google_apis_forwarding_rules_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/psc_google_apis_forwarding_rules_per_vpc_network/usage` GA ** _(project)_**   
PSC Google APIs Forwarding Rules per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/psc_google_apis_forwarding_rules_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network/exceeded` GA ** _(project)_**   
PSC ILB Consumer Forwarding Rules per Producer VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network/limit` GA ** _(project)_**   
PSC ILB Consumer Forwarding Rules per Producer VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network/usage` GA ** _(project)_**   
PSC ILB Consumer Forwarding Rules per Producer VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/psc_propagated_connections_per_vpc_network/exceeded` GA ** _(project)_**   
PSC propagated connections per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/psc_propagated_connections_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/psc_propagated_connections_per_vpc_network/limit` GA ** _(project)_**   
PSC propagated connections per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/psc_propagated_connections_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/psc_propagated_connections_per_vpc_network/usage` GA ** _(project)_**   
PSC propagated connections per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/psc_propagated_connections_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_backend_services_protocol_forwarding_fast_ha/exceeded` GA ** _(project)_**   
Regional Backend Services Protocol Forwarding Fast HA per region per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/regional_backend_services_protocol_forwarding_fast_ha. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_backend_services_protocol_forwarding_fast_ha/limit` GA ** _(project)_**   
Regional Backend Services Protocol Forwarding Fast HA per region per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/regional_backend_services_protocol_forwarding_fast_ha. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_backend_services_protocol_forwarding_fast_ha/usage` GA ** _(project)_**   
Regional Backend Services Protocol Forwarding Fast HA per region per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/regional_backend_services_protocol_forwarding_fast_ha. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_external_managed_forwarding_rules_per_region_per_vpc_network/exceeded` GA ** _(project)_**   
Regional External Managed Forwarding Rules per region per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/regional_external_managed_forwarding_rules_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_external_managed_forwarding_rules_per_region_per_vpc_network/limit` GA ** _(project)_**   
Regional External Managed Forwarding Rules per region per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/regional_external_managed_forwarding_rules_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_external_managed_forwarding_rules_per_region_per_vpc_network/usage` GA ** _(project)_**   
Regional External Managed Forwarding Rules per region per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/regional_external_managed_forwarding_rules_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_external_proxy_lb_config_per_region_per_vpc_network/exceeded` BETA ** _(project)_**   
Regional external proxy LB config size per region per VPC network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/regional_external_proxy_lb_config_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_external_proxy_lb_config_per_region_per_vpc_network/limit` BETA ** _(project)_**   
Regional external proxy LB config size per region per VPC network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/regional_external_proxy_lb_config_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_external_proxy_lb_config_per_region_per_vpc_network/usage` BETA ** _(project)_**   
Regional external proxy LB config size per region per VPC network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/regional_external_proxy_lb_config_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_internal_managed_forwarding_rules_per_region_per_vpc_network/exceeded` GA ** _(project)_**   
Regional Internal Managed Forwarding Rules per region per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/regional_internal_managed_forwarding_rules_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_internal_managed_forwarding_rules_per_region_per_vpc_network/limit` GA ** _(project)_**   
Regional Internal Managed Forwarding Rules per region per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/regional_internal_managed_forwarding_rules_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_internal_managed_forwarding_rules_per_region_per_vpc_network/usage` GA ** _(project)_**   
Regional Internal Managed Forwarding Rules per region per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/regional_internal_managed_forwarding_rules_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_internal_proxy_lb_config_per_region_per_vpc_network/exceeded` BETA ** _(project)_**   
Regional internal proxy LB config size per region per VPC network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/regional_internal_proxy_lb_config_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_internal_proxy_lb_config_per_region_per_vpc_network/limit` BETA ** _(project)_**   
Regional internal proxy LB config size per region per VPC network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/regional_internal_proxy_lb_config_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_internal_proxy_lb_config_per_region_per_vpc_network/usage` BETA ** _(project)_**   
Regional internal proxy LB config size per region per VPC network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/regional_internal_proxy_lb_config_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_network_firewall_policy_associations_per_region_per_vpc_network/exceeded` GA ** _(project)_**   
Regional customer defined Network Firewall Policy Associations per region per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/regional_network_firewall_policy_associations_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_network_firewall_policy_associations_per_region_per_vpc_network/limit` GA ** _(project)_**   
Regional customer defined Network Firewall Policy Associations per region per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/regional_network_firewall_policy_associations_per_region_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/regional_network_firewall_policy_associations_per_region_per_vpc_network/usage` GA ** _(project)_**   
Regional customer defined Network Firewall Policy Associations per region per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/regional_network_firewall_policy_associations_per_region_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/rule_attributes_per_global_network_firewall_policy/exceeded` GA ** _(project)_**   
Rule attributes per global network firewall policy quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/rule_attributes_per_global_network_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/rule_attributes_per_global_network_firewall_policy/limit` GA ** _(project)_**   
Rule attributes per global network firewall policy quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current limit on quota metric compute.googleapis.com/rule_attributes_per_global_network_firewall_policy. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/rule_attributes_per_global_network_firewall_policy/usage` GA ** _(project)_**   
Rule attributes per global network firewall policy quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current usage on quota metric compute.googleapis.com/rule_attributes_per_global_network_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/rule_attributes_per_hierarchical_firewall_policy/exceeded` GA ** _(project)_**   
Hierarchical firewall policy rule attributes (atoms) per firewall policy. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/rule_attributes_per_hierarchical_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/rule_attributes_per_hierarchical_firewall_policy/limit` GA ** _(project)_**   
Hierarchical firewall policy rule attributes (atoms) per firewall policy. quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current limit on quota metric compute.googleapis.com/rule_attributes_per_hierarchical_firewall_policy. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/rule_attributes_per_hierarchical_firewall_policy/usage` GA ** _(project)_**   
Hierarchical firewall policy rule attributes (atoms) per firewall policy. quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current usage on quota metric compute.googleapis.com/rule_attributes_per_hierarchical_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/rule_attributes_per_regional_network_firewall_policy/exceeded` GA ** _(project)_**   
Rule attributes per regional network firewall policy quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/rule_attributes_per_regional_network_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/rule_attributes_per_regional_network_firewall_policy/limit` GA ** _(project)_**   
Rule attributes per regional network firewall policy quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current limit on quota metric compute.googleapis.com/rule_attributes_per_regional_network_firewall_policy. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/rule_attributes_per_regional_network_firewall_policy/usage` GA ** _(project)_**   
Rule attributes per regional network firewall policy quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/FirewallPolicy](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/FirewallPolicy)** |  _Current usage on quota metric compute.googleapis.com/rule_attributes_per_regional_network_firewall_policy. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/statera_lb_per_org_per_region_per_folder/exceeded` ALPHA ** _(project)_**   
Envoy Pool Per Region Per Folder quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/statera_lb_per_org_per_region_per_folder. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`folder_id`: Folder ID custom dimension.   
`quota/statera_lb_per_org_per_region_per_folder/limit` ALPHA ** _(project)_**   
Envoy Pool Per Region Per Folder quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current limit on quota metric compute.googleapis.com/statera_lb_per_org_per_region_per_folder. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`folder_id`: Folder ID custom dimension.   
`quota/statera_lb_per_org_per_region_per_folder/usage` ALPHA ** _(project)_**   
Envoy Pool Per Region Per Folder quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current usage on quota metric compute.googleapis.com/statera_lb_per_org_per_region_per_folder. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`folder_id`: Folder ID custom dimension.   
`quota/static_routes_per_peering_group/limit` GA ** _(project)_**   
Custom static routes per peering group quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/static_routes_per_peering_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/static_routes_per_peering_group/usage` GA ** _(project)_**   
Custom static routes per peering group quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/static_routes_per_peering_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/static_routes_per_vpc_network/exceeded` GA ** _(project)_**   
Custom static routes per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/static_routes_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/static_routes_per_vpc_network/limit` GA ** _(project)_**   
Custom static routes per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/static_routes_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/static_routes_per_vpc_network/usage` GA ** _(project)_**   
Custom static routes per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/static_routes_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/subnet_ranges_per_peering_group/limit` GA ** _(project)_**   
Subnet ranges Per peering group quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/subnet_ranges_per_peering_group. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/subnet_ranges_per_peering_group/usage` GA ** _(project)_**   
Subnet ranges Per peering group quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/subnet_ranges_per_peering_group. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/subnet_ranges_per_vpc_network/exceeded` GA ** _(project)_**   
Subnetwork ranges per VPC Network quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/subnet_ranges_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/subnet_ranges_per_vpc_network/limit` GA ** _(project)_**   
Subnetwork ranges per VPC Network quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current limit on quota metric compute.googleapis.com/subnet_ranges_per_vpc_network. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/subnet_ranges_per_vpc_network/usage` GA ** _(project)_**   
Subnetwork ranges per VPC Network quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/VpcNetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/VpcNetwork)** |  _Current usage on quota metric compute.googleapis.com/subnet_ranges_per_vpc_network. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/tpus_per_tpu_family/exceeded` ALPHA ** _(project)_**   
TPU count per TPU family. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/tpus_per_tpu_family. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`tpu_family`: TPU family custom dimension.   
`quota/tpus_per_tpu_family/limit` ALPHA ** _(project)_**   
TPU count per TPU family. quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current limit on quota metric compute.googleapis.com/tpus_per_tpu_family. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`tpu_family`: TPU family custom dimension.   
`quota/tpus_per_tpu_family/usage` ALPHA ** _(project)_**   
TPU count per TPU family. quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _Current usage on quota metric compute.googleapis.com/tpus_per_tpu_family. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`tpu_family`: TPU family custom dimension.   
`quota/wire_groups_gold_unmetered_bandwidth_gbps/exceeded` GA ** _(project)_**   
Wire groups gold unmetered bandwidth quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/NetworkPathQuotasResource](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkPathQuotasResource)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/wire_groups_gold_unmetered_bandwidth_gbps. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/wire_groups_gold_unmetered_bandwidth_gbps/limit` GA ** _(project)_**   
Wire groups gold unmetered bandwidth quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkPathQuotasResource](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkPathQuotasResource)** |  _Current limit on quota metric compute.googleapis.com/wire_groups_gold_unmetered_bandwidth_gbps. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/wire_groups_gold_unmetered_bandwidth_gbps/usage` GA ** _(project)_**   
Wire groups gold unmetered bandwidth quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/NetworkPathQuotasResource](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/NetworkPathQuotasResource)** |  _Current usage on quota metric compute.googleapis.com/wire_groups_gold_unmetered_bandwidth_gbps. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/wire_groups_per_interconnect/exceeded` GA ** _(project)_**   
Wire groups per Interconnect quota exceeded error   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/Interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Interconnect)** |  _Number of attempts to exceed the limit on quota metric compute.googleapis.com/wire_groups_per_interconnect. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/wire_groups_per_interconnect/limit` GA ** _(project)_**   
Wire groups per Interconnect quota limit   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Interconnect)** |  _Current limit on quota metric compute.googleapis.com/wire_groups_per_interconnect. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/wire_groups_per_interconnect/usage` GA ** _(project)_**   
Wire groups per Interconnect quota usage   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Interconnect)** |  _Current usage on quota metric compute.googleapis.com/wire_groups_per_interconnect. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_concurrent_operations` ALPHA ** _(project)_**   
Concurrent regional operations per project   
`DELTA`, `INT64`, `1`   
**[compute.googleapis.com/OperationType](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/OperationType)** |  _Concurrent quota for regional operations._  
`reservation/reserved` GA ** _(project)_**   
Reserved   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Reservation](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Reservation)** |  _The number of resources reserved by this reservation. Sampled every 300 seconds. After sampling, data is not visible for up to 300 seconds._   
`reserved_resource_type`: Represents type of resource reserved. One of [instance].   
`reservation/used` GA ** _(project)_**   
Used   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Reservation](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Reservation)** |  _The number of resources used by this reservation. Sampled every 300 seconds. After sampling, data is not visible for up to 300 seconds._   
`reserved_resource_type`: Represents type of resource reserved. One of [instance].   
`service_name`: The name of the service which used the resource. One of [COMPUTE_ENGINE, VERTEX_TRAINING, VERTEX_ONLINE_PREDICTION].   
`storage_pool/capacity_overprovisioning` GA ** _(project)_**   
Capacity Overprovisioning   
`GAUGE`, `DOUBLE`, `%`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Ratio of total provisioned capacity of disks in the storage pool to storage pool provisioned capacity, in percentage. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/capacity_utilization` GA ** _(project)_**   
Capacity Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Ratio of total used capacities of disks in the storage pool to storage pool provisioned capacity, in percentage. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/disks` GA ** _(project)_**   
Disks   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Count of disks that are in the storage pool. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/iops_overprovisioning` GA ** _(project)_**   
IOPS Overprovisioning   
`GAUGE`, `DOUBLE`, `%`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Ratio of total provisioned IOPS of disks in the storage pool to storage pool provisioned IOPS, in percentage. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/iops_utilization` GA ** _(project)_**   
IOPS Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Ratio of total used IOPS of disks in the storage pool to storage pool provisioned IOPS, in percentage. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/provisioned_capacity` GA ** _(project)_**   
Provisioned Capacity   
`GAUGE`, `DOUBLE`, `TiBy`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Provisioned capacity of the storage pool. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/provisioned_iops` GA ** _(project)_**   
Provisioned IOPS   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Provisioned IOPS of the storage pool. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/provisioned_throughput` GA ** _(project)_**   
Provisioned Throughput   
`GAUGE`, `INT64`, `MiBy/s`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Provisioned throughput of the storage pool. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/throughput_overprovisioning` GA ** _(project)_**   
Throughput Overprovisioning   
`GAUGE`, `DOUBLE`, `%`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Ratio of total provisioned throughput of disks in the storage pool to storage pool provisioned throughput, in percentage. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/throughput_utilization` GA ** _(project)_**   
Throughput Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Ratio of total used throughput of disks in the storage pool to storage pool provisioned throughput, in percentage. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/total_disk_provisioned_capacity` GA ** _(project)_**   
Total Disk Provisioned Capacity   
`GAUGE`, `DOUBLE`, `TiBy`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Sum of provisioned capacity of the disks that are in the storage pool. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/total_disk_provisioned_iops` GA ** _(project)_**   
Total Disk Provisioned IOPS   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Sum of provisioned IOPS of the disks that are in the storage pool. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/total_disk_provisioned_throughput` GA ** _(project)_**   
Total Disk Provisioned Throughput   
`GAUGE`, `INT64`, `MiBy/s`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Sum of provisioned throughput of the disks that are in the storage pool. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/used_capacity` GA ** _(project)_**   
Used Capacity   
`GAUGE`, `DOUBLE`, `TiBy`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Sum of used capacity of the disks that are in the storage pool. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/used_iops` GA ** _(project)_**   
Used IOPS   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Sum of used IOPS of the disks that are in the storage pool. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/used_read_iops` BETA ** _(project)_**   
Used Read IOPS   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Sum of used read IOPS of the disks that are in the storage pool. Only available for exapool type storage pools. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/used_read_throughput` BETA ** _(project)_**   
Used Read Throughput   
`GAUGE`, `INT64`, `MiBy/s`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Sum of used read throughput of the disks that are in the storage pool. Only available for exapool type storage pools. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/used_throughput` GA ** _(project)_**   
Used Throughput   
`GAUGE`, `INT64`, `MiBy/s`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Sum of used throughput of the disks that are in the storage pool. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/used_write_iops` BETA ** _(project)_**   
Used Write IOPS   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Sum of used write IOPS of the disks that are in the storage pool. Only available for exapool type storage pools. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage_pool/used_write_throughput` BETA ** _(project)_**   
Used Write Throughput   
`GAUGE`, `INT64`, `MiBy/s`   
**[compute.googleapis.com/StoragePool](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/StoragePool)** |  _Sum of used write throughput of the disks that are in the storage pool. Only available for exapool type storage pools. Sampled every 1800 seconds. After sampling, data is not visible for up to 240 seconds._  
`tpu/capacity/available_chips` BETA ** _(project)_**   
Available TPU Chips Count   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _The current count of TPU chips that are available and ready to use._   
`accelerator_type`: The accelerator type and generation.   
`reservation_id`: The ID of the physical machine reservation.   
`provisioning_model`: The associated provisioning model.   
`protection_tier`: The associated protection model.   
`is_exr`: Indicates whether the TPU chip is part of an extended reservation.   
`tpu/capacity/committed_chips` BETA ** _(project)_**   
Purchased TPU Chips Count   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Location)** |  _The current count of purchased TPU chips._   
`accelerator_type`: The accelerator type and generation.   
`reservation_id`: The ID of the physical machine reservation.   
`provisioning_model`: The associated provisioning model.   
`protection_tier`: The associated protection model.   
`is_exr`: Indicates whether the TPU chip is part of an extended reservation.   
`tpu/multislice/accelerator/device_to_host_transfer_latencies` BETA ** _(project)_**   
Device to Host Transfer Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cumulative distribution of device to host transfer latency for each chunk of data. A latency starts when the request for data to be transferred to the host is issued and ends when an acknowledgement is received that the transfer of data has completed._   
`buffer_size`: Buffer size.   
`tpu/multislice/accelerator/host_to_device_transfer_latencies` BETA ** _(project)_**   
Host to Device Transfer Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cumulative distribution of host to device transfer latency for each chunk of data of multislice traffic. A latency starts when the request for data to be transferred to the device is issued and ends when an acknowledgement is received that the transfer of data has completed._   
`buffer_size`: Buffer size.   
`tpu/multislice/network/collective_end_to_end_latencies` BETA ** _(project)_**   
Collective End-to-End Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cumulative distribution of end to end collective latency for multislice traffic. A latency starts when the request for the collective is issued and ends when an acknowledgement is received that the transfer of data has completed._   
`input_size`: Input size of the collective operation.   
`collective_type`: Type of the collective operation.   
`tpu/multislice/network/dcn_transfer_latencies` BETA ** _(project)_**   
DCN Transfer Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cumulative distribution of network-transfer latencies for multislice traffic. A latency starts when the request for data to be transferred over the DCN is issued and ends when an acknowledgement is received that the transfer of data has completed._   
`buffer_size`: Buffer size.   
`type`: Type.   
`tpu/multislice/network/grpc_client_call_latencies` BETA ** _(project)_**   
gRPC Client Call Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cumulative distribution of network-transfer latencies for gRPC library takes to complete an RPC from the caller perspective._   
`buffer_size`: Buffer size.   
`tpu/multislice/network/grpc_server_call_latencies` BETA ** _(project)_**   
gRPC Server Call Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cumulative distribution of network-transfer latencies for gRPC server to complete an RPC on transport perspective._   
`buffer_size`: Buffer size.   
`tpu/multislice/network/grpc_tcp_delivery_rates` BETA ** _(project)_**   
gRPC TCP Delivery Rates   
`CUMULATIVE`, `DISTRIBUTION`, `Mb/s`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cumulative distribution of the TCP connections data transfer rates. Each sample is the latest mean data transfer rate for a given TCP connection over the last TCP ACK interval. Samples of data transfer rates are pulled from the Linux TCP Kernel every 20s, so it can be expected that every TCP connection creates approximately 3 samples per 60s interval._  
`tpu/multislice/network/grpc_tcp_min_round_trip_times` BETA ** _(project)_**   
gRPC TCP Min Round Trip Times   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cumulative distribution of minimum network-transfer latencies per TCP connection._  
`tpu/multislice/network/grpc_tcp_packets_retransmitted_count` BETA ** _(project)_**   
gRPC TCP Packets Retransmitted Count   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of packets retransmitted._  
`tpu/multislice/network/grpc_tcp_packets_sent_count` BETA ** _(project)_**   
gRPC TCP Packets Sent Count   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of packets TCP sends._  
`tpu/network/nic_packets_dropped_count_rx` BETA ** _(project)_**   
NIC Packets Dropped Count Rx   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total number of incoming or outgoing packets discarded by the host NIC, for RX._   
`nic_id`: Nic Id.   
`tpu/network/nic_packets_dropped_count_tx` BETA ** _(project)_**   
NIC Packets Dropped Count Tx   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total number of incoming or outgoing packets discarded by the host NIC, for TX._   
`nic_id`: Nic Id.   
`tpu/network/nic_packets_received_count` BETA ** _(project)_**   
NIC Packets Received Count   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total count of packets received by the NIC._   
`nic_id`: Nic Id.   
`tpu/network/nic_packets_sent_count` BETA ** _(project)_**   
NIC Packets Sent Count   
`CUMULATIVE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The total count of packets sent by the NIC._   
`nic_id`: Nic Id.   
`tpu/slice/capacity/available_chips` GA ** _(project)_**   
Available TPU Chips Count   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/AcceleratorSlice](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/AcceleratorSlice)** |  _The current count of TPU chips of Extended Reservation that are actively available and ready to use. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`accelerator_type`: Accelerator type and generation.   
`reservation_id`: The ID of the physical machine reservation.   
`block_id`: The block ID associated with the slice.   
`subblock_id`: The subblock ID associated with the slice.   
`provisioning_model`: The associated provisioning model.   
`protection_tier`: The associated protection model.   
`tpu/slice/capacity/committed_chips` GA ** _(project)_**   
Purchased TPU Chips Count   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/AcceleratorSlice](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/AcceleratorSlice)** |  _The current count of purchased TPU chips of Extended Reservation. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`accelerator_type`: Accelerator type and generation.   
`reservation_id`: The ID of the physical machine reservation.   
`block_id`: The block ID associated with the slice.   
`subblock_id`: The subblock ID associated with the slice.   
`provisioning_model`: The associated provisioning model.   
`protection_tier`: The associated protection model.   
`vm_extensions/extension/cpu/max_usage` BETA ** _(project)_**   
VM Extension CPU Max Usage   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Max CPU time used by the VM extension in percentage._   
`extension_name`: The name of the VM extension.   
`vm_extensions/extension/enforcement_status` BETA ** _(project)_**   
VM Extension Enforcement Status   
`GAUGE`, `BOOL`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current enforcement state of a VM extension. A point is True if the extension is in the specified state._   
`extension_name`: The name of the VM extension (e.g., "ops-agent").   
`status`: The enforcement status. e.g. INSTALLED, INSTALL_FAILED,"ROLLED_BACK.   
`vm_extensions/extension/health_status` BETA ** _(project)_**   
VM Extension Health Status   
`GAUGE`, `BOOL`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current health status of a VM extension. A point is True if the extension is in the specified health state._   
`extension_name`: The name of the VM extension (e.g., "ops-agent").   
`status`: The health status. e.g. RUNNING, CRASHED, STOPPED.   
`vm_extensions/extension/memory/used_bytes` BETA ** _(project)_**   
VM Extension Memory Max Used Bytes   
`GAUGE`, `INT64`, `By`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Max memory usage of the VM extension in bytes._   
`extension_name`: The name of the VM extension.   
`workload/available_slice_efficiency` BETA ** _(project)_**   
Available Slice Efficiency   
`GAUGE`, `DOUBLE`, `1`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _Out of all the requested slices, how many are healthy from the perspective of the elastic manager in the requested window (CUMULATIVE) or over a rolling window (INTERVAL)._   
`cluster_name`: The name of the cluster where the workload is running.   
`accelerator_type`: The type of the accelerator used by the workload.   
`rolling_window_size`: (INT64) The size of the rolling window used to calculate efficiency of the workload in seconds.   
`window_type`: The type of the window used to calculate efficiency. This can be `CUMULATIVE` or `INTERVAL`.   
`workload/badput_time` BETA ** _(project)_**   
Non-Productive Time (seconds)   
`GAUGE`, `DOUBLE`, `s`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _This is a writable metric that allows users to report the total time (in seconds) their workload spend on a specific non-productive activity. Values reported to this metric are visible to the Google Cloud team. Providing this value helps the Google Cloud team understand workload inefficiencies and how they are affected by infrastructure changes. The reported value represents time spent on a specific non-productive task in ML workloads._   
`cluster_name`: The name of the cluster where the workload is running.   
`accelerator_type`: The type of the accelerator used by the workload.   
`badput_source`: The source of the badput activity.   
`workload/disruptions` BETA ** _(project)_**   
Disruptions Count   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _This is a writable metric that allows users to report the number of disruptions in the workload since it started (CUMULATIVE) or over a rolling window (INTERVAL)._   
`cluster_name`: The name of the cluster where the workload is running.   
`accelerator_type`: The type of the accelerator used by the workload.   
`window_type`: The type of the window used to calculate the total elapsed time. This can be `CUMULATIVE` or `INTERVAL`.   
`workload/goodput_time` BETA ** _(project)_**   
Productive Time (seconds)   
`GAUGE`, `DOUBLE`, `s`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _This is a writable metric that allows users to report the total time (in seconds) their workload spends on a specific productive activity. Values reported to this metric are visible to the Google Cloud team. Providing this value helps the Google Cloud team understand how user workloads respond to changes in Google Cloud infrastructure. The reported value represents the absolute time spent on a specific useful, value-generating task in ML workloads._   
`goodput_source`: The source of the goodput activity.   
`cluster_name`: The name of the cluster where the workload is running.   
`accelerator_type`: The type of the accelerator used by the workload.   
`workload/interval_badput` BETA ** _(project)_**   
Rolling Window Badput   
`GAUGE`, `DOUBLE`, `%`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _This is a writable metric that allows users to report the badput of the workload over a rolling window as percentage of the total time in the window._   
`cluster_name`: The name of the cluster where the workload is running.   
`accelerator_type`: The type of the accelerator used by the workload.   
`rolling_window_size`: (INT64) The size of the rolling window used to calculate badput of the workload in seconds.   
`badput_source`: The source of the badput activity.   
`workload/interval_goodput` BETA ** _(project)_**   
Rolling Window Goodput   
`GAUGE`, `DOUBLE`, `%`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _This is a writable metric that allows users to report the goodput of the workload over a rolling window as percentage of the total time in the window._   
`goodput_source`: The source of the goodput activity.   
`cluster_name`: The name of the cluster where the workload is running.   
`accelerator_type`: The type of the accelerator used by the workload.   
`rolling_window_size`: (INT64) The size of the rolling window used to calculate goodput of the workload in seconds.   
`workload/max_productive_steps` BETA ** _(project)_**   
Step Count   
`GAUGE`, `INT64`, `1`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _This is a writable metric that allows users to report the last productive step count completed by the workload._   
`cluster_name`: The name of the cluster where the workload is running.   
`accelerator_type`: The type of the accelerator used by the workload.   
`workload/performance` BETA ** _(project)_**   
Performance   
`GAUGE`, `DOUBLE`, `1`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _This is a writable metric that allows users to report the performance of their workload. Values reported to this metric is visible to Google Cloud team. Providing this value helps Google Cloud team understanding user workload react to different changes to the Google Cloud infrastructure. The performance value is a numeric value that is up to the user to define its range. For eg: It could be the training step time in seconds or ratio of expected performance of the workload._  
`workload/step_time_deviation` BETA ** _(project)_**   
Step Time Deviation (seconds)   
`GAUGE`, `DOUBLE`, `s`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _This is a writable metric that allows users to report the step time deviation experienced by the workload from the expected step time._   
`cluster_name`: The name of the cluster where the workload is running.   
`accelerator_type`: The type of the accelerator used by the workload.   
`workload/stepping_slice_efficiency` BETA ** _(project)_**   
Stepping Slice Efficiency   
`GAUGE`, `DOUBLE`, `1`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _Out of all the requested slices, how many are used in stepping in the requested window (CUMULATIVE) or over a rolling window (INTERVAL)._   
`cluster_name`: The name of the cluster where the workload is running.   
`accelerator_type`: The type of the accelerator used by the workload.   
`rolling_window_size`: (INT64) The size of the rolling window used to calculate efficiency of the workload in seconds.   
`window_type`: The type of the window used to calculate efficiency. This can be `CUMULATIVE` or `INTERVAL`.   
`workload/total_elapsed_time` BETA ** _(project)_**   
Total Elapsed Time (seconds)   
`GAUGE`, `DOUBLE`, `s`   
**[compute.googleapis.com/Workload](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/Workload)** |  _This is a writable metric that allows users to report the total elapsed time of the workload since it started (CUMULATIVE) or over a rolling window (INTERVAL)._   
`cluster_name`: The name of the cluster where the workload is running.   
`accelerator_type`: The type of the accelerator used by the workload.   
`window_type`: The type of the window used to calculate the total elapsed time. This can be `CUMULATIVE` or `INTERVAL`.   
`workload_process/heartbeat` BETA ** _(project)_**   
Heartbeat   
`GAUGE`, `BOOL`, ``   
**[compute.googleapis.com/WorkloadProcess](https://docs.cloud.google.com/monitoring/api/resources#tag_compute.googleapis.com/WorkloadProcess)** |  _This is the heartbeat of a process that is part of a workload. A non zero value indicates the workload is alive._   
`instance_id`: The VM ID of the instance running the workload process.   
`gpu_index`: If the process is going to be utilizing a single GPU in the VM, this should be the ID of the GPU on the VM. Typically, this is the process local rank.   
`local_rank`: The local rank of the process.   
  
### connectors

Metrics from [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `connectors.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`connection/connection_status` BETA ** _(project)_**   
Connection Status   
`GAUGE`, `BOOL`, ``   
**[connectors.googleapis.com/Connection](https://docs.cloud.google.com/monitoring/api/resources#tag_connectors.googleapis.com/Connection)** |  _The current status of connection._   
`status`: Connection status.   
`connection/event_count` BETA ** _(project)_**   
Event count   
`DELTA`, `INT64`, `1`   
**[connectors.googleapis.com/Connection](https://docs.cloud.google.com/monitoring/api/resources#tag_connectors.googleapis.com/Connection)** |  _Total count of events received by a connection. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`provider`: The provider of the corresponding connector (GCP, SAP, etc.).   
`connector`: The name of the corresponding connector (pub/sub, etc.).   
`connection/event_request_sizes` BETA ** _(project)_**   
Event request size   
`DELTA`, `DISTRIBUTION`, `1`   
**[connectors.googleapis.com/Connection](https://docs.cloud.google.com/monitoring/api/resources#tag_connectors.googleapis.com/Connection)** |  _Cumulative size of request body with headers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`provider`: The provider of the corresponding connector (GCP, SAP, etc.).   
`connector`: The name of the corresponding connector (pub/sub, etc.).   
`connection/latencies` BETA ** _(project)_**   
Connection request latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[connectors.googleapis.com/Connection](https://docs.cloud.google.com/monitoring/api/resources#tag_connectors.googleapis.com/Connection)** |  _The latency of handled requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`code`: Response code.   
`service`: Connector service.   
`method`: Connector method.   
`connection/nodes` BETA ** _(project)_**   
Connection node count   
`GAUGE`, `INT64`, `1`   
**[connectors.googleapis.com/Connection](https://docs.cloud.google.com/monitoring/api/resources#tag_connectors.googleapis.com/Connection)** |  _The number of connection nodes available for a connection. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`provider`: The provider of the corresponding connector (GCP, SAP, etc.).   
`connection/request_count` BETA ** _(project)_**   
Connection request count   
`DELTA`, `INT64`, `1`   
**[connectors.googleapis.com/Connection](https://docs.cloud.google.com/monitoring/api/resources#tag_connectors.googleapis.com/Connection)** |  _The number of requests received by the connection. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`service`: Connector service.   
`method`: Connector method.   
`connection/request_sizes` BETA ** _(project)_**   
Connection request sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[connectors.googleapis.com/Connection](https://docs.cloud.google.com/monitoring/api/resources#tag_connectors.googleapis.com/Connection)** |  _The size of the request body and headers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`service`: Connector service.   
`method`: Connector method.   
`provider`: The provider of the corresponding connector (GCP, SAP, etc.).   
`connection/response_count` BETA ** _(project)_**   
Connection response count   
`DELTA`, `INT64`, `1`   
**[connectors.googleapis.com/Connection](https://docs.cloud.google.com/monitoring/api/resources#tag_connectors.googleapis.com/Connection)** |  _The number of requests fully responded and handled by the connection. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`code`: Response code.   
`service`: Connector service.   
`method`: Connector method.   
`connector_fault`: Indicates whether the connector service caused a fault.   
`connection/response_sizes` BETA ** _(project)_**   
Connection response sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[connectors.googleapis.com/Connection](https://docs.cloud.google.com/monitoring/api/resources#tag_connectors.googleapis.com/Connection)** |  _The size of the response body and headers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`code`: Response code.   
`service`: Connector service.   
`method`: Connector method.   
`connector_fault`: Indicates whether the connector service caused a fault.   
`provider`: The provider of the corresponding connector (GCP, SAP, etc.).   
`connection/state` BETA ** _(project)_**   
Connection state   
`GAUGE`, `INT64`, `1`   
**[connectors.googleapis.com/Connection](https://docs.cloud.google.com/monitoring/api/resources#tag_connectors.googleapis.com/Connection)** |  _Metadata metric tracking labels. This can be joined with other metrics to use provider,connector or connector_version labels. The value represents the number of running nodes for the connection. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`provider`: The provider of the corresponding connector (GCP, SAP, etc.).   
`connector`: The name of the corresponding connector (pub/sub, etc.).   
`connector_version`: The version of the corresponding connector.   
  
### contactcenterinsights

Metrics from [Customer Experience Insights](https://cloud.google.com/solutions/customer-engagement-ai). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `contactcenterinsights.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`analysis_count` BETA ** _(project)_**   
Analysis count   
`DELTA`, `INT64`, `1`   
**[contactcenterinsights.googleapis.com/Environment](https://docs.cloud.google.com/monitoring/api/resources#tag_contactcenterinsights.googleapis.com/Environment)** |  _Count of analyses performed._   
`response_code`: (INT64) HTTP status code of the response.   
`conversation_count` BETA ** _(project)_**   
New Conversations   
`DELTA`, `INT64`, `1`   
**[contactcenterinsights.googleapis.com/Environment](https://docs.cloud.google.com/monitoring/api/resources#tag_contactcenterinsights.googleapis.com/Environment)** |  _Count of new conversations._   
`medium`: Medium over which the conversation occurred.   
`highlighted_conversation_count` BETA ** _(project)_**   
Highlighted Conversations   
`DELTA`, `INT64`, `1`   
**[contactcenterinsights.googleapis.com/Environment](https://docs.cloud.google.com/monitoring/api/resources#tag_contactcenterinsights.googleapis.com/Environment)** |  _Count of Conversations with different highlights._   
`highlight_type`: Type of the highlight used for annotation.   
`highlight_name`: Display name of the highlight used for annotation.   
`highlight_id`: Unique id of the highlight used for annotation.   
`runtime_integration_notification_count` BETA ** _(project)_**   
Notifications from Dialogflow Runtime Integration   
`DELTA`, `INT64`, `1`   
**[contactcenterinsights.googleapis.com/Environment](https://docs.cloud.google.com/monitoring/api/resources#tag_contactcenterinsights.googleapis.com/Environment)** |  _Count of notifications from Dialogflow Runtime Integration._   
`response_code`: (INT64) HTTP status code of the response.   
`topic_classification_count` BETA ** _(project)_**   
Topic Classifications   
`DELTA`, `INT64`, `1`   
**[contactcenterinsights.googleapis.com/Environment](https://docs.cloud.google.com/monitoring/api/resources#tag_contactcenterinsights.googleapis.com/Environment)** |  _Count of topic classifications in conversations._   
`issue_model_name`: Resource name of the issue model used to classify the topic.   
`issue_name`: The issue resource name of classified topic. Empty if not successfully classified.   
`issue_display_name`: The display name of classified topic. Empty if not successfully classified.   
`is_classified`: (BOOL) Whether the conversation is classified with a topic.   
  
### container

Metrics from [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs). For newer Kubernetes metrics, see the [`kubernetes.io` metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes). Launch stages of these metrics: ALPHA

The "metric type" strings in this table must be prefixed with `container.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`container/accelerator/duty_cycle` DEPRECATED ** _(project)_**   
Accelerator duty cycle   
`GAUGE`, `INT64`, `1`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Percent of time over the past sample period (10s)during which the accelerator was actively processing. Sampled every 60 seconds._   
`make`: Make of the accelerator (e.g. nvidia)   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator (e.g. 'Tesla P100')   
`container/accelerator/memory_total` DEPRECATED ** _(project)_**   
Accelerator memory total   
`GAUGE`, `INT64`, `By`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Total accelerator memory in bytes. Sampled every 60 seconds._   
`make`: Make of the accelerator (e.g. nvidia)   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator (e.g. 'Tesla P100')   
`container/accelerator/memory_used` DEPRECATED ** _(project)_**   
Accelerator memory used   
`GAUGE`, `INT64`, `By`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Total accelerator memory allocated in bytes. Sampled every 60 seconds._   
`make`: Make of the accelerator (e.g. nvidia)   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator (e.g. 'Tesla P100')   
`container/accelerator/request` DEPRECATED ** _(project)_**   
Request accelerators   
`GAUGE`, `INT64`, `{devices}`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Number of accelerator devices requested by the container. Sampled every 60 seconds._   
`resource_name`: Name of the requested accelerator resource.   
`container/cpu/reserved_cores` DEPRECATED ** _(project)_**   
Reserved cores   
`GAUGE`, `DOUBLE`, `1`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Number of cores of CPU reserved for the container. If no core limit is set, this will be zero. Sampled every 60 seconds._  
`container/cpu/usage_time` DEPRECATED ** _(project)_**   
CPU usage   
`CUMULATIVE`, `DOUBLE`, `s{CPU}`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Cumulative CPU usage on all cores in seconds. This number divided by the elapsed time represents usage as a number of cores, regardless of any core limit that might be set. Sampled every 60 seconds._  
`container/cpu/utilization` DEPRECATED ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _The percentage of the allocated CPU that is currently in use on the container. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0), charts display the values as a percentage between 0% and 100% (or more). If no core limit is set, then this metric is not set. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._  
`container/disk/bytes_total` DEPRECATED ** _(project)_**   
Disk capacity   
`GAUGE`, `INT64`, `By`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Total number of bytes of capacity on the disk identified by label ‘device_name’. Sampled every 60 seconds._   
`device_name`: The device name for the disk (e.g. `/dev/sda1`).   
`container/disk/bytes_used` DEPRECATED ** _(project)_**   
Disk usage   
`GAUGE`, `INT64`, `By`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Total number of bytes used on the disk identified by label ‘device_name’. Sampled every 60 seconds._   
`device_name`: The device name for the disk (e.g. `/dev/sda1`).   
`container/disk/inodes_free` DEPRECATED ** _(project)_**   
Inode free   
`GAUGE`, `INT64`, `1`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Free number of inodes on the disk identified by label 'device_name'. This metric is only for the `machine` container. Sampled every 60 seconds._   
`device_name`: The device name for the disk (e.g. `/dev/sda1`).   
`container/disk/inodes_total` DEPRECATED ** _(project)_**   
Inode capacity   
`GAUGE`, `INT64`, `1`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Total number of inodes on the disk identified by label 'device_name'. This metric is only for the `machine` container. Sampled every 60 seconds._   
`device_name`: The device name for the disk (e.g. `/dev/sda1`).   
`container/memory/bytes_total` DEPRECATED ** _(project)_**   
Memory limit   
`GAUGE`, `INT64`, `By`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Memory limit of the container in bytes. Sampled every 60 seconds._  
`container/memory/bytes_used` DEPRECATED ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Memory usage in bytes, broken down by type: evictable and non-evictable. Sampled every 60 seconds._   
`memory_type`: Either `evictable` or `non-evictable`. Evictable memory is memory that can be easily reclaimed by the kernel, while non-evictable memory cannot.   
`container/memory/page_fault_count` DEPRECATED ** _(project)_**   
Page faults   
`DELTA`, `INT64`, `1`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Number of page faults, broken down by type: major and minor. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`fault_type`: Fault type - either 'major' or 'minor', with the former indicating that the page had to be loaded from disk.   
`container/pid_limit` DEPRECATED ** _(project)_**   
PID capacity   
`GAUGE`, `INT64`, `1`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _The max PID of OS on the node. This metric is only for the `machine` container. Sampled every 60 seconds._  
`container/pid_used` DEPRECATED ** _(project)_**   
PID usage   
`GAUGE`, `INT64`, `1`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _The number of running process in the OS on the node. This metric is only for the `machine` container. Sampled every 60 seconds._  
`container/uptime` DEPRECATED ** _(project)_**   
Uptime   
`CUMULATIVE`, `DOUBLE`, `s`   
**[gke_container](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container)** |  _Number of seconds since the container started. Sampled every 60 seconds._  
`quota/quota/containers_per_cluster_autopilot/exceeded` ALPHA ** _(project)_**   
Number of containers in GKE Autopilot cluster. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Number of attempts to exceed the limit on quota metric container.googleapis.com/quota/containers_per_cluster_autopilot. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/containers_per_cluster_autopilot/limit` ALPHA ** _(project)_**   
Number of containers in GKE Autopilot cluster. quota limit   
`GAUGE`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current limit on quota metric container.googleapis.com/quota/containers_per_cluster_autopilot. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/containers_per_cluster_autopilot/usage` ALPHA ** _(project)_**   
Number of containers in GKE Autopilot cluster. quota usage   
`GAUGE`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current usage on quota metric container.googleapis.com/quota/containers_per_cluster_autopilot. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/containers_per_cluster_standard/exceeded` ALPHA ** _(project)_**   
Number of containers in GKE Standard cluster. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Number of attempts to exceed the limit on quota metric container.googleapis.com/quota/containers_per_cluster_standard. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/containers_per_cluster_standard/limit` ALPHA ** _(project)_**   
Number of containers in GKE Standard cluster. quota limit   
`GAUGE`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current limit on quota metric container.googleapis.com/quota/containers_per_cluster_standard. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/containers_per_cluster_standard/usage` ALPHA ** _(project)_**   
Number of containers in GKE Standard cluster. quota usage   
`GAUGE`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current usage on quota metric container.googleapis.com/quota/containers_per_cluster_standard. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/etcd_database_size_bytes/exceeded` ALPHA ** _(project)_**   
Etcd database size. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Number of attempts to exceed the limit on quota metric container.googleapis.com/quota/etcd_database_size_bytes. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/etcd_database_size_bytes/limit` ALPHA ** _(project)_**   
Etcd database size. quota limit   
`GAUGE`, `INT64`, `By`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current limit on quota metric container.googleapis.com/quota/etcd_database_size_bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/etcd_database_size_bytes/usage` ALPHA ** _(project)_**   
Etcd database size. quota usage   
`GAUGE`, `INT64`, `By`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current usage on quota metric container.googleapis.com/quota/etcd_database_size_bytes. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/nodes_per_cluster/exceeded` ALPHA ** _(project)_**   
Number of nodes in GKE cluster. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Number of attempts to exceed the limit on quota metric container.googleapis.com/quota/nodes_per_cluster. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/nodes_per_cluster/limit` ALPHA ** _(project)_**   
Number of nodes in GKE cluster. quota limit   
`GAUGE`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current limit on quota metric container.googleapis.com/quota/nodes_per_cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/nodes_per_cluster/usage` ALPHA ** _(project)_**   
Number of nodes in GKE cluster. quota usage   
`GAUGE`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current usage on quota metric container.googleapis.com/quota/nodes_per_cluster. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/pods_per_cluster_autopilot/exceeded` ALPHA ** _(project)_**   
Number of pods in GKE Autopilot cluster. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Number of attempts to exceed the limit on quota metric container.googleapis.com/quota/pods_per_cluster_autopilot. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/pods_per_cluster_autopilot/limit` ALPHA ** _(project)_**   
Number of pods in GKE Autopilot cluster. quota limit   
`GAUGE`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current limit on quota metric container.googleapis.com/quota/pods_per_cluster_autopilot. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/pods_per_cluster_autopilot/usage` ALPHA ** _(project)_**   
Number of pods in GKE Autopilot cluster. quota usage   
`GAUGE`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current usage on quota metric container.googleapis.com/quota/pods_per_cluster_autopilot. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/pods_per_cluster_standard/exceeded` ALPHA ** _(project)_**   
Number of pods in GKE Standard cluster. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Number of attempts to exceed the limit on quota metric container.googleapis.com/quota/pods_per_cluster_standard. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/pods_per_cluster_standard/limit` ALPHA ** _(project)_**   
Number of pods in GKE Standard cluster. quota limit   
`GAUGE`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current limit on quota metric container.googleapis.com/quota/pods_per_cluster_standard. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/quota/pods_per_cluster_standard/usage` ALPHA ** _(project)_**   
Number of pods in GKE Standard cluster. quota usage   
`GAUGE`, `INT64`, `1`   
**[container.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_container.googleapis.com/Cluster)** |  _Current usage on quota metric container.googleapis.com/quota/pods_per_cluster_standard. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
  
Generated at 2026-10-14 20:24:33 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
