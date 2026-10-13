---
url: https://docs.cloud.google.com/vpc/docs/routes/
title: Routes \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:11.938443+00:00
---

# Routes  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Routes

Google Cloud routes define the paths that network traffic takes from a virtual machine (VM) instance to other destinations. These destinations can be inside your Google Cloud Virtual Private Cloud (VPC) network (for example, in another VM) or outside it.

In a VPC network, a route consists of a single _destination_ prefix in CIDR format and a single _next hop_. When an instance in a VPC network sends a packet, Google Cloud delivers the packet to the route's next hop if the packet's destination address is within the route's destination range.

This page provides an overview of how routes work in Google Cloud.

## Routing in Google Cloud

Every VPC network uses a scalable, distributed virtual routing mechanism. There is no physical device that's assigned to the network. Some routes can be applied selectively, but the [routing table](https://wikipedia.org/wiki/Routing_table) for a VPC network is defined at the VPC network level.

Each VM instance has a controller that is kept informed of all applicable routes from the network's routing table. Each packet leaving a VM is delivered to the appropriate next hop of an applicable route based on a routing order. When you add or delete a route, the set of changes is propagated to the VM controllers [by using an eventually consistent design](https://docs.cloud.google.com/vpc/docs/using-routes#order_of_operations).

## Route types

The following tables summarize how Google Cloud categorizes routes in VPC networks.

