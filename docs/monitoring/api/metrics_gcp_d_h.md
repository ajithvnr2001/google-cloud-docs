---
url: https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h/
title: Google Cloud metrics: API prefix is D through H \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:19.651123+00:00
---

# Google Cloud metrics: API prefix is D through H  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Google Cloud metrics: API prefix is D through H Stay organized with collections  Save and categorize content based on your preferences. 

These tables list the Google Cloud metric types whose service domain name begins with the letters `d` through `h`, such as `dns.googleapis.com`. For information about other metric types, see [Google Cloud metrics overview](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

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

### databasecenter

Metrics from [Database Center](https://docs.cloud.google.com/database-center/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `databasecenter.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`resource/new_resource_count` BETA ** _(project)_**   
New database resources   
`CUMULATIVE`, `INT64`, `1`   
**[databasecenter.googleapis.com/Resource](https://docs.cloud.google.com/monitoring/api/resources#tag_databasecenter.googleapis.com/Resource)** |  _Number of new database resources._   
`product`: Type of product.   
`engine`: Type of engine.   
`version`: Version of the product.   
`resource/new_signal_count` BETA ** _(project)_**   
New database signals   
`CUMULATIVE`, `INT64`, `1`   
**[databasecenter.googleapis.com/Resource](https://docs.cloud.google.com/monitoring/api/resources#tag_databasecenter.googleapis.com/Resource)** |  _Number of signals generated for resources._   
`issue_type`: Type of signal.   
  
### dataflow

Metrics from [Dataflow](https://docs.cloud.google.com/dataflow/docs). For more information about Dataflow monitoring, see [Monitoring Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring) and [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `dataflow.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`job/active_worker_instances` GA ** _(project)_**   
Active Worker Instances   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The active number of worker instances. Streaming engine jobs only._   
`job_id`: The job id of the associated dataflow job.   
`job/aggregated_worker_utilization` GA ** _(project)_**   
Aggregated Worker Utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Aggregated worker utilization (e.g. worker CPU utilization) across the worker pool._   
`job_id`: The job id of the associated dataflow job.   
`job/archived_shuffle_data` GA ** _(project)_**   
Archived Shuffle Data   
`GAUGE`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The archived shuffle bytes incurring storage cost, at any time the job is paused._   
`job_id`: The job id of the associated Dataflow job.   
`job/backlog_bytes` GA ** _(project)_**   
Per-stage backlog in bytes   
`GAUGE`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Amount of known, unprocessed input for a stage, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`stage`: The stage of the pipeline.   
`job/backlog_elements` GA ** _(project)_**   
Per-stage backlog in elements   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Amount of known, unprocessed input for a stage, in elements. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`stage`: The stage of the pipeline.   
`job/backlogged_keys` GA ** _(project)_**   
Backlogged Keys   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The number of backlogged keys for a bottleneck stage. If a stage has backlogged keys, then it signifies its inability to process data at the required rate and the stage could be a bottleneck that slows down the overall job's progress._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/bigquery/write_count` GA ** _(project)_**   
BigQueryIO.Write Requests   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _BigQuery write requests from BigQueryIO.Write in Dataflow jobs. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`status`: The canonical response code. See: https://cloud.google.com/apis/design/errors#handling_errors.   
`job_id`: The job id of the associated Dataflow job.   
`ptransform`: The pipeline PTransform making the requests.   
`bigquery_project_id`: The project of the associated BigQuery table, view or query.   
`bigquery_dataset_id`: The BigQuery dataset of the associated BigQuery table or view.   
`bigquery_table_or_view_id`: The BigQuery table or view id.   
`job/billable_shuffle_data_processed` GA ** _(project)_**   
Billable shuffle data processed   
`GAUGE`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The billable bytes of shuffle data processed by this Dataflow job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/bundle_user_processing_latencies` GA ** _(project)_**   
Bundle user processing latencies   
`GAUGE`, `DISTRIBUTION`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Bundle user processing latencies from a particular stage. Available for jobs running on Streaming Engine. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/curr_hyperdisk_balanced_iops` GA ** _(project)_**   
Current Billable Hyperdisk Balanced IOPS   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The current billable Hyperdisk Balanced IOPS for the job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`storage_type`: The type of disk: HDD, SSD, HYPERDISK_BALANCED.   
`job/curr_hyperdisk_balanced_throughput` GA ** _(project)_**   
Current Billable Hyperdisk Balanced throughput   
`GAUGE`, `INT64`, `MBy`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The current billable Hyperdisk Balanced throughput for the job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`storage_type`: The type of disk: HDD, SSD, HYPERDISK_BALANCED.   
`job/current_num_vcpus` GA ** _(project)_**   
Current number of vCPUs in use   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The number of vCPUs currently being used by this Dataflow job. This is the current number of workers times the number of vCPUs per worker. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/current_shuffle_slots` GA ** _(project)_**   
Current shuffle slots in use   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The current shuffle slots used by this Dataflow job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/data_watermark_age` GA ** _(project)_**   
Data watermark lag   
`GAUGE`, `INT64`, `s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The age (time since event timestamp) up to which all data has been processed by the pipeline. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/disk_space_capacity` GA ** _(project)_**   
Disk Space Capacity   
`GAUGE`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The amount of persistent disk currently being allocated to all workers associated with this Dataflow job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`storage_type`: The type of persistent disk: one of [HDD, SSD].   
`job/dofn_latency_average` GA ** _(project)_**   
Average message processing time per DoFn.   
`GAUGE`, `DOUBLE`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The average processing time for a single message in a given DoFn (over the past 3 min window). Note that this includes time spent in GetData calls. Available for jobs running on Streaming Engine on the Legacy Runner. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`do_fn`: The user defined DoFn name.   
`job/dofn_latency_max` GA ** _(project)_**   
Maximum message processing time per DoFn.   
`GAUGE`, `INT64`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The maximum processing time for a single message in a given DoFn (over the past 3 min window). Note that this includes time spent in GetData calls. Available for jobs running on Streaming Engine on the Legacy Runner. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`do_fn`: The user defined DoFn name.   
`job/dofn_latency_min` GA ** _(project)_**   
Minimum message processing time per DoFn.   
`GAUGE`, `INT64`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The minimum processing time for a single message in a given DoFn (over the past 3 min window). Available for jobs running on Streaming Engine on the Legacy Runner. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`do_fn`: The user defined DoFn name.   
`job/dofn_latency_num_messages` GA ** _(project)_**   
Number of messages processed per DoFn.   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The number of messages processed by a given DoFn (over the past 3 min window). Available for jobs running on Streaming Engine on the Legacy Runner. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`do_fn`: The user defined DoFn name.   
`job/dofn_latency_total` GA ** _(project)_**   
Total message processing time per DoFn.   
`GAUGE`, `INT64`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total processing time for all messages in a given DoFn (over the past 3 min window). Note that this includes time spent in GetData calls. Available for jobs running on Streaming Engine on the Legacy Runner. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`do_fn`: The user defined DoFn name.   
`job/duplicates_filtered_out_count` GA ** _(project)_**   
Duplicate message count per stage   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The number of messages being processed by a particular stage that have been filtered out as duplicates. Available for jobs running on Streaming Engine. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/elapsed_time` GA ** _(project)_**   
Elapsed time   
`GAUGE`, `INT64`, `s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Duration that the current run of this pipeline has been in the Running state so far, in seconds. When a run completes, this stays at the duration of that run until the next run starts. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/element_count` GA ** _(project)_**   
Element count   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Number of elements added to the pcollection so far. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`pcollection`: The pipeline pcollection reporting this element count. PCollections are usually named by appending .out to the producing transform name.   
`job/elements_produced_count` GA ** _(project)_**   
Elements Produced   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The number of elements produced by each PTransform. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`pcollection`: The pipeline PCollection to which the elements were produced.   
`ptransform`: The pipeline PTransform producing the elements.   
`job/estimated_backlog_processing_time` GA ** _(project)_**   
Estimated time to process current backlog per stage   
`GAUGE`, `INT64`, `s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Estimated time (in seconds) to consume current backlog if no new data comes in and throughput stays the same. Only available for Streaming Engine jobs._   
`job_id`: The ID of the current run of this pipeline.   
`stage`: The stage of the pipeline.   
`job/estimated_byte_count` GA ** _(project)_**   
Estimated byte count   
`GAUGE`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _An estimated number of bytes added to the pcollection so far. Dataflow calculates the average encoded size of elements in a pcollection and mutiplies it by the number of elements. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`pcollection`: The pipeline pcollection reporting this estimated byte count. PCollections are usually named by appending .out to the producing transform name.   
`job/estimated_bytes_active` GA ** _(project)_**   
Active Size   
`GAUGE`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Estimated number of bytes active in this stage of the job._   
`job_id`: The ID of the current run of this pipeline.   
`stage`: The stage of the pipeline.   
`job/estimated_bytes_consumed_count` GA ** _(project)_**   
Throughput   
`DELTA`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Estimated number of bytes consumed by the stage of this job._   
`job_id`: The ID of the current run of this pipeline.   
`stage`: The stage of the pipeline.   
`job/estimated_bytes_produced_count` GA ** _(project)_**   
Estimated Bytes Produced   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The estimated total byte size of elements produced by each PTransform. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`pcollection`: The pipeline PCollection to which the elements were produced.   
`ptransform`: The pipeline PTransform producing the elements.   
`job/estimated_timer_backlog_processing_time` GA ** _(project)_**   
Estimated time (in seconds) for timers to complete.   
`GAUGE`, `INT64`, `s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Estimated time (in seconds) for timers to complete. Only available for Streaming Engine jobs._   
`job_id`: The ID of the current run of this pipeline.   
`stage`: The stage of the pipeline.   
`job/gpu_memory_utilization` GA ** _(project)_**   
GPU memory utilization   
`GAUGE`, `INT64`, `%`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Percent of time over the past sample period during which global (device) memory was being read or written._   
`job_id`: The ID of the current run of this pipeline.   
`job/gpu_utilization` GA ** _(project)_**   
GPU utilization   
`GAUGE`, `INT64`, `%`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Percent of time over the past sample period during which one or more kernels was executing on the GPU._   
`job_id`: The ID of the current run of this pipeline.   
`job/high_availability_mode` BETA ** _(project)_**   
High Availability Mode   
`GAUGE`, `BOOL`, ``   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Whether a job is protected by the High Availability feature._   
`job_id`: The ID of the current run of this pipeline.   
`status`: The current High Availability status of the job.   
`job/horizontal_worker_scaling` GA ** _(project)_**   
Horizontal Worker Scaling   
`GAUGE`, `BOOL`, ``   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _A boolean value that indicates what kind of horizontal scaling direction which the autoscaler recommended and rationale behind it. A true metric output means a scaling decision is made and a false metric output means the corresponding scaling is not taking effect._   
`job_id`: The job id of the associated dataflow job.   
`rationale`: Horizontal worker scaling rationale: one of [Waiting for the signals to stabilize, Hit non-resource related limit, Low backlog and high worker utilization, High worker utilization, Low worker utilization, High backlog]   
`direction`: Horizontal worker scaling direction: one of [Upscale number of workers, Downscale number of workers, No change in scaling and signals are not stable, No change in scaling and signals are stable]   
`job/is_bottleneck` GA ** _(project)_**   
Bottleneck Status and Likely Causes   
`GAUGE`, `BOOL`, ``   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Whether a specific Dataflow pipeline stage is a bottleneck, along with its bottleneck kind and likely cause. See the troubleshooting guide https://cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks for more details._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`likely_cause`: The most probable reason for the stage being identified as a bottleneck.   
`bottleneck_kind`: The kind of bottleneck the stage is experiencing.   
`job/is_failed` GA ** _(project)_**   
Failed   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _A value of 1 indicates that the job has failed. This metric isn't recorded for jobs that fail before launch. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._  
`job/longest_processing_time` GA ** _(project)_**   
Longest Processing Times   
`GAUGE`, `INT64`, `us`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Top 10 oldest active operation times grouped by user worker. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`user_worker_id`: The id of the user worker of the associated dataflow job.   
`job/max_worker_instances_limit` GA ** _(project)_**   
Autoscaling worker instances ceiling   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The maximum number of workers autoscaling is allowed to request._   
`job_id`: The job id of the associated dataflow job.   
`job/memory_capacity` GA ** _(project)_**   
Memory Capacity   
`GAUGE`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The amount of memory currently being allocated to all workers associated with this Dataflow job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/min_worker_instances_limit` GA ** _(project)_**   
Autoscaling worker instances flooring   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The minimum number of workers autoscaling is allowed to request._   
`job_id`: The job id of the associated dataflow job.   
`job/oldest_active_message_age` GA ** _(project)_**   
Oldest active message processing time per DoFn.   
`GAUGE`, `INT64`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _How long the oldest active message in a DoFn has been processing for. Available for jobs running on Streaming Engine on the Legacy Runner. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`do_fn`: The user defined DoFn name.   
`job/per_stage_data_watermark_age` GA ** _(project)_**   
Per-stage data watermark lag   
`GAUGE`, `INT64`, `s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The age (time since event timestamp) up to which all data has been processed by this stage of the pipeline. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`stage`: The stage of the pipeline.   
`job/per_stage_system_lag` GA ** _(project)_**   
Per-stage system lag   
`GAUGE`, `INT64`, `s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The current maximum duration that an item of data has been processing or awaiting processing in seconds, per pipeline stage. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`stage`: The stage of the pipeline.   
`job/processing_parallelism_keys` GA ** _(project)_**   
The approximate number of parallel processing keys   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Approximate number of keys in use for data processing for each stage. Processing for any given key is serialized, so the total number of keys for a stage represents the maximum available parallelism at that stage. Available for jobs running on Streaming Engine. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/pubsub/late_messages_count` GA ** _(project)_**   
Pub/Sub Late Messages Count   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The number of messages from Pub/Sub with timestamp older than the estimated watermark. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The job id of the associated dataflow job.   
`stage`: The computation stage consuming from Pub/Sub.   
`subscription_project_id`: The project of the associated Pub/Sub subscription.   
`subscription_id`: The id of the associated Pub/Sub subscription.   
`topic_project_id`: The project of the associated Pub/Sub topic.   
`topic_id`: The id of the associated Pub/Sub topic.   
`job/pubsub/published_messages_count` GA ** _(project)_**   
Pub/Sub Published Messages Count   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The number of Pub/Sub messages published broken down by topic and status. Sampled every 60 seconds. After sampling, data is not visible for up to 660 seconds._   
`job_id`: The job id of the associated dataflow job.   
`stage`: The computation stage consuming from Pub/Sub.   
`topic_project_id`: The project of the associated Pub/Sub topic.   
`topic_id`: The id of the associated Pub/Sub topic.   
`status`: Status code string that indicates the result of the message, one of [OK, DROPPED].   
`job/pubsub/pulled_message_ages` GA ** _(project)_**   
Pub/Sub Pulled Message Ages   
`GAUGE`, `DISTRIBUTION`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The distribution of pulled but unacked Pub/Sub message ages. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_id`: The job id of the associated dataflow job.   
`stage`: The computation stage consuming from pubsub.   
`subscription_project_id`: The project of the associated Pub/Sub subscription.   
`subscription_id`: The id of the associated Pub/Sub subscription.   
`topic_project_id`: The project of the associated Pub/Sub topic.   
`topic_id`: The id of the associated Pub/Sub topic.   
`job/pubsub/read_count` GA ** _(project)_**   
PubsubIO.Read requests from Dataflow jobs   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Pub/Sub Pull Requests. For Streaming Engine, this metric is deprecated. See the "Using the Dataflow monitoring interface" page for upcoming changes. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`status`: The canonical response code. See: https://cloud.google.com/apis/design/errors#handling_errors.   
`job_id`: The job id of the associated Dataflow job.   
`ptransform`: The pipeline PTransform making the requests.   
`subscription_project_id`: The project of the associated Pub/Sub subscription.   
`subscription_id`: The id of the associated Pub/Sub subscription.   
`topic_project_id`: The project of the associated Pub/Sub topic.   
`topic_id`: The id of the associated Pub/Sub topic.   
`job/pubsub/read_latencies` GA ** _(project)_**   
Pub/Sub Pull Request Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Pub/Sub Pull request latencies from PubsubIO.Read in Dataflow jobs. For Streaming Engine, this metric is deprecated. See the "Using the Dataflow monitoring interface" page for upcoming changes. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`ptransform`: The pipeline PTransform making the requests.   
`subscription_project_id`: The project of the associated Pub/Sub subscription.   
`subscription_id`: The id of the associated Pub/Sub subscription.   
`topic_project_id`: The project of the associated Pub/Sub topic.   
`topic_id`: The id of the associated Pub/Sub topic.   
`job/pubsub/streaming_pull_connection_status` GA ** _(project)_**   
Percentage of active/terminated Streaming Pull connections   
`GAUGE`, `DOUBLE`, `%`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Percentage of all Streaming Pull connections that are either active (OK status) or terminated because of an error (non-OK status). When a connection is terminated, Dataflow will wait some time before attempting to re-connect. For Streaming Engine only. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The canonical response code for the error. See: https://cloud.google.com/apis/design/errors#handling_errors.   
`job_id`: The job id of the associated dataflow job.   
`ptransform`: The pipeline PTransform making the requests.   
`subscription_project_id`: The project of the associated Pub/Sub subscription.   
`subscription_id`: The id of the associated Pub/Sub subscription.   
`topic_project_id`: The project of the associated Pub/Sub topic.   
`topic_id`: The id of the associated Pub/Sub topic.   
`job/pubsub/timestamp_events` GA ** _(project)_**   
Pub/Sub Event Timestamp Status   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The number of Pub/Sub messages with event timestamps broken down by topic and status. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_id`: The job id of the associated dataflow job.   
`stage`: The computation stage consuming from Pub/Sub.   
`topic_project_id`: The project of the associated Pub/Sub topic.   
`topic_id`: The id of the associated Pub/Sub topic.   
`status`: Status code string that indicates the result of parsing the event timestamp.   
`job/pubsub/write_count` GA ** _(project)_**   
Pub/Sub Publish Requests   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Pub/Sub Publish requests from PubsubIO.Write in Dataflow jobs. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`status`: The canonical response code. See: https://cloud.google.com/apis/design/errors#handling_errors.   
`job_id`: The job id of the associated Dataflow job.   
`ptransform`: The pipeline PTransform making the requests.   
`topic_project_id`: The project of the associated Pub/Sub topic.   
`topic_id`: The id of the associated Pub/Sub topic.   
`job/pubsub/write_latencies` GA ** _(project)_**   
Pub/Sub Publish Request Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Pub/Sub Publish request latencies from PubsubIO.Write in Dataflow jobs. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`ptransform`: The pipeline PTransform making the requests.   
`topic_project_id`: The project of the associated Pub/Sub topic.   
`topic_id`: The id of the associated Pub/Sub topic.   
`job/recommended_parallelism` GA ** _(project)_**   
Recommended Parallelism   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The recommended parallelism for a stage to reduce bottlenecking. If this is a source stage, then the parallelism is a consequence of source partition count and the source may need to be repartitioned to increase parallelism._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/status` GA ** _(project)_**   
Status   
`GAUGE`, `STRING`, ``   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Current state of this pipeline (e.g.: RUNNING, DONE, CANCELLED, FAILED, ...). Not reported while the pipeline is not running. Sampled every 60 seconds. After sampling, data is not visible for up to 360 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/streaming_engine/key_processing_availability` GA ** _(project)_**   
Current processing key-range availability   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Percentage of streaming processing keys that are assigned to workers and available to perform work. Work for unavailable keys will be deferred until keys are available._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/streaming_engine/persistent_state/read_bytes_count` GA ** _(project)_**   
Storage bytes read   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Storage bytes read by a particular stage. Available for jobs running on Streaming Engine. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/streaming_engine/persistent_state/stored_bytes` GA ** _(project)_**   
Current persistence state usage   
`GAUGE`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Current bytes stored in persistent state for the job._   
`job_id`: The job id of the associated Dataflow job.   
`job/streaming_engine/persistent_state/write_bytes_count` GA ** _(project)_**   
Storage bytes written   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Storage bytes written by a particular stage. Available for jobs running on Streaming Engine. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/streaming_engine/persistent_state/write_latencies` GA ** _(project)_**   
Storage write latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Storage write latencies from a particular stage. Available for jobs running on Streaming Engine. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/streaming_engine/stage_end_to_end_latencies` GA ** _(project)_**   
Per stage end to end latencies.   
`GAUGE`, `DISTRIBUTION`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Distribution of time spent by streaming engine in each stage of the pipeline. This time includes shuffling messages, queueing them for processing, processing, queueing for persistent state write, and the write itself. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The job id of the associated Dataflow job, for example, 2023-01-01-_01_02_03-45678987654.   
`stage`: The stage of the pipeline, for example, F0.   
`job/system_lag` GA ** _(project)_**   
System lag   
`GAUGE`, `INT64`, `s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The current maximum duration that an item of data has been processing or awaiting processing, in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/target_worker_instances` GA ** _(project)_**   
Target Worker Instances   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The desired number of worker instances._   
`job_id`: The job id of the associated dataflow job.   
`job/thread_time` GA ** _(project)_**   
Thread Time   
`DELTA`, `INT64`, `ms`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Estimated time in milliseconds spent running in the function of the ptransform totaled across threads on all workers of the job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`ptransform`: The pipeline PTransform running the function.   
`function`: The function name, one of [start_bundle, process_element, process_timers, split_source, finish_bundle].   
`job/timers_pending_count` GA ** _(project)_**   
Timers pending count per stage   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The number of timers pending in a particular stage. Available for jobs running on Streaming Engine. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/timers_processed_count` GA ** _(project)_**   
Timers processed count per stage   
`DELTA`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The number of timers completed by a particular stage. Available for jobs running on Streaming Engine. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`stage`: The stage of the pipeline.   
`job/total_billable_shuffle_archived_data_time` GA ** _(project)_**   
Total Billable Shuffle Archived Data Time   
`GAUGE`, `INT64`, `GBy.s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total gigabyte seconds of shuffle archived data. This shows the cumulative cost accrued from all past sessions where the job was paused._   
`job_id`: The job id of the associated Dataflow job.   
`job/total_dcu_usage` GA ** _(project)_**   
Total DCU usage   
`CUMULATIVE`, `DOUBLE`, `{dcu}`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total amount of DCUs (Data Compute Unit) used by the Dataflow job since it was launched._   
`job_id`: The job id of the associated Dataflow job, for example, 2023-04-05_19_41_09-14297402485873831817.   
`job/total_hyperdisk_balanced_iops_time` GA ** _(project)_**   
Total Billable Hyperdisk Balanced IOPS time   
`GAUGE`, `INT64`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total billable IOPS-seconds for Hyperdisk Balanced disks in the job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`storage_type`: The type of disk: HDD, SSD, HYPERDISK_BALANCED.   
`job/total_hyperdisk_balanced_throughput_time` GA ** _(project)_**   
Total Billable Hyperdisk Balanced throughput time   
`GAUGE`, `INT64`, `MBy.s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total billable throughput-seconds for Hyperdisk Balanced disks in the job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`storage_type`: The type of disk: HDD, SSD, HYPERDISK_BALANCED.   
`job/total_memory_usage_time` GA ** _(project)_**   
Total memory usage time   
`GAUGE`, `INT64`, `GBy.s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total GB seconds of memory allocated to this Dataflow job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/total_pd_usage_time` GA ** _(project)_**   
Total PD usage time   
`GAUGE`, `INT64`, `GBy.s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total GB seconds for all persistent disk used by all workers associated with this Dataflow job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`storage_type`: The type of disk: HDD, SSD, HYPERDISK_BALANCED.   
`job/total_secu_usage` GA ** _(project)_**   
Total SECU usage   
`GAUGE`, `DOUBLE`, `{secu}`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total amount of SECUs (Streaming Engine Compute Unit) used by the Dataflow job since it was launched. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The job id of the associated Dataflow job, for example, 2023-04-05_19_41_09-14297402485873831817.   
`job/total_shuffle_data_processed` GA ** _(project)_**   
Total shuffle data processed   
`GAUGE`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total bytes of shuffle data processed by this Dataflow job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/total_streaming_data_processed` GA ** _(project)_**   
Total streaming data processed   
`GAUGE`, `INT64`, `By`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total bytes of streaming data processed by this Dataflow job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/total_vcpu_time` GA ** _(project)_**   
Total vCPU time   
`GAUGE`, `INT64`, `s`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _The total vCPU seconds used by this Dataflow job. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The ID of the current run of this pipeline.   
`job/user_counter` GA ** _(project)_**   
User Counter   
`GAUGE`, `DOUBLE`, `1`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _A user-defined counter metric. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`metric_name`: The name provided by the user for this counter.   
`job_id`: The ID of the current run of this pipeline.   
`ptransform`: The pipeline PTransform reporting this counter value.   
`job/worker_utilization_hint` GA ** _(project)_**   
Worker Utilization Hint   
`GAUGE`, `DOUBLE`, `%`   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Worker utilization hint for autoscaling. This hint value is configured by the customers and defines a target worker CPU utilization range thus influencing scaling aggressiveness._   
`job_id`: The job id of the associated dataflow job.   
`job/worker_utilization_hint_is_actively_used` GA ** _(project)_**   
Worker Utilization Hint Is Actively Used   
`GAUGE`, `BOOL`, ``   
**[dataflow_job](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job)** |  _Reports whether or not the worker utilization hint is actively used by the horizontal autoscaling policy._   
`job_id`: The job id of the associated dataflow job.   
`quota/region_endpoint_shuffle_slot/exceeded` GA ** _(project)_**   
Shuffle slots per region per endpoint quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dataflow.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow.googleapis.com/Project)** |  _Number of attempts to exceed the limit on quota metric dataflow.googleapis.com/region_endpoint_shuffle_slot. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint`: The shuffle endpoint.   
`quota/region_endpoint_shuffle_slot/limit` GA ** _(project)_**   
Shuffle slots per region per endpoint quota limit   
`GAUGE`, `INT64`, `1`   
**[dataflow.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow.googleapis.com/Project)** |  _Current limit on quota metric dataflow.googleapis.com/region_endpoint_shuffle_slot. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint`: The shuffle endpoint.   
`quota/region_endpoint_shuffle_slot/usage` GA ** _(project)_**   
Shuffle slots per region per endpoint quota usage   
`GAUGE`, `INT64`, `1`   
**[dataflow.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow.googleapis.com/Project)** |  _Current usage on quota metric dataflow.googleapis.com/region_endpoint_shuffle_slot. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`endpoint`: The shuffle endpoint.   
`worker/accelerator/gpu/clock/device_memory_current` BETA ** _(project)_**   
GPU Current Memory Clock Frequency   
`GAUGE`, `INT64`, `MHz`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The current frequency of the memory clock._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/clock/device_memory_max` BETA ** _(project)_**   
GPU Max Memory Clock Frequency   
`GAUGE`, `INT64`, `MHz`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The max frequency of the memory clock._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/clock/device_sm_current` BETA ** _(project)_**   
GPU Current SM Clock Frequency   
`GAUGE`, `INT64`, `MHz`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The current frequency of the SM clock._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/clock/device_sm_max` BETA ** _(project)_**   
GPU Max SM Clock Frequency   
`GAUGE`, `INT64`, `MHz`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The max frequency of the SM clock._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/memory/device_limit` BETA ** _(project)_**   
GPU Total Memory   
`GAUGE`, `INT64`, `MiB`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Total available memory on the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/memory/device_usage` BETA ** _(project)_**   
GPU Memory Usage   
`GAUGE`, `INT64`, `MiB`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Memory in use on the device, including reserved memory._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/memory/ecc/volatile/device_correctable_total` BETA ** _(project)_**   
GPU total volatile correctable ECC errors   
`GAUGE`, `INT64`, `count`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The total number of correctable (single-bit) ECC errors on the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/memory/ecc/volatile/device_uncorrectable_total` BETA ** _(project)_**   
GPU total volatile uncorrectable ECC errors   
`GAUGE`, `INT64`, `count`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The total number of uncorrectable (double-bit) ECC errors on the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/nvlink/device_read` BETA ** _(project)_**   
GPU NVLink Rx   
`GAUGE`, `INT64`, `MiB/s`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The rate that data is read by the device from other GPUs on the host._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/nvlink/device_transfer` BETA ** _(project)_**   
GPU NVLink Tx   
`GAUGE`, `INT64`, `MiB/s`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The rate that data is transferred from the device to other GPUs on the host._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/pcie/device_read` BETA ** _(project)_**   
GPU PCIe Rx   
`GAUGE`, `INT64`, `MiB/s`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The rate that data is read by the device from the host over PCIe._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/pcie/device_transfer` BETA ** _(project)_**   
GPU PCIe Tx   
`GAUGE`, `INT64`, `MiB/s`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The rate that data is transmitted from the device to the host over PCIe._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/power/device_limit` BETA ** _(project)_**   
GPU Power Limit   
`GAUGE`, `DOUBLE`, `W`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The power limit of the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/power/device_usage` BETA ** _(project)_**   
GPU Power Usage   
`GAUGE`, `DOUBLE`, `W`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The current power draw of the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/temperature/device_current` BETA ** _(project)_**   
GPU Current Temperature   
`GAUGE`, `INT64`, `C`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The current temperature of the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/temperature/device_max_op` BETA ** _(project)_**   
GPU Max Operating Temperature   
`GAUGE`, `INT64`, `C`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The max operating temperature of the GPU, above which the GPU will try to cool itself to below this temperature._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/temperature/device_shutdown` BETA ** _(project)_**   
GPU Shutdown Temperature   
`GAUGE`, `INT64`, `C`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The temperature at which the GPU will shut down._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/temperature/device_slowdown` BETA ** _(project)_**   
GPU Slowdown Temperature   
`GAUGE`, `INT64`, `C`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The temperature at which the GPU will start throttling._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/utilization/device_fp16_pipe_activity` BETA ** _(project)_**   
GPU FP16 Pipe Activity   
`GAUGE`, `INT64`, `%`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Percent of time that the FP16 Pipe was active on the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/utilization/device_fp32_pipe_activity` BETA ** _(project)_**   
GPU FP32 Pipe Activity   
`GAUGE`, `INT64`, `%`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Percent of time that the FP32 Pipe was active on the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/utilization/device_fp64_pipe_activity` BETA ** _(project)_**   
GPU FP64 Pipe Activity   
`GAUGE`, `INT64`, `%`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Percent of time that the FP64 Pipe was active on the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/utilization/device_kernel_runtime` BETA ** _(project)_**   
GPU Kernel Running Percentage   
`GAUGE`, `INT64`, `%`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Percent of time over the last sample period during which at least one kernel was executing on the GPU._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/utilization/device_memory_access` BETA ** _(project)_**   
GPU Device Memory Access Percentage   
`GAUGE`, `INT64`, `%`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Percent of time over the last sample period during which global device memory was being read or written._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/utilization/device_sm_activity` BETA ** _(project)_**   
GPU SM Activity   
`GAUGE`, `INT64`, `%`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Percent of time a warp was active on an SM averaged across all SMs on the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/utilization/device_sm_occupancy` BETA ** _(project)_**   
GPU SM Occupancy   
`GAUGE`, `INT64`, `%`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Percent of the active warps on the device relative to the max._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/accelerator/gpu/utilization/device_tensor_pipe_activity` BETA ** _(project)_**   
GPU Tensor Pipe Activity   
`GAUGE`, `INT64`, `%`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Percent of time that the Tensor Pipe was active on the device._   
`device_uuid`: The unique identifier of the GPU.   
`device_number`: (INT64) The zero-indexed number of the GPU relative to other GPUs on the machine.   
`device_model`: The model name of the GPU.   
`worker/memory/bytes_used` GA ** _(project)_**   
Container memory used   
`GAUGE`, `INT64`, `By`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The memory usage in bytes by a particular container instance on a Dataflow worker._   
`container`: Container instance name, such as "java-streaming" or "harness".   
`worker/memory/container_limit` GA ** _(project)_**   
Container memory limit   
`GAUGE`, `INT64`, `By`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _Maximum RAM size in bytes available to a particular container instance on a Dataflow worker._   
`container`: Container instance name, such as "java-streaming" or "harness".   
`worker/memory/total_limit` GA ** _(project)_**   
Worker memory limit   
`GAUGE`, `INT64`, `By`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _RAM size in bytes available to a Dataflow worker._  
`worker/time_per_active_work_item_state` GA ** _(project)_**   
Time Per Active Work Item State   
`GAUGE`, `DISTRIBUTION`, `ms`   
**[dataflow_worker](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_worker)** |  _The distributions of time spent in each state of the active work item. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._   
`job_id`: The job id of the associated Dataflow job.   
`state`: The state of the associated distribution for the active work item.   
`stage`: The stage of the associated distribution for the active work item.   
  
### datafusion

Metrics from [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `datafusion.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`instance/v2/api_request_count` BETA ** _(project)_**   
CDAP REST API Requests Received   
`CUMULATIVE`, `INT64`, `{request}`   
**[datafusion.googleapis.com/InstanceV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV2)** |  _Cumulative count of REST API requests received by a service in the backend. Sampled every 120 seconds._   
`service`: The name of the service receiving the request.   
`handler`: The name of the handler handling the request.   
`method`: The name of the method that is called within the handler.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v2/api_response_count` BETA ** _(project)_**   
CDAP REST API Responses   
`CUMULATIVE`, `INT64`, `{request}`   
**[datafusion.googleapis.com/InstanceV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV2)** |  _Cumulative count of REST API responses sent by a service in the backend. Sampled every 120 seconds._   
`service`: The name of the service serving the request.   
`handler`: The name of the handler handling the request.   
`method`: The name of the method that is called within the handler.   
`response_code`: The response code generated from the request.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v2/authorization_check_count` BETA ** _(project)_**   
Authorization Check Count   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV2)** |  _Cumulative count of authorization checks made by the access enforcer. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`type`: Type of authorization check performed.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v2/authorization_check_time` BETA ** _(project)_**   
Authorization Check Time   
`GAUGE`, `INT64`, `ms`   
**[datafusion.googleapis.com/InstanceV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV2)** |  _Latency of authorization checks made by the access enforcer. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`type`: Type of authorization check performed.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v2/concurrent_pipelines_launched` BETA ** _(project)_**   
Concurrent Pipeline Launches Count   
`GAUGE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV2)** |  _Count of pipelines in provisioning/starting state. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v2/concurrent_pipelines_running` BETA ** _(project)_**   
Concurrent Pipelines Running Count   
`GAUGE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV2)** |  _Count of concurrent pipelines running. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v2/draft_pipelines` BETA ** _(project)_**   
Draft pipeline count   
`GAUGE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV2)** |  _Number of draft pipelines. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v2/namespaces` BETA ** _(project)_**   
Namespace count   
`GAUGE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV2)** |  _Number of namespaces. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v2/pipelines` BETA ** _(project)_**   
Deployed pipeline count   
`GAUGE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV2)** |  _Number of deployed pipelines. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`maintenance_window_enabled`: Whether maintenance window is enabled for the instance.   
`instance/v2/service_available` BETA ** _(project)_**   
Service status   
`GAUGE`, `BOOL`, `1`   
**[datafusion.googleapis.com/InstanceV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV2)** |  _CDAP service availability. Sampled every 120 seconds._   
`service`: The name of the service.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v3/api_request_count` BETA ** _(project)_**   
CDAP REST API Requests Received   
`CUMULATIVE`, `INT64`, `{request}`   
**[datafusion.googleapis.com/InstanceV3](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV3)** |  _Cumulative count of REST API requests received by a service in the backend. Sampled every 120 seconds._   
`service`: The name of the service receiving the request.   
`handler`: The name of the handler handling the request.   
`method`: The name of the method that is called within the handler.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v3/api_response_count` BETA ** _(project)_**   
CDAP REST API Responses   
`CUMULATIVE`, `INT64`, `{request}`   
**[datafusion.googleapis.com/InstanceV3](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV3)** |  _Cumulative count of REST API responses sent by a service in the backend. Sampled every 120 seconds._   
`service`: The name of the service serving the request.   
`handler`: The name of the handler handling the request.   
`method`: The name of the method that is called within the handler.   
`response_code`: The response code generated from the request.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v3/authorization_check_count` BETA ** _(project)_**   
Authorization Check Count   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV3](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV3)** |  _Count of authorization checks made by the access enforcer. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`type`: Type of authorization check performed.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v3/authorization_check_time` BETA ** _(project)_**   
Authorization Check Time   
`GAUGE`, `INT64`, `ms`   
**[datafusion.googleapis.com/InstanceV3](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV3)** |  _Latency of authorization checks made by the access enforcer. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`type`: Type of authorization check performed.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v3/concurrent_pipelines_launched` BETA ** _(project)_**   
Concurrent Pipeline Launches Count   
`GAUGE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV3](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV3)** |  _Count of pipelines in provisioning/starting state. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v3/concurrent_pipelines_running` BETA ** _(project)_**   
Concurrent Pipelines Running Count   
`GAUGE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV3](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV3)** |  _Count of concurrent pipelines running. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v3/draft_pipelines` BETA ** _(project)_**   
Draft pipeline count   
`GAUGE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV3](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV3)** |  _Number of draft pipelines. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v3/namespaces` BETA ** _(project)_**   
Namespace count   
`GAUGE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV3](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV3)** |  _Number of namespaces. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`instance/v3/pipelines` BETA ** _(project)_**   
Deployed pipeline count   
`GAUGE`, `INT64`, `1`   
**[datafusion.googleapis.com/InstanceV3](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV3)** |  _Number of deployed pipelines. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`maintenance_window_enabled`: Whether maintenance window is enabled for the instance.   
`instance/v3/service_available` BETA ** _(project)_**   
Service status   
`GAUGE`, `BOOL`, `1`   
**[datafusion.googleapis.com/InstanceV3](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/InstanceV3)** |  _CDAP service availability. Sampled every 120 seconds._   
`service`: The name of the service.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/engine_bytes_billed_count` BETA ** _(project)_**   
BigQuery Pushdown: bytes billed by BigQuery jobs.   
`CUMULATIVE`, `INT64`, `By`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative bytes billed by BigQuery jobs. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/engine_bytes_processed_count` BETA ** _(project)_**   
BigQuery Pushdown: bytes processed by BigQuery jobs.   
`CUMULATIVE`, `INT64`, `By`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative bytes processed by BigQuery jobs. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/engine_slot_count` BETA ** _(project)_**   
BigQuery Pushdown: Cumulative slot usage by BigQuery jobs in milliseconds.   
`CUMULATIVE`, `INT64`, `ms`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: Cumulative slot usage by BigQuery jobs in milliseconds. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/records_in_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative count of records entering a pipeline.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative count of records entering a pipeline. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/records_out_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative count of records leaving a pipeline.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative count of records leaving a pipeline. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/records_pulled_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative count of records pulled from the BQ engine in the pipeline.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative count of records pulled from the BQ engine in the pipeline. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/records_pushed_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative count of records pushed to engine in the pipeline.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative count of records pushed to engine in the pipeline. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/stages_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative number of stages in the pipeline.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative number of stages in the pipeline. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/stages_join_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative number of stages in the pipeline that are of type join.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative number of stages in the pipeline of type join. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/stages_pulled_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative number of stages in the pipeline that have records pulled from the BQ engine.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative number of stages in the pipeline that have records pulled from the BQ engine. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/stages_pushed_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative number of stages in the pipeline that have records pushed into the BQ engine.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative number of stages in the pipeline that have records pushed into the BQ engine. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/stages_read_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative number of read stages in the pipeline.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative number of read stages in the pipeline. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/stages_spark_pulled_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative number of stages in the pipeline that have records pulled from the Spark engine.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative number of stages in the pipeline that have records pulled from the Spark engine. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/stages_spark_pushed_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative number of stages in the pipeline that have records pushed into the Spark engine.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative number of stages in the pipeline that have records pushed into the Spark engine. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/stages_transform_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative number of stages in the pipeline that are of type transform.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative number of stages in the pipeline of type transform. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/bqpushdown/stages_write_count` BETA ** _(project)_**   
BigQuery Pushdown: cumulative number of write stages in the pipeline.   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _BigQuery Pushdown: cumulative number of write stages in the pipeline. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/dataproc/api_request_count` BETA ** _(project)_**   
Dataproc API Requests   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Cumulative count of Dataproc API requests. Sampled every 120 seconds._   
`provisioner`: Name of the provisioner.   
`method`: Name of the method that is called.   
`response_code`: The response code generated from the request.   
`region`: The region that the Dataproc cluster is hosted in.   
`launch_mode`: Launch mode for the Dataproc job.   
`image_version`: The dataproc image version used.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/dataproc/provisioning_latency` BETA ** _(project)_**   
Provisioning Latency   
`GAUGE`, `INT64`, `s`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Dataproc cluster provisioning latency. Sampled every 120 seconds._   
`provisioner`: Name of the provisioner.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/pipeline_duration` BETA ** _(project)_**   
Pipeline Run Time   
`GAUGE`, `INT64`, `s`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Pipeline run time. Sampled every 120 seconds._   
`complete_state`: The state in which the run completed.   
`program`: Name of the program.For eg,"DataPipelineWorkflow" in case of batch pipeline.   
`provisioner`: Name of the provisioner.   
`cluster_state`: The state of the cluster when the run completed.   
`compute_profile_id`: Name of compute profile used to run the pipeline.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/pipeline_start_latency` BETA ** _(project)_**   
Pipeline Start Latency   
`GAUGE`, `INT64`, `s`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Pipeline starting latency. Sampled every 120 seconds._   
`program`: Name of the program.For eg,"DataPipelineWorkflow" in case of batch pipeline.   
`provisioner`: Name of the provisioner.   
`cluster_state`: The state of the cluster when the run completed.   
`compute_profile_id`: Name of compute profile used to run the pipeline.   
`complete_state`: The state in which the run completed.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/plugin/incoming_records_count` BETA ** _(project)_**   
Plugin Records Processed In   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Cumulative count of records entering a plugin. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`stage_name`: The name of the node in pipeline which represents the plugin.   
`pipeline/v2/plugin/outgoing_records_count` BETA ** _(project)_**   
Plugin Records Processed Out   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Cumulative count of records exiting a plugin. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`stage_name`: The name of the node in pipeline which represents the plugin.   
`pipeline/v2/preview_duration` BETA ** _(project)_**   
Pipeline Preview Run time   
`GAUGE`, `INT64`, `s`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Pipeline Preview Run Time. Sampled every 120 seconds._   
`complete_state`: The state in which the run completed.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/read_bytes_count` BETA ** _(project)_**   
Pipeline Bytes Read   
`CUMULATIVE`, `INT64`, `By`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Cumulative count of bytes read by a pipeline. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/runs_completed_count` BETA ** _(project)_**   
Pipeline Run Status   
`CUMULATIVE`, `INT64`, `1`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Cumulative count of pipelines that have completed. Sampled every 120 seconds._   
`complete_state`: The state in which the run completed.   
`previous_state`: The state from which the run transitioned to any of the completed state.   
`program`: Name of the program.For eg,"DataPipelineWorkflow" in case of batch pipeline.   
`provisioner`: Name of the provisioner.   
`cluster_state`: The state of the cluster when the run completed.   
`compute_profile_id`: Name of compute profile used to run the pipeline.   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/shuffle_bytes_count` BETA ** _(project)_**   
Pipeline Bytes Shuffled   
`CUMULATIVE`, `INT64`, `By`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Cumulative count of bytes shuffled in a pipeline. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
`pipeline/v2/write_bytes_count` BETA ** _(project)_**   
Pipeline Bytes Written   
`CUMULATIVE`, `INT64`, `By`   
**[datafusion.googleapis.com/PipelineV2](https://docs.cloud.google.com/monitoring/api/resources#tag_datafusion.googleapis.com/PipelineV2)** |  _Cumulative count of bytes written by a pipeline. Sampled every 120 seconds._   
`enable_rbac`: Whether role-based access control is enabled for the instance.   
`private_service_connect_enabled`: Whether private service connect is enabled for the instance.   
  
### datamigration

Metrics from [Database Migration Service](https://docs.cloud.google.com/database-migration/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `datamigration.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`migration_job/fulldump_progress_percentage` GA ** _(project)_**   
Fulldump progress percentage   
`GAUGE`, `DOUBLE`, `%`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Progress percentage of the initial fulldump of the migration job.. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`migration_job/fulldump_progress_percentage_per_object` GA ** _(project)_**   
Fulldump progress percentage per object   
`GAUGE`, `DOUBLE`, `%`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Progress percentage of the initial fulldump of a single table in a migration job. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`schema`: The schema associated with this metric.   
`table`: The table associated with this metric.   
`migration_job/initial_sync_complete` GA ** _(project)_**   
Initial replication sync complete   
`GAUGE`, `BOOL`, ``   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Whether all databases on the destination DB instance have completed the initial sync and are replicating changes from the source._   
`database`: The database in the given instance associated with this metric.   
`migration_job/max_replica_bytes_lag` GA ** _(project)_**   
Max lag bytes of the migration job data   
`GAUGE`, `INT64`, `By`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Current replication lag, aggregated across all of the migration job's data. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/max_replica_sec_lag` GA ** _(project)_**   
Max lag in seconds of the migration job data   
`GAUGE`, `INT64`, `s`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Current replication lag, aggregated across all of the migration job's data. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/sqlserver/processed_file_bytes_count` GA ** _(project)_**   
Processed Files Bytes Count   
`DELTA`, `INT64`, `By`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Number of bytes uploaded to the destination. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/sqlserver/processed_file_count` GA ** _(project)_**   
Processed Files Count   
`DELTA`, `INT64`, `1`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Number of files uploaded to the destination. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/sqlserver/transaction_log_upload_sec_lag` GA ** _(project)_**   
Transaction Log Upload Sec Lag   
`GAUGE`, `INT64`, `s`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _The lag in seconds since the last uploaded transaction log. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/sqlserver/unprocessed_file_bytes` GA ** _(project)_**   
Unprocessed File Bytes   
`GAUGE`, `INT64`, `By`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Unprocessed file bytes waiting to be uploaded to Cloud SQL. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/sqlserver/unprocessed_files` GA ** _(project)_**   
Unprocessed Files   
`GAUGE`, `INT64`, `1`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Unprocessed files waiting to be uploaded to Cloud SQL. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/unsupported_events_count` GA ** _(project)_**   
Unsupported Events Count   
`DELTA`, `INT64`, `1`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Number of unsupported events per migration and per table. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`schema`: The schema associated with this metric.   
`table`: The table associated with this metric.   
`migration_job/write_bytes_count` GA ** _(project)_**   
Write Bytes Count   
`DELTA`, `INT64`, `By`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Number of bytes written to the destination. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`schema`: The schema associated with this metric.   
`table`: The table associated with this metric.   
`phase`: The phase associated with this metric (i.e. FULL_DUMP, CDC).   
`migration_job/write_rows_count` GA ** _(project)_**   
Write Rows Count   
`DELTA`, `INT64`, `1`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Number of rows written to the destination. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`schema`: The schema associated with this metric.   
`table`: The table associated with this metric.   
`phase`: The phase associated with this metric (i.e. FULL_DUMP, CDC).   
  
### dataplex

Metrics from [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `dataplex.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`asset/active` BETA ** _(project)_**   
Active   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _Whether the asset is active._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/data_items` BETA ** _(project)_**   
Data items   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _The count of items within the referenced resource._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/data_size` BETA ** _(project)_**   
Data size   
`GAUGE`, `INT64`, `By`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _The number of stored bytes within the referenced resource._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/entities_pending_bigquery_iampolicy_updates` BETA ** _(project)_**   
Entities with BigQuery IAM policy updates pending   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _Number of Entities associated with the Asset with BigQuery IAM policy updates pending._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/entities_pending_bigquery_metadata_updates` BETA ** _(project)_**   
Entities with BigQuery metadata updates pending   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _Number of Entities associated with the Asset with BigQuery metadata updates pending._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/filesets` BETA ** _(project)_**   
Filesets   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _The count of fileset entities within the referenced resource._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/requires_action` BETA ** _(project)_**   
Requires action   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _Whether the asset has unresolved admin actions._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/tables` BETA ** _(project)_**   
Tables   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _The count of table entities within the referenced resource._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`lake/requires_action` BETA ** _(project)_**   
Requires action   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Lake](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Lake)** |  _Whether the lake has unresolved admin actions._  
`zone/requires_action` BETA ** _(project)_**   
Requires action   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Zone](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Zone)** |  _Whether the zone has unresolved admin actions._   
`type`: The type of the zone.   
  
### dataproc

Metrics from [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `dataproc.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`batch/spark/executors` GA ** _(project)_**   
Batch Spark executors   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_batch](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_batch)** |  _Indicates the number of Batch Spark executors. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`status`: The status of Batch Spark executors, one of [running, pending-delete, required, maximum-needed, target].   
`cluster/capacity_deviation` BETA ** _(project)_**   
Cluster capacity deviation   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Difference between the expected node count in the cluster and the actual active YARN node managers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`cluster/hdfs/datanodes` GA ** _(project)_**   
HDFS DataNodes   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of HDFS DataNodes that are running inside a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The status of DataNode such as running, decommissioning, decommissioned.   
`cluster/hdfs/storage_capacity` GA ** _(project)_**   
HDFS capacity   
`GAUGE`, `DOUBLE`, `GiBy`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates capacity of HDFS system running on cluster in GB. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The status of HDFS capacity such as used, remaining.   
`cluster/hdfs/storage_utilization` GA ** _(project)_**   
HDFS storage utilization   
`GAUGE`, `DOUBLE`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _The percentage of HDFS storage currently used. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`cluster/hdfs/unhealthy_blocks` GA ** _(project)_**   
Unhealthy HDFS blocks by status   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of unhealthy blocks inside the cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The status of unhealthy HDFS block such as missing, under_replication, corrupt, pending_deletion, missing_repl_one.   
`cluster/job/completion_time` GA ** _(project)_**   
Job duration   
`DELTA`, `DISTRIBUTION`, `s`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _The time jobs took to complete from the time the user submits a job to the time Dataproc reports it is completed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_type`: The type of job such as HADOOP_JOB or SPARK_JOB.   
`cluster/job/duration` GA ** _(project)_**   
Job state duration   
`DELTA`, `DISTRIBUTION`, `s`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _The time jobs have spent in a given state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_type`: The type of job such as HADOOP_JOB or SPARK_JOB.   
`state`: The state of the job such as PENDING or RUNNING.   
`cluster/job/failed_count` GA ** _(project)_**   
Failed jobs   
`DELTA`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of jobs that have failed on a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`error_type`: The rpc code of the error such as 404 or 503.   
`job_type`: The type of job such as HADOOP_JOB or SPARK_JOB.   
`cluster/job/running_count` GA ** _(project)_**   
Running jobs   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of jobs that are running on a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_type`: The type of job such as HADOOP_JOB or SPARK_JOB.   
`cluster/job/submitted_count` GA ** _(project)_**   
Submitted jobs   
`DELTA`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of jobs that have been submitted to a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`job_type`: The type of job such as HADOOP_JOB or SPARK_JOB.   
`cluster/mig_instances/failed_count` BETA ** _(project)_**   
Dataproc Managed Instance Group Instance Errors   
`DELTA`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of instance failures for a managed instance group. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`mig_uuid`: The unique identifier of managed instance group associated with the cluster.   
`error_code`: The error code of the instances which failed while creating/recreating.   
`cluster/nodes/expected` BETA ** _(project)_**   
Expected Nodes   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of nodes that are expected in a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`node_type`: The type of node. One of [SINGLE_NODE, MASTER, HA_PRIMARY_MASTER, HA_SECONDARY_MASTER, HA_TERTIARY_MASTER, PRIMARY_WORKER, SECONDARY_WORKER].   
`cluster/nodes/failed_count` BETA ** _(project)_**   
Failed Nodes   
`DELTA`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of nodes that have failed in a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`node_type`: The type of node. One of [SINGLE_NODE, MASTER, HA_PRIMARY_MASTER, HA_SECONDARY_MASTER, HA_TERTIARY_MASTER, PRIMARY_WORKER, SECONDARY_WORKER].   
`failure_type`: Indicates the type of failure such as GCE_ERROR, DATAPROC_AGENT_ERROR or DATAPROC_DATAPLANE_ERROR.   
`cluster/nodes/recovered_count` BETA ** _(project)_**   
Recovered Nodes   
`DELTA`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of nodes that are detected as failed and have been successfully removed from cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`node_type`: The type of node. One of [SINGLE_NODE, MASTER, HA_PRIMARY_MASTER, HA_SECONDARY_MASTER, HA_TERTIARY_MASTER, PRIMARY_WORKER, SECONDARY_WORKER].   
`cluster/nodes/running` BETA ** _(project)_**   
Running Nodes   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of nodes in running state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`node_type`: The type of node. One of [SINGLE_NODE, MASTER, HA_PRIMARY_MASTER, HA_SECONDARY_MASTER, HA_TERTIARY_MASTER, PRIMARY_WORKER, SECONDARY_WORKER].   
`cluster/operation/completion_time` GA ** _(project)_**   
Operation duration   
`DELTA`, `DISTRIBUTION`, `s`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _The time operations took to complete from the time the user submits a operation to the time Dataproc reports it is completed. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operation_type`: The type of operation such as CREATE_CLUSTER or DELETE_CLUSTER.   
`cluster/operation/duration` GA ** _(project)_**   
Operation state duration   
`DELTA`, `DISTRIBUTION`, `s`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _The time operations have spent in a given state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operation_type`: The type of operation such as CREATE_CLUSTER or DELETE_CLUSTER.   
`state`: The state of the operation such as PENDING or CREATE_VMS.   
`cluster/operation/failed_count` GA ** _(project)_**   
Failed operations   
`DELTA`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of operations that have failed on a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`error_type`: The rpc code of the error such as 404 or 503.   
`operation_type`: The type of operation such as CREATE_CLUSTER or DELETE_CLUSTER.   
`cluster/operation/running_count` GA ** _(project)_**   
Running operations   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of operations that are running on a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operation_type`: The type of operation such as CREATE_CLUSTER or DELETE_CLUSTER.   
`cluster/operation/submitted_count` GA ** _(project)_**   
Submitted operations   
`DELTA`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of operations that have been submitted to a cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`operation_type`: The type of operation such as CREATE_CLUSTER or DELETE_CLUSTER.   
`cluster/state` BETA ** _(project)_**   
Cluster state   
`GAUGE`, `BOOL`, ``   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates whether Dataproc cluster is currently in a particular state or not. True indicates in that state and False indicates exited that state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: The state of the Dataproc cluster such as RUNNING or ERROR.   
`cluster/yarn/allocated_memory_percentage` GA ** _(project)_**   
YARN allocated memory percentage   
`GAUGE`, `DOUBLE`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _The percentage of YARN memory is allocated. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`cluster/yarn/apps` GA ** _(project)_**   
YARN active applications   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of active YARN applications. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The status of YARN application such as running, pending, completed, failed, killed.   
`cluster/yarn/containers` GA ** _(project)_**   
YARN containers   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of YARN containers. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The status of YARN container such as allocated, pending, reserved.   
`cluster/yarn/memory_size` GA ** _(project)_**   
YARN memory size   
`GAUGE`, `DOUBLE`, `GiBy`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the YARN memory size in GB. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The status of YARN memory such as available, allocated, reserved.   
`cluster/yarn/nodemanagers` GA ** _(project)_**   
YARN NodeManagers   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of YARN NodeManagers running inside cluster. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The status of YARN NodeManager such as active, lost, unhealthy, rebooted, decommissioned.   
`cluster/yarn/pending_memory_size` GA ** _(project)_**   
YARN pending memory size   
`GAUGE`, `DOUBLE`, `GiBy`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _The current memory request, in GB, that is pending to be fulfilled by the scheduler. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`cluster/yarn/virtual_cores` GA ** _(project)_**   
YARN virtual cores   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_cluster)** |  _Indicates the number of virtual cores in YARN. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: The status of YARN virtual cores such as pending, allocated, available, reserved.   
`job/state` GA ** _(project)_**   
Job state   
`GAUGE`, `BOOL`, ``   
**[cloud_dataproc_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_job)** |  _Indicates whether job is currently in a particular state or not. True indicates in that state and False indicates exited that state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: The state of the job such as PENDING or RUNNING.   
`job/yarn/memory_seconds` BETA ** _(project)_**   
Consumed memory seconds by job   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_job)** |  _Indicates the Memory Seconds consumed by the `job_id` job per yarn `application_id`. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`application_id`: Yarn application ID.   
`job/yarn/vcore_seconds` BETA ** _(project)_**   
Consumed vcore seconds by job   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_job](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_job)** |  _Indicates the VCore Seconds consumed by the `job_id` job per yarn `application_id`. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`application_id`: Yarn application ID.   
`node/problem_count` BETA ** _(project)_**   
Problem count   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of times a specific type of problem has occurred. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`reason`: Description of the type of the problem.   
`node/yarn/nodemanager/health` BETA ** _(project)_**   
YARN NodeManager Health   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _YARN nodemanager health state. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`state`: Health state of yarn nodemanager for the gce instance resource.   
`session/spark/executors` GA ** _(project)_**   
Session Spark executors   
`GAUGE`, `INT64`, `1`   
**[cloud_dataproc_session](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dataproc_session)** |  _Indicates the number of Session Spark executors. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`status`: The status of Session Spark executors, one of [running, pending-delete, required, maximum-needed, target].   
  
