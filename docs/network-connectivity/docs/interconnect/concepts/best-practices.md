---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices/
title: Best practices for Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:21.082294+00:00
---

# Best practices for Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Best practices for Cloud Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

Use the following best practices when planning for and configuring Cloud Interconnect.

**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

## Work with Google Cloud projects

If your network architecture supports it, configure your Cloud Interconnect projects as recommended in this section.

### Provision physical Cloud Interconnect connections in a separate project

**Warning:** After you create a Cloud Interconnect connection in a project, you can't move the connection to a different project or rename the connection later.

Provision physical connections (ports) for Cloud Interconnect in one project, but provision VLAN attachments in other projects. The other projects must be in the same Google Cloud organization as the project that contains the physical connections.

VLAN attachments that connect a physical connection to a region through a Cloud Router don't have to be in the same project as the physical connection. For more information, see [Use connections in other projects](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/using-interconnects-other-projects).

This practice makes the following configuration steps easier:

  * You can associate a separate internal billing account with the project that contains the physical connections.
  * You can configure Identity and Access Management (IAM) roles and permissions in the project that contains the physical connections.
  * If you want to delete or update a resource that is not a physical connection, you can do so without affecting the physical connections.



### Configure VLAN attachments in the Shared VPC host project

In a Shared VPC network, configure all VLAN attachments, not physical Cloud Interconnect connections (ports), in the host project. For more information about connecting attachments to Shared VPC networks, see [Options for connecting to multiple VPC networks](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/enabling-multiple-networks-access-same-attachment).

## Create redundant Cloud Interconnect connections with sufficient capacity

This section describes best practices for creating redundant Cloud Interconnect connections that have sufficient capacity for your VLAN attachments during planned connection maintenance or during an unexpected failure in an edge availability domain (EAD) and colocation facility combination.

Your Cloud Interconnect connections and VLAN attachments must be configured according to one of the following topologies:

  * [Topology for production-level applications](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview)
  * [Topology for non-critical applications](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/non-critical-overview)



Regardless of which topology you choose, your Cloud Interconnect connections must be placed in a pair of EADs and colocation facility combinations within either the metro or each of the metros.

Within each metro, deploy Cloud Interconnect connections in a pair of colocation facility and edge availability domain combinations, distributing the bandwidth evenly between them. The total bandwidth of all Cloud Interconnect connections in the metro should be at least _twice_ as much as what's needed by your VLAN attachments. This way, each metro has enough Cloud Interconnect connections to sustain an issue that affects a single colocation facility and edge availability domain combination within the metro.

### Ensure sufficient capacity in each edge availability domain

If there is downtime or maintenance in one of the edge availability domains in a metropolitan area, traffic fails over to the other edge availability domain.

To avoid packet loss if a single edge availability domain fails, follow this guidance:

Type of capacity | Guidance  
---|---  
Cloud Interconnect connection capacity | Ensure that each edge availability domain has enough connection capacity to carry all your production traffic.  
VLAN attachment capacity | Ensure that each edge availability domain has enough VLAN attachment capacity to carry all the production traffic for the target VPC network. VPC traffic on Cloud Interconnect connections is carried over VLAN attachments, which link the connection to VPC networks. Even if each edge availability domain has enough connection capacity, it must also have enough VLAN attachment capacity.  
  
#### VLAN attachment capacity and multiple VPC networks

If you are using your Cloud Interconnect connections to access more than one Virtual Private Cloud (VPC) network, create VLAN attachments from each VPC network to each Cloud Interconnect connection. For each VPC network, ensure that there is enough VLAN attachment capacity to carry all the production traffic for that VPC network if a failover occurs.

Consider an example in which you have the following VPC networks and workloads:

  * `vpc-1` receives 2 Gbps of total traffic from your on-premises network.
  * `vpc-2` also receives 2 Gbps of total traffic from your on-premises network.



The following table describes the minimum amount of attachment capacity that you need in each edge availability domain for each VPC network:

Edge availability domain | Connection capacity | Attachment capacity  
---|---|---  
EDGE_DOMAIN_1 | 1 x 10 Gbps | 2 x 1 Gbps to `vpc-1`  
2 x 1 Gbps to `vpc-2`  
EDGE_DOMAIN_2 | 1 x 10 Gbps | 2 x 1 Gbps to `vpc-1`  
2 x 1 Gbps to `vpc-2`  
  
When you add VLAN attachments over a Cloud Interconnect connection, your configured attachment capacity might exceed the total capacity of the connection. Although this configuration is valid, your actual traffic cannot exceed the total capacity of the connection. Ensure that your workload does not generate more traffic than the capacity of the connection.

### Use active-active VLAN attachments

There are two ways to configure redundant VLAN attachments:

  * An active-active configuration that splits traffic between the VLAN attachments.
  * An active/passive configuration that uses only one VLAN attachment at a time.



We recommend that you use an active-active configuration because it makes it easy to determine whether all VLAN attachments are working correctly during normal operation. When using an active-active configuration, monitor your usage patterns to ensure that you have sufficient capacity if a failure occurs.

