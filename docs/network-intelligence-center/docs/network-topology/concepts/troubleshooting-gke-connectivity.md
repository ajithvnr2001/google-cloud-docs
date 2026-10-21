---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/troubleshooting-gke-connectivity/
title: Use case: Troubleshoot GKE connectivity \u00a0|\u00a0 Network Intelligence Center - Network Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:04.301245+00:00
---

# Use case: Troubleshoot GKE connectivity  |  Network Intelligence Center - Network Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/troubleshooting-gke-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Topology ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use case: Troubleshoot GKE connectivity

In this use case, you're a network administrator supporting a network that includes several GKE namespaces. You've been alerted of a latency problem and have been told that your organization's mobile application is intermittently slow and timing out. You know that a number of different users are affected, and that there have been no recent application deployments. The issue is likely related to a specific GKE cluster.

The following use case demonstrates how Network Topology can help you quickly troubleshoot and investigate issues in your GKE deployment.

## Topology details

The deployment spans three Google Cloud regions (`us-central1`, `europe-west1`, and `asia-east1`). All external client requests are served by the three clusters within the three regions with multiple namespaces. Client requests that come from one of three business regions (Americas, EMEA, and APAC) are served by application instances in the closest Google Cloud region.

The following topology shows the top-level hierarchy for the deployment:

[ ![A network topology that shows three Google Cloud regions.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/gke-auditing-topology.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/gke-auditing-topology.png) Network Topology GKE view example topology (click to enlarge)

## Network latency

In this scenario, assume that you have a GKE cluster named online-boutique. You check the latency between external clients and the GKE cluster to see if the latency between them has changed. You discover that it has changed and decide to further investigate the cluster's nodes.

  1. You filter the topology to show only the traffic for your cluster `online-boutique`.

In the **Filter** section, you can add a filter to select nodes and its peers. This section is available only for metric views and not for the insights views. Click **Add filter** and select the type of node and the node.

After you apply the filter, Network Topology shows only the connections related to the cluster, as shown in the following example.

  2. Starting with the external clients in Americas, you click the traffic metrics between the Americas business region and the GKE cluster. Network Topology shows charts in the details pane. The information includes ingress and egress traffic between your selected entity and the connected entity. For example, Network Topology provides the latest values for queries per second (QPS) and the HTTP request latency. In the request latency chart, you see values for the 50th, 95th, and 99th percentiles. In this example, assume that all of the latency values are higher than you expected.

  3. To expand the time series charts to 6 weeks, at the top of the details pane, you select **6 weeks**.

You see a significant jump that happened about two hours ago, roughly when the first issues were reported. You're confident that the issue is related to increased latency with a GKE Pod.

**Note:** Traffic details from external entities are only available till the GKE cluster level. Network Topology does not show the traffic to the nodes within a GKE cluster.
  4. Having a high-level view of the issue, you investigate the GKE nodes further. For more information about troubleshooting GKE nodes, see [Troubleshooting GKE connectivity issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#ConnectivityIssues).




## What's next

  * [Monitor your networking configuration with Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)
  * [Use case: Audit network performance](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/auditing-network-performance)
  * [Troubleshoot Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/support/troubleshooting)
  * [Cloud Interconnect quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas)
  * [Cloud VPN quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/vpn/quotas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
