---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-built-in-compute-classes/
title: About built-in ComputeClasses in GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:09.299582+00:00
---

# About built-in ComputeClasses in GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-built-in-compute-classes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About built-in ComputeClasses in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the ComputeClasses that Google Kubernetes Engine (GKE) installs in your clusters. You learn about the name, availability, and node configuration of each built-in ComputeClass. This page is for platform engineers and app operators who want to make an informed choice about which ComputeClasses are available, and which class is optimal for specific workloads.

You should already be familiar with [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes).

## Overview of built-in ComputeClasses

Many GKE workloads are _general-purpose_ workloads that don't require specialized hardware, such as web servers or small-scale batch jobs. For these workloads, the priority is often to reduce the overhead associated with manually managing the node infrastructure and autoscaling configuration.

GKE has various _built-in ComputeClasses_ for use cases such as running [Autopilot workloads in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters) or placing fault-tolerant general-purpose workloads on Spot VMs. Use a built-in ComputeClass for workloads that don't require specific hardware (such as GPUs) or specific node settings (such as Linux sysctl flags). If your workloads need more specialized hardware, use a [custom ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

## Available built-in ComputeClasses in GKE

The following table describes the built-in ComputeClasses that are available in GKE:

Built-in ComputeClasses  
---  
`autopilot` | Create on-demand x86 nodes that use the Autopilot [container-optimized compute platform](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#autopilot-compute-platform). This ComputeClass is the default for Autopilot clusters in any GKE version, but is available for explicit selection in specific GKE versions. This is an _Autopilot ComputeClass_ , which means that GKE manages the nodes for you even in Standard clusters. You can use this ComputeClass to [run Autopilot mode workloads in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters). Available in Autopilot clusters and Standard clusters that run GKE version 1.34.1-gke.1829001 or later.  
`autopilot-spot` | Create Spot VMs that use the Autopilot container-optimized compute platform. This ComputeClass is applied by default to any Pods in Autopilot clusters that explicitly select Spot VMs in the Pod specification. This is an _Autopilot ComputeClass_ , which means that GKE manages the nodes for you even in Standard clusters. You can use this ComputeClass to [run Autopilot mode workloads in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters). Available in Autopilot clusters and Standard clusters that run GKE version 1.34.1-gke.1829001 or later.  
`autopilot-arm` | Create on-demand Arm nodes that use the Autopilot [container-optimized compute platform](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#autopilot-compute-platform). This platform is generation-less, which means that it's not tied to a specific machine family. This distinguishes it from specifying a machine series like C4A, N4A, or T2A. Using the `autopilot-arm` ComputeClass is recommended for general-purpose Arm workloads. Available in Autopilot clusters (GKE version 1.35.3-gke.1389000 or later) and in Standard clusters that use Autopilot ComputeClasses (GKE version 1.36.0-gke.3302001 or later). This feature is only available in the following regions: `us-east1`, `us-west1`, `europe-west1`, `europe-west2`, `europe-west4`, `asia-southeast1`, and `us-central1`.  
`autopilot-arm-spot` | Create Spot VMs that use the Autopilot container-optimized Arm platform. This ComputeClass is recommended for fault-tolerant or batch Arm workloads to optimize costs. Available in Autopilot clusters and Standard clusters that use Autopilot ComputeClasses (GKE version 1.36.0-gke.3302001 or later). This feature is only available in the following regions: `us-east1`, `us-west1`, `europe-west1`, `europe-west2`, `europe-west4`, `asia-southeast1`, and `us-central1`.  
  
To view the specifications of these built-in ComputeClasses, use the `kubectl get` command:
    
    
    kubectl get computeclass COMPUTECLASS_NAME -o yaml
    

## Pricing

Autopilot bills you differently depending on the ComputeClass that your Pods request. For more information, see [Google Kubernetes Engine pricing](https://cloud.google.com/kubernetes-engine/pricing).

## Built-in ComputeClass selection in workloads

To select a built-in or custom ComputeClass when you deploy a GKE workload, you select the `cloud.google.com/compute-class` label in your workload manifest, like in the following example:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: helloweb
      labels:
        app: hello
    spec:
      selector:
        matchLabels:
          app: hello
      template:
        metadata:
          labels:
            app: hello
        spec:
    ** nodeSelector:**
    ** # Replace with the name of a compute class**
    ** cloud.google.com/compute-class: COMPUTE_CLASS **
          containers:
          - name: hello-app
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
            ports:
            - containerPort: 8080
            resources:
              requests:
                cpu: "250m"
                memory: "1Gi"

In this example, `COMPUTE_CLASS` is the name of a compute class. You can't select more that one ComputeClass in a specific workload.

When you deploy a workload that selects a ComputeClass, GKE uses the properties of that ComputeClass to create new nodes to run the Pods. For example, if you select the `autopilot` built-in ComputeClass in a workload, GKE [runs those Pods in Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-classes-standard-clusters).

### Default application of built-in ComputeClasses

You can set any ComputeClass in a cluster as the _default_ ComputeClass for a specific namespace or for an entire cluster. GKE applies that ComputeClass to any Pods that don't explicitly select a different ComputeClass. To set a built-in ComputeClass as the default, you do one of the following:

  * To set the ComputeClass as the namespace default, you add a label for the ComputeClass to the namespace.
  * To set the ComputeClass as the cluster-level default, you create a new ComputeClass that's named `default` and that has the same priority rules as the built-in ComputeClass.



For more information about setting a ComputeClass as the default for a namespace or a cluster, see [Apply ComputeClasses to Pods by default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes).

For example, consider a Standard cluster that runs many general-purpose Pods, such as web servers or small batch Jobs. If you set a ComputeClass that imitates the `autopilot` built-in ComputeClass as the default for the cluster, those general-purpose workloads run on the Autopilot container-optimized compute platform with no changes needed to the workload specifications. Workloads that need different hardware can add a selector for a specific ComputeClass.

## What's next

  * [Learn about best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses)
  * [Read the ComputeClass CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
