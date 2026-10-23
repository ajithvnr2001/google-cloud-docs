---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview/
title: Dedicated Interconnect overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:55:32.673887+00:00
---

# Dedicated Interconnect overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Dedicated Interconnect overview Stay organized with collections  Save and categorize content based on your preferences. 

Dedicated Interconnect provides direct physical connections between your on-premises network and Google's network. Dedicated Interconnect lets you transfer large amounts of data between networks, which can be more cost-effective than purchasing additional bandwidth over the public internet.

## Before you use Dedicated Interconnect

Make sure that you meet the following requirements:

  * Be familiar with basic network [interconnections](https://wikipedia.org/wiki/Interconnection) so that you can order and configure circuits.
  * Be familiar with [Cloud Interconnect terminology](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).
  * Your network must physically meet Google's network in a [colocation facility](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities). You must provide your own routing equipment. Your on-premises router is typically located in the colocation facility. However, you can also extend your connection to a router outside of the colocation facility.
  * In the colocation facility, your network devices must support the following technical requirements:

    * At least one of the following:

      * 10-Gbps circuits, single mode fiber, 10GBASE-LR (1310 nm)
      * 100-Gbps circuits, single mode fiber, 100GBASE-LR4
      * 400-Gbps circuits, single mode fiber, 400GBASE-LR4
**Note:** The maximum supported fiber length for 10GBASE-LR, 100GBASE-LR4, or 400GBASE-LR optics is 10 km. If your on-premises router is more than 10 km away from the Google demarcation, you must use a lit wavelength, [DWDM](https://www.wikipedia.org/wiki/Wavelength-division_multiplexing), or other managed circuit to complete your connection.
    * IPv4 link local addressing

    * LACP, even if you're using a single circuit

    * EBGP-4 with multi-hop

    * 802.1Q VLANs




## How does Dedicated Interconnect work?

For Dedicated Interconnect, you provision a Dedicated Interconnect connection between the Google network and your own network.

The following example diagram shows a single Dedicated Interconnect connection between a Virtual Private Cloud (VPC) network and your on-premises network.

[ ![A Dedicated Interconnect connection \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/single-interconnect.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/single-interconnect.svg) Dedicated Interconnect connection (click to enlarge)

For the basic setup shown in the diagram, a Dedicated Interconnect connection is provisioned between the Google network and the on-premises router in a common colocation facility. Your setup might be different if your on-premises router is not in the same colocation facility as your Dedicated Interconnect demarcation.

When you create a VLAN attachment, you associate it with a Cloud Router. This Cloud Router creates a BGP session for the VLAN attachment and its corresponding on-premises peer router. The Cloud Router receives the routes that your on-premises router advertises. These routes are added as custom dynamic routes in your VPC network. The Cloud Router also advertises routes for Google Cloud resources to the on-premises peer router.

## VLAN attachment MTU options

VLAN attachments can have a maximum transmission unit (MTU) of 1440, 1460, 1500 or 8896 bytes.

The following limitations apply:

  * VLAN attachments with an MTU of 8896 (also known as _jumbo frames_) are supported only on unencrypted IPv4 and IPv6 VLAN attachments.

  * Requests to Google API Client Libraries automatically use 1440 MTU packets, even if your VLAN attachment is set to a higher MTU value, including jumbo frames.




We recommend that you use the same MTU for all VLAN attachments that are connected to the same VPC network, and that you set the MTU of the VPC networks to the same value. For more information about Cloud Interconnect MTUs, see [Cloud Interconnect MTU](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#interconnect-mtu).

## Provisioning

To create and configure a Dedicated Interconnect connection, you start by deciding where you want a Dedicated Interconnect connection and whether you want [MACsec for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview). Then, you order a Dedicated Interconnect connection so that Google can allocate the necessary resources and send you a Letter of Authorization and Connecting Facility Assignment (LOA-CFA). After you receive the LOA-CFA, you need to submit it to your vendor so that they can provision the connections between Google's network and your network.

You then need to configure and test the connections with Google before you can use them. After they're ready, you can create VLAN attachments to allocate a VLAN on the connection.

For detailed steps to provision a Dedicated Interconnect connection, see the [Provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

**Note:** If you encounter any issues during the provisioning stage, we advise you to reply directly to the email received with your [LOA-CFA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#loa). Replying to that email lets you receive support faster than creating a support case.

### Port capacity

When you order a Dedicated Interconnect connection, you can request one of the following link types. Each link type has a different maximum capacity: 

  * 1 x 10-Gbps (10 Gbps) circuit up to 8 x 10-Gbps (80 Gbps) circuits
  * 1 x 100-Gbps (100 Gbps) circuit up to 8 x 100-Gbps (800 Gbps) circuits
  * 1 x 400-Gbps (400 Gbps) circuit up to 8 x 400-Gbps (3200 Gbps) circuits

**Caution:** The link type that you select when you create a Dedicated Interconnect connection cannot be changed later. For example, if you select a 10-Gbps link type and need a 100-Gbps link type later, you must create a new Dedicated Interconnect connection with the higher capacity.

### Fixed pricing

Dedicated Interconnect offers fixed port pricing for outbound data transfers for VLAN attachments. You can choose fixed pricing for each Dedicated Interconnect connection and choose which types of connections you want the fixed pricing to apply to. This lets you get a fixed monthly invoice for outbound data transfers.

Fixed port pricing considers the following types of connections:

  * **Local connection** : The VLAN attachment is in the same a metro location where the destination Google Cloud [region](https://docs.cloud.google.com/docs/geography-and-regions) is located.

For example, if you obtain a VLAN attachment in the Los Angeles, California metro location and the destination Google Cloud region is `us-west2`, then the VLAN attachment's location and destination Google Cloud region are the same. This is considered a local connection.

  * **Remote connection** : The VLAN attachment is in a different metro location where the destination Google Cloud region is located.

For example, if you create a VLAN attachment in the Los Angeles, California metro location and the destination Google Cloud region is `us-east4`, then the VLAN attachment's location and destination Google Cloud region are different. This is considered a remote connection.

Similarly, if you obtain a VLAN attachment in the Portland, Oregon metro location, then there isn't a local Google Cloud region available within that metro location. Because you can't connect to a local Google Cloud region, this is considered a remote connection.




The following Google Cloud regions only offer support for fixed pricing for remote connections on Dedicated Interconnect:

  * us-west1
  * us-east1
  * europe-west4
  * europe-north1
  * asia-east1



To request a Dedicated Interconnect connection with fixed port pricing, contact your account team.

## Cloud Interconnect groups

You can use connection groups to communicate your intended level of reliability, and to receive feedback on how your Cloud Interconnect resources meet that intended level of reliability. There are two types of Cloud Interconnect resource groups:

  * **Interconnect groups**. Use these to group your Cloud Interconnect connections.
  * **Attachment groups**. Use these to group your VLAN attachments.



When you group your Cloud Interconnect connections and VLAN attachments, you receive information about the group's structure, global routing requirements, operational status, SLA eligibilityand blockers. Use these groups to establish that your deployment meets the requirements for your chosen level of reliability. You can use Cloud Interconnect connection groups without configuring VLAN attachment groups, and you can use VLAN attachment groups without configuring Cloud Interconnect connection groups.

Connection groups are only an informational and organizational tool. Connection groups **never change the behavior** of your Cloud Interconnect connections or your VLAN attachments. This makes connection groups safe to use for your production resources.

You can add a Cloud Interconnect connection to more than one Cloud Interconnect connection group. The connection group must be in the same project as the resources in the group.

You can't add a VLAN attachment to more than one VLAN attachment group. In addition, all of the VLAN attachments in an attachment group must be configured for the same VPC network.

To configure Cloud Interconnect groups, see [Create a Dedicated Interconnect connection group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect#create-group).

## Redundancy and SLA

When you configure a Cloud Interconnect connection, you can do so at a specific level of reliability. You can choose between the following reliability options:

  * **Critical production**. Choose this option for critical production workloads that require maximum resiliency. This option provides a 99.99% uptime SLA.
  * **Non-critical production**. Choose this option for non-critical production and development workloads. This option provides a 99.9% uptime SLA.
  * **No SLA**. You can configure your connection group without specifying an intended level of reliability. We recommend that you avoid using this option for resources in which extended downtime is undesirable. This option doesn't provide an uptime SLA.



For more information about Cloud Interconnect SLAs, see [Dedicated Interconnect and Partner Interconnect SLA](https://cloud.google.com/network-connectivity/docs/interconnect/sla).

For the highest level availability, we recommend the configuration for 99.99% availability as the base configuration, as shown in the following diagram. Clients in the on-premises network can reach the IP addresses of virtual machine (VM) instances in the `us-central1` region through at least one of the redundant paths. If one path is unavailable, the other paths can continue to serve traffic.

[ ![Redundant connections for 99.99% availability \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/9999-availability.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/9999-availability.svg) Redundant connections for 99.99% availability (click to enlarge)

We recommend that you use the 99.99% availability configuration for production-level applications with a low tolerance for downtime. If your applications aren't mission-critical and can tolerate some downtime, you can use the 99.9% availability configuration.

The SLA requires properly configured topologies that are defined by the 99.99% and 99.9% configurations. These configurations support availability and provide an SLA. 

Each level of reliability has a different set of metropolitan area (metro) and edge availability domain (metro availability zone) requirements:

  * **Critical production**. _At least_ four Dedicated Interconnect connections, two connections in one metropolitan area (metro) and two connections in another metro. Connections that are in the same metro must be placed in _different_ [edge availability domains](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain) (metro availability zones) to achieve 99.99% availability. Placing Dedicated Interconnect connections in two separate edge availability domains within the same metro is important because maintenance windows are coordinated across edge availability domains within a metro, while maintenance windows are _not_ coordinated across metros.
  * **Non-critical production**. _At least_ two Cloud Interconnect connections. The connections must be located in the same metropolitan area (metro) but in different edge availability domains (metro availability zones). It doesn't matter if the connections are in the same facility or in different facilities, as long as they are located in two _different_ edge availability domains.



### Balance egress traffic with redundant connections

When you have a redundant topology similar to the 99.99% configuration, there are multiple paths for traffic to traverse from the VPC network to your on-premises network.

Google Cloud uses [ECMP](https://www.wikipedia.org/wiki/Equal-cost_multi-path_routing) to balance the egress traffic across connections. To use ECMP, the Cloud Routers used by the VLAN attachments must receive the same announcement with equal cost (the same CIDR range and the same MED values).

Google Cloud balances the traffic between the VLAN attachments based upon the configured capacity of each VLAN attachment.

### Create redundant connections with sufficient capacity

The Best practices document describes best practices for [creating redundant Cloud Interconnect connections that have sufficient capacity in a failover scenario](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#capacity). When you follow these practices, events such as planned maintenance or hardware failures are less likely to cause a loss of connectivity.

### Dedicated Interconnect availability

A Dedicated Interconnect connection is considered available if you can send and receive ICMP packets (`ping`) between a VM in a specific Google Cloud region and a correctly configured machine in your on-premises network. You should be able to send and receive packets through at least one of your redundant connections.

**Note:** When testing availability, Google assumes that all connections and related devices are correctly configured and connected.

## IPv6 support

Dedicated Interconnect supports IPv6 traffic.

To support IPv6 traffic in a Dedicated Interconnect, do the following:

  * Configure your VPC networks to use either IPv4 and IPv6 (dual stack) or IPv6-only [subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

  * Assign subnets within [internal IPv6 ranges](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).

  * [Configure IPv6 addresses for VMs and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address) within the subnet.




For more information about configuring IPv6 within a subnet, see the following:

  * To create a custom mode VPC network with internal IPv6 addresses, see [Create a custom mode VPC network with a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-network-dual).

  * To create a dual-stack subnet, see [Add a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6).

  * To enable IPv6 in an existing IPv4-only subnet, see [Change an IPv4-only subnet to dual stack](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-enable-ipv6).

  * To add an IPv6-only subnet, see [Add an IPv6-only subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only)

  * To create or enable VMs with IPv6, see [Configure IPv6 for instances and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address).




For information about using internal IPv6 ranges in your VPC network and subnets, see [Internal IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).

After configuring IPv6 in your VPC network, subnets, and VMs, configure your VLAN attachments.

## Stack types and BGP sessions

With Dedicated Interconnect, you can choose between two different stack types for your VLAN attachment.

  * Single stack (IPv4 only)
  * Dual stack (IPv4 and IPv6)



The stack type that you select for your VLAN attachment determines what version of IP traffic is supported by your Dedicated Interconnect connection.

When you create the BGP sessions for a dual-stack VLAN attachment, you have the following options for IPv6 route exchange:

  * You can create an IPv6 BGP session
  * You can create an IPv4 BGP session that [exchanges IPv6 routes by using multiprotocol BGP (MP-BGP)](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).



The following table summarizes the types of BGP sessions allowed for each Dedicated Interconnect VLAN attachment.

Stack type | Supported BGP sessions  
---|---  
IPv4 only | IPv4 BGP  
IPv4 and IPv6 | 

  * IPv4 BGP, with or without MP-BGP
  * IPv6 BGP, with or without MP-BGP
  * Both IPv4 BGP and IPv6 BGP, no MP-BGP

  
  
For more information about BGP sessions, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp) in the Cloud Router documentation.

**Single-stack IPv4-only VLAN attachments**

By default, a Dedicated Interconnect VLAN attachment is assigned the IPv4-only stack type.

An IPv4-only VLAN attachment can support only IPv4 traffic.

Use the following procedure to create an IPv4-only Dedicated Interconnect VLAN attachment and an IPv4 BGP session.

  * [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)



**Dual-stack IPv4 and IPv6 VLAN attachments**

A Dedicated Interconnect VLAN attachment that is configured with the dual-stack (IPv4 and IPv6) stack type can support both IPv4 and IPv6 traffic.

For a dual-stack VLAN attachment, you can configure your Cloud Router with an IPv4 BGP session, an IPv6 BGP session, or both. If you configure only one BGP session, you can enable MP-BGP to allow that session to exchange both IPv4 and IPv6 routes. If you create an IPv4 BGP session and an IPv6 BGP session, you can't enable MP-BGP on either session.

Use the following procedure to create a dual-stack Dedicated Interconnect VLAN attachment and all supported BGP sessions.

  * [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)



You can also change the stack type of your VLAN attachment after you create the attachment. For more information, see [Modify VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect//how-to/dedicated/modifying-vlans).

## Custom IP address ranges

When you create a VLAN attachment for Dedicated Interconnect, you can configure custom IP address ranges for the Cloud Router and customer router ends of the attachment. For information about how it works, including limitations and best practices, see the [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip) section in the Cloud Interconnect overview.

When you configure custom IP address ranges for VLAN attachments that you use with Dedicated Interconnect, you must provide the custom IP address ranges during VLAN creation. However, you can add IPv6 custom IP address ranges when you upgrade your stack type from `IPV4_ONLY` to `IPV4_IPV6`. To configure custom IP address ranges with Dedicated Interconnect, see [Configure custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#custom-ip).

## Restrict Dedicated Interconnect usage

By default, any VPC network can use Cloud Interconnect. To control which VPC networks can use Cloud Interconnect, you can set an organization policy. For more information, see [Restrict Cloud Interconnect usage](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/restricting-usage). 

## What's next?

  * To find answers to common questions about Cloud Interconnect architecture and features, see the [Cloud Interconnect FAQ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq).
  * To find out more about Cloud Interconnect, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  * To learn about best practices when planning for and configuring Cloud Interconnect, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).
  * To find Google Cloud resource names, see the [Cloud Interconnect APIs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/reference/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
