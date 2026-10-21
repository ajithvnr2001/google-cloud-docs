---
url: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/
title: Cross-Cloud Network for distributed applications \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:21.989662+00:00
---

# Cross-Cloud Network for distributed applications  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Cross-Cloud Network for distributed applications Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-30 UTC

Cross-Cloud Network enables an architecture for the assembly of distributed applications. Cross-Cloud Network lets you distribute workloads and services across multiple cloud and on-premises networks. This solution provides application developers and operators the experience of a single cloud across multiple clouds. This solution uses and also expands the [established uses of hybrid and multicloud networking](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns).

This guide is intended for network architects and engineers who want to design and build distributed applications on Cross-Cloud Network. This guide provides you with a comprehensive understanding of Cross-Cloud Network design considerations.

This design guide is a series that includes the following documents:

  * Cross-Cloud Network design for distributed applications (this document)
  * [Network segmentation and connectivity for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity)
  * [Service networking for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/service-networking)
  * [Network security for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/security)



The architecture supports regional and global application stacks, and it's organized in the following functional layers:

  * **Network segmentation and connectivity** : involves the Virtual Private Cloud (VPC) segmentation structure and IP connectivity across VPCs and to external networks.
  * **Service networking** : involves the deployment of application services, which are load balanced and made available across projects and organizations.
  * **Network security** : enables the enforcement of security for intra-cloud and inter-cloud communications, using both built-in cloud security and network virtual appliances (NVAs).



## Network segmentation and connectivity

Segmentation structure and connectivity is the foundation of the design. The following diagram shows a VPC segmentation structure, which you can implement by using either a consolidated or segmented infrastructure. This diagram doesn't show the connections between the networks.

![VPC segmentation structure for Cross-Cloud Network design](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-1a.svg)

This structure includes the following components:

  * **Transit VPC** : Handles external network connections and routing policies. This VPC can also provide connectivity between other VPCs.
  * **Services access VPCs** : Contain access points to different services. The service access points in these VPCs can be reached from other networks.
  * **Managed services VPCs** : Contain services produced by other entities. The services are made accessible to applications running in VPC networks by using Private Service Connect or private services access.
  * **Application VPCs** : Contain the workloads that make up the software services that your organization creates and hosts itself.



Your choice of segmentation structure for the application VPCs depends on the scale of application VPCs required, whether you plan to deploy perimeter firewalls in Cross-Cloud Network or externally, and the choice of central or distributed service publication.

Cross-Cloud Network supports the deployment of regional application stacks and global application stacks. Both of these application resiliency archetypes are supported by the proposed segmentation structure with the inter-VPC connectivity pattern.

You can achieve inter-VPC connectivity with Network Connectivity Center or by using a combination of VPC Network Peering and HA VPN hub-and-spoke patterns.

The design of the DNS infrastructure is also defined in the context of the segmentation structure, independent of the connectivity pattern.

## Service networking

Different application [deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes) lead to different patterns for service networking. For Cross-Cloud Network design, focus on the [Multi-regional deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional), in which an application stack runs independently in multiple zones across two or more Google Cloud regions.

A multi-regional deployment archetype has the following features that are useful for Cross-Cloud Network design:

  * You can use DNS routing policies to route incoming traffic to the regional load balancers.
  * The regional load balancers can then distribute the traffic to the application stack.
  * You can implement regional failover by re-anchoring the DNS mappings of the application stack with a [DNS failover routing policy](https://docs.cloud.google.com/dns/docs/policies-overview#failover-policy).



An alternative to the multi-regional deployment archetype would be the [global deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/global), in which a single stack is built on global load balancers and spans multiple regions. Consider the following features of this archetype when working with Cross-Cloud Network design:

  * The load balancers distribute traffic to the region that's nearest to the user.
  * The internet-facing frontends are global, but the internal-facing frontends are regional with global access, so you can reach them in failover scenarios.
  * You can use geolocation DNS routing policies and DNS health checks on the internal service layers of the application stack.



How you provide access to managed published services depends on the service that needs to be reached. The different private reachability models are modularized and orthogonal to the design of the application stack.

Depending on the service, you can use Private Service Connect or private services access for private access. You can build an application stack by combining built-in services and services published by other organizations. The service stacks can be regional or global to meet your required level of resiliency and optimized access latency.

## Network security

For workload security, we recommend that you use [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) from Google Cloud.

If your organization requires additional advanced capabilities to meet security or compliance requirements, you can incorporate perimeter security firewalls by inserting Next-Generation Firewall (NGFW) Network Virtual Appliances (NVAs).

You can insert NGFW NVAs in a single network interface (single-NIC mode) or over multiple network interfaces (multi-NIC mode). The NGFW NVAs can support security zones or Classless Inter-Domain Routing (CIDR)-based perimeter policies. Cross-Cloud Network deploys perimeter NGFW NVAs by using a transit VPC and VPC routing policies.

## What's next

  * Design the [network segmentation and connectivity](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity) for Cross-Cloud Network applications.
  * Learn more about the Google Cloud products used in this design guide: 
    * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)
    * [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc)
    * [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)
    * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect)
    * [Private services access](https://docs.cloud.google.com/vpc/docs/private-services-access)
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
