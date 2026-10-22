---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer/
title: Site-to-site data transfer overview \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:18.570221+00:00
---

# Site-to-site data transfer overview  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Site-to-site data transfer overview Stay organized with collections  Save and categorize content based on your preferences. 

Network Connectivity Center (NCC) lets you use Google's network as part of a wide area network (WAN) that includes your external sites. This feature is known as _site-to-site data transfer_.

For example, suppose you have an office in New York, an office in Sydney, and an office in Tokyo. After completing the required configuration, you can use Google's network to move data between all three locations.

To enable this functionality, you use a supported resource to connect each site to Google Cloud. Then you create a NCC _spoke_ to represent each connectivity resource. Each spoke is attached to a central _hub_ , which provides full mesh connectivity between all of the spokes.

Supported connectivity resources include Cloud VPN (HA VPN tunnels), Cloud Interconnect, and Router appliance. Router appliance is a NCC feature that lets you install a third-party network virtual appliance in Google Cloud and use it to exchange routes with Cloud Router.

[ ![Data transfer over Google's network.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/data-transfer.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/data-transfer.svg) Data transfer over Google's network (click to enlarge).

For a comparison of hybrid connectivity products and features, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

For more information about Router appliance, see the [Router appliance overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview). For information about NCC, see the [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

## Considerations

Before using NCC for data transfer, review and consider the following points:

  * Data transfer traffic between sites is best-effort, and there are no bandwidth or latency guarantees.

  * Data transfer is available only in [supported locations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations). For an example of how to configure route advertisements when one of your redundant Cloud Interconnect connections is to an unsupported location, see [Configure on-premises router for mixed advertisements](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/optimal-route-advertisement).

  * When data transfer is enabled for one or more spokes, all connectivity resources associated with these spokes must be part of a single VPC network.

  * If you want to exchange routes between spokes in multiple regions, the VPC network where your spoke resources are located must have its [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-dynamic-routing) set to `global`.

  * For each spoke, ensure that the on-premises router advertises identical routes to the Cloud Router associated with the spoke.

  * In some cases, your network might experience duplicate route advertisements from multiple spokes for the same subnets with the same priority. NCC handles these situations as follows:

    * When different types of resources are being used, VLAN attachments receive more traffic than Cloud VPN connections, which receive more traffic than VMs acting as router appliance instances.
    * When NCC splits traffic across multiple resources of the same type (for example, two VPN tunnels), it uses equal-cost multi-path ([ECMP](https://en.wikipedia.org/wiki/Equal-cost_multi-path_routing)) routing to distribute traffic.
  * **Known issue.** Problems can occur if there are duplicate route advertisements from resources in participating spokes, such as HA VPN tunnels, and from similar resources outside spokes. When duplicate router advertisements exist, then the traffic in participating spokes might use ECMP to distribute traffic across all available next hops. This behavior occurs even if the next hops aren't participating hubs or spokes themselves.

  * [Cloud Router custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes) aren't honored. If you use custom learned routes on BGP sessions associated with this feature, the routes aren't propagated to external sites.

  * See also [Considerations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#considerations) in the main NCC overview.




## Requirements

When using site-to-site data transfer, you must do all of the following:

  * Make sure that all connectivity resources associated with your spokes use a high availability configuration. For more information, see [High availability for spoke resources](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/high-availability).

  * Follow the guidelines described in [ASN requirements for site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/asn-requirements).

  * Make sure that routing prefixes are exclusively advertised within a hub or outside of a hub. If you fail to do this, best-path selection might choose a route that is not associated with a spoke.




## What's next

  * To view a sample topology, see [Sample topology for site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer-topology).
  * To learn more about how NCC enables full mesh connectivity, see [Route exchange with site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/route-exchange).
  * To learn about high availability requirements, see [High availability requirements for spoke resources](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/high-availability).
  * To work through a tutorial, see [Connecting two sites by using Cloud VPN spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/tutorials/connecting-two-offices-with-vpns).
  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
