---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer-topology/
title: Sample topology for data transfer \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:16.390338+00:00
---

# Sample topology for data transfer  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer-topology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Sample topology for data transfer Stay organized with collections  Save and categorize content based on your preferences. 

The following topology shows a VPC network and two on-premises sites. Each on-premises site connects to Google Cloud by using a Router appliance spoke. The two on-premises sites can use Google's network to exchange data with each other.

[ ![Router appliance topology](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/router-appliance-topology.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/router-appliance-topology.svg) Router appliance topology (click to enlarge)

  1. On-premises `Customer network A` and `Customer network B` are each connected through _customer premises equipment (CPE)_ to a router appliance instance. CPEs typically use a connectivity mechanism, such as an SD-WAN overlay tunnel or an IPsec VPN tunnel, to establish connectivity with the router appliance instance.

Each router appliance instance is located in the Google Cloud region closest to its associated customer network. Both router appliance instances are in a single VPC network. However, the router appliance instances are in different regions. For this reason, the VPC network has its [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-dynamic-routing) set to `global`.

  2. Both router appliance instances are attached as spokes to the Network Connectivity Center (NCC) hub. Because `Customer network A` and `Customer network B` need to send data to each other, both spokes have the site-to-site data transfer field enabled.

_You can use site-to-site data transfer only in supported locations._ For more information, see [Locations supported for data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations).

  3. In each region, a router appliance instance establishes Border Gateway Protocol (BGP) peering with the appropriate Cloud Router. Each Cloud Router receives and advertises route prefixes from the corresponding on-premises location.

  4. The Cloud Routers dynamically exchange all received routes with each other. This configuration provides end-to-end dynamic route exchange and data plane connectivity between `Customer network A` and `Customer network B`.

**Important:** For Cloud Routers in different regions to exchange routes with each other, you must enable global dynamic routing mode in your VPC network. For more information, see [Dynamic routing](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).



## What's next

  * To learn about high availability requirements, see [High availability requirements for spoke resources](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/high-availability).
  * To learn about requirements for assigning ASNs, see [ASN requirements for site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/asn-requirements).
  * To create hubs and spokes, see [Working with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To work through a tutorial, see [Connecting two sites by using Cloud VPN spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/tutorials/connecting-two-offices-with-vpns).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
