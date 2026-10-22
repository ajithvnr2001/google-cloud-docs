---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress/
title: Gated ingress \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:53.776730+00:00
---

# Gated ingress  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Gated ingress Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

The architecture of the _gated ingress_ pattern is based on exposing select APIs of workloads running in Google Cloud to the private computing environment without exposing them to the public internet. This pattern is the counterpart to the [_gated egress_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress) and is well suited for [_edge hybrid_](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/edge-hybrid-pattern), [_tiered hybrid_](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern), and [_partitioned multicloud_](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern) scenarios.

Like with the _gated egress_ pattern, you can facilitate this limited exposure through an API gateway or load balancer that [serves as a facade](https://cloud.google.com/apigee/resources/ebook/api-facade-pattern-register) for existing workloads or services. Doing so makes it accessible to private computing environments, on-premises environments, or on other cloud environment, as follows:

  * Workloads that you deploy in the private computing environment or other cloud environments are able to communicate with the API gateway or load balancer by using internal IP addresses. Other systems deployed in Google Cloud can't be reached.
  * Communication from Google Cloud to the private computing environment or to other cloud environments isn't allowed. Traffic is only initiated from the private environment or other cloud environments to the APIs in Google Cloud.



## Architecture

The following diagram shows a reference architecture that meets the requirements of the gated ingress pattern.

![Data flowing in one direction from an on-premises environment or a cloud through a Cloud VPN or Cloud Interconnect into a Google Cloud environment and ending up in a workload.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-ingress.svg)

The description of the architecture in the preceding diagram is as follows:

  * On the Google Cloud side, you deploy workloads into an application VPC (or multiple VPCs).
  * The Google Cloud environment network extends to other computing environments (on-premises or on another cloud) by using hybrid or multicloud network connectivity to facilitate the communication between environments.
  * Optionally, you can use a transit VPC to accomplish the following: 
    * Provide additional perimeter security layers to allow access to specific APIs outside of your application VPC.
    * Route traffic to the IP addresses of the APIs. You can create VPC firewall rules to prevent some sources from accessing certain APIs through an endpoint.
    * Inspect Layer 7 traffic at the transit VPC by integrating a network virtual appliance (NVA).
  * Access APIs through an API gateway or a load balancer (proxy or application load balancer) to provide a proxy layer, and an abstraction layer or facade for your service APIs. If you need to distribute traffic across multiple API gateway instances, you could use an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).
  * Provide limited and fine-grained access to a published [service through a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) by using a load balancer through Private Service Connect to expose an application or service.
  * All environments should use an overlap-free RFC 1918 IP address space.



The following diagram illustrates the design of this pattern using Apigee as the API platform.

![Data flows into a Google Cloud environment and is delivered into a project in an Apigee instance from an on-premises or cloud environment through a Cloud VPN or Cloud Interconnect.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-ingress-apigee.svg)

In the preceding diagram, using Apigee as the API platform provides the following features and capabilities to enable the _gated ingress_ pattern:

  * Gateway or proxy functionality
  * Security capabilities
  * Rate limiting
  * Analytics



