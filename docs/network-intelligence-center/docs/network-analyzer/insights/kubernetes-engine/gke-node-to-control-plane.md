---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-node-to-control-plane/
title: GKE node connectivity insights \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:40:56.775294+00:00
---

# GKE node connectivity insights  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-node-to-control-plane/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  GKE node connectivity insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Network Analyzer insights for Google Kubernetes Engine (GKE) node connectivity. For information about all the insight types, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

Network Analyzer detects connectivity issues caused by configurations when a GKE node initiates a connection to the GKE control plane.

## View insights in the Recommender API

To view these insights in the Google Cloud CLI or the Recommender API, use the following insight type:

  * `google.networkanalyzer.container.connectivityInsight`



You need the following permissions:

  * `recommender.networkAnalyzerGkeConnectivityInsights.list`
  * `recommender.networkAnalyzerGkeConnectivityInsights.get`



For more information about using the Recommender API for Network Analyzer insights, see [Use the Recommender CLI and API](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api).

## GKE node to control plane connectivity blocked by routing issue

This insight indicates that the connections from the GKE nodes to the control plane endpoint are blocked by a routing issue.

In private clusters, the control plane's VPC network is connected to your cluster's VPC network with [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). Traffic is routed to the control plane using a [peering subnet route](https://docs.cloud.google.com/vpc/docs/routes#peering-subnet-routes) imported by the VPC Network Peering configuration. In public clusters, traffic is routed to the control plane through the control plane endpoint IP using a route to the default internet gateway.

This insight includes the following information:

  * **GKE cluster:** The name of the GKE cluster.
  * **Control plane endpoint:** The IP address of the endpoint.
  * **Network:** The name of the network where the GKE cluster is configured.



### Related topics

For more information, see [Control plane in private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#the_control_plane_in_private_clusters).

### Recommendations

Go to the GKE cluster details and verify VPC peering. If VPC peering is deleted, create the GKE cluster again.

## GKE node to control plane connectivity: public endpoint blocked by egress firewall

This insight indicates that the connectivity from GKE nodes to the public endpoint is blocked by an egress firewall.

GKE nodes in a public cluster communicate with the control plane through TCP on port 443. This connection is allowed by default by the [implied firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) in your Google Cloud project. The firewall rule that is blocking the connection is listed in the insight details.

### Related topics

For more information, see [Using firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls).

### Recommendations

Create an egress firewall rule that allows TCP traffic on port 443 with a destination filter of the cluster's endpoint. This rule should have a higher priority than the blocking firewall rule.

For increased security this rule can be configured with the network tag of your GKE cluster nodes.

## GKE node to control plane connectivity: private endpoint blocked by egress firewall

This insight indicates that the connectivity from GKE nodes to the private endpoint is blocked by an egress firewall.

GKE nodes in a public cluster communicate with the control plane through TCP on port 443. This connection is allowed by default by the [implied firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) in your Google Cloud project. The firewall rule that is blocking the connection is listed in the insight details.

### Related topics

For more information, see [Using firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls).

### Recommendations

Create an egress firewall rule that allows TCP traffic on port 443 with a destination filter of the cluster's control plane address range. This rule should have a higher priority than the blocking firewall rule.

For increased security this rule can be configured with the network tag of your GKE cluster nodes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
