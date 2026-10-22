---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-networking-policies/
title: About multi-network network policies \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:55.485591+00:00
---

# About multi-network network policies  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-networking-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About multi-network network policies Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to control the network traffic flow between Pods and Services using firewall rules at the Pod level.

[Network policies for applications](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy) help you define communication traffic rules between Pods. It controls how Pods communicate with each other within their applications and with external endpoints. You can enable network policy on Pod-networks in GKE clusters that have multi-network enabled. You can enforce network policies on additional Pod interfaces that correspond to user-specified Pod-networks.

## Why use multi-network network policies

You might want to use multi-network network policies in the following scenarios:

  * **Enhanced network security** : You want to isolate and protect sensitive workloads or data by defining network policies for specific Pod-networks. Multi-networking network policies limit exposure and reduce the attack surface.

  * **Fine-grained traffic control** : You want to achieve precise control over traffic flow between Pods and Services on different Pod-networks, allowing for complex network topologies and security requirements.

  * **Multi-tenant environments** : You want to create isolated networks for different tenants or applications, which helps ensure that they can't interfere with each other's communication, while maintaining control over network access within each Pod-network.

  * **Optimize resource utilization** : You want to implement network policies on specific Pod-networks to efficiently allocate resources and prioritize traffic based on application requirements, improving performance and reliability.

  * **Security for Containerized Network Functions (CNFs)** : You want to segregate management traffic from dataplane traffic within the same Pod, preventing potential security breaches and unauthorized access.




## How multi-network network policies work with Pod-networks

The following diagram illustrates how network policies, applied to specific Pod-networks using annotations, control traffic flow between Pods within a GKE cluster.

![working of multi-network network policies](https://docs.cloud.google.com/static/kubernetes-engine/images/multinetwork-policies.jpg)

The preceding diagram shows multiple worker nodes running Pods (containerized applications) and how they communicate within the same node or across different nodes using the network infrastructure. It also illustrates the use of network policies to control traffic flow and the segmentation of the network using VPCs and subnets for enhanced security and organization.

  1. **Isolates traffic with targeted Network Policies** : The network policies only affect traffic on the "blue" Pod-network because of the annotation `networking.gke.io/network: blue-Pod-network`. Traffic on the default Pod-network remains unrestricted.
  2. **Enforces one-way traffic with Pod-network policies** : In the preceding diagram, network policies allow Pod1 to send traffic to Pod2 on the "blue" Pod-network. Pod2 can't send traffic back to Pod1 on the same network. The network policy for Pods labeled 'test-app-2' functions as a one-way channel. It specifically allows outgoing traffic only towards Pods labeled 'test-app-3', preventing communication with other Pods like 'test-app-1'.
  3. **Allows outgoing traffic by default** : If no egress policy is defined for a Pod (Pod1 in this example), all outgoing traffic is allowed by default on the "blue" network interface.
  4. **Ensures existing features compatibility** : All standard GKE network policy options like label selectors and IP address blocks work with multi-network network policies.
  5. **Controls network policy scope with annotations** : 
     1. If you create a network policy without annotation, GKE applies multi-network network policies to all network interfaces on the Pods in the selected namespace, regardless of which Pod-networks they are connected to.
     2. If you include the annotation and specify the name of a valid Pod-network (for example, `networking.gke.io/network: blue-Pod-network`), GKE applies the policy to Pods connected to that specific Pod-network.
     3. If the annotation references the Pod-network that doesn't actually exist in your cluster, GKE doesn't apply the network policy to any Pods at all. This is because no Pods are connected to the specified non-existent network.
  6. **Maintains cross-network communication for Pods with multiple network interfaces** : If you apply a network policy to restrict traffic on a specific Pod-network within a Pod, it won't affect the traffic on other Pod-networks connected to the same Pod.



## Benefits

Following are the benefits in using multi-network network policies:

  * **Improved Security** : You can mitigate risks associated with unauthorized access and lateral movement within the GKE cluster by applying network policies at a granular level.

  * **Flexibility and Customization** : You can tailor network policies to meet your specific security and traffic management needs for different Pod-networks by accommodating diverse workloads and applications.

  * **Simplified Network Management** : You can avoid creating excessive Pod-networks and have fine-grained control over communication by using network policies, simplifying network management, and reducing complexity.

  * **Cost Optimization** : By avoiding the need to create numerous Pod-networks, you can optimize resource utilization and reduce costs associated with network infrastructure.

  * **Enhanced Protection for CNFs** : You can ensure the security and integrity of CNF deployments by isolating management and dataplane traffic, and by applying specific network policies to each deployment.




## What's next

  * [Control communication between Pods and Services using network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
