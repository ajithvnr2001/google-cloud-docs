---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-networking/
title: Overview of Service networking in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:08.573946+00:00
---

# Overview of Service networking in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Overview of Service networking in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how you can deploy Services in Google Kubernetes Engine (GKE). Use this page as a guide to better understand the facets of Service networking and the Service network features that exist in GKE.

## Service networking overview

Service networking is the publishing of applications in a way that abstracts the underlying ownership, implementation, or environment of the application that is being consumed by clients. In its simplest form, a Service is a secure, consistent, and available endpoint through which an application is accessed.

Clients and applications have diverse needs for how they can and should communicate. It can be as simple as exposing your application in the Kubernetes cluster for Pods to consume, or as complicated as routing traffic to your application from internet clients across the globe. GKE provides many ways to expose applications as Services that fit your unique use cases.

## Elements of a Service

Exposing an application to clients involves three key elements of a Service:

  * **Frontend** : The load balancer frontend defines the scope in which clients can access and send traffic to the load balancer. This is the network location that is listening for traffic. It has a network, a specific region (or subnet within the network), one or more IPs in the network, ports, specific protocols, and TLS certificates presented to establish secure connections.

  * **Routing and load balancing** : Routing and load balancing define how you process and route your traffic. You can route traffic to [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) based on parameters such as protocols, HTTP headers, and HTTP paths. Depending on the load balancer you use, it might balance traffic to provide lower latency and increased resiliency to your customers.

  * **Backends** : The load balancer backends are defined by the type of endpoints, application platform, and backend service discovery integration. GKE uses service discovery integration to update load balancer backends dynamically as GKE endpoints come up and down.




The following diagram illustrates these concepts for internal and external traffic:

