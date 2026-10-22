---
url: https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster/
title: Connect to a cluster \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:00.959409+00:00
---

# Connect to a cluster  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Connect to a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to establish an SSH connection to your cluster's nodes in Cluster Director. Based on the node type, connecting to a node lets you perform the following tasks:

  * **Login node** : manage shared file systems and submit Slurm jobs to the cluster schedulers.

  * **Compute node** : troubleshoot issues by letting you access logs or [manually run a health check](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/health-checks#manual-run) before you start critical jobs.




For more information on how Compute Engine uses key-based SSH authentication to establish connections to a Compute Engine instance, see [About SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh).

## Before you begin

When you access and use the Google Cloud console, you don't need to authenticate. You can automatically use Google Cloud services and APIs.

### Required roles

To get the permissions that you need to connect to a login node in a cluster, ask your administrator to grant you the following IAM roles on the project: 

  * To view clusters: [Hypercompute Cluster Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.viewer) (`roles/hypercomputecluster.viewer`) 
  * To connect to a node: [Compute OS Login ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.osLogin) (`roles/compute.osLogin`) 
  * To connect to a node secured by Identity-Aware Proxy (IAP): [IAP-Secured Tunnel User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelResourceAccessor) (`roles/iap.tunnelResourceAccessor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to connect to a login node in a cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to connect to a login node in a cluster:

  * To view the details of a single cluster: `hypercomputecluster.clusters.describe`
  * To connect to a node: `compute.instances.osLogin`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Connect to a cluster

The following sections explain how to connect to a login node or compute node in your cluster.

### Connect to a cluster's login node

To connect to a cluster's login node through SSH by using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/cluster-director/clusters/list)

  2. In the **Clusters** table, in the **Name** column, click the name of the cluster that you want to connect to. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  3. Click the **Nodes** tab.

  4. In the **Login nodes** section, in the **Connect** column, click the **SSH** button in the row that contains your login node. The **SSH-in-browser** window opens.

  5. If prompted, then click **Authorize**. Connecting to your node can take up to a minute to complete.

**Note:** If you encounter errors when connecting to your node, then see [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors).



### Connect to a cluster's compute node

To connect to a cluster's node through SSH by using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/cluster-director/clusters/list)

  2. In the **Clusters** table, in the **Name** column, click the name of the cluster that you want to connect to. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  3. Click the **Nodes** tab.

  4. In the **Compute nodes** section, in the **Name** column, click the name of the node that you want to connect to. A page that gives the details of the node appears, and the **Details** tab is selected.

  5. Click **SSH**.

  6. If prompted, then click **Authorize**. Connecting to your node can take up to a minute to complete.

**Note:** If you encounter errors when connecting to your node, then see [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors).



## What's next

  * [View a cluster topology](https://docs.cloud.google.com/cluster-director/docs/monitor/view-topology)

  * [Run health checks before running workloads](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health#health-checks)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
