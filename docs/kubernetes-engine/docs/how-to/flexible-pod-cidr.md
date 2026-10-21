---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr/
title: Configure maximum Pods per node \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:03.108828+00:00
---

# Configure maximum Pods per node  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure maximum Pods per node Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to optimize cluster resources to ensure sufficient scheduling capacity for your Pods by configuring the maximum number of Pods per node in Standard clusters on Google Kubernetes Engine (GKE). This page helps you understand how the relationship between Pods, CIDR block sizes, and the number of nodes influences how GKE schedules Pods and allocates IP addresses within your cluster. This page also includes details about restrictions and default values for maximum Pods per node.

This page helps Operators, Cloud architects, Developers, and Network engineers who provision and configure cloud resources, deploy apps and services, and manage networking for their cloud deployments. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, familiarize yourself with [when to use GKE Standard instead of Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode#when-use-standard) clusters, and the [Kubernetes networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Restrictions

  * You can only configure the maximum Pods per node in [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  * Node creation is limited by the number of available addresses in the Pod address range. Check the [IP address range planning table](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#defaults_limits) for the default, minimum, and maximum Pod address range sizes. You can also add additional Pod IP addresses using [discontiguous multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).
  * Each cluster needs to create kube-system Pods, such as [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/), in the `kube-system` namespace. Remember to account for both your workload Pods and System Pods when you reduce the maximum number of Pods per node. To list System Pods in your cluster, run the following command:
        
        kubectl get pods --namespace kube-system
        




## Configure the maximum Pods per node

You can configure the maximum number of Pods per node in a Standard cluster when creating a cluster or when creating a node pool. You cannot change this setting after the cluster or node pool is created. For Autopilot clusters, the maximum number of nodes is pre-configured and immutable.

However, if you run out of Pod IP addresses, you can create additional Pod IP address ranges using [discontiguous multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).

You can set the size of the Pod address range when creating a cluster by using the gcloud CLI or the Google Cloud console.

### gcloud

To set the default maximum Pods per node using the gcloud CLI, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --enable-ip-alias \
        --cluster-ipv4-cidr=10.0.0.0/21 \
        --services-ipv4-cidr=10.4.0.0/19 \
        --create-subnetwork=name='SUBNET_NAME',range=10.5.32.0/27 \
        --default-max-pods-per-node=MAXIMUM_PODS \
        --location=COMPUTE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new cluster.
  * `SUBNET_NAME`: the name of the new subnetwork for your cluster.
  * `MAXIMUM_PODS`: the default maximum number of Pods per node for your cluster, can be configured up to `512`. If omitted, Kubernetes assigns the default value of `110`.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the new cluster.



### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Configure your new cluster.

  3. From the navigation pane, under **Cluster** , click **Networking**.

  4. Ensure the **Enable VPC-native traffic routing (uses alias IP)** checkbox is selected.

  5. From the navigation pane, under **Node pools** , click **Networking**.

  6. Set the **Maximum pods per node** field to `110`. GKE uses this value to tune the size of the IP address range assigned to nodes.

  7. Click **Create**.




When you configure the maximum number of Pods per node for the cluster, Kubernetes uses this value to allocate a CIDR range for the nodes. You can calculate the maximum number of nodes on the cluster based on the cluster's secondary IP address range for Pods and the allocated CIDR range for the node.

For example, if you set the default maximum number of Pods to `110` and the secondary IP address range for Pods to `/21`, Kubernetes assigns a `/24` CIDR range to nodes on the cluster. The CIDR range assignment allows a maximum of `2(24-21) = 23 = 8` nodes on the cluster.

Similarly, if you set the default maximum Pods to `8` and the cluster's secondary IP address range for Pods to `/21`, Kubernetes assigns a `/28` CIDR range to nodes. The CIDR range assignment allows a maximum of `2(28-21) = 27 = 128` nodes on the cluster.

## Configure the maximum number of Pods in a new node pool for an existing cluster

You can also specify the maximum number of Pods per node when creating a node pool in an existing Standard cluster. Creating a new node pool lets you optimize IP address allocation, even in existing clusters where there is no configured default maximum number of Pods per node at the cluster level.

Setting the maximum number of Pods at the node pool level overrides the cluster-level default maximum. If you don't configure a maximum number of Pods per node when you create the node pool, the cluster-level maximum applies.

### gcloud
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --max-pods-per-node=MAXIMUM_PODS
    

Replace the following:

  * `POOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of the cluster in which you want to create the node pool.
  * `MAXIMUM_PODS`: the maximum number of Pods in the node pool.



### Console

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_ **Create user-managed node pool**.

  5. From the navigation pane, click **Networking**.

  6. In the **Maximum pods per node** field, enter a value. GKE uses this value to tune the size of the IP address range assigned to nodes.




## Pod secondary ranges and maximum Pods per node

When you configure the maximum number of Pods per node, you are indirectly affecting the required size of the Pod secondary range. GKE requires a minimum CIDR block of /24 per node pool. Attempting to specify a Pod secondary range smaller than /24 when creating a node pool results in the following error:
    
    
    Pod secondary range 'Pod' must have a CIDR block of at least /24
    

If you need a smaller range than /24 for your overall cluster, you can specify this at the cluster level using the --cluster-ipv4-cidr argument with Google Cloud CLI. For more information, see [Creating a cluster with a specific CIDR range](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#cluster_sizing). You can also use [discontiguous multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr) to add more Pod IP address ranges to the cluster.

Each cluster needs to create kube-system Pods, such as kube-proxy, in the kube-system namespace. Remember to account for both your workload Pods and System Pods when you configure the maximum number of Pods per node.

## About default maximum Pods per node

By default, GKE allows up to 110 Pods per node on Standard clusters, however Standard clusters can be configured to allow up to 512 Pods per node. Autopilot clusters, based on the expected workload Pod density, choose the maximum Pods per node from a range between 8 and 256. Kubernetes assigns each node a range of IP addresses, [a CIDR block](https://tools.ietf.org/html/rfc1918), so that each Pod can have a unique IP address. The size of the CIDR block corresponds to the maximum number of Pods per node.

### Pod CIDR ranges in Standard clusters

With the default maximum of 110 Pods per node for Standard clusters, Kubernetes assigns a /24 CIDR block (256 addresses) to each of the nodes. By having more than twice as many available IP addresses as the maximum number of Pods that can be created on a node, Kubernetes can reduce IP address reuse as Pods are added to and removed from a node.

Although having 512 Pods per node is a hard limit, you can reduce the number of Pods on a node. The size of the CIDR block assigned to a node depends on the maximum Pods per node value. The block always contains at least twice as many addresses as the maximum number of Pods per node.

The following table lists the size of the CIDR block and the corresponding number of available IP addresses that Kubernetes assigns to nodes based on the maximum Pods per node:

Maximum Pods per Node | CIDR Range per Node | Number of IP addresses  
---|---|---  
8 | /28 | 16  
9 – 16 | /27 | 32  
17 – 32 | /26 | 64  
33 – 64 | /25 | 128  
65 – 128 | /24 | 256  
129 – 256 | /23 | 512  
257 – 512 | /22 | 1024  
  
### Cluster sizing considerations for secondary IP address range for Pods

When you create a cluster, the size of the secondary IP address range for Pods is immutable. You must carefully plan the size of this range to accommodate your current and future workload needs. Insufficient IP address space for Pods can lead to scheduling failures and prevent your cluster from scaling.

If you are unsure about the required size, we recommend starting with a larger range, such as `/21`, which is the default for clusters created with the Google Cloud CLI. A larger range provides enough IP addresses for a moderately sized cluster and gives you flexibility for future growth. If you run out of Pod IP addresses, you can use [discontiguous multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr) to add more Pod IP address ranges.

However, if you are working in an environment with constrained IP address space, you might need to use a smaller range. In such cases, you can reduce the maximum number of Pods per node. Reducing the maximum number of Pods per node allows each node to have a smaller Pod CIDR range, which in turn allows more nodes to fit within a smaller Pod secondary range for the entire cluster. The configuration is a trade-off between Pod density per node and the total number of nodes in your cluster.

To calculate the maximum number of Pods that your cluster can support, you provide input values for the number of Pods per node and the CIDR ranges. GKE uses these inputs to determine the size of the address ranges for your nodes and Pods.

**User-specified values**

These are the values you provide when creating a cluster or node pool.

  * `Q`: The maximum number of Pods per node.
  * `DS`: The prefix length of the Pod subnet. For example, for a CIDR range of `/17`, the prefix length is `17`.
  * `S`: The prefix length of the primary subnet. For example, for a CIDR range of `/24`, the prefix length is `24`.



**Calculated values**

GKE calculates the following values based on your inputs.

  * `M`: The netmask size for each node's Pod range.

$$ M = 31 - \lceil{log_2(Q)}\rceil $$ 

Use the ceiling function (\\( \lceil \rceil \\)) to round up to the nearest integer.

  * `HM`: The number of host bits for the node's Pod range netmask.

$$ HM = 32 - M $$ 

  * `HD`: The number of host bits for the selected CIDR Pod subnet netmask.

$$ HD = 32 - DS $$ 

  * `MN`: The maximum number of nodes that can be supported by the Pod subnet.

$$ MN = 2^{(HD - HM)} $$ 

  * `MP`: The maximum number of Pods that can be supported by the Pod subnet.

$$ MP = MN * Q $$ 

  * `N`: The number of usable IP addresses in the primary range.

$$ N = 2^{(32 - S)} - 4 $$ 

**Note:** The first two and last two IP addresses of a primary IP address range are reserved by Google Cloud.



**Important notes:**

  * All IP addresses in the secondary range are usable for Pods.
  * These calculations provide the _theoretical_ maximums. Real-world performance can be affected by other factors.



**Example:**

Suppose you are creating a GKE Autopilot cluster with the following:

  * A Pod subnet CIDR of `/17` (`DS` = 17).
  * A maximum of 32 Pods per node (`Q` = 32).



Calculate the maximum number of Pods:

  1. \\( M = 31 - \lceil{log_2(32)}\rceil = 26 \\)
  2. \\( HM = 32 - 26 = 6 \\)
  3. \\( HD = 32 - 17 = 15 \\)
  4. \\( MN = 2^{(15 - 6)} = 512 \\)
  5. \\( MP = 512 * 32 = 16384 \\)



This cluster can support a maximum of 512 nodes and 16,384 Pods.

### Reduce the maximum number of Pods

Reducing the maximum number of Pods per node allows the cluster to have more nodes, since each node requires a smaller part of the total IP address space. Alternatively, you could support the same number of nodes in the cluster by specifying a smaller IP address space for Pods at cluster creation time.

Reducing the maximum number of Pods per node also lets you create smaller clusters that require fewer IP addresses. For example, with eight Pods per node, each node is granted a /28 CIDR. These IP address ranges plus the [subnet and secondary ranges](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing) that you define determine the number of IP addresses required to create a cluster successfully.

You can configure the maximum number of Pods per node at cluster creation time and at [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) creation time.

## What's next

  * Learn how to create [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) clusters.
  * Learn how to add [additional Pod IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr) to clusters.
  * Learn about [IP address management strategies when migrating to GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies).
  * Learn about [GKE IP address utilization insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-ip-utilization).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