In the design:

  * The northbound networking connectivity (for traffic coming from other environments) passes through a Private Service Connect endpoint in your application VPC that's associated with the Apigee VPC.
  * At the application VPC, an internal load balancer is used to expose the application APIs through a Private Service Connect endpoint presented in the Apigee VPC. For more information, see [Architecture with VPC peering disabled](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/overview#withoutvpcpeering).
  * Configure firewall rules and traffic filtering at the application VPC. Doing so provides fine-grained and controlled access. It also helps stop systems from directly reaching your applications without passing through the Private Service Connect endpoint and API gateway.

Also, you can restrict the advertisement of the internal IP address subnet of the backend workload in the application VPC to the on-premises network to avoid direct reachability without passing through the Private Service Connect endpoint and the API gateway.




Certain security requirements might require perimeter security inspection outside the application VPC, including hybrid connectivity traffic. In such cases, you can incorporate a transit VPC to implement additional security layers. These layers, like next generation firewalls (NGFWs) NVAs with [multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts), or Cloud Next Generation Firewall Enterprise with [intrusion prevention service (IPS)](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention), perform deep packet inspection outside of your application VPC, as illustrated in the following diagram:

![Data flows into a Google Cloud environment and is delivered into an application from an on-premises or cloud environment through a Cloud VPN or Cloud Interconnect.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-ingress-vpc.svg)

As illustrated in the preceding diagram:

  * The northbound networking connectivity (for traffic coming from other environments) passes through a separate transit VPC toward the Private Service Connect endpoint in the transit VPC that's associated with the Apigee VPC.
  * At the application VPC, an internal load balancer (ILB in the diagram) is used to expose the application through a Private Service Connect endpoint in the Apigee VPC.



You can provision several endpoints in the same VPC network, as shown in the following diagram. To cover different [use cases](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#use-cases), you can control the different possible network paths using Cloud Router and VPC firewall rules. For example, If you're connecting your on-premises network to Google Cloud using multiple hybrid networking connections, you could send some traffic from on-premises to specific Google APIs or published services over one connection and the rest over another connection. Also, you can use [Private Service Connect global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) to provide failover options.

![Data flows into a Google Cloud environment and is delivered through multiple Private Service Connect endpoints to multiple producer VPCs from an on-premises or cloud environment through a Cloud VPN or Cloud Interconnect.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-ingress-multi-vpc.svg)

## Variations

The _gated ingress_ architecture pattern can be combined with other approaches to meet different design requirements, while still considering the communication requirements of the pattern. The pattern offers the following options:

  * Access Google APIs from other environments

  * Expose application backends to other environments using Private Service Connect

  * Use a hub and spoke architecture to expose application backends to other environments




### Access Google APIs from other environments

For scenarios requiring access to Google services, like Cloud Storage or BigQuery, without sending traffic over the public internet, Private Service Connect offers a solution. As shown in the following diagram, it [enables reachability](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises) to the [supported Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#supported-apis) and services (including Google Maps, Google Ads, and Google Cloud) from on-premises or other cloud environments through a hybrid network connection using the IP address of the Private Service Connect endpoint. For more information about accessing Google APIs through Private Service Connect endpoints, see [About accessing Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#use-cases).

![Data flows from an on-premises environment to Google services into a Google Cloud environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-ingress-api.svg)

In the preceding diagram, your on-premises network must be connected to the transit (consumer) VPC network using either Cloud VPN tunnels or a Cloud Interconnect VLAN attachment.

[Google APIs](https://docs.cloud.google.com/vpc/docs/private-service-connect#google-apis) can be accessed by using [endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) or [backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends). Endpoints let you target a [bundle of Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#supported-apis). Backends let you target a specific [regional Google API](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).

**Note:** Private Service Connect endpoints are registered with [Service Directory](https://docs.cloud.google.com/service-directory) for Google APIs where you can store, manage, and publish services.

### Expose application backends to other environments using Private Service Connect

In specific scenarios, as highlighted by the _tiered hybrid_ pattern, you might need to deploy backends in Google Cloud while maintaining frontends in private computing environments. While less common, this approach is applicable when dealing with heavyweight, monolithic frontends that might rely on legacy components. Or, more commonly, when managing distributed applications across multiple environments, including on-premises and other clouds, that require connectivity to backends hosted in Google Cloud over a hybrid network.

In such an architecture, you can use a local API gateway or load balancer in the private on-premises environment, or other cloud environments, to directly expose the application frontend to the public internet. Using Private Service Connect in Google Cloud facilitates private connectivity to the backends that are exposed through a Private Service Connect endpoint, ideally using predefined APIs, as illustrated in the following diagram:

![Data flows into a Google Cloud environment from an on-premises environment or another cloud environment. The data flows through an Apigee instance and a frontend service in the non-Google Cloud environment and ends up in a customer project application VPC.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-ingress-psc.svg)

The design in the preceding diagram uses an [Apigee Hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/what-is-hybrid) deployment consisting of a management plane in Google Cloud and a runtime plane hosted in your other environment. You can install and manage the runtime plane on a distributed API gateway on one of the supported [Kubernetes platforms](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms) in your on-premises environment or in other cloud environments. Based on your requirements for distributed workloads across Google Cloud and other environments, you can use Apigee on Google Cloud with Apigee Hybrid. For more information, see [Distributed API gateways](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress-ingress#distributed_api_gateways).

### Use a hub and spoke architecture to expose application backends to other environments

Exposing APIs from application backends hosted in Google Cloud across different VPC networks might be required in certain scenarios. As illustrated in the following diagram, a hub VPC serves as a central point of interconnection for the various VPCs (spokes), enabling secure communication over private hybrid connectivity. Optionally, local API gateway capabilities in other environments, such as [Apigee Hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/what-is-hybrid), can be used to terminate client requests locally where the application frontend is hosted.

![Data flows between a Google Cloud environment and an on-premises or other cloud environment and exposes APIs from application backends hosted in Google Cloud across different VPC networks.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/gated-ingress-hub.svg)

As illustrated in the preceding diagram:

  * To provide additional NGFW Layer 7 inspection abilities, the NVA with NGFW capabilities is optionally integrated with the design. You might require these abilities to comply with specific security requirements and the security policy standards of your organization.
  * This design assumes that spoke VPCs don't require direct VPC to VPC communication.

    * If spoke-to-spoke communication is required, you can use the NVA to facilitate such communication.
    * If you have different backends in different VPCs, you can use Private Service Connect to expose these backends to the Apigee VPC.
    * If VPC peering is used for the northbound and southbound connectivity between spoke VPCs and hub VPC, you need to consider the [transitivity limitation](https://docs.cloud.google.com/vpc/docs/vpc-peering#specifications) of VPC networking over VPC peering. To overcome this limitation, you can use any of the following options: 
      * To interconnect the VPCs, use [an NVA](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/Using-network-appliances-to-overcome-the-transitive-VPC-peering/ta-p/76070).
      * Where applicable, consider the Private Service Connect model.
      * To establish connectivity between the Apigee VPC and backends that are located in other Google Cloud projects in the same organization without additional networking components, use [Shared VPC](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs#benefit-of-shared-vpc).
  * If NVAs are required for traffic inspection—including traffic from your other environments—the hybrid connectivity to on-premises or other cloud environments should be terminated on the hybrid-transit VPC.

  * If the design doesn't include the NVA, you can terminate the hybrid connectivity at the hub VPC.

  * If certain load-balancing functionalities or security capabilities are required, like adding Google Cloud Armor DDoS protection or WAF, you can optionally deploy an external Application Load Balancer at the perimeter through an external VPC before routing external client requests to the backends.




## Best practices

  * For situations where client requests from the internet need to be received locally by a frontend hosted in a private on-premises or other cloud environment, consider using Apigee Hybrid as an API gateway solution. This approach also facilitates a seamless migration of the solution to a completely Google Cloud-hosted environment while maintaining the consistency of the API platform (Apigee).
  * Use Apigee Adapter for Envoy with an [Apigee Hybrid deployment with Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/example-hybrid) architecture where applicable to your requirements and the architecture.
  * The design of VPCs and projects in Google Cloud should follow the resource hierarchy and secure communication model requirements, as described in this guide.
  * Incorporating a transit VPC into this design provides the flexibility to provision additional perimeter security measures and hybrid connectivity outside the workload VPC.
  * Use Private Service Connect to access Google APIs and services from on-premises environments or other cloud environments using the internal IP address of the endpoint over a hybrid connectivity network. For more information, see [Access the endpoint from on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#on-premises).
  * To help protect Google Cloud services in your projects and help mitigate the risk of data exfiltration, use VPC Service Controls to specify service perimeters at the project or VPC network level. 
    * When needed, you can [extend service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/overview#hybrid_access) to a hybrid environment over a VPN or Cloud Interconnect. For more information about the benefits of service perimeters, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * Use [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) or [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) to control network-level access to Private Service Connect resources through the Private Service Connect endpoint. For example, [outbound firewall rules](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers#firewall-rules) at the application (consumer) VPC can restrict access from VM instances to the IP address or subnet of your endpoints. For more information about VPC firewall rules in general, see [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).
  * When designing a solution that includes NVAs, it's important to consider the high availability (HA) of the NVAs to avoid a single point of failure that could block all communication. Follow the HA and redundancy design and implementation guidance provided by your NVA vendor.
  * To strengthen perimeter security and secure your API gateway that's deployed in the respective environment, you can optionally implement load balancing and web application firewall mechanisms in your other computing environment (hybrid or other cloud). Implement these options at the perimeter network that's directly connected to the internet.
  * If instances require internet access, use [Cloud NAT](https://docs.cloud.google.com/nat/docs) in the application VPC to allow workloads to access the internet. Doing so lets you avoid assigning VM instances with external public IP addresses in systems that are deployed behind an API gateway or a load balancer.
  * For outbound web traffic, use [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview). The proxy offers [several benefits](https://docs.cloud.google.com/secure-web-proxy/docs/overview#benefits).
  * Review the [general best practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices) for hybrid and multicloud networking patterns.



[ Previous arrow_back  Gated egress  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress)

[ Next Gated egress and gated ingress  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress-ingress)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
