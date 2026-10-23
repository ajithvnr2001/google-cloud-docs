---
url: https://docs.cloud.google.com/network-connectivity/quotas/
title: Quotas and limits \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:53.234596+00:00
---

# Quotas and limits  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Resources ](https://docs.cloud.google.com/network-connectivity/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This page describe quotas and limits for Network Connectivity products. To change a quota, see [Request additional quota](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas#requesting-additional-quota). _Limits_ can't generally be increased unless specifically noted.

## Cloud VPN

### Quotas

This table covers important quotas per project. For other quotas, see the Google Cloud console [**Quotas** page](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com).

Item | Quota | Notes  
---|---|---  
VPN gateways per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/vpn_gateways_per_region) | For HA VPN only   
External VPN gateways | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/external_vpn_gateways) | For HA VPN only  
VPN tunnels per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/vpn_tunnels_per_region) | This quota represents the combined total number of Classic VPN tunnels and HA VPN tunnels.  
Routers | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/routers) |  This quota represents the number of Cloud Routers that you can create within your project, in any network and region. Networks also have a limit on the number of Cloud Routers in any given region. For more details, see [Cloud Router quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas). Subject to the Cloud Router quotas and limits, the number of Cloud Routers is independent of the type of Cloud VPN gateway, Classic VPN or HA VPN, that a tunnel is attached to. The quota is applied the same to either type of gateway.  
Target VPN gateways per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/target_vpn_gateways_per_region) | For Classic VPN only  
Forwarding rules | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/forwarding_rules) | For Classic VPN only  
  
### Limits

The following limits apply to Cloud VPN. In this table, _VPN tunnel_ means either a Classic VPN tunnel or an HA VPN tunnel. Unless otherwise stated, these limits cannot be increased.

Item | Limit | Notes  
---|---|---  
Bandwidth per VPN tunnel | 250,000 packets per second for the sum of ingress and egress |  250,000 packets per second is roughly equivalent to 1 Gbps to 3 Gbps, depending on the average packet size within the tunnel. Traffic is throttled once the limit is reached. For more details, see [Network bandwidth](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#network-bandwidth).  
  
### Known issues

Be aware of the following issues:

  * Google Cloud resources specific to HA VPN are not yet displayed in [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview) or [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center). These resources include `compute.vpnGateways` and `compute.externalVpnGateways`. However, the `compute.vpnTunnels` resource is listed in both locations and is required for a working HA VPN connection.

  * To view Cloud Monitoring metrics for HA VPN, use Metrics Explorer. For more information, see [Viewing logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics#vpn-monitoring-issue).

  * When setting up VPN tunnels to AWS, [use IKEv2 and configure fewer IKE transform sets](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#aws-known-issue).




## Cloud Interconnect

### Quotas

This table highlights important quotas for each project. For other quotas, see the [Google Cloud console **Quotas** page](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com).

Item | Quota | Notes  
---|---|---  
Cloud Interconnect connections | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/interconnects) | The number of Dedicated Interconnect connections per project. Cloud Interconnect connections aren't associated with regions or VPC networks.  
VLAN attachments | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/interconnect_attachments_per_region) | The number of VLAN attachments that you can configure in each region for your project. This includes VLAN attachments for both Dedicated Interconnect and Partner Interconnect. In addition to this quota, the _VLAN attachments per Interconnect_ applies.  
VLAN attachments per Interconnect | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/interconnect_attachments_per_interconnect) | The number of VLAN attachments that you can configure on a single interconnect connection.  
VLAN attachments total Mbps | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/interconnect_attachments_total_mbps) | The maximum bandwidth capacity of all VLAN attachments in a given region for a given project, irrespective of their relationship with Cloud Interconnect connections. In addition to this quota, the limits described in the **Limits** table apply.  
Cross-site networks | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/cross_site_networks) | The number of cross-site networks per project.  
Wire groups | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/wire_groups) | The number of wire groups per project. In addition to this quota, the _Wire groups per Interconnect_ applies.  
Wire groups per Interconnect | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/wire_groups_per_interconnect) | The number of wire groups that you can configure on a single Interconnect connection.  
Wire groups unmetered bandwidth per Interconnect metro pair | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/wire_groups_gold_unmetered_bandwidth_gbps) | The maximum bandwidth capacity between a pair of Interconnect metros, in Gbps. This quota includes both traffic directions. There is a unique quota for each pair of metros as identified in the **Dimensions** column in the format metro-a|metro-b.  
Cloud Routers | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/routers) | The number of Cloud Routers that you can create within your project, in any network and region. Networks also have a _limit_ on the number of Cloud Routers in any given _region_. For more details, see [Cloud Router quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas).  
Transports | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-transports) | The number of partner Cross-Cloud Interconnect transport resources that you can create in a single project per region.  
Number of 500 Mbps transports | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-transports-500mbps) | The number of 500 Mbps speed partner Cross-Cloud Interconnect transport resources that you can create in a single project per region.  
Transport bandwidth | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-transport-bandwidth) | Bandwidth per partner Cross-Cloud Interconnect transport resource that you can create in a single project per region.  
  
