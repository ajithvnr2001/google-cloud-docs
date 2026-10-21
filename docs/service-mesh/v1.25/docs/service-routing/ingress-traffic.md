---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/ingress-traffic/
title: Ingress traffic for your mesh \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:20.679332+00:00
---

# Ingress traffic for your mesh  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/ingress-traffic/

You are viewing archived v1.25 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Ingress traffic for your mesh

A service mesh facilitates communications among the services running in the mesh. How do you get traffic into your mesh? You can use a _gateway_ to direct traffic from outside your mesh into your mesh through an entry point.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview).

This document describes how to use Cloud Load Balancing as a gateway to get traffic into your mesh, and includes the following:

  * High-level considerations for your gateway.
  * An overview of options when you select a gateway for your mesh.
  * Architectural recommendations that you can apply to your gateway topology.



In this document, _gateway_ refers to a solution or pattern for handling traffic that is destined to a service in your mesh. Istio's Ingress Gateway is one implementation of this pattern. In this document, _gateway_ is a generic term that refers to the general pattern, not the Istio implementation.

This document applies to the Cloud Service Mesh APIs. After the preparatory setup steps, see which contains instructions for deploying with an ingress gateway.

When you design your service mesh, consider traffic coming from the following sources:

  * Traffic that originates inside your mesh
  * Traffic that originates outside your mesh



Traffic that originates inside your mesh travels on the service mesh data plane to reach a backend or endpoint associated with the destination service. However, traffic that originates outside your mesh needs to first reach the service mesh data plane.

In the following example of traffic that originates inside your mesh, Cloud Service Mesh configures your sidecar proxies. These sidecar proxies form the data plane of your service mesh. If Service A wants to communicate with Service B, the following occurs:

  1. Service A makes a request to Service B by name.
  2. This request is intercepted and redirected to Service A's sidecar proxy.
  3. The sidecar proxy then sends the request to an endpoint associated with Service B.

