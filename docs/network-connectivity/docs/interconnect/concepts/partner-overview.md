---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview/
title: Partner Interconnect overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:32.604379+00:00
---

# Partner Interconnect overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Partner Interconnect overview Stay organized with collections  Save and categorize content based on your preferences. 

Partner Interconnect provides connectivity between your on-premises network and your Virtual Private Cloud (VPC) network through a supported service provider. A Partner Interconnect connection is useful if your data center is in a physical location that can't reach a Dedicated Interconnect colocation facility, or your data needs don't warrant an entire 10-Gbps connection.

## Before you use Partner Interconnect

Ensure that you meet the following requirements:

  * Be familiar with [Cloud Interconnect terminology](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).
  * Work with a [supported service provider](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers) to establish connectivity between their network and your on-premises network. Supported service providers offer Layer 2 connectivity, Layer 3 connectivity, or both. Work with your service provider to understand their offerings and requirements.

**Note:** Partner Interconnect requires that you separately obtain services from a third-party network service provider. Google is not responsible for any aspects of Partner Interconnect provided by the third-party service provider nor any issues outside of Google's network.

## How does Partner Interconnect work?

Service providers have existing physical connections to Google's network that they make available for their customers to use. After you establish connectivity with a service provider, you can request a Partner Interconnect connection from your service provider. After the service provider provisions your connection, you can start passing traffic between your networks by using the service provider's network.

