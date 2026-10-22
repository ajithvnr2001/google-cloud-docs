---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/dataplane-v2/
title: Dataplane V2 \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:39.358645+00:00
---

# Dataplane V2  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/dataplane-v2/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Dataplane V2

Dataplane V2 is a data plane for GKE and GKE clusters that is optimized for Kubernetes networking. This page gives an overview of what Dataplane V2 does and how it works.

## Introduction

Dataplane V2 provides:

  * A consistent user experience for networking in GKE and all GKE cluster environments. See [Availability of Dataplane V2](https://docs.cloud.google.com/anthos/clusters/docs/dataplane-v2) for information about the environments that support Dataplane V2.
  * Real-time visibility of network activity.
  * Simpler architecture that makes it easier to manage and troubleshoot clusters.



Dataplane V2 is based on [eBPF](https://ebpf.io/) and Linux nodes to flexibly and efficiently process network packets in-kernel using Kubernetes-specific metadata.

**Note:** For Dataplane V2 to function correctly, GKE on Azure deploys Pods such as `anetd` with elevated [RBAC permissions](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb), to your nodes, such as the ability to update or patch all Pod objects on the same node as the `anetd` Pod. These permissions are required for Dataplane V2 to interpret Kubernetes objects and program network topologies in eBPF based on your configuration.

## Advantages of Dataplane V2

### Security

Kubernetes [Network policy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) is always on in clusters with Dataplane V2. You don't have to install and manage third-party software add-ons such as Calico to enforce network policy.

### Scalability

Dataplane V2 is designed to improve routing in large clusters. It doesn't use [kube-proxy](https://kubernetes.io/docs/concepts/overview/components/#kube-proxy) or iptables.

### Operations

When you create a cluster with Dataplane V2, network policy logging is built in. To see when your Pod objects allow and deny connections, configure the [logging CRD](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) on your cluster.

### Consistency

Dataplane V2 is available and provides the same features on GKE and on other GKE clusters environments. See [Availability of Dataplane V2](https://docs.cloud.google.com/anthos/clusters/docs/dataplane-v2) for more details.

## How Dataplane V2 works

As packets arrive at a node, eBPF programs installed in the kernel decide how to route and process the packets. Unlike packet processing with iptables, eBPF programs can use Kubernetes-specific metadata in the packet. This lets Dataplane V2 efficiently process network packets in the kernel and report annotated actions back to user space for logging. The following diagram shows the path of a packet through a node using Dataplane V2:

![A packet arriving at a node is processed in-kernel by eBPF. eBPF programs perform policy enforcement, service resolution, and connection tracking. This activity is reported to userspace for logging. The packet payload is then delivered to a Pod.](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/images/dataplanev2.svg)

The Dataplane V2 controller on the node is called `anetd`. `anetd` is deployed as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) to each node and is responsible for interpreting Kubernetes objects and programming network topologies in eBPF. The `anetd` controller replaces the service routing kube-proxy and the routing it would perform in the kube-system namespace.

Dataplane V2 on GKE clusters runs in [Overlay Network mode](https://en.wikipedia.org/wiki/Overlay_network). In this mode, all cluster nodes form a mesh of tunnels using the [Geneve encapsulation protocol](https://www.redhat.com/en/blog/what-geneve). All container-to-container network traffic is routed through these tunnels. The main advantage of this model is that the cluster's nodes don't need to be aware of the underlying Azure network configuration.

## What's next

  * [Configuring Network Policies on GKE Multi-Cloud](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/network-policy)
  * Use [network policy logging](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/network-policy-logging) to record when your cluster's [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) allow or deny connections to a Pod.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