In an active/passive configuration, VLAN attachments might be configured incorrectly without your realizing it. If you do use this configuration, ensure that you test failover before adding production traffic.

**Warning:** To ensure reliable connectivity when using ECMP across active-active VLAN attachments, use flow-based hashing on your on-premises devices. Using per-packet load balancing— for example, round-robin or random—with ECMP is not supported. Using this configuration might cause services in the VPC network, such as Private Service Connect, to close TCP connections unexpectedly.

### Understand failover between regions

Network traffic leaving a region prefers to use the path with the lowest metric, as described in [Effects of dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes) in the Cloud Router overview. In typical usage, this means that egress traffic leaves through the closest Google Cloud region that has any live VLAN attachments, with the local region being the closest.

Consider an example in which you build the [topology for production-level applications](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview), and you have a VPC network with the following:

  * VLAN attachments in two regions
  * Global dynamic routing enabled



Traffic prefers to egress the VLAN attachments in the local region, even if the attachments in that region are overloaded. The traffic only flows to the other region if all the VLAN attachments in the local region are down. This means that each of the four Cloud Interconnect connections in the topology must have enough VLAN attachment capacity to carry all your production traffic.

### Scenarios

This section describes scenarios in which you configure Cloud Interconnect resources. It also describes how each configuration handles your workload during normal operation and failover. Each scenario includes a recommendation related to the best practices for redundancy and capacity.

#### Scenario 1: Sufficient capacity

In this scenario, you provision two Dedicated Interconnect connections in two different edge availability domains as shown in the following table:

Edge availability domain | Connection capacity | Attachment capacity | Attachment region  
---|---|---|---  
EDGE_DOMAIN_1 | 1 x 10 Gbps | 1 x 10 Gbps | ATTACHMENT_REGION_1  
EDGE_DOMAIN_2 | 1 x 10 Gbps | 1 x 10 Gbps | ATTACHMENT_REGION_1  
  
The following table describes how this configuration handles your workload during normal operation and failover:

Resource | Description  
---|---  
Size of your workload | 10 Gbps of total traffic between ATTACHMENT_REGION_1 and your on-premises network.  
Capacity during normal operation | Sufficient capacity 20 Gbps of capacity from ATTACHMENT_REGION_1 to your on-premises network. Your 10-Gbps workload runs successfully.  
Capacity during failover | Sufficient capacity if either Cloud Interconnect connection goes down. For example, if the connection in EDGE_DOMAIN_1 fails, your available capacity is the connection in EDGE_DOMAIN_2. This single Cloud Interconnect connection has 10 Gbps of capacity. The 10 Gbps of attachment capacity that you created on it is enough to carry your production workload. If your workload increases to more than 10 Gbps of traffic, it exceeds the capacity of your attachment, and you might experience packet loss.  
Recommendation | Provision your Cloud Interconnect connection and VLAN attachment capacity so that each edge availability domain has enough capacity for all your production workload.  
  
#### Scenario 2: Insufficient capacity during failover

In this scenario, you provision two Dedicated Interconnect connections in two different edge availability domains as shown in the following table:

Edge availability domain | Connection capacity | Attachment capacity | Attachment region  
---|---|---|---  
EDGE_DOMAIN_1 | 1 x 100 Gbps | 100 Gbps (2 x 50 Gbps) | ATTACHMENT_REGION_1  
EDGE_DOMAIN_2 | 1 x 100 Gbps | 100 Gbps (2 x 50 Gbps) | ATTACHMENT_REGION_1  
  
The following table describes how this configuration handles your workload during normal operation and failover:

Resource | Description  
---|---  
Size of your workload | 150 Gbps of total traffic between ATTACHMENT_REGION_1 and your on-premises network.  
Capacity during normal operation | Sufficient capacity 200 Gbps of capacity from ATTACHMENT_REGION_1 to your on-premises network. Your 150-Gbps workload runs successfully.  
Capacity during failover | Insufficient capacity if either Cloud Interconnect connection goes down. If one of your Cloud Interconnect connections goes down for maintenance, your entire 150-Gbps workload attempts to fail over to a single 100-Gbps connection. This is more than the capacity of the connection, so you experience congestion and packet loss.  
Recommendation | To ensure full availability during a failure event, make sure that the combined traffic over each connection doesn't exceed the total capacity of a single edge availability domain. In this scenario, you need at least 200 Gbps of connection capacity and 3 x 50 Gbps of attachment capacity in each edge availability domain to have sufficient capacity during failover.  
  
#### Scenario 3: Imbalanced VLAN attachments

In this scenario, you provision two Dedicated Interconnect connections in two different edge availability domains as shown in the following table. You initially provision 1 x 10 Gbps of attachment capacity in EDGE_DOMAIN_1. Later, you realize that your workload has grown to 20 Gbps, so you update only the attachment capacity in EDGE_DOMAIN_1 to 2 x 10 Gbps.

