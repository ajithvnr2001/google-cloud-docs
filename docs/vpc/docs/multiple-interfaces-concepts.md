---
url: https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts/
title: Multiple network interfaces \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:16:01.268314+00:00
---

# Multiple network interfaces  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Multiple network interfaces

This page provides an overview of multiple network interfaces for Compute Engine instances. Instances with multiple network interfaces are referred to as _multi-NIC instances_.

An instance network interface connects to a Virtual Private Cloud (VPC) network and can be either a _virtual network interface (vNIC)_ or a _Dynamic NIC_ , where a Dynamic NIC is a child sub-interface of a parent vNIC. An instance's vNICs are backed by one or more physical NICs on the host server that runs the instance. For more information, see Network interface types.

## Use cases

Multi-NIC instances are useful in the following scenarios:

  * **To connect to resources in separate VPC networks** : multi-NIC instances can connect to resources located in different VPC networks that aren't connected to each other through VPC Network Peering or NCC.

    * Because each interface of a multi-NIC instance is in a separate VPC network, you can use each interface for a unique purpose. For example, you can use some interfaces to route packets between VPC networks that carry production traffic and another interface for management or configuration purposes.

    * Within the guest OS of each multi-NIC instance, you must configure route policies and local route tables.

  * **To route packets between VPC networks** : multi-NIC instances can be used as next hops for routes to connect two or more VPC networks.

    * Software running within the guest OS of a multi-NIC instance can perform packet inspection, network address translation (NAT), or another network security function.

    * When connecting VPC networks using multi-NIC instances, it's a best practice to configure two or more multi-NIC instances, using them as backends for an internal passthrough Network Load Balancer in each VPC network. For more information, see [Use cases](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#use_cases) in the Internal passthrough Network Load Balancers as next hops documentation.

  * **To increase the total network bandwidth of an instance** : multi-NIC instances support increased bandwidth as follows:

    * For some machine types in Google Cloud, instances are backed by multiple physical NICs on the host server. Creating an instance with multiple vNICs where each vNIC uses a different physical NIC increases the total [network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth) of the instance. For more information, see Bandwidth for multiple network interfaces in the same VPC network.

    * For most machine types in Google Cloud, instances are backed by a single physical NIC on the host server, and each vNIC uses the same physical NIC. When vNICs share a physical NIC, adding vNICs doesn't increase network bandwidth.




You can also use multi-NIC instances with [Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) to connect service producer and consumer networks in different projects.

## Network interface types

See the following sections for details about network interface types in Google Cloud.

### Instance network interfaces

