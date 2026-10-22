---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots/
title: About volume snapshots \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:13.620921+00:00
---

# About volume snapshots  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About volume snapshots Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

In Google Kubernetes Engine (GKE), you can use the Kubernetes [volume snapshot feature](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) for [persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) in your GKE clusters.

  * Kubernetes volume snapshots let you create a copy of your volume at a specific point in time. You can use this copy to bring a volume back to a prior state or to provision a new volume.

  * A [volume snapshot in Kubernetes](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) is equivalent to taking a backup of your data in other storage systems. For example, creating a Kubernetes volume snapshot is equivalent to creating a [Filestore backup](https://docs.cloud.google.com/filestore/docs/backups).

  * You can use snapshots to protect your workloads and achieve business-critical recovery point objectives in your disaster recovery plan, or if you have compliance needs to periodically save data.




GKE supports two ways to create volume snapshots:

  * **Container storage interface (CSI) volume snapshot API** : This is a manual process that lets you create and manage volume snapshots through the [Compute Engine Persistent Disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver) or the [Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver), applying configuration conventions commonly used in open source Kubernetes programming.

  * **Backup for GKE** : This is a fully-managed service that automates the creation and management of volume snapshots. [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) supports both the [configuration and volume backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup) for stateful workloads with persistent disks. For workloads with Filestore, only the configuration backup is supported. To back up data in your Filestore [basic tier](https://docs.cloud.google.com/filestore/docs/service-tiers) instances, you should continue to use the volume snapshot API through the Filestore CSI driver.




From GKE version 1.17 or later, you can provision and attach volume snapshots with the following components:

  * [VolumeSnapshotClass](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/)

  * [VolumeSnapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)

  * [VolumeSnapshotContent](https://kubernetes.io/docs/concepts/storage/volume-snapshots/#volume-snapshot-contents)


**Note:** In Kubernetes version 1.20, the VolumeSnapshot API version was [promoted to GA](https://kubernetes.io/blog/2020/12/10/kubernetes-1.20-volume-snapshot-moves-to-ga/). In GKE 1.23, `snapshot.storage.k8s.io/v1beta1` is deprecated. If you are using a GKE cluster version 1.21 and later, migrate to `snapshot.storage.k8s.io/v1`.

The following documentation covers how to use the volume snapshot API with a GKE CSI driver:

  * [Back up and restore Filestore storage using volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/backup-filestore-volume-snapshots).

  * [Back up and restore Persistent Disk storage using volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/backup-pd-volume-snapshots).




## What's next

  * Read the [Kubernetes Volume Snapshot](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-feature-cis-volume-snapshot-beta/) documentation.
  * Learn about [volume expansion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/volume-expansion).
  * Learn how to [manually install a CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/install-csi-driver).
  * Learn about [Filestore support for GKE](https://docs.cloud.google.com/filestore/docs/filestore-for-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
