---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics/
title: View cost-related optimization metrics \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:43.160723+00:00
---

# View cost-related optimization metrics  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  View cost-related optimization metrics Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to view cost-related utilization metrics for your Google Kubernetes Engine (GKE) clusters. These metrics describe how effectively your GKE clusters and workloads are utilizing the Compute Engine resources you pay for.

You can use this information to optimize the cost-to-performance ratio of your clusters and workloads.

## Cost optimization metrics

In the **Cost Optimization** tab in the Google Cloud console, you can view the following metrics for your clusters and workloads:

  * **CPU utilization:** Displays a bar chart that shows the relationship between the following CPU metrics: 
    * **Used** : The amount of CPU used by all containers in the cluster or workload. Calculated from the [`container/cpu/core_usage_time`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/core_usage_time) metric.
    * **Requested** : The amount of CPU requested by all containers in the cluster or workload. Calculated from the [`container/cpu/request_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/request_cores) metric.
    * **Allocatable** : The amount of CPU allocated to all nodes in the cluster. This metric is shown on the Clusters page. Calculated from the [`node/cpu/allocatable_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/cpu/allocatable_cores) metric. For Autopilot clusters, there is no allocatable value because Google automatically adjusts CPU allocations.
    * **Limit** : The CPU limit for all containers in a workload. This metric is shown on the Workloads page. Calculated from the [`container/cpu/limit_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/limit_cores) metric.
  * **CPU hours** : The total number of core hours on all nodes in a workload or cluster within the selected timeframe. Calculated from the [`node/cpu/total_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/cpu/total_cores) metric (for Standard clusters) and the [`container/cpu/request_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/request_cores) metric (for Autopilot clusters and workloads).
  * **Memory utilization** : Displays a bar chart that shows the relationship between the following memory metrics: 
    * **Used** : The amount of memory used by all containers in a cluster or workload. Calculated from the [`container/memory/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/used_bytes) metric.
    * **Requested** : The amount of memory requested for all containers in a cluster or workload. Calculated from the [`container/memory/request_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/request_bytes) metric.
    * **Allocatable** : The amount of memory allocated to all nodes in the cluster. This metric is shown on the Clusters page. Calculated from the [`node/memory/allocatable_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/memory/allocatable_bytes) metric. For Autopilot clusters, there is no allocatable value because Google automatically adjusts memory allocations.
    * **Limit** : The memory limit for all containers in a workload. This metric is shown on the Workloads page. Calculated from the [`container/memory/limit_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/limit_bytes) metric.
  * **Memory hours** : The total amount of memory on all nodes in a workload or cluster within the selected timeframe. Calculated from the [`node/memory/total_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/memory/total_bytes) metric (for clusters) and the [`container/memory/requested_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/requested_bytes) metric (for Autopilot clusters and workloads).



## View the metrics

To view cost-related utilization metrics, perform the following steps in the Google Cloud console :

  1. To see cluster-level metrics, go to the **Kubernetes Clusters** page.

[Go to Kubernetes Clusters](https://console.cloud.google.com/kubernetes/list)

To see workload-level metrics, go to the **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Select the **Cost Optimization** tab.

  3. Choose the timeframe over which the metrics are averaged (utilization) or accumulated (total hours). For example, 1 day, 1 month, and more. If the lifetime of the cluster or workload is less than the selected timeframe, metrics accumulated for the lifetime of cluster or workload displays. For example, you choose a timeframe of 1 day but the workload was created only 4 hours ago, so only 4 hours of metrics are displayed.

  4. Hold the pointer over the utilization metric to see further details.




Cost optimization metrics will display for cluster modes as follows:

  * Standard clusters will always have used, requested and allocatable metrics visible at creation time due to the inclusion of managed GKE components in the overall calculation (kube-system namespace).


  * Autopilot clusters only display metrics when you deploy workloads with specified requests to the cluster. This is due to the [Autopilot pricing](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode) model. Autopilot clusters don't show allocatable metrics because you only pay for resources requested by your running workloads.



Workloads deployed to Standard clusters that don't have requests or limits specified, won't show a ratio on the chart. Instead, the bar chart will represent just the workload usage metric.

Workloads deployed to Autopilot clusters that don't have requests or limits specified, will have [default](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#default_container_resource_requests) values applied to the containers, and will show the ratios at all times.

## What's next

  * Learn about [Best practices for running cost-optimized applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke).
  * Read the [Create a cost-optimized cluster in just a few clicks](https://cloud.google.com/blog/products/containers-kubernetes/gke-setup-guide-automates-creation-of-cost-optimized-cluster) blog post.
  * Learn how to [view observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
