---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/troubleshooting-hybrid-connectivity/
title: Use case: Troubleshoot hybrid connectivity \u00a0|\u00a0 Network Intelligence Center - Network Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:31.497500+00:00
---

# Use case: Troubleshoot hybrid connectivity  |  Network Intelligence Center - Network Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/troubleshooting-hybrid-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Topology ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use case: Troubleshoot hybrid connectivity

In the following use cases, you're a network administrator supporting a network that includes Interconnect connections, VPN tunnels, or router appliance instances to on-premises networks. You want to view bandwidth to on-premises networks and diagnose bottlenecks and other network problems. You want to learn about the network utilization of the VPN tunnels, VLAN attachments and Interconnect connections, or router appliance instances.

The following use cases demonstrate how Network Topology can help you quickly monitor and identify any issues in your network.

## Interconnect topology details

In this topology, the node `australia-southeast1` is expanded. You can see the associated Interconnect connections and the (not-yet expanded) node collecting VPN tunnels. In addition, one Interconnect connection is expanded, and you can see the associated VLAN attachments. The Interconnect connection is the enclosing entity and it includes VLAN attachments. Because the Interconnect connection and VLAN attachments are regional resources, they appear within the region where they are located. The Interconnect connection has two endpoints, one in the Google Cloud network and the other in the on-premises network.

The following topology shows the hierarchy of the network topology.

[ ![A network topology that shows Interconnect connections and VLAN attachments.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-hybrid.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-hybrid.png) Network Topology example hybrid topology with VLAN attachments (click to enlarge)

### Interconnect bandwidth throughput

In this scenario, you can perform the following actions:

  1. Monitor the utilization of your VLAN attachments and Interconnect connections so that you can make better-informed decisions when planning for network growth.

  2. Select a VLAN attachment. Click the traffic metrics, such as ingress bytes count, and see the traffic bandwidth traversing the VLAN attachment to Google Cloud from the on-premises network.

  3. Hold the pointer over an entity, such as a VLAN attachment. Click the traffic metrics, such as egress bytes count, to view the bandwidth throughput to on-premises networks and diagnose bottlenecks and any other network problems.

  4. For any entity metrics, expand the time series charts to the required time selection to view any bandwidth bottlenecks.




## VPN gateway topology details

In this topology, a node that has a VPN gateway and a VPN tunnel is expanded. Hierarchically in the Network Topology topology interface, within each Cloud VPN gateway, you can see one or more VPN tunnels. The Cloud VPN gateway has two endpoints, one in Google Cloud network and the other in the on-premises network.

The following topology shows the hierarchy of the network topology with VPN tunnels:

[ ![A network topology that shows VPN tunnels.](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-vpn-onprem.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/network-topology/images/use-cases/auditing-vpn-onprem.png) Network Topology example hybrid topology with VPN tunnels (click to enlarge)

### VPN bandwidth throughput

In this topology, the node `us-central1` is expanded, and you can see the associated peering connections, gateways, and VPN tunnels connected to on-premises networks. An on-premises network can refer to any remote network that is outside the Google Cloud domain.

In this scenario, you can perform the following actions:

  1. Monitor the network utilization of the VPN tunnel to make empowered decisions for planning your network growth.

  2. Select the VPN tunnel. Click the traffic metrics, such as ingress bytes count, and see the traffic bandwidth traversing the VPN tunnel to Google Cloud from the on-premises network.

  3. Hold the pointer over the VPN tunnel. Click the traffic metrics, such as egress bytes count, to view the bandwidth throughput to on-premises networks and diagnose bottlenecks and any other network problems.

  4. For any entity metrics, expand the time series charts to the required time selection to view any bandwidth bottlenecks.




## Router appliance details

In a typical topology that includes a router appliance instance connected to an on-premises network, you can see the router appliance instance. Because the router appliance instances are regional resources, they appear within the region where they are located. The router appliance instance has two endpoints, one in the Google Cloud network and the other in the on-premises network.

### Router appliance bandwidth throughput

In this scenario, you can perform the following actions:

  1. Monitor usage of your router appliance instance so that you can make better-informed decisions when planning for network growth.

  2. Select a router appliance instance. Click the traffic metrics, such as ingress bytes count or egress bytes count, and see the traffic bandwidth traversing the router appliance instance between Google Cloud and the on-premises network. Diagnose bottlenecks and any other network problems.

  3. For any entity metrics, expand the time series charts to the required time selection to view any bandwidth bottlenecks.




## What's next

  * [Monitor your networking configuration with Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/how-to/audit-troubleshoot-networking-issues)
  * [Use case: Audit network performance](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/auditing-network-performance)
  * [Troubleshoot Network Topology](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/support/troubleshooting)
  * [Cloud Interconnect quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas)
  * [Cloud VPN quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/vpn/quotas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
