---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics/
title: Configure metrics collection \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:23.924683+00:00
---

# Configure metrics collection  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure metrics collection Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to configure Google Kubernetes Engine (GKE) to send metrics to [Cloud Monitoring](https://docs.cloud.google.com/monitoring). Metrics in Cloud Monitoring can populate [custom dashboards](https://docs.cloud.google.com/monitoring/dashboards), generate [alerts](https://docs.cloud.google.com/monitoring/alerts), create [service-level objectives](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring), or be fetched by third-party monitoring services using the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api).

GKE provides several sources of metrics:

  * **System metrics** : metrics from essential system components, describing low-level resources such as CPU, memory and storage.
  * **[Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)** : lets you monitor and alert on your workloads, using Prometheus, without having to manually manage and operate Prometheus at scale.
  * Packages of observability metrics:

    * **Control plane metrics** : metrics exported from certain control plane components such as the API server and scheduler.
    * **Kube state metrics** : a curated set of metrics exported from the [kube state](https://github.com/kubernetes/kube-state-metrics#readme) service, used to monitor the state of Kubernetes objects like Pods, Deployments, and more. For the set of included metrics, see [Use kube state metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/kube-state-metrics).

The kube state package is a managed solution. If you need greater flexibility—for example, if you need to collect additional metrics, or need to manage scrape intervals or to scrape other resources—you can disable the package, if it is enabled, and deploy your own instance of the open source kube state metrics service. For more information, see the Google Cloud Managed Service for Prometheus exporter documentation for [Kube state metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kube_state_metrics).

    * **cAdvisor/Kubelet** : a curated set of cAdvisor and `kubelet` metrics. For the set of included metrics, see [Use cAdvisor/Kubelet metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics).

The cAdvisor/Kubelet package is a managed solution. If you need greater flexibility—for example, if you need to collect additional metrics or to manage scrape intervals or to scrape other resources—you can disable the package, if it is enabled, and deploy your own instance of the open source cAdvisor/Kubelet metrics services.

    * **NVIDIA Data Center GPU Manager (DCGM) metrics** : metrics from [DCGM](https://developer.nvidia.com/dcgm) that provide a comprehensive view of GPU health, performance, and utilization.

  * [**Kubernetes metrics**](https://kubernetes.io/docs/reference/instrumentation/metrics/): raw metrics in Prometheus format that are emitted by Kubernetes components and are available at the `/metrics` endpoints for those components. The curated metrics packages for GKE are a subset of these metrics. You can configure Google Cloud Managed Service for Prometheus to ingest these metrics by using custom resources like PodMonitoring and ClusterNodeMonitoring. For more information, see [Collect specific Prometheus metrics from Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/collect-specific-prometheus-metrics).




You can also configure [automatic application monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring) for certain workloads.

## System metrics

When a cluster is created, GKE by default collects certain metrics emitted by system components.

You have a choice whether or not to send metrics from your GKE cluster to Cloud Monitoring. If you choose to send metrics to Cloud Monitoring, you must send system metrics.

All GKE system metrics are ingested into Cloud Monitoring with the prefix `kubernetes.io`.

### Pricing

Cloud Monitoring does not charge for the ingestion of GKE system metrics. For more information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing#metrics-non-chargeable).

### Configuring collection of system metrics

To enable system metric collection, pass the `SYSTEM` value to the `--monitoring` flag of the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) or [`gcloud container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update) commands.

To disable system metric collection, use the `NONE` value for the `--monitoring` flag. If system metric collection is disabled, basic information like CPU usage, memory usage, and disk usage are not available for a cluster when viewing [observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

For GKE Autopilot clusters, you cannot disable the collection of system metrics.

**Warning:** If you disable Cloud Logging or Cloud Monitoring or apply exclusion filters, GKE customer support is offered on a best-effort basis and might require additional effort from your engineering team.

See [Observability for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability) for more details about Cloud Monitoring integration with GKE.

To configure the collection of system metrics by using Terraform, see the `monitoring_config` block in the [ Terraform registry for `google_container_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#monitoring_config). For general information about using Google Cloud with Terraform, see [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

### List of system metrics

System metrics include metrics from essential system components important for Kubernetes. For a list of these metrics, see [GKE system metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes).

If you enable Cloud Monitoring for your cluster, then you can't disable system monitoring (`--monitoring=SYSTEM`).

### Troubleshooting system metrics

If system metrics are not available in Cloud Monitoring as expected, see [Troubleshoot system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/system-metrics).

## Package: Control plane metrics

You can configure a GKE cluster to send certain metrics emitted by the Kubernetes API server, Scheduler, and Controller Manager to Cloud Monitoring.

For more information, see [Collect and view control plane metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics).

## Package: Kube state metrics

You can configure a GKE cluster to send a curated set of kube state metrics in Prometheus format to Cloud Monitoring. This package of kube state metrics includes metrics for Pods, Deployments, StatefulSets, DaemonSets, HorizontalPodAutoscaler resources, Persistent Volumes, Persistent Volume Claims, and JobSets.

For more information, see [Collect and view Kube state metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics).

## Package: cAdvisor/Kubelet metrics

You can configure a GKE cluster to send a curated set of cAdvisor/Kubelet metrics in Prometheus format to Cloud Monitoring. The curated set of metrics is a subset of the large set of cAdvisor/Kubelet metrics built into every Kubernetes deployment by default. The curated cAdvisor/Kubelet is designed to provide the most useful metrics, reducing ingestion volume and associated costs.

For more information, see [Collect and view cAdvisor/Kubelet metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics).

## Package: NVIDIA Data Center GPU Manager (DCGM) metrics

You can monitor GPU utilization, performance, and health by configuring GKE to send [NVIDIA Data Center GPU Manager (DCGM) metrics](https://developer.nvidia.com/dcgm) to Cloud Monitoring.

For more information, see [Collect and view NVIDIA Data Center GPU Manager (DCGM) metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics).

## Disable metric packages

You can disable the use of metric packages in the cluster. You might want to disable certain packages to reduce costs or if you are using an alternate mechanism for collecting the metrics, like Google Cloud Managed Service for Prometheus and an exporter.

### Console

To disable the collection of metrics from the **Details** tab for the cluster, do the following:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page: 

[Go to **Kubernetes clusters**](https://console.cloud.google.com/kubernetes/list)

If you use the search bar to find this page, then select the result whose subheading is **Kubernetes Engine**.

  2. Click your cluster's name.

  3. In the **Features** row labelled **Cloud Monitoring** , click the **Edit** icon.

  4. In the **Components** drop-down menu, clear the metric components that you want to disable.

  5. Click **OK**.

  6. Click **Save Changes**.




### gcloud

  1. Open a terminal window with Google Cloud SDK and the Google Cloud CLI installed. One way to do this is to use Cloud Shell.

  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  3. Call the [`gcloud container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) command and pass an updated set of values to the `--monitoring` flag. The set of values supplied to the `--monitoring` flag overrides any previous setting.

For example, to turn off the collection of all metrics except system metrics, run the following command:
         
         gcloud container clusters update CLUSTER_NAME \
             --location=COMPUTE_LOCATION \
             --enable-managed-prometheus \
             --monitoring=SYSTEM
         

This command disables the collection of any previously configured metric packages.




### Terraform

To configure the collection of metrics by using Terraform, see the `monitoring_config` block in the [ Terraform registry for `google_container_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#monitoring_config). For general information about using Google Cloud with Terraform, see [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

### Understanding your Monitoring bill

You can use Cloud Monitoring to identify the control plane or kube state metrics that are writing the largest numbers of samples. These metrics are contributing the most to your costs. After you identify the most expensive metrics, you can modify your scrape configs to filter these metrics appropriately.

The Cloud Monitoring **Metrics Management** page provides information that can help you control the amount you spend on billable metrics without affecting observability. The **Metrics Management** page reports the following information: 

  * Ingestion volumes for both byte- and sample-based billing, across metric domains and for individual metrics.
  * Data about labels and cardinality of metrics.
  * Number of reads for each metric.
  * Use of metrics in alerting policies and custom dashboards.
  * Rate of metric-write errors.



You can also use the **Metrics Management** page to [exclude unneeded metrics](https://docs.cloud.google.com/monitoring/docs/metrics-management#exclude-metrics), eliminating the cost of ingesting them. 

To view the **Metrics Management** page, do the following: 

  1. In the Google Cloud console, go to the  query_stats **Metrics management** page: 

[Go to **Metrics management**](https://console.cloud.google.com/monitoring/metrics-management)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar, select your time window. By default, the **Metrics Management** page displays information about the metrics collected in the previous one day.



For more information about the **Metrics Management** page, see [View and manage metric usage](https://docs.cloud.google.com/monitoring/docs/metrics-management).

To identify which control plane or kube state metrics have the largest number of samples being ingested, do the following:

  1. In the Google Cloud console, go to the  query_stats **Metrics management** page: 

[Go to **Metrics management**](https://console.cloud.google.com/monitoring/metrics-management)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. On the **Billable samples ingested** scorecard, click **View charts**.

  3. Locate the **Namespace Volume Ingestion** chart, and then click _more_vert_ **More chart options**.

  4. In the **Metric** field, verify that the following resource and metric are selected:  
[`Metric Ingestion Attribution`](https://docs.cloud.google.com/monitoring/api/resources#tag_monitoring.googleapis.com/MetricIngestionAttribution) and [`Samples written by attribution id`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/collection/attribution/write_sample_count).

  5. In the **Filters** page, do the following:

     1. In the **Label** field, verify that the value is `attribution_dimension`.

     2. In the **Comparison** field, verify that the value is `= (equals)`.

     3. In the **Value** field, select `cluster`.

  6. Clear the **Group by** setting.

  7. Optionally, filter for only certain metrics. For example, control plane API server metrics all include "apiserver" as part of the metric name, and kube state Pod metrics all include "kube_pod" as part of the metric name, so you can filter for metrics containing those strings:

     * Click **Add Filter**.

     * In the **Label** field, select `metric_type`.

     * In the **Comparison** field, select `=~ (equals regex)`.

     * In the **Value** field, enter `.*apiserver.*` or `.*kube_pod.*`.

  8. Optionally, group the number of samples ingested by GKE region or project:

     * Click **Group by**.

     * Ensure **metric_type** is selected.

     * To group by GKE region, select **location**.

     * To group by project, select **project_id**.

     * Click **OK**.

  9. Optionally, group the number of samples ingested by GKE cluster name:

     * Click **Group by**.

     * To group by GKE cluster name, ensure both **attribution_dimension** and **attribution_id** are selected.

     * Click **OK**.

  10. To see the ingestion volume for each of the metrics, in the toggle labeled **Chart Table Both** , select **Both**. The table shows the ingested volume for each metric in the **Value** column.

Click the **Value** column header twice to sort the metrics by descending ingestion volume.




These steps show the metrics with the highest rate of samples ingested into Cloud Monitoring. Because the metrics in the observability packages are [charged](https://cloud.google.com/stackdriver/pricing) by the number of samples ingested, pay attention to metrics with the greatest rate of samples being ingested.

## Other metrics

In addition to the system metrics and metric packages described in this document, [**Istio metrics**](https://docs.cloud.google.com/monitoring/api/metrics_istio) are also available for GKE clusters. For pricing information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing#metrics-non-chargeable).

## Available metrics

The following table indicates supported values for the `--monitoring` flag for the [create](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) and [update](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update) commands.

Source | `--monitoring` value | Metrics Collected  
---|---|---  
None | `NONE` |  No metrics sent to Cloud Monitoring; no metric collection agent installed in the cluster. This value isn't supported for Autopilot clusters.   
[ System](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) | `SYSTEM` | Metrics from essential system components required for Kubernetes. For a complete list of the metrics, see [ Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes).  
[ API server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#control-plane-metrics) | `API_SERVER` | Metrics from `kube-apiserver`. For a complete list of the metrics, see [ API server metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics#api-server).  
[ Scheduler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#control-plane-metrics) | `SCHEDULER` | Metrics from `kube-scheduler`. For a complete list of the metrics, see [ Scheduler metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics#scheduler).   
[ Controller Manager](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#control-plane-metrics) | `CONTROLLER_MANAGER` | Metrics from `kube-controller-manager`. For a complete list of the metrics, see [ Controller Manager metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics#controller-manager).  
[ Persistent volume (Storage)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) | `STORAGE` | Storage metrics from `kube-state-metrics`. Includes metrics for Persistent Volume and Persistent Volume Claims. For a complete list of the metrics, see [ Storage metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/kube-state-metrics#ksm-storage-metrics).   
[ Pod](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) | `POD` | Pod metrics from `kube-state-metrics`. For a complete list of the metrics, see [ Pod metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/kube-state-metrics#ksm-pod-metrics).   
[ Deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) | `DEPLOYMENT` | Deployment metrics from `kube-state-metrics`. For a complete list of the metrics, see [ Deployment metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/kube-state-metrics#ksm-deployment-metrics).   
[ StatefulSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) | `STATEFULSET` | StatefulSet metrics from `kube-state-metrics`. For a complete list of the metrics, see [ StatefulSet metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/kube-state-metrics#ksm-statefulset-metrics).  
[ DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) | `DAEMONSET` | DaemonSet metrics from `kube-state-metrics`. For a complete list of the metrics, see [ DaemonSet metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/kube-state-metrics#ksm-daemonset-metrics).   
[ HorizontalPodAutoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) | `HPA` | HPA metrics from `kube-state-metrics`. See a complete list of [ HorizontalPodAutoscaler metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/kube-state-metrics#ksm-hpa-metrics).   
[ JobSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) | `JOBSET` | JobSet metrics from `kube-state-metrics`. See a complete list of [ JobSet metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics#ksm-jobset-metrics).   
[ cAdvisor](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#cadvisor-kubelet-package) | `CADVISOR` | cAdvisor metrics from the cAdvisor/Kubelet metrics package. For a complete list of the metrics, see [ cAdvisor metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics#cadvisor-metrics).   
[ `kubelet`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#cadvisor-kubelet-package) | `KUBELET` | `kubelet` metrics from the cAdvisor/Kubelet For a complete list of the metrics, see [`kubelet` metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics#kubelet-pod-metrics).   
[ NVIDIA Data Center GPU Manager (DCGM) metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#dcgm-package) | `DCGM` | Metrics from NVIDIA Data Center GPU Manager (DCGM).  
  
You can also collect Prometheus-style metrics exposed by any GKE workload by using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), which lets you monitor and alert on your workloads, using Prometheus, without having to manually manage and operate Prometheus at scale.

## What's next

  * Learn how to troubleshoot [system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/system-metrics).
  * Learn how to [collect and view kube state metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics).
  * Learn how to [view observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).
  * Learn how to [collect and view control plane metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
