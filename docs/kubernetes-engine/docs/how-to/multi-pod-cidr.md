---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr/
title: Adding Pod IPv4 address ranges \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:00.842564+00:00
---

# Adding Pod IPv4 address ranges  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Adding Pod IPv4 address ranges Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to configure additional Pod IPv4 address ranges for a VPC-native cluster and how to specify custom Pod IPv4 address ranges for node pools of a VPC-native cluster.

**Note:** The IPv4 addresses that you use for your Pod IP address ranges must come from a valid subnet range. The valid ranges include private IPv4 addresses, such as [RFC 1918](https://tools.ietf.org/html/rfc1918), and privately used public IP addresses. For more information, see [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) and [Prohibited IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#restricted-ranges).

Pod IPv4 address ranges in [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips) always come from subnet secondary IPv4 address ranges. When you create a new cluster, you assign the cluster a default Pod IPv4 address range.

  * For Autopilot and Standard clusters, you can configure a cluster to use additional Pod IPv4 address ranges. GKE uses these additional Pod IPv4 address ranges for Pod IPv4 addresses on nodes created in future node pools.
  * For Standard clusters, you can create node pools that each use a custom subnet secondary IPv4 address range for their Pod IPv4 addresses.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Make sure that you have the [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) Identity and Access Management (IAM) role for the project containing the cluster's subnet. This is required to create new subnet secondary IPv4 address ranges. When using Shared VPC, you'll need to coordinate with the Network Admin for the Shared VPC host project.
  * By default, all new clusters are VPC-native. If you need a new one, [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster). Routes-based clusters don't support additional Pod IPv4 address ranges or node pool custom Pod IPv4 address ranges.
  * Review the Follow-up steps section.



### Create a new subnet secondary IPv4 address range

To create a new subnet secondary IPv4 address range, use either the Google Cloud console or the Google Cloud CLI. Each subnet supports up to 170 secondary IPv4 address ranges. For more information, see [Edit secondary IPv4 ranges](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#edit-secondary) in the VPC documentation.

### Console

  1. Go to the **VPC networks** page in the Google Cloud console.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the **VPC networks** list, select the network that you want to expand.

  3. In the **Subnets** list, select the subnet that you want.

  4. Click **Edit**.

  5. Click **Add IP range**.

  6. For **Subnet range name** , enter the name of the new subnet secondary IPv4 address range. For example, `pod-range-2`.

  7. For **Secondary IP range** , enter the IPv4 address range in CIDR format. For example, `10.2.204.0/22`.

  8. Click **Save**.




### gcloud
    
    
    gcloud compute networks subnets update SUBNET_NAME \
        --region=REGION \
        --add-secondary-ranges=SECONDARY_RANGE_NAME=SECONDARY_RANGE_CIDR
    

Replace the following:

  * `SUBNET_NAME`: The name of the cluster's subnet (the same subnet assigned to the cluster when it was created).
  * `REGION`: The region of the cluster's subnet. The region of the cluster's subnet is the region that contains the GKE cluster.
  * `SECONDARY_RANGE_NAME`: The name of the new subnet secondary IPv4 address range to serve as an additional Pod IPv4 address range for the cluster. For example, `pod-range-2`.
  * `SECONDARY_RANGE_CIDR`: The CIDR to be used by the new subnet secondary IPv4 address range. For example, `10.2.204.0/22`.



You can add two or more new subnet secondary IPv4 address ranges by specifying additional `SECONDARY_RANGE_NAME`=`SECONDARY_RANGE_CIDR` pairs, separated by commas, after the `--add-secondary-ranges` flag.

## Assign additional Pod IPv4 ranges to a cluster

You can assign additional Pod IPv4 address ranges at the cluster level, applicable to new nodes created in new node pools you create in the cluster. To assign additional Pod IPv4 address ranges to a cluster, you must first create a new subnet secondary IPv4 address range.

Adding new Pod IPv4 address ranges to a cluster does not automatically make them available to existing node pools. This behavior occurs because a node pool's IP address range is an immutable setting that's defined when the node pool is created. An existing node pool is only aware of its original range. To use a new Pod IPv4 address range, create a new node pool and assign that new Pod IPv4 address range to it.

Assigning additional Pod IPv4 address ranges to a cluster is supported by:

  * Autopilot clusters running GKE version 1.26 and later
  * Standard clusters




### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Next to the cluster you want to edit, click _more_vert_ **Actions** , then click _edit_ **Edit**.

  3. In the **Networking** section, next to **Cluster Pod IPv4 ranges (additional)** , click _edit_ **Edit**.

  4. In the **Edit additional Cluster Pod IPv4 ranges** dialog, click **Pod secondary CIDR ranges** and select the name(s) of one or more existing subnet secondary IPv4 address ranges in the cluster's subnet. If no additional subnet secondary IPv4 address ranges are available, first Create a new subnet secondary IPv4 address range then repeat these steps.

  5. Click **Save Changes**.




### gcloud

  1. Update your cluster using the `--additional-pod-ipv4-ranges` flag:
         
         gcloud container clusters update CLUSTER_NAME \
             --additional-pod-ipv4-ranges=SECONDARY_RANGE_NAME \
             --location=COMPUTE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: The name of the cluster.
     * `SECONDARY_RANGE_NAME`: The name of one or more existing subnet secondary IPv4 address range(s) in the cluster's subnet, separated by commas. If no subnet secondary IPv4 address ranges are available, Create a new subnet secondary IPv4 address range first.
     * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



### Look up cluster Pod IPv4 ranges

To look up the default Pod IPv4 address range of a cluster and any additional Pod IPv4 address ranges that have been assigned to the cluster, use the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=COMPUTE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: The name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



The output is similar to the following, which includes the cluster's [IPAllocationPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.IPAllocationPolicy):
    
    
    ipAllocationPolicy:
      clusterSecondaryRangeName: cluster-pods
      clusterIpv4CidrBlock: 10.10.0.0/23
      additionalPodRangesConfig:
        podRangeNames:
          - pod-range-1
          - pod-range-2
    

where:

  * `clusterSecondaryRangeName`: The name of the subnet secondary IPv4 address range used as the default Pod IPv4 address range of the cluster, defined when the cluster was created.
  * `clusterIpv4CidrBlock`: The CIDR of the subnet secondary IPv4 address range for Pod IPv4 addresses, defined when the cluster was created.
  * `additionalPodRangesConfig.podRangeNames`: A list of any additional assigned subnet secondary IPv4 address range for Pod IPv4 addresses.

**Note:** The `ipAllocationPolicy` output also includes the deprecated `clusterIpv4Cidr` attribute. Refer to the `clusterIpv4CidrBlock` attribute in the output instead.

## Node pool custom Pod IPv4 address ranges

For Standard clusters running GKE 1.20.4-gke.500 or later, you can assign a custom Pod IPv4 range to a new node pool using one of following methods:

  * Node pool custom Pod IPv4 address range managed by GKE: With this option, you create a new node pool and provide GKE with the information necessary to create a new subnet secondary IPv4 address range in the cluster's subnet. Each new node created in the new node pool is assigned an alias IP address range for its Pod IPv4 addresses, and each alias IP address range comes from the new subnet secondary IPv4 address range that GKE creates. This option can only be used if both the cluster and the VPC network containing the cluster's subnet are in the same project.

  * User-managed node pool custom Pod IPv4 address range: With this option, you create a new node pool where GKE uses an existing subnet secondary IPv4 address range. Each new node created in the new node pool is assigned an alias IP address range for its Pod IPv4 addresses, and each alias IP address range comes from the subnet secondary IPv4 address range that you instruct GKE to use. If your cluster is located in a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) service project, and if your cluster's subnet is located in the host project's Shared VPC network, you must use this option.




A node pool's custom Pod IPv4 address range overrides all Pod IPv4 address ranges defined at the cluster level, including additional Pod IPv4 address ranges assigned to the cluster. Custom Pod IPv4 address ranges assigned to node pools are also called _discontiguous multi-Pod CIDR_.

### Node pool custom Pod IPv4 address range example

The following diagram shows a VPC-native cluster with [user-managed Pod IPv4 address ranges](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#user-managed):

![Adding a node pool to a cluster with an exhausted secondary Pod IP
          address range using discontiguous multi-Pod CIDR](https://docs.cloud.google.com/static/kubernetes-engine/images/multi-pod-cidr.svg)**Diagram:** Node pool custom Pod IPv4 address range example

In the preceding diagram:

  * The maximum number of Pods per node for each node pool in the cluster has been set to `64`. To accommodate a maximum of 64 Pods per node, GKE creates each node with a `/25` alias IP address range, providing `128` Pod IPv4 addresses per node.
  * The cluster's default Pod IPv4 address range is a `/24`. Because each node requires a `/25` for Pod IPv4 addresses, the cluster's default Pod IPv4 address range only supports two nodes.
  * To support additional nodes, a cluster administrator has created an additional node pool, maintaining the `64` maximum Pods per node. The additional node pool uses a custom `/20` Pod IPv4 address range, which supports 32 additional nodes.



### Node pool custom Pod IPv4 address range managed by GKE

To create a node pool with a custom Pod IPv4 address range managed by GKE, use gcloud CLI or GKE API as follows:

### gcloud
    
    
    gcloud container node-pools create POOL_NAME \
      --cluster=CLUSTER_NAME \
      --location=COMPUTE_LOCATION \
      --create-pod-ipv4-range=name=SECONDARY_RANGE_NAME,range=CIDR_OR_NETMASK
    

Replace the following:

  * `POOL_NAME`: The name of the new node pool.
  * `CLUSTER_NAME`: The name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
  * `SECONDARY_RANGE_NAME`: The name of the subnet secondary IPv4 address range that GKE creates. If you omit `name=SECONDARY_RANGE_NAME`, GKE generates the name of the new subnet secondary IPv4 address range automatically.
  * `CIDR_OR_NETMASK`: The Pod IPv4 address range expressed in either CIDR format (for example, `10.12.4.0/20`) or as a subnet mask (for example, `/20`). 
    * If you provide only a subnet mask, GKE attempts to create a new subnet secondary IPv4 address range that doesn't conflict with existing subnet IPv4 address ranges in the VPC network that contains the cluster's subnet.
    * If you omit `range=CIDR_OR_NETMASK`, GKE attempts to create a new `/14` subnet secondary IPv4 address range that doesn't conflict with existing subnet IPv4 address ranges in the VPC network that contains the cluster's subnet.

**Note:** You can use `""` as the value for the `--create-pod-ipv4-range` flag. When you do that, GKE attempts to create a new `/14` subnet secondary IPv4 address range that doesn't conflict with existing subnet IPv4 address ranges in the VPC network that contains the cluster's subnet. GKE generates the name of the new subnet secondary IPv4 address range automatically. For more information, see the [`gcloud container node-pools create` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--create-pod-ipv4-range).

### API
    
    
    "nodePool": {
      "name": "POOL_NAME",
      ...
      "networkConfig": {
        "createPodRange": true,
        "podRange": "SECONDARY_RANGE_NAME",
        "podIpv4CidrBlock": "CIDR_OR_NETMASK"
        }
    }
    

Replace the following:

  * `POOL_NAME`: The name of the new node pool.
  * `SECONDARY_RANGE_NAME`: Optional—the name of the subnet secondary IPv4 address range that GKE creates. If you use `""` as the value for `networkConfig.podRange` or if you omit the `podRange` parameter in the request, GKE generates the name of the new subnet secondary IPv4 address range automatically.
  * `CIDR_OR_NETMASK`: The Pod IPv4 address range expressed in either CIDR format (for example, `10.12.4.0/20`) or as a subnet mask (for example, `/20`). 
    * If you provide only a subnet mask, GKE attempts to create a new subnet secondary IPv4 address range that doesn't conflict with existing subnet IPv4 address ranges in the VPC network that contains the cluster's subnet.
    * If you use `""` as the value for `networkConfig.podIpv4CidrBlock`, GKE attempts create a new `/14` subnet secondary IPv4 address range that doesn't conflict with existing subnet IPv4 address ranges in the VPC network that contains the cluster's subnet.



### User-managed node pool custom Pod IPv4 address range

To create a node pool with a user-managed custom Pod IPv4 address range, use gcloud CLI or GKE API as follows:

### gcloud
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --pod-ipv4-range SECONDARY_RANGE_NAME
    

Replace the following:

  * `POOL_NAME`: The name of the new node pool.
  * `CLUSTER_NAME`: The name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
  * `SECONDARY_RANGE_NAME`: The name of an existing subnet secondary IPv4 address range in the cluster's subnet. If necessary, create a new subnet secondary IPv4 address range first.



### API
    
    
    "nodePool": {
      "name": "POOL_NAME",
      ...
      "networkConfig": {
        "createPodRange": false,
        "podRange": "SECONDARY_RANGE_NAME"
        }
    }
    

Replace the following:

  * `POOL_NAME`: The name of the new node pool.
  * `SECONDARY_RANGE_NAME`: The name of an existing subnet secondary IPv4 address range in the cluster's subnet. If necessary, create a new subnet secondary IPv4 address range first.



### Look up node pool Pod IPv4 ranges

To look up the Pod IPv4 address range of a node pool, use the following command:
    
    
    gcloud container node-pools describe POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=COMPUTE_LOCATION
    

Replace the following:

  * `POOL_NAME`: The name of the node pool.
  * `CLUSTER_NAME`: The name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



The output is similar to the following, which includes the node pool's [NodeNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodeNetworkConfig):
    
    
      networkConfig:
        podRange: podrange
        podIpv4CidrBlock: 192.168.0.0/18
    

where:

  * `podRange`: The name of the subnet secondary IPv4 address range for the node pool's Pod IPv4 addresses.
  * `podIpv4CidrBlock`: The CIDR of the subnet secondary IPv4 address range for the node pool's Pod IPv4 addresses.



If the node pool is using a custom Pod IPv4 address range, the `podRange` and `podIpv4CidrBlock` values are different from the cluster's default Pod IPv4 address range.

## Follow-up steps

After you have assigned additional Pod IPv4 address ranges to a cluster or configured node pool custom Pod IPv4 address ranges, GKE updates the [automatically-created `gke-[cluster-name]-[cluster-hash]-all` VPC firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#cluster-fws) so that its source range includes all Pod IPv4 addresses.

You might also need to:

  * Update your cluster's [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent) configuration. The effective set of non-masquerade CIDRs must include all Pod IPv4 address ranges used by your cluster (and its node pools). For more information, see [Checking `ip-masq-agent` status](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#check-ip-masq-agent) and [Configuring and deploying the `ip-masq-agent`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent).

  * Review your cluster's [`NetworkPolicy`](https://kubernetes.io/docs/concepts/services-networking/network-policies/) configuration. You might need to update `ipBlock` attributes that reference Pod IPv4 address ranges.

  * Troubleshoot connectivity issues using [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) and [Firewall Rules Logging](https://docs.cloud.google.com/firewall/docs/firewall-rules-logging).




## What's next

  * Learn more about [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  * Read the [GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * Learn more about [Optimizing IP address allocation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr).
  * [Learn about GKE IP address utilization insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-ip-utilization).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
