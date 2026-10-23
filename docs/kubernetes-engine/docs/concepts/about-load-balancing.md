---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-load-balancing/
title: About load balancing in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:52.448145+00:00
---

# About load balancing in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-load-balancing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About load balancing in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides a general overview of how Google Kubernetes Engine (GKE) creates and manages Cloud Load Balancing. This page assumes that you know about the following:

  * Types of [Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#load-balancer-types)
  * The difference between Layer 4 (Network Load Balancers) and Layer 7 (Application Load Balancers) load balancers



This page is for Cloud architects and Networking specialists who design and architect the network for their organization. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE Enterprise user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## How GKE creates load balancers

To make your applications accessible either from outside the cluster (external users) or within your private network (internal users), you can expose your applications by provisioning load balancers using the Gateway, Ingress, and Service APIs. Alternatively, you can create the load balancer components yourself, while GKE manages the network endpoint groups (NEGS) that connect your load balancer to the Pods in your cluster.

### Gateway

The GKE Gateway controller is Google's implementation of the Kubernetes Gateway API for Cloud Load Balancing. Gateway API is an open-source project aimed at standardizing how service meshes and ingress controllers expose applications in Kubernetes. Gateway API is designed to be a more expressive, flexible, and extensible successor to the Ingress resource.

The GKE Gateway controller is used to configure Layer 7 Application Load Balancers to expose HTTP(S) traffic to applications that run in the cluster.

**Best practice** : 

Use Gateway API to implement your load balancer.

### Ingress

The GKE Ingress controller is Google's implementation of the Ingress API. The Ingress API lets you manage external access to Services that run in a cluster. When you create an Ingress resource in GKE, the controller automatically configures a Layer 7 Application Load Balancer that allows HTTP or HTTP(S) traffic to reach your applications that run in the cluster.

GKE Gateway is the recommended choice for new deployments and applications that require advanced traffic management, multi-protocol support, or better multi-tenancy. However, GKE Ingress is a viable option for simpler HTTP/HTTPS routing scenarios, especially for existing configurations where the benefits of migrating to the Gateway API might not yet outweigh the effort.

### LoadBalancer Services

The [Service API](https://kubernetes.io/docs/concepts/services-networking/service/) lets you expose applications that run as Pods in your cluster to external or internal traffic. When you create a Service of type `LoadBalancer`, GKE automatically creates a Layer 4 (TCP/UDP) Passthrough Network Load Balancer based on the parameters of your Service manifest.

In Passthrough Network Load Balancers, when traffic reaches your backend VMs, the original source and destination IP addresses, the communication protocol (like TCP or UDP), and the port numbers (if the protocol uses them) remain the same. This means that traffic is directly passed through to the backend VMs or Pods and the load balancer does not terminate the connections. The backend services handle the termination of connections and ensure that traffic flows seamlessly from the client to the Service.

#### Weighted load balancing

If you configured an external LoadBalancer Service that clients outside your VPC network and Google Cloud VMs can access, then you can enable [weighted load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#weighted-lb). Weighted load balancing distributes traffic based on the number of serving Pods on each GKE node so that nodes that have more serving Pods receive a larger proportion of traffic compared to nodes that have fewer Pods.

### Standalone NEGs

Another method to manage your load balancers in GKE is to create the load balancer components yourself, and let GKE manage the NEGs. This type of load balancer is called a Proxy Network Load Balancer. NEGs are a way to represent groups of backend endpoints (for example, Pods) for load balancing.

This type of load balancer is intended for TCP traffic only. Proxy Network Load Balancers distribute TCP traffic to backends in your VPC network or in other cloud environments. Traffic is terminated at the load balancing layer. The load balancer then forwards the traffic by establishing new TCP connections to the closest available backend.

## What is container-native load balancing?

Container-native load balancing is the practice of evenly distributing traffic directly to the IP addresses of individual Pods (rather than nodes) using the `GCE_VM_IP_PORT` NEGs. `GCE_VM_IP_PORT` NEGs allow you to specify backend endpoints using either the primary internal IP address of a Compute Engine virtual machine (VM), or an IP address from one of the VM's configured alias IP ranges.

Container-native load balancing is used for all GKE-managed Layer 7 load balancers, including Gateway and Ingress, and standalone NEGs. LoadBalancer Services don't use container-native load balancing. However, you can achieve a similar capability by enabling weighted load balancing.

Container-native load balancing has several advantages, including improved network performance and improved health checks, because it targets Pods directly. For more information, see [Container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing).

**Note:** To determine which load balancer best meets your needs, see [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer).

## Summary tables

Use the following tables to help you plan your load balancing configuration.

### Choose a type of load balancer

The following table shows you what type of load balancer is created for a given resource (Gateway, Ingress, or LoadBalancer Service):

Kubernetes resource  |  Type of load balancer created   
---|---  
Application Load Balancer | Passthrough Network Load Balancer  
Gateway  |  |   
Ingress  |  |   
LoadBalancer Service  |  |   
  
### Choose a method for creating a load balancer

The following table shows you the options in GKE to create your chosen load balancer:

Load balancer type  |  Methods to create the chosen load balancer   
---|---  
Gateway | Ingress | LoadBalancer Service | Standalone NEGs  
[Global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) |  |  |  |   
[Classic external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) |  |  |  |   
[Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) |  |  |  |   
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) |  |  |  |   
[Cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) |  |  |  |   
[Proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/proxy-network-load-balancer)   
(all types)  |  |  |  |   
[Passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer)   
(internal and external)  |  |  |  |   
  
## What's next

  * Learn about the [Gateway API in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * Learn about [GKE Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress).
  * Learn about [LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
