---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/routes-based-cluster/
title: Creating a routes-based cluster \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:01.304322+00:00
---

# Creating a routes-based cluster  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/routes-based-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Creating a routes-based cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows how to create a routes-based cluster in Google Kubernetes Engine (GKE).

## Overview

In GKE, clusters can be distinguished according to the way they route traffic from one Pod to another Pod. A cluster that uses [Google Cloud Routes](https://docs.cloud.google.com/vpc/docs/routes) is called a _routes-based cluster_. A cluster that uses Alias IPs is called a _VPC-native cluster_.

[VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) is the recommended type and is the default for new clusters in GKE versions 1.21.0-gke.1500 and later. To create a routes-based cluster, you must explicitly turn off the VPC-native option.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Create a routes-based cluster

You can create a routes-based cluster by using the gcloud CLI or the Google Cloud console.

### gcloud

To create a routes-based cluster, include the `--no-enable-ip-alias` flag in the cluster creation command:
    
    
    gcloud container clusters create CLUSTER_NAME --no-enable-ip-alias
    

Replace `CLUSTER_NAME` with a name that you choose for your cluster.

### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Enter a name for your cluster.

  3. From the navigation pane, under **Cluster** , click **Networking**.

  4. Under **Advanced networking options** , clear the **Enable VPC-native traffic routing (uses alias IP)** checkbox.

  5. Click **Create**.




### Create a routes-based cluster and select the control plane IP range

By default, clusters with [Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect#clusters-private-service-connect) use the primary subnet range to provision the internal IP address assigned to the control plane endpoint. You can override this default setting by selecting a different subnet range during the cluster creation time only. The following sections show you how to create a cluster with Private Service Connect and override the subnet range.

### gcloud

Create a cluster with Private Service Connect:
    
    
    gcloud container clusters create CLUSTER_NAME --no-enable-ip-alias \
        --private-endpoint-subnetwork=SUBNET_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the GKE cluster.
  * `SUBNET_NAME`: the name of an existing subnet.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



### Console

#### Prerequisite

To assign a subnet to the control plane of a new cluster, you must [add a subnet](https://docs.cloud.google.com/vpc/docs/using-vpc#add-subnets) first.

#### Create a cluster and assign the control plane IP range

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Enter a name for your cluster.

  3. From the navigation pane, under **Cluster** , click **Networking**.

  4. Under **Control Plane Access** , configure access to the [endpoints of the control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#configure-control-plane-access).

  5. In the **Advanced networking options** section, select the **Override control plane's default private endpoint subnet** checkbox.

  6. In the **Private endpoint subnet** list, select your created subnet.

  7. Clear the **Enable VPC-native traffic routing (uses alias IP)** checkbox.

  8. Click **Create**.




## Verify that your cluster uses routes

### gcloud

List your cluster nodes:
    
    
    kubectl get nodes
    

The output shows the names of your nodes:
    
    
    NAME                                 STATUS   ...     AGE    VERSION
    gke-xxx-default-pool-83e239a7-kcg8   Ready    ...     42m    v1.9.7-gke.6
    gke-xxx-default-pool-83e239a7-qm6b   Ready    ...     42m    v1.9.7-gke.6
    gke-xxx-default-pool-83e239a7-wnrq   Ready    ...     42m    1.9.7-gke.6
    

List your routes:
    
    
    gcloud compute routes list
    

In this output, in the **NEXT_HOP** column, look for the name of one of your cluster nodes:
    
    
    NAME                 NETWORK        DEST_RANGE         NEXT_HOP
    ...
    [ROUTE_NAME]         default        10.24.0.0/24       [YOUR_NODE_NAME]
    ...
    

In this output, the route provides a next hop for any packet that is destined for a particular Pod address range.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to inspect.

  3. On the **Cluster details** page, click the **Nodes** tab.

  4. In the **Nodes** section, note the names of any of the nodes.

  5. Go to the **Routes** page in the Google Cloud console.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  6. In the list of routes, in the **Next hop** column, look for the name of one of your cluster nodes. Click the route name for that row.

  7. On the **Route details** page, check the **Next hop** section to verify that the route provides a next hop for any packet destined for a particular Pod address range.




## Pods per node

In a routes-based cluster, each node is allocated a /24 range of IP addresses for Pods. With a /24 range, there are 256 addresses, but the maximum number of Pods per node is 110. By having approximately twice as many available IP addresses as possible Pods, Kubernetes is able to mitigate IP address reuse as Pods are added to and removed from a node.

## Pod address range

A routes-based cluster has a range of IP addresses that are used for Pods and Services. Even though the range is used for both Pods and Services, it is called the _Pod address range_. The last /20 of the Pod address range is used for Services. A /20 range has 212 = 4096 addresses. So 4096 addresses are used for Services, and the rest of the range is used for Pods.

In command output, the Pod address range is called `clusterIpv4Cidr`, and the range of addresses used for Services is called `servicesIpv4Cidr`. For example, the output of `gcloud container clusters describe` includes output similar to the following:
    
    
    clusterIpv4Cidr: 10.96.0.0/16
    ...
    servicesIpv4Cidr: 10.96.240.0/20
    

The Pod address range can be from any RFC 1918 block: `10.0.0.0/8`, `172.16.0.0/12` or `192.168.0.0/16`.

You can customize Pod address range by specifying a CIDR range. For example, you could specify the range `10.96.0.0/16`.

### gcloud
    
    
    gcloud container clusters create CLUSTER_NAME \
        --no-enable-ip-alias \
        --cluster-ipv4-cidr 10.96.0.0/16
    

Replace `CLUSTER_NAME` with a name that you choose for your cluster.

### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Enter a name for your cluster.

  3. From the navigation pane, under **Cluster** , click **Networking**.

  4. Under **Advanced networking options** , clear the **Enable VPC-native traffic routing (uses alias IP)** checkbox.

  5. In the **Pod address range** field, enter `10.96.0.0/16`.

  6. Click **Create**.




### Considerations for cluster sizing

The maximum number of nodes, Pods, and Services for a given GKE cluster is determined by the size of the cluster subnet and the size of the Pod address range. You cannot change the Pod address range size after you create a cluster. When you create a cluster, ensure that you choose a Pod address range large enough to accommodate the cluster's anticipated growth.

The following table explains how to choose address ranges that are sufficient for a cluster that has 900 nodes:

Range | Guidance  
---|---  
Nodes |  Node IP addresses are taken from the primary range of the cluster subnet. Your cluster subnet must be large enough to hold the total number of nodes in your cluster. For example, if you plan to create a 900-node cluster, the cluster subnet must be at least a /22 in size. A /22 range has 210 = 1024 addresses. Subtract the [4 unusable IP addresses](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet), and you get 1020, which is sufficient for the 900 nodes.  
Pod address range |  Each node has a /24 range of IP addresses for Pods. A /24 range has 28 = 256 addresses. Recall that 4096 addresses in the Pod address range are used for Services. The remaining portion of the Pod address range is used for Pods, and must be big enough to hold the number of nodes x 256 addresses. Suppose you plan to create a 900-node cluster. Then you need 900 x 256 = 230,400 addresses for Pods. Now suppose you have a /14 Pod address range. A /14 range has 218 = 262,144 addresses. Subtract the 4096 addresses used for Services, and you get 258,048, which is sufficient for 900 nodes.  
  
## Defaults and limits for range sizes

The following table gives the minimum, maximum, and default sizes for the cluster subnet and the Pod address range.

Range | Default size | Minimum size | Maximum size  
---|---|---|---  
Nodes | /20, which has 212 = 4,096 addresses. Subtract 4 reserved addresses, and you get 4092 addresses for nodes. | /29, which has 23 = 8 addresses. Subtract 4 reserved addresses, and you get 4 addresses for nodes. | /7, which has 225 addresses. This is approximately 33 million addresses for nodes.  
Pod address range | /14, which has 218 = 262,144 addresses. | /19, which has 213 = 8192 addresses. | /9, which has 223 = 8,388,608 addresses.  
  
## Restrictions

  * You cannot migrate a VPC-native cluster to a routes-based cluster.
  * You cannot migrate a routes-based cluster to a VPC-native cluster.
  * Routes-based clusters can only use addresses in the [RFC 1918](https://tools.ietf.org/html/rfc1918) range for private IP addresses. VPC-native clusters have a [larger range](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) of usable addresses.
  * Routes-based clusters don't support dual-stack networking.



## What's next

  * [Creating a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips)
  * [Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster)
  * [Alias IP ranges overview](https://docs.cloud.google.com/vpc/docs/alias-ip)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
