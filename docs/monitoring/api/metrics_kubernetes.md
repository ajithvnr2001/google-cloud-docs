---
url: https://docs.cloud.google.com/monitoring/api/metrics_kubernetes/
title: GKE system metrics \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:00.461315+00:00
---

# GKE system metrics  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  GKE system metrics Stay organized with collections  Save and categorize content based on your preferences. 

When Google Kubernetes Engine (GKE) [system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) are enabled, Cloud Monitoring collects the following metrics.

## About the tables of metrics

The tables of metrics provide formatted versions of the publicly available [metric descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor). This section provides additional information to help you interpret and use these descriptors.

  * For a general explanation of the entries in the tables, including information about values like `DELTA` and `GAUGE`, see [Metric types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

To chart or monitor metric types with values of type `STRING`, you must use Monitoring Query Language (MQL), and you must convert the value into a numeric value. For information about MQL string-conversion methods, see [`String`](https://docs.cloud.google.com/monitoring/mql/reference#string-group).

  * For information about the units used in the metric lists, see the [`unit` field](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.unit) in the `MetricDescriptor` reference.

  * For information about statements of the form “Sampled every _x_ seconds” and “After sampling, data is not visible for up to _y_ seconds”, see [Additional information: metadata](https://docs.cloud.google.com/monitoring/api/metrics#metadata).

  * The resource-hierarchy level tells you if the metric is written at the project, organization, or folder level(s). When the level is not specified in the metric descriptor, the metric writes at the project level by default.



  * For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).


  * For information about the meaning of launch stages such as `GA` (General Availability) and `BETA` (Preview), see [Product launch stages](https://cloud.google.com/products#product-launch-stages).



## Kubernetes metrics

Metrics from [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine).

The following list was last generated at 2026-10-14 20:24:33 UTC. For more information about this process, see [ About the lists](https://docs.cloud.google.com/monitoring/api/metrics#generated).

### kubernetes

Metrics for [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs). For information on viewing these metrics, go to [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics). Launch stages of these metrics: BETA GA

The "metric type" strings in this table must be prefixed with `kubernetes.io/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`accelerator/partition/metadata` BETA ** _(project)_**   
TPU Accelerator Partition Metadata   
`GAUGE`, `BOOL`, `1`   
**[k8s_node_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node_pool)** |  _The metadata of a TPU accelerator partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`partition_id`: ID of the partition.   
`partition_topology`: Topology of the partition. Such as 2x4x4, 4x4x4, etc.   
`reservation_name`: The name of the associated reservation.   
`block_id`: The ID of the associated reservation block.   
`block_name`: The name of the associated reservation block.   
`subblock_id`: The ID of the associated reservation subblock.   
`subblock_name`: The name of the associated reservation subblock.   
`accelerator/partition/state` BETA ** _(project)_**   
TPU Accelerator Partition State   
`GAUGE`, `INT64`, `1`   
**[k8s_node_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node_pool)** |  _The current state of a TPU accelerator partition, state will show the health of the partition. The metric is 1 if the partition state is detected, 0 otherwise. Sampled every 60 seconds._   
`state`: State of the partition. Such as HEALTHY, UNHEALTHY, etc.   
`accelerator_type`: Type of the accelerator. Such as tpu7x.   
`partition_topology`: Topology of the partition. Such as 2x4x4, 4x4x4, etc.   
`partition_id`: ID of the partition.   
`slice_id`: ID of the associated slice.   
`block_id`: ID of the associated block.   
`accelerator/slice/deformation_durations` BETA ** _(project)_**   
TPU Accelerator Slice Deformation Duration   
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _Total distribution of the durations taken to tear down or disassemble a TPU slice and release its underlying resources. Sampled every 60 seconds. Sampled every 60 seconds._   
`accelerator_type`: Type of the accelerator. Such as tpu7x.   
`slice_topology`: Topology of the slice. Such as 4x4x4.   
`block_id`: ID of the associated block.   
`accelerator/slice/formation_durations` BETA ** _(project)_**   
TPU Accelerator Slice Formation Duration   
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _Total distribution of the durations taken to create and assemble a TPU slice from underlying resources. Sampled every 60 seconds. Sampled every 60 seconds._   
`end_state`: End state of the slice. Such as ACTIVE, FAILED, ACTIVE_DEGRADED.   
`accelerator_type`: Type of the accelerator. Such as tpu7x.   
`slice_topology`: Topology of the slice. Such as 4x4x4.   
`block_id`: ID of the associated block.   
`accelerator/slice/metadata` BETA ** _(project)_**   
TPU Accelerator Slice Metadata   
`GAUGE`, `INT64`, `1`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _The metadata of a TPU accelerator slice. Emits a discrete stream for each discovered combination of slice and its partition. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`node_pool_name`: The name of the node pool.   
`partition_id`: The ID of the associated partition.   
`accelerator_type`: The type of accelerator. Such as tpu7x.   
`slice_topology`: The topology of the slice. Such as 2x4x4, 4x4x4, etc.   
`retry_on_creation_failures`: (BOOL) Whether SliceCreationFailed are retried automatically during slice formation.   
`accelerator/slice/state` BETA ** _(project)_**   
TPU Accelerator Slice State   
`GAUGE`, `INT64`, `1`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _The current state of a TPU accelerator slice, state will show the status of the slice. The metric is 1 if the slice state is detected, 0 otherwise. Sampled every 60 seconds._   
`state`: State of the slice. Such as ACTIVE, FAILED, etc.   
`accelerator_type`: Type of the accelerator. Such as tpu7x.   
`slice_topology`: Topology of the slice. Such as 2x4x4, 4x4x4, etc.   
`block_id`: ID of the associated block.   
`autoscaler/cluster_node_provisioning_attempts_count_per_ccc` BETA ** _(project)_**   
Node Provisioning Attempts by CCC   
`DELTA`, `INT64`, `1`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _The total number of node provisioning attempts initiated by Cluster Autoscaler, broken down by custom Compute Class (CCC). Sampled every 60 seconds._  
`autoscaler/cluster_node_provisioning_failed_attempts_count_per_ccc` BETA ** _(project)_**   
Node Provisioning Failures by CCC   
`DELTA`, `INT64`, `1`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _The total number of failed node provisioning attempts by Cluster Autoscaler, broken down by Custom Compute Class and reason. Sampled every 60 seconds._   
`reason`: The reason why the node provisioning attempt failed.   
`autoscaler/cluster_pending_pods_per_ccc` BETA ** _(project)_**   
Pending Pods for Scale-Up by CCC   
`GAUGE`, `INT64`, `1`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _The number of pods currently in the Pending state that Cluster Autoscaler is considering for scale-up, broken down by the custom Compute Class (CCC), the reason the pod is pending, and whether it is a system pod. Sampled every 60 seconds._   
`reason`: The reason category why the pod is pending.   
`type`: Indicates if the pod is a system pod or user pod.   
`autoscaler/container/cpu/per_replica_recommended_request_cores` GA ** _(project)_**   
Recommended per replica request cores   
`GAUGE`, `DOUBLE`, `{cpu}`   
**[k8s_scale](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_scale)** |  _Number of CPU cores for the recommended CPU request for a single replica of the workload. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`container_name`: Name of the container.   
`autoscaler/container/memory/per_replica_recommended_request_bytes` GA ** _(project)_**   
Recommended per replica request bytes   
`GAUGE`, `INT64`, `By`   
**[k8s_scale](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_scale)** |  _Recommended memory request for a single replica of the workload, in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`container_name`: Name of the container.   
`autoscaler/latencies/per_hpa_recommendation_scale_latency_seconds` GA ** _(project)_**   
Per HPA recommendation scale latency   
`GAUGE`, `DOUBLE`, `s`   
**[k8s_scale](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_scale)** |  _HPA Scaling recommendation latency (time between metrics being created and corresponding scaling recommendation being applied to the apiserver) for the HPA target. Sampled every 60 seconds. After sampling, data is not visible for up to 20 seconds._   
`metric_type`: type is the type of metric source. It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource".   
`cluster/in_maintenance_window` BETA ** _(project)_**   
In Maintenance Window   
`GAUGE`, `BOOL`, `1`   
**[k8s_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_cluster)** |  _Indicates whether the cluster is currently in a maintenance window. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._  
`cluster/kcp_healthchecks` BETA ** _(project)_**   
KCP Healthchecks   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_cluster)** |  _Cumulative count of Kubernetes Control Plane healthchecks, categorized by success or failure. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`success`: (BOOL) Indicates whether the KCP healthcheck was successful. False when KCP reported unhealthy or did not respond.   
`cluster/version` BETA ** _(project)_**   
GKE Cluster Version   
`GAUGE`, `BOOL`, `1`   
**[k8s_cluster](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_cluster)** |  _The GKE control plane version of the cluster. Value is always true; the cluster version is in the 'cluster_version' label. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`cluster_version`: The GKE control plane version string.   
`container/accelerator/duty_cycle` GA ** _(project)_**   
Accelerator duty cycle   
`GAUGE`, `INT64`, `%`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Percent of time over the past sample period (10s) during which the accelerator was actively processing. Values are integers between 0 and 100. Sampled every 60 seconds._   
`make`: Make of the accelerator (e.g. nvidia)   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator (e.g. 'Tesla P100')   
`container/accelerator/memory_bandwidth_utilization` GA ** _(project)_**   
Memory bandwidth utilization   
`GAUGE`, `DOUBLE`, `percent`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Current percentage of the accelerator memory bandwidth that is being used. Computed by dividing the memory bandwidth used over a sample period by the maximum supported bandwidth over the same sample period. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/accelerator/memory_total` GA ** _(project)_**   
Accelerator memory total   
`GAUGE`, `INT64`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total accelerator memory in bytes. Sampled every 60 seconds._   
`make`: Make of the accelerator (e.g. nvidia)   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator (e.g. 'Tesla P100')   
`container/accelerator/memory_used` GA ** _(project)_**   
Accelerator memory used   
`GAUGE`, `INT64`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total accelerator memory allocated in bytes. Sampled every 60 seconds._   
`make`: Make of the accelerator (e.g. nvidia)   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator (e.g. 'Tesla P100')   
`container/accelerator/request` GA ** _(project)_**   
Request accelerators   
`GAUGE`, `INT64`, `{devices}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of accelerator devices requested by the container. Sampled every 60 seconds._   
`resource_name`: Name of the requested accelerator resource.   
`container/accelerator/tensorcore_utilization` GA ** _(project)_**   
Tensorcore utilization   
`GAUGE`, `DOUBLE`, `percent`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Current percentage of the Tensorcore that is utilized. Computed by dividing the Tensorcore operations that were performed over a sample period by the supported number of Tensorcore operations over the same sample period. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/cpu/core_usage_time` GA ** _(project)_**   
CPU usage time   
`CUMULATIVE`, `DOUBLE`, `s{CPU}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Cumulative CPU usage on all cores used by the container in seconds. Sampled every 60 seconds._  
`container/cpu/limit_cores` GA ** _(project)_**   
Limit cores   
`GAUGE`, `DOUBLE`, `{cpu}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _CPU cores limit of the container. Sampled every 60 seconds._  
`container/cpu/limit_utilization` GA ** _(project)_**   
CPU limit utilization   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _The fraction of the CPU limit that is currently in use on the instance. This value can be greater than 1 as a container might be allowed to exceed its CPU limit for extended periods of time. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`container/cpu/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Container CPU full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Fraction of time in which all tasks are stalled on CPU at container level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/cpu/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Container CPU some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Fraction of time in which some tasks are stalled on CPU at container level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/cpu/request_cores` GA ** _(project)_**   
Request cores   
`GAUGE`, `DOUBLE`, `{cpu}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of CPU cores requested by the container. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/cpu/request_utilization` GA ** _(project)_**   
CPU request utilization   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _The fraction of the requested CPU that is currently in use on the instance. This value can be greater than 1 as usage can exceed the request. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`container/ephemeral_storage/limit_bytes` GA ** _(project)_**   
Ephemeral storage limit   
`GAUGE`, `INT64`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Local ephemeral storage limit in bytes. Sampled every 60 seconds._  
`container/ephemeral_storage/request_bytes` GA ** _(project)_**   
Ephemeral storage request   
`GAUGE`, `INT64`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Local ephemeral storage request in bytes. Sampled every 60 seconds._  
`container/ephemeral_storage/used_bytes` GA ** _(project)_**   
Ephemeral storage usage   
`GAUGE`, `INT64`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Local ephemeral storage usage in bytes. Sampled every 60 seconds._  
`container/io/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Container IO full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Fraction of time in which all tasks are stalled on IO at container level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/io/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Container IO some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Fraction of time in which some tasks are stalled on IO at container level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/memory/limit_bytes` GA ** _(project)_**   
Memory limit   
`GAUGE`, `INT64`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Memory limit of the container in bytes. Sampled every 60 seconds._  
`container/memory/limit_utilization` GA ** _(project)_**   
Memory limit utilization   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _The fraction of the memory limit that is currently in use on the instance. This value cannot exceed 1 as usage cannot exceed the limit. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`memory_type`: Either `evictable` or `non-evictable`. Evictable memory is memory that can be easily reclaimed by the kernel, while non-evictable memory cannot.   
`container/memory/page_fault_count` GA ** _(project)_**   
Page faults   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of page faults, broken down by type: major and minor. Sampled every 60 seconds._   
`fault_type`: Fault type - either 'major' or 'minor', with the former indicating that the page had to be loaded from disk.   
`container/memory/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Container Memory full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Fraction of time in which all tasks are stalled on Memory at container level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/memory/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Container Memory some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Fraction of time in which some tasks are stalled on Memory at container level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/memory/request_bytes` GA ** _(project)_**   
Memory request   
`GAUGE`, `INT64`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Memory request of the container in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/memory/request_utilization` GA ** _(project)_**   
Memory request utilization   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _The fraction of the requested memory that is currently in use on the instance. This value can be greater than 1 as usage can exceed the request. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`memory_type`: Either `evictable` or `non-evictable`. Evictable memory is memory that can be easily reclaimed by the kernel, while non-evictable memory cannot.   
`container/memory/swap_used_bytes` GA ** _(project)_**   
Container swap used bytes   
`GAUGE`, `INT64`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Bytes of swap memory used by the container. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/memory/used_bytes` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Memory usage in bytes. Sampled every 60 seconds._   
`memory_type`: Either `evictable` or `non-evictable`. Evictable memory is memory that can be easily reclaimed by the kernel, while non-evictable memory cannot.   
`container/multislice/accelerator/allocator_usage` BETA ** _(project)_**   
Allocator usage   
`GAUGE`, `INT64`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Peak bytes allocated from the premapped region of Megascale block allocator. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/accelerator/compute_latencies` BETA ** _(project)_**   
Host compute latencies   
`DELTA`, `DISTRIBUTION`, `us`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of host compute latency for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`buffer_size`: Size of the buffer.   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/accelerator/device_to_host_transfer_latencies` GA ** _(project)_**   
Device to Host transfer latencies   
`DELTA`, `DISTRIBUTION`, `us`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of device to host transfer latency for each chunk of data for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`buffer_size`: Size of the buffer.   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/accelerator/host_to_device_transfer_latencies` GA ** _(project)_**   
Host to Device transfer latencies   
`DELTA`, `DISTRIBUTION`, `us`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of host to device transfer latency for each chunk of data for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`buffer_size`: Size of the buffer.   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/compute/mxla_compute_latencies` BETA ** _(project)_**   
Megascale compute latencies   
`DELTA`, `DISTRIBUTION`, `us`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of compute latencies for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/compute/mxla_compute_operand_sizes` BETA ** _(project)_**   
Megascale compute operand sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of compute operand sizes for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/network/collective_end_to_end_latencies` GA ** _(project)_**   
Collective latencies   
`DELTA`, `DISTRIBUTION`, `us`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of end to end collective latency for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`collective_type`: Collective operation type.   
`input_size`: Size of the message.   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/network/collective_input_sizes` BETA ** _(project)_**   
Collective input sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of collective input sizes for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`collective_type`: Collective operation type.   
`execution_type`: Execution type.   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/network/dcn_inbound_transfer_latencies` BETA ** _(project)_**   
DCN (Data Center Network) inbound transfer latencies   
`DELTA`, `DISTRIBUTION`, `us`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of inbound network transfer latencies for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`buffer_size`: Size of the buffer.   
`type`: Protocol type.   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/network/dcn_inbound_transfer_sizes` BETA ** _(project)_**   
DCN (Data Center Network) inbound transfer sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of inbound network transfer sizes for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`type`: Protocol type.   
`container/multislice/network/dcn_transfer_latencies` GA ** _(project)_**   
DCN (Data Center Network) transfer latencies   
`DELTA`, `DISTRIBUTION`, `us`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of network transfer latencies for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`buffer_size`: Size of the buffer.   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`type`: Protocol Type.   
`container/multislice/network/dcn_transfer_sizes` BETA ** _(project)_**   
DCN (Data Center Network) transfer sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of network transfer sizes for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`type`: Protocol type.   
`container/multislice/network/device_to_host_transfer_sizes` BETA ** _(project)_**   
Device to Host transfer sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of device to host transfer sizes for each chunk of data for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/network/grpc_tcp_delivery_rates` BETA ** _(project)_**   
GRPC TCP Delivery Rates   
`DELTA`, `DISTRIBUTION`, `Mbps`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of gRPC TCP delivery rates for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/network/grpc_tcp_min_round_trip_times` BETA ** _(project)_**   
GRPC TCP Minimum Round Trip Times   
`DELTA`, `DISTRIBUTION`, `us`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of gRPC TCP min round trip times for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/multislice/network/host_to_device_transfer_sizes` BETA ** _(project)_**   
Host to Device transfer sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of host to device transfer sizes for each chunk of data for multislice traffic. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`container/restart_count` GA ** _(project)_**   
Restart count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of times the container has restarted. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`container/uptime` GA ** _(project)_**   
Uptime   
`GAUGE`, `DOUBLE`, `s`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Time in seconds that the container has been running. Sampled every 60 seconds._  
`gcsfusecsi/file_cache_read_bytes_count` BETA ** _(project)_**   
File cache read bytes count   
`CUMULATIVE`, `INT64`, `By`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The cumulative number of bytes read from file cache along with read type - Sequential/Random. Sampled every 10 seconds._   
`read_type`: Type of read, either sequential or random.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/file_cache_read_count` BETA ** _(project)_**   
File cache read count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Specifies the cumulative number of read requests made via file cache along with type - Sequential/Random and cache hit - true/false. Sampled every 10 seconds._   
`cache_hit`: (BOOL) Cache hit or miss.   
`read_type`: Type of read, either sequential or random.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/file_cache_read_latencies` BETA ** _(project)_**   
File cache read latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The cumulative distribution of the file cache read latencies along with cache hit - true/false. Sampled every 10 seconds._   
`cache_hit`: (BOOL) Cache hit or miss.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/fs_ops_count` BETA ** _(project)_**   
File system operations count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The cumulative number of operations processed by the filesystem. Sampled every 10 seconds._   
`fs_op`: Filesystem operation type.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/fs_ops_error_count` BETA ** _(project)_**   
File system operations error count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The cumulative number of errors generated by filesystem operations. Sampled every 10 seconds._   
`fs_op`: Filesystem operation type.   
`fs_error_category`: Filesystem error category.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/fs_ops_latencies` BETA ** _(project)_**   
File system operation latencies   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The cumulative distribution of filesystem operation latencies. Sampled every 10 seconds._   
`fs_op`: Filesystem operation type.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/gcs_download_bytes_count` BETA ** _(project)_**   
GCS download bytes count   
`CUMULATIVE`, `INT64`, `By`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The cumulative number of bytes downloaded from GCS along with type - Sequential/Random. Sampled every 10 seconds._   
`read_type`: Type of read, either sequential or random.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/gcs_read_bytes_count` BETA ** _(project)_**   
GCS read bytes count   
`CUMULATIVE`, `INT64`, `By`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The cumulative number of bytes read from GCS objects. Sampled every 10 seconds._   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/gcs_read_count` BETA ** _(project)_**   
GCS read count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Specifies the cumulative number of GCS reads made along with type - Sequential/Random. Sampled every 10 seconds._   
`read_type`: Type of read, either sequential or random.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/gcs_reader_count` BETA ** _(project)_**   
GCS reader count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The cumulative number of GCS object readers opened or closed. Sampled every 10 seconds._   
`io_method`: The name of the IO method.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/gcs_request_count` BETA ** _(project)_**   
GCS request count   
`CUMULATIVE`, `INT64`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The cumulative number of GCS requests processed. Sampled every 10 seconds._   
`gcs_method`: The name of the GCS method.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`gcsfusecsi/gcs_request_latencies` BETA ** _(project)_**   
GCS request latencies   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The cumulative distribution of GCS request latencies. Sampled every 10 seconds._   
`gcs_method`: The name of the GCS method.   
`volume_name`: Name of the GCSFuse CSI backed volume.   
`bucket_name`: Name of the GCS Bucket.   
`pod_uid`: Pod UID.   
`jobset/assigned_node_pools` GA ** _(project)_**   
Node Pools where Jobset Pods are Scheduled   
`GAUGE`, `BOOL`, `1`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _GKE node pools where a Kubernetes Jobset has scheduled Pods. Jobset's entity_uid will be left empty if its value is not found in Jobset Pod labels. A value of True indicates that there is at least one Jobset Pod scheduled in the node pool; a value of False is written to mark the moment when this is no longer the case. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`node_pool_name`: The node pool name where at least one Jobset Pod is scheduled.   
`jobset/assigned_nodes` GA ** _(project)_**   
Nodes where Jobset Pods are Scheduled   
`GAUGE`, `BOOL`, `1`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _GKE nodes where a Kubernetes Jobset has scheduled Pods. Jobset's entity_uid will be left empty if its value is not found in Jobset Pod labels. A value of True indicates that there is at least one Jobset Pod scheduled in the node; a value of False is written to mark the moment when this is no longer the case. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`node_name`: The node name where at least one Jobset Pod is scheduled.   
`jobset/assigned_slices` BETA ** _(project)_**   
Slices where Jobset Pods are Scheduled   
`GAUGE`, `BOOL`, `1`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _The TPU slices where a Kubernetes jobset is scheduled. A value of True indicates that there is at least one Jobset scheduled in the slice; a value of False is written to mark the moment when this is no longer the case. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`slice_id`: The slice ID where at least one Jobset Pod is scheduled.   
`slice_name`: The slice name where at least one Jobset Pod is scheduled.   
`node_pool_name`: The node pool name of the slice and the corresponding jobset.   
`block_id`: The superpod ID of slice's associated block.   
`accelerator_type`: Type of the accelerator. Such as tpu7x.   
`jobset/proxy_runtime_goodput` GA ** _(project)_**   
JobSet Proxy Runtime Goodput   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _The duration when all active accelerators are productive (duty_cycle > 10). Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._  
`jobset/scheduling_goodput` GA ** _(project)_**   
JobSet Scheduling Goodput   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _The duration when the GKE resources (k8s pods) are ready to run the GKE training jobs. Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._  
`jobset/startup_duration` BETA ** _(project)_**   
Jobset Startup Duration   
`GAUGE`, `DOUBLE`, `s`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _The duration time in seconds from a JobSet's creation to its initial availability or the current time. The metric is available when a JobSet is created. This metric does not include a JobSet older than 7 days. It is expected that the sample has a discrepancy up to 60s due to processing latency. Sampled every 60 seconds. This metric is only applicable for JobSets with one single GPU/TPU replicated job. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`jobset/times_between_interruptions` GA ** _(project)_**   
Distribution of times between the end of last interruption and beginning of current interruption.   
`GAUGE`, `DISTRIBUTION`, `s`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _Distribution of times between the end of last interruption and beginning of current interruption for a JobSet. Each sample indicates a single duration between last and current interruption. The data is sampled within 60s after the current interruption starts, and emitted within 1h. This metric may not include a sample for duration between interruption shorter than 60s or longer than 7 days. It is expected that the sample has a discrepancy up to 60s due to processing latency. This metric is only applicable for JobSets with one single GPU/TPU replicated jobs (i.e., JobSets could contain non-GPU/TPU replicated jobs, but there should be only one GPU/TPU replicated job). The metric calculation is only based on the availability of that single GPU/TPU replicated job. The first uptime period after provisioning is included as a TBI. The last uptime period before terminating is included as a TBI only if the JobSet completes due to failures. Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._  
`jobset/times_to_recover` GA ** _(project)_**   
Distribution of recovery period durations.   
`GAUGE`, `DISTRIBUTION`, `s`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _Distribution of recovery period durations. Each sample indicates a single recovery operation for the JobSet to recover from a downtime period. The data is sampled within 60s after the completion of JobSet recovery, and emitted within 1h. This metric may not include a sample for downtime periods shorter than 60s or longer than 7 days. It is expected that the sample has a discrepancy up to 60s due to processing latency. This metric is only applicable for JobSets with one single GPU/TPU replicated jobs (i.e., JobSets could contain non-GPU/TPU replicated jobs, but there should be only one GPU/TPU replicated job). The metric calculation is only based on the availability of that single GPU/TPU replicated job. The provisioning period is not considered as a TTR. Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._  
`jobset/uptime` GA ** _(project)_**   
Time in seconds that the JobSet has been up.   
`GAUGE`, `DOUBLE`, `s`   
**[k8s_entity](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_entity)** |  _Total time the JobSet has been available. The data is sampled every 60s and emitted within 1h after sampling. This metric may not include a sample for JobSets being up less than 120s. This metric is only applicable for JobSets with one single GPU/TPU replicated jobs (i.e., JobSets could contain non-GPU/TPU replicated jobs, but there should be only one GPU/TPU replicated job). The metric calculation is only based on the availability of that single GPU/TPU replicated job. Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._  
`networking/dns/kubedns/dns_cache_request_count` BETA ** _(project)_**   
KubeDNS Cache Hit/Miss Count   
`DELTA`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of KubeDNS cache hits and misses. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`dns_zone`: DNS zones.   
`status`: Cache status: cache_hit or cache_miss.   
`server`: DNS server IP.   
`view`: DNS view name.   
`type`: Indicates if this was a success or denial (NXDOMAIN).   
`networking/dns/kubedns/dns_request_count` BETA ** _(project)_**   
KubeDNS Request Count   
`DELTA`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of DNS requests processed by KubeDNS. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`family`: The address family of the transport (ipv4 or ipv6).   
`type`: Query type (e.g. A, AAAA, MX, ...).   
`proto`: Transport protocol used for DNS query.   
`dns_zone`: DNS zone.   
`server`: DNS server IP.   
`view`: DNS view name.   
`networking/dns/kubedns/dns_request_latencies` BETA ** _(project)_**   
KubeDNS Request Latency   
`DELTA`, `DISTRIBUTION`, `s`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Histogram of the time (in seconds) each KubeDNS request took. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`dns_zone`: DNS zone.   
`view`: DNS view name.   
`server`: DNS server IP.   
`type`: Query type (e.g. A, AAAA, MX, ...).   
`networking/dns/kubedns/forwarding_request_latencies` BETA ** _(project)_**   
KubeDNS Upstream Request Latency   
`DELTA`, `DISTRIBUTION`, `s`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Histogram of the time (in seconds) each forwarded KubeDNS request took. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`type`: Query type (e.g. A, AAAA, MX, ...).   
`rcode`: DNS return code.   
`to`: Upstream DNS server.   
`proxy_name`: Proxy name.   
`networking/dns/kubedns/max_concurrent_rejected_request_count` BETA ** _(project)_**   
KubeDNS Max Concurrent Reject Count   
`DELTA`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total number of KubeDNS queries rejected because the number of concurrent queries were at maximum. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`networking/dns/node_local_dns/dns_cache_request_count` BETA ** _(project)_**   
NodeLocalDNS Cache Hit/Miss Count   
`DELTA`, `INT64`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Total number of NodeLocalDNS cache hits and misses. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`dns_zone`: DNS zones.   
`status`: Cache status: cache_hit or cache_miss.   
`server`: DNS server IP.   
`type`: Indicates if this was a success or denial (NXDOMAIN).   
`networking/dns/node_local_dns/dns_request_count` BETA ** _(project)_**   
NodeLocalDNS Request Count   
`DELTA`, `INT64`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Total number of DNS requests processed by NodeLocalDNS. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`family`: The address family of the transport (ipv4 or ipv6).   
`type`: Query type (e.g. A, AAAA, MX, ...).   
`proto`: Transport protocol used for DNS query.   
`dns_zone`: DNS zone.   
`server`: DNS server IP.   
`view`: DNS view name.   
`networking/dns/node_local_dns/dns_request_latencies` BETA ** _(project)_**   
NodeLocalDNS Request Latency   
`DELTA`, `DISTRIBUTION`, `s`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Histogram of the time (in seconds) each NodeLocalDNS request took. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`dns_zone`: DNS zone.   
`view`: DNS view name.   
`server`: DNS server IP.   
`type`: Query type (e.g. A, AAAA, MX, ...).   
`networking/dns/node_local_dns/forwarding_request_latencies` BETA ** _(project)_**   
NodeLocalDNS Upstream Request Latency   
`DELTA`, `DISTRIBUTION`, `s`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Histogram of the time (in seconds) each forwarded NodeLocalDNS request took. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`type`: Query type (e.g. A, AAAA, MX, ...).   
`rcode`: DNS return code.   
`to`: Upstream DNS server.   
`proxy_name`: Proxy name.   
`networking/dns/node_local_dns/max_concurrent_rejected_request_count` BETA ** _(project)_**   
NodeLocalDNS Max Concurrent Reject Count   
`DELTA`, `INT64`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Total number of NodeLocalDNS queries rejected because the number of concurrent queries were at maximum. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/accelerator/duty_cycle` GA ** _(project)_**   
Accelerator duty cycle with node   
`GAUGE`, `DOUBLE`, `percent`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Percent of time over the past sample period (10s) during which the accelerator was actively processing. Sampled every 60 seconds._   
`make`: Make of the accelerator.   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator.   
`node/accelerator/memory_bandwidth_utilization` GA ** _(project)_**   
Memory bandwidth utilization   
`GAUGE`, `DOUBLE`, `percent`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Current percentage of the accelerator memory bandwidth that is being used. Computed by dividing the memory bandwidth used over a sample period by the maximum supported bandwidth over the same sample period. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`node/accelerator/memory_total` GA ** _(project)_**   
Accelerator memory total with node   
`GAUGE`, `INT64`, `bytes`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Total accelerator memory in bytes. Sampled every 60 seconds._   
`make`: Make of the accelerator.   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator.   
`node/accelerator/memory_used` GA ** _(project)_**   
Accelerator memory used with node   
`GAUGE`, `INT64`, `bytes`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Total accelerator memory allocated in bytes. Sampled every 60 seconds._   
`make`: Make of the accelerator.   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator.   
`node/accelerator/tensorcore_utilization` GA ** _(project)_**   
Tensorcore utilization   
`GAUGE`, `DOUBLE`, `percent`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Current percentage of the Tensorcore that is utilized. Computed by dividing the Tensorcore operations that were performed over a sample period by the supported number of Tensorcore operations over the same sample period. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`make`: Make of the accelerator.   
`accelerator_id`: ID of the accelerator.   
`model`: Model of the accelerator.   
`tpu_topology`: Topology of the TPU accelerator.   
`node/assigned_jobsets` GA ** _(project)_**   
Nodes where Jobset Pods are Scheduled   
`GAUGE`, `BOOL`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _GKE nodes where a Kubernetes Jobset has scheduled Pods. jobset_uid will be left empty if its value is not found in Jobset Pod labels. A value of True indicates that there is at least one Jobset Pod scheduled in the node; a value of False is written to mark the moment when this is no longer the case. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`jobset_namespace`: The namespace name where at least one Jobset Pod is scheduled.   
`jobset_name`: The Jobset name where at least one Jobset Pod is scheduled.   
`jobset_uid`: The jobset_uid field is populated with the Jobset's UID if found in Pod labels. Otherwise, the field is left empty.   
`node/cpu/allocatable_cores` GA ** _(project)_**   
Allocatable cores   
`GAUGE`, `DOUBLE`, `{cpu}`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Number of allocatable CPU cores on the node. Sampled every 60 seconds._  
`node/cpu/allocatable_utilization` GA ** _(project)_**   
CPU allocatable utilization   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _The fraction of the allocatable CPU that is currently in use on the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._  
`node/cpu/core_usage_time` GA ** _(project)_**   
CPU usage time   
`CUMULATIVE`, `DOUBLE`, `s{CPU}`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Cumulative CPU usage on all cores used on the node in seconds. Sampled every 60 seconds._  
`node/cpu/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Node CPU some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which some tasks are stalled on CPU at node level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/cpu/total_cores` GA ** _(project)_**   
Total cores   
`GAUGE`, `DOUBLE`, `{cpu}`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Total number of CPU cores on the node. Sampled every 60 seconds._  
`node/ephemeral_storage/allocatable_bytes` GA ** _(project)_**   
Allocatable ephemeral storage   
`GAUGE`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Local ephemeral storage bytes allocatable on the node. Sampled every 60 seconds._  
`node/ephemeral_storage/inodes_free` GA ** _(project)_**   
Free inodes   
`GAUGE`, `INT64`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Free number of inodes on local ephemeral storage. Sampled every 60 seconds._  
`node/ephemeral_storage/inodes_total` GA ** _(project)_**   
Total inodes   
`GAUGE`, `INT64`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Total number of inodes on local ephemeral storage. Sampled every 60 seconds._  
`node/ephemeral_storage/total_bytes` GA ** _(project)_**   
Total ephemeral storage   
`GAUGE`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Total ephemeral storage bytes on the node. Sampled every 60 seconds._  
`node/ephemeral_storage/used_bytes` GA ** _(project)_**   
Ephemeral storage usage   
`GAUGE`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Local ephemeral storage bytes used by the node. Sampled every 60 seconds._  
`node/interruption_count` GA ** _(project)_**   
Interruption Count   
`GAUGE`, `INT64`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Interruptions are system evictions of infrastructure while the customer is in control of that infrastructure. This metric is the current count of interruptions by type and reason. The stream is often undefined when the count is zero. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`interruption_type`: Type of interruption.   
`interruption_reason`: Reason for interruption.   
`node/io/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Node IO full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which all tasks are stalled on IO at node level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/io/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Node IO some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which some tasks are stalled on IO at node level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/latencies/startup` GA ** _(project)_**   
Node startup latency   
`GAUGE`, `INT64`, `s`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _The total startup latency of the node, from GCE instance's CreationTimestamp to K8s node ready first time. Sampled every 60 seconds._   
`accelerator_family`: A classification of nodes based on hardware accelerators: gpu, tpu, cpu.   
`kube_control_plane_available`: Whether the node creation request was received when KCP (kube control plane) was available.   
`node/logs/input_bytes` GA ** _(project)_**   
Logging throughput   
`DELTA`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Volume of log bytes generated on the node by user and system workloads. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`type`: Type is either 'system' or 'workload'. 'system' indicates the logging throughput of GKE system components. 'workload' indicates the throughput of logs generated by non-system containers running on user nodes.   
`node/memory/allocatable_bytes` GA ** _(project)_**   
Allocatable memory   
`GAUGE`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Number of bytes of memory that can be allocated for workloads on the node. Sampled every 60 seconds._  
`node/memory/allocatable_utilization` GA ** _(project)_**   
Memory allocatable utilization   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _The fraction of the allocatable memory that is currently in use on the instance. This value cannot exceed 1 as usage cannot exceed allocatable memory bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`memory_type`: Either `evictable` or `non-evictable`. Evictable memory is memory that can be easily reclaimed by the kernel, while non-evictable memory cannot.   
`component`: Name of the respective system daemon.   
`node/memory/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Node Memory full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which all tasks are stalled on Memory at node level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/memory/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Node Memory some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which some tasks are stalled on Memory at node level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/memory/swap_used_bytes` GA ** _(project)_**   
Node swap used bytes   
`GAUGE`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Bytes of swap memory used by the node. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node/memory/total_bytes` GA ** _(project)_**   
Total memory   
`GAUGE`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Total number of bytes of memory on the node. Sampled every 60 seconds._  
`node/memory/used_bytes` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Cumulative memory bytes used by the node. Sampled every 60 seconds._   
`memory_type`: Either `evictable` or `non-evictable`. Evictable memory is memory that can be easily reclaimed by the kernel, while non-evictable memory cannot.   
`node/network/received_bytes_count` GA ** _(project)_**   
Bytes received   
`CUMULATIVE`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Cumulative number of bytes received by the node over the network. Sampled every 60 seconds._  
`node/network/sent_bytes_count` GA ** _(project)_**   
Bytes transmitted   
`CUMULATIVE`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Cumulative number of bytes transmitted by the node over the network. Sampled every 60 seconds._  
`node/pid_limit` GA ** _(project)_**   
PID capacity   
`GAUGE`, `INT64`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _The max PID of OS on the node. Sampled every 60 seconds._  
`node/pid_used` GA ** _(project)_**   
PID usage   
`GAUGE`, `INT64`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _The number of running process in the OS on the node. Sampled every 60 seconds._  
`node/status_condition` GA ** _(project)_**   
Kubernetes node status condition   
`GAUGE`, `BOOL`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Condition of a node from the node status condition field. Ready has `Unknown` status if the node controller has not heard from the node in the last `node-monitor-grace-period`. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: Status of the condition. True, False, or Unknown.   
`condition`: The condition of the node.   
`node_daemon/cpu/core_usage_time` GA ** _(project)_**   
CPU usage time   
`CUMULATIVE`, `DOUBLE`, `s{CPU}`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Cumulative CPU usage on all cores used by the node level system daemon in seconds. Sampled every 60 seconds._   
`component`: Name of the respective system daemon.   
`node_daemon/cpu/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Node daemon CPU full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which all tasks are stalled on CPU at node daemon level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: Name of the respective system daemon.   
`node_daemon/cpu/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Node daemon CPU some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which some tasks are stalled on CPU at node daemon level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: Name of the respective system daemon.   
`node_daemon/io/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Node daemon IO full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which all tasks are stalled on IO at node daemon level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: Name of the respective system daemon.   
`node_daemon/io/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Node daemon IO some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which some tasks are stalled on IO at node daemon level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: Name of the respective system daemon.   
`node_daemon/memory/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Node daemon Memory full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which all tasks are stalled on Memory at node daemon level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: Name of the respective system daemon.   
`node_daemon/memory/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Node daemon Memory some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Fraction of time in which some tasks are stalled on Memory at node daemon level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`component`: Name of the respective system daemon.   
`node_daemon/memory/used_bytes` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[k8s_node](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node)** |  _Memory usage by the system daemon in bytes. Sampled every 60 seconds._   
`component`: Name of the respective system daemon.   
`memory_type`: Either `evictable` or `non-evictable`. Evictable memory is memory that can be easily reclaimed by the kernel, while non-evictable memory cannot.   
`node_pool/accelerator/startup_duration` BETA ** _(project)_**   
Multi-host NodePool Startup Duration   
`GAUGE`, `DOUBLE`, `s`   
**[k8s_node_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node_pool)** |  _The duration time in seconds from a NodePool's creation to its initial availability or the current time. The metric is available when a NodePool is created. This metric does not include a NodePool older than 7 days. It is expected that the sample has a discrepancy up to 60s due to processing latency. Sampled every 60 seconds. Multi-host TPU node pool only. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`node_pool/accelerator/times_between_interruptions` GA ** _(project)_**   
Distribution of times between the end of last interruption and beginning of current interruption.   
`GAUGE`, `DISTRIBUTION`, `s`   
**[k8s_node_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node_pool)** |  _Distribution of times between the end of last interruption and beginning of current interruption. Each sample indicates a single duration between last and current interruption. The data is sampled within 60s after the current interruption starts, and emitted within 1h. This metric may not include a sample for duration periods shorter than 60s or longer than 7 days. The metric is only applicable for GKE multi-host TPU node pools. Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._  
`node_pool/accelerator/times_to_recover` GA ** _(project)_**   
Distribution of recovery period durations.   
`GAUGE`, `DISTRIBUTION`, `s`   
**[k8s_node_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node_pool)** |  _Distribution of recovery period durations. Each sample indicates a single recovery operation for the NodePool to recover from a downtime period. The data is sampled within 60s after the completion of NodePool recovery, and emitted within 1h. This metric may not include a sample for downtime periods shorter than 60s or longer than 7 days. This metric is only applicable for GKE multi-host TPU node pools. Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._  
`node_pool/assigned_jobsets` GA ** _(project)_**   
Node Pools where Jobset Pods are Scheduled   
`GAUGE`, `BOOL`, `1`   
**[k8s_node_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node_pool)** |  _GKE node pools where a Kubernetes Jobset has scheduled Pods. jobset_uid will be left empty if its value is not found in Jobset Pod labels. A value of True indicates that there is at least one Jobset Pod scheduled in the node pool; a value of False is written to mark the moment when this is no longer the case. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`jobset_namespace`: The namespace name where at least one Jobset Pod is scheduled.   
`jobset_name`: The Jobset name where at least one Jobset Pod is scheduled.   
`jobset_uid`: The jobset_uid field is populated with the Jobset's UID if found in Pod labels. Otherwise, the field is left empty.   
`node_pool/interruption_count` GA ** _(project)_**   
Interruption Count   
`GAUGE`, `INT64`, `1`   
**[k8s_node_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node_pool)** |  _The count of interruptions to all nodes in the node pool, by interruption-type and interruption-reason, since the last sample. The stream is often undefined when the count is zero. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`interruption_type`: Type of interruption.   
`interruption_reason`: Reason for interruption.   
`node_pool/multi_host/available` GA ** _(project)_**   
Kubernetes Multi-host TPU Node Pool Availability   
`GAUGE`, `BOOL`, `1`   
**[k8s_node_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node_pool)** |  _Whether or not the multi-host NodePool is available. Is True when all Nodes in the NodePool are available, and False if any of the Nodes in the NodePool are unavailable. Multi-host TPU node pool only. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`unavailability_reason`: Reason for a node pool unavailability. This label is empty when the node pool is available. Possible reasons include `MaintenanceTaint`, `RebootEvent`, `Reconciling`, `Stopping`, `Unallocatable`, `Unhealthy`, `MachineNotRunning`, or `ProvisioningError`.   
`node_pool/status` GA ** _(project)_**   
Kubernetes Node Pool Status   
`GAUGE`, `BOOL`, `1`   
**[k8s_node_pool](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node_pool)** |  _Current status of the NodePool from the NodePool instance. Status updates will happen after GKE API operations complete. Multi-host TPU node pool only. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`status`: Status of the nodepool.   
`pod/cpu/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Pod CPU full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Fraction of time in which all tasks are stalled on CPU at pod level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`pod/cpu/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Pod CPU some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Fraction of time in which some tasks are stalled on CPU at pod level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`pod/ephemeral_storage/used_bytes` GA ** _(project)_**   
Ephemeral pod storage usage   
`GAUGE`, `INT64`, `By`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Pod ephemeral storage usage in bytes. Sampled every 60 seconds._  
`pod/io/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Pod IO full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Fraction of time in which all tasks are stalled on IO at pod level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`pod/io/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Pod IO some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Fraction of time in which some tasks are stalled on IO at pod level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`pod/latencies/pod_first_ready` GA ** _(project)_**   
Pod first ready latency   
`GAUGE`, `DOUBLE`, `s`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The Pod end-to-end startup latency (from Pod Created to Ready), including image pulls. Sampled every 60 seconds._  
`pod/memory/pressure/full/total_stall_time_seconds` BETA ** _(project)_**   
Pod Memory full pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Fraction of time in which all tasks are stalled on Memory at pod level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`pod/memory/pressure/some/total_stall_time_seconds` BETA ** _(project)_**   
Pod Memory some pressure   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Fraction of time in which some tasks are stalled on Memory at pod level. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._  
`pod/network/policy_event_count` BETA ** _(project)_**   
Network policy event count   
`DELTA`, `INT64`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Change in the number of network policy events seen in the dataplane. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`verdict`: Policy verdict, possible values: [allow, deny].   
`workload_kind`: Kind of the workload, policy-enforced-pod belongs to, for example, "Deployment", "Replicaset", "StatefulSet", "DaemonSet", "Job" or "CronJob".   
`workload_name`: Name of the workload, policy-enforced-pod belongs to.   
`direction`: Direction of the traffic from the point of view of policy-enforced-pod, possible values: [ingress, egress].   
`pod/network/received_bytes_count` GA ** _(project)_**   
Bytes received   
`CUMULATIVE`, `INT64`, `By`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Cumulative number of bytes received by the pod over the network. Sampled every 60 seconds._   
`interface`: The name of the interface (e.g. `eth0`).   
`pod/network/sent_bytes_count` GA ** _(project)_**   
Bytes transmitted   
`CUMULATIVE`, `INT64`, `By`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Cumulative number of bytes transmitted by the pod over the network. Sampled every 60 seconds._   
`interface`: The name of the interface (e.g. `eth0`).   
`pod/volume/total_bytes` GA ** _(project)_**   
Volume capacity   
`GAUGE`, `INT64`, `By`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Total number of disk bytes available to the pod. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`volume_name`: The name of the volume (e.g. `/dev/sda1`).   
`persistentvolumeclaim_name`: The name of the referenced Persistent Volume Claim.   
`persistentvolumeclaim_namespace`: The namespace of the referenced Persistent Volume Claim.   
`pod/volume/used_bytes` GA ** _(project)_**   
Volume usage   
`GAUGE`, `INT64`, `By`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Number of disk bytes used by the pod. Sampled every 60 seconds._   
`volume_name`: The name of the volume (e.g. `/dev/sda1`).   
`persistentvolumeclaim_name`: The name of the referenced Persistent Volume Claim.   
`persistentvolumeclaim_namespace`: The namespace of the referenced Persistent Volume Claim.   
`pod/volume/utilization` GA ** _(project)_**   
Volume utilization   
`GAUGE`, `DOUBLE`, `1`   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _The fraction of the volume that is currently being used by the instance. This value cannot be greater than 1 as usage cannot exceed the total available volume space. Sampled every 60 seconds. After sampling, data is not visible for up to 120 seconds._   
`volume_name`: The name of the volume (e.g. `/dev/sda1`).   
`persistentvolumeclaim_name`: The name of the referenced Persistent Volume Claim.   
`persistentvolumeclaim_namespace`: The namespace of the referenced Persistent Volume Claim.   
  
### nginx

Metrics exported from the [NGINX Prometheus Exporter](https://github.com/nginxinc/nginx-prometheus-exporter#exported-metrics). Launch stages of these metrics: ALPHA

The "metric type" strings in this table must be prefixed with `kubernetes.io/nginx/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`connections_accepted` ALPHA ** _(project)_**   
Nginx connections_accepted   
`CUMULATIVE`, `INT64`, `{connection}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Accepted client connections. Sampled every 60 seconds._  
`connections_active` ALPHA ** _(project)_**   
Nginx connections_active   
`GAUGE`, `INT64`, `{connection}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Active client connections. Sampled every 60 seconds._  
`connections_handled` ALPHA ** _(project)_**   
Nginx connections_handled   
`CUMULATIVE`, `INT64`, `{connection}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Handled client connections. Sampled every 60 seconds._  
`connections_reading` ALPHA ** _(project)_**   
Nginx connections_reading   
`GAUGE`, `INT64`, `{connection}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Connections where NGINX is reading the request header. Sampled every 60 seconds._  
`connections_waiting` ALPHA ** _(project)_**   
Nginx connections_waiting   
`GAUGE`, `INT64`, `{connection}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Idle client connections. Sampled every 60 seconds._  
`connections_writing` ALPHA ** _(project)_**   
Nginx connections_writing   
`GAUGE`, `INT64`, `{connection}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Connections where NGINX is writing the response back to the client. Sampled every 60 seconds._  
`http_requests_total` ALPHA ** _(project)_**   
Nginx http_requests_total   
`CUMULATIVE`, `INT64`, `{request}`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Total http requests. Sampled every 60 seconds._  
`nginxexporter_build_info` ALPHA ** _(project)_**   
Nginx nginxexporter_build_info   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Exporter build information. Sampled every 60 seconds._   
`gitCommit`: Commit hash of the build which can be abbreviated.   
`version`: Build version.   
`up` ALPHA ** _(project)_**   
Nginx up   
`GAUGE`, `INT64`, `1`   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Status of the last metric scrape. Indicates if the server is up or not. Sampled every 60 seconds._  
  
Generated at 2026-10-14 20:24:33 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