### Limits

The following limits apply to Cloud Interconnect connections, VLAN attachments, and cross-site network wires. Unless otherwise stated, these limits can't be increased.

Item | Limit | Notes  
---|---|---  
Maximum number of physical circuits per Cloud Interconnect connection | 8 x 10 Gbps (80-Gbps) circuits or  
8 x 100 Gbps (800-Gbps) circuits or  
8 x 400 Gbps (3200-Gbps) circuits | A Cloud Interconnect connection is a logical connection to Google, made up of one or more physical circuits. You can request one of the following circuit choices:

  * Up to 8 x 400 Gbps (3200-Gbps) circuits.
  * Up to 8 x 100 Gbps (800-Gbps) circuits.
  * 10-Gbps increments up to eight circuits (80 Gbps) to increase the maximum total bandwidth of all VLAN attachments that use the Cloud Interconnect connection to 80 Gbps. To determine the bandwidth, multiply the number of physical circuits by the bandwidth per circuit (10 Gbps).

  
Maximum bandwidth per VLAN attachment | 

  * Dedicated Interconnect, Cross-Cloud Interconnect: Capacities from 50 Mbps to 400 Gbps
  * Partner Interconnect, Cross-Site Interconnect: Capacities from 50 Mbps to 100 Gbps

| The maximum possible bandwidth per VLAN attachment depends on the bandwidth capacity that you order. For capacities, see the [pricing page](https://cloud.google.com/network-connectivity/docs/interconnect/resources/pricing). For Partner Interconnect, not all service providers offer all capacities. The throughput of individual flows on a VLAN attachment is limited. To achieve maximum throughput, you must use multiple five-tuple flows (for example: 10+) with packet sizes within the MTU of the VLAN attachment.  
Maximum bandwidth per traffic flow on a VLAN attachment |  10 Gbps Even if you configure your attachment with a higher bandwidth, an individual traffic flow might be limited to the maximum defined for an attachment. | A traffic flow to a destination in a VPC network is identified by either a five-tuple hash for non-fragmented packets or a three-tuple hash for fragmented packets. In addition, traffic flows that use Private Google Access for on-premises hosts are identified by a three-tuple hash.

  * A five-tuple hash consists of a protocol, source IP address, source port, destination IP address, and destination port.
  * A three-tuple hash consists of a protocol, source IP address, and destination IP address.

The following cases describe where the maximum bandwidth is lower than the 10 Gbps limit:

  * If the bandwidth capacity of your VLAN attachment is less than the maximum for the attachment, the bandwidth per traffic flow is limited by the bandwidth of the VLAN attachment.
  * If you reach the _maximum packet rate per traffic flow_ (as described in the next section).

  
Maximum packet rate per traffic flow on a VLAN attachment | 1,000,000 packets per second (pps) | The maximum rate of packets per traffic flow, identified by a five-tuple hash for non-fragmented packets and by a three-tuple hash for fragmented packets (as described in the previous section).  
[Maximum transmission unit (MTU)](https://wikipedia.org/wiki/Maximum_transmission_unit) | 

  * 1,440 bytes
  * 1,460 bytes
  * 1,500 bytes
  * 8,896 bytes

| Depending on the VLAN attachment MTU setting, the size of the largest IP address packet that can be transmitted over a VLAN attachment. For more information, see [Cloud Interconnect MTU](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#interconnect-mtu).  
Maximum lifetime of (Partner Interconnect) VLAN attachment pairing key | 28 days | The maximum amount of time that can pass between generating a (Partner Interconnect) VLAN attachment pairing key and successful attachment provisioning by the service provider. If a pairing key is no longer valid, you delete and create a new pairing key for the Partner Interconnect service provider to use.  
Maximum bandwidth per wire | 10 Gbps | This limit can be increased. Requires confirmation that you won't exceed the limit for the _Maximum bandwidth per traffic flow on a wire_. To request an update to this limit, [file a support case](https://cloud.google.com/support-hub).  
Maximum bandwidth per traffic flow on a wire | 10 Gbps | A traffic flow is defined by one of the following: If you configure end-to-end MACsec encryption between your on-premises routers, a traffic flow is defined by a two-tuple hash that consists of a source MAC address and destination MAC address. Otherwise, a traffic flow is defined by an eight-tuple hash that consists of a source MAC address, destination MAC address, source IP address, destination IP address, physical interface of Google's edge router, IP protocol number, TCP/UDP source port, and TCP/UDP destination port.  
Cloud Router limits |  | Because Dedicated Interconnect and Partner Interconnect require Cloud Router, all the Cloud Router quotas and limits apply. There are limits on the maximum number of learned routes and on the number of advertised routes. For more information, see the Cloud Router [Quotas and limits page](https://docs.cloud.google.com/network-connectivity/docs/router/quotas).  
  
## Cloud Router

### Quotas

This table covers important quotas per project. For other quotas, see the [Google Cloud console **Quotas & System Limits** page](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com).

Item | Quota | Notes  
---|---|---  
Cloud Routers per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/routers) | Regardless of quota, each network is limited to five Cloud Routers per region. See Limits.  
Unique Cloud Router dynamic route prefixes from own region per region per VPC network The maximum number of assured unique destination prefixes for learned routes to be applied to subnets in a given region by all Cloud Routers in _the same_ region. This is referred to as a region's _from-own-region_ quota. | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/cloud_router_prefixes_from_own_region_per_region_per_vpc_network) |  Both IPv4 and IPv6 prefixes count toward this quota. All learned routes count toward this quota, including [custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/learned-routes) and BGP-received routes. Routes are grouped by unique destinations. Routes with identical destinations but different next hops only count as a single destination. Routes with identical destinations and identical next hops also only count as a single destination. For networks in _global dynamic routing mode_ , it is possible to reach one of the unique dynamic route prefix quotas without reaching the other. If either of the quotas has been exceeded, you may experience intermittent connectivity issues when routes are dropped. For details, see the learned route example. For more information about these quotas, including metrics that you can use to understand your current usage, see [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshoot-bgp-routes#check-quotas-and-limits).  
_Only applicable to VPC networks in[global dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#dynamic-routing-mode)._ Unique Cloud Router dynamic route prefixes from other regions per region per VPC network The maximum number of assured unique destinations for learned routes that can be applied to subnets in a given region by Cloud Routers from _different_ regions. This is referred to as a region's _from-other-regions_ quota. | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/cloud_router_prefixes_from_other_regions_per_region_per_vpc_network) |  Both IPv4 and IPv6 prefixes count toward this quota. All learned routes count toward this quota, including [custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/learned-routes) and BGP-received routes. Routes are grouped by unique destinations. Routes with identical destinations but different next hops only count as a single destination. Routes with identical destinations and identical next hops also only count as a single destination. For networks in _global dynamic routing mode_ , it is possible to reach one of the unique dynamic route prefix quotas without reaching the other. If either of the quotas has been reached, you might experience intermittent connectivity issues when routes are dropped. For details, see the learned route example. For more information about these quotas, including metrics that you can use to understand your current usage, see [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshoot-bgp-routes#check-quotas-and-limits).  
  
### Limits

The following limits for Cloud Router apply to Virtual Private Cloud (VPC) networks. Unless otherwise stated, these limits cannot be increased.

Item | Limit | Notes  
---|---|---  
Maximum number of Cloud Routers per combination of VPC network and region | 5 | If you have sufficient project quota, you can create up to five Cloud Routers in a given VPC network and region.   
Maximum number of BGP peers for each Cloud Router in a given VPC network and region | 128 | The BGP peer can be any of the following: 

  * A [ Cloud VPN tunnel using dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#dynamic-routing)
  * A VLAN attachment for any of the following: 
    * [ Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview)
    * [ Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview)
    * [ Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview)
  * A [ Router appliance within Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview)

  
Maximum number of prefixes that Cloud Router accepts from a single BGP peer | 5,000 | If a BGP peer advertises more than 5,000 prefixes, Cloud Router resets the BGP session.  
For a given Cloud Router, the maximum size of all policy resources. | 35kB (35,000 bytes) |   
Maximum number of terms of all applied BGP route policies within a single BGP peer or direction | 1,000 | This limit isn't split across resources, but combined. There isn't a limit on the size of a single match or action expression, number of actions in a term, number of terms in a single policy, or the number of policies.  
For a given Cloud Router, the maximum number of _subnet route_ advertisements per BGP session | No restriction | Cloud Routers don't have a limit for the number of subnet routes they can advertise. The number of subnet routes are determined by the number of subnets ranges, which are controlled by [VPC network quotas and limits](https://docs.cloud.google.com/vpc/docs/quota).  
For a given Cloud Router, the maximum number of _custom advertised routes_ per BGP session | 200 | If the custom advertised routes are identical for all BGP sessions on a Cloud Router, this limit represents the total number of _unique_ IPv4 and IPv6 custom advertised routes for the Cloud Router. In this case, each session receives the same set of custom advertised routes.  
The maximum size for a single match expression literal used in a BGP route policy, combined across `destination` and `community` matches. | 100 match elements | For example, `destination.inAnyRange([prefix(...), prefix(..)]) && communities.matchesEvery(['0:0', '1:1'])` has four match elements and ` destination == ... || destination == ...` has two match elements. There isn't a limit on the number of actions in a term, number of terms in a single BGP route policy, or the number of BGP route policies.  
The maximum number of action elements allowed in an action operation that accepts a list in BGP route policies. | 10 action elements | The following action operations accept lists:

  * `asPath.prependSequence`
  * `communities.add`
  * `communities.remove`
  * `communities.replaceAll`

There isn't a limit on the number of actions in a term, number of terms in a single BGP route policy, or the number of BGP route policies.  
For a given Cloud Router, the maximum number of named sets. | 500 | Named sets contribute to the overall limit on the size of policy related resources on the router.  
The maximum number of elements per named set. | 1000 |   
Maximum queries per minute for `list-bgp-routes` calls on a single Cloud Router | 1500 | This quota is from `compute.googleapis.com/list_requests_per_region`. For more information, see [ Rate quotas](https://docs.cloud.google.com/compute/api-quota#api-rate-limits-global).  
Maximum number of BGP route policies per Cloud Router. | 500 |   
For a given BGP session, the maximum number of custom learned routes | 10 |  For more information about this feature, see [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/custom-learned-routes).   
For a given region in a VPC network, the maximum number of unique IP prefixes that can be configured as custom learned routes; this limit allows for the same ranges to be used on multiple peers  | 10 |  For more information about this feature, see [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/custom-learned-routes).   
  
### Learned route example

The following examples illustrate the route dropping behavior that you can encounter when the from-own-region quota or the from-other-regions quota is exceeded.

Suppose you have Cloud Routers in the `us-east1` region and Cloud Routers in the `us-west1` region in the same VPC network, and global dynamic routing is enabled. Each Cloud Router in each region learns 250 _unique_ destinations. For illustrative purposes of this example, each Cloud Router in each region doesn't learn any of the same destinations.

Regardless of which Cloud Routers learn the routes within each region, each region's from-own-region quota is exhausted because 250 of 250 unique destinations are learned by the Cloud Routers in each region. The from-other-regions quotas for both regions are also exhausted because each Cloud Router imports 250 unique destinations from the other region. If the example VPC network used regional dynamic routing, the from-other-regions quotas in each region doesn't apply because regional dynamic routing mode instructs the VPC network to only create dynamic routes in the region that matches the route's next hop.

### Exceeding a region's from-own-region quota

Suppose your on-premises router that's connected to a Cloud Router in `us-west1` advertises a 251st destination. Cloud Routers in the `us-west1` region pick 250 of the 251 unique destinations following a [deterministic route order](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#deterministic). These routers send those 250 unique destinations to the VPC network, creating 250 dynamic routes in the `us-west1` region.

Because the VPC network uses global dynamic routing mode, it also creates no more than 250 dynamic routes _in every other region_ , subject to each other region's from-other-regions unique destination quota. The next section describes what happens in other regions in more detail.

### Exceeding a region's from-other-regions quota

When 251 unique destinations are learned by Cloud Routers in the `us-west1` region, 250 of the 251 unique destinations from `us-west1` are made available to resources in the `us-east1` region because the `us-east1` region's from-other-regions quota can only accept 250 unique destinations.

Suppose that you create a Cloud Router in a third region, `us-central1`, in the same VPC network. Suppose that the new Cloud Router learns 10 unique destinations from its BGP peer. Although the `us-central1` region's from-own-region quota has not been exceeded, the `us-central1` region's from-other-regions quota has been exceeded because a total of 500 unique destinations are provided by the other two regions (250 from `us-east1` and a different 250 from `us-west1`).

On a region-by-region basis, the [deterministic route order](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#deterministic) selects routes for no more than 250 unique destinations in other regions, as indicated in the following table.

Region |  Unique destinations local to the region   
(usage of region's from-own-region quota)  |  Unique destinations from other regions   
(usage of region's from-other-regions quota)  |  **us-west1** |  251 received. 250 of the 251 are selected, and one of the 251 is dropped by the deterministic route order. 250 dynamic routes with next hops in `us-west1` are created in `us-west1`. The 250 selected prefixes are shared with other regions. |  260 received (250 from `us-east1`, 10 from `us-central1`). 250 of the 260 are selected, and 10 of the 260 are dropped by the deterministic route order. 250 dynamic routes with next hops outside of `us-west1` are created in `us-west1`.  
---|---|---  
**us-east1** |  250 received. All 250 are selected by the deterministic route order. 250 dynamic routes with next hops in `us-east1` are created in `us-east1`. All 250 selected prefixes are shared with other regions. |  260 received (250 from `us-west1`, 10 from `us-central1`). 250 of the 260 are selected, and 10 of the 260 are dropped by the deterministic route order. 250 dynamic routes with next hops outside of `us-east1` are created in `us-east1`.  
**us-central1** |  10 received. All 10 are selected by the deterministic route order. 10 dynamic routes with next hops in `us-central1` are created in `us-central1`. All 10 selected prefixes are shared with other regions. |  500 received (250 from `us-west1`, 250 from `us-east1`). 250 of the 500 are selected, and 250 of the 500 are dropped by the deterministic route order. 250 dynamic routes with next hops outside of `us-central1` are created in `us-central1`.  
  
Although the `us-central1` region's from-other-regions quota is exceeded, its from-own-region quota can accept destinations whose next hops are in the `us-central1` region.

### Deterministic route dropping behavior

Cloud Router implements a deterministic route dropping behavior based on the subnet mask length and lexicographic characteristics of each prefix received. Within each region, the following process applies independently to the region's from-own-region destinations list and the region's from-other-regions unique destinations list:

  * The list is sorted first from shortest to longest subnet mask length, then IPv4 before IPv6, then lexicographically. For example, `10.0.0.0/8` comes before `10.2.1.0/24`, which comes before `10.99.1.0/24`.

  * The first 250 entries in the list are preserved. All others are discarded.




As shown in [exceeding a region's from-other-regions quota](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#exceeding_region_other), the deterministic dropping behavior is applied _independently_ to each region's from-own-region quota and each region's from-other-regions quota.

The deterministic route dropping behavior has the following consequences:

  * If the mask lengths are equal, IPv6 prefixes are discarded before IPv4 prefixes.

  * If the set of prefixes learned in each region remains constant, Google Cloud programs a consistent set of local dynamic routes in every region, subject to the dynamic routing mode of the VPC network. This consistency, including which routes are dropped by Cloud Router, is preserved when Cloud Router tasks restart.




### Avoiding route dropping

During route dropping, you lose connectivity for the prefixes that are dropped. To avoid route dropping, monitor each region's from-own-region and from-other-regions prefix usage by using Cloud Monitoring or Cloud Logging, and make sure not to advertise more unique destinations than each quota.

Consider summarizing routes to reduce the number of unique destinations. For example, if you have the four subnets `10.10.0.0/24`, `10.10.1.0/24`, `10.10.2.0/24`, and `10.10.3.0/24`, then you can summarize them as one prefix, `10.10.0.0/22`.

If summarization isn't possible, contact your Google Cloud Sales team to discuss alternative options.

## Router appliance

### Quotas

Quotas that apply to network routes for Cloud Router also apply to routes for Router appliance spokes attached to NCC hubs.

For more information, see [Cloud Router quotas](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#quotas).

### Limits

The following limits for Cloud Router also apply to Router appliance:

  * The maximum number of Cloud Routers per combination of VPC network and region
  * The maximum number of BGP peers for each Cloud Router in a given VPC network and region



For more information, see [Cloud Router limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

## Network Connectivity Center

### Quotas

Quotas that apply to network routes for Cloud Router also apply to routes for NCC hubs and spokes. For more information, see Cloud Router [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas).

Item | Quota | Notes  
---|---|---  
Number of hubs per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/global-per-project-hubs) | Per project, global  
Number of Cloud VPN tunnel spokes per project per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-vpn-tunnel-spokes) | Per project in each region; only HA VPN tunnels are supported  
Number of Cloud Interconnect VLAN attachment spokes per project per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-interconnect-attachment-spokes) | Per project in each region  
Number of Router appliance spokes per project per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-router-appliance-instance-spokes) | Per project in each region  
Number of VPC spokes per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/global-per-project-vpc-spokes) | Includes VPC spokes (_edge_ and _center_ spokes combined) even if they are not connected to any hub  
Number of _active_ VPC spokes per hub | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/active_vpc_spokes_per_hub) | Only applicable to VPC spokes that have been accepted into a hub; not applicable to VPC spokes that are pending review or that have been rejected  
Number of subnet routes _per_ hub route table | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/routes_per_route_table) | Only applicable to hubs with VPC spokes  
Number of dynamic routes _per_ hub | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/dynamic_route_prefixes_per_hub_route_table_per_route_region) | Applicable to all VPC spokes  
Number of routing VPC networks _per_ hub | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/routing_vpcs_per_hub) |   
Number of static routes with an internal passthrough Network Load Balancer IP address as the next hop _per_ hub | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/static_routes_per_hub) | Per project, global  
Number of Private Service Connect forwarding rules _per_ hub | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/psc_ilb_consumer_forwarding_rules_per_hub) | Applicable to all VPC spokes  
  
### Secure Access Connect quotas

Item | Quota | Notes  
---|---|---  
Number of Secure Access Connect realms per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&metric=networksecurity.googleapis.com/sac-realms-per-project) | Per project  
Number of Secure Access Connect attachments per project per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&metric=networksecurity.googleapis.com/sac-attachments-per-project-per-region) | Per project, per region  
Number of Secure Access Connect attachments per project per realm per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&metric=networksecurity.googleapis.com/sac-attachments-per-project-per-sac-realm-per-region) | Per project, per realm, per region  
Number of Secure Access Connect attachments per project per region per gateway spoke | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&metric=networksecurity.googleapis.com/sac-attachments-per-project-per-region-per-gateway-spoke) | Per project, per region, per gateway spoke  
  
