---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress-ingress/
title: Gated egress and gated ingress \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:56.955644+00:00
---

# Gated egress and gated ingress  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Gated egress and gated ingress Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

The _gated egress and gated ingress_ pattern uses a combination of gated egress and gated ingress for scenarios that demand bidirectional usage of selected APIs between workloads. Workloads can run in Google Cloud, in private on-premises environments, or in other cloud environments. In this pattern, you can use API gateways, Private Service Connect endpoints, or load balancers to expose specific APIs and optionally provide authentication, authorization, and API call audits.

The key distinction between this pattern and the [_meshed_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/meshed-pattern) lies in its application to scenarios that solely require bidirectional API usage or communication with specific IP address sources and destinations—for example, an application published through a Private Service Connect endpoint. Because communication is restricted to the exposed APIs or specific IP addresses, the networks across the environments don't need to align in your design. Common applicable scenarios include, but aren't limited to, the following:

  * Mergers and acquisitions.
  * Application integrations with partners.
  * Integrations between applications and services of an organization with different organizational units that manage their own applications and host them in different environments.



The communication works as follows:

  * Workloads that you deploy in Google Cloud can communicate with the API gateway (or specific destination IP addresses) by using internal IP addresses. Other systems deployed in the private computing environment can't be reached.
  * Conversely, workloads that you deploy in other computing environments can communicate with the Google Cloud-side API gateway (or a specific published endpoint IP address) by using internal IP addresses. Other systems deployed in Google Cloud can't be reached.



## Architecture

The following diagram shows a reference architecture for the gated egress and gated ingress pattern:

![Data egresses and ingresses between Google Cloud and an on-premises or other cloud network.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-e-i.svg)