[ ![The mesh's data plane handles traffic internal to the service mesh.](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/csm-ingress-mesh.svg)](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/csm-ingress-mesh.svg) The mesh's data plane handles traffic internal to the service mesh (click to enlarge)

  
In the following example, traffic originates outside your service mesh and doesn't travel along the service mesh data plane.

[ ![The service mesh data plane doesn't handle traffic external
        to the service mesh.](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/csm-mesh-challenge.svg)](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/csm-mesh-challenge.svg) The service mesh data plane doesn't handle traffic external to the service mesh (click to enlarge)

In this example, the client is outside your service mesh. Because it doesn't directly participate in the mesh, the client doesn't know which endpoints belong to services inside the mesh. In other words, because the client doesn't use a Cloud Service Mesh-configured proxy to send outbound requests, it doesn't know which IP address-port pairs to use when sending traffic to Service A or Service B. Without that information, the client can't reach services inside your mesh.

## Considerations for your gateway

This section provides an overview of issues to consider when you select a gateway, including the following:

  * How can clients reach my gateway?
  * What policies do I want to apply to traffic that reaches my gateway?
  * How does my gateway distribute traffic to services in my mesh?



### Enable clients to reach the gateway to your mesh

Clients, whether on the public internet, in your on-premises environment, or within Google Cloud, need a way to reach a service within your mesh. Reaching a service in your mesh is typically achieved by using a publicly or privately routable IP address and port that resolve to a gateway. Clients outside your mesh use this IP address and port to send requests to services in your mesh through your gateway.

Cloud Load Balancing provides various load-balancing options that you can use as the gateway to your mesh. The main questions to ask when you choose a Google Cloud load balancer to act as your gateway are the following:

  * Are my clients on the public internet, in an on-premises environment, or part of my Virtual Private Cloud (VPC) network?
  * Which communication protocols do my clients use?



For an overview of Cloud Load Balancing options, depending on client location and communication protocol, see the Choose a gateway for your mesh section.

### Handle traffic at the gateway

Because your gateway sits at the edge of your mesh—between clients that are outside your mesh and services that are inside your mesh—the gateway is a natural place to apply policies when traffic enters your mesh. These policies include the following:

  * Traffic management—for example, routing, redirects, and request transformation
  * Security—for example, TLS termination and Google Cloud Armor distributed denial-of-service (DDoS) protection
  * Cloud CDN caching



The Choose a gateway for your mesh section highlights policies that are relevant at the edge of your mesh.

### Send traffic from the gateway to a service in your mesh

After your gateway applies policies to incoming traffic, the gateway decides where to send the traffic. You use traffic management and load balancing policies to configure this. The gateway might, for example, inspect the request header to identify the mesh service that should receive the traffic. After the gateway identifies the service, it distributes traffic to a specific backend according to a load-balancing policy.

The Choose a gateway for your mesh section outlines the backends to which a gateway can send traffic.

## Choose a gateway for your mesh

Google Cloud offers a wide range of load balancers that can act as the gateway to your mesh. This section discusses selecting a gateway, comparing the following options along dimensions relevant to the gateway pattern:

  * [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
  * [External Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)
  * [Regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network)
  * [External proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)



In this section, we refer to _first-level_ and _second-level_ gateways. These terms are used to describe the use of one gateway or two gateways to handle ingress traffic to your mesh.

You might need only one level, a single load balancer that acts as a gateway to the mesh. Sometimes, though, it makes sense to have multiple gateways. In these configurations, one gateway handles traffic coming into Google Cloud, and a separate second-level gateway handles traffic as it enters the service mesh.

For example, you might want to apply Google Cloud Armor security policies to traffic entering Google Cloud and advanced traffic management policies to traffic that is entering the mesh. The pattern of using a second Cloud Service Mesh-configured gateway is discussed in the section Handle ingress traffic using a second-level gateway at the edge of your mesh.

The following table compares the capabilities available, depending on the gateway option that you select.

Gateway | Client location | Protocols | Policies | Backends/endpoints  
---|---|---|---|---  
Internal Application Load Balancer | Google Cloud-based clients in the same region as the load balancer. On-premises clients whose requests arrive in the same Google Cloud region as the load balancer—for example, using Cloud VPN or Cloud Interconnect. | HTTP/1.1 HTTP/2 HTTPS | Advanced traffic management TLS termination using self-managed certificates | Backends in the same Google Cloud region as the load balancer, running on:

  * Virtual machine (VM) instance backends on Compute Engine
  * Container instances on Google Kubernetes Engine (GKE) and Kubernetes

  
External Application Load Balancer | Clients on the public internet | HTTP/1.1 HTTP/2 HTTPS |  Traffic management Cloud CDN (including Cloud Storage bucket backends) TLS termination using Google- or self-managed certificates SSL policies Cloud Armor for DDoS and web attack prevention Identity-Aware Proxy (IAP) support for user authentication | Backends in any Google Cloud region, running on:

  * VMs on Compute Engine
  * Container instances on GKE and Kubernetes

  
Internal passthrough Network Load Balancer | Google Cloud-based clients in any region; this requires global access if clients are in a different region from the load balancer. On-premises clients whose requests arrive in any Google Cloud region—for example, using Cloud VPN or Cloud Interconnect. | TCP |  | Backends in the same Google Cloud region as the load balancer, running on VMs on Compute Engine.  
Regional external passthrough Network Load Balancer | Clients on the public internet | TCP or UDP |  | Backends in the same Google Cloud region as the load balancer, running on VMs on Compute Engine.  
External proxy Network Load Balancer | Clients on the public internet | SSL or TCP | TLS termination using Google- or self-managed certificates (SSL proxy only) SSL policies (SSL proxy only) | Backends in any Google Cloud region, running on:

  * VMs on Compute Engine
  * Container instances on GKE and Kubernetes

  
Edge proxy  
(on VM or container instances) configured by Cloud Service Mesh | Clients must be in a location where one of the following applies:

  * They can send a request to a Google Cloud-managed load balancer, which then sends the request to the edge proxy. For details, see [Handle ingress traffic using a second-level gateway at the edge of your mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/traffic-director-ingress-traffic#second-level-gateway).
  * They can send a request through a proxy—for example, a sidecar proxy—that Cloud Service Mesh configures.
  * They can send a request directly to the IP address and port of a VM or container instance that is running the edge proxy.

| HTTP/1.1 HTTP/2 | [Advanced traffic management](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/advanced-traffic-management) (including `regex` support) | Backends in any Google Cloud region, running on:

  * VMs on Compute Engine
  * Container instances on GKE and Kubernetes

  
**Note:** Cloud Service Mesh-configured proxies [support specific protocols](https://docs.cloud.google.com/service-mesh/v1.25/docs/supported-features). Requests that use an unsupported protocol are dropped when they reach a Cloud Service Mesh-configured proxy.

For a detailed feature-by-feature comparison, see the [Load balancer features](https://docs.cloud.google.com/load-balancing/docs/features) page. For a detailed overview of Cloud Service Mesh features, see the [Cloud Service Mesh features](https://docs.cloud.google.com/service-mesh/v1.25/docs/supported-features) page.

### Deploy and configure gateways

A final consideration in selecting your gateway is the developer experience and tooling that you want to use. Google Cloud offers multiple approaches for creating and managing your gateway.

#### Google Cloud CLI and Compute Engine APIs

To configure Google Cloud's managed load-balancing products and Cloud Service Mesh, you can use the Google Cloud CLI and Compute Engine APIs. The gcloud CLI and APIs provide mechanisms to deploy and configure your Google Cloud resources imperatively. To automate repetitive tasks, you can create scripts.

#### Google Cloud console

To configure Cloud Service Mesh and Google Cloud's managed load balancers, you can use the Google Cloud console.

To configure your gateway pattern, you are likely to need both the [**Cloud Service Mesh** page](https://console.cloud.google.com/net-services/trafficdirector/services/list) and the [**Load balancing** page](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list).

#### GKE and Multi Cluster Ingress

GKE and GKE Enterprise network controllers also support the deployment of Cloud Load Balancing for built-in integration with container networking. They provide a Kubernetes-style declarative interface for deploying and configuring gateways. [GKE Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) and [Multi-cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress) controllers manage [internal](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress) and [external](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress) load balancers for sending traffic to a single cluster or across multiple GKE clusters. The Ingress resource can also be configured to point to Cloud Service Mesh-configured services that are deployed in GKE clusters.

## Gateway architecture patterns

This section describes high-level patterns and provides architecture diagrams for your gateway.

The most common pattern involves using a Google Cloud-managed load balancer as your gateway:

  1. Clients send traffic to a Google Cloud-managed load balancer that acts as your gateway.

     * The gateway applies policies.
  2. The gateway sends the traffic to a service in your mesh.




A more advanced pattern involves gateways at two levels. The gateways work as follows:

  1. Clients send traffic to a Google Cloud-managed load balancer that acts as your first-level gateway.

     * The gateway applies policies.
  2. The gateway sends the traffic to an edge proxy (or pool of edge proxies) configured by Cloud Service Mesh. This edge proxy acts as a second-level gateway. This level does the following:

     * Provides a clear separation of concerns in which, for example, one team is responsible for ingress traffic entering Google Cloud while another team is responsible for ingress traffic entering that team's mesh.

     * Lets you apply policies that might not be supported in the Google Cloud-managed load balancer.

  3. The second-level gateway sends the traffic to a service in your mesh.




The ingress pattern ends after traffic reaches an in-mesh service. Both the common case and advanced patterns are described in the following sections.

### Enable ingress traffic from the internet

If your clients are outside Google Cloud and need to reach Google Cloud through the public internet, you can use one of the following load balancers as your gateway:

  * [External Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network)
  * [External proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)

[ ![Ingress traffic from clients on the public internet to in-mesh services using a load balancer.](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/csm-ingress-public.svg)](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/csm-ingress-public.svg) Ingress traffic from clients on the public internet to in-mesh services using a load balancer (click to enlarge)

In this pattern, the Google Cloud-managed load balancer serves as your gateway. The gateway handles ingress traffic before forwarding it to a service in your mesh.

For example, you might choose an external Application Load Balancer as your gateway to use the following:

  * A publicly routable global Anycast IP address, which minimizes latency and network traversal costs.
  * [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) and TLS termination to secure traffic to your mesh.
  * [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) to serve web and video content.
  * Traffic management capabilities such as host-based and path-based routing.



For more information to help you decide on an appropriate gateway, see the Choose a gateway for your mesh section.

### Enable ingress traffic from clients in VPC and connected on-premises networks

If your clients are inside your VPC network, or if they are on-premises and can reach Google Cloud services by using a private connectivity method (such as Cloud VPN or Cloud Interconnect), you can use one of the following load balancers as your gateway:

  * [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
  * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)

[ ![Ingress traffic from clients on a VPC network to in-mesh services using a load balancer.](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/csm-ingress-private.svg)](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/csm-ingress-private.svg) Ingress traffic from clients on a VPC network to in-mesh services using a load balancer (click to enlarge)

In this pattern, the Google Cloud-managed load balancer serves as your gateway. The gateway handles ingress traffic before forwarding it to a service in your mesh.

For example, you might choose an internal Application Load Balancer as your gateway so that you can use these features:

  * A privately addressable IP address
  * TLS termination to secure your mesh
  * Advanced traffic management capabilities such as weight-based traffic splitting
  * NEGs as backends



For more information to help you decide on an appropriate gateway, see the Choose a gateway for your mesh section.

### Handle ingress traffic using a second-level gateway at the edge of your mesh

Depending on your needs, you might consider a more advanced pattern that adds an additional gateway.

[ ![Ingress traffic from external clients to in-mesh services using a load balancer and an edge proxy.](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/csm-ingress-edge-proxy.svg)](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/csm-ingress-edge-proxy.svg) Ingress traffic from external clients to in-mesh services using a load balancer and an edge proxy (click to enlarge)

This gateway is a Cloud Service Mesh-configured edge proxy (or pool of proxies) that sits behind the Google Cloud-managed load balancer. You can host this second-level gateway in your project by using a pool of Compute Engine VMs (a managed instance group) or GKE services.

While this pattern is more advanced, it provides additional benefits:

  * The Google Cloud-managed load balancer applies an initial set of policies—for example, Cloud Armor protection if you are using an external Application Load Balancer.

  * The Cloud Service Mesh-configured edge proxy applies a second set of policies that might not be available in the Google Cloud-managed load balancer. These policies include advanced traffic management that uses regular expressions applied to HTTP headers and weight-based traffic splitting.


**Note:** Cloud Service Mesh-configured proxies [support specific protocols](https://docs.cloud.google.com/service-mesh/v1.25/docs/supported-features). Requests that use an unsupported protocol are dropped when they reach a Cloud Service Mesh-configured proxy.

This pattern can be set up to reflect your organizational structure. For example:

  1. One team might be responsible for handling ingress traffic to Google Cloud while another team is responsible for handling ingress traffic to its mesh.

  2. If multiple teams offer services on one Shared VPC, with each team owning its own service project, teams can use this pattern to manage and apply policies in their own meshes. Each team can expose a Cloud Service Mesh-configured gateway that is reachable on a single IP address and port pair. A team can then independently define and manage the policies that are applied on ingress traffic to the team's mesh.




This pattern can be implemented by using any Google Cloud-managed load balancer, as long as the load balancer can send traffic to the backends that host the Cloud Service Mesh-configured gateways.

## Use the service routing APIs for ingress traffic

The service routing APIs provide the `Gateway` resource for configuring traffic management and security for Envoy proxies acting as ingress gateways, allowing external clients to connect to the service mesh (north-south). For more information, read the [service routing overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-routing-overview) and [Set up an ingress gateway](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/set-up-ingress-gateway).

## What's next

  * To set up an ingress gateway, see [Cloud Service Mesh setup for an ingress gateway](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/set-up-ingress-gateway),
  * To group the VMs and containers that run your code as endpoints of your services, see [Cloud Service Mesh service discovery](https://docs.cloud.google.com/service-mesh/v1.25/docs/traffic-management/service-discovery).
  * To use Cloud Service Mesh with Shared VPC, see [Set up a multi-cluster service mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/set-up-multicluster-gke-mesh).
  * To learn more about Cloud Service Mesh, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
