---
url: https://docs.cloud.google.com/vpc/docs/static-routes/
title: Static routes \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:19.577584+00:00
---

# Static routes  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/static-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Static routes

This page provides an overview of how static routes work in Google Cloud.

For a general overview of routes in Google Cloud, see the [Routes overview](https://docs.cloud.google.com/vpc/docs/routes).

## Considerations for creating static routes

You can create static routes in one of two ways:

  * You can [create static routes manually](https://docs.cloud.google.com/vpc/docs/using-routes#addingroute) using the Google Cloud console, [`gcloud compute routes create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/create), or [the `routes.insert` API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes/insert).

  * If you use the Google Cloud console to create a Classic VPN tunnel that doesn't use dynamic routing, Cloud VPN might create corresponding static routes automatically. For more information, see [ Cloud VPN networks and tunnel routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing).




You can exchange static routes with a peered VPC network as described in [Options for exchanging custom static routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#static-route-exchange) in the VPC Network Peering documentation.

**Note:** In auto mode VPC networks, don't create custom static routes whose destinations fit inside the `10.128.0.0/9` range. That range contains automatically created subnets. Static routes with destinations inside `10.128.0.0/9` that exist in an auto mode VPC network might be disabled unexpectedly when a new Google Cloud region becomes available. This happens because a new subnet route is created for the primary IPv4 address range of the new region's automatically created subnet. For more information, see [auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges) and [considerations for auto mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#auto-mode-considerations).

## Route parameters

Static routes support the following attributes:

  * **Name** and **Description**. These fields identify the route. A name is required, but a description is optional. Every route in your _project_ must have a unique name.

  * **Network**. Each route must be associated with exactly one VPC network.

  * **Next hop**. The next hop identifies the network resource to which packets are sent. All next hop types support IPv4 destinations, and some next hop types support IPv6 destinations. For more information, see Next hops and features.

  * **Destination range**. The destination range is a single IPv4 or IPv6 [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

Destinations for static routes must follow the rules described in [Interactions between subnet routes and static routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-static-interactions) and VPC Network Peering [Subnet and static route interactions](https://docs.cloud.google.com/vpc/docs/vpc-peering#interaction-subnet-static). The broadest possible destination for an IPv4 static route is `0.0.0.0/0`. The broadest possible destination for an IPv6 static route is `::/0`.

  * **Priority**. Lower numbers indicate _higher_ priorities. The highest possible priority is `0`, and the lowest possible priority is `65,535`.

  * **Network tags**. You can make a static route apply to _only_ select VM instances in the VPC network, identified by a [network tag](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags):

    * A static route _without_ a network tag applies to all resources in the VPC network, including all VM instances, Cloud VPN tunnels, Cloud Interconnect VLAN attachments, Router appliances, and Envoy proxies in proxy-only subnets.

    * A static route _with_ a network tag _only_ applies to VM instances that have that network tag. It doesn't apply to any other resources.

    * [Static routes with tags are never exchanged when using VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering#static-route-exchange).




## Next hops and features

The following table summarizes static route feature support by next hop type:

Next hop type | IPv4 | IPv6 | ECMP1  
---|---|---|---  
**Next hop gateway (`next-hop-gateway`)**  
Specify a default internet gateway to define a path to external IP addresses. |  |  |   
**Next hop instance by name and zone (`next-hop-instance`)**   
Send packets to a next hop VM that is identified by name and zone and is in the same project as the route. For more information, see Considerations for next hop instances. |  |  |   
**Next hop instance by address (`next-hop-address`)**  
Send packets to a next hop VM that is identified by the primary internal IPv4 address, or an internal or external IPv6 address, of its network interface. For more information, see Considerations for next hop instances. |  |  |   
**Next hop internal passthrough Network Load Balancer by forwarding rule name (`next-hop-ilb`) and region (`next-hop-ilb-region`)**   
Send packets to backends of an internal passthrough Network Load Balancer that is identified by the forwarding rule's name, region, and, optionally, project. For more information, see Considerations for internal passthrough Network Load Balancer next hops. |  |  |   
**Next hop internal passthrough Network Load Balancer by address (`next-hop-ilb`)**  
Send packets to backends of an internal passthrough Network Load Balancer that is identified by the IP address of the load balancer's forwarding rule. For more information, see Considerations for internal passthrough Network Load Balancer next hops.  |  | 2 |   
**Next hop Classic VPN tunnel (`next-hop-vpn-tunnel`)**   
Send packets to a next hop Classic VPN tunnel by using either [policy-based routing or route-based VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#ts-tun-routing). For more information, see Considerations for Classic VPN tunnel next hops. |  |  |   
  
1Equal-cost multipath (ECMP) means that two or more static routes can share the same destination range and priority. Although you can create two or more static routes in a VPC network with the same destination, same priority, and default internet gateway next hop, the effect is the same as having a single static route that uses the default internet gateway next hop for that destination and priority.

2IPv6 support depends on the Next hop project and network.

### Next hop project and network

A static route next hop is associated with both a VPC network and a project:

  * **Network** : except as indicated in the following table, the next hop's VPC network must match the route's VPC network.

  * **Project** : except as indicated in the following table, the next hop must be located in the project that contains the next hop's VPC network (a standalone project or a Shared VPC host project). Some next hops can be located in Shared VPC service projects.


Next hop type | Can be in a peered VPC network | Can be in a different VPC spoke of a NCC hub | Can be in a Shared VPC service project  
---|---|---|---  
**Next hop gateway (`next-hop-gateway`)** |  |  |   
**Next hop instance by name (`next-hop-instance`)** |  |  |   
**Next hop instance by address (`next-hop-address`)** |  |  |   
**Next hop internal passthrough Network Load Balancer by forwarding rule name and region (`next-hop-ilb`)** |  |  |   
**Next hop internal passthrough Network Load Balancer by forwarding rule resource link (`next-hop-ilb`)** |  |  |   
**Next hop internal passthrough Network Load Balancer by address (`next-hop-ilb`)** |  |   
IPv4 only |   
**Next hop Classic VPN tunnel (`next-hop-vpn-tunnel`)** |  |  |   
  
### Considerations common to instance and internal passthrough Network Load Balancer next hops

_Instance-based routing_ refers to a static route with a next hop that is a VM instance (`next-hop-instance` or `next-hop-address`).

_Internal passthrough Network Load Balancer as a next hop_ refers to a static route with a next hop that is an internal passthrough Network Load Balancer (`next-hop-ilb`).

When you configure instance-based routing or an internal passthrough Network Load Balancer as a next hop, consider the following guidelines:

  * **You must configure the backend VMs or the next hop instance to forward packets from any source IP address**. To configure forwarding, [enable IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward) (`can-ip-forward`) on a per-VM basis when you create the VM. For VMs created automatically as part of a managed instance group, enable IP forwarding in the instance template used by the instance group. You must make this configuration change _in addition_ to any operating system configuration necessary to route packets.

  * **Software running on the backend VM or the next hop instance must be configured appropriately**. For example, third-party appliance VMs that act as routers or firewalls must be configured according to the manufacturer's instructions.

  * **Backend VMs or the next hop instance must have appropriate firewall rules**. You must configure firewall rules that apply to the packets being routed. Keep the following in mind:

    * Ingress firewall rules applicable to instances that perform routing functions must include the IP addresses of _routed packet sources_. The implied deny ingress rule blocks all incoming packets, so you must at least create custom ingress allow firewall rules.
    * Egress firewall rules applicable to instances that perform routing functions must include the IP addresses of _routed packet destinations_. The implied allow egress rule permits this unless you've created a specific egress deny rule to override it.
    * Take into account whether the backend VM or Next Hop Instance is performing Network Address Translation (NAT) when creating your firewall rules.

For more information, see [Implied firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules).

  * **The source region of a packet sent by a backend VM or a next hop instance is the region where the backend VM or next hop instance is located**. For example, packets processed by backend VMs or next hop instances in `us-west1` can be sent to destinations that are accessible only in `us-west1` even if the backend VM or next hop instance originally received the packet from a resource in a region different from `us-west1`. Examples of resources that are accessible only in the same region as a VM sending a packet include the following:

    * Internal passthrough Network Load Balancers, internal Application Load Balancers, and regional internal proxy Network Load Balancers with global access turned off
    * Cloud VPN tunnels, Cloud Interconnect VLAN attachments, and Network Connectivity Router appliance VMs if the VPC network uses regional dynamic routing



### Considerations for next hop instances

  * **Next hop by instance name and zone (`next-hop-instance`)**: When you create a static route that has a next hop instance specified by instance name and zone, Google Cloud requires that an instance with that name exists in the specified zone, and meets the following:

    * The instance is located in the same project as the route.
    * The instance has a network interface (NIC) in the route's VPC network (not a peered VPC network).

As long as the static route exists, the following applies:

    * Google Cloud automatically updates programming for the next hop in either of the following cases:

      * The primary internal IPv4 address of the next hop instance changes, or
      * You replace the next hop instance, and the replacement instance has the same name, is in the same zone and project, and has a network interface in the route's VPC network.
    * Google Cloud _doesn't_ update programming for the next hop in the following cases:

      * When the instance is deleted.
      * The IPv6 address range assigned to the instance's NIC changes.
      * When the IPv4 or IPv6 address of the instance is unassigned.
  * **Next hop instance IP address (`next-hop-address`)**: Valid next hop VM IP addresses are the following: 
    * The primary internal IPv4 address of a VM network interface.
    * Any internal or external IPv6 address in the `/96` IPv6 address range assigned to a VM network interface.

When you create a static route with a next hop instance specified by an IP address, Google Cloud accepts any VM-assigned IP address that fits within a subnet range of a subnet in the same VPC network as the route. However, Google Cloud only programs the route if the next hop address is a valid _next hop_ VM IP address. For example, if you create a route and specify the next hop as an IP address that comes from an alias IP range, the route is created. However, because alias IP addresses aren't valid next hop VM IP addresses, the route is not programmed.

Google Cloud automatically updates programming for the next hop if the next hop IP address is moved to a different VM, if the IP address remains a valid next hop VM IP address.

When you specify a next hop instance by IP address, packets are routed to the network interface of the instance, not the specific IP address.

  * **Next hop instances in Shared VPC service projects** : When you specify a next hop VM by IP address, the VM can be located in _either_ the same project as the route (a standalone project or a Shared VPC host project) _or_ the VM can be located in a Shared VPC service project. When you specify a next hop VM by instance name and zone, the next hop VM must be located in the same project as the route and VPC network (a standalone project or a Shared VPC host project).

  * **Region-to-region costs and latency** : When you use a VM as a next hop, the next hop is located in a zone of a region. The route that uses the next hop is available to all instances in the same VPC network or to select instances with a matching network tag. Google Cloud doesn't consider regional distance for routes that use an instance as a next hop, so it is possible to create a route that sends traffic to a next hop VM in a different region. Sending packets from one region to another adds outbound data transfer costs and introduces network latency.

  * **No health checking, no configuration validation** : Google Cloud never checks whether a next hop instance meets all requirements outlined in the Considerations common to instance and internal passthrough Network Load Balancer next hops section. Disabling the VM's network interface by configuring the guest operating system of the instance _doesn't_ cause Google Cloud to disregard the next hop instance.

  * **No symmetric hashing when connecting two VPC networks** : Google Cloud doesn't offer symmetric hashing when using two or more next hop VMs that have multiple network interfaces in a configuration that meets all of the following criteria:

    * The VMs have one network interface in one VPC network and another interface in a second VPC network.
    * In each VPC network, there exists a set of at least two custom static routes for the same destination, using the same priority, where each route in the set references a unique next hop VM.

If you use two or more VMs with multiple interfaces to connect VPC networks, and you require that the same VM processes packets for a given connection in both directions, you need symmetric hashing, which is only supported by next hop internal passthrough Network Load Balancers. For more information, see [Symmetric hashing](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#symmetric-hashing).

  * **Behavior when instances are stopped or deleted** : Google Cloud _doesn't_ prevent you from stopping or deleting a static route next hop VM (specified by either name and zone or internal address). When a next hop VM is not running, routing depends on whether other routes _for the exact same destination_ exist and whether those other routes have next hops that are running. To illustrate this behavior, consider the following examples: 
    * You have the following routes and VM states:

      * `route-a`, destination `192.168.168.0/24`, priority `10`, next hop VM `vm-a` is stopped
      * `route-b`, destination `192.168.168.0/24`, priority `20`, next hop VM `vm-b` is running
      * `route-c`, destination `192.168.168.0/24`, priority `30`, next hop VM `vm-c` is running

In this example, packets whose destinations fit in `192.168.168.0/24` are sent to the `vm-b` next hop because the `vm-a` next hop of the highest priority `route-a` is not running. This happens because the [_disregard static and dynamic routes with unusable next hops_ step](https://docs.cloud.google.com/vpc/docs/routes#disregard-static-dynamic-routes) precedes the [_disregard low priority routes_ step](https://docs.cloud.google.com/vpc/docs/routes#disregard-lower-priority-routes) in the Google Cloud routing order.

    * You have the following routes and VM states:

      * `route-x`, destination `192.168.168.0/24`, priority `10`, next hop VM `vm-x` is stopped
      * `route-y`, destination `192.168.168.0/24`, priority `20`, next hop VM `vm-y` is stopped
      * `route-z`, destination `192.168.0.0/16`, priority `0`, next hop VM `vm-z` is running

In this example, packets whose destinations fit in `192.168.168.0/24` are dropped because the next hop VMs for the two `192.168.168.0/24` routes (`route-x` and `route-y`) are not running, even though a route for the broader `192.168.0.0/16` destination exists (`route-z`) with a running next hop VM. This happens because the [_most specific destination_ step](https://docs.cloud.google.com/vpc/docs/routes#most-specific-dest) precedes the [_disregard static and dynamic routes with unusable next hops_ step](https://docs.cloud.google.com/vpc/docs/routes#disregard-static-dynamic-routes) in the Google Cloud routing order.




### Considerations for internal passthrough Network Load Balancer next hops

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




### Considerations for Classic VPN tunnel next hops

  * **Region-to-region costs and latency** : Google Cloud doesn't consider regional distance for routes that use a next hop Classic VPN tunnel. Sending traffic to a next hop Classic VPN tunnel in another region adds outbound data transfer costs and introduces network latency. As a best practice, use an [HA VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn) with [dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#dynamic-routing) instead because that configuration considers regional distance.

  * **Behavior when Classic VPN tunnels are not running** : Custom static routes whose next hops are Classic VPN tunnels are not automatically removed when the Classic VPN tunnels are not running. For details about what happens when tunnels are not running, see [When tunnels are down](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/order-of-routes#tunnels_down) in the Classic VPN documentation.




### Considerations for NCC

  * You can create static routes from your VPC spokes to internal passthrough Network Load Balancers that are accessible through the NCC hub.
  * Additional limitations apply to these NCC static routes. For more information, see the [static routes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/static-routes-overview).



## What's next

  * To create and manage routes, see [Use routes](https://docs.cloud.google.com/vpc/docs/using-routes).
  * To get a general overview of routes Google Cloud, see [ Routes](https://docs.cloud.google.com/vpc/docs/routes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
