---
url: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/security/
title: Network security for distributed applications in Cross-Cloud Network \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:48.001530+00:00
---

# Network security for distributed applications in Cross-Cloud Network  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Network security for distributed applications in Cross-Cloud Network Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-30 UTC

This document is part of a design guide series for Cross-Cloud Network. This part explores the network security layer.

The series consists of the following parts:

  * [Cross-Cloud Network for distributed applications](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design)
  * [Network segmentation and connectivity for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity)
  * [Service networking for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/service-networking)
  * Network security for distributed applications in Cross-Cloud Network (this document)



## Security surfaces

When you design the security layer for the Cross-Cloud Network, you must consider the following security surfaces:

  * Workload security
  * Domain perimeter security



Workload security controls the communication between workloads across and within the Virtual Private Cloud (VPC). Workload security uses security enforcement points that are close to the workloads in the architecture. Whenever possible, Cross-Cloud Network provides workload security by using Cloud Next Generation Firewall from Google Cloud.

Perimeter security is required at all network boundaries. Because the perimeter usually interconnects networks that are managed by different organizations, tighter security controls are often required. You must ensure that the following communications across networks are secured:

  * Communications across VPCs
  * Communications across hybrid connections to other cloud providers or on-premises data centers
  * Communications to the internet



The ability to insert third-party network virtual appliances (NVAs) within the Google Cloud environment is critical to address the requirements for perimeter security across hybrid connections. 

## Workload security in cloud

Use [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) in Google Cloud to secure workloads and provide stateful firewall capabilities that are horizontally scalable and applied to each VM instance. The distributed nature of Google Cloud firewalls helps you implement security policies for network micro-segmentation without negatively impacting the performance of your workloads.

Use [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies) to improve the manageability and enforce posture compliance for your firewall policies. Hierarchical firewall policies let you create and enforce a consistent firewall policy across your organization. You can assign Hierarchical firewall policies to the organization or to individual folders. In addition, Hierarchical firewall policies rules can delegate evaluation to lower-level policies (global or regional network firewall policies) with a `goto_next` action.

