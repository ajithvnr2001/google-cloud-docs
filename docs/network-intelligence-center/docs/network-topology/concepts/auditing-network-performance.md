---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/auditing-network-performance/
title: Use case: Audit network performance \u00a0|\u00a0 Network Intelligence Center - Network Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:18.406438+00:00
---

# Use case: Audit network performance  |  Network Intelligence Center - Network Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/auditing-network-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Topology ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use case: Audit network performance

Assume that you're a network administrator who supports a network that includes several load-balanced applications. You've been asked to audit the network configurations that support those applications to ensure that the configurations are consistent with the expected state of your network. By doing this audit, you can ensure that customers are getting the lowest possible latency to your applications.

The following use case demonstrates how Network Topology can help you check your existing configurations. For example, you can check that all client requests are being served by application instances from the Google Cloud region that's closest to the client. You can also ensure that cross-region traffic is low because that traffic comes from databases that replicate data globally.

## Topology overview

The deployment spans three Google Cloud regions (`us-central1`, `europe-west1`, and `asia-east1`). All external client requests are served by a single external Application Load Balancer that has multiple backends in each of the three regions. Client requests that come from one of three business regions (Americas, EMEA, and APAC) are served by application instances in the closest Google Cloud region.

The following graph shows the top-level hierarchy for the deployment.

[ ![A network topology that shows three business regions and three Google Cloud regions.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-topology.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-topology.png) Network Topology example topology (click to enlarge)

### Resources and traffic paths

In this example, the project contains the following Google Cloud resources:

  * 1 HTTPS load balancer

  * 4 backend services: `browse`, `shopping_cart`, `checkout`, and `feeds`

  * 12 instance groups (which are the load balancer's backends)

There is one instance group for each backend service in each of the three regions.

  * 3 database instances, one in each region




You expect that traffic from certain countries goes to the following locations:

  * Traffic from countries in the `Americas` business region goes to backends in the `us-central1` region. For example, traffic from an external client in Canada travels through the load balancer to the `checkout` backend in the `us-central1` region.
  * Traffic from countries in the `EMEA` business region goes to backends in the `europe-west1` region. For example, traffic from an external client in Poland travels through the load balancer to the `checkout` backend in the `europe-west1` region.
  * Traffic from countries in the `APAC` business region goes to backends in the `asia-east1` region. For example, traffic from an external client in Japan travels through the load balancer to the `checkout` backend in the `asia-east1` region.
  * Traffic to a database instance comes from a backend in the same region. For example, the backends in `asia-east1` send data only to the database instance in `asia-east1`.
  * Cross-region traffic is limited to database replication. For example, traffic between `us-central1` and `europe-west1` travels only between database instances in those regions.



## Unexpected traffic flow

In this scenario, you discover that traffic from the `EMEA` business region is now going to two different Google Cloud regions, `us-central1` and `europe-west1`. By using Network Topology, you discover that one of the backends is overutilized.

  1. You want to check that external traffic that is going through the load balancer eventually goes to the correct Google Cloud region. You filter the graph to show only the traffic for your external load balancer `shopping-site-lb`.

After you apply the filter, Network Topology shows only the connections related to the load balancer, as shown in the following example.

[ ![Screenshot that shows a filter for the load balancer.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-filter.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-filter.png) Filter for a load balancer (click to enlarge)
  2. You hold the pointer over each business region to highlight the communication to that region.

When you hold the pointer over **Americas** and **APAC** , you see traffic going to the nearest Google Cloud region: `us-central1` and `asia- east1` respectively. However, when you hold the pointer over **EMEA** , you see traffic going to `us-central1` and `europe-west1`. Ideally, to reduce latency, all traffic from EMEA should go to `europe-west1`.

  3. Next, you click **EMEA** to study the throughput between it and the Google Cloud regions. Network Topology overlays bandwidth values on each connection. You see that about 0.58 bytes per second is going to `us-central1` and 29.9 kilobytes per second is going to `europe-west1`. You know that most of the traffic is being directed as you would expect, but some traffic is flowing to `us-central1`.

[ ![Screenshot that shows the throughput between the load balancer and
         different regions.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-bandwidth.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-bandwidth.png) Overlaid bandwidth values1 (click to enlarge)

1The figure is for reference. Its data doesn't reflect the use case. 

  4. To investigate further, you expand `us-central1` to view where traffic is going. Because there's only one network with a single subnet in that region, Network Topology doesn't show those levels of the hierarchy and skips to the instance groups.

You see that traffic is going to an instance group that's associated with the load balancer's backend service. Because it's a relatively small amount of traffic going to `europe-west1`, it's possible that resources in `europe-west1` are overutilized and causing traffic to overflow to `us-central1`.

[ ![Screenshot that shows the traffic path between EMEA and us-central1.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-traffic.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-traffic.png) Traffic path1 (click to enlarge)

1The figure is for reference. Its data doesn't reflect the use case. 

  5. To confirm your conclusion, you expand the `europe-west1` region until you reach the instance that is associated with the same load balancer's backend service. Network Topology shows time-series charts in the details pane for the instance.

In the chart, you notice that the CPU utilization rate is at 81% for the instance. The threshold for this example is 80%, indicating that the instance is oversubscribed. You resolve this issue by scaling up the instance group so that traffic returns to the ideal flow.

[ ![Screenshot that shows time-series charts for an instance.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-chart.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-chart.png) Time-series chart for an instance1 (click to enlarge)

1The figure is for reference. Its data doesn't reflect the use case. 




## Inter-region traffic

In the following section, you check that internal traffic between regions is limited to only database instance traffic.

  1. To focus on internal traffic, in the **Topology configuration** list, you select only the **Instances** and **Cloud NAT gateways** checkboxes. Because you are only viewing traffic within your application, you don't need to see external clients and external load balancer traffic.

[ ![Screenshot that shows external clients and load balancers
         cleared from the entities pane.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-internalonly.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-internalonly.png) Showing internal-only traffic (click to enlarge)
  2. You expand the `asia-east1` region, and you see five instance groups. They are not aggregated by network, subnet, or zone because they are all in the same network, subnet, and so on.

You notice that only one instance group (`db-group-asia`) contains a path for inter-region traffic. All other instance groups are communicating within the region.

You continue to expand the `db-group-asia` group until you reach the base entity. In this scenario, the base entity is a virtual machine (VM) instance (`db-instance-asia`) that acts as a database server. It's communicating with other regions to replicate data, which is what you expected, so no further investigations are required. ̦ [ ![Screenshot that shows a database instance connecting to other
         regions.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-dbtraffic.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-dbtraffic.png) Inter-region traffic1 (click to enlarge)

1The figure is for reference. Its data doesn't reflect the use case. 




## What's next

  * [Monitor your networking configuration with Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)
  * [Use case: Troubleshoot network connectivity](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/troubleshooting-network-connectivity)
  * [Troubleshoot Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
