---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-auto-ipam/
title: Use auto IP address management \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:07.556176+00:00
---

# Use auto IP address management  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-auto-ipam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Use auto IP address management Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to enable automatic IP address management (auto IPAM) on a Google Kubernetes Engine (GKE) cluster. When you enable auto IPAM, GKE automatically creates subnets in the cluster and manages IP addresses for nodes and Pods. For Services, GKE assigns IP addresses from a [GKE-managed range](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing) by default.

This document is for Operators, Cloud architects, Developers, and Network engineers who provision and configure cloud resources, deploy apps and services, and manage networking for their cloud deployments. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Overview

Traditionally, when you create a GKE cluster, you manually configure a subnet with a primary range for node IP addresses and two secondary ranges for Pod and Service IP addresses. When you manually configure the Pod IP address range, it can be difficult to know the exact size of the IP address range to set. If you don't allocate enough IP addresses, you might restrict cluster scaling and the creation of new Pods. Conversely, if you over-allocate IP addresses, you risk wasting valuable IP address space that other resources could utilize.

GKE auto IPAM resolves this issue and has the following advantages:

**Reduced complexity** : auto IPAM reduces the complexity of IP address allocation by automatically creating a subnet and assigning an appropriate IP address range to that subnet.

**Automatic adjustment of IP address ranges** : when you enable auto IPAM, GKE begins with a smaller IP address range for nodes and Pods. As the cluster scales up or down, GKE dynamically adds or removes additional IP address ranges by using multiple IP address ranges that don't overlap and are defined at the cluster level. This automated approach optimizes IP address health and efficiency throughout the entire GKE cluster lifecycle.

**Simplified IP address management** : auto IPAM reduces the need for you to meticulously plan and manage IP address allocation for your GKE clusters.

Auto IPAM doesn't add or remove IP address ranges that are already assigned to _existing_ node pools when these node pools are scaled up or down. When you create _new_ node pools with insufficient IP address space in the cluster, auto IPAM creates additional subnets and IP address ranges.

You can enable auto IPAM when you create a new cluster. You can also enable or disable auto IPAM for existing clusters.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Restrictions and limitations

When you use auto IPAM in your GKE cluster, understand the following restrictions and limitations:

  * Your cluster must be a VPC-native cluster. Routes-based clusters don't support auto IPAM.
  * You can't use Auto IPAM in a cluster with [Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc).
  * Auto IPAM won't work when you create a new node pool with [multiple network interfaces](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods). To use auto IPAM, you must disable multi-networking capabilities in your node pool.
  * You can't use auto IPAM to create a new subnet in a cluster with [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network). You can use auto IPAM with an _existing_ dual-stack subnet, however auto IPAM will allocate and manage only the IPv4 addresses in your cluster.
  * When you enable auto IPAM, the default maximum node size for any node pool, including the default node pool, is 252 nodes with a CIDR block of /24.
  * By default, GKE allows up to 48 Pods per node in a cluster with auto IPAM.
  * You can't overprovision a Pod CIDR range in clusters that use auto IPAM.

**Caution:** Don't use subnets that are created with auto IPAM (identified with the prefix `gke-auto`) for resources that are _not_ managed by GKE. GKE automatically deletes and recycles these subnets when they are no longer in use by a GKE cluster, which can lead to unexpected service disruptions. You also won't be able to delete your GKE cluster or node pool if the `gke-auto` subnet is used by other resources.

## Create a cluster with auto IPAM

When you create a new cluster and enable auto IPAM, you can either have GKE create a new subnet, or you can specify an existing subnet to use.

### Enable auto IPAM with a new subnet

To create a cluster with auto IPAM and have GKE create a new subnet, use the Google Cloud console or the gcloud CLI. You don't have to specify any IP address ranges when you create a cluster and enable auto IPAM.

### Console

For Autopilot clusters, use the gcloud CLI. For Standard clusters, complete the following steps:

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. From the navigation pane, under **Cluster** , click **Networking**.
  3. In the **Cluster networking** section, under **VPC** , expand the **Network** drop-down list and select a VPC.
  4. In the **IP Management** section, under **Auto-IPAM** , click **Enabled**.
  5. Configure the remaining settings as required.
  6. Click **Create**.



