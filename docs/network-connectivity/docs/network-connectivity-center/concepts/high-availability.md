---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/high-availability/
title: High availability requirements for spoke resources \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:35.783111+00:00
---

# High availability requirements for spoke resources  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/high-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  High availability requirements for spoke resources Stay organized with collections  Save and categorize content based on your preferences. 

For Network Connectivity Center (NCC) to properly enable site-to-site data transfer, you must configure spoke resources in high availability configurations. If you don't, sites might be unable to pass traffic to one another.

Each resource type has different requirements for high availability, as described in the following sections.

## High availability for Cloud Interconnect

For site-to-site data transfer to work correctly with Cloud Interconnect resources, you must configure multiple Cloud Interconnect connections, each in a separate edge availability domain. As a cost-effective but less optimal option, you can replace one of the Cloud Interconnect connections with a pair of HA VPN tunnels. One Cloud Interconnect connection spoke and a pair of HA VPN tunnels as a Cloud VPN spoke are supported in a high availability configuration. The following table shows the supported configurations:

Deployment option | Minimum topology requirement | Performance profile  
---|---|---  
Cloud Interconnect (Recommended) | Provision at least two Cloud Interconnect connections, with each connection residing in a different edge availability domain within the metropolitan area | Highest throughput, maximum reliability  
Cloud Interconnect connections paired with HA VPN | A single Cloud Interconnect connection as a spoke paired with a HA VPN spoke | Lower standby throughput  
  
For detailed information about how to configure Cloud Interconnect resources for high availability, see the following documentation:

  * [Redundancy and SLA for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#redundancy)
  * [Establish 99.99% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability)
  * [Redundancy and SLA for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#redundancy)
  * [Establish 99.99% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability)
  * [Create redundant Cloud Interconnect connections with sufficient capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#capacity)



## High availability for Cloud VPN

For site-to-site data transfer to work correctly with Cloud VPN resources, you must configure multiple HA VPN gateway interfaces and tunnels to achieve a 99.99% SLO. For guidance, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn).

## High availability for Router appliance

For site-to-site data transfer to work correctly with router appliance instances attached to a spoke, you must do the following:

If you place all your router appliance instances in a single spoke, use equal-cost multipath (ECMP) to advertise the same set of prefixes from two router appliance instances. To advertise different prefixes for each spoke, add each router appliance instance to a different spoke.

You can't create a cross-region configuration in a single spoke.

ECMP is the result of advertising the same prefix or prefixes, with the same MEDs and AS path as applicable, from two or more router appliance instances. The guidance about [route selection in VPC networks](https://docs.cloud.google.com/vpc/docs/routes#routeselection) applies to router appliance instances as it does to other Google Cloud resources.

For detailed information about how to configure router appliance instances for high availability, see the [requirements for 99.9% availability](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview#ra-availability).

## What's next

  * To view a sample topology, see [Sample topology for site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer-topology).
  * To learn more about how NCC enables full mesh connectivity, see [Route exchange with site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/route-exchange).
  * To work through a tutorial, see [Connect two sites by using Cloud VPN spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/tutorials/connecting-two-offices-with-vpns).
  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
