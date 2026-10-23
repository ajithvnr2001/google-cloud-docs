---
url: https://docs.cloud.google.com/filestore/docs/filestore-for-gke/
title: About Filestore support for Google Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:24.558546+00:00
---

# About Filestore support for Google Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/filestore-for-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  About Filestore support for Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

Filestore instances are fully managed file servers on Google Cloud that you can use as durable storage with [ReadWriteMany](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#access_modes) access for your Google Kubernetes Engine (GKE) clusters.

  * As a type of durable or [non-ephemeral](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview) storage, your data persists beyond the lifecycle of your GKE Pods.

  * As durable storage with [ReadWriteMany](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) access, your GKE [PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumes) can be mounted as read-write by many nodes.

  * Unlike the single read-write access mode inherent to Persistent Disk, Filestore instances are accessible from multiple GKE nodes simultaneously. This lets you initiate Pods on any available GKE node, giving you greater efficiency of your GKE clusters.

  * As a type of [file storage](https://docs.cloud.google.com/filestore/docs/overview), Filestore supports multiple concurrent application instances accessing the same file system, simultaneously.




For more information, see [Deploy a stateful workload with Filestore](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workload).

## Filestore and the GKE Filestore CSI driver

The GKE Filestore CSI driver is the primary way for you to use Filestore instances with GKE and provides the following benefits:

  * You have access to fully-managed NFS storage through the Kubernetes APIs ([`kubectl`](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api)).

  * You can use the GKE Filestore CSI driver to dynamically provision your PersistentVolumes.

  * You can use the GKE Filestore CSI driver to decouple capacity from performance, allowing the dynamic scaling of performance. For more information, see [Dynamically scale Filestore performance using `VolumeAttributesClass`](https://docs.cloud.google.com/filestore/docs/csi-driver#scale-custom-performance).

  * You can use the GKE Filestore CSI driver to create [CSI volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots) which subsequently create [Filestore backups](https://docs.cloud.google.com/filestore/docs/backups).




For a detailed list of benefits, see [Access instances with the GKE Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver).

## Filestore multishares for GKE

Filestore multishares for GKE combined with the [GKE Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver), version 1.27 or later, provides the following benefits:

  * Provides a comprehensive view of your PersistentVolumes as one pool of storage.

  * Supports [dynamic volume provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/), scaling share and instance capacity up or down as needed.

  * Supports multiple shares with smaller, more flexible sizing for improved utilization and cost efficiency of each Filestore instance.




For more information, see [Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares).

## What's next

  * [Deploy a stateful workload with Filestore](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workload)
  * [StorageClasses and dynamic volume provisioning](https://docs.cloud.google.com/filestore/docs/multishares#storageclasses_and_dynamic_volume_provisioning)
  * [Access Filestore instances with the Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver)
  * [Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares)
  * [Optimize storage with Filestore multishares for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/optimize-multishares)
  * [Encrypt your GKE clusters' persistent storage using CMEK](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek#create_a_cmek_protected_attached_disk)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
