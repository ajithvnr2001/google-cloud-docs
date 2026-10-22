---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode/
title: About GKE modes of operation \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:53.957887+00:00
---

# About GKE modes of operation  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About GKE modes of operation Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page helps you to choose the Google Kubernetes Engine (GKE) _mode of operation_ that's the best fit for your requirements. This information is intended for the following people:

  * Application developers who want to run containerized workloads optimally based on workload requirements.
  * Platform administrators who want to know about the recommended methods to use GKE.



If you want to learn about whether GKE as a _platform_ is the best choice for your containerized applications, refer to the [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) and [GKE and Cloud Run](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-and-cloud-run).

## Introduction to Autopilot mode and Standard mode

GKE lets you choose one of the following _modes of operation_ , which determines factors like who manages the infrastructure, how you're billed for resources, and how much flexibility you have:

  * **Autopilot (recommended)** : a managed experience in which GKE handles most of your infrastructure for you so that you can focus on your applications. Autopilot is optimized for most production scenarios and implements many of Google's best practices for security, scaling, and workloads.

For more information, see [About GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).

  * **Standard** : a flexible experience in which you have direct control over your node infrastructure and autoscaling.




You can use either of these modes of operation to run your GKE workloads or to operate entire GKE clusters, as described in the following sections.

## Autopilot and Standard mode for workloads

**Best Practice** : 

Use Autopilot for most workloads, unless your application requires privileges or configuration options that don't meet the Autopilot constraints.

You can run your workloads in Autopilot or Standard, depending on your use case and on the requirements of the workload. The following table describes the differences between Autopilot workloads and and Standard workloads:

**Table 1.** Comparison of Autopilot and Standard workloads Autopilot workloads | Standard workloads  
---|---  
Ideal for most production workloads. | Ideal for workloads that require special privileges, or for when you need granular control over your workload infrastructure.  
GKE provisions compute resources based on your Kubernetes workload specifications. | You manage resource allocation and the placement of Pods on specific nodes.  
Autopilot workloads can use the Autopilot [_container-optimized compute platform_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#autopilot-compute-platform), which is a scalable, cost-efficient platform that works well for most general-purpose workloads. | You must plan the capacity of nodes in Standard node pools based on your workload requirements. You must also configure settings for scaling your node sizes and quantity.  
GKE maximizes node resource usage by [_bin-packing_](https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/) Pods onto nodes. | You plan workload placement based on the size of the nodes that you create. To minimize wasted node resources, you must also manage effective bin-packing of Pods.  
GKE applies many best practice configurations and constraints by default, such as preventing privileged Pods. | You can configure Pods in any way that you want, such as by enabling privileged mode.  
You can run Autopilot workloads in Autopilot clusters or in Standard clusters. | You can run Standard workloads in only Standard clusters.  
  
Workloads run in Autopilot or Standard mode depending on the workload and cluster configuration, as follows:

  * **Autopilot workloads** : if your cluster is an Autopilot cluster, every workload runs in Autopilot mode. If your cluster is a Standard cluster, you can run specific workloads in Autopilot mode.
  * **Standard workloads** : if you create a workload in a Standard cluster, the workload uses Standard mode unless Autopilot mode is selected for that workload.



### About Autopilot workloads in Standard clusters

You can run workloads in Autopilot mode in your Standard clusters, which lets you have granular control over your cluster settings and node pool infrastructure while also getting many of the automation, scaling, and pricing benefits of Autopilot for a subset of your applications.

Run Autopilot workloads in Standard clusters when you need the flexibility of a Standard mode cluster, but you also have workloads that can benefit from the cost-efficiency and automation of Autopilot mode.

To run Autopilot workloads in a Standard cluster, you use a _compute class_ , which is a GKE feature that lets you declaratively control node configuration options during scaling. GKE manages bin-packing, resource scaling, and the underlying infrastructure for the Autopilot workloads that you run in your Standard cluster.

For more information, see [About Autopilot workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters).

## Autopilot and Standard mode for clusters

To run workloads in GKE, you create a GKE cluster. Similarly to selecting a mode for your workloads, you can use Autopilot or Standard mode to operate your entire cluster. The mode that you use for the cluster affects how much flexibility and control you have over your infrastructure and cluster settings, as follows:

**Table 2.** Comparison of cluster modes Autopilot clusters | Standard clusters  
---|---  
GKE manages the cluster infrastructure, including nodes and scaling. GKE configures various settings by default, such as security constraints. | You control the cluster infrastructure and can change most settings. In Standard clusters, you can configure your own _node pools_ , which are groups of nodes that share characteristics. You also configure node settings, security policies and constraints, and scaling.  
Autopilot clusters are pre-configured with Google's best practices and run only Autopilot workloads. | Standard clusters can run both Autopilot and Standard workloads.  
  
For more information about the detailed differences between Autopilot and Standard clusters, see [Compare features in Autopilot and Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison).

Unless you require the granular control and flexibility of Standard clusters, we recommend that you use Autopilot clusters. For an interactive walkthrough that sets up an Autopilot cluster and creates a `hello-world` application, go to the Autopilot walkthrough in the Google Cloud console:

[Go to walkthrough](https://console.cloud.google.com/welcome?walkthrough_id=gke_autopilot)

## Pricing

In GKE, the mode of operation that you use affects the charges that you incur. For more information, see [Google Kubernetes Engine pricing](https://cloud.google.com/kubernetes-engine/pricing).

## What's next

  * [View a detailed comparison between Autopilot and Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison)
  * [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster)
  * [Learn about GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
  * [Learn more about Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
