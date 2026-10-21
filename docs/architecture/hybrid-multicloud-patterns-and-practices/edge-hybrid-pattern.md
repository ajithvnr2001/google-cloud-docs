---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/edge-hybrid-pattern/
title: Edge hybrid pattern \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:45.223032+00:00
---

# Edge hybrid pattern  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/edge-hybrid-pattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Edge hybrid pattern Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

Running workloads in the cloud requires that clients in some scenarios have fast and reliable internet connectivity. Given today's networks, this requirement rarely poses a challenge for cloud adoption. There are, however, scenarios when you can't rely on continuous connectivity, such as:

  * Sea-going vessels and other vehicles might be connected only intermittently or have access only to high-latency satellite links.
  * Factories or power plants might be connected to the internet. These facilities might have reliability requirements that exceed the availability claims of their internet provider.
  * Retail stores and supermarkets might be connected only occasionally or use links that don't provide the necessary reliability or throughput to handle business-critical transactions.



The _edge hybrid_ architecture pattern addresses these challenges by running time- and business-critical workloads locally, at the edge of the network, while using the cloud for all other kinds of workloads. In an edge hybrid architecture, the internet link is a noncritical component that is used for management purposes and to synchronize or upload data, often asynchronously, but isn't involved in time or business-critical transactions.

![Data flowing from a Google Cloud environment to the edge.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns-and-practices/edge-hybrid.svg)

## Advantages

Running certain workloads at the edge and other workloads in the cloud offers several advantages:

  * Inbound traffic—moving data from the edge to Google Cloud—[might be free of charge](https://docs.cloud.google.com/vpc/network-pricing#general).
  * Running workloads that are business- and time-critical at the edge helps ensure low latency and self-sufficiency. If internet connectivity fails or is temporarily unavailable, you can still run all important transactions. At the same time, you can benefit from using the cloud for a significant portion of your overall workload.
  * You can reuse existing investments in computing and storage equipment.
  * Over time, you can incrementally reduce the fraction of workloads that are run at the edge and move them to the cloud, either by reworking certain applications or by equipping some edge locations with internet links that are more reliable.
  * Internet of Things (IoT)-related projects can become more cost-efficient by performing data computations locally. This allows enterprises to run and process some services locally at the edge, closer to the data sources. It also allows enterprises to selectively send data to the cloud, which can help to reduce the capacity, data transfer, processing, and overall costs of the IoT solution.
  * Edge computing can act as an [intermediate communication layer](https://docs.cloud.google.com/solutions/unlocking-legacy-applications#section-3) between legacy and modernized services. For example, services that might be running a containerized API gateway such as Apigee hybrid). This enables legacy applications and systems to integrate with modernized services, like IoT solutions.



## Best practices

Consider the following recommendations when implementing the edge hybrid architecture pattern:

  * If communication is unidirectional, use the [gated ingress pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress).
  * If communication is bidirectional, consider the [gated egress and gated ingress pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress-ingress).
  * If the solution consists of many edge remote sites connecting to Google Cloud over the public internet, you can use a software-defined WAN (SD-WAN) solution. You can also use [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview) with a third-party SD-WAN router supported by a [Google Cloud partner](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners) to simplify the provisioning and management of secure connectivity at scale.
  * Minimize dependencies between systems that are running at the edge and systems that are running in the cloud environment. Each dependency can undermine the reliability and latency advantages of an edge hybrid setup.
  * To manage and operate multiple edge locations efficiently, you should have a centralized management plane and monitoring solution in the cloud.
  * Ensure that CI/CD pipelines along with tooling for deployment and monitoring are consistent across cloud and edge environments.
  * Consider using containers and Kubernetes when applicable and feasible, to abstract away differences among various edge locations and also among edge locations and the cloud. Because Kubernetes provides a common runtime layer, you can develop, run, and operate workloads consistently across computing environments. You can also move workloads between the edge and the cloud. 
    * To simplify the hybrid setup and operation, you can use [Google Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview) for this architecture (if containers are used across the environments). Consider [the possible connectivity options](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/concepts/connect-on-prem-gcp) that you have to connect a GKE cluster running in your on-premises or edge environment to Google Cloud.
  * As part of this pattern, although some Google Kubernetes Engine (GKE) components might sustain during a temporary connectivity interruption to Google Cloud, don't use a software-only Google Distributed Cloud deployment when it's disconnected from Google Cloud as a nominal working mode. For more information, see [Impact of temporary disconnection from Google Cloud](https://docs.cloud.google.com/anthos/docs/concepts/anthos-connectivity).
  * To overcome inconsistencies in protocols, APIs, and authentication mechanisms across diverse backend and edge services, we recommend, where applicable, to deploy an API gateway or proxy as a unifying [facade](https://cloud.google.com/apigee/resources/ebook/api-facade-pattern-register). This gateway or proxy acts as a centralized control point and performs the following measures: 
    * Implements additional security measures.
    * Shields client apps and other services from backend code changes.
    * Facilitates audit trails for communication between all cross-environment applications and its decoupled components.
    * Acts as an [intermediate communication layer](https://docs.cloud.google.com/solutions/unlocking-legacy-applications#section-3) between legacy and modernized services. 
      * Apigee and [Apigee Hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/what-is-hybrid) let you host and manage enterprise-grade and hybrid gateways across on-premises environments, edge, other clouds, and Google Cloud environments.
  * [Establish common identity](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment) between environments so that systems can authenticate securely across environment boundaries.
  * Because the data that is exchanged between environments might be sensitive, ensure that all communication is encrypted in transit by using VPN tunnels, [TLS](https://docs.cloud.google.com/architecture/landing-zones/decide-security#option-2-require-layer7), or both.



[ Previous arrow_back  Analytics hybrid and multicloud patterns  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/analytics-hybrid-multicloud-pattern)

[ Next Environment hybrid pattern  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/environment-hybrid-pattern)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
