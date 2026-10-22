---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases/
title: Explore GKE networking documentation and use cases \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:50.491032+00:00
---

# Explore GKE networking documentation and use cases  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Explore GKE networking documentation and use cases Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Networking in Google Kubernetes Engine (GKE) covers a broad set of concepts, including Pods, services, DNS, load balancing, security, and IP address management. Although the documentation explains each feature in detail, it can be difficult to know where to start when facing a real-world problem.

This document helps you navigate the GKE networking documentation by linking common challenges to the features and sections that solve them. Each use case presents a scenario, identifies the challenge, and points you to the relevant documentation. This document is for cloud architects, developers, and operations teams who must understand and solve common networking challenges in GKE.

If you're already familiar with common networking challenges and prefer to delve straight into the technical details, explore the following resources to build your foundational knowledge of GKE networking:

  * [Learn GKE networking fundamentals](https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-fundamentals).
  * [Learn GKE networking architecture](https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-architecture).
  * [Glossary of GKE networking terms](https://docs.cloud.google.com/kubernetes-engine/docs/reference/gke-networking-terminology) (for a quick refresher on any unfamiliar terms).



## Use case: Design the network foundation for GKE

In this use case, you're a cloud architect who needs to design a scalable, secure, and reliable network foundation for a new GKE platform.

### Challenge: Prevent IP address exhaustion

**Scenario:** your application's complexity and usage are expected to grow, so you need to design a network that can scale to handle the increased traffic and support Pod, service, and node growth. You also need to plan your IP address allocation to avoid exhaustion

**Solution:** plan your IP addressing scheme to account for the number of nodes, Pods, and Services you'll need. This plan includes choosing appropriate IP address ranges for each, considering Pod density, and avoiding overlaps with other networks. For more information, see [Manage IP address migration in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies).

### Challenge: Enforce defense-in-depth security

**Scenario:** you need to secure your cluster perimeters and enforce zero-trust, Pod-to-Pod rules.

**Solution:** use [Firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) for cluster perimeters. For more information, see [Control communication between Pods and Services using network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).

### Challenge: Route traffic to different types of applications

**Scenario:** you need to make sure that other services and users can reach different types of applications, such as private backends and public HTTP(S) applications.

**Solution:** use internal load balancers for private backends. For public HTTP(S) applications, use Ingress or Gateway API. For more information, see [About load balancing in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-load-balancing).

### Challenge: Use observability tools to monitor and troubleshoot workload issues

**Scenario:** you must fix problems with network traffic, and need to understand and monitor GKE traffic flows to diagnose issues effectively.

**Solution:** implement observability tools to monitor and troubleshoot network traffic. For more information, see [Observe your traffic using GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/observe-your-traffic).

## Use case: Expose a new microservice

In this use case, you're a developer deploying a new microservice in GKE. You need to make the microservice accessible to other services in the cluster, and later, to external clients.

### Challenge: Provide a stable endpoint for Pod-to-Pod communication

**Scenario:** your application needs Pods to communicate with other Pods, but the dynamic IP addresses used by Pods make this communication unreliable.

**Solution:** create a Kubernetes service. A ClusterIP service provides a stable virtual IP address and DNS name, load-balanced across Pods. For more information, see [Understand Kubernetes services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service).

### Challenge: Expose the service for external access

**Scenario:** the microservice must be reachable from the internet for a demo.

**Solution:** create a LoadBalancer service. GKE provisions a regional external passthrough Network Load Balancer with a public IP address. For HTTP(S) traffic, consider using Ingress or Gateway, which provide Layer 7 features. For more information, see [About LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).

### Challenge: Assign a permanent, user-friendly URL

**Scenario:** the service needs a stable domain name for clients.

**Solution:** reserve a static IP address and configure DNS for a custom domain. For more information, see [Configure domain names with static IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip).

### Challenge: Manage advanced traffic routing

**Scenario:** as your application grows, you need more sophisticated control over how traffic is routed. For example, you might need to do the following:

  * Host multiple websites (like api.example.com and shop.example.com) on a single load balancer to conserve costs.
  * Route requests to different services based on the URL path (for example, sending `/` to the frontend workload and `/api/v1` to the backend workload).
  * Secure your application with HTTPS by managing TLS certificates.
  * Safely deploy new features in stages by using canary releases, where you send a small portion of traffic to a new version before a full rollout.



**Solution:** use Gateway API. GKE's implementation of Gateway API provides a powerful and standardized way to manage this kind of north-south traffic, supporting advanced features like path-based routing, header matching, and traffic splitting. For more information, see [About Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).

## Use case: Scale service discovery for a growing application

As your microservice-based application grows in traffic and complexity, DNS queries between services increase significantly. Although developers need to understand how to build resilient applications in this environment, platform and operations teams are often responsible for implementing scalable networking solutions.

### Challenge: Enable service-to-service communication

**Scenario:** Pods need a reliable way to locate other services.

**Solution:** GKE provides an in-cluster DNS service (such as `kube-dns` or Cloud DNS) that resolves stable DNS names for Services, enabling reliable Pod-to-Pod communication. For more information, see [Service discovery and DNS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery).

### Challenge: Improve DNS performance at scale

**Scenario:** high query volume causes lookup delays.

**Solution:** enable NodeLocal DNSCache. Each node caches DNS queries locally, reducing latency. For more information, see [Set up NodeLocal DNSCache overview](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache).

### Challenge: Provide service discovery across the VPC

**Scenario:** Compute Engine VMs need to access services inside the cluster.

**Solution:** integrate with Cloud DNS so service DNS records resolve across the VPC. For more information, see [Use Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns).

## Use case: Secure a multi-tier application

In this use case, you're on a platform engineering team that's deploying a three-tier application (frontend, billing, database), and you must enforce zero-trust communication.

### Challenge: Enforce strict traffic rules

**Scenario:** only specific services should communicate with each other.

**Solution:** enable network policy enforcement and apply `default deny` policies, then define explicit allow rules (for example, frontend allows traffic to billing, billing allows traffic to database). For more information, see [Configure network policies for applications](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy).

### Challenge: Audit and verify network policies

**Scenario:** security requires proof of enforcement and visibility.

**Solution:** enable network policy logging to record allowed and denied connections. For more information, see [Use network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging).

### Challenge: Expose a service privately to consumers

**Scenario:** a backend service, like a database or API, needs to be accessible to consumers in other VPC networks without exposing it to the public internet or dealing with VPC peering complexities.

**Solution:** use Private Service Connect to publish the service. Consumers can then create a PSC endpoint in their own VPC to access your service privately and securely. For more information, see [Expose services with Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect#configure-cluster-access). 

## Use case: Achieve high availability across multiple clusters

In this use case, you're an SRE running workloads for an ecommerce company in multiple GKE clusters across different regions to improve reliability.

### Challenge: Enable cross-cluster communication

**Scenario:** services in one cluster must discover and call services in another.

**Solution:** use GKE multi-cluster Services (MCS) to create a global DNS name and route traffic automatically to healthy backends. For more information, see [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services).

### Challenge: Ensure resilient failover

**Scenario:** if one regional service becomes unavailable, traffic must reroute automatically.

**Solution:** MCS provides health-aware service discovery, allowing clients to resolve a single DNS name to a healthy backend in the nearest available cluster. This approach enables resilient failover. For more information, see [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services). 

## Use case: Build a secure and efficient multi-tenant GKE environment

As part of a platform engineering team, you provide GKE clusters to multiple application teams. You need to centralize network control, conserve IP addresses, and enforce strict security.

### Challenge: Centralize network control

**Scenario:** multiple app teams need their own clusters, but networking must be centrally managed.

**Solution:** use Shared VPC. Networking resources reside in a host project, but app clusters run in service projects. For more information, see [Configure clusters with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc).

### Challenge: Efficiently manage limited IP addresses

**Scenario:** IP address space is limited and needs to be used efficiently.

**Solution:** adjust maximum Pods per node and, if required, use non-RFC 1918 ranges for Pod IP addresses. For more information, see [Manage IP address migration in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies).

### Challenge: Use a modern, secure dataplane, and provision clusters with the new dataplane

**Scenarios:**

  * The enterprise requires high performance and built-in policy enforcement to support demanding workloads and a zero-trust security posture. For example, you might be running large-scale microservices that are sensitive to network latency, or you might need to enforce strict security boundaries between applications in a multi-tenant cluster to meet regulatory compliance requirements.
  * Clusters must be configured to use a modern networking dataplane for high performance and security, and they must be deployed within the organization's centrally managed network structure.



**Solution:** use GKE Dataplane V2, which is eBPF-based and provides high performance and built-in network policy enforcement. For more information, see [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2). 

## Use case: Observe and troubleshoot traffic

As an SRE, you're investigating why a checkout service can't connect to a payment service.

### Challenge: Resolve connectivity issues

**Scenario:** packets are dropped, but the cause is unclear.

**Solution:** enable GKE Dataplane V2 observability. Metrics like `hubble_drop_total` confirm packets are denied. For more information, see [Troubleshoot with Hubble](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/observe-your-traffic).

### Challenge: Pinpoint root cause of dropped packets

**Scenario:** after confirming network packets are being dropped (for example, by using `hubble_drop_total`), identify which specific network policy is blocking traffic between services.

**Solution:** use the Hubble command-line interface or UI to trace flows. The Hubble UI provides a visual representation of the traffic, highlighting the exact misconfigured policy that is denying the connection. This visualization allows the team to quickly pinpoint the root cause of the issue and correct the policy. For more information, see [Observe your traffic using GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/observe-your-traffic). 

## End-to-end use case: Deploy and scale a secure retail application

In this end-to-end scenario, a platform engineering team builds a standardized GKE platform for multiple application teams. The team deploys and optimizes a three-tier retail application (frontend, billing, database). This process includes securing, scaling, enhancing performance for machine learning workloads, and integrating advanced security appliances.

The following diagram illustrates the end-to-end architecture of a secure, multi-tier retail application deployed on GKE. The architecture evolves through several phases:

  * **Phase 1:** build a foundational setup by using Shared VPC and GKE Dataplane V2.
  * **Phase 2:** expose the application by using Gateway API and multi-cluster services for high availability. 
  * **Phase 3:** accelerate ML tasks by using gVNIC and Tier 1 networking.
  * **Phase 4:** deploy advanced security appliances by using multi-network support. 

![Diagram
  showing the end-to-end architecture for a secure, multi-tier retail application
  on GKE, illustrating networking components across six phases of
  deployment and scaling.](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-networking-use-case.svg)**Figure 1.** An end-to-end architecture for a secure, multi-tier retail application on GKE, highlighting the key networking components used in each phase of deployment and scaling. The details of each phase are described in the following sections.

### Phase 1: Build the platform foundation

**Challenge:** Centralize networking for multiple application teams and allocate sufficient IP addresses to handle scaling.

**Solution:**

  * Use [Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc) for centralized control. 
  * [Plan IP addressing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies) to ensure scalability.
  * Enable [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) for a high-performance and secure data plane.
  * Use [Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect) to securely connect to the GKE control plane.



### Phase 2: Deploy and secure the application

**Challenge:** ensure reliable service-to-service communication and enforce zero-trust security.

**Solution:**

  * Create [ClusterIP services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) for stable internal endpoints.
  * Apply [network policies](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy) with a default-deny baseline and explicit allow rules.



### Phase 3: Expose the application and scale for growth

**Challenge:** provide external access and reduce DNS lookup latency as traffic increases.

**Solution:**

  * Expose the frontend with [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) for advanced traffic management.
  * Assign a [static IP address with DNS](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip).
  * Enable [NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache) for faster lookups. 



### Phase 4: Achieve high availability and troubleshoot issues

**Challenge:** ensure regional failover and debug dropped traffic.

**Solution:**

  * Use [multi-cluster services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services) for cross-region failover.
  * Enable [GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-dpv2-observability) with Hubble to diagnose and fix misconfigured network policies.



### Phase 5: Accelerate machine learning workloads

**Challenge:** eliminate network bottlenecks for GPU-based model training.

**Solution:**

  * Enable [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) for higher bandwidth.
  * Configure [Tier 1 networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-tier-1) on critical nodes for maximum throughput.



### Phase 6: Deploy advanced security appliances

**Challenge:** deploy a third-party firewall and IDS with separate management and data plane traffic at ultra-low latency.

**Solution:**

  * Enable [multi-network support](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods) to attach multiple interfaces to Pods.
  * Configure [device-mode networking (DPDK)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#configure-dpdk-network). 



## What's next

  * [Learn GKE networking fundamentals](https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-fundamentals)
  * [Learn GKE networking architecture](https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-architecture)
  * [Glossary of GKE networking terms](https://docs.cloud.google.com/kubernetes-engine/docs/reference/gke-networking-terminology)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
