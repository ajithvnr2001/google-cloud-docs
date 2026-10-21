---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-overview/
title: Cloud TPU deployments overview \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:45.405291+00:00
---

# Cloud TPU deployments overview  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Cloud TPU deployments overview Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the core concepts and advanced configurations available when you use Cluster Toolkit to deploy Google Kubernetes Engine (GKE) clusters with dedicated Cloud TPU node pools.

When you use Cluster Toolkit to provision Google Kubernetes Engine (GKE) clusters, you can deploy dedicated Cloud TPU node pools designed for artificial intelligence (AI) and machine learning (ML) workloads. Cluster Toolkit provides blueprints to automate the deployment of various supported Cloud TPU architectures.

## Key concepts for Cloud TPU deployments in Cluster Toolkit

To deploy a Cloud TPU cluster, you must understand how Cloud TPU hardware is grouped and allocated. You create Cloud TPU slices as a single, fixed hardware unit with physical, high-speed interconnects between all nodes.

### Cloud TPU in GKE

Cloud TPU is Google's custom-developed Application-Specific Integrated Circuit (ASIC) that is used to accelerate machine learning workloads. GKE provides full support for Cloud TPU node and node pool lifecycle management, including node creation, configuration, and automatic upgrades.

For more information about how Cloud TPU works with GKE, see [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).

### TPU slices

A Cloud TPU slice is a collection of Cloud TPU chips that are physically connected by a dedicated, ultra-low-latency network called the Inter-Chip Interconnect (ICI). This interconnect lets the nodes function as a single supercomputer.

In Cluster Toolkit, the `num_slices` parameter specifies the number of identical, independent Cloud TPU slices to create. Each slice corresponds to an individual node pool.

### TPU topologies

The `tpu_topology` parameter defines the shape and total size of your Cloud TPU slice. Topologies describe the number and physical arrangement of the Cloud TPU chips in a slice.

  * **Cloud TPU v6e** chips are arranged in a 2D torus topology, such as `2x4`.
  * **Cloud TPU 7x** chips have a direct connection to the nearest neighboring chips in 3 dimensions, forming a 3D torus interconnect topology, such as `2x2x1`.



The numbers in the topology represent the number of chips along each dimension of the TPU slice.

For more information about the architecture and configurations of these TPUs, see [Cloud TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e#configurations) and [Cloud TPU 7x](https://docs.cloud.google.com/tpu/docs/tpu7x#configurations) in the Cloud TPU documentation.

## Comparison of blueprint options

Cluster Toolkit provides both standard and advanced blueprints for deploying Cloud TPU v6e and Cloud TPU 7x clusters.

Both standard and advanced blueprints support the following features:

  * **Multi-Virtual Private Cloud (VPC) network architecture** : Provides the network architecture required for optimized high-throughput inter-chip communication.
  * **Dedicated service accounts** : Provides dedicated service accounts for the deployment, which helps improve security isolation.



For more information about blueprints, see the [Cluster blueprint overview](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).

### Standard blueprints

Standard blueprints provide a basic, functional cluster with a single TPU node pool and standard networking configuration. You can view the following standard blueprints on GitHub:

  * Cloud TPU v6e: [`examples/gke-tpu-v6e/gke-tpu-v6e.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-v6e/gke-tpu-v6e.yaml)
  * Cloud TPU 7x: [`examples/gke-tpu-7x/gke-tpu-7x.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x.yaml)



### Advanced blueprints

To optimize high-throughput inter-chip communication and data pipelines, advanced blueprints add the following features to the standard blueprint:

  * **Automatic bucket creation** : Creates two Cloud Storage buckets to store training data and checkpoints.
  * **Performance-tuned Cloud Storage FUSE mounts** : Pre-configures Cloud Storage FUSE mounts in the cluster as Persistent Volumes for optimized high-throughput performance. Cloud Storage FUSE uses [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) access. To learn how to mount Cloud Storage buckets in Google Kubernetes Engine (GKE), see [Access Cloud Storage buckets with the Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver).
  * **Hyperdisk Balanced support** : Provides highly available and consistent performance across GKE nodes. For more information, see [About Hyperdisk for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk).
  * **Google Cloud Managed Lustre support** : Provides a high-performance, fully managed parallel file system optimized for AI and high performance computing (HPC) workloads. For more information, see the [Google Cloud Managed Lustre overview](https://docs.cloud.google.com/managed-lustre/docs/overview).
  * **Filestore support** : Provides managed Network File System (NFS) capabilities that let multiple Cloud TPU hosts share logs, code, or datasets. For more information, see the [Filestore overview](https://docs.cloud.google.com/filestore/docs/overview).



You can view the following advanced blueprints on GitHub:

  * Cloud TPU v6e: [`examples/gke-tpu-v6e/gke-tpu-v6e-advanced.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-v6e/gke-tpu-v6e-advanced.yaml)
  * Cloud TPU 7x: [`examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml)



## Workload scheduling and consumption

Cluster Toolkit supports advanced scheduling and consumption models to help you manage costs and resource availability:

  * **[Kueue](https://kueue.sigs.k8s.io/)** : A Kubernetes-native system for managing quotas and Job queuing. Cluster Toolkit can automatically calculate and set a Cloud TPU quota matching the total static Cloud TPU capacity of your cluster.
  * **Dynamic Workload Scheduler** : Cluster Toolkit supports the Dynamic Workload Scheduler (DWS) flex-start provisioning mode. The flex-start provisioning mode is ideal for training jobs that can wait for capacity and are cost-effective. The blueprints also provide queued provisioning support with DWS Flex Start. For more information, see [About GPU, TPU, and H4D consumption with flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).



## What's next

  * To learn how to deploy a cluster with a dedicated Cloud TPU v6e node pool, see [Deploy a GKE TPU v6e cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-v6e).
  * To learn how to deploy a cluster with a dedicated Cloud TPU 7x node pool, see [Deploy a GKE TPU 7x cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