Lower-level rules cannot override a rule from a higher level in the resource hierarchy. This rule structure lets organization-wide administrators manage mandatory firewall rules in one place. Common use cases for Hierarchical firewall policies include organization or multi-project bastion host access, permitting centralized probing or health check systems, and enforcing a virtual network boundary across an organization or group of projects. For additional examples of using Hierarchical firewall policies, see [Hierarchical firewall policies examples](https://docs.cloud.google.com/firewall/docs/firewall-policies-examples).

Use [global](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) and [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies) to define rules on an individual VPC-network basis, either for all regions of the network (global) or a single [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) (regional). 

To achieve more granular controls enforced at the virtual machine (VM) level, we recommend that you use Identity and Access Management (IAM)-governed [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) at the organization or project level. IAM-governed tags allows applying firewall rules based on the identity of workload host, as opposed to host IP address, and works across VPC Network Peering. Firewall rules deployed using tags can provide intra-subnet micro-segmentation with policy coverage that automatically applies to workloads wherever they are deployed, independent of the network architecture. 

In addition to stateful inspection capabilities and tag support, [Cloud Next Generation Firewall](https://docs.cloud.google.com/firewall) also supports Threat Intelligence, FQDN, and geolocation filtering. 

We recommend that you [migrate from VPC firewall rules to firewall policies](https://cloud.google.com/blog/products/identity-security/best-practices-for-migrating-to-network-firewall-policies). To assist with the migration, use the [migration tool](https://services.google.com/fh/files/misc/vpc_firewall_rules_network_firewall_policy_migration_guide.pdf), which creates a global network firewall policy and converts existing VPC firewall rules into the new policy.

## Perimeter security in cloud

In a multicloud network environment, perimeter security is usually implemented at each network. For example, the on-premises network has its own set of perimeter firewalls, while each cloud network implements separate perimeter firewalls. 

Because the Cross-Cloud Network is designed to be the hub for all communications, you can unify and centralize the perimeter security controls and deploy a single set of perimeter firewalls in your Cross-Cloud Network. To deliver a built-in perimeter security stack of choice, Cross-Cloud Network provides flexible options for you to insert NVAs.

In the designs shown in the diagrams, you can deploy third-party NVAs in the transit VPC in the hub project. 

NVAs can be deployed over a single network interface (single-NIC mode) or over multiple network interfaces across multiple VPCs (multi-NIC mode). For Cross-Cloud Network, we recommend a single-NIC deployment for NVAs, because this option lets you do the following: 

  * Insert the NVAs with policy-based routes. 
  * Avoid creating rigid topologies.
  * Deploy in a variety of inter-VPC topologies. 
  * Enable autoscaling for the NVAs.
  * Scale to many VPCs over time, without required changes to the NVA interface deployment.



If your design requires multi-NIC, recommendations are detailed in Multi-NIC NVA perimeter security.

To accomplish the traffic steering that's required for NVA deployment, this guide recommends the selective enforcement of policy-based and static routes in the VPC routing tables. The policy-based routes are more flexible than standard routes because policy-based routes match on both source and destination information. These policy-based routes are also enforced only at specific places in the cloud network topology. This granularity allows the definition of very specific traffic steering behavior for very specific connectivity flows.

In addition, this design enables the resiliency mechanisms required by the NVAs. NVAs are fronted by an [internal TCP/UDP load balancer](https://docs.cloud.google.com/load-balancing/docs/internal) to enable NVA redundancy, autoscaling for elastic capacity, and flow symmetry to support stateful bi-directional traffic processing.

### Single-NIC NVA perimeter security

In the design described in [Inter-VPC connectivity for centralized services](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity#inter-vpc-connectivity-for-centralized-services), the transit VPC acts as a hub to the spoke VPCs that are connected by using VPC Network Peering and HA VPN. The transit VPC also enables connectivity between the external networks and the spoke VPCs. 

For the purpose of single-NIC NVA insertion, this design combines the following two patterns:

  * Insert NVAs at a VPC Network Peering hub with external hybrid connections
  * Insert NVAs at an HA VPN VPC hub with external hybrid connections



The following diagram shows NVAs inserted at the hubs for VPC Network Peering and HA VPN:

![NVAs inserted at the hubs for VPC Network Peering and HA VPN](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-32.svg)

The preceding diagram illustrates a combined pattern:

  * A transit VPC that hosts the Cloud Interconnect VLAN attachments that provide hybrid or multicloud connectivity. This VPC also contains the single-NIC NVAs that monitor the hybrid connections.
  * Application VPCs connected to the transit VPC over VPC Network Peering.
  * A central services VPC connected to the transit VPC over HA VPN.



In this design the spokes that are connected using HA VPN use the transit VPC to communicate with the spokes that are connected by VPC Network Peering. The communication is steered through the third-party NVA firewalls by using the following combination of passthrough load balancing, static routes, and policy-based routes:

  1. To steer HA VPN traffic to the internal load balancer, apply untagged policy-based routes to the Transit VPC. On these policy-based routes, use source and destination CIDR ranges that provide for traffic symmetry.
  2. To steer incoming traffic to the internal passthrough Network Load Balancer, apply policy-based routes to the Cloud Interconnect connections in the Transit VPC. These are regional routes.
  3. So that traffic leaving the NVA doesn't get routed directly back to the NVA, make all NVA interfaces the target of a [skip-policy-based route](https://docs.cloud.google.com/vpc/docs/policy-based-routes#skip-option) to skip other policy-based routes. Traffic then follows the VPC routing table once it has been processed by the NVAs.
  4. To steer traffic to the NVA internal load balancers in the Transit VPC, apply static routes to the application VPCs. These can be scoped regionally using network tags.



### Multi-NIC NVA perimeter security

In multi-NIC mode, the topology is more static because NVAs bridge the connectivity between the different VPCs in which the different network interfaces reside.

When interface-based zones are required in a firewall, the following multi-NIC design enables the required external connectivity. This design assigns different firewall interfaces to the external networks. The external networks are referred to by security practitioners as untrusted networks and the internal networks are known as trusted networks. For the multi-NIC NVA deployment, this design is implemented using trusted and untrusted VPCs.

For internal communications, firewalling can be enforced using a single-NIC insertion model that corresponds to a CIDR-based zone model.

In this design, you insert NVAs by configuring the following:

  1. To steer HA VPN traffic to the internal load balancer, apply untagged policy-based routes to the trusted VPC. On these policy-based routes, use source and destination CIDR ranges that provide for traffic symmetry.
  2. To steer incoming traffic to the internal passthrough Network Load Balancer, apply policy-based routes to the Cloud Interconnect connections in the untrusted VPC. These are regional routes.
  3. So that traffic leaving the NVA doesn't get routed directly back to the NVA, make all NVA interfaces the target of a [skip-policy-based route](https://docs.cloud.google.com/vpc/docs/policy-based-routes#skip-option) to skip other policy-based routes. Traffic then follows the VPC routing table once it has been processed by the NVAs.
  4. To steer traffic to the NVA internal load balancers in the trusted VPC, apply static routes to the application VPCs. These can be scoped regionally using network tags.



The following diagram shows multi-NIC NVAs inserted between the untrusted and trusted VPC networks in the hub project:

![NVAs for internal communication](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-35.svg)

## What's next

  * Learn more about the Google Cloud products used in this design guide: 
    * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)
    * [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)
    * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)
    * [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * For more reference architectures, design guides, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture).



## Contributors

Authors: 

  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking
  * [Ghaleb Al-habian](https://www.linkedin.com/in/galhabian) | Network Specialist
  * Deepak Michael | Networking Specialist Customer Engineer
  * [Osvaldo Costa](https://www.linkedin.com/in/osvaldocostajr) | Networking Specialist Customer Engineer
  * [Jonathan Almaleh](https://www.linkedin.com/in/jonathan-almaleh) | Staff Technical Solutions Consultant



Other contributors: 

  * [Zach Seils](https://www.linkedin.com/in/zachseils) | Networking Specialist
  * [Christopher Abraham](https://www.linkedin.com/in/christopher-abraham-33291b) | Networking Specialist Customer Engineer
  * [Emanuele Mazza](https://www.linkedin.com/in/emanuelemazza) | Networking Product Specialist
  * [Aurélien Legrand](https://www.linkedin.com/in/aurelienlegrand) | Strategic Cloud Engineer
  * [Eric Yu](https://www.linkedin.com/in/eyu719) | Networking Specialist Customer Engineer
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer
  * [Ammett Williams](https://www.linkedin.com/in/ammett) | Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-30 UTC."],[],[]] 
