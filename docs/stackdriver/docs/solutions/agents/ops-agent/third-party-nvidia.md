---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party-nvidia/
title: NVIDIA Data Center GPU Manager (DCGM) \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:18.516262+00:00
---

# NVIDIA Data Center GPU Manager (DCGM)  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party-nvidia/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  NVIDIA Data Center GPU Manager (DCGM) Stay organized with collections  Save and categorize content based on your preferences. 

The NVIDIA Data Center GPU Manager integration collects key advanced GPU metrics from DCGM. The Ops Agent can be configured to collect one of two different sets of metrics by selecting the version of the `dcgm` receiver:

  * Version 2 of the `dcgm` receiver provides a curated set of metrics for monitoring the performance and state of the GPUs attached to a given VM instance.
  * Version 1 of the `dcgm` receiver provides a set of profiling metrics meant to be used in combination with the default GPU metrics. For information about the purpose and interpretation of these metrics, see [Profiling Metrics](https://docs.nvidia.com/datacenter/dcgm/3.1/user-guide/feature-overview.html#profiling-metrics) in the DCGM feature overview.



For more information about the NVIDIA Data Center GPU Manager, see the [DCGM documentation](https://developer.nvidia.com/dcgm). This integration is compatible with DCGM version 3.1 through 3.3.9.

**These metrics are available for Linux systems only.** Profiling metrics are not collected from NVIDIA GPU models P100 and P4.

## Prerequisites

To collect NVIDIA DCGM metrics, you must do the following:

  * [Install the NVIDIA Datacenter driver](https://docs.nvidia.com/datacenter/tesla/drivers/index.html#cuda-drivers).

  * Install DCGM.

  * [Install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index).

    * Version 1 metrics: Ops Agent version 2.38.0 or higher. Only Ops Agent version 2.38.0 or versions 2.41.0 or higher are compatible with GPU monitoring. **Do not install Ops Agent versions 2.39.0 and 2.40.0 on VMs with attached GPUs.** For more information, see [Agent crashes and report mentions NVIDIA](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-install-startup#nvidia-crashes). 
    * Version 2 metrics: Ops Agent version 2.51.0 or higher.



### Install DCGM and verify installation

You must install DCGM version 3.1 through 3.3.9 and ensure that it runs as a privileged service. To install DCGM, see [Installation](https://docs.nvidia.com/datacenter/dcgm/3.1/user-guide/getting-started.html#id1) in the DCGM documentation.

To verify that DCGM is running correctly, do the following:

  1. Check the status of the DCGM service by running the following command:
         
         sudo service nvidia-dcgm status
         

If the service is running, the `nvidia-dcgm` service is listed as `active (running)`. The output resembles the following:
         
         ● nvidia-dcgm.service - NVIDIA DCGM service
         Loaded: loaded (/usr/lib/systemd/system/nvidia-dcgm.service; disabled; vendor preset: enabled)
         Active: active (running) since Sat 2023-01-07 15:24:29 UTC; 3s ago
         Main PID: 24388 (nv-hostengine)
         Tasks: 7 (limit: 14745)
         CGroup: /system.slice/nvidia-dcgm.service
                └─24388 /usr/bin/nv-hostengine -n --service-account nvidia-dcgm
         

  2. Verify that the GPU devices are found by running the following command:
         
         dcgmi discovery --list
         

If devices are found, the output resembles the following:
         
         1 GPU found.
         +--------+----------------------------------------------------------------------+
         | GPU ID | Device Information                                                   |
         +--------+----------------------------------------------------------------------+
         | 0      | Name: NVIDIA A100-SXM4-40GB                                          |
         |        | PCI Bus ID: 00000000:00:04.0                                         |
         |        | Device UUID: GPU-a2d9f5c7-87d3-7d57-3277-e091ad1ba957                |
         +--------+----------------------------------------------------------------------+
         




## Configure the Ops Agent for DCGM

Following the guide for [Configuring the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#file-location), add the required elements to collect telemetry from your DCGM service, and [restart the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest the receiver version 2 metrics for NVIDIA DCGM:
    
    
    # Configures Ops Agent to collect telemetry from the app. You must restart the agent for the configuration to take effect.
    set -e
    
    # Check if the file exists
    if [ ! -f /etc/google-cloud-ops-agent/config.yaml ]; then
      # Create the file if it doesn't exist.
      sudo mkdir -p /etc/google-cloud-ops-agent
      sudo touch /etc/google-cloud-ops-agent/config.yaml
    fi
    
    # Create a back up of the existing file so existing configurations are not lost.
    sudo cp /etc/google-cloud-ops-agent/config.yaml /etc/google-cloud-ops-agent/config.yaml.bak
    
    # Configure the Ops Agent.
    sudo tee /etc/google-cloud-ops-agent/config.yaml > /dev/null << EOF
    metrics:
      receivers:
        dcgm:
          type: dcgm
          receiver_version: 2
      service:
        pipelines:
          dcgm:
            receivers:
              - dcgm
    EOF
    
    

If you want to collect only DCGM profiling metrics, then replace the value of the `receiver_version` field with `1`. You can also remove the `receiver_version` entry entirely; the default version is `1`. You can't use both versions at the same time.

For these changes to take effect, you must restart the Ops Agent:

  1. To restart the agent, run the following command on your instance: 
         
         sudo systemctl restart google-cloud-ops-agent
         

  2. To confirm that the agent restarted, run the following command and verify that the components "Metrics Agent" and "Logging Agent" started: 
         
         sudo systemctl status "google-cloud-ops-agent*"
         




If you get an error message like "Unable to connect to DCGM daemon at localhost:5555 on libdcgm.so not Found; Is the DCGM daemon running?", then you have probably installed version 4.0 of the DGCM service. The DCGM shared library was renamed to `libdgcdm.so.4`, which the Ops Agent DCGM receiver doesn't recognize. You must use DCGM version 3.1 through 3.3.9.

**Note:** If you restarted the Ops Agent by using the command `sudo service google-cloud-ops-agent restart` and the sub-agents did not restart correctly, then use the `systemctl restart` command shown in the configuration commands. For some Deep Learning VM Images, the Ops Agent doesn't restart all the dependencies when you restart with `service restart`.

If you are using custom service account instead of the default Compute Engine service account, or if you have a very old Compute Engine VM, then you might need to [authorize the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/authorization).

### Configure metrics collection

To ingest metrics from NVIDIA DCGM, you must create a receiver for the metrics that NVIDIA DCGM produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `dcgm` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration), such as `30s` or `5m`.  
`endpoint` | `localhost:5555` | Address of the DCGM service, formatted as `host:port`.  
`receiver_version` | `1` | Either 1 or 2. Version 2 has many more metrics available.  
`type` |  | This value must be `dcgm`.  
  
#### What is monitored

The following tables provides lists of metrics that the Ops Agent collects from the NVIDIA DGCM instance. Not all metrics are available for all GPU models. Profiling metrics are not collected from NVIDIA GPU models P100 and P4.

##### Version 1 metrics

The following metrics are collected by using version 1 of the `dcgm` receiver.

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

##### Version 2 metrics

The following metrics are collected by using version 2 of the `dcgm` receiver.

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

##### GPU metrics

In addition, the built-in configuration for the Ops Agent also collects [`agent.googleapis.com/gpu` metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-gpu), which are reported by the NVIDIA [ Management Library (NVML)](https://developer.nvidia.com/nvidia-management-library-nvml). You do not need any additional configuration in the Ops Agent to collect these metrics, but you must [ create your VM with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus) and [ install the GPU driver](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu). For more information, see [About the `gpu` metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#receiver-nvml-metrics). The `dcgm` receiver version 1 metrics are designed to complement these default metrics, while `dcgm` receiver version 2 metrics are intended to be standalone.

## Verify the configuration

This section describes how to verify that you correctly configured the NVIDIA DCGM receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that NVIDIA DCGM metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
     * For v1 metrics, enter the following query in the editor, and then click **Run query** :   

           
           {"workload.googleapis.com/dcgm.gpu.profiling.sm_utilization", monitored_resource="gce_instance"}
           

     * For v2 metrics, enter the following query in the editor, and then click **Run** :   

           
           {"workload.googleapis.com/gpu.dcgm.sm.utilization", monitored_resource="gce_instance"}
           




## View dashboard

To view your NVIDIA DCGM metrics, you must have a chart or dashboard configured. The NVIDIA DCGM integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

You can also view static previews of dashboards without installing the integration.

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab, and then choose the **Integrations** category.
  3. Click the name of the dashboard you want to view. 



If you have configured an integration but the dashboard has not been installed, then check that the Ops Agent is running. When there is no metric data for a chart in the dashboard, installation of the dashboard fails. After the Ops Agent begins collecting metrics, the dashboard is installed for you.

To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Compute Engine** deployment-platform filter.
  3. Locate the entry for NVIDIA DCGM and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## DCGM limitations, and pausing profiling

Concurrent usage of DCGM can conflict with usage of some other NVIDIA developer tools, such as Nsight Systems or Nsight Compute. This limitation applies to NVIDIA A100 and earlier GPUs. For more information, see [Profiling Sampling Rate](https://docs.nvidia.com/datacenter/dcgm/3.1/user-guide/feature-overview.html#profiling-sampling-rate) in the DCGM feature overiew.

When you need to use tools like Nsight Systems without significant disruption, you can temporarily pause or resume the metrics collection by using the following commands:
    
    
    dcgmi profile --pause
    dcgmi profile --resume
    

When profiling is paused, none of the DCGM metrics that the Ops Agent collects are emitted from the VM.

## What's next

For a walkthrough on how to use Ansible to install the Ops Agent, configure a third-party application, and install a sample dashboard, see the [ Install the Ops Agent to troubleshoot third-party applications](https://www.youtube.com/watch?v=GQgNygd-XJU&t=7s) video.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