[ ![A Partner Interconnect connection \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/partner-interconnect-overview-intro.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/partner-interconnect-overview-intro.svg) Partner Interconnect connection (click to enlarge)

## VLAN attachment MTU options

We recommend that you use the same MTU for all VLAN attachments that are connected to the same VPC network, and that you set the MTU of the VPC networks to the same value. For more information about Cloud Interconnect MTUs, see [Cloud Interconnect MTU](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#interconnect-mtu).

## Provisioning

To provision a Partner Interconnect connection with a service provider, you start by selecting a partner and whether you want [MACsec for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview), and then connecting your on-premises network to a supported service provider. Work with the service provider to establish connectivity.

Next, you create a VLAN attachment for a Partner Interconnect connection in your Google Cloud project, which generates a unique pairing key that you use to request a connection from your service provider. You also need to provide other information such as the connection location, IP stack type, and capacity.

After the service provider configures your VLAN attachment, you activate your connection to start using it. Depending on your connection, either you or your service provider then establishes a Border Gateway Protocol (BGP) session.

For detailed steps to provision a Partner Interconnect connection, see the [Provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview).

## Port capacity

When you order a Dedicated Interconnect connection, your service provider request one of the following link types. Each link type has a different maximum capacity:

  * 1 x 10-Gbps (10 Gbps) circuit up to 8 x 10-Gbps (80 Gbps) circuits
  * 1 x 100-Gbps (100 Gbps) circuit up to 8 x 100-Gbps (800 Gbps) circuits



## Layer 2 versus Layer 3 connectivity

For Layer 2 connections, you must configure and establish a BGP session between your Cloud Routers and on-premises routers for each VLAN attachment that you create. The BGP configuration information is provided by the VLAN attachment after your service provider has configured it.

For Layer 3 connections, your service provider establishes a BGP session between your Cloud Routers and their on-premises routers for each VLAN attachment. You don't need to configure BGP on your local router. Google and your service provider automatically set the correct BGP configurations.

Because the BGP configuration for Layer 3 connections is fully automated, you can pre-activate your connections (VLAN attachments). When you enable pre-activation, the VLAN attachments are active as soon as the service provider configures them.

### Pre-activation

After you create a VLAN attachment and your service provider configures it, the attachment can't pass traffic until you activate it. Activation lets you check that you're connecting to an expected service provider.

If you don't need to verify the connection and are using a Layer 3 connection, you can choose to pre-activate the attachment. If you pre-activate the attachment, it can immediately pass traffic after your service provider has configured it.

If you want to verify who you're connecting to, don't pre-activate your attachments.

Consider pre-activation if you're using Layer 3 and want your connection to activate without additional approval. Layer 3 service providers automatically configure BGP sessions with your Cloud Routers so that BGP starts immediately. You don't need to return to Google after your service provider configures your attachments.

For Layer 2 connections, there's no benefit to pre-activating VLAN attachments.

### Basic topology

The following topology diagrams show example Partner Interconnect connections for Layer 2 and Layer 3.

For Layer 2 connections, traffic passes through the service provider's network to reach the VPC network or on-premises network. BGP is configured between the on-premises router and a Cloud Router in the VPC network, as shown in the following diagram.

[ ![Layer 2 topology \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/layer2-basic.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/layer2-basic.svg) Layer 2 topology (click to enlarge)

For Layer 3 connections, traffic is passed to the service provider's network. Their network then routes the traffic to the correct destination, either to the on-premises network or to the VPC network. Connectivity between the on-premises network and the service provider network depends on the service provider. For example, the service provider might request that you establish a BGP session with them or configure a static default route to their network.

[ ![Layer 3 topology \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/layer3-basic.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/layer3-basic.svg) Layer 3 topology (click to enlarge)

## Redundancy and SLA

Depending on your availability needs, you can configure Partner Interconnect to support mission-critical services or applications that can tolerate some downtime. To achieve a specific level of reliability, Google has two prescriptive configurations:

  * [Establish 99.99% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability) (recommended)
  * [Establish 99.9% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-999-availability)



We recommend that you use the 99.99% availability configuration for production-level applications with a low tolerance for downtime. If your applications aren't mission-critical and can tolerate some downtime, you can use the 99.9% availability configuration.

For the 99.99% and 99.9% availability configurations, Google offers an SLA _that applies only to the connectivity between your VPC network and the service provider's network._ The SLA doesn't include the connectivity between your network and the service provider's network. If your service provider does offer an SLA, you can get an end-to-end SLA based on the Google-defined topologies. For more information, ask your service provider.

### 99.99% availability topology

For the highest level availability, we recommend the 99.99% availability configuration. Clients in the on-premises network can reach the IP addresses of virtual machine (VM) instances in the selected [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions) through at least one of the redundant paths. If one path is unavailable, the other paths can continue to serve traffic.

99.99% availability requires at least four VLAN attachments across two metros, one in each edge availability domain (metro availability zone). You also need two Cloud Routers (one in each Google Cloud region of a VPC network). Associate one Cloud Router with each pair of VLAN attachments. You must also [enable global routing](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes) for the VPC network.

For Layer 2 connections, four virtual circuits are required, split between two metros. Layer 2 also requires that you add four BGP sessions to the on-premises router, two for each Cloud Router, as shown in the following diagram.

[ ![Redundant connections for 99.99% availability using Layer 2 \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/9999-layer2.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/9999-layer2.svg) Redundant connections for 99.99% availability using Layer 2 (click to enlarge)

For Layer 3 connections, four connections between Google and your service provider are required. You create four VLAN attachments, and then your service provider establishes two BGP sessions with each of your Cloud Routers. The VLAN attachments must be split between two metros, as shown in the following diagram.

[ ![Redundant connections for 99.99% availability using Layer 3 \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/9999-layer3.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/9999-layer3.svg) Redundant connections for 99.99% availability using Layer 3 (click to enlarge)

### Multiple service providers

To build a highly available topology, you can use multiple service providers. You must build redundant connections for each service provider in each metro.

For example, you might provision two primary connections by using a local service provider that's close to your data center. For the backup connection, you might use a long-haul service provider to build two connections in a different metro. Ensure that this topology meets all your requirements for availability.

### Balancing egress traffic with redundant VLAN attachments

When you have a redundant topology similar to the 99.99% configuration, there are multiple paths for traffic to traverse from the VPC network to your on-premises network.

Google Cloud uses [ECMP](https://www.wikipedia.org/wiki/Equal-cost_multi-path_routing) to balance the egress traffic across connections. To use ECMP, the Cloud Routers used by the VLAN attachments must receive the same announcement with equal cost (the same CIDR range and the same MED values).

Dedicated Interconnect does the following to balance traffic across connections:

Google Cloud balances the traffic between the VLAN attachments based upon the configured capacity of each VLAN attachment.

### Create redundant connections with sufficient capacity

The [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#capacity) document describes best practices for creating redundant connections that have sufficient capacity in a failover scenario. Following these practices helps ensure that events such as planned maintenance or hardware failures do not cause loss of connectivity.

## IPv6 support

Partner Interconnect supports IPv6 traffic for both Layer 2 and Layer 3 connectivity. You have the option to create an IPv4 and IPv6 (dual stack) VLAN attachment.

Dual-stack Partner Interconnect VLAN attachments must use separate IPv4 and IPv6 BGP sessions. Multiprotocol BGP (MP-BGP)—IPv4 + IPv6 route exchange—on a single BGP session isn't supported.

**Important:** Encrypted VLAN attachments don't support IPv6 dual-stack sessions.

To support IPv6 traffic in a Partner Interconnect connection, do the following:

  * Configure your VPC networks to use either IPv4 and IPv6 (dual stack) or IPv6-only [subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

  * Assign subnets within [internal IPv6 ranges](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).

  * [Configure IPv6 addresses for VMs and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address) within the subnet.




For more information about configuring IPv6 within a subnet, see the following:

  * To create a custom mode VPC network with internal IPv6 addresses, see [Create a custom mode VPC network with a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/using-vpc#create-network-dual).

  * To create a subnet with IPv6 enabled, see [Add a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6).

  * To enable IPv6 in an existing subnet, see [Change a subnet's stack type to dual stack](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-enable-ipv6).

  * To create or enable VMs with IPv6, see [Configure IPv6 for instances and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address).




For information about using internal IPv6 ranges in your VPC network and subnets, see [Internal IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).

After configuring IPv6 in your VPC network, subnets, and VMs, configure your VLAN attachments.

## Custom IP address ranges

When you create a VLAN attachment for Partner Interconnect, you can configure custom IP address ranges for the Cloud Router and customer router ends of the attachment. For information about how it works, including limitations and best practices, see the [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip) section in the Cloud Interconnect overview.

The process for creating VLAN attachments differs based on whether you request a Layer 3 or Layer 2 connection from your service provider:

  * Layer 2: when you configure custom IP address ranges for VLAN attachments that you use with Partner Interconnect, you must provide the custom IP address ranges during VLAN creation. You can also add IPv6 custom IP address ranges when you upgrade your stack type from `IPV4_ONLY` to `IPV4_IPV6`. To configure custom IP address ranges for Layer 2 connections, see [Use custom IP address ranges with Layer 2 connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#custom-ip-l2).
  * Layer 3: after you create a VLAN attachment and share it with your service provider, they configure the custom IP address. This means that you don't manually configure custom IP address ranges when you configure your VLAN attachment. Your service provider can also configure custom IP addresses when you upgrade an attachment's stack type from `IPV4_ONLY` to `IPV4_IPV6`.



## Restrict Partner Interconnect usage

By default, any VPC network can use Cloud Interconnect. To control which VPC networks can use Cloud Interconnect, you can set an organization policy. For more information, see [Restrict Cloud Interconnect usage](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/restricting-usage). 

## Limitations

You can't send and learn MED values over a Layer 3 Partner Interconnect connection.

If you are using a Partner Interconnect connection where a Layer 3 service provider handles BGP for you, Cloud Router can't learn MED values from your on-premises router or send MED values to that router. This is because MED values can't pass through autonomous systems. Over this type of connection, you can't set route priorities for routes advertised by Cloud Router to your on-premises router. In addition, you can't set route priorities for routes advertised by your on-premises router to your VPC network.

## What's next?

  * To find answers to common questions about Cloud Interconnect architecture and features, see the [Cloud Interconnect FAQ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq).
  * To find out more about Cloud Interconnect, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  * To learn about best practices when planning for and configuring Cloud Interconnect, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).
  * To find Google Cloud resource names, see the [Cloud Interconnect APIs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/reference/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
