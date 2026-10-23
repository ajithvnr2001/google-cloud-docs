---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics/
title: Collect and view cAdvisor/Kubelet metrics \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:37.452540+00:00
---

# Collect and view cAdvisor/Kubelet metrics  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Collect and view cAdvisor/Kubelet metrics Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how to configure a Google Kubernetes Engine (GKE) cluster to send a curated set of cAdvisor/Kubelet metrics to Cloud Monitoring using Google Cloud Managed Service for Prometheus. This page also describes how these metrics are formatted when they are written to Monitoring, and how to query metrics.

The curated set of metrics is a subset of the set of cAdvisor/Kubelet metrics built into every Kubernetes deployment by default and includes metrics related to reducing ingestion volume and associated costs.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements

To collect cAdvisor/Kubelet metrics, your GKE cluster must meet the following requirements:

  * The cluster must be running GKE version 1.29.3-gke.1093000 or later. cAdvisor/Kubelet packages are enabled by default when you create a cluster running version 1.29.3-gke.1093000 or later.
  * The cluster must have [system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) enabled.
  * The cluster has [Google Cloud Managed Service for Prometheus managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) enabled. Google Cloud Managed Service for Prometheus managed collection is enabled by default for new clusters.

**Warning:** If you are already ingesting cAdvisor/Kubelet metrics into Google Cloud Managed Service for Prometheus, then you must stop ingesting those metrics before enabling managed cAdvisor/Kubelet metrics, otherwise you might end up with duplicate or incorrect metrics.

## Configuring collection of cAdvisor/Kubelet metrics

You can enable cAdvisor/Kubelet metrics in an existing GKE cluster using the Google Cloud console, the gcloud CLI, or Terraform.

### Console

To configure cAdvisor/Kubelet metrics from the **Details** tab for the cluster, do the following:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page: 

[Go to **Kubernetes clusters**](https://console.cloud.google.com/kubernetes/list)

If you use the search bar to find this page, then select the result whose subheading is **Kubernetes Engine**.

  2. Click your cluster's name.

  3. In the **Features** row labelled **Cloud Monitoring** , click the **Edit** icon.

  4. In the **Edit Cloud Monitoring** dialog that appears, confirm that **Enable Cloud Monitoring** is selected.

  5. In the **Components** drop-down menu, select the cAdvisor/Kubelet components from which you would like to collect metrics:

     * **cAdvisor**
     * **Kubelet**
  6. Click **OK**.

  7. Click **Save Changes**.




### gcloud

Update your cluster to collect metrics:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --enable-managed-prometheus \
        --monitoring=SYSTEM,CADVISOR,KUBELET
    

Replace the following:

  * `CLUSTER_NAME`: the name of the existing cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) of the cluster.



The set of values supplied to the `monitoring` flag overrides any previous setting.

### Terraform

