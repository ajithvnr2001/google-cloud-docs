---
url: https://docs.cloud.google.com/cluster-director/docs/monitor/view-topology/
title: View cluster topology \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:59.735538+00:00
---

# View cluster topology  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/monitor/view-topology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  View cluster topology Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view the physical layout and real-time status of your cluster nodes in Cluster Director.

You can view the topology of the nodes in your cluster by using the Google Cloud console, including their health, usage, and maintenance schedules. This information can help you to manage high-performance workloads, troubleshoot networking issues, and help ensure optimal cluster configuration.

## Before you begin

Before you view the topology of the nodes in your cluster, consider the following:

  * You can only view topology information for A4X, A4, A3 Ultra, or A3 Mega instances that were created by using a reservation.

  * When you access and use the Google Cloud console, you don't need to authenticate. You can automatically use Google Cloud services and APIs.




### Required roles

To get the permissions that you need to view clusters, ask your administrator to grant you the [Hypercompute Cluster Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.viewer) (`roles/hypercomputecluster.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view clusters. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view clusters:

  * To view the details of a cluster: `hypercomputecluster.clusters.describe`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View a cluster topology

To view a cluster topology by using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director)

  2. In the navigation menu, click **Clusters**. The **Clusters** page appears.

  3. In the **Clusters** table, in the **Name** column, click the name of the cluster that you want to view the details of. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  4. Click the **Topology** tab. Then, based on the topology information that you want to view, click one of the following tabs:

     * To view cluster health information, click the **Health** tab.

     * To view cluster maintenance information, click the **Maintenance** tab.

     * To view cluster CPU and GPU usage information, click the **CPU utilization** and **GPU utilization** tabs.

For more information, see Understand cluster topology tabs in this document.




## Understand cluster topology tabs

When you view a cluster topology, you can view the following tabs to monitor the status and performance of your cluster:

  * Cluster health information

  * Cluster maintenance information

  * Cluster CPU and GPU usage information




### Cluster health information

When you view the **Health** tab on the page that gives the details of a cluster, you can see the health status for each compute node in your cluster. Each node is color-coded to indicate one of three operational states:

  * **Healthy** : the node is fully operational.

  * **Suspected bad** : the system has detected potential issues with your node, but the node remains operational. To run additional tests on the node to verify its status, see [Verify cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health#verify-health).

  * **Unhealthy** : the node failed the health check, and Slurm drained the node to prevent new jobs from scheduling. To undrain the node and resume running jobs on it, see [Troubleshoot GPU health check failures](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/health-checks).




### Cluster maintenance information

When you view the **Maintenance** tab on the page that gives the details of a cluster, you can view information about any upcoming [maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) for the nodes in your cluster. This information lets you anticipate and plan for necessary downtime.

If a maintenance event is scheduled for the nodes in your cluster, then you can manually start maintenance, rather than waiting for the scheduled time. For instructions, see [Manually start planned host maintenance events](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health#start-maintenance).

### Cluster CPU and GPU usage information

When you view the **CPU utilization** and **GPU utilization** tabs on the page that gives the details of a cluster, you can see a visual representation of resource usage across all nodes in your cluster in real time. These views help you understand how your workloads are distributed and whether your resources are being used efficiently. Use this information to identify performance bottlenecks and opportunities for optimization.

## What's next

  * [Monitor cluster performance with prebuilt dashboards](https://docs.cloud.google.com/cluster-director/docs/monitor/dashboards)

  * [Manage cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