### datastore

Metrics from [Datastore](https://docs.cloud.google.com/datastore/docs). Metrics from [Firestore](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-firestore) written against `firestore.googleapis.com/Database` resources are also applicable to Datastore databases. Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `datastore.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`api/request_count` GA ** _(project)_**   
Requests   
`DELTA`, `INT64`, `1`   
**[datastore_request](https://docs.cloud.google.com/monitoring/api/resources#tag_datastore_request)** |  _Count of Datastore API calls. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`api_method`: The API method called (for example: BeginTransaction or Commit).   
`response_code`: Operation response code string, derived as a string representation of a HTTP status code (e.g. success, not_found, unavailable).   
`entity/read_sizes` GA ** _(project)_**   
Sizes of read entities   
`DELTA`, `DISTRIBUTION`, `By`   
**[datastore_request](https://docs.cloud.google.com/monitoring/api/resources#tag_datastore_request)** |  _Distribution of sizes of read entities, grouped by type. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`type`: The type of entity read (for example: KEYS_ONLY or ENTITY_SCAN).   
`entity/ttl_deletion_count` GA ** _(project)_**   
TTL deletion count   
`DELTA`, `INT64`, `1`   
**[datastore_request](https://docs.cloud.google.com/monitoring/api/resources#tag_datastore_request)** |  _Total count of entities deleted by TTL services. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`entity/ttl_expiration_to_deletion_delays` GA ** _(project)_**   
TTL expiration to deletion delays   
`DELTA`, `DISTRIBUTION`, `s`   
**[datastore_request](https://docs.cloud.google.com/monitoring/api/resources#tag_datastore_request)** |  _Time elapsed between when an entity with a TTL expired, and when it was actually deleted. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`entity/write_sizes` GA ** _(project)_**   
Sizes of written entities   
`DELTA`, `DISTRIBUTION`, `By`   
**[datastore_request](https://docs.cloud.google.com/monitoring/api/resources#tag_datastore_request)** |  _Distribution of sizes of written entities, grouped by op. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`op`: The operation type (for example: CREATE or DELETE_NOOP).   
`index/write_count` GA ** _(project)_**   
Index writes   
`DELTA`, `INT64`, `1`   
**[datastore_request](https://docs.cloud.google.com/monitoring/api/resources#tag_datastore_request)** |  _Count of Datastore index writes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
  
### datastream

Metrics from [Datastream](https://docs.cloud.google.com/datastream/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `datastream.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`stream/bytes_count` GA ** _(project)_**   
Stream bytes count   
`DELTA`, `INT64`, `By`   
**[datastream.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_datastream.googleapis.com/Stream)** |  _The total bytes count replicated by the stream._   
`read_method`: The read method used to process the events (CDC or BACKFILL).   
`stream/event_count` GA ** _(project)_**   
Stream event count   
`DELTA`, `INT64`, `1`   
**[datastream.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_datastream.googleapis.com/Stream)** |  _The total event count replicated by the stream._   
`read_method`: The read method used to process the events (CDC or BACKFILL).   
`stream/freshness` GA ** _(project)_**   
Stream freshness   
`GAUGE`, `INT64`, `s`   
**[datastream.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_datastream.googleapis.com/Stream)** |  _Indicates how far behind Datastream is compared to the source. This is calculated as the time difference between when the change occurred in the source database, until it is read by Datastream. If no new changes are available to read then the freshness is set to 0._  
`stream/latencies` GA ** _(project)_**   
Stream latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[datastream.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_datastream.googleapis.com/Stream)** |  _The stream latencies._   
`read_method`: The read method used to process the events (CDC or BACKFILL).   
`stream/system_latencies` GA ** _(project)_**   
Stream system latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[datastream.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_datastream.googleapis.com/Stream)** |  _A distribution of the latency calculated from when the event was read from the source until it was written to the destination._   
`read_method`: The read method used to process the events (CDC or BACKFILL).   
`stream/total_latencies` GA ** _(project)_**   
Stream total latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[datastream.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_datastream.googleapis.com/Stream)** |  _A distribution of the latency calculated from when the event was created at the source until it was written to the destination._   
`read_method`: The read method used to process the events (CDC or BACKFILL).   
`stream/unsupported_event_count` GA ** _(project)_**   
Stream unsupported event count   
`DELTA`, `INT64`, `1`   
**[datastream.googleapis.com/Stream](https://docs.cloud.google.com/monitoring/api/resources#tag_datastream.googleapis.com/Stream)** |  _The stream unsupported event count._   
`read_method`: The read method used to process the events (CDC or BACKFILL).   
`object_name`: The name of the object that reported the unsupported events.   
`error_code`: The reason code to why the events are unsupported.   
`streamobject/bytes_count` GA ** _(project)_**   
bytes count per stream object   
`DELTA`, `INT64`, `By`   
**[datastream.googleapis.com/StreamObject](https://docs.cloud.google.com/monitoring/api/resources#tag_datastream.googleapis.com/StreamObject)** |  _The total bytes count replicated per stream object._   
`read_method`: The read method used to process the events (CDC or BACKFILL).   
`streamobject/event_count` GA ** _(project)_**   
event count per stream object   
`DELTA`, `INT64`, `1`   
**[datastream.googleapis.com/StreamObject](https://docs.cloud.google.com/monitoring/api/resources#tag_datastream.googleapis.com/StreamObject)** |  _The total event count replicated per stream object._   
`read_method`: The read method used to process the events (CDC or BACKFILL).   
  
### dbinsights

Metrics from [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `dbinsights.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`aggregate/execution_count` BETA ** _(project)_**   
Number of calls   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of query executions per user and database._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`aggregate/execution_time` BETA ** _(project)_**   
Execution time   
`CUMULATIVE`, `INT64`, `us{CPU}`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative query execution time per user and database. This is the sum of the time required for the CPU, IO wait, lock wait, process context switching, and scheduling for all the processes involved in the query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`aggregate/io_time` BETA ** _(project)_**   
IO wait time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative IO wait time per user and database._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`aggregate/latencies` BETA ** _(project)_**   
Latency   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative query latency distribution per user and database._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`aggregate/lock_time` BETA ** _(project)_**   
Lock wait time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative lock wait time per user and database._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`lock_type`: The lock type. For PostgreSQL, it can be lw, hw, or buffer_pin. For MySQL, a value is not required.   
`aggregate/row_count` BETA ** _(project)_**   
Affected rows   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of rows affected during query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`row_status`: The status of rows. For Postgres, it can be output. For MySQL, it can be output or scan).   
`perquery/execution_count` BETA ** _(project)_**   
Number of calls per query   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of query executions per user, database, and query._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`perquery/execution_time` BETA ** _(project)_**   
Execution time per query   
`CUMULATIVE`, `INT64`, `us{CPU}`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative query execution time per user, database, and query. This is the sum of the time required for the CPU, IO wait, lock wait, process context switching, and scheduling for all the processes involved in the query execution._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`perquery/io_time` BETA ** _(project)_**   
IO wait time per query   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative io wait time per user, database, and query._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`perquery/latencies` BETA ** _(project)_**   
Latency per query   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative query latency distribution per user, database, and query._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`perquery/lock_time` BETA ** _(project)_**   
Lock wait time per query   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative lock wait time per user, database, and query._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`lock_type`: The lock type. For PostgreSQL, it can be lw, hw, or buffer_pin. For MySQL, a value is not required.   
`query_hash`: A unique hash of the query string.   
`perquery/row_count` BETA ** _(project)_**   
Affected rows per query   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of rows affected during query execution._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`row_status`: The status of rows. For Postgres, it can be output. For MySQL, it can be output or scan).   
`pertag/execution_count` BETA ** _(project)_**   
Number of calls per tag   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of query executions per user, database, and tag._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`pertag/execution_time` BETA ** _(project)_**   
Execution time per tag   
`CUMULATIVE`, `INT64`, `us{CPU}`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative query execution time per user, database, and tag. This is the sum of the time required for the CPU, IO wait, lock wait, process context switching, and scheduling for all the processes involved in the query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`pertag/io_time` BETA ** _(project)_**   
IO wait time per tag   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative IO wait time per user, database and tag._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`pertag/latencies` BETA ** _(project)_**   
Latency per tag   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative query latency distribution per user, database, and tag._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`pertag/lock_time` BETA ** _(project)_**   
Lock wait time per tag   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Cumulative lock wait time per user, database and tag._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`lock_type`: The lock type. For PostgreSQL, it can be lw, hw, or buffer_pin. For MySQL, a value is not required.   
`tag_hash`: A unique hash of the tag string.   
`pertag/row_count` BETA ** _(project)_**   
Affected rows per tag   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of rows affected during query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the database driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`row_status`: The status of rows. For Postgres, it can be output. For MySQL, it can be output or scan).   
  
### dialogflow

Metrics from [Dialogflow](https://docs.cloud.google.com/dialogflow/docs). Launch stages of these metrics: ALPHA GA

The "metric type" strings in this table must be prefixed with `dialogflow.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`location/phone_call_count` GA ** _(project)_**   
Phone Call   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _The number of phone calls made in the location. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`call_status`: Status of the phone call: successful, reject, etc.   
`location/phone_call_duration_count` GA ** _(project)_**   
Phone Call Duration   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Duration in seconds of phone calls made in the location. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`quota/ConversationalAgentGlobalLLMTokenConsumption/exceeded` GA ** _(project)_**   
Conversational Agent Global LLM tokens quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/ConversationalAgentGlobalLLMTokenConsumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/ConversationalAgentGlobalLLMTokenConsumption/limit` GA ** _(project)_**   
Conversational Agent Global LLM tokens quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/ConversationalAgentGlobalLLMTokenConsumption. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/ConversationalAgentGlobalLLMTokenConsumption/usage` GA ** _(project)_**   
Conversational Agent Global LLM tokens quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/ConversationalAgentGlobalLLMTokenConsumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/ConversationalAgentLLMTokenConsumption/exceeded` GA ** _(project)_**   
Conversational Agent LLM tokens quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/ConversationalAgentLLMTokenConsumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/ConversationalAgentLLMTokenConsumption/limit` GA ** _(project)_**   
Conversational Agent LLM tokens quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/ConversationalAgentLLMTokenConsumption. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`base_model`: The base model custom dimension.   
`quota/ConversationalAgentLLMTokenConsumption/usage` GA ** _(project)_**   
Conversational Agent LLM tokens quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/ConversationalAgentLLMTokenConsumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`base_model`: The base model custom dimension.   
`quota/ConversationalAgentMultiRegionGNLUTokenConsumption/exceeded` ALPHA ** _(project)_**   
Conversational Agent Multi-Region GNLU tokens quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/ConversationalAgentMultiRegionGNLUTokenConsumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`quota/ConversationalAgentMultiRegionGNLUTokenConsumption/limit` ALPHA ** _(project)_**   
Conversational Agent Multi-Region GNLU tokens quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/ConversationalAgentMultiRegionGNLUTokenConsumption. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`quota/ConversationalAgentMultiRegionGNLUTokenConsumption/usage` ALPHA ** _(project)_**   
Conversational Agent Multi-Region GNLU tokens quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/ConversationalAgentMultiRegionGNLUTokenConsumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`multi_region`: The multi-region custom dimension.   
`quota/ConversationalAgentMultiRegionLLMTokenConsumption/exceeded` GA ** _(project)_**   
Conversational Agent Multi-Region LLM tokens quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/ConversationalAgentMultiRegionLLMTokenConsumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`base_model`: The base model custom dimension.   
`quota/ConversationalAgentMultiRegionLLMTokenConsumption/limit` GA ** _(project)_**   
Conversational Agent Multi-Region LLM tokens quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/ConversationalAgentMultiRegionLLMTokenConsumption. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`base_model`: The base model custom dimension.   
`quota/ConversationalAgentMultiRegionLLMTokenConsumption/usage` GA ** _(project)_**   
Conversational Agent Multi-Region LLM tokens quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/ConversationalAgentMultiRegionLLMTokenConsumption. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`multi_region`: The multi-region custom dimension.   
`base_model`: The base model custom dimension.   
`quota/PhoneNumbersPerMultiRegion/exceeded` ALPHA ** _(project)_**   
Phone numbers per multi-region quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/PhoneNumbersPerMultiRegion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`quota/PhoneNumbersPerMultiRegion/limit` ALPHA ** _(project)_**   
Phone numbers per multi-region quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/PhoneNumbersPerMultiRegion. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`quota/PhoneNumbersPerMultiRegion/usage` ALPHA ** _(project)_**   
Phone numbers per multi-region quota usage   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/PhoneNumbersPerMultiRegion. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`quota/generator_suggestion_operations_per_model_type/exceeded` GA ** _(project)_**   
Generator suggestion operations quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/generator_suggestion_operations_per_model_type. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model_type`: The model type custom dimension.   
`quota/generator_suggestion_operations_per_model_type/limit` GA ** _(project)_**   
Generator suggestion operations quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/generator_suggestion_operations_per_model_type. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model_type`: The model type custom dimension.   
`quota/generator_suggestion_operations_per_model_type/usage` GA ** _(project)_**   
Generator suggestion operations quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/generator_suggestion_operations_per_model_type. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model_type`: The model type custom dimension.   
`quota/generator_suggestion_operations_per_model_type_per_multi_region/exceeded` GA ** _(project)_**   
Generator suggestion operations quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/generator_suggestion_operations_per_model_type_per_multi_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model_type`: The model type custom dimension.   
`multi_region`: The multi-region custom dimension.   
`quota/generator_suggestion_operations_per_model_type_per_multi_region/limit` GA ** _(project)_**   
Generator suggestion operations quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/generator_suggestion_operations_per_model_type_per_multi_region. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model_type`: The model type custom dimension.   
`multi_region`: The multi-region custom dimension.   
`quota/generator_suggestion_operations_per_model_type_per_multi_region/usage` GA ** _(project)_**   
Generator suggestion operations quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/generator_suggestion_operations_per_model_type_per_multi_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model_type`: The model type custom dimension.   
`multi_region`: The multi-region custom dimension.   
`quota/generator_suggestion_operations_per_model_type_per_region/exceeded` GA ** _(project)_**   
Generator suggestion operations quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/generator_suggestion_operations_per_model_type_per_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model_type`: The model type custom dimension.   
`quota/generator_suggestion_operations_per_model_type_per_region/limit` GA ** _(project)_**   
Generator suggestion operations quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/generator_suggestion_operations_per_model_type_per_region. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model_type`: The model type custom dimension.   
`quota/generator_suggestion_operations_per_model_type_per_region/usage` GA ** _(project)_**   
Generator suggestion operations quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/generator_suggestion_operations_per_model_type_per_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model_type`: The model type custom dimension.   
`quota/knowledge_assist_ops_per_minute_per_project_per_version/exceeded` GA ** _(project)_**   
Suggest knowledge assist operations quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/knowledge_assist_ops_per_minute_per_project_per_version. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`version`: The PGKA version custom dimension.   
`quota/knowledge_assist_ops_per_minute_per_project_per_version/limit` GA ** _(project)_**   
Suggest knowledge assist operations quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/knowledge_assist_ops_per_minute_per_project_per_version. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`version`: The PGKA version custom dimension.   
`quota/knowledge_assist_ops_per_minute_per_project_per_version/usage` GA ** _(project)_**   
Suggest knowledge assist operations quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/knowledge_assist_ops_per_minute_per_project_per_version. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`version`: The PGKA version custom dimension.   
`quota/knowledge_assist_ops_per_minute_per_project_per_version_per_multi_region/exceeded` GA ** _(project)_**   
Suggest knowledge assist operations quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/knowledge_assist_ops_per_minute_per_project_per_version_per_multi_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`version`: The PGKA version custom dimension.   
`multi_region`: The multi-region custom dimension.   
`quota/knowledge_assist_ops_per_minute_per_project_per_version_per_multi_region/limit` GA ** _(project)_**   
Suggest knowledge assist operations quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/knowledge_assist_ops_per_minute_per_project_per_version_per_multi_region. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`version`: The PGKA version custom dimension.   
`multi_region`: The multi-region custom dimension.   
`quota/knowledge_assist_ops_per_minute_per_project_per_version_per_multi_region/usage` GA ** _(project)_**   
Suggest knowledge assist operations quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/knowledge_assist_ops_per_minute_per_project_per_version_per_multi_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`version`: The PGKA version custom dimension.   
`multi_region`: The multi-region custom dimension.   
`quota/knowledge_assist_ops_per_minute_per_project_per_version_per_region/exceeded` GA ** _(project)_**   
Suggest knowledge assist operations quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/knowledge_assist_ops_per_minute_per_project_per_version_per_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`version`: The PGKA version custom dimension.   
`quota/knowledge_assist_ops_per_minute_per_project_per_version_per_region/limit` GA ** _(project)_**   
Suggest knowledge assist operations quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/knowledge_assist_ops_per_minute_per_project_per_version_per_region. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`version`: The PGKA version custom dimension.   
`quota/knowledge_assist_ops_per_minute_per_project_per_version_per_region/usage` GA ** _(project)_**   
Suggest knowledge assist operations quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/knowledge_assist_ops_per_minute_per_project_per_version_per_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`version`: The PGKA version custom dimension.   
`quota/search_knowledge_requests_per_multi_region/exceeded` GA ** _(project)_**   
Search knowledge requests quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/search_knowledge_requests_per_multi_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`quota/search_knowledge_requests_per_multi_region/limit` GA ** _(project)_**   
Search knowledge requests quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/search_knowledge_requests_per_multi_region. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`quota/search_knowledge_requests_per_multi_region/usage` GA ** _(project)_**   
Search knowledge requests quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/search_knowledge_requests_per_multi_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`multi_region`: The multi-region custom dimension.   
`quota/stt_v2_streaming_requests/exceeded` GA ** _(project)_**   
Transcription requests using STT V2 quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/stt_v2_streaming_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`resource_type`: The resource type custom dimension.   
`quota/stt_v2_streaming_requests/limit` GA ** _(project)_**   
Transcription requests using STT V2 quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/stt_v2_streaming_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`resource_type`: The resource type custom dimension.   
`quota/stt_v2_streaming_requests/usage` GA ** _(project)_**   
Transcription requests using STT V2 quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/stt_v2_streaming_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`resource_type`: The resource type custom dimension.   
`quota/suggest_knowledge_assist_operations_per_multi_region/exceeded` GA ** _(project)_**   
Suggest knowledge assist operations quota exceeded error   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric dialogflow.googleapis.com/suggest_knowledge_assist_operations_per_multi_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`quota/suggest_knowledge_assist_operations_per_multi_region/limit` GA ** _(project)_**   
Suggest knowledge assist operations quota limit   
`GAUGE`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current limit on quota metric dialogflow.googleapis.com/suggest_knowledge_assist_operations_per_multi_region. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`multi_region`: The multi-region custom dimension.   
`quota/suggest_knowledge_assist_operations_per_multi_region/usage` GA ** _(project)_**   
Suggest knowledge assist operations quota usage   
`DELTA`, `INT64`, `1`   
**[dialogflow.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_dialogflow.googleapis.com/Location)** |  _Current usage on quota metric dialogflow.googleapis.com/suggest_knowledge_assist_operations_per_multi_region. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`multi_region`: The multi-region custom dimension.   
  
### discoveryengine

Metrics from [Discovery Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction) Launch stages of these metrics: ALPHA BETA

The "metric type" strings in this table must be prefixed with `discoveryengine.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`agent_session_count` BETA ** _(project)_**   
Gemini Enterprise Agent Session Count   
`CUMULATIVE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Agent)** |  _Number of sessions created for each Gemini Enterprise agent._  
`agent_session_with_tool_count` BETA ** _(project)_**   
Gemini Enterprise Session with Tool Count   
`CUMULATIVE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Agent)** |  _Number of sessions where at least one tool was invoked._  
`agent_total_latencies` BETA ** _(project)_**   
Gemini Enterprise Agent Total Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[discoveryengine.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Agent)** |  _Distribution of total latency of Gemini Enterprise agent invocations over a 1-minute window. Sampled every 30 seconds. After sampling, data is not visible for up to 330 seconds._   
`status`: The response code as a gRPC status code (e.g. OK, INVALID_ARGUMENT, etc.)   
`agent_turn_count` BETA ** _(project)_**   
Gemini Enterprise Agent Turn Count   
`CUMULATIVE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Agent)** |  _Number of session turns created for each Gemini Enterprise agent._  
`conversational_search_service/stream_answer_query/first_token_latencies` BETA ** _(project)_**   
Streaming Answer API Time to First Token   
`GAUGE`, `DISTRIBUTION`, `ms`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Latency to the first token returned by the Streaming Answer API. Sampled every 30 seconds. After sampling, data is not visible for up to 30 seconds._   
`model_version`: The model and version being used to generate an answer.   
`session_mode`: The mode of the session associated with the request.   
`data_stores_regional` BETA ** _(project)_**   
Regional number of data stores.   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Regional number of data stores. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`regional_location`: The multi region custom dimension.   
`dataconnector/request_count` BETA ** _(project)_**   
Gemini Enterprise DataConnector Request Count   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/DataConnector](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/DataConnector)** |  _Total number of requests made to the datastore, broken down by request status, gRPC canonical response code, connector tool, engine, and whether the tool reads or writes. Sampled every 30 seconds. After sampling, data is not visible for up to 360 seconds._   
`status`: The status of the request (e.g. SUCCESS, FAILURE).   
`response_code`: The gRPC canonical response code for the request (e.g. OK, INVALID_ARGUMENT, UNAVAILABLE).   
`tool_id`: The connector tool invoked (e.g. search_tool, create_issue).   
`engine_id`: The Gemini Enterprise engine (app) the request belongs to.   
`tool_type`: Whether the invoked tool reads or writes (READ or WRITE). Tools that do not declare themselves read-only are reported as WRITE.   
`dataconnector/request_latencies` BETA ** _(project)_**   
Gemini Enterprise DataConnector Request Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[discoveryengine.googleapis.com/DataConnector](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/DataConnector)** |  _Distribution of wall-clock latency (ms) of DataConnector tool invocations, measured at the ADK tool callback boundary. Sampled every 30 seconds. After sampling, data is not visible for up to 360 seconds._   
`status`: The status of the request (e.g. SUCCESS, ERROR).   
`response_code`: The gRPC canonical response code for the request (e.g. OK, INVALID_ARGUMENT, UNAVAILABLE).   
`tool_id`: The connector tool invoked (e.g. search_tool, create_issue).   
`engine_id`: The Gemini Enterprise engine (app) the request belongs to.   
`tool_type`: Whether the invoked tool reads or writes (READ or WRITE). Tools that do not declare themselves read-only are reported as WRITE.   
`documents_regional` BETA ** _(project)_**   
Regional number of documents.   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Regional number of documents. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`regional_location`: The multi region custom dimension.   
`engine/request_count` BETA ** _(project)_**   
Gemini Enterprise Engine Request Count   
`CUMULATIVE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Engine](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Engine)** |  _Total number of requests received by a Gemini Enterprise app (engine), broken down by public API method, canonical gRPC response code, response code class, query type, and model. Spans all traffic an engine receives, including non-agent paths (search / answer / assist)._   
`method`: The public API method that served the request (e.g. AssistantService.StreamAssist).   
`response_code`: The canonical gRPC response code (e.g. OK, INVALID_ARGUMENT, INTERNAL).   
`response_code_class`: The response code class (2xx, 4xx, or 5xx).   
`query_type`: A coarse classification of the turn workload derived from the tools invoked and the request payload (e.g. Parametric, Web, Connector, MediaGen, FileAnalysis, Canvas, Skill, Unclassified). Only populated for AssistantService.StreamAssist; empty for other methods.   
`model_id`: The identifier of the model that served the turn. Reported as unknown_model_id when the request failed before a model was selected.   
`engine/request_total_latency` BETA ** _(project)_**   
Gemini Enterprise Engine Request Total Latency   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[discoveryengine.googleapis.com/Engine](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Engine)** |  _Distribution of end-to-end request latency for a Gemini Enterprise app (engine), measured at the assistant server request boundary. Broken down by public API method, canonical gRPC response code, response code class, query type, and model._   
`method`: The public API method that served the request (e.g. AssistantService.StreamAssist).   
`response_code`: The canonical gRPC response code (e.g. OK, INVALID_ARGUMENT, INTERNAL).   
`response_code_class`: The response code class (2xx, 4xx, or 5xx).   
`query_type`: A coarse classification of the turn workload derived from the tools invoked and the request payload (e.g. Parametric, Web, Connector, MediaGen, FileAnalysis, Canvas, Skill, Unclassified). Only populated for AssistantService.StreamAssist; empty for other methods.   
`model_id`: The identifier of the model that served the turn. Reported as unknown_model_id when the request failed before a model was selected.   
`engine/time_to_first_answer_latency` BETA ** _(project)_**   
Gemini Enterprise Engine Time to First Answer Latency   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[discoveryengine.googleapis.com/Engine](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Engine)** |  _Distribution of latency from request receipt to the first streamed non-thought answer token, for a Gemini Enterprise app (engine). Only emitted for requests that produce at least one answer token; broken down by public API method, canonical gRPC response code, response code class, query type, and model._   
`method`: The public API method that served the request (e.g. AssistantService.StreamAssist).   
`response_code`: The canonical gRPC response code (e.g. OK, INVALID_ARGUMENT, INTERNAL).   
`response_code_class`: The response code class (2xx, 4xx, or 5xx).   
`query_type`: A coarse classification of the turn workload derived from the tools invoked and the request payload (e.g. Parametric, Web, Connector, MediaGen, FileAnalysis, Canvas, Skill, Unclassified). Only populated for AssistantService.StreamAssist; empty for other methods.   
`model_id`: The identifier of the model that served the turn. Reported as unknown_model_id when the request failed before a model was selected.   
`engine/time_to_first_token_latency` BETA ** _(project)_**   
Gemini Enterprise Engine Time to First Token Latency   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[discoveryengine.googleapis.com/Engine](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Engine)** |  _Distribution of latency from request receipt to the first streamed token (thought or answer), for a Gemini Enterprise app (engine). Only emitted for requests that produce at least one streamed token; broken down by public API method, canonical gRPC response code, response code class, query type, and model._   
`method`: The public API method that served the request (e.g. AssistantService.StreamAssist).   
`response_code`: The canonical gRPC response code (e.g. OK, INVALID_ARGUMENT, INTERNAL).   
`response_code_class`: The response code class (2xx, 4xx, or 5xx).   
`query_type`: A coarse classification of the turn workload derived from the tools invoked and the request payload (e.g. Parametric, Web, Connector, MediaGen, FileAnalysis, Canvas, Skill, Unclassified). Only populated for AssistantService.StreamAssist; empty for other methods.   
`model_id`: The identifier of the model that served the turn. Reported as unknown_model_id when the request failed before a model was selected.   
`engines_regional` BETA ** _(project)_**   
Regional number of engines.   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Regional number of engines. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_business_regional/exceeded` BETA ** _(project)_**   
Agents for business tier. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_business_regional/limit` BETA ** _(project)_**   
Agents for business tier. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_business_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_business_regional/usage` BETA ** _(project)_**   
Agents for business tier. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_consumption_only_regional/exceeded` BETA ** _(project)_**   
Agents for consumption-only tier. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_consumption_only_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_consumption_only_regional/limit` BETA ** _(project)_**   
Agents for consumption-only tier. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_consumption_only_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_consumption_only_regional/usage` BETA ** _(project)_**   
Agents for consumption-only tier. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_consumption_only_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Agents for developer ultra tier. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Agents for developer ultra tier. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Agents for developer ultra tier. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_emerging_regional/exceeded` BETA ** _(project)_**   
Number of agents for edu emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_emerging_regional/limit` BETA ** _(project)_**   
Number of agents for edu emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_edu_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_emerging_regional/usage` BETA ** _(project)_**   
Number of agents for edu emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_gov_emerging_regional/exceeded` BETA ** _(project)_**   
Number of agents for edu gov emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_edu_gov_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_gov_emerging_regional/limit` BETA ** _(project)_**   
Number of agents for edu gov emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_edu_gov_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_gov_emerging_regional/usage` BETA ** _(project)_**   
Number of agents for edu gov emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_edu_gov_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_pro_emerging_regional/exceeded` BETA ** _(project)_**   
Number of agents for edu pro emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_pro_emerging_regional/limit` BETA ** _(project)_**   
Number of agents for edu pro emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_edu_pro_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_pro_emerging_regional/usage` BETA ** _(project)_**   
Number of agents for edu pro emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_pro_regional/exceeded` BETA ** _(project)_**   
Agents for edu pro tier. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_pro_regional/limit` BETA ** _(project)_**   
Agents for edu pro tier. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_edu_pro_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_pro_regional/usage` BETA ** _(project)_**   
Agents for edu pro tier. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_regional/exceeded` BETA ** _(project)_**   
Custom agents number quota for edu tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_regional/limit` BETA ** _(project)_**   
Custom agents number quota for edu tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_edu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_edu_regional/usage` BETA ** _(project)_**   
Custom agents number quota for edu tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_enterprise_emerging_regional/exceeded` BETA ** _(project)_**   
Agents for enterprise emerging tier. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_enterprise_emerging_regional/limit` BETA ** _(project)_**   
Agents for enterprise emerging tier. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_enterprise_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_enterprise_emerging_regional/usage` BETA ** _(project)_**   
Agents for enterprise emerging tier. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_enterprise_plus_regional/exceeded` BETA ** _(project)_**   
Agents for enterprise plus tier. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_enterprise_plus_regional/limit` BETA ** _(project)_**   
Agents for enterprise plus tier. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_enterprise_plus_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_enterprise_plus_regional/usage` BETA ** _(project)_**   
Agents for enterprise plus tier. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_enterprise_regional/exceeded` BETA ** _(project)_**   
Agents for enterprise tier. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_enterprise_regional/limit` BETA ** _(project)_**   
Agents for enterprise tier. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_enterprise_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_enterprise_regional/usage` BETA ** _(project)_**   
Agents for enterprise tier. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_frontline_starter_regional/exceeded` BETA ** _(project)_**   
Custom agents number quota for frontline starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_frontline_starter_regional/limit` BETA ** _(project)_**   
Custom agents number quota for frontline starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_frontline_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_frontline_starter_regional/usage` BETA ** _(project)_**   
Custom agents number quota for frontline starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_frontline_worker_regional/exceeded` BETA ** _(project)_**   
Custom agents number quota for frontline worker tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_frontline_worker_regional/limit` BETA ** _(project)_**   
Custom agents number quota for frontline worker tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_frontline_worker_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_frontline_worker_regional/usage` BETA ** _(project)_**   
Custom agents number quota for frontline worker tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_starter_regional/exceeded` BETA ** _(project)_**   
Agents for starter tier. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/agents_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_starter_regional/limit` BETA ** _(project)_**   
Agents for starter tier. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/agents_tier_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/agents_tier_starter_regional/usage` BETA ** _(project)_**   
Agents for starter tier. quota usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/agents_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_overage_wtu_regional/exceeded` BETA ** _(project)_**   
Number of AI dev tool overage WTUs quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_overage_wtu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_overage_wtu_regional/limit` BETA ** _(project)_**   
Number of AI dev tool overage WTUs quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_overage_wtu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_overage_wtu_regional/usage` BETA ** _(project)_**   
Number of AI dev tool overage WTUs quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/ai_dev_tool_overage_wtu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_business_regional/exceeded` BETA ** _(project)_**   
Number of AI dev tool WTUs for business tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_business_regional/limit` BETA ** _(project)_**   
Number of AI dev tool WTUs for business tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_business_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_business_regional/usage` BETA ** _(project)_**   
Number of AI dev tool WTUs for business tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_business_trial_regional/exceeded` BETA ** _(project)_**   
Number of AI dev tool WTUs for business free trial quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_business_trial_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_business_trial_regional/limit` BETA ** _(project)_**   
Number of AI dev tool WTUs for business free trial quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_business_trial_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_business_trial_regional/usage` BETA ** _(project)_**   
Number of AI dev tool WTUs for business free trial quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_business_trial_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Number of AI dev tool WTUs for developer ultra tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Number of AI dev tool WTUs for developer ultra tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Number of AI dev tool WTUs for developer ultra tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_enterprise_plus_regional/exceeded` BETA ** _(project)_**   
Number of AI dev tool WTUs for enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_enterprise_plus_regional/limit` BETA ** _(project)_**   
Number of AI dev tool WTUs for enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_enterprise_plus_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_enterprise_plus_regional/usage` BETA ** _(project)_**   
Number of AI dev tool WTUs for enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_enterprise_standard_regional/exceeded` BETA ** _(project)_**   
Number of AI dev tool WTUs for enterprise standard tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_enterprise_standard_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_enterprise_standard_regional/limit` BETA ** _(project)_**   
Number of AI dev tool WTUs for enterprise standard tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_enterprise_standard_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/ai_dev_tool_wtu_tier_enterprise_standard_regional/usage` BETA ** _(project)_**   
Number of AI dev tool WTUs for enterprise standard tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/ai_dev_tool_wtu_tier_enterprise_standard_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/alpha_evolve_input_tokens_count_regional/exceeded` BETA ** _(project)_**   
AlphaEvolve input tokens count consumed across all tiers. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/alpha_evolve_input_tokens_count_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/alpha_evolve_input_tokens_count_regional/limit` BETA ** _(project)_**   
AlphaEvolve input tokens count consumed across all tiers. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/alpha_evolve_input_tokens_count_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/alpha_evolve_input_tokens_count_regional/usage` BETA ** _(project)_**   
AlphaEvolve input tokens count consumed across all tiers. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/alpha_evolve_input_tokens_count_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/alpha_evolve_output_tokens_count_regional/exceeded` BETA ** _(project)_**   
AlphaEvolve output tokens count produced across all tiers. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/alpha_evolve_output_tokens_count_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/alpha_evolve_output_tokens_count_regional/limit` BETA ** _(project)_**   
AlphaEvolve output tokens count produced across all tiers. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/alpha_evolve_output_tokens_count_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/alpha_evolve_output_tokens_count_regional/usage` BETA ** _(project)_**   
AlphaEvolve output tokens count produced across all tiers. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/alpha_evolve_output_tokens_count_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_input_tokens_count_per_project_per_engine_regional/exceeded` BETA ** _(project)_**   
Per-engine Coscientist input tokens count consumed across all tiers quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/coscientist_input_tokens_count_per_project_per_engine_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`engine_id`: The VAIS Engine custom dimension.   
`quota/coscientist_input_tokens_count_per_project_per_engine_regional/limit` BETA ** _(project)_**   
Per-engine Coscientist input tokens count consumed across all tiers quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/coscientist_input_tokens_count_per_project_per_engine_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`engine_id`: The VAIS Engine custom dimension.   
`quota/coscientist_input_tokens_count_per_project_per_engine_regional/usage` BETA ** _(project)_**   
Per-engine Coscientist input tokens count consumed across all tiers quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/coscientist_input_tokens_count_per_project_per_engine_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`engine_id`: The VAIS Engine custom dimension.   
`quota/coscientist_input_tokens_count_regional/exceeded` BETA ** _(project)_**   
Coscientist input tokens count consumed across all tiers. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/coscientist_input_tokens_count_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_input_tokens_count_regional/limit` BETA ** _(project)_**   
Coscientist input tokens count consumed across all tiers. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/coscientist_input_tokens_count_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_input_tokens_count_regional/usage` BETA ** _(project)_**   
Coscientist input tokens count consumed across all tiers. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/coscientist_input_tokens_count_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_output_tokens_count_per_project_per_engine_regional/exceeded` BETA ** _(project)_**   
Per-engine Coscientist output tokens count produced across all tiers quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/coscientist_output_tokens_count_per_project_per_engine_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`engine_id`: The VAIS Engine custom dimension.   
`quota/coscientist_output_tokens_count_per_project_per_engine_regional/limit` BETA ** _(project)_**   
Per-engine Coscientist output tokens count produced across all tiers quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/coscientist_output_tokens_count_per_project_per_engine_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`engine_id`: The VAIS Engine custom dimension.   
`quota/coscientist_output_tokens_count_per_project_per_engine_regional/usage` BETA ** _(project)_**   
Per-engine Coscientist output tokens count produced across all tiers quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/coscientist_output_tokens_count_per_project_per_engine_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`engine_id`: The VAIS Engine custom dimension.   
`quota/coscientist_output_tokens_count_regional/exceeded` BETA ** _(project)_**   
Coscientist output tokens count produced across all tiers. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/coscientist_output_tokens_count_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_output_tokens_count_regional/limit` BETA ** _(project)_**   
Coscientist output tokens count produced across all tiers. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/coscientist_output_tokens_count_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_output_tokens_count_regional/usage` BETA ** _(project)_**   
Coscientist output tokens count produced across all tiers. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/coscientist_output_tokens_count_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_start_instance_tier_regional/exceeded` BETA ** _(project)_**   
Coscientist start instance requests per user independent of tier. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/coscientist_start_instance_tier_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_start_instance_tier_regional/limit` BETA ** _(project)_**   
Coscientist start instance requests per user independent of tier. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/coscientist_start_instance_tier_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_start_instance_tier_regional/usage` BETA ** _(project)_**   
Coscientist start instance requests per user independent of tier. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/coscientist_start_instance_tier_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_start_instance_upper_bound_regional/exceeded` BETA ** _(project)_**   
Coscientist start instance upper bound for all tiers. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/coscientist_start_instance_upper_bound_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_start_instance_upper_bound_regional/limit` BETA ** _(project)_**   
Coscientist start instance upper bound for all tiers. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/coscientist_start_instance_upper_bound_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/coscientist_start_instance_upper_bound_regional/usage` BETA ** _(project)_**   
Coscientist start instance upper bound for all tiers. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/coscientist_start_instance_upper_bound_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/data_stores_regional/exceeded` BETA ** _(project)_**   
Regional number of data stores. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/data_stores_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/data_stores_regional/limit` BETA ** _(project)_**   
Regional number of data stores. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/data_stores_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/data_stores_regional/usage` BETA ** _(project)_**   
Regional number of data stores. quota usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/data_stores_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_business_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for business tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_business_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for business tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_business_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_business_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for business tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_consumption_only_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for consumption-only tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_consumption_only_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_consumption_only_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for consumption-only tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_consumption_only_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_consumption_only_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for consumption-only tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_consumption_only_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for developer ultra tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for developer ultra tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for developer ultra tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_emerging_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for edu emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_emerging_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for edu emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_emerging_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for edu emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_gov_emerging_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for edu gov emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_gov_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_gov_emerging_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for edu gov emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_gov_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_gov_emerging_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for edu gov emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_gov_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_pro_emerging_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for edu pro emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_pro_emerging_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for edu pro emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_pro_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_pro_emerging_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for edu pro emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_pro_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for edu pro tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_pro_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for edu pro tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_pro_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_pro_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for edu pro tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for edu tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for edu tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_edu_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for edu tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_enterprise_emerging_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for enterprise emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_enterprise_emerging_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for enterprise emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_enterprise_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_enterprise_emerging_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for enterprise emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_enterprise_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_enterprise_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_enterprise_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_enterprise_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_enterprise_standard_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for enterprise standard tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_enterprise_standard_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_enterprise_standard_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for enterprise standard tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_enterprise_standard_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_enterprise_standard_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for enterprise standard tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_enterprise_standard_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_frontline_starter_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for frontline starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_frontline_starter_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for frontline starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_frontline_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_frontline_starter_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for frontline starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_frontline_worker_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for frontline worker tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_frontline_worker_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for frontline worker tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_frontline_worker_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_frontline_worker_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for frontline worker tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_starter_regional/exceeded` BETA ** _(project)_**   
Deep research query total daily quota for starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_starter_regional/limit` BETA ** _(project)_**   
Deep research query total daily quota for starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_starter_regional/usage` BETA ** _(project)_**   
Deep research query total daily quota for starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_starter_v2_regional/exceeded` BETA ** _(project)_**   
Deep research query total quota for starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_starter_v2_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_starter_v2_regional/limit` BETA ** _(project)_**   
Deep research query total quota for starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_starter_v2_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/deep_research_query_total_tier_starter_v2_regional/usage` BETA ** _(project)_**   
Deep research query total quota for starter tier quota usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/deep_research_query_total_tier_starter_v2_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/document_size_tier_business_regional/exceeded` BETA ** _(project)_**   
Document storage size in term of bytes for business tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/document_size_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/document_size_tier_business_regional/limit` BETA ** _(project)_**   
Document storage size in term of bytes for business tier quota limit   
`GAUGE`, `INT64`, `By`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/document_size_tier_business_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/document_size_tier_business_regional/usage` BETA ** _(project)_**   
Document storage size in term of bytes for business tier quota usage   
`GAUGE`, `INT64`, `By`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/document_size_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/document_size_tier_starter_regional/exceeded` BETA ** _(project)_**   
Document storage size in term of bytes for starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/document_size_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/document_size_tier_starter_regional/limit` BETA ** _(project)_**   
Document storage size in term of bytes for starter tier quota limit   
`GAUGE`, `INT64`, `By`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/document_size_tier_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/document_size_tier_starter_regional/usage` BETA ** _(project)_**   
Document storage size in term of bytes for starter tier quota usage   
`GAUGE`, `INT64`, `By`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/document_size_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/documents_regional/exceeded` BETA ** _(project)_**   
Regional number of documents. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/documents_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/documents_regional/limit` BETA ** _(project)_**   
Regional number of documents. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/documents_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/documents_regional/usage` BETA ** _(project)_**   
Regional number of documents. quota usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/documents_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/engines_regional/exceeded` BETA ** _(project)_**   
Regional number of engines. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/engines_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/engines_regional/limit` BETA ** _(project)_**   
Regional number of engines. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/engines_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/engines_regional/usage` BETA ** _(project)_**   
Regional number of engines. quota usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/engines_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_business_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for business tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_business_regional/limit` BETA ** _(project)_**   
Grounding with Google search for business tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_business_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_business_regional/usage` BETA ** _(project)_**   
Grounding with Google search for business tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for developer ultra tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Grounding with Google search for developer ultra tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Grounding with Google search for developer ultra tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_emerging_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for edu emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_emerging_regional/limit` BETA ** _(project)_**   
Grounding with Google search for edu emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_emerging_regional/usage` BETA ** _(project)_**   
Grounding with Google search for edu emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_pro_emerging_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for edu pro emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_pro_emerging_regional/limit` BETA ** _(project)_**   
Grounding with Google search for edu pro emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_pro_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_pro_emerging_regional/usage` BETA ** _(project)_**   
Grounding with Google search for edu pro emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_pro_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for edu pro tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_pro_regional/limit` BETA ** _(project)_**   
Grounding with Google search for edu pro tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_pro_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_pro_regional/usage` BETA ** _(project)_**   
Grounding with Google search for edu pro tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for edu tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_regional/limit` BETA ** _(project)_**   
Grounding with Google search for edu tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_edu_regional/usage` BETA ** _(project)_**   
Grounding with Google search for edu tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_enterprise_emerging_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for enterprise emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_enterprise_emerging_regional/limit` BETA ** _(project)_**   
Grounding with Google search for enterprise emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_enterprise_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_enterprise_emerging_regional/usage` BETA ** _(project)_**   
Grounding with Google search for enterprise emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_enterprise_plus_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_enterprise_plus_regional/limit` BETA ** _(project)_**   
Grounding with Google search for enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_enterprise_plus_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_enterprise_plus_regional/usage` BETA ** _(project)_**   
Grounding with Google search for enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_enterprise_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for enterprise tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_enterprise_regional/limit` BETA ** _(project)_**   
Grounding with Google search for enterprise tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_enterprise_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_enterprise_regional/usage` BETA ** _(project)_**   
Grounding with Google search for enterprise tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_frontline_starter_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for frontline starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_frontline_starter_regional/limit` BETA ** _(project)_**   
Grounding with Google search for frontline starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_frontline_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_frontline_starter_regional/usage` BETA ** _(project)_**   
Grounding with Google search for frontline starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_frontline_worker_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for frontline worker tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_frontline_worker_regional/limit` BETA ** _(project)_**   
Grounding with Google search for frontline worker tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_frontline_worker_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_frontline_worker_regional/usage` BETA ** _(project)_**   
Grounding with Google search for frontline worker tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_starter_regional/exceeded` BETA ** _(project)_**   
Grounding with Google search for starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_starter_regional/limit` BETA ** _(project)_**   
Grounding with Google search for starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/grounding_with_search_tier_starter_regional/usage` BETA ** _(project)_**   
Grounding with Google search for starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/grounding_with_search_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_business_regional/exceeded` BETA ** _(project)_**   
Idea Generation start instance requests per user for the business tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_business_regional/limit` BETA ** _(project)_**   
Idea Generation start instance requests per user for the business tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_business_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_business_regional/usage` BETA ** _(project)_**   
Idea Generation start instance requests per user for the business tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Idea Generation start instance requests per user for the developer ultra tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Idea Generation start instance requests per user for the developer ultra tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Idea Generation start instance requests per user for the developer ultra tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_edu_pro_regional/exceeded` BETA ** _(project)_**   
Idea Generation start instance requests per user for the edu pro tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_edu_pro_regional/limit` BETA ** _(project)_**   
Idea Generation start instance requests per user for the edu pro tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_edu_pro_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_edu_pro_regional/usage` BETA ** _(project)_**   
Idea Generation start instance requests per user for the edu pro tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_edu_regional/exceeded` BETA ** _(project)_**   
Idea Generation start instance requests per user for the edu tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_edu_regional/limit` BETA ** _(project)_**   
Idea Generation start instance requests per user for the edu tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_edu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_edu_regional/usage` BETA ** _(project)_**   
Idea Generation start instance requests per user for the edu tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_enterprise_regional/exceeded` BETA ** _(project)_**   
Idea Generation start instance requests per user for the enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_enterprise_regional/limit` BETA ** _(project)_**   
Idea Generation start instance requests per user for the enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_enterprise_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_enterprise_regional/usage` BETA ** _(project)_**   
Idea Generation start instance requests per user for the enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_enterprise_standard_regional/exceeded` BETA ** _(project)_**   
Idea Generation start instance requests per user for the enterprise standard tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_enterprise_standard_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_enterprise_standard_regional/limit` BETA ** _(project)_**   
Idea Generation start instance requests per user for the enterprise standard tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_enterprise_standard_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_enterprise_standard_regional/usage` BETA ** _(project)_**   
Idea Generation start instance requests per user for the enterprise standard tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_enterprise_standard_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_frontline_worker_regional/exceeded` BETA ** _(project)_**   
Idea Generation start instance requests per user for the frontline worker tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_frontline_worker_regional/limit` BETA ** _(project)_**   
Idea Generation start instance requests per user for the frontline worker tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_frontline_worker_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_frontline_worker_regional/usage` BETA ** _(project)_**   
Idea Generation start instance requests per user for the frontline worker tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_starter_regional/exceeded` BETA ** _(project)_**   
Idea Generation start instance requests per user for the starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_starter_regional/limit` BETA ** _(project)_**   
Idea Generation start instance requests per user for the starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/idea_gen_start_instance_tier_starter_regional/usage` BETA ** _(project)_**   
Idea Generation start instance requests per user for the starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/idea_gen_start_instance_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_business_regional/exceeded` BETA ** _(project)_**   
Image generation for business tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_business_regional/limit` BETA ** _(project)_**   
Image generation for business tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_business_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_business_regional/usage` BETA ** _(project)_**   
Image generation for business tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_consumption_only_regional/exceeded` BETA ** _(project)_**   
Image generation for consumption-only tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_consumption_only_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_consumption_only_regional/limit` BETA ** _(project)_**   
Image generation for consumption-only tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_consumption_only_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_consumption_only_regional/usage` BETA ** _(project)_**   
Image generation for consumption-only tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_consumption_only_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Image generation for developer ultra tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Image generation for developer ultra tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Image generation for developer ultra tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_emerging_regional/exceeded` BETA ** _(project)_**   
Image generation for edu emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_emerging_regional/limit` BETA ** _(project)_**   
Image generation for edu emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_emerging_regional/usage` BETA ** _(project)_**   
Image generation for edu emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_pro_emerging_regional/exceeded` BETA ** _(project)_**   
Image generation for edu pro emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_pro_emerging_regional/limit` BETA ** _(project)_**   
Image generation for edu pro emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_pro_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_pro_emerging_regional/usage` BETA ** _(project)_**   
Image generation for edu pro emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_pro_regional/exceeded` BETA ** _(project)_**   
Image generation for edu pro tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_pro_regional/limit` BETA ** _(project)_**   
Image generation for edu pro tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_pro_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_pro_regional/usage` BETA ** _(project)_**   
Image generation for edu pro tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_regional/exceeded` BETA ** _(project)_**   
Image generation for edu tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_regional/limit` BETA ** _(project)_**   
Image generation for edu tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_edu_regional/usage` BETA ** _(project)_**   
Image generation for edu tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_enterprise_emerging_regional/exceeded` BETA ** _(project)_**   
Image generation for enterprise emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_enterprise_emerging_regional/limit` BETA ** _(project)_**   
Image generation for enterprise emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_enterprise_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_enterprise_emerging_regional/usage` BETA ** _(project)_**   
Image generation for enterprise emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_enterprise_plus_regional/exceeded` BETA ** _(project)_**   
Image generation for enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_enterprise_plus_regional/limit` BETA ** _(project)_**   
Image generation for enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_enterprise_plus_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_enterprise_plus_regional/usage` BETA ** _(project)_**   
Image generation for enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_enterprise_regional/exceeded` BETA ** _(project)_**   
Image generation for enterprise tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_enterprise_regional/limit` BETA ** _(project)_**   
Image generation for enterprise tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_enterprise_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_enterprise_regional/usage` BETA ** _(project)_**   
Image generation for enterprise tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_frontline_regional/exceeded` BETA ** _(project)_**   
Image generation for frontline tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_frontline_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_frontline_regional/limit` BETA ** _(project)_**   
Image generation for frontline tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_frontline_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_frontline_regional/usage` BETA ** _(project)_**   
Image generation for frontline tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_frontline_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_frontline_starter_regional/exceeded` BETA ** _(project)_**   
Image generation for frontline starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_frontline_starter_regional/limit` BETA ** _(project)_**   
Image generation for frontline starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_frontline_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_frontline_starter_regional/usage` BETA ** _(project)_**   
Image generation for frontline starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_starter_regional/exceeded` BETA ** _(project)_**   
Image generation for starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/image_gen_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_starter_regional/limit` BETA ** _(project)_**   
Image generation for starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/image_gen_tier_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/image_gen_tier_starter_regional/usage` BETA ** _(project)_**   
Image generation for starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/image_gen_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/ratev2/agentic_wtu_tier_enterprise_plus_pp_weekly_regional/exceeded` BETA ** _(project)_**   
Number of agentic services WTUs weekly per-project for enterprise plus tier windowed rate quota exceeded   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Windowed rate exceeded on quota metric discoveryengine.googleapis.com/agentic_wtu_tier_enterprise_plus_pp_weekly_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`window_size`: window_size.   
`regional_location`: The multi region custom dimension.   
`quota/ratev2/agentic_wtu_tier_enterprise_plus_pp_weekly_regional/limit` BETA ** _(project)_**   
Number of agentic services WTUs weekly per-project for enterprise plus tier windowed rate quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Windowed rate quota limit on quota metric discoveryengine.googleapis.com/agentic_wtu_tier_enterprise_plus_pp_weekly_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`window_size`: window_size.   
`regional_location`: The multi region custom dimension.   
`quota/ratev2/agentic_wtu_tier_enterprise_plus_pp_weekly_regional/net_usage` ALPHA ** _(project)_**   
agentic_wtu_tier_enterprise_plus_pp_weekly_regional usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _The windowed rate usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`method`: The API method name, such as "compute.insert".   
`window_size`: The window size such as \"6h\".   
`window_start_time`: The window start time in seconds since epoch.   
`regional_location`: The number of regional_location items.   
`quota/ratev2/agentic_wtu_tier_enterprise_plus_ppu_weekly_regional/exceeded` BETA ** _(project)_**   
Number of agentic services WTUs weekly per-project per-user for enterprise plus tier windowed rate quota exceeded   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/LocalizedUser](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/LocalizedUser)** |  _Windowed rate exceeded on quota metric discoveryengine.googleapis.com/agentic_wtu_tier_enterprise_plus_ppu_weekly_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`window_size`: window_size.   
`regional_location`: The multi region custom dimension.   
`quota/ratev2/agentic_wtu_tier_enterprise_plus_ppu_weekly_regional/limit` BETA ** _(project)_**   
Number of agentic services WTUs weekly per-project per-user for enterprise plus tier windowed rate quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/LocalizedUser](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/LocalizedUser)** |  _Windowed rate quota limit on quota metric discoveryengine.googleapis.com/agentic_wtu_tier_enterprise_plus_ppu_weekly_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`window_size`: window_size.   
`regional_location`: The multi region custom dimension.   
`quota/ratev2/agentic_wtu_tier_enterprise_plus_ppu_weekly_regional/net_usage` ALPHA ** _(project)_**   
agentic_wtu_tier_enterprise_plus_ppu_weekly_regional usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/LocalizedUser](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/LocalizedUser)** |  _The windowed rate usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`method`: The API method name, such as "compute.insert".   
`window_size`: The window size such as \"6h\".   
`window_start_time`: The window start time in seconds since epoch.   
`regional_location`: The number of regional_location items.   
`quota/ratev2/agentic_wtu_tier_enterprise_standard_pp_weekly_regional/exceeded` BETA ** _(project)_**   
Number of agentic services WTUs weekly per-project for enterprise standard tier windowed rate quota exceeded   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Windowed rate exceeded on quota metric discoveryengine.googleapis.com/agentic_wtu_tier_enterprise_standard_pp_weekly_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`window_size`: window_size.   
`regional_location`: The multi region custom dimension.   
`quota/ratev2/agentic_wtu_tier_enterprise_standard_pp_weekly_regional/limit` BETA ** _(project)_**   
Number of agentic services WTUs weekly per-project for enterprise standard tier windowed rate quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Windowed rate quota limit on quota metric discoveryengine.googleapis.com/agentic_wtu_tier_enterprise_standard_pp_weekly_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`window_size`: window_size.   
`regional_location`: The multi region custom dimension.   
`quota/ratev2/agentic_wtu_tier_enterprise_standard_pp_weekly_regional/net_usage` ALPHA ** _(project)_**   
agentic_wtu_tier_enterprise_standard_pp_weekly_regional usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _The windowed rate usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`method`: The API method name, such as "compute.insert".   
`window_size`: The window size such as \"6h\".   
`window_start_time`: The window start time in seconds since epoch.   
`regional_location`: The number of regional_location items.   
`quota/ratev2/agentic_wtu_tier_enterprise_standard_ppu_weekly_regional/exceeded` BETA ** _(project)_**   
Number of agentic services WTUs weekly per-project per-user for enterprise standard tier windowed rate quota exceeded   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/LocalizedUser](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/LocalizedUser)** |  _Windowed rate exceeded on quota metric discoveryengine.googleapis.com/agentic_wtu_tier_enterprise_standard_ppu_weekly_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`window_size`: window_size.   
`regional_location`: The multi region custom dimension.   
`quota/ratev2/agentic_wtu_tier_enterprise_standard_ppu_weekly_regional/limit` BETA ** _(project)_**   
Number of agentic services WTUs weekly per-project per-user for enterprise standard tier windowed rate quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/LocalizedUser](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/LocalizedUser)** |  _Windowed rate quota limit on quota metric discoveryengine.googleapis.com/agentic_wtu_tier_enterprise_standard_ppu_weekly_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`window_size`: window_size.   
`regional_location`: The multi region custom dimension.   
`quota/ratev2/agentic_wtu_tier_enterprise_standard_ppu_weekly_regional/net_usage` ALPHA ** _(project)_**   
agentic_wtu_tier_enterprise_standard_ppu_weekly_regional usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/LocalizedUser](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/LocalizedUser)** |  _The windowed rate usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`method`: The API method name, such as "compute.insert".   
`window_size`: The window size such as \"6h\".   
`window_start_time`: The window start time in seconds since epoch.   
`regional_location`: The number of regional_location items.   
`quota/search_requests_regional/exceeded` BETA ** _(project)_**   
Regional search requests. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/search_requests_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/search_requests_regional/limit` BETA ** _(project)_**   
Regional search requests. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/search_requests_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/search_requests_regional/usage` BETA ** _(project)_**   
Regional search requests. quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/search_requests_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/search_tier_frontline_worker_regional/exceeded` BETA ** _(project)_**   
Enterprise search for frontline worker tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/search_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/search_tier_frontline_worker_regional/limit` BETA ** _(project)_**   
Enterprise search for frontline worker tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/search_tier_frontline_worker_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/search_tier_frontline_worker_regional/usage` BETA ** _(project)_**   
Enterprise search for frontline worker tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/search_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_business_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for business tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_business_regional/limit` BETA ** _(project)_**   
Tasks and actions for business tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_business_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_business_regional/usage` BETA ** _(project)_**   
Tasks and actions for business tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for developer ultra tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Tasks and actions for developer ultra tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Tasks and actions for developer ultra tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_emerging_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for edu emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_emerging_regional/limit` BETA ** _(project)_**   
Tasks and actions for edu emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_emerging_regional/usage` BETA ** _(project)_**   
Tasks and actions for edu emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_pro_emerging_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for edu pro emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_pro_emerging_regional/limit` BETA ** _(project)_**   
Tasks and actions for edu pro emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_pro_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_pro_emerging_regional/usage` BETA ** _(project)_**   
Tasks and actions for edu pro emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_pro_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for edu pro tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_pro_regional/limit` BETA ** _(project)_**   
Tasks and actions for edu pro tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_pro_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_pro_regional/usage` BETA ** _(project)_**   
Tasks and actions for edu pro tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for edu tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_regional/limit` BETA ** _(project)_**   
Tasks and actions for edu tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_edu_regional/usage` BETA ** _(project)_**   
Tasks and actions for edu tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_enterprise_emerging_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for enterprise emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_enterprise_emerging_regional/limit` BETA ** _(project)_**   
Tasks and actions for enterprise emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_enterprise_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_enterprise_emerging_regional/usage` BETA ** _(project)_**   
Tasks and actions for enterprise emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_enterprise_plus_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_enterprise_plus_regional/limit` BETA ** _(project)_**   
Tasks and actions for enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_enterprise_plus_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_enterprise_plus_regional/usage` BETA ** _(project)_**   
Tasks and actions for enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_enterprise_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for enterprise tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_enterprise_regional/limit` BETA ** _(project)_**   
Tasks and actions for enterprise tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_enterprise_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_enterprise_regional/usage` BETA ** _(project)_**   
Tasks and actions for enterprise tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_frontline_starter_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for frontline starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_frontline_starter_regional/limit` BETA ** _(project)_**   
Tasks and actions for frontline starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_frontline_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_frontline_starter_regional/usage` BETA ** _(project)_**   
Tasks and actions for frontline starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_frontline_worker_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for frontline worker tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_frontline_worker_regional/limit` BETA ** _(project)_**   
Tasks and actions for frontline worker tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_frontline_worker_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_frontline_worker_regional/usage` BETA ** _(project)_**   
Tasks and actions for frontline worker tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_starter_regional/exceeded` BETA ** _(project)_**   
Tasks and actions for starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_starter_regional/limit` BETA ** _(project)_**   
Tasks and actions for starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/tasks_and_actions_tier_starter_regional/usage` BETA ** _(project)_**   
Tasks and actions for starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/tasks_and_actions_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_3p_tier_enterprise_plus_regional/exceeded` BETA ** _(project)_**   
Text answer generation on 3P models for enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_3p_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_3p_tier_enterprise_plus_regional/limit` BETA ** _(project)_**   
Text answer generation on 3P models for enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_3p_tier_enterprise_plus_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_3p_tier_enterprise_plus_regional/usage` BETA ** _(project)_**   
Text answer generation on 3P models for enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_3p_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_3p_tier_enterprise_regional/exceeded` BETA ** _(project)_**   
Text answer generation on 3P models for enterprise tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_3p_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_3p_tier_enterprise_regional/limit` BETA ** _(project)_**   
Text answer generation on 3P models for enterprise tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_3p_tier_enterprise_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_3p_tier_enterprise_regional/usage` BETA ** _(project)_**   
Text answer generation on 3P models for enterprise tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_3p_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_business_standard_regional/exceeded` BETA ** _(project)_**   
Text answer generation for business tier standard model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_business_standard_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_business_standard_regional/limit` BETA ** _(project)_**   
Text answer generation for business tier standard model quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_business_standard_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_business_standard_regional/usage` BETA ** _(project)_**   
Text answer generation for business tier standard model quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_business_standard_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_consumption_only_regional/exceeded` BETA ** _(project)_**   
Text answer generation for consumption-only tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_consumption_only_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_consumption_only_regional/limit` BETA ** _(project)_**   
Text answer generation for consumption-only tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_consumption_only_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_consumption_only_regional/usage` BETA ** _(project)_**   
Text answer generation for consumption-only tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_consumption_only_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Text answer generation for developer ultra tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Text answer generation for developer ultra tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Text answer generation for developer ultra tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_emerging_regional/exceeded` BETA ** _(project)_**   
Text answer generation for edu emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_emerging_regional/limit` BETA ** _(project)_**   
Text answer generation for edu emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_emerging_regional/usage` BETA ** _(project)_**   
Text answer generation for edu emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_pro_emerging_regional/exceeded` BETA ** _(project)_**   
Text answer generation for edu pro emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_pro_emerging_regional/limit` BETA ** _(project)_**   
Text answer generation for edu pro emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_pro_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_pro_emerging_regional/usage` BETA ** _(project)_**   
Text answer generation for edu pro emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_pro_regional/exceeded` BETA ** _(project)_**   
Text answer generation for edu pro tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_pro_regional/limit` BETA ** _(project)_**   
Text answer generation for edu pro tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_pro_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_pro_regional/usage` BETA ** _(project)_**   
Text answer generation for edu pro tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_regional/exceeded` BETA ** _(project)_**   
Text answer generation for edu tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_regional/limit` BETA ** _(project)_**   
Text answer generation for edu tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_edu_regional/usage` BETA ** _(project)_**   
Text answer generation for edu tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_enterprise_emerging_regional/exceeded` BETA ** _(project)_**   
Text answer generation for enterprise emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_enterprise_emerging_regional/limit` BETA ** _(project)_**   
Text answer generation for enterprise emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_enterprise_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_enterprise_emerging_regional/usage` BETA ** _(project)_**   
Text answer generation for enterprise emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_enterprise_plus_regional/exceeded` BETA ** _(project)_**   
Text answer generation for enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_enterprise_plus_regional/limit` BETA ** _(project)_**   
Text answer generation for enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_enterprise_plus_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_enterprise_plus_regional/usage` BETA ** _(project)_**   
Text answer generation for enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_enterprise_standard_regional/exceeded` BETA ** _(project)_**   
Text answer generation for enterprise tier standard model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_enterprise_standard_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_enterprise_standard_regional/limit` BETA ** _(project)_**   
Text answer generation for enterprise tier standard model quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_enterprise_standard_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_enterprise_standard_regional/usage` BETA ** _(project)_**   
Text answer generation for enterprise tier standard model quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_enterprise_standard_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_frontline_starter_regional/exceeded` BETA ** _(project)_**   
Text answer generation for frontline starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_frontline_starter_regional/limit` BETA ** _(project)_**   
Text answer generation for frontline starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_frontline_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_frontline_starter_regional/usage` BETA ** _(project)_**   
Text answer generation for frontline starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_frontline_worker_regional/exceeded` BETA ** _(project)_**   
Text answer generation for frontline worker tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_frontline_worker_regional/limit` BETA ** _(project)_**   
Text answer generation for frontline worker tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_frontline_worker_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_frontline_worker_regional/usage` BETA ** _(project)_**   
Text answer generation for frontline worker tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_starter_regional/exceeded` BETA ** _(project)_**   
Text answer generation for starter tier model quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_starter_regional/limit` BETA ** _(project)_**   
Text answer generation for starter tier model quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/text_answer_gen_tier_starter_regional/usage` BETA ** _(project)_**   
Text answer generation for starter tier model quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/text_answer_gen_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/total_document_size_regional/exceeded` BETA ** _(project)_**   
Total stored document size quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/total_document_size_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/total_document_size_regional/limit` BETA ** _(project)_**   
Total stored document size quota limit   
`GAUGE`, `INT64`, `By`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/total_document_size_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/total_document_size_regional/usage` BETA ** _(project)_**   
Total stored document size quota usage   
`GAUGE`, `INT64`, `By`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/total_document_size_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/user_events_regional/exceeded` BETA ** _(project)_**   
Regional number of user events. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/user_events_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/user_events_regional/limit` BETA ** _(project)_**   
Regional number of user events. quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/user_events_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/user_events_regional/usage` BETA ** _(project)_**   
Regional number of user events. quota usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/user_events_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_business_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for business tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_business_regional/limit` BETA ** _(project)_**   
Number of videos generated for business tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_business_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_business_regional/usage` BETA ** _(project)_**   
Number of videos generated for business tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_consumption_only_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for consumption-only tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_consumption_only_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_consumption_only_regional/limit` BETA ** _(project)_**   
Number of videos generated for consumption-only tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_consumption_only_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_consumption_only_regional/usage` BETA ** _(project)_**   
Number of videos generated for consumption-only tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_consumption_only_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for developer ultra tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Number of videos generated for developer ultra tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Number of videos generated for developer ultra tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_emerging_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for edu emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_emerging_regional/limit` BETA ** _(project)_**   
Number of videos generated for edu emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_emerging_regional/usage` BETA ** _(project)_**   
Number of videos generated for edu emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_pro_emerging_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for edu pro emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_pro_emerging_regional/limit` BETA ** _(project)_**   
Number of videos generated for edu pro emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_pro_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_pro_emerging_regional/usage` BETA ** _(project)_**   
Number of videos generated for edu pro emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_pro_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for edu pro tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_pro_regional/limit` BETA ** _(project)_**   
Number of videos generated for edu pro tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_pro_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_pro_regional/usage` BETA ** _(project)_**   
Number of videos generated for edu pro tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for edu tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_regional/limit` BETA ** _(project)_**   
Number of videos generated for edu tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_edu_regional/usage` BETA ** _(project)_**   
Number of videos generated for edu tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_enterprise_emerging_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for enterprise emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_enterprise_emerging_regional/limit` BETA ** _(project)_**   
Number of videos generated for enterprise emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_enterprise_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_enterprise_emerging_regional/usage` BETA ** _(project)_**   
Number of videos generated for enterprise emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_enterprise_plus_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_enterprise_plus_regional/limit` BETA ** _(project)_**   
Number of videos generated for enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_enterprise_plus_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_enterprise_plus_regional/usage` BETA ** _(project)_**   
Number of videos generated for enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_enterprise_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for enterprise tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_enterprise_regional/limit` BETA ** _(project)_**   
Number of videos generated for enterprise tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_enterprise_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_enterprise_regional/usage` BETA ** _(project)_**   
Number of videos generated for enterprise tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_frontline_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for frontline tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_frontline_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_frontline_regional/limit` BETA ** _(project)_**   
Number of videos generated for frontline tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_frontline_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_frontline_regional/usage` BETA ** _(project)_**   
Number of videos generated for frontline tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_frontline_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_frontline_starter_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for frontline starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_frontline_starter_regional/limit` BETA ** _(project)_**   
Number of videos generated for frontline starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_frontline_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_frontline_starter_regional/usage` BETA ** _(project)_**   
Number of videos generated for frontline starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_starter_regional/exceeded` BETA ** _(project)_**   
Number of videos generated for starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_starter_regional/limit` BETA ** _(project)_**   
Number of videos generated for starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_numbers_tier_starter_regional/usage` BETA ** _(project)_**   
Number of videos generated for starter tier quota usage   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_numbers_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_business_regional/exceeded` BETA ** _(project)_**   
Video generation seconds for business tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_business_regional/limit` BETA ** _(project)_**   
Video generation seconds for business tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_tier_business_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_business_regional/usage` BETA ** _(project)_**   
Video generation seconds for business tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_tier_business_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Video generation seconds for developer ultra tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Video generation seconds for developer ultra tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Video generation seconds for developer ultra tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_edu_pro_regional/exceeded` BETA ** _(project)_**   
Video generation seconds for edu pro tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_edu_pro_regional/limit` BETA ** _(project)_**   
Video generation seconds for edu pro tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_tier_edu_pro_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_edu_pro_regional/usage` BETA ** _(project)_**   
Video generation seconds for edu pro tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_edu_regional/exceeded` BETA ** _(project)_**   
Video generation seconds for edu tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_edu_regional/limit` BETA ** _(project)_**   
Video generation seconds for edu tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_tier_edu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_edu_regional/usage` BETA ** _(project)_**   
Video generation seconds for edu tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_enterprise_emerging_regional/exceeded` BETA ** _(project)_**   
Video generation seconds for enterprise emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_enterprise_emerging_regional/limit` BETA ** _(project)_**   
Video generation seconds for enterprise emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_tier_enterprise_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_enterprise_emerging_regional/usage` BETA ** _(project)_**   
Video generation seconds for enterprise emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_enterprise_plus_regional/exceeded` BETA ** _(project)_**   
Video generation seconds for enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_enterprise_plus_regional/limit` BETA ** _(project)_**   
Video generation seconds for enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_tier_enterprise_plus_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_enterprise_plus_regional/usage` BETA ** _(project)_**   
Video generation seconds for enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_enterprise_regional/exceeded` BETA ** _(project)_**   
Video generation seconds for enterprise tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_enterprise_regional/limit` BETA ** _(project)_**   
Video generation seconds for enterprise tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_tier_enterprise_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_enterprise_regional/usage` BETA ** _(project)_**   
Video generation seconds for enterprise tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_starter_regional/exceeded` BETA ** _(project)_**   
Video generation seconds for starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/video_gen_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_starter_regional/limit` BETA ** _(project)_**   
Video generation seconds for starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/video_gen_tier_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/video_gen_tier_starter_regional/usage` BETA ** _(project)_**   
Video generation seconds for starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/video_gen_tier_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_developer_ultra_regional/exceeded` BETA ** _(project)_**   
Web grounding for enterprise for developer ultra tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_developer_ultra_regional/limit` BETA ** _(project)_**   
Web grounding for enterprise for developer ultra tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_developer_ultra_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_developer_ultra_regional/usage` BETA ** _(project)_**   
Web grounding for enterprise for developer ultra tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_developer_ultra_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_emerging_regional/exceeded` BETA ** _(project)_**   
Web grounding for enterprise for edu emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_emerging_regional/limit` BETA ** _(project)_**   
Web grounding for enterprise for edu emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_emerging_regional/usage` BETA ** _(project)_**   
Web grounding for enterprise for edu emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_pro_emerging_regional/exceeded` BETA ** _(project)_**   
Web grounding for enterprise for edu pro emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_pro_emerging_regional/limit` BETA ** _(project)_**   
Web grounding for enterprise for edu pro emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_pro_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_pro_emerging_regional/usage` BETA ** _(project)_**   
Web grounding for enterprise for edu pro emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_pro_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_pro_regional/exceeded` BETA ** _(project)_**   
Web grounding for enterprise for edu pro tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_pro_regional/limit` BETA ** _(project)_**   
Web grounding for enterprise for edu pro tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_pro_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_pro_regional/usage` BETA ** _(project)_**   
Web grounding for enterprise for edu pro tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_pro_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_regional/exceeded` BETA ** _(project)_**   
Web grounding for enterprise for edu tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_regional/limit` BETA ** _(project)_**   
Web grounding for enterprise for edu tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_edu_regional/usage` BETA ** _(project)_**   
Web grounding for enterprise for edu tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_edu_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_enterprise_emerging_regional/exceeded` BETA ** _(project)_**   
Web grounding for enterprise for enterprise emerging tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_enterprise_emerging_regional/limit` BETA ** _(project)_**   
Web grounding for enterprise for enterprise emerging tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_enterprise_emerging_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_enterprise_emerging_regional/usage` BETA ** _(project)_**   
Web grounding for enterprise for enterprise emerging tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_enterprise_emerging_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_enterprise_plus_regional/exceeded` BETA ** _(project)_**   
Web grounding for enterprise for enterprise plus tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_enterprise_plus_regional/limit` BETA ** _(project)_**   
Web grounding for enterprise for enterprise plus tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_enterprise_plus_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_enterprise_plus_regional/usage` BETA ** _(project)_**   
Web grounding for enterprise for enterprise plus tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_enterprise_plus_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_enterprise_regional/exceeded` BETA ** _(project)_**   
Web grounding for enterprise for enterprise tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_enterprise_regional/limit` BETA ** _(project)_**   
Web grounding for enterprise for enterprise tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_enterprise_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_enterprise_regional/usage` BETA ** _(project)_**   
Web grounding for enterprise for enterprise tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_enterprise_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_frontline_starter_regional/exceeded` BETA ** _(project)_**   
Web grounding for enterprise for frontline starter tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_frontline_starter_regional/limit` BETA ** _(project)_**   
Web grounding for enterprise for frontline starter tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_frontline_starter_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_frontline_starter_regional/usage` BETA ** _(project)_**   
Web grounding for enterprise for frontline starter tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_frontline_starter_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_frontline_worker_regional/exceeded` BETA ** _(project)_**   
Web grounding for enterprise for frontline worker tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_frontline_worker_regional/limit` BETA ** _(project)_**   
Web grounding for enterprise for frontline worker tier quota limit   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current limit on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_frontline_worker_regional. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`regional_location`: The multi region custom dimension.   
`quota/web_grounding_for_enterprise_tier_frontline_worker_regional/usage` BETA ** _(project)_**   
Web grounding for enterprise for frontline worker tier quota usage   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Current usage on quota metric discoveryengine.googleapis.com/web_grounding_for_enterprise_tier_frontline_worker_regional. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`regional_location`: The multi region custom dimension.   
`search_requests_regional` BETA ** _(project)_**   
Regional search requests.   
`DELTA`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Regional search requests._   
`regional_location`: The multi region custom dimension.   
`tool_total_latencies` BETA ** _(project)_**   
Gemini Enterprise Tool Total Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[discoveryengine.googleapis.com/AgentToolInvocation](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/AgentToolInvocation)** |  _Distribution of total latency of Gemini Enterprise Tool invocations over a 1-minute window. Sampled every 30 seconds. After sampling, data is not visible for up to 330 seconds._   
`status`: The response code as a gRPC status code (e.g. OK, INVALID_ARGUMENT, etc.)   
`user_events_regional` BETA ** _(project)_**   
Regional number of user events.   
`GAUGE`, `INT64`, `1`   
**[discoveryengine.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_discoveryengine.googleapis.com/Location)** |  _Regional number of user events. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`regional_location`: The multi region custom dimension.   
  
### displayvideo

Metrics from [Display & Video 360 API](https://developers.google.com/display-video/api/guides/getting-started/overview). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `displayvideo.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`allocate_requests_per_advertiser` GA ** _(project)_**   
All requests with advertiser id   
`DELTA`, `INT64`, `1`   
**[displayvideo.googleapis.com/Advertiser](https://docs.cloud.google.com/monitoring/api/resources#tag_displayvideo.googleapis.com/Advertiser)** |  _All requests with advertiser id._  
`write_requests_per_advertiser` GA ** _(project)_**   
Write requests with advertiser id   
`DELTA`, `INT64`, `1`   
**[displayvideo.googleapis.com/Advertiser](https://docs.cloud.google.com/monitoring/api/resources#tag_displayvideo.googleapis.com/Advertiser)** |  _Write requests with advertiser id._  
  
### dlp

Metrics from [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `dlp.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`content_bytes_inspected_count` GA ** _(project)_**   
Content bytes inspected   
`DELTA`, `INT64`, `By`   
**[cloud_dlp_project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dlp_project)** |  _Content bytes inspected. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`content_bytes_transformed_count` GA ** _(project)_**   
Content bytes transformed   
`DELTA`, `INT64`, `By`   
**[cloud_dlp_project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dlp_project)** |  _Content bytes transformed. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`finding_count` GA ** _(project)_**   
Findings   
`DELTA`, `INT64`, `1`   
**[cloud_dlp_project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dlp_project)** |  _Number of findings. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`info_type`: The info type of the finding.   
`job_result_count` GA ** _(project)_**   
Job results   
`DELTA`, `INT64`, `1`   
**[cloud_dlp_project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dlp_project)** |  _Job results. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`success`: (BOOL) True if the job result was success and false otherwise.   
`job_trigger_run_count` GA ** _(project)_**   
Job trigger runs   
`DELTA`, `INT64`, `1`   
**[cloud_dlp_project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dlp_project)** |  _Job trigger runs. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`status`: Status of trigger.   
`job_type`: The type of job triggered.   
`storage_bytes_inspected_count` GA ** _(project)_**   
Storage bytes inspected   
`DELTA`, `INT64`, `By`   
**[cloud_dlp_project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dlp_project)** |  _Storage bytes inspected. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`storage_bytes_transformed_count` GA ** _(project)_**   
Storage bytes transformed   
`DELTA`, `INT64`, `By`   
**[cloud_dlp_project](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_dlp_project)** |  _Storage bytes transformed. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
  
### dns

Metrics from [Cloud DNS](https://docs.cloud.google.com/dns/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `dns.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`query/latencies` GA ** _(project)_**   
DNS server latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[dns_query](https://docs.cloud.google.com/monitoring/api/resources#tag_dns_query)** |  _Distribution of latency of DNS requests. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`query/response_count` GA ** _(project)_**   
DNS response counts   
`DELTA`, `INT64`, `{request}`   
**[dns_query](https://docs.cloud.google.com/monitoring/api/resources#tag_dns_query)** |  _Rate of all DNS responses from private DNS. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`response_code`: The DNS RCODE of the response, e.g. NOERROR, NXDOMAIN, FORMERR.   
  
### earthengine

Metrics from [Google Earth Engine API](https://earthengine.google.com/). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `earthengine.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`project/cpu/in_progress_usage_time` BETA ** _(project)_**   
In-progress EECU-seconds   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[earthengine.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_earthengine.googleapis.com/Project)** |  _Earth Engine compute usage of all requests in EECU-seconds (https://developers.google.com/earth-engine/guides/computation_overview#eecus). Usage is reported periodically as a request is running. Sampled every 10 seconds._   
`compute_type`: The type of computation. One of [online, batch, highvolume].   
`client_type`: The client type (if known), for example: python/v0.1.300.   
`workload_tag`: The workload tag (if supplied by the user), for example: my-export1.   
`project/cpu/usage_time` BETA ** _(project)_**   
Completed EECU-seconds   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[earthengine.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_earthengine.googleapis.com/Project)** |  _Earth Engine compute usage of successful requests in EECU-seconds (https://developers.google.com/earth-engine/guides/computation_overview#eecus). Usage is reported when a request completes._   
`compute_type`: The type of computation. One of [online, batch, highvolume].   
`client_type`: The client type (if known), for example: python/v0.1.300.   
`workload_tag`: The workload tag (if supplied by the user), for example: my-export1.   
`project/disk/used_bytes` BETA ** _(project)_**   
Used bytes   
`GAUGE`, `INT64`, `By`   
**[earthengine.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_earthengine.googleapis.com/Project)** |  _The number of bytes of asset storage used. Sampled every 1800 seconds._  
  
### edgecache

Metrics from [Media CDN](https://docs.cloud.google.com/media-cdn/docs). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `edgecache.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`edge_cache_route_rule/cmcd/buffer_lengths` GA ** _(project)_**   
Buffer length of the client   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of the client's buffer length._   
`stream_type`: The type of stream being requested, one of [UNKNOWN, VOD, LIVE] with UNKNOWN when the stream type is not reported.   
`device_type`: The device type of the client (currently not implemented and is UNKNOWN).   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`edge_cache_route_rule/cmcd/buffer_starvation_count` GA ** _(project)_**   
Buffer starvation of the client   
`DELTA`, `INT64`, `1`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A count of the client's buffer starvation._   
`stream_type`: The type of stream being requested, one of [UNKNOWN, VOD, LIVE] with UNKNOWN when the stream type is not reported.   
`device_type`: The device type of the client (currently not implemented and is UNKNOWN).   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`edge_cache_route_rule/cmcd/encoded_bitrates` GA ** _(project)_**   
Encoded bitrate of the client   
`DELTA`, `DISTRIBUTION`, `kbit/s`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of the client's encoded bitrate._   
`stream_type`: The type of stream being requested, one of [UNKNOWN, VOD, LIVE] with UNKNOWN when the stream type is not reported.   
`device_type`: The device type of the client (currently not implemented and is UNKNOWN).   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`edge_cache_route_rule/cmcd/encoded_bitrates_over_measured_throughputs` GA ** _(project)_**   
Encoded bitrate over measured throughput of the client   
`DELTA`, `DISTRIBUTION`, `1`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of the client's buffer length._   
`stream_type`: The type of stream being requested, one of [UNKNOWN, VOD, LIVE] with UNKNOWN when the stream type is not reported.   
`device_type`: The device type of the client (currently not implemented and is UNKNOWN).   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`edge_cache_route_rule/cmcd/measured_throughputs` GA ** _(project)_**   
Measured throughput of the client   
`DELTA`, `DISTRIBUTION`, `kbit/s`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of the client's measured throughput._   
`stream_type`: The type of stream being requested, one of [UNKNOWN, VOD, LIVE] with UNKNOWN when the stream type is not reported.   
`device_type`: The device type of the client (currently not implemented and is UNKNOWN).   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`edge_cache_route_rule/cmcd/playback_time_count` GA ** _(project)_**   
Playback time of the client   
`DELTA`, `INT64`, `1`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A count of playback time._   
`stream_type`: The type of stream being requested, one of [UNKNOWN, VOD, LIVE] with UNKNOWN when the stream type is not reported.   
`device_type`: The device type of the client (currently not implemented and is UNKNOWN).   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`edge_cache_route_rule/cmcd/request_count` GA ** _(project)_**   
Requests with CMCD   
`DELTA`, `INT64`, `1`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A count of requests with CMCD._   
`cmcd_version`: The version of CMCD sent in the request, one of [NONE, UNKNOWN, 1] with NONE being no CMCD sent and UNKNOWN being an unknown version.   
`stream_type`: The type of stream being requested, one of [UNKNOWN, VOD, LIVE] with UNKNOWN when the stream type is not reported.   
`device_type`: The device type of the client (currently not implemented and is UNKNOWN).   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`edge_cache_route_rule/frontend_rtt_by_client` GA ** _(project)_**   
Frontend round trip time by client   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Round trip times from the end user to the proxy terminating the request._   
`proxy_continent`: The continent of the proxy terminating the request, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`protocol`: The protocol used by the client, one of [HTTP/1.1, HTTP/2, gQUIC, HTTP/3].   
`edge_cache_route_rule/http_ttfb` GA ** _(project)_**   
HTTP time to first byte   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was received by the proxy until the first byte of the response is sent (not received)._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`tls_version`: The TLS version the client is using to connect, one of [none, TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3].   
`ip_protocol`: The IP protocol the client connected to, one of [IPv4, IPv6].   
`cache_result`: The result returned from the cache, one of [HIT, MISS, PARTIAL, REVALIDATED, STALE, BYPASSED, UNCACHEABLE].   
`protocol`: The protocol used by the client, one of [HTTP/1.1, HTTP/2, gQUIC, HTTP/3].   
`edge_cache_route_rule/http_ttfb_by_client` GA ** _(project)_**   
HTTP time to first byte by client   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was received by the proxy until the first byte of the response is sent (not received) with client location information._   
`proxy_continent`: The continent of the proxy terminating the request, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`protocol`: The protocol used by the client, one of [HTTP/1.1, HTTP/2, gQUIC, HTTP/3].   
`edge_cache_route_rule/http_ttfb_by_client_asn` GA ** _(project)_**   
HTTP time to first byte per client ASN   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was received by the proxy until the first byte of the response is sent (not received). Broken down by client ASN._   
`client_asn`: The client's ASN (Autonomous System Number).   
`edge_cache_route_rule/http_ttfb_by_client_device` GA ** _(project)_**   
HTTP time to first byte per client device   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was received by the proxy until the first byte of the response is sent (not received). Broken down by client device._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`device_request_type`: The type of device used by the client.   
`user_agent_family`: The browser family used by the client.   
`edge_cache_route_rule/http_ttlb` GA ** _(project)_**   
HTTP time to last byte   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was received by the proxy until the last byte of the response is sent (not received)._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`tls_version`: The TLS version the client is using to connect, one of [none, TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3].   
`ip_protocol`: The IP protocol the client connected to, one of [IPv4, IPv6].   
`cache_result`: The result returned from the cache, one of [HIT, MISS, PARTIAL, REVALIDATED, STALE, BYPASSED, UNCACHEABLE].   
`protocol`: The protocol used by the client, one of [HTTP/1.1, HTTP/2, gQUIC, HTTP/3].   
`edge_cache_route_rule/http_ttlb_by_client` GA ** _(project)_**   
HTTP time to last byte by client   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was received by the proxy until the last byte of the response is sent (not received) with client location information._   
`proxy_continent`: The continent of the proxy terminating the request, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`protocol`: The protocol used by the client, one of [HTTP/1.1, HTTP/2, gQUIC, HTTP/3].   
`edge_cache_route_rule/http_ttlb_by_client_asn` GA ** _(project)_**   
HTTP time to last byte per client ASN   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was received by the proxy until the last byte of the response is sent (not received). Broken down by client ASN._   
`client_asn`: The client's ASN (Autonomous System Number).   
`edge_cache_route_rule/http_ttlb_by_client_device` GA ** _(project)_**   
HTTP time to last byte per client device   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was received by the proxy until the last byte of the response is sent (not received). Broken down by client device._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`device_request_type`: The type of device used by the client.   
`user_agent_family`: The browser family used by the client.   
`edge_cache_route_rule/network_actions/wasm_action_invocation_count` BETA ** _(project)_**   
Wasm action invocation count   
`DELTA`, `INT64`, `1`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of WasmAction callbacks invoked._   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`attachment_point`: The point in the request processing flow where the WasmAction was invoked.   
`phase`: The Network Actions processing phase, one of [HTTP_REQUEST_HEADERS, HTTP_RESPONSE_HEADERS].   
`status`: The overall status of the invocation, one of [SUCCESS, ERROR].   
`wasm_action`: The name of the WasmAction resource attached to the EdgeCacheService that was invoked for the request.   
`edge_cache_route_rule/network_actions/wasm_action_invocation_latencies` BETA ** _(project)_**   
Wasm action invocation latencies   
`DELTA`, `DISTRIBUTION`, `us`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies of WasmAction callback invocations._   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`attachment_point`: The point in the request processing flow where the WasmAction was invoked.   
`phase`: The Network Actions processing phase, one of [HTTP_REQUEST_HEADERS, HTTP_RESPONSE_HEADERS].   
`status`: The overall status of the invocation, one of [SUCCESS, ERROR].   
`wasm_action`: The name of the WasmAction resource attached to the EdgeCacheService that was invoked for the request.   
`edge_cache_route_rule/origin_http_ttfb` GA ** _(project)_**   
Origin time to first byte   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was sent by the proxy until the response headers are received from the origin._   
`response_code`: (INT64) The response code from the origin.   
`response_code_class`: The class of the response code from the origin, such as "2xx" or "4xx".   
`proxy_continent`: The continent of the proxy, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`proxy_region`: The region of the proxy, one of [Asia, Europe, India, Latin America, Middle East, North America, Oceania, South Korea & China, Other].   
`protocol`: The protocol used to connect to the origin, one of [HTTP/1.1, HTTP/2, gQUIC, HTTP/3].   
`origin_name`: The name of the origin that produced the response (may be a failover origin).   
`edge_cache_route_rule/origin_http_ttlb` GA ** _(project)_**   
Origin time to last byte   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was sent by the proxy to the origin until the last byte of the response is received from the origin._   
`response_code`: (INT64) The response code from the origin.   
`response_code_class`: The class of the response code from the origin, such as "2xx" or "4xx".   
`proxy_continent`: The continent of the proxy, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`proxy_region`: The region of the proxy, one of [Asia, Europe, India, Latin America, Middle East, North America, Oceania, South Korea & China, Other].   
`protocol`: The protocol used to connect to the origin, one of [HTTP/1.1, HTTP/2, gQUIC, HTTP/3].   
`origin_name`: The name of the origin that produced the response (may be a failover origin).   
`edge_cache_route_rule/origin_request_count` GA ** _(project)_**   
Origin request count   
`DELTA`, `INT64`, `1`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of requests to an origin._   
`response_code`: (INT64) The response code from the origin.   
`response_code_class`: The class of the response code from the origin, such as "2xx" or "4xx".   
`proxy_continent`: The continent of the proxy, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`proxy_region`: The region of the proxy, one of [Asia, Europe, India, Latin America, Middle East, North America, Oceania, South Korea & China, Other].   
`protocol`: The protocol used to connect to the origin, one of [HTTP/1.1, HTTP/2, gQUIC, HTTP/3].   
`origin_name`: The name of the origin that produced the response (may be a failover origin).   
`edge_cache_route_rule/origin_response_bytes_count` GA ** _(project)_**   
Origin response bytes count   
`DELTA`, `INT64`, `By`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of response bytes from an origin._   
`response_code`: (INT64) The response code from the origin.   
`response_code_class`: The class of the response code from the origin, such as "2xx" or "4xx".   
`proxy_continent`: The continent of the proxy, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`proxy_region`: The region of the proxy, one of [Asia, Europe, India, Latin America, Middle East, North America, Oceania, South Korea & China, Other].   
`protocol`: The protocol used to connect to the origin, one of [HTTP/1.1, HTTP/2, gQUIC, HTTP/3].   
`origin_name`: The name of the origin that produced the response (may be a failover origin).   
`edge_cache_route_rule/request_bytes_count` GA ** _(project)_**   
Request bytes count   
`DELTA`, `INT64`, `By`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of request bytes (body and headers)._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`proxy_continent`: The continent of the proxy terminating the request, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`proxy_region`: The region of the proxy terminating the request, one of [Asia, Europe, India, Latin America, Middle East, North America, Oceania, South Korea & China, Other].   
`cache_result`: The result returned from the cache, one of [HIT, MISS, PARTIAL, REVALIDATED, STALE, BYPASSED, UNCACHEABLE].   
`signed_request_mode`: (BOOL) Whether or not the route is expecting signed requests.   
`edge_cache_route_rule/request_bytes_count_by_client` GA ** _(project)_**   
Request bytes count by client   
`DELTA`, `INT64`, `By`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of request bytes (body and headers) with client location information._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`edge_cache_route_rule/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of requests._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`proxy_continent`: The continent of the proxy terminating the request, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`proxy_region`: The region of the proxy terminating the request, one of [Asia, Europe, India, Latin America, Middle East, North America, Oceania, South Korea & China, Other].   
`cache_result`: The result returned from the cache, one of [HIT, MISS, PARTIAL, REVALIDATED, STALE, BYPASSED, UNCACHEABLE].   
`signed_request_mode`: (BOOL) Whether or not the route is expecting signed requests.   
`edge_cache_route_rule/request_count5xx_by_client_asn` GA ** _(project)_**   
Count of 5xx responses by client ASN   
`DELTA`, `INT64`, `1`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of requests with HTTP 5xx responses, broken down by client ASN._   
`client_asn`: The client's ASN (Autonomous System Number).   
`edge_cache_route_rule/request_count_by_blocked` GA ** _(project)_**   
Request count by Cloud Armor action   
`DELTA`, `INT64`, `1`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of requests with client location information and Cloud Armor action._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`blocked_by_cloud_armor`: (BOOL) Whether or not the request was blocked by Cloud Armor.   
`edge_cache_route_rule/request_count_by_client` GA ** _(project)_**   
Request count by client   
`DELTA`, `INT64`, `1`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of requests with client location information._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`cache_result`: The result returned from the cache, one of [HIT, MISS, PARTIAL, REVALIDATED, STALE, BYPASSED, UNCACHEABLE].   
`signed_request_mode`: (BOOL) Whether or not the route is expecting signed requests.   
`edge_cache_route_rule/response_bytes_count` GA ** _(project)_**   
Response bytes count   
`DELTA`, `INT64`, `By`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of response bytes._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`proxy_continent`: The continent of the proxy terminating the request, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`proxy_region`: The region of the proxy terminating the request, one of [Asia, Europe, India, Latin America, Middle East, North America, Oceania, South Korea & China, Other].   
`cache_result`: The result returned from the cache, one of [HIT, MISS, PARTIAL, REVALIDATED, STALE, BYPASSED, UNCACHEABLE].   
`signed_request_mode`: (BOOL) Whether or not the route is expecting signed requests.   
`edge_cache_route_rule/response_bytes_count_by_client` GA ** _(project)_**   
Response bytes count by client   
`DELTA`, `INT64`, `By`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _Count of response bytes (body and headers) with client location information._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`client_country`: The country of the user sending the request based on GeoIP.   
`client_continent`: The continent of the user sending the request based on GeoIP, one of [Africa, Asia, Europe, North America, South America, Other].   
`edge_cache_route_rule/total_latencies` GA ** _(project)_**   
Total latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was received by the proxy until the proxy got ACK from client on last response byte._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`cache_result`: The result returned from the cache, one of [HIT, MISS, PARTIAL, REVALIDATED, STALE, BYPASSED, UNCACHEABLE].   
`protocol`: The protocol used by the client, one of [HTTP/1.1, HTTP/2, gQUIC, HTTP/3].   
`tls_version`: The TLS version the client is using to connect, one of [none, TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3].   
`ip_protocol`: The IP protocol the client connected to, one of [IPv4, IPv6].   
`edge_cache_route_rule/total_latencies_by_proxy` GA ** _(project)_**   
Total latencies by proxy   
`DELTA`, `DISTRIBUTION`, `ms`   
**[edgecache.googleapis.com/EdgeCacheRouteRule](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecache.googleapis.com/EdgeCacheRouteRule)** |  _A distribution of latencies calculated from when the request was received by the proxy until the proxy got ACK from client on last response byte. Includes proxy location information._   
`response_code`: (INT64) The response code served to the user.   
`response_code_class`: The class of the response code served to the user, such as "2xx" or "4xx".   
`proxy_country`: The country of the proxy terminating the request.   
`proxy_continent`: The continent of the proxy terminating the request, one of [Africa, Asia, Europe, North America, South America, Oceania, Other].   
`proxy_region`: The region of the proxy terminating the request, one of [Asia, Europe, India, Latin America, Middle East, North America, Oceania, South Korea & China, Other].   
  
### edgecontainer

Metrics from [Google Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/overview). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `edgecontainer.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`edge_cluster/connection_status` GA ** _(project)_**   
Cluster Connection to the Core Network.   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _A metric with a constant 'true' value labeled by Cluster's connection status._   
`status`: Cluster's connection status, such as CONNECTED, SURVIVABILITY or RECONNECTING.   
`edge_cluster/current_cluster_version` GA ** _(project)_**   
Current Cluster Version.   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _A metric with a constant 'true' value labeled by Cluster's current version._   
`version`: The current GDCE product version of the cluster. During an upgrade, this is the old version and will be updated after the upgrade is completed.   
`edge_cluster/fileblock_storage/volume_read_data_per_sec` DEPRECATED ** _(project)_**   
Volume Read Data Count   
`GAUGE`, `DOUBLE`, `Bps`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Bytes read per second._   
`cluster`: The ONTAP cluster for the metric.   
`aggr`: The associated ONTAP aggregate for the metric.   
`node`: The associated ONTAP node for the metric.   
`style`: The style of volume for the metric.   
`svm`: The associated ONTAP SVM for the metric.   
`volume`: The associated volume for the metric.   
`edge_cluster/fileblock_storage/volume_read_latency` DEPRECATED ** _(project)_**   
Volume Read Latency   
`GAUGE`, `DOUBLE`, `us`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Average latency in microseconds for the WAFL filesystem to process read request to the volume; not including request processing or network communication time._   
`cluster`: The ONTAP cluster for the metric.   
`aggr`: The associated ONTAP aggregate for the metric.   
`node`: The associated ONTAP node for the metric.   
`style`: The style of volume for the metric.   
`svm`: The associated ONTAP SVM for the metric.   
`volume`: The associated volume for the metric.   
`edge_cluster/fileblock_storage/volume_read_ops_per_sec` DEPRECATED ** _(project)_**   
Volume read Operations Count   
`GAUGE`, `DOUBLE`, `{ops}/s`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Number of read operations per second from the volume._   
`cluster`: The ONTAP cluster for the metric.   
`aggr`: The associated ONTAP aggregate for the metric.   
`node`: The associated ONTAP node for the metric.   
`style`: The style of volume for the metric.   
`svm`: The associated ONTAP SVM for the metric.   
`volume`: The associated volume for the metric.   
`edge_cluster/fileblock_storage/volume_size_available` DEPRECATED ** _(project)_**   
Volume Available Size   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Bytes available to use (aka unused) for the volume._   
`cluster`: The ONTAP cluster for the metric.   
`aggr`: The associated ONTAP aggregate for the metric.   
`node`: The associated ONTAP node for the metric.   
`style`: The style of volume for the metric.   
`svm`: The associated ONTAP SVM for the metric.   
`volume`: The associated volume for the metric.   
`edge_cluster/fileblock_storage/volume_size_physical` DEPRECATED ** _(project)_**   
Volume Physical Size   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Physical size of the volume, in bytes._   
`cluster`: The ONTAP cluster for the metric.   
`aggr`: The associated ONTAP aggregate for the metric.   
`node`: The associated ONTAP node for the metric.   
`style`: The style of volume for the metric.   
`svm`: The associated ONTAP SVM for the metric.   
`volume`: The associated volume for the metric.   
`edge_cluster/fileblock_storage/volume_size_total` DEPRECATED ** _(project)_**   
Volume Total Size   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Total usable size (in bytes) of the volume, not including WAFL reserve or volume snapshot reserve. If the volume is restricted or offline, a value of 0 is returned._   
`cluster`: The ONTAP cluster for the metric.   
`aggr`: The associated ONTAP aggregate for the metric.   
`node`: The associated ONTAP node for the metric.   
`style`: The style of volume for the metric.   
`svm`: The associated ONTAP SVM for the metric.   
`volume`: The associated volume for the metric.   
`edge_cluster/fileblock_storage/volume_size_used` DEPRECATED ** _(project)_**   
Volume Used Size   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Bytes used by the volume._   
`cluster`: The ONTAP cluster for the metric.   
`aggr`: The associated ONTAP aggregate for the metric.   
`node`: The associated ONTAP node for the metric.   
`style`: The style of volume for the metric.   
`svm`: The associated ONTAP SVM for the metric.   
`volume`: The associated volume for the metric.   
`edge_cluster/fileblock_storage/volume_write_data_per_sec` DEPRECATED ** _(project)_**   
Volume Write Data Count   
`GAUGE`, `DOUBLE`, `Bps`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Bytes written per second._   
`cluster`: The ONTAP cluster for the metric.   
`aggr`: The associated ONTAP aggregate for the metric.   
`node`: The associated ONTAP node for the metric.   
`style`: The style of volume for the metric.   
`svm`: The associated ONTAP SVM for the metric.   
`volume`: The associated volume for the metric.   
`edge_cluster/fileblock_storage/volume_write_latency` DEPRECATED ** _(project)_**   
Volume Write Latency   
`GAUGE`, `DOUBLE`, `us`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Average latency in microseconds for the WAFL filesystem to process write request to the volume; not including request processing or network communication time._   
`cluster`: The ONTAP cluster for the metric.   
`aggr`: The associated ONTAP aggregate for the metric.   
`node`: The associated ONTAP node for the metric.   
`style`: The style of volume for the metric.   
`svm`: The associated ONTAP SVM for the metric.   
`volume`: The associated volume for the metric.   
`edge_cluster/fileblock_storage/volume_write_ops_per_sec` DEPRECATED ** _(project)_**   
Volume Write Operations Count   
`GAUGE`, `DOUBLE`, `{ops}/s`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Number of write operations per second to the volume._   
`cluster`: The ONTAP cluster for the metric.   
`aggr`: The associated ONTAP aggregate for the metric.   
`node`: The associated ONTAP node for the metric.   
`style`: The style of volume for the metric.   
`svm`: The associated ONTAP SVM for the metric.   
`volume`: The associated volume for the metric.   
`edge_cluster/is_ha` GA ** _(project)_**   
If it is a High Availability cluster.   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _If it is a High Availability cluster._  
`edge_cluster/lifecycle_status` GA ** _(project)_**   
Cluster's lifecycle status.   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _A metric with a constant 'true' value labeled by Cluster's lifecycle status._   
`status`: Cluster's lifecycle status such as provisioning or deleting.   
`edge_cluster/object_storage/data_usage_per_tenant` DEPRECATED ** _(project)_**   
Date Usage Per Tenant   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _The amount of space used on StorageGRID per tenant._   
`cluster`: The associated StorageGRID storage cluster for the metric.   
`job`: The associated job for the metric.   
`node`: The associated StorageGRID storage node for the metric.   
`node_id`: The associated StorageGRID storage node ID for the metric.   
`site_id`: The ID of the associated StorageGRID site for the metric.   
`site_name`: The associated StorageGRID site for the metric.   
`service`: The associated StorageGRID service for the metric.   
`tenant_id`: The ID of the associated StorageGRID tenant for the metric.   
`edge_cluster/object_storage/s3_requests_total` DEPRECATED ** _(project)_**   
Storagegrid S3 Requests Total   
`GAUGE`, `INT64`, `1`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _Total number of s3 requests._   
`cluster`: The associated StorageGRID storage cluster for the metric.   
`job`: The associated job for the metric.   
`node`: The associated StorageGRID storage node for the metric.   
`node_id`: The associated StorageGRID storage node ID for the metric.   
`site_id`: The ID of the associated StorageGRID site for the metric.   
`site_name`: The associated StorageGRID site for the metric.   
`operation`: The associated StorageGRID operation for the metric.   
`edge_cluster/object_storage/storage_utilization_data` DEPRECATED ** _(project)_**   
Storage Utilization Data   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _The amount of space used on StorageGRID._   
`cluster`: The associated StorageGRID storage cluster for the metric.   
`job`: The associated job for the metric.   
`node`: The associated StorageGRID storage node for the metric.   
`node_id`: The associated StorageGRID storage node ID for the metric.   
`site_id`: The ID of the associated StorageGRID site for the metric.   
`site_name`: The associated StorageGRID site for the metric.   
`service`: The associated StorageGRID service for the metric.   
`edge_cluster/object_storage/storage_utilization_usable_space` DEPRECATED ** _(project)_**   
Storage Utilization Usable Space   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _The amount of space available for use on StorageGRID._   
`cluster`: The associated StorageGRID storage cluster for the metric.   
`job`: The associated job for the metric.   
`node`: The associated StorageGRID storage node for the metric.   
`node_id`: The associated StorageGRID storage node ID for the metric.   
`site_id`: The ID of the associated StorageGRID site for the metric.   
`site_name`: The associated StorageGRID site for the metric.   
`service`: The associated StorageGRID service for the metric.   
`edge_cluster/shared_deployment_policy` GA ** _(project)_**   
Cluster's control plane shared deployment policy.   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _A metric with a constant 'true' value labeled by Cluster's shared deployment policy._   
`policy`: Defines via policy field whether it is allowed to run user workload on control plane nodes of the cluster: such as SHARED_DEPLOYMENT_POLICY_UNSPECIFIED, ALLOWED, DISALLOWED.   
`edge_cluster/target_cluster_version` GA ** _(project)_**   
Target Cluster Version.   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/EdgeCluster](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeCluster)** |  _A metric with a constant 'true' value labeled by Cluster's intended target version._   
`version`: Intended GDCE version of the cluster.   
`edge_zone/state` GA ** _(project)_**   
State   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/EdgeZone](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/EdgeZone)** |  _The state of the zone, such as 'ACTIVE' if the zone is turned up, 'PREPARING' if the zone is created but not active, etc._   
`state`: The edge zone turnup state.   
`machine/ambient_temperature` BETA ** _(project)_**   
Machine ambient temperature in Celsius   
`GAUGE`, `INT64`, `C`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Machine ambient temperature in Celsius._  
`machine/cluster_assignment` BETA ** _(project)_**   
Machine Cluster Assignment   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _A metric with a constant 'true' value labeled by the cluster the machine belongs to._   
`cluster_name`: The name of the cluster the machine belongs to.   
`edge_zone`: The name of the Edge Zone the machine belongs to.   
`machine/connected` GA ** _(project)_**   
Machine Connected   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Whether the machine is connected to Google._  
`machine/cpu/total_cores` GA ** _(project)_**   
CPU cores   
`GAUGE`, `INT64`, `1`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Total number of CPU cores on the machine._  
`machine/cpu/usage_time` GA ** _(project)_**   
CPU usage   
`CUMULATIVE`, `DOUBLE`, `s{CPU}`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Cumulative CPU usage on all cores in seconds._   
`type`: Either 'system' or 'workload'. Where workload is what the customer is actually running and system is everything else that Google runs to manage the machine.   
`machine/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `%`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Percent of CPU utilization in a machine (between 0-1)._   
`type`: Either 'system' or 'workload'. Where workload is what the customer is actually running and system is everything else that Google runs to manage the machine.   
`machine/disk/total_bytes` GA ** _(project)_**   
Total Disk Size   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Total disk bytes on the machine._  
`machine/disk/used_bytes` GA ** _(project)_**   
Disk Usage   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Total disk bytes used on the machine._  
`machine/disk/utilization` GA ** _(project)_**   
Disk Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Percent of disk bytes utilization in a machine (between 0-1)._  
`machine/gpu/power_consumption` GA ** _(project)_**   
GPU Power Consumption   
`GAUGE`, `DOUBLE`, `watts`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Power consumption of the GPU in Watts._   
`edge_zone`: The name of the Edge Zone the machine belongs to.   
`gpu_id`: Identifier of the GPU.   
`machine/gpu/temperature` GA ** _(project)_**   
GPU Temperature   
`GAUGE`, `INT64`, `Cel`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Temperature of the GPU in Celsius._   
`edge_zone`: The name of the Edge Zone the machine belongs to.   
`gpu_id`: Identifier of the GPU.   
`machine/gpu/total` GA ** _(project)_**   
GPUs   
`GAUGE`, `INT64`, `1`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Number of GPUs in the machine._  
`machine/gpu/utilization` GA ** _(project)_**   
GPU Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _This is the proportion of time in which the GPU was being used._   
`devpath`: dev path of the GPU, uniquely identifying it.   
`machine/led_status` GA ** _(project)_**   
Machine LED Status   
`GAUGE`, `STRING`, ``   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Status of the front panel LED on the machine._   
`edge_zone`: The name of the Edge Zone the machine belongs to.   
`machine/led_status_v2` BETA ** _(project)_**   
Machine LED Status   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Status of the front panel LED on the machine._   
`edge_zone`: The name of the Edge Zone the machine belongs to.   
`status`: Status of the front panel LED on the machine.   
`machine/memory/total_bytes` GA ** _(project)_**   
Total Memory   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Number of bytes of memory in the machine._  
`machine/memory/used_bytes` GA ** _(project)_**   
Memory Usage   
`GAUGE`, `INT64`, `By`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Memory usage in bytes._   
`type`: Either 'system' or 'workload'. Where workload is what the customer is actually running and system is everything else that Google runs to manage the machine.   
`machine/memory/utilization` GA ** _(project)_**   
Memory Utilization   
`GAUGE`, `DOUBLE`, `%`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Percent of memory utilization in a machine (between 0-1)._   
`type`: Either 'system' or 'workload'. Where workload is what the customer is actually running and system is everything else that Google runs to manage the machine.   
`machine/network/connectivity` GA ** _(project)_**   
Connectivity   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Whether the primary NIC has internet connectivity._  
`machine/network/link_speed` GA ** _(project)_**   
Link Speed   
`GAUGE`, `DOUBLE`, `Bps`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Link speed in bytes per second. Only reports data on the primary NIC._  
`machine/network/network_neighbor` BETA ** _(project)_**   
Network Neighbor   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Network neighbor discovered by LLDP._   
`link`: Local interface name.   
`chassis_id`: Remote chassis ID.   
`port_id`: Remote port ID.   
`system_name`: Remote system name.   
`machine/network/received_bytes_count` GA ** _(project)_**   
Received Bytes   
`CUMULATIVE`, `DOUBLE`, `By`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Total network bytes received by the interface. Only reports data on the primary NIC._  
`machine/network/sent_bytes_count` GA ** _(project)_**   
Sent Bytes   
`CUMULATIVE`, `DOUBLE`, `By`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Total network bytes sent by the interface. Only reports data on the primary NIC._  
`machine/network/up` GA ** _(project)_**   
Network Up   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Whether the network interface is up and running or not._   
`interface`: Any of the network devices (including primary and secondary cards) and port.   
`machine/power_consumption` GA ** _(project)_**   
Machine Power Consumption (Watts)   
`GAUGE`, `INT64`, `watts`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Machine power consumption in watts._  
`machine/psu_status` BETA ** _(project)_**   
Machine PSU Status   
`GAUGE`, `STRING`, ``   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Machine PSU status._   
`name`: Identifier of the PSU.   
`serial_number`: Serial number of the PSU.   
`is_redundant`: Whether the PSU is redundant.   
`want_redundancy`: Whether the rack configuration wants redundancy.   
`expected_psu_count`: Number of PSUs expected to be present.   
`machine/psu_status_v2` BETA ** _(project)_**   
Machine PSU Status   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Machine PSU status._   
`name`: Identifier of the PSU.   
`serial_number`: Serial number of the PSU.   
`is_redundant`: Whether the PSU is redundant.   
`want_redundancy`: Whether the rack configuration wants redundancy.   
`expected_psu_count`: Number of PSUs expected to be present.   
`status`: Status of the PSU.   
`machine/restart_count` GA ** _(project)_**   
Machine Restarts   
`CUMULATIVE`, `INT64`, `1`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _Total number of times the machine restarted._  
`machine/uptime` GA ** _(project)_**   
Machine Uptime   
`GAUGE`, `INT64`, `s`   
**[edgecontainer.googleapis.com/Machine](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Machine)** |  _For how long (in seconds) the machine is up._  
`node/current_node_version` GA ** _(project)_**   
Current Node Version   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Node](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Node)** |  _A metric with a constant 'true' value labeled by Node's current version._   
`current_node_version`: The current GDCE product version of the node.   
`node/node_pool_name` GA ** _(project)_**   
Node Pool Name   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Node](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Node)** |  _A metric with a constant 'true' value labeled by Node's nodepool name._   
`node_pool_name`: The name of the node pool the node belongs to.   
`node/node_type` GA ** _(project)_**   
Node Type   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Node](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Node)** |  _A metric with a constant 'true' value labeled by Node's node type._   
`node_type`: The node type of the node, one of [ControlPlaneNode, WorkerNode].   
`node/target_node_version` GA ** _(project)_**   
Target Node Version   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Node](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Node)** |  _A metric with a constant 'true' value labeled by Node's target version._   
`target_node_version`: The target GDCE product version of the node.   
`router/bgp_up` GA ** _(project)_**   
BGP Up   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Rack](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Rack)** |  _Whether the BGP session on the router is up and healthy._   
`router_id`: The identifier for the router. Each rack contains up to two routers.   
`router/connected` GA ** _(project)_**   
Router Connected   
`GAUGE`, `BOOL`, ``   
**[edgecontainer.googleapis.com/Rack](https://docs.cloud.google.com/monitoring/api/resources#tag_edgecontainer.googleapis.com/Rack)** |  _Whether the router is connected to Google._   
`router_id`: The identifier for the router. Each rack contains up to two routers.   
  
### eventarc

Metrics from [Eventarc](https://docs.cloud.google.com/eventarc/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `eventarc.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`quota/enrollments_per_message_bus/exceeded` GA ** _(project)_**   
Enrollments per message bus quota exceeded error   
`DELTA`, `INT64`, `1`   
**[eventarc.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_eventarc.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric eventarc.googleapis.com/enrollments_per_message_bus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`message_bus`: The message bus that the enrollments are attached to.   
`quota/enrollments_per_message_bus/limit` GA ** _(project)_**   
Enrollments per message bus quota limit   
`GAUGE`, `INT64`, `1`   
**[eventarc.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_eventarc.googleapis.com/Location)** |  _Current limit on quota metric eventarc.googleapis.com/enrollments_per_message_bus. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`message_bus`: The message bus that the enrollments are attached to.   
`quota/enrollments_per_message_bus/usage` GA ** _(project)_**   
Enrollments per message bus quota usage   
`GAUGE`, `INT64`, `1`   
**[eventarc.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_eventarc.googleapis.com/Location)** |  _Current usage on quota metric eventarc.googleapis.com/enrollments_per_message_bus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`message_bus`: The message bus that the enrollments are attached to.   
  
### faulttesting

Metrics from [Fault Injection Testing](https://docs.cloud.google.com/fault-injection-testing). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `faulttesting.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`experiment/active` BETA ** _(project)_**   
Active experiments   
`GAUGE`, `INT64`, `{experiment}`   
**[faulttesting.googleapis.com/Experiment](https://docs.cloud.google.com/monitoring/api/resources#tag_faulttesting.googleapis.com/Experiment)** |  _Current number of active Fault Injection experiments. Reports 1 for each active experiment, 0 otherwise. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`fault_type`: The fault type performed by the experiment, one of [CloudSQLFailover, L7LBHTTPFault, GCEFailCompute, GKEFailCompute].   
`experiment/completed_count` BETA ** _(project)_**   
Completed experiments   
`DELTA`, `INT64`, `{experiment}`   
**[faulttesting.googleapis.com/Experiment](https://docs.cloud.google.com/monitoring/api/resources#tag_faulttesting.googleapis.com/Experiment)** |  _Number of completed Fault Injection experiments, since the last sample. Reports 1 for each completed experiment, 0 otherwise._   
`fault_type`: The fault type performed by the experiment, one of [CloudSQLFailover, L7LBHTTPFault, GCEFailCompute, GKEFailCompute].   
  
### file

Metrics from [Filestore](https://docs.cloud.google.com/filestore/docs). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `file.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`instance/time_since_last_replication` GA ** _(project)_**   
RPO   
`GAUGE`, `DOUBLE`, `s`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Current RPO of the active instance replication. The metric is reported per share, and not populated for basic tier instances. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`share_name`: The name of the file share.   
`nfs/server/average_read_latency` GA ** _(project)_**   
Average read latency   
`GAUGE`, `DOUBLE`, `ms`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Average latency for all disk read operations. This metric is not populated for basic tier instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/average_write_latency` GA ** _(project)_**   
Average write latency   
`GAUGE`, `DOUBLE`, `ms`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Average latency for all disk write operations. This metric is not populated for basic tier instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/deleted_bytes_count` GA ** _(project)_**   
Bytes Deleted   
`DELTA`, `INT64`, `By`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Bytes deleted from share. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`file_share`: The name of the file share.   
`nfs/server/domain_reachable` GA ** _(project)_**   
Directory Service network reachable   
`GAUGE`, `BOOL`, ``   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _True if at least one of the directory services domain controllers is reachable. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`nfs/server/free_bytes` GA ** _(project)_**   
Free bytes   
`GAUGE`, `INT64`, `By`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Total free bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/free_bytes_percent` GA ** _(project)_**   
Free disk space percent   
`GAUGE`, `DOUBLE`, `%`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Free disk space as a percentage of the total space. Values are numbers between 0.0 and 100.0. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/free_raw_capacity_percent` GA ** _(project)_**   
Free raw capacity percent   
`GAUGE`, `DOUBLE`, `%`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _The free raw capacity as a percentage of the total space. Values are numbers between 0.0 and 100.0. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`nfs/server/instance_available` GA ** _(project)_**   
LDAP Domain online / Active Directory KRB5 mount   
`GAUGE`, `BOOL`, ``   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _True if LDAP domain is online or Active Directory KRB5 mount is available. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`nfs/server/locks` GA ** _(project)_**   
Lock count   
`GAUGE`, `INT64`, `{lock}`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Number of locks. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`type`: The type of lock is either READ or WRITE.   
`severity`: The severity is either MANDATORY or ADVISORY.   
`class`: The class of lock refers to the method by which the lock was acquired (e.g. FLOCK, POSIX, etc.).   
`nfs/server/metadata_ops_count` GA ** _(project)_**   
Metadata operations count   
`DELTA`, `INT64`, `{operation}`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Count of disk metadata operations. This metric is not populated for basic tier instances. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/procedure_call_count` GA ** _(project)_**   
Procedure call count   
`DELTA`, `INT64`, `1`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _NFS server procedure call count. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`name`: The name of the NFS Server procedure.   
`version`: The version of the NFS protocol.   
`nfs/server/read_bytes_count` GA ** _(project)_**   
Bytes read   
`DELTA`, `INT64`, `By`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Bytes read from disk. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/read_milliseconds_count` GA ** _(project)_**   
Time (in milliseconds) spent on read operations   
`DELTA`, `INT64`, `ms`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Count of milliseconds spent on disk read operations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/read_ops_count` GA ** _(project)_**   
Disk read operation count   
`DELTA`, `INT64`, `{operation}`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Count of disk read operations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/snapshots_used_bytes` GA ** _(project)_**   
Snapshots used bytes   
`GAUGE`, `INT64`, `By`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _The number of bytes used by the snapshots. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/used_bytes` GA ** _(project)_**   
Used bytes   
`GAUGE`, `INT64`, `By`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Used bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/used_bytes_percent` GA ** _(project)_**   
Used space percent   
`GAUGE`, `DOUBLE`, `%`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Used space as a percentage of the total space. Values are numbers between 0.0 and 100.0. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/write_bytes_count` GA ** _(project)_**   
Bytes written   
`DELTA`, `INT64`, `By`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Bytes written to disk. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/write_milliseconds_count` GA ** _(project)_**   
Time (in milliseconds) spent on write operations   
`DELTA`, `INT64`, `ms`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Count of milliseconds spent on disk write operations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
`nfs/server/write_ops_count` GA ** _(project)_**   
Disk write operation count   
`DELTA`, `INT64`, `{operation}`   
**[filestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_filestore_instance)** |  _Count of disk write operations. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`file_share`: The name of the File Share.   
  
### firebaseappcheck

Metrics from [Firebase](https://firebase.google.com/). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `firebaseappcheck.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`resources/verification_count` GA ** _(project)_**   
Firebase App Check resource verification count   
`DELTA`, `INT64`, `1`   
**[firebaseappcheck.googleapis.com/Resource](https://docs.cloud.google.com/monitoring/api/resources#tag_firebaseappcheck.googleapis.com/Resource)** |  _Verifications performed by an integrating service for a target resource._   
`result`: Result of the token verification; one of [ALLOW, DENY].   
`security`: Security property of the request; one of [VALID, CONSUMED, INVALID, MISSING_OUTDATED_CLIENT, MISSING_UNKNOWN_ORIGIN].   
`app_id`: Firebase App ID.   
`services/verdict_count` DEPRECATED ** _(project)_**   
Firebase App Check verdict count   
`DELTA`, `INT64`, `1`   
**[firebaseappcheck.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_firebaseappcheck.googleapis.com/Instance)** |  _Verdicts from performing Firebase App Check verifications._   
`result`: Result of the token verification; one of [ALLOW, DENY].   
`security`: Security property of the request; one of [VALID, CONSUMED, INVALID, MISSING_OUTDATED_CLIENT, MISSING_UNKNOWN_ORIGIN].   
`services/verification_count` GA ** _(project)_**   
Firebase App Check service verification count   
`DELTA`, `INT64`, `1`   
**[firebaseappcheck.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebaseappcheck.googleapis.com/Service)** |  _Verifications performed by an integrating service._   
`result`: Result of the token verification; one of [ALLOW, DENY].   
`security`: Security property of the request; one of [VALID, CONSUMED, INVALID, MISSING_OUTDATED_CLIENT, MISSING_UNKNOWN_ORIGIN].   
`app_id`: Firebase App ID.   
  
### firebaseapphosting

Metrics from [Firebase](https://firebase.google.com/). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `firebaseapphosting.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`backend/request_count` BETA ** _(project)_**   
Request Count   
`DELTA`, `INT64`, `1`   
**[firebaseapphosting.googleapis.com/Backend](https://docs.cloud.google.com/monitoring/api/resources#tag_firebaseapphosting.googleapis.com/Backend)** |  _Count of user requests._   
`cache_hit`: Whether the requests were served from the CDN cache.   
`response_code`: The HTTP response code served to the end user (200, 404, etc.).   
`response_code_class`: The HTTP response code class of the response served to the end user (200, 400, etc.).   
`cdn_metro`: The Cloud CDN metro that this traffic was served out of.   
`domain_name`: The domain name that this traffic was served for.   
`backend/response_bytes_count` BETA ** _(project)_**   
Response Bytes Count   
`DELTA`, `INT64`, `By`   
**[firebaseapphosting.googleapis.com/Backend](https://docs.cloud.google.com/monitoring/api/resources#tag_firebaseapphosting.googleapis.com/Backend)** |  _Bytes sent in response to user requests._   
`cache_hit`: Whether the requests were served from the CDN cache.   
`response_code`: The HTTP response code served to the end user (200, 404, etc.).   
`response_code_class`: The HTTP response code class of the response served to the end user (200, 400, etc.).   
`cdn_metro`: The Cloud CDN metro that this traffic was served out of.   
`domain_name`: The domain name that this traffic was served for.   
  
### firebaseauth

Metrics from [Firebase](https://firebase.google.com/). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `firebaseauth.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`phone_auth/phone_verification_count` GA ** _(project)_**   
Phone Verification Metrics   
`DELTA`, `INT64`, `1`   
**[firebase_auth](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_auth)** |  _Detailed count of phone verification. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tier_name`: Tier name for verified phone number.   
`country_code`: Country code for verified phone number.   
  
### firebasedatabase

Metrics from [Firebase](https://firebase.google.com/). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `firebasedatabase.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`io/database_load` GA ** _(project)_**   
Database Load   
`GAUGE`, `DOUBLE`, `1`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _Fraction of database load, grouped by type. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._   
`type`: The message type that the actor processed.   
`io/persisted_bytes_count` GA ** _(project)_**   
Saved Bytes   
`DELTA`, `INT64`, `By`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _Bytes of data persisted to disk._  
`io/sent_responses_count` GA ** _(project)_**   
Responses sent   
`DELTA`, `INT64`, `1`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _Number of responses sent or broadcasted to clients._  
`io/utilization` GA ** _(project)_**   
I/O utilization   
`GAUGE`, `DOUBLE`, `1`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _Fraction of I/O used. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`network/active_connections` GA ** _(project)_**   
Connections   
`GAUGE`, `INT64`, `1`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _The number of outstanding connections. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`network/api_hits_count` GA ** _(project)_**   
API Hits   
`DELTA`, `INT64`, `1`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _The number of hits against your database grouped by type._   
`operation_type`: The operation type, this lines up with the profiler.   
`network/broadcast_load` GA ** _(project)_**   
Broadcast Load   
`GAUGE`, `DOUBLE`, `1`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _Utilization of the time it takes to prep and send broadcasts to clients. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`network/disabled_for_overages` GA ** _(project)_**   
Disabled for network   
`GAUGE`, `BOOL`, ``   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _Indicates if the Firebase database has been disabled for network overages. Sampled every 900 seconds. After sampling, data is not visible for up to 1800 seconds._  
`network/https_requests_count` GA ** _(project)_**   
HTTPS Requests Received   
`DELTA`, `INT64`, `1`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _Number of HTTPS requests received._   
`reused_ssl_session`: If the SSL Session was reused.   
`network/monthly_sent` GA ** _(project)_**   
Bytes sent monthly   
`GAUGE`, `INT64`, `By`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _The total outgoing bytes sent aggregated and reset monthly. Sampled every 1800 seconds. After sampling, data is not visible for up to 5400 seconds._  
`network/monthly_sent_limit` GA ** _(project)_**   
Bytes sent limit   
`GAUGE`, `INT64`, `By`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _The monthly network limit for the Firebase database. Sampled every 900 seconds. After sampling, data is not visible for up to 1800 seconds._  
`network/sent_bytes_count` GA ** _(project)_**   
Total billed bytes   
`DELTA`, `INT64`, `By`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _The outgoing bandwidth used by the database, including encryption and protocol overhead._  
`network/sent_payload_and_protocol_bytes_count` GA ** _(project)_**   
Payload and Protocol Bytes sent   
`DELTA`, `INT64`, `By`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _The outgoing bandwidth usage without encryption overhead._  
`network/sent_payload_bytes_count` GA ** _(project)_**   
Payload Bytes Sent   
`DELTA`, `INT64`, `By`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _The outgoing bandwidth usage without encryption nor protocol._  
`rules/evaluation_count` GA ** _(project)_**   
Rule evaluations   
`DELTA`, `INT64`, `1`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _The number of Firebase Realtime Database Security Rule evaluations performed in response to write and read requests._   
`request_method`: The request method.   
`ruleset_label`: The ruleset label.   
`result`: The result.   
`storage/disabled_for_overages` GA ** _(project)_**   
Disabled for storage   
`GAUGE`, `BOOL`, ``   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _Indicates if the Firebase database has been disabled for storage overages. Sampled every 86400 seconds. After sampling, data is not visible for up to 86400 seconds._  
`storage/limit` GA ** _(project)_**   
Bytes stored limit   
`GAUGE`, `INT64`, `By`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _The storage limit for the Firebase database. Sampled every 900 seconds. After sampling, data is not visible for up to 1800 seconds._  
`storage/total_bytes` GA ** _(project)_**   
Bytes stored   
`GAUGE`, `INT64`, `By`   
**[firebase_namespace](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_namespace)** |  _The size of the Firebase database storage. Sampled every 86400 seconds. After sampling, data is not visible for up to 86400 seconds._  
  
### firebasedataconnect

Metrics from [Firebase](https://firebase.google.com/). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `firebasedataconnect.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`connector/datasource_latencies` GA ** _(project)_**   
Datasource Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[firebasedataconnect.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Connector)** |  _The latency of the data sources queried by the operations executed._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`datasource_id`: The datasource ID.   
`connector/datasource_request_bytes_count` GA ** _(project)_**   
Datasource Request Bytes   
`DELTA`, `INT64`, `By`   
**[firebasedataconnect.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Connector)** |  _The number of bytes sent to the data source queried by the operations executed._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`datasource_id`: The datasource ID.   
`connector/datasource_response_bytes_count` GA ** _(project)_**   
Datasource Response Bytes   
`DELTA`, `INT64`, `By`   
**[firebasedataconnect.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Connector)** |  _The number of bytes returned by the data source queried by the operations executed._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`datasource_id`: The datasource ID.   
`connector/network/active_connections` GA ** _(project)_**   
Active Realtime Connections   
`GAUGE`, `INT64`, `1`   
**[firebasedataconnect.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Connector)** |  _The number of bidirectional connections maintained for realtime updates. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`connector/network/active_subscriptions` GA ** _(project)_**   
Active Realtime Subscriptions   
`GAUGE`, `INT64`, `1`   
**[firebasedataconnect.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Connector)** |  _The number of active query subscriptions. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`connector/network/sent_bytes_count` GA ** _(project)_**   
Network Data Transferred Out   
`DELTA`, `INT64`, `By`   
**[firebasedataconnect.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Connector)** |  _The number of bytes transferred out._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`connector/operation_count` GA ** _(project)_**   
Operations   
`DELTA`, `INT64`, `1`   
**[firebasedataconnect.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Connector)** |  _The number of operations executed._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`connector/operation_latencies` GA ** _(project)_**   
Operation Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[firebasedataconnect.googleapis.com/Connector](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Connector)** |  _The latency of the operations executed._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`postgrest/network/sent_bytes_count` BETA ** _(project)_**   
PostgREST Network Data Transferred Out   
`DELTA`, `INT64`, `By`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The number of bytes transferred out by PostgREST operations._   
`resource_type`: The targeted resource type: table, view, or function.   
`resource_name`: The name of the targeted resource.   
`http_method`: The HTTP method.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`postgrest/operation_count` BETA ** _(project)_**   
PostgREST Operations   
`DELTA`, `INT64`, `1`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The number of PostgREST operations executed._   
`resource_type`: The targeted resource type: table, view, or function.   
`resource_name`: The name of the targeted resource.   
`http_method`: The HTTP method.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`postgrest/operation_latencies` BETA ** _(project)_**   
PostgREST Operation Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The latency of PostgREST operations._   
`resource_type`: The targeted resource type: table, view, or function.   
`resource_name`: The name of the targeted resource.   
`http_method`: The HTTP method.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`service/datasource_latencies` DEPRECATED ** _(project)_**   
Datasource Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The latency of the data sources queried by operations executed (same as connector/datasource_latencies, but without connector_id label)._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`datasource_id`: The datasource ID.   
`service/datasource_request_bytes_count` DEPRECATED ** _(project)_**   
Datasource Request Bytes   
`DELTA`, `INT64`, `By`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The number of bytes sent to the data source queried by operations executed (same as connector/datasource_request_bytes_count, but without connector_id label)._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`datasource_id`: The datasource ID.   
`service/datasource_response_bytes_count` DEPRECATED ** _(project)_**   
Datasource Response Bytes   
`DELTA`, `INT64`, `By`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The number of bytes returned by the data sources queried by operations executed (same as connector/datasource_response_bytes_count, but without connector_id label)._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`datasource_id`: The datasource ID.   
`service/network/active_connections` DEPRECATED ** _(project)_**   
Active Realtime Connections   
`GAUGE`, `INT64`, `1`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The number of bidirectional connections maintained for realtime updates (same as connector/network/active_connections, but without connector_id label). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`service/network/active_subscriptions` DEPRECATED ** _(project)_**   
Active Realtime Subscriptions   
`GAUGE`, `INT64`, `1`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The number of active query subscriptions (same as connector/network/active_subscriptions, but without connector_id label). Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`service/network/sent_bytes_count` DEPRECATED ** _(project)_**   
Network Data Transfer Out   
`DELTA`, `INT64`, `By`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The number of bytes transferred out by operations executed (same as connector/network/sent_bytes_count, but without connector_id label)._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`service/operation_count` DEPRECATED ** _(project)_**   
Operations   
`DELTA`, `INT64`, `1`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The number of operations executed (same as connector/operation_count, but without connector_id label)._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
`service/operation_latencies` DEPRECATED ** _(project)_**   
Operation Latency   
`DELTA`, `DISTRIBUTION`, `ms`   
**[firebasedataconnect.googleapis.com/Service](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasedataconnect.googleapis.com/Service)** |  _The latency of operations executed (same as connector/operation_latencies, but without connector_id label)._   
`type`: The type of operation.   
`response_code`: The response code for the operation.   
`response_code_class`: The response code class for the operation: 2xx, 3xx, 4xx, 5xx or 0 for none.   
`operation_name`: The name of the operation.   
`client_version`: The client version based on X-Client-Version header.   
`client_platform`: The client platform based on X-Client-Platform header.   
  
### firebaseextensions

Metrics from [Firebase](https://firebase.google.com/). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `firebaseextensions.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`extension/version/active_instances` BETA ** _(project)_**   
Active instances   
`GAUGE`, `INT64`, `1`   
**[firebaseextensions.googleapis.com/ExtensionVersion](https://docs.cloud.google.com/monitoring/api/resources#tag_firebaseextensions.googleapis.com/ExtensionVersion)** |  _The number of active instances of the published extension version. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
  
### firebasehosting

Metrics from [Firebase](https://firebase.google.com/). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `firebasehosting.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`network/monthly_sent` GA ** _(project)_**   
Bytes sent monthly   
`GAUGE`, `INT64`, `By`   
**[firebase_domain](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_domain)** |  _The total outgoing bytes sent, aggregated and reset monthly. Sampled every 28800 seconds. After sampling, data is not visible for up to 4200 seconds._  
`network/monthly_sent_limit` GA ** _(project)_**   
Bytes sent limit   
`GAUGE`, `INT64`, `By`   
**[firebase_domain](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_domain)** |  _The monthly network limit for Firebase Hosting. Sampled every 28800 seconds. After sampling, data is not visible for up to 4200 seconds._  
`network/sent_bytes_count` GA ** _(project)_**   
Bytes sent   
`DELTA`, `INT64`, `By`   
**[firebase_domain](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_domain)** |  _The outgoing bandwidth usage for Firebase Hosting._  
`storage/limit` GA ** _(project)_**   
Bytes stored limit   
`GAUGE`, `INT64`, `By`   
**[firebase_domain](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_domain)** |  _The storage limit for Firebase Hosting. Sampled every 28800 seconds._  
`storage/total_bytes` GA ** _(project)_**   
Bytes stored   
`GAUGE`, `INT64`, `By`   
**[firebase_domain](https://docs.cloud.google.com/monitoring/api/resources#tag_firebase_domain)** |  _The size of the Firebase Hosting storage. Sampled every 28800 seconds._  
  
### firebaseremoteconfig

Metrics from [Firebase Remote Config](https://firebase.google.com/docs/remote-config/). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `firebaseremoteconfig.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`project/fetch_request_count` BETA ** _(project)_**   
Fetch requests   
`DELTA`, `INT64`, `1`   
**[firebaseremoteconfig.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_firebaseremoteconfig.googleapis.com/Project)** |  _Count of fetch requests._   
`app_id`: The Firebase app ID.   
`is_realtime`: Whether the request originated from a realtime config push.   
`namespace`: The namespace of the Remote Config template.   
  
### firebasestorage

Metrics from [Cloud Storage for Firebase](https://firebase.google.com/docs/storage/). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `firebasestorage.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`rules/evaluation_count` GA ** _(project)_**   
Rule evaluations   
`DELTA`, `INT64`, `1`   
**[gcs_bucket](https://docs.cloud.google.com/monitoring/api/resources#tag_gcs_bucket)** |  _The number of Cloud Storage for Firebase Security Rules evaluations performed in response to write or read requests. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`request_method`: The method/operation type of the request: CREATE, UPDATE, or DELETE; or GET, LIST.   
`ruleset_label`: The ruleset label indicating whether it's the current production release.   
`result`: The evaluation result: ALLOW, DENY, or ERROR.   
  
### firebasevertexai

Metrics from [Gemini in Firebase](https://firebase.google.com/docs/vertex-ai) Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `firebasevertexai.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`PromptTemplate/render_count` BETA ** _(project)_**   
Render Count   
`DELTA`, `INT64`, `1`   
**[firebasevertexai.googleapis.com/PromptTemplate](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasevertexai.googleapis.com/PromptTemplate)** |  _The number of attempts to render the template._   
`gcp_firebase_app_id`: The Firebase App ID.   
`gcp_firebase_app_version`: The Firebase App version, such as 1.0.0.   
`gcp_firebase_request_framework_name`: The SDK framework used to make the request, such as `swift_sdk`.   
`gen_ai_firebase_response_status`: `success` or `failure`'.   
`gen_ai_provider_name`: The Generative AI provider, such as `gcp.gen_ai` or `gcp.vertex_ai`.   
`PromptTemplate/render_latency` BETA ** _(project)_**   
Render Latency   
`DELTA`, `DISTRIBUTION`, `1`   
**[firebasevertexai.googleapis.com/PromptTemplate](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasevertexai.googleapis.com/PromptTemplate)** |  _The time spent rendering the template only. It does not include the LLM invocation time._   
`gcp_firebase_app_id`: The Firebase App ID.   
`gcp_firebase_app_version`: The Firebase App version, such as 1.0.0.   
`gcp_firebase_request_framework_name`: The SDK framework used to make the request, such as `swift_sdk`.   
`gen_ai_firebase_response_status`: `success` or `failure`'.   
`gen_ai_provider_name`: The Generative AI provider, such as `gcp.gen_ai` or `gcp.vertex_ai`.   
`model/gen_ai_client_operation_duration` GA ** _(project)_**   
Operation Duration   
`DELTA`, `DISTRIBUTION`, `1`   
**[firebasevertexai.googleapis.com/Model](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasevertexai.googleapis.com/Model)** |  _The duration from request to response._   
`gcp_firebase_app_id`: The Firebase App ID.   
`gcp_firebase_app_version`: The Firebase App version, such as 1.0.0.   
`gcp_firebase_request_framework_name`: The SDK framework used to make the request, such as `swift_sdk`.   
`gen_ai_firebase_response_status`: `success` or `failure`'.   
`gen_ai_operation_name`: The operation name, such as `generate_content`.   
`gen_ai_request_model`: The model specified in the request, such as `gemini-0.0-flash`.   
`gen_ai_response_model`: The specific model that generated the response, such as `gemini-0.0-flash-002`.   
`error_type`: A short string representing the error type, such as `INVALID_ARGUMENT`, `RESOURCE_EXHAUSTED` or `BLOCKED_SAFETY`.   
`model/gen_ai_client_token_usage` GA ** _(project)_**   
Client Token Usage   
`DELTA`, `INT64`, `1`   
**[firebasevertexai.googleapis.com/Model](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasevertexai.googleapis.com/Model)** |  _The number of tokens used in a request/response._   
`gcp_firebase_app_id`: The Firebase App ID.   
`gcp_firebase_app_version`: The Firebase App version, such as 1.0.0.   
`gcp_firebase_request_framework_name`: The SDK framework used to make the request, such as `swift_sdk`.   
`gen_ai_firebase_response_status`: `success` or `failure`'.   
`gen_ai_operation_name`: The operation name, such as `generate_content`.   
`gen_ai_token_type`: The type of token, such as `input`, `output`, or `thinking`.   
`gen_ai_request_model`: The model specified in the request, such as `gemini-0.0-flash`.   
`gen_ai_response_model`: The specific model that generated the response, such as `gemini-0.0-flash-002`.   
`error_type`: A short string representing the error type, such as `INVALID_ARGUMENT`, `RESOURCE_EXHAUSTED` or `BLOCKED_SAFETY`.   
`model/gen_ai_firebase_modality_count` GA ** _(project)_**   
Modality Usage Count   
`DELTA`, `INT64`, `1`   
**[firebasevertexai.googleapis.com/Model](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasevertexai.googleapis.com/Model)** |  _The count of usage of a particular modality._   
`gcp_firebase_app_id`: The Firebase App ID.   
`gcp_firebase_app_version`: The Firebase App version, such as 1.0.0.   
`gcp_firebase_request_framework_name`: The SDK framework used to make the request, such as `swift_sdk`.   
`gen_ai_firebase_response_status`: `success` or `failure`'.   
`gen_ai_firebase_usage_type`: The direction of usage, such as `input` or `output`.   
`gen_ai_firebase_modality_type`: One of the modalities, such as `text`, `image`, `video`, `audio`, or `document`.   
`gen_ai_operation_name`: The operation name, such as `generate_content`.   
`gen_ai_request_model`: The model specified in the request, such as `gemini-0.0-flash`.   
`gen_ai_response_model`: The specific model that generated the response, such as `gemini-0.0-flash-002`.   
`error_type`: A short string representing the error type, such as `INVALID_ARGUMENT`, `RESOURCE_EXHAUSTED` or `BLOCKED_SAFETY`.   
`model/gen_ai_firebase_modality_usage` GA ** _(project)_**   
Modality Token Usage   
`DELTA`, `INT64`, `1`   
**[firebasevertexai.googleapis.com/Model](https://docs.cloud.google.com/monitoring/api/resources#tag_firebasevertexai.googleapis.com/Model)** |  _The count of token usage of a particular modality._   
`gcp_firebase_app_id`: The Firebase App ID.   
`gcp_firebase_app_version`: The Firebase App version, such as 1.0.0.   
`gcp_firebase_request_framework_name`: The SDK framework used to make the request, such as `swift_sdk`.   
`gen_ai_firebase_response_status`: `success` or `failure`'.   
`gen_ai_firebase_usage_type`: The direction of usage, such as `input` or `output`.   
`gen_ai_firebase_modality_type`: One of the modalities, such as `text`, `image`, `video`, `audio`, or `document`.   
`gen_ai_operation_name`: The operation name, such as `generate_content`.   
`gen_ai_request_model`: The model specified in the request, such as `gemini-0.0-flash`.   
`gen_ai_response_model`: The specific model that generated the response, such as `gemini-0.0-flash-002`.   
`error_type`: A short string representing the error type, such as `INVALID_ARGUMENT`, `RESOURCE_EXHAUSTED` or `BLOCKED_SAFETY`.   
  
### firestore

Metrics from [Firestore](https://firebase.google.com/docs/firestore/). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `firestore.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`api/billable_read_units` GA ** _(project)_**   
Billable read units   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _The number of billable read units. These metrics are only available for Firestore databases with Enterprise Edition. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`service`: The API service called, one of ["firestore.googleapis.com", "datastore.googleapis.com"].   
`api_method`: The API method called, for example, "RunQuery" or "MongoDBCompatible.Find".   
`api/billable_realtime_read_units` GA ** _(project)_**   
Billable real-time read units   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _The number of billable real-time read units. This metric is only available for Firestore databases with Enterprise Edition. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`service`: The API service called, one of ["firestore.googleapis.com", "datastore.googleapis.com"].   
`api_method`: The API method called, for example, "RunQuery" or "MongoDBCompatible.Find".   
`api/billable_write_units` GA ** _(project)_**   
Billable write units   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _The number of billable write units. This metric is only available for Firestore databases with Enterprise Edition. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`service`: The API service called, one of ["firestore.googleapis.com", "datastore.googleapis.com"].   
`api_method`: The API method called, for example, "RunQuery" or "MongoDBCompatible.Find".   
`api/request_count` GA ** _(project)_**   
Requests   
`DELTA`, `INT64`, `1`   
**[datastore_request](https://docs.cloud.google.com/monitoring/api/resources#tag_datastore_request)**   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Count of Firestore API calls. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`api_method`: The API method called (for example: BeginTransaction or Commit).   
`response_code`: Operation response code string, derived as a string representation of a HTTP status code (e.g. success, not_found, unavailable).   
`api/request_latencies` GA ** _(project)_**   
Request latencies per database   
`DELTA`, `DISTRIBUTION`, `s`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Non-streaming Firestore v1, Datastore v1 and Datastore v3 request latencies from the frontend. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`service`: The API service called, one of ["firestore.googleapis.com", "datastore.googleapis.com", "datastore-private.googleapis.com"].   
`api_method`: The API method called, for example, "BeginTransaction", "Commit" or "MongoDBCompatible.Find".   
`response_code`: Operation response code string, derived as a string representation of a HTTP status code, for example, "OK", "DEADLINE_EXCEEDED", "ABORTED", "PERMISSION_DENIED", "INVALID_ARGUMENT".   
`composite_indexes_per_database` GA ** _(project)_**   
Composite Indexes Per Database   
`GAUGE`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Current number of composite indexes per database. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`document/billable_managed_delete_write_units` GA ** _(project)_**   
Billable managed delete write units   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _The number of billable managed delete write units. This metric is only available for Firestore databases with Enterprise Edition. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`document/delete_count` GA ** _(project)_**   
Document Deletes   
`DELTA`, `INT64`, `1`   
**[firestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore_instance)** |  _The number of successful document deletes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`module`: The service/module name.   
`version`: The version name.   
`document/delete_ops_count` GA ** _(project)_**   
Document deletes   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _The number of successful document deletes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`document/read_count` GA ** _(project)_**   
Document Reads   
`DELTA`, `INT64`, `1`   
**[firestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore_instance)** |  _The number of successful document reads from queries or lookups. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`module`: The service/module name.   
`version`: The version name.   
`type`: The type of the read (e.g. 'LOOKUP', 'QUERY').   
`document/read_ops_count` GA ** _(project)_**   
Document reads   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _The number of successful document reads from queries or lookups. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`type`: The type of the read, one of [LOOKUP, QUERY].   
`document/ttl_deletion_count` GA ** _(project)_**   
TTL deletion count   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)**   
**[firestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore_instance)** |  _Total count of documents deleted by TTL services. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`document/ttl_expiration_to_deletion_delays` GA ** _(project)_**   
TTL expiration to deletion delays   
`DELTA`, `DISTRIBUTION`, `s`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)**   
**[firestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore_instance)** |  _Time elapsed between when a document with a TTL expired, and when it was actually deleted. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`document/write_count` GA ** _(project)_**   
Document Writes   
`DELTA`, `INT64`, `1`   
**[firestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore_instance)** |  _The number of successful document writes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`module`: The service/module name.   
`version`: The version name.   
`op`: The operation name for the write (e.g. 'CREATE', 'UPDATE').   
`document/write_ops_count` GA ** _(project)_**   
Document writes   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _The number of successful document writes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`op`: The operation name for the write, one of [CREATE, UPDATE].   
`field_configurations_per_database` DEPRECATED ** _(project)_**   
Field Configurations Per Database   
`GAUGE`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Current number of field configurations per database. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`mcp/request_count` BETA ** _(project)_**   
Firestore MCP Request Count   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Count of Firestore MCP calls. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`tool_name`: The name of the MCP tool making the MCP call.   
`response_code`: Operation response code string, derived as a string representation of a HTTP status code (e.g. success, not_found, unavailable).   
`mcp/request_latencies` BETA ** _(project)_**   
Firestore MCP Request Latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Distribution of latencies for Firestore MCP calls. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`tool_name`: The name of the MCP tool making the MCP call.   
`response_code`: Operation response code string, derived as a string representation of a HTTP status code (e.g. success, not_found, unavailable).   
`network/active_connections` GA ** _(project)_**   
Connected Clients   
`GAUGE`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)**   
**[firestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore_instance)** |  _The number of active connections. Each mobile client will have one connection. Each listener in admin SDK will be one connection. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`module`: The service/module name.   
`version`: The version name.   
`network/active_ignite_connections` GA ** _(project)_**   
Active Ignite Connections   
`GAUGE`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _The number of active ignite connections. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`module`: The service/module name.   
`version`: The version name.   
`network/snapshot_listeners` GA ** _(project)_**   
Snapshot Listeners   
`GAUGE`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)**   
**[firestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore_instance)** |  _The number of snapshot listeners currently registered across all connected clients. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`module`: The service/module name.   
`version`: The version name.   
`query_stat/per_query/result_counts` GA ** _(project)_**   
Number of results yielded per query   
`DELTA`, `DISTRIBUTION`, `{result}`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Distribution of number of results yielded per query. Real-time queries are excluded. Note. This metric is for performance observability. It is not relevant to billing calculations. To understand how read operations contribute to your bill, use "firestore.googleapis.com/document/read_ops_count". Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`service`: The API service called, one of ["firestore.googleapis.com", "datastore.googleapis.com"].   
`method`: The API method called, for example, "RunQuery" or "RunAggregationQuery".   
`query_stat/per_query/scanned_documents_counts` GA ** _(project)_**   
Number of documents scanned per query   
`DELTA`, `DISTRIBUTION`, `{document}`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Distribution of number of documents scanned per query. Real-time queries are excluded. Note. This metric is for performance observability. It is not relevant to billing calculations. To understand how read operations contribute to your bill, use "firestore.googleapis.com/document/read_ops_count". Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`service`: The API service called, one of ["firestore.googleapis.com", "datastore.googleapis.com"].   
`method`: The API method called, for example, "RunQuery" or "RunAggregationQuery".   
`query_stat/per_query/scanned_index_entries_counts` GA ** _(project)_**   
Number of index entries scanned per query   
`DELTA`, `DISTRIBUTION`, `{index entry}`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Distribution of number of scanned index entries per query. Real-time queries are excluded. Note. This metric is for performance observability. It is not relevant to billing calculations. To understand how read operations contribute to your bill, use "firestore.googleapis.com/document/read_ops_count". Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`service`: The API service called, one of ["firestore.googleapis.com", "datastore.googleapis.com"].   
`method`: The API method called, for example, "RunQuery" or "RunAggregationQuery".   
`quota/composite_indexes_per_database/exceeded` GA ** _(project)_**   
Composite Indexes Per Database quota exceeded error   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Number of attempts to exceed the limit on quota metric firestore.googleapis.com/composite_indexes_per_database. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/composite_indexes_per_database/limit` GA ** _(project)_**   
Composite Indexes Per Database quota limit   
`GAUGE`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Current limit on quota metric firestore.googleapis.com/composite_indexes_per_database. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/composite_indexes_per_database/usage` GA ** _(project)_**   
Composite Indexes Per Database quota usage   
`GAUGE`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Current usage on quota metric firestore.googleapis.com/composite_indexes_per_database. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`rules/evaluation_count` GA ** _(project)_**   
Rule Evaluations   
`DELTA`, `INT64`, `1`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)**   
**[firestore_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore_instance)** |  _The number of Cloud Firestore Security Rule evaluations performed in response to write (create, update, delete) or read (get, list) requests. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`request_method`: The permission type of the request.   
`ruleset_label`: The ruleset label indicating whether it is the current production release.   
`version`: The version name.   
`module`: The service/module name.   
`result`: The evaluation result: ALLOW, DENY, or ERROR.   
`storage/backups_storage_bytes` GA ** _(project)_**   
Backups Storage Size   
`GAUGE`, `INT64`, `By`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Per database total backup storage size(in bytes). Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage/data_and_index_storage_bytes` GA ** _(project)_**   
Data and Index Storage Size   
`GAUGE`, `INT64`, `By`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Per database data and index storage size(in bytes). Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`storage/pitr_storage_bytes` GA ** _(project)_**   
Point in time recovery Storage Size   
`GAUGE`, `INT64`, `By`   
**[firestore.googleapis.com/Database](https://docs.cloud.google.com/monitoring/api/resources#tag_firestore.googleapis.com/Database)** |  _Per database point in time recovery storage size(in bytes). Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
  
### firewallinsights

Metrics from [Firewall Insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `firewallinsights.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`subnet/all/firewall_hit_count` GA ** _(project)_**   
Firewall All Types Hit Counts   
`DELTA`, `INT64`, `1`   
**[gce_subnetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_subnetwork)** |  _The hit count of various firewalls for network traffic. Please note that this metric applies only to firewalls for which Firewall Logging has been turned on. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`type`: Type of firewall rule, one of [VPC_FIREWALL, NETWORK_FIREWALL_POLICY, HIERARCHICAL_FIREWALL_POLICY ,UNSPECIFIED].   
`firewall_name`: For VPC firewall rules, this is the name of the rule. For hierarchical firewall policies, this is the policy numeric ID. For network firewall policies, this is the name of the policy.   
`firewall_location`: For regional firewall policies the firewall region, otherwisecontains a fixed value "global".   
`priority`: (INT64) Priority of the VPC firewall rule or of the policy rule.   
`subnet/all/firewall_last_used_timestamp` GA ** _(project)_**   
Firewall Last Used Timestamp   
`GAUGE`, `INT64`, `1`   
**[gce_subnetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_subnetwork)** |  _The epoch timestamp (in seconds) of the last time a firewall was used for network traffic. Please note that this metric applies only to firewalls for which Firewall Logging has been turned on. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`type`: Type of firewall rule, one of [VPC_FIREWALL, NETWORK_FIREWALL_POLICY, HIERARCHICAL_FIREWALL_POLICY ,UNSPECIFIED].   
`firewall_name`: For VPC firewall rules, this is the name of the rule. For hierarchical firewall policies, this is the policy numeric ID. For network firewall policies, this is the name of the policy.   
`firewall_location`: For regional firewall policies the firewall region, for global firewall policies contains a fixed value.   
`priority`: (INT64) Priority of the VPC firewall rule or of the policy rule.   
`subnet/firewall_hit_count` GA ** _(project)_**   
Subnet Firewall Hit Counts   
`DELTA`, `INT64`, `1`   
**[gce_subnetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_subnetwork)** |  _The hit count of various firewalls for the traffic corresponding to a subnet. Please note that this metric applies only to firewalls for which Firewall Logging has been turned on. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`network_name`: The name of the network that this subnet belongs to.   
`firewall_name`: The name of firewall to which a hit is attributed.   
`subnet/firewall_last_used_timestamp` GA ** _(project)_**   
Subnet Firewall Last Used Timestamp   
`GAUGE`, `INT64`, `1`   
**[gce_subnetwork](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_subnetwork)** |  _The epoch timestamp (in seconds) of the last time a firewall was used for the traffic corresponding to a subnet. Please note that this metric applies only to firewalls for which Firewall Logging has been turned on. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`network_name`: The name of the network that this subnet belongs to.   
`firewall_name`: The name of firewall to which a hit is attributed.   
`vm/all/firewall_hit_count` GA ** _(project)_**   
Firewall All Types Hit Counts   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The hit count of various firewalls for network traffic. Please note that this metric applies only to firewalls for which Firewall Logging has been turned on. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`type`: Type of firewall rule, one of [VPC_FIREWALL, NETWORK_FIREWALL_POLICY, HIERARCHICAL_FIREWALL_POLICY ,UNSPECIFIED].   
`firewall_name`: For VPC firewall rules, this is the name of the rule. For hierarchical firewall policies, this is the policy numeric ID. For network firewall policies, this is the name of the policy.   
`firewall_location`: For regional firewall policies the firewall region, otherwisecontains a fixed value "global".   
`interface_name`: The vm network interface which the rule was triggered for, such as "nic0".   
`priority`: (INT64) Priority of the VPC firewall rule or of the policy rule.   
`vm/all/firewall_last_used_timestamp` GA ** _(project)_**   
Firewall Last Used Timestamp   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The epoch timestamp (in seconds) of the last time a firewall was used for network traffic. Please note that this metric applies only to firewalls for which Firewall Logging has been turned on. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`type`: Type of firewall rule, one of [VPC_FIREWALL, NETWORK_FIREWALL_POLICY, HIERARCHICAL_FIREWALL_POLICY ,UNSPECIFIED].   
`firewall_name`: For VPC firewall rules, this is the name of the rule. For hierarchical firewall policies, this is the policy numeric ID. For network firewall policies, this is the name of the policy.   
`firewall_location`: For regional firewall policies the firewall region, for global firewall policies contains a fixed value.   
`interface_name`: The vm network interface which the rule was triggered for, such as "nic0".   
`priority`: (INT64) Priority of the VPC firewall rule or of the policy rule.   
`vm/firewall_hit_count` GA ** _(project)_**   
VM Firewall Hit Counts   
`DELTA`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The hit count of various firewalls for the traffic corresponding to a VM. Please note that this metric applies only to firewalls for which Firewall Logging has been turned on. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`firewall_project_id`: The project id that this firewall belongs to. In the shared VPC case, the host project might be different from the instance project that a VM belongs to.   
`firewall_name`: The name of firewall to which a hit is attributed.   
`vm/firewall_last_used_timestamp` GA ** _(project)_**   
VM Firewall Last Used Timestamp   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _The epoch timestamp (in seconds) of the last time a firewall was used for the traffic corresponding to a VM. Please note that this metric applies only to firewalls for which Firewall Logging has been turned on. Sampled every 60 seconds. After sampling, data is not visible for up to 210 seconds._   
`firewall_project_id`: The project id that this firewall belongs to. In the shared VPC case, the host project might be different from the instance project that a VM belongs to.   
`firewall_name`: The name of firewall to which a hit is attributed.   
  
### fleetengine

Metrics from [Google Maps Platform Mobility services](https://developers.google.com/maps/documentation/mobility). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `fleetengine.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`task/billable_shipment_task_count` GA ** _(project)_**   
Billable shipment task count   
`DELTA`, `INT64`, `1`   
**[fleetengine.googleapis.com/DeliveryFleet](https://docs.cloud.google.com/monitoring/api/resources#tag_fleetengine.googleapis.com/DeliveryFleet)** |  _The number of billable shipment tasks completed._   
`country_code`: The task's country code.   
`trip/billable_trip_count` GA ** _(project)_**   
Billable trip count   
`DELTA`, `INT64`, `1`   
**[fleetengine.googleapis.com/Fleet](https://docs.cloud.google.com/monitoring/api/resources#tag_fleetengine.googleapis.com/Fleet)** |  _The number of billable trips reported._   
`country_code`: The trip's country code.   
  
### fpnv

Metrics from [Firebase Phone Number Verification](https://firebase.google.com/docs/phone-number-verification). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `fpnv.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`verification_count` BETA ** _(project)_**   
Verification Attempts   
`DELTA`, `INT64`, `1`   
**[fpnv.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_fpnv.googleapis.com/Project)** |  _Number of phone number verification attempts._   
`method`: Verification method used (API).   
`region_code`: The two-letter region code for the phone number.   
`outcome`: The outcome of the verification attempt.   
`platform`: The platform where verification was requested.   
  
### geminidataanalytics

Metrics from [Gemini Data Analytics](https://docs.cloud.google.com/gemini/data-agents/reference/rest). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `geminidataanalytics.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`agent/created_count` BETA ** _(project)_**   
Agent Created Count   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _The total number of data agents created._   
`status`: The type of error if the final status contains ERROR. Or "OK" if there is no error.   
`chat/conversation/created_count` BETA ** _(project)_**   
Conversation Created Count   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _The total number of conversations created, across all agents._   
`status`: The type of error if the final status contains ERROR. Or "OK" if there is no error.   
`chat/input_token_count` BETA ** _(project)_**   
Input Token Count   
`DELTA`, `INT64`, `{token}`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _The total number of input tokens used, across all conversations / agents._   
`agent_type`: The type of agent (e.g. DEA, CAA_LOOKER, CAA_BQ).   
`model_name`: The name of the model invoked.   
`status`: The type of error if the final status of LLM call contains ERROR. Or the stop reason if there is no error.   
`chat/model/invocation_count` BETA ** _(project)_**   
Model Invocation Count   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _The total number of model invocations, across all conversations / agents._   
`model_name`: The name of the model invoked.   
`status`: The type of error if the final status of LLM call contains ERROR. Or the stop reason if there is no error.   
`chat/model_latencies` BETA ** _(project)_**   
Chat Model Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _A distribution of the time taken for model invocations._   
`agent_type`: The type of agent (e.g. DEA, CAA_LOOKER, CAA_BQ).   
`model_name`: The name of the model invoked.   
`status`: The type of error if the final status of LLM call contains ERROR. Or the stop reason if there is no error.   
`chat/output_token_count` BETA ** _(project)_**   
Output Token Count   
`DELTA`, `INT64`, `{token}`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _The total number of output tokens used, across all conversations / agents._   
`agent_type`: The type of agent (e.g. DEA, CAA_LOOKER, CAA_BQ).   
`model_name`: The name of the model invoked.   
`status`: The type of error if the final status of LLM call contains ERROR. Or the stop reason if there is no error.   
`chat/tool/invocation_count` BETA ** _(project)_**   
Tool Invocation Count   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _The total number of tool invocations, across all conversations / agents._   
`tool_name`: The name of the tool invoked.   
`status`: The type of error if the final status contains ERROR. Or the stop reason if there is no error.   
`chat/tool_latencies` BETA ** _(project)_**   
Chat Tool Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _A distribution of the time taken for tool invocations._   
`tool_name`: The name of the tool invoked.   
`status`: The type of error if the final status contains ERROR. Or "OK" if there is no error.   
`chat/turn_count` BETA ** _(project)_**   
Turn Count   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _The total number of turns processed, across all conversations / agents._   
`status`: The type of error if the final status contains ERROR. Or "OK" if there is no error.   
`chat/turn_latencies` BETA ** _(project)_**   
Turn Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _A distribution of the time taken to complete a turn._   
`status`: The type of error if the final status contains ERROR. Or "OK" if there is no error.   
`quota/a2a/requests_per_agent/exceeded` BETA ** _(project)_**   
A2A requests per agent quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/a2a/requests_per_agent. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_id`: The unique identifier for the singleton agent. All user defined agents share one identifier.   
`quota/a2a/requests_per_agent/limit` BETA ** _(project)_**   
A2A requests per agent quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/a2a/requests_per_agent. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_id`: The unique identifier for the singleton agent. All user defined agents share one identifier.   
`quota/a2a/requests_per_agent/usage` BETA ** _(project)_**   
A2A requests per agent quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/a2a/requests_per_agent. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_id`: The unique identifier for the singleton agent. All user defined agents share one identifier.   
`quota/cost_control/bigquery_ca/agent/paid_input_tokens/exceeded` BETA ** _(project)_**   
Paid Input Tokens per Agent (BigQuery CA Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/agent/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/bigquery_ca/agent/paid_input_tokens/limit` BETA ** _(project)_**   
Paid Input Tokens per Agent (BigQuery CA Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/agent/paid_input_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/bigquery_ca/agent/paid_input_tokens/usage` BETA ** _(project)_**   
Paid Input Tokens per Agent (BigQuery CA Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/agent/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/cost_control/bigquery_ca/agent/paid_output_tokens/exceeded` BETA ** _(project)_**   
Paid Output Tokens per Agent (BigQuery CA Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/agent/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/bigquery_ca/agent/paid_output_tokens/limit` BETA ** _(project)_**   
Paid Output Tokens per Agent (BigQuery CA Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/agent/paid_output_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/bigquery_ca/agent/paid_output_tokens/usage` BETA ** _(project)_**   
Paid Output Tokens per Agent (BigQuery CA Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/agent/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/cost_control/bigquery_ca/user/paid_input_tokens/exceeded` BETA ** _(project)_**   
Paid Input Tokens per User (BigQuery CA Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/user/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/bigquery_ca/user/paid_input_tokens/limit` BETA ** _(project)_**   
Paid Input Tokens per User (BigQuery CA Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/user/paid_input_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/bigquery_ca/user/paid_input_tokens/usage` BETA ** _(project)_**   
Paid Input Tokens per User (BigQuery CA Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/user/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/cost_control/bigquery_ca/user/paid_output_tokens/exceeded` BETA ** _(project)_**   
Paid Output Tokens per User (BigQuery CA Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/user/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/bigquery_ca/user/paid_output_tokens/limit` BETA ** _(project)_**   
Paid Output Tokens per User (BigQuery CA Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/user/paid_output_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/bigquery_ca/user/paid_output_tokens/usage` BETA ** _(project)_**   
Paid Output Tokens per User (BigQuery CA Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/bigquery_ca/user/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/cost_control/database_ca/agent/paid_input_tokens/exceeded` BETA ** _(project)_**   
Paid Input Tokens per Agent (Database CA Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/agent/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/agent/paid_input_tokens/limit` BETA ** _(project)_**   
Paid Input Tokens per Agent (Database CA Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/agent/paid_input_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/agent/paid_input_tokens/usage` BETA ** _(project)_**   
Paid Input Tokens per Agent (Database CA Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/agent/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/agent/paid_output_tokens/exceeded` BETA ** _(project)_**   
Paid Output Tokens per Agent (Database CA Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/agent/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/agent/paid_output_tokens/limit` BETA ** _(project)_**   
Paid Output Tokens per Agent (Database CA Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/agent/paid_output_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/agent/paid_output_tokens/usage` BETA ** _(project)_**   
Paid Output Tokens per Agent (Database CA Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Agent](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Agent)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/agent/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/paid_input_tokens/exceeded` BETA ** _(project)_**   
Paid Input Tokens (Database CA Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/paid_input_tokens/limit` BETA ** _(project)_**   
Paid Input Tokens (Database CA Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/paid_input_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/paid_input_tokens/usage` BETA ** _(project)_**   
Paid Input Tokens (Database CA Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/paid_output_tokens/exceeded` BETA ** _(project)_**   
Paid Output Tokens (Database CA Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/paid_output_tokens/limit` BETA ** _(project)_**   
Paid Output Tokens (Database CA Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/paid_output_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/paid_output_tokens/usage` BETA ** _(project)_**   
Paid Output Tokens (Database CA Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/user/paid_input_tokens/exceeded` BETA ** _(project)_**   
Paid Input Tokens per User (Database CA Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/user/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/user/paid_input_tokens/limit` BETA ** _(project)_**   
Paid Input Tokens per User (Database CA Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/user/paid_input_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/user/paid_input_tokens/usage` BETA ** _(project)_**   
Paid Input Tokens per User (Database CA Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/user/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/user/paid_output_tokens/exceeded` BETA ** _(project)_**   
Paid Output Tokens per User (Database CA Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/user/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/user/paid_output_tokens/limit` BETA ** _(project)_**   
Paid Output Tokens per User (Database CA Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/user/paid_output_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/database_ca/user/paid_output_tokens/usage` BETA ** _(project)_**   
Paid Output Tokens per User (Database CA Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/database_ca/user/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_type`: The Database CA agent type: CAA_ALLOYDB, CAA_SPANNER, CAA_CLOUD_SQL, CAA_BIGTABLE, CAA_FIRESTORE.   
`quota/cost_control/dsa/user/paid_input_tokens/exceeded` BETA ** _(project)_**   
Paid Input Tokens per User (Data Science Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/dsa/user/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/dsa/user/paid_input_tokens/limit` BETA ** _(project)_**   
Paid Input Tokens per User (Data Science Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/dsa/user/paid_input_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/dsa/user/paid_input_tokens/usage` BETA ** _(project)_**   
Paid Input Tokens per User (Data Science Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/dsa/user/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/cost_control/dsa/user/paid_output_tokens/exceeded` BETA ** _(project)_**   
Paid Output Tokens per User (Data Science Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/dsa/user/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/dsa/user/paid_output_tokens/limit` BETA ** _(project)_**   
Paid Output Tokens per User (Data Science Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/dsa/user/paid_output_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`quota/cost_control/dsa/user/paid_output_tokens/usage` BETA ** _(project)_**   
Paid Output Tokens per User (Data Science Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/dsa/user/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`quota/cost_control/querydata/paid_input_tokens/exceeded` BETA ** _(project)_**   
Paid Input Tokens (QueryData Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/paid_input_tokens/limit` BETA ** _(project)_**   
Paid Input Tokens (QueryData Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/paid_input_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/paid_input_tokens/usage` BETA ** _(project)_**   
Paid Input Tokens (QueryData Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/paid_output_tokens/exceeded` BETA ** _(project)_**   
Paid Output Tokens (QueryData Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/paid_output_tokens/limit` BETA ** _(project)_**   
Paid Output Tokens (QueryData Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/paid_output_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/paid_output_tokens/usage` BETA ** _(project)_**   
Paid Output Tokens (QueryData Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/Location)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/user/paid_input_tokens/exceeded` BETA ** _(project)_**   
Paid Input Tokens per User (QueryData Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/user/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/user/paid_input_tokens/limit` BETA ** _(project)_**   
Paid Input Tokens per User (QueryData Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/user/paid_input_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/user/paid_input_tokens/usage` BETA ** _(project)_**   
Paid Input Tokens per User (QueryData Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/user/paid_input_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/user/paid_output_tokens/exceeded` BETA ** _(project)_**   
Paid Output Tokens per User (QueryData Agent) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Number of attempts to exceed the limit on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/user/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/user/paid_output_tokens/limit` BETA ** _(project)_**   
Paid Output Tokens per User (QueryData Agent) quota limit   
`GAUGE`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current limit on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/user/paid_output_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
`quota/cost_control/querydata/user/paid_output_tokens/usage` BETA ** _(project)_**   
Paid Output Tokens per User (QueryData Agent) quota usage   
`DELTA`, `INT64`, `1`   
**[geminidataanalytics.googleapis.com/User](https://docs.cloud.google.com/monitoring/api/resources#tag_geminidataanalytics.googleapis.com/User)** |  _Current usage on quota metric geminidataanalytics.googleapis.com/cost_control/querydata/user/paid_output_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`agent_type`: The QueryData agent type: QD_ALLOYDB, QD_SPANNER, QD_CLOUD_SQL, QD_BIGTABLE, QD_FIRESTORE.   
  
### generativelanguage

Metrics from [Gemini API](https://ai.google.dev/gemini-api/docs/text-generation) Launch stages of these metrics: ALPHA BETA

The "metric type" strings in this table must be prefixed with `generativelanguage.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`generate_content_usage_output_token_count` BETA ** _(project)_**   
Generate content usage output token count   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Generate content usage output token count._   
`model`: The model used.   
`output_modality`: The modality of the output content.   
`thinking_enabled`: Whether thinking was enabled.   
`quota/embed_content_batch_active_concurrent_batches_paid_tier_1/exceeded` ALPHA ** _(project)_**   
Active EmbedContentBatch batches (paid tier 1) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_batches_paid_tier_1. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_batches_paid_tier_1/limit` ALPHA ** _(project)_**   
Active EmbedContentBatch batches (paid tier 1) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_batches_paid_tier_1. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_batches_paid_tier_1/usage` ALPHA ** _(project)_**   
Active EmbedContentBatch batches (paid tier 1) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_batches_paid_tier_1. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_batches_paid_tier_2/exceeded` ALPHA ** _(project)_**   
Active EmbedContentBatch batches (paid tier 2) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_batches_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_batches_paid_tier_2/limit` ALPHA ** _(project)_**   
Active EmbedContentBatch batches (paid tier 2) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_batches_paid_tier_2. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_batches_paid_tier_2/usage` ALPHA ** _(project)_**   
Active EmbedContentBatch batches (paid tier 2) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_batches_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_batches_paid_tier_3/exceeded` ALPHA ** _(project)_**   
Active EmbedContentBatch batches (paid tier 3) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_batches_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_batches_paid_tier_3/limit` ALPHA ** _(project)_**   
Active EmbedContentBatch batches (paid tier 3) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_batches_paid_tier_3. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_batches_paid_tier_3/usage` ALPHA ** _(project)_**   
Active EmbedContentBatch batches (paid tier 3) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_batches_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_tokens_paid_tier_1/exceeded` ALPHA ** _(project)_**   
Active EmbedContentBatch # of tokens (paid tier 1) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_tokens_paid_tier_1. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_tokens_paid_tier_1/limit` ALPHA ** _(project)_**   
Active EmbedContentBatch # of tokens (paid tier 1) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_tokens_paid_tier_1. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_tokens_paid_tier_1/usage` ALPHA ** _(project)_**   
Active EmbedContentBatch # of tokens (paid tier 1) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_tokens_paid_tier_1. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_tokens_paid_tier_2/exceeded` ALPHA ** _(project)_**   
Active EmbedContentBatch # of tokens (paid tier 2) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_tokens_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_tokens_paid_tier_2/limit` ALPHA ** _(project)_**   
Active EmbedContentBatch # of tokens (paid tier 2) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_tokens_paid_tier_2. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_tokens_paid_tier_2/usage` ALPHA ** _(project)_**   
Active EmbedContentBatch # of tokens (paid tier 2) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_tokens_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_tokens_paid_tier_3/exceeded` ALPHA ** _(project)_**   
Active EmbedContentBatch # of tokens (paid tier 3) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_tokens_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_tokens_paid_tier_3/limit` ALPHA ** _(project)_**   
Active EmbedContentBatch # of tokens (paid tier 3) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_tokens_paid_tier_3. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_batch_active_concurrent_tokens_paid_tier_3/usage` ALPHA ** _(project)_**   
Active EmbedContentBatch # of tokens (paid tier 3) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_batch_active_concurrent_tokens_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_free_tier_requests/exceeded` BETA ** _(project)_**   
Embed Content API requests per model for free tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_free_tier_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_free_tier_requests/limit` BETA ** _(project)_**   
Embed Content API requests per model for free tier quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_free_tier_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_free_tier_requests/usage` BETA ** _(project)_**   
Embed Content API requests per model for free tier quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_free_tier_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/embed_content_free_tier_tokens/exceeded` BETA ** _(project)_**   
Embed Content API tokens per model for free tier quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_free_tier_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_free_tier_tokens/limit` BETA ** _(project)_**   
Embed Content API tokens per model for free tier quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_free_tier_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_free_tier_tokens/usage` BETA ** _(project)_**   
Embed Content API tokens per model for free tier quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_free_tier_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/embed_content_paid_tier_2_requests/exceeded` BETA ** _(project)_**   
Embed Content API requests per model for paid tier 2 quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_2_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_2_requests/limit` BETA ** _(project)_**   
Embed Content API requests per model for paid tier 2 quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_2_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_2_requests/usage` BETA ** _(project)_**   
Embed Content API requests per model for paid tier 2 quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_2_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/embed_content_paid_tier_2_tokens/exceeded` BETA ** _(project)_**   
Embed Content API tokens per model for paid tier 2 quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_2_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_2_tokens/limit` BETA ** _(project)_**   
Embed Content API tokens per model for paid tier 2 quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_2_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_2_tokens/usage` BETA ** _(project)_**   
Embed Content API tokens per model for paid tier 2 quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_2_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/embed_content_paid_tier_3_requests/exceeded` BETA ** _(project)_**   
Embed Content API requests per model for paid tier 3 quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_3_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_3_requests/limit` BETA ** _(project)_**   
Embed Content API requests per model for paid tier 3 quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_3_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_3_requests/usage` BETA ** _(project)_**   
Embed Content API requests per model for paid tier 3 quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_3_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/embed_content_paid_tier_3_tokens/exceeded` BETA ** _(project)_**   
Embed Content API tokens per model for paid tier 3 quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_3_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_3_tokens/limit` BETA ** _(project)_**   
Embed Content API tokens per model for paid tier 3 quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_3_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_3_tokens/usage` BETA ** _(project)_**   
Embed Content API tokens per model for paid tier 3 quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_3_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/embed_content_paid_tier_requests/exceeded` BETA ** _(project)_**   
Embed Content API requests per model for paid tier 1 quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_requests/limit` BETA ** _(project)_**   
Embed Content API requests per model for paid tier 1 quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_requests/usage` BETA ** _(project)_**   
Embed Content API requests per model for paid tier 1 quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/embed_content_paid_tier_tokens/exceeded` BETA ** _(project)_**   
Embed Content API tokens per model for paid tier 1 quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_tokens/limit` BETA ** _(project)_**   
Embed Content API tokens per model for paid tier 1 quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_tokens. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/embed_content_paid_tier_tokens/usage` BETA ** _(project)_**   
Embed Content API tokens per model for paid tier 1 quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/embed_content_paid_tier_tokens. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_batches_paid_tier_1/exceeded` ALPHA ** _(project)_**   
Active GenerateContentBatch batches (paid tier 1) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_batches_paid_tier_1. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_batches_paid_tier_1/limit` ALPHA ** _(project)_**   
Active GenerateContentBatch batches (paid tier 1) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_batches_paid_tier_1. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_batches_paid_tier_1/usage` ALPHA ** _(project)_**   
Active GenerateContentBatch batches (paid tier 1) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_batches_paid_tier_1. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_batches_paid_tier_2/exceeded` ALPHA ** _(project)_**   
Active GenerateContentBatch batches (paid tier 2) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_batches_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_batches_paid_tier_2/limit` ALPHA ** _(project)_**   
Active GenerateContentBatch batches (paid tier 2) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_batches_paid_tier_2. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_batches_paid_tier_2/usage` ALPHA ** _(project)_**   
Active GenerateContentBatch batches (paid tier 2) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_batches_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_batches_paid_tier_3/exceeded` ALPHA ** _(project)_**   
Active GenerateContentBatch batches (paid tier 3) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_batches_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_batches_paid_tier_3/limit` ALPHA ** _(project)_**   
Active GenerateContentBatch batches (paid tier 3) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_batches_paid_tier_3. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_batches_paid_tier_3/usage` ALPHA ** _(project)_**   
Active GenerateContentBatch batches (paid tier 3) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_batches_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_tokens_paid_tier_1/exceeded` ALPHA ** _(project)_**   
Active GenerateContentBatch # of tokens (paid tier 1) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_tokens_paid_tier_1. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_tokens_paid_tier_1/limit` ALPHA ** _(project)_**   
Active GenerateContentBatch # of tokens (paid tier 1) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_tokens_paid_tier_1. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_tokens_paid_tier_1/usage` ALPHA ** _(project)_**   
Active GenerateContentBatch # of tokens (paid tier 1) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_tokens_paid_tier_1. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_tokens_paid_tier_2/exceeded` ALPHA ** _(project)_**   
Active GenerateContentBatch # of tokens (paid tier 2) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_tokens_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_tokens_paid_tier_2/limit` ALPHA ** _(project)_**   
Active GenerateContentBatch # of tokens (paid tier 2) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_tokens_paid_tier_2. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_tokens_paid_tier_2/usage` ALPHA ** _(project)_**   
Active GenerateContentBatch # of tokens (paid tier 2) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_tokens_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_tokens_paid_tier_3/exceeded` ALPHA ** _(project)_**   
Active GenerateContentBatch # of tokens (paid tier 3) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_tokens_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_tokens_paid_tier_3/limit` ALPHA ** _(project)_**   
Active GenerateContentBatch # of tokens (paid tier 3) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_tokens_paid_tier_3. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_batch_active_concurrent_tokens_paid_tier_3/usage` ALPHA ** _(project)_**   
Active GenerateContentBatch # of tokens (paid tier 3) quota usage   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_batch_active_concurrent_tokens_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_free_tier_input_token_count/exceeded` BETA ** _(project)_**   
Generate content free tier input token count quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_free_tier_input_token_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_free_tier_input_token_count/limit` BETA ** _(project)_**   
Generate content free tier input token count quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_free_tier_input_token_count. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_free_tier_input_token_count/usage` BETA ** _(project)_**   
Generate content free tier input token count quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_free_tier_input_token_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_free_tier_input_tokens_internal/usage` ALPHA ** _(project)_**   
Generate content free tier input token count for 1P clients quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_free_tier_input_tokens_internal. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_free_tier_requests/exceeded` BETA ** _(project)_**   
Number of requests made to a specific model, in the free tier. quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_free_tier_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_free_tier_requests/limit` BETA ** _(project)_**   
Number of requests made to a specific model, in the free tier. quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_free_tier_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_free_tier_requests/usage` BETA ** _(project)_**   
Number of requests made to a specific model, in the free tier. quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_free_tier_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_free_tier_requests_internal/usage` BETA ** _(project)_**   
Number of requests made to an internal accounting model, in the free tier. quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_free_tier_requests_internal. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_paid_tier_1_input_tokens_internal/usage` ALPHA ** _(project)_**   
Generate content paid tier 1 input token count for 1P clients quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_1_input_tokens_internal. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_paid_tier_1_requests_internal/usage` BETA ** _(project)_**   
Number of requests made to an internal accounting model, in the paid tier 1. quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_1_requests_internal. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_paid_tier_2_input_token_count/exceeded` ALPHA ** _(project)_**   
Generate content paid tier 2 input token count quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_2_input_token_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_paid_tier_2_input_token_count/limit` ALPHA ** _(project)_**   
Generate content paid tier 2 input token count quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_2_input_token_count. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_paid_tier_2_input_token_count/usage` ALPHA ** _(project)_**   
Generate content paid tier 2 input token count quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_2_input_token_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_paid_tier_2_requests/exceeded` ALPHA ** _(project)_**   
Generate content requests per model (paid tier 2) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_2_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_paid_tier_2_requests/limit` ALPHA ** _(project)_**   
Generate content requests per model (paid tier 2) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_2_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_paid_tier_2_requests/usage` ALPHA ** _(project)_**   
Generate content requests per model (paid tier 2) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_2_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_paid_tier_2_requests_internal/usage` BETA ** _(project)_**   
Number of requests made to an internal accounting model, in the paid tier 2. quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_2_requests_internal. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_paid_tier_3_input_token_count/exceeded` ALPHA ** _(project)_**   
Generate content paid tier 3 input token count quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_3_input_token_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_paid_tier_3_input_token_count/limit` ALPHA ** _(project)_**   
Generate content paid tier 3 input token count quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_3_input_token_count. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_paid_tier_3_input_token_count/usage` ALPHA ** _(project)_**   
Generate content paid tier 3 input token count quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_3_input_token_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_paid_tier_3_requests/exceeded` ALPHA ** _(project)_**   
Generate content requests per model (paid tier 3) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_3_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_paid_tier_3_requests/limit` ALPHA ** _(project)_**   
Generate content requests per model (paid tier 3) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_3_requests. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_paid_tier_3_requests/usage` ALPHA ** _(project)_**   
Generate content requests per model (paid tier 3) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_3_requests. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_paid_tier_3_requests_internal/usage` BETA ** _(project)_**   
Number of requests made to an internal accounting model, in the paid tier 3. quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_3_requests_internal. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_paid_tier_input_token_count/exceeded` BETA ** _(project)_**   
Generate content paid tier input token count quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_input_token_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_paid_tier_input_token_count/limit` BETA ** _(project)_**   
Generate content paid tier input token count quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_input_token_count. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_paid_tier_input_token_count/usage` BETA ** _(project)_**   
Generate content paid tier input token count quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_paid_tier_input_token_count. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_content_search_request_usage/exceeded` BETA ** _(project)_**   
GenerateContent search request usage quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_content_search_request_usage. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_search_request_usage/limit` BETA ** _(project)_**   
GenerateContent search request usage quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_content_search_request_usage. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_content_search_request_usage/usage` BETA ** _(project)_**   
GenerateContent search request usage quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_content_search_request_usage. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_requests_per_model/exceeded` BETA ** _(project)_**   
Generate content requests per model (paid tier) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/generate_requests_per_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_requests_per_model/limit` BETA ** _(project)_**   
Generate content requests per model (paid tier) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/generate_requests_per_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/generate_requests_per_model/usage` BETA ** _(project)_**   
Generate content requests per model (paid tier) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_requests_per_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/generate_requests_per_model_per_day_internal/usage` BETA ** _(project)_**   
Number of requests made to an internal accounting model in a day. quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/generate_requests_per_model_per_day_internal. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/map_grounding_request_free_tier/exceeded` BETA ** _(project)_**   
Map grounding request per project per day (free tier) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/map_grounding_request_free_tier. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/map_grounding_request_free_tier/limit` BETA ** _(project)_**   
Map grounding request per project per day (free tier) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/map_grounding_request_free_tier. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/map_grounding_request_free_tier/usage` BETA ** _(project)_**   
Map grounding request per project per day (free tier) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/map_grounding_request_free_tier. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/map_grounding_request_paid/exceeded` BETA ** _(project)_**   
Map grounding request per project per day (paid tier) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/map_grounding_request_paid. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/map_grounding_request_paid/limit` BETA ** _(project)_**   
Map grounding request per project per day (paid tier) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/map_grounding_request_paid. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/map_grounding_request_paid/usage` BETA ** _(project)_**   
Map grounding request per project per day (paid tier) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/map_grounding_request_paid. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model/exceeded` BETA ** _(project)_**   
Predict long running requests per project quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model/limit` BETA ** _(project)_**   
Predict long running requests per project quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model/usage` BETA ** _(project)_**   
Predict long running requests per project quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_free_tier/exceeded` BETA ** _(project)_**   
Predict long running requests per project (free tier) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_free_tier. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_free_tier/limit` BETA ** _(project)_**   
Predict long running requests per project (free tier) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_free_tier. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_free_tier/usage` BETA ** _(project)_**   
Predict long running requests per project (free tier) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_free_tier. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_paid_tier_2/exceeded` BETA ** _(project)_**   
Predict long running requests per project (paid tier 2) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_paid_tier_2/limit` BETA ** _(project)_**   
Predict long running requests per project (paid tier 2) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_paid_tier_2. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_paid_tier_2/usage` BETA ** _(project)_**   
Predict long running requests per project (paid tier 2) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_paid_tier_3/exceeded` BETA ** _(project)_**   
Predict long running requests per project (paid tier 3) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_paid_tier_3/limit` BETA ** _(project)_**   
Predict long running requests per project (paid tier 3) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_paid_tier_3. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_paid_tier_3/usage` BETA ** _(project)_**   
Predict long running requests per project (paid tier 3) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day/exceeded` BETA ** _(project)_**   
Predict long running requests per project per day quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day/limit` BETA ** _(project)_**   
Predict long running requests per project per day quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day/usage` BETA ** _(project)_**   
Predict long running requests per project per day quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day_free_tier/exceeded` BETA ** _(project)_**   
Predict long running requests per project per day (free tier) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day_free_tier. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day_free_tier/limit` BETA ** _(project)_**   
Predict long running requests per project per day (free tier) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day_free_tier. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day_free_tier/usage` BETA ** _(project)_**   
Predict long running requests per project per day (free tier) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day_free_tier. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day_paid_tier_2/exceeded` BETA ** _(project)_**   
Predict long running requests per project per day (paid tier 2) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day_paid_tier_2/limit` BETA ** _(project)_**   
Predict long running requests per project per day (paid tier 2) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day_paid_tier_2. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day_paid_tier_2/usage` BETA ** _(project)_**   
Predict long running requests per project per day (paid tier 2) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day_paid_tier_3/exceeded` BETA ** _(project)_**   
Predict long running requests per project per day (paid tier 3) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day_paid_tier_3/limit` BETA ** _(project)_**   
Predict long running requests per project per day (paid tier 3) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day_paid_tier_3. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_long_running_requests_per_model_per_day_paid_tier_3/usage` BETA ** _(project)_**   
Predict long running requests per project per day (paid tier 3) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_long_running_requests_per_model_per_day_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_requests_free_tier_per_model/exceeded` BETA ** _(project)_**   
Predict requests per model (free tier) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_requests_free_tier_per_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_free_tier_per_model/limit` BETA ** _(project)_**   
Predict requests per model (free tier) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_requests_free_tier_per_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_free_tier_per_model/usage` BETA ** _(project)_**   
Predict requests per model (free tier) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_requests_free_tier_per_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_requests_per_model/exceeded` BETA ** _(project)_**   
Predict requests per model (paid tier 1) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model/limit` BETA ** _(project)_**   
Predict requests per model (paid tier 1) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model/usage` BETA ** _(project)_**   
Predict requests per model (paid tier 1) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_requests_per_model. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_requests_per_model_paid_tier_2/exceeded` BETA ** _(project)_**   
Predict requests per model (paid tier 2) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model_paid_tier_2/limit` BETA ** _(project)_**   
Predict requests per model (paid tier 2) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model_paid_tier_2. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model_paid_tier_2/usage` BETA ** _(project)_**   
Predict requests per model (paid tier 2) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_requests_per_model_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_requests_per_model_paid_tier_3/exceeded` BETA ** _(project)_**   
Predict requests per model (paid tier 3) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model_paid_tier_3/limit` BETA ** _(project)_**   
Predict requests per model (paid tier 3) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model_paid_tier_3. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model_paid_tier_3/usage` BETA ** _(project)_**   
Predict requests per model (paid tier 3) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_requests_per_model_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_requests_per_model_per_day_paid_tier_1/exceeded` BETA ** _(project)_**   
Predict requests per model per day (paid tier 1) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model_per_day_paid_tier_1. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model_per_day_paid_tier_1/limit` BETA ** _(project)_**   
Predict requests per model per day (paid tier 1) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model_per_day_paid_tier_1. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model_per_day_paid_tier_1/usage` BETA ** _(project)_**   
Predict requests per model per day (paid tier 1) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_requests_per_model_per_day_paid_tier_1. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_requests_per_model_per_day_paid_tier_2/exceeded` BETA ** _(project)_**   
Predict requests per model per day (paid tier 2) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model_per_day_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model_per_day_paid_tier_2/limit` BETA ** _(project)_**   
Predict requests per model per day (paid tier 2) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model_per_day_paid_tier_2. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model_per_day_paid_tier_2/usage` BETA ** _(project)_**   
Predict requests per model per day (paid tier 2) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_requests_per_model_per_day_paid_tier_2. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
`quota/predict_requests_per_model_per_day_paid_tier_3/exceeded` BETA ** _(project)_**   
Predict requests per model per day (paid tier 3) quota exceeded error   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model_per_day_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model_per_day_paid_tier_3/limit` BETA ** _(project)_**   
Predict requests per model per day (paid tier 3) quota limit   
`GAUGE`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current limit on quota metric generativelanguage.googleapis.com/predict_requests_per_model_per_day_paid_tier_3. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`model`: The model name.   
`quota/predict_requests_per_model_per_day_paid_tier_3/usage` BETA ** _(project)_**   
Predict requests per model per day (paid tier 3) quota usage   
`DELTA`, `INT64`, `1`   
**[generativelanguage.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_generativelanguage.googleapis.com/Location)** |  _Current usage on quota metric generativelanguage.googleapis.com/predict_requests_per_model_per_day_paid_tier_3. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`method`: method.   
`model`: The model name.   
  
### gkebackup

Metrics from [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `gkebackup.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`backup_completion_times` GA ** _(project)_**   
Backup completion time   
`DELTA`, `DISTRIBUTION`, `s`   
**[gkebackup.googleapis.com/BackupPlan](https://docs.cloud.google.com/monitoring/api/resources#tag_gkebackup.googleapis.com/BackupPlan)** |  _Distribution of the backup completion time._   
`state`: State of the backup, one of [SUCCEEDED, FAILED].   
`backup_created_count` GA ** _(project)_**   
Backup created count   
`DELTA`, `INT64`, `1`   
**[gkebackup.googleapis.com/BackupPlan](https://docs.cloud.google.com/monitoring/api/resources#tag_gkebackup.googleapis.com/BackupPlan)** |  _Count of the backups created under a backupPlan._   
`scheduled`: Whether the backup was created by schedule, one of [true, false].   
`backup_deleted_count` GA ** _(project)_**   
Backup deleted count   
`DELTA`, `INT64`, `1`   
**[gkebackup.googleapis.com/BackupPlan](https://docs.cloud.google.com/monitoring/api/resources#tag_gkebackup.googleapis.com/BackupPlan)** |  _Count of the backups deleted under a backupPlan._   
`scheduled`: Whether the backup was deleted by schedule, one of [true, false].   
`restore_created_count` GA ** _(project)_**   
Restore created count   
`DELTA`, `INT64`, `1`   
**[gkebackup.googleapis.com/RestorePlan](https://docs.cloud.google.com/monitoring/api/resources#tag_gkebackup.googleapis.com/RestorePlan)** |  _Count of the restores created under a restorePlan._  
  
### healthcare

Metrics from [Cloud Healthcare API](https://docs.cloud.google.com/healthcare/docs). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `healthcare.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`pipeline_job/backlog_elements` BETA ** _(project)_**   
Backlog Elements   
`GAUGE`, `INT64`, `1`   
**[healthcare_pipeline_job](https://docs.cloud.google.com/monitoring/api/resources#tag_healthcare_pipeline_job)** |  _The number of unprocessed input elements buffered on a streaming pipeline. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`pipeline_job/processed_element_count` BETA ** _(project)_**   
Processed Element Count   
`DELTA`, `INT64`, `1`   
**[healthcare_pipeline_job](https://docs.cloud.google.com/monitoring/api/resources#tag_healthcare_pipeline_job)** |  _The number of input elements processed by a pipeline, grouped by status. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`response_code`: (INT64) HTTP status code for the processing request.   
  
### hypercomputecluster

Metrics from [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview). Launch stages of these metrics: BETA

The "metric type" strings in this table must be prefixed with `hypercomputecluster.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`slurm/cpus_alloc` BETA ** _(project)_**   
CPUs allocated   
`GAUGE`, `INT64`, `1`   
**[hypercomputecluster.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_hypercomputecluster.googleapis.com/Cluster)** |  _Number of allocated CPUs in the entire cluster._  
`slurm/gpus_utilization` BETA ** _(project)_**   
Utilization of GPUs   
`GAUGE`, `DOUBLE`, `1`   
**[hypercomputecluster.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_hypercomputecluster.googleapis.com/Cluster)** |  _Ratio of allocated GPUs to total GPUs in the entire cluster._  
`slurm/node_cpu_alloc` BETA ** _(project)_**   
Node CPUs allocated   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of CPUs allocated for a node._   
`partition`: Partition the node belongs to.   
`node`: Name of the node.   
`cluster_id`: ID of the cluster the node belongs to.   
`slurm/node_mem_alloc` BETA ** _(project)_**   
Node memory allocated   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Number of memory allocated for a node._   
`partition`: Partition the node belongs to.   
`node`: Name of the node.   
`cluster_id`: ID of the cluster the node belongs to.   
`slurm/node_state` BETA ** _(project)_**   
Node state   
`GAUGE`, `INT64`, `1`   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _State of a node in the cluster._   
`cluster_id`: ID of the cluster the node belongs to.   
`node`: Name of the node.   
`state`: State of the node.   
`reason`: Reason why a node is unavailable (DOWN, DRAINING, or DRAINED).   
`user`: User who set the reason why a node is unavailable.   
`timestamp`: Latest time when the node was set unavailable.   
`partition`: Partition the node belongs to.   
`slurm/nodes_down` BETA ** _(project)_**   
Nodes down   
`GAUGE`, `INT64`, `1`   
**[hypercomputecluster.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_hypercomputecluster.googleapis.com/Cluster)** |  _Number of nodes down in the cluster._   
`partition`: Partition the node belongs to.   
`slurm/queue_failed` BETA ** _(project)_**   
Failed jobs in queue   
`GAUGE`, `INT64`, `1`   
**[hypercomputecluster.googleapis.com/Cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_hypercomputecluster.googleapis.com/Cluster)** |  _Number of failed jobs in queue for the entire cluster._   
`partition`: Partition the job belongs to.   
`reason`: Reason why the job is in a failed state.   
`user`: User who scheduled the job.   
  
Generated at 2026-10-14 20:24:33 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
