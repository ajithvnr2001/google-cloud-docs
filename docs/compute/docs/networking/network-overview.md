---
url: https://docs.cloud.google.com/compute/docs/networking/network-overview/
title: Networking overview for VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:57.937955+00:00
---

# Networking overview for VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/network-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Networking overview for VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the networking functionality of your virtual machine (VM) instances. It provides a basic foundational understanding of how your virtual machine (VM) instances interact with Virtual Private Cloud (VPC) networks. For more information about VPC networks and related features, read the [VPC network overview](https://docs.cloud.google.com/vpc/docs/vpc).

## Networks and subnets

Every VM is part of a VPC network. VPC networks provide connectivity for your VM instance to other Google Cloud products and to the internet. VPC networks can be [auto mode or custom mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges).

  * [Auto mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#auto-mode-considerations) have one subnetwork (subnet) in each region. All subnets are contained within this IP address range: `10.128.0.0/9`. Auto mode VPC networks support only IPv4 subnet ranges.
  * Custom mode networks don't have a specified subnet configuration; you decide which subnets to create in regions that you choose by using [IP ranges that you specify](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). Custom mode networks also support IPv6 subnet ranges.



Unless you choose to disable it, each project has a `default` network, which is an auto mode VPC network. You can disable the creation of default networks by [creating an organization policy](https://docs.cloud.google.com/vpc/docs/vpc#org-policies).

Each subnet in a VPC network is associated with a region and contains one or more IP address ranges. You can create more than one subnet per region. Each of the network interfaces for your VM must be connected to a subnet.

When you create a VM, you can specify a VPC network and subnet. If you omit this configuration, the `default` network and subnet are used. Google Cloud assigns an internal IPv4 address to the new VM from the primary IPv4 address range of the selected subnet. If the subnet also has an IPv6 address range (referred to as _dual-stack_), or if you created an IPv6-only subnet, you can assign an IPv6 address to the VM.

For more information on VPC networks, read the [VPC network overview](https://docs.cloud.google.com/vpc/docs/vpc). For an illustrated example of VMs using a VPC network with three subnets in two regions, see [VPC network example](https://docs.cloud.google.com/vpc/docs/vpc#network_example).

## Network interface controllers (NICs)

Every compute instance in a VPC network has a default virtual network interface (vNIC). When you configure a vNIC, you select a VPC network and a subnet within that VPC network to connect the interface to. You can create additional network interfaces for your instances.

Multiple network interfaces enable you to create configurations in which an instance connects directly to several VPC networks. Multiple network interfaces are useful when applications running in an instance require traffic separation, such as separation of data plane traffic from management plane traffic. For more information about using multiple network interfaces, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

Multiple vNICs aren't supported with bare metal instances. Additionally, you can only add vNICs to an instance during instance creation. With [Dynamic Network Interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dynamic-nics), you can create VLAN-based network subinterfaces for each exposed vNIC, which lets you scale the number of network interfaces and VPC network connections. You can add or remove Dynamic Network Interfaces without having to restart or recreate the compute instance. For more information about Dynamic NIC, see [Create VMs with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces).

When you configure the vNIC for a compute instance, you can specify the type of network driver to use with the interface.

  * For [first and second generation machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology), the default is [VirtIO](https://ozlabs.org/%7Erusty/virtio-spec/virtio-0.9.5.pdf).
  * Third generation and newer machine series are configured to use [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) by default and don't support VirtIO for the network interface.
  * Bare metal instances use [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf).
  * With supported machine series, such as H4D and Z4M, compute instances can optionally use [Cloud RDMA (IRDMA)](https://docs.cloud.google.com/compute/docs/networking/using-irdma). The remote data memory access (RDMA) network driver enables low-latency, reliable messaging capabilities for Compute Engine instances. Cloud RDMA transfers data between remote machines and local memory through the network interface without using host CPU or intermediate host buffers.



Additionally, you can choose to use per VM Tier_1 networking performance with a compute instance that uses gVNIC or IPDF. Tier_1 networking enables higher network throughput limits for both inbound and outbound data transfers.

## Network bandwidth

Google Cloud accounts for bandwidth per VM instance, not per network interface (NIC) or IP address. Bandwidth is measured using two dimensions: traffic direction (ingress and egress) and type of destination IP address. The maximum possible egress rate is determined by the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#predefined-types) that was used to create the instance; however, you can only achieve that maximum possible egress rate in specific situations. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

To support higher network bandwidths—such as 200 Gbps for third generation and later machine series—Google Virtual NIC (gVNIC) is required.

  * Standard maximum egress bandwidth limits range from 1 Gbps to 100 Gbps.
  * The [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) increases the maximum egress bandwidth limit to 200 Gbps, depending on the size and machine type of your compute instance.



Some machine series have different limits, as documented in the [Bandwidth summary table](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table).

If using both gVNIC and IRDMA network interfaces for an instance, the network bandwidth limit for the instance is shared between the two network communication methods. Cloud RDMA traffic has priority over gVNIC traffic.

## IP addresses

Each VM is assigned an IP address from the subnet associated with the network interface. The following list provides additional information about the requirements for configuring IP addresses.

  * For IPv4-only subnets, the IP address is an internal IPv4 address. You can optionally configure an external IPv4 address for the VM.
  * If the network interface connects to a dual-stack subnet that has an IPv6 range, you must use a custom mode VPC network. The VM has the following IP addresses: 
    * An internal IPv4 address. You can optionally configure an external IPv4 address for the VM.
    * Either an internal or external IPv6 address, depending on the access type of the subnet.
  * For IPv6-only subnets, you must use a custom mode VPC network. The VM has either an internal or external IPv6 address, depending on the access type of the subnet.
  * To create an IPv6-only instance with both an internal and external IPv6 address, you must specify two network interfaces when creating the VM. You can't add network interfaces to an existing instance.



Both external and internal IP addresses can be either [ephemeral or static](https://docs.cloud.google.com/vpc/docs/ip-addresses#ephemeral_and_static_ip_addresses).

Internal IP addresses are local to one of the following:

  * A VPC network
  * A VPC network connected using VPC Network Peering
  * An on-premises network connected to a VPC network using Cloud VPN, Cloud Interconnect, or a Router appliance



An instance can communicate with instances on the same VPC network, or a connected network as specified in the preceding list, using the VM's internal IPv4 address. If the VM network interface connects to a dual-stack subnet or to an IPv6-only subnet, you can use either the VM's internal or external IPv6 addresses to communicate with other instances on the same network. As a best practice, use internal IPv6 addresses for internal communication. For more information about IP addresses, read the [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses) overview for Compute Engine.

To communicate with the internet or external systems, use an external IPv4 or external IPv6 address configured on the VM instance. External IP addresses are publicly routable IP addresses. If an instance doesn't have an external IP address, [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) can be used for IPv4 traffic.

If you have multiple services running on a single VM instance, you can give each service a different internal IPv4 address by using alias IP ranges. The VPC network forwards packets that are destined to a particular service to the corresponding VM. For more information, see [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip).

## Network Service Tiers

[Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview) lets you optimize connectivity between systems on the internet and your Compute Engine instances. Premium Tier delivers traffic on Google's premium backbone, while Standard Tier uses regular ISP networks. Use Premium Tier to optimize for performance, and use Standard Tier to optimize for cost.

Because you choose a network tier at the resource level—such as the external IP address for a VM—you can use Standard Tier for some resources and Premium Tier for others. If you don't specify a tier, Premium Tier is used.

Compute instances that use internal IP addresses to communicate within VPC networks always use the Premium Tier networking infrastructure.

When using either Premium Tier or Standard Tier, there is no charge for inbound data transfer. Outbound data transfer pricing is per GiB delivered, and is different for each of the Network Service Tiers. For information about pricing, see [Network Service Tiers pricing](https://cloud.google.com/network-tiers/pricing).

Network Service Tiers aren't the same as per VM Tier_1 networking performance, which is a configuration option you can choose to use with your compute instances. There is an extra cost associated with using Tier_1 networking, as described in [Tier_1 higher bandwidth network pricing](https://cloud.google.com/products/compute/pricing/general-purpose#tier-1-higher-bandwidth-network-pricing). For more information about Tier_1 networking, see [Configure per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

### Premium tier

Premium Tier delivers traffic from external systems to Google Cloud resources by using Google's low latency, highly reliable global network. This network is designed to tolerate multiple failures and disruptions while still delivering traffic. Premium Tier is ideal for customers with users in multiple locations worldwide who need the best network performance and reliability.

The Premium Tier network consists of an extensive private fiber network with over 100 [points of presence (PoPs)](https://docs.cloud.google.com/docs/geography-and-regions#points_of_presence_pops) around the globe. Within [Google's network](https://cloud.google.com/about/locations#network), traffic is routed from that PoP to the compute instance in your VPC network. Outbound traffic is sent through Google's network, exiting at the PoP that is closest to its destination. This routing method minimizes congestion and maximizes performance by reducing the number of hops between end users and the PoPs that are closest to them.

### Standard tier

The Standard Tier network delivers traffic from external systems to Google Cloud resources by routing it over the internet. Packets that leave Google's network are delivered using the public internet and are subject to the reliability of intervening transit providers and ISPs. Standard Tier provides network quality and reliability comparable to that of other cloud providers.

Standard Tier is priced lower than Premium Tier because traffic from systems on the internet is routed over transit (ISP) networks before being sent to compute instances in your VPC network. Standard Tier outbound traffic normally exits Google's network from the same region used by the sending compute instance, regardless of its destination.

Standard Tier includes 200 GB of free usage per month in each region that you use across all of your projects, on a per resource basis.

## Internal Domain Name System (DNS) names

When you create a virtual machine (VM) instance, Google Cloud [creates an internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns) from the VM name. Unless you specify a [custom hostname](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm), Google Cloud uses the automatically created internal DNS name as the hostname it provides to the VM.

For communication between VMs in the same VPC network, you can specify the fully qualified DNS name (FQDN) of the target instance instead of using its internal IP address. Google Cloud automatically resolves the FQDN to the internal IP address of the instance.

For more information about fully qualified domain names (FQDN), see [Zonal and global internal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names).

## Routes

Google Cloud _routes_ define the paths that network traffic takes from a virtual machine (VM) instance to other destinations. These destinations can be inside your VPC network (for example, in another VM) or outside it. The [routing table](https://wikipedia.org/wiki/Routing_table) for a VPC network is defined at the VPC network level. Each VM instance has a controller that is kept informed of all [applicable routes](https://docs.cloud.google.com/vpc/docs/routes#applicable_routes) from the network's routing table. Each packet leaving a VM is delivered to the appropriate next hop of an applicable route based on a routing order.

Subnet routes define paths to resources like VMs and internal load balancers in a VPC network. Each subnet has at least one subnet route whose destination matches the primary IP range of the subnet. Subnet routes always have the most specific destinations. They cannot be overridden by other routes, even if another route has a higher priority. This is because Google Cloud considers destination specificity before priority when selecting a route. For more information about subnet IP ranges, see the [subnets overview](https://docs.cloud.google.com/vpc/docs/subnets).

## Forwarding rules

While routes govern traffic leaving an instance, forwarding rules direct traffic to a Google Cloud resource in a VPC network based on IP address, protocol, and port. Some forwarding rules direct traffic from outside of Google Cloud to a destination in the network; other rules direct traffic from inside the network.

You can configure forwarding rules for your instances to implement virtual hosting by IPs, Cloud VPN, private virtual IPs (VIPs), and load balancing. For more information about forwarding rules, see [Using protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding).

## Firewall rules

VPC firewall rules let you allow or deny connections to or from your VM based on a configuration that you specify. Google Cloud always enforces enabled VPC firewall rules, protecting your VMs regardless of their configuration and operating system, even if the VM has not started.

By default, every VPC network has incoming (ingress) and outgoing (egress) [firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls#firewall-rules-in-google-cloud) that block all incoming connections and allow all outgoing connections. The `default` network has [additional firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls#more_rules_default_vpc), including the `default-allow-internal` rule, which permits communication among instances in the network. If you are not using the `default` network, you must explicitly create higher priority [ingress firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#rules-for-common-use-cases) to allow instances to communicate with one another.

Every VPC network functions as a distributed firewall. Firewall rules are defined at the VPC level, and can apply to all instances in the network, or you can use target tags or target service accounts to apply rules to specific instances. You can think of the VPC firewall rules as existing not only between your instances and other networks, but also between individual instances within the same VPC network.

[Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies) let you create and enforce a consistent firewall policy across your organization. You can assign Hierarchical firewall policies to the organization as a whole or to individual folders. These policies contain rules that can explicitly deny or allow connections, the same as VPC firewall rules. In addition, hierarchical firewall policy rules can delegate evaluation to lower-level policies or VPC firewall rules with a `goto_next` action. Lower-level rules can't override a rule from a higher place in the resource hierarchy. This lets organization-wide administrators manage critical firewall rules in one place.

## Accelerator-optimized machines and networking configurations

If you use accelerator-optimized machine types (GPUs or TPUs), see the following pages:

  * For information about networking for GPUs, see [Networking and GPU machines](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth).

  * For information about networking for TPUs, see [Configure networking and access to your TPU](https://docs.cloud.google.com/tpu/docs/configure-networking-access-compute) in the Cloud TPU documentation.




## Managed instance groups and networking configurations

If you use [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances), the network configuration you specify on the instance template applies across all VMs created with the template. If you create an instance template in an auto mode VPC network, Google Cloud automatically selects the subnet for the region where you created the managed instance group.

For more information, see [Networks and subnets](https://docs.cloud.google.com/vpc/docs/subnets#vpc_networks_and_subnets) and [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## What's next

  * Learn how to [create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).
  * Learn how to [create and manage routes](https://docs.cloud.google.com/vpc/docs/using-routes) for VPC networks.
  * Learn how to [create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  * Learn how to [create a managed instance group (MIG) ](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).
  * Learn how to scale your VMs and [optimize application latency with load balancing](https://docs.cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency).
  * Learn how to [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) to Google Cloud.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
