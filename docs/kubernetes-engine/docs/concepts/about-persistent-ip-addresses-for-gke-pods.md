---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-persistent-ip-addresses-for-gke-pods/
title: About persistent IP addresses for Pods \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:13.706687+00:00
---

# About persistent IP addresses for Pods  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-persistent-ip-addresses-for-gke-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About persistent IP addresses for Pods Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how you can configure reliable communication by assigning one or more persistent IP addresses to specific Pods in your Google Kubernetes Engine (GKE) clusters. For applications that require high availability, you can also configure these persistent IP addresses to support fast failover or use health-check-based load balancing.

**Note:** The fast failover capability requires [device-type multi-networks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods#terminology-concepts).

In certain cases, where you are running a custom Network Address Translation (NAT) solution, you might want a static persistent IP address for both outgoing and incoming connections, either when the NAT solution initiates the connection or when it receives it. You might also want to have control over the IP addresses allocated to the application for managing how it interacts with other systems or how it handles specific types of requests based on your business requirements.

By default, the Pod uses its interface IP addresses for egressing traffic. Interface IP addresses change when the Pod restarts or gets moved. To have more control over routing communication, you can configure persistent IP addresses manually for your Pods in GKE.

These IP addresses can be either external IP addresses to communicate over the internet or internal IP addresses to communicate within your Google Cloud network. You can either use Google-provided IP addresses or bring your own IP addresses (BYOIP).

By configuring persistent IP addresses for Pods in GKE, you can map application and business logic to allow specific Pods to send and receive traffic to or from any of the persistent IP addresses.

The following diagram illustrates how a Pod with multiple network interfaces can use a Persistent IP address from a secondary network while still communicating on the default network:

Multi network architecture![Multi-network-architecture](https://docs.cloud.google.com/static/kubernetes-engine/images/persistent-IP-architecture.png)

## Terminology and concepts

This page uses the following concepts:

**Health-check-based load balancing**

Use health-checked-based load balancing when you want to distribute traffic from a persistent IP address across multiple active Pods that match a specific label selector. This feature uses regional health checks that you create to constantly monitor Pods and ensure that traffic is only routed to healthy endpoints. You can also configure standby (backup) Pods for the persistent IP address. GKE automatically distributes traffic to these standby Pods only if all primary active Pods fail their health checks. This configuration prevents individual Pods from being overwhelmed during a failure and ensures continuous service availability.

**Gateway classes**

_Gateway classes_ , which manage your persistent IP address assignments, come in the following classes:

  * **gke-persistent-regional-external-managed** for external IP addresses
  * **gke-persistent-regional-internal-managed** for internal (Google Cloud-only) IP addresses
  * **gke-persistent-fast-regional-external-managed** for external IP addresses with fast failover
  * **gke-persistent-fast-regional-internal-managed** for internal (Google Cloud-only) IP addresses with fast failover



The following Gateway classes apply to health-check-based load balancing:

  * **gke-passthrough-lb-internal-managed** for internal (Google Cloud-only) persistent IP addresses that are shared across multiple Pods.
  * **gke-passthrough-lb-external-managed** for external persistent IP addresses that are shared across multiple Pods.

Gateway classes work within specific regions. Gateway classes offer basic IP address management and are focused on Layer 3 (L3) network routing.




The following table compares the capabilities of each Gateway class:

Feature | gke-persistent-* Gateway classes | gke-passthrough-lb-* Gateway classes  
---|---|---  
**Primary goal** | Persistent IP address for a single workload. | Load balancing across multiple workloads.  
**Pod mapping** | 1:1 (routes to the most recently-created matching Pod). | 1:N (distributes traffic to all healthy matching Pods).  
**Health checks** | Not supported for routing decisions. | Required (uses regional health checks).  
**Backup Pods** | Not supported. | Supported (uses standby Pods for failover).  
**Failover speed** | Standard or Fast (uses `*-fast-*` classes). | Configurable with health-check parameters  
  
**Gateway objects**

_Gateway objects_ serve as the central point for managing and configuring persistent IP addresses. Gateway objects in GKE manage a pool of persistent IP addresses. They list these addresses and define rules for how these IP addresses can be assigned to `GKEIPRoute`.

**Listener**

A _Listener_ is a part of your GKE Gateway configuration that controls which Pods across Gateway namespaces can use the persistent IP addresses held by the Gateway. The Listener lets you customize access for flexibility and security. Each Listener needs a unique name and lets you filter access by namespace (all, label-based, or only the Gateway's namespace).

**GKEIPRoute Object**

The _GKEIPRoute_ object is a custom resource which you configure to assign a persistent IP address to a specific Pod in your GKE cluster. You can use the status section of the `GKEIPRoute` object to monitor your persistent IP address setup, which provides key information through the following fields:

  * **Pod**

The _Pod_ field shows you the exact name of the Pod linked to the persistent IP addresses. A single Pod can use multiple persistent IP addresses.

  * **Conditions**

The _Conditions_ field informs whether your external IP address setup is working correctly and can also help diagnose issues if your configuration is not valid. There are four conditions:

    * **`Accepted`:** denotes if the `GKEIPRoute` resource specification is valid. If your configuration has errors, the `Accepted` condition is `False` with a reason.
    * **`GCPReady`:** denotes that Google Cloud has prepared all necessary resources. Errors during the Google Cloud resource provisioning process are reflected in the `GCPReady` condition's status.
    * **`DPV2Ready`:** denotes the status of datapath programming, such as the datapath is ready and programmed to allow network connections on the configured persistent IP addresses.
    * **`Ready`:** denotes that your persistent IP address setup is valid and functional. The Pods can be reached on the persistent IP addresses provided you have configured your application to use it. This is set to `True` when all the other three preceding conditions are also `True`.
  * **`nodeSelector`**

When using fast failover, you must use the `nodeSelector` field to specify which nodes are preconfigured for fast failover. This helps ensure that when a failover occurs, you can quickly bring the new Pod online on a designated node with the persistent IP address. Make sure that you schedule your Pods with persistent IP addresses on these nodes. Typically, you do this by using the Pod's `nodeSelector` to match labels on the nodes. Use the `nodeSelector` field when configuring fast failover, and make sure that the specified labels don't select more than 64 nodes.




The following fields are applicable only to health-check-based load balancing:

  * **`loadBalancing`** : specifies the regional health check name that monitors the health of the Pods.
  * **`backupPodSelector`** : defines the set of Pods that receive traffic if all the primary Pods are unhealthy.



**Reaction Modes**

_Reaction Modes_ determine how the system behaves when the Pod linked to a persistent IP address undergoes changes, such as moving across nodes or when a newly-created matching Pod becomes available. You can use reaction modes to keep your persistent IP addresses usable even as your Pods change.

Reaction modes are one of:

  * **ReadyCondition**

In _ReadyCondition_ mode, the persistent IP address system prioritizes Pod health. The persistent IP address system only assigns IP addresses to Pods that match your specified labels and have passed Kubernetes health probes, signaling their `Ready` status as `True`. This mode is ideal for applications where it's crucial that the Pod receiving the persistent IP address is fully prepared to handle incoming and outgoing traffic.

  * **Exists**

The _Exists_ mode prioritizes the presence of a Pod. The persistent IP address attaches to a Pod if that Pod matches the labels in your configuration and has been scheduled onto a specific node in your cluster. This means the Pod exists and has a designated place to run. This mode is well-suited for scenarios where rapid assignment of the persistent IP address takes priority over strict readiness, or in environments like development and testing where immediate connectivity might be more important than full application health.




**StatefulSets**

_StatefulSets_ are a type of Kubernetes workload designed for applications that need stable identifiers and persistent storage. Pods within a StatefulSet have predictable names (For example: my-app-0, my-app-1).

**Deployments**

_Deployments_ are a type of Kubernetes workload for managing stateless applications where Pods are generally interchangeable. Pod names within Deployments aren't fully predictable.

## Use cases

Persistent IP addresses for GKE Pods address several use cases for network and security service providers running network-related applications on GKE.

Persistent IP addresses for GKE Pods address the following use cases:

  * **Control over NAT:** by assigning persistent IP addresses to Pods running network functions, you get granular control over the source IP addresses used for outbound traffic. This lets you to integrate your proprietary NAT logic.
  * **Dedicated IP address pools:** dedicated IP addresses let you to match specific addresses to individual 5G Core Pods, ensuring compatibility with specialized vendor software.
  * **Reliable Traffic Flows:** since return traffic needs to be routed back through the same network function, persistent IP addresses ensure that external systems recognize and respond to the correct Pod without breaks in communication.
  * **High availability for time-sensitive applications:** for applications with strict uptime requirements, such as in the telecommunications industry, you can use persistent IP addresses with fast failover to quickly redirect traffic to a healthy Pod in the event of a failure, which can minimize the downtime to only a few seconds.
  * **Load distribution:** when you use health-check-based load balancing, GKE distributes traffic across multiple active Pods to avoid overloading a single instance. If no healthy Pods are available, you can configure backup Pods in different namespaces or nodes.



## Benefits

Persistent IP addresses for GKE Pods provide you the following benefits:

  * **External Identity:** if you give a Pod an external persistent IP address, external systems can consistently reach that Pod, even if it gets restarted or moved within the cluster. This is helpful for services that need an externally discoverable endpoint.
  * **Reliable Communication:** applications that depend on other resources with specific IP addresses can reliably establish connections using persistent IP addresses. Persistent IP addresses are important for legacy systems or applications with hardcoded IP address dependencies.
  * **Legacy migrations** : legacy migrations can assist in migrating applications that rely on having specific IP addresses during the transition process.
  * **BYOIP** : BYOIP lets you maintain control over specific IP address ranges you already own by using them within your GKE clusters.
  * **Improved application uptime** : with the fast failover capability, you can significantly improve the uptime of your critical applications by minimizing downtime to only a few seconds in the event of a Pod failure.
  * **High availability with automatic failover** : achieve service availability by automatically redirecting traffic to healthy standby Pods when primary Pods fail health checks.



## What's next

  * [Control communication with persistent IP addresses on GKE Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-persistent-ip-addresses-on-gke-pods)
  * Learn how to set up [health-check-based load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/health-check-based-load-balancing)
  * Read [About multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods)
  * Read [Set up multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
