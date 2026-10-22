---
url: https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview/
title: Internal passthrough Network Load Balancers as next hops \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:27.954366+00:00
---

# Internal passthrough Network Load Balancers as next hops  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Internal passthrough Network Load Balancers as next hops Stay organized with collections  Save and categorize content based on your preferences. 

An internal passthrough Network Load Balancer is a regional load balancer that lets you to run and scale your services behind an internal IP address. You can use an internal passthrough Network Load Balancer as the next hop to which packets are forwarded along the path to their final destination. To do this, you set the load balancer as the _next hop_ in a [static route](https://docs.cloud.google.com/vpc/docs/static-routes).

Before reviewing the information on this page, you should already be familiar with concepts from the following:

  * [Routes overview](https://docs.cloud.google.com/vpc/docs/routes)
  * [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal)



An internal passthrough Network Load Balancer next hop is useful in the following cases:

  * To load balance traffic across multiple VMs that are functioning as gateway or router VMs.

  * To use gateway [virtual appliances](https://wikipedia.org/wiki/Virtual_appliance) as your next hop for a default route. With this configuration, virtual machine (VM) instances in your Virtual Private Cloud (VPC) network send traffic to the internet through a set of load-balanced virtual gateway VMs.

  * To send traffic through multiple load balancers in two or more directions by using the same set of multi-NIC gateway or router VMs as backends. To do this, you create a load balancer and use it as the next hop for a static route in _each_ VPC network. Each internal passthrough Network Load Balancer operates within a single VPC network, distributing traffic to the network interfaces of backend VMs in that network.




## Architecture

In the following diagram, a VM instance group of router VMs serves as the backend for two different load balancers. The first internal passthrough Network Load Balancer sends packets to `nic0` of the backend VMs, and the second internal passthrough Network Load Balancer sends packets to `nic1` on the same backends.

[ ![Load balancing to multiple NICs.](https://docs.cloud.google.com/static/load-balancing/images/multi-nic.svg)](https://docs.cloud.google.com/static/load-balancing/images/multi-nic.svg) Load balancing to multiple NICs (click to enlarge).

## Benefits of using your internal passthrough Network Load Balancer as a next hop

When the load balancer is a next hop for a static route, no special configuration is needed within the guest operating systems of the client VMs in the VPC network where the route is defined. Client VMs send packets to the load balancer's backends through VPC network routing, in a [bump-in-the-wire](https://wikipedia.org/wiki/Bump-in-the-wire) fashion.

Using an internal passthrough Network Load Balancer as a next hop for a static route provides the same benefits as a standalone internal passthrough Network Load Balancer. The load balancer's health check ensures that new connections are routed to healthy backend VMs. By using a managed instance group as a backend, you can configure autoscaling to grow or shrink the set of VMs based on service demand.

## Specifications

The following are specifications for using internal passthrough Network Load Balancers as next hops.

### Routes

You can create a static route to pass TCP, UDP, and other protocol traffic to an internal passthrough Network Load Balancer where the load balancer is the next hop for the static route. The route can be an external (publicly routable) CIDR prefix or an internal CIDR prefix, if the prefix doesn't conflict with a [subnet route](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes). For example, you can replace your default route (`0.0.0.0/0`) with a route that directs traffic to third-party backend VMs for packet processing.

**Caution:** When sending traffic to Google APIs and services, don't route the traffic through a next-hop VM or through a next-hop internal passthrough Network Load Balancer. Instead, route such traffic through a next-hop default internet gateway. This includes traffic to Google APIs and services sent by means of [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

### Options for specifying the next hop

You can specify an internal passthrough Network Load Balancer next hop in one of two ways:

  * By using the forwarding rule's name and region
  * By using the forwarding rule's IP address



For details about the project and VPC network in which an internal passthrough Network Load Balancer next hop can reside, see [Next hops and features](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops).

You can exchange static routes with internal passthrough Network Load Balancer next hops using VPC Network Peering. For details, see [Options for exchanging static routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#static-route-exchange).

**Note:** A load balancer whose forwarding rule uses the `L3_DEFAULT` protocol cannot be the next hop for a static route. If this static route is created, traffic is silently dropped. 

### Destination range

The destination of a [static route](https://docs.cloud.google.com/vpc/docs/static-routes) cannot be equal to or more specific than a [subnet route](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes). Note that _more specific_ means that the subnet mask is longer. This rule applies to all static routes, including when the next hop is an internal passthrough Network Load Balancer. For example, suppose that your subnet route is `10.140.0.0/20`. The destination of a static route can't be the same (`10.140.0.0/20`), and it can't be more specific, as in `10.140.0.0/22`.

### Same VPC network and region

Static routes that use internal passthrough Network Load Balancers as next hops are limited to the following:

  * **A single VPC network.** The load balancer and the static route must be in the same VPC network.

  * **A single region or all regions.** Unless you configure [global access](https://docs.cloud.google.com/load-balancing/docs/internal#client-access), the static route is only available to resources in the same region as the load balancer. This regional restriction is enforced even though the route itself is part of the routing table for the entire VPC network. If you enable global access, the static route is available to resources in any region.




### Advertising the static route

To advertise the prefix (destination) for the static route, you can use Cloud Router [custom advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes). The scope of the route advertisement depends on the load balancer's global access setting, as follows:

  * When global access is disabled, the internal passthrough Network Load Balancer is only available to VMs, Cloud VPN tunnels, and Cloud Interconnect attachments (VLANs) that are in the same region as the load balancer. Consequently, a custom route advertisement for a static route's prefix only makes sense if the Cloud Router and load balancer are in the same region.

  * When global access is enabled, the internal passthrough Network Load Balancer is available to VMs, Cloud VPN tunnels, and Cloud Interconnect attachments (VLANs) that are in any region. With global dynamic routing, on-premises systems can use the static route from any connected region.




The following table summarizes the accessibility of the load balancer.

Global access | VPC network dynamic routing mode | Load balancer access  
---|---|---  
Disabled | Regional | Accessible by routers in the **same** region  
Disabled | Global | Accessible by routers in the **same** region  
Enabled | Regional | Accessible by all routers in **any** region  
Enabled | Global | Accessible by all routers in **any** region  
  
For more information, see [Internal passthrough Network Load Balancers and connected networks](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks).

### Order of operations

You must create an internal passthrough Network Load Balancer before you can create a static route that uses it as a next hop. The load balancer must exist before you can create the route. If you try to create a route that refers to a nonexistent load balancer, Google Cloud returns an error.

You specify an internal passthrough Network Load Balancer next hop by using the forwarding rule's name and the load balancer's region, or by using the internal IP address associated with the forwarding rule.

After you've created a route with a next hop that refers to an internal passthrough Network Load Balancer, you cannot delete the load balancer unless you first delete the route. Specifically, you can't delete an internal forwarding rule until no static route uses that load balancer as a next hop.

### Processing of TCP, UDP, and other protocol traffic

**Important:** The information in this section applies only to custom routes created before May 15, 2021. 

If an internal passthrough Network Load Balancer as next hop route was created before May 15, 2021, the load balancer forwards only TCP and UDP traffic on all ports to the backend VMs, regardless of the forwarding rule or backend service configuration. All other traffic, such as ICMP pings, will be handled by the next most specific route in your VPC network.

If a route created before May 15, 2021 was still in operation on August 16, 2021, it was automatically migrated to forward all protocol traffic starting August 16, 2021.

When an internal passthrough Network Load Balancer is deployed as a next hop, Google Cloud forwards _all_ traffic on all ports to the backend VMs, regardless of the following:

  * The forwarding rule's protocol and port configuration
  * The backend service's protocol configuration



The internal passthrough Network Load Balancer, which is the next hop of the route, seamlessly supports forwarding all the traffic for the protocols supported by Google Cloud VPC networks (such as TCP, UDP, and ICMP).

### Additional considerations

  * **Supported forwarding rules.** Google Cloud supports only next hop internal passthrough Network Load Balancer forwarding rules. Google Cloud does _not_ support next hop forwarding rules used by other load balancers, protocol forwarding, or as Private Service Connect endpoints.

  * **Specification methods and forwarding rule network and project.** You can specify a next hop forwarding rule by using one of following three methods. The specification method that you use determines whether the forwarding rule's network must match the route's network and in what project the forwarding rule can be located.

Choose one of the following methods and ensure that the IP version of your forwarding rule matches the IP version of the static route that you create:

    * **By forwarding rule name (`--next-hop-ilb`) and region (`--next-hop-ilb-region`)**: when you specify a next hop forwarding rule by name and region, the forwarding rule's network must match the route's VPC network. The forwarding rule must be located in the same project that contains the forwarding rule's network (a standalone project or a Shared VPC host project).

    * **By forwarding rule resource link** : a forwarding rule's resource link uses the format `/projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE_NAME`, where `PROJECT_ID` is the project ID of the project that contains the forwarding rule, `REGION` is the forwarding rule's region, and `FORWARDING_RULE_NAME` is the forwarding rule's name. When you specify a next hop forwarding rule by its resource link, the forwarding rule's network must match the route's VPC network. The forwarding rule can be located in _either_ the project that contains the forwarding rule's network (a standalone project or a Shared VPC host project) _or_ a Shared VPC service project.

    * **By a forwarding rule IP address** : when you specify a next hop forwarding rule by its IPv4 or IPv6 address, the forwarding rule's network can be _either_ the route's VPC network _or_ a VPC network that's connected to the route's VPC network by using either VPC Network Peering or NCC. NCC supports a next hop internal passthrough Network Load Balancer in a VPC spoke subject to [NCC requirements for connectivity](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/static-routes-overview). The forwarding rule can be located in _either_ the project that contains the forwarding rule's network (a standalone project or a Shared VPC host project) _or_ a Shared VPC service project.

  * **Effect of global access.** Custom static routes using internal passthrough Network Load Balancer next hops are programmed in all regions. Whether the next hop is usable depends on the load balancer's [global access](https://docs.cloud.google.com/load-balancing/docs/internal#client-access) setting. With global access enabled, the load balancer next hop is accessible in all regions of the VPC network. With global access disabled, the load balancer next hop is only accessible in the same region as the load balancer. With global access disabled, packets sent from another region to a route using an internal passthrough Network Load Balancer next hop are dropped.

  * **When all backends are unhealthy.** When all backends of an internal passthrough Network Load Balancer fail health checks, the routes using that load balancer next hop are still in effect. Packets processed by the route are sent to one of the next hop load balancer's backends according to [traffic distribution](https://docs.cloud.google.com/load-balancing/docs/internal#traffic_distribution).

  * **Forwarding rules that use a common internal IP address (`--purpose=SHARED_LOADBALANCER_VIP`) are not supported.** Next hop internal passthrough Network Load Balancers and [internal passthrough Network Load Balancer forwarding rules that use a common IP address to reference different backend services (different internal passthrough Network Load Balancers)](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip) are mutually exclusive features. A next hop internal passthrough Network Load Balancer must use an IP address that is unique to the load balancer's forwarding rule so that only one backend service (one load balancer) is unambiguously referenced. Traffic sent to a next-hop internal passthrough Network Load Balancer configured with a shared IP address is silently dropped.

  * **Multiple routes with the same destinations and priorities, but different next hop internal passthrough Network Load Balancers.** Google Cloud _never_ distributes traffic among two or more next hop internal passthrough Network Load Balancers using ECMP. Google Cloud selects a single next hop internal passthrough Network Load Balancer using an internal algorithm, and Google Cloud makes no guarantee that the same next hop internal passthrough Network Load Balancer is consistently selected. As a best practice, don't create two or more static routes in the same VPC network if the routes differ only in next hop internal passthrough Network Load Balancer.

  * **Multiple routes with the same destinations, priorities, and next hop internal passthrough Network Load Balancers.** Without a network tag, Google Cloud does not allow you to create multiple static routes that have the same combination of destination, priority, and internal passthrough Network Load Balancer next hop. With network tags, you can create multiple static routes having the same combination of destination, priority, and internal passthrough Network Load Balancer next hop.




## Requirements

The following requirements apply when you need to send traffic through two internal passthrough Network Load Balancers that use the same backend VMs. In this situation, the backend VMs have two load-balanced network interfaces, one interface used by each load balancer. Each interface is in a different VPC network, and each VPC network has a static route using one of the load balancers as a next hop. This is a common configuration if backend VMs perform routing, firewall, or proxy functionality.

### Load balancer requirements

  1. Both the load balancers need to have the same set of eligible backends. Note that you arrive at the set of eligible backends after [steps 2.1 and 2.2 in the backend selection and connection tracking process](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#select-backend).

This has the following consequences:

     * Both load balancers must either have the failover feature disabled or both have the failover feature enabled. If enabled, both load balancers need to have identical failover policies.

     * Backends must simultaneously pass or simultaneously fail health checks for both load balancers.

     * Both load balancers must have the same zonal affinity configuration.
  2. Both load balancers must [select an eligible backend in the same way](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#select-backend). To meet this requirement:

     * Both load balancers must use the same session affinity setting.
     * The common session affinity setting cannot be `CLIENT_IP_NO_DESTINATION`.

The session affinity determines which packet characteristics are hashed to select an eligible backend. Symmetric hashing means that Google Cloud calculates the same hash for packets in both directions of a flow; the hash doesn't change when the source IP address:port is swapped with the destination IP address:port. Because symmetric hashing requires a session affinity setting that includes destination IP address or destination IP address:port information, you can use any session affinity _except for_ `CLIENT_IP_NO_DESTINATION`.

**Important:** Symmetric hashing is only supported if the internal passthrough Network Load Balancer forwarding rule and static route that references it were created on or after June 22, 2021. Replace static routes and forwarding rules that were created before this date to ensure that symmetric hashing works correctly.
  3. Both load balancers must [track connections](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#tracking-mode) in the same way. This has the following consequences:

     * Both load balancers must use the same connection tracking mode (`PER_CONNECTION` or `PER_SESSION`). This avoids a situation where one load balancer might group multiple connections into the same connection tracking table entry compared to the other load balancer.

     * Both load balancers should use the same idle timeout and connection persistence on unhealthy backends setting.




### Client and server requirements

If you configure next hop internal passthrough Network Load Balancers with zonal affinity, carefully consider how zonal affinity affects client to server and server to client flows for the same connection. If you require packets to be processed by the same backend VM in both directions for the same connection, the following placement options are supported:

  * **Client, server, and backend VMs all in the same zone** : With this placement, each load balancer's modified eligible backends can be identical, subject to the load balancer requirements, because a zonal match happens in both directions. Client to server packet flow for a connection can use the same backend as the corresponding server to client flow.

  * **Client and server VMs in a zone (or zones) where there are no backend VMs** : With this placement, a zonal match is never possible when packets are sent between clients and servers, so zonal affinity doesn't affect the original eligible backends.




### Backend requirements

  * You must configure all of the internal passthrough Network Load Balancer's backend VMs to allow IP forwarding (`--can-ip-forward = True`). For more information, see [Considerations common to instance and internal passthrough Network Load Balancer next hops](https://docs.cloud.google.com/vpc/docs/static-routes#instance_next_hops).

  * You cannot use an internal passthrough Network Load Balancer whose backends are Google Kubernetes Engine (GKE) nodes as a next hop for a static route. Software on the nodes can only route traffic to Pods if the destination matches an IP address managed by the cluster, not an arbitrary destination.




## Use cases

You can use an internal passthrough Network Load Balancer as a next hop in multiple deployments and topologies.

For each example, note the following guidelines:

  * In these examples, each VM's network interfaces are in separate VPC networks.

  * You cannot use backend VMs or load balancers to route traffic between subnets in the same VPC network because subnet routes cannot be overridden.

  * The internal passthrough Network Load Balancer is a [software-defined pass-through load balancer](https://docs.cloud.google.com/load-balancing/docs/internal#architecture). Packets are delivered to backend VMs without alterations to source or destination information (addresses or addresses and ports).

Routing, packet filtering, proxying, and address translation are the responsibility of the virtual appliance VMs that serve as backends for the internal passthrough Network Load Balancer.




### Using an internal passthrough Network Load Balancer as the next hop to a NAT gateway

This use case load balances traffic from internal VMs to multiple NAT gateway instances that route traffic to the internet.

[ ![NAT use case.](https://docs.cloud.google.com/static/load-balancing/images/nat-use-case.svg)](https://docs.cloud.google.com/static/load-balancing/images/nat-use-case.svg) NAT use case (click to enlarge).

### Hub and spoke: Exchanging next-hop routes by using VPC Network Peering

In addition to exchanging subnet routes, you can configure [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) to export and import custom static and dynamic routes. Static routes that have a next hop of the default internet gateway are excluded. Custom static routes that use next-hop internal passthrough Network Load Balancers are included.

You can configure a hub-and-spoke topology with your next-hop firewall virtual appliances located in the `hub` VPC network by doing the following:

  * In the `hub` VPC network, create an internal passthrough Network Load Balancer with firewall virtual appliances as the backends.
  * In the `hub` VPC network, create a static route, and set the next hop to be the internal passthrough Network Load Balancer.
  * Connect the `hub` VPC network to each of the `spoke` VPC networks by using VPC Network Peering.
  * For each peering, configure the `hub` network to export its custom routes, and configure the corresponding `spoke` network to import custom routes. The route with the load balancer next hop is one of the routes that the `hub` network exports.



Subject to the [routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection), the next hop firewall appliance load balancer in the `hub` VPC network is available in the spoke networks:

  * to clients in the same region as the load balancer, if global access is disabled
  * to clients in all regions, if global access is enabled, according to the [routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).

[ ![Hub and spoke.](https://docs.cloud.google.com/static/load-balancing/images/use-case4-hub-spoke.svg)](https://docs.cloud.google.com/static/load-balancing/images/use-case4-hub-spoke.svg) Hub and spoke (click to enlarge).

### Load balancing to multiple NICs

In the following use case, the backend VMs are virtual appliance instances (for example, packet inspection, routing, or gateway VMs) with NICs in multiple VPC networks. These virtual appliance instances can be commercial solutions from third parties or solutions that you build yourself. The virtual appliances are Compute Engine VMs with [multiple NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

This example shows a single set of backend virtual appliances in a managed VM instance group.

In the VPC network called `testing`, the internal passthrough Network Load Balancer has a forwarding rule called `fr-ilb1`. In the example, this load balancer distributes traffic to the `nic0` interface.

In the VPC network called `production`, a different internal passthrough Network Load Balancer has a forwarding rule called `fr-ilb2`. This load balancer distributes traffic to a different interface, `nic1` in this example.

[ ![Traffic with multi-NIC load balancing.](https://docs.cloud.google.com/static/load-balancing/images/use-case-multi-nic.svg)](https://docs.cloud.google.com/static/load-balancing/images/use-case-multi-nic.svg) Traffic with multi-NIC load balancing (click to enlarge).

For a detailed configuration setup, see [Load balancing to multiple backend NICs](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-next-hop#ilb-nh-multi-nic-setup).

#### Symmetric hashing

The preceding example doesn't use source network address translation (SNAT). SNAT isn't required because Google Cloud uses _symmetric hashing_. This means that when packets belong to the same flow, Google Cloud calculates the same hash. In other words, the hash doesn't change when the source IP address:port is swapped with the destination IP address:port.

Notes:

  * Symmetric hashing is enabled automatically when you create the internal passthrough Network Load Balancer forwarding rule on or after June 22, 2021.

  * To enable symmetric hashing on existing internal passthrough Network Load Balancers, you must re-create the forwarding rule and the next-hop route, as described in [Enabling symmetric hashing](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-next-hop#symmetric-hashing).

  * Symmetric hashing is only supported with internal passthrough Network Load Balancers.

  * Symmetric hashing is supported with the following session affinity types for protocols TCP and UDP:

    * Client IP (`CLIENT_IP`)
    * Client IP and protocol (`CLIENT_IP_PROTO`)
    * Client IP, protocol, and port (`CLIENT_IP_PORT_PROTO`)

For more information about these settings, see [Session affinity options](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#session_affinity).

  * You can optionally use SNAT if your use case requires it for some reason.




## What's next

  * To configure an internal passthrough Network Load Balancer to be a next hop, see [Set up an internal passthrough Network Load Balancer for third-party appliances](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-next-hop) or [Deploy a hub-and-spoke network by using a load balancer as the next hop](https://docs.cloud.google.com/load-balancing/docs/internal/deploying-ilb-next-hop-vm).
  * To configure and test an internal passthrough Network Load Balancer, see [Set up an internal passthrough Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal).
  * To troubleshoot next hop issues with your internal passthrough Network Load Balancer, see [Troubleshoot internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb#lb-as-next-hop).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
