---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-onprem-control-plane/
title: GKE on-premises to control plane connectivity insights \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:50.116979+00:00
---

# GKE on-premises to control plane connectivity insights  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-onprem-control-plane/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  GKE on-premises to control plane connectivity insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Network Analyzer insights for Google Kubernetes Engine (GKE) on-premises to control plane connectivity. For information about all the insight types, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

## View insights in the Recommender API

To view these insights in the Google Cloud CLI or the Recommender API, use the following insight type:

  * `google.networkanalyzer.container.connectivityInsight`



You need the following permissions:

  * `recommender.networkAnalyzerGkeConnectivityInsights.list`
  * `recommender.networkAnalyzerGkeConnectivityInsights.get`



For more information about using the Recommender API for Network Analyzer insights, see [Use the Recommender CLI and API](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api).

## GKE on-premises to control plane connectivity missing return route

This analyzer verifies connectivity between your on-premises network and the GKE control plane.

If this analyzer infers that there is a route in your on-premises network that delivers traffic to the control plane, the analyzer also verifies that the return route exists in the control plane's VPC network. This insight is generated when a Cloud Router advertises the control plane's CIDR range to the on-premises network, but the custom route to the on-premises network is not exported to the GKE cluster's VPC Network Peering. When this happens, the analyzer infers that your on-premises network has a route to the control plane's VPC network. However, the GKE control plane does not have a return route to your on-premises network. If this is your intended network configuration, you can dismiss this insight.

This insight includes the following information:

  * **GKE cluster:** Name of the GKE cluster.
  * **Network:** Name of the network where the GKE cluster is configured.
  * **VPC Network Peering:** The name of the VPC peering configuration that connects your GKE cluster to the control plane.
  * **Associated Cloud Routers:** The list of Cloud Routers that are advertising the control plane's address range.



### Related topics

For more information, see [Connecting to the control plane's private endpoint from on-premises networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#cp-on-prem-routing).

### Recommendations

  * Configure your VPC network to export its custom routes in the peering relationship to the control plane's VPC network.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