Compute Engine instances connect to VPC networks by using network interfaces that you configure, which can be either vNICs or Dynamic NICs. These instance network interfaces correspond to the [`instances.networkInterfaces[]`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances#resource:-instance) resource and property in the Compute Engine API.

For more information about each type of instance network interface, see the following:

  * **Virtual network interface (vNIC)** : a software-defined network interface exposed to your instance's guest OS that lets your instance connect to VPC networks. Each instance must have at least one vNIC.

    * You can only configure vNICs when creating an instance.

    * The name of a vNIC assigned by Google Cloud has the following format: `nicN`, such as `nic0`. The corresponding guest OS-assigned name depends on the operating system, such as `ens4` for Ubuntu.

    * A vNIC can be one of the following types, depending on the associated VPC network. Each type corresponds to a specific network driver in the guest OS:

      * Regular VPC networks accept attachments from the following vNIC types: [`GVNIC`](https://docs.cloud.google.com/compute/docs/networking/using-gvnic), [`IDPF`](https://docs.cloud.google.com/compute/docs/networking/using-idpf), and [`VIRTIO_NET`](https://ozlabs.org/%7Erusty/virtio-spec/virtio-0.9.5.pdf).

      * VPC networks with an [RDMA network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles) accept attachments from vNIC types [`IRDMA`](https://docs.cloud.google.com/compute/docs/networking/using-irdma) or [`MRDMA`](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#gpudirect-rdma-mrdma), which are also called RDMA vNICs.

For information about which machine types support which vNIC types, see [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).

  * **Dynamic NIC** : a child of a parent vNIC that is implemented as a sub-interface in the guest OS of your instance.

    * You can configure Dynamic NICs when you create an instance, or add them later.

    * The name of a Dynamic NIC assigned by Google Cloud has the following format: `nicN.VLAN_ID`, such as `nic0.2`. The corresponding guest OS-assigned name depends on the operating system. For example, if you use the guest agent to manage Dynamic NICs in Ubuntu, the name might be `a-gcp.ens4.2`.

    * Dynamic NICs aren't supported in VPC networks with an [RDMA network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).

For more information, see Dynamic NICs.




#### Dynamic NIC details

If your use case requires any of the following, use Dynamic NICs. Ensure that you also review the properties and limitations of Dynamic NICs.

  * You need to add or remove network interfaces to or from existing instances. Adding or removing Dynamic NICs doesn't require restarting or recreating the instance.

  * You need more network interfaces than the maximum number of vNICs. For most machine types in Google Cloud, the maximum number is 10; however, you can configure up to 16 total interfaces by using Dynamic NICs. For more information, see Maximum number of network interfaces.

  * You need to configure multi-NIC Compute Engine bare metal instances, which only have one vNIC.




##### Properties of Dynamic NICs

See the following information about the properties of Dynamic NICs:

  * Dynamic NICs are VLAN interfaces that use the [IEEE 802.1Q](https://en.wikipedia.org/wiki/IEEE_802.1Q) standard packet format. See the following considerations:

    * The VLAN ID of a Dynamic NIC must be an integer from 2 to 255.
    * The VLAN ID of a Dynamic NIC must be unique within a parent vNIC. However, Dynamic NICs that belong to different parent vNICs can use the same VLAN ID.
  * Google Cloud uses the following format for the name of a Dynamic NIC: `nicNUMBER.VLAN_ID`, where

    * `nicNUMBER` is the name of the parent vNIC, such as `nic0`.
    * `VLAN_ID` is the VLAN ID that you set, such as `4`.

An example Dynamic NIC name is `nic0.4`.

  * Creating an instance with Dynamic NICs or adding Dynamic NICs to an existing instance requires additional steps to install and manage the corresponding VLAN interfaces in the guest OS. You can use one of the following methods:

    * Configure automatic management of Dynamic NICs by using the guest agent.

    * Configure the guest OS manually.

For more information, see [Configure the guest OS for Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics#configure-guest-os).

  * Dynamic NICs share the bandwidth of their parent vNIC. To prevent any of the network interfaces from consuming all of the bandwidth, you must create an application-specific traffic policy in the guest OS to prioritize or distribute traffic, such as by using Linux Traffic Control (TC).

  * Dynamic NICs share the same [receive and transmit queues](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx) as their parent vNIC. To configure a network interface to use different receive and transmit queues, use vNICs instead of Dynamic NICs.

  * The stack type of a Dynamic NIC can be the same as or different than its parent vNIC. For example, you can create IPv6-only and dual-stack Dynamic NICs under an IPv4-only parent vNIC.




##### Limitations of Dynamic NICs

See the following limitations of Dynamic NICs:

  * You can't modify the following properties of a Dynamic NIC after it is created:

    * The parent vNIC to which the Dynamic NIC belongs.
    * The VLAN ID of the Dynamic NIC.
  * A Dynamic NIC can't be deleted if the Dynamic NIC is a load-balanced network interface.

  * Dynamic NICs don't support the following:

    * [Advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos) and [network edge security policies](https://docs.cloud.google.com/armor/docs/network-edge-policies) for Google Cloud Armor
    * Configuring IP addresses by using [per-instance configurations](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs) for MIGs.
    * Features that rely on packet intercept, such as [firewall endpoints](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#specifications)
    * [Compute Engine Windows drivers](https://docs.cloud.google.com/compute/docs/images/guest-environment#gce-windows-drivers)
  * Dynamic NICs aren't supported for use with [GPU instances](https://docs.cloud.google.com/compute/docs/gpus). For more information, see Creation errors and decreased performance when using Dynamic NICs with GPU instances.

  * Dynamic NICs require that you manually create local routes in certain scenarios. For more information, see Dropped packets when using Dynamic NICs with alias IP ranges, protocol forwarding, or Passthrough Network Load Balancers.




### Physical NICs

A physical NIC is the hardware component directly installed on the host server where an instance runs. Depending on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) of your instance, the instance's vNICs map to one or more physical NICs on a host server as follows:

  * **Instances backed by one physical NIC** : For most machine types, instances run on a host server with a single physical NIC. For a given instance, all of the instance's vNICs map to the single physical NIC.

  * **Instances backed by multiple physical NICs** : For a limited set of machine types, such as [C4N machine types](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_machine_types) and [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus), instances run on a host server with multiple physical NICs. For a given instance, Compute Engine maps the instance's vNICs to different physical NICs.

    * Instances backed by multiple physical NICs support use cases such as increased [network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth) and GPU-to-GPU communication over an RoCE VPC network. For more information, see [Network support for C4N instances](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_network) and [Networking and GPU machines](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth).

    * When you create the instance, Compute Engine maps each vNIC to a unique physical NIC, up to the total physical NIC count of the instance's machine type.

    * To understand support for multiple physical NICs, view the documentation for a given machine series. If applicable, the table of machine types includes a column titled _Physical NIC count_. For example, see [C4N machine types](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_machine_types).




Additionally, for most machine types, instances share a host server with other instances. Instances that share a host server also share its physical NIC or set of physical NICs. However, for some machine types, such as [bare metal](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances) machine types or [H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series) and [H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series) machine types, a single instance occupies an entire host server.

## Specifications

The following specifications apply to instances with multiple network interfaces:

  * **Instances and network interfaces** : every instance has a `nic0` interface. The maximum number of network interfaces varies depending on the instance's machine type.

    * Each interface has an associated stack type, which determines the supported subnet stack types and IP address versions. For more information, see Stack type and IP addresses.
  * **Network and subnetwork requirements** : each network interface must use a unique subnet in a VPC network.

    * Attaching network interfaces to subnets in different VPC networks is supported.

    * Attaching network interfaces to different subnets in the same VPC network is supported in the following scenarios:

      * For regular VPC networks, multiple network interfaces can use the same VPC network according to the rules for multiple network interfaces in the same VPC network. Cloud Load Balancing and static routes have additional rules that are described in Load balancers and Static routes.

      * For VPC networks created with an RDMA network profile, multiple RDMA NICs can use the same VPC network. For more information, see the table for each network profile in [Supported and unsupported features](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#supported-features).

    * A VPC network and subnet must exist before you can create an instance whose network interface uses the network and subnet. For more information about creating networks and subnets, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

    * Network interface bonding with link aggregation isn't supported. For details about how multiple network interfaces in the same VPC network affect bandwidth, see Bandwidth for multiple network interfaces in the same VPC network.

  * **Project of instance and subnets** : for multi-NIC instances in standalone projects, each network interface must use a subnet located in the same project as the instance.

    * For instances in Shared VPC host or service projects, see Shared VPC .

    * [Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) provide a way for a multi-NIC instance to have network interfaces in subnets in different projects. For more information, see [About network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments).

  * **IP forwarding, MTU, and routing considerations** : multi-NIC instances require careful planning for the following instance and interface specific configuration options:

    * The IP forwarding option is configurable on a per instance basis, applying to all network interfaces. For more information, see [Enable IP forwarding for instances](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward).

    * Each network interface can use a unique maximum transmission unit (MTU), matching the MTU of the associated VPC network. For more information, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).

    * Each instance receives a default route using DHCP Option 121, as defined by [RFC 3442](https://datatracker.ietf.org/doc/html/rfc3442). The default route is associated with `nic0`. Unless manually configured otherwise, any traffic leaving an instance for any destination other than a directly connected subnet will leave the instance using the default route on `nic0`.

On Linux systems, you can configure custom rules and routes within the guest OS using the `/etc/iproute2/rt_tables` file and the `ip rule` and `ip route` commands. For more information, consult the guest OS documentation. For an example, see the following tutorial: [Configure routing for an additional interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface).




### Rules for multiple network interfaces in the same VPC network

Compute Engine enforces _all_ of the following rules when two or more network interfaces of a single instance use the same VPC network:

  * **Unique subnet** : Each network interface must be attached to a unique subnet.

  * **Additional vNICs must be attached to the network that contains`nic0`**: Two or more vNICs can be attached to the same VPC network only if that network also contains the `nic0` vNIC. For example, `nic0`, `nic1`, and `nic2` can be attached to unique subnets in the same VPC network, but `nic1` and `nic2` can't be attached to the same VPC network if `nic0` isn't attached to that network.

  * **A network containing a Dynamic NIC and at least one other NIC must contain each Dynamic NIC's parent vNIC** : For example:

    * To attach the `nic1.6` and `nic1.7` Dynamic NICs to the same VPC network, you must also attach their parent vNIC, `nic1`, to that VPC network.

    * To attach the `nic1.6` Dynamic NIC and the `nic2` vNIC to the same VPC network, you must also attach the `nic1` and `nic0` vNICs to that VPC network. Attaching `nic1` is required because `nic1` is the parent vNIC of the `nic1.6` Dynamic NIC. Attaching `nic0` is required because the network contains multiple vNICs.

    * To attach the `nic2.5` and `nic3.6` Dynamic NICs to the same VPC network, you must also attach all of the following vNICs to that same VPC network: `nic0`, `nic2`, and `nic3`. Attaching the `nic2` and `nic3` vNICs is required because they are the parent vNICs of the `nic2.5` and `nic3.6` Dynamic NICs. Attaching `nic0` is required because the network contains multiple vNICs.

  * **Unique network for each Private Service Connect interface** : Two or more network interfaces can't be attached to the same VPC network if one of the network interfaces uses a network attachment in that network.




### Bandwidth for multiple network interfaces in the same VPC network

Multiple vNICs in the same VPC network affects [network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth) according to these rules:

  * For instances backed by one physical NIC, attaching two or more vNICs to the same VPC network never increases network bandwidth.

  * For instances backed by multiple physical NICs, attaching two or more vNICs to the same VPC network increases network bandwidth when Compute Engine maps the vNICs to different physical NICs.




Regardless of machine type, adding Dynamic NICs to an instance doesn't increase bandwidth because a Dynamic NIC uses the bandwidth of its parent vNIC.

### Stack types and IP addresses

When you create a network interface, you specify one of the following _interface stack types_ :

  * IPv4-only
  * Dual-stack
  * IPv6-only



A VM instance can have network interfaces that have different stack types.

The following table describes supported subnet stack types and IP address details for each interface stack type:

Interface | IPv4-only subnet | Dual-stack subnet | IPv6-only subnet | IP address details  
---|---|---|---|---  
IPv4-only (single-stack) |  |  |  | IPv4 addresses only. See IPv4 address details.  
IPv4 and IPv6 (dual-stack) |  |  |  | Both IPv4 and IPv6 addresses. See IPv4 address details and IPv6 address details  
IPv6-only (single-stack) |  |  |  | IPv6 addresses only. See IPv6 address details.  
  
#### Changing network interface stack type

You can [change the stack type](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#update-vm-stacktype) of a network interface as follows:

  * You can convert an IPv4-only interface to dual-stack if the interface's subnet is a dual-stack subnet or if you stop the instance and assign the interface to a dual-stack subnet.

  * You can convert a dual-stack interface to IPv4-only.




You can't change the stack type of an IPv6-only interface. IPv6-only interfaces are only supported when creating instances.

#### IPv4 address details

Each IPv4-only or dual-stack network interface receives a primary internal IPv4 address. Each interface optionally supports alias IP ranges and an external IPv4 address. The following are the IPv4 specifications and requirements:

  * **Primary internal IPv4 address** : Compute Engine assigns the network interface a primary internal IPv4 address from the primary IPv4 address range of the interface's subnet. The primary internal IPv4 address is allocated by DHCP.

    * You can control which primary internal IPv4 address is assigned by [configuring a static internal IPv4 address](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address) or by specifying a custom ephemeral internal IPv4 address.

    * Within a VPC network, the primary internal IPv4 address of each VM network interface is unique.

  * **Alias IP ranges** : optionally, you can assign the interface one or more alias IP ranges. Each alias IP range can come from either the primary IPv4 address range or a secondary IPv4 address range of the interface's subnet.

    * Within a VPC network, each interface's alias IP range must be unique.
  * **External IPv4 address** : optionally, you can assign the interface an ephemeral or reserved external IPv4 address. Google Cloud ensures the uniqueness of each external IPv4 address.




#### IPv6 address details

Compute Engine assigns each dual-stack or IPv6-only network interface a `/96` IPv6 address range from the `/64` IPv6 address range of the interface's subnet:

  * Whether the `/96` IPv6 address range is internal or external depends on the _IPv6 access type_ of the interface's subnet. Google Cloud ensures the uniqueness of each internal and external IPv6 address range. For more information, see [IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-specifications).

    * If an instance needs both an internal IPv6 address range and an external IPv6 address range: you must configure two dual-stack interfaces, two IPv6-only interfaces, or one dual-stack interface and one IPv6-only interface. The subnet used by one interface must have an external IPv6 address range, and the subnet used by the other interface must have an internal IPv6 address range.
  * The first IPv6 address (`/128`) is configured on the interface by DHCP. For more information, see [IPv6 address assignment](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#ipv6-assignment).

  * You can control which `/96` IPv6 address range is assigned by configuring a static [internal](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address) or [external](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address) IPv6 address range. For internal IPv6 addresses, you can specify a custom ephemeral internal IPv6 address.




If you are connecting an instance to multiple networks by using IPv6 addresses, install `google-guest-agent` version [20220603.00](https://github.com/GoogleCloudPlatform/guest-agent/releases/tag/20220603.00) or later. For more information, see [I can't connect to a secondary interface's IPv6 address](https://docs.cloud.google.com/vpc/docs/troubleshoot-multiple-interfaces#connect-ipv6).

### Maximum number of network interfaces

For most machine types, the maximum number of network interfaces that you can attach to an instance scales with the number of vCPUs as described in the following tables.

The following are machine-specific exceptions:

  * Most Compute Engine bare metal instances support only a single vNIC. However, select bare metal machine types support multiple vNICs, such as Z4M. For information about the number of supported network interfaces for Z4M instances, see [Create a Cloud RDMA-enabled instance](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-rdma#create-vm-with-rdma).

  * The maximum number of vNICs is different for some accelerator optimized machine types, such as A3, A4, and A4X. For more information, see [Accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines).




###  Max interface numbers 

Use the following table to determine how many network interfaces can be attached to an instance.

Number of vCPU | Maximum number of vNICs | Maximum number of Dynamic NICs | Maximum number of network interfaces  
(vNICs + Dynamic NICs)  
---|---|---|---  
2 or fewer | 2 | 1 | 2  
4 | 4 | 3 | 4  
6 | 6 | 5 | 6  
8 | 8 | 7 | 8  
10 | 10 | 9 | 10  
12 | 10 | 10 | 11  
14 | 10 | 11 | 12  
16 | 10 | 12 | 13  
18 | 10 | 13 | 14  
20 | 10 | 14 | 15  
22 or more | 10 | 15 | 16  
  
###  Reference formulas 

The following table provides the formulas used to calculate the maximum number of network interfaces for an instance. The formula depends on the number of vCPU.

Number of vCPU (X) | Maximum number of vNICs | Maximum number of Dynamic NICs | Maximum number of network interfaces  
(vNICs + Dynamic NICs)  
---|---|---|---  
`X=1` | `2` | `1` | `2`  
`2 ≤ X ≤ 10` | `X` | `(X-1)` | `X`  
`X ≥ 12` | `10` | `min(15, (X-10)/2 + 9)` | `min(16, (X-10)/2 + 10)`  
  
#### Example distributions of Dynamic NICs

You don't have to distribute Dynamic NICs evenly across vNICs. However, you might want an even distribution because Dynamic NICs share the bandwidth of their parent vNIC.

An instance must have at least one vNIC. For example, an instance that has 2 vCPUs can have one of the following configurations:

  * 1 vNIC
  * 2 vNICs
  * 1 vNIC and 1 Dynamic NIC



The following tables provide example configurations that evenly distribute Dynamic NICs across vNICs while using the maximum number of network interfaces for a given number of vCPU.

###  2 vCPUs, 2 NICs 

The following table provides examples for an instance with 2 vCPUs that show how many Dynamic NICs you can have for a given number of vNICs.

Number of vCPU | Number of vNICs | Number of Dynamic NICs per vNIC | Total number of network interfaces (vNICs + Dynamic NICs)  
---|---|---|---  
2 | 1 | 1 | 2  
2 | 0  
  
###  4 vCPUs, 4 NICs 

The following table provides examples for an instance with 4 vCPUs that show how many Dynamic NICs you can have for a given number of vNICs.

Number of vCPU | Number of vNICs | Number Dynamic NICs per vNIC | Total number of network interfaces (vNICs + Dynamic NICs)  
---|---|---|---  
4 | 1 | 3 | 4  
2 | 1  
4 | 0  
  
###  8 vCPUs, 8 NICs 

The following table provides examples for an instance with 8 vCPUs that show how many Dynamic NICs you can have for a given number of vNICs.

Number of vCPU | Number of vNICs | Number of Dynamic NICs per vNIC | Total number of network interfaces (vNICs + Dynamic NICs)  
---|---|---|---  
8 | 1 | 7 | 8  
2 | 3  
4 | 1  
8 | 0  
  
###  14 vCPUs, 12 NICs 

The following table provides examples for an instance with 12 vCPUs that show how many Dynamic NICs you can have for a given number of vNICs.

Number of vCPU | Number of vNICs | Number of Dynamic NICs per vNIC | Total number of network interfaces (vNICs + Dynamic NICs)  
---|---|---|---  
14 | 1 | 11 | 12  
2 | 5  
4 | 2  
6 | 1  
  
###  22 vCPUs, 16 NICs 

The following table provides examples for an instance with 22 vCPUs that show how many Dynamic NICs you can have for a given number of vNICs.

Number of vCPU | Number of vNICs | Number of Dynamic NICs per vNIC | Total number of network interfaces (vNICs + Dynamic NICs)  
---|---|---|---  
22 | 1 | 15 | 16  
2 | 7  
4 | 3  
8 | 1  
  
## Product interactions

This section describes interactions between multi-NIC instances and other products and features in Google Cloud.

### Shared VPC

Except for Private Service Connect interfaces, the subnet and project relationship of a multi-NIC instance in a Shared VPC host or service project is as follows:

  * Each network interface of a multi-NIC instance located in a Shared VPC host project must use a subnet of a Shared VPC network in the host project.

  * Each network interface of a multi-NIC instance located in a Shared VPC service project can use either of the following:

    * A subnet of a VPC network in the service project.
    * A subnet of a Shared VPC network in the host project.



For more information about Shared VPC, see:

  * [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc)
  * [Provision Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc)



### Compute Engine internal DNS

Compute Engine creates internal DNS name A and PTR records only for the primary internal IPv4 address of the `nic0` network interface of an instance. Compute Engine _doesn't_ create internal DNS records for any IPv4 or IPv6 address associated with a network interface different from `nic0`.

For more information, see [Compute Engine internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns).

### Static routes

[Static routes](https://docs.cloud.google.com/vpc/docs/static-routes) can be scoped to specific instances by using [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags). When a network tag is associated with an instance, the tag applies to _all_ network interfaces of the instance. Consequently, adding a network tag to or removing a network tag from an instance might change which static routes apply to _any_ of the instance's network interfaces.

When you create a static route whose next hop is an instance:

  * If you specify a next hop instance by name and zone (`next-hop-instance`), packets are delivered only to the `nic0` vNIC of the instance, and the `nic0` vNIC must be attached to the same VPC network in which the static route is created.

  * If you specify a next hop instance by address (`next-hop-address`), packets can be delivered to a specific vNIC or Dynamic NIC in the same VPC in which the static route is created.




For more information, see [Next hops and features](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops).

### Load balancers

The following table describes which instance network interfaces meet the necessary conditions to receive load-balanced traffic, including situations when multiple interfaces are attached to the same VPC network according to the rules for multiple network interfaces in the same VPC network. A network interface that meets the necessary load balancer conditions is a _load balancer target interface_. An instance has exactly one load balancer target interface in each VPC network that it uses, even if it has two or more interfaces in the same network.

Interface | Conditions for receiving load-balanced traffic  
---|---  
`nic0` vNIC | Can be attached to a VPC network with or without other network interfaces:

  * When multiple vNICs share a common VPC network with the `nic0` vNIC, only `nic0` can receive load-balanced traffic.
  * When one or more Dynamic NICs share a common VPC network with the `nic0` vNIC, only `nic0` can receive load-balanced traffic.

  
Non-`nic0` vNIC | Must be attached to a VPC network without any other vNICs:

  * Can be attached to a VPC network by itself.
  * When one or more Dynamic NICs share a common VPC network with a parent vNIC, only the parent vNIC can receive load-balanced traffic.

  
Dynamic NIC | Must be attached to a unique VPC network without other network interfaces (no other vNICs _and_ no other Dynamic NICs).  
  
The following tables detail the load balancer and backend group configurations that you can use to send traffic to a load balancer target interface.

#### Load balancer target interfaces for Application Load Balancers and proxy Network Load Balancers

Type of backend group  
on a backend service of an Application Load Balancer  
or proxy Network Load Balancer | Load balancer target interface  
---|---  
`nic0` vNIC | Non-`nic0` vNIC | Dynamic NIC  
Instance group |  |  |   
`GCE_VM_IP_PORT` NEG |  |  |   
  
#### Load balancer target interfaces for passthrough Network Load Balancers

For internal passthrough Network Load Balancers:

Type of backend group  
on a backend service of an internal passthrough Network Load Balancer | Load balancer target interface  
---|---  
`nic0` vNIC | Non-`nic0` vNIC | Dynamic NIC  
Instance group |  |  |   
`GCE_VM_IP` NEG |  |  |   
  
For external passthrough Network Load Balancers:

Type of backend  
of an external passthrough Network Load Balancer | Load balancer target interface  
---|---  
`nic0` vNIC | Non-`nic0` vNIC | Dynamic NIC  
Instance group  
on a backend service of a backend service-based regional external passthrough Network Load Balancer or global external passthrough Network Load Balancer |  |  |   
`GCE_VM_IP` NEG  
on a backend service of a backend service-based regional external passthrough Network Load Balancer or global external passthrough Network Load Balancer |  |  |   
Target pool  
of a target pool-based regional external passthrough Network Load Balancer |  |  |   
  
#### `GCE_VM_IP_PORT` zonal NEG backends and network interfaces

When you create a new zonal NEG with `GCE_VM_IP_PORT` endpoints, you specify a zone, a default port, a VPC network, and a subnet in that network. None of these attributes can be changed after the zonal NEG has been created.

The NEG's subnet must be in the same region as the NEG's zone. If the NEG's network is an auto mode VPC network, you can omit specifying the NEG's subnet. When you don't specify a subnet, Google Cloud sets the NEG's subnet to the automatically created subnet in the region that contains the NEG's zone.

Zonal NEGs with `GCE_VM_IP_PORT` endpoints enforce the following rules for adding endpoints:

  * If you specify only an instance name for the endpoint, the instance must be in the same zone as the NEG and have a load balancer target interface in the NEG's subnet. The endpoint's IP address is set to the primary internal IPv4 address of the load balancer target interface, and the endpoint's port is set to the NEG's default port.

  * If you specify an instance name and an IP address, or an instance name, an IP address, and port information for the endpoint, the instance must be in the same zone as the NEG, and:

    * If you specify an IPv4 address: The IPv4 address must be a primary internal IPv4 address or IPv4 address from an alias IP range that's associated with a load balancer target interface in the NEG's subnet.

    * If you specify an IPv6 address: The IPv6 address must be a single IPv6 address from the `/96` IPv6 address range of the load balancer target interface in the NEG's subnet.

    * The endpoint's port is the port you specify. If you don't specify a port, the endpoint's port is set to the NEG's default port.




#### `GCE_VM_IP` zonal NEG backends and network interfaces

When you create a new zonal NEG with `GCE_VM_IP` endpoints, you specify a zone, a VPC network, and a subnet in that network. None of these attributes can be changed after the zonal NEG has been created.

The NEG's subnet must be in the same region as the NEG's zone. If the NEG's network is an auto mode VPC network, you can omit specifying the NEG's subnet. When you don't specify a subnet, Google Cloud sets the NEG's subnet to the automatically created subnet in the region that contains the NEG's zone.

Zonal NEGs with `GCE_VM_IP` endpoints enforce the following rules for adding endpoints:

  * If you specify only an instance name for the endpoint, the instance must be in the same zone as the NEG and have a load balancer target interface in the NEG's subnet.

  * If you specify both an instance name and an IP address for adding an endpoint, the instance must be in the same zone as the NEG, and the IP address must be the primary internal IPv4 address of a load balancer target interface in the NEG's subnet.




Since an instance can have only one NIC in the NEG's subnet, it can have only one `GCE_VM_IP` endpoint per zonal NEG, and the endpoint is always identified with the primary internal IPv4 address of the load balancer target interface. The actual destination IP addresses of load-balanced packets match a passthrough Network Load Balancer forwarding rule.

#### Instance group backends and network interfaces

The VPC network and subnet that are associated with an instance group are set implicitly by one of these actions:

  * For managed instance groups (MIGs), the instance group's VPC network and subnet are set to the network and subnet of the `nic0` vNIC defined in the instance template.

  * For unmanaged instance groups, the instance group's VPC network and subnet are set to the network and subnet of the `nic0` vNIC of the first instance that you add to the unmanaged instance group. You can't change the instance group's VPC network or subnet later, even if you remove the first instance that you added to the group.




Google Cloud enforces the following rules when adding instances to an unmanaged instance group after the instance group's VPC network and subnet have been set:

  * The `nic0` vNIC of an instance to be added to an instance group must match the instance group's network and subnet. This rule is enforced because the `nic0` vNIC is always a load balancer target interface.

  * For each load balancer target interface of an instance to be added to an instance group: If the load balancer target interface is attached to a VPC network to which load balancer target interfaces of existing instances are attached, both new and existing load balancer target interfaces must use the same subnet.




### Firewall rules

The set of firewall rules—from [hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies), [global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies), [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies), and [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls)—are unique to each network interface. Ensure that each network has appropriate firewall rules to allow the traffic that you want to allow to and from a multi-NIC instance. To determine which firewall rules apply to a network interface, and the source for each rule, see [Get effective firewall rules for a VM interface](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#get_effective_firewall_rules_for_a_vm_interface).

Firewall rules can be scoped to specific VM instances by using network tags or secure tags, both of which apply to all network interfaces of an instance. For more information, see [Comparison of secure tags and network tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#differences).

## Known issues

This section describes known issues related to using multiple network interfaces in Google Cloud.

### Creation errors and decreased performance when using Dynamic NICs with GPU instances

[Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dynamic-nics) aren't supported for use with GPU instances. If you create a GPU instance with Dynamic NICs, or add Dynamic NICs to an existing GPU instance, the following issues might occur:

  * The operation fails with an error such as the following:

`Internal error. Please try again or contact Google Support. (Code: 'CODE')`

  * The operation succeeds, but the instance experiences decreased performance, such as significantly lower [network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).




These issues occur because the Dynamic NIC configuration leads to errors when Compute Engine attempts to distribute the instance's vNICs across physical NICs on the host server.

### Dropped packets when using Dynamic NICs with alias IP ranges, protocol forwarding, or Passthrough Network Load Balancers

The guest agent automatically add local routes in the following scenarios for vNICs, but not for Dynamic NICs:

  * When you [configure an alias IP range](https://docs.cloud.google.com/vpc/docs/configure-alias-ip-ranges), the guest agent creates a local route for the alias IP range.
  * When you create a [target instance](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding#target-instances) that references a compute instance for protocol forwarding, the guest agent creates a local route for the associated forwarding rule IP address.
  * When you add a backend to a [Passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer), the guest agent creates a local route for the associated forwarding rule IP address.



Because the local routes aren't added for Dynamic NICs, the Dynamic NIC might experience dropped packets.

To resolve this issue, add the IP addresses manually as follows:

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) by using SSH.

  2. If you are configuring an alias IP range, do the following. Otherwise, you can skip this step.

     1. In `/etc/default/instance_configs.cfg`, ensure that the `ip_aliases` setting is set to `true`.
     2. If the ip_aliases setting is set to `false`, modify the file to change it to `true` and then restart the guest agent:
            
            systemctl restart google-guest-agent
            

  3. Configure a local route for the alias IP range or the forwarding rule IP address by using the following command:
         
         ip route add to local IP_ADDRESS dev DYNAMIC_NIC_DEVICE_NAME proto 66
         

Replace the following:

     * `IP_ADDRESS`: the alias IP range or forwarding rule IP address that you want to add a local route for.
     * `DYNAMIC_NIC_DEVICE_NAME`: the device name of the Dynamic NIC that you want to add a local route for. For example, `a-gcp.ens4.3`.



### Issues with installation and management of Dynamic NICs in guest agent versions 20250901.00 to 20251120.01

If you [configure automatic management of Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics#configure-guest-os-automatic) and your instance is running the guest agent at a version from 20250901.00 to 20251120.01, you might encounter the following issues:

  * The guest agent fails to install and manage Dynamic NICs in the guest OS of your instance.

You might receive an error that includes `Cannot find device` when running commands in the guest OS that reference Dynamic NICs.

  * Deleting multiple Dynamic NICs causes the [metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview) to become inaccessible.




#### Root cause

Starting with version [20250901.00](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#September_03_2025), the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) migrated to a new plugin-based architecture to improve modularity. The new architecture didn't initially support the automatic installation and management of Dynamic NICs.

#### Resolution

To resolve these issues, update your instance to use guest agent version 20251205.00 or later:

  1. To update the guest agent to the latest version, see [Update the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#update-guest).
  2. To confirm the guest agent version that your instance is running, see [View installed packages by operating system version](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#wgei_packages).



If necessary, you can temporarily work around these issues for instances that are running guest agent versions 20250901.00 to 20251120.01 by following the instructions in [Backward compatibility](https://docs.cloud.google.com/compute/docs/images/guest-agent#backward-compatibility) to revert to the previous guest agent architecture.

### Dynamic NIC operations fail when a compute instance is in multiple instance groups

If you add or delete a Dynamic NIC, and the operation gets stuck in a `RUNNING` state at 0% progress and eventually fails with an `INTERNAL_ERROR`, this might be because the compute instance is in multiple instance groups (managed or unmanaged).

To let the operation complete, remove the instance from all but one instance group. You can [remove an instance from a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances) or [remove an instance from an unmanaged instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances#removing_vms).

## What's next

  * [Create VMs with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
