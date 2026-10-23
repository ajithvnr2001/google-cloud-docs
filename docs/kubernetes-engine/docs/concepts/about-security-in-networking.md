---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-in-networking/
title: Understand network security in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:52.021913+00:00
---

# Understand network security in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-in-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Understand network security in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains core GKE network security concepts, such as the principle of least privilege, and helps you choose the right tools to secure your cluster. The primary goals of implementing GKE network security are workload isolation and secure multi-tenancy. To achieve these goals, you should apply the principles of least privilege, defense-in-depth, and use actionable data to inform your security decisions.

In Google Kubernetes Engine (GKE), applying the principle of least privilege to network traffic means restricting communication to only what is necessary for your applications to function. By default, the network within a GKE cluster is open, which means every Pod can communicate with every other Pod.

GKE now supports a hierarchical approach to network security by using ClusterNetworkPolicy for administrative-level enforcement across all namespaces.

This document provides information that Operators, Networking specialists, and Security specialists need to understand and implement network security within GKE clusters. For more information about common roles and example tasks in Google Cloud, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this document, verify that you are familiar with the following:

  * **GKE networking concepts** : for an overview, see [About GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-fundamentals).
  * **Kubernetes Pods, Services, and namespaces** : these fundamental Kubernetes resources are central to defining network security policies. See the [Kubernetes documentation](https://kubernetes.io/docs/concepts/).
  * **The principle of least privilege** : this security principle is a core concept applied throughout this document.



## Goals of GKE network security

GKE network security policies provide fine-grained, Kubernetes-aware traffic control within your cluster. These policies are a critical element of your overall security strategy. To implement robust network security, consider these fundamental principles:

  * **Least privilege** : grant systems and services only the minimum privileges required to perform their functions. This principle reduces the potential impact of a compromise. [Kubernetes network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) help you move from a default-open network to one where only necessary connections are allowed.
  * **Defense in depth** : layer multiple, independent security controls. A failure in one control does not lead to a total system compromise. For example, you use a [network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) to isolate a database, even if the database itself requires authentication.
  * **Actionable data** : base security decisions on data. Threat modeling and risk assessment inform your security posture. Features like [network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) provide the data to verify policies and detect potential breaches.



## Choose a network security policy

To choose the right policy, identify the type and scope of the traffic you need to control.

### Types of traffic

To choose the right policy, consider the source and destination of the traffic you want to manage:

  * **Communication between Pods within the cluster** : to control how microservices communicate with each other, use policies that operate on Pod labels and namespaces.

    * As an application developer, use the standard Kubernetes [NetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) to define ingress and egress rules for your application within its namespace.
    * As a cluster administrator, use the standard Kubernetes [ClusterNetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cluster-network-policy) to enforce mandatory security guardrails (`Admin` tier) or establish zero-trust defaults (`Baseline` tier) across all namespaces. This resource is supported on clusters running GKE version 1.36.1-gke.1067000 or later.
    * As a cluster administrator, use the proprietary [CiliumClusterwideNetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cilium-network-policy) for specialized cluster-wide traffic control. For new deployments, use the Kubernetes-native `ClusterNetworkPolicy` instead of this proprietary policy.
  * **Egress traffic from Pods to external services** : to control egress traffic from Pods to external services based on domain names, use [FQDNNetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies). This policy is useful when the IP addresses of external services are not static, because it automatically resolves and updates the allowed IP addresses based on DNS.

  * **Encryption for all service-to-service traffic** : to help ensure all communication between services is encrypted and authenticated, use a service mesh. Use [Istio or Anthos Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs) to implement mutual TLS (mTLS), which automatically handles encryption.




### Policy evaluation tiers

GKE evaluates network security policies in three hierarchical tiers.

  1. **Admin tier (ClusterNetworkPolicy)** : the highest level of precedence. Use this tier to enforce mandatory security mandates. **Deny** rules in this tier override all other policies. **Accept** rules permit traffic and stop evaluation for that packet.
  2. **NetworkPolicy tier** : the tier where developers define application-specific security. Policies include the standard `NetworkPolicy`, `FQDNNetworkPolicy`, and `CiliumClusterwideNetworkPolicy` resources.
  3. **Baseline tier (ClusterNetworkPolicy)** : the lowest level of precedence. Use this tier to set default "deny-by-default" guardrails that developers can selectively override in the NetworkPolicy tier.



If no policies match in any tier, GKE defaults to an implicit "allow all" behavior.

### Summary of policy choices

The following table summarizes which policy to use based on your security goal.

**Goal** | **Recommended policy**  
---|---  
Control traffic between Pods by using labels and namespaces. | [Kubernetes `NetworkPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)  
Control egress traffic to external services by domain name. | [`FQDNNetworkPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies)  
Encrypt and authenticate all service-to-service traffic. | [Istio or Anthos Cloud Service Mesh (for mTLS)](https://docs.cloud.google.com/service-mesh/docs)  
Enforce mandatory, non-overridable security guardrails. | [`ClusterNetworkPolicy` (Admin tier)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cluster-network-policy)  
Establish default "zero-trust" guardrails that developers can override. | [`ClusterNetworkPolicy` (Baseline tier)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cluster-network-policy)  
Configure proprietary cluster-wide policies (not recommended for new deployments). | [`CiliumClusterwideNetworkPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cilium-network-policy)  
Audit and log connections allowed or denied by policies. | [network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) (enabled for any policy)  
  
## Audit and troubleshoot network policies

After implementing network policies, verify that they work as expected and diagnose any connectivity issues. You can use [Network Policy Logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) as the primary tool for this.

When you enable network policy logging, GKE generates a log record in Cloud Logging for every connection that a network policy allows or denies. These logs are essential for performing security auditing and troubleshooting unexpected behavior. Reviewing these logs lets you see the concrete effects of your rules, confirming that legitimate traffic flows as expected and that unauthorized traffic is blocked.

Unlike standard policies which are "allow-only," `ClusterNetworkPolicy` resources support explicit **Deny** actions. If an administrative policy drops traffic, the log record attributes the denial to the specific policy responsible for the block.

## What's next

  * Learn how to [configure a Kubernetes NetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).
  * Learn how to [control egress traffic using an FQDNNetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies).
  * Learn how to [enforce cluster-wide security guardrails using ClusterNetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cluster-network-policy).
  * Learn how to [set up CiliumClusterwideNetworkPolicy for cluster-wide rules](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cilium-network-policy).
  * Learn how to [enable network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) to audit your policies.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