### Limits

Network Connectivity Center enforces the following usage limits.

Item | Value  
---|---  
Number of VPN tunnels that can be linked to a spoke | 8  
Number of VLAN attachments that can be linked to a spoke | 6  
Number of router appliance instances that can be linked to a spoke | 8  
Number of active VPC spokes per hub | 250  
Maximum number of VPC spokes (active and inactive) per hub | 1,000  
Number of include or exclude export CIDR ranges per spoke | 16  
  
## Manage quotas

Google Cloud enforces quotas on resource usage for various reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help users who are exploring Google Cloud with the [free tier](https://docs.cloud.google.com/free/docs/gcp-free-tier) to stay within their trial. 

All projects start with the same quotas, which you can change by requesting additional quota. Some quotas might increase automatically based on your use of a product.

### Permissions

To view quotas or request quota increases, Identity and Access Management (IAM) principals need one of the following roles. 

Task | Required role  
---|---  
Check quotas for a project | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) (`roles/servicemanagement.quotaViewer`)

  
Modify quotas, request additional quota | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) (`roles/servicemanagement.quotaAdmin`)
  * A custom role with the `serviceusage.quotas.update` permission

  
  
### Check your quota

### Console

  1. In the Google Cloud console, go to the **Quotas** page. 

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. To search for the quota that you want to update, use the **Filter table**. If you don't know the name of the quota, use the links on this page instead.



### gcloud

Using the Google Cloud CLI, run the following command to check your quotas. Replace `PROJECT_ID` with your own project ID.
    
    
        gcloud compute project-info describe --project PROJECT_ID

To check your used quota in a region, run the following command:
    
    
        gcloud compute regions describe example-region
        

### Errors when exceeding your quota

If you exceed a quota with a `gcloud` command, `gcloud` outputs a `quota exceeded` error message and returns with the exit code `1`.

If you exceed a quota with an API request, Google Cloud returns the following HTTP status code: `413 Request Entity Too Large`. 

### Request additional quota

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

### Resource availability

Each quota represents a maximum number for a particular type of resource that you can create, if that resource is available. It's important to note that quotas _don't_ guarantee resource availability. Even if you have available quota, you can't create a new resource if it is not available.

For example, you might have sufficient quota to create a new regional, external IP address in a given region. However, that is not possible if there are no available external IP addresses in that region. Zonal resource availability can also affect your ability to create a new resource.

Situations where resources are unavailable in an entire region are rare. However, resources within a zone can be depleted from time to time, typically without impact to the service level agreement (SLA) for the type of resource. For more information, review the relevant SLA for the resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
