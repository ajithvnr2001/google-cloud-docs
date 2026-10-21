---
url: https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview/
title: Cloud Multicast configuration overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:45.856541+00:00
---

# Cloud Multicast configuration overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Multicast configuration overview

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes the process of configuring Cloud Multicast according to each supported topology.

After the configuration process is complete, you can use Cloud Multicast for the following:

  * Multicast producers can send multicast traffic.
  * Multicast consumers can receive multicast traffic. A given multicast consumer must have IGMP configured as described in [Configure multicast consumer instances](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms).



## Single VPC network topology

The following table describes the steps required by the multicast administrator to configure Cloud Multicast in a [single VPC network topology](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#single-network).

Step | Sub-step | Description  
---|---|---  
[Create a VPC network](https://docs.cloud.google.com/vpc/docs/multicast/create-domains#network) | N/A | If you don't already have one, create a VPC network to use for Cloud Multicast. Ensure that the firewall configuration for the VPC network allows multicast and IGMP traffic.  
[Create a multicast domain](https://docs.cloud.google.com/vpc/docs/multicast/create-domains)  
Create a domain group (optional) | If you plan to create redundant domains, we recommend that you create a domain group for higher availability between the domains.  
Create a domain | Create one or more domains. Each domain uses separate infrastructure to distribute multicast traffic.  
Activate the domain | Activate the domain in each zone that contains multicast producers or consumers.  
[Create a multicast group range](https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges)  
Create a group range | Associate a multicast group IP address range with the multicast domain.  
Activate the group range | Activate the group range in each zone where multicast producers or consumers need to use the associated group IP addresses.  
[Enable the VPC network to produce multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network)  
Add the network to the domain as a multicast producer network | Create a multicast producer association between the VPC network and the domain in each zone that contains multicast producers.  
Activate the network for a group range as a multicast producer network | Create a multicast group producer activation for each group range in each zone that contains multicast producers.  
Create multicast producers | Create multicast producer instances in the VPC network.  
[Enable the VPC network to consume multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network)  
Add the network to the domain as a multicast consumer network | Create a multicast consumer association between the VPC network and the domain in each zone that contains multicast consumers.  
Activate the network for a group range as a multicast consumer network | Create a group consumer activation for each group range in each zone that contains multicast consumers.  
Create multicast consumers | Create multicast consumer instances in the VPC network and configure the instances for IGMP.  
  
## Network Connectivity Center star topology

The following sections describe how you configure Cloud Multicast in a [Network Connectivity Center (NCC) star topology](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#network-connectivity-center).

### Multicast administrator configuration

The multicast administrator completes the following steps described in [Create multicast domains](https://docs.cloud.google.com/vpc/docs/multicast/create-domains) and [Create multicast group ranges](https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges):

Step | Sub-step | Description  
---|---|---  
Create a VPC network | N/A | If you don't already have one, create a VPC network to use for managing the Cloud Multicast infrastructure and IP address ranges of multicast groups.  
Configure NCC  
Create a hub | Create a NCC hub using the preset star topology.  
Add a spoke to the hub | Add the multicast administrator VPC network as a center spoke to the hub. You can accept spoke proposals for multicast consumer VPC networks as needed as described in [Control access to multicast domains](https://docs.cloud.google.com/vpc/docs/multicast/control-access-domains).  
Create a multicast domain  
Create a domain group (optional) | If you plan to create redundant domains, we recommend that you create a domain group for higher availability between the domains.  
Create a domain | Create one or more domains. Each domain uses separate infrastructure to distribute multicast traffic.  
Activate the domain | Activate the domain in each zone that contains multicast producers or consumers.  
Create a multicast group range  
Create a group range | Associate a multicast group IP address range with the multicast domain. If you configure a group range that has an accept list, ensure that each multicast consumer project that needs to use the group range is in the accept list so that they can complete their configurations successfully.  
Activate the group range | Activate the group range in each zone where multicast producers or consumers need to use the associated group IP addresses.  
  
### Multicast producer configuration

This section describes the steps that a multicast producer network administrator must complete to enable multicast producers in a VPC network to send multicast traffic.

The following table provides an overview of the steps described in [Enable a VPC network to produce multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network):

Step | Description  
---|---  
Create a VPC network | If you don't already have one, create a VPC network to host multicast producers. In the NCC star topology, you can use the multicast administrator network to host multicast producers, or create a separate multicast producer network.  
Add firewall rules | Ensure that the firewall configuration for the VPC network allows multicast traffic.  
Add the VPC network to a hub | Add the multicast producer network as a center spoke to the hub created by the multicast administrator.  
Add the multicast producer VPC network to a domain | Create a producer association between the network and the domain that was created by the multicast administrator. Complete this step in each zone that contains multicast producers.  
Activate the multicast producer VPC network for a group range | Create a group producer activation for each group range in each zone that contains multicast producers.  
Create multicast producers | Create multicast producer instances in the VPC network.  
  
### Multicast consumer configuration

This section describes the steps that a multicast consumer network administrator must complete to enable multicast consumers in a VPC network to receive multicast traffic.

The following table provides an overview of the steps described in [Enable a VPC network to consume multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network):

Step | Description  
---|---  
Create a VPC network | If you don't already have one, create a VPC network to host multicast consumers.  
Add firewall rules | Ensure that the firewall configuration for the VPC network allows multicast and IGMP traffic.  
Add the VPC network to the hub | Add the multicast consumer network as an edge spoke1 to the hub created by the multicast administrator.  
Add the multicast consumer VPC network to a domain | Create a consumer association between the network and the domain that was created by the multicast administrator. Complete this step in each zone that contains multicast consumers.  
Activate the multicast consumer VPC network for a group range | Create a group consumer activation for each group range in each zone that contains multicast consumers.  
Create multicast consumers | Create multicast consumer instances in the VPC network and configure the instances for IGMP.  
  
1 A multicast administrator VPC network or multicast producer VPC network can host multicast consumers while being a center spoke on the hub.

## What's next

  * [Create multicast domains](https://docs.cloud.google.com/vpc/docs/multicast/create-domains)
  * [Create multicast group ranges](https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges)
  * [Enable a VPC network to produce multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network)
  * [Enable a VPC network to consume multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
