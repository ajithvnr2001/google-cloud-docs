---
url: https://docs.cloud.google.com/cluster-director/docs/monitor/dashboards/
title: Monitor cluster performance with prebuilt dashboards \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:03.978552+00:00
---

# Monitor cluster performance with prebuilt dashboards  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/monitor/dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Monitor cluster performance with prebuilt dashboards Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to monitor how your cluster uses resources in Cluster Director by using pre-configured Cloud Monitoring dashboards.

Cluster Director provides built-in [Monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards) that let you view telemetry data and track the performance of the resources that your cluster uses. Use these dashboards to monitor the health and resource usage of your cluster.

To use customized Monitoring dashboards to monitor your clusters, see instead [Build custom Monitoring dashboards](https://docs.cloud.google.com/cluster-director/docs/monitor/custom-dashboards).

## Before you begin

When you access and use the Google Cloud console, you don't need to authenticate. You can automatically use Google Cloud services and APIs.

### Required roles

To get the permissions that you need to monitor clusters, ask your administrator to grant you the following IAM roles on the project: 

  * To view the details of a cluster: [Hypercompute Cluster Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.viewer) (`roles/hypercomputecluster.viewer`) 
  * To view Monitoring dashboards: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View Monitoring dashboards

To view the prebuilt Monitoring dashboards in a cluster, complete the following steps:

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director)

  2. In the navigation menu, click **Clusters**. The **Clusters** page appears.

  3. In the **Clusters** table, in the **Name** column, click the name of the cluster that you want to view the details of. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  4. Click the **Observability** tab. A pane that shows the available Monitoring prebuilt dashboards for your cluster appears.




## Available Monitoring dashboards

The prebuilt Monitoring dashboards that you can view in a cluster show real-time and historical data for the following resource categories:

  * **CPU** : you can monitor vCPU usage across all nodes in your cluster. This information can help you improve the performance of your workloads or save costs by deleting unused resources.

  * **Memory** : you can track memory usage to help ensure that your nodes have sufficient memory for your jobs and prevent out-of-memory errors.

  * **Network** : you can observe network traffic patterns, including bandwidth and throughput. This information is useful for diagnosing and troubleshooting communication bottlenecks in distributed workloads.

  * **GPU** : for clusters with GPU nodes, you can monitor GPU usage and GPU memory usage. This information helps you verify that your resources are efficiently used.

  * **Orchestrator** : you can view real-time CPU, GPU, and memory utilization, node health, and queue status for Slurm workloads. This information helps you troubleshoot job queue delays, identify performance bottlenecks, and balance compute capacity.




## What's next

  * [View cluster topology](https://docs.cloud.google.com/cluster-director/docs/monitor/view-topology)

  * [Manage cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
