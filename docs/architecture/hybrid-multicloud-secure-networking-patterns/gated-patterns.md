---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-patterns/
title: Gated patterns \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:46.256658+00:00
---

# Gated patterns  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Gated patterns Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

The _gated_ pattern is based on an architecture that exposes select applications and services in a fine-grained manner, based on specific exposed APIs or endpoints between the different environments. This guide categorizes this pattern into three possible options, each determined by the specific communication model:

  * [Gated egress](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress)
  * [Gated ingress](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress)

  * [Gated egress and ingress](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress-ingress) (bidirectional gated in both directions)




As previously mentioned in this guide, the networking architecture patterns described here can be adapted to various applications with diverse requirements. To address the specific needs of different applications, your main landing zone architecture might incorporate one pattern or a combination of patterns simultaneously. The specific deployment of the selected architecture is determined by the specific communication requirements of each gated pattern.

**Note:** In general, the _gated_ pattern can be applied or incorporated with the landing zone design option that exposes the services in a [consumer-producer model](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-4).

This series discusses each gated pattern and its possible design options. However, one common design option applicable to all gated patterns is the [Zero Trust Distributed Architecture](https://docs.cloud.google.com/architecture/network-hybrid-multicloud#zero_trust_distributed_architecture) for containerized applications with microservice architecture. This option is powered by [Cloud Service Mesh](https://cloud.google.com/products/service-mesh), Apigee, and [Apigee Adapter for Envoy](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/concepts)—a lightweight Apigee gateway deployment within a Kubernetes cluster. Apigee Adapter for Envoy is a popular, open source edge and service proxy that's designed for cloud-first applications. This architecture controls allowed secure service-to-service communications and the direction of communication at a service level. Traffic communication policies can be designed, fine-tuned, and applied at the service level based on the selected pattern.

Gated patterns allow for the implementation of Cloud Next Generation Firewall Enterprise with [intrusion prevention service (IPS)](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention) to perform deep packet inspection for threat prevention without any design or routing modifications. That inspection is subject to the specific applications being accessed, the communication model, and the security requirements. If security requirements demand Layer 7 and deep packet inspection with advanced firewalling mechanisms that surpass the capabilities of Cloud Next Generation Firewall, you can use a centralized next generation firewall (NGFW) [hosted in a network virtual appliance (NVA)](https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access#network_virtual_appliance). Several Google Cloud [security partners](https://cloud.google.com/security/partners) offer NGFW appliances that can meet your security requirements. Integrating NVAs with these gated patterns can require introducing multiple security zones within the network design, each with distinct access control levels.

[ Previous arrow_back  Meshed pattern  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/meshed-pattern)

[ Next Gated egress  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
