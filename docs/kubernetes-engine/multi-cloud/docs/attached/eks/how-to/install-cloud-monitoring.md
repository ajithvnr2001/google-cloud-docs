---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/install-cloud-monitoring/
title: Install Cloud Monitoring on EKS attached clusters \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:03.494525+00:00
---

# Install Cloud Monitoring on EKS attached clusters  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/install-cloud-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/concepts/overview)



Send feedback 

#  Install Cloud Monitoring on EKS attached clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how GKE attached clusters integrates with Cloud Monitoring and how to view your metrics.

## Before you begin

  1. Fulfill the [prerequisites for GKE attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/cluster-prerequisites).

  2. [Authorize Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/attach-cluster#telemetry-agent-auth) to set up permissions for Google Cloud Observability.




## Overview

GKE attached clusters has built-in integration with Cloud Monitoring for system metrics of nodes, pods, and containers. This allows you to easily see the resource consumption of workloads in the cluster, build dashboards, and configure alerts.

GKE attached clusters installs the metrics collector `gke-metrics-agent` in your cluster. This agent is based on [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/), and runs on every node in the cluster. It samples metrics every minute, and uploads measurements to Cloud Monitoring.

Once metrics for your cluster have been uploaded, they reside in your Google Cloud project. You can aggregate data across all of your clusters, build custom dashboards, explore a single cluster's data, view line charts, set up alerts, and more.

## Using the Metrics Explorer

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Kubernetes Container` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Kubernetes Container**.
     2. In the **Active metric categories** menu, select **Anthos**.
     3. In the **Active metrics** menu, select **CPU usage time**. 
     4. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



## Metrics monitored resource type

Metrics are collected using one of the following three monitored resource types. These types correspond to a Kubernetes object that the measurement is being made for:

  * [k8s_node](https://cloud.google.com/monitoring/api/resources#tag_k8s_node)
  * [k8s_container](https://cloud.google.com/monitoring/api/resources#tag_k8s_container)
  * [k8s_pod](https://cloud.google.com/monitoring/api/resources#tag_k8s_pod)



For example, measurements about a Pod would use the monitored resource type `k8s_pod`. These metrics would therefore include labels for `pod_name` and `namespace_name`, that identify a particular Pod. If you want to see metrics for a specific cluster, use the following format:
    
    
    attachedClusters/CLUSTER_NAME
    

A different set of _metrics types_ are used for each _monitored resource type_. To learn more about these metrics types, see [GKE system metrics](https://cloud.google.com/monitoring/api/metrics_kubernetes).

## What metrics are collected

  * [v1.35.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.35.0-gke.1/metrics)
  * [v1.34.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.34.0-gke.2/metrics)
  * [v1.34.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.34.0-gke.1/metrics)
  * [v1.33.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.33.0-gke.3/metrics)
  * [v1.33.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.33.0-gke.2/metrics)
  * [v1.33.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.33.0-gke.1/metrics)
  * [v1.32.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.32.0-gke.3/metrics)
  * [v1.32.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.32.0-gke.2/metrics)
  * [v1.32.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.32.0-gke.1/metrics)
  * [v1.31.0-gke.5](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.31.0-gke.5/metrics)
  * [v1.31.0-gke.4](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.31.0-gke.4/metrics)
  * [v1.31.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.31.0-gke.3/metrics)
  * [v1.31.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.31.0-gke.2/metrics)
  * [v1.31.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.31.0-gke.1/metrics)
  * [v1.30.0-gke.7](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.30.0-gke.7/metrics)
  * [v1.30.0-gke.6](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.30.0-gke.6/metrics)
  * [v1.30.0-gke.5](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.30.0-gke.5/metrics)
  * [v1.30.0-gke.4](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.30.0-gke.4/metrics)
  * [v1.30.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.30.0-gke.3/metrics)
  * [v1.30.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.30.0-gke.2/metrics)
  * [v1.30.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.30.0-gke.1/metrics)
  * [v1.29.0-gke.9](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.29.0-gke.9/metrics)
  * [v1.29.0-gke.8](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.29.0-gke.8/metrics)
  * [v1.29.0-gke.7](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.29.0-gke.7/metrics)
  * [v1.29.0-gke.6](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.29.0-gke.6/metrics)
  * [v1.29.0-gke.5](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.29.0-gke.5/metrics)
  * [v1.29.0-gke.4](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.29.0-gke.4/metrics)
  * [v1.29.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.29.0-gke.3/metrics)
  * [v1.29.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.29.0-gke.2/metrics)
  * [v1.29.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.29.0-gke.1/metrics)
  * [v1.28.0-gke.9](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.28.0-gke.9/metrics)
  * [v1.28.0-gke.8](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.28.0-gke.8/metrics)
  * [v1.28.0-gke.7](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.28.0-gke.7/metrics)
  * [v1.28.0-gke.6](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.28.0-gke.6/metrics)
  * [v1.28.0-gke.5](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.28.0-gke.5/metrics)
  * [v1.28.0-gke.4](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.28.0-gke.4/metrics)
  * [v1.28.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.28.0-gke.3/metrics)
  * [v1.28.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.28.0-gke.2/metrics)
  * [v1.28.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.28.0-gke.1/metrics)
  * [v1.27.0-gke.9](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.27.0-gke.9/metrics)
  * [v1.27.0-gke.8](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.27.0-gke.8/metrics)
  * [v1.27.0-gke.7](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.27.0-gke.7/metrics)
  * [v1.27.0-gke.6](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.27.0-gke.6/metrics)
  * [v1.27.0-gke.5](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.27.0-gke.5/metrics)
  * [v1.27.0-gke.4](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.27.0-gke.4/metrics)
  * [v1.27.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.27.0-gke.3/metrics)
  * [v1.27.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.27.0-gke.2/metrics)
  * [v1.27.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.27.0-gke.1/metrics)
  * [v1.26.0-gke.9](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.26.0-gke.9/metrics)
  * [v1.26.0-gke.8](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.26.0-gke.8/metrics)
  * [v1.26.0-gke.7](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.26.0-gke.7/metrics)
  * [v1.26.0-gke.6](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.26.0-gke.6/metrics)
  * [v1.26.0-gke.5](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.26.0-gke.5/metrics)
  * [v1.26.0-gke.4](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.26.0-gke.4/metrics)
  * [v1.26.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.26.0-gke.3/metrics)
  * [v1.26.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.26.0-gke.2/metrics)
  * [v1.26.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.26.0-gke.1/metrics)
  * [v1.25.0-gke.8](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.25.0-gke.8/metrics)
  * [v1.25.0-gke.7](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.25.0-gke.7/metrics)
  * [v1.25.0-gke.6](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.25.0-gke.6/metrics)
  * [v1.25.0-gke.5](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.25.0-gke.5/metrics)
  * [v1.25.0-gke.4](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.25.0-gke.4/metrics)
  * [v1.25.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.25.0-gke.3/metrics)
  * [v1.25.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.25.0-gke.2/metrics)
  * [v1.25.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.25.0-gke.1/metrics)
  * [v1.24.0-gke.5](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.24.0-gke.5/metrics)
  * [v1.24.0-gke.4](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.24.0-gke.4/metrics)
  * [v1.24.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.24.0-gke.3/metrics)
  * [v1.24.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.24.0-gke.2/metrics)
  * [v1.24.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.24.0-gke.1/metrics)
  * [v1.23.0-gke.3](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.23.0-gke.3/metrics)
  * [v1.23.0-gke.2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.23.0-gke.2/metrics)
  * [v1.23.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.23.0-gke.1/metrics)
  * [v1.22.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.22.0-gke.1/metrics)
  * [v1.21.0-gke.1](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/versions/v1.21.0-gke.1/metrics)



## What's next?

  * [Set up managed data collection with Managed Service for Prometheus](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/managed-service-prometheus)
  * [Using Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer)
  * [Create logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics)
  * [Building queries for Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql)
  * [Setting up Alerting](https://docs.cloud.google.com/monitoring/alerts)
  * [The GKE overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
