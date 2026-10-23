---
url: https://docs.cloud.google.com/architecture/network-hybrid-multicloud/
title: Networking for hybrid and multi-cloud workloads: Reference architectures \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:03.247496+00:00
---

# Networking for hybrid and multi-cloud workloads: Reference architectures  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/network-hybrid-multicloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Networking for hybrid and multi-cloud workloads: Reference architectures Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-13 UTC

This document is part of a series that describes networking and security architectures for enterprises that are migrating data center workloads to Google Cloud.

The series consists of the following documents:

  * [Designing networks for migrating enterprise workloads: Architectural approaches](https://docs.cloud.google.com/architecture/network-architecture)
  * [Networking for secure intra-cloud access: Reference architectures](https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access)
  * [Networking for internet-facing application delivery: Reference architectures](https://docs.cloud.google.com/architecture/network-application-delivery)
  * Networking for hybrid and multi-cloud workloads: Reference architectures (this document)



This document discusses networking for a scenario where workloads run in more than one place, such as on-premises and the cloud, or in multiple cloud environments.

## Lift-and-shift architecture

The first hybrid workload access scenario is a lift-and-shift architecture.

### Establishing private connectivity

You can establish connectivity to on-premises networks using either Dedicated Interconnect or Partner Interconnect. The topology illustrated in figure 1 shows how you can use four Dedicated Interconnect connections in two different metros and different edge availability domains to [achieve 99.99% availability](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability). (You can also achieve [99.99% availability using Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability).)

For connectivity between your Google Cloud networks and your networks hosted by another cloud provider, use [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

For more information and detailed recommendations, see [Hybrid connectivity between an on-premises environment and Google Cloud](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking#hybrid-connectivity) in the enterprise foundations blueprint.

![Configuration of redundant Cloud Interconnect connections for 99.99% availability.](https://docs.cloud.google.com/static/architecture/images/network-architecture/on-premises-private-connectivity.svg)

**Figure 1**. Configuration of redundant Dedicated Interconnect connections for 99.99% availability.

**Note:** You need to consider the Cloud Router properties when [advertising prefixes and assigning route priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority).

[NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) lets you use Google's network for data transfer between multiple on-premises or cloud-hosted sites. This approach lets you take advantage of the reach and reliability of Google's network when you need to move data. You can use your existing Cloud VPN, Cloud Interconnect, SD-WAN router appliances, and VPC networks as NCC spokes to support data transfer between the on-premises networks, branch sites, other cloud providers, and Google Cloud VPC networks as shown in figure 2.

![NCC configuration connecting different on-premises enterprise networks outside of Google Cloud using the Google backbone network.](https://docs.cloud.google.com/static/architecture/images/network-architecture/network-connectivity-center.svg)

**Figure 2**. NCC configuration connecting different on-premises enterprise and other cloud networks outside of Google Cloud using the Google backbone network.

For more information about setting up NCC, see [Considerations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#considerations) in the NCC documentation.

### SD-WAN appliances

NCC lets you [use a third-party router appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview) as a NCC spoke to establish connectivity between an external site and your VPC network resources. A router appliance could be a third-party [SD-WAN router supported by one of our partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners) or another virtual appliance that lets you exchange routes with the Cloud Router instance. These appliance-based solutions are in addition to the current site-to-cloud connectivity options that are available with Cloud VPN and Cloud Interconnect as spokes. Figure 3 shows a topology that uses SD-WAN appliances.

![NCC configuration using router appliance for integrating your SD-WAN implementation with Google's network.](https://docs.cloud.google.com/static/architecture/images/network-architecture/sd-wan.svg)

**Figure 3**. NCC configuration using router appliance for integrating your SD-WAN implementation with Google's network.

You can use third-party appliances to perform security functions. The security capabilities of the appliance can be integrated in the router appliance as shown in figure 3. It's also a common pattern to use a networking virtual appliance, where traffic from on-premises lands in a transit VPC network, and the appliance establishes the connectivity with the workload VPC network, as shown in figure 4.

For more information about setting up NCC, see [Considerations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#considerations) in the NCC documentation.

## Hybrid services architecture

As in the intra-cloud use case discussed in [Networking for secure intra-cloud access: Reference architectures](https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access), NCC enables connectivity from your branch sites and on-premises networks to Google Cloud. Private Service Connect provides private access to Google-managed services or lets you consume other services that are built and deployed in the cloud.

You can also implement network security by using a combination of VPC Service Controls, Google Cloud firewalls, and network virtual appliances, as shown in figure 4.

![Networks with an architecture that uses both a lift-and-shift pattern and a hybrid services design pattern that is designed to provide a secure data plane.](https://docs.cloud.google.com/static/architecture/images/network-architecture/hybrid-w-router-appliance.svg)

**Figure 4**. Networks with an architecture that uses both a lift-and-shift pattern and a hybrid services design pattern that is designed to provide a secure data plane.

## Zero Trust Distributed Architecture

In a hybrid environment, microservices run in [service meshes](https://cloud.google.com/products/service-mesh) that are deployed across different [cloud providers](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/previous-generation) and on-premises environments. You can help secure communication between the microservices by using mutual Transport Layer Security (mTLS) and authorization policies. It's a common practice for enterprises to build service meshes in the cloud and to extend the meshes to on-premises. Figure 5 shows an example in which services that are deployed on-premises access the services in the cloud. End-to-end mTLS between the services is enabled using the east-west gateway and Server Name Indication (SNI)-based routing. Cloud Service Mesh helps you secure service-to-service communications, letting you configure authorization policies for the services and deploy certificates and keys that are provided by a managed [certificate authority](https://docs.cloud.google.com/certificate-authority-service/docs).

Hybrid environments typically feature multiple mesh deployments, such as multiple GKE clusters. An important component in this flow is SNI routing, which is used at the GKE east-west gateway for each cluster. This [configuration](https://docs.cloud.google.com/service-mesh/docs/unified-install/multi-cloud-hybrid-mesh) allows direct-to-workload mTLS routing by the gateway while preserving end-to-end mTLS connectivity.

![Zero-trust service mesh deployed across an on-premises environment and Google Cloud.](https://docs.cloud.google.com/static/architecture/images/network-architecture/zero-trust-service-mesh.svg)

**Figure 5**. Zero-trust service mesh deployed across an on-premises environment and Google Cloud.

Enterprises can use Cloud Service Mesh to deploy across clouds. To address challenges in managing identity and certificates across cloud providers, Cloud Service Mesh provides [workload identity](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/concepts/workload-identity) and an intermediate in-cluster certificate authority (CA), using CA Service (CA Service). The intermediate CA can be chained to an external CA or can be hosted in Google. You can customize CA attributes like region and the signature algorithm, using both enterprise-owned HSMs and [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm).

Workload identity lets you assign distinct, fine-grained identities and authorization for each microservice in your cluster. Cloud Service Mesh [manages](https://docs.cloud.google.com/service-mesh/docs/security/security-overview) the process of issuing certificates and of automatically rotating keys and certificates, without disrupting communications. It also provides a single root of trust across GKE clusters.

Figure 6 shows an architecture that uses Cloud Service Mesh to manage identity and authorization.

Services in the mesh can access Google Cloud services using [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation). This feature lets services act with the authority of a Google service account when they invoke Google Cloud APIs. [Workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) also lets the service mesh that's installed in other cloud providers access the Google cloud APIs.

![Zero-trust service mesh deployed across clouds.](https://docs.cloud.google.com/static/architecture/images/network-architecture/zero-trust-mesh-cross-cloud.svg)

**Figure 6**. Zero-trust service mesh deployed across clouds.

You can use Cloud Service Mesh to route traffic from the mesh to on-premises or to any other cloud.

For example, you can create services in Cloud Service Mesh called `on-prem-service` and `other-cloud-service` and [add hybrid connectivity network endpoint groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts) that have endpoints `10.1.0.1:80` and `10.2.0.1:80`. Cloud Service Mesh then sends the traffic to its clients, which are mesh sidecar proxies that run alongside your applications. Thus, when your application sends a request to the `on-prem-service` service, the Cloud Service Mesh client inspects the request and directs it to the `10.2.0.1:80` endpoint. Figure 7 illustrates this configuration.

![Traffic steered from a service mesh using Cloud Service Mesh.](https://docs.cloud.google.com/static/architecture/images/network-architecture/traffic-director-from-service-mesh.svg)

**Figure 7**. Traffic steered from a service mesh using Cloud Service Mesh.

You can also incorporate advanced functionality such as weight-based traffic steering, as shown in figure 8. This capability lets you enable critical enterprise needs such as cloud migration. Cloud Service Mesh serves as a versatile, globally managed control plane for your service meshes.

![Weighted traffic steered using Cloud Service Mesh.](https://docs.cloud.google.com/static/architecture/images/network-architecture/weighted-traffic-steering.svg)

**Figure 8**. Weighted traffic steered using Cloud Service Mesh.

## What's next

  * [Networking for secure intra-cloud access: Reference architectures](https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access).
  * [Networking for internet-facing application delivery: Reference architectures](https://docs.cloud.google.com/architecture/network-application-delivery)
  * [Migration to Google Cloud](https://docs.cloud.google.com/solutions/migration-to-gcp-getting-started) can help you to plan, design, and implement the process of migrating your workloads to Google Cloud.
  * [Landing zone design in Google Cloud](https://docs.cloud.google.com/architecture/landing-zones) has guidance for creating a landing zone network.
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-13 UTC."],[],[]] 