Type and destination | Next hop | Notes  
---|---|---  
**Policy-based routes** : Policy-based routes are evaluated before any other type of route.   
[Policy-based route](https://docs.cloud.google.com/vpc/docs/policy-based-routes)  
Policy-based routes can apply to packets based on source IP address, destination IP address, protocol, or a combination thereof.  | 

  * An option to skip evaluating other policy-based routes
  * [An internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)

|  Policy-based routes can apply to all VMs in the network, to certain VMs selected by network tag, or to traffic entering the VPC network through VLAN attachments for Cloud Interconnect (in only one region, or in all regions). Policy-based routes are never exchanged through VPC Network Peering.  
**Subnet routes** : All subnet route types are evaluated after policy based routes but before custom routes.   
Local subnet route  
Created automatically for each [subnet IP address range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) | VPC network | Created, updated, and removed automatically by Google Cloud during subnet lifecycle events. Local subnet routes apply to the whole VPC network.  
Peering subnet route  
Represents a subnet IP address range in a different VPC network connected using VPC Network Peering  | Next hop in the peer VPC network | VPC Network Peering provides [options for exchanging subnet routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#subnet-route-exchange). Created, updated, and removed automatically by Google Cloud during subnet lifecycle events. Imported peering subnet routes apply to the whole VPC network.  
NCC subnet route  
Represents a subnet IP address range in a VPC spoke (a different VPC network connected to the NCC hub)  | NCC hub | NCC spoke administrators can [ exclude the export of subnet routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin#subnet-uniqueness). Created, updated, and removed automatically by Google Cloud during subnet lifecycle events. Imported NCC subnet routes apply to the whole VPC network.  
**Custom routes** : Custom routes are evaluated after policy based routes and after subnet routes.  
[Local static route](https://docs.cloud.google.com/vpc/docs/static-routes)  
Supports various [ destinations](https://docs.cloud.google.com/vpc/docs/static-routes#individualroutes) | Forwards packets to a [static route next hop](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops) | For details about each [static route next hop](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops), see considerations for: 

  * [ Instances and internal passthrough Network Load Balancers](https://docs.cloud.google.com/vpc/docs/static-routes#instance_next_hops)
  * [Next hop instances](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-vm-only)
  * [ Internal passthrough Network Load Balancer next hops](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-l4ilb-only)
  * [ Classic VPN tunnel next hops](https://docs.cloud.google.com/vpc/docs/static-routes#classic_vpn_nh)

  
Local dynamic route  
Destinations that don't conflict with subnet routes or static routes | Peer of a BGP session on a Cloud Router | Routes are added and removed automatically based on [learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#benefits) from Cloud Routers in your VPC network.  
  
Routes apply to VMs according to the VPC network's [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).  
Peering static route, peering dynamic route  
Static or dynamic routes in a different VPC network connected using VPC Network Peering  | Next hop in the peer VPC network |  VPC Network Peering provides [options for exchanging static routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#static-route-exchange). Imported peering static routes apply to the whole VPC network. VPC Network Peering provides [options for exchanging dynamic routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#dynamic-route-exchange). Peering dynamic routes apply to one region or all regions of the VPC network according to the [ dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc-peering#interaction-dynamic-routing-mode) of the VPC network that _exports_ the routes.  
NCC dynamic route  
Dynamic routes imported from NCC hybrid spokes located in different VPC networks  | NCC hub |  A NCC hub can have [ both VPC spokes and hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes). NCC dynamic routes apply to one region or all regions of the VPC network according to the dynamic routing mode of the VPC network that contains the hybrid spoke.  
**System-generated routes**  
System-generated default routes   
`0.0.0.0/0` for IPv4   
`::/0` for IPv6 | `default-internet-gateway` | Applies to the whole VPC network  
  
Can be removed or replaced  
  
### Subnet routes

Each subnet has at least one subnet route for each IP address range that is associated with the subnet. For more information about subnet IP ranges, see [Subnets](https://docs.cloud.google.com/vpc/docs/subnets).

#### Types of subnet routes

A VPC network can include the following types of subnet routes:

  * Subnet routes for subnets in the same VPC network, referred to as _local subnet routes_.
  * _NCC subnet routes_ that are imported from VPC spokes of a NCC hub.
  * _Peering subnet routes_ that are imported from networks connected using VPC Network Peering.



Destination ranges for all types of subnet routes must be unique. For more information, see:

  * [Options for exchanging subnet routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#subnet-route-exchange) and [Subnet and peering subnet route interactions](https://docs.cloud.google.com/vpc/docs/vpc-peering#interaction-subnet-subnet) in the VPC Network Peering documentation

  * [Subnet route uniqueness](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin#subnet-uniqueness) and [VPC spokes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview) in the NCC documentation




#### Hybrid subnet routes

Local subnet routes and peering subnet routes can be hybrid subnet routes if the corresponding subnet is configured to use [hybrid subnet routing](https://docs.cloud.google.com/vpc/docs/hybrid-subnets).

#### Lifecycle of subnet routes

All IP address ranges that are part of a subnet—primary IPv4 address ranges, secondary IPv4 address ranges, and IPv6 address ranges—have a corresponding subnet route. Google Cloud creates and deletes subnet routes in these scenarios:

  * You make a [subnet configuration change](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks), for example:

    * Add or delete a subnet.
    * Expand a primary IPv4 range.
    * Add or delete a secondary IPv4 range.
    * Add or delete an IPv6 range.
  * Google Cloud adds a new region, which automatically adds a new subnet to auto VPC mode networks. For information about the IPv4 address ranges for each subnet by its region, see [auto mode IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).




### Dynamic routes

Cloud Routers instruct the VPC network to create, update, and remove dynamic routes based on received Border Gateway Protocol (BGP) messages, [applicable BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview), and [Cloud Router custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).

Dynamic routes are created in one region or in all regions based on the dynamic routing mode and best path selection mode of the VPC network that contains the Cloud Router. For more information, see the following:

  * [How Cloud Router works](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works)
  * [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes)



The next hop of a dynamic route can be one of the following:

  * A VLAN attachment backed by either a [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) connection or a [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) connection

  * A Cloud VPN tunnel, either a [HA VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies) or a [Classic VPN configured to use dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#dynamic-routing)

  * A [Router appliance VM instance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances)




If a next hop for a dynamic route becomes inaccessible, the Cloud Router that manages its BGP session instructs the VPC network to remove the dynamic route. For more information, see [BGP state changes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#bgp-state-changes).

#### Types of dynamic routes

A VPC network can include the following types of dynamic routes:

  * Dynamic routes learned by Cloud Routers in the same VPC network are referred to as _local dynamic routes_.
  * _Peering dynamic routes_ that are imported with [custom route exchange](https://docs.cloud.google.com/vpc/docs/vpc-peering#dynamic-route-exchange) from networks connected using VPC Network Peering .
  * _NCC dynamic routes_ that are [imported from hybrid spokes located in different VPC networks](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes) of a NCC hub.



Google Cloud resolves conflicts between dynamic routes and subnet routes as described in Interactions with dynamic routes.

### System-generated default routes

A default route has the broadest possible destination: `0.0.0.0/0` for IPv4 and `::/0` for IPv6. Google Cloud _only_ uses a default route to deliver a packet when the packet doesn't match a more specific route in the routing order.

The absence of a default route doesn't necessarily isolate your network from the internet because special routing paths for external passthrough Network Load Balancers and external protocol forwarding don't depend on a default route.

When you [create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks), Google Cloud adds a system-generated IPv4 [default route](https://wikipedia.org/wiki/Default_route) to the VPC network. The system-generated IPv4 default route is a local static route that has a `0.0.0.0/0` destination and default internet gateway next hop. A local static route with the `0.0.0.0/0` destination and default internet gateway next hop provides a path to [external IPv4 addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses), including IPv4 addresses on the internet. The following example resources use this path:

  * VMs with external IPv4 addresses assigned to their network interfaces, when the packets they send have sources matching the network interface primary internal IPv4 address.
  * A [public Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/overview#public-nat) configured to provide NAT services to subnets used by VM network interfaces. For both NAT44 and NAT64, public Cloud NAT gateways always depend on a local IPv4 static route that uses the default internet gateway next hop. For more information about which traffic can be translated by public Cloud NAT gateways, see [General specifications](https://docs.cloud.google.com/nat/docs/public-nat#specs-gen-pub-nat).



When you create a subnet that has an external IPv6 address range, Google Cloud adds a system-generated IPv6 default route to the VPC network if it doesn't already have one. The system-generated IPv6 default route is a local static route that has a `::/0` destination and default internet gateway next hop. A local static route with the `::/0` destination and default internet gateway next hop provides a path to [external IPv6 addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses#external), including IPv6 addresses on the internet. This path can be used by the following:

  * VMs with `/96` external IPv6 address ranges assigned to their network interfaces, when the packets they send have sources in that `/96` address range.



Accessing global Google APIs _sometimes_ depends on a local IPv4 or IPv6 default route with default internet gateway next hop:

  * If you access global Google APIs and services by sending packets to a [Private Service Connect endpoint for global Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis), your VPC network doesn't require a default route with default internet gateway next hop because the internal forwarding rule of the Private Service Connect endpoint is the route. For more information, see Private Service Connect endpoints for global Google APIs.

  * If you access global Google APIs and services by sending packets to IPv4 or IPv6 addresses for the default domains, the IPv4 or IPv6 addresses for `private.googleapis.com`, or the IPv4 or IPv6 addresses for `restricted.googleapis.com`, you can either use default IPv4 and IPv6 routes that have default internet gateway next hops, or you can create and use IPv4 and IPv6 static routes that have more specific destinations and default internet gateway next hops:

    * If your VMs have only internal IP addresses, see [Routing options](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-routing) for Private Google Access.
    * If your VMs have external IP addresses, see [Routing options](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip#config-routing).



## Route interactions

The following sections describe the interactions between subnet routes and other route types.

### Interactions between subnet routes and static routes

Google Cloud enforces the following rules for local subnet routes, peering subnet routes, and NCC subnet routes _unless_ the corresponding subnet has been configured to use [hybrid subnet routing](https://docs.cloud.google.com/vpc/docs/hybrid-subnets).

  * Google Cloud doesn't let you create a new static route if the destination of the new static route exactly matches or fits within the destination of an existing local, peering, or NCC subnet route. For example:

    * If a local, peering, or NCC subnet route exists with the `10.70.1.0/24` destination, you cannot create a new static route for `10.70.1.0/24`, `10.70.1.0/25`, `10.70.1.128/25`, or any other destination that fits within `10.70.1.0/24`.

    * If a local or peering subnet route exists with the `2001:0db8:0a0b:0c0d::/64` destination, you can't create a new static route for `2001:0db8:0a0b:0c0d::/64`, `2001:0db8:0a0b:0c0d::/96`, or any other destination that fits within `2001:0db8:0a0b:0c0d::/64`.

  * Google Cloud doesn't let you make any changes to subnets that result in a subnet IP address range that exactly matches or contains the destination of an existing local or peering static route. For example:

    * If your VPC network has a static route with the `10.70.1.128/25` destination, you can't create a new subnet that has a primary or secondary IPv4 address range of `10.70.1.128/25`, `10.70.1.0/24`, or any other IP address range that contains all the IPv4 addresses in `10.70.1.128/25`.

    * If your VPC network has a static route with the `2001:db8:a0b:c0d:e0f:f0e::/96` destination, Google Cloud prohibits the creation of a new local or peering subnet route that has an IPv6 address range of `2001:db8:a0b:c0d::/64` or any other range that contains all the IPv6 addresses in `2001:db8:a0b:c0d:e0f:f0e::/96`.




### Interactions between subnet routes and dynamic routes

Google Cloud enforces the following rules _unless_ a subnet has been configured to use [hybrid subnet routing](https://docs.cloud.google.com/vpc/docs/hybrid-subnets).

  * Google Cloud doesn't create a dynamic route if a Cloud Router sends a prefix that either exactly matches or fits within the destination of an existing local, peering, or NCC subnet route. For example:

    * If a local, peering, or NCC subnet route exists with the `10.70.1.0/24` destination, and if a Cloud Router in the VPC network, a peered VPC network, or a network containing a NCC hybrid spoke receives `10.70.1.128/25`, `10.70.1.0/24`, or any other prefix that fits within `10.70.1.0/24`, Google Cloud doesn't create any local, peering, or NCC dynamic routes for the received conflicting prefixes.

    * If a local, peering, or NCC subnet route exists with the `2001:0db8:0a0b:0c0d::/64` destination, and if a Cloud Router in the VPC network, a peered VPC network, or a network containing a NCC hybrid spoke receives `2001:0db8:0a0b:0c0d::/96`, `2001:0db8:0a0b:0c0d::/64`, or any other prefix that fits within `2001:0db8:0a0b:0c0d::/64`, Google Cloud doesn't create any local, peering, or NCC dynamic routes for the received conflicting prefixes.

  * Google Cloud removes any existing dynamic route if any change to subnets results in the creation of a new local, peering, or NCC subnet route whose destination exactly matches or contains the destination of the existing local, peering, or NCC dynamic route. For example:

    * If your VPC network has a local, peering, or NCC dynamic route with the `10.70.1.128/25` destination, Google Cloud removes the dynamic route when a new local, peering, or NCC subnet route for `10.70.1.128/25`, `10.70.1.0/24`, or any other IP address range that contains all the IPv4 addresses in `10.70.1.128/25` is created.

    * If your VPC network has a local, peering, or NCC dynamic route with the `2001:db8:a0b:c0d::/96` destination, Google Cloud removes the dynamic route when a new local, peering, or NCC subnet route for `2001:db8:a0b:c0d::/64` is created.




## Applicability and order

### Applicable routes

Each instance, Cloud VPN tunnel, and VLAN attachment has a set of _applicable routes_ —routes that apply to that specific resource. Applicable routes are a subset of all routes in the VPC network.

The following route types always apply to all VM instances, VLAN attachments, and Cloud VPN tunnels:

  * Special routing paths
  * Subnet routes



The following route types can be configured to apply only to certain VM instances, VLAN attachments, or Cloud VPN tunnels:

  * [Policy-based routes](https://docs.cloud.google.com/vpc/docs/policy-based-routes) can apply to:

    * All VM instances, VLAN attachments, and Cloud VPN tunnels
    * Only VM instances identified by [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags)
    * Only VLAN attachments in a particular region
  * [Static routes](https://docs.cloud.google.com/vpc/docs/static-routes) can apply to:

    * All VM instances, VLAN attachments, and Cloud VPN tunnels
    * Only VM instances identified by network tags
  * Dynamic routes can apply to VM instances, VLAN attachments, and Cloud VPN tunnels in either the region containing the dynamic route's next hop or all regions, based on the dynamic routing mode of the VPC network.




### Special routing paths

VPC networks have special routes for certain services. These special routing paths don't appear in your VPC network route table. You can't remove any special routing paths. However, you can allow or deny packets by using VPC firewall rules or firewall policies.

#### Paths for external passthrough Network Load Balancers and external protocol forwarding

[External passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network) and [external protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding) use [Maglev](https://research.google/pubs/maglev-a-fast-and-reliable-software-network-load-balancer/) systems to route packets from clients on the internet to backend VMs and target instances in your VPC network. These Maglev systems route packets that have destinations that match the destination of the external forwarding rule.

Each forwarding rule for an external passthrough Network Load Balancer or for external protocol forwarding also provides a routing path for its backend VMs or target instance to send packets to destinations outside of the VPC network:

  * Packets sent by backend VMs or target instances can be either outbound response packets (sent back to the client) or they can be outbound packets that initiate a new connection.
  * Packet sources must match the forwarding rule's IP address. Packet protocol and source port don't have to match the forwarding rule's protocol and port specification.
  * Forwarding rule routing paths don't depend on a default route or the use of the default internet gateway next hop.
  * Backend VMs and target instances don't need to have IP forwarding enabled.



#### Paths between Google Front Ends and backends

[External Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https) and [external proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/tcp) use Google Front Ends (GFEs). Second layer GFEs open TCP connections to your backend VMs and send packets from the following sources:

  * `35.191.0.0/16` and `130.211.0.0/22` for IPv4
  * `2600:2d00:1:1::/64` for IPv6



Google Cloud uses routes in Google's network to deliver packets from those source ranges to backend VMs in your VPC network. Each VPC network includes routing paths that allow VMs to send response packets to the ranges.

#### Paths for health checks

Health checks for all load balancers and for [managed instance group autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) send packets to your backend VMs from [health check probe IP address ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).

Google Cloud uses routes in Google's network to deliver packets from health check probe systems to VMs in your VPC network. Each VPC network includes routing paths that allow VMs to send response packets to the health check probe systems.

#### Paths for Identity-Aware Proxy (IAP)

[IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) uses `35.235.240.0/20` (IPv4) and `2600:2d00:1:7::/64` (IPv6). These ranges are used exclusively within Google's production network, and can't be used for any other purpose:

  * Google edge routers drop packets from the internet if the packets spoof source IP addresses from the IAP ranges. Google edge routers also don't have valid next hops for destinations in these ranges.

  * Each VPC network includes non-removable routes whose destinations are the IAP ranges. These routes provide communication between IAP proxies and VMs (for administrative protocols like SSH and RDP). You can't privately use the IAP ranges as subnet ranges in VPC networks.




#### Paths for Cloud DNS and Service Directory

The following Cloud DNS and Service Directory features use `35.199.192.0/19`:

  * Cloud DNS [forwarding targets that use private routing](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones#firewall-rules)
  * Cloud DNS [alternative name servers that use private routing](https://docs.cloud.google.com/dns/docs/server-policies-overview#altns-targets)
  * [Private network access for Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access#creating-endpoint-with-private-network-access)



This range is used exclusively within Google's production network, and can't be used for any other purpose:

  * Google edge routers drop packets from the internet if the packets spoof source IP addresses from the Cloud DNS and Service Directory feature range. Google edge routers also don't have valid next hops for destinations in this range.

  * Each VPC network includes a non-removable route whose destination is the Cloud DNS and Service Directory range. This route allows Cloud DNS and Service Directory proxies to communicate with resources in a VPC network. You can't privately use the Cloud DNS and Service Directory range as a subnet range in a VPC network.




#### Paths for Serverless VPC Access

[Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) uses `35.199.224.0/19`. This range is used exclusively within Google's production network, and can't be used for any other purpose:

  * Google edge routers drop packets from the internet if the packets spoof source IP addresses from the Serverless VPC Access range. Google edge routers also don't have valid next hops for destinations in this range.

  * Each VPC network includes a non-removable route whose destination is the Serverless VPC Access range. This route allows the VM instances that power Serverless VPC Access connectors to communicate with serverless products. You can't privately use the Serverless VPC Access range as a subnet range in a VPC network.




#### Paths for Chrome Enterprise Premium

[Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/security-gateway-private-web-apps#configure_network_routing_and_firewall_rules) uses `136.124.16.0/20`. This range is used exclusively within Google's production network, and can't be used for any other purpose:

  * Google edge routers drop packets from the internet if the packets spoof source IP addresses from the Chrome Enterprise Premium ranges. Google edge routers also don't have valid next hops for destinations in these ranges.

  * Each VPC network includes non-removable routes whose destinations are the Chrome Enterprise Premium ranges. These routes provide communication between Chrome Enterprise Premium secure gateways and private applications running on resources in a VPC network. You can't privately use the Chrome Enterprise Premium ranges as subnet ranges in VPC networks.




### Routing order

There might be more than one applicable route for a given packet. The following steps model the process that Google Cloud uses to select a route.

  1. **Special routing paths** : Some Google Cloud special routing paths not shown in VPC network route tables. For details, see Special routing paths.

If a special routing path is applicable, your route selection model contains only the special path. All other routes are disregarded, and evaluation stops at this step.

  2. **Policy-based routes** : Policy-based routes are evaluated after special routing paths but before other types of routes. If no policy-based routes exist in the VPC network, Google Cloud skips this step and continues to the subnet routes step.

Google Cloud evaluates policy-based routes solely by their priority. Google Cloud evaluates a packet's source and destination for each policy-based route, starting with the highest priority policy-based route or routes. If a packet's characteristics don't match a policy-based route, Google Cloud disregards that policy-based route and continues to evaluate the next policy-based route in the sorted list. The next policy-based route to evaluate might share the same priority as the disregarded policy-based route, or it might have a lower priority.

     * If a packet's characteristics _don't_ match any policy-based route after evaluating all policy-based routes in your route selection model, Google Cloud disregards all policy-based routes and continues to the subnet routes step.

     * If a packet's characteristics match a highest-priority policy-based route, Google Cloud first disregards all lower-priority policy-based routes. If two or more policy-based routes are left in the list, Google Cloud evaluates each of the remaining policy-based routes that have identical priorities. Google Cloud disregards any remaining policy-based routes if a packet's characteristics don't match it. After this step, your route selection model might contain one or more policy-based routes.

     * If your route selection model includes two or more matching highest-priority policy-based routes, Google Cloud selects a single policy-based route by using an internal algorithm. The selected policy-based route might not be the most specific match for the packet's source or destination. To avoid this ambiguity, we recommend that you create policy-based routes that have unique priorities.

     * If your route selection model includes only a single highest-priority policy-based route that is configured to [skip other policy-based routes](https://docs.cloud.google.com/vpc/docs/policy-based-routes#skip-option), Google Cloud disregards all policy-based routes and continues to the subnet routes step.

     * If your route selection model includes only a single highest-priority policy-based route that _is not configured to skip other policy-based routes_ , Google Cloud delivers the packet to the next hop internal passthrough Network Load Balancer, and disregards all non-policy-based routes.

  3. **Subnet routes** : Google Cloud checks whether the packet's destination fits within the destination range of a local, peering, or Network Connectivity Center subnet route in the VPC network.

     * **No matching subnet route** : If a packet's destination _doesn't_ match the destination range of any subnet route, Google Cloud disregards all subnet routes. Remove all subnet routes from your route selection model and continue to the Most specific destination step to evaluate static and dynamic routes.

     * **Matching regular subnet route** : For most subnets, if a packet's destination matches the destination range of a regular subnet route, Google Cloud exclusively uses the subnet route. Google Cloud disregards all other routes, and evaluation stops at this step. If the packet's destination isn't associated with a resource or belongs to a stopped VM instance, the packet is dropped.

     * **Matching hybrid subnet route** : If a packet's destination matches the destination range of a [hybrid subnet route](https://docs.cloud.google.com/vpc/docs/hybrid-subnets), and the destination matches an IP address that's associated with a running VM instance or an internal forwarding rule, Google Cloud routes the packet using the hybrid subnet route. Google Cloud disregards all other routes, and evaluation stops at this step.

If the destination doesn't match a running VM or an internal forwarding rule, see Unmatched resources in hybrid subnet routes.

  4. **Private Service Connect endpoints for global Google APIs** : Each [Private Service Connect endpoint for global Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#ip-address-requirements) is an internal forwarding rule that acts as a route in the VPC network. If the packet's destination matches a Private Service Connect endpoint for global Google APIs, Google Cloud sends the packet to a Google Front End, and evaluation stops at this step.

  5. **Most specific destination** : At the beginning of this step, Google Cloud has disregarded all special routing paths, policy-based routes, subnet routes, and routes for Private Service Connect endpoints for global Google APIs.

Google Cloud determines which applicable static or dynamic routes have the most specific destination that contains the destination IP address of the packet. Google Cloud disregards all routes except those with the most specific destination. For example, `10.240.1.0/24` is a more specific destination than `10.240.0.0/16`.

At the end of this step, your route selection model only contains static or dynamic routes with identical destinations.

  6. **Select only the most favorable custom route type** : In this step, Google Cloud removes all custom routes except the most favorable custom route type. Local custom routes are preferred over NCC dynamic routes, and NCC dynamic routes are preferred over peering custom routes.

The following table summarizes the logic that Google Cloud uses in this step.

Custom route category | What happens  
---|---  
Local dynamic and local static routes | If your route model contains at least one local dynamic or local static route for the destination, Google Cloud removes the following custom route types, if they are present in the route model: 
     * NCC dynamic routes from hybrid spokes, in different VPC networks
     * Peering dynamic routes (imported from other VPC networks connected using VPC Network Peering)  
NCC dynamic routes | If _all_ of the following conditions are met, Google Cloud removes all peering dynamic and peering static routes from the route model: 
     * Your route model _doesn't_ contain any local custom routes for the destination
     * Your route mode does contain at least one NCC dynamic route for the destination
     * The NCC dynamic route comes from from a hybrid spoke in a different VPC network  
Peering dynamic and peering static routes | The least favorable custom route type contains peering custom routes. Peering custom routes for the destination are used only when the route model _doesn't_ contain any local custom routes or NCC dynamic routes for the destination.   
  7. **Select next hops for peering custom routes from a single VPC network** : Next hops for the same destination must be located in the same VPC network. This step _only_ applies if your route model contains peering dynamic or peering static routes that are imported from two or more different VPC networks connected using VPC Network Peering.

Google Cloud uses an internal algorithm to import peering custom routes from a _single_ VPC network. The peer network that Google Cloud selects might change if your VPC network peers with a new VPC network or if it disconnects from an existing peer VPC network.

  8. **Disregard static and dynamic routes with unusable next hops** : This step models situations where Google Cloud disregards next hops that are down or invalid.

     * **Invalid next hop VM IP address specification** : The `next-hop-address` of a static route must match an IP address that is assigned to a VM in the route's VPC network. The IP address must be assigned to the VM's network interface as one of the following:

       * A primary internal IPv4 address
       * An internal IPv6 address
       * An external IPv6 address

If the IP address specified by `next-hop-address` matches a different type of resource (like an alias IP range) or doesn't match any resource, Google Cloud disregards the route.

     * **Next hop VM stopped or deleted** : Google Cloud disregards each static route whose next hop VM instance has been stopped or deleted. This behavior applies to routes whose next hops are specified using either `next-hop-instance` or `next-hop-address`. For more information, see [Behavior when instances are stopped or deleted](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-vm-only-when-stopped-or-deleted).

     * **Invalid next hop load balancer IP address specification** : For static routes that have a next hop load balancer specified by IP address, the IP address must match a forwarding rule of an internal passthrough Network Load Balancer that is located in the route's VPC network or in a peered VPC network. If the next hop IP address matches the forwarding rule of a different type of load balancer or doesn't match any forwarding rule, Google Cloud disregards the route.

     * **Unestablished next hop Classic VPN tunnel** : Google Cloud disregards each static route with a next hop Classic VPN tunnel that doesn't have an active Phase 1 (IKE) security association (SA). For more details, see [Order of routes](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/order-of-routes#static_routing) in the Classic VPN documentation.

     * **Dynamic route with nonfunctional next hop** : Even before the BGP session responsible for programming a dynamic route goes down, Google Cloud disregards a dynamic route if its next hop Cloud VPN tunnel, VLAN attachment, or Router appliance VM isn't functional. This situation generally only exists for a few seconds before the dynamic route is removed when the corresponding Cloud Router BGP session goes down.

Google Cloud doesn't validate whether the guest OS of a next hop VM or a backend VM for a next hop load balancer is processing packets. For more information, see [Considerations common to instance and internal passthrough Network Load Balancer next hops](https://docs.cloud.google.com/vpc/docs/static-routes#instance_next_hops).

  9. **Disregard low priority routes** : This step models how Google Cloud discards all routes except for those with the highest priority.

After this step, your route model might be empty, or it might contain one or more routes. If your model isn't empty, all routes in your model have the following characteristics:

     * Identical priorities
     * Next hops that haven't been disregarded
     * Identical destinations
     * Route types that aren't policy-based or subnet routes
  10. **Select next hops for NCC dynamic routes from a single routing VPC network** : Next hops for an NCC dynamic route destination must be in the same [routing VPC network](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes#routing-vpc). This step _only_ applies if your route model contains NCC dynamic routes from two or more hybrid spokes located in _different_ routing VPC networks.

Google Cloud uses an internal algorithm to select hybrid spokes from a single routing VPC network. The selected hybrid spokes might change if you change the number of routing VPC networks that contain hybrid spokes. To avoid this ambiguity, ensure that NCC dynamic routes have unique priorities in each hybrid spoke if hybrid spokes come from two or more different routing VPC networks.

  11. **Select only the most favorable preference category** : Google Cloud doesn't perform [equal-cost multipath (ECMP)](https://wikipedia.org/wiki/Equal-cost_multi-path_routing) among routes that belong to different preference categories, as defined in this step.

Preference category | Route type and next hop type  
---|---  
First preference (most preferred) | One or more static routes with next hop instances (`next-hop-instance` or `next-hop-address`) or next hop Classic VPN tunnels.  
Second preference | One or more dynamic routes of a single type.  
Third choice | A single static route with next hop internal passthrough Network Load Balancer.  
Google Cloud doesn't perform ECMP among multiple internal passthrough Network Load Balancer next hops. For more information, see [Considerations for internal passthrough Network Load Balancer next hops](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-l4ilb-only).  
Fourth preference (least preferred) | One or more static routes with next hop `default-internet-gateway`.   
  
After this step, your route model might be empty, or it might contain one or more routes. If your model isn't empty, all routes in your model have these characteristics:

     * Identical preference category
     * Identical priorities
     * Next hops that haven't been disregarded
     * Next hops in one VPC network
     * Identical destinations
     * Route types that aren't policy-based or subnet routes
  12. **Send or drop packet** : Depending on the number of routes remaining in the route model, Google Cloud sends or drops the packet:

     * If your route model contains a single route, Google Cloud sends the packet to the next hop, with the following exception:

Next hop internal passthrough Network Load Balancers that don't have global access enabled aren't reachable from regions outside of the load balancer's region. Consequently, if a next hop load balancer _doesn't_ have global access enabled, Google Cloud drops all packets sent from VM instances, VLAN attachments, and Cloud VPN tunnels in regions different from the load balancer's region. To change this behavior, [enable global access](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access).

     * If your route model contains two or more routes, Google Cloud performs ECMP, distributing packets among the next hops. Selection of the next hop depends on a hash calculation and the number of next hops. Google Cloud uses a five-tuple hash if the packet contains port information; otherwise, it uses a three-tuple hash. Consistent next hop selection for a given hash is not guaranteed—Google Cloud might direct packets to a different next hop even if the hash is the same and the route model is unchanged.

     * If your route model is empty, Google Cloud drops the packet with an [ICMP type 3, code 0 (network unreachable) message](https://www.rfc-editor.org/rfc/rfc792.html).




### Unmatched resources in hybrid subnet routes

If your route model contains a hybrid subnet route, and the packet's destination matches an IP address that's associated with a stopped VM, or isn't associated with any resource within the hybrid subnet route's destination range, Google Cloud uses a different process to route the packet. The following steps model the process that Google Cloud uses to route these packets:

  1. Identify the VPC network that contains the hybrid subnet route:

     * The hybrid subnet route and the resource that sends packets to the destination range of the hybrid subnet route might use the same VPC network. In this case, the hybrid subnet route is a local subnet route.

     * The hybrid subnet route and the resource that sends packets to the hybrid subnet route might be in different VPC networks that are connected using VPC Network Peering. In this case, the hybrid subnet route is a peering subnet route.

  2. Start with all routes of the VPC network that contains the hybrid subnet route and then remove the following routes:

     * All policy-based routes
     * All subnet routes
     * All static routes that have network tags
     * All routes whose destinations are broader than and contain the hybrid subnet route that was matched in the first route model
  3. Perform the most specific destination through select only the most favorable preference category steps in the routing order.

  4. Use the following rules to determine if Google Cloud sends or drops the packet:

     * If the route model contains a single route, _and_ the route's next hop is in the same region as the hybrid subnet route, Google Cloud sends the packet to the next hop.

     * If the route model contains two or more routes, Google Cloud performs ECMP among those routes. When a next hop is in the same region as the hybrid subnet route, Google Cloud sends the packet to the next hop.

     * Google Cloud drops the packet with an [ICMP type 3, code 0 (network unreachable) message](https://www.rfc-editor.org/rfc/rfc792.html) if the route model is empty, or if a next hop is in a different region than the hybrid subnet route.

The following routes have next hops in regions different from the hybrid subnet's region, so they always result in packet drops:

     * Dynamic routes learned by Cloud Routers in regions different from the hybrid subnet route's region, even if the dynamic routing mode of the VPC network that contains the Cloud Routers is global
     * Static routes that have next hops in regions different from the hybrid subnet's region, including all internal passthrough Network Load Balancers in different regions even if they have global access enabled



## What's next

  * To create and manage routes, see [Use routes](https://docs.cloud.google.com/vpc/docs/using-routes).
  * To learn more about static routes, see [Static routes](https://docs.cloud.google.com/vpc/docs/static-routes).
  * To get an overview of Google Cloud VPC networks, see [ VPC networks](https://docs.cloud.google.com/vpc/docs/vpc).
  * To create, modify, or delete VPC networks, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
