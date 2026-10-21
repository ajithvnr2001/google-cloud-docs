---
url: https://docs.cloud.google.com/vpc/docs/advanced-vpc/
title: Advanced VPC concepts \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:52:46.670229+00:00
---

# Advanced VPC concepts  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/advanced-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Advanced VPC concepts

This page goes into additional detail about Virtual Private Cloud (VPC) networks. Before reading this page, see [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc). If you are interested in peered VPC networks, see [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).

## Low-level VPC networking details

This section provides some low-level VPC networking details. You do not need to read this for typical usage, but it provides more insight about how VPC networking works. The following diagram describes these low-level details, with more information in the corresponding sections.

[ ![The VPC network.](https://docs.cloud.google.com/static/vpc/images/detailednetworkingdiagram.svg)](https://docs.cloud.google.com/static/vpc/images/detailednetworkingdiagram.svg) The VPC network (click to enlarge).

### Who handles what

The different VPC networking features are handled by different parts of the system. Some of these are standard networking features that are well documented, and some of them are specific to VPC networks. Some features you can configure, and some you cannot. VPC networks use Linux's [VIRTIO network module](http://dl.acm.org/citation.cfm?id=1400097.1400108) to model Ethernet card and router functionality, but higher levels of the networking stack, such as ARP lookups, are handled using standard networking software.

ARP lookup
    The instance kernel issues [ARP requests](https://wikipedia.org/wiki/Address_Resolution_Protocol) and the VPC network issues ARP replies. The mapping between MAC addresses and IP addresses is handled by the instance kernel.
MAC lookup table, IP lookup table, active connection table
    These tables are hosted on the underlying VPC network and cannot be inspected or configured.
DNS server
    

Each instance's metadata server acts as a DNS server. It stores the DNS entries for all VPC network IP addresses in the local VPC network and calls Google's public DNS server for entries outside the VPC network. You cannot configure this DNS server. The DHCP client on each instance is configured to manage the instance's `/etc/resolv.conf` file.

    

You can add your own search domain or nameservers to the instance's `/etc/resolv.conf` by modifying the DHCP policy. Many Linux distributions allow these modifications to persist via [`/etc/dhcp/dhclient.conf`](https://www.isc.org/wp-content/uploads/2017/08/dhcp41clientconf.html). See the [Internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns) documentation for more information.

Packet handling between the VPC network and the outside
    

Packets coming into or out of the VPC network are handled by network code that examines the packet against firewall rules, against the external IP lookup table, and against the active connections table. The VPC network also performs NAT on packets coming into and out of the VPC network.

Packets received by an instance
    

These packets are received and turned into a stream by the instance kernel in the standard fashion.

Packets sent by an instance
    

Packets are sent by the instance kernel in the standard way. Interface and network functionality are modeled using the [VIRTIO network module](http://dl.acm.org/citation.cfm?id=1400097.1400108).

### Detailed connection walkthroughs

Here are more details about what happens when an instance makes a VPC network call.

**An instance makes a call:**

  1. If the target address is an instance name or a URL such as www.google.com, the instance calls the DNS service on its metadata server and gets back the matching IP address. You can configure your instance to consult another DNS service, but then you will not be able to resolve instance names.
  2. The destination IP address is examined against the subnet's IP address range, which every instance knows.

     1. If the IP address is not in the current VPC network or in a VPC network peered using VPC Network Peering:

        1. The instance sends the packet to the subnet's gateway MAC address with the destination set to the packet's final destination. The instance might need to make an ARP request to resolve the gateway's MAC address.

        2. The VPC network rewrites the IP header to declare the instance's external IP address as the source. If the instance has no external IP address, the call is not allowed, and the VPC network drops the packet without informing the sender.

        3. The VPC network records the outgoing packet and adds the source and destination to the active connections table.

        4. The VPC network sends the packet on to its destination.

        5. The destination gets the packet and responds if it chooses.

        6. The VPC network receives the response, consults the active connections table, notes that this is an active connection, and allows it. The VPC network consults its network/external IP lookup table and replaces the instance's external IP address with the matching network address and sends the packet to the source instance.

        7. The instance receives the packet.

     2. If the destination IP address is within the VPC network or in a VPC network peered using VPC Network Peering:

        1. The instance is configured with an IP with 255.255.255.255 mask, so the instance sends the packet to the subnet's gateway MAC address. The instance first might need to make an ARP request to resolve the gateway's MAC address.

        2. Google Cloud forwards the packet to the destination IP address within the current or peered VPC network.

        3. The target instance receives the packet. The target instance checks ingress firewall to determine if the packet is allowed. If not, the packet is dropped silently. Otherwise, the instance processes the packet.




**An external instance or computer calls an instance:**

  1. The external caller sends a packet to an instance's external IP address, which is owned by the VPC network.

  2. The VPC network compares the packet against the active connections table to see whether this is an existing connection:

     1. If it is not an existing connection, the VPC network looks for a firewall rule to allow the connection.
     2. If there is no firewall rule, the VPC network drops the packet without informing the sender.
  3. If there is an existing connection or valid firewall rule, the VPC network examines its lookup table and replaces the external IP with the corresponding internal IP in the packet, logs the incoming packet in the active connections table, and sends the packet to the target instance.

  4. The instance receives the packet and responds as described in **If the IP address is outside the VPC network IP range** when sending a packet outside the network range.

  5. The VPC network receives the reply, finds the matching incoming request in the active connections table, and allows the packet through. Before sending, it modifies the source IP address by replacing the instance's internal IP with the corresponding external IP from its lookup table.




## Measure VPC network throughput

For instructions, see [Calculate network throughput](https://github.com/GoogleCloudPlatform/community/blob/master/archived/network-throughput.md).

## What's next

  * To learn about VPC networks, see [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc).
  * To create, modify, and delete VPC networks, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
