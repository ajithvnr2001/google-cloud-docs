---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/collect-specific-prometheus-metrics/
title: Collect specific Prometheus metrics from Kubernetes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:34:41.688440+00:00
---

# Collect specific Prometheus metrics from Kubernetes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/collect-specific-prometheus-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Collect specific Prometheus metrics from Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows operators how to configure [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) to filter and collect specific Kubernetes metrics from Google Kubernetes Engine (GKE) clusters and workloads.

You should already be familiar with the following:

  * [PromQL for Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql)
  * [Kubernetes metrics](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#component-metrics)



## Metrics collection in GKE

System components in GKE clusters emit and expose Prometheus metrics. By default, all clusters ingest system metrics that are specific to GKE. Additional built-in [metrics packages](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#available-metrics) are available to ingest curated collections of metrics for various components.

Independently of the built-in GKE metrics packages, you can manually configure Google Cloud Managed Service for Prometheus to ingest specific Prometheus metrics. This custom configuration works well for use cases like the following:

  * Monitor for specific signals in your cluster and workloads.
  * Optimize costs by disabling metrics packages that you don't need and ingesting only a subset of metrics.
  * Collect metrics that are emitted by components but aren't included in a metrics package.



For operators, [node metrics](https://kubernetes.io/docs/reference/instrumentation/node-metrics/), which are emitted by the `kubelet` process on each node, might be useful for monitoring workloads and nodes for specific signals.

### Metric collection custom resources

To filter and ingest a specific metric, you configure [Prometheus relabeling rules](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config) in one of the following custom resources:

  * [`PodMonitoring`](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#podmonitoring): configure metrics collection from Pods in a specific namespace.
  * [`ClusterPodMonitoring`](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#clusterpodmonitoring): configure metrics collection from Pods in any namespace.
  * [`ClusterNodeMonitoring`](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/main/doc/api.md#monitoring.googleapis.com/v1.ClusterNodeMonitoring): configure metrics collection from node components like the `kubelet` and cAdvisor.



### Metric duplication

If you filter for a metric that's also included in an active metrics package for a cluster, then the metric appears multiple times in Google Cloud Managed Service for Prometheus. For example, if your cluster has the [`KUBELET`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#available-metrics) metrics package enabled and you configure the collection of the `kubelet_running_containers` metric, you'll see duplicate values.

To avoid duplication, verify that the metrics that you're collecting aren't included in one of the active metrics packages. For more information about the included metrics, see the following metrics packages:

  * [GKE system metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes)
  * [Control plane metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics)
  * [Kubernetes object state metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics)
  * [cAdvisor and `kubelet` metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics)
  * [NVIDIA DCGM metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics)



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Verify that you have the permissions that are required for this document.
  * Use an existing GKE cluster or [create a new cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



### Required roles

To get the permissions that you need to collect and view metrics, ask your administrator to grant you the following IAM roles on your project: 

  * Create Kubernetes resources in your cluster: [Kubernetes Engine Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) (`roles/container.developer`) 
  * View metrics in Monitoring: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable Google Cloud Managed Service for Prometheus

Google Cloud Managed Service for Prometheus is enabled by default in all GKE clusters and can't be disabled in Autopilot clusters. If you're using an Autopilot cluster, then skip to the Configure metrics collection section.

To verify that Google Cloud Managed Service for Prometheus is enabled in your Standard cluster, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. In the row for the cluster that you want to check, click more_vert **Actions** > edit **Edit**. The **Cluster details** page opens.

  3. In the **Features** section, check the value in the **Managed Service for Prometheus** field. If the value is **Enabled** , skip to the Configure metrics collection section. If the value is **Disabled** , enable Google Cloud Managed Service for Prometheus:

     1. Click edit **Edit Managed Service for Prometheus**. The **Edit Managed Service for Prometheus** dialog opens.
     2. Select the **Enable Managed Service for Prometheus** checkbox.
     3. Click **Save changes**.



###  gcloud 

Check whether Google Cloud Managed Service for Prometheus is enabled in the cluster:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --format='value(monitoringConfig.managedPrometheusConfig.enabled)'
    

Replace the following:

  * `CLUSTER_NAME`: the name of your Standard cluster.
  * `CONTROL_PLANE_LOCATION`: the region or zone of the cluster control plane, such as `us-central1` or `us-central1-a`.



If the output is `True`, then Google Cloud Managed Service for Prometheus is enabled. If the output is `False`, then enable Google Cloud Managed Service for Prometheus:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-managed-prometheus
    

## Configure metrics collection

To configure Google Cloud Managed Service for Prometheus to ingest a specific emitted metric, you need the following information about the metric:

  * The metric name, such as `kubelet_working_pods`.
  * The endpoint that exposes the metric, such as `/metrics/cadvisor` or `/metrics`.



To find metrics and configure collection, follow these steps:

  1. Find a metric in the reference documentation for the specific component. For example, you can use the following resources to find a node metric:

     * [Monitoring cAdvisor with Prometheus](https://github.com/google/cadvisor/blob/master/docs/storage/prometheus.md#prometheus-container-metrics)

     * [Metrics for Kubernetes system components](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#kube-scheduler-metrics)

     * [kubelet/cAdvisor metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics)

  2. Check the active metrics packages for the cluster:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --flatten=monitoringConfig.componentConfig \
             --format='value(enableComponents)'
         

The output is similar to the following:
         
         SYSTEM_COMPONENTS;STORAGE;POD;DEPLOYMENT;STATEFULSET;DAEMONSET;HPA;JOBSET;CADVISOR;KUBELET;DCGM
         

  3. Check whether the metric that you want to collect is in one of these active packages by using the information in [Available metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#available-metrics). If your metric is included in an active metrics package, duplicate metrics might appear in Monitoring. If your metric isn't in an active metrics package, proceed to the next step.

  4. Optional: To verify that the metric is available at the metrics endpoint, query the endpoint by using the [`kubectl get --raw`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) command. For example, the following command queries the `/metrics` endpoint for the `kubelet_working_pods` metric:
         
         kubectl get --raw "/api/v1/nodes/NODE_NAME/proxy/metrics" | grep "kubelet_working_pods"
         

Replace `NODE_NAME` with the name of the node to query.

The output is similar to the following, which indicates that the metric is available:
         
         # HELP kubelet_working_pods [ALPHA] Number of pods the kubelet is actually running, broken down by lifecycle phase, whether the pod is desired, orphaned, or runtime only (also orphaned), and whether the pod is static. An orphaned pod has been removed from local configuration or force deleted in the API and consumes resources that are not otherwise visible.
         # TYPE kubelet_working_pods gauge
         kubelet_working_pods{config="desired",lifecycle="sync",static=""} 8
         kubelet_working_pods{config="desired",lifecycle="sync",static="true"} 1
         kubelet_working_pods{config="desired",lifecycle="terminated",static=""} 0
         kubelet_working_pods{config="desired",lifecycle="terminated",static="true"} 0
         kubelet_working_pods{config="desired",lifecycle="terminating",static=""} 0
         kubelet_working_pods{config="desired",lifecycle="terminating",static="true"} 0
         

  5. After you identify the metric that you want to collect, use a Prometheus relabeling rule in a PodMonitoring, ClusterPodMonitoring, or a ClusterNodeMonitoring custom resource to filter for that metric. The custom resource that you use depends on the properties of the metric, as described in the Metric collection custom resources section.

For example, review the following ClusterNodeMonitoring manifest:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: ClusterNodeMonitoring
         metadata:
           name: kubelet-pod-counts
         spec:
           selector:
             matchLabels: {}
           endpoints:
           - path: "/metrics"
             scheme: "https"
             interval: "30s"
             tls:
               insecureSkipVerify: true
             # metricRelabeling specifies the metrics to ingest. The metrics must be
             # available at the specified endpoint.
             metricRelabeling:
             - action: keep
               sourceLabels: [__name__]
               regex: kubelet_(active|working)_pods
         

This manifest has the following properties:

     * The `selector.matchLabels` field is an empty set (`{}`), which matches all nodes.
     * The `endpoints.path` field identifies the metrics endpoint to scrape.
     * The `metricRelabeling` field identifies the specific metrics to collect. In this example, Google Cloud Managed Service for Prometheus collects metrics that have the name `kubelet_active_pods` and `kubelet_working_pods` from the endpoint.



When you deploy the custom resource, Google Cloud Managed Service for Prometheus ingests metrics that match your specified configuration. You can view and query these metrics by using the same methods that you use for other metrics, such as Cloud Monitoring.

## Verify metrics collection for an example metric

The following steps show you how to configure Google Cloud Managed Service for Prometheus to collect the `kubelet_runtime_operations_errors_total` metric from the `kubelet`. In these example steps, you verify that the metric is not currently collected, create a ClusterNodeMonitoring (because the `kubelet` is a node component), and then verify that the metric appears in Monitoring.

  1. Verify that the `kubelet_runtime_operations_errors_total` metric isn't already in Monitoring:

     1. In the Google Cloud console, go to the **Metrics explorer** page.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

     2. In the **Queries** section, in the **Metric** field, try to select the `prometheus/kubelet_runtime_operations_errors_total/counter` metric. If you don't see a search result, the metric isn't being collected.

  2. Create a ClusterNodeMonitoring to filter for the `kubelet_runtime_operations_errors_total` metric:

     1. Save the following ClusterNodeMonitoring manifest as `kubelet-runtime-errors-collector.yaml`:
            
            apiVersion: monitoring.googleapis.com/v1
            kind: ClusterNodeMonitoring
            metadata:
              name: kubelet-runtime-errors-collector
            spec:
              selector:
                matchLabels: {}
              endpoints:
              - path: /metrics
                scheme: https
                interval: 30s
                tls:
                  insecureSkipVerify: true
                metricRelabeling:
                - action: keep
                  sourceLabels: [__name__]
                  regex: kubelet_runtime_operations_errors_total
            

     2. Create the ClusterNodeMonitoring:
            
            kubectl apply -f kubelet-runtime-errors-collector.yaml
            

The metric might take up to 10 minutes to appear in Monitoring.

  3. In the Google Cloud console, verify that the metric appears in Monitoring:

     1. Go to the **Metrics explorer** page.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

     2. In the **Queries** section, in the **Metric** field, select the `prometheus/kubelet_runtime_operations_errors_total/counter` metric.

     3. Optional: In the **Filter** drop-down menu, select your cluster.

The **Results** section shows a chart with the collected metric.




## What's next

  * [Explore the available metrics packages in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics)
  * [Configure automatic application monitoring for workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring)
  * [Create and manage custom Monitoring dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
