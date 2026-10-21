---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-fundamentals/
title: Learn GKE networking fundamentals \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:04:08.548771+00:00
---

# Learn GKE networking fundamentals  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-fundamentals/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Learn GKE networking fundamentals Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) networking provides a powerful, scalable, and secure foundation for your containerized applications, built on Google's global VPC. It translates the abstract Kubernetes networking model into concrete, high-performance resources like global load balancers and high-throughput VM networking.

This document and the rest of this documentation set are for cloud architects and networking specialists who design their organization's network architecture.

## Why Kubernetes networking is different

When you use Kubernetes to orchestrate your applications, you think differently about network design. With Kubernetes, you focus on how Pods, Services, and external clients communicate, rather than managing individual host or virtual machine (VM) networking. This abstraction simplifies application deployment and scaling by eliminating complexities like manual port mapping.

## Prerequisites

Before you learn about networking in GKE, you should understand the following:

  * Key concepts in general networking, Google Cloud, and Kubernetes.
  * Read [Start learning about GKE](https://docs.cloud.google.com/kubernetes-engine/docs/learn).



## Core networking and Google Cloud fundamentals

GKE builds on standard networking principles. To understand how GKE manages and routes traffic within and across clusters, you should be familiar with the following core networking concepts.

### Networking layers and protocols

To understand how data travels through a network, start with networking layers. GKE extensively uses concepts from the transport, internet, and application layers of the network stack. You should be familiar with their basic functions and common protocols like HTTP, DNS, and the TCP/IP suite. For more information, see the [OSI model](https://en.wikipedia.org/wiki/OSI_model).

  * **Transport layer—Transmission Control Protocol (TCP) or User Datagram Protocol (UDP)** : handles end-to-end communication between applications. Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery, which is essential for most application traffic. User Datagram Protocol (UDP) offers faster, connectionless communication, often used for streaming or gaming. GKE uses both protocols for Pod and Service communication.

  * **Internet layer—Internet Protocol (IP)** : addresses and routes packets across different networks. Every Pod and node in GKE gets an IP address, and IP address routing dictates how traffic finds its way through your cluster and VPC network.

  * **Application layer—Hypertext Transfer Protocol (HTTP) and Domain Name System (DNS)** : this layer is where applications interact with the network. HTTP and HTTPS are fundamental to web communication and are commonly used by Ingress controllers and load balancers to expose applications. DNS is vital for service discovery in Kubernetes, translating human-readable service names into IP addresses.




### IP addressing and CIDR notation

You must understand [IP addressing](https://en.wikipedia.org/wiki/IP_address) and [CIDR (Classless Inter-Domain Routing)](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation because the Kubernetes networking model uses IP addresses extensively for communication between all its components. CIDR is crucial for planning your cluster's IP address allocation within your Google Cloud VPC network. It lets you define blocks of IP addresses for Pods, Services, and Nodes. For example, allocating `10.10.0.0/16` for your Pods reserves 65,536 IP addresses. Proper CIDR planning helps prevent situations where you run out of IP addresses as your cluster scales.

### Linux networking utilities

GKE uses underlying Linux kernel features to implement traffic routing and load balancing within the cluster. You should be familiar with fundamental Linux network management concepts and utilities like [routing tables](https://en.wikipedia.org/wiki/Routing_table) and [iptables](https://www.netfilter.org/projects/iptables/index.html). Traditionally, `kube-proxy`, a key Kubernetes component on each node, programs these utilities to intercept traffic destined for a Service and redirect it to one of the backend Pods. Modern GKE clusters that use GKE Dataplane V2 replace `iptables` with [eBPF](https://ebpf.io/) for improved performance and observability.

### Understand the Kubernetes networking model

The Kubernetes networking model defines how containerized applications communicate within a cluster. Unlike conventional models that focus on virtual machines, Kubernetes emphasizes Pod-to-Pod and Service-based communication. This model makes application networking more predictable by abstracting away the unreliability of dynamic Pod IP addresses. Because Pods are ephemeral and can be re-created at any time with a new IP address, direct communication with Pod IP addresses is inherently unstable. Kubernetes solves this problem by grouping Pods into a Service. A Service provides a stable, virtual IP address (`ClusterIP`) and a consistent DNS name, which applications can reliably connect to. This stable endpoint, combined with a flat network that allows all Pods to communicate directly without needing NAT, creates a robust foundation for modern, containerized applications.

#### Key principles of the Kubernetes networking model

  * **Each Pod has a unique IP address** : every Pod in a Kubernetes cluster gets its own IP address, which is shared by all containers within that Pod. This unique IP address lets Pods act like individual hosts on the network, similar to virtual machines.

  * **Flat Pod-to-Pod communication without NAT** : all Pods can communicate directly with each other by using their IP addresses, regardless of the node they're running on. In GKE, this direct communication is achieved using [ VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips), where Pod IP addresses are alias IP addresses within your VPC network. These alias IP addresses make Pods directly routable within the VPC, which removes the need for Network Address Translation (NAT) and simplifies cross-node communication.

  * **Services provide stable endpoints** : because Pods are ephemeral and can be re-created at any time with new IP addresses, direct communication with Pod IP addresses is unreliable. Kubernetes Services solve this by grouping a set of Pods and exposing a stable IP address (`ClusterIP`) and DNS name. This issue abstraction enables consistent access to a dynamic set of Pods.

  * **Built-in Service discovery with DNS** : Kubernetes includes a built-in DNS service that automatically assigns DNS names to Services. Applications can use these names (for example, `my-service.my-namespace.svc.cluster.local`) to reliably locate and communicate with other Services.

  * **Integrated load balancing.** when clients send traffic to a Service's `ClusterIP` address, networking rules on the node (programmed by `kube-proxy` or GKE Dataplane V2) intercept the traffic and load-balance it across all healthy Pods in that Service. This distribution happens at the source, making it highly efficient and helping to ensure high availability.




In summary, the Kubernetes networking model abstracts many conventional network complexities into a simpler, more powerful set of primitives for containerized applications. By enabling direct Pod communication, stable Service endpoints, and integrated DNS and load balancing, it provides a robust, scalable foundation for modern, containerized applications.

### The GKE and Google Cloud relationship

GKE networking acts as the bridge between the conceptual model of Kubernetes networking and the physical infrastructure of Google Cloud:

  * **Kubernetes networking model** : Kubernetes defines rules where every Pod gets its own IP address, enabling direct Pod-to-Pod communication without needing [NAT](https://docs.cloud.google.com/nat/docs/overview).

  * **[Google Cloud Networking](https://docs.cloud.google.com/vpc/docs)** : this is the underlying infrastructure, including VPC, subnets, firewalls, and load balancers.

  * **GKE networking** : this connecting layer implements the Kubernetes model by using Google Cloud's infrastructure.

  * **[Container Network Interface (CNI)](https://github.com/containernetworking/cni)** : GKE uses a CNI plugin on each node to handle Pod IP address allocation and connect Pods to the node's network.

  * **GKE control plane** : these components interact with Google Cloud to automatically configure VPC routes for Pod IP ranges, manage firewall rules, and provision load balancers based on your Kubernetes deployments.


![The following diagram shows the flow of ingress and egress traffic both to and from GKE clusters that are in a VPC and behind a cloud firewall. Ingress traffic includes load-balanced traffic from components such as SSL proxy, TCP proxy, or HTTP\(S\) load balancing. Egress traffic includes destinations such as external networks, users, and TCP proxy load balancing.](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-networking-components.svg)**Figure 1.** GKE networking integrates with Google Cloud components like VPC, Cloud Load Balancing, and Cloud Firewall to provide a secure and scalable environment.

## Why Google Cloud networking knowledge is essential for GKE

GKE builds on Google Cloud networking infrastructure. GKE doesn't create a separate network layer—instead, it uses existing Google Cloud networking components. As a result, understanding Google Cloud networking is essential for designing and securing your GKE clusters.

Here's why Google Cloud networking fundamentals matter:

  * **Your cluster runs in a VPC** : every GKE cluster operates within a VPC. All IP addresses—for nodes, Pods, and Services—draw from the IP address ranges defined in your VPC subnets. To properly allocate IP addresses and avoid running out of them, you need a working knowledge of VPC and subnet design. For more information, see the [VPC](https://docs.cloud.google.com/vpc/docs) documentation.

  * **Application exposure uses Google Cloud Load Balancers** : when you expose applications outside the cluster by using a LoadBalancer Service or Ingress, GKE provisions a built-in Google Cloud load balancer. A LoadBalancer Service is typically used for Layer 4 traffic, and an Ingress is used for Layer 7 HTTP(S) traffic. Understanding how these load balancers operate helps you manage external traffic, set up health checks, and troubleshoot connectivity issues effectively. For more information, see the [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs) documentation.

  * **Security is enforced through Google Cloud firewall rules** : GKE automatically creates some firewall rules to allow essential cluster traffic. However, securing your workloads requires defining custom VPC firewall rules. Misconfigurations can block critical traffic, so it's important to understand how these rules work. For more information, see the [Cloud Next Generation Firewall](https://docs.cloud.google.com/firewall/docs) documentation.




## What's next

  * Read about the [three pillars of GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-architecture#three-pillars) for a deeper dive into the architecture.
  * Learn about [GKE NetworkPolicies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) and [Kubernetes network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).
  * Explore [exposing applications by using Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps) and the concept of [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/).
  * Understand [Ingress for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) and [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/).
  * Dive deeper into [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips).
  * Learn about the benefits of [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2).
  * Troubleshoot [GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshoot-networking).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
