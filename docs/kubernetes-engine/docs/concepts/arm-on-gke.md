---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke/
title: Arm workloads on GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:03.164275+00:00
---

# Arm workloads on GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Arm workloads on GKE Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This document explains how to run Arm workloads on Google Kubernetes Engine (GKE). You can run Arm workloads in the following ways:

  * **GKE Autopilot mode** : on the Autopilot container-optimized compute platform, explicitly request the Arm architecture and the `autopilot-arm` ComputeClass for general-purpose workloads. To request specific hardware, use the `Performance` or `Scale-Out` [compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes#when-to-use).
  * **GKE Standard mode** : using the [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series), [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series), or [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) machine series.



You can run single-architecture Arm images or multi-architecture (multi-arch) images compatible with both x86 and Arm processors. To learn about the benefits of Arm, see [Arm VMs on Compute](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute).

## Run Arm workloads on GKE

See the following for more information about choosing workloads to deploy on Arm and preparing those workloads for deployment:

  * **Choosing workloads to run on Arm** : Consider the benefits of the following options when choosing workloads to run on Arm:

    * **Autopilot container-optimized compute platform** : Recommended for general-purpose Arm workloads in Autopilot clusters, providing Pod-based billing and elasticity without requiring you to manage specific machine types.
    * **Specific machine families** : For workloads requiring specific hardware characteristics, consider the following machine types. For more information, see the table in [General-purpose machine family for Compute Engine](https://docs.cloud.google.com/compute/docs/general-purpose-machines):

      * C4A nodes provide Arm-based compute which achieves consistently high performance for your most performance-sensitive Arm-based workloads.
      * N4A nodes provide Arm-based compute that balances price and performance.
      * T2A nodes are appropriate for more-flexible workloads, or workloads which rely on horizontal scale-out.
  * **Deploying across architectures** : With GKE, you can use multi-arch images to deploy one image manifest across nodes with different architectures, including Arm.

    * To ensure that your container image is Arm-compatible and can run on your targeted architectures, see [Build multi-architecture images for Arm workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm).
    * To follow a tutorial for using multi-arch images to deploy across architectures, see [Migrate x86 application on GKE to multi-arch with Arm](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrate-x86-to-multi-arch-arm).
  * **Preparing Arm workloads for deployment** : Once you have an Arm-compatible image, use [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) rules and [node selectors](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) to make sure your workload is scheduled to nodes with a compatible architecture type.

    * **Autopilot clusters** : see [Deploy Autopilot workloads on Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads).
    * **Standard clusters** : see [Prepare an Arm workload for deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment).



## Requirements and limitations

  * Arm nodes are available in Google Cloud locations that support Arm architecture. For details, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * The `general-purpose-arm` pod family and `autopilot-arm` compute class are only available in the following regions: `us-east1`, `us-west1`, `europe-west1`, `europe-west2`, `europe-west4`, `asia-southeast1`, and `us-central1`.
  * [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) and [Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview) are not supported on clusters with Arm node pools.
  * See the following requirements and limitations for the C4A virtual machines (VMs) and [bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#c4a-metal), respectively: 
    * C4A VMs: 
      * To create a cluster that uses [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) mode, [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning), or [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes) that auto-create node pools, use the following versions or later: 
        * 1.30.7-gke.1136000
        * 1.31.3-gke.1056000
      * To create a Standard cluster, use 1.30.4-gke.1213000 or later.
      * To use [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd), use the following versions or later: 
        * 1.30.12-gke.1033000
        * 1.31.8-gke.1045000
        * 1.32.1-gke.1357000
      * GKE doesn't support the following features with C4A VMs: 
        * [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)
        * [Compact placement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement)
        * [Simultaneous multi-threading (SMT)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-smt)
        * [Persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) (use [Hyperdisk](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk) instead, see [Supported disk types for C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4a))
        * [Nested virtualization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization)
        * [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)
    * C4A bare metal instances, including `c4a-standard-96-metal` and `c4a-highmem-96-metal`: 
      * To create a Standard node pool, use version 1.35.0-gke.2232000 or later.
      * In addition to the limitations of the C4A VMs, GKE doesn't support the following features with C4A bare metal instances: 
        * [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd).
        * Provisioning the bare metal instance through [optimizing Autopilot Pod performance by choosing a machine series](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods), because you can't explicitly select the machine type.
        * Live migration. For more information, see [Manage disruption to GKE nodes that don't live migrate](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).
      * To create a cluster that uses `c4a-highmem-96-metal` and [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) mode, [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#cluster-level-enablement), or [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes) that auto-create node pools, use version 1.35.3-gke.1389000 or later. `c4a-standard-96-metal` isn't supported with these features. The following also applies: 
        * To [configure auto-created node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#configure-common-scenarios) that use `c4a-highmem-96-metal`, you must explicitly specify the machine type. If you specify only the C4A machine series, and not the machine type, GKE provisions C4A VMs, not bare metal instances. This behavior is true for both node auto-provisioning, and ComputeClasses that auto-create node pools.
  * See the following requirements and limitations for N4A:

    * To create a cluster with N4A nodes that uses [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) mode, use GKE version 1.34.1-gke.3403001 or later.
    * GKE doesn't support the following features with N4A nodes:

      * [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd)
      * [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)
      * [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)
      * [Compact placement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement)
      * [Simultaneous multi-threading (SMT)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-smt)
      * [Persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) (use [Hyperdisk](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk) instead, see [Supported disk types for N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_n4a))
      * [Nested virtualization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization)
      * [1 GB hugepages](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#transparent-hugepage) (only 2 MB hugepages supported)
  * See the following requirements and limitations for T2A:

    * GKE doesn't support the following features with T2A nodes:

      * [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)
      * [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)
      * [GKE Windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/windows-server-gke)
      * [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd)
      * [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller), [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview), and [Config Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview)



## What's next

  * [Create clusters and node pools with Arm nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes)
  * [Build multi-architecture images for Arm workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm)
  * [Prepare an Arm workload for deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment)
  * [Migrate x86 application on GKE to multi-arch with Arm](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrate-x86-to-multi-arch-arm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
