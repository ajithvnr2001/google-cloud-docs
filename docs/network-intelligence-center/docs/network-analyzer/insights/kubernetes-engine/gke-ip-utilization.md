---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-ip-utilization/
title: GKE IP address utilization insights \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:18.101837+00:00
---

# GKE IP address utilization insights  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-ip-utilization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  GKE IP address utilization insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Network Analyzer insights for Google Kubernetes Engine (GKE) IP address utilization. For information about all the insight types, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

## View insights in the Recommender API

To view these insights in the gcloud CLI or the Recommender API, use the following insight type:

  * `google.networkanalyzer.container.ipAddressInsight`



You need the following permissions:

  * `recommender.networkAnalyzerGkeIpAddressInsights.list`
  * `recommender.networkAnalyzerGkeIpAddressInsights.get`



For more information about using the Recommender API for Network Analyzer insights, see [Use the Recommender CLI and API](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api).

## High GKE Pod ranges allocation

This insight indicates that the IP address utilization on the Pod address ranges for a GKE cluster is higher than 80%. The IP address allocation policy for GKE Pods varies depending on whether your cluster was created as a VPC-native cluster or a route-based cluster.

**Note:** If the GKE cluster is in error state, the network insight doesn't trigger even if the Pod IP address utilization is more than 80%.

### Route-based clusters

