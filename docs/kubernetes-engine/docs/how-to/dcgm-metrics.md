---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics/
title: Collect and view DCGM metrics \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:06.810334+00:00
---

# Collect and view DCGM metrics  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Collect and view DCGM metrics Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can monitor GPU utilization, performance, and health by configuring GKE to send [NVIDIA Data Center GPU Manager (DCGM) metrics](https://developer.nvidia.com/dcgm) to Cloud Monitoring.

When you enable DCGM metrics, GKE installs the [DCGM-Exporter](https://developer.nvidia.com/dcgm) tool, installs Google-managed GPU drivers, and deploys a ClusterPodMonitoring resource to send metrics to Google Cloud Managed Service for Prometheus. For new GKE clusters created running version 1.32.1-gke.1357000 or later, the DCGM metrics metrics package is enabled by default. For clusters running earlier versions, you can enable collection of DCGM metrics using the Google Cloud console, the gcloud CLI or Terraform.

You can also configure [self-managed DCGM](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nvidia-dcgm) if you want to customize the set of DCGM metrics or if you have a cluster that does not meet the requirements for managed DCGM metrics.

## What is DCGM

NVIDIA Data Center GPU Manager (DCGM) is a set of tools from NVIDIA that let you manage and monitor NVIDIA GPUs. DCGM exposes various observability structures and counters using what it refers to as `fields`. Each field has a symbolic identifier and a field number. You can find a complete list of them at [NVIDIA DCGM list of Field IDs](https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html).

If you enable DCGM metrics on GKE, [the supported metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics#dcgm-metrics) are automatically available in Cloud Monitoring. Those metrics provides a comprehensive view of GPU utilization, performance, and health.

  * GPU utilization metrics are an indication of how busy the monitored GPU is and if it is effectively utilized for processing tasks. This includes metrics for core processing, memory, I/O, and power utilization.
  * GPU performance metrics refer to how effectively and efficiently a GPU can perform a computational task. This includes metrics for clock speed and temperature.
  * GPU I/O metrics like NVlink and PCIe measure data transfer bandwidth.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements for NVIDIA Data Center GPU Manager (DCGM) metrics

To collect NVIDIA Data Center GPU Manager (DCGM) metrics, your GKE cluster must meet the following requirements:

  * The clusters must be running GKE version 1.30.1-gke.1204000 or later.
  * [System metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) collection must be enabled
  * [Google Cloud Managed Service for Prometheus managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) must be enabled
  * The node pools must be running GKE managed GPU drivers. This means that you must create your node pools using `default` or `latest` for `--gpu-driver-version`.
  * For GKE version 1.32.0-gke.1764000 or later, [profiling metrics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html#profiling-metrics) are collected for all GKE supported GPU types. For earlier GKE versions, [profiling metrics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html#profiling-metrics) are only collected for NVIDIA H100 80GB GPUs.



### Limitations

  * If you are running a self-deployed NVIDIA Data Center GPU Manager (DCGM) metrics package, you must stop collecting it before enabling managed NVIDIA Data Center GPU Manager (DCGM) metrics, otherwise you might end up with duplicate or incorrect metrics.

  * Managed DCGM metrics, including its underlying manifests and container images, is intended to work only on GKE clusters. Don't use managed DCGM metrics standalone or run it outside of GKE.




### Configure collection of DCGM metrics

You can enable GKE to collect DCGM metrics for an existing cluster using the Google Cloud console, the gcloud CLI, or Terraform.

###  Console 

  1. [Create a GPU node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#create-gpu-pool-auto-drivers).

You must use either **Default** or **Latest** for **GPU Driver Installation**.

  2. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  3. Click the name of your cluster.

  4. Next to **Cloud Monitoring** , click _edit_.

  5. Select `SYSTEM` and `DCGM`.

  6. Click Save.




###  gcloud 

  1. Create a [GPU node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#create-gpu-pool-auto-drivers).

You must use either `default` or `latest` for `--gpu-driver-version`.

  2. Update your cluster:
         
         gcloud container clusters update CLUSTER_NAME \
             --location=COMPUTE_LOCATION \
             --enable-managed-prometheus \
             --monitoring=SYSTEM,DCGM
         

Replace the following:

     * `CLUSTER_NAME`: the name of the existing cluster.
     * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) of the cluster.



###  Terraform 

To configure the collection of DCGM metrics by using Terraform, see the `monitoring_config` block in the [Terraform registry for `google_container_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#monitoring_config). For general information about using Google Cloud with Terraform, see [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

## Use DCGM metrics

You can view DCGM metrics by using the dashboards in the Google Cloud console or directly in the cluster overview and cluster details pages. For information, see [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

You can view metrics using the [Grafana DCGM metrics dashboard](https://grafana.com/grafana/dashboards/12239-nvidia-dcgm-exporter-dashboard/). For more information, see [Query using Grafana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query). If you encounter any errors, see [API compatibility](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#http-api-details).

## Pricing

DCGM metrics use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) to load metrics into Cloud Monitoring. Cloud Monitoring charges for the ingestion of these metrics are based on the number of samples ingested.

For more information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

## Quota

DCGM metrics consume the **Time series ingestion requests per minute** quota of the Cloud Monitoring API. Before enabling the metrics packages, [check your recent peak usage](https://console.cloud.google.com/iam-admin/quotas) of that quota. If you have many clusters in the same project or are already approaching that quota limit, you can [request a quota-limit increase](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota) before enabling either observability package.

## DCGM metrics

The Cloud Monitoring metric names in this table must be prefixed with `prometheus.googleapis.com/`. That prefix has been omitted from the entries in the table. 

Along with labels on the `prometheus_target` monitored resource, all collected DCGM metrics on GKE have the following labels attached to them: 

GPU labels:

  * `UUID`: the GPU device UUID
  * `device`: the GPU device name.
  * `gpu`: the index number as an integer of the GPU device on the node. For example, if there are 8 GPUs attached, this value could range from `0` to `7`. 
  * `modelName`: the name of the GPU device model, such as `NVIDIA L4`.



Kubernetes labels:

  * `container`: the name of the Kubernetes container using the GPU device.
  * `namespace`: the Kubernetes namespace of the Pod and container using the GPU device. 
  * `pod`: the Kubernetes Pod using the GPU device.

PromQL metric name  
Cloud Monitoring metric name  
---  
Kind, Type, Unit   
Monitored resources   
Required GKE version | _Description_  
`DCGM_FI_DEV_FB_FREE`  
`DCGM_FI_DEV_FB_FREE/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  Free Frame Buffer in MB.   
`DCGM_FI_DEV_FB_TOTAL`  
`DCGM_FI_DEV_FB_TOTAL/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  Total Frame Buffer of the GPU in MB.   
`DCGM_FI_DEV_FB_USED`  
`DCGM_FI_DEV_FB_USED/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  Used Frame Buffer in MB.   
`DCGM_FI_DEV_GPU_TEMP`  
`DCGM_FI_DEV_GPU_TEMP/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  Current temperature readings for the device (in °C).   
`DCGM_FI_DEV_GPU_UTIL`  
`DCGM_FI_DEV_GPU_UTIL/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  GPU utilization (in %).   
`DCGM_FI_DEV_MEM_COPY_UTIL`  
`DCGM_FI_DEV_MEM_COPY_UTIL/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  Memory utilization (in %).   
`DCGM_FI_DEV_MEMORY_TEMP`  
`DCGM_FI_DEV_MEMORY_TEMP/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  Memory temperature for the device (in °C).   
`DCGM_FI_DEV_POWER_USAGE`  
`DCGM_FI_DEV_POWER_USAGE/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  Power usage for the device (in Watts).   
`DCGM_FI_DEV_SM_CLOCK`  
`DCGM_FI_DEV_SM_CLOCK/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  SM clock frequency (in MHz).   
`DCGM_FI_DEV_TOTAL_ENERGY_CONSUMPTION`  
`DCGM_FI_DEV_TOTAL_ENERGY_CONSUMPTION/counter`  
  
  
`CUMULATIVE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  Total energy consumption for the GPU in mJ since the driver was last reloaded.   
`DCGM_FI_PROF_DRAM_ACTIVE`  
`DCGM_FI_PROF_DRAM_ACTIVE/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The ratio of cycles the device memory interface is active sending or receiving data.   
`DCGM_FI_PROF_GR_ENGINE_ACTIVE`  
`DCGM_FI_PROF_GR_ENGINE_ACTIVE/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The ratio of time the graphics engine is active.   
`DCGM_FI_PROF_NVLINK_RX_BYTES`  
`DCGM_FI_PROF_NVLINK_RX_BYTES/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The rate of active NvLink rx (read) data in bytes including both header and payload.   
`DCGM_FI_PROF_NVLINK_TX_BYTES`  
`DCGM_FI_PROF_NVLINK_TX_BYTES/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The rate of active NvLink tx (transmit) data in bytes including both header and payload.   
`DCGM_FI_PROF_PCIE_RX_BYTES`  
`DCGM_FI_PROF_PCIE_RX_BYTES/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The rate of active PCIe rx (read) data in bytes including both header and payload.   
`DCGM_FI_PROF_PCIE_TX_BYTES`  
`DCGM_FI_PROF_PCIE_TX_BYTES/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The rate of active PCIe tx (transmit) data in bytes including both header and payload.   
`DCGM_FI_PROF_PIPE_FP16_ACTIVE`  
`DCGM_FI_PROF_PIPE_FP16_ACTIVE/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The ratio of cycles that the fp16 pipe is active.   
`DCGM_FI_PROF_PIPE_FP32_ACTIVE`  
`DCGM_FI_PROF_PIPE_FP32_ACTIVE/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The ratio of cycles that the fp32 pipe is active.   
`DCGM_FI_PROF_PIPE_FP64_ACTIVE`  
`DCGM_FI_PROF_PIPE_FP64_ACTIVE/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The ratio of cycles that the fp64 pipe is active.   
`DCGM_FI_PROF_PIPE_TENSOR_ACTIVE`  
`DCGM_FI_PROF_PIPE_TENSOR_ACTIVE/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The ratio of cycles that any tensor pipe is active.   
`DCGM_FI_PROF_SM_ACTIVE`  
`DCGM_FI_PROF_SM_ACTIVE/gauge`  
  
  
`GAUGE`, `DOUBLE`, `1` **[prometheus_target](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target)**   
1.30.1-gke.1204000  |  The ratio of cycles an SM has at least 1 warp assigned.   
  
To help you understand how these metrics can be used, we've grouped them as follows:

### Compute or Core Utilization

These metrics allow you to identify under-utilized devices and adjust either your computation or GPU allocation to optimize utilization. Low utilization means you might be paying for more GPU capacity than needed. These metrics can help save costs by consolidating computation on fewer devices.

`DCGM_FI_DEV_GPU_UTIL`

This metric represents the fraction of time the GPU was active.

**Expected usage:** Provides an overview of average GPU utilization. This metric is similar to **DCGM_FI_PROF_GR_ENGINE_ACTIVE** , which could be a more accurate metric for GPU utilization.

`DCGM_FI_PROF_GR_ENGINE_ACTIVE`

This metric represents how busy the Graphics Engine was for each sampling interval. The value is derived from the average number of active cycles versus the maximum possible available cycles over the sampling interval. For example, if over a one second sampling interval, 1000 cycles were available and an average of 324 cycles were actually active (doing work), the resulting metric value would be 0.324. This roughly can be interpreted as (0.324 x 100) 32.4% utilization.

**Expected usage:** Provides an overview of average GPU utilization. Consistently high utilization values represent that the GPU might be a bottleneck causing system performance issues. Consistently low utilization values indicate that the application is not fully using the available processing power.

`DCGM_FI_PROF_PIPE_FP16_ACTIVE`, `DCGM_FI_PROF_PIPE_FP32_ACTIVE`, `DCGM_FI_PROF_PIPE_FP64_ACTIVE`, `DCGM_FI_PROF_PIPE_TENSOR_ACTIVE`

These metrics represent the ratio of cycles that any given GPU pipe is active over the peak sustained elapsed cycles.

**Expected usage:** Measure how effectively the various computational pipelines in the GPU are used.

`DCGM_FI_PROF_SM_ACTIVE`

This metric represents the fraction of time at least one warp was active on an SM(Streaming Multiprocessor), averaged over all SMs. For example, if the GPU has 80 SMs available, and over the sampling period 16 SMs were executing a warp, the resulting `sm_active` value would be (16/80) 0.20, which can be interpreted as 20% of available SMs had a warp executing.

**Expected usage:** Provides a measure of how GPU parallelism is utilized.

### Memory Utilization

The main usage of these metrics is to detect when GPU devices don't have sufficient memory for the applications. Those applications might benefit from allocating more GPU capacity.

`DCGM_FI_DEV_FB_FREE`, `DCGM_FI_DEV_FB_USED`, `DCGM_FI_DEV_FB_TOTAL`

These metrics are for frame buffer memory, which is the memory on the GPU. The metrics report memory free, memory used, which add up to the total. And also, total memory available.

**Expected usage:** Determine the patterns of GPU memory use. This lets you correlate actual on-GPU memory usage with the expected usage to determine the memory efficiency of their application.

`DCGM_FI_DEV_MEM_COPY_UTIL`

This metric represents the fraction of time over the past sample period during which global (device) memory was being read or written.

**Expected usage:** Determine the patterns of data transfer to and from GPU memory. High values of this metric, combined with low values of compute utilization metrics, might indicate that memory transfer is the bottleneck in the running applications.

`DCGM_FI_PROF_DRAM_ACTIVE`

This metric represents the ratio of cycles the GPU memory interface is either sending or receiving data. This includes loads and stores from threads executing on SMs, as well as memory copies to and from GPU memory. Higher values indicate higher levels of memory traffic.

**Expected usage:** This metric is similar to the metric `DCGM_FI_DEV_MEM_COPY_UTIL` and this metric could be more precise.

### I/O Utilization

The following metrics provide insight into data transmission usage between the GPU and the host, or between multiple GPU devices. One way to use those metrics is to detect when an application overloads the interconnect. Due to the inherent burstiness of such transmission, it might be worth exploring higher-resolution data (e.g., a distribution) to give a finer-grained picture of how the interconnect behaved.

`DCGM_FI_PROF_NVLINK_RX_BYTES`, `DCGM_FI_PROF_NVLINK_TX_BYTES`

These metrics represent NVLink transmit (tx) and receive (rx) throughput in bytes.

**Expected usage:** Track the load on the NVLink connectors (between GPU chips). If the value of these metrics are close to the total available NVLink bandwidth and the compute utilization metrics are low, this might indicate that the NVLink is a bottleneck in the running applications.

`DCGM_FI_PROF_PCIE_RX_BYTES`, `DCGM_FI_PROF_PCIE_TX_BYTES`

These metrics represent PCIe transmit (tx) and receive (rx) throughput in bytes, where tx is the GPU transmitting data, and rx is the GPU receiving data.

**Expected usage:** Track the load on the PCIe bus (between CPU and GPU). If the values of these metrics are close to the total bandwidth of the PCIe bus and the compute utilization metrics are low, this might indicate that the PCIe bus is a bottleneck in the running applications.

### Power Utilization

The following metrics provide insight into GPU power utilization, sometimes crucial for workload performance and efficiency.

`DCGM_FI_DEV_GPU_TEMP`

This metric represents average temperature across all GPU cores.

**Expected usage:** Track when the GPU is close to overheating, mostly to correlate with clock throttling. You can also use this metric to identify GPUs prone to overheating for lighter load in more advanced applications.

`DCGM_FI_DEV_POWER_USAGE`

This metric represents GPU power consumption in watts. You might want to track power usage as a GPU busy metric. NVIDIA GPUs adjust engine clocks based on how much work they are doing. As the clock speed (and thus utilization) increases, the power consumption increases as well.

**Expected usage:** Track how much power the GPU is using for user applications.

`DCGM_FI_DEV_TOTAL_ENERGY_CONSUMPTION`

This metric represents total GPU energy consumption in millijoule (mJ) after the driver was last reloaded. The rate computed over this metric should correspond to the power draw metric.

**Expected usage:** Track how much power the GPU is using for user applications.

### GPU Performance Metrics

GPU performance refers to how effectively and efficiently a GPU can perform a computational task.

`DCGM_FI_DEV_MEMORY_TEMP`

This metric indicates the average temperature of the memory block.

**Expected usage:** To show the temperature of the memory block and correlate with GPU temperature.

`DCGM_FI_DEV_SM_CLOCK`

This metric represents the average clock speed across all SMs. This metric is calculated over a specified time interval.

**Expected usage:** Track the clock speed to detect throttling and correlate with application performance.

## What's next

  * Learn how to [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
