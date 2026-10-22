---
url: https://docs.cloud.google.com/nat/docs/about-hybrid-nat/
title: Hybrid NAT \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:41.135686+00:00
---

# Hybrid NAT  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/about-hybrid-nat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Hybrid NAT

Hybrid NAT enables network address translation (NAT) between a Virtual Private Cloud (VPC) network and destinations in an on-premises or another cloud provider network. The networks must be connected by using Google Cloud Network Connectivity products such as [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect) or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-vpn).

The information on this page applies only to IPv4 traffic. For IPv6 traffic, see [NAT64 in Private NAT](https://docs.cloud.google.com/nat/docs/private-nat#nat64).

## Specifications

In addition to the [general Private NAT specifications](https://docs.cloud.google.com/nat/docs/private-nat#pvt-nat-specs), Hybrid NAT has the following specifications:

  * Hybrid NAT lets a VPC network communicate with an on-premises network or other cloud provider network even if the subnet IP address ranges of the networks overlap. By using a NAT configuration of `type=PRIVATE`, resources in both the overlapping and non-overlapping subnets of the VPC network can connect to resources in the non-overlapping subnets of the non-Google Cloud network.
  * To enable Hybrid NAT, the non-Google Cloud network must advertise its dynamic routes so that your VPC network can learn and use them. Your Cloud Router learns these dynamic routes from Google Cloud's Network Connectivity products such as Cloud Interconnect, HA VPN, or Classic VPN with dynamic routing configured. The destinations of these dynamic routes are IP address ranges outside of your VPC network.

**Note:** Only the non-overlapping subnet routes need to be advertised; overlapping subnet routes must not be advertised.

Similarly, for return traffic, your VPC network must [advertise](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am) the Private NAT subnet route by using a Cloud Router, and this subnet route must not overlap with an existing subnet in the connected networks.

  * Hybrid NAT performs NAT on traffic originating from a VPC network to an on-premises network or other cloud provider network. The networks must be connected by Cloud Interconnect or Cloud VPN.

  * Hybrid NAT supports existing Classic VPN tunnels only if dynamic routing is enabled.

  * You need to create a custom NAT rule with a match expression `nexthop.is_hybrid`. The NAT rule specifies a NAT IP address range from a subnet of purpose `PRIVATE_NAT` that the resources in your VPC network can use to communicate with other networks.

  * The Cloud Router on which you configure Hybrid NAT must be in the same region as the VPC network.

  * Hybrid NAT doesn't translate traffic for [Hybrid Subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets). For more information, see [Hybrid Subnets interactions](https://docs.cloud.google.com/nat/docs/nat-product-interactions#hybrid).




## Basic Hybrid NAT configuration and workflow

The following diagram shows a basic Hybrid NAT configuration:

[ ![Hybrid NAT translation example.](https://docs.cloud.google.com/static/nat/images/hybrid-nat.svg)](https://docs.cloud.google.com/static/nat/images/hybrid-nat.svg) Hybrid NAT translation example (click to enlarge).

In this example, Hybrid NAT is set up as follows:

  * The `pvt-nat-gw` gateway is configured in `vpc-a` to apply to all the IP address ranges of `subnet-a` in the `us-east1` region.
  * Cloud Router and the on-premises or other cloud provider router exchange the following subnet routes: 
    * Cloud Router advertises `10.1.2.0/29` to the external router.
    * The external router advertises `192.168.2.0/24` to Cloud Router.
  * By using the NAT IP address range of `pvt-nat-gw`, a virtual machine (VM) instance in `subnet-a` of `vpc-a` can send traffic to a VM in `subnet-b` of the on-premises network or other cloud provider network, even though `subnet-a` of `vpc-a` overlaps with another subnet in the non-Google Cloud network.



### Example Hybrid NAT workflow

In the preceding diagram, `vm-a` with the internal IP address `192.168.1.2` in `subnet-a` of `vpc-a` needs to download an update from `vm-b` with the internal IP address `192.168.2.2` in `subnet-b` of an on-premises network or other cloud provider network. Cloud Interconnect connects your VPC network to the on-premises network or other cloud provider network. Assume that the non-Google Cloud network contains another subnet `192.168.1.0/24` that overlaps with the subnet in `vpc-a`. For `subnet-a` of `vpc-a` to communicate with `subnet-b` of the non-Google Cloud network, you need to configure a Private NAT gateway, `pvt-nat-gw`, in `vpc-a` as follows:

  * Specify a Private NAT subnet of purpose `PRIVATE_NAT`, for example, `10.1.2.0/29`. Create this subnet before configuring the Private NAT gateway. Ensure that this subnet doesn't overlap with an existing subnet in any of the connected networks.
  * Create a NAT rule with `match='nexthop.is_hybrid'`.
  * Configure the Private NAT gateway to apply to all IP address ranges of `subnet-a`.



Hybrid NAT follows the [port reservation procedure](https://docs.cloud.google.com/nat/docs/ports-and-addresses#port-reservation-procedure) to reserve the following NAT source IP address and source port tuples for each of the VMs in the network. For example, the Private NAT gateway reserves 64 source ports for `vm-a`: `10.1.2.2:34000` through `10.1.2.2:34063`.

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
  4. The `pvt-nat-gw` gateway performs destination network address translation (DNAT) on the response packet, and rewrites the response packet's destination address and destination port so that the packet is delivered to the VM that requested the update with the following attributes:

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