To configure the collection of cAdvisor/Kubelet metrics by using Terraform, see the `monitoring_config` block in the [ Terraform registry for `google_container_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#monitoring_config). For general information about using Google Cloud with Terraform, see [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

## Metric format

All Kubernetes cAdvisor/Kubelet metrics written to Cloud Monitoring use the resource type [ `prometheus_target`](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target). Each metric name is prefixed with `prometheus.googleapis.com/` and has a suffix indicating the Prometheus metric type, such as `/gauge`, `/histogram`, or `/counter`. Otherwise, each metric name is identical to the metric name exposed by open source Kubernetes.

## Exporting from Cloud Monitoring

The cAdvisor/Kubelet metrics can be exported from Cloud Monitoring by using the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/v3). Because all cAdvisor/Kubelet metrics are ingested by using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), cAdvisor/Kubelet metrics can be queried [by using Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql). They can also be queried by using [by using Monitoring Query Language (MQL)](https://docs.cloud.google.com/monitoring/mql).

## Querying metrics

When you query cAdvisor/Kubelet metrics, the name you use depends on whether you are using PromQL or Cloud Monitoring-based features like MQL or the Metrics Explorer [ menu-driven interface](https://docs.cloud.google.com/monitoring/charts/metrics-explorer#menu-driven-interface).

The following tables of cAdvisor/Kubelet metrics show two versions of each metric name: 

  * **PromQL metric name** : When [using PromQL](https://docs.cloud.google.com/monitoring/promql) in Cloud Monitoring pages of the Google Cloud console or in PromQL fields of the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/v3), use the PromQL metric name. 
  * **Cloud Monitoring metric name** When using other Cloud Monitoring features, use the Cloud Monitoring metric name in the tables below. This name must be prefixed with `prometheus.googleapis.com/`, which has been omitted from the entries in the table. 



## cAdvisor metrics

The Cloud Monitoring metric names in this table must be prefixed with `prometheus.googleapis.com/`. That prefix has been omitted from the entries in the table. 

PromQL metric name  
Cloud Monitoring metric name  
---  
Kind, Type, Unit   
Monitored resources   
Required GKE version | _Description_  
Labels  
`container_cpu_cfs_periods_total`  
`container_cpu_cfs_periods_total/counter`  
`CUMULATIVE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Number of elapsed enforcement period intervals. Sampled every 30 seconds._  
  
`cpu`  
`container_cpu_cfs_throttled_periods_total`  
`container_cpu_cfs_throttled_periods_total/counter`  
`CUMULATIVE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Number of throttled period intervals. Sampled every 30 seconds._  
  
`cpu`  
`container_cpu_usage_seconds_total`  
`container_cpu_usage_seconds_total/counter`  
`CUMULATIVE`, `DOUBLE`, `s`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative cpu time consumed. Sampled every 30 seconds._  
  
`cpu`  
`container_fs_limit_bytes`  
`container_fs_limit_bytes/gauge`  
`GAUGE`, `DOUBLE`, `By`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Number of bytes that can be consumed by the container on this filesystem. Sampled every 30 seconds._  
  
`disk`  
`container_fs_read_seconds_total`  
`container_fs_read_seconds_total/counter`  
`CUMULATIVE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of reads completed. Sampled every 30 seconds._  
  
`diskIO`  
`container_fs_reads_bytes_total`  
`container_fs_reads_bytes_total/counter`  
`CUMULATIVE`, `DOUBLE`, `By`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of bytes read. Sampled every 30 seconds._  
  
`diskIO`  
`container_fs_reads_total`  
`container_fs_reads_total/counter`  
`CUMULATIVE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of reads completed. Sampled every 30 seconds._  
  
`diskIO`  
`container_fs_usage_bytes`  
`container_fs_usage_bytes/gauge`  
`GAUGE`, `DOUBLE`, `By`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Number of bytes that are consumed by the container on this filesystem. Sampled every 30 seconds._  
  
`disk`  
`container_fs_write_seconds_total`  
`container_fs_write_seconds_total/counter`  
`CUMULATIVE`, `DOUBLE`, `s`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of seconds spent writing. Sampled every 30 seconds._  
  
`diskIO`  
`container_fs_writes_bytes_total`  
`container_fs_writes_bytes_total/counter`  
`CUMULATIVE`, `DOUBLE`, `By`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of bytes written. Sampled every 30 seconds._  
  
`diskIO`  
`container_fs_writes_total`  
`container_fs_writes_total/counter`  
`CUMULATIVE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of writes completed. Sampled every 30 seconds._  
  
`diskIO`  
`container_memory_rss`  
`container_memory_rss/gauge`  
`GAUGE`, `DOUBLE`, `By`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Size of RSS. Sampled every 30 seconds._  
  
`memory`  
`container_memory_working_set_bytes`  
`container_memory_working_set_bytes/gauge`  
`GAUGE`, `DOUBLE`, `By`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Current working set. Sampled every 30 seconds._  
  
`memory`  
`container_network_receive_bytes_total`  
`container_network_receive_bytes_total/counter`  
`CUMULATIVE`, `DOUBLE`, `By`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of bytes received. Sampled every 30 seconds._  
  
`network`  
`container_network_receive_packets_dropped_total`  
`container_network_receive_packets_dropped_total/counter`  
`CUMULATIVE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of packets dropped while receiving. Sampled every 30 seconds._  
  
`network`  
`container_network_receive_packets_total`  
`container_network_receive_packets_total/counter`  
`CUMULATIVE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of packets received. Sampled every 30 seconds._  
  
`network`  
`container_network_transmit_bytes_total`  
`container_network_transmit_bytes_total/counter`  
`CUMULATIVE`, `DOUBLE`, `By`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of bytes transmitted. Sampled every 30 seconds._  
  
`network`  
`container_network_transmit_packets_dropped_total`  
`container_network_transmit_packets_dropped_total/counter`  
`CUMULATIVE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of packets dropped while transmitting. Sampled every 30 seconds._  
  
`network`  
`container_network_transmit_packets_total`  
`container_network_transmit_packets_total/counter`  
`CUMULATIVE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative count of packets transmitted. Sampled every 30 seconds._  
  
`network`  
`container_pressure_cpu_stalled_seconds_total`  
`container_pressure_cpu_stalled_seconds_total/counter`  
`CUMULATIVE`, `DOUBLE`, `s`   
**prometheus_target**   
1.37  |  _Total time in seconds tasks were stalled on CPU (full). Sampled every 30 seconds._  
  
`cpu`  
`container_pressure_cpu_waiting_seconds_total`  
`container_pressure_cpu_waiting_seconds_total/counter`  
`CUMULATIVE`, `DOUBLE`, `s`   
**prometheus_target**   
1.37  |  _Total time in seconds tasks were waiting on CPU (some). Sampled every 30 seconds._  
  
`cpu`  
`container_pressure_io_stalled_seconds_total`  
`container_pressure_io_stalled_seconds_total/counter`  
`CUMULATIVE`, `DOUBLE`, `s`   
**prometheus_target**   
1.37  |  _Total time in seconds tasks were stalled on I/O (full). Sampled every 30 seconds._  
  
`diskIO`  
`container_pressure_io_waiting_seconds_total`  
`container_pressure_io_waiting_seconds_total/counter`  
`CUMULATIVE`, `DOUBLE`, `s`   
**prometheus_target**   
1.37  |  _Total time in seconds tasks were waiting on I/O (some). Sampled every 30 seconds._  
  
`diskIO`  
`container_pressure_memory_stalled_seconds_total`  
`container_pressure_memory_stalled_seconds_total/counter`  
`CUMULATIVE`, `DOUBLE`, `s`   
**prometheus_target**   
1.37  |  _Total time in seconds tasks were stalled on memory (full). Sampled every 30 seconds._  
  
`memory`  
`container_pressure_memory_waiting_seconds_total`  
`container_pressure_memory_waiting_seconds_total/counter`  
`CUMULATIVE`, `DOUBLE`, `s`   
**prometheus_target**   
1.37  |  _Total time in seconds tasks were waiting on memory (some). Sampled every 30 seconds._  
  
`memory`  
  
## Kubelet metrics

The Cloud Monitoring metric names in this table must be prefixed with `prometheus.googleapis.com/`. That prefix has been omitted from the entries in the table. 

PromQL metric name  
Cloud Monitoring metric name  
---  
Kind, Type, Unit   
Monitored resources   
Required GKE version | _Description_  
Labels  
`kubelet_certificate_manager_server_ttl_seconds`  
`kubelet_certificate_manager_server_ttl_seconds/gauge`  
`GAUGE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Gauge of the shortest TTL (time-to-live) of the Kubelet's serving certificate. The value is in seconds until certificate expiry (negative if already expired). If serving certificate is invalid or unused, the value will be +INF. Sampled every 30 seconds._  
  
  
`kubelet_node_name`  
`kubelet_node_name/gauge`  
`GAUGE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _The node's name. The count is always 1. Sampled every 30 seconds._  
  
`node`  
`kubelet_pleg_relist_duration_seconds`  
`kubelet_pleg_relist_duration_seconds/histogram`  
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Duration in seconds for relisting pods in PLEG. Sampled every 30 seconds._  
  
  
`kubelet_pod_worker_duration_seconds`  
`kubelet_pod_worker_duration_seconds/histogram`  
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Duration in seconds to sync a single pod. Broken down by operation type: create, update, or sync. Sampled every 30 seconds._  
  
`operation_type`  
`kubelet_running_containers`  
`kubelet_running_containers/gauge`  
`GAUGE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Number of containers currently running. Sampled every 30 seconds._  
  
`container_state`  
`kubelet_running_pods`  
`kubelet_running_pods/gauge`  
`GAUGE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Number of pods that have a running pod sandbox. Sampled every 30 seconds._  
  
  
`kubelet_runtime_operations_total`  
`kubelet_runtime_operations_total/counter`  
`CUMULATIVE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Cumulative number of runtime operations by operation type. Sampled every 30 seconds._  
  
`operation_type`  
`kubelet_volume_stats_available_bytes`  
`kubelet_volume_stats_available_bytes/gauge`  
`GAUGE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Number of available bytes in the volume. Sampled every 30 seconds._  
  
`namespace`   
`persistentvolumeclaim`  
`kubelet_volume_stats_capacity_bytes`  
`kubelet_volume_stats_capacity_bytes/gauge`  
`GAUGE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Capacity in bytes of the volume. Sampled every 30 seconds._  
  
`namespace`   
`persistentvolumeclaim`  
`kubelet_volume_stats_inodes`  
`kubelet_volume_stats_inodes/gauge`  
`GAUGE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Maximum number of inodes in the volume. Sampled every 30 seconds._  
  
`namespace`   
`persistentvolumeclaim`  
`kubelet_volume_stats_inodes_free`  
`kubelet_volume_stats_inodes_free/gauge`  
`GAUGE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Number of free inodes in the volume. Sampled every 30 seconds._  
  
`namespace`   
`persistentvolumeclaim`  
`kubelet_volume_stats_inodes_used`  
`kubelet_volume_stats_inodes_used/gauge`  
`GAUGE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Number of used inodes in the volume. Sampled every 30 seconds._  
  
`namespace`   
`persistentvolumeclaim`  
`kubelet_volume_stats_used_bytes`  
`kubelet_volume_stats_used_bytes/gauge`  
`GAUGE`, `DOUBLE`, `1`   
**prometheus_target**   
1.29.3-gke.1093000  |  _Number of used bytes in the volume. Sampled every 30 seconds._  
  
`namespace`   
`persistentvolumeclaim`  
  
## What's next

  * [Explore the other available metrics packages](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics)
  * [Collect specific Kubernetes metrics that aren't in this package](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/collect-specific-prometheus-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
