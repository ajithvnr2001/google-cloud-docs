---
url: https://docs.cloud.google.com/ull-solution/participants/participant-ull-network-profile/
title: About participant ULL VPC networks \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:09.946474+00:00
---

# About participant ULL VPC networks  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/participant-ull-network-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About participant ULL VPC networks

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page provides an overview of Ultra Low Latency (ULL) Virtual Private Cloud (VPC) networks for exchange participants.

## Overview

ULL VPC networks provide support for ultra-low latency unicast and multicast traffic for market trading applications, respecting strict latency, jitter, and multicast variance targets. ULL VPC networks use a dedicated zonal physical fabric that is isolated from other traffic in Google Cloud. To help ensure optimal performance, non-essential traffic and features are restricted.

You create ULL VPC networks by using a pre-configured, role-specific network profile provided by Google Cloud. Participant ULL VPC networks are created by using the _participant ULL network profile_. For a general overview of network profiles, see [Network profiles for specific use cases](https://docs.cloud.google.com/vpc/docs/network-profiles).

Participant ULL VPC networks support ULL communication between Compute Engine instances as described in the following sections.

### ULL unicast connectivity

Participant ULL VPC networks have limited support for ULL unicast connectivity as follows:

  * **Within the network** : ULL unicast traffic isn't supported between instances in the same participant ULL VPC network.

  * **With other networks through NCC** : If a participant ULL VPC network is a VPC spoke in the edge group of a Network Connectivity Center (NCC) hub that uses the star topology:

    * ULL unicast traffic is supported between instances in the participant ULL VPC network and instances in operator ULL VPC networks in the center group of the hub.
    * ULL unicast traffic isn't supported between participant ULL VPC networks in the edge group of the hub.



### ULL multicast connectivity

Participant ULL VPC networks support ULL multicast traffic, and can act as _multicast consumer networks_ for multicast traffic sent from operator ULL VPC networks. For detailed information, see the [ULL Multicast overview](https://docs.cloud.google.com/ull-solution/participants/multicast-overview).

## Specifications

Participant ULL VPC networks have the following specifications:

  * **Zonal constraint**. A participant ULL VPC network is constrained to the zone of the network profile that you specify when you create the network.

    * The name of the network profile that you specify when you create the network has the following format: `ZONE-vpc-ull-participant`, for example `us-south1-d-vpc-ull-participant`. The zone must be from the list of [Supported locations](https://docs.cloud.google.com/ull-solution/participants/configuration-overview#locations).

    * Resources that use a participant ULL VPC network are limited to the same zone as the network profile associated with the network.

      * All instances that have network interfaces in the participant ULL VPC network must be created in the zone that matches the zone of the network profile used by the network.

      * All subnets created in the participant ULL VPC network must be located in the region that contains the zone of the network profile used by the network.

  * **Supported Compute Engine instance types**. Participant ULL VPC networks support attachments from only U4C instances.

  * **Network interface egress bandwidth limits**. For a given network interface attached to the network, participant ULL VPC networks support a maximum egress bandwidth of 1 Gbps.

  * **1500 byte maximum transmission unit (MTU)**. The default [MTU](https://docs.cloud.google.com/vpc/docs/mtu) in a participant ULL VPC network is `1500` bytes. You can't modify this value.

    * **TCP MSS clamping** : During a TCP handshake, Google Cloud clamps the advertised maximum segment size (MSS) to align with the 1500-byte MTU. This ensures that TCP connections don't negotiate an MSS higher than the MTU.
    * **Egress packet drops and ICMP response** : The virtual switch (vSwitch) on the egress network interface drops packets that exceed the 1500-byte MTU and returns an ICMP `Fragmentation Needed` (Type 3, Code 4) message to the sender. Additionally, the Google Virtual NIC (gVNIC) driver prevents applications from setting an MTU larger than `1500`.
  * **Firewall differences**. Participant ULL VPC networks support only regional network firewall policies that have a ULL policy type. For more information, see [Firewall for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/firewall/overview).

  * **Other features**. The set of features that are supported in participant ULL VPC networks is pre-configured by Google Cloud to support running financial exchange workloads with ULL requirements. To help ensure optimal performance, participant ULL VPC networks support a limited set of features. For more information, see the following Supported and unsupported features section.




## Supported and unsupported features

This section describes which features are supported by participant ULL VPC networks.

The following table lists the specific features that are enabled or disabled by the participant ULL network profile and includes the network profile property values set by Google Cloud.

If a feature isn't explicitly enabled or disabled by a network profile property, then the availability of that feature typically matches that of a regular VPC network. For example, [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) isn't a feature configured by the network profile, but is supported for participant ULL VPC networks.

Feature | Supported | Network profile property and value | Details  
---|---|---|---  
ULL communication  
ULL unicast |  |  `unicast`:  
  
`UNICAST_ULL` |  Participant ULL VPC networks support ULL unicast traffic as described in ULL unicast connectivity.   
ULL unicast in the same network |  |  `allowSameNetworkUnicast`:  
  
`SAME_NETWORK_UNICAST_BLOCKED`  
ULL Multicast |  |  `multicast`:  
  
`MULTICAST_ULL` |  Participant ULL VPC networks support receiving ULL multicast traffic as described in ULL multicast connectivity.   
|  `allowMulticast`:  
  
`MULTICAST_ALLOWED`  
Subnets  
IPv4-only subnets |  |  `subnetworkStackTypes`:  
  
`SUBNET_STACK_TYPE_IPV4_ONLY` | Participant ULL VPC networks support IPv4-only subnets, including the same [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) as regular VPC networks. Participant ULL VPC networks don't support dual-stack or IPv6-only subnets. For more information, see [Types of subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).  
`PRIVATE` subnet purpose |  |  `subnetworkPurposes`:  
  
`SUBNET_PURPOSE_PRIVATE` | Participant ULL VPC networks support regular subnets, which have a `purpose` attribute value of `PRIVATE`. Participant ULL VPC networks don't support Private Service Connect subnets, proxy-only subnets, or Private NAT subnets. For more information, see [Purposes of subnets](https://docs.cloud.google.com/vpc/docs/subnets#purpose).  
Auto mode |  |  `allowAutoModeSubnet`:  
  
`AUTO_MODE_SUBNET_BLOCKED` | Participant ULL VPC networks can't be auto mode networks. For more information, see [subnet creation mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges).  
Network interfaces  
Multi-NIC in the same network |  |  `allowMultiNicInSameNetwork`:  
  
`MULTI_NIC_IN_SAME_NETWORK_ALLOWED` | Participant ULL VPC networks support [multi-NIC instances](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts), allowing two or more network interfaces of the same instance to be in the same network. Each network interface must attach to a unique subnet in the network.  
Attachments from `nic0` |  |  `allowDefaultNicAttachment`:  
  
`DEFAULT_NIC_ATTACHMENT_BLOCKED` | Participant ULL VPC networks don't support attaching the `nic0` network interface of an instance to the network. For a given ULL compute instance: 

  * the `nic0` interface attaches to a general-purpose VPC network.
  * the `nic1` and `nic2` interfaces attach to a ULL VPC network, which gives the instance access to ULL unicast and multicast.

  
Dynamic Network Interfaces |  |  `allowSubInterfaces`:  
  
`SUBINTERFACES_BLOCKED` | Participant ULL VPC networks don't support [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-types).  
Instance network migration |  |  `allowNetworkMigration`:  
  
`NETWORK_MIGRATION_BLOCKED` | Participant ULL VPC networks don't support [migrating instance network interfaces between networks](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks).  
IP addresses  
`GCE_ENDPOINT` address purpose |  |  `addressPurposes`:  
  
`GCE_ENDPOINT` | Participant ULL VPC networks support IP addresses with a `purpose` attribute value of `GCE_ENDPOINT`, which is used by internal IP addresses of instance network interfaces. Participant ULL VPC networks don't support special purpose IP addresses, such as the `SHARED_LOADBALANCER_VIP` purpose. For more information, see the [addresses resource reference](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses).  
External IP addresses for instances |  |  `allowExternalIpAccess`:  
  
`EXTERNAL_IP_ACCESS_BLOCKED` | Participant ULL VPC networks don't support assigning [external IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses) to instance network interfaces. Consequently, network interfaces attached to the network don't have internet access.  
Routes  
Static routes |  |  `allowStaticRoutes`:  
  
`STATIC_ROUTES_BLOCKED` | Participant ULL VPC networks don't support [static routes](https://docs.cloud.google.com/vpc/docs/static-routes).  
IP forwarding |  |  `allowIpForwarding`:  
  
`IP_FORWARDING_BLOCKED` | Participant ULL VPC networks don't support [IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward).  
Network security  
Cloud NGFW firewall policies |  |  `allowFirewallPolicy`:  
  
`FIREWALL_POLICY_ALLOWED` | Participant ULL VPC networks support Cloud NGFW firewall policies that have the ULL policy type as described in [Firewall for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/firewall/overview).  
ULL policy type |  |  `firewallPolicyTypes`:  
  
`ULL_POLICY`  
Class D firewalls |  |  `allowClassDFirewalls`:  
  
`CLASS_D_FIREWALLS_BLOCKED` | Participant ULL VPC networks don't support firewall rules that have class D addresses (`224.0.0.0/4`).  
VPC firewall rules |  |  `allowVpcFirewallRules`:  
  
`VPC_FIREWALL_RULES_BLOCKED` | Participant ULL VPC networks don't support [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).  
VPC Packet Mirroring |  |  `allowPacketMirroring`:  
  
`PACKET_MIRRORING_BLOCKED` | Participant ULL VPC networks don't support [VPC Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring), which is a packet mirroring service for regular VPC networks. Instead, use [Packet Mirroring for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/packet-mirroring-ull).  
Network Connectivity  
VPC Network Peering |  |  `allowVpcPeering`:  
  
`VPC_PEERING_BLOCKED` | Participant ULL VPC networks don't support connecting to other VPC networks using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). Consequently, Participant ULL VPC networks don't support connecting to services using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).  
Cloud Router |  |  `allowCloudRouter`:  
  
`CLOUD_ROUTER_BLOCKED` | Participant ULL VPC networks don't support [Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) and dynamic routes.  
Cloud Interconnect |  |  `allowInterconnect`:  
  
`INTERCONNECT_BLOCKED` | Participant ULL VPC networks don't support [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) VLAN attachments.  
Cloud VPN |  |  `allowVpn`:  
  
`VPN_BLOCKED` | Participant ULL VPC networks don't support [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) tunnels.  
NAT  
Cloud NAT |  |  `allowCloudNat`:  
  
`CLOUD_NAT_BLOCKED` | Participant ULL VPC networks don't support [Cloud NAT](https://docs.cloud.google.com/nat/docs).  
Load balancing  
Cloud Load Balancing |  |  `allowLoadBalancing`:  
  
`LOAD_BALANCING_BLOCKED` | Participant ULL VPC networks don't support [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). Consequently, Participant ULL VPC networks don't support load balancer features, including [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview).  
Private access for services  
Private Google Access |  |  `allowPrivateGoogleAccess`:  
  
`PRIVATE_GOOGLE_ACCESS_BLOCKED` | Participant ULL VPC networks don't support [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).  
Private Service Connect |  |  `allowPsc`:  
  
`PSC_BLOCKED` | Participant ULL VPC networks don't support [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).  
  
## What's next

  * [Create VPC networks for exchange participant workloads](https://docs.cloud.google.com/ull-solution/participants/create-participant-ull-vpc-networks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
