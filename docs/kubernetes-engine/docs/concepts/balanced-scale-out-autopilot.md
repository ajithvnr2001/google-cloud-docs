---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/balanced-scale-out-autopilot/
title: About Balanced and Scale-Out ComputeClasses in Autopilot clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:10.192536+00:00
---

# About Balanced and Scale-Out ComputeClasses in Autopilot clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/balanced-scale-out-autopilot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About Balanced and Scale-Out ComputeClasses in Autopilot clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

You can use the `Balanced` and `Scale-Out` _ComputeClasses_ in Google Kubernetes Engine (GKE) Autopilot clusters to run workloads that require extra compute capacity or specialized CPU configurations. This page is intended for cluster administrators who want more flexible compute options than the default Autopilot cluster configuration provides.

## Overview of Balanced and Scale-Out ComputeClasses

By default, Pods in GKE Autopilot clusters run on a _container-optimized compute platform_. This platform is ideal for general-purpose workloads such as web servers and medium-intensity batch jobs. The container-optimized compute platform provides a reliable, scalable, cost-optimized hardware configuration that can handle the requirements of most workloads.

If you have workloads that have unique hardware requirements (such as performing machine learning or AI tasks, running real-time high traffic databases, or needing specific CPU platforms and architecture) you can use [_ComputeClasses_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes) to provision that hardware.

In Autopilot clusters only, GKE provides the following curated ComputeClasses that let you run Pods that need more flexibility than the default container-optimized compute platform:

  * `Balanced`: provides higher maximum CPU and memory capacity than the container-optimized compute platform.
  * `Scale-Out`: disables simultaneous multi-threading (SMT) and is optimized for scaling out.



These ComputeClasses are available in only Autopilot clusters. Similar to the default container-optimized compute platform, Autopilot manages node sizing and resource allocation based on your running Pods.

### Custom ComputeClasses for additional flexibility

If the Balanced or Scale-Out ComputeClasses in Autopilot clusters don't meet your workload requirements, you can configure [your own ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes). You deploy ComputeClass Kubernetes custom resources to your clusters with sets of node attributes that GKE uses to configure new nodes in the cluster. These custom ComputeClasses can, for example, let you deploy workloads on the same hardware as the `Balanced` or `Scale-Out` ComputeClasses in any GKE Autopilot or Standard cluster. For more information, see [About Autopilot mode workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters).

## Pricing