Edge availability domain | Connection capacity | Attachment capacity | Attachment region  
---|---|---|---  
EDGE_DOMAIN_1 | 1 x 100 Gbps | 1 x 10 Gbps (initially provisioned)  
**2 x 10 Gbps (updated later)** | ATTACHMENT_REGION_1  
EDGE_DOMAIN_2 | 1 x 100 Gbps | 1 x 10 Gbps | ATTACHMENT_REGION_1  
  
The following table describes how this configuration handles your workload during normal operation and failover:

Resource | Description  
---|---  
Size of workload | 20 Gbps of total traffic between ATTACHMENT_REGION_1 and your on-premises network.  
Capacity during normal operation | Sufficient capacity 30 Gbps of capacity from ATTACHMENT_REGION_1 to your on-premises network. Your 20-Gbps workload runs successfully.  
Capacity during failover | Sufficient capacity if the Cloud Interconnect connection in EDGE_DOMAIN_2 goes down.  
Insufficient capacity if the Cloud Interconnect connection in EDGE_DOMAIN_1 goes down. If your Cloud Interconnect connection in EDGE_DOMAIN_2 goes down, there is still 20 Gbps of attachment capacity from the remaining connection, and your workload runs successfully. However, if your Cloud Interconnect connection in EDGE_DOMAIN_1 goes down, there is only 10 Gbps of attachment capacity from the remaining connection, and you experience congestion and packet loss.  
Recommendation | Make sure that you have equal capacity to both edge availability domains in a metropolitan area; this applies to both Cloud Interconnect connections and VLAN attachments. In this scenario, you need at least 2 x 10 Gbps of attachment capacity in each edge availability domain to ensure sufficient capacity if either Cloud Interconnect connection goes down.   
  
## Use the same MTU for all VLAN attachments

We recommend that you use the same MTU for all VLAN attachments that are connected to the same VPC network, _and_ that you set the MTU of the VPC network to the same value. While that is the recommended practice, you are not forced to make VLAN attachment MTUs and VPC network MTUs match. However, you can experience dropped packets, especially for protocols other than TCP, if you do any of the following:

  * Use different VLAN attachment MTUs for VLAN attachments connected to the same VPC network.
  * Configure VLAN attachment MTUs that are _less than_ the MTU of the VPC network that contains the VLAN attachments.



For general information about how protocols handle mismatched MTUs, see [Mismatched MTUs, MSS clamping, path MTU discovery](https://docs.cloud.google.com/vpc/docs/mtu#mss-clamping-and-pmtud) in the VPC MTU documentation.

Packets sent through a VLAN attachment are processed in the following way:

Situation | Behavior  
---|---  
TCP SYN and SYN-ACK packets | Google Cloud performs MSS clamping, changing the MSS so that packets fit within the VLAN attachment MTU. For example, if the VLAN attachment MTU is 1,500 bytes, MSS clamping uses a 1,460-byte maximum segment size.  
IP packets up to (and including) the MTU of the VLAN attachment | Google Cloud makes no changes to the packet, except for SYN and SYN-ACK packets as discussed in the first row.  
MTU checks for IP packets | 

  * The MTU for packets sent by Google Cloud resources through a VLAN attachment is limited by the VLAN attachment's MTU. For example, when a VM instance sends packets to a destination reachable by a dynamic route whose next hop is a VLAN attachment, packets that exceed the VLAN attachment's MTU are dropped: 
    * Google Cloud drops the packet and sends a Fragmentation Needed (ICMP over IPv4) or Packet Too Big (ICMPv6) message both when the Don't Fragment (DF) bit is on and also when the DF bit is off.
    * You must configure ingress allow [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) or [ rules in firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details) such that ICMP (for IPv4) or ICMPv6 (for IPv6) are allowed from sources that match the original packet destinations.
    * Forwarding rules for internal passthrough Network Load Balancer and internal protocol forwarding must use the `L3_DEFAULT` protocol so that they process both ICMP for Path MTU discovery (PMTUD) and the protocol used by the original packet.
  * Cloud Interconnect doesn't enforce the VLAN attachment MTU for packets received from an on-premises network. Instead, Google Cloud enforces the MTU on the Google Cloud resource that receives the packet: 
    * If the resource that receives the packet is a VM instance, Google Cloud enforces the MTU of the VPC network used by the network interface of the receiving VM, as if the receiving VM had received a packet routed [within the VPC network](https://docs.cloud.google.com/vpc/docs/mtu#within_vpc_net).
    * Packets sent to Google APIs and services from on-premises through a VLAN attachment are processed in the same way as packets sent from VM instances to Google APIs and services. For more information, see [Communication to Google APIs and services](https://docs.cloud.google.com/vpc/docs/mtu#to-cloudpath).

  
Packets sent through HA VPN over Cloud Interconnect | HA VPN over Cloud Interconnect uses a gateway MTU of 1440 bytes, and payload MTUs are smaller, depending on the ciphers used. For more information, see [MTU considerations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations) in the Cloud VPN documentation.   
  
## What's next

  * To choose a connection type for Cloud Interconnect, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect).
  * To find out more about Cloud Interconnect, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
