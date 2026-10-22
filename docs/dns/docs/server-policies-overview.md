---
url: https://docs.cloud.google.com/dns/docs/server-policies-overview/
title: DNS server policies \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:39.892412+00:00
---

# DNS server policies  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/server-policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  DNS server policies Stay organized with collections  Save and categorize content based on your preferences. 

A DNS server policy lets you configure which DNS servers to use when resolving domain names for your Google Cloud resources. You can use DNS server policies to control DNS resolution within a specific Virtual Private Cloud (VPC) network. A DNS server policy specifies inbound DNS forwarding, outbound DNS forwarding, or both. An inbound DNS server policy permits inbound DNS forwarding, while an outbound DNS server policy is one way to implement outbound DNS forwarding.

You can also [configure DNS64](https://docs.cloud.google.com/dns/docs/configure-dns64) to enable IPv6-only VM instances to communicate with IPv4-only destinations.

IPv6-only VPC subnets don't support inbound DNS server policies. However, you can configure outbound DNS server policies for your IPv6-only VM instances.

## Inbound server policies

Each VPC network provides Cloud DNS name resolution services to virtual machine (VM) instances that have a network interface (vNIC) attached to the VPC network. When a VM uses its metadata server `169.254.169.254` as its name server, Google Cloud searches for Cloud DNS resources according to the [VPC network name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order#vpc_steps).

To make a VPC network's name resolution services available to on-premises networks that are connected to the VPC network by using Cloud VPN tunnels, Cloud Interconnect VLAN attachments, or Router appliances, you can use an _inbound server policy_.

When you create an inbound server policy, Cloud DNS creates _inbound server policy entry points_ in the VPC network to which the server policy is applied. Inbound server policy entry points are internal IPv4 addresses sourced from the primary IPv4 address range of _every_ subnet in the applicable VPC network, except for subnets with specific `--purpose` data, such as proxy-only subnets for certain load balancers and subnets used by Cloud NAT for Private NAT.

For example, if you have a VPC network that contains two subnets in the same region and a third subnet in a different region, when you configure an inbound server policy for the VPC network, Cloud DNS uses a total of three IPv4 addresses as inbound server policy entry points, one per subnet.

**Note:** You can't use inbound server policies with [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy) because these policies require VPC networks.

For information about how to create an inbound server policy for a VPC, see [Create an inbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-in).

### Network and region for inbound queries

To process DNS queries that are sent to inbound server policy entry points, Cloud DNS associates the query with a VPC network and a region:

  * The associated VPC network for a DNS query is the VPC network that contains the Cloud VPN tunnel, Cloud Interconnect VLAN attachment, or network interface of the Router appliance that receives the packets for the DNS query.

    * Google recommends creating an inbound server policy in the VPC network that connects to your on-premises network. That way, the inbound server policy entry points are located in the same VPC network as the Cloud VPN tunnels, Cloud Interconnect VLAN attachments, or Router appliances that connect to the on-premises network.

    * Inbound DNS forwarding IP addresses are not reachable across VPC Network Peering or Network Connectivity Center (NCC) boundaries and require a local policy. To ensure successful resolution, you must do the following:

      * **Deploy a local policy**. Create the inbound DNS forwarding policy directly in the VPC network that receives the queries from your hybrid connection (Cloud VPN, Cloud Interconnect, or Router appliance).
      * **Use DNS peering**. To resolve records located in a peered VPC network, create a DNS peering zone in the local VPC network that targets the remote network.
    * If an on-premises network sends queries to an inbound server policy using VPC Network Peering, the network with the inbound server policy must contain a VM, a VLAN attachment, or a Cloud VPN tunnel located in the same region as the incoming queries.

  * The associated region for a DNS query is _always_ the region that contains the Cloud VPN tunnel, Cloud Interconnect VLAN attachment, or network interface of the Router appliance that receives the packets for the DNS query, _not_ the region of the subnet containing the inbound server policy entry point.

    * For example, if the packets for a DNS query enter a VPC network using a Cloud VPN tunnel located in the `us-east1` region and are sent to an inbound server policy entry point in the `us-west1` region, the associated region for the DNS query is `us-east1`.
    * As a best practice, send DNS queries to the IPv4 address of an inbound server policy entry point in the same region as the Cloud VPN tunnel, Cloud Interconnect VLAN attachment, or Router appliance.
    * The associated region for a DNS query is important if you use geolocation routing policies. For more information, see [Manage DNS routing policies and health checks](https://docs.cloud.google.com/dns/docs/zones/manage-routing-policies).



### Inbound server policy entry point route advertisement

Because inbound server policy entry point IP addresses are taken from the primary IPv4 address ranges of subnets, Cloud Routers advertise those IP addresses when the Border Gateway Protocol (BGP) session for a Cloud VPN tunnel, Cloud Interconnect VLAN attachment, or Router appliance is configured to use the Cloud Router [default advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am-default). You can also configure a BGP session to advertise inbound server policy entry point IP addresses if you use the Cloud Router [custom advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am-custom) in one of the following ways:

  * You advertise subnet IP address ranges in addition to your custom prefixes.
  * You include inbound server policy entry point IP addresses in your custom prefix advertisements.



## Outbound server policies

You can modify the Cloud DNS name resolution order of a VPC network by creating an _outbound server policy_ that specifies a list of _alternative name servers_. When a VM uses its metadata server `169.254.169.254` as its name server, and when you have specified alternative name servers for a VPC network, Cloud DNS sends all queries to the alternative name servers _unless_ the queries are matched by a Google Kubernetes Engine cluster-scoped response policy or GKE cluster-scoped private zone.

When two or more alternative name servers exist in an outbound server policy, Cloud DNS ranks the alternative name servers and queries them as described in the first step of the VPC name resolution order. Important: Review the [VPC network resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order#vpc_steps) carefully. Use of alternative name servers disables the resolution of many Cloud DNS features, and can also affect the resolution of public DNS queries, depending on the configuration of the alternative name servers. For more information about other strategies for outbound DNS forwarding, see [DNS forwarding methods](https://docs.cloud.google.com/dns/docs/overview#dns-forwarding-methods) in the Cloud DNS overview. For information about how to create outbound server policies, see [Creating an outbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-out). 

### Alternative name server types, routing methods, and addresses

Cloud DNS supports the following alternative name servers and offers standard or private routing methods for connectivity.

Alternative name server type | Standard routing supports | Private routing supports | Query source address range  
---|---|---|---  
**Type 1 name server** An [internal IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) of a Google Cloud VM in _the same_ VPC network where the outbound server policy is defined. | Only RFC 1918 IP addresses—traffic always routed through an authorized VPC network. | Any internal IP address, such as an RFC 1918 private address, a non-RFC 1918 private IP addresses, or a privately reused external IP address, except for a prohibited alternative name server IP address—traffic always routed through an authorized VPC network. | `35.199.192.0/19`  
**Type 2 name server** An IP address of an on-premises system, connected to the VPC network with the outbound server policy, using Cloud VPN or Cloud Interconnect. | Only RFC 1918 IP addresses—traffic always routed through an authorized VPC network. | Any internal IP address, such as an RFC 1918 private address, a non-RFC 1918 private IP addresses, or a privately reused external IP address, except for a prohibited alternative name server IP address— traffic always routed through an authorized VPC network. | `35.199.192.0/19`  
**Type 3 name server** An [external IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) of a DNS name server accessible to the internet _or_ the external IP address of a Google Cloud resource—for example, the external IP address of a VM in another VPC network. | Only internet-routable external IP addresses—traffic always routed to the internet or to the external IP address of a Google Cloud resource. | Private routing isn't supported. | [Google Public DNS source ranges](https://developers.google.com/speed/public-dns/faq#locations)  
  
Cloud DNS offers two routing methods for querying alternative name servers:

  * **Standard routing**. Cloud DNS determines the type of the alternative name server using its IP address, and then uses either private or public routing:

    * If the alternative name server is an RFC 1918 IP address, Cloud DNS classifies the name server as either a _Type 1_ or _Type 2_ name server, and routes queries through an authorized VPC network (private routing). 
    * If the alternative name server is _not_ an RFC 1918 IP address, Cloud DNS classifies the name server as _Type 3_ , and expects the alternative name server to be internet accessible. Cloud DNS routes queries over the internet (public routing). 
  * **Private routing**. Cloud DNS treats the alternative name server as either _Type 1_ or _Type 2_. Cloud DNS always routes traffic through an authorized VPC network, regardless of the alternative name server's IP address (RFC 1918 or not).


**Important:** A _Type 1_ alternative name server _cannot_ be located in a VPC network that's connected to the VPC network with the outbound server policy. It doesn't matter _how_ the two VPC networks are connected—for example, using VPC Network Peering or Cloud VPN tunnels.

#### Prohibited alternative name server IP addresses

You cannot use the following IP addresses for Cloud DNS alternative name servers: 

  * `169.254.0.0/16`
  * `192.0.0.0/24`
  * `192.0.2.0/24`
  * `192.88.99.0/24`
  * `198.51.100.0/24`
  * `203.0.113.0/24`
  * `224.0.0.0/4`
  * `240.0.0.0/4`
  * `::1/128`
  * `::/128`
  * `2001:db8::/32`
  * `fe80::/10`
  * `fec0::/10`
  * `ff00::/8`



### Alternative name server network requirements

Network requirements for alternative name servers vary based on the alternative name server's _type_. To determine the type for an alternative name server, see Alternative name server types, routing methods, and addresses. Then refer to one of the following sections for network requirements.

#### Network requirements for Type 1 alternative name servers

Cloud DNS sends packets whose sources are from the `35.199.192.0/19` IP address range to the Type 1 alternative name server IP address. Google Cloud routes packets for queries using local subnet routes in the VPC network. Ensure you haven't created any [policy-based routes](https://docs.cloud.google.com/vpc/docs/policy-based-routes) whose destinations include Type 1 alternative name server IP addresses.

To allow incoming packets on alternative name server VMs, you must create ingress allow [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) or rules in [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) with the following characteristics:

  * Targets: must include the alternative name server VMs
  * Sources: `35.199.192.0/19`
  * Protocols: `TCP` and `UDP`
  * Port: `53`



Cloud DNS requires that each alternative name server send response packets back to the Cloud DNS IP address in `35.199.192.0/19` from which the query originated. Sources for response packets _must_ match the IP address of the alternative name server to which Cloud DNS sends the original query. Cloud DNS ignores responses if they come from an unexpected IP address source—for example, the IP address of another name server to which an alternative name server might forward a query.

When a _Type 1_ alternative name server sends response packets to `35.199.192.0/19`, it uses a [special routing path](https://docs.cloud.google.com/vpc/docs/routes#cloud-dns).

#### Network requirements for Type 2 alternative name servers

Cloud DNS sends packets whose sources are from the `35.199.192.0/19` IP address range to _Type 2_ alternative name servers. Cloud DNS relies on the following types of routes _within_ the VPC network to which the outbound server policy applies:

  * [Static routes](https://docs.cloud.google.com/vpc/docs/static-routes) _except for_ static routes that only apply to VMs by network tag
  * [Dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes)



To allow incoming packets on _Type 2_ alternative name servers, make sure that you configure ingress allow firewall rules that are applicable to the alternative name servers and any relevant on-premises network equipment with firewall features. The effective firewall configuration must allow both `TCP` and `UDP` protocols with destination port `53` and `35.199.192.0/19` sources.

Cloud DNS requires that each alternative name server send response packets back to the Cloud DNS IP address in `35.199.192.0/19` from which the query originated. Sources for response packets _must_ match the IP address of the alternative name server to which Cloud DNS sends the original query. Cloud DNS ignores responses if they come from an unexpected IP address source—for example, the IP address of another name server to which an alternative name server might forward a query.

Your on-premises network must have routes for the `35.199.192.0/19` destination whose next hops are Cloud VPN tunnels, Cloud Interconnect VLAN attachments, or Cloud Routers located in the same VPC network and region from which Cloud DNS sends the query. As long as the next hops meet those network and region requirements, Google Cloud doesn't require a symmetric return path. Responses from _Type 2_ alternative name servers _cannot_ be routed using any of the following next hops:

  * Next hops on the internet
  * Next hops in a VPC network that is different from the VPC network where the queries originated
  * Next hops in the same VPC network but in a region that is different from the region where the queries originated



To configure the `35.199.192.0/19` routes in your on-premises network, use the Cloud Router [custom advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am-custom) and include `35.199.192.0/19` as a custom prefix in the BGP sessions of the relevant Cloud VPN tunnels, Cloud Interconnect VLAN attachments, or Cloud Routers that connect your VPC network to the on-premises network that contains the _Type 2_ alternative name server. Alternatively, you can configure equivalent static routes in your on-premises network.

#### Network requirements for Type 3 alternative name servers

Cloud DNS sends packets whose sources match the [Google Public DNS source ranges](https://developers.google.com/speed/public-dns/faq#locations) to _Type 3_ alternative name servers. Cloud DNS uses public routing— it does _not_ rely on any routes _within_ the VPC network to which the outbound server policy applies.

To allow incoming packets on _Type 3_ alternative name servers, make sure that the effective firewall configuration that is applicable to the alternative name server permits packets from the Google Public DNS source ranges. 

## What's next

  * To configure and apply DNS server policies, see [Apply DNS server policies](https://docs.cloud.google.com/dns/docs/policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
