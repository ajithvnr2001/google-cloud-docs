---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connect-vpc-networks/
title: VPC-to-VPC topology that uses a third-party appliance \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:16.778314+00:00
---

# VPC-to-VPC topology that uses a third-party appliance  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connect-vpc-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  VPC-to-VPC topology that uses a third-party appliance Stay organized with collections  Save and categorize content based on your preferences. 

Network Connectivity Center (NCC) lets you use a third-party network virtual appliance to establish connectivity between your Virtual Private Cloud (VPC) networks. To establish this type of connectivity, you use the Router appliance feature. Using Router appliance in this way is supported in all Google Cloud regions.

When you use Router appliance, you install the image of a virtual appliance on a Compute Engine virtual machine (VM) that uses Border Gateway Protocol (BGP). We recommend using an image provided by a [supported NCC partner](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners). For more information about Router appliance, see the [Router appliance overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview).

This page uses a firewall appliance as an example. However, you could use the topology described on this page when setting up an SD-WAN router, a load-balancing appliance, or another type of device.

NCC lets you use a hub-and-spoke architecture for network connectivity. For information about NCC, see the [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview). For more information about Router appliance, see the [Router appliance overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview).

## Sample topology

In the following topology, the router appliance instance hosts a firewall appliance image. The firewall appliance mediates connectivity between two Virtual Private Cloud (VPC) networks.

The VM that hosts the router appliance instance has interfaces in both VPC networks. Each interface has been used to create a Router appliance spoke.

The router appliance instance engages in a total of four Border Gateway Protocol (BGP) peering sessions: In VPC network A, Cloud Router A establishes two sessions with the router appliance instance. In VPC network B, Cloud Router B establishes two sessions with the router appliance instance.

In this scenario, Cloud Router A learns the 192.168.10.0/24 subnet through the firewall Router appliance. This route is installed on the routing table in VPC network A. Similarly, Cloud Router B learns the 10.1.3.0/24 subnet through the firewall Router appliance, and the route is installed on the routing table in VPC network B. Now, VM A and VM B can communicate—subject to the firewall rules that you've defined for your appliance.

Using Router appliance in this way is supported in all Google Cloud regions.

[ ![Manage connectivity between VPC networks.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/firewall-topology.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/firewall-topology.svg) Use a firewall appliance (click to enlarge)**Note:** This topology would also work for a scenario where you want to use an SD-WAN router, a load balancer, or some other type of appliance in two VPC networks.

To set up Router appliance spokes in this way, follow the procedure in [Establish connectivity by using a third-party appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/connect-site-to-cloud). Although "Connect to Google Cloud" describes a site-to-cloud connectivity scenario, the NCC steps are the same as in the preceding diagram.

## What's next

  * To create hubs and spokes, see [Working with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for Router appliance issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
