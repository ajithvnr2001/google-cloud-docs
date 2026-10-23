---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/static-routes-overview/
title: Static routes overview \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:36.967150+00:00
---

# Static routes overview  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/static-routes-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Static routes overview Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how Network Connectivity Center (NCC) supports static routes in VPC spokes.

Before reading this page, ensure that you're familiar with the following resources:

  * [Routes](https://docs.cloud.google.com/vpc/docs/routes) for a general overview of routes in Google Cloud
  * [Static routes](https://docs.cloud.google.com/vpc/docs/static-routes) for an overview of static routes



## Introduction

Unlike subnet routes and dynamic routes, NCC hubs don't exchange static routes. Instead, a hub provides additional configuration flexibility for static routes created in each VPC spoke.

A static route in one VPC spoke can use a next hop in a different VPC spoke if all of the following are true:

  * The static route doesn't use a network tag.
  * The destination range of the static route is an IPv4 range.
  * The specified next hop of the static route is an IPv4 address of an internal passthrough Network Load Balancer.
  * Google Cloud is able to identify a next hop internal passthrough Network Load Balancer at the specified next hop IP address.
  * NCC connectivity requirements have been met.



The additional configuration flexibility for static routes applies only to VPC spokes, not to VPC networks that are purely routing VPC networks (containing only hybrid spokes).

For a comparison to other types of static route next hops, see [Next hop project and network](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hop-loc).

## Identifying the next hop internal passthrough Network Load Balancer

Google Cloud attempts to find an internal passthrough Network Load Balancer for a static route that has a next hop internal passthrough Network Load Balancer IP address by using the following process:

  * If the next hop IP address is in the destination range of a local subnet route: Google Cloud exclusively searches for an internal passthrough Network Load Balancer whose forwarding rule IP address is in the corresponding local subnet. If a next hop internal passthrough Network Load Balancer is found, both the static route and next hop are in the same VPC network.

  * If the next hop IP address is in the destination range of a NCC subnet route (imported from the hub): Google Cloud exclusively searches for an internal passthrough Network Load Balancer whose forwarding rule IP address is in the corresponding subnet of another VPC spoke. If a next hop internal passthrough Network Load Balancer is found, the static route is in one VPC spoke, and the next hop is in a different VPC spoke.

    * For details about how an internal passthrough Network Load Balancer in another VPC spoke can be found, see NCC requirements for connectivity.

    * If you want to use a next hop internal passthrough Network Load Balancer in a routing VPC network (containing hybrid spokes), you must add the routing VPC network to the hub as a VPC spoke. For more limitations relevant to using a routing VPC network as a VPC spoke, see [Considerations for dynamic route exchange with VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#limitations-of-route-exchange).

  * If the next hop IP address is in the destination range of a peering subnet route (imported from another network that is using VPC Network Peering): Google Cloud exclusively searches for an internal passthrough Network Load Balancer whose forwarding rule IP address is in the corresponding subnet of the peered VPC network. If a next hop internal passthrough Network Load Balancer is found, the static route is in one VPC network, and the next hop is in the peered VPC network.




If no next hop internal passthrough Network Load Balancer is found, packets sent to the destination range of the static route are dropped.

### Updates to the next hop internal passthrough Network Load Balancer

Google Cloud continuously attempts to identify a next hop internal passthrough Network Load Balancer. In the following example situations, the next hop for a static route is updated automatically.

  * Replacing the next hop internal passthrough Network Load Balancer: when the next hop for a static route is the IP address of an internal passthrough Network Load Balancer, you can delete the next hop internal passthrough Network Load Balancer without needing to first delete the static route. If Google Cloud finds a replacement internal passthrough Network Load Balancer with the same IP address, Google Cloud switches to the replacement internal passthrough Network Load Balancer next hop.

  * An existing static route without a valid next hop internal passthrough Network Load Balancer can become operational: when a valid next hop internal passthrough Network Load Balancer is found, Google Cloud begins using that internal passthrough Network Load Balancer next hop.

  * Adjusting NCC configuration: moving a VPC spoke to a different spoke group or adjusting export filters can result in a next hop internal passthrough Network Load Balancer no longer being found or a different next hop internal passthrough Network Load Balancer being found and used.




## NCC requirements for connectivity

To find a next hop internal passthrough Network Load Balancer in another VPC spoke, the subnet used by the internal passthrough Network Load Balancer forwarding rule must be accessible in the VPC spoke where the static route is defined. Both the following conditions must be true:

  1. The [hub topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies) must allow exchange of subnet routes that contain the next hop internal passthrough Network Load Balancer.

     * If you use the mesh topology, all VPC spokes are part of the same spoke group. The static route can exist in any VPC spoke, and its next hop internal passthrough Network Load Balancer can exist in any VPC spoke.

     * If you use the star topology, the following requirements apply:

       * If the static route is in a VPC spoke of the edge spoke group, the next hop internal passthrough Network Load Balancer can be in that edge VPC spoke or in any VPC spoke of the center spoke group. The next hop can't be in a different VPC spoke of the edge spoke group.

       * If the static route is in a VPC spoke of the center spoke group, its next hop internal passthrough Network Load Balancer can be in any VPC spoke (in either the edge spoke group or the center spoke group).

  2. The subnet range used by the internal passthrough Network Load Balancer forwarding rule must be exported to the hub. For more information, see [VPC connectivity with export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters).




## Effect of global access

Next hop internal passthrough Network Load Balancers that don't have global access enabled aren't reachable from regions outside of the load balancer's region. If Google Cloud has identified a next hop load balancer at the specified next hop IP address, and NCC connectivity requirements are met, but the load balancer doesn't have global access enabled, Google Cloud drops all packets sent from VM instances, VLAN attachments, and Cloud VPN tunnels in regions different from the load balancer's region.

To change this behavior and make the next hop load balancer reachable from all regions, [enable global access](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access).

## What's next

  * [Configure static routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/configure-static-routes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
