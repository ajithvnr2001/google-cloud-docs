---
url: https://docs.cloud.google.com/monitoring/api/metrics_opsagent/
title: Ops Agent metrics \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:00.944128+00:00
---

# Ops Agent metrics  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_opsagent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Ops Agent metrics Stay organized with collections  Save and categorize content based on your preferences. 

When you install the Ops Agent on your VM instances, the agent transmits data for the metric types listed in this document to Monitoring. For information about choosing the right agent, see [Ops Agent overview](https://docs.cloud.google.com/monitoring/agent/ops-agent).

**Important:** You must install the Ops Agent to collect the metrics listed in this document. The legacy Monitoring and Logging agents collect similar metrics; see [Legacy Monitoring and Logging agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent) for the list of legacy these metrics, and Metrics from the Ops Agent and the legacy Monitoring agent for the list of differences.

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

The following table describes differences in the data ingested by the Ops Agent and the legacy Monitoring agent. Metric type, omitting  
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

Metrics from the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent) running on VM instances in Google Cloud.

### agent

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/agent/`. That prefix has been omitted from the entries in the table. 

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
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of API requests from the Monitoring agent. Sampled every 60 seconds._   
`state`: Request state.   
`log_entry_count` GA ** _(project)_**   
Logging Agent Log Entry Count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of log entries written by the Logging agent. Sampled every 60 seconds._   
`response_code`: Numeric response code from both the gRPC and HTTP error spaces.   
`memory_usage` GA ** _(project)_**   
Monitoring Agent Memory Usage   
`GAUGE`, `DOUBLE`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Memory in use by the Monitoring agent. Sampled every 60 seconds._  
`monitoring/point_count` GA ** _(project)_**   
Monitoring Agent Metric Point Count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of metric points written by the agent to Cloud Monitoring. Sampled every 60 seconds._   
`status`: gRPC response code.   
`ops_agent/enabled_receivers` GA ** _(project)_**   
Ops Agent Enabled Receiver Count   
`GAUGE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of enabled logging and metrics receivers in the Ops Agent configuration. Sampled every 60 seconds._   
`receiver_type`: The type of receiver used.   
`telemetry_type`: The type of telemetry ingested by the enabled receiver, one of ['logs', 'metrics']   
`request_count` GA ** _(project)_**   
Logging Agent API Request Count   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Count of API requests from the Logging agent. Sampled every 60 seconds._   
`response_code`: Numeric response code from both the gRPC and HTTP error spaces.   
`uptime` GA ** _(project)_**   
Monitoring/Logging Agent Uptime   
`CUMULATIVE`, `INT64`, `s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gae_app](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_app)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Uptime of Monitoring agent or Logging agent. Sampled every 60 seconds._   
`version`: Agent version.   
  
Table built at 2026-04-05 02:25:45 UTC.

### cpu

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default). Compute Engine also reports [similar metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute), but those come from the hypervisor rather than from inside the VM. Launch stages of these metrics: GA

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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Load average over the last 15 minutes. Sampled every 60 seconds._  
`load_1m` GA ** _(project)_**   
CPU load (1m)   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Load average over the last 1 minute. Sampled every 60 seconds._  
`load_5m` GA ** _(project)_**   
CPU load (5m)   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Load average over the last 5 minutes. Sampled every 60 seconds._  
`usage_time` GA ** _(project)_**   
CPU usage time (OS reported)   
`CUMULATIVE`, `INT64`, `s{CPU}`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total time the CPU spent in different states. This value is reported from inside the VM and can differ from `compute.googleapis.com/instance/cpu/usage_time`, which is reported by the hypervisor for the VM. Sampled every 60 seconds._   
`cpu_number`: CPU number, for example, "0", "1", or "2". This label is only set with certain Monitoring configurations.   
`cpu_state`: CPU state, one of [idle, interrupt, nice, softirq, steal, system, user, wait].   
`utilization` GA ** _(project)_**   
CPU utilization (OS reported)   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Percentage of the total CPU capacity spent in different states. This value is reported from inside the VM and can differ from `compute.googleapis.com/instance/cpu/utilization`, which is reported by the hypervisor for the VM. Sampled every 60 seconds._   
`cpu_number`: CPU number, for example, "0", "1", or "2". This label is only set with certain Monitoring configurations.   
`cpu_state`: CPU state, one of [idle, interrupt, nice, softirq, steal, system, user, wait] on Linux, or [idle, interrupt, system, user] from Windows Ops Agent, or [idle, used] from Windows Monitoring agent.   
  
### disk

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default). Launch stages of these metrics: GA

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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current number of disk bytes used by state and by partition. Summing the values of all states yields the total available disk space. Sampled every 60 seconds._   
`device`: Device name.   
`state`: Type of usage, one of [free, used, reserved].   
`io_time` GA ** _(project)_**   
Disk I/O time   
`CUMULATIVE`, `INT64`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Cumulative time spent while I/O operations are in queue and when the disks are busy. The value of this metric increases when there is at least one I/O operation pending or in progress. This value corresponds to Field 10 in the https://www.kernel.org/doc/Documentation/iostats.txt documentation. Sampled every 60 seconds._   
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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of disk operations by direction. Sampled every 60 seconds._   
`device`: Device name.   
`direction`: Direction, one of [read, write].   
`operation_time` GA ** _(project)_**   
Disk operation time   
`CUMULATIVE`, `INT64`, `ms`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Average time to complete a disk operation multiplied by wall clock time. When aligned as a rate, the value is the average time to complete a disk operation. Sampled every 60 seconds._   
`device`: Device name.   
`direction`: Direction, one of [read, write].   
`pending_operations` GA ** _(project)_**   
Disk pending operations   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current count of pending disk operations. Sampled every 60 seconds._   
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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of disk bytes that have been read. Sampled every 60 seconds._   
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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of disk bytes that have been written. Sampled every 60 seconds._   
`device`: Device name.   
  
### gpu

**Linux only.** Metrics reported by the NVIDIA [Management Library (NVML)](https://developer.nvidia.com/nvidia-management-library-nvml), and collected by the built-in configuration of the Ops Agent for all Cloud GPUs. For more information, see [About the `gpu` metrics](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#receiver-nvml-metrics). Launch stages of these metrics: GA

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/gpu/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`memory/bytes_used` GA ** _(project)_**   
GPU memory usage   
`GAUGE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current number of GPU memory bytes used by state. Summing the values of all states yields the total GPU memory space. Linux only. Sampled every 60 seconds._   
`gpu_number`: GPU number, for example, "0", "1", or "2". The gpu_number matches the CUDA device index. It is not guaranteed to be consistent across reboots. To reference a specific GPU consistently, use the uuid label.   
`uuid`: GPU universally unique identifier.   
`model`: GPU model, for example, "NVIDIA A100-SXM4-40GB". .   
`memory_state`: Memory state, one of [used, free].   
`processes/max_bytes_used` GA ** _(project)_**   
Process maximum GPU memory usage   
`GAUGE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Maximum total GPU memory in bytes that has ever been allocated by the process. Only samples processes alive at time of collection. Not supported for any device in Multi-Instance GPU mode. Linux only. Sampled every 60 seconds._   
`gpu_number`: GPU number, for example, "0", "1", or "2". The gpu_number matches the CUDA device index. It is not guaranteed to be consistent across reboots. To reference a specific GPU consistently, use the uuid label.   
`uuid`: GPU universally unique identifier.   
`model`: GPU model, for example, "NVIDIA A100-SXM4-40GB". .   
`pid`: Process ID.   
`process`: Process name.   
`command`: Process command.   
`command_line`: Process command line, 1024 characters maximum.   
`owner`: Process owner.   
`processes/utilization` GA ** _(project)_**   
Process lifetime GPU utilization   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Percentage of time over the process's lifetime, thus far, during which one or more kernels was executing on the GPU. Only samples processes alive at time of collection. Values are between 0.0 and 100.0. Not supported for any device in Multi-Instance GPU mode. Linux only. Sampled every 60 seconds._   
`gpu_number`: GPU number, for example, "0", "1", or "2". The gpu_number matches the CUDA device index. It is not guaranteed to be consistent across reboots. To reference a specific GPU consistently, use the uuid label.   
`uuid`: GPU universally unique identifier.   
`model`: GPU model, for example, "NVIDIA A100-SXM4-40GB". .   
`pid`: Process ID.   
`process`: Process name.   
`command`: Process command.   
`command_line`: Process command line, 1024 characters maximum.   
`owner`: Process owner.   
`utilization` GA ** _(project)_**   
GPU utilization   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Percentage of time GPU was not idle since the last sample. Values are between 0.0 and 100.0. Not supported for any device in Multi-Instance GPU mode. Linux only. Sampled every 60 seconds._   
`gpu_number`: GPU number, for example, "0", "1", or "2". The gpu_number matches the CUDA device index. It is not guaranteed to be consistent across reboots. To reference a specific GPU consistently, use the uuid label.   
`uuid`: GPU universally unique identifier.   
`model`: GPU model, for example, "NVIDIA A100-SXM4-40GB". .   
  
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

Network-interface metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default). Launch stages of these metrics: GA

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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of network errors. Sampled every 60 seconds._   
`device`: Name of the network device.   
`direction`: Direction of the network traffic, one of [tx, rx].   
`packets` GA ** _(project)_**   
Network packets   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of packets sent over the network. Sampled every 60 seconds._   
`device`: Name of the network device.   
`direction`: Direction of the network traffic, one of [tx, rx].   
`traffic` GA ** _(project)_**   
Network traffic   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total number of bytes sent over the network. Sampled every 60 seconds._   
`device`: Name of the network device.   
`direction`: Direction of the network traffic, one of [tx, rx].   
  
### memory

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default). Launch stages of these metrics: GA

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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current memory usage by memory state. Summing the values of all states yields the total memory on the machine. Sampled every 60 seconds._   
`state`: One of [buffered, cached, free, slab, used].   
`percent_used` GA ** _(project)_**   
Memory utilization   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current percentage of memory used by memory state. Summing percentages over all states yields 100 percent. Sampled every 60 seconds._   
`state`: One of [buffered, cached, free, slab, used].   
  
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
  
### processes

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default). Launch stages of these metrics: ALPHA GA

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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Process disk read I/O. Sampled every 60 seconds._   
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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Process disk write I/O. Sampled every 60 seconds._   
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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Resident memory usage of the given process. Sampled every 60 seconds._   
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
  
### swap

Metrics from the default configuration for the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default). Launch stages of these metrics: GA

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
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current number of swap bytes used by state. For this metric to be available, swap must be enabled on the instance. Sampled every 60 seconds._   
`device`: Swap device.   
`state`: One of [used, free, cached, reserved].   
`io` GA ** _(project)_**   
Swap I/O operations   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Total count of swap I/O operations by direction. For this metric to be available, swap must be enabled on the instance. Sampled every 60 seconds._   
`direction`: Swap I/O direction, one of [in, out].   
`percent_used` GA ** _(project)_**   
Swap utilization   
`GAUGE`, `DOUBLE`, `%`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[baremetalsolution.googleapis.com/Instance](https://docs.cloud.google.com/monitoring/api/resources#tag_baremetalsolution.googleapis.com/Instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Current percentage of swap used by state. Values are between 0.0 and 100.0. For this metric to be available, swap must be enabled on the instance. Sampled every 60 seconds._   
`device`: Swap device.   
`state`: One of [used, free, cached, reserved].   
  
## Third-party application metrics

Starting with Ops Agent version 2.26.0, all metrics written with the `workload.googleapis.com` domain have two additional labels: `instrumentation_source` and `instrumentation_version`. These new labels are populated with [instrumentation scope information](https://opentelemetry.io/docs/reference/specification/glossary/#instrumentation-scope) that identifies the metric scheme in use. 

For example, each of the `workload.googleapis.com/iis.*` metrics has the following values for these labels: 

  * For `instrumentation_source`, a value of `agent.googleapis.com/iis`
  * For `instrumentation_version`, a value of `2.0`



The value of the metric `instrumentation_source` label matches the value of the corresponding [`logging.googleapis.com/instrumentation_source`](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration#default-ingested-labels) label on log entries. 

### Active Directory Domain Services (AD DS)

Metrics for [ Active Directory Domain Services (AD DS)](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Active Directory Domain Services (AD DS)](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/active_directory_ds). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/active_directory.ds.bind.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `type`  
`workload.googleapis.com/active_directory.ds.ldap.bind.last_successful.time`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.ldap.bind.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.ldap.client.session.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.ldap.search.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.name_cache.hit_rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.notification.queued`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.operation.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `type`  
`workload.googleapis.com/active_directory.ds.replication.network.io`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`type`  
`workload.googleapis.com/active_directory.ds.replication.object.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `direction`  
`workload.googleapis.com/active_directory.ds.replication.operation.pending`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.replication.property.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `direction`  
`workload.googleapis.com/active_directory.ds.replication.sync.object.pending`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.replication.sync.request.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `result`  
`workload.googleapis.com/active_directory.ds.replication.value.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `direction`  
`type`  
`workload.googleapis.com/active_directory.ds.security_descriptor_propagations_event.queued`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.suboperation.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `type`  
`workload.googleapis.com/active_directory.ds.thread.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
### Aerospike

Metrics for [ Aerospike](https://aerospike.com/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Aerospike](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/aerospike). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/aerospike.namespace.disk.available`  
`GAUGE`, `INT64`  
**gce_instance** |  `namespace_name`  
`node_name`  
`workload.googleapis.com/aerospike.namespace.memory.free`  
`GAUGE`, `INT64`  
**gce_instance** |  `namespace_name`  
`node_name`  
`workload.googleapis.com/aerospike.namespace.memory.usage`  
`GAUGE`, `INT64`  
**gce_instance** |  `component`  
`namespace_name`  
`node_name`  
`workload.googleapis.com/aerospike.namespace.scan.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `namespace_name`  
`node_name`  
`result`  
`type`  
`workload.googleapis.com/aerospike.namespace.transaction.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `namespace_name`  
`node_name`  
`result`  
`type`  
`workload.googleapis.com/aerospike.node.connection.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `node_name`  
`operation`  
`type`  
`workload.googleapis.com/aerospike.node.connection.open`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
`type`  
`workload.googleapis.com/aerospike.node.memory.free`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
  
### Apache ActiveMQ

Metrics for [ Apache ActiveMQ](https://activemq.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache ActiveMQ](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/activemq). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/activemq.connection.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/activemq.consumer.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `broker`  
`destination`  
`workload.googleapis.com/activemq.disk.store_usage`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/activemq.disk.temp_usage`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/activemq.memory.usage`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `broker`  
`destination`  
`workload.googleapis.com/activemq.message.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `broker`  
`destination`  
`workload.googleapis.com/activemq.message.dequeued`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `broker`  
`destination`  
`workload.googleapis.com/activemq.message.enqueued`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `broker`  
`destination`  
`workload.googleapis.com/activemq.message.expired`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `broker`  
`destination`  
`workload.googleapis.com/activemq.message.wait_time.avg`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `broker`  
`destination`  
`workload.googleapis.com/activemq.producer.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `broker`  
`destination`  
  
### Apache Cassandra

Metrics for [ Apache Cassandra](http://cassandra.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache Cassandra](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/cassandra). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/cassandra.client.request.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/cassandra.client.request.error.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`status`  
`workload.googleapis.com/cassandra.client.request.range_slice.latency.50p`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/cassandra.client.request.range_slice.latency.99p`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/cassandra.client.request.range_slice.latency.max`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/cassandra.client.request.read.latency.50p`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/cassandra.client.request.read.latency.99p`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/cassandra.client.request.read.latency.max`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/cassandra.client.request.write.latency.50p`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/cassandra.client.request.write.latency.99p`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/cassandra.client.request.write.latency.max`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/cassandra.compaction.tasks.completed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/cassandra.compaction.tasks.pending`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/cassandra.storage.load.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/cassandra.storage.total_hints.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/cassandra.storage.total_hints.in_progress.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
### Apache CouchDB

