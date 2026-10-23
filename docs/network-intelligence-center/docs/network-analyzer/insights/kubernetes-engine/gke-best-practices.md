---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-best-practices/
title: GKE best practices insights \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:42.764298+00:00
---

# GKE best practices insights  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  GKE best practices insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Network Analyzer insights for Google Kubernetes Engine (GKE) best practices. For information about all the insight types, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

GKE best practices insights validate that best practices are being followed for GKE cluster configurations. An insight from this category suggests areas of improvement and does not indicate active failures. Network Analyzer validates the following conditions:

  * The control plane is able to receive traffic from all IP addresses in the node subnet.
  * Private Google Access is enabled for the private clusters.



## View insights in the Recommender API

To view these insights in the Google Cloud CLI or the Recommender API, use the following insight type:

  * `google.networkanalyzer.container.connectivityInsight`



You need the following permissions:

  * `recommender.networkAnalyzerGkeConnectivityInsights.list`
  * `recommender.networkAnalyzerGkeConnectivityInsights.get`



For more information about using the Recommender API for Network Analyzer insights, see [Use the Recommender CLI and API](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api).

## GKE cluster needs extended authorized range

The subnet used by a GKE cluster has been expanded with authorized networks enabled. However, the cluster's authorized network hasn't been updated to include the expanded IP address range. The nodes created in the extended subnet range won't be able to communicate with the GKE control plane.

This insight includes the following information:

  * **GKE cluster:** The name of the GKE cluster.
  * **Network:** The name of the network where the GKE cluster is configured.
  * **Subnet:** The name of the subnetwork where the GKE cluster is configured.
  * **Subnet range:** The primary IP range of the cluster's primary subnet.



### Related topics

For more information, see [Authorized network limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#limitations).

### Recommendations

Add the cluster's primary subnet range as an authorized network range. For more information, see [Add an authorized network to an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#add).

## Private Google Access disabled on GKE private cluster

Your private GKE cluster is on a subnet that has Private Google Access disabled. Private Google Access provides private nodes and their workloads access to Google Cloud APIs and services over Google's private network.

This insight includes the following information:

  * **GKE cluster:** The name of the GKE cluster.
  * **Network:** The name of the network where the GKE cluster is configured.
  * **Subnet:** The name of the subnetwork where the GKE cluster is configured.



### Related topics

For more information, see [Using Private Google Access in private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#using_in_private_clusters).

### Recommendations

[Enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) on the cluster's primary subnet.

## GKE private cluster without routes to Google APIs and services

Your private GKE cluster uses a VPC network that does not meet the routing requirement for connectivity to Google APIs and services. Network Analyzer generates an insight if your VPC network does not meet the routing requirement. But, Network Analyzer doesn't validate that the destination IP address ranges match the domain names you have chosen in your DNS configuration. For details about this routing requirement, see [Routing options](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-routing) in Configuring Private Google Access.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
