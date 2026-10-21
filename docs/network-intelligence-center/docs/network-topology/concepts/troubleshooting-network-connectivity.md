---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/troubleshooting-network-connectivity/
title: Use case: Troubleshoot network connectivity \u00a0|\u00a0 Network Intelligence Center - Network Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:03.837160+00:00
---

# Use case: Troubleshoot network connectivity  |  Network Intelligence Center - Network Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/troubleshooting-network-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Topology ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use case: Troubleshoot network connectivity

In this use case, you're a network administrator supporting a network that includes several load-balanced applications. You've been alerted of a latency problem and have been told that your organization's mobile application is intermittently slow and timing out. You know that a number of different users are affected, and that there have been no recent application deployments. The issue is likely related to a change in the environment and not the application.

The following use case demonstrates how Network Topology can help you quickly troubleshoot and investigate issues in your deployment.

## Topology details

The deployment spans three Google Cloud regions (`us-central1`, `europe-west1`, and `asia-east1`). All external client requests are served by a single external Application Load Balancer that has multiple backends in each of the three regions. Client requests that come from one of three business regions (Americas, EMEA, and APAC) are served by application instances in the closest Google Cloud region.

The following topology shows the top-level hierarchy for the deployment:

[ ![A network topology that shows three business regions and three Google Cloud regions.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-topology.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-topology.png) Network Topology example topology (click to enlarge)

## Network latency

In this scenario, assume that you have a load balancer named `shopping-site-lb`. You check the latency between external clients and the load balancer to see if the latency between them has changed. You discover that it has and decide to further investigate the load balancer's backends.

  1. You filter the topology to show only the traffic for your external load balancer `shopping-site-lb`.

After you apply the filter, Network Topology shows only the connections related to the load balancer, as shown in the following example.

[ ![Screenshot that shows a filter for the load balancer.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-filter.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-filter.png) Filter for a load balancer (click to enlarge)
  2. Starting with the external clients in Americas, you click the traffic metrics between the Americas business region and the load balancer.

Network Topology shows charts in the details pane. The information includes ingress and egress traffic between your selected entity and the connected entity. For example, Network Topology provides the latest values for queries per second (QPS) and the HTTP request latency.

In the request latency chart, you see values for the 50th, 95th, and 99th percentiles. In this example, assume that all of the latency values are higher than you expected.

  3. To expand the time series charts to 6 weeks, at the top of the details pane, you select **6 weeks**.

[ ![Screenshot that shows the location of the chart zoom.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/troubleshooting-zoom.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/troubleshooting-zoom.png) Expanding the chart1 (click to enlarge)

1The figure is for reference. Its data doesn't reflect the use case. 

You see a significant jump that happened about two hours ago, roughly when the first issues were reported. You're confident that the issue is related to increased latency with the load balancer.

  4. Having a high-level view of the issue, you investigate the load balancer further by going to the **Load balancing** page in the Google Cloud console. You eventually find that an instance in the load balancer's backend service was taking longer than normal to respond. You take that instance out of service, which resolves the issue.




## What's next

  * [Monitor your networking configuration with Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)
  * [Use case: Audit network performance](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/auditing-network-performance)
  * [Troubleshoot Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
