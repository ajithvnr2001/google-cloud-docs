---
url: https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-overview/
title: About the Managed Lustre CSI driver \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:18.473589+00:00
---

# About the Managed Lustre CSI driver  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  About the Managed Lustre CSI driver Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud Managed Lustre Container Storage Interface (CSI) driver is a GKE-managed solution designed to integrate Google Cloud's high-performance, parallel file system service, [Managed Lustre](https://cloud.google.com/products/managed-lustre), with Google Kubernetes Engine (GKE) clusters. This integration is designed for demanding workloads that require persistent, scalable, and high-throughput storage, particularly those in artificial intelligence (AI), machine learning (ML), and high performance computing (HPC). 

For more information on how you can use Managed Lustre to optimize performance for AI/ML workloads that are deployed on GKE, see the [Optimize AI and ML workloads with Google Cloud Managed Lustre](https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-managed-lustre) reference architecture.

By utilizing the Managed Lustre CSI driver, you can provision, manage, and access Managed Lustre instances directly through standard Kubernetes Persistent Volume Claims (PVCs) and Persistent Volumes (PVs). The driver acts as the control plane, automating the lifecycle management of Managed Lustre instances in response to CSI calls, including creating, deleting, mounting, and unmounting volumes on GKE nodes.

The Managed Lustre CSI driver supports both [dynamically provisioned persistent volumes](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-new-volume) (where the driver creates the Managed Lustre instance based on the PVC) and [statically provisioned persistent volumes](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-existing-instance) (for connecting to pre-existing Managed Lustre instances). It provides an efficient way for your Kubernetes applications to fully use the performance capabilities of Managed Lustre.

## Benefits

The Managed Lustre CSI driver offers several advantages for integrating high-performance storage with your Kubernetes workloads:

  * You gain access to fully Managed Lustre file systems as your workload storage through the [Kubernetes APIs](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api).
  * The driver supports the `ReadWriteMany`, `ReadOnlyMany`, and `ReadWriteOnce` [access modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).
  * You can use the driver to create and connect to new Managed Lustre instances as [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).
  * Your Kubernetes workloads can access existing Managed Lustre instances without requiring the manual installation of any Managed Lustre software, including kernel modules or client utilities.



## Limitations

When using the Managed Lustre CSI driver, be aware of the following limitations:

  * Mounting multiple volumes from different Managed Lustre instances with the same [`filesystem`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances) name on a single node is not supported.
  * Supported operating systems and minimum GKE node versions: 
    * **Container-Optimized OS (COS)** : 
      * x86_64: 1.33.2-gke.1111000 or later
      * ARM: 1.34.1-gke.2541000 or later
    * **Ubuntu** : 
      * x86_64 & ARM: 1.36.0-gke.3302001 or later
  * The Managed Lustre CSI driver does not support custom GKE node images.
  * [Volume expansion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/expand-lustre-volumes) is only supported for GKE cluster versions 1.35.0-gke.2331000 and later. To change the size of a PVC on earlier versions, use one of the following options: 
    * (Recommended) Re-create the PVC with the selected size [`spec.resources.requests.storage` size](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-new-volume#pvc). GKE provisions a new volume with the selected size.
    * Delete the PVC and PV. If the PV's `reclaimPolicy` is `Delete`, the Lustre instance is deleted. To preserve the instance for reuse, patch the [`reclaimPolicy` to `Retain`](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-new-volume#pvc) before deleting.
    * Alternatively, create a new Lustre instance manually with the selected size. Whether reusing an instance or connecting to a new one, use [static provisioning](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-existing-instance) to connect the instance to a new PVC.



## Requirements

To use the Managed Lustre CSI driver, your cluster must meet these requirements:

  * You need GKE cluster and node pool version 1.33.2-gke.1111000 or later.
  * You must have installed the latest version of the Google Cloud CLI, with a minimum supported version of 523.0.0 or later.
  * The CSI driver must be enabled in your GKE cluster. The driver is disabled by default in both Standard and Autopilot clusters. You can enable it during cluster creation or on an existing cluster.
  * Your GKE cluster should run in the same VPC network as the Managed Lustre instance.



## What's next

  * [Create and use a volume backed by a Managed Lustre instance in Google Kubernetes Engine](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-new-volume).
  * [Access an existing Managed Lustre instance from Google Kubernetes Engine](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-existing-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
