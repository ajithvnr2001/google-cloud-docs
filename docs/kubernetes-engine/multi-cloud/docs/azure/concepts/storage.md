---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/storage/
title: Storage overview \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:57.611239+00:00
---

# Storage overview  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/storage/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Storage overview

You create persistent storage for workloads running on GKE on Azure with Kubernetes objects.

## Control plane storage

When you create a cluster, GKE on Azure provisions Premium SSD LRS disks for control plane and etcd volumes.

## Use persistent storage in your GKE on Azure workloads

In GKE on Azure, you use the Kubernetes [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PV), [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#lifecycle-of-a-volume-and-claim) (PVC), and [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) resources to provide persistent file and block storage to workloads. You can create snapshots of persistent storage with the [VolumeSnapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) and [VolumeSnapshotClass](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/) resources. Snapshots are stored in your Azure account.

### StorageClass

Clusters have a [default](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class-1) Kubernetes StorageClass that [dynamically provisions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#dynamic_provisioning) stateful storage for workloads on Azure Disk Storage (AzureDisk) volumes. You can also use a [different StorageClass](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-class#custom) to provision other types of volumes. These options are described in the following section.

### Azure storage accounts

GKE on Azure automatically creates an Azure [storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview) when a cluster is created. If you would like to use a specific storage account, [create a custom storage class](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-class).

## Configure cluster storage

If you want to provision storage volumes with a non-default StorageClass, you can create a new [StorageClass](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-class#custom) in a cluster that uses different parameters or a different storage driver. Then, you can [set the StorageClass as the cluster's default](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-class#set_default), or configure your workloads to use the StorageClass. For example, you can use a [StatefulSet](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-class#statefulset) to set a specific StorageClass name.

## Azure Disk Storage (AzureDisk)

GKE on Azure manages [Azure Disk](https://docs.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) volumes with the [`azuredisk-csi-driver`](https://github.com/kubernetes-sigs/azuredisk-csi-driver).

The CSI Driver version is tied to a GKE on Azure Kubernetes version. When you upgrade your cluster version, GKE on Azure updates the driver version automatically. This version is typically the latest driver available at the time that the GKE on Azure version is released. The legacy Kubernetes `kubernetes.io/azure-disk` volume type is not supported.

The driver pre-installed with GKE on Azure provides the following StorageClasses by default:

  * `standard-rwo` (default): Used for provisioning standard SSD Azure disks with [LRS](https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy#redundancy-in-the-primary-region)
  * `premium-rwo`: Used for provisioning premium SSD Azure disks with LRS



Azure Disk volumes support the Kubernetes ReadWriteOnce access mode.

**Note:** GKE on Azure doesn't support the UltraSSD_LRS account type.

### Volume snapshots

You can use the [VolumeSnapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) resource to create snapshots of storage volumes. Then, you can [provision](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#volume-snapshot-and-restore-volume-from-snapshot-support) new persistent volumes from these snapshots.

### Volume cloning

You can use [CSI volume cloning](https://kubernetes.io/docs/concepts/storage/volume-pvc-datasource/) to clone existing Azure Disk volumes. For more information, see the [Volume cloning example](https://github.com/kubernetes-sigs/azuredisk-csi-driver/tree/master/deploy/example/cloning).

### Volume resizing

You can resize unattached Azure Disk volumes with volume resizing. For more information, see the [Volume resizing example](https://github.com/kubernetes-sigs/azuredisk-csi-driver/tree/master/deploy/example/resize). Resizing while the volume is attached and mounted is not supported.

### Azure shared disks

For workloads that are designed to coordinate writes to a shared raw block disk, GKE on Azure supports [Azure shared disks](https://docs.microsoft.com/en-us/azure/virtual-machines/disks-shared). For more information, see [Shared disk(Multi-node ReadWrite)](https://github.com/kubernetes-sigs/azuredisk-csi-driver/tree/master/deploy/example/sharedisk) in the Azure disk CSI documentation.

**Caution:** Workloads that are not specifically designed for using shared raw block disks can lose or corrupt data. If your workloads need a multi-write file system but are not designed to support raw block disks, use Azure File storage.

## Azure File Storage (AzureFile)

GKE on Azure manages [Azure Files](https://docs.microsoft.com/en-us/azure/storage/files/storage-files-introduction) volumes with the [`azurefile-csi-driver`](https://github.com/kubernetes-sigs/azurefile-csi-driver)

The CSI Driver is tied to a GKE on Azure Kubernetes version. When you upgrade your cluster version, the new driver version applies automatically. This version is typically the latest driver available at the time that the GKE on Azure version is released. The legacy Kubernetes `kubernetes.io/azure-file` volume type is not supported.

The driver pre-installed with GKE on Azure provides the following StorageClasses by default:

  * standard-rwx: Used for provisioning [standard SSD](https://docs.microsoft.com/en-us/azure/aks/azure-files-dynamic-pv#create-a-storage-class) Azure file shares with LRS
  * premium-rwx: Used for provisioning [premium SSD](https://docs.microsoft.com/en-us/azure/aks/azure-files-dynamic-pv#create-a-storage-class) Azure file shares with LRS



Azure file volumes use the Kubernetes ReadWriteMany access mode.

### Volume snapshots

You can use the [VolumeSnapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) resource to create snapshots of Azure File volumes. For more information, see the [Azure File Snapshot feature](https://github.com/kubernetes-sigs/azurefile-csi-driver/tree/master/deploy/example/snapshot) documentation. To restore a snapshot, you use the Azure portal. For more information, see [Overview of share snapshots for Azure Files](https://docs.microsoft.com/en-us/azure/storage/files/storage-snapshots-files).

### Volume resizing

You can resize Azure File volumes with volume resizing. For more information, see the [Volume resizing example](https://github.com/kubernetes-sigs/azurefile-csi-driver/tree/master/deploy/example/resize).

## Additional storage drivers

Other third-party storage systems can be used with GKE on Azure through third-party Container Storage Interface (CSI) drivers (recommended) or in-tree Kubernetes volume plugins.

**Note:** Google does not provide support for third-party drivers. Contact your storage vendor for support.

### CSI drivers

The [Container Storage Interface (CSI)](https://github.com/container-storage-interface/spec/blob/master/spec.md) is an open standard API that enables Kubernetes to attach arbitrary storage systems to containerized workloads. A non-comprehensive list of CSI drivers can be found in the [Kubernetes CSI Developer Documentation](https://kubernetes-csi.github.io/docs/drivers.html). GKE on Azure supports CSI v1.x.

To use a CSI driver in your cluster, you need to [install the CSI driver](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-drivers) provided by your storage vendor. You can then configure workloads to use the driver's StorageClass or set it as the [default StorageClass](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-class#set_default).

### Azure-specific storage drivers

The following volume drivers can be used with GKE on Azure:

  * [`blob-csi-driver`](https://github.com/kubernetes-sigs/blob-csi-driver)



GKE on Azure doesn't manage Azure [Blob](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) storage directly. You can manually install the [`blob-csi-driver`](https://github.com/kubernetes-sigs/blob-csi-driver) CSI driver, but support is not available from Google.

### Kubernetes in-tree volume plugins

Kubernetes ships with [in-tree (built-in) volume plugins](https://kubernetes.io/docs/concepts/storage/volumes/#volume-types). Supported in-tree drivers include the following:

  * configMap
  * emptyDir
  * hostPath
  * nfs
  * projected
  * secrets

**Note:** Using a vendor-supported in-tree volume plugin is not recommended. New Kubernetes storage features, such as volume snapshots, are supported only with CSI drivers. Also, many of the in-tree plugins do not support [dynamic provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes). When using a driver that does not support dynamic provisioning, you must manually create PersistentVolumes for your workloads.

## What's next?

  * Learn about [Using StorageClasses with your workloads](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-class).
  * [Import a preexisting Azure Disk volume into GKE on Azure](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/preexisting-volume).
  * Read the documentation for the [Azure Disk CSI driver](https://github.com/kubernetes-sigs/azuredisk-csi-driver/tree/v1.8.0/docs) or the [Azure File CSI driver](https://github.com/kubernetes-sigs/azurefile-csi-driver/tree/v1.7.0/docs).
  * Learn about [Volume snapshots in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots).
  * Read the Kubernetes [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/) documentation.
  * Read the [Container Storage Interface](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/) release announcement.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