The design approach in the preceding diagram has the following elements:

  * On the Google Cloud side, you deploy workloads in a VPC (or shared VPC) without exposing them directly to the internet.
  * The Google Cloud environment network is extended to other computing environments. That environment can be on-premises or on another cloud. To extend the environment, use a suitable [hybrid and multicloud connectivity communication pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/design-considerations#hybrid_and_multicloud_activity) to facilitate the communication between environments so they can use internal IP addresses.
  * Optionally, by enabling access to specific target IP addresses, you can use a transit VPC to help add a perimeter security layer outside of your application VPC. 
    * You can use Cloud Next Generation Firewall or network virtual appliances (NVAs) with next generation firewalls (NGFWs) at the transit VPC to inspect traffic and to allow or prohibit access to certain APIs from specific sources before reaching your application VPC.
  * APIs should be accessed through an API gateway or a load balancer to provide a proxy layer, and an abstraction or facade for your service APIs.
  * For applications consumed as APIs, you can also use Private Service Connect to provide an internal IP address for the published application.
  * All environments use overlap-free RFC 1918 IP address space.



A common application of this pattern involves deploying application backends (or a subset of application backends) in Google Cloud while hosting other backend and frontend components in on-premises environments or in other clouds ([_tiered hybrid_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern) or [_partitioned multicloud_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern)). As applications evolve and migrate to the cloud, dependencies and preferences for specific cloud services often emerge.

Sometimes these dependencies and preferences lead to the distribution of applications and backends across different cloud providers. Also, some applications might be built with a combination of resources and services distributed across on-premises environments and multiple cloud environments.

For distributed applications, the capabilities of [external Cloud Load Balancing hybrid and multicloud connectivity](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#public_clients) can be used to terminate user requests and route them to frontends or backends in other environments. This routing occurs over a hybrid network connection, as illustrated in the following diagram. This integration enables the gradual distribution of application components across different environments. Requests from the frontend to backend services hosted in Google Cloud communicate securely over the established hybrid network connection facilitated by an internal load balancer (ILB in the diagram).

![Data ingresses and egresses between an application frontend in an on-premises or other cloud environment and an application backend in a Google Cloud environment. The data flows through an internal load balancer \(ILB\) in Google Cloud.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-e-i-distributed.svg)

Using the Google Cloud design in the preceding diagram helps with the following:

  * Facilitates two-way communication between Google Cloud, on-premises, and other cloud environments using predefined APIs on both sides that align with the communication model of this pattern.
  * To provide [global frontends for internet-facing applications](https://docs.cloud.google.com/solutions/cross-cloud-network#deliver-internet-facing-apps-and-content) with distributed application components (frontends or backends), and to accomplish the following goals, you can use the advanced load balancing and security capabilities of Google Cloud distributed at [points of presence (PoPs)](https://peering.google.com/#/infrastructure):
  * Reduce capital expenses and simplify operations by using serverless managed services.
  * Optimize connections to application backends globally for speed and latency. 
    * Google Cloud [Cross-Cloud Network](https://docs.cloud.google.com/solutions/cross-cloud-network#how-it-works) enables multicloud communication between application components over optimal private connections.
  * Cache high demand static content and improve application performance for applications using global Cloud Load Balancing by providing access to Cloud CDN.
  * Secure the global frontends of the internet facing applications by using Google Cloud Armor capabilities that provide [globally distributed](https://docs.cloud.google.com/armor/docs/security-policy-overview#edge-security) web application firewall (WAF) and DDoS mitigation services.
  * Optionally, you can incorporate Private Service Connect into your design. Doing so enables private, fine-grained access to Google Cloud service APIs or your published services from other environments without traversing the public internet.



## Variations

The _gated egress and gated ingress_ architecture patterns can be combined with other approaches to meet different design requirements, while still considering the communication requirements of this pattern. The patterns offer the following options:

  * Distributed API gateways
  * Bidirectional API communication using Private Service Connect
  * Bidirectional communication using Private Service Connect endpoints and interfaces



### Distributed API gateways

In scenarios like the one based on the [_partitioned multicloud_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern), applications (or application components) can be built in different cloud environments—including a private on-premises environment. The common requirement is to route client requests to the application frontend directly to the environment where the application (or the frontend component) is hosted. This kind of communication requires a local load balancer or an API gateway. These applications and their components might also require specific API platform capabilities for integration.

The following diagram illustrates how Apigee and [Apigee Hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/what-is-hybrid) are designed to address such requirements with a localized API gateway in each environment. API platform management is centralized in Google Cloud. This design helps to enforce strict access control measures where only pre-approved IP addresses (target and destination APIs or Private Service Connect endpoint IP addresses) can communicate between Google Cloud and the other environments.

![Data ingresses and egresses between an on-premises or other cloud environment and a Google Cloud environment. Client requests to the application frontend go directly to the environment where the application \(or the frontend component\) is hosted.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-e-i-api.svg)

The following list describes the two distinct communication paths in the preceding diagram that use Apigee API gateway:

  * Client requests arrive at the application frontend directly in the environment that hosts the application (or the frontend component).
  * API gateways and proxies within each environment handle client and application API requests in different directions across multiple environments. 
    * The API gateway functionality in Google Cloud (Apigee) exposes the application (frontend or backend) components that are hosted in Google Cloud.
    * The API gateway functionality in another environment (Hybrid) exposes the application frontend (or backend) components that are hosted in that environment.



Optionally, you can consider using a transit VPC. A transit VPC can provide flexibility to separate concerns and to perform security inspection and hybrid connectivity in a separate VPC network. From an IP address reachability standpoint, a transit VPC (where the hybrid connectivity is attached) facilitates the following requirements to maintain end-to-end reachability:

  * The IP addresses for target APIs need to be advertised to the other environments where clients/requesters are hosted.
  * The IP addresses for the hosts that need to communicate with the target APIs have to be advertised to the environment where the target API resides—for example, the IP addresses of the API requester (the client). The exception is when communication occurs through a load balancer, proxy, Private Service Connect endpoint, or NAT instance.



To extend connectivity to the remote environment, this design uses direct VPC peering with [customer route exchange](https://docs.cloud.google.com/vpc/docs/vpc-peering#custom-route-exchange) capability. The design lets specific API requests that originate from workloads hosted within the Google Cloud application VPC to route through the transit VPC. Alternatively, you can use a Private Service Connect endpoint in the application VPC that's associated with a load balancer with a hybrid network endpoint group backend in the transit VPC. That setup is described in the next section: Bidirectional API communication using Private Service Connect.

### Bidirectional API communication using Private Service Connect

Sometimes, enterprises might not need to use an API gateway (like Apigee) immediately, or might want to add it later. However, there might be business requirements to enable communication and integration between certain applications in different environments. For example, if your company acquired another company, you might need to expose certain applications to that company. They might need to expose applications to your company. Both companies might each have their own workloads hosted in different environments (Google Cloud, on-premises, or in other clouds), and must avoid IP address overlap. In such cases, you can use Private Service Connect to facilitate effective communication.

For applications consumed as APIs, you can also use Private Service Connect to provide a private address for the published applications, enabling secure access within the private network across [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) and over hybrid connectivity. This abstraction facilitates the integration of resources from diverse clouds and on-premises environments over a hybrid and multicloud connectivity model. It also enables the assembly of applications across multicloud and on-premises environments. This can satisfy different communication requirements, like integrating secure applications where an API gateway isn't used or isn't planned to be used.

By using Private Service Connect with Cloud Load Balancing, as shown in the following diagram, you can achieve two distinct communication paths. Each path is initiated from a different direction for a separate connectivity purpose, ideally through API calls.

  * All the design considerations and recommendations of Private Service Connect discussed in this guide apply to this design.
  * If additional Layer 7 inspection is required, you can integrate NVAs with this design (at the transit VPC).
  * This design can be used with or without API gateways.



![On-premises or other cloud environments and a Google Cloud environment communicate data through different paths, and through various load balancers, VPC endpoints, and subnets.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-e-i-psc.svg)

The two connectivity paths depicted in the preceding diagram represent independent connections and don't illustrate two-way communication of a single connection or flow.

### Bidirectional communication using Private Service Connect endpoints and interfaces

As discussed in the [_gated ingress_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress), one of the options to enable client-service communication is by using a Private Service Connect endpoint to expose a service in a producer VPC to a consumer VPC. That connectivity can be extended to an on-premises environment or even another cloud provider environment over a hybrid connectivity. However, in some scenarios, the hosted service can also require private communication.

To access a certain service, like retrieving data from data sources that can be hosted within the consumer VPC or outside it, this private communication can be between the application (producer) VPC and a remote environment, such as an on-premises environment.

In such a scenario, [Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) enable a service producer VM instance to access a consumer's network. It does so by sharing a network interface, while still maintaining the separation of producer and consumer roles. With this network interface in the consumer VPC, the application VM can access consumer resources as if they resided locally in the producer VPC.

A Private Service Connect interface is a network interface attached to the consumer (transit) VPC. It's possible to reach external destinations that are reachable from the consumer (transit) VPC where the Private Service Connect interface is attached. Therefore, this connection can be extended to an external environment over a hybrid connectivity such as an on-premises environment, as illustrated in the following diagram:

![Data egresses and ingresses between an application in Google Cloud and a workload in an on-premises or other cloud network.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-e-i-psc-2.svg)

If the consumer VPC is an external organization or entity, like a third-party organization, typically you won't have the ability to secure the communication to the Private Service Connect interface in the consumer VPC. In such a scenario, you can define security policies in the guest OS of the Private Service Connect interface VM. For more information, see [Configure security for Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/configure-security-private-service-connect-interfaces). Or, you might consider an alternative approach if it doesn't comply with the security compliance or standards of your organization.

### Best practices

  * For situations where client requests from the internet need to be received locally by a frontend hosted in a private on-premises or other cloud environment, consider using Hybrid as an API gateway solution.

    * This approach also facilitates a migration of the solution to a fully Google Cloud-hosted environment while maintaining the consistency of the API platform (Apigee).
  * To minimize latency and optimize costs for high volumes of outbound data transfers to your other environments when those environments are in long-term or permanent hybrid or multicloud setups, consider the following:

    * Use Cloud Interconnect or Cross-Cloud Interconnect.
    * To terminate user connections at the targeted frontend in the appropriate environment, use [Hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/what-is-hybrid).
  * Where applicable to your requirements and the architecture, use Apigee Adapter for Envoy with a [Hybrid deployment with Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/example-hybrid).

  * Before designing the connectivity and routing paths, you first need to identify what traffic or API requests need to be directed to a local or remote API gateway, along with the source and destination environments.

  * Use VPC Service Controls to protect Google Cloud services in your projects and to mitigate the risk of data exfiltration, by specifying service perimeters at the project or VPC network level.

    * You can [extend service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/overview#hybrid_access) to a hybrid environment over an authorized VPN or Cloud Interconnect. For more information about the benefits of service perimeters, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * Use [Virtual Private Cloud (VPC) firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) or [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) to control network-level access to Private Service Connect resources through the Private Service Connect endpoint. For example, [outbound firewall rules](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers#firewall-rules) at the application (consumer) VPC can restrict access from VM instances to the IP address or subnet of your endpoints.

  * When using a Private Service Connect interface, you must protect the communication to the interface by configuring security for the Private Service Connect interface.

  * If a workload in a private subnet requires internet access, use [Cloud NAT](https://docs.cloud.google.com/nat/docs) to avoid assigning an external IP address to the workload and exposing it to the public internet.

    * For outbound web traffic, use [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview). The proxy offers [several benefits](https://docs.cloud.google.com/secure-web-proxy/docs/overview#benefits).
  * Review the [general best practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices) for hybrid and multicloud networking patterns.




[ Previous arrow_back  Gated ingress  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress)

[ Next Handover pattern  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/handover-pattern)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
