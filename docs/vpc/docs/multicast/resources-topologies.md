---
url: https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies/
title: Cloud Multicast resource model and topologies \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:51.637176+00:00
---

# Cloud Multicast resource model and topologies  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Multicast resource model and topologies

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page provides an overview of the resource model and supported topologies for Cloud Multicast.

For more information about the specific properties of each resource, see [Multicast API reference](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest).

For information about the Identity and Access Management (IAM) roles and permissions for Cloud Multicast resources, see the [permissions reference](https://docs.cloud.google.com/vpc/docs/multicast/reference/permissions-reference).

## Cloud Multicast resource model

The following sections describe the Google Cloud resources that are required for administering Cloud Multicast, producing multicast traffic, and consuming multicast traffic.

For diagrams that illustrate the Cloud Multicast resource model in different configuration scenarios, see multicast topologies and additional deployment patterns.

### Overview of the Cloud Multicast resource model

The following table describes the resources that are required to use Cloud Multicast and who manages them. For more information about a type of resource, see its corresponding section.

Resource types | Description  
---|---  
Multicast domains and group ranges **Managed by** A _multicast administrator_ |  Resources that you use to administer Cloud Multicast:

  * Multicast domains represent the infrastructure that distributes multicast traffic.
  * Multicast group ranges represent the IP addresses of multicast groups.

A domain can contain one or more group ranges.  
Multicast producer configurations **Managed by** Either the multicast administrator or a _multicast producer network administrator_ , depending on the multicast topology. |  Resources that you configure to enable multicast producers in a given VPC network to send multicast traffic for a given domain and one or more group ranges. These resources must be in the same project as the multicast domain and group range resources.  
Multicast consumer configurations **Managed by** Either the multicast administrator or a _multicast consumer network administrator_ , depending on the multicast topology. |  Resources that you configure to enable multicast consumers in a given VPC network to receive multicast traffic for a given domain and one or more group ranges. These resources can be in the same project as the multicast domain and group range resources or in a different project.  
  
### Multicast domains

The following table describes the resources that multicast administrators use to create and manage Cloud Multicast infrastructure.

For information about creating these resources, see [Create multicast domains](https://docs.cloud.google.com/vpc/docs/multicast/create-domains).

Resource | Scope | Description  
---|---|---  
Multicast domain group (optional) | Global |  A container for logically grouping two related domains together that can help you achieve high availability for your multicast infrastructure. When two domains are part of a domain group, Google Cloud places the infrastructure for each domain in two different high availability shards.  Additionally, for configurations that use a domain group, Google Cloud automatically creates a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) that can optionally be [applied to new or existing multicast consumer instances](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms). When applied, Compute Engine tries to place the instance as close as possible to the infrastructure for the multicast domain in the corresponding zone.   
Multicast domain | Global | Represents a reliability domain in the multicast administrator VPC network, where each domain uses separate infrastructure to distribute multicast traffic. Multicast domains help create infrastructure redundancy if producers send the same traffic to multicast group IP addresses in different domains. Multicast domains provide higher availability when configured as part of a domain group. The multicast administrator also sets the network topology to use for Cloud Multicast when creating a domain.  
Multicast domain activation | Zonal | Represents the infrastructure that distributes multicast traffic. When you activate a multicast domain in a zone, Google Cloud provisions infrastructure for your domain in that zone. The infrastructure runs in a tenant project and VPC network that is managed by Google.  
  
### Multicast group ranges

The following table describes the resources that multicast administrators use to create and manage multicast group IP address ranges.

For information about creating these resources, see [Create multicast group ranges](https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges).

Resource | Scope | Description  
---|---|---  
Multicast group range | Global | A unique multicast group IP address range in the multicast administrator VPC network that is associated with a specific multicast domain. A domain can contain one or more multicast group ranges. The administrator network manages multicast group IP addresses to ensure that there is no overlap between multiple domains. Multicast groups must use a Class D IP address range (`224.0.0.0/4`) as defined by the [IETF](https://datatracker.ietf.org/doc/html/rfc870). The multicast group range also provides a way to control access to multicast groups. You can configure the set of Google Cloud projects that can use the group range. For more information, see [Create a multicast group range](https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges).  
Multicast group range activation | Zonal | Enables multicast producers and consumers to start using a multicast group IP address range in a given zone.  
  
### Multicast producer configurations

The following table describes the resources that must be configured to enable multicast producers in a given VPC network to send multicast traffic as a source for one or more multicast group ranges.

For information about creating these resources, see [Enable a VPC network to produce multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network).

Resource | Scope | Description  
---|---|---  
Multicast producer association | Zonal | For a given multicast domain, this resource associates a multicast producer VPC network with the domain in a specific zone. In other words, it adds the network to a domain and zone as a multicast producer network. A multicast producer association is required in each zone that contains multicast producers. Additionally, you must create the producer association before you can create the group producer activation.  
Multicast group producer activation | Zonal | For a given multicast group range, this resource allows multicast producers to begin sending traffic to a group from a specific zone. In other words, it _activates_ a multicast producer VPC network for a group range and zone. A multicast group producer activation is required for each multicast group range and zone in which you want to produce multicast traffic.  
  
### Multicast consumer configurations

The following table describes the resources that must be configured to enable multicast consumers in a given VPC network to receive multicast traffic for one or more multicast group ranges.

For information about creating these resources, see [Enable a VPC network to consume multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network). Additionally, you must follow the steps to [configure IGMP for multicast consumer instances](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms).

If the same network hosts multicast producers and consumers, then the multicast consumer associations and activations must be created after the multicast producer associations and activations.

Resource | Scope | Description  
---|---|---  
Multicast consumer association | Zonal | For a given multicast domain, this resource associates a multicast consumer VPC network with the domain in a specific zone. In other words, it adds the network to a domain and zone as a multicast consumer network. A multicast consumer association is required in each zone that contains multicast consumers. Additionally, you must create the consumer association before you can create the group consumer activation.  
Multicast group consumer activation | Zonal | For a given multicast group range, this resource allows multicast consumers to begin receiving traffic for a group in a specific zone. In other words, it _activates_ a multicast consumer VPC network for a group range and zone. A multicast group consumer activation is required for each multicast group range and zone in which you want to consume multicast traffic.  
  
## Cloud Multicast topologies

This section describes the topologies that the multicast administrator can configure for Cloud Multicast.

### Overview of Cloud Multicast topologies

When you create a multicast domain, you must choose one of the following topologies. You can't change the topology after creating the domain. If your use case requires or might later require hosting multicast producers and consumers in different VPC networks, ensure that you configure the Network Connectivity Center (NCC) star topology.

Topology | Description  
---|---  
Single VPC network topology | If multicast producers and consumers are always in the same VPC network, use the single VPC network topology. This topology uses a single network to manage multicast domains and group ranges and to host multicast producers and consumers. Multicast traffic is sent and received only within the network.  
NCC star topology |  If your use case requires multicast producers and consumers to be in different VPC networks, use the NCC star topology. This topology uses separate VPC networks1 that are part of the same NCC hub as follows:

  * A multicast administrator VPC network that is a VPC spoke in the center group of a hub.
  * One or more multicast producer VPC networks that are VPC spokes in the center group of the hub. You can choose one of the following options: 
    * If you want to host multicast producers in a different VPC network from the multicast administrator network, you can create a multicast producer network. A multicast producer network must be in the same project as the multicast administrator network.
    * If you want to host multicast producers in the multicast administrator VPC network, you can use the multicast administrator network as the multicast producer network.
  * One or more multicast consumer VPC networks that are VPC spokes in the edge group of the hub. A multicast consumer network can be in the same or different project than the administrator network.

This topology enables both unicast and multicast connectivity between the networks in the center group and the networks in the edge group. However, it doesn't establish connectivity between networks in the edge group, which means that multicast consumer networks can't communicate with each other. When using this topology, consider the following:

  * The VPC spoke for each network must export to the hub the subnet ranges that contain multicast producers or multicast consumers.
  * Google Cloud prohibits subnet range overlap across VPC spokes connected to a hub as described in [Subnet route uniqueness](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin#subnet-uniqueness). To help avoid overlap, you can use [export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters) when you create a spoke to specify which subnet ranges to advertise.

In this topology, you can control access to the domain through accepting or rejecting VPC spokes to or from the hub. For more information about NCC, see the [NCC documentation](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).  
  
1 In the NCC star topology, the multicast administrator VPC network can also host multicast producers and consumers. 

### Single VPC network topology

The diagrams in this section describe the single VPC network topology for Cloud Multicast.

#### Multicast traffic in the single VPC network topology

The following diagram illustrates multicast traffic in the single VPC network topology.

In this basic example, a multicast producer sends traffic to multicast consumers in the same zone. You can expand this topology by configuring cross-zone multicast distribution or redundant multicast domains.

[ ![Multicast traffic in the single VPC network topology.](https://docs.cloud.google.com/static/vpc/images/multicast/single-vpc-data.svg)](https://docs.cloud.google.com/static/vpc/images/multicast/single-vpc-data.svg) Multicast traffic in the single VPC network topology (click to enlarge).

#### Resource configuration for the single VPC network topology

This diagram illustrates the Cloud Multicast resources that you must configure to achieve the multicast connectivity that's described in the previous section.

[ ![Multicast resources in a single VPC network topology.](https://docs.cloud.google.com/static/vpc/images/multicast/single-vpc-management.svg)](https://docs.cloud.google.com/static/vpc/images/multicast/single-vpc-management.svg) Multicast resources in single VPC network topology (click to enlarge).

The following table describes the resource configurations in the preceding diagram.

Resource types | Configuration  
---|---  
Multicast domains and group ranges |  A multicast domain with one or more group ranges are created in the VPC network and are activated in zone A.  
Multicast producer configurations |  Resources that allow the multicast producer to send traffic from zone A:

  * a multicast producer association between the VPC network and the domain
  * a multicast group producer activation for one or more group ranges

  
Multicast consumer configurations |  Resources that allow the multicast consumers to receive traffic in zone A:

  * a multicast consumer association between the VPC network and the domain
  * a multicast group consumer activation for one or more group ranges

  
  
### NCC star topology

The diagrams in this section describe the NCC star topology for Cloud Multicast.

#### Multicast traffic in the star topology

The following diagram illustrates multicast traffic in the NCC star topology.

In this basic example, a multicast producer sends traffic to multicast consumers in the same zone in different VPC networks. You can expand this topology by configuring cross-zone multicast distribution or redundant multicast domains, or adding more multicast producer networks.

[ ![Multicast traffic in the NCC star topology.](https://docs.cloud.google.com/static/vpc/images/multicast/ncc-data.svg)](https://docs.cloud.google.com/static/vpc/images/multicast/ncc-data.svg) Multicast traffic in the NCC star topology (click to enlarge).

#### Resource configuration for the star topology

The following diagram illustrates the network and Cloud Multicast resources that you must configure to achieve the multicast connectivity that's described in the previous section.

[ ![Multicast resources in the NCC star topology.](https://docs.cloud.google.com/static/vpc/images/multicast/ncc-management.svg)](https://docs.cloud.google.com/static/vpc/images/multicast/ncc-management.svg) Multicast resources in the NCC star topology (click to enlarge).

The following table describes the resource configurations in the preceding diagram.

Resource types | Configuration  
---|---  
Multicast domains and group ranges |  A multicast administrator VPC network is a center spoke on the hub and contains a multicast domain with one or more group ranges that are activated in zone A. The multicast domain is configured with the NCC topology setting and the specific hub to use.  
Multicast producer configurations |  A multicast producer VPC network is a center spoke on the hub and contains resources that allow the multicast producer to send traffic from zone A:

  * a multicast producer association between the VPC network and the domain
  * a multicast group producer activation for one or more group ranges

  
Multicast consumer configurations |  Three multicast consumer VPC networks are edge spokes on the hub and each contain resources that allow multicast consumers to receive traffic in zone A:

  * a multicast consumer association between the VPC network and the domain
  * a multicast group consumer activation for one or more group ranges

  
  
## Additional deployment patterns

This section describes additional deployment patterns that you can follow when configuring Cloud Multicast in either the single VPC network or NCC star topology. You can use any combination of these deployment patterns.

### Cross-zone multicast

This section includes diagrams that illustrate cross-zone multicast traffic and the corresponding configuration requirements.

#### Cross-zone multicast traffic

The following diagram illustrates cross-zone multicast traffic in a single VPC network topology. You can also configure cross-zone multicast traffic when using the NCC star topology.

In this example, a multicast producer in zone B sends traffic to multicast consumers in both zone A and zone B.

[ ![Cross-zone multicast traffic distribution.](https://docs.cloud.google.com/static/vpc/images/multicast/cross-zone-data.svg)](https://docs.cloud.google.com/static/vpc/images/multicast/cross-zone-data.svg) Cross-zone multicast traffic distribution (click to enlarge).

#### Resource configuration for cross-zone multicast

This diagram illustrates the multicast resources that you must configure to achieve the cross-zone multicast connectivity that's described in the previous section.

[ ![Multicast resources for cross-zone distribution.](https://docs.cloud.google.com/static/vpc/images/multicast/cross-zone-management.svg)](https://docs.cloud.google.com/static/vpc/images/multicast/cross-zone-management.svg) Multicast resources for cross-zone distribution (click to enlarge).

The following table describes the resource configurations in the preceding diagram. This configuration requires that you configure several resources in each zone where multicast producers or consumers send or receive traffic.

Resource types | Configuration  
---|---  
Multicast domains and group ranges |  A multicast domain and one or more group ranges are created in the VPC network and are activated in both zone A and zone B.  
Multicast producer configurations |  Resources that allow the multicast producer to send traffic from zone B:

  * a multicast producer association between the VPC network and the domain
  * a multicast group producer activation for one or more group ranges

  
Multicast consumer configurations |  Resources that allow multicast consumers to receive traffic in zone A:

  * a multicast consumer association between the VPC network and the domain
  * a multicast group consumer activation for one or more group ranges

Resources that allow multicast consumers to receive traffic in zone B:

  * a multicast consumer association between the VPC network and the domain
  * a multicast group consumer activation for one or more group ranges

  
  
### Redundant multicast domains

This section includes diagrams that illustrate sending multicast traffic through redundant multicast domains and the corresponding configuration requirements.

#### Multicast traffic through redundant domains

The following diagram illustrates redundant multicast domains in a single VPC network topology. You can also configure redundant domains when using the NCC star topology.

In this example, a multicast producer sends traffic to multicast consumers in the same zone through redundant multicast infrastructure that corresponds to two separate multicast domains.

[ ![Multicast traffic through redundant domains.](https://docs.cloud.google.com/static/vpc/images/multicast/redundant-data.svg)](https://docs.cloud.google.com/static/vpc/images/multicast/redundant-data.svg) Multicast traffic through redundant domains (click to enlarge).

#### Resource configuration for redundant domains

This diagram illustrates the multicast resources that you must configure to achieve the redundant multicast connectivity that's described in the previous section.

[ ![Resource configuration for redundant domains.](https://docs.cloud.google.com/static/vpc/images/multicast/redundant-management.svg)](https://docs.cloud.google.com/static/vpc/images/multicast/redundant-management.svg) Resource configuration for redundant domains (click to enlarge).

The following table describes the resource configurations in the preceding diagram. To use redundant multicast domains, you must create redundant configurations for each resource type.

Resource types | Configuration  
---|---  
Multicast domains and group ranges |  Resources for redundant multicast domains:

  * a multicast domain group that acts as a container for the redundant multicast domains.
  * multicast domain 1 and one or more corresponding group ranges are created in the VPC network and are activated in zone A.
  * multicast domain 2 and one or more corresponding group ranges are created in the VPC network and are activated in zone A.

  
Multicast producer configurations |  Resources that allow the multicast producer to send traffic through multicast domain 1 from zone A:

  * a multicast producer association between the VPC network and domain 1
  * a multicast group producer activation for one or more group ranges that are associated with domain 1

Resources that allow the multicast producer to send traffic through multicast domain 2 from zone A:

  * a multicast producer association between the VPC network and domain 2
  * a multicast group producer activation for one or more group ranges that are associated with domain 2

  
Multicast consumer configurations |  Resources that allow multicast consumers to receive traffic through multicast domain 1 in zone A:

  * a multicast consumer association between the VPC network and domain 1
  * a multicast group consumer activation for one or more group ranges that are associated with domain 1

Resources that allow the multicast consumer to receive traffic through multicast domain 2 in zone A:

  * a multicast consumer association between the VPC network and domain 2
  * a multicast group consumer activation for one or more group ranges that are associated with domain 2

  
  
### Shared VPC

You can optionally use Shared VPC to separate network resources in a host project from compute resources in a service project. For more information, see the [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc).

The following diagram illustrates an example configuration:

  * Host project A contains a shared VPC network with multicast producer configurations. Service project A contains a multicast producer instance that is created in the shared network.
  * Host project B contains a shared VPC network with multicast consumer configurations. Service project B contains a multicast consumer instance that is created in the shared network.

[ ![Shared VPC example configuration for multicast.](https://docs.cloud.google.com/static/vpc/images/multicast/shared-vpc-topology.svg)](https://docs.cloud.google.com/static/vpc/images/multicast/shared-vpc-topology.svg) Shared VPC example configuration for multicast (click to enlarge).

## What's next

  * See the [Cloud Multicast configuration overview](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
