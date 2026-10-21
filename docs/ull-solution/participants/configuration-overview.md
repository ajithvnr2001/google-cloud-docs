---
url: https://docs.cloud.google.com/ull-solution/participants/configuration-overview/
title: Configuration overview for ULL Solution \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:23.261064+00:00
---

# Configuration overview for ULL Solution  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/configuration-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configuration overview for ULL Solution

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page provides an overview of the configuration process for Google Cloud Ultra Low Latency (ULL) Solution for exchange participants.

After the configuration process is complete, workloads that run on ULL Compute Engine instances can send and receive ULL unicast traffic, and receive ULL multicast traffic.

For an illustration of the ULL multicast connectivity enabled by this configuration, see [ULL Multicast zonal deployment pattern](https://docs.cloud.google.com/ull-solution/participants/multicast-overview#zonal-deployment-pattern).

## Before you begin

Before you configure ULL Solution, see the following sections.

### Review supported locations for ULL Solution

ULL Solution is supported in the following Google Cloud region and private zones. You use these locations when following the configuration procedure for ULL Solution.

Region | Zone  
---|---  
`us-south1` | 

  * `us-south1-d`
  * `us-south1-e`

  
  
Additionally, if you plan to connect your on-premises network to Google Cloud by using [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview), the [Equinix Dallas (DA1)](https://www.peeringdb.com/fac/4) colocation facility is the optimal facility for access to the preceding locations. For more information, see [All colocation facilities](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities).

### Review the maintenance process for ULL Solution private zones

The private zones used for ULL Solution have unique availability and maintenance properties compared to public zones in Google Cloud. To understand and plan for maintenance in ULL Solution private zones, see [Maintenance in ULL Solution private zones](https://docs.cloud.google.com/ull-solution/participants/zone-maintenance).

## Exchange participant configuration

This section describes the steps that exchange participants must complete in a given zone to configure ULL infrastructure and enable ULL unicast and multicast connectivity with the exchange operator. Follow these steps to create configurations in each supported zone.

Step | Sub-step (if applicable) | Description  
---|---|---  
Create networks  
[Create VPC networks](https://docs.cloud.google.com/ull-solution/participants/create-participant-ull-vpc-networks) |  Create a general-purpose VPC network  |  Create a VPC network for general-purpose traffic, such as management and service access. When you create ULL Compute Engine instances in a later step, the `nic0` interfaces of each instance attach to this network.   
Create a participant ULL VPC network  |  Create a VPC network with the participant ULL network profile for ULL unicast and multicast traffic. When you create ULL Compute Engine instances in a later step, the `nic1` and `nic2` interfaces attach to different subnets in this network.  
Add a spoke to the hub | Add the participant ULL VPC network as an edge spoke to the hub created by the exchange operator. This enables unicast connectivity and the creation of multicast consumer configurations.  
[Configure ULL firewall policies](https://docs.cloud.google.com/ull-solution/participants/firewall/create-firewall-rules) | Create ULL firewall policy rules as needed for ULL unicast connectivity with the exchange operator.  
Configure ULL Multicast  
[Enable a ULL VPC network to consume multicast traffic](https://docs.cloud.google.com/ull-solution/participants/enable-consumer-network) | Add the multicast consumer network to each domain | For the participant ULL VPC network that you are using as the multicast consumer network, create a consumer association between the network and each domain that was created and activated by the exchange operator.   
Activate the multicast consumer VPC network for each group range | Create a group consumer activation for each multicast group range that was created and activated by the exchange operator.  
Create compute instances  
[Create ULL Compute Engine instances](https://docs.cloud.google.com/ull-solution/participants/create-ull-instances) | Create and configure one or more ULL compute instances as multicast consumers.  
  
### Additional procedures for exchange participants

See the following additional configuration procedures for exchange participants:

  * **Optimize performance:** To configure Onload or DPDK on ULL Compute Engine instances, see [Work with Onload](https://docs.cloud.google.com/ull-solution/participants/use-onload) or [Work with DPDK](https://docs.cloud.google.com/ull-solution/participants/use-dpdk).
  * **Create instances for auxiliary workloads:** To create non-ULL compute instances (U4S) in your general-purpose VPC network, see [Create non-ULL Compute Engine instances for auxiliary workloads](https://docs.cloud.google.com/ull-solution/participants/create-non-ull-instances).
  * **Configure accurate time:** To synchronize the system clock of a U4 instance to the physical NIC clock on the instance's host server, see [Configure accurate time for U4 Compute Engine instances](https://docs.cloud.google.com/ull-solution/participants/configure-time-sync).
  * **View flow logs:** To understand VPC Flow Logs records for ULL unicast and multicast traffic and to view flow logs, see [View flow logs for ULL traffic](https://docs.cloud.google.com/ull-solution/participants/view-flow-logs).
  * **Observe mirrored traffic:** ULL traffic is mirrored by default. To configure collectors to observe and analyze mirrored traffic from ULL VPC networks, see [Packet Mirroring for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/packet-mirroring-ull).
  * **Configure Cloud Multicast:** You can create [Cloud Multicast configurations](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview) in your general-purpose VPC network and use U4C and U4S instances as multicast consumers in ULL Solution private zones.



## What's next

  * To get started by creating networks, see [Create VPC networks for exchange participant workloads](https://docs.cloud.google.com/ull-solution/participants/create-participant-ull-vpc-networks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
