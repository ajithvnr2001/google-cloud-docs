---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/monitor/
title: Monitor Compute Engine instances and Slurm clusters \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:48.291162+00:00
---

# Monitor Compute Engine instances and Slurm clusters  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Monitor Compute Engine instances and Slurm clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document explains how to use [Cloud Monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards) to monitor A4X Max, A4X, A4, A3 Ultra, and A3 Mega instances that you created by using reservation-bound capacity. Using these dashboards helps you identify and troubleshoot performance bottlenecks in your standalone Compute Engine instances or Slurm clusters, minimizing downtime in your workloads.

By creating custom dashboards or using prebuilt Monitoring dashboards, you can monitor the following:

  * Compute instance health

  * GPU performance

  * Network transmission efficiency

  * Network efficiency among blocks and sub-blocks

  * Machine learning (ML) workload efficiency

  * Straggler detection

  * Unresponsive workload detection




To monitor clusters Cluster Director, see [Monitor cluster performance with prebuilt dashboards](https://docs.cloud.google.com/cluster-director/docs/monitor/dashboards).

## Before you begin

Before monitoring your workload, if you haven't already done so, complete the following steps:

  * **Deploy a workload that you can monitor**. To learn which workloads are supported, see the limitations in this document. To learn how to deploy a workload, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

  * **Learn about the Google Cloud services for monitoring workloads** :

    * The metrics in this document use Monitoring dashboards. Learn about [Monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards), [Monitoring retention periods](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy), and [Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-costs).

    * Straggler detection also provides log entries in Cloud Logging. Learn about [Logging interfaces](https://docs.cloud.google.com/logging/docs/log-analytics), [Logging retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods), and [Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary).




When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### Limitations

  * The metrics in this document are only supported for workloads that run on compute instances that meet all the following criteria:

    * The compute instances must be created as either standalone Compute Engine instances or as part of a Slurm cluster.
    * The compute instances must have been created by using reservation-bound capacity.
    * The compute instances must use the A4X Max, A4X, A4, A3 Ultra, or A3 Mega [machine series](https://docs.cloud.google.com/ai-hypercomputer/docs/gpu). 
      * However, straggler detection also supports virtual machine (VM) instances that use the A3 Mega machine series.
**Caution:** Although metrics might appear for other machine series than A4X Max, A4X, A4, A3 Ultra, or A3 Mega, those metrics might be incorrect.
  * **Known issues for infrastructure metrics:**
    * Some compute instances might not display `GPU Power Consumption` metrics.
    * Some compute instances might not display `GPU Temperature` or `GPU Thermal Margin` metrics, or they might display `NaN` instead of metrics.
    * Metrics might not appear in the Google Cloud console for up to seven minutes after they're collected.
    * You might see incorrect metrics for machine series other than A4X Max, A4X, A4, A3 Ultra, or A3 Mega.



The metrics in this document are only supported for workloads that run on compute instances that meet all of the following criteria:

  * The compute instances must be created as either standalone Compute Engine instances or as part of a Slurm cluster.
  * The compute instances must have been created by using reserved capacity.
  * The compute instances must use the A4X Max, A4X, A4, A3 Ultra, or A3 Mega [machine series](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus).



To monitor ML workload metrics, you must [set up monitoring for your workload](https://github.com/AI-Hypercomputer/ml-goodput-measurement).

#### Straggler detection limitations

Straggler detection metrics have the following additional limitations:

  * For supported machine series other than A3 Mega, straggler detection only supports compute instances that enable the Collective Communication Analyzer (CoMMA) library to export NCCL telemetry to Google Cloud services. For more information, see [CoMMA overview](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma).
  * Straggler detection typically takes up to 10 minutes to report a straggler.
  * Unlike the other metrics in this document, you can't filter straggler detection metrics for your projects by cluster, block, sub-block, or compute instance. However, you can filter queries for straggler detection logs by the ID of one or more compute instances that are suspected stragglers.



**Caution** : You might see false positives or false negatives when using straggler detection such as, but not limited to, the following:

  * Straggler detection logs report that running compute instances that don't support straggler detection aren't suspected stragglers.
  * Although straggler detection is accurate for many ML workloads, inaccuracies are more likely for workloads with complex communication patterns.



Consequently, we recommend that you act on suspected stragglers only when other metrics indicate that the workload is experiencing issues. Otherwise, if the overall performance of the workload is satisfactory, then no action is recommended.

#### Unresponsive workload detection limitations

Unresponsive workload detection metrics only support compute instances that use the Collective Communication Analyzer (CoMMA) library to export NCCL telemetry to Google Cloud services. For more information, see [CoMMA overview](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma).

### Required roles

To get the permissions that you need to monitor metrics for AI Hypercomputer workloads, ask your administrator to grant you the following IAM roles: 

  * To view metrics in Cloud Monitoring: [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) on the project 
  * To view straggler detection logs in Logging: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to monitor metrics for AI Hypercomputer workloads. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to monitor metrics for AI Hypercomputer workloads:

  * To view dashboards: `monitoring.dashboards.get` on the project 
  * To create dashboards: `monitoring.dashboards.create` on the project 
  * To view log entries: `logging.logEntries.list` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Available metrics

Depending on your use case, the following metrics are available for monitoring your compute instances and Slurm clusters:

  * To monitor the health, performance, and network performance of the GPUs attached to your compute instances, see Infrastructure metrics.

  * To monitor the efficiency of the GPUs in your ML workloads, see ML workload metrics.

  * To monitor suspected straggler compute instances in ML workloads with slow performance, see Straggler detection metrics.




To learn how to view these metrics, see Visualize metrics in this document.

### Infrastructure metrics

To monitor the health, performance, and network performance of the GPUs attached to your compute instances, you can use the following metrics:

  * GPU health metrics

  * GPU performance metrics

  * GPU network performance metrics

  * Top-of-rack (ToR) switch metrics

  * GPU fatal errors metrics




For an overview of available metrics in Compute Engine, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute).

#### GPU health metrics

To monitor the health of your GPUs, use the following metrics:

Name | Metric type | Supported machine series | Description  
---|---|---|---  
Machine Status | `machine/machine_status` | A4X Max, A4X, A4, A3 Ultra, or A3 Mega | Whether the machine that the compute instance uses is healthy, or the machine is unhealthy and requires repair.  
NVSwitch Status | `instance/gpu/nvswitch_status` | A4X Max, A4X, A4, A3 Ultra, or A3 Mega | Whether an [NVLink Switch](https://www.nvidia.com/en-gb/data-center/nvlink/) on an NVIDIA GPU attached to a compute instance is encountering issues.   
VM Infra Health | `instance/gpu/infra_health` | A4X, A4, A3 Ultra, or A3 Mega |  The health of the cluster, block, sub-block, and host on which your compute instances are running. If this metric shows that a compute instance's infrastructure is unhealthy, then the metric also describes the issue.  
VM Failure Prediction Score | `instance/gpu/failure_prediction_score` | A4X, A4, A3 Ultra, or A3 Mega |  The likelihood that the host on which the compute instance runs degrades in the next five hours. The value can be between `0.0` and `1.0`. The closer the value remains to `1.0` for a consistent period of time, the more likely the compute instance will degrade. In that case, we recommend that you move the job to a different compute instance and, if you encounter issues with the compute instance, then report its host as faulty.   
  
#### GPU performance metrics

To monitor the performance of your GPUs, use the following metrics:

Name | Metric type | Supported machine series | Description  
---|---|---|---  
Accumulated Context Utilization | `instance/gpu/accumulated_context_utilization_seconds` | A4X Max, A4X, A4, A3 Ultra, or A3 Mega | The total time, in seconds, that the GPU is busy processing a workload.  
GPU Power Consumption | `instance/gpu/power_consumption` | A4X Max, A4X, A4, A3 Ultra, or A3 Mega | The power in watts (W) and in decimal values that is consumed on individual GPUs on the host. For compute instances with multiple GPUs attached, the metric provides the power consumption separately for each GPU on the host.   
SM Utilization | `instance/gpu/sm_utilization` | A4X Max, A4X, A4, A3 Ultra, or A3 Mega | A non-zero value indicates that the streaming multiprocessors (SMs) on your GPUs are actively being used.  
GPU Temperature | `instance/gpu/temperature` | A4X Max, A4X, A4, A3 Ultra, or A3 Mega | The temperature in Celsius (℃) and in decimal values of individual GPUs on the host. For compute instances with multiple GPUs attached, the metric provides the temperature separately for each GPU on the host.   
GPU Thermal Margin | `instance/gpu/tlimit` | A4X Max, A4X, A4, A3 Ultra, or A3 Mega | The thermal headroom in Celsius (℃) and in decimal values that individual GPUs have before they need to slow down due to high temperature. For compute instances with multiple GPUs attached, the metric provides the thermal headroom separately for each GPU on the host.   
  
#### GPU network performance metrics

To monitor the network performance of your GPUs, use the following metrics. To monitor backend ToR network switches, see ToR switch metrics.

Name | Metric type | Supported machine series | Description  
---|---|---|---  
Link Carrier Changes | `instance/gpu/link_carrier_changes` | A4X, A4, A3 Ultra, or A3 Mega | How often the network link carrier changes in a minute.  
Network RTT | `instance/gpu/network_rtt` | A4X, A4, A3 Ultra, or A3 Mega | The round-trip time, measured in microseconds, for network data to travel between a source and destination.  
Network Traffic at Inter-Block | `instance/gpu/network/inter_block_tx` | A4X, A4, A3 Ultra, or A3 Mega | The number of bytes of network traffic among blocks.  
Network Traffic at Inter-Sub-block | `instance/gpu/network/inter_subblock_tx` | A4X, A4, A3 Ultra, or A3 Mega | The number of bytes of network traffic among sub-blocks.  
Network Traffic at Intra-Sub-block | `instance/gpu/network/intra_subblock_tx` | A4X, A4, A3 Ultra, or A3 Mega | The number of bytes of network traffic within a single sub-block.  
NVLink Active Speed | `instance/gpu/nvlink_active_speed` | A4X Max, A4X, A4, A3 Ultra, or A3 Mega | The current access link port speed, in GBps.  
Throughput Rx Bytes | `instance/gpu/throughput_rx_bytes` | A4X, A4, A3 Ultra, or A3 Mega | The number of bytes received from network traffic.  
Throughput Tx Bytes | `instance/gpu/throughput_tx_bytes` | A4X, A4, A3 Ultra, or A3 Mega | The number of bytes transmitted to network traffic.  
  
#### ToR switch metrics

For A4X Max and A4X clusters, you can monitor backend ToR network switch telemetry to do the following during distributed ML training:

  * Observe switch and port health.
  * Evaluate available bandwidth capacity and buffer queue depths.
  * Diagnose packet discards, errors, interface flaps, and congestion management events.



These metrics use the `compute.googleapis.com/NetworkSwitch` monitored resource type and the `compute.googleapis.com/` metric type prefix. In Metrics Explorer, select the **NetworkSwitch** resource type (`compute.googleapis.com/NetworkSwitch`).

Switch metrics are organized into the following categories:

##### Switch health and status metrics

Use the metrics listed in this section to do the following: 

  * Verify the operational status of switch ports.
  * Monitor switch CPU and memory utilization.
  * Check boot times to detect unexpected reboots.

Name | Metric type | Supported machine series | Description  
---|---|---|---  
Port status | `network_switch/port_status` | A4X Max or A4X | Indicates the operational status of the physical interface (port) on the network switch. The metric value is always `1` for aggregation; the actual state is provided in the `status` label (such as `UP` or `DOWN`).  
**Key labels:** `port_identifier`, `status`, `peer_target_identifier`, `peer_port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
CPU utilization | `network_switch/cpu_utilization` | A4X Max or A4X | The CPU utilization of the network switch, measured as a fraction from `0.0` to `1.0`.  
**Key labels:** `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Memory used | `network_switch/memory_used` | A4X Max or A4X | The memory used by the network switch, in bytes.  
**Key labels:** `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Total memory | `network_switch/total_memory_bytes` | A4X Max or A4X | The total memory capacity of the network switch, in bytes.  
**Key labels:** `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Boot time | `network_switch/boot_time_in_ns` | A4X Max or A4X | The boot timestamp of the network switch, in nanoseconds since the Unix epoch.  
**Key labels:** `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
  
##### Switch capacity and queue metrics

To track baseline versus usable network capacity and monitor buffer queue depths and queue drops on the switch, use the following metrics:

Name | Metric type | Supported machine series | Description  
---|---|---|---  
Baseline capacity | `network_switch/baseline_capacity_kbps` | A4X Max or A4X | The total potential baseline bandwidth capacity of a ToR switch connection to the superblock, in kilobits per second (kbit/s).  
**Key labels:** `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Effective capacity | `network_switch/effective_capacity_kbps` | A4X Max or A4X | The usable operational capacity of a ToR switch connection to the superblock, in kilobits per second (kbit/s). This metric reflects capacity reductions caused by degraded or offline links.  
**Key labels:** `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Egress max queue depth | `network_switch/egress_max_queue_depth` | A4X Max or A4X | The maximum queue depth observed during the most recent measurement cycle.  
**Key labels:** `port_identifier`, `queue_name`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Egress queue drops | `network_switch/egress_queue_drops_count` | A4X Max or A4X | The cumulative count of packets dropped from egress queues due to queue congestion or buffer exhaustion.  
**Key labels:** `port_identifier`, `queue_name`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
In buffer discards | `network_switch/in_buffer_discards` | A4X Max or A4X | The cumulative count of incoming packets discarded at ingress due to buffer overflow.  
**Key labels:** `port_identifier`, `peer_target_identifier`, `peer_port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
  
##### Switch drops, errors, and flow control metrics

Use the metrics in this section to diagnose the following issues, which can cause distributed training stalls or collective communication timeouts (such as NCCL watchdog timeouts):

  * Packet discards, transmission errors, and physical link flaps.
  * Forward error correction (FEC) word errors.
  * Congestion management events, such as Priority-based Flow Control (PFC) pauses and Explicit Congestion Notification (ECN) markings.



**Note:** Priority-based Flow Control (PFC) metrics (`network_switch/pfc_rx_packets_count` and `network_switch/pfc_tx_packets_count`) are only applicable to dedicated environments where PFC is enabled.

Name | Metric type | Supported machine series | Description  
---|---|---|---  
Interface flaps | `network_switch/interface_flaps_count` | A4X Max or A4X | The cumulative count of physical link state transitions (flaps between `UP` and `DOWN`) on the switch port interface.  
**Key labels:** `port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Fec word errors | `network_switch/fec_word_error_count` | A4X Max or A4X | The cumulative count of Forward Error Correction (FEC) word errors. Use the `correctable` boolean label (`true` or `false`) to distinguish between correctable and uncorrectable errors.  
**Key labels:** `port_identifier`, `correctable`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Ecn marked packets | `network_switch/ecn_marked_packets_count` | A4X Max or A4X | The cumulative count of packets marked with Explicit Congestion Notification (ECN) bits due to buffer threshold crossings.  
**Key labels:** `port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Pfc rx packets | `network_switch/pfc_rx_packets_count` | A4X Max or A4X | The cumulative count of Priority-based Flow Control (PFC) pause frames received on the port.  
_Note:_ Only applicable to dedicated environments where PFC is enabled.  
**Key labels:** `port_identifier`, `priority_index`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Pfc tx packets | `network_switch/pfc_tx_packets_count` | A4X Max or A4X | The cumulative count of Priority-based Flow Control (PFC) pause frames transmitted out of the port to throttle incoming traffic.  
_Note:_ Only applicable to dedicated environments where PFC is enabled.  
**Key labels:** `port_identifier`, `queue_name`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
QoS tx packets | `network_switch/qos_tx_packets` | A4X Max or A4X | The cumulative count of Quality of Service (QoS) packets transmitted on the specified queue.  
**Key labels:** `port_identifier`, `queue_name`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
In packets count | `network_switch/in_packets_count` | A4X Max or A4X | The cumulative count of incoming packets received on the switch port.  
**Key labels:** `port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
In errors | `network_switch/in_errors` | A4X Max or A4X | The cumulative count of incoming packets received with errors that prevented them from being delivered.  
**Key labels:** `port_identifier`, `peer_target_identifier`, `peer_port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
In Discards | `network_switch/in_discards` | A4X Max or A4X | The cumulative count of valid incoming packets that were discarded (for example, due to lack of buffer space).  
**Key labels:** `port_identifier`, `peer_target_identifier`, `peer_port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Out errors | `network_switch/out_errors` | A4X Max or A4X | The cumulative count of outbound packets that failed to be transmitted because of errors.  
**Key labels:** `port_identifier`, `peer_target_identifier`, `peer_port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Out discards | `network_switch/out_discards` | A4X Max or A4X | The cumulative count of outbound packets that were chosen to be discarded even though no errors were detected.  
**Key labels:** `port_identifier`, `peer_target_identifier`, `peer_port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Inbound bytes count | `network_switch/in_bytes_count` | A4X Max or A4X | The cumulative count of incoming bytes received on the switch port.  
**Key labels:** `port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
Outbound bytes count | `network_switch/out_bytes_count` | A4X Max or A4X | The cumulative count of outgoing bytes transmitted out of the switch port.  
**Key labels:** `port_identifier`, `subblock_id`, `block_id`, `reservation_id`, `switch_type`.   
  
#### GPU fatal errors metrics

To monitor the errors that your GPUs encounter and that might force your compute instances to stop, or negatively impact their performance, use the following metrics:

Name | Metric type | Supported machine series | Description  
---|---|---|---  
NVLink runtime error | `instance/gpu/nvlink_runtime_error` | A4X Max or A4X | Whether an NVLink runtime error occurred.  
Uncorrectable DRAM ECC errors | `instance/gpu/dram_uncorrectable_ecc_error_count` | A4X Max or A4X | The number of uncorrectable error-correcting codes (ECCs) in a GPU dynamic random access memory (DRAM).  
Uncorrectable DRAM row remapping count | `instance/gpu/dram_uncorrectable_row_remapping_count` | A4X Max or A4X | The number of row remappings from uncorrectable errors in GPU DRAMs.   
Uncorrectable DRAM row remapping failed | `instance/gpu/dram_row_remapping_failed` | A4X Max or A4X | Whether a row remapping in GPU DRAMs has failed due to one of the following issues:   


  * A remapping attempt on a memory bank failed because the memory bank already has eight uncorrectable error rows remapped. 
  * A remapping attempt on a row failed because the row was already remapped.
  * A remapping attempt failed because 512 total remappings have occurred.

  
Uncorrectable PCIe errors | `instance/gpu/pcie_fatal_error_count` | A4X Max or A4X | The number of uncorrectable peripheral component interconnect express (PCIe) errors.  
Uncorrectable cache ECC errors | `instance/gpu/cache_uncorrectable_ecc_error_count` | A4X Max or A4X | The number of uncorrectable ECCs in cache memory.  
  
### ML workload metrics

To monitor the productivity—specifically, the [goodput](https://cloud.google.com/blog/products/ai-machine-learning/goodput-metric-as-measure-of-ml-productivity)—of your ML workloads, use the following metrics:

Name | Metric type | Supported machine series | Description  
---|---|---|---  
Productive time | `workload/goodput_time` | A4X, A4, A3 Ultra, or A3 Mega | The time, in seconds, the workload spends on _goodput_ activities. These activities are core, useful tasks, such as a forward or backward pass during model training.   
Non-productive time | `workload/badput_time` | A4X, A4, A3 Ultra, or A3 Mega | The time, in seconds, the workload spends on _badput_ activities. These activities are overhead tasks, such as loading or preprocessing data for training.   
  
### Straggler detection metrics

Straggler detection metrics help you notice and pinpoint suspected stragglers. _Stragglers_ are single-point, non-crashing failures that eventually slow down the entire workload.

To monitor straggler detection for your VMs, use the following metric:

Name | Metric type | Supported machine series | Description  
---|---|---|---  
Suspected Stragglers | `instance/gpu/straggler_status` | A4X, A4, A3 Ultra, or A3 Mega | Whether a VM is suspected as a straggler that is affecting the performance of the workload. We recommend that you act on suspected stragglers only when other metrics indicate that the workload is experiencing issues.   
  
You can also view straggler detection metrics in the log entries for an A4X, A4, A3 Ultra or A3 Mega instance. For example, you can use the following queries: 

Description | Query  
---|---  
**Logs with suspected stragglers for specific VMs**. Use this query to check if there are any suspected stragglers for a specific workload in your project. | 
    
    
        logName=~ "/logs/compute.googleapis.com%2Fworkload_diagnostic" AND jsonPayload.suspectedStragglersDetection.numNodes > 0 AND jsonPayload.suspectedStragglersDetection.nodes.instanceId="INSTANCE_ID"
        

Replace `INSTANCE_ID` with the [ID of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details). For each additional VM that you want to specify, add the following condition to the query:
    
    
        OR jsonPayload.suspectedStragglersDetection.nodes.instanceId="INSTANCE_ID"
          
  
**All logs from straggler detection for your project**. Use this query to verify if the straggler detection service is running when no suspected stragglers are detected. (Due to the limitations, you can't filter the logs without suspected stragglers by specific VMs.) |  `
    
    
        logName=~ "/logs/compute.googleapis.com%2Fworkload_diagnostic"
        

`  
  
Straggler detection metrics are particularly helpful for large-scale ML workloads for the following reasons:

  * **Large-scale ML workloads are very susceptible to stragglers**. Large-scale ML workloads use synchronous and massively distributed computing. (In other words, they have many, highly interdependent components that run simultaneously.) This architecture makes large-scale ML workloads very susceptible to single-point failures like stragglers.

  * **Noticing and pinpointing stragglers in large-scale ML workloads is very difficult**. For reference, consider that there are two types of single-point failures:

    * _stopping failures_ : Failures that cause the entire system to halt; for example [host errors and maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview). They are relatively straightforward to detect and resolve.

    * _slow failures_ : Failures that cause severe performance degradation without crashes. They are very difficult to pinpoint and debug.

Due to their slow-failure nature, stragglers are inherently difficult to notice and pinpoint, especially in large-scale synchronous workloads.




### Unresponsive workload detection metrics

Unresponsive workload detection metrics help you do the following:

  * Notice when an entire workload has stalled (sometimes referred to as a _NCCL hang_)
  * Understand why the workload has stalled, such as whether it was caused by a process crash or a stalled network



To detect and diagnose unresponsive workloads for your compute instances, use the following metrics:

Name | Metric type | Supported machine series | Description  
---|---|---|---  
Unresponsive workload events detected by using NCCL telemetry | `instance/gpu/nccl_hang` | A4X Max, A4X, A4 and A3 Ultra | The number of detected unresponsive workload events, as a time series.  
  
#### Enable unresponsive workload detection

To enable unresponsive workload detection, you must enable [CoMMA](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma) with _heartbeat telemetry_ , a periodic ping signal which indicates that a workload is running. For recent versions of CoMMA, this is enabled by default. However, if you're using the version of CoMMA from version 1.1.1 of the NICCL/gIB bundle, then you must manually enable heartbeat telemetry. To verify which version of the NICCL/gIB bundle you're using, see [Check NCCL and gIB version](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand#check_version).

To manually enable heartbeat telemetry for CoMMA, specify the following environment variables in your training environment:
    
    
    NCCL_PROFILER_HEARTBEAT=true
    
    NCCL_PROFILER_HEARTBEAT_UPLOAD_INTERVAL=10s
    

Use `NCCL_PROFILER_HEARTBEAT` to turn heartbeat telemetry on or off, and `NCCL_PROFILER_HEARTBEAT_UPLOAD_INTERVAL` to specify the frequency of the heartbeat telemetry. For more information, see [CoMMA environment variables](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/configure-comma#env-variables).

#### Turn off unresponsive workload detection

To turn off unresponsive workload detection, turn off heartbeat telemetry in CoMMA by specifying the following environment variable in your training environment:
    
    
    NCCL_PROFILER_HEARTBEAT=false
    

#### Understand why workloads are unresponsive

To understand why a workload is unresponsive, check the value of the label `hang_reason` by completing the following steps:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Search for the following metric:
         
         compute.googleapis.com/instance/gpu/nccl_hang
         

  3. Use the **Aggregation** feature, and select the following labels:

     * `instance_id`
     * `hang_reason`



The following table lists possible values for the label, what those values mean about your workloads, and recommended next steps.

Label value | Description | Recommended next steps  
---|---|---  
`MissingHeartbeatIssue` | Heartbeat telemetry has stopped for one or more ranks, which typically indicates a fatal process or node crash. | 

  * Verify if the instance is still reachable.
  * Verify if workload processes have crashed.
  * Check for out-of-memory (OOM) events, such as `dmesg`, in system logs.
  * Look for hardware failures or NVIDIA XID errors.

  
`StalledRankIssue` | Heartbeat telemetry is still being received, but the ranks aren't progressing on NCCL operations. | 

  * Investigate potential deadlocks in app-level operations.
  * Check if the application process is stuck in an operation that prevents it from communicating with others, such as computation or checkpointer.

  
`MissingCommunicatorIssue` | All of the ranks that belong to a NCCL communicator have stopped making progress. | 

  * Your workload might have been interrupted, or its NCCL communicators might have closed abruptly. If you're expecting a workload to run uninterrupted on this VM instance, then check if the workload has been abnormally interrupted or shut down.

  
`NoHangIssue` | The default value. No issues have been detected. | 

  * No action is required.

  
  
## View metrics

To view metrics for your compute instances and Slurm clusters, use Monitoring dashboards as follows:

  * To view infrastructure metrics and straggler detection metrics, you can do the following:

    * For a quick overview of your infrastructure health and performance, or to customize an existing dashboard, use prebuilt dashboards.

    * For specific monitoring needs, create custom dashboards.

  * To view ML workload metrics, see the documentation for how to [set up monitoring for your workload](https://github.com/AI-Hypercomputer/ml-goodput-measurement).

  * To view logs from straggler detection, view straggler detection logs.




If you encounter issues when you use a dashboard, then see [Troubleshoot slow performance](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance).

### Use prebuilt dashboards

You can use Monitoring dashboards that are prebuilt for AI Hypercomputer to view metrics for your compute instances and Slurm clusters. You can also create a copy of a prebuilt dashboard and modify it to fit your needs.

To use a prebuilt dashboard for AI Hypercomputer, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the **Name** column, click the name of one of the following dashboards based on which metrics you want to view:

     * To monitor compute instance health, GPU performance, and straggler detection, use the **Cluster Director Health Monitoring** dashboard.

For more information about how to use these metrics to identify and analyze issues, also use the **GCE Interactive Playbook - Cluster Director Health Monitoring** playbook dashboard.

     * To monitor network transmission efficiency, use the **Cluster Director Transmission Efficiency** dashboard.

     * To monitor network efficiency among blocks and sub-blocks, use the **Cluster Director Block Network** dashboard.

For more information about how to use these metrics to identify and analyze issues, also use the **GCE Interactive Playbook - Cluster Director Block Network** playbook dashboard.

The details page of your chosen dashboard opens. You can use the time-range selector in the toolbar to change the time range of the data.

  3. Optional: To create a copy of a dashboard and customize it to fit your needs, click edit **Copy dashboard**.




### Create custom dashboards

To create a custom Monitoring dashboard, do the following:

  1. Choose the metrics to monitor. If you haven't already, then see Available metrics in this document.

  2. [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).




### View straggler detection logs

To view straggler detection logs by using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), complete the following steps:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

The page queries all logs in your project by default. Click **Stop query**.

  2. Use the time-range selector in the toolbar to select the time range that you want to analyze.

  3. In the **Query** pane, enter a query for straggler detection logs.

  4. Click **Run Query**.




The following is an example of a straggler detection log entry.
    
    
      {
        ...
        "jsonPayload": {
          ...
          "@type": "type.googleapis.com/ml.aitelemetry.performancedebugging.output.NetworkStragglersOutput",
          "suspectedStragglersDetection": {
            "numNodes": 4,
            "nodes": [
              {
                "latencyMs": 9,
                "instanceId": "INSTANCE_ID_1"
              },
              {
                "latencyMs": 9,
                "instanceId": "INSTANCE_ID_2"
              },
              {
                "instanceId": "INSTANCE_ID_3",
                "latencyMs": 4
              },
              {
                "instanceId": "INSTANCE_ID_4",
                "latencyMs": 0
              }
            ],
            "message": "Suspected stragglers detected."
          }
        },
        "resource": {
          "type": "project",
          "labels": {
            "project_id": "PROJECT_NUMBER"
          }
        },
        ...
        "severity": "INFO",
        "logName": "projects/PROJECT_ID/logs/compute.googleapis.com%2Fworkload_diagnostic",
        ...
      }
      

The log entry includes the following fields:

  * `numNodes`: The number of suspected straggler compute instances that are detected in the project. In the example, four suspected straggler compute instances have been detected.
  * `instanceId`: The ID of a compute instance that was detected as a suspected straggler.



## What's next

  * [Observe and monitor VMs](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms)
  * [Customize dashboards for Google Cloud services](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards#customize-gc-dashboards)
  * [Troubleshoot slow performance](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
