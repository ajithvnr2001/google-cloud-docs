---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing/
title: Networks and tunnel routing \u00a0|\u00a0 Cloud VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:18:51.123474+00:00
---

# Networks and tunnel routing  |  Cloud VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Networks and tunnel routing Stay organized with collections  Save and categorize content based on your preferences. 

This page describes supported Virtual Private Cloud (VPC) networks and routing options.

For definitions of terms used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms).

## Supported networks

Cloud VPN supports [custom mode VPC networks, auto mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges), and [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy). However, you should consider the following best practices:

  * **Use VPC networks instead of legacy networks.** Legacy networks don't support subnets; the entire network uses a single range of IP addresses. Legacy networks cannot be converted into VPC networks.

  * **Use a custom mode VPC network.** VPC networks in custom mode provide you with full control over the range of IP addresses used by their subnets.

    * If you use Cloud VPN to connect two VPC networks, at least one network _must_ be a custom mode VPC network. [Auto mode VPC networks use the same range of internal IP addresses](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges) for their subnets.

    * Review the [considerations for auto mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#auto-mode-considerations) before using one with Cloud VPN. Auto mode VPC networks automatically create a subnet in each Google Cloud region, including automatically creating new subnets in new regions as they are added. Avoid using the internal IP addresses from the range used by auto mode VPC networks in the network to which Cloud VPN tunnels connect.




## Routing options for VPN tunnels

Classic VPN supports static routing options for VPN tunnels, while HA VPN supports the dynamic routing option. You can use Classic VPN tunnels that use dynamic routing only if the Classic VPN gateway connects to VPN gateway software running inside a Compute Engine VM.

Dynamic routing uses the [Border Gateway Protocol (BGP)](https://wikipedia.org/wiki/Border_Gateway_Protocol).

### Dynamic (BGP) routing

Dynamic routing uses a [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) to automatically manage the exchange of routes by using BGP. A BGP interface on a Cloud Router in the same region as the corresponding Cloud VPN tunnel manages this exchange. The Cloud Router adds and removes routes without requiring that the tunnel be deleted and re-created.

The [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks) of your VPC network controls the behavior of all its Cloud Routers. This mode determines whether the routes learned from your peer network are applied to Google Cloud resources in the same region as the VPN tunnel, or if they are applied in all regions. You control the routes advertised by your peer router or gateway.

The dynamic routing mode also determines whether subnet routes from only the tunnel's region or all regions are shared with your peer router or gateway. In addition to these subnet routes, you can configure [custom route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) on a Cloud Router.

### Static routing

Classic VPN tunnels support policy-based and route-based static routing options. Consider a static routing option only if you cannot use dynamic (BGP) routing or HA VPN.

  * **Policy-based routing.** Local IP ranges (left side) and remote IP ranges (right side) are defined as part of the tunnel creation process.

  * **Route-based VPN.** When you use the Google Cloud console to create a route-based VPN, you only specify a list of remote IP ranges. Those ranges are used _only_ to create routes in your VPC network to peer resources.




You can find more information about these two static routing options in the next section.

**Note:** The dynamic routing mode of a VPC network _only_ affects the behavior of Cloud Routers. It does not affect Cloud VPN policy-based or route-based tunnels.

## Traffic selectors

A traffic selector defines a set of IP address ranges or CIDR blocks used to establish a VPN tunnel. These ranges are used as part of the IKE negotiation for the tunnel. Some literature refers to traffic selectors as _encryption domains_.

There are two types of traffic selectors:

  * The _local traffic selector_ defines the set of _local_ IP ranges (CIDR blocks) from the perspective of the VPN gateway that emits the VPN tunnel. For Cloud VPN tunnels, the local traffic selector defines the set of primary and secondary subnet CIDRs for [subnets](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) in the VPC network, representing the _left side_ of the tunnel.

  * The _remote traffic selector_ defines the set of _remote_ IP ranges (CIDR blocks) from the perspective of the VPN gateway that emits the VPN tunnel. For Cloud VPN tunnels, the remote traffic selector is the _right side_ or peer network.




Traffic selectors are an intrinsic part of a VPN tunnel, used to establish the IKE handshake. If either the local or remote CIDRs need to be changed, the Cloud VPN tunnel and its peer counterpart tunnel must be destroyed and re-created.

**Important:** In Google Cloud, a traffic selector (encryption domain) is _not_ the same thing as a route. When you use the Google Cloud console to create a policy-based or route-based Cloud VPN tunnel, Google Cloud automatically creates the necessary routes to peer networks in your VPC network. If you use the Google Cloud CLI to create a policy-based or route-based Cloud VPN tunnel, routes are _not_ automatically created; you must create the custom static routes manually. For instructions, see [Create a Classic VPN using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns).

### Routing options and traffic selectors

The IP range (CIDR block) values for local and remote traffic selectors depend on the routing option used by the Cloud VPN tunnel.

HA VPN tunnels  
---  
Tunnel  
routing option | Local  
traffic selector | Remote  
traffic selector | Routes  
to the VPC network | Routes  
to the peer network  
Requires  
dynamic (BGP) routing | Always  
`0.0.0.0/0` for IPv4 (single-stack)  
or `0.0.0.0/0,::/0` for IPv4 and IPv6 (dual-stack) or `::/0` for IPv6 (single-stack) | Always  
`0.0.0.0/0` for IPv4 (single-stack)  
or `0.0.0.0/0,::/0` for IPv4 and IPv6 (dual-stack) or `::/0` for IPv6 (single-stack) | Unless modified by [custom advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes), the Cloud Router managing the BGP interface for the Cloud VPN tunnel shares the routes to the subnets in the VPC network according to the [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks) of the network and [quotas and limits for Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/quotas). | Subject to restrictions on [custom routes](https://docs.cloud.google.com/vpc/docs/routes#custom-routes) and the [quotas and limits for Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/quotas), the Cloud Router managing the BGP interface for the Cloud VPN tunnel learns routes sent to it by the peer VPN gateway, and adds them to the VPC network as [custom dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes).  
Classic VPN tunnels  
Tunnel  
routing option | Local  
traffic selector | Remote  
traffic selector | Routes  
to the VPC network | Routes  
to the peer network  
Policy-based routing | Configurable.  
See policy-based tunnels and traffic selectors. | Required.  
See policy-based tunnels and traffic selectors. | You must manually create and maintain the routes to the subnets in your VPC network on your peer routers. | If you use the Google Cloud console to create the policy-based VPN tunnel, [custom static routes](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes) are created automatically. If you use the gcloud CLI to create the tunnel, you must use additional `gcloud` commands to create the routes. For instructions, see [Create a Classic VPN using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns).   
Route-based VPN | Always  
`0.0.0.0/0` | Always  
`0.0.0.0/0` | You must manually create and maintain the routes to the subnets in your VPC network on your peer routers. | If you use the Google Cloud console to create the route-based VPN tunnel, custom static routes are created automatically. If you use the gcloud CLI to create the tunnel, you must use additional `gcloud` commands to create the routes. For instructions, see [Create a Classic VPN using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns).   
  
### Policy-based tunnels and traffic selectors

This section describes special considerations for traffic selectors when you create policy-based Classic VPN tunnels. It does not apply to any other type of Classic VPN or HA VPN tunnel.

You can choose to specify the local traffic selector of a policy-based Cloud VPN tunnel when you create it:

  * **Custom local traffic selector.** You can define the local traffic selector as a set of subnets in the VPC network or a set of [internal IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses) that include your chosen IP ranges of subnets in the VPC network. IKEv1 limits local traffic selectors to a single CIDR.

  * **Custom mode VPC networks.** Specify a custom local traffic selector that consists of a range of internal IP addresses.

  * **Auto mode VPC networks.** If unspecified, the local traffic selector is the primary IP range (CIDR block) of the automatically created subnet in the same region as the Cloud VPN tunnel. Auto mode VPC networks have one subnet per region with well-defined IP ranges.

  * **Legacy networks.** If unspecified, the local traffic selector is defined as the entire RFC 1918 IP address range of the legacy network.




Specify the remote traffic selector of a policy-based Cloud VPN tunnel when you create it. If you use the Google Cloud console to create the Cloud VPN tunnel, custom static routes whose destinations correspond to the CIDRs of the remote traffic selector are automatically created. IKEv1 limits remote traffic selectors to a single CIDR. For instructions, see [Create a Classic VPN using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns).

### Important considerations for traffic selectors

Before you create a Cloud VPN policy-based tunnel, consider the following:

  * Most VPN gateways only pass traffic through a VPN tunnel if the source IP address of a packet fits in the tunnel's local traffic selector, and if the destination IP address of a packet fits in the tunnel's remote traffic selector. Some VPN devices don't enforce this requirement.

  * Cloud VPN supports traffic selector CIDRs of `0.0.0.0/0` or `::/0` (any IP address). To determine if your peer VPN gateway does as well, consult the documentation that came with your peer VPN gateway. Creating a policy-based VPN tunnel with both traffic selectors set to `0.0.0.0/0` or `::/0` is functionally equivalent to creating a route-based VPN.

  * Carefully review multiple CIDRs per traffic selector to learn how Cloud VPN implements IKEv1 and IKEv2 protocols.

  * Cloud VPN disallows editing any traffic selectors after you have created a VPN. To change either the local or the remote traffic selector for a Cloud VPN tunnel, you must delete the tunnel and then recreate it. You do _not_ have to delete the Cloud VPN gateway, though.

  * If you convert an auto mode VPC network to a custom mode VPC network, you might need to delete and re-create the Cloud VPN tunnel (but not the gateway). This might be the case if you add custom subnets, remove any automatically created subnets, or modify the secondary IP ranges of any subnet. Avoid switching the mode of a VPC network that has existing Cloud VPN tunnels. For suggestions, review the [considerations for auto mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#auto-mode-considerations).




For consistent and predictable VPN behavior, do the following:

  * Make both the local and remote traffic selectors as specific as possible.

  * Make the Cloud VPN local traffic selector the same as the remote traffic selector configured for the corresponding tunnel on the peer VPN gateway.

  * Make the Cloud VPN remote traffic selector the same as the local traffic selector configured for the corresponding tunnel on the on-premises VPN gateway.




### Multiple CIDRs per traffic selector

When you create a policy-based Classic VPN tunnel, if you use IKEv2, you can specify multiple CIDRs per traffic selector. Cloud VPN _always_ uses a single Child Security Association (SA), regardless of IKE version.

The following table summarizes Cloud VPN support for multiple CIDRs per traffic selector in policy-based VPN tunnels.

IKE version | Multiple CIDRs per traffic selector  
---|---  
IKEv1 | **No** The IKEv1 protocol only supports a single CIDR per Child SA as defined in RFC 2407 and RFC 2409. Because Cloud VPN requires a single Child SA per VPN tunnel, when you use IKEv1, you can only supply a single CIDR for the local traffic selector and a single CIDR for the remote traffic selector. Cloud VPN does _not_ support creating a VPN tunnel by using IKEv1 with multiple Child SAs, each with a single CIDR.  
IKEv2 | **Yes** , if the following conditions are met: 

  * Your peer VPN gateway uses a single Child SA. All CIDRs for the local traffic selector and all CIDRs for the remote traffic selector _must_ be in a single Child SA.
  * The number of CIDRs that you configure does not cause IKE proposal packets to exceed Cloud VPN's maximum MTU of 1460 bytes. If IKE proposals exceed this MTU, Cloud VPN tunnels don't establish.
  * You don't exceed any restriction for the number of CIDRs supported by your on-premises gateway. For details, consult your gateway vendor's documentation.

A best practice is to use 30 or fewer CIDRs per traffic selector so that you don't create an IKE proposal packet that exceeds the maximum MTU.  
**Important:** When using IKEv2, your peer VPN gateway _must_ accept all of the CIDRs in each traffic selector by using a single Child SA. This is typically done by adding all your local and remote IP ranges into a single "Phase 2" (or "Quick Mode") configuration entry on your device, rather than creating a separate Phase 2 configuration for each pair of IP ranges. Not all VPN gateways support this action. VPN gateways that create a unique Child SA per CIDR are _not_ compatible with Cloud VPN. For more information, see the next section.**Tip:** When using **IKEv2**, check how your on-premises device handles multiple selectors to ensure they are negotiated in a single Child SA. 

**Example:** Suppose you have two local ranges (`10.0.0.0/24` and `10.0.1.0/24`) and one remote range (`192.168.1.0/24`).

  * **Correct:** Create **one** Phase 2 configuration containing both local ranges and the remote range. This results in a single Child SA.
  * **Incorrect:** Creating **two** Phase 2 configurations (one for each local range) results in two Child SAs. In this scenario, the VPN tunnel might fail to establish or experience intermittent connectivity.



### Traffic selector strategies

Consider the following strategies if your on-premises VPN gateway creates multiple Child SAs per VPN tunnel, or if multiple CIDRs per traffic selector would cause an IKE proposal for IKEv2 to exceed 1460 bytes (for details, see Routing options and traffic selectors):

  1. Use dynamic routing for the VPN tunnel. If your peer VPN gateway supports BGP, configure both local and remote traffic selectors for the VPN tunnel to allow any IP address. Use `0.0.0.0/0` for IPv4 only or use `0.0.0.0/0,::/0` for IPv4 and IPv6 traffic. Routes are exchanged automatically between the peer VPN gateway and the Cloud Router associated with your Cloud VPN tunnel. If you can use dynamic routing, consider HA VPN.

  2. Use broad, single CIDR traffic selectors and static tunnel routing:

     * Use a route-based VPN. Both traffic selectors are `0.0.0.0/0` by definition for route-based VPNs. You can create routes that are more specific than the traffic selectors.

     * Use policy-based routing and configure the local and remote traffic selectors to be as broad as possible. For policy-based Cloud VPN tunnels, you can create routes to on-premises networks in your VPC network whose destinations are more specific than the CIDR blocks specified in the remote traffic selectors. Use the gcloud CLI to create the routes separately from the VPN tunnels by following the steps at [Create a Classic VPN using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns).

  3. Use policy-based routing to create multiple Cloud VPN tunnels so that each tunnel only has one CIDR block for its local traffic selector and one CIDR block for its remote traffic selector. Configure the on-premises counterpart tunnel in a similar way. Cloud VPN supports multiple tunnels per gateway; however, using multiple tunnels has some implications:

     * Your peer VPN gateway must offer separate external IP addresses to which each Cloud VPN tunnel can connect. Tunnels on the same Classic VPN gateway must connect to unique peer gateway IP addresses. Your peer VPN gateway might also require that its tunnels connect to unique IP addresses. In some situations, you need to create a separate Cloud VPN gateway per Cloud VPN tunnel.
     * When you use the Google Cloud console to create route-based or policy-based Cloud VPN tunnels, routes to the peer network are automatically created in addition to the tunnel. If routes are automatically created for multiple VPN tunnels that each use the same remote traffic selectors—as is the case if you create route-based VPNs—you can have multiple routes in your VPC network, all with identical destinations but different next hops. This can lead to unpredictable or unexpected behavior because traffic is delivered to a VPN tunnel according to the [applicability and order of routes](https://docs.cloud.google.com/vpc/docs/routes#instancerouting). If you don't use dynamic (BGP) tunnel routing, create and review static routes in both your VPC network and your peer network.



## What's next

  * To learn about the basic concepts of Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
