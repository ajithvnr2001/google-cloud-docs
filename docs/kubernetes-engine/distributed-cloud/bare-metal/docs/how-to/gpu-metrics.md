---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-metrics/
title: Send GPU metrics to Cloud Monitoring \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:01.367078+00:00
---

# Send GPU metrics to Cloud Monitoring  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Send GPU metrics to Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

If your [cluster has nodes that use NVIDIA GPUs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-manual-use), you can monitor the GPU utilization, performance, and health by configuring the cluster to send [NVIDIA Data Center GPU Manager (DCGM)](https://developer.nvidia.com/dcgm) metrics to Cloud Monitoring. This solution uses Google Cloud Managed Service for Prometheus to collect metrics from NVIDIA DCGM.

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

To use Google Cloud Managed Service for Prometheus to collect metrics from DCGM, your Google Distributed Cloud deployment must meet the following requirements:

  * NVIDIA [DCGM-Exporter tool](https://github.com/NVIDIA/dcgm-exporter) must be already installed on your cluster. DCGM-Exporter is installed when you install NVIDIA GPU Operator. For NVIDIA GPU Operator installation instructions, see [Install and verify the NVIDIA GPU Operator](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-manual-use#install_verify).

  * Google Cloud Managed Service for Prometheus must be enabled. For instructions, see [Enable Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/application-logging-monitoring#enable_managed_prometheus).




## Configure a PodMonitoring resource

Configure a PodMonitoring resource for Google Cloud Managed Service for Prometheus to collect the exported metrics. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

To ingest the metric data emitted by the DCGM Exporter Pod (`nvidia-dcgm-exporter`), Google Cloud Managed Service for Prometheus uses target scraping. Target scraping and metrics ingestion are configured using Kubernetes [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). The managed service uses [PodMonitoring](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.13.0/doc/api.md#podmonitoring) custom resources.

A PodMonitoring custom resource scrapes targets in the namespace in which it's deployed only. To scrape targets in multiple namespaces, deploy the same PodMonitoring custom resource in each namespace.

  1. Create a manifest file with the following configuration:

The `selector` section in the manifest specifies that the DCGM Exporter Pod, `nvidia-dcgm-exporter`, is selected for monitoring. This Pod is deployed when you install the NVIDIA GPU Operator.
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: dcgm-gmp
         spec:
           selector:
             matchLabels:**      app: nvidia-dcgm-exporter**
           endpoints:
           - port: metrics
             interval: 30s
         

  2. Deploy the PodMonitoring custom resource:
         
         kubectl apply -n NAMESPACE -f FILENAME --kubeconfig KUBECONFIG
         

Replace the following:

     * `NAMESPACE`: the namespace into which you're deploying the PodMonitoring custom resource.

     * `FILENAME`: the path of the manifest file for the PodMonitoring custom resource.

     * `KUBECONFIG`: the path of the kubeconfig file for the cluster.

  3. Verify that the PodMonitoring custom resource is installed in the intended namespace, run the following command:
         
         kubectl get podmonitoring -n NAMESPACE --kubeconfig KUBECONFIG
         

The output should look similar to the following:
         
         NAME       AGE
         dcgm-gmp   3m37s
         




## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured the DCGM exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Use Prometheus Query Language (PromQL) to specify the data to display on the chart:

     1. In the toolbar of the query-builder pane, click **< > PromQL**.

     2. Enter your query into the query editor. For example, to chart the average number of seconds CPUs spent in each mode over the past hour, use the following query:
            
            DCGM_FI_DEV_GPU_UTIL{cluster="CLUSTER_NAME", namespace="NAMESPACE"}
            

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster with nodes that are using GPUs.

     * `NAMESPACE`: the namespace into which you deployed the PodMonitoring custom resource.

For more information about using PromQL, see [PromQL in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