In GKE, clusters can be distinguished by the way they route traffic from one Pod to another Pod. A cluster that uses [Google Cloud routes](https://docs.cloud.google.com/vpc/docs/routes) is called a _routes-based cluster_. For more information, see [Creating a routes-based cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/routes-based-cluster).

A route-based cluster has a range of IP addresses that are used for Pods and services. Even though the range is used for both Pods and services, it is called the _Pod address range_.

The last `/20` of the Pod address range is used for services. A `/20` range has `212 = 4096` addresses. So `4096` addresses are used for services, and the rest of the range is used for Pods.

Each node of the Pod address range has a `/24` range of IP addresses for the Pods. A `/24` range has `28 = 256` addresses. Recall that `4096` addresses in the Pod address range are used for services. The remaining portion of the Pod address range is used for Pods and must be big enough to hold the number of nodes x 256 addresses.

The allocation ratio for the Pod address range is calculated as follows:

$\frac{\text {GKE node count} \times {256}}{\text {Pod address range size}-{4096}}$ 

For example, you plan to create a `900` node cluster. Then you need `900 x 256 = 230,400` addresses for Pods. Now suppose you have a `/14` Pod address range. A `/14` range has `218 = 262,144` addresses. Subtract the `4096` addresses used for services, and you get `258,048`, which is sufficient for `900` nodes.

### VPC-native clusters

In GKE, clusters can be distinguished by the way they route traffic from one Pod to another Pod. A cluster that uses [alias IP address ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) is called a _VPC-native cluster_. For more information, see [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips).

When you create a node pool in a VPC-native cluster, you select a secondary IP address range to allocate IPs for GKE Pods. Different node pools can use different secondary ranges to allocate Pod IP addresses. For more information, see [multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr). Network Analyzer computes the allocation ratio for each secondary IP address range used to allocate Pod IP addresses for a given cluster. If the overall allocation ratio is greater than 80%, you get a high utilization insight.

The allocation ratio for a single secondary IP address range is calculated as follows:

$\frac{\text {IP addresses from the secondary range allocated to nodes}}{\text {Secondary range size}}$ 

For example, a `/24` secondary Pod range can hold `256` Pods. If there is only `1` node with default `max_pods_per_node`, `110`, and `16` Pods running, the ratio shows 100% (`256/256`) instead of 6.25% (`16/256`) because even though `240` Pod IP addresses are not used, they still belong to this node. Another new node can only be created successfully if there are `256` unused Pod IP addresses.

The overall allocation is calculated as follows:

$\frac{\text {Sum of allocated IPs across all secondary IP address ranges used to allocate Pod IP addresses}}{\text {Sum of secondary IP address range sizes used to allocate Pod IP addresses}}$ 

For example, if the default Pod IP address and the additional Pod IPv4 address range is set to `/22` and there are `2` node pools, one node pool uses the default Pod IP address range and has `3` nodes, while the second node pool uses an additional Pod IP address range and also has `3` nodes, with the default maximum number of Pods set to `110`. Kubernetes assigns a `/24` CIDR range to nodes on the cluster. With `6` nodes and a `/24` CIDR range allocated, there are a total of `256 * 6 = 1536` IP addresses. This is 75% of the total number of IP addresses available in the two Pod IP address ranges (`1024 * 2 = 2048`).

It is important to note that if the secondary IP address is shared among different clusters, the insights show the aggregated total value of all the clusters. To view a single cluster IP range utilization, you can run `gcloud container cluster describe CLUSTER_NAME` to see each secondary IP address utilization status. Replace `CLUSTER_NAME` with the name of the cluster.

**Note:** If you have added an additional cluster Pod with IPv4 address ranges that are not assigned to any node pool, the insight does not consider that range for IP utilization calculation.

### Related topics

  * [Routes based cluster Pod IP address information](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/routes-based-cluster#pod_address_range)
  * [Subnet secondary IP address range for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing_secondary_range_pods)
  * [Multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr)



### Recommendations

  * For route-based clusters, if you need to create additional node pools in this cluster and run out of space, then recreate this cluster with a [larger Pod address range size](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/routes-based-cluster#pod_address_range).
  * For VPC-native clusters, create future node pools with a [larger Pod IP address range](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr#creating_a_node_pool_with_a_new_secondary_pod_ip_range).
  * [Reduce the maximum number of Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr#reducing_the_maximum_number_of_pods).
  * Add additional Pod IPv4 address ranges by using [multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr) for both Standard and Autopilot clusters.



## Allocation of GKE Pod ranges limits autoscaling

This insight indicates that the cluster's Pod IP address ranges don't have enough addresses to support the creation of the maximum number of nodes in all node pools. The Insight details page includes a table that shows the number of currently used Pod IP addresses and the maximum number of Pod IP addresses in each of your GKE cluster's Pod IP address ranges.

Network Analyzer generates this insight when the fully autoscaled IP address utilization value exceeds 100%.

The fully autoscaled IP address utilization value exceeds 100% when the number of Pod IP addresses required to support the maximum number of nodes in the cluster exceeds the number of IP addresses in the cluster's Pod IP address ranges. The maximum number of nodes in the cluster is the sum of the maximum number of nodes in each node pool of the cluster ([maxNodeCount](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#nodepoolautoscaling)).

The fully autoscaled IP address utilization value is calculated using the formula found in High GKE Pod ranges allocation.

### Route-based clusters

This insight is generated when the allocation ratio for the Pod address range is more than 100% and all the node pools are fully autoscaled. The GKE nodes will not be created due to the lack of IP address space.

### VPC-native clusters

This insight is generated if any secondary IP address range used to allocate Pod IP addresses doesn't have enough unallocated IP address space. The insufficient IP address space cannot handle the situation when all the node pools are fully autoscaled.

### Related topics

For more information, see [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking#reserve-ip-space) and [Cluster autoscaler limitation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#limitations).

### Recommendations

  * For route-based clusters, recreate the cluster with a larger Pod address range. Create this cluster as a VPC-native cluster because it is the recommended network mode. See [VPC-native and routes-based clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#vpc-clusters).
  * For VPC-native clusters, add additional Pod ranges to the cluster level by using [multi-pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr#add_more_pod_ranges_autopilot) and enable node auto-provisioning to automate the node scaling with automatic Pod IP address allocation. If you want more control over which Pod IP addresses are used for which node pool, you can create the node pools that use a specific secondary IP address range by using [multi-pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr#add_more_pod_ranges_standard); however, this _only_ applies to Standard clusters.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