Metrics for [ Apache CouchDB](https://couchdb.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache CouchDB](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/couchdb). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/couchdb.average_request_time`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/couchdb.database.open`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/couchdb.database.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/couchdb.file_descriptor.open`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/couchdb.httpd.bulk_requests`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/couchdb.httpd.requests`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `http_method`  
`workload.googleapis.com/couchdb.httpd.responses`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `http_status_code`  
`workload.googleapis.com/couchdb.httpd.views`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `view`  
  
### Apache Flink

Metrics for [ Apache Flink](https://flink.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache Flink](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/flink). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/flink.job.checkpoint.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `checkpoint`  
`host_name`  
`job_name`  
`workload.googleapis.com/flink.job.checkpoint.in_progress`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`workload.googleapis.com/flink.job.last_checkpoint.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`workload.googleapis.com/flink.job.last_checkpoint.time`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`workload.googleapis.com/flink.job.restart.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`workload.googleapis.com/flink.jvm.class_loader.classes_loaded`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.cpu.load`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.cpu.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.gc.collections.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `garbage_collector_name`  
`host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.gc.collections.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `garbage_collector_name`  
`host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.direct.total_capacity`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.direct.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.heap.committed`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.heap.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.heap.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.mapped.total_capacity`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.mapped.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.metaspace.committed`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.metaspace.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.metaspace.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.nonheap.committed`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.nonheap.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.nonheap.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.threads.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.memory.managed.total`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.memory.managed.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.operator.record.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`operator_name`  
`record`  
`subtask_index`  
`task_name`  
`taskmanager_id`  
`workload.googleapis.com/flink.operator.watermark.output`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`operator_name`  
`subtask_index`  
`task_name`  
`taskmanager_id`  
`workload.googleapis.com/flink.task.record.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`record`  
`subtask_index`  
`task_name`  
`taskmanager_id`  
  
### Apache Hadoop

Metrics for [ Apache Hadoop](https://hadoop.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache Hadoop](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/hadoop). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/hadoop.name_node.block.corrupt`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
`workload.googleapis.com/hadoop.name_node.block.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
`workload.googleapis.com/hadoop.name_node.block.missing`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
`workload.googleapis.com/hadoop.name_node.capacity.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
`workload.googleapis.com/hadoop.name_node.capacity.usage`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
`workload.googleapis.com/hadoop.name_node.data_node.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
`state`  
`workload.googleapis.com/hadoop.name_node.file.load`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
`workload.googleapis.com/hadoop.name_node.volume.failed`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
  
### Apache HBase

Metrics for [ Apache HBase](https://hbase.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache HBase](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/hbase). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/hbase.master.region_server.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/hbase.master.regions_in_transition.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/hbase.master.regions_in_transition.oldest_age`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/hbase.master.regions_in_transition.over_threshold`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/hbase.region_server.active_handler.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.authentication.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`state`  
`workload.googleapis.com/hbase.region_server.block_cache.operation.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`state`  
`workload.googleapis.com/hbase.region_server.blocked_update.time`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.disk.store_file.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.disk.store_file.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.files.local`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.gc.old_gen.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.gc.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.gc.young_gen.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.open_connection.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.append.latency.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.append.latency.mean`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.append.latency.median`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.append.latency.min`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.append.latency.p99`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.delete.latency.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.delete.latency.mean`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.delete.latency.median`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.delete.latency.min`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.delete.latency.p99`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.get.latency.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.get.latency.mean`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.get.latency.median`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.get.latency.min`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.get.latency.p99`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.increment.latency.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.increment.latency.mean`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.increment.latency.median`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.increment.latency.min`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.increment.latency.p99`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.put.latency.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.put.latency.mean`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.put.latency.median`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.put.latency.min`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.put.latency.p99`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.replay.latency.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.replay.latency.mean`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.replay.latency.median`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.replay.latency.min`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operation.replay.latency.p99`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.operations.slow`  
`GAUGE`, `INT64`  
**gce_instance** |  `operation`  
`region_server`  
`workload.googleapis.com/hbase.region_server.queue.length`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`state`  
`workload.googleapis.com/hbase.region_server.queue.request.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`state`  
`workload.googleapis.com/hbase.region_server.region.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`workload.googleapis.com/hbase.region_server.request.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
`state`  
`workload.googleapis.com/hbase.region_server.write_ahead_log.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `region_server`  
  
### Apache Kafka

Metrics for [ Apache Kafka](https://kafka.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache Kafka](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/kafka). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/kafka.isr.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/kafka.message.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/kafka.network.io`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/kafka.partition.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/kafka.partition.offline`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/kafka.partition.under_replicated`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/kafka.purgatory.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `type`  
`workload.googleapis.com/kafka.request.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `type`  
`workload.googleapis.com/kafka.request.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `type`  
`workload.googleapis.com/kafka.request.time.total`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `type`  
  
### Apache Solr

Metrics for [ Apache Solr](https://solr.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache Solr](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/solr). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/solr.cache.eviction.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `cache`  
`core`  
`workload.googleapis.com/solr.cache.hit.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `cache`  
`core`  
`workload.googleapis.com/solr.cache.insert.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `cache`  
`core`  
`workload.googleapis.com/solr.cache.lookup.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `cache`  
`core`  
`workload.googleapis.com/solr.cache.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `cache`  
`core`  
`workload.googleapis.com/solr.document.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `core`  
`workload.googleapis.com/solr.index.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `core`  
`workload.googleapis.com/solr.request.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `core`  
`handler`  
`type`  
`workload.googleapis.com/solr.request.error.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `core`  
`handler`  
`type`  
`workload.googleapis.com/solr.request.time.average`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `core`  
`handler`  
`type`  
`workload.googleapis.com/solr.request.timeout.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `core`  
`handler`  
`type`  
  
### Apache Tomcat

Metrics for [ Apache Tomcat](https://tomcat.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache Tomcat](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/tomcat). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/tomcat.errors`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `proto_handler`  
`workload.googleapis.com/tomcat.max_time`  
`GAUGE`, `INT64`  
**gce_instance** |  `proto_handler`  
`workload.googleapis.com/tomcat.processing_time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `proto_handler`  
`workload.googleapis.com/tomcat.request_count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `proto_handler`  
`workload.googleapis.com/tomcat.sessions`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/tomcat.threads`  
`GAUGE`, `INT64`  
**gce_instance** |  `proto_handler`  
`state`  
`workload.googleapis.com/tomcat.traffic`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`proto_handler`  
  
### Apache Web Server (httpd)

Metrics for [ Apache Web Server (httpd)](http://httpd.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache Web Server (httpd)](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/apache). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/apache.current_connections`  
`GAUGE`, `INT64`  
**gce_instance** |  `server_name`  
`workload.googleapis.com/apache.requests`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `server_name`  
`workload.googleapis.com/apache.scoreboard`  
`GAUGE`, `INT64`  
**gce_instance** |  `server_name`  
`state`  
`workload.googleapis.com/apache.traffic`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `server_name`  
`workload.googleapis.com/apache.workers`  
`GAUGE`, `INT64`  
**gce_instance** |  `server_name`  
`state`  
  
### Apache ZooKeeper

Metrics for [ Apache ZooKeeper](https://zookeeper.apache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Apache ZooKeeper](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/zookeeper). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/zookeeper.connection.active`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.data_tree.ephemeral_node.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.data_tree.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.file_descriptor.limit`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.file_descriptor.open`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.fsync.exceeded_threshold.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.latency.avg`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.latency.max`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.latency.min`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.packet.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`workload.googleapis.com/zookeeper.request.active`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.watch.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/zookeeper.znode.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
### Couchbase

Metrics for [ Couchbase](https://www.couchbase.com/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Couchbase](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/couchbase). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/couchbase.bucket.error.oom.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `bucket_name`  
`error_type`  
`workload.googleapis.com/couchbase.bucket.item.count`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `bucket_name`  
`state`  
`workload.googleapis.com/couchbase.bucket.item.ejection.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `bucket_name`  
`workload.googleapis.com/couchbase.bucket.memory.high_water_mark.limit`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `bucket_name`  
`workload.googleapis.com/couchbase.bucket.memory.low_water_mark.limit`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `bucket_name`  
`workload.googleapis.com/couchbase.bucket.memory.usage`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `bucket_name`  
`workload.googleapis.com/couchbase.bucket.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `bucket_name`  
`op`  
`workload.googleapis.com/couchbase.bucket.vbucket.count`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `bucket_name`  
`state`  
  
### Elasticsearch 7.9+

Metrics for [ Elasticsearch 7.9+](http://elasticsearch.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Elasticsearch 7.9+](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/elasticsearch). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/elasticsearch.breaker.memory.estimated`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.breaker.memory.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.breaker.tripped`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.cluster.data_nodes`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.cluster.health`  
`GAUGE`, `INT64`  
**gce_instance** |  `status`  
`workload.googleapis.com/elasticsearch.cluster.in_flight_fetch`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.cluster.nodes`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.cluster.pending_tasks`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.cluster.published_states.differences`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/elasticsearch.cluster.published_states.full`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.cluster.shards`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/elasticsearch.cluster.state_queue`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/elasticsearch.cluster.state_update.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/elasticsearch.cluster.state_update.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `state`  
`type`  
`workload.googleapis.com/elasticsearch.indexing_pressure.memory.limit`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.indexing_pressure.memory.total.primary_rejections`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.indexing_pressure.memory.total.replica_rejections`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.memory.indexing_pressure`  
`GAUGE`, `INT64`  
**gce_instance** |  `stage`  
`workload.googleapis.com/elasticsearch.node.cache.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `type`  
`workload.googleapis.com/elasticsearch.node.cache.evictions`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `cache_name`  
`workload.googleapis.com/elasticsearch.node.cache.memory.usage`  
`GAUGE`, `INT64`  
**gce_instance** |  `cache_name`  
`workload.googleapis.com/elasticsearch.node.cluster.connections`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.cluster.io`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`workload.googleapis.com/elasticsearch.node.disk.io.read`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.disk.io.write`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.documents`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/elasticsearch.node.fs.disk.available`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.fs.disk.free`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.fs.disk.total`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.http.connections`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.ingest.documents`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.ingest.documents.current`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.ingest.operations.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.open_files`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.operations.completed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/elasticsearch.node.operations.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/elasticsearch.node.pipeline.ingest.documents.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.node.pipeline.ingest.documents.preprocessed`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.node.pipeline.ingest.operations.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.node.script.cache_evictions`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.script.compilation_limit_triggered`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.script.compilations`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.shards.data_set.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.shards.reserved.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.shards.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.thread_pool.tasks.finished`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `state`  
`thread_pool_name`  
`workload.googleapis.com/elasticsearch.node.thread_pool.tasks.queued`  
`GAUGE`, `INT64`  
**gce_instance** |  `thread_pool_name`  
`workload.googleapis.com/elasticsearch.node.thread_pool.threads`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`thread_pool_name`  
`workload.googleapis.com/elasticsearch.node.translog.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.translog.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.translog.uncommitted.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.os.cpu.load_avg.15m`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.os.cpu.load_avg.1m`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.os.cpu.load_avg.5m`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.os.cpu.usage`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.os.memory`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
  
### Elasticsearch 8.0+ and 9.0+

Metrics for [ Elasticsearch 8.0+ and 9.0+](http://elasticsearch.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Elasticsearch 8.0+ and 9.0+](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/elasticsearch9). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/elasticsearch.breaker.memory.estimated`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`name`  
`workload.googleapis.com/elasticsearch.breaker.memory.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`name`  
`workload.googleapis.com/elasticsearch.breaker.tripped`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`name`  
`workload.googleapis.com/elasticsearch.cluster.data_nodes`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.cluster.health`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`status`  
`workload.googleapis.com/elasticsearch.cluster.in_flight_fetch`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.cluster.nodes`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.cluster.pending_tasks`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.cluster.published_states.differences`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`state`  
`workload.googleapis.com/elasticsearch.cluster.published_states.full`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.cluster.shards`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`state`  
`workload.googleapis.com/elasticsearch.cluster.state_queue`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`state`  
`workload.googleapis.com/elasticsearch.cluster.state_update.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`state`  
`workload.googleapis.com/elasticsearch.cluster.state_update.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`state`  
`type`  
`workload.googleapis.com/elasticsearch.indexing_pressure.memory.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.indexing_pressure.memory.total.primary_rejections`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.indexing_pressure.memory.total.replica_rejections`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.memory.indexing_pressure`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`stage`  
`workload.googleapis.com/elasticsearch.node.cache.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`type`  
`workload.googleapis.com/elasticsearch.node.cache.evictions`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `cache_name`  
`instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.cache.memory.usage`  
`GAUGE`, `INT64`  
**gce_instance** |  `cache_name`  
`instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.cluster.connections`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.cluster.io`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.disk.io.read`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.disk.io.write`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.documents`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`state`  
`workload.googleapis.com/elasticsearch.node.fs.disk.available`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.fs.disk.free`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.fs.disk.total`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.http.connections`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.ingest.documents`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.ingest.documents.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.ingest.operations.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.open_files`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.operations.completed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`operation`  
`workload.googleapis.com/elasticsearch.node.operations.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`operation`  
`workload.googleapis.com/elasticsearch.node.pipeline.ingest.documents.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`name`  
`workload.googleapis.com/elasticsearch.node.pipeline.ingest.documents.preprocessed`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`name`  
`workload.googleapis.com/elasticsearch.node.pipeline.ingest.operations.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`name`  
`workload.googleapis.com/elasticsearch.node.script.cache_evictions`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.script.compilation_limit_triggered`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.script.compilations`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.shards.data_set.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.shards.reserved.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.shards.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.thread_pool.tasks.finished`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`state`  
`thread_pool_name`  
`workload.googleapis.com/elasticsearch.node.thread_pool.tasks.queued`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`thread_pool_name`  
`workload.googleapis.com/elasticsearch.node.thread_pool.threads`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`state`  
`thread_pool_name`  
`workload.googleapis.com/elasticsearch.node.translog.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.translog.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.node.translog.uncommitted.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.os.cpu.load_avg.15m`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.os.cpu.load_avg.1m`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.os.cpu.load_avg.5m`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.os.cpu.usage`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`workload.googleapis.com/elasticsearch.os.memory`  
`GAUGE`, `INT64`  
**gce_instance** |  `instrumentation_source`  
`state`  
  
### Hashicorp Vault

Metrics for [ Hashicorp Vault](https://www.vaultproject.io/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Hashicorp Vault](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/vault). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/vault.audit.request.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/vault.audit.response.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/vault.core.leader.duration`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/vault.core.request.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `cluster`  
`workload.googleapis.com/vault.memory.usage`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/vault.storage.operation.delete.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.delete.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.get.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.get.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.list.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.list.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.put.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.put.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.token.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `cluster`  
`namespace`  
`workload.googleapis.com/vault.token.lease.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/vault.token.renew.time`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/vault.token.revoke.time`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
### Internet Information Services (v2)

Metrics (v2) for Internet Information Services. For information about collecting these metrics, see the guide for [configuring the Ops Agent for Internet Information Services](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/iis). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/iis.connection.active`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.connection.anonymous`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.connection.attempt.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.network.blocked`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.network.file.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`workload.googleapis.com/iis.network.io`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`workload.googleapis.com/iis.request.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `request`  
`workload.googleapis.com/iis.request.queue.age.max`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.request.queue.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.request.rejected`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.thread.active`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.uptime`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
### Jetty

Metrics for [ Jetty](https://www.eclipse.org/jetty/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Jetty](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/jetty). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/jetty.select.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jetty.session.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `resource`  
`workload.googleapis.com/jetty.session.time.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `resource`  
`workload.googleapis.com/jetty.session.time.total`  
`GAUGE`, `INT64`  
**gce_instance** |  `resource`  
`workload.googleapis.com/jetty.thread.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/jetty.thread.queue.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
### JVM

Metrics for [ JVM](https://docs.oracle.com/javase/specs/index.html). For information about collecting these metrics, see the guide for [configuring the Ops Agent for JVM](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/jvm). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/jvm.classes.loaded`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.gc.collections.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.gc.collections.elapsed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.memory.heap.committed`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.heap.init`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.heap.max`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.heap.used`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.nonheap.committed`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.nonheap.init`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.nonheap.max`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.nonheap.used`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.pool.committed`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.memory.pool.init`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.memory.pool.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.memory.pool.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.threads.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
### MariaDB

Metrics for [ MariaDB](http://www.mariadb.com/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for MariaDB](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/mariadb). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/mysql.buffer_pool_data_pages`  
`GAUGE`, `INT64`  
**gce_instance** |  `status`  
`workload.googleapis.com/mysql.buffer_pool_limit`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.buffer_pool_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.buffer_pool_page_flushes`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.buffer_pool_pages`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.buffer_pool_size`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.commands`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `command`  
`workload.googleapis.com/mysql.double_writes`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.handlers`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.locks`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.log_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.page_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.replica.sql_delay`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.replica.time_behind_source`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.row_locks`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.row_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.sorts`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.threads`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `kind`  
  
### Memcached

Metrics for [ Memcached](http://www.memcached.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Memcached](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/memcached). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/memcached.bytes`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/memcached.commands`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `command`  
`workload.googleapis.com/memcached.connections.current`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/memcached.connections.total`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/memcached.cpu.usage`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `state`  
`workload.googleapis.com/memcached.current_items`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/memcached.evictions`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/memcached.network`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`workload.googleapis.com/memcached.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`type`  
`workload.googleapis.com/memcached.threads`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
### Microsoft SQL Server (v2)

Metrics (v2) for SQL Server (MSSQL). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Microsoft SQL Server](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/mssql). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/sqlserver.batch.request.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.batch.sql_compilation.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.batch.sql_recompilation.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.lock.wait.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.lock.wait_time.avg`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.page.buffer_cache.hit_ratio`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.page.checkpoint.flush.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.page.lazy_write.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.page.life_expectancy`  
`GAUGE`, `INT64`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.page.operation.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `type`  
`workload.googleapis.com/sqlserver.page.split.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.transaction.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction.write.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.flush.data.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.flush.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.flush.wait.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.growth.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.percent_used`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.shrink.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.user.connection.count`  
`GAUGE`, `INT64`  
**gce_instance** |  ` `  
  
### MongoDB

Metrics for [ MongoDB](https://www.mongodb.com/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for MongoDB](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/mongodb). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/mongodb.cache.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `type`  
`workload.googleapis.com/mongodb.collection.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/mongodb.connection.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`type`  
`workload.googleapis.com/mongodb.cursor.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mongodb.cursor.timeout.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mongodb.data.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/mongodb.database.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mongodb.document.operation.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`operation`  
`workload.googleapis.com/mongodb.global_lock.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mongodb.index.access.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `collection`  
`database`  
`workload.googleapis.com/mongodb.index.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/mongodb.index.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/mongodb.memory.usage`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`type`  
`workload.googleapis.com/mongodb.network.io.receive`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mongodb.network.io.transmit`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mongodb.network.request.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mongodb.object.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/mongodb.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mongodb.operation.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mongodb.session.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mongodb.storage.size`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
  
### MySQL

Metrics for [ MySQL](http://www.mysql.com/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for MySQL](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/mysql). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/mysql.buffer_pool_data_pages`  
`GAUGE`, `INT64`  
**gce_instance** |  `status`  
`workload.googleapis.com/mysql.buffer_pool_limit`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.buffer_pool_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.buffer_pool_page_flushes`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.buffer_pool_pages`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.buffer_pool_size`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.commands`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `command`  
`workload.googleapis.com/mysql.double_writes`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.handlers`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.locks`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.log_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.page_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.replica.sql_delay`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.replica.time_behind_source`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.row_locks`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.row_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.sorts`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.threads`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `kind`  
  
### nginx

Metrics for [ nginx](https://nginx.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for nginx](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/nginx). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/nginx.connections_accepted`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/nginx.connections_current`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/nginx.connections_handled`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/nginx.requests`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
  
### NVIDIA Data Center GPU Manager (DCGM) (v1)

Metrics for [ NVIDIA Data Center GPU Manager (DCGM)](https://developer.nvidia.com/dcgm), collected by using version 1 of the Ops Agent `dcgm` receiver. For information about collecting these metrics, see [configuring the Ops Agent for NVIDIA Data Center GPU Manager](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/dcgm.gpu.profiling.dram_utilization` †  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/dcgm.gpu.profiling.nvlink_traffic_rate` †  
`GAUGE`, `INT64`  
**gce_instance** |  `direction`  
`gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/dcgm.gpu.profiling.pcie_traffic_rate` †  
`GAUGE`, `INT64`  
**gce_instance** |  `direction`  
`gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/dcgm.gpu.profiling.pipe_utilization` †  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`pipe` ‡  
`uuid`  
`workload.googleapis.com/dcgm.gpu.profiling.sm_occupancy` †  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/dcgm.gpu.profiling.sm_utilization` †  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
  
† Not available on GPU models P100 and P4.

‡ For L4, the `pipe` value `fp64` is not supported.

### NVIDIA Data Center GPU Manager (DCGM) (v2)

Metrics for [ NVIDIA Data Center GPU Manager (DCGM)](https://developer.nvidia.com/dcgm), collected by using version 2 of the Ops Agent `dcgm` receiver. For information about collecting these metrics, see [configuring the Ops Agent for NVIDIA Data Center GPU Manager (DCGM)](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia). 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/gpu.dcgm.clock.frequency`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.clock.throttle_duration.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
`violation` †  
`workload.googleapis.com/gpu.dcgm.codec.decoder.utilization`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.codec.encoder.utilization`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.ecc_errors`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `error_type`  
`gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.energy_consumption`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.memory.bandwidth_utilization`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.memory.bytes_used`  
`GAUGE`, `INT64`  
**gce_instance** |  `gpu_number`  
`model`  
`state`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.nvlink.io` ‡  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.pcie.io` ‡  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.pipe.utilization` ‡  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`pipe` §  
`uuid`  
`workload.googleapis.com/gpu.dcgm.sm.utilization` ‡  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.temperature`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
`workload.googleapis.com/gpu.dcgm.utilization`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `gpu_number`  
`model`  
`uuid`  
  
† For P100 and P4, only `violation` values `power`, `thermal`, and `sync_boost` are supported.

‡ Not available on GPU models P100 and P4.

§ For L4, the `pipe` value `fp64` is not supported.

### Oracle Database

Metrics for [ Oracle Database](https://www.oracle.com/database/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Oracle Database](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/oracledb). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/oracle.backup.latest`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`workload.googleapis.com/oracle.buffer.cache.ratio`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.cursor.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.cursor.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.disk.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`direction`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.disk.operation.size`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`direction`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.logon.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.logon.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.network.data`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`direction`  
`global_name`  
`instance_id`  
`target`  
`workload.googleapis.com/oracle.process.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.process.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.process.pga_memory.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`program`  
`state`  
`workload.googleapis.com/oracle.row.cache.ratio`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.service.response_time`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.session.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.session.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.sort.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`type`  
`workload.googleapis.com/oracle.sort.row.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.tablespace.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `contents`  
`database_id`  
`db_system`  
`global_name`  
`status`  
`workload.googleapis.com/oracle.tablespace.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `contents`  
`database_id`  
`db_system`  
`global_name`  
`state`  
`tablespace_name`  
`workload.googleapis.com/oracle.user.calls`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.user.commits`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.user.rollbacks`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.wait.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`type`  
`wait_class`  
`workload.googleapis.com/oracle.wait.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`type`  
`wait_class`  
`workload.googleapis.com/oracle.wait.timeouts`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`type`  
`wait_class`  
  
### PostgreSQL

Metrics for [ PostgreSQL](http://www.postgresql.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for PostgreSQL](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/postgresql). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/postgresql.backends`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/postgresql.bgwriter.buffers.allocated`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/postgresql.bgwriter.buffers.writes`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `source`  
`workload.googleapis.com/postgresql.bgwriter.checkpoint.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `type`  
`workload.googleapis.com/postgresql.bgwriter.duration`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `type`  
`workload.googleapis.com/postgresql.bgwriter.maxwritten`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/postgresql.blocks_read`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
`source`  
`table`  
`workload.googleapis.com/postgresql.commits`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/postgresql.connection.max`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/postgresql.database.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/postgresql.db_size`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/postgresql.index.scans`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
`index`  
`table`  
`workload.googleapis.com/postgresql.index.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`index`  
`table`  
`workload.googleapis.com/postgresql.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
`operation`  
`table`  
`workload.googleapis.com/postgresql.replication.data_delay`  
`GAUGE`, `INT64`  
**gce_instance** |  `replication_client`  
`workload.googleapis.com/postgresql.rollbacks`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/postgresql.rows`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`state`  
`table`  
`workload.googleapis.com/postgresql.table.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/postgresql.table.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`table`  
`workload.googleapis.com/postgresql.table.vacuum.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
`table`  
`workload.googleapis.com/postgresql.wal.age`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/postgresql.wal.lag`  
`GAUGE`, `INT64`  
**gce_instance** |  `operation`  
`replication_client`  
  
### RabbitMQ

Metrics for [ RabbitMQ](https://www.rabbitmq.com/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for RabbitMQ](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/rabbitmq). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/rabbitmq.consumer.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
`queue_name`  
`vhost_name`  
`workload.googleapis.com/rabbitmq.message.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `node_name`  
`queue_name`  
`state`  
`vhost_name`  
  
### Redis

Metrics for [ Redis](http://redis.io/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Redis](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/redis). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/redis.clients.blocked`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.clients.connected`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.clients.max_input_buffer`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.clients.max_output_buffer`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.commands.processed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.connections.received`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.connections.rejected`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.cpu.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `state`  
`workload.googleapis.com/redis.keys.evicted`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.keys.expired`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.keyspace.hits`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.keyspace.misses`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.latest_fork`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.memory.fragmentation_ratio`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/redis.memory.lua`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.memory.peak`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.memory.rss`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.memory.used`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.net.input`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.net.output`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.rdb.changes_since_last_save`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.replication.backlog_first_byte_offset`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.replication.offset`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.slaves.connected`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
### SAP HANA

Metrics for [ SAP HANA](https://www.sap.com/products/hana.html). For information about collecting these metrics, see the guide for [configuring the Ops Agent for SAP HANA](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/saphana). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/saphana.alert.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `rating`  
`workload.googleapis.com/saphana.backup.latest`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/saphana.column.memory.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`subtype`  
`type`  
`workload.googleapis.com/saphana.component.memory.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `component`  
`host`  
`workload.googleapis.com/saphana.connection.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`status`  
`workload.googleapis.com/saphana.cpu.used`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`type`  
`workload.googleapis.com/saphana.disk.size.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`path`  
`state`  
`usage_type`  
`workload.googleapis.com/saphana.host.memory.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`state`  
`workload.googleapis.com/saphana.host.swap.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`state`  
`workload.googleapis.com/saphana.instance.code_size`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`workload.googleapis.com/saphana.instance.memory.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`state`  
`workload.googleapis.com/saphana.instance.memory.shared.allocated`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`workload.googleapis.com/saphana.instance.memory.used.peak`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`workload.googleapis.com/saphana.license.expiration.time`  
`GAUGE`, `INT64`  
**gce_instance** |  `product`  
`system`  
`workload.googleapis.com/saphana.license.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `product`  
`system`  
`workload.googleapis.com/saphana.license.peak`  
`GAUGE`, `INT64`  
**gce_instance** |  `product`  
`system`  
`workload.googleapis.com/saphana.network.request.average_time`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `host`  
`workload.googleapis.com/saphana.network.request.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`state`  
`workload.googleapis.com/saphana.network.request.finished.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`type`  
`workload.googleapis.com/saphana.replication.average_time`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `mode`  
`port`  
`primary`  
`secondary`  
`workload.googleapis.com/saphana.replication.backlog.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `mode`  
`port`  
`primary`  
`secondary`  
`workload.googleapis.com/saphana.replication.backlog.time`  
`GAUGE`, `INT64`  
**gce_instance** |  `mode`  
`port`  
`primary`  
`secondary`  
`workload.googleapis.com/saphana.row_store.memory.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`type`  
`workload.googleapis.com/saphana.schema.memory.used.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`schema`  
`type`  
`workload.googleapis.com/saphana.schema.memory.used.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`schema`  
`workload.googleapis.com/saphana.schema.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`schema`  
`type`  
`workload.googleapis.com/saphana.schema.record.compressed.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`schema`  
`workload.googleapis.com/saphana.schema.record.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`schema`  
`type`  
`workload.googleapis.com/saphana.service.code_size`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`status`  
`workload.googleapis.com/saphana.service.memory.compactors.allocated`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.memory.compactors.freeable`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.memory.effective_limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.memory.heap.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`state`  
`workload.googleapis.com/saphana.service.memory.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.memory.shared.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`state`  
`workload.googleapis.com/saphana.service.memory.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`type`  
`workload.googleapis.com/saphana.service.stack_size`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.thread.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`status`  
`workload.googleapis.com/saphana.transaction.blocked`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`workload.googleapis.com/saphana.transaction.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`type`  
`workload.googleapis.com/saphana.volume.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`path`  
`type`  
`usage_type`  
`workload.googleapis.com/saphana.volume.operation.size`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`path`  
`type`  
`usage_type`  
`workload.googleapis.com/saphana.volume.operation.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`path`  
`type`  
`usage_type`  
  
### Varnish HTTP Cache

Metrics for [ Varnish HTTP Cache](https://varnish-cache.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for Varnish HTTP Cache](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/varnish). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/varnish.backend.connection.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/varnish.backend.request.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/varnish.cache.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/varnish.client.request.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/varnish.client.request.error.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `status_code`  
`workload.googleapis.com/varnish.object.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/varnish.object.expired`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/varnish.object.moved`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/varnish.object.nuked`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/varnish.session.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/varnish.thread.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
  
### WildFly

Metrics for [ WildFly](https://www.wildfly.org/). For information about collecting these metrics, see the guide for [configuring the Ops Agent for WildFly](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/wildfly). 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/wildfly.jdbc.connection.open`  
`GAUGE`, `INT64`  
**gce_instance** |  `data_source`  
`state`  
`workload.googleapis.com/wildfly.jdbc.request.wait`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `data_source`  
`workload.googleapis.com/wildfly.jdbc.rollback.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `cause`  
`workload.googleapis.com/wildfly.jdbc.transaction.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/wildfly.network.io`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `listener`  
`server`  
`state`  
`workload.googleapis.com/wildfly.request.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `listener`  
`server`  
`workload.googleapis.com/wildfly.request.server_error`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `listener`  
`server`  
`workload.googleapis.com/wildfly.request.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `listener`  
`server`  
`workload.googleapis.com/wildfly.session.active`  
`GAUGE`, `INT64`  
**gce_instance** |  `deployment`  
`workload.googleapis.com/wildfly.session.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `deployment`  
`workload.googleapis.com/wildfly.session.expired`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `deployment`  
`workload.googleapis.com/wildfly.session.rejected`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `deployment`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
