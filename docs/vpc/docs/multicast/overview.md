---
url: https://docs.cloud.google.com/vpc/docs/multicast/overview/
title: Cloud Multicast overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:44.383178+00:00
---

# Cloud Multicast overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Multicast overview

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page provides an overview of Cloud Multicast.

[Multicast](https://en.wikipedia.org/wiki/Multicast) is a type of network communication that allows a source (multicast producer) to send the same data to multiple destinations (multicast consumers) at the same time. To receive traffic, multicast consumers must first join the _multicast group_ that the multicast producer sends traffic to. Multicast group membership is managed with [Internet Group Management Protocol (IGMP)](https://en.wikipedia.org/wiki/Internet_Group_Management_Protocol).

Cloud Multicast is a managed service that delivers cloud-based multicast support for Virtual Private Cloud (VPC) networks. You can use Cloud Multicast to enable Compute Engine instances to act as multicast producers and consumers. For an overview of the resource model and the topologies that you can configure, see [Cloud Multicast resource model and topologies](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies).

This documentation and the [multicast API](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest) use the terms _multicast producer_ and _multicast consumer_ throughout to refer to resources involved in sending and receiving multicast traffic. Multicast producers are also known as multicast publishers, senders, or sources. Multicast consumers are also known as multicast subscribers, receivers, or listeners.

## Specifications

Cloud Multicast has the following specifications:

  * **IGMPv2 for managing multicast group membership** : Cloud Multicast uses IGMPv2 to manage multicast group membership as defined by [RFC 2236](https://www.rfc-editor.org/rfc/rfc2236). Multicast applications moving to Google Cloud can continue to use IGMPv2 to join and leave multicast groups. For more information, see How IGMPv2 works.
  * **Intra-region, cross-zone multicast distribution** : Cloud Multicast supports distributing traffic to multicast consumers in the same region as the multicast producer. Multicast consumers can be located in different zones from the multicast producer. You can optionally restrict distribution to intra-zone only, where the multicast producer and multicast consumers are both in the same zone.
  * **Multicast infrastructure redundancy through domains** : Cloud Multicast uses multicast _domains_ as a reliability boundary, where each domain uses separate infrastructure to distribute multicast traffic. For more information, see [Multicast domains](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#domains).



### How IGMPv2 works

The following list describes how IGMPv2 works after [Cloud Multicast is configured](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview):

  * Multicast producers can send traffic to a multicast group _without_ joining the group.
  * For multicast consumers, see the following: 
    * Multicast routers send IGMP general query messages to `224.0.0.1` to determine the groups that multicast consumers want to join.
    * To receive IGMP general query messages, a multicast consumer [must be configured for IGMP](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms). After the multicast consumer is configured for IGMP, the multicast consumer continuously receives periodic IGMP general query messages.
    * To join a multicast group, the multicast consumer responds with an IGMP membership report. The destination IP address for an IGMP membership report is the multicast group IP address. If the multicast consumer stops responding, it is automatically removed after three missed queries.
    * To leave a multicast group, the multicast consumer sends an IGMP leave message to `224.0.0.2`.



You can view logs for multicast group membership events, such as when the Google Cloud control plane received a join request or successfully added a multicast consumer to a group. For more information, see [View multicast group membership event logs](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs).

## Machine considerations for multicast producers and consumers

This section describes the factors that you must consider when you choose a Compute Engine machine type for multicast producer and consumer instances. For multicast applications that send or receive a high level of traffic, follow the guidance in this section for optimal performance and to help prevent issues such as packet loss caused by resource exhaustion.

See the following guidance:

  * Use machine types from the [C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines) when you create multicast producer or consumer instances.
  * You can create VM instances or bare metal instances.
  * The following table includes the minimum supported number of vCPUs and the maximum supported packets per second (pps) based on the number of vCPUs. The maximum pps is an aggregate limit across all multicast traffic flows, not a per-flow limit. Additionally, the maximum pps applies per multicast domain, and a multicast producer or consumer instance supports a maximum of two domains. For optimal performance, choose a machine type and vCPU count according to your anticipated volume of multicast traffic.
  * The _maximum traffic flows_ columns correspond to the number of multicast groups for which a multicast producer or consumer instance can send or receive traffic. This limit applies across all domains and group ranges. For multicast producers, the limit is always 512, regardless of machine type. For multicast consumers, the limit depends on the vCPU count. For more information, see [Cloud Multicast quotas and limits](https://docs.cloud.google.com/vpc/docs/multicast/quotas#other_system_limits_for_multicast).
  * If you use a machine type that has 48 vCPUs or more, create the instance with [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) enabled.

Machine types | vCPUs | Maximum pps | Maximum traffic flows (multicast producer) | Maximum traffic flows (multicast consumer)  
---|---|---|---|---  
[C4 machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_machine_types) | 32 | 140,000 | 512 | 128  
48 | 266,000 | 512 | 170  
96 | 533,000 | 512 | 340  
144 | 800,000 | 512 | 512  
288 | 1,600,000 | 512 | 1024  



In addition to choosing a machine type based on the guidance in this section, consider using a network kernel bypass such as DPDK as described in [Enable faster network packet processing with DPDK](https://docs.cloud.google.com/compute/docs/networking/use-dpdk).

## Supported locations

You can use Cloud Multicast in the following Google Cloud regions and zones:

Region | Zones  
---|---  
`europe-west2` | 

  * `europe-west2-a`
  * `europe-west2-b`

  
`europe-west3` | 

  * `europe-west3-a`
  * `europe-west3-b`

  
`us-central1` | 

  * `us-central1-b`
  * `us-central1-c`

  
`us-east5` | 

  * `us-east5-a`
  * `us-east5-b`

  
  
## Billing

The following list provides information about billing charges that apply to Cloud Multicast infrastructure and traffic. For pricing details, contact your Google Cloud sales representative.

  * **Multicast infrastructure resource reservation** : Billing for multicast infrastructure is charged to multicast administrator projects that contain multicast domain activations. Billing starts when a multicast domain activation is created.
  * **Multicast data processing** : Billing for multicast data processing is charged to projects in which multicast consumers receive multicast traffic.



If you use Network Connectivity Center (NCC), [Advanced Data Networking](https://docs.cloud.google.com/network-connectivity/pricing#ncc-pricing) charges apply to traffic sent from multicast producers to the multicast infrastructure. These charges don't apply to the traffic that is replicated by the multicast infrastructure and delivered to multicast consumers.

## Limitations

Cloud Multicast has the following limitations:

  * Cloud Multicast is available in a limited set of zones as described in Supported locations.
  * Cloud Multicast is supported only for Compute Engine instances in VPC networks. Cloud Multicast isn't supported for other endpoint types, or through hybrid connectivity options such as Cloud Interconnect or Cloud VPN that you use to access on-premises networks or remote cloud service providers.
  * Cloud Multicast supports only the machine types described in Machine considerations for multicast producers and consumers. Other machine types aren't supported for use with Cloud Multicast.
  * Cloud Multicast supports only IPv4 traffic. IPv6 traffic isn't supported.
  * Cloud Multicast supports UDP as the layer 4 protocol.
  * Don't use the multicast address space (`224.0.0.0/4`) for non-multicast traffic as this can lead to issues such as traffic being misrouted or handled incorrectly.
  * Cloud Multicast doesn't support jumbo frames. Don't use a maximum transmission unit (MTU) size greater than 1500 bytes. For more information about VPC MTU sizes, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
  * Cross-region multicast traffic isn't supported. While you can activate the same multicast domain in different regions to enable cross-zone multicast traffic within each region, this configuration doesn't enable sending multicast traffic between regions.
  * The total number of IP addresses in one or more multicast group ranges associated with the same domain can't exceed your quota for [Multicast groups per domain](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_groups_per_domain). Additionally, we recommend grouping multicast IP addresses into ranges instead of reserving many individual addresses. For example, use one `/24` address range instead of reserving 256 `/32` addresses.
  * Support for packet mirroring depends on the packet mirroring service:

    * [Network Security Integration Packet Mirroring](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview) is supported for use with Cloud Multicast. However, it impacts performance as described in the [Limitations of Network Security Integration Packet Mirroring](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview#limitations).
    * [VPC Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) isn't supported for use with Cloud Multicast.

For information about the differences between VPC Packet Mirroring and Network Security Integration Packet Mirroring, see [Comparison of VPC Packet Mirroring and Network Security Integration Packet Mirroring](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview#difference-between-vpc-packet-mirroring-and-nsi-mirroring).

  * To help avoid performance degradation or packet loss, we recommend that Cloud Multicast configurations don't exceed the following for a given multicast domain:

    * A maximum aggregate egress packet per second (pps) throughput of 100,000,000 pps per zone.
    * A maximum of 500 multicast consumers per multicast group per zone.



## Quotas and limits

Cloud Multicast resources are subject to the quotas and limits described in [Cloud Multicast quotas and limits](https://docs.cloud.google.com/vpc/docs/multicast/quotas).

## What's next

  * [Learn more about the Cloud Multicast resource model and topologies](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies)
  * [Learn more about configuring Cloud Multicast](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
