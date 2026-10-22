---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/design-considerations/
title: Design considerations \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:07.690370+00:00
---

# Design considerations  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/design-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Design considerations Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

When designing a hybrid and multicloud network, various factors influence your architectural choices. As you analyze your hybrid and multicloud networking design, think about the following design considerations. To build a cohesive architecture, assess these considerations collectively, not in isolation.

## Hybrid and multicloud connectivity

[Hybrid and multicloud connectivity](https://cloud.google.com/hybrid-connectivity) refers to the communication connections that link on-premises, Google Cloud, and other cloud environments. Choosing the right connectivity method is essential to the success of hybrid and multicloud architectures, because these connections carry all inter-environment traffic. Any network performance issues, such as bandwidth, latency, packet loss, or jitter, can directly affect the performance of business applications and services.

For the connectivity between an on-premises environment and Google Cloud or other clouds, Google Cloud offers multiple [connectivity options](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product) to select from, including:

  * Internet-based connectivity using public IP addresses:

    * Transfer data between Google Cloud and an on-premises environment or another cloud environment over the internet. This option uses the public external IP addresses of an instance—ideally with application layer [encryption in transit](https://docs.cloud.google.com/architecture/landing-zones/decide-security#option-2-require-layer7).

    * Secure connectivity over APIs with Transport Layer Security (TLS) encryption over the public internet. This option requires the application or target APIs to be publicly reachable from the internet and that the application performs the [encryption in transit](https://docs.cloud.google.com/architecture/landing-zones/decide-security#option-2-require-layer7).

  * Private secure connectivity over the public internet using either [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or customer-managed VPN gateways. This option includes using a network virtual appliance (NVA) including software-defined WAN (SD-WAN) solutions from Google Cloud partners. These solutions are available on [Google Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs).

  * Private connectivity over a private transport using Cloud Interconnect ([Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) or [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview)) that offers a more deterministic performance and has an [SLA](https://cloud.google.com/network-connectivity/docs/interconnect/sla). If encryption in transit is required at the network connectivity layer, you can use [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) or [MACsec for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview).

  * [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) provides enterprises that use multicloud environments the ability to enable private and secure connectivity across clouds (between Google Cloud and [supported cloud service providers](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#supported-cloud-service-providers) in certain [locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#locations)). This option has line-rate performance with [high availability options](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#service-level-agreement) of 99.9% and 99.99%, which ultimately helps to lower total cost of ownership (TCO) without the complexity and cost of managing infrastructure. Also, if encryption in transit is required at the network connectivity layer for additional security, Cross-Cloud Interconnect supports [MACsec for Cloud Interconnect encryption](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#encryption).




Consider using [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) when it fits your cloud solution architecture [use case](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#use_cases). NCC is an orchestration framework that provides network connectivity among [spoke resources](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#supported-spoke-resources), like Virtual Private Cloud (VPC) networks, router appliances, or hybrid connections that are connected to a central management resource called a hub. A NCC hub supports either VPC spokes or hybrid spokes. For more information, see [Route exchange with VPC connectivity](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#hybrid-with-vpc-connectivity). Also, to facilitate route exchange with the Cloud Router instance, NCC enables the integration of [third-party network virtual appliances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview). That integration includes third-party SD-WAN routers that are [supported by Google Cloud NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).

With the variety of hybrid and multicloud connectivity options available, selecting the most suitable one requires a thorough evaluation of your business and technical requirements. These requirements include the following factors:

  * Network performance
  * Security
  * Cost
  * Reliability and SLA
  * Scalability



For more information on selecting a connectivity option to Google Cloud, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product). For guidance on selecting a network connectivity option that meets the needs of your multicloud architecture, see [Patterns for connecting other cloud service providers with Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-connecting-other-csps-with-gcp).

## Google Cloud projects and VPC networks

You can use the networking architecture patterns discussed in this guide with either single or multiple projects where supported. A [project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) in Google Cloud contains related services and workloads that have a single administrative domain. Projects form the basis for the following processes:

  * Creating, enabling, and using Google Cloud services
  * Managing services APIs
  * Enabling billing
  * Adding and removing collaborators
  * Managing permissions



A project can contain one or more VPC networks. Your organization, or the structure of the applications you use in a project, should determine whether to use a single project or multiple projects. Your organization, or the structure of the applications, should also determine how to use VPCs. For more information, see [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).

The following factors can influence whether you decide to use a single VPC, multiple VPCs, or a [shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) with one or multiple projects:

  * Organizational resource hierarchies.
  * Network traffic, communication, and administrative domain requirements between workloads.
  * Security requirements. 
    * Security requirements can require Layer 7 firewall inspection by third-party NVAs located in the path between certain networks or applications.
  * Resource management. 
    * Enterprises that use an administrative model where the network operation team manages networking resources, can require workload separation at the team level.
  * VPC use decisions.

    * Using shared VPC networks across multiple Google Cloud projects avoids the need to maintain many individual VPC networks per workload or per team.
    * Using shared VPC networks enables centralized management for host VPC networking, including the following technical factors: 
      * Peering configuration
      * Subnet configuration
      * Cloud Firewall configuration
      * Permission configuration

Sometimes, you might need to use more than one VPC (or shared VPC) network to meet scale requirements without exceeding the [limits](https://docs.cloud.google.com/vpc/docs/quota) of resources for a single VPC.

For more information, see [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs).




## DNS resolution

In a hybrid and multicloud architecture, it's essential that the domain name system (DNS) is extended and integrated between environments where communication is permitted. This action helps to provide seamless communication between various services and applications. It also maintains private DNS resolution between these environments.

In a hybrid and multicloud architecture with Google Cloud, you can use [DNS peering](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones) and [DNS forwarding](https://docs.cloud.google.com/dns/docs/overview#dns-forwarding-methods) capabilities to enable the DNS integration between different environments. With these DNS capabilities, you can cover the different use cases that can align with different networking communication models. Technically, you can use [DNS forwarding zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding_zones) to query on-premises DNS servers and inbound [DNS server policies](https://docs.cloud.google.com/dns/docs/server-policies-overview) to allow queries from on-premises environments. You can also use [DNS peering](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones) to forward DNS requests within Google Cloud environments.

For more information, see [Best practices for Cloud DNS](https://docs.cloud.google.com/dns/docs/best-practices) and reference architectures for hybrid DNS with Google Cloud.

To learn about redundancy mechanisms for maintaining Cloud DNS availability in a hybrid setup, see [It's not DNS: Ensuring high availability in a hybrid cloud environment](https://cloud.google.com/blog/products/networking/create-a-highly-available-hybrid-cloud-dns-configuration). Also watch this demonstration of how to design and set up a [multicloud private DNS](https://www.youtube.com/watch?v=hOUlt9Nylq8) between AWS and Google Cloud.

## Cloud network security

[Cloud network security](https://cloud.google.com/learn/what-is-cloud-network-security#section-3) is a foundational layer of cloud security. To help manage the risks of the dissolving network perimeter, it enables enterprises to embed security monitoring, threat prevention, and network security controls.

A standard on-premises approach to network security is primarily based on a distinct perimeter between the internet edge and the internal network of an organization. It uses various multi-layered security preventive systems in the network path, like physical firewalls, routers, intrusion detection systems, and others.

With cloud-based computing, this approach is still applicable in certain use cases. But it's not enough to handle the scale and the distributed and dynamic nature of cloud workloads—such as autoscaling and containerized workloads—by itself. The cloud network security approach helps you minimize risk, meet compliance requirements, and ensure safe and efficient operations though several cloud-first capabilities. For more information, see [Cloud network security benefits](https://cloud.google.com/learn/what-is-cloud-network-security#section-5). To secure your network, also look at [Cloud network security challenges](https://cloud.google.com/learn/what-is-cloud-network-security#section-6), and general [Cloud network security best practices](https://cloud.google.com/learn/what-is-cloud-network-security#section-7).

Adopting a hybrid cloud architecture calls for a security strategy that [goes beyond replicating the on-premises approach](https://docs.cloud.google.com/architecture/blueprints/security-foundations#starting_off_with_security_in_mind). Replicating that approach can limit design flexibility. It can also potentially expose the cloud environment to security threats. Instead, you should first identify the available cloud-first network security capabilities that meet the security requirements of your company. You might also need to combine these capabilities with third-party security solutions from Google Cloud technology partners, like network virtual appliances.

To design a consistent architecture across environments in a multicloud architecture, it's important to identify the different services and capabilities offered by each cloud provider. We recommend, in all cases, that you use a unified security posture that has visibility across all environments.

To protect your _hybrid cloud_ architecture environments, you should also consider using [defense-in-depth principles](https://cloud.google.com/blog/products/networking/google-cloud-networking-in-depth-three-defense-in-depth-principles-for-securing-your-environment).

Finally, design your cloud solution with network security in mind from the start. Incorporate all required capabilities as part of your initial design. This initial work will help you avoid the need to make major changes to the design to integrate security capabilities later in your design process.

However, cloud security isn't limited to networking security. It must be applied throughout the entire application development lifecycle across the entire application stack, from development to production and operation. Ideally, you should use multiple layers of protection (the defense-in-depth approach) and security visibility tools. For more information on how to architect and operate secure services on Google Cloud, see the [Security, privacy, and compliance pillar](https://docs.cloud.google.com/architecture/framework/security) of the Google Cloud Well-Architected Framework.

To protect your valuable data and infrastructure from a wide range of threats, adopt a comprehensive approach to cloud security. To stay ahead of existing threats, continuously assess and refine your security strategy.

[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns)

[ Next Architecture patterns  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/architecture-patterns)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
