---
url: https://docs.cloud.google.com/architecture/network-architecture/
title: Designing networks for migrating enterprise workloads: Architectural approaches \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:32.542357+00:00
---

# Designing networks for migrating enterprise workloads: Architectural approaches  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/network-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Designing networks for migrating enterprise workloads: Architectural approaches Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-13 UTC

This document introduces a series that describes networking and security architectures for enterprises that are migrating data center workloads to Google Cloud. These architectures emphasize advanced connectivity, zero-trust security principles, and manageability across a hybrid environment.

As described in an accompanying document, [Architectures for Protecting Cloud Data Planes](https://research.google/pubs/pub51077/), enterprises deploy a spectrum of architectures that factor in connectivity and security needs in the cloud. We classify these architectures into three distinct architectural patterns: lift-and-shift, hybrid services, and zero-trust distributed. The current document considers different security approaches, depending on which architecture an enterprise has chosen. It also describes how to realize those approaches using the building blocks provided by Google Cloud. You should use these security guidances in conjunction with other architectural guidances covering reliability, availability, scale, performance, and governance.

This document is designed to help systems architects, network administrators, and security administrators who are planning to migrate on-premises workloads to the cloud. It assumes the following:

  * You are familiar with data center networking and security concepts.
  * You have existing workloads in your on-premises data center and are familiar with what they do and who their users are.
  * You have at least some workloads that you plan to migrate.
  * You are generally familiar with the concepts described in [Architectures for Protecting Cloud Data Planes](https://research.google/pubs/pub51077/).



The series consists of the following documents:

  * Designing networks for migrating enterprise workloads: Architectural approaches (this document)
  * [Networking for secure intra-cloud access: Reference architectures](https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access)
  * [Networking for internet-facing application delivery: Reference architectures](https://docs.cloud.google.com/architecture/network-application-delivery)
  * [Networking for hybrid and multi-cloud workloads: Reference architectures](https://docs.cloud.google.com/architecture/network-hybrid-multicloud)



This document summarizes the three primary architectural patterns and introduces the resource building blocks that you can use to create your infrastructure. Finally, it describes how to assemble the building blocks into a series of reference architectures that match the patterns. You can use these reference architectures to guide your own architecture.

This document mentions virtual machines (VMs) as examples of workload resources. The information applies to other resources that use VPC networks, like Cloud SQL instances and Google Kubernetes Engine nodes.

## Overview of architectural patterns

Typically, network engineers have focused on building the physical networking infrastructure and security infrastructure in on-premises data centers.

The journey to the cloud has changed this approach because cloud networking constructs are software-defined. In the cloud, application owners have limited control of the underlying infrastructure stack. They need a model that has a secure perimeter and provides isolation for their workloads.

In this series, we consider three common architectural patterns. These patterns build on one another, and they can be seen as a spectrum rather than a strict choice.

### Lift-and-shift pattern

In the lift-and-shift architectural pattern, enterprise application owners migrate their workloads to the cloud without refactoring those workloads. Network and security engineers use Layer 3 and Layer 4 controls to provide protection using a combination of network virtual appliances that mimic on-premises physical devices and cloud firewall rules in the VPC network. Workload owners deploy their services in VPC networks.

### Hybrid services pattern

Workloads that are built using lift-and-shift might need access to cloud services such as BigQuery or Cloud SQL. Typically, access to such cloud services is at Layer 4 and Layer 7. In this context, isolation and security cannot be done strictly at Layer 3. Therefore, service networking and VPC Service Controls are used to provide connectivity and security, based on the identities of the service that's being accessed and the service that's requesting access. In this model, it's possible to express rich access-control policies.

### Zero-trust distributed pattern

In a zero-trust architecture, enterprise applications extend security enforcement beyond perimeter controls. Inside the perimeter, workloads can communicate with other workloads only if their IAM identity has specific permission, which is denied by default. In a Zero Trust Distributed Architecture, trust is identity-based and enforced for each application. Workloads are built as microservices that have centrally issued identities. That way, services can validate their callers and make policy-based decisions for each request about whether that access is acceptable. This architecture is often implemented using distributed proxies (a service mesh) instead of using centralized gateways.

Enterprises can enforce zero-trust access from users and devices to enterprise applications by configuring Identity-Aware Proxy (IAP). IAP provides identity- and context-based controls for user traffic from the internet or intranet.

### Combining patterns

Enterprises that are building or migrating their business applications to the cloud usually use a combination of all three architectural patterns.

Google Cloud offers a portfolio of products and services that serve as building blocks to implement the cloud data plane that powers the architectural patterns. These building blocks are discussed later in this document. The combination of controls that are provided in the cloud data plane, together with administrative controls to manage cloud resources, form the foundation of an end-to-end security perimeter. The perimeter that's created by this combination lets you govern, deploy, and operate your workloads in the cloud.

## Resource hierarchy and administrative controls

This section presents a summary of the administrative controls that Google Cloud provides as resource containers. The controls include Google Cloud organization resources, folders, and projects that let you group and [hierarchically organize](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) cloud resources. This hierarchical organization provides you with an ownership structure and with anchor points for applying policy and controls.

A Google [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) resource is the root node in the hierarchy and is the foundation for creating deployments in the cloud. An organization resource can have folders and projects as children. A folder has projects or other folders as children. All other cloud resources are the children of projects.

You use [folders](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders) as a method of grouping projects. [Projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) form the basis for creating, enabling, and using all Google Cloud services. Projects let you manage APIs, enable billing, add and remove collaborators, and manage permissions.

Using Google [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview), you can assign roles and define access policies and permissions at all resource hierarchy levels. IAM policies are inherited by resources lower in the hierarchy. These policies can't be altered by resource owners who are lower in the hierarchy. In some cases, the identity and access management is provided at a more granular level, for example at the scope of objects in a namespace or cluster as in [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam).

## Design considerations for Google Virtual Private Cloud networks

When you're designing a migration strategy to the cloud, it's important to develop a strategy for how your enterprise will use VPC networks. You can think of a VPC network as a virtual version of your traditional physical network. It is a completely isolated, private network partition. By default, workloads or services that are deployed in one VPC network cannot communicate with jobs in another VPC network. VPC networks therefore enable workload isolation by forming a security boundary.

Because each VPC network in the cloud is a fully virtual network, each has its own private IP address space. You can therefore use the same IP address in multiple VPC networks without conflict. A typical on-premises deployment might consume a large portion of the RFC 1918 private IP address space. On the other hand, if you have workloads both on-premises and in VPC networks, you can reuse the same address ranges in different VPC networks, as long as those networks aren't [connected](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#google-cloud) or [peered](https://docs.cloud.google.com/vpc/docs/vpc-peering), thus using up IP address space less quickly.

### VPC networks are global

VPC networks in Google Cloud are global, which means that resources deployed in a project that has a VPC network can communicate with each other directly using Google's private backbone.

As figure 1 shows, you can have a VPC network in your project that contains subnetworks in different [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) that span multiple zones. The VMs in any region can communicate privately with each other using the local VPC routes.

![Google Cloud global VPC network implementation with subnetworks configured in different regions.](https://docs.cloud.google.com/static/architecture/images/network-architecture/global-vpc.svg)

**Figure 1.** Google Cloud global VPC network implementation with subnetworks configured in different regions.

### Sharing a network using Shared VPC

[Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) lets an [organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) connect multiple projects to a common [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) so that they can communicate with each other securely using internal IP addresses from the shared network. Network administrators for that shared network apply and enforce centralized control over network resources.

When you use Shared VPC, you designate a project as a host project and attach one or more service projects to it. The VPC networks in the host project are called _Shared VPC networks_. [Eligible resources](https://docs.cloud.google.com/vpc/docs/shared-vpc#resources_that_can_be_attached_to_shared_vpc_networks_from_a_service_project) from service projects can use subnets in the Shared VPC network.

Enterprises typically use Shared VPC networks when they need network and security administrators to centralize management of network resources such as subnets and routes. At the same time, Shared VPC networks let application and development teams create and delete VM instances and deploy workloads in designated subnets using the service projects.

### Isolating environments by using VPC networks

Using VPC networks to isolate environments has a number of advantages, but you need to consider a few disadvantages as well. This section addresses these tradeoffs and describes common patterns for implementing isolation.

#### Reasons to isolate environments

Because VPC networks represent an isolation domain, many enterprises use them to keep environments or business units in separate domains. Common reasons to create VPC-level isolation are the following:

  * An enterprise wants to establish default-deny communications between one VPC network and another, because these networks represent an organizationally meaningful distinction. For more information, see Common VPC network isolation patterns later in this document.
  * An enterprise needs to have overlapping IP address ranges because of pre-existing on-premises environments, because of acquisitions, or because of deployments to other cloud environments.
  * An enterprise wants to delegate full administrative control of a network to a portion of the enterprise.



#### Disadvantages of isolating environments

Creating isolated environments with VPC networks can have some disadvantages. Having multiple VPC networks can increase the administrative overhead of managing the services that span multiple networks. This document discusses techniques that you can use to manage this complexity.

#### Common VPC network isolation patterns

There are some common patterns for isolating VPC networks:

  * **Isolate development, staging, and production environments**. This pattern lets enterprises fully segregate their development, staging, and production environments from each other. In effect, this structure maintains multiple complete copies of applications, with progressive rollout between each environment. In this pattern, VPC networks are used as security boundaries. Developers have a high degree of access to development VPC networks to do their day-to-day work. When development is finished, an engineering production team or a QA team can migrate the changes to a staging environment, where the changes can be tested in an integrated fashion. When the changes are ready to be deployed, they are sent to a production environment.
  * **Isolate business units**. Some enterprises want to impose a high degree of isolation between business units, especially in the case of units that were acquired or ones that demand a high degree of autonomy and isolation. In this pattern, enterprises often create a VPC network for each business unit and delegate control of that VPC to the business unit's administrators. The enterprise uses techniques that are described later in this document to expose services that span the enterprise or to host user-facing applications that span multiple business units.



#### Recommendation for creating isolated environments

We recommend that you design your VPC networks to have the broadest domain that aligns with the administrative and security boundaries of your enterprise. You can achieve additional isolation between workloads that run in the same VPC network by using security controls such as firewalls.

For more information about designing and building an isolation strategy for your organization, see [Best practices and reference architectures for VPC design](https://docs.cloud.google.com/architecture/best-practices-vpc-design) and [Networking](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking) in the Google Cloud enterprise foundations blueprint.

## Building blocks for cloud networking

This section discusses the important building blocks for network connectivity, network security, service networking, and service security. Figure 2 shows how these building blocks relate to one another. You can use one or more of the products that are listed in a given row.

![Building blocks in the realm of cloud network connectivity and security.](https://docs.cloud.google.com/static/architecture/images/network-architecture/network-building-blocks.svg)

**Figure 2**. Building blocks in the realm of cloud network connectivity and security.

The following sections discuss each of the building blocks and which Google Cloud services you can use for each of the blocks.

### Network connectivity

The network connectivity block is at the base of the hierarchy. It's responsible for connecting Google Cloud resources to on-premises data centers or other clouds. Depending on your needs, you might need only one of these products, or you might use all of them to handle different use cases.

#### Cloud VPN

[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) lets you connect your remote branch offices or other cloud providers to Google VPC [networks](https://docs.cloud.google.com/vpc/docs/vpc) through IPsec VPN connections. Traffic traveling between the two networks is encrypted by one VPN gateway and then decrypted by the other VPN gateway, thereby helping to protect data as it traverses the internet.

Cloud VPN lets you connect your on-premises environment and Google Cloud for less cost, but lower bandwidth, than Cloud Interconnect (described in the next section). You can provision an [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#to_peer_vpn_gateways) to meet an SLA requirement of up to 99.99% availability if you have the conforming architecture. For example, Cloud VPN is a good choice for non-mission-critical use cases or for extending connectivity to other cloud providers.

#### Cloud Interconnect

[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) provides enterprise-grade dedicated connectivity to Google Cloud that has higher throughput and more reliable network performance compared to using VPN or internet ingress. [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) provides direct physical connectivity to Google's network from your routers. [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) provides dedicated connectivity through an extensive network of partners, who might offer broader reach or other bandwidth options than Dedicated Interconnect does. [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) provides dedicated direct connectivity from your VPC networks to other cloud providers. [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability) requires that you connect at a colocation facility where Google has a presence, but [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability) does not. Cloud Interconnect ensures that the traffic between your on-premises network or other cloud network and your VPC network doesn't traverse the public internet.

You can provision these Cloud Interconnect connections to meet an SLA requirement of up to 99.99% availability if you provision the appropriate architecture. You can consider using Cloud Interconnect to support workloads that require low latency, high bandwidth, and predictable performance while ensuring that all of your traffic stays private.

#### Network Connectivity Center for hybrid

[NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) provides site-to-site connectivity among your on-premises and other cloud networks. It does this using Google's backbone network to deliver reliable connectivity among your sites.

Additionally, you can extend your existing SD-WAN overlay network to Google Cloud by configuring a VM or a [third-party vendor](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners) [router appliance as a logical spoke attachment](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview).

You can access resources inside the VPC networks using the Router appliance, [VPN](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpn-spoke), or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vlan-spoke) network as spoke attachments. You can use NCC to consolidate connectivity between your on-premises sites, your presences in other clouds, and Google Cloud and manage it all using a single view.

#### NCC for VPC networks

NCC also lets you create a [mesh or star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies) among many VPC networks using [VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview). You can connect the hub to on-premises or other clouds using [NCC hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#hybrid_spokes).

#### VPC Network Peering

[VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) lets you connect Google VPC networks so that workloads in different VPC networks can communicate internally regardless of whether they belong to the same project or to the same organization resource. Traffic stays within Google's network and doesn't traverse the public internet.

VPC Network Peering requires that the networks to be peered don't have overlapping IP addresses.

### Network security

The network security block sits on top of the network connectivity block. It's responsible for allowing or denying access to resources based on the characteristics of IP packets.

#### Cloud NGFW

[Cloud Next Generation Firewall (Cloud NGFW)](https://docs.cloud.google.com/vpc/docs/firewalls) is a distributed firewall service that lets you apply firewall policies at the organization, folder, and network level. Enabled firewall rules are always enforced, protecting your instances regardless of their configuration or the operating system, or even whether the VMs have fully booted. The rules are applied on a per-instance basis, meaning that the rules protect connections between VMs within a given network as well connections to outside the network. Rule application can be governed using IAM-governed Tags, which allow you to control which VMs are covered by particular rules. Cloud NGFW also offers the option to do L7 inspection of packets.

#### Packet mirroring

[Packet mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) clones the traffic of specific instances in your VPC network and [forwards it to collectors](https://docs.cloud.google.com/vpc/docs/using-packet-mirroring#gcloud) for examination. Packet mirroring captures all traffic and packet data, including payloads and headers. You can configure mirroring for both ingress and egress traffic, for only ingress traffic, or for only egress traffic. The mirroring happens on the VM instances, not on the network.

#### Network virtual appliance

Network virtual appliances let you apply security and compliance controls to the virtual network that are consistent with controls in the on-premises environment. You can do this by deploying VM images that are available in the Google Cloud Marketplace to VMs that have multiple network interfaces, each attached to a different VPC network, to perform a variety of network virtual functions.

Typical use cases for virtual appliances are as follows:

  * [Next-generation firewall (NGFW)](https://wikipedia.org/wiki/Next-generation_firewall). NGFW NVAs deliver protection in situations not covered by Cloud NGFW or to provide management consistency with on-premises NGFW installations.
  * [Intrusion detection system/intrusion prevention system (IDS/IPS)](https://wikipedia.org/wiki/Intrusion_detection_system). A network-based IDS provides visibility into potentially malicious traffic. To prevent intrusions, IPS devices can block malicious traffic from reaching its destination. Google Cloud offers Cloud Intrusion Detection System (Cloud IDS) as a managed service.
  * Secure web gateway (SWG). A SWG blocks threats from the internet by letting enterprises apply corporate policies on traffic that's traveling to and from the internet. This is done by using URL filtering, malicious code detection, and access control. Google Cloud offers Secure Web Proxy as a managed service.
  * [Network address translation (NAT) gateway](https://wikipedia.org/wiki/Network_address_translation). A NAT gateway translates IP addresses and ports. For example, this translation helps avoid overlapping IP addresses. Google Cloud offers [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) as a managed service.
  * [Web application firewall (WAF)](https://en.wikipedia.org/wiki/Web_application_firewall). A WAF is designed to block malicious HTTP(S) traffic that's going to a web application. Google Cloud offers WAF functionality through [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies). The exact functionality differs between WAF vendors, so it's important to determine what you need.



#### Cloud IDS

[Cloud IDS](https://docs.cloud.google.com/intrusion-detection-system/docs/overview) is an intrusion detection service that provides threat detection for intrusions, malware, spyware, and command-and-control attacks on your network. Cloud IDS works by creating a Google-managed peered network containing VMs that will receive mirrored traffic. The mirrored traffic is then inspected by [Palo Alto Networks](https://www.paloaltonetworks.com/) threat protection technologies to provide advanced threat detection.

Cloud IDS provides full visibility into intra-subnet traffic, letting you monitor VM-to-VM communication and to detect [lateral movement](https://www.wikipedia.org/wiki/Network_Lateral_Movement).

#### Cloud NAT

[Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) provides fully managed, software-defined network address translation support for applications. It enables source network address translation (source NAT or SNAT) for internet-facing traffic from VMs that don't have external IP addresses.

#### Firewall Insights

[Firewall Insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/overview) helps you understand and optimize your firewall rules. It provides data about how your firewall rules are being used, exposes misconfigurations, and identifies rules that could be made more strict. It also uses machine learning to predict future usage of your firewall rules so that you can make informed decisions about whether to remove or tighten rules that seem overly permissive.

#### Network logging

You can use multiple Google Cloud products to log and analyze network traffic.

[Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) lets you audit, verify, and analyze the effects of your firewall rules. For example, you can determine if a firewall rule that's designed to deny traffic is functioning as intended. Firewall Rules Logging is also useful if you need to determine how many connections are affected by a given firewall rule.

You enable Firewall Rules Logging individually for each firewall rule whose connections you need to log. Firewall Rules Logging is an option for any firewall rule, regardless of the action (allow or deny) or direction (ingress or egress) of the rule.

[VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) records a sample of network flows that are sent from and received by [VM instances](https://docs.cloud.google.com/compute/docs/instances), including instances used as [Google Kubernetes Engine (GKE) nodes](https://docs.cloud.google.com/kubernetes-engine/docs). These logs can be used for network monitoring, forensics, real-time security analysis, and expense optimization.

### Service networking

Service networking blocks are responsible for providing lookup services that tell services where a request should go (DNS, Service Directory) and with getting requests to the correct place (Private Service Connect, Cloud Load Balancing).

#### Cloud DNS

Workloads are accessed using domain names. [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) offers reliable, low-latency translation of domain names to IP addresses that are located anywhere in the world. Cloud DNS offers both public zones and private managed DNS zones. A public zone is visible to the public internet, while a private zone is visible only from one or more VPC networks that you specify.

#### Cloud Load Balancing

Within Google Cloud, [load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) are a crucial component—they route traffic to various services to provide speed and efficiency, and to help improve security globally for both internal and external traffic.

Our load balancers also let traffic be routed and scaled across multiple clouds or hybrid environments. This makes Cloud Load Balancing the "front door" through which any application can be scaled no matter where it is or in how many places it's hosted. Google offers various types of load balancing: global and regional, external and internal, and Layer 4 and Layer 7.

#### Service Directory

[Service Directory](https://docs.cloud.google.com/service-directory/docs/overview) lets you manage your service inventory, providing a single secure place to publish, discover, and connect services, all operations underpinned by identity-based access control. It lets you register named services and their endpoints. Registration can be either manual or by using integrations with Private Service Connect, GKE, and Cloud Load Balancing. Service discovery is possible by using explicit HTTP and gRPC APIs, as well as by using Cloud DNS.

#### Cloud Service Mesh

[Cloud Service Mesh](https://cloud.google.com/products/service-mesh) is designed to run complex, distributed applications by enabling a rich set of traffic management and security policies in service mesh architectures.

Cloud Service Mesh supports Kubernetes-based regional and global deployments, both Google Cloud and on-premises, that benefit from a managed [Istio](https://istio.io/) product. It also supports Google Cloud using proxies on VMs or proxyless gRPC.

#### Private Service Connect

[Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) creates service abstractions by making workloads accessible across VPC networks through a single endpoint. This allows two networks to communicate in a client-server model that exposes just the service to the consumer instead of the entire network or the workload itself. A service-oriented network model allows network administrators to reason about the services they expose between networks rather than subnets or VPCs, enabling consumption of the services in a producer-consumer model, be it for first-party or third-party services (SaaS).

With Private Service Connect a consumer VPC can use a private IP address to connect to a [Google API](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) or a [service in another VPC](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services).

You can extend Private Service Connect [to your on-premises network](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#on-premises) to access endpoints that connect to Google APIs or to managed services in another VPC network. Private Service Connect allows consumption of services at Layer 4 or Layer 7.

At Layer 4, Private Service Connect requires the producer to create one or more subnets specific to Private Service Connect. These subnets are also referred to as _NAT subnets_. Private Service Connect performs source NAT using an IP address that's selected from one of the Private Service Connect subnets to route the requests to a service producer. This approach lets you use overlapping IP addresses between consumers and producers.

At Layer 7, you can [create a Private Service Connect backend](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls) using an internal Application Load Balancer. The internal Application Load Balancer lets you choose which services are available using a [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts). For more information, see [About Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).

#### Private services access

[Private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) is a private connection between your VPC network and a network that's owned by Google or by a third party. Google or the third parties who offer services are known as _service producers_. Private services access uses VPC Network Peering to establish the connectivity, and it requires the producer and consumer VPC networks to be peered with each other. This is different from Private Service Connect, which lets you project a single private IP address into your subnet.

The private connection lets VM instances in your VPC network and the services that you access communicate exclusively by using [internal IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses). VM instances don't need internet access or external IP addresses to reach services that are available through private services access. Private services access can also be [extended to the on-premises network](https://docs.cloud.google.com/vpc/docs/private-services-access#on-premises-connectivity) by using Cloud VPN or Cloud Interconnect to provide a way for the on-premises hosts to reach the service producer's network. For a list of Google-managed services that are supported using private services access, see [Supported services](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services) in the Virtual Private Cloud documentation.

#### Serverless VPC Access

[Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) makes it possible for you to connect directly to your VPC network from services hosted in serverless environments such as Cloud Run, App Engine, or Cloud Run functions. Configuring Serverless VPC Access lets your serverless environment send requests to your VPC network using internal DNS and internal IP addresses. The responses to these requests also use your virtual network.

Serverless VPC Access sends internal traffic from your VPC network to your serverless environment only when that traffic is a response to a request that was sent from your serverless environment through the Serverless VPC Access connector.

Serverless VPC Access has the following benefits:

  * Requests sent to your VPC network are never exposed to the internet.
  * Communication through Serverless VPC Access can have less latency compared to communication over the internet.



#### Direct VPC egress

[Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) lets your Cloud Run service send traffic to a VPC network without setting up a Serverless VPC Access connector.

### Service security

The service security blocks control access to resources based on the identity of the requestor or based on higher-level understanding of packet patterns instead of just the characteristics of an individual packet.

#### Cloud Armor for DDoS/WAF

[Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) is a web-application firewall (WAF) and distributed denial-of-service (DDoS) mitigation service that helps you defend your web applications and services from multiple types of threats. These threats include DDoS attacks, web-based attacks such as cross-site scripting (XSS) and SQL injection (SQLi), and fraud and automation-based attacks.

Cloud Armor inspects incoming requests on Google's global edge. It has a built-in set of web application firewall rules to scan for [common web attacks](https://docs.cloud.google.com/armor/docs/rule-tuning) and an advanced [ML-based attack detection system](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview) that builds a model of good traffic and then detects bad traffic. Finally, Cloud Armor integrates with Google [reCAPTCHA](https://cloud.google.com/security/products/recaptcha) to help detect and stop sophisticated fraud and automation-based attacks by using both endpoint telemetry and cloud telemetry.

#### Identity Aware Proxy (IAP)

[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap) provides context-aware access controls to cloud-based applications and VMs that are running on Google Cloud or that are connected to Google Cloud using any of the hybrid networking technologies. IAP verifies the user identity and determines if the user request is originating from trusted sources, based on various contextual attributes. IAP also supports TCP tunneling for SSH/RDP access from enterprise users.

#### VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) helps you mitigate the risk of data exfiltration from Google Cloud services such as Cloud Storage and BigQuery. Using VPC Service Controls helps ensure that use of your Google Cloud services happens only from approved environments.

You can use VPC Service Controls to create perimeters that protect the resources and data of services that you specify by limiting access to specific cloud-native identity constructs like service accounts and VPC networks. After a perimeter has been created, access to the specified Google services is denied unless the request comes from within the perimeter.

### Content delivery

The content delivery blocks control the optimization of delivery of applications and content.

#### Cloud CDN

[Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) provides static content acceleration by using Google's global edge network to deliver content from a point closest to the user. This helps reduce latency for your websites and applications.

#### Media CDN

[Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview) is Google's media delivery solution and is built for high-throughput egress workloads.

### Observability

The observability blocks give you visibility into your network and provide insight which can be used to troubleshoot, document, investigate, issues.

#### Network Intelligence Center

[Network Intelligence Center](https://docs.cloud.google.com/network-intelligence-center/docs) comprises several products that address various aspects of network observability. Each product has a different focus and provides rich insights to inform administrators, architects, and practitioners about network health and issues.

## Reference architectures

The following documents present reference architectures for different types of workloads: intra-cloud, internet-facing, and hybrid. These workload architectures are built on top of a cloud data plane that is realized using the building blocks and the architectural patterns that were outlined in earlier sections of this document.

You can use the reference architectures to design ways to migrate or build workloads in the cloud. Your workloads are then underpinned by the cloud data plane and use the architectures. Although these documents don't provide an exhaustive set of reference architectures, they do cover the most common scenarios.

As with the security architecture patterns that are described in [Architectures for Protecting Cloud Data Planes](https://research.google/pubs/pub51077/), real-world services might use a combination of these designs. These documents discuss each workload type and the considerations for each security architecture.

  * [Networking for secure intra-cloud access: Reference architectures](https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access)
  * [Networking for internet-facing application delivery: Reference architectures](https://docs.cloud.google.com/architecture/network-application-delivery)
  * [Networking for hybrid and multi-cloud workloads: Reference architectures](https://docs.cloud.google.com/architecture/network-hybrid-multicloud)



## What's next

  * [Migration to Google Cloud](https://docs.cloud.google.com/solutions/migration-to-gcp-getting-started) can help you to plan, design, and implement the process of migrating your workloads to Google Cloud.
  * [Landing zone design in Google Cloud](https://docs.cloud.google.com/architecture/landing-zones) has guidance for creating a landing zone network.
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-13 UTC."],[],[]] 
