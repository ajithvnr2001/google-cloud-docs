---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-service-steering/
title: About Service Steering \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:53.042721+00:00
---

# About Service Steering  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-service-steering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About Service Steering Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Overview

You can control how network traffic flows within your GKE cluster by using GKE Service Steering. You can define rules to direct specific types of traffic to network functions that you've deployed in your cluster. GKE Service Steering is similar to policy-based routing, where you override the normal path of the network traffic.

## Terminology and concepts

This page uses the following concepts:

**Service Function (SF)**

A _Service Function_ is a software component that works on the received data packets. A Service layer can operate at any layer of the OSI model starting Layer 2 (data link layer).

Service Functions can be broadly categorized into the following:

  * Firewalls for security
  * Proxies for controlling access
  * WAN acceleration for improving speed,
  * Deep Packet Inspection (DPI) for analyzing content
  * Lawful Intercept (LI) for surveillance and investigation
  * Network Address Translator (NAT) for private and public IP addresses
  * HTTP for header enrichment
  * Load balancers for distributing traffic efficiently



Alternate terminologies for Service Functions include:

  * Container appliances
  * Virtual appliances
  * Virtualized network functions (NFVs)
  * Containerized network functions (CNFs)
  * Cloud-native network functions (CNFs)



In Service Steering, a Service object represents a Service Function (SF).

**Service Function Chain (SFC)**

Service Function Chain (SFC) is a series of Service Functions such as firewalls, proxies, or load balancers linked together to process network traffic in specific order. This chain acts like a pipeline, where each Service Function performs a particular task on the traffic before passing it onto the next function.

Service Function Chain (SFC) is also called Service Chain (SC).

In Service Steering, `ServiceFunctionChain` object represents a Service Function Chain (SFC).

A Service Function operates independent of any Service Function Chain. Service Function is typically unaware of which Service Function Chains it's part of.

**Service Steering**

