---
url: https://docs.cloud.google.com/vpc/docs/rdma-network-profiles/
title: RDMA network profiles \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:41.961864+00:00
---

# RDMA network profiles  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/rdma-network-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# RDMA network profiles

This page provides an overview of [Remote Direct Memory Access (RDMA)](https://en.wikipedia.org/wiki/Remote_direct_memory_access) network profiles in Google Cloud.

## Overview

RDMA network profiles let you create Virtual Private Cloud (VPC) networks that provide low-latency, high-bandwidth RDMA communication between the memory or GPUs of Compute Engine instances that are created in the network.

RDMA network profiles are useful for running AI workloads. For more information about running AI workloads in Google Cloud, see [AI Hypercomputer overview](https://docs.cloud.google.com/ai-hypercomputer/docs/overview).

You can create the following types of VPC networks by using RDMA network profiles:

VPC network type | Protocol | Network profile resource name | Instance types | vNIC type  
---|---|---|---|---  
Falcon VPC network | [RDMA over Falcon transport](https://www.opencompute.org/documents/rdma-over-falcon-spec-v1-1-pdf) | `ZONE-vpc-falcon` |  VM:  
[H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series), [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series) Bare metal:  
[Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series) | `IRDMA`  
RoCE VPC network | [RDMA over converged ethernet v2 (RoCE v2)](https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet) |  For VM instances:  
`ZONE-vpc-roce`  
For bare metal instances:  
`ZONE-vpc-roce-metal` |  VM:  
[A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms), [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms), [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-machine-type) Bare metal:  
[A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-max-metal-machine-type) | `MRDMA`  
  
## Supported zones

RDMA network profiles are available in a limited set of zones. You can only create a Falcon VPC network or RoCE VPC network in a zone where the corresponding network profile is available.

To view the supported zones, see [List network profiles](https://docs.cloud.google.com/vpc/docs/view-network-profiles#list_network_profiles).

Alternatively, you can view the supported zones for the machine type that you intend to create in the network. RDMA network profiles are available in the same zones as their supported machine types. For more information, see the following:

  * For GPU machine types, see [GPU locations](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones).
  * For other machine types, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).



## Specifications

VPC networks created with an RDMA network profile have the following specifications:

  * **Zonal constraint**. Resources using a VPC network with an RDMA network profile are limited to the same zone as the RDMA network profile associated with the VPC network during the network creation. This zonal limit has the following effects:

    * All instances that have virtual network interfaces (vNICs) in the VPC network must be created in the zone that matches the zone of the RDMA network profile used by the VPC network.

    * All subnets created in the VPC network must be located in the region that contains the zone of the RDMA network profile used by the VPC network.

  * **RDMA network interfaces only**. A VPC network with an RDMA network profile supports attachments only from specific network interfaces:

    * Falcon VPC networks only support `IRDMA` vNICs.
    * RoCE VPC networks only support `MRDMA` vNICs.

All non-RDMA vNICs of an instance, such as its `GVNIC` or `IDPF` vNICs, must be attached to a regular VPC network. Regular VPC networks have no [network profile](https://docs.cloud.google.com/vpc/docs/network-profiles). Consequently, the Supported and unsupported features listed for RDMA network profiles don't apply to an instance's non-RDMA vNICs.

  * **8896 byte MTU**. For best performance, we recommend a [maximum transmission unit (MTU)](https://en.wikipedia.org/wiki/Maximum_transmission_unit) of `8896` bytes for VPC networks with an RDMA network profile. This allows the RDMA driver in the instance's guest operating system to use smaller MTUs if needed.

If you create a VPC network with an RDMA network profile, then `8896` bytes is the default MTU.

  * **Firewall differences**. See the following information about firewall differences in VPC networks with an RDMA network profile:

    * VPC networks with an RDMA network profile use the following implied firewall rules, which are different from the implied firewall rules used by regular VPC networks:

      * Implied allow egress
      * Implied allow ingress
    * Cloud NGFW support depends on the type of VPC network:

      * For RoCE VPC networks, see the following:

        * RoCE VPC networks for VM instances only support regional network firewall policies that have an RoCE firewall policy type. The set of parameters for rules within a supported regional network firewall policy are limited. For more information, see [Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce).
        * RoCE VPC networks for bare metal instances don't support configuring Cloud NGFW rules or policies.
      * Falcon VPC networks don't support configuring Cloud NGFW rules or policies.

  * **No Connectivity Tests support**. [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) doesn't support VPC networks with an RDMA network profile.

  * **Other VPC features**. VPC networks with an RDMA network profile support a limited set of other VPC features. For more information, see the following Supported and unsupported features section.




## Supported and unsupported features

The following sections describe which VPC features are supported and unsupported for each type of VPC network that you can create by using an RDMA network profile:

  * Falcon VPC networks (`falcon`)
  * RoCE VPC networks for VM instances (`roce`)
  * RoCE VPC networks for bare metal instances (`roce-metal`)



### Falcon VPC networks (`falcon`)

The following table lists the features that are supported by Falcon VPC networks, which are created by using the `falcon` network profile.

Feature | Supported | Network profile property | Network profile property value | Details  
---|---|---|---|---  
RDMA NICs |  | `interfaceTypes` | `IRDMA` | Falcon VPC networks support only `IRDMA` NICs Other NIC types, such as `MRDMA`, `GVNIC`, `IDPF`, and `VIRTIO_NET`, aren't supported.  
Multi-NIC in the same network |  | `allowMultiNicInSameNetwork` | `MULTI_NIC_IN_SAME_NETWORK_ALLOWED` | Falcon VPC networks support [multi-NIC instances](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts), allowing two or more RDMA NICs of the same instance to be in the same VPC network. Each NIC must attach to a unique subnet in the VPC network.  
IPv4-only subnets |  | `subnetworkStackTypes` | `SUBNET_STACK_TYPE_IPV4_ONLY` | Falcon VPC networks support IPv4-only subnets, including the same [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) as regular VPC networks. Falcon VPC networks don't support dual-stack or IPv6-only subnets. For more information, see [Types of subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).  
`PRIVATE` subnet purpose |  | `subnetworkPurposes` | `SUBNET_PURPOSE_PRIVATE` | Falcon VPC networks support regular subnets, which have a `purpose` attribute value of `PRIVATE`. Falcon VPC networks don't support Private Service Connect subnets, proxy-only subnets, or Private NAT subnets. For more information, see [Purposes of subnets](https://docs.cloud.google.com/vpc/docs/subnets#purpose).  
`GCE_ENDPOINT` address purpose |  | `addressPurposes` | `GCE_ENDPOINT` | Falcon VPC networks support IP addresses with a `purpose` attribute value of `GCE_ENDPOINT`, which is used by internal IP addresses of instance NICs. Falcon VPC networks don't support special purpose IP addresses, such as the `SHARED_LOADBALANCER_VIP` purpose. For more information, see the [addresses resource reference](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses).  
Private Service Connect interfaces |  | `allowPscInterface` | `PSC_INTERFACE_ALLOWED` | Falcon VPC networks support [network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments) and connections from [virtual Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#virtual-specifications).  
Dynamic Network Interfaces |  | `allowSubInterfaces` | `SUBINTERFACES_BLOCKED` | Falcon VPC networks don't support [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-types).  
Attachments from `nic0` |  | `allowDefaultNicAttachment` | `DEFAULT_NIC_ATTACHMENT_BLOCKED` | Falcon VPC networks don't support attaching the `nic0` network interface of an instance to the network. Each RDMA NIC attached to the VPC network must not be `nic0`.  
External IP addresses for instances |  | `allowExternalIpAccess` | `EXTERNAL_IP_ACCESS_BLOCKED` | Falcon VPC networks don't support assigning [external IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses) to RDMA NICs. Consequently, RDMA NICs don't have internet access.  
Alias IP ranges |  | `allowAliasIpRanges` | `ALIAS_IP_RANGE_BLOCKED` | Falcon VPC networks don't support assigning [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) to RDMA NICs.  
IP forwarding |  | `allowIpForwarding` | `IP_FORWARDING_BLOCKED` | Falcon VPC networks don't support [IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward).  
Instance network migration |  | `allowNetworkMigration` | `NETWORK_MIGRATION_BLOCKED` | Falcon VPC networks don't support [migrating instance NICs between networks](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks).  
Auto mode |  | `allowAutoModeSubnet` | `AUTO_MODE_SUBNET_BLOCKED` | Falcon VPC networks can't be auto mode networks. For more information, see [subnet creation mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges).  
VPC Network Peering |  | `allowVpcPeering` | `VPC_PEERING_BLOCKED` | Falcon VPC networks don't support connecting to other VPC networks using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). Consequently, Falcon VPC networks don't support connecting to services using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).  
Static routes |  | `allowStaticRoutes` | `STATIC_ROUTES_BLOCKED` | Falcon VPC networks don't support [static routes](https://docs.cloud.google.com/vpc/docs/static-routes).  
Packet Mirroring |  | `allowPacketMirroring` | `PACKET_MIRRORING_BLOCKED` | Falcon VPC networks don't support [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring).  
Cloud NAT |  | `allowCloudNat` | `CLOUD_NAT_BLOCKED` | Falcon VPC networks don't support [Cloud NAT](https://docs.cloud.google.com/nat/docs).  
Cloud Router |  | `allowCloudRouter` | `CLOUD_ROUTER_BLOCKED` | Falcon VPC networks don't support [Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) and dynamic routes.  
Cloud Interconnect |  | `allowInterconnect` | `INTERCONNECT_BLOCKED` | Falcon VPC networks don't support [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) VLAN attachments.  
Cloud VPN |  | `allowVpn` | `VPN_BLOCKED` | Falcon VPC networks don't support [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) tunnels.  
Network Connectivity Center |  | `allowNcc` | `NCC_BLOCKED` | Falcon VPC networks don't support [NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview). You can't add a Falcon VPC network as a VPC spoke to a NCC hub.  
Cloud Load Balancing |  | `allowLoadBalancing` | `LOAD_BALANCING_BLOCKED` | Falcon VPC networks don't support [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). Consequently, Falcon VPC networks don't support load balancer features, including [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview).  
Private Google Access |  | `allowPrivateGoogleAccess` | `PRIVATE_GOOGLE_ACCESS_BLOCKED` | Falcon VPC networks don't support [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).  
Private Service Connect |  | `allowPsc` | `PSC_BLOCKED` | Falcon VPC networks don't support Private Service Connect [published services](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services), [endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints), or [backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).  
  
### RoCE VPC networks for VM instances (`roce`)

The following table lists the features that are supported by RoCE VPC networks for VM instances, which are created by using the `roce` network profile.

Feature | Supported | Network profile property | Network profile property value | Details  
---|---|---|---|---  
RDMA NICs |  | `interfaceTypes` | `MRDMA` | RoCE VPC networks for VM instances support only `MRDMA` NICs Other NIC types, such as `IRDMA`, `GVNIC`, `IDPF`, and `VIRTIO_NET`, aren't supported.  
Multi-NIC in the same network |  | `allowMultiNicInSameNetwork` | `MULTI_NIC_IN_SAME_NETWORK_ALLOWED` | RoCE VPC networks for VM instances support [multi-NIC instances](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts), allowing two or more RDMA NICs of the same instance to be in the same VPC network. Each NIC must attach to a unique subnet in the VPC network. See also RoCE VPC network multi-NIC considerations.  
IPv4-only subnets |  | `subnetworkStackTypes` | `SUBNET_STACK_TYPE_IPV4_ONLY` | RoCE VPC networks for VM instances support IPv4-only subnets, including the same [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) as regular VPC networks. RoCE VPC networks for VM instances don't support dual-stack or IPv6-only subnets. For more information, see [Types of subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).  
`PRIVATE` subnet purpose |  | `subnetworkPurposes` | `SUBNET_PURPOSE_PRIVATE` | RoCE VPC networks for VM instances support regular subnets, which have a `purpose` attribute value of `PRIVATE`. RoCE VPC networks for VM instances don't support Private Service Connect subnets, proxy-only subnets, or Private NAT subnets. For more information, see [Purposes of subnets](https://docs.cloud.google.com/vpc/docs/subnets#purpose).  
`GCE_ENDPOINT` address purpose |  | `addressPurposes` | `GCE_ENDPOINT` | RoCE VPC networks for VM instances support IP addresses with a `purpose` attribute value of `GCE_ENDPOINT`, which is used by internal IP addresses of instance NICs. RoCE VPC networks for VM instances don't support special purpose IP addresses, such as the `SHARED_LOADBALANCER_VIP` purpose. For more information, see the [addresses resource reference](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses).  
Alias IP ranges |  | `allowAliasIpRanges` | `ALIAS_IP_RANGES_ALLOWED` | RoCE VPC networks for VM instances support assigning [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) to MRDMA NICs. For more information, see [Considerations for RoCE VPC networks](https://docs.cloud.google.com/vpc/docs/alias-ip#roce-considerations) in the Alias IP ranges overview. | Attachments from `nic0` |  | `allowDefaultNicAttachment` | `DEFAULT_NIC_ATTACHMENT_BLOCKED` | RoCE VPC networks for VM instances don't support attaching the `nic0` network interfaces of an instance to the network. Each RDMA NIC attached to the VPC network must not be `nic0`.  
External IP addresses for instances |  | `allowExternalIpAccess` | `EXTERNAL_IP_ACCESS_BLOCKED` | RoCE VPC networks for VM instances don't support assigning [external IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses) to RDMA NICs. Consequently, RDMA NICs don't have internet access.  
Dynamic Network Interfaces |  | `allowSubInterfaces` | `SUBINTERFACES_BLOCKED` | RoCE VPC networks for VM instances don't support [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-types).  
Private Service Connect interfaces |  | `allowPscInterface` | `PSC_INTERFACE_BLOCKED` | RoCE VPC networks don't support [network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments) or connections from [Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces).  
IP forwarding |  | `allowIpForwarding` | `IP_FORWARDING_BLOCKED` | RoCE VPC networks for VM instances don't support [IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward).  
Instance network migration |  | `allowNetworkMigration` | `NETWORK_MIGRATION_BLOCKED` | RoCE VPC networks for VM instances don't support [migrating instance NICs between networks](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks).  
Auto mode |  | `allowAutoModeSubnet` | `AUTO_MODE_SUBNET_BLOCKED` | RoCE VPC networks for VM instances can't be auto mode networks. For more information, see [subnet creation mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges).  
VPC Network Peering |  | `allowVpcPeering` | `VPC_PEERING_BLOCKED` | RoCE VPC networks for VM instances don't support connecting to other VPC networks using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). Consequently, RoCE VPC networks for VM instances don't support connecting to services using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).  
Static routes |  | `allowStaticRoutes` | `STATIC_ROUTES_BLOCKED` | RoCE VPC networks for VM instances don't support [static routes](https://docs.cloud.google.com/vpc/docs/static-routes).  
Packet Mirroring |  | `allowPacketMirroring` | `PACKET_MIRRORING_BLOCKED` | RoCE VPC networks for VM instances don't support [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring).  
Cloud NAT |  | `allowCloudNat` | `CLOUD_NAT_BLOCKED` | RoCE VPC networks for VM instances don't support [Cloud NAT](https://docs.cloud.google.com/nat/docs).  
Cloud Router |  | `allowCloudRouter` | `CLOUD_ROUTER_BLOCKED` | RoCE VPC networks for VM instances don't support [Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) and dynamic routes.  
Cloud Interconnect |  | `allowInterconnect` | `INTERCONNECT_BLOCKED` | RoCE VPC networks for VM instances don't support [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) VLAN attachments.  
Cloud VPN |  | `allowVpn` | `VPN_BLOCKED` | RoCE VPC networks for VM instances don't support [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) tunnels.  
Network Connectivity Center |  | `allowNcc` | `NCC_BLOCKED` | RoCE VPC networks for VM instances don't support [NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview). You can't add a VPC network with an RDMA network profile as a VPC spoke to a NCC hub.  
Cloud Load Balancing |  | `allowLoadBalancing` | `LOAD_BALANCING_BLOCKED` | RoCE VPC networks for VM instances don't support [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). Consequently, RoCE VPC networks for VM instances don't support load balancer features, including [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview).  
Private Google Access |  | `allowPrivateGoogleAccess` | `PRIVATE_GOOGLE_ACCESS_BLOCKED` | RoCE VPC networks for VM instances don't support [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).  
Private Service Connect |  | `allowPsc` | `PSC_BLOCKED` | RoCE VPC networks don't support Private Service Connect [published services](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services), [endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints), or [backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).  
  
### RoCE VPC networks for bare metal instances (`roce-metal`)

The following table lists the features that are supported by RoCE VPC networks for bare metal instances, which are created by using the `roce-metal` network profile.

In addition to the properties described in the table, see the following limitations that apply to GPU bare metal instances:

  * GPU bare metal instances can't use the following UDP ports in RoCE VPC networks because they are reserved by Google Cloud: `3882-3895` and `13882-13895`.
  * GPU bare metal instances can't use the following IPv6 link-local address range, because it is reserved by Google Cloud: `fe80::badd:c0de:cafe:0/120`.

Feature | Supported | Network profile property | Network profile property value | Details  
---|---|---|---|---  
RDMA NICs |  | `interfaceTypes` | `MRDMA` | RoCE VPC networks for bare metal instances support only `MRDMA` NICs Other NIC types, such as `IRDMA`, `GVNIC`, `IDPF`, and `VIRTIO_NET`, aren't supported.  
Multi-NIC in the same network |  | `allowMultiNicInSameNetwork` | `MULTI_NIC_IN_SAME_NETWORK_ALLOWED` | RoCE VPC networks for bare metal instances support [multi-NIC instances](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts), allowing two or more RDMA NICs of the same instance to be in the same VPC network. See also RoCE VPC network multi-NIC considerations.  
Multi-NIC in the same subnet |  | `allowMultiNicInSameSubnetwork` | `MULTI_NIC_IN_SAME_SUBNETWORK_ALLOWED` | RoCE VPC networks for bare metal instances support [multi-NIC instances](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts), allowing two or more RDMA NICs of the same instance to be in the same subnet of a VPC network. See also RoCE VPC network multi-NIC considerations.  
Predefined network ULA IPv6 range |  | `predefinedNetworkInternalIpv6Range` | ULA_IPV6_RANGE | RoCE VPC networks for bare metal instances support internal IPv6 and have a predefined `/48` [unique local address (ULA)](https://datatracker.ietf.org/doc/html/rfc4193) range. The predefined range is provided by Google Cloud for each network profile instance and isn't configurable.  
One IPv6-only subnet |  | `subnetworkStackTypes` | `SUBNET_STACK_TYPE_IPV6_ONLY` | RoCE VPC networks for bare metal instances support a single, automatically-provided IPv6-only subnet that uses a predefined IPv6 subnet range and naming convention as described in the following table row. RoCE VPC networks for bare metal instances don't support dual-stack or IPv4-only subnets, or the creation of additional IPv6-only subnets. For more information, see [Types of subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).  
Predefined IPv6 subnet range and name prefix |  | `predefinedSubnetworkRanges` |  `ipv6Range: ULA_IPV6_RANGE`  
  
`namePrefix: default-subnet-1` |  RoCE VPC networks for bare metal instances have a single subnet that is automatically-provided and has the following properties:

  * The subnet uses a predefined `/48` IPv6 range that exactly matches the network's `/48` range. 
  * The subnet uses the following naming format: `default-subnet-1-NETWORK_NAME`, where NETWORK_NAME is the name that you provided when you created the network. 

  
`PRIVATE` subnet purpose |  | `subnetworkPurposes` | `SUBNET_PURPOSE_PRIVATE` | RoCE VPC networks for bare metal instances support regular subnets, which have a `purpose` attribute value of `PRIVATE`. RoCE VPC networks for bare metal instances don't support Private Service Connect subnets, proxy-only subnets, or Private NAT subnets. For more information, see [Purposes of subnets](https://docs.cloud.google.com/vpc/docs/subnets#purpose).  
`GCE_ENDPOINT` address purpose |  | `addressPurposes` | `GCE_ENDPOINT` | RoCE VPC networks for bare metal instances support IP addresses with a `purpose` attribute value of `GCE_ENDPOINT`, which is used by internal IP addresses of instance NICs. RoCE VPC networks for bare metal instances don't support special purpose IP addresses, such as the `SHARED_LOADBALANCER_VIP` purpose. For more information, see the [addresses resource reference](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses).  
Subnet creation |  | `allowSubnetworkCreation` | `SUBNETWORK_CREATION_BLOCKED` | RoCE VPC networks for bare metal instances don't support [creating subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only) in the network.  
Attachments from `nic0` |  | `allowDefaultNicAttachment` | `DEFAULT_NIC_ATTACHMENT_BLOCKED` | RoCE VPC networks for bare metal instances don't support attaching the `nic0` network interfaces of an instance to the network. Each RDMA NIC attached to the VPC network must not be `nic0`.  
Static IP addresses for instances |  | `allowAddressCreation` | `ADDRESS_CREATION_BLOCKED` |  RoCE VPC networks for bare metal instances don't support reserving static [internal](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address) or [external](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address) IP addresses, or configuring static [internal](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address) or [external](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address) IP addresses for instances.  Consequently, instances in the network can use only ephemeral internal IP addresses.   
External IP addresses for instances |  | `allowExternalIpAccess` | `EXTERNAL_IP_ACCESS_BLOCKED` | RoCE VPC networks for bare metal instances don't support assigning [external IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses), either static or ephemeral, to RDMA NICs. Consequently, RDMA NICs don't have internet access.  
Dynamic Network Interfaces |  | `allowSubInterfaces` | `SUBINTERFACES_BLOCKED` | RoCE VPC networks for bare metal instances don't support [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-types).  
Private Service Connect interfaces |  | `allowPscInterface` | `PSC_INTERFACE_BLOCKED` | RoCE VPC networks don't support [network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments) or connections from [Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces).  
Alias IP ranges |  | `allowAliasIpRanges` | `ALIAS_IP_RANGE_BLOCKED` | RoCE VPC networks for bare metal instances don't support assigning [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) to RDMA NICs.  
IP forwarding |  | `allowIpForwarding` | `IP_FORWARDING_BLOCKED` | RoCE VPC networks for bare metal instances don't support [IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward).  
Instance network migration |  | `allowNetworkMigration` | `NETWORK_MIGRATION_BLOCKED` | RoCE VPC networks for bare metal instances don't support [migrating instance NICs between networks](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks).  
Auto mode |  | `allowAutoModeSubnet` | `AUTO_MODE_SUBNET_BLOCKED` | RoCE VPC networks for bare metal instances can't be auto mode networks. For more information, see [subnet creation mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges).  
VPC Network Peering |  | `allowVpcPeering` | `VPC_PEERING_BLOCKED` | RoCE VPC networks for bare metal instances don't support connecting to other VPC networks using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). Consequently, RoCE VPC networks for bare metal instances don't support connecting to services using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).  
Static routes |  | `allowStaticRoutes` | `STATIC_ROUTES_BLOCKED` | RoCE VPC networks for bare metal instances don't support [static routes](https://docs.cloud.google.com/vpc/docs/static-routes).  
VPC firewall rules |  | `allowVpcFirewallRules` | `VPC_FIREWALL_RULES_BLOCKED` | RoCE VPC networks for bare metal instances don't support [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).  
Firewall policies |  | `allowFirewallPolicy` | `FIREWALL_POLICY_BLOCKED` | RoCE VPC networks for bare metal instances don't support [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).  
Packet Mirroring |  | `allowPacketMirroring` | `PACKET_MIRRORING_BLOCKED` | RoCE VPC networks for bare metal instances don't support [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring).  
Cloud NAT |  | `allowCloudNat` | `CLOUD_NAT_BLOCKED` | RoCE VPC networks for bare metal instances don't support [Cloud NAT](https://docs.cloud.google.com/nat/docs).  
Cloud Router |  | `allowCloudRouter` | `CLOUD_ROUTER_BLOCKED` | RoCE VPC networks for bare metal instances don't support [Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) and dynamic routes.  
Cloud Interconnect |  | `allowInterconnect` | `INTERCONNECT_BLOCKED` | RoCE VPC networks for bare metal instances don't support [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) VLAN attachments.  
Cloud VPN |  | `allowVpn` | `VPN_BLOCKED` | RoCE VPC networks for bare metal instances don't support [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) tunnels.  
Network Connectivity Center |  | `allowNcc` | `NCC_BLOCKED` | RoCE VPC networks for bare metal instances don't support [NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview). You can't add a RoCE VPC network as a VPC spoke to a NCC hub.  
Cloud Load Balancing |  | `allowLoadBalancing` | `LOAD_BALANCING_BLOCKED` | RoCE VPC networks for bare metal instances don't support [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). Consequently, RoCE VPC networks for bare metal instances don't support load balancer features, including [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview).  
Private Google Access |  | `allowPrivateGoogleAccess` | `PRIVATE_GOOGLE_ACCESS_BLOCKED` | RoCE VPC networks for bare metal instances don't support [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).  
Private Service Connect |  | `allowPsc` | `PSC_BLOCKED` | RoCE VPC networks for bare metal instances don't support Private Service Connect [published services](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services), [endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints), or [backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).  
  
## Multi-NIC considerations for RoCE VPC networks

To support workloads that benefit from cross-rail GPU-to-GPU communication, RoCE VPC networks support instances that have multiple `MRDMA` NICs in the network. Placing two or more `MRDMA` NICs in the same RoCE VPC network might affect network performance, including increased latency. `MRDMA` NICs use [NCCL](https://developer.nvidia.com/nccl). NCCL attempts to align all network transfers, even for cross-rail communication. For example, it uses PXN to copy data through NVlink to a rail-aligned GPU before transferring it over the network.

## Number of connections limit for RoCE VPC networks

A given RoCE VPC network has the following system limit:

Item | Limit | Notes  
---|---|---  
Maximum number of connections | 20,000 | The maximum number of connections over `MRDMA` vNICs per 2-tuple (source IP address, destination IP address). A connection is established when a source IP address and destination IP address communicate for the first time. For a given 2-tuple, [multiple receive and transmit queue pairs](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx) share the connection. For example, assume `instance-a` and `instance-b` both have 8 `MRDMA` vNICs, each with 2 routable IP addresses:

  * The initial connection count is 0.
  * When the first IP address on the first vNIC of `instance-a` communicates with the first IP address on the first vNIC of `instance-b`, the connection count becomes 1.
  * When `instance-a` opens another queue pair to `instance-b` using the same IP addresses on the same vNICs, the connection count remains 1.
  * When `instance-a` starts a rail-aligned all-to-all communicator engaging all 8 vNICs, the connection count becomes 8.

If the connection count goes beyond the limit of 20,000, new connections might see failures, but existing connections aren't impacted.  
  
## What's next

  * [Network profiles for specific use cases](https://docs.cloud.google.com/vpc/docs/network-profiles)
  * [Create a VPC network for RDMA NICs](https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma)
  * [Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
