---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview/
title: Cloud VPN overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:29:17.723369+00:00
---

# Cloud VPN overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Cloud VPN overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes concepts related to Cloud VPN. For definitions of terms used in the Cloud VPN documentation, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms).

Cloud VPN securely extends your _peer network_ to your [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) through an [IPsec](https://wikipedia.org/wiki/IPsec) [VPN](https://wikipedia.org/wiki/Virtual_private_network) connection. The VPN connection encrypts traffic traveling between the networks, with one VPN gateway handling encryption and the other handling decryption. This process protects your data during transmission. You can also connect two VPC networks together by connecting two Cloud VPN instances. You cannot use Cloud VPN to route traffic to the public internet; it is designed for secure communication between private networks.

### Choose a hybrid networking solution

To determine whether to use Cloud VPN, Dedicated Interconnect, Partner Interconnect, or Cloud Router as your hybrid networking connection to Google Cloud, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud VPN performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud VPN free ](https://console.cloud.google.com/freetrial)

To enhance the security of your Dedicated Interconnect or Partner Interconnect connection, use [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect). This solution establishes encrypted HA VPN tunnels over your VLAN attachments. 

## Types of Cloud VPN

Google Cloud offers two types of Cloud VPN gateways:

  * HA VPN
  * Classic VPN



The following table compares HA VPN features with Classic VPN features.

**Note:** The tunnel API resource and tunnel configuration remain the same for both Classic VPN and HA VPN.Feature | HA VPN | Classic VPN  
---|---|---  
SLA | Provides 99.99% SLA for most topologies, with a few exceptions. For more information, see [HA VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies). | Provides a 99.9% SLA.  
Creation of external IP addresses and forwarding rules | External IP addresses created from a pool; no forwarding rules required. | External IP addresses and forwarding rules must be created.  
Supported routing options | Only dynamic routing (BGP). | Only static (policy-based, route-based) routing.  
Two tunnels from one Cloud VPN gateway to the same peer gateway | Supported | Not supported  
Connect a Cloud VPN gateway to Compute Engine VMs with external IP addresses. | Supported and recommended topology. For more information, see [HA VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#vm-multi-zone). | Supported.  
API resources | Known as the `vpn-gateway` resource. | Known as the `target-vpn-gateway` resource.  
IPv6 traffic | Supports dual stack (IPv4 and IPv6) and IPv6-only configuration  | Not supported  
  
For information about how to move from Classic VPN to HA VPN, see [Move from Classic VPN to HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/moving-to-ha-vpn).

### HA VPN

HA VPN is a high-availability (HA) Cloud VPN solution that lets you securely connect your on-premises network to your VPC network through an IPsec VPN connection. Based on the topology and configuration, HA VPN can provide an SLA of 99.99% or 99.9% service availability. 

When you create an HA VPN gateway, Google Cloud automatically chooses two external IP addresses, one for each of its interfaces. Each IP address is automatically chosen from a unique address pool to support high availability. Each of the HA VPN gateway interfaces supports multiple tunnels. You can also create multiple HA VPN gateways. When you delete the HA VPN gateway, Google Cloud releases the IP addresses for reuse. You can configure an HA VPN gateway with only one active interface and one external IP address; however, _this configuration does not provide an availability SLA._

One option for using HA VPN is to use [ HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect). With HA VPN over Cloud Interconnect, you get the security of IPsec encryption from Cloud VPN alongside the increased capacity of Cloud Interconnect. In addition, because you are using Cloud Interconnect, your network traffic never traverses the public internet. If you use Partner Interconnect, you must add IPsec encryption to your Cloud Interconnect traffic to meet data security and compliance requirements when connecting to third-party providers. HA VPN uses an _external VPN gateway_ resource in Google Cloud to provide information to Google Cloud about your _peer VPN gateway_ or gateways.

**Note:** When you deploy HA VPN over Cloud Interconnect, you have the option of assigning regional internal IP addresses to HA VPN gateway interfaces. You can only use these internal IP addresses for HA VPN gateways that are associated with VLAN attachments. In all other HA VPN gateways, internal IP address assignment is not supported. 

In the API documentation and in `gcloud` commands, HA VPN gateways are referred to as _VPN gateways_ rather than _target VPN gateways_. You don't need to create any [forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) for HA VPN gateways.

HA VPN can provide an availability SLA of 99.99% or 99.9% depending on the topologies or configuration scenarios. For more information about HA VPN topologies and supported SLAs, see [HA VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies). 

While setting up HA VPN, consider the following guidelines:

  * When you connect an HA VPN gateway to another HA VPN gateway, the gateways must use identical IP stack types. For example, if you create an HA VPN gateway with the stack type of `IPV4_IPV6`, the other HA VPN gateway must also be set to `IPV4_IPV6`.

  * Configure two VPN tunnels from the perspective of the Cloud VPN gateway:

    * If you have _two peer VPN gateway devices_ , each of the tunnels from each interface on the Cloud VPN gateway must be connected to its own peer gateway.
    * If you have _a single peer VPN gateway device with two interfaces_ , each of the tunnels from each interface on the Cloud VPN gateway must be connected to its own interface on the peer gateway.
    * If you have _a single peer VPN gateway device with a single interface_ , both of the tunnels from each interface on the Cloud VPN gateway must be connected to the same interface on the peer gateway.
  * A peer VPN device must be configured with adequate redundancy. The device vendor specifies the details of an adequately redundant configuration, which might include multiple hardware instances. For details, see the vendor documentation for the peer VPN device.

If two peer devices are required, each peer device must be connected to a different HA VPN gateway interface. If the peer side is another cloud provider like AWS, VPN connections must be configured with adequate redundancy on the AWS side as well.

  * Make sure that your Cloud Router advertises the same prefixes on all links, possibly with different priorities.

  * Your peer VPN gateway device must support dynamic Border Gateway Protocol (BGP) routing.

The following diagram shows the HA VPN concept, showing a topology that includes the two interfaces of an HA VPN gateway connected to two peer VPN gateways. For more detailed HA VPN topologies (configuration scenarios), see [HA VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies).

[ ![An HA VPN gateway to two peer VPN gateways.](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/ha-vpn-gcp-to-on-prem-2-a.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/ha-vpn-gcp-to-on-prem-2-a.svg) An HA VPN gateway to two peer VPN gateways (click to enlarge).



### Classic VPN

In contrast to HA VPN, Classic VPN gateways have a single interface, a single external IP address, and support tunnels that use static routing (policy based or route based).

Classic VPN gateways provide an SLA of 99.9% service availability. 

Classic VPN gateways don't support IPv6.

For supported Classic VPN topologies, see the [ Classic VPN topologies page](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/classic-topologies).

Classic VPNs are referred to as _target VPN gateways_ in the API documentation and in the Google Cloud CLI.

## Specifications

Cloud VPN has the following specifications:

  * Each Cloud VPN gateway is a regional resource. When you create a Cloud VPN gateway, you can select a specific [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions) for its location. You cannot choose a zone, only a region.


  * Cloud VPN only supports site-to-site IPsec VPN connectivity, subject to the requirements listed in this section. It does not support client-to-gateway scenarios. In other words, Cloud VPN doesn't support use cases where client computers need to "dial in" to a VPN by using client VPN software.

Cloud VPN only supports IPsec. Other VPN technologies (such as SSL VPN) are not supported.

  * Cloud VPN can be used with VPC networks and [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy). For VPC networks, we recommend [custom mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) so that you have full control over the ranges of IP addresses used by the subnets in the network.

    * Classic VPN and HA VPN gateways use external (internet routable) IPv4 addresses. Only ESP, UDP 500, and UDP 4500 traffic is permitted to these addresses. This applies to Cloud VPN addresses configured by you for Classic VPN or to automatically assigned IP addresses for HA VPN.

    * If IP address ranges for on-premises subnets overlap with IP addresses used by subnets in your VPC network, to determine how routing conflicts are resolved, see [Order of routes](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/order-of-routes).

  * The following Cloud VPN traffic remains within the Google Cloud network:

    * Between two HA VPN gateways
    * Between two Classic VPN gateways
    * Between a Classic VPN or HA VPN gateway and the external IP address of a Compute Engine VM acting as a VPN gateway
  * Cloud VPN can be used with _Private Google Access for on-premises hosts_. For more information, see [Private access options for services](https://docs.cloud.google.com/vpc/docs/private-access-options).

  * Each Cloud VPN gateway must be connected to another Cloud VPN gateway or a peer VPN gateway.

  * The peer VPN gateway must have a static external (internet-routable) IP address that matches your selected stack type (IPv4, IPv6, or both). You need this IP address to configure Cloud VPN.

You cannot use reserved addresses for the peer IP address. This includes IPv4 addresses reserved by [RFC 5737](https://tools.ietf.org/html/rfc5737) or [RFC 5735](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/\(https:/datatracker.ietf.org/doc/html/rfc5735\)), and IPv6 addresses reserved by [RFC 3849](https://datatracker.ietf.org/doc/html/rfc3849) or [RFC 6890](https://datatracker.ietf.org/doc/html/rfc6890).

    * If your peer VPN gateway is behind a firewall rule, you must configure the firewall rule to pass ESP (IPsec) protocol and IKE (UDP 500 and UDP 4500) traffic to it. If the firewall rule provides network address translation (NAT), see UDP encapsulation and NAT-T.
  * Cloud VPN requires that the peer VPN gateway be configured to support prefragmentation. Packets must be fragmented _before_ being encapsulated.

  * Cloud VPN uses replay detection with a window of 4096 packets. You cannot turn this off.

  * Cloud VPN supports [generic routing encapsulation (GRE)](https://wikipedia.org/wiki/Generic_Routing_Encapsulation) traffic. Support for GRE lets you terminate GRE traffic on a VM from the internet (external IP address) and Cloud VPN or Cloud Interconnect (internal IP address). The decapsulated traffic can then be forwarded to a reachable destination. GRE lets you use services such as Secure Access Service Edge (SASE) and [SD-WAN](https://wikipedia.org/wiki/SD-WAN). You must create a [firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls) to allow GRE traffic.

**Note:** GRE support for VPN has been tested only with GRE version 0. Additionally, support for GRE traffic does not include [support](https://cloud.google.com/support) from Google Cloud for troubleshooting your overlay networks.
  * HA VPN tunnels support the exchange of IPv6 traffic, but Classic VPN tunnels don't.




### Network bandwidth

Each Cloud VPN tunnel supports up to 250,000 packets per second for the sum of ingress and egress traffic. Depending on average packet size in the tunnel, 250,000 packets per second is equivalent to between 1 Gbps and 3 Gbps of bandwidth.

The metrics related to this limit are `Sent bytes` and `Received bytes`, which are described in [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics#metrics). Consider that the unit for the metrics is _bytes_ , while the 3-Gbps limit refers to _bits_ per second. When converted to bytes, the limit is 375 megabytes per second (MBps). When measuring usage against the limit, use the sum of `Sent bytes` and `Received bytes` compared to the converted limit of 375 MBps. For information about how to create alerting policies, see [Define alerts for VPN tunnel bandwidth](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics#defining_alerts_for_vpn_tunnel_bandwidth). 

#### Factors that affect bandwidth

The bandwidth is influenced by a number of factors, including the following:

  * The network connection between the Cloud VPN gateway and your peer gateway:

    * **Network bandwidth between the two gateways.** If you have established a [Direct Peering](https://docs.cloud.google.com/network-connectivity/docs/direct-peering) relationship with Google, throughput is higher than if your VPN traffic is sent over the public internet.

    * **[Round-trip time (RTT)](https://wikipedia.org/wiki/Round-trip_delay_time) and packet loss.** Elevated RTT or packet loss rates greatly reduce TCP performance.

  * **Capabilities of your peer VPN gateway.** For more information, see your device's documentation.

  * **Packet size.** Cloud VPN uses the IPsec protocol in tunnel mode, encapsulating and encrypting entire IP packets in Encapsulating Security Payload (ESP), and then storing the ESP data in a second, outer IP packet. Consequently, there is both a _gateway MTU_ for the IPsec encapsulated packets and a _payload MTU_ for packets before and after IPsec encapsulation. For details, see [MTU considerations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations).

  * **Packet rate.** For ingress and egress, the recommended maximum packet rate for each Cloud VPN tunnel is 250,000 packets per second (pps). If you need to send packets at a higher rate, you must create more VPN tunnels.




When measuring TCP bandwidth of a VPN tunnel, you should measure more than one simultaneous TCP stream. If you are using the [`iperf` tool](https://wikipedia.org/wiki/Iperf), use the `-P` parameter to specify the number of simultaneous streams.

### IPv6 support

Cloud VPN supports IPv6 in HA VPN, but not in Classic VPN.

To support IPv6 traffic in HA VPN tunnels, do the following:

  * Use the `IPV6_ONLY` or `IPV4_IPV6` stack type when creating a HA VPN gateway and tunnels that connect IPv6-enabled VPC networks with other IPv6-enabled networks. These networks can be on-premises networks, multicloud networks, or other VPC networks.

  * Use [dual-stack subnets or IPv6-only subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types) in IPv6-enabled VPC networks. For more information, see [Create a custom mode VPC network with a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-network-dual) and [Create a custom mode VPC network with IPv6-only subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-network-ipv6-only).




The following table summarizes the external IP addresses allowed for each stack type of the HA VPN gateway.

Stack type | Supported gateway external IP addresses  
---|---  
IPV4_ONLY | IPv4  
IPV4_IPV6 | IPv4, IPv6  
IPV6_ONLY | IPv6  
  
#### Organization policy constraints for IPv6

You can disable the creation of all IPv6 hybrid resources in your project by setting the following [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) to true:

  * `constraints/compute.disableHybridCloudIpv6`



For HA VPN, this organization policy constraint prevents the creation of any dual-stack HA VPN gateways and IPv6-only HA VPN gateways in the project. This policy also prevents the creation of IPv6 BGP sessions and dual-stack Dedicated Interconnect VLAN attachments.

### Stack types and BGP sessions

HA VPN gateways support different stack types. The stack type of an HA VPN gateway determines what version of IP traffic is allowed in your HA VPN tunnels.

When you create the HA VPN tunnels for a dual-stack HA VPN gateway, you can create either an IPv6 BGP session for IPv6 route exchange, or an IPv4 BGP session that [exchanges IPv6 routes by using multiprotocol BGP (MP-BGP)](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).

The following table summarizes the types of BGP sessions supported for each stack type.

Stack type | Supported BGP sessions | Gateway external IP addresses  
---|---|---  
Single stack (IPv4 only) | IPv4 BGP, no MP-BGP | IPv4  
Single stack (IPv6 only) | IPv6 BGP, no MP-BGP | IPv6  
Dual stack (IPv4 and IPv6) | 

  * IPv4 BGP, with or without MP-BGP
  * IPv6 BGP, with or without MP-BGP
  * Both IPv4 BGP and IPv6 BGP, no MP-BGP

| IPv4 and IPv6  
**Note:** After you create an HA VPN gateway, you cannot modify its stack type. If you need a different stack type for an existing HA VPN gateway, you must delete and recreate the gateway. 

To support IPv6 traffic, HA VPN gateways must use either the `IPv4 and IPv6 (dual-stack)` or `IPv6 (single-stack)` configuration. To temporarily disable IPv6 traffic without deleting your gateway, [ disable IPv6 route exchange in the IPv4 BGP session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp#disable-ipv6-bgp) or [ disable the IPv6 session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#disable_a_bgp_session) that you established for the HA VPN tunnels. 

For more information about BGP sessions, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp) in the Cloud Router documentation.

**Single-stack IPv4-only gateways**

By default, an HA VPN gateway is assigned the IPv4-only stack type and is automatically assigned two external IPv4 addresses.

An IPv4-only HA VPN gateway can support only IPv4 traffic.

Use the following procedures to create IPv4-only HA VPN gateways and IPv4 BGP sessions.

  * For an HA VPN to peer VPN gateway configuration, see [Create an HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#create_an_gateway) and [Create BGP sessions - IPv4 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#ipv4-bgp).
  * For an HA VPN to HA VPN gateway configuration, see [Create the HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create-ha-gateways) and [Create BGP sessions - IPv4 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#ipv4-bgp).



**Single-stack IPv6-only gateways**

An IPv6-only HA VPN gateway supports only IPv6 traffic. By default, an IPv6-only HA VPN gateway is assigned two external IPv6 addresses.

Use the following procedures to create IPv6-only HA VPN gateways and IPv6 BGP sessions.

  * For an HA VPN to peer VPN gateway configuration, see [Create an HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#create_an_gateway) and [Create BGP sessions - IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#ipv6-bgp).
  * For an HA VPN to HA VPN gateway configuration, see [Create the HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create-ha-gateways) and [Create BGP sessions - IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#ipv6-bgp).



**Dual-stack IPv4 and IPv6 gateways**

An HA VPN gateway that is configured with the dual-stack (IPv4 and IPv6) stack type can support both IPv4 and IPv6 traffic.

For a dual-stack HA VPN gateway, you can configure your Cloud Router with an IPv4 BGP session, an IPv6 BGP session, or both. If you configure only one BGP session, you can enable MP-BGP to allow that session to exchange both IPv4 and IPv6 routes. If you create an IPv4 BGP session and an IPv6 BGP session, you can't enable MP-BGP on either session.

To exchange IPv6 routes on an IPv4 BGP session using MP-BGP, you must configure that session with IPv6 next hop addresses. Similarly, to exchange IPv4 routes on an IPv6 BGP session using MP-BGP, you must configure that session with IPv4 next hop addresses. You can configure these next hop addresses either manually or automatically.

If you manually configure the next hop addresses, you must select them from the Google-owned IPv6 Global Unicast Address (GUA) range `2600:2d00:0:2::/63`, or from the IPv4 link-local address range `169.254.0.0/16`. These IP address ranges are pre-allocated by Google. The next hop IP addresses you select must be unique across all Cloud Routers within your VPC network.

If you select automatic configuration, Google Cloud selects the next hop IP addresses for you.

Use the following procedures to create dual-stack HA VPN gateways and all supported BGP sessions.

  * **IPv4 BGP sessions, with or without MP-BGP**
    * For an HA VPN gateway to peer VPN gateway configuration, see [Create an HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#create_an_gateway) and [Create BGP sessions - IPv4 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#ipv4-bgp).
    * For an HA VPN gateway to HA VPN gateway configuration, see [Create the HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create-ha-gateways) and [Create BGP sessions - IPv4 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#ipv4-bgp).
  * **IPv6 BGP sessions, with or without MP-BGP**
    * For an HA VPN gateway to peer VPN gateway configuration, see [Create an HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#create_an_gateway) and [Create BGP sessions - IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#ipv6-bgp).
    * For an HA VPN gateway to HA VPN gateway configuration, see [Create the HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create-ha-gateways) and [Create BGP sessions - IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#ipv6-bgp).
  * **Both IPv4 and IPv6 BGP sessions**
    * For an HA VPN gateway to peer VPN gateway configuration, see [Create an HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#create_an_gateway) and [Create BGP sessions - Both IPv4 BGP and IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#both-ipv4-ipv6-bgp).
    * For an HA VPN gateway to HA VPN gateway configuration, see [Create the HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create-ha-gateways) and [Create BGP sessions - Both IPv4 and IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#both-ipv4-ipv6-bgp).



### IPsec and IKE support

Cloud VPN supports [IKEv1](https://tools.ietf.org/html/rfc2409) and [IKEv2](https://tools.ietf.org/html/rfc5996) by using an IKE pre-shared key (shared secret) and IKE ciphers. Cloud VPN only supports a pre-shared key for authentication. When you create the Cloud VPN tunnel, specify a pre-shared key. When you create the tunnel at the peer gateway, specify this same pre-shared key. For information about creating a strong pre-shared key, see [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key).

Cloud VPN supports [ESP in tunnel mode](https://wikipedia.org/wiki/IPsec#Tunnel_mode) with authentication, but does not support [AH](https://wikipedia.org/wiki/IPsec#Authentication_Header) or [ESP in transport mode](https://wikipedia.org/wiki/IPsec#Transport_mode).

You must use IKEv2 to enable IPv6 traffic in HA VPN.

Cloud VPN does not perform policy-related filtering on incoming authentication packets. Outgoing packets are filtered based on the IP range configured on the Cloud VPN gateway.

#### Configure ciphers in Cloud VPN tunnel

With Cloud VPN, you can configure ciphers that help you tailor your VPN connections to meet compliance and security needs.

You can configure cipher options when you create Cloud VPN tunnels. However, once configured, you cannot modify the selected cipher options later; you must delete and re-create the tunnel. Cipher selection is available only with IKEv2, not IKEv1.

You can configure ciphers for both IKE SA negotiation (phase 1) and IPsec SA negotiation (phase 2). If you don't configure a cipher option for a phase, Cloud VPN uses the default cipher for that option.

You must configure ciphers from the supported list of ciphers that meet the following criteria:

  * If you specify [AEAD ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers#ikev2-aead-ciphers) for encryption, you cannot specify separate ciphers for integrity because Cloud VPN uses the same encryption ciphers for handling integrity.

  * If you specify [non-AEAD ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers#ikev2_ciphers_that_dont_use_aead) for encryption, then you can also specify ciphers for integrity. If you don't specify integrity ciphers, Cloud VPN uses the default cipher options for integrity.

  * If you specify a mix of both AEAD and non-AEAD ciphers for encryption, you must list the AEAD ciphers before non-AEAD ciphers. Cloud VPN uses the same encryption ciphers for handling integrity for AEAD ciphers.

For non-AEAD ciphers, you can specify the integrity ciphers. If you don't specify integrity ciphers, Cloud VPN uses the default cipher options for integrity.




To learn more about the supported ciphers, default cipher order, and configuration parameters supported by Cloud VPN, see [Supported IKE ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers).

Use the following procedures to configure cipher options for the various Cloud VPN gateways:

  * To configure cipher options for Classic VPN using static routing, see [Create a gateway and tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns#create_a_gateway_and_tunnel).

  * To configure cipher options for HA VPN to a peer VPN gateway, see [Create VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#create_vpn_tunnels). 




### IKE and dead peer detection

Cloud VPN supports dead peer detection (DPD), per the [DPD Protocol](https://datatracker.ietf.org/doc/html/rfc3706#section-5) section of [RFC 3706](https://datatracker.ietf.org/doc/html/rfc3706).

To verify that the peer is alive, Cloud VPN might send DPD packets at any time, per RFC 3706. If the DPD requests aren't returned after several retries, Cloud VPN recognizes that the VPN tunnel is unhealthy. The unhealthy VPN tunnel in turn causes removal of the routes using this tunnel as a next-hop (BGP routes or static routes) triggering a failover of VM traffic to other VPN tunnels that are healthy.

The DPD interval isn't configurable in Cloud VPN.

### UDP encapsulation and NAT-T

For information about how to configure your peer device to support NAT-Traversal (NAT-T) with Cloud VPN, see [UDP encapsulation](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced#udp-encapsulation) in the Advanced overview.

### Cloud VPN as a data transfer network

Before you use Cloud VPN, carefully review [Section 2 of the General Service Terms](https://cloud.google.com/terms/service-terms) for Google Cloud.

Using [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center), you can use HA VPN tunnels to connect on-premises networks together, passing traffic between them as a data transfer network. You connect the networks by attaching a pair of tunnels to a NCC spoke for each on-premises location. You then connect each spoke to a NCC hub.

For more information about NCC, see the [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview). 

### Bring your own IP (BYOIP) support

For information about using BYOIP addresses with Cloud VPN, see [Support for BYOIP addresses](https://docs.cloud.google.com/vpc/docs/using-bring-your-own-ip#support).

## Restricting peer IP addresses through a Cloud VPN tunnel

If you're an [Organization Policy Administrator (`roles/orgpolicy.policyAdmin`)](https://docs.cloud.google.com/resource-manager/docs/access-control-org#orgpolicy.policyAdmin), you can create a policy constraint that restricts the IP addresses that users can specify for peer VPN gateways.

The restriction applies to all Cloud VPN tunnels—both Classic VPN and HA VPN—in a specific project, folder, or organization.

For steps describing how to restrict IP addresses, see [Restrict IP addresses for peer VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/restrict-peer-ip-addresses).

## Visualizing and monitoring Cloud VPN connections

Network Topology is a visualization tool that shows the topology of your VPC networks, hybrid connectivity to and from your on-premises networks, and the associated metrics. You can view your Cloud VPN gateways and VPN tunnels as entities in the Network Topology view.

A base entity is the lowest level of a particular hierarchy and represents a resource that can directly communicate with other resources over a network. Network Topology aggregates base entities into hierarchical entities that you can expand or collapse. When you first view a Network Topology graph, it aggregates all the base entities into their top-level hierarchy.

For example, Network Topology aggregates VPN tunnels into their VPN gateway connection. You can view the hierarchy by expanding or collapsing the VPN gateway icons.

For more information, see the [Network Topology overview](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview). 

## Maintenance and availability

Cloud VPN undergoes periodic maintenance during which Cloud VPN tunnels remain online, and network traffic is unaffected. In rare scenarios, tunnels might briefly go offline, which can cause a momentary drop in network traffic. After the maintenance is complete, Cloud VPN tunnels are automatically re-established. These incidents are investigated to implement corrective actions and improve future maintenance procedures.

Maintenance for Cloud VPN is a normal operational task that can happen at any time without prior notice. Maintenance periods are designed to be short enough that the [Cloud VPN SLA](https://docs.cloud.google.com/network-connectivity/docs/vpn/sla) isn't impacted.

HA VPN is the recommended method of configuring high-availability VPNs. For configuration options, see the [ HA VPN topologies page](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies). If you are using Classic VPN for redundancy and high-throughput options, see the [Classic VPN topologies page](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/classic-topologies).

## Best practices

To build your Cloud VPN effectively, use these [best practices](https://docs.cloud.google.com/network-connectivity/docs/vpn/resources/best-practices).

## What's next

  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).

  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).

  * Learn more about the [recommended topologies for HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
