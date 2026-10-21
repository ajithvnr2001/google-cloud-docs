---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/meshed-pattern/
title: Meshed pattern \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:45.972360+00:00
---

# Meshed pattern  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/meshed-pattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Meshed pattern Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

The _meshed_ pattern is based on establishing a hybrid network architecture. That architecture spans multiple computing environments. In these environments, all systems can communicate with one another and aren't limited to one-way communication based on the security requirements of your applications. This networking pattern applies primarily to [_tiered hybrid_](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern), [_partitioned multicloud_](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern), or [_bursting_](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/cloud-bursting-pattern) architectures. It's also applicable to [business continuity](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/business-continuity-patterns) design to provision a disaster recovery (DR) environment in Google Cloud. In all cases, it requires that you connect computing environments in a way that align with the following communication requirements:

  * Workloads can communicate with one another across environment boundaries using private RFC 1918 IP addresses.
  * Communication can be initiated from either side. The specifics of the communications model can vary based on the applications and security requirements, such as the communication models discussed in the design options that follow.
  * The firewall rules that you use must allow traffic between specific IP address sources and destinations based on the requirements of the application, or applications, for which the pattern is designed. Ideally, you can use a multi-layered security approach to restrict traffic flows in a fine-grained fashion, both between and within computing environments.



## Architecture

The following diagram illustrates a high level reference architecture of the _meshed_ pattern.

![Data in a hybrid network architecture flows from two subnets in Google Cloud to a workload in an on-premises environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/mesh.svg)

  * All environments should use an overlap-free RFC 1918 IP address space.
  * On the Google Cloud side, you can deploy workloads into a single or multiple shared VPCs or non-shared VPCs. For other possible design options of this pattern, refer to the design variations that follow. The selected structure of your VPCs should align with the projects and [resources hierarchy design](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy) of your organization.
  * The VPC network of Google Cloud extends to other computing environments. Those environments can be on-premises or in another cloud. Use one of the [hybrid and multicloud networking connectivity](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/design-considerations#hybrid_and_multicloud_connectivity) options that meet your business and application requirements.
  * Limit communications to only the allowed IP addresses of your sources and destinations. Use any of the following capabilities, or a combination of them:

    * [Firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) or [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).

    * Network virtual appliance (NVA) with next generation firewall (NGFW) inspection capabilities, placed in the network path.

    * [Cloud Next Generation Firewall Enterprise](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention) with intrusion prevention service (IPS) to implement deep packet inspection for threat prevention without changing the network design or routing.




## Variations

The _meshed_ architecture pattern can be combined with other approaches to meet different design requirements, while still considering the communication requirements of the pattern. The pattern options are described in the following sections:

  * One VPC per environment
  * Use a centralized application layer firewall
  * Microservices zero trust distributed architecture



### One VPC per environment

The common reasons to consider the one-VPC-per-environment option are as follows:

  * The cloud environment requires network-level separation of the VPC networks and resources, in alignment with your organization's [resource hierarchy design](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy). If administrative domain separation is required, it can also be combined with a separate project per environment. 
    * To centrally manage network resources in a common network and provide network isolation between the different environments, use a [shared VPC for each environment](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-1) that you have in Google Cloud, such as development, testing, and production.
  * Scale requirements that might need to go beyond the [VPC quotas](https://docs.cloud.google.com/vpc/docs/quota) for a single VPC or project.



As illustrated in the following diagram, the one-VPC-per-environment design lets each VPC integrate directly with the on-premises environment or other cloud environments using VPNs, or a Cloud Interconnect with multiple [VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments).

![Data in a hybrid network architecture with one VPC in each environment flows from two subnets in Google Cloud to a workload in an on-premises environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/mesh-vpc.svg)

The pattern displayed in the preceding diagram can be applied on a landing zone [hub-and-spoke network topology](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-3). In that topology, a single (or multiple) hybrid connection can be shared with all spoke VPCs. It's shared by using a transit VPC to terminate both the hybrid connectivity and the other spoke VPCs. You can also expand this design by adding NVA with next-generation firewall (NGFW) inspection capabilities at the transit VPC, as described in the next section, "Use a centralized application layer firewall."

### Use a centralized application layer firewall

If your technical requirements mandate considering application layer (Layer 7) and deep packet inspection with advanced firewalling capabilities that exceed the capabilities of Cloud Next Generation Firewall, you can use an NGFW appliance hosted in an NVA. However, that NVA must meet the security needs of your organization. To implement these mechanisms, you can extend the topology to pass all cross-environment traffic through a centralized NVA firewall, as shown in the following diagram.

You can apply the pattern in the following diagram on the landing zone design by using a [hub-and-spoke topology with centralized appliances](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-2):

![Data from two shared VPCs in Google Cloud flow through an NVA to a transit VPC network over to a workload in an on-premises environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/mesh-centralized.svg)

As shown in the preceding diagram, The NVA acts as the perimeter security layer and serves as the foundation for enabling inline traffic inspection. It also enforces strict access control policies. To inspect both east-west and north-south traffic flows, the design of a centralized NVA might include multiple segments with different levels of security access controls.

### Microservices zero trust distributed architecture

When containerized applications are used, the microservices zero trust distributed architecture discussed in the [_mirrored_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/mirrored-pattern) section is also applicable to this architecture pattern.

The key difference between this pattern and the mirrored pattern is that the communication model between workloads in Google Cloud and other environments can be initiated from either side. Traffic must be controlled and fine-grained, based on the application requirements and security requirements using [Cloud Service Mesh](https://cloud.google.com/products/service-mesh).

## Meshed pattern best practices

  * Before you do anything else, decide on your [resource hierarchy design](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy), and the design required to support any project and VPC. Doing so can help you select the optimal networking architecture that aligns with the structure of your Google Cloud projects.
  * Use a [zero trust distributed architecture](https://docs.cloud.google.com/architecture/network-hybrid-multicloud#zero_trust_distributed_architecture) when using Kubernetes within your private computing environment and Google Cloud.
  * When you use centralized NVAs in your design, you should define multiple segments with different levels of security access controls and traffic inspection policies. Base these controls and policies on the security requirements of your applications.
  * When designing a solution that includes NVAs, it's important to consider the high availability (HA) of the NVAs to avoid a single point of failure that could block all communication. Follow the HA and redundancy design and implementation guidance provided by the [Google Cloud security vendor](https://cloud.google.com/security/partners) that supplies your NVAs.
  * To provide increased privacy, data integrity, and a controlled communication model, expose applications through APIs using API gateways, like [Apigee](https://docs.cloud.google.com/apigee) and [Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/what-is-hybrid) with end-to-end mTLS. You can also use a shared [VPC with Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs#configuring-shared-vpc-with-apigee) in the same [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) resource.
  * If the design of your solution requires exposing a Google Cloud based application to the public internet, consider the design recommendations discussed in [Networking for internet-facing application delivery](https://docs.cloud.google.com/architecture/network-application-delivery).
  * To help protect Google Cloud services in your projects, and to help mitigate the risk of data exfiltration, use VPC Service Controls to specify service perimeters at the project or VPC network level. Also, you can [extend service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/overview#hybrid_access)to a hybrid environment over an authorized VPN or Cloud Interconnect. For more information about the benefits of service perimeters, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * Review the [general best practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices) for hybrid and multicloud networking patterns.



If you intend to enforce stricter isolation and more fine-grained access between your applications hosted in Google Cloud, and in other environments, consider using one of the [_gated_ patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-patterns) that are discussed in the other documents in this series.

[ Previous arrow_back  Mirrored pattern  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/mirrored-pattern)

[ Next Gated patterns  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-patterns)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
