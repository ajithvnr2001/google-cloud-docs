---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/monitoring/
title: Monitor deployments \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:56.412121+00:00
---

# Monitor deployments  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/monitoring/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  Monitor deployments Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to monitor the health, uptime, and upgrades of your Google Distributed Cloud connected deployments, including supported workloads. For more information about configuring monitoring and about the available metrics, see [Logs and metrics](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/logs-metrics).

## Monitor workload health and uptime

You are responsible for monitoring the health and uptime of your workloads (containers and virtual machines) running on your Distributed Cloud connected deployment.

### Container workloads

To monitor the health and uptime of the containerized workloads that you deploy, we recommend using the Prometheus metrics solution. You can configure Prometheus to scrape metrics from your Pods and Services. Google-managed system services are monitored and managed automatically by Google. For more information about configuring Prometheus, see [Collect metrics with Prometheus](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/logs-metrics#collect-metrics-with-prometheus).

Use the following key metrics to monitor for container workloads. If you use Prometheus, you're responsible for deploying and managing Kube State Metrics to expose these specific metrics for your workloads:

  * `kube_pod_status_phase`: Monitor for Pods in `Failed` or `Unknown` phases.
  * `kube_pod_container_status_waiting_reason`: Identify Pods stuck in `CrashLoopBackOff` or `ImagePullBackOff`.
  * `container_cpu_usage_seconds_total` and `container_memory_working_set_bytes` (from cAdvisor): Monitor resource consumption to prevent out-of-memory (OOM) issues.



### Virtual machine workloads

In Distributed Cloud connected, virtual machines (VMs) run inside standard Kubernetes Pods, typically prefixed with `virt-launcher-`. Monitor VM health and status primarily by checking the `VirtualMachine` custom resource status or by monitoring application metrics from within the VM.

Use the underlying `virt-launcher` Pod metrics as secondary indicators for the following details:

  * **Resource usage** : Monitor CPU and memory consumption of launcher Pods to ensure that VMs have sufficient resources.
  * **Pod phase** : Track launcher Pod phases to identify VMs that fail to start or crash.



To adjust the resources assigned to a VM, modify the VM custom resource specification. Don't modify the underlying `virt-launcher` Pod YAMLs directly, because these are managed by the platform. Any direct changes will be overwritten or lead to reconciliation errors.

To troubleshoot VMs stuck in a pending state, see [Troubleshoot virtual machines stuck in Pending state](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/troubleshooting#vm-stuck-pending).

## Monitor Distributed Cloud connected upgrades

Monitor the progress and status of Distributed Cloud connected software upgrades using Cloud Monitoring metrics and `gcloud` commands. Upgrades are scheduled and run by Google. Monitoring is strictly for visibility and planning workload migration.

For detailed instructions about how to check if an upgrade is in progress, monitor its status, and troubleshoot failed upgrades, see [Troubleshoot software upgrades](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/troubleshooting#software-upgrades).

## Monitor local storage health

Distributed Cloud connected continuously monitors the health of its storage devices and alerts Google when a physical drive needs replacement. Google works with you to schedule a visit and replace the failing drive. You can monitor the health of your storage using Kubernetes condition alerts, such as `DiskPressure`.

### Monitor system storage health

You can monitor the health of Distributed Cloud connected system storage using one of the following methods:

  * **Prometheus with Kube State Metrics (PromQL).** Deploy and manage Kube State Metrics in your cluster to expose Kubernetes condition metrics.

  * **Cloud Monitoring metrics**. Create alerting policies based on host-level metrics exported to Cloud Monitoring.




#### Monitor system storage health with Prometheus

To monitor system storage health with Prometheus with Kube State Metrics (PromQL), set up the following alerts:

  1. Alert immediately when a node condition enters the `DiskPressure` state:
         
         kube_node_status_condition{condition="DiskPressure",status="true"} == 1
         

  2. Alert proactively before eviction thresholds are breached by checking when disk utilization exceeds an operational threshold:
         
         (1 - (node_filesystem_avail_bytes{mountpoint="/mnt/shared_lpvs"} / node_filesystem_size_bytes{mountpoint="/mnt/shared_lpvs"})) > THRESHOLD
         

Replace `THRESHOLD` with the target operational threshold in the `0.00` ~ `1.00` range. Google recommends setting this value to `0.85`.




#### Monitor system storage health with Cloud Monitoring

To monitor system storage health with Cloud Monitoring metrics, create an alerting policy with the following parameters:

  * **Metric:** `edgecontainer.googleapis.com/machine/disk/utilization`
  * **Scope:** This metric specifically reports the disk utilization of the node's local system partition file system (`/dev/mapper/shared_lpvs_encrypted`).
  * **Threshold:** Configure an alerting threshold when disk utilization is greater than 85%. This will detect system disk saturation before a hard node `DiskPressure` event occurs.



### Monitor workload storage health

You can monitor the health of workload storage using either Kubelet volume metrics or directly using application-level telemetry, depending on the volume mode used by the workload.

  * **`Filesystem` volume mode**. You can monitor file system volumes using Prometheus by scraping the following Kubelet volume metrics:

    * `kubelet_volume_stats_capacity_bytes`
    * `kubelet_volume_stats_available_bytes`
    * `kubelet_volume_stats_used_bytes`
    * `kubelet_volume_stats_inodes_used`
    * `kubelet_volume_stats_inodes_free`
  * **`Block` volume mode**. Raw block volumes are invisible to Kubelet. To monitor their health, you must use application-level or Symcloud Storage metrics.




## Multi-cluster monitoring

If you manage many Distributed Cloud connected clusters, we recommend using Cloud Monitoring to aggregate and filter metrics.

  * **Use resource labels** : Metrics exported to Cloud Monitoring include labels that identify the source. The labels available depend on the resource type:

    * For cluster and container metrics, such as `k8s_container`, key labels include the following values:

      * `project_id`: The Google Cloud project hosting the cluster.
      * `location`: The Google Cloud region where the cluster is registered.
      * `cluster_name`: The name of the cluster.
    * For hardware metrics, such as `edgecontainer.googleapis.com/machine`, key labels include the following values:

      * `resource_container`: The Google Cloud project associated with the hardware.
      * `location`: The Google Cloud region where the Distributed Cloud connected zone is registered.
      * `machine_id`: The identifier of the machine.

Hardware metrics don't include a `cluster_name` label directly.

  * **Create custom dashboards** : Build dashboards that display key health indicators across your entire fleet. Key health indicators include connectivity, VM status, and resource usage. To show data from multiple clusters in a single chart, use wildcards or group-by operations.

  * **Set up multi-cluster alerts** : Configure alerting policies that apply to multiple clusters. For example, you can create an alert that triggers if any machine in any cluster loses connectivity.




## Alerting strategy

Monitoring and maintaining Distributed Cloud connected is a shared responsibility. This section explains what Google alerts on and how you can configure your own alerting policies.

### What Google alerts on

Google continuously monitors the underlying infrastructure. It takes action and notifies you if necessary for the following situations:

  * **Hardware failures** : Power supply failures, fan failures, overheating, or disk failures, such as a disk reaching its spare threshold or end of viable life. Google continuously monitors the health of its internal storage devices and triggers an automatic replacement when a storage device fails.
  * **Connectivity issues** : Complete loss of connection between the Distributed Cloud connected zone and Google Cloud.
  * **Control plane health** : Failures in the Kubernetes control plane or Google-managed system services.
  * **Upgrade failures** : Automated upgrade processes that get stuck or fail.



### Configure alerts

Configure your own alerting policies in Cloud Monitoring or in Prometheus for issues affecting your workloads or local environment.

  * To configure alerts in Cloud Monitoring, use the Google Cloud console or the Cloud Monitoring API. For detailed instructions, see [Create alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). You can create alerting policies based on the metrics documented in [Logs and metrics](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/logs-metrics#metrics).

  * If you [use Prometheus to collect metrics](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/logs-metrics#collect-metrics-with-prometheus), define standard [Prometheus alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) in your Prometheus configuration.




You can set up alerts for the following issues:

Issue | Description | Monitoring system | Details  
---|---|---|---  
**Workload downtime** | Pods or VMs failing to start or crash-looping | Prometheus | For container workloads, create alerts on `kube_pod_status_phase` to detect Pods in `Failed` or `Unknown` phases. You can also alert on `kube_pod_container_status_waiting_reason` when it equals `CrashLoopBackOff` or `ImagePullBackOff`.  
Cloud Monitoring | For VM workloads running in Pods, set up alerts using standard Kubernetes container metrics in Cloud Monitoring to track the status of `virt-launcher` Pods.  
**Workload resource exhaustion** | Disk usage approaching capacity, or high memory or CPU usage on workloads | Prometheus | For container workloads, set threshold alerts on `container_cpu_usage_seconds_total` and `container_memory_working_set_bytes` (from cAdvisor) to identify Pods approaching their resource limits.  
Cloud Monitoring | For machine storage, monitor the machine disk utilization metric `edgecontainer.googleapis.com/machine/disk/utilization` to detect when node storage is approaching capacity.  
**Local network issues** | Network interface drops on machines | Cloud Monitoring | Monitor whether the machine network up metric `edgecontainer.googleapis.com/machine/network/up` is `false`.   
Loss of internet connectivity | Cloud Monitoring | Monitor whether the network connectivity metric `edgecontainer.googleapis.com/machine/network/connectivity` is `false`.   
**Machine restarts** | Unexpected machine reboots or shutdowns | Cloud Monitoring | Configure alerts with `edgecontainer.googleapis.com/machine/uptime` and `edgecontainer.googleapis.com/machine/restart_count` metrics. For more information, see [Troubleshoot machine restarts](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/troubleshooting#machine-restarts).  
**System storage exhaustion** | System storage runs out of space | Cloud Monitoring | Configure alerts with the `edgecontainer.googleapis.com/machine/disk/utilization` metric. For more information, see [Monitor system storage health](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/monitoring#monitor-system-storage).  
  
Distributed Cloud connected hardware is managed by Google. You don't have SSH access to the machines or control over the host operating system. If alerts based on machine-level metrics fire, such as network connectivity or restarts, your action items are limited to checking physical power, cabling, and local network and firewall configurations, or escalating the issue to Google Support.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