[ ![](https://docs.cloud.google.com/static/kubernetes-engine/images/internal-external-traffic.svg)](https://docs.cloud.google.com/static/kubernetes-engine/images/internal-external-traffic.svg)

In this diagram, the [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) is listening for traffic on the public internet through hundreds of Google points of presence around the world. This global frontend allows traffic to be terminated at the edge, close to clients, before it load balances the traffic to its backends in a Google data center.

The [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) listens within the scope of your VPC network, allowing private communications to take place internally. These load balancer properties make them suited for different kinds of application use cases.

## Understanding GKE load balancing

To expose applications outside of a GKE cluster, GKE provides a built-in [GKE Ingress controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) and [GKE Service controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps) which deploy load balancers on behalf of GKE users. This is the same as the VM load balancing infrastructure, except its lifecycle is fully automated and controlled by GKE. The GKE network controllers provide container-native Pod IP load balancing using opinionated, higher-level interfaces that conform to the Ingress and Service API standards.

The following diagram illustrates how the GKE network controllers automate the creation of load balancers:

[ ![](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-controllers.svg)](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-controllers.svg)

As displayed in the diagram, an infrastructure or app administrator deploys a [declarative manifest](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/) against their GKE cluster. Ingress and Service controllers watch for GKE networking resources (such as [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) objects) and deploy load balancers (plus IP addressing, firewall rules, etc) based on the manifest.

The controller continues managing the load balancer and backends based on environmental and traffic changes. Because of this, GKE load balancing becomes a dynamic and self-sustaining load balancer with a developer-oriented interface.

## Choosing the method to expose your application

When you choose a method for exposing your application in GKE, client network, protocol, and application regionality are the core factors to consider. With GKE's suite of Ingress and Service controllers, you can expose your applications with each of these factors in mind.

While the following sections don't cover every aspect of application networking, working through each of the following factors can help you to determine which solutions are best for your applications. Most GKE environments host many different types of applications, all with unique requirements, so it's likely that you'll use more than one in any given cluster.

For a detailed comparison of Ingress capabilities see [Ingress configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration).

### Client network

A client network refers to the network from where your application clients are accessing the application. This influences where the frontend of your load balancer should be listening. For example, clients could be within the same GKE cluster as the application. In this case, they would be accessing your application from within the cluster network, allowing them to use Kubernetes-native [ClusterIP load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_clusterip).

Clients could also be internal network clients, accessing your application from within the Virtual Private Cloud (VPC) or from an on-premises network across a [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

Clients could also be external, accessing your application from across the public internet. Each type of network dictates a different load balancing topology.

In GKE, you can choose between internal and external load balancers. _Internal_ refers to the VPC network which is an internal private network not directly accessible from the internet. _External_ refers to the public internet. ClusterIP Services are internal to a single GKE cluster so they are scoped to an even smaller network than the VPC network.

The following table provides an overview of which solutions are available for internal and external networks.

Network type | Available solutions  
---|---  
Internal |  [ClusterIP Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_clusterip)   
[NodePort Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_nodeport)   
[Internal LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing)   
[Internal Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress)  
External |  [NodePort Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_nodeport)1  
[External LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_loadbalancer)   
[External Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress)   
[Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup)  
  
1 GKE clusters using the `--no-enable-private-nodes` flag can have nodes with public and private IP addresses and so NodePort Services can be accessible internally and externally.

### Protocol

A protocol is the language your clients speak to the application. Voice, gaming, and low-latency applications commonly use TCP or UDP directly, requiring load balancers that have granular control at layer 4. Other applications speak HTTP, HTTPS, gRPC, or HTTP2, and require load balancers with explicit support of these protocols. Protocol requirements further define which kinds of application exposure methods are the best fit.

In GKE, you can configure Layer 4 load balancers, which route traffic based on network information like port and protocol, and Layer 7 load balancers, which have awareness of application information like client sessions. Each different load balancer comes with specific protocol support as shown in the following table:

Layers | Protocols | Available solutions  
---|---|---  
L4 | TCP   
UDP |  [ClusterIP Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_clusterip)   
[NodePort Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_nodeport)   
[Internal LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing)   
[External LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_loadbalancer)  
L7 |  HTTP   
HTTPS   
HTTP2  |  [Internal Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress)   
[External Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress)   
[Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup)  
  
### Application regionality

Application regionality refers to the degree that your application is distributed across more than one region or GKE cluster. Hosting a single instance of an application has different requirements than hosting redundant instances of an application across two independent GKE clusters. Hosting a geographically distributed application across five GKE clusters to place workloads closer to the end user for lower latency requires even more multi-cluster and multi-regional awareness for the load balancer.

You can break the regionality of GKE load balancing solutions down into two areas:

  * **Backend scope (or cluster scope)** : This scope refers to whether a load balancer can send traffic to backends across multiple GKE clusters. Multi Cluster Ingress has the ability to expose a single [virtual IP address that](https://en.wikipedia.org/wiki/Virtual_IP_address) directs traffic to Pods from different clusters and different regions.

  * **Frontend scope** : This scope refers to whether a load balancer IP listens within a single region or across multiple regions. All of the external load balancers listen on the internet, which is inherently multi-region, but some internal load balancers listen within a single region only.




The following table breaks down the GKE load balancing solutions across these two dimensions.

Backend scope   
(cluster scope) | Available solutions  
---|---  
Single-cluster |  [ClusterIP Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_clusterip)   
[NodePort Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_nodeport)   
[Internal LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing)   
[External LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_loadbalancer)   
[Internal Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress)   
[External Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress)  
Multi-cluster |  [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup)  
Frontend scope | Available solutions  
---|---  
Regional |  [ClusterIP Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_clusterip)   
[Internal Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress)  
Global |  [ClusterIP Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_clusterip)   
[NodePort Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_nodeport)   
[Internal LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing)   
[External LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_loadbalancer)   
[External Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress)   
[Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup)  
  
## Other solutions for application exposure

The preceding solutions are not the only ones available for exposing applications. The following solutions might also be viable replacements or complements to GKE load balancers.

### In-cluster Ingress

In-cluster Ingress refers to software Ingress controllers which have their Ingress proxies hosted inside the Kubernetes cluster itself. This is different from the GKE Ingress controllers, which host and manage their load balancing infrastructure separately from the Kubernetes cluster. These third-party solutions are commonly self-deployed and self-managed by the cluster operator. [istio-ingressgateway](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/) and [nginx-ingress](https://kubernetes.github.io/ingress-nginx/) are two examples of commonly used and open source in-cluster Ingress controllers.

The in-cluster Ingress controllers typically conform to the Kubernetes Ingress specification, and provide varying capabilities and ease of use. The open source solutions are likely to require closer management and a higher level of technical expertise, but might suit your needs if they provide specific features your applications require. There is also a vast ecosystem of enterprise Ingress solutions built around the open source community which provide advanced features and enterprise support.

### Standalone Network Endpoint Groups (NEGs)

GKE Ingress and Service controllers provide automated, declarative, and Kubernetes-native methods of deploying Cloud Load Balancing. There are also valid use cases for deploying load balancers manually for GKE backends, for example having direct and more granular control over the load balancer, or load balancing between container and VM backends.

[Standalone NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg) provide this ability by updating Pod backend IPs dynamically for a NEG, but allow the frontend of the load balancer to be deployed manually. This provides maximum and direct control of the load balancer while retaining dynamic backends controlled by the GKE cluster.

### Service mesh

Service meshes provide client-side load balancing through a centralized control plane. [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) powers the ability to load balance internal traffic across GKE clusters, across regions, and also between containers and VMs. This blurs the line between internal load balancing (east-west traffic) and application exposure (north-south traffic). With the flexibility and reach of modern service mesh control planes, it's more likely than ever to have both the client and server within the same service mesh scope. The preceding GKE Ingress and Service solutions generally deploy middle-proxy load balancers for clients that don't have their own sidecar proxies. However, if a client and server are in the same mesh, then application exposure can be handled using the mesh rather than middle-proxy load balancing.

## What's next

  * [Learn more about Ingress features](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration).
  * [Learn more about external Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb).
  * [Learn more about internal Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb).
  * [Use external LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).
  * [Use internal LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
