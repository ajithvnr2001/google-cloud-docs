---
url: https://docs.cloud.google.com/nat/docs/about-private-nat-for-ncc/
title: Private NAT for NCC spokes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:38.428795+00:00
---

# Private NAT for NCC spokes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/about-private-nat-for-ncc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private NAT for NCC spokes

Private NAT lets you create a Cloud NAT gateway that works in conjunction with Network Connectivity Center spokes to perform network address translation (NAT) between the following networks:

  * Virtual Private Cloud (VPC) networks: in this configuration, the VPC networks that you want to connect must be attached to an NCC hub as VPC spokes.
  * VPC networks and networks outside of Google Cloud: in this configuration, the source VPC network must be attached to an NCC hub as a VPC spoke, and it must exchange rotes with an on-premises or another cloud provider network through a hybrid spoke.



The information on this page applies only to IPv4 traffic. For IPv6 traffic, see [NAT64 in Private NAT](https://docs.cloud.google.com/nat/docs/private-nat#nat64).

## Specifications

In addition to the [general Private NAT specifications](https://docs.cloud.google.com/nat/docs/private-nat#pvt-nat-specs), Private NAT for NCC spokes has the following specifications:

  * Private NAT uses a NAT configuration of `type=PRIVATE` to let networks with overlapping subnet IP address ranges communicate. However, only non-overlapping subnets can connect to each other.
  * You need to create a custom NAT rule by referencing a NCC hub. The NAT rule specifies a NAT IP address range from a subnet of purpose `PRIVATE_NAT` that Private NAT uses to perform NAT on traffic between your connected networks.
  * When you create a VM instance in a subnet range where the Private NAT applies, all egress traffic from this virtual machine (VM) instance is translated by the gateway if the destination spoke is in the same NCC hub as the gateway. Private NAT translates traffic to destination spokes within the same region as the Private NAT gateway as well as across regions.
  * A Private NAT gateway is associated with subnet IP address ranges in a single region in a single VPC network. This means a Private NAT gateway created in one VPC network doesn't provide NAT services to VMs in other spokes of the NCC hub, even if the VMs are in the same region as the gateway.



### Traffic between VPC networks

The following additional specifications apply for traffic between VPC networks (Inter-VPC NAT):

  * To enable Inter-VPC NAT between two VPC networks, each VPC network must be configured as a VPC spoke of a NCC hub. You must ensure that there are no overlapping IP address ranges across your VPC spokes. For more information, see [Create a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke).
  * The NCC hub associated with the Private NAT gateway must have at least two VPC spokes, where one of the VPC spokes is the VPC network of the Private NAT gateway.
  * Inter-VPC NAT supports NAT between NCC VPC spokes only, and not between VPC networks connected using VPC Network Peering.



### Traffic between VPC networks and other networks

The following additional specifications apply for traffic between VPC networks and networks outside of Google Cloud:

  * The source VPC network must be configured as a VPC spoke of a NCC hub.
  * A hybrid spoke must be attached to the same NCC hub to establish connectivity between the VPC spoke and the destination network outside of Google Cloud. For more information, see [Establishing connectivity between hybrid spokes and VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes#connectivity-between-hybrid-and-vpc-spokes).



For information about the requirements for using VPC spokes and hybrid spokes in the same NCC hub, see [Route exchange with VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes).

## Basic configuration and workflow

The following diagram shows a basic Private NAT configuration for traffic between two VPC spokes:

[ ![Inter-VPC NAT translation example.](https://docs.cloud.google.com/static/nat/images/inter-vpc-nat-flow.png)](https://docs.cloud.google.com/static/nat/images/inter-vpc-nat-flow.png) Inter-VPC NAT translation example (click to enlarge).

In this example, Private NAT is set up as follows:

  * The `pvt-nat-gw` gateway is configured in `vpc-a` to apply to all the IP address ranges of `subnet-a` in the `us-east1` region. Using the NAT IP ranges of `pvt-nat-gw`, a virtual machine (VM) instance in `subnet-a` of `vpc-a` can send traffic to a VM in `subnet-b` of `vpc-b`, even though `subnet-a` of `vpc-a` overlaps with `subnet-c` of `vpc-b`.
  * Both `vpc-a` and `vpc-b` are configured as spokes of a NCC hub.
  * The `pvt-nat-gw` gateway is configured to provide NAT between VPC networks that are configured as VPC spokes in the same NCC hub.



### Example workflow

In the preceding diagram, `vm-a` with the internal IP address `192.168.1.2` in `subnet-a` of `vpc-a` needs to download an update from `vm-b` with the internal IP address `192.168.2.2` in `subnet-b` of `vpc-b`. Both the VPC networks are connected to the same NCC hub as VPC spokes. Assume that `vpc-b` contains another subnet `192.168.1.0/24` that overlaps with the subnet in `vpc-a`. For `subnet-a` of `vpc-a` to communicate with `subnet-b` of `vpc-b`, you need to configure a Private NAT gateway, `pvt-nat-gw`, in `vpc-a` as follows:

  * Private NAT subnet: before configuring the Private NAT gateway, create a Private NAT subnet of purpose `PRIVATE_NAT`, for example, `10.1.2.0/29`. Ensure that this subnet doesn't overlap with an existing subnet in any of the VPC spokes attached to the same NCC hub.

  * A NAT rule whose `nexthop.hub` matches the NCC hub URL.

  * NAT for all address ranges of `subnet-a`.




The following table summarizes the network configuration specified in the preceding example:

Network name | Network component | IP address/range | Region  
---|---|---|---  
vpc-a | subnet-a | `192.168.1.0/24` | us-east1  
vm-a | `192.168.1.2`  
pvt-nat-gw | `10.1.2.0/29`  
vpc-b | subnet-b | `192.168.2.0/24` | us-west1  
vm-b | `192.168.2.2`  
subnet-c | `192.168.1.0/24`  
vm-c | `192.168.1.3`  
  
Private NAT for NCC spokes follows the [port reservation procedure](https://docs.cloud.google.com/nat/docs/ports-and-addresses#port-reservation-procedure) to reserve the following NAT source IP address and source port tuples for each of the VMs in the network. For example, the Private NAT gateway reserves 64 source ports for `vm-a`: `10.1.2.2:34000` through `10.1.2.2:34063`.

When the VM uses the TCP protocol to send a packet to the update server `192.168.2.2` on destination port `80`, the following occurs:

  1. The VM sends a request packet with these attributes:

     * Source IP address: `192.168.1.2`, the internal IP address of the VM
     * Source port: `24000`, the ephemeral source port chosen by the VM's operating system
     * Destination address: `192.168.2.2`, the update server's IP address
     * Destination port: `80`, the destination port for HTTP traffic to the update server
     * Protocol: TCP
  2. The `pvt-nat-gw` gateway performs source network address translation (SNAT or source NAT) for egress traffic, rewriting the request packet's NAT source IP address and source port:

     * NAT source IP address: `10.1.2.2`, from one of the VM's reserved NAT source IP address and source port tuples
     * Source port: `34022`, an unused source port from one of the VM's reserved source port tuples
     * Destination address: `192.168.2.2`, unchanged
     * Destination port: `80`, unchanged
     * Protocol: TCP, unchanged
  3. The update server sends a response packet that arrives on the `pvt-nat-gw` gateway with these attributes:

     * Source IP address: `192.168.2.2`, the update server's internal IP address
     * Source port: `80`, the HTTP response from the update server
     * Destination address: `10.1.2.2`, which matches the original NAT source IP address of the request packet
     * Destination port: `34022`, which matches the source port of the request packet
     * Protocol: TCP, unchanged
  4. The `pvt-nat-gw` gateway performs destination network address translation (DNAT) on the response packet, rewriting the response packet's destination address and destination port so that the packet is delivered to the VM that requested the update with the following attributes:

     * Source IP address: `192.168.2.2`, unchanged
     * Source port: `80`, unchanged
     * Destination address: `192.168.1.2`, the internal IP address of the VM
     * Destination port: `24000`, matching the original ephemeral source port of the request packet
     * Protocol: TCP, unchanged



## What's next

  * [Set up and manage network address translation with Private NAT](https://docs.cloud.google.com/nat/docs/set-up-private-nat)
  * Learn about [Cloud NAT product interactions](https://docs.cloud.google.com/nat/docs/nat-product-interactions)
  * Learn about [IP addresses and ports](https://docs.cloud.google.com/nat/docs/ports-and-addresses)
  * Learn about [Cloud NAT rules](https://docs.cloud.google.com/nat/docs/nat-rules-overview)
  * [Troubleshoot configuration](https://docs.cloud.google.com/nat/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
