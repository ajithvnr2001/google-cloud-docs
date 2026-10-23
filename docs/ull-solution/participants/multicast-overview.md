---
url: https://docs.cloud.google.com/ull-solution/participants/multicast-overview/
title: ULL Multicast overview \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:34.774413+00:00
---

# ULL Multicast overview  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/multicast-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ULL Multicast overview

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page provides an overview of Ultra Low Latency (ULL) Multicast in Google Cloud.

ULL Multicast shares many of the same properties as [Cloud Multicast](https://docs.cloud.google.com/vpc/docs/multicast/overview). The following sections focus on the unique properties of ULL Multicast.

## Comparison of ULL Multicast and Cloud Multicast

The following table summarizes the key differences between ULL Multicast and Cloud Multicast:

Property | Cloud Multicast | ULL Multicast  
---|---|---  
Overview and configuration  
Summary | A multicast service based on software-defined networking that uses infrastructure in a tenant project and network managed by Google to replicate and distribute traffic. | A hardware-based multicast service for applications with strict latency and multicast variance requirements. Relies on infrastructure directly in the physical network fabric to replicate and distribute traffic.  
API and resource model | See the following  


  * Uses a [multicast resource model](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#resources) that consists of multicast domains, group ranges, producer configurations, and consumer configurations.
  * Resources are implemented by the network services API as described in the [multicast API reference](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)

| See the following  


  * Uses the same [multicast resource model](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#resources) as Cloud Multicast. However, ULL Multicast domains have several differences. For details, see ULL Multicast resource model.
  * Uses the same [API](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest) as Cloud Multicast.

  
Configuration procedure | To configure Cloud Multicast, see the [Cloud Multicast configuration overview](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview). | To configure ULL Multicast, see [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview).  
Location and scope  
Supported locations | Each of the following:  


  * The list of [public regions and zones](https://docs.cloud.google.com/vpc/docs/multicast/overview#locations) in the Cloud Multicast overview
  * The list of [private regions and zones](https://docs.cloud.google.com/ull-solution/participants/configuration-overview#locations) in the ULL Solution configuration overview

| Only the following:  


  * The list of [private regions and zones](https://docs.cloud.google.com/ull-solution/participants/configuration-overview#locations) in the ULL Solution configuration overview

  
Traffic distribution scope | Each of the following:  


  * Intra-zone
  * Intra-region

A single multicast domain can be created and activated in multiple zones to enable cross-zone multicast as described in the [cross-zone deployment pattern for Cloud Multicast](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#cross-zone). | Only the following:  


  * Intra-zone

  
Each pre-configured multicast domain is created and activated once for a given zone to enable intra-zone multicast as described in the zonal deployment pattern for ULL Multicast.  
Compatible compute and network resources  
Supported Compute Engine instance types | Each of the following:  


  * The list of [ supported instance types](https://docs.cloud.google.com/vpc/docs/multicast/overview#machine-requirements) in the Cloud Multicast overview
  * U4P instances
  * U4C instances
  * U4S instances

| Only the following:  


  * U4P and U4C instances

  
Supported VPC network types | General-purpose VPC networks:  


  * Regular VPC networks (no network profile)
  * VPC networks that are created with a regional network profile (_regional VPC networks_)

| VPC networks with a ULL network profile:  


  * Operator ULL VPC networks
  * Participant ULL VPC networks

  
  
## ULL Multicast resource model

ULL Multicast uses the same [API](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest) and resource model as Cloud Multicast, including each resource described in [Overview of the multicast resource model](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#resources).

For ULL Multicast, see the following details:

  * **Multicast domains** : are created by the exchange operator, but have unique considerations for consumers compared to Cloud Multicast. For more information, see the following Instance and network interface mapping for ULL Multicast domains section.
  * **Multicast consumer configurations** : consumer associations and group consumer activations have the same properties described in [Multicast consumer configurations](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#consumer-resources). For information about creating these resources for ULL Multicast, see [Enable a ULL VPC network to consume multicast traffic](https://docs.cloud.google.com/ull-solution/participants/enable-consumer-network).



### Instance and network interface mapping for ULL Multicast domains

This section describes the relationship between ULL Multicast domains, ULL Compute Engine instance types, and the network interfaces of those compute instances. The behavior described in this section assumes that corresponding multicast configurations are created as described in [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview).

The following table describes which instance types, network interfaces, and actions are supported for a given ULL Multicast domain. Multicast producer and consumer instances that don't adhere to this mapping can't send and receive ULL multicast traffic successfully.

Domain | Instance type | Supported action  
---|---|---  
**Feed A**  
(created with the `feed-a` pre-configured domain)  | U4P instance |  Send multicast traffic A U4P instance can send traffic for this domain from any of its ULL network interfaces.  
U4C instance |  Receive multicast traffic. A U4C instance must receive traffic on the same network interface number from which the U4P instance sends traffic. For example, if the U4P instance sends traffic from `nic1` for this domain, the U4C instance must receive traffic on `nic1`.  
**Feed B**  
(created with the `feed-b` pre-configured domain)  | U4P instance |  Send multicast traffic A U4P instance can send traffic for this domain from any of its ULL network interfaces.  
U4C instance |  Receive multicast traffic. A U4C instance must receive traffic on the same network interface number from which the U4P instance sends traffic. For example, if the U4P instance sends traffic from `nic2` for this domain, the U4C instance must receive traffic on `nic2`.  
  
## ULL Multicast zonal deployment pattern

ULL Multicast supports the same [topologies](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#topologies) and [deployment patterns](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#deployment-patterns) as Cloud Multicast, except for cross-zone multicast.

This section provides the general per-zone deployment pattern for ULL Multicast that enables multicast connectivity between multicast producers in an exchange operator project and multicast consumers in exchange participant projects. This deployment pattern uses the Network Connectivity Center (NCC) star topology and redundant multicast domains.

### ULL multicast traffic in a zone

The following diagram illustrates ULL multicast traffic through redundant multicast domains in the NCC star topology.

In this example, a multicast producer sends traffic to multicast consumers in the same zone and in different ULL VPC networks through redundant multicast infrastructure that corresponds to two separate multicast domains.

**Note:** This diagram focuses on ULL connectivity. `nic0` interface attachments to general-purpose VPC networks are omitted.[ ![ULL multicast traffic in a zone.](https://docs.cloud.google.com/static/ull-solution/images/ull-zonal-data.svg)](https://docs.cloud.google.com/static/ull-solution/images/ull-zonal-data.svg) ULL multicast traffic in a zone (click to enlarge).

### Resource configuration in a zone

The following diagram illustrates the network and multicast resources that must be configured to achieve the multicast connectivity that's described in the previous section.

[ ![ULL Multicast resource configuration in a zone.](https://docs.cloud.google.com/static/ull-solution/images/ull-zonal-management.svg)](https://docs.cloud.google.com/static/ull-solution/images/ull-zonal-management.svg) ULL Multicast resource configuration in a zone (click to enlarge).

The following table describes the resource configurations in the preceding diagram. To use redundant multicast domains, you must create redundant configurations for each multicast resource type.

Resource types | Configuration  
---|---  
Multicast domains and group ranges |  Resources for redundant multicast domains:

  * a multicast administrator network that is a center spoke on the hub. Each of the following multicast domains is configured with the NCC topology setting and the same hub.
  * a multicast domain group that acts as a container for the redundant multicast domains.
  * a Feed A multicast domain and one or more corresponding group ranges are created in the network and are activated in `us-south1-d`. The multicast domain is created with the pre-configured `feed-a` ULL domain.
  * a Feed B multicast domain and one or more corresponding group ranges are created in the network and are activated in `us-south1-d`. The multicast domain is created with the pre-configured `feed-b` ULL domain.

  
Multicast producer configurations |  The example configuration uses the same network as the multicast administrator network and multicast producer network. Resources that allow `nic1` of the multicast producer to send traffic through the Feed A multicast domain:

  * a multicast producer association between the network and the Feed A domain
  * a multicast group producer activation for one or more group ranges that are associated with the Feed A domain

Resources that allow `nic2` of the multicast producer to send traffic through the Feed B multicast domain:

  * a multicast producer association between the network and the Feed B domain
  * a multicast group producer activation for one or more group ranges that are associated with the Feed B domain

  
Multicast consumer configurations |  Two multicast consumer networks are edge spokes on the hub and each contain resources that allow multicast consumers to receive traffic. Resources that allow `nic1` of the multicast consumers to receive traffic through the Feed A multicast domain:

  * a multicast consumer association between the network and the Feed A domain
  * a multicast group consumer activation for one or more group ranges that are associated with the Feed A domain

Resources that allow `nic2` of the multicast consumers to receive traffic through the Feed B multicast domain:

  * a multicast consumer association between the network and the Feed B domain
  * a multicast group consumer activation for one or more group ranges that are associated with the Feed B domain

  
  
## Limitations

ULL Multicast shares most of the [limitations of Cloud Multicast](https://docs.cloud.google.com/vpc/docs/multicast/overview#limitations) (such as being restricted to IPv4 and UDP, and requiring a 1500 byte MTU). For limitations specific to ULL Multicast, see the following:

  * ULL Multicast is supported only in the private zones for ULL Solution, and only for ULL Compute Engine instances attached to ULL VPC networks as described in Comparison of ULL Multicast and Cloud Multicast. Other locations and resource types aren't supported. 
  * Cross-zone multicast traffic isn't supported.
  * Support for packet mirroring depends on the packet mirroring service: 
    * ULL Packet Mirroring mirrors all traffic from every eligible ULL VPC network, and you can't disable this feature. To observe and analyze mirrored traffic, see [Packet Mirroring for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/packet-mirroring-ull). 
    * [Network Security Integration Packet Mirroring](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview) and [VPC Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) aren't supported. 



## Quotas and limits

Multicast resources created for use with ULL Multicast contribute to most of the same quotas and limits for Cloud Multicast as described in [Multicast quotas and limits](https://docs.cloud.google.com/vpc/docs/multicast/quotas).

## What's next

  * To get started, see [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
