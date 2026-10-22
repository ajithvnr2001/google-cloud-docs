---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/storage/
title: Storage overview \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:29.303684+00:00
---

# Storage overview  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Storage overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud can use several storage configurations, and provides interfaces for block and file storage management through the following Kubernetes objects:

  * [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
  * [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
  * [Storage classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
  * [Volume snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)

**Warning:** Google Distributed Cloud doesn't include a persistent storage provider. You must provide and configure a persistent storage system for your stateful workloads.

## Ephemeral Storage through Kubernetes volumes

Kubernetes `Volume` resources are storage units accessible to containers in a `Pod`. Ephemeral storage backs the following volume types:

  * [`emptyDir`](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir)

  * [`ConfigMap`](https://kubernetes.io/docs/concepts/configuration/configmap/)

  * [`Secrets`](https://kubernetes.io/docs/concepts/configuration/secret/)




Ephemeral storage types don't persist after a pod ceases to exist. Use ephemeral storage for configuration information and to cache storage for applications.

Ephemeral storage types share and consume resources from the node's boot disk. You can [manage your local ephemeral storage resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#local_ephemeral_storage) in the same way that you manage CPU and memory resources.

## Persistent Storage using `PersistentVolume` resources

A Kubernetes `PersistentVolume` is a resource that a `Pod` can use for durable storage. The lifetime of persistent volumes is independent from the lifetime of a pod. Thus, the disk and data in a persistent volume continue to exist as the cluster changes and as pods are deleted and recreated. You can provision `PersistentVolume` resources dynamically through the `PersistentVolumeClaims` API, or a cluster administrator can create them explicitly.

Google Distributed Cloud can back persistent storage by using a variety of storage systems, including [Container Storage Interface (CSI)](https://kubernetes.io/docs/reference/glossary/?all=true#term-csi) drivers and local volumes.

### Container Storage Interface (CSI) drivers

Google Distributed Cloud is compatible with [CSI v1.0 drivers](https://github.com/container-storage-interface/spec). CSI is an open standard interface that many major storage vendors support. For production storage, [install a CSI driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-csi-driver) from a GDC Ready storage partner. For the full list of GDC Ready storage partners, see [GDC Ready Storage Partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

To use CSI in your cluster, deploy the CSI driver that your storage vendor provided to your clusters. Then, configure workloads to [use the CSI driver with the `StorageClass` API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-csi-driver#using_csi_driver), or set `StorageClass` as the [default API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/default-storage-class).

### Local volumes

For proof of concept and advanced use cases, you can use [local PersistentVolume resources](https://kubernetes.io/docs/concepts/storage/volumes/#local). Google Distributed Cloud bundles the [sig-storage-local-static-provisioner](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner), which discovers mount points on each node and creates a local persistent volume for each mount point.

**Caution:** Using a local persistent volume binds the pods to a specific disk and node. If that disk or node becomes unavailable, then the pods also become unavailable. Workloads using local PersistentVolume resources need to be resilient to this kind of failure, and may require additional orchestration to release the persistent volume claims of the pods and find a new and empty disk on another node.

Google Distributed Cloud clusters use the local volume provisioner (LVP) to manage local persistent volumes. There are three types of storage classes for local persistent volumes in a Google Distributed Cloud cluster:

  * LVP share
  * LVP node mounts
  * `anthos-system`



#### LVP share

This option creates a local persistent volume that subdirectories in a local and shared file system are backing. Cluster creation automatically generates these subdirectories. Workloads using this storage class share capacity and input/output operations per second (IOPS) because the same shared file system backs the persistent volumes. To have better isolation, configure disks through LVP node mounts.

For more information, see [Configuring an LVP Share](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-local-storage#configuring_an_lvp_share).

#### LVP node mounts

This option creates a local persistent volume for each mounted disk in the configured directory. You must format and mount each disk before or after cluster creation.

For more information, see [Configuring LVP node mounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-local-storage#configuring_lvp_node_mounts).

#### `anthos-system`

This storage class creates preconfigured local persistent volumes during cluster creation that the cluster system pods use. The storage class name is `anthos-system`. Don't change or delete this storage class and don't use this storage class for stateful workloads.

## What's next

  * Learn more about [volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/volumes).
  * Learn more about [Container Storage Interface](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/) in Kubernetes.
  * Learn how to [take volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots).
  * Learn how to [increase the capacity of persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-expansion).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
