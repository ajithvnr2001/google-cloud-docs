---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hypercluster-overview/
title: About GKE Hypercluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:33.569754+00:00
---

# About GKE Hypercluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hypercluster-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About GKE Hypercluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** GKE Hypercluster is available only to specific eligible GKE customers, and isn't intended for most production AI/ML workloads. To check your eligibility and to request access to this feature, contact your dedicated account team.

Many GKE customers run large-scale AI/ML workloads or own sensitive intellectual property (IP) such as proprietary model weights. This document describes an infrastructure architecture that runs containers on remote instances that can run in multiple regions and are managed by nodes in your cluster. This linked infrastructure, including the various operating system (OS) images and features, is named _GKE Hypercluster_.

GKE Hypercluster is intended for customers who want security and scalability beyond the limits of GKE or AI Hypercomputer, and are willing to accept increased operational friction to achieve those goals.

## When to use GKE Hypercluster

By default, GKE clusters are designed to meet the requirements of most production AI workloads, including workloads that have special security and scalability requirements. For example, GKE supports use cases like the following:

  * Run GPUs on Confidential Google Kubernetes Engine Nodes and access vTPMs or hardware-based Confidential Computing modules from your workloads.
  * Use Workload Identity Federation for GKE to restrict access to encrypted data to specific authorized identities.
  * Deploy TPU and GPU nodes based on available capacity by using ComputeClasses and node pool auto-creation.
  * Control and observe any access by Google personnel by using [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview), [Access Transparency](https://docs.cloud.google.com/security/products/access-transparency), and [GKE control plane authority](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority).



The linked infrastructure in GKE Hypercluster is designed for specific security and scalability use cases that require capabilities that are beyond the existing limits of the typical GKE architecture. By design, certain GKE observability, troubleshooting capabilities, and features aren't available for the linked infrastructure. This infrastructure modifies the typical GKE cluster architecture to meet the following specialized use cases:

  * **Protect models and queries from insider threats** : prevent access to proprietary model weights or sensitive inference queries and responses from your own platform administrators and Google personnel. AI assets are decrypted only in attested and verifiable environments.

  * **Run AI workloads across regions** : deploy workloads at a scale that's beyond the [supported node scaling limits](https://docs.cloud.google.com/kubernetes-engine/quotas#limits_per_cluster). Create and use accelerator infrastructure in any region that has available capacity, including in locations outside of the cluster region or zone.




## How it works

As described in [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture), a Standard mode cluster has a regional or zonal control plane that serves the Kubernetes API and manages all of the nodes and node pools in the cluster. All of the nodes in a cluster use a specific VPC network, which might also be used by other Google Cloud resources. Every GKE node runs various system components like `kubelet` node agents, logging and metrics agents, and other Kubernetes and GKE components.

In contrast, GKE Hypercluster uses instances named _linked runners_ that aren't registered as `Node` objects in the Kubernetes API server. These instances have the following properties:

  * No Kubernetes agents and a minimal set of GKE components.
  * Specialized OS images based on use case. No GKE node images.
  * The instances use a separate, dedicated VPC network.



The linked runners are managed by _control nodes_ in the cluster that link the runner with the cluster. The control nodes run system components like the `kubelet` processes. A single control node can link with multiple runners. These linked runners are designed for running workloads at a very large scale, such as a training Job that requires more power than the data center in your cluster region can provide.

During infrastructure setup, you create runners with a specific configuration based on your use case, and then link the instances to dedicated control nodes in your cluster. The Kubernetes API needs to manage only the control nodes, because the linked runner instances don't have a `kubelet` and don't generate API server traffic. When you create your linked runner instances, you can configure the instances in one of the following ways:

  * **Default configuration**: by default, the linked instances are Compute Engine VMs that run a Container-Optimized OS image. Platform administrators and emergency personnel like SREs can access the instances by using SSH. These instances work well for when you want to maintain administrator access to the infrastructure.
  * **Sealed configuration**: some AI workloads process sensitive data, such as proprietary model weights and encrypted queries. In situations where you need to protect your AI assets from all access, including from Google personnel and your own administrators, you can configure your linked runner instances in _sealed mode_. These sealed instances have the following properties: 
    * Use a minimal OS image.
    * Use the Titanium Intelligence enclave for TPUs and NVIDIA Confidential Computing for GPUs.
    * Perform workload-level and firmware attestation.
    * Validate container image signatures.
    * Prevent all administrative access to instances and containers.



Regardless of the configuration that you use, the instances don't include many of the components and features that are included in GKE nodes, such as GKE-specific TPU runtime parameters or GKE logging and monitoring agents.

### About the default configuration

By default, the instances that you create for GKE Hypercluster are designed for running production workloads while providing similar mechanisms to typical GKE nodes for troubleshooting and emergency response purposes. The instances run on Compute Engine machine types and use a Container-Optimized OS image. During incidents like disruptions or crashes, your administrators can directly access the instances to troubleshoot issues. Unlike Kubernetes nodes, the instances don't run many of the system components that enable Kubernetes and GKE features, which results in more allocatable resources on each instance.

You can create instances in any Google Cloud region and then link those instances to control nodes in your cluster. The control nodes perform many of the functions of the Kubernetes control plane, managing the lifecycle of deployed workloads.

### About the sealed configuration

If your primary use case is to protect your assets from all access, then you can configure your linked runners to use a sealed configuration, which results in instances that have the following security properties:

  * Each instance is a Trusted Execution Environment (TEE) that's based on specific technologies: 
    * TPUs use the Titanium Intelligence enclave, which is part of the [Private AI Compute](https://services.google.com/fh/files/misc/private_ai_compute_technical_brief.pdf) platform.
    * GPUs use [NVIDIA Confidential Computing](https://www.nvidia.com/en-us/data-center/solutions/confidential-computing/) to protect data while in-use.
  * The instances run a minimal OS image, based on Container-Optimized OS, that disables SSH access, prevents container shell access, and runs an attestation agent.
  * You define a policy that specifies exactly which workloads can run on the instances. For example, you can require workloads to use signed container image digests or to have a specific Pod specification.
  * An attestation agent sends firmware and workload measurements to Google Cloud Attestation and returns verifiable attestation claims results tokens.



The resulting instances provide restricted, validated environments in which only approved code can run and sensitive data is processed on hardware-based secure enclaves. The attestation information that's returned by the instances verifies that workloads run approved code and are deployed on the correct instances.

You can use these sealed instances to protect your encrypted models, queries, and responses in the following ways:

  * **Model weights** :

    1. Encrypt model weights by using a Cloud HSM key in Cloud KMS.
    2. Store encrypted model weights in Cloud Storage.
    3. Give read access to the bucket only to attested workloads.
    4. Give decryption key access only to attested workloads.
  * **Queries and responses** :

    1. Encrypt queries and responses by using an Cloud HSM key in Cloud KMS.
    2. Give decryption access only to attested workloads.
    3. Require proof of attestation when sending encrypted data between workloads.



The sealed configuration is an optional layer of security for your linked runner instances. Similarly to the default configuration, you can create the sealed instances in any region and zone. However, the security properties of the sealed instances mean that administrators and Google personnel can't access host instances for troubleshooting.

## Eligibility

GKE Hypercluster is designed for specific AI/ML use cases that can't be satisfied by the typical GKE cluster architecture and features. Customers who use GKE Hypercluster have atypical security and scalability requirements. GKE Hypercluster is available only to eligible GKE customers. To check whether you're eligible and to request access, contact your dedicated account team.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
