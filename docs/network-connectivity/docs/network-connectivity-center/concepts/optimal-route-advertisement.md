---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/optimal-route-advertisement/
title: Configure external router to avoid unsupported locations \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:34.530667+00:00
---

# Configure external router to avoid unsupported locations  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/optimal-route-advertisement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Configure external router to avoid unsupported locations Stay organized with collections  Save and categorize content based on your preferences. 

The site-to-site data transfer feature lets you connect your external sites by using the Google network. In this context, an external site is any network that you maintain outside of Google Cloud. For example, an external site might be your on-premises network or your network in another cloud service provider. 

Site-to-site data transfer is supported only in [certain locations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations). However, you might need to maintain a connectivity resource in a region that's _unsupported_ for site-to-site data transfer. If you have this type of network topology and you want to conduct site-to-site data transfer, use the configuration described on this page. Otherwise, your site-to-site connectivity might fail.

[Site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer) is part of Network Connectivity Center, which lets you manage your network by using a hub-and-spoke architecture. To use site-to-site data transfer, you establish connectivity to each external network by using a [supported connectivity resource](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#supported-spoke-resources). Afterward, you associate each connectivity resource with a Network Connectivity Center (NCC) spoke, which is attached to an NCC hub. NCC then establishes full mesh connectivity between all external sites associated with your spokes.

**Note:** The guidance on this page is tailored to a sample topology. This topology uses a Dedicated Interconnect resource in an unsupported location. However, the options described on this page apply to any network topology that places a connectivity resource in an unsupported location. The resources could also be VPN tunnels, third-party network virtual appliances, or Partner Interconnect VLAN attachments.

## Sample topology

In this example, an organization uses site-to-site data transfer to connect two on-premises networks:

  * Network A, in India 

  * Network B, in Australia




These networks connect to Google Cloud by using Dedicated Interconnect VLAN attachments and Cloud VPN (HA VPN) tunnels. These resources are located in two regions that are supported for site-to-site data transfer: `asia-south1` and `australia-southeast1`. Both of these VLAN attachments are associated with NCC spokes that have the site-to-site data transfer feature enabled.

This topology also places Compute Engine virtual machines (VM) in `australia-southeast1`. These VMs run services that are accessed regularly by on-premises systems located in network A.

However, this topology has been designed so that the Dedicated Interconnect resources have [99.99% availability](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability). To have 99.99% availability, you must use two pairs of Dedicated Interconnect connections in two regions. Each connection must have its own VLAN attachment.

To satisfy this requirement, the sample topology places a redundant pair of VLAN attachments in a hypothetical unsupported region (`region-unsupported1`). Network A is equidistant between `asia-south1` and `region-unsupported1`. However, the unsupported region is closer to `australia-southeast1` than is `asia-south1`.

This setup poses a potential problem for site-to-site data transfer. Because `region-unsupported1` is closer to `australia-southeast1`, the Cloud Router in `australia-southeast1` sees the resource in `region-unsupported1` as the optimal path to network A. However, because this path is not associated with NCC, Cloud Router does not readvertise the network A prefixes to network B.

[ ![Sample topology that uses a location unsupported for site-to-site data transfer.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/unsupported-location.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/unsupported-location.svg) **Figure 1.** Sample topology that uses a location unsupported for site-to-site data transfer (click to enlarge).

## Configuration options

In the sample scenario, you can control how traffic is routed by configuring the external router for network A. Use one of the options described in the following sections.

Both of these options involve using MED. For help understanding how Cloud Router uses MED, see [Guidance for base priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority).

### Option 1: Optimize for site-to-site data transfer

If site-to-site data transfer is critical, force all traffic to give preference to resources that are associated with NCC spokes. You can effect this behavior by using different MED values for `asia-south1` and `region-unsupported1`.

For example, configure the router for on-premises network A to advertise `10.1/16` by using the following:

  * A MED of `100` to `asia-south1`
  * A MED of `20000` to `region-unsupported1`



In this case, the Cloud Router in `australia-southeast1` sees the advertisement coming from `asia-south1` as the best path. It also readvertises `10.1/16` to on-premises network B.

The advantage of this approach is that it lets you use site-to-site data transfer consistently. The disadvantage is that it increases latency for the network A systems that need to access the VMs in `australia-southeast1`.

### Option 2: Optimize for site-to-cloud traffic

If site-to-site data transfer is not critical, force all traffic to give preference to `region-unsupported1`. You can effect this behavior by using the same MED values for `asia-south1` and `region-unsupported1`.

For example, configure the router for on-premises network A to advertise `10.1/16` by using the following:

  * A MED of `100` to `asia-south1`
  * A MED of `100` to `region-unsupported1`



In this scenario, the Cloud Router in `australia-southeast1` sees the advertisement coming from `region-unsupported1` as the best path because it's geographically closer than `asia-south1`.

Because this path is not associated with NCC, Cloud Router does not readvertise `10.1/16` to on-premises network B.

The advantage of this approach is that, for systems in network A that need to access VMs in `australia-southeast1`, preference is given to the route that has lower latency. The disadvantage of this approach is that it causes site-to-site data transfer to fail.

## What's next

  * To learn more about how NCC enables full mesh connectivity between external sites, see [Route exchange with site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/route-exchange).
  * To view a sample topology, see [Sample topology for site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer-topology).
  * To learn about high availability requirements, see [High availability requirements for spoke resources](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/high-availability).
  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
