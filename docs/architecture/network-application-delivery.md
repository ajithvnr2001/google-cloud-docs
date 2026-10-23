---
url: https://docs.cloud.google.com/architecture/network-application-delivery/
title: Networking for internet-facing application delivery: Reference architectures \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:03.326192+00:00
---

# Networking for internet-facing application delivery: Reference architectures  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/network-application-delivery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Networking for internet-facing application delivery: Reference architectures Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-13 UTC

This document is part of a series that describes networking and security architectures for enterprises that are migrating data center workloads to Google Cloud.

The series consists of the following documents:

  * [Designing networks for migrating enterprise workloads: Architectural approaches](https://docs.cloud.google.com/architecture/network-architecture)
  * [Networking for secure intra-cloud access: Reference architectures](https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access)
  * Networking for internet-facing application delivery: Reference architectures (this document)
  * [Networking for hybrid and multi-cloud workloads: Reference architectures](https://docs.cloud.google.com/architecture/network-hybrid-multicloud)



Google offers a set of products and capabilities that help secure and scale your most critical internet-facing applications. Figure 1 shows an architecture that uses Google Cloud services to deploy a web application with multiple tiers.

![Typical multi-tier web application deployed on Google Cloud.](https://docs.cloud.google.com/static/architecture/images/network-architecture/web-tier-application.svg)

**Figure 1**. Typical multi-tier web application deployed on Google Cloud.

**Note:** You need to consider limitations of using Application Load Balancers. For more information, see the [Limitations](https://docs.cloud.google.com/load-balancing/docs/https#limitations) section in the "External Application Load Balancer overview" documentation.

## Lift-and-shift architecture

As internet-facing applications move to the cloud, they must be able to scale, and they must have security controls and visibility that are equivalent to those controls in the on-premises environment. You can provide these controls by using network virtual appliances that are available in the marketplace.

![Application deployed with an appliance-based external load balancer.](https://docs.cloud.google.com/static/architecture/images/network-architecture/lift-and-shift.svg)

**Figure 2**. Application deployed with an appliance-based external load balancer.

These virtual appliances provide functionality and visibility that is consistent with your on-premises environments. When you use a network virtual appliance, you deploy the software appliance image by using autoscaled managed instance groups. It's up to you to monitor and manage the health of the VM instances that run the appliance, and you also maintain software updates for the appliance.

After you perform your initial shift, you might want to transition from self-managed network virtual appliances to managed services. Google Cloud offers a number of managed services to deliver applications at scale.

Figure 2 shows a network virtual appliance configured as the frontend of a web tier application. For a list of partner ecosystem solutions, see the [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?filter=category:networking) page in the Google Cloud console.

## Hybrid services architecture

Google Cloud offers the following approaches to manage internet-facing applications at scale:

  * Use Google's global network of anycast DNS name servers that provide high availability and low latency to translate requests for domain names into IP addresses.
  * Use Google's global fleet of external Application Load Balancers to route traffic to an application that's hosted inside Google Cloud, hosted on-premises, or hosted on another public cloud. These load balancers scale automatically with your traffic and ensure that each request is directed to a healthy backend. By setting up [hybrid connectivity network endpoint groups](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts), you can bring the benefits of external Application Load Balancer networking capabilities to services that are running on your existing infrastructure outside of Google Cloud. The on-premises network or the other public cloud networks are privately connected to your Google Cloud network through a VPN tunnel or through Cloud Interconnect.
  * Use other network edge services such as Cloud CDN to distribute content, Google Cloud Armor to protect your content, and Identity-Aware Proxy (IAP) to control access to your services.

Figure 3 shows hybrid connectivity that uses external Application Load Balancer.

![Hybrid connectivity configuration using external Application Load Balancer and network edge services.](https://docs.cloud.google.com/static/architecture/images/network-architecture/network-services-for-hybrid.svg)

**Figure 3**. Hybrid connectivity configuration using external Application Load Balancer and network edge services.

Figure 4 shows a different connectivity option—using hybrid connectivity network endpoint groups.

![External Application Load Balancer configuration using hybrid connectivity network endpoint groups.](https://docs.cloud.google.com/static/architecture/images/network-architecture/hybrid-w-negs.svg)

**Figure 4**. External Application Load Balancer configuration using hybrid connectivity network endpoint groups.

  * Use a Application Load Balancer (HTTP/HTTPS) to route requests based on their attributes, such as the HTTP uniform resource identifier (URI). Use a proxy Network Load Balancer to implement TLS offload, TCP proxy, or support for external load balancing to backends in multiple [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). Use a passthrough Network Load Balancer to preserve client source IP addresses, avoid the overhead of proxies, and to support additional protocols like UDP, ESP, and ICMP.

  * Protect your service with [Cloud Armor](https://docs.cloud.google.com/armor). This product is an edge DDoS defense and WAF security product that's available to all services that are accessed through load balancers.

  * Use [Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs). You can reuse certificates and private keys that you already use for other Google Cloud products. This eliminates the need to manage separate certificates.

  * Enable caching on your application to take advantage of the distributed application delivery footprint of Cloud CDN.

  * Use [Cloud Next Generation Firewall](https://docs.cloud.google.com/vpc/docs/firewalls) to inspect and filter traffic in your VPC networks.

  * Use Cloud IDS to detect threats in north-south traffic, as shown in figure 6.

![Cloud IDS configuration to mirror and inspect all internet and internal traffic.](https://docs.cloud.google.com/static/architecture/images/network-architecture/ids-mirroring.svg)

**Figure 6**. Cloud IDS configuration to mirror and inspect all internet and internal traffic.




## Zero Trust Distributed Architecture

You can expand Zero Trust Distributed Architecture to include application delivery from the internet. In this model, the Google external Application Load Balancer provides global load balancing across GKE clusters that have Cloud Service Mesh meshes in distinct clusters. For this scenario, you adopt a composite ingress model. The first-tier load balancer provides cluster selection, and then a Cloud Service Mesh-managed ingress gateway provides cluster-specific load balancing and ingress security. An example of this multi-cluster ingress is the [Cymbal Bank reference architecture](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/cymbal-bank) as described in the enterprise application blueprint. For more information about Cloud Service Mesh edge ingress, see [From edge to mesh: Exposing service mesh applications through GKE Ingress](https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress).

Figure 7 shows a configuration in which a external Application Load Balancer directs traffic from the [internet to the service mesh](https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress) through an [ingress gateway](https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress). The gateway is a dedicated proxy in the service mesh.

![Application delivery in a zero-trust microservices environment.](https://docs.cloud.google.com/static/architecture/images/network-architecture/zero-trust-microservices-environment.svg)

**Figure 7**. Application delivery in a zero-trust microservices environment.

## What's next

  * [Networking for secure intra-cloud access: Reference architectures](https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access).
  * [Networking for hybrid and multi-cloud workloads: Reference architectures](https://docs.cloud.google.com/architecture/network-hybrid-multicloud).
  * [Use Cloud Armor, load balancing, and Cloud CDN to deploy programmable global front ends](https://docs.cloud.google.com/architecture/deploy-programmable-gfe-cloud-armor-lb-cdn)
  * [Migration to Google Cloud](https://docs.cloud.google.com/solutions/migration-to-gcp-getting-started) can help you to plan, design, and implement the process of migrating your workloads to Google Cloud.
  * [Landing zone design in Google Cloud](https://docs.cloud.google.com/architecture/landing-zones) has guidance for creating a landing zone network.
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-13 UTC."],[],[]] 
