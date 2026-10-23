---
url: https://docs.cloud.google.com/vpc/docs/mtu/
title: Maximum transmission unit \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:14.636982+00:00
---

# Maximum transmission unit  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/mtu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Maximum transmission unit

The [maximum transmission unit (MTU)](https://www.wikipedia.org/wiki/Maximum_transmission_unit) is the size, in bytes, of the largest possible IP packet, including IP headers, Layer 4 protocol headers, and Layer 4 data, that can fit inside an Ethernet frame.

## Valid VPC network MTU sizes

Virtual Private Cloud (VPC) networks use a default MTU of 1,460 bytes. You can set a VPC network's MTU to any value between 1,300 bytes and 8,896 bytes (inclusive). Common custom MTU sizes are 1,500 bytes (standard Ethernet) or 8,896 bytes (the maximum possible). We recommend that you configure the MTU for each Compute Engine instance network interface (NIC) to match the MTU of the VPC network to which it is connected. For more information, see Compute instances and MTU settings.

**Note:** If you create a VPC network with a network profile provided by Google Cloud for a specific use case, the default MTU might be different. For more information, see the documentation for the specific [network profile](https://docs.cloud.google.com/vpc/docs/network-profiles).

### Communication between compute instances within VPC networks

IP packets up to the MTU size can be sent between two compute instances, if the following apply:

  * Both the sending and receiving instances use the same VPC network, or [peered VPC networks](https://docs.cloud.google.com/vpc/docs/vpc-peering) that have identical MTUs.
  * The interfaces for both instances are configured to use the VPC network MTU.



To avoid MTU mismatch issues, we recommend that you use the same MTU for all of your connected VPC networks. Although that is the recommended practice, you are not forced to configure identical MTUs on connected VPC networks. For details about how protocols handle situations where there is a MTU mismatch between VPC networks, see Mismatched MTUs, MSS clamping, path MTU discovery.

From the perspective of a sending instance, paths to the following destinations represent instance-to-instance traffic routed within a VPC network:

  * A regional internal IPv4 address in a [subnet primary IPv4 or subnet secondary IPv4 address range](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges), including private IPv4 address ranges and privately used public IPv4 address ranges, used by these destination resources: 
    * The primary internal IPv4 address of a receiving instance's network interface (NIC).
    * An internal IPv4 address in an alias IP range of a receiving instance's NIC.
    * An internal IPv4 address of an internal forwarding rule for either protocol forwarding or for an internal passthrough Network Load Balancer.
  * [Internal IPv6 subnet address ranges](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6) used by these destination resources: 
    * An IPv6 address from the `/96` IPv6 address range assigned to a receiving instance's NIC.
    * An IPv6 address from the `/96` IPv6 address range of an internal forwarding rule for either protocol forwarding or for an internal passthrough Network Load Balancer.
  * [External IPv6 subnet address ranges](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6) used by these destination resources _when packets are routed using subnet routes or peering subnet routes within the VPC network_ : 
    * An IPv6 address from the `/96` IPv6 address range assigned to a receiving instance's NIC.
    * An IPv6 address from the `/96` IPv6 address range of an external forwarding rule for either protocol forwarding or for a regional external passthrough Network Load Balancer.



The following instance-to-instance paths are treated in the same way as Communication to destinations outside of a VPC network:

  * If the packet destination is an external IPv4 address of a receiving instance's NIC.
  * If the packet destination is an external IPv4 address of a [regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network).
  * If the packet destination is an external IPv4 address of a [forwarding rule for protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding)
  * If the packet destination is an external IPv6 address of an instance's NIC, regional external passthrough Network Load Balancer, or forwarding rule for external protocol forwarding _and_ the applicable route in the VPC network uses a default internet gateway next hop. In this scenario, receiving instances are neither in the same VPC network as the sending instance nor in a VPC network connected to the sending instance's VPC network using VPC Network Peering.



### Communication to destinations outside of a VPC network

Google Cloud processes packets sent from compute instances to destinations outside of the sending instance's VPC network as shown in the following table. Destinations outside of a sending instance's VPC network include publicly routable IP addresses for resources outside of Google Cloud and [customer-usable external IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses#external) within Google Cloud.

**Important:** If a destination IPv6 address for a compute instance NIC or forwarding rule for a regional external passthrough Network Load Balancer or external protocol forwarding is in the sending instance's own VPC network or a peered VPC, see Communication between compute instances within VPC networks instead.

Because the internet generally uses an MTU of 1,500 bytes, keeping IP packet size at 1,500 bytes or less usually avoids MTU-related packet loss.

Situation | Behavior  
---|---  
TCP SYN and SYN-ACK packets | Google Cloud performs MSS clamping if necessary, changing the MSS to ensure packets fits within the MTU.  
IP packet MTU between 1,300 bytes and 1,600 bytes (inclusive) | Google Cloud makes no changes to the packet, except for SYN and SYN-ACK packets as discussed in the first row.  
IP packet larger than 1,600 bytes | Google Cloud drops the packet and sends a Fragmentation Needed (ICMP over IPv4) or Packet Too Big (ICMPv6) message both when the DF bit is on and also when the DF bit is off.   
  
### Communication to Google APIs and services

Compute instances using any valid VPC network MTU size can send packets to Google APIs and services, including using [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) and [Private Service Connect for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis). The details in this section also apply to on-premises resources that send packets to Google APIs and services using [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

The traffic path to Google APIs and services described in this section is implemented by Google Front Ends (GFEs). These GFEs use non-configurable, fixed MTUs. Traffic from Google Cloud to Google APIs and services always uses the TCP protocol: If a compute instance connects to Google APIs and services from a VPC network whose MTU doesn't match the MTU of the GFE, the segment size is negotiated by using TCP MSS advertisement as described in Mismatched MTUs, MSS clamping, path MTU discovery.

Packet source | Packet destination  
---|---  
Any internal IPv4 address: primary internal IPv4 address or internal IPv4 address from an alias IP range of the instance NIC An external IPv4 address assigned to the instance NIC using a 1-1 NAT access config: In this situation, Google Cloud performs 1-1 NAT on egress, converting an original source primary internal IPv4 address to a source external IPv4 address specified in the access config. | 

  * Google APIs and services IPv4 addresses for the [ default domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults)
  * `199.36.153.4/30` (restricted.googleapis.com)
  * `199.36.153.8/30` (private.googleapis.com)
  * Private Service Connect endpoint for Google APIs and services

  
External or internal IPv6 address, for dual-stack or IPv6-only instances | 

  * Google APIs and services IPv6 addresses for the [ default domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults)
  * `2600:2d00:0002:1000::/56` (restricted.googleapis.com)
  * `2600:2d00:0002:2000::/56` (private.googleapis.com)

  
  
### Communication through Cloud VPN tunnels

Cloud VPN has both a _gateway MTU_ for encapsulated packets and a _payload MTU_ for packets before and after encapsulation.

For precise payload MTU values and other Cloud VPN MTU information, see [MTU considerations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations) in the Cloud VPN documentation.

### Communication through Cloud Interconnect (VLAN) attachments

We recommend that you use the same MTU for all VLAN attachments that are connected to the same VPC network, _and_ that you set the MTU of the VPC network to the same value. For details about Cloud Interconnect VLAN attachment MTUs, see [Cloud Interconnect MTU](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#interconnect-mtu).

### Communication through firewall endpoints

If you use [firewall endpoints](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints), configure an appropriate MTU for your VPC network. If the MTU setting of your VPC network exceeds the packet size that your firewall endpoint supports, Cloud Next Generation Firewall can't perform Layer 7 inspection successfully. For more information, see [Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size).

## Jumbo frame support

[Jumbo frames](https://en.wikipedia.org/wiki/Jumbo_frame) have a payload more than 1,460 bytes in size. The following table summarizes jumbo frame support for Google Cloud products and features:

Product or feature | Jumbo frame support  
---|---  
Compute Engine | Yes  
Cloud Interconnect | Yes  
Firewall endpoints | Yes  
Cloud VPN | No  
Google APIs | No  
  
## Compute instances and MTU settings

As a best practice, match a compute instance NIC's MTU to the MTU of the VPC network that the NIC is connected to. The NIC MTU configuration varies depending on the operating system and configuration:

  * **Linux instances based on a[public OS image](https://docs.cloud.google.com/compute/docs/images/os-details)**: each NIC MTU is automatically set to the respective VPC network MTU by using DHCP Option 26.

  * **Windows instances based on a[public OS image](https://docs.cloud.google.com/compute/docs/images/os-details)**: by default, each NIC MTU is configured with a fixed MTU of `1,460` bytes. If you change the MTU of a VPC network that contains Windows instances based on public OS images, you must [change the MTU setting of the Windows instances](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network#change-mtu-windows).

  * **Custom guest OS images** : you must configure NIC MTUs or verify that the guest OS accepts the VPC network MTU by using DHCP Option 26.

  * **Instances with[multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts)**: set each NIC MTU to the respective VPC network MTU.




If a NIC MTU must differ from the VPC network MTU, set the NIC MTU to a value that's _less than_ the VPC network MTU. Forcibly decreasing the NIC MTU is advantageous for some advanced networking scenarios.

### Changing the MTU of a VPC network

To avoid connectivity issues, before you change the VPC network MTU, you _must_ first [stop each compute instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance). Rebooting an instance from within its guest operating system _doesn't_ update its MTU. If you choose to configure instances with a lower MTU than the network MTU, the requirement to stop the instance before changing the MTU still applies.

For more information about changing the network MTU, see [Change the MTU setting of a VPC network](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network).

## GKE and MTU settings

The MTU selected for a Pod interface is dependent on the Container Network Interface (CNI) used by the cluster Nodes and the underlying VPC MTU setting. For more information, see [Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#pods).

Autopilot is configured to always inherit the VPC MTU. 

The Pod interface MTU value is either `1460` or inherited from the primary interface of the Node.

CNI | MTU | GKE Standard  
---|---|---  
kubenet | 1460 | Default  
kubenet  
(GKE version 1.26.1 and later)  | Inherited | Default  
Calico | 1460 |  Enabled by using `--enable-network-policy`. For details, see [Control communication between Pods and Services using network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).  
netd | Inherited |  Enabled by using any of the following: 

  * [Intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility)
  * [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
  * [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network)

  
GKE Dataplane V2 | Inherited |  Enabled by using `--enable-dataplane-v2`. For details, see [Using GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2).  
  
## Mismatched MTUs, MSS clamping, path MTU discovery

This section describes how TCP and non-TCP protocols handle mismatched MTUs. 

### TCP protocol

The TCP protocol handles MTU mismatches automatically. Both the client and server individually calculate their own effective TCP maximum segment size (MSS) values each time a TCP connection is opened. The client and server don't have to agree on an identical effective MSS value.

  * Effective TCP maximum segment size (MSS) of the client: The largest amount of transmissible data in a TCP segment sent from a client to a server is the _minimum_ of the following two values:

    * The value of the MSS field in the SYN-ACK packet received by the client from the server during TCP connection establishment.

    * The MTU of the client's network interface, minus 40 bytes. The subtracted 40 bytes includes 20 bytes for the IP header and 20 bytes for the base TCP header.

  * Effective TCP maximum segment size (MSS) of the server: The largest amount of transmissible data in a TCP segment sent from a server to a client is the _minimum_ of the following two values:

    * The value of the MSS field in the SYN packet received by the server from the client during TCP connection establishment.

    * The MTU of the server's network interface, minus 40 bytes. The subtracted 40 bytes includes 20 bytes for the IP header and 20 bytes for the base TCP header.




### TCP MSS clamping

TCP MSS clamping is a process where a network device between a client and server changes the MSS values in SYN and SYN-ACK packets as it routes the packets between the client and server. Google Cloud uses MSS clamping whenever it sends packets to destinations outside of a VPC network.

Cloud VPN tunnels and Cloud Interconnect VLAN attachments also use MSS clamping. For more information, see [Packet encapsulation and processing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations#encapsulation-and-fragmentation) in the Cloud VPN documentation and [Cloud Interconnect MTU](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#interconnect-mtu).

VPC networks don't perform MSS clamping for packets routed by the next hops within a VPC network because the TCP protocol itself is sufficient.

### Non-TCP protocols

Other protocols, such as UDP, require special care when two different VPC network MTUs are involved. It is the responsibility of a sending system to emit packets that fit within its network interface MTU, the MTU of the receiving system's network interface, and the MTU of all networks in between. Google Cloud does _not_ perform IP fragmentation for packets routed by the next hops within a VPC network.

When an IP packet is too large to be delivered—for example, when the packet exceeds the MTU of the VPC network where the receiving compute instance's NIC is located— Google Cloud drops the packet. If the packet has the `DF` bit set, Google Cloud also sends a Fragmentation Needed (ICMP over IPv4) or Packet Too Big (ICMPv6) message back to the sender.

Google Cloud sends a Fragmentation Needed or Packet Too Big message in the following circumstances, even when a `DF` bit is off:

  * If the VPC network MTU is less than 1,600 bytes, and the packet being sent exceeds the VPC network MTU.
  * If the VPC network MTU is 1,600 bytes or more, and the packet being sent exceeds 1,600 bytes.



ICMP Fragmentation Needed or Packet Too Big messages are necessary for a compute instance that is sending packets to use [Path MTU discovery (PMTUD)](https://www.wikipedia.org/wiki/Path_MTU_Discovery). To illustrate how PMTUD works, consider the following example with two compute instances in different VPC networks that are connected by using VPC Network Peering:

  * The sending instance has a NIC in a VPC network whose MTU is 8,896 bytes.
  * The receiving instance has a NIC in a VPC network whose MTU is 1,460 bytes.
  * The sending instance emits an 8,000-byte IP packet whose Don't Fragment (`DF`) bit is set. Because the packet is too large to be delivered to the receiving instance, Google Cloud sends a Fragmentation Required or Packet Too Big message to the sending instance. This message indicates the largest possible IP packet size that the sender can use when it attempts to re-transmit packets for the connection.
  * The sending instance's operating system uses this information to lower the IP packet size when sending subsequent packets to the receiving instance.



PMTUD has the following additional requirements because PMTUD-generated Fragmentation Needed or Packet Too Big packets use the ICMP protocol and have sources that match an original packet's destination:

  * You must configure ingress allow [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) or [rules in firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details) such that ICMP (for IPv4) or ICMPv6 (for IPv6) are allowed from sources that match the original packet destinations. To simplify firewall configuration, consider allowing ICMP and ICMPv6 from all sources.
  * Forwarding rules for internal passthrough Network Load Balancer and internal protocol forwarding must use the `L3_DEFAULT` protocol so that they process both ICMP for PMTUD and the protocol used by the original packet.



## What's next

  * To see a different MTU working, see [Create and verify a jumbo frame MTU network](https://docs.cloud.google.com/vpc/docs/configure-jumbo-frame-mtu-vpc).
  * Create a [VPC network with a specified MTU](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).
  * [Change the MTU setting of a VPC network](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how VPC performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try VPC free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
