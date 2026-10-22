---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress/
title: Gated egress \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:27.660560+00:00
---

# Gated egress  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Gated egress Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

The architecture of the _gated egress_ networking pattern is based on exposing select APIs from the on-premises environment or another cloud environment to workloads that are deployed in Google Cloud. It does so without directly exposing them to the public internet from an on-premises environment or from other cloud environments. You can facilitate this limited exposure through an API gateway or proxy, or a load balancer that serves as a [facade](https://cloud.google.com/apigee/resources/ebook/api-facade-pattern-register) for existing workloads. You can deploy the API gateway functionality in an isolated perimeter network segment, like a [perimeter network](https://en.wikipedia.org/wiki/DMZ_\(computing\)).

The _gated egress_ networking pattern applies primarily to (but isn't limited to) [tiered application architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern) and [partitioned application architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern). When deploying backend workloads within an internal network, gated egress networking helps to maintain a higher level of security within your on-premises computing environment. The pattern requires that you connect computing environments in a way that meets the following communication requirements:

  * Workloads that you deploy in Google Cloud can communicate with the API gateway or load balancer (or a Private Service Connect endpoint) that exposes the application by using internal IP addresses.
  * Other systems in the private computing environment can't be reached directly from within Google Cloud.
  * Communication from the private computing environment to any workloads deployed in Google Cloud isn't allowed.
  * Traffic to the private APIs in other environments is only initiated from within the Google Cloud environment.



The focus of this guide is on hybrid and multicloud environments connected over a private hybrid network. If the security requirements of your organization permit it, API calls to remote target APIs with public IP addresses can be directly reached over the internet. But you must consider the following security mechanisms:

  * API [OAuth 2.0](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-introduction) with Transport Layer Security (TLS).
  * Rate limiting.
  * Threat protection policies.
  * Mutual TLS configured to the backend of your API layer.
  * IP address allowlist filtering configured to only allow communication with predefined API sources and destinations from both sides.



To secure an API proxy, consider these [other security aspects](https://docs.cloud.google.com/apigee/docs/api-platform/security/api-security). For more information, see [Best practices for securing your applications and APIs using Apigee](https://docs.cloud.google.com/architecture/best-practices-securing-applications-and-apis-using-apigee).

## Architecture

The following diagram shows a reference architecture that supports the communication requirements listed in the previous section:

![Data flows in one direction from a host project in Google Cloud to a workload in an on-premises environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated.svg)

Data flows through the preceding diagram as follows:

  * On the Google Cloud side, you can deploy workloads into virtual private clouds (VPCs). The VPCs can be single or multiple (shared or non-shared). The deployment should be in alignment with the projects and [resource hierarchy design](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy) of your organization.
  * The VPC networks of the Google Cloud environment are extended to the other computing environments. The environments can be on-premises or in another cloud. To facilitate the communication between environments using internal IP addresses, use a suitable hybrid and multicloud networking connectivity.
  * To limit the traffic that originates from specific VPC IP addresses, and is destined for remote gateways or load balancers, use IP address allowlist filtering. Return traffic from these connections is allowed when using [stateful firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls#specifications). You can use any combination of the following capabilities to secure and limit communications to only the allowed source and destination IP addresses:

    * [Firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) or [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).

    * Network virtual appliance (NVA) with next generation firewall (NGFW) inspection capabilities that are placed in the network path.

    * [Cloud Next Generation Firewall Enterprise](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention) with intrusion prevention service (IPS) to implement deep packet inspection for threat prevention.

  * All environments share overlap-free RFC 1918 IP address space.




## Variations

The _gated egress_ architecture pattern can be combined with other approaches to meet different design requirements that still consider the communication requirements of this pattern. The pattern offers the following options:

  * Use Google Cloud API gateway and global frontend
  * Expose remote services using Private Service Connect



### Use Google Cloud API gateway and global frontend

![Data flowing in Google Cloud from Apigee to a customer project VPC and then out of Cloud to an on-premises environment or another cloud instance.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-api.svg)

With this design approach, API exposure and management reside within Google Cloud. As shown in the preceding diagram, you can accomplish this through the implementation of Apigee as the API platform. The decision to deploy an API gateway or load balancer in the remote environment depends on your specific needs and current configuration. Apigee provides [two options for provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/overview#withoutvpcpeering) connectivity:

  * With VPC peering
  * Without VPC peering



Google Cloud global frontend capabilities like Cloud Load Balancing, Cloud CDN (when accessed over Cloud Interconnect), and Cross-Cloud Interconnect enhance the speed with which users can access applications that have backends hosted in your on-premises environments and in other cloud environments.

Optimizing content delivery speeds is achieved by delivering those applications from Google Cloud points of presence (PoP). Google Cloud PoPs are present on over [180 internet exchanges and at over 160 interconnection facilities](https://www.peeringdb.com/net/433) around the world.

To see how PoPs help to deliver high-performing APIs when using Apigee with Cloud CDN to accomplish the following, watch [Delivering high-performing APIs with Apigee and Cloud CDN](https://www.youtube.com/watch?v=lwiJUaGPCK4) on YouTube:

  * Reduce latency.
  * Host APIs globally.
  * Increase availability for peak traffic.



The design example illustrated in the preceding diagram is based on Private Service Connect without VPC peering.

The northbound network in this design is established through:

  * A load balancer (LB in the diagram), where client requests terminate, processes the traffic and then routes it to a Private Service Connect backend.
  * A [Private Service Connect backend](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) lets a Google Cloud load balancer send clients requests over a Private Service Connect connection associated with a producer service attachment to the published service (Apigee runtime instance) using [Private Service Connect network endpoint groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs#psc-neg).



The southbound networking is established through:

  * A Private Service Connect endpoint that references a [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments) associated with an internal load balancer (ILB in the diagram) in the customer VPC.
  * The ILB is deployed with hybrid connectivity network endpoint groups ([hybrid connectivity NEGs](https://docs.cloud.google.com/vpc/docs/private-service-connect-deployments#hybrid-services)).

  * Hybrid services are accessed through the hybrid connectivity NEG over a hybrid network connectivity, like VPN or Cloud Interconnect.




For more information, see [Set up a regional internal proxy Network Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid) and [Private Service Connect deployment patterns](https://docs.cloud.google.com/vpc/docs/private-service-connect-deployments).

**Note:** Depending on your requirements, the APIs of the on-premises backends can be exposed through [Apigee Hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/what-is-hybrid), a third party API gateway or proxy, or a load balancer.

### Expose remote services using Private Service Connect

![Data flowing from Google Cloud to an on-premises environment or another cloud, after originating from a workload in a VPC, and traveling through Cloud Load Balancing, a hybrid connectivity NEG, and a Cloud VPN or interconnect.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-psc.svg)

Use the Private Service Connect option to expose remote services for the following scenarios:

  * You aren't using an API platform or you want to avoid connecting your entire VPC network directly to an external environment for the following reasons: 
    * You have security restrictions or compliance requirements.
    * You have an IP address range overlap, such as in a merger and acquisition scenario.
  * To enable secure uni-directional communications between clients, applications, and services across the environments even when you have a short deadline.
  * You might need to provide connectivity to multiple consumer VPCs through a service-producer VPC (transit VPC) to offer highly scalable multi-tenant or single-tenant service models, to reach published services on other environments.



Using Private Service Connect for applications that are consumed as APIs provides an internal IP address for the published applications, enabling secure access within the private network across [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) and over hybrid connectivity. This abstraction facilitates the integration of resources from diverse clouds and on-premises environments over a hybrid and multicloud connectivity model. You can accelerate application integration and securely expose applications that reside in an on-premises environment, or another cloud environment, by using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to [publish the service](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services) with fine-grained access. In this case, you can use the following option:

  * A service attachment that references a [regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid#overview) or an [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-hybrid). 
    * The load balancer uses a hybrid network endpoint group (hybrid connectivity NEG) in a producer VPC that acts in this design as a transit VPC.



In the preceding diagram, the workloads in the VPC network of your application can reach the hybrid services running in your on-premises environment, or in other cloud environments, through the Private Service Connect endpoint, as illustrated in the following diagram. This design option for uni-directional communications provides an alternative option to [peering to a transit VPC](https://docs.cloud.google.com/vpc/docs/vpc-peering).

![Data flowing through and between multiple VPCs inside Google Cloud before exiting through a Cloud VPN or Cloud Interconnect and into an on-premises environment or another cloud.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-psc-2.svg)

As part of the design in the preceding diagram, multiple frontends, backends, or endpoints can connect to the same [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments), which lets multiple VPC networks or multiple consumers access the same service. As illustrated in the following diagram, you can make the application accessible to multiple VPCs. This accessibility can help in [multi-tenant services](https://docs.cloud.google.com/vpc/docs/private-service-connect-deployments#multi-tenant-services) scenarios where your service is consumed by multiple consumer VPCs even if their IP address ranges overlap.

IP address overlap is one of most common issues when integrating applications that reside in different environments. The Private Service Connect connection in the following diagram helps to avoid the IP address overlap issue. It does so without requiring provisioning or managing any additional networking components, like Cloud NAT or an NVA, to perform the IP address translation. For an example configuration, see [Publish a hybrid service by using Private Service Connect](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid#publish).

The design has the following advantages:

  * Avoids potential shared scaling dependencies and complex manageability at scale.
  * [Improves security](https://codelabs.developers.google.com/cloudnet-psc-ilb-gke#1) by providing fine-grained connectivity control.
  * Reduces IP address coordination between the producer and consumer of the service and the remote external environment.



The design approach in the preceding diagram can expand at later stages to integrate Apigee as the API platform by using the networking design options discussed earlier, including the Private Service Connect option.

You can make the Private Service Connect endpoint accessible from other regions by using [Private Service Connect global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access).

The client connecting to the Private Service Connect endpoint can be in the same region as the endpoint or in a different region. This approach might be used to provide high availability across services hosted in multiple regions, or to access services available in a single region from other regions. When a Private Service Connect endpoint is accessed by resources hosted in other regions, [inter-regional outbound charges](https://docs.cloud.google.com/vpc/network-pricing#psc-forwarding-rule-service) apply to the traffic destined to endpoints with global access.

**Note:** To achieve distributed wellness checks and to facilitate connecting multiple VPCs to on-premises environments over multiple hybrid connections, chain an internal Application Load Balancer with an external Application Load Balancer. For more information, see [Explicit Chaining of Google Cloud L7 Load Balancers with PSC](https://codelabs.developers.google.com/codelabs/l7lb-chain-psc#0).

## Best practices

  * Considering [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) and Apigee Hybrid as your API platform solution offers several benefits. It provides a proxy layer, and an abstraction or facade, for your backend service APIs combined with security capabilities, rate limiting, quotas, and analytics. 
    * Use Apigee Adapter for Envoy with an [Apigee Hybrid deployment with Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/example-hybrid) architecture where applicable to your requirements and the architecture.
  * VPCs and project design in Google Cloud should be driven by your resource hierarchy and your secure communication model requirements.
  * When APIs with API gateways are used, you should also use an IP address allowlist. An allowlist limits communications to the specific IP address sources and destinations of the API consumers and API gateways that might be hosted in different environments.
  * Use [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) or [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) to control access to Private Service Connect resources through the Private Service Connect endpoint.
  * If an application is exposed externally through an application load balancer, consider using [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) as an extra layer of security to protect against DDoS and application layer security threats.
  * If instances require internet access, use [Cloud NAT](https://docs.cloud.google.com/nat/docs) in the application (consumer) VPC to allow workloads to access the internet. Doing so lets you avoid assigning VM instances with external public IP addresses in systems that are deployed behind an API gateway or a load balancer.

    * For outbound web traffic, you can use Google Cloud [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview). The proxy offers [several benefits](https://docs.cloud.google.com/secure-web-proxy/docs/overview#benefits).
  * Review the [general best practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices) for hybrid and multicloud networking patterns.




[ Previous arrow_back  Gated patterns  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-patterns)

[ Next Gated ingress  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