### gcloud
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        **--enable-auto-ipam**
    

Replace the following:

  * `CLUSTER_NAME`: a name for your cluster.
  * `CONTROL_PLANE_LOCATION`: the [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster control plane, such as `us-central1` or `us-central1-a`.



GKE does the following:

  * Creates a new subnet for the cluster.
  * Sets up an initial IP address allocation for the cluster and automatically allocates new node and Pod IP addresses to the new node pool.
  * Monitors the use of subnets and secondary IP address ranges.



### Enable auto IPAM with your own subnet

When you create a cluster and specify an existing subnet, ensure that there are enough secondary IP address ranges available for the cluster.

### Console

For Autopilot clusters, use the gcloud CLI. For Standard clusters, complete the following steps:

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. From the navigation pane, under **Cluster** , click **Networking**.
  3. In the **Cluster networking** section, under **VPC** , expand the **Network** drop-down list and select a VPC.
  4. In the **IP Management** section, under **Auto-IPAM** , click **Enabled**.
  5. In the **VPC** section, expand the **Node subnet** drop-down list, and select a subnet that you want to use.
  6. Configure the remaining settings as required, and then click **Create**.



### gcloud

To create a cluster with auto IPAM and specify your own subnet, follow the instructions in the [Create a cluster in an existing subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#creating_cluster) section and use the `--enable-auto-ipam` flag in the command. For example:
    
    
    gcloud container clusters create CLUSTER_NAME \
       --location=CONTROL_PLANE_LOCATION \
       **--enable-auto-ipam** \
       --network=NETWORK \
       --subnetwork=SUBNET_NAME
    

Replace the following values:

  * `CLUSTER_NAME`: a name for your cluster.
  * `CONTROL_PLANE_LOCATION`: the [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster control plane, such as `us-central1` or `us-central1-a`.
  * `NETWORK`: the name of your cluster's VPC network.
  * `SUBNET_NAME`: the name of an existing subnet.



The subnet's primary IP address range is used for nodes. The subnet must exist in the same region as the one used by the cluster.

## Update an existing cluster

You can enable or disable auto IPAM on an existing cluster.

### Enable auto IPAM

To enable auto IPAM on an existing cluster, use the Google Cloud console or the gcloud CLI.

### Console

For Autopilot clusters, use the gcloud CLI. For Standard clusters, complete the following steps:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Next to the cluster you want to edit, click _more_vert_ **Actions** , then click _edit_ **Edit**.

  3. On the **Cluster details** page, click the **Details** tab.

  4. In the **Cluster Networking** section, click edit **Edit Auto-IPAM**.

  5. In the **Edit Auto-IPAM** dialog, select **Enabled**.

  6. Click **Save Changes**.




### gcloud

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-auto-ipam
    

After you update the cluster, when you create a new node pool without sufficient IP address space, GKE creates and manages a new IP address range in your cluster.

### Disable auto IPAM

To disable auto IPAM on an existing cluster, use the Google Cloud console or the gcloud CLI.

### Console

For Autopilot clusters, use the gcloud CLI. For Standard clusters, complete the following steps:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Next to the cluster you want to edit, click _more_vert_ **Actions** , then click _edit_ **Edit**.

  3. On the **Cluster details** page, click the **Details** tab.

  4. In the **Cluster Networking** section, click edit **Edit Auto-IPAM**.

  5. In the **Edit Auto-IPAM** dialog, select **Disabled**.

  6. Click **Save Changes**.




### gcloud

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --disable-auto-ipam
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the cluster control plane, such as `us-central1` or `us-central1-a`.



After you disable auto IPAM in your cluster:

  * GKE will retain ownership of any subnets and secondary IP address ranges that were created with auto IPAM. These resources are deleted when you delete the GKE cluster.
  * When you create new node pools, GKE automatically assigns the default subnet and the associated secondary IP address range.



## What's next

  * Learn about [IP address allocation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#ip-allocation).
  * Learn how to [create VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#create_a_cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
