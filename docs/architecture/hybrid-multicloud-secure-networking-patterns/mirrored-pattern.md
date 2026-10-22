---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/mirrored-pattern/
title: Mirrored pattern \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:25.646496+00:00
---

# Mirrored pattern  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/mirrored-pattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Mirrored pattern Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

The _mirrored_ pattern is based on replicating the design of a certain existing environment or environments to a new environment or environments. Therefore, this pattern applies primarily to architectures that follow the [_environment hybrid_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/environment-hybrid-pattern). In that pattern, you run your development and testing workloads in one environment while you run your staging and production workloads in another.

The mirrored pattern assumes that testing and production workloads aren't supposed to communicate directly with one another. However, it should be possible to manage and deploy both groups of workloads in a consistent manner.

If you use this pattern, connect the two computing environments in a way that aligns with the following requirements:

  * Continuous integration/continuous deployment (CI/CD) can deploy and manage workloads across all computing environments or specific environments.
  * Monitoring, configuration management, and other administrative systems should work across computing environments.
  * Workloads can't communicate directly across computing environments. If necessary, communication has to be in a fine-grained and controlled fashion.



## Architecture

The following architecture diagram shows a high level reference architecture of this pattern that supports CI/CD, Monitoring, configuration management, other administrative systems, and workload communication:

![Data flows between a CI/CD and an admin VPC in Google Cloud and an on-premises production environment. Data also flows between the CI/CD-VPC and development and testing environments within Google Cloud.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/mirrored.svg)

The description of the architecture in the preceding diagram is as follows:

  * Workloads are distributed based on the functional environments (development, testing, CI/CD and administrative tooling) across separate VPCs on the Google Cloud side.
  * [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) is used for development and testing workloads. An extra VPC is used for the CI/CD and administrative tooling. With shared VPCs: 
    * The applications are managed by different teams per environment and per service project.
    * The host project administers and controls the network communication and security controls between the development and test environments—as well as to outside the VPC.
  * CI/CD VPC is connected to the network running the production workloads in your private computing environment.
  * Firewall rules permit only allowed traffic. 
    * You might also use [Cloud Next Generation Firewall Enterprise](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention) with intrusion prevention service (IPS) to implement deep packet inspection for threat prevention without changing the design or routing. Cloud Next Generation Firewall Enterprise works by creating Google-managed zonal firewall endpoints that use packet intercept technology to transparently inspect the workloads for the configured threat signatures. It also protects workloads against threats.
  * Enables communication among the peered VPCs using internal IP addresses. 
    * The peering in this pattern allows CI/CD and administrative systems to deploy and manage development and testing workloads.
  * Consider these [general best practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices).