Service Steering routes packets to the selected Service Function in a way that is completely transparent to the source and destination. This concept is sometimes referred to as "policy-based routing", "traffic redirection", or "Service Function forwarding". Service Steering achieves the transparent routing using Geneve + NSH encapsulation (see [RFC 8926](https://www.rfc-editor.org/rfc/rfc8926), [RFC 8300](https://www.rfc-editor.org/rfc/rfc8300), [Geneve + NSH IETF Draft](https://datatracker.ietf.org/doc/html/draft-boutros-nvo3-geneve-applicability-for-sfc-04)).

Some of the important characteristics of Service Steering include:

  * **Load balancing across a Service Function's backend Pods:** Service Functions often run on multiple Pods for scalability and reliability. Service Steering distributes incoming network traffic evenly across these Pods to prevent any single Pod from becoming overloaded.
  * **Supporting 5-tuple flow affinity (all intermediate hops must be stable for a given flow):** A 5-tuple flow is a way of identifying a specific stream of network traffic based on source IP address, source port, destination IP address, destination port, and protocol. Service Steering helps ensure that all packets within the same flow are consistently directed to the same set of Service Functions (hops).
  * **Enabling a symmetric return datapath:** A symmetric return datapath means that the response traffic follows the same path back to the source as the original request traffic did. Service Steering helps ensure this symmetry, which is important for some network protocols and applications.



For any given network traffic that's being service steered, the intermediate Service Function Pods handle all the packets of that particular network traffic ensuring consistent intermediate hops and predictable route. The same Service Function Pods receives the return traffic to ensure symmetric traffic flow. If the original traffic is sent to a destination within the same cluster, the return traffic automatically finds a way back through the same Service Chain. If the original traffic is outside the cluster, the final Service Function in the chain attracts the traffic back to itself using either source network address translation (SNAT) or a proxy, which acts as an intermediary.

## Use cases

GKE Service Steering integrates policy-based routing into your clusters. This enables the following primary use cases:

**Self-managed security services:**

Organizations can construct their own security infrastructure using containerized network functions (CNFs) such as virtual firewalls (vFWs), virtual next-generation firewalls (vNG-FWs), and virtual intrusion detection systems (vIDSs). Service Steering helps ensure that traffic is routed through these CNFs before reaching its intended destination, providing a layer of protection and control.

**Managed security providers (MSPs):**

MSPs can utilize GKE Service Steering to route your traffic through their cloud-based security Service Chains. This allows them to offer comprehensive security solutions, including Secure Web Gateways (SWGs), SASE (Secure Access Service Edge), and SD-WAN (Software-Defined Wide Area Network) functionalities.

**Telecommunications and 5G Networks:**

Service Steering manages traffic flows for various network functions within telecom and 5G infrastructures. You can orchestrate virtual routers (vRouters), virtual session border controllers (vSBCs), and 5G core network functions to ensure efficient traffic management, load balancing, and the enforcement of specific security or quality of Service policies.

## How Service Steering works

This section describes how various components of Service Steering works.

**Service Function**

  1. **Identifies network traffic flow** : GKE Service Steering identifies each network connection by using a unique flow ID, a 5-tuple hash of the packet's source IP address, source port, destination IP address, destination port, and protocol.

  2. **Helps ensure flow affinity** : Service Steering helps ensure flow affinity by directing all packets with the same flow ID through the same path of Service Functions (SFs).

  3. **Modifies packets to create new flows** : If an Service Function modifies any of the 5-tuple fields in a packet. For example, NAT changing the source IP address, this creates a new flow.

  4. **Selects traffic for new flows** : Traffic selection process evaluates the new flow to determine its path through the remaining `Service Functions`, potentially taking a different route than the original flow.

  5. **Handles proxies and NATs as two flows** : Traffic through proxies or NATs is considered as two separate flows: source to proxy/NAT and proxy/NAT to destination. Service Steering doesn't guarantee the same path for these two flows.

  6. **Validates source address** : SFs are always subject to source address validation, even for traffic not steered by Service Steering. If an Service Function originates a new flow with a mismatched source IP address, those packets are dropped unless explicitly allowed.

  7. **Maintains encapsulation transparency** : Service Steering uses Geneve encapsulation for traffic between SFs, but Service Function Pods themselves are unaware of it. Packets are decapsulated before entering the Pod, simplifying Service Function development.




**Existing connections**

When you create a `TrafficSelector`, Service Steering automatically applies it to any existing connections that match the selector's criteria. It redirects packets from these connections to the appropriate service functions. The Service Function itself is responsible for managing these in-flight connections. A common approach is to drop the packets and rely on the client to initiate a new connection, which then seamlessly integrates into the service chain from the beginning.

**Resource lifecycle**

Both `TrafficSelector` and `ServiceFunctionChain` resources are deleted immediately after they're marked for deletion. There are no webhooks or finalizers that prevent or delay resource deletion.

**Pod-to-Service traffic**

Service Steering performs traffic selection after it resolves the Service Virtual IP address. The traffic directed to a Service using its ClusterIP can be selected for Service Steering if the destination Pod's IP address falls within the CIDR specified in the `.egress.to.ipBlock` field after the Virtual IP address is resolved.

**NetworkPolicy enforcement**

Service Steering does not bypass `NetworkPolicy`. Egress policy at the source Pod and ingress policy at the destination Pod still apply to traffic selected for Service Steering. However, it is not subject to `NetworkPolicy` enforcement at the ingress or egress of a Service Function. This is because the ingress or egress rules of `NetworkPolicy` are well-defined for source and destination Pods, but not packet forwarders.

## Benefits

The adoption of GKE Service Steering, coupled with the transition to cloud-native technologies, has the following benefits:

  * **Marketplace offering:** Third Parties can offer their containerized product on Google Cloud Marketplace and use the Service Steering APIs. They can provide a deployment guide based on Kubernetes built-in API provided and managed by GKE.
  * **Kubernetes granularity:** You can control traffic within your Kubernetes cluster. You can classify traffic that you want to steer. You can select workloads where you want Service Steering selectively applied.
  * **Bidirectionality:** GKE's Service Steering is bidirectional in nature. This means that for a given flow, the return path is symmetrical to the forward path. This is important when the Service Functions (SFs) are being deployed as a group of replicas. Ensure that the same flow goes through the same set Replica so as to maintain statefulness.
  * **Multi-Network support:** A majority of Service Functions require multiple Pod interfaces for separation of dataplane from control and management plane. Some Service Functions have multiple interfaces as part of their architecture. GKE's Service Steering includes integration with Multi-Network on Pods. With this, a user can create a Service Steering on a specific Pod-Network.
  * **Raw Packet Delivery to Application:** GKE's Service Steering encapsulates the original packet and delivers it to the Pod directly. This way you don't have to do any decapsulation and your application can act on the original packet directly.



## What's next

  * [Control network traffic flows using Service Steering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-service-steering)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
