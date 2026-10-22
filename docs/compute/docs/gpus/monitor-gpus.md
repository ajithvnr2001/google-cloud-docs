---
url: https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus/
title: Monitoring GPU performance on Linux VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:23.966630+00:00
---

# Monitoring GPU performance on Linux VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitoring GPU performance on Linux VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Tip:** If you want to monitor A4 or A3 Ultra machine types that are deployed using the features provided by AI Hypercomputer, see [Monitor Compute Engine instances and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor) in the AI Hypercomputer documentation instead.

You can track metrics such as GPU utilization and GPU memory from your virtual machine (VM) instances by using the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent), which is Google's recommended telemetry collection solution for Compute Engine. By using the Ops Agent, you can manage your GPU VMs as follows:

  * Visualize the health of your NVIDIA GPU fleet with our pre-configured dashboards.
  * Optimize costs by identifying underutilized GPUs and consolidating workloads.
  * Plan scaling by looking at trends to decide when to expand GPU capacity or upgrade existing GPUs.
  * Use NVIDIA Data Center GPU Manager (DCGM) profiling metrics to identify bottlenecks and performance issues within your GPUs.
  * Set up [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) to autoscale resources.
  * Get alerts on metrics from your NVIDIA GPUs.



This document covers the procedures for monitoring GPUs on Linux VMs by using the Ops Agent. Alternatively, a reporting script is available on GitHub that can also be set up for monitoring GPU usage on Linux VMs, see [`compute-gpu-monitoring` monitoring script](https://github.com/GoogleCloudPlatform/compute-gpu-monitoring/tree/main/linux). This script is not actively maintained.

For monitoring GPUs on Windows VMs, see [Monitoring GPU performance (Windows)](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus-windows).

## Overview

The Ops Agent, version 2.38.0 or later, can automatically track GPU utilization and GPU memory usage rates on your Linux VMs that have the agent installed. These metrics, obtained from the NVIDIA Management Library (NVML), are tracked per GPU and per process for any process that uses GPUs. To view the metrics that are monitored by the Ops Agent, see [Agent metrics: gpu](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-gpu).

You can also set up the NVIDIA Data Center GPU Manager (DCGM) integration with the Ops Agent. This integration allows the Ops Agent to track metrics using the hardware counters on the GPU. DCGM provides access to the GPU device-level metrics. These include Streaming Multiprocessor (SM) block utilization, SM occupancy, SM pipe utilization, PCIe traffic rate, and NVLink traffic rate. To view the metrics monitored by the Ops Agent, see [Third-party application metrics: NVIDIA Data Center GPU Manager (DCGM)](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#opsagent-dcgm).

To review GPU metrics by using the Ops Agent, complete the following steps:

  1. On each VM, check that you have met the requirements.
  2. On each VM, install the Ops Agent.
  3. Optional: On each VM, set up the NVIDIA Data Center GPU Manager (DCGM) integration.
  4. Review metrics in Cloud Monitoring.



## Limitations

  * The Ops Agent doesn't track GPU utilization on VMs that use Container-Optimized OS.



## Requirements

On each of your VMs, check that you meet the following requirements:

  * Each VM must have [GPUs attached](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).
  * Each VM must have a [GPU driver installed](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#verify-driver-install).
  * The Linux operating system and version for each of your VM must support the Ops Agent. See the list of [Linux operating systems](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#linux_operating_systems) that support the Ops Agent.
  * Ensure you have `sudo` access to each VM.



## Install the Ops Agent

To install the Ops Agent, complete the following steps:

  1. If you were previously using the [`compute-gpu-monitoring` monitoring script](https://github.com/GoogleCloudPlatform/compute-gpu-monitoring/tree/main/linux) to track GPU utilization, disable the service before installing the Ops Agent. To disable the monitoring script, run the following command:
         
         sudo systemctl --no-reload --now disable google_gpu_monitoring_agent

  2. Install the latest version of the Ops Agent. For detailed instructions, see [Installing the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index).

  3. After you have installed the Ops agent, if you need to install or upgrade your GPU drivers by using the [installation scripts provided by Compute Engine](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#installation_scripts), review the _limitations_ section.




## Review NVML metrics in Compute Engine

You can review the NVML metrics that the Ops Agent collects from the **Observability** tabs for Compute Engine Linux VM instances.

To view the metrics for a single VM do the following:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select a VM to open the **Details** page.

  3. Click the **Observability** tab to display information about the VM.

  4. Select the **GPU** quick filter.




To view the metrics for multiple VMs, do the following:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Observability** tab.

  3. Select the **GPU** quick filter.




## Optional: Set up NVIDIA Data Center GPU Manager (DCGM) integration

The Ops Agent also provides integration for NVIDIA Data Center GPU Manager (DCGM) to collect key advanced GPU metrics such as Streaming Multiprocessor (SM) block utilization, SM occupancy, SM pipe utilization, PCIe traffic rate, and NVLink traffic rate.

These advanced GPU metrics are not collected from NVIDIA P4 models.

For detailed instructions on how to set up and use this integration on each VM, see [NVIDIA Data Center GPU Manager (DCGM)](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party-nvidia).

## Review DCGM metrics in Cloud Monitoring

  1. In the Google Cloud console, go to the **Monitoring > Dashboards** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring/dashboards)

  2. Select the **Sample Library** tab.

  3. In the filter_list **Filter** field, type **NVIDIA**. The **NVIDIA GPU Monitoring Overview (GCE and GKE)** dashboard displays.

If you have set up the NVIDIA Data Center GPU Manager (DCGM) integration, the **NVIDIA GPU Monitoring Advanced DCGM Metrics (GCE Only)** dashboard also displays.

![Cloud Monitoring dashboards](https://docs.cloud.google.com/static/compute/images/gpus/dashboards.png)

  4. For the required dashboard, click **Preview**. The **Sample dashboard preview** page displays.

  5. From the **Sample dashboard preview** page, click **Import sample dashboard**.

     * The **NVIDIA GPU Monitoring Overview (GCE and GKE)** dashboard displays the GPU metrics such as GPU utilization, NIC traffic rate, and GPU memory usage.

Your GPU utilization display is similar to the following output:

![Cloud Monitoring \(NVML\)](https://docs.cloud.google.com/static/compute/images/gpus/gpu_monitoring_nvml.png)

     * The **NVIDIA GPU Monitoring Advanced DCGM Metrics (GCE Only)** dashboard displays key advanced metrics such as SM utilization, SM occupancy, SM pipe utilization, PCIe traffic rate, and NVLink traffic rate.

Your Advanced DCGM Metric display is similar to the following output:

![Cloud Monitoring \(DCGM\)](https://docs.cloud.google.com/static/compute/images/gpus/gpu_monitoring_dcgm.png)




## What's next?

  * To handle GPU host maintenance, see [Handling GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).
  * To improve network performance, see [Use higher network bandwidth](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