Pods that use the `Balanced` or `Scale-Out` ComputeClasses are billed based on the following SKUs:

  * [`Autopilot Balanced`](https://cloud.google.com/skus?filter=Autopilot%20Balanced)
  * [`Autopilot Scale-Out`](https://cloud.google.com/skus?filter=Autopilot%20Scale-Out)



For more information, see [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing).

## Balanced and Scale-Out technical details

This section describes the machine types and use cases for the `Balanced` and `Scale-Out` classes. If you don't request a ComputeClass in your Pods, Autopilot places the Pods on the container-optimized compute platform by default. The container-optimized compute platform uses any of the machine series from the Compute Engine [general-purpose machine family](https://docs.cloud.google.com/compute/docs/general-purpose-machines) with a preference for resizable machine types. Because the underlying machine series isn't fixed, per-CPU performance varies depending on which machine series GKE schedules your Pod on.

Additionally, scheduling for Pods with attached persistent storage depends on disk type compatibility:

  * **Legacy Persistent Disks** : Pods with attached legacy Persistent Disks (such as `pd-standard`) run only on machine series that support them, such as `E2`.
  * **Hyperdisk** : Pods with attached next-generation storage (such as `hyperdisk-balanced`) run on newer machine series, such as `C3`.
  * **Pending state** : If you explicitly configure a Pod to run on a newer machine series (for example, by using node selectors to request `C3` nodes, or by configuring a custom ComputeClass) but attach a legacy Persistent Disk, the Pod remains in the `Pending` state indefinitely. This occurs because GKE cannot find a node that satisfies both the machine type and disk compatibility constraints. When you explicitly select a machine series, you are responsible for ensuring PersistentVolume and disk compatibility.



The following table provides a technical overview of the `Balanced` and `Scale-Out` ComputeClasses.

**Note:** The machine types that back each ComputeClass might change over time.Balanced and Scale-Out ComputeClasses |   
---|---  
`Balanced` | Provides more CPU capacity and memory capacity than the [container-optimized compute platform maximums](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#min-max-requests). Provides additional CPU platforms and the ability to set [minimum CPU platforms](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform) for Pods, such as Intel Ice Lake or later.

  * **Available CPUs** : AMD EPYC Milan, Intel Ice Lake, Intel Cascade Lake
  * **Available architecture** : amd64
  * **Machine series** : [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series) (Intel CPUs) or [N2D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines) (AMD CPUs).

Use the `Balanced` class for applications such as the following:

  * Web servers
  * Medium to large databases
  * Caching
  * Streaming and media serving
  * Hyperdisk Throughput and Extreme storage

  
`Scale-Out` | Provides single-thread-per-core computing and horizontal scaling.

  * **Available CPUs** : Ampere Altra Arm or AMD EPYC Milan
  * **Available architecture** : arm64 or amd64
  * **Machine series** : [T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) (Arm) or [T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines) (x86).
  * **Additional features** : 
    * SMT is disabled, so one vCPU is equal to one physical core.
    * 3.5GHz maximum clock speed.

Use the `Scale-Out` class for applications such as the following:

  * Web servers
  * Containerized microservices
  * Data log processing
  * Large-scale Java apps
  * Hyperdisk Throughput storage

  
  
## ComputeClass selection in workloads

To use a ComputeClass for a GKE workload, you select the ComputeClass in the workload manifest by using a [node selector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) for the `cloud.google.com/compute-class` label.

The following example Deployment manifest selects a ComputeClass:
    
    
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

Replace `COMPUTE_CLASS` with the name of a ComputeClass, such as `Balanced` or `Scale-Out`. You can select a maximum of one ComputeClass in a workload.

When you deploy the workload, GKE does the following:

  * Automatically provisions nodes backed by the specified configuration to run your Pods.
  * Automatically adds node labels and [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to the new nodes to prevent other Pods from scheduling on those nodes. The taints are unique to each ComputeClass. If you also select a CPU architecture, GKE adds a separate taint unique to that architecture.
  * Automatically adds tolerations corresponding to the applied taints to your deployed Pods, which lets GKE place those Pods on the new nodes.



For example, if you request the `Scale-Out` ComputeClass for a Pod:

  1. Autopilot adds a taint specific to `Scale-Out` for those nodes.
  2. Autopilot adds a toleration for that taint to the `Scale-Out` Pods.



Pods that don't request `Scale-Out` won't get the toleration. As a result, GKE won't schedule those Pods on the `Scale-Out` nodes.

If you don't explicitly request a ComputeClass in your workload specification, Autopilot schedules Pods on nodes that use the default container-optimized compute platform. Most general-purpose workloads can run with no issues on this platform.

If you use ComputeClasses or request specific machine series, ensure that your workloads don't use incompatible storage. For example, don't use earlier Persistent Disk volume types, such as standard Persistent Disk (`pd-standard`) or SSD Persistent Disk (`pd-ssd`) volumes, on machine series that don't support them. Using incompatible storage can cause Pods to remain in the `Pending` state if GKE can't find or provision a node that satisfies all constraints. If a Pod is scheduled but the storage fails to attach or mount, the Pod remains in the `ContainerCreating` state. For more information about troubleshooting storage compatibility, see [Workload scheduled on older machine series or stuck in `Pending` state due to storage incompatibility](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-clusters#storage-incompatibility-scheduling).

## How to request a CPU architecture

In some cases, your workloads might be built for a specific architecture, such as [Arm](https://www.arm.com/architecture). The Scale-Out ComputeClass supports multiple CPU architectures. You can request a specific architecture alongside your ComputeClass request by specifying a label in your node selector or node affinity rule, such as in the following example:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-arm
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx-arm
      template:
        metadata:
          labels:
            app: nginx-arm
        spec:
          **nodeSelector :
            cloud.google.com/compute-class: COMPUTE_CLASS
            kubernetes.io/arch: ARCHITECTURE**
          containers:
          - name: nginx-arm
            image: nginx
            resources:
              requests:
                cpu: 2000m
                memory: 2Gi
    

Replace `ARCHITECTURE` with the CPU architecture that you want, such as `arm64` or `amd64`. You can select a maximum of one architecture in your workload. The ComputeClass that you select must support your specified architecture.

If you don't explicitly request an architecture, Autopilot uses the default architecture of the ComputeClass.

### Arm architecture on Autopilot

Autopilot supports requests for nodes that use the Arm CPU architecture. Arm nodes are more cost-efficient than similar x86 nodes while delivering performance improvements. For instructions to request Arm nodes, refer to [Deploy Autopilot workloads on Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads).

Ensure that you're using the correct images in your deployments. If your Pods use Arm images and you don't request Arm nodes, Autopilot schedules the Pods on x86 nodes and the Pods will crash. Similarly, if you accidentally use x86 images but request Arm nodes for the Pods, the Pods will crash.

## Default, minimum, and maximum resource requests

When choosing a ComputeClass for your Autopilot workloads, make sure that you specify resource requests that meet the minimum and maximum requests for that ComputeClass. For information about the default requests, as well as the minimum and maximum requests for each ComputeClass, refer to [Resource requests and limits in GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).

## What's next

  * [Learn about best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses).
  * [Learn how to select specific ComputeClasses in your Autopilot workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-compute-classes).
  * [Read about the default, minimum, and maximum resource requests for each platform](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
