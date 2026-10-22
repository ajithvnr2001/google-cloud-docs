---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/k8s-network-policy/k8s-network-policy-overview/
title: Overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:11.395431+00:00
---

# Overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/k8s-network-policy/k8s-network-policy-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of how to use standard Kubernetes network policies to control network traffic within a cluster in Google Distributed Cloud (GDC) air-gapped.

A [Kubernetes network policy](https://kubernetes.io/docs/concepts/services-networking/network-policies) is a standard, namespaced resource that controls traffic flow at the IP address or port level (Layer 3 or 4). Network policies use pod labels to select pods, and define rules that specify what traffic is allowed to and from those pods.

In GDC, network policy resources created within a cluster are restricted to that cluster's scope only. You can use network policy resources to define rules for traffic between pods and namespaces within that same cluster, but you can't use their label selectors to select pods or namespaces in other clusters. To control traffic between clusters, you must use a `ProjectNetworkPolicy`. For more information, see [PNP Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview). You can also use the `ipBlock` field in a Kubernetes `NetworkPolicy` to control organization-external traffic and traffic to and from specific nodes in the cluster.

## Security and connectivity

The default behavior is inherited from the project. If the base `ProjectNetworkPolicy` is present, traffic from within the project is allowed by default, and all other traffic is denied. Otherwise, traffic is denied by default.

GDC network policies are additive. When multiple policies select the same pod, their rules are combined. Traffic is allowed if it matches the rules in at least one of the applicable policies.

## Prepare predefined roles and access

To configure Kubernetes network policies, you must have the necessary identity and access roles:

  * K8s Network Policy Admin: Manages Kubernetes network policies. Ask your Organization IAM Admin to grant you this cluster role.



## Target cluster nodes using IP blocks

**Preview:** Targeting specific cluster nodes using the `ipBlock` field is a Preview feature that is available as-is and is not recommended for production environments. Google provides no Service Level Agreements (SLA) or technical support commitments for Preview features. For more information, see [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview).

You can use the `ipBlock` field in a `NetworkPolicy` resource to specify individual node IP addresses or node CIDR ranges and control traffic to and from specific nodes in a standard cluster. Common use cases include:

  * **Webhook ingress from control plane nodes** : Allow ingress traffic from cluster control plane (API server) nodes to a pod running a custom Kubernetes admission webhook.
  * **Pod egress restricted to control plane nodes** : Allow egress traffic from a pod to cluster control plane (API server) nodes while default-deny rules block egress traffic to worker nodes.



For instructions, see [Create an intra-cluster node policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/k8s-network-policy/standard-cluster-traffic#create-node-policy).

## What's next

  * [Create Kubernetes network policies for standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/k8s-network-policy/standard-cluster-traffic)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