You establish this CI/CD connection by using one of the discussed [hybrid and multicloud networking connectivity options](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/design-considerations#hybrid_and_multicloud_connectivity) that meet your business and applications requirements. To let you deploy and manage production workloads, this connection provides private network reachability between the different computing environments. All environments should have overlap-free RFC 1918 IP address space.

If the instances in the development and testing environments require internet access, consider the following options:

  * You can deploy [Cloud NAT](https://docs.cloud.google.com/nat/docs) into the same Shared VPC host project network. Deploying into the same Shared VPC host project network helps to avoid making these instances directly accessible from the internet.
  * For outbound web traffic, you can use [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview). The proxy offers [several benefits](https://docs.cloud.google.com/secure-web-proxy/docs/overview#benefits).



For more information about the Google Cloud tools and capabilities that help you to build, test, and deploy in Google Cloud and across hybrid and multicloud environments, see the [DevOps and CI/CD on Google Cloud explained](https://cloud.google.com/blog/topics/developers-practitioners/devops-and-cicd-google-cloud-explained) blog.

## Variations

To meet different design requirements, while still considering all communication requirements, the _mirrored_ architecture pattern offers these options, which are described in the following sections:

  * Shared VPC per environment
  * Centralized application layer firewall
  * Hub-and-spoke topology
  * Microservices zero trust distributed architecture



### Shared VPC per environment

The shared VPC per environment design option allows for application- or service-level separation across environments, including CI/CD and administrative tools that might be required to meet certain organizational security requirements. These requirements limit communication, administrative domain, and access control for different services that also need to be managed by different teams.

This design achieves separation by providing network- and project-level isolation between the different environments, which enables more fine-grained communication and [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) access control.

From a management and operations perspective, this design provides the flexibility to manage the applications and workloads created by different teams per environment and per service project. VPC networking, and its security features can be provisioned and managed by networking operations teams based on the following possible structures:

  * One team manages all host projects across all environments.
  * Different teams manage the host projects in their respective environments.



Decisions about managing host projects should be based on the team structure, security operations, and access requirements of each team. You can apply this design variation to the [Shared VPC network for each environment landing zone design option](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-1). However, you need to consider the communication requirements of the _mirrored_ pattern to define what communication is allowed between the different environments, including communication over the hybrid network.

You can also provision a Shared VPC network for each main environment, as illustrated in the following diagram:

![VPC peering in Google Cloud shares data between development and test environments and CI/CD and administrative subnets. The subnets share data between Google Cloud and an on-premises environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/mirrored-shared.svg)

### Centralized application layer firewall

In some scenarios, the security requirements might mandate the consideration of application layer (Layer 7) and deep packet inspection with advanced firewalling mechanisms that exceed the capabilities of Cloud Next Generation Firewall. To meet the security requirements and standards of your organization, you can use an NGFW appliance [hosted in a network virtual appliance (NVA)](https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access#network_virtual_appliance). Several Google Cloud [security partners](https://cloud.google.com/security/partners) offer options well suited to this task.

As illustrated in the following diagram, you can place the NVA in the network path between Virtual Private Cloud and the private computing environment using [multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

![VPC peering in Google Cloud shares data between development and test environments and CI/CD and administrative subnets. The subnets share data between Google Cloud and an on-premises environment through a transit VPC network.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/mirrored-centralized1.svg)

This design also can be used with multiple shared VPCs as illustrated in the following diagram.

![VPC peering in Google Cloud shares data between development and test environments and CI/CD and administrative subnets. The subnets use an NVA to share data between Google Cloud and an on-premises environment through a transit VPC network.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/mirrored-centralized2.svg)

The NVA in this design acts as the perimeter security layer. It also serves as the foundation for enabling inline traffic inspection and enforcing strict access control policies.

For a robust multilayer security strategy that includes VPC firewall rules and intrusion prevention service capabilities, include further traffic inspection and security control to both east-west and north-south traffic flows.

**Note:** In supported cloud [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones), and when technically feasible for your design, NVAs can be deployed without requiring multiple VPC networks or appliance interfaces. This deployment is based on using load balancing and [policy-based routing](https://docs.cloud.google.com/vpc/docs/policy-based-routes) capabilities. These capabilities enable a topology-independent, policy-driven mechanism for integrating NVAs into your cloud network. For more details, see [Deploy network virtual appliances (NVAs) without multiple VPCs](https://cloud.google.com/blog/products/networking/policy-based-routing-network-patterns-for-virtual-appliances).

### Hub-and-spoke topology

Another possible design variation is to use separate VPCs (including shared VPCs) for your development and different testing stages. In this variation, as shown in the following diagram, all stage environments connect with the CI/CD and administrative VPC in a hub-and-spoke architecture. Use this option if you must separate the administrative domains and the functions in each environment. The hub-and-spoke communication model can help with the following requirements:

  * Applications need to access a common set of services, like monitoring, configuration management tools, CI/CD, or authentication.
  * A common set of security policies needs to be applied to inbound and outbound traffic in a centralized manner through the hub.



For more information about hub-and-spoke design options, see [Hub-and-spoke topology with centralized appliances](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-2) and [Hub-and-spoke topology without centralized appliances](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-3).

![Development and test environments share data with a hub VPC CI/CD and an admin VPC to an on-premises environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/mirrored-hub.svg)

As shown in the preceding diagram, the inter-VPC communication and hybrid connectivity all pass through the hub VPC. As part of this pattern, you can control and restrict the communication at the hub VPC to align with your connectivity requirements.

As part of the hub-and-spoke network architecture the following are the primary connectivity options (between the spokes and hub VPCs) on Google Cloud:

  * VPC Network Peering
  * VPN
  * Using network virtual appliance (NVA) 
    * With multiple network interfaces
    * With [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connect-vpc-networks) (NCC)



For more information on which option you should consider in your design, see [Hub-and-spoke network architecture](https://docs.cloud.google.com/architecture/deploy-hub-spoke-vpc-network-topology). A key influencing factor for selecting VPN over VPC peering between the spokes and the hub VPC is when [traffic transitivity](https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access#hub_and_spoke_with_transitivity) is required. Traffic transitivity means that traffic from a spoke can reach other spokes through the hub.

### Microservices zero trust distributed architecture

Hybrid and multicloud architectures can require [multiple clusters](https://docs.cloud.google.com/anthos/fleet-management/docs/multi-cluster-use-cases) to achieve their technical and business objectives, including separating the production environment from the development and testing environments. Therefore, network perimeter security controls are important, especially when they're required to comply with certain security requirements.

It's not enough to support the security requirements of current cloud-first distributed microservices architectures, you should also consider zero trust distributed architectures. The microservices zero trust distributed architecture supports your microservices architecture with microservice level security policy enforcement, authentication, and workload identity. Trust is [identity-based](https://docs.cloud.google.com/service-mesh/docs/security/security-overview#mutual_tls) and enforced for each service.

By using a distributed proxy architecture, such as a service mesh, services can effectively validate callers and implement fine-grained access control policies for each request, enabling a more secure and scalable microservices environment. [Cloud Service Mesh](https://cloud.google.com/products/service-mesh) gives you the flexibility to have a common mesh that can span your Google Cloud and on-premises deployments. The mesh uses authorization policies to help secure service-to-service communications.

You might also incorporate [Apigee Adapter for Envoy](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/concepts), which is a lightweight Apigee API gateway deployment within a Kubernetes cluster, with this architecture. Apigee Adapter for Envoy is an open source edge and service proxy that's designed for cloud-first applications.

![Data flows between services in Google Cloud and an on-premises environment through a distributed proxy architecture.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/mirrored-mztda.svg)

For more information about this topic, see the following articles:

  * [Zero Trust Distributed Architecture](https://docs.cloud.google.com/architecture/network-hybrid-multicloud#zero_trust_distributed_architecture)
  * [Google Kubernetes Engine (GKE) hybrid environment](https://docs.cloud.google.com/anthos/docs/architecture/anthos-hybrid-environment)
  * [Connect to Google](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/concepts/connect-on-prem-gcp)
    * Connect an on-premises cluster to a Google Cloud network.
  * [Set up a multicloud or hybrid mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/multi-cloud-hybrid-mesh)
    * Deploy Cloud Service Mesh across environments and clusters.



## Mirrored pattern best practices

  * The CI/CD systems required for deploying or reconfiguring production deployments must be highly available, meaning that all architecture components must be designed to provide the expected level of system availability. For more information, see [Google Cloud infrastructure reliability](https://docs.cloud.google.com/architecture/infra-reliability-guide).
  * To eliminate configuration errors for repeated processes like code updates, automation is essential to standardize your builds, tests, and deployments.
  * The integration of centralized NVAs in this design might require the incorporation of multiple segments with varying levels of security access controls.
  * When designing a solution that includes NVAs, it's important to consider the high availability (HA) of the NVAs to avoid a single point of failure that could block all communication. Follow the HA and redundancy design and implementation guidance provided by your NVA vendor.
  * By not exporting on-premises IP routes over VPC peering or VPN to the development and testing VPC, you can restrict network reachability from development and testing environments to the on-premises environment. For more information, see [VPC Network Peering custom route exchange](https://docs.cloud.google.com/vpc/docs/vpc-peering#custom-route-exchange).
  * For workloads with private IP addressing that can require Google's APIs access, you can expose [Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#supported-apis) by using a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect) within a VPC network. For more information, see [_Gated ingress_](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress), in this series.
  * Review the [general best practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices) for hybrid and multicloud networking architecture patterns.



[ Previous arrow_back  Architecture patterns  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/architecture-patterns)

[ Next Meshed pattern  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/meshed-pattern)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
