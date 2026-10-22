---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/storage/
title: Storage overview \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:59.430101+00:00
---

# Storage overview  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/storage/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Storage overview Stay organized with collections  Save and categorize content based on your preferences. 

You create persistent storage for workloads running on GKE on AWS with Kubernetes objects.

## Using persistent storage in your GKE on AWS workloads

In GKE on AWS, you use the Kubernetes [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PV), [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#lifecycle-of-a-volume-and-claim) (PVC), and [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) resources to provide persistent file and block storage to workloads. You can create snapshots of persistent storage with the [VolumeSnapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) and [VolumeSnapshotClass](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/) resources. Snapshots are stored in your AWS account.

### StorageClass

Clusters have a [default](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class-1) Kubernetes StorageClass that [dynamically provisions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#dynamic_provisioning) stateful storage for workloads on AWS Elastic Block Storage (EBS) volumes. You can also use a [custom StorageClass](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class#custom) to provision other types of volumes. These options are described in the following section.

### VolumeSnapshotClass

Clusters have a [default](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/#the-volumesnapshotclass-resource) Kubernetes VolumeSnapshotClass that creates snapshots of stateful storage on EBS volumes.

## Configuring cluster storage

If you want to provision storage volumes with a non-default StorageClass, you can [Create a custom StorageClass](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class#custom) in a cluster that uses different parameters or a different storage driver. Then, you can [set the default StorageClass](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class#set_default), or configure your workloads to use the StorageClass. For example, you can use a [Reference the StorageClass in a StatefulSet](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class#statefulset) to set a specific StorageClass name.

## Using volume snapshots

You can use the [VolumeSnapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) resource to create snapshots of storage volumes. Then, you can provision new persistent volumes from these snapshots. For more information, see [Snapshot a PersistentVolume](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/snapshot-persistentvolume).

## Elastic Block Storage (EBS)

GKE on AWS manages AWS [EBS](https://aws.amazon.com/ebs/) volumes with the [aws-ebs-csi-driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver).

The EBS CSI Driver version is tied to a GKE on AWS Kubernetes version. When you upgrade your cluster version, the new driver version applies automatically. This version is typically the latest driver available at the time that the GKE on AWS version is released.

The driver pre-installed with GKE on AWS provides the following StorageClasses by default:

  * `standard-rwo` (default): Used for provisioning EBS `gp2` volumes.
  * `premium-rwo`: Used for provisioning EBS `io1` volumes.



EBS volumes support the Kubernetes ReadWriteOnce access mode.

**Note:** The legacy Kubernetes `kubernetes.io/aws-ebs` volume type is not supported.

### Preexisting EBS volumes

You can provision existing EBS volumes in your GKE on AWS workloads. See [Importing a preexisting EBS volume](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/preexisting-volume) for examples on how to use EBS volumes in GKE on AWS.

## Elastic File System (EFS)

GKE on AWS supports mounting preexisting [EFS](https://aws.amazon.com/efs/) file systems and access points. For more information, see [Use an EFS file system](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-efs).

## Additional storage options

Other third-party storage systems can be used with GKE on AWS through third-party Container Storage Interface (CSI) drivers (recommended) or in-tree Kubernetes volume plugins.

**Note:** Google does not provide support for third-party drivers. Contact your storage vendor for support.

### CSI drivers

The [Container Storage Interface (CSI)](https://github.com/container-storage-interface/spec/blob/master/spec.md) is an open standard API that enables Kubernetes to attach arbitrary storage systems to containerized workloads. A non-comprehensive list of CSI [Drivers](https://kubernetes-csi.github.io/docs/drivers.html) can be found in the Kubernetes CSI Developer Documentation. GKE on AWS supports CSI v1.x.

To use a CSI driver in your cluster, you need to [install a CSI driver](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-drivers) provided by your storage vendor. You can then configure workloads to use the driver's StorageClass or [Set the default StorageClass](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class#set_default).

### Specific storage drivers

The following volume drivers can be used with GKE on AWS.

#### FSx for Lustre (FSX)

GKE on AWS doesn't manage [FSx](https://aws.amazon.com/fsx/lustre) volumes directly. You can manually install the [aws-fsx-csi-driver](https://github.com/kubernetes-sigs/aws-fsx-csi-driver), but support is not available from Google.

### Kubernetes in-tree volume plugins

Kubernetes ships with [in-tree (built-in) volume plugins](https://kubernetes.io/docs/concepts/storage/volumes/#volume-types). Supported in-tree drivers include the following:

  * configMap
  * emptyDir
  * hostPath
  * nfs
  * projected
  * secrets

**Note:** Using a vendor-supported in-tree volume plugin (for example, `awsElasticBlockStore`) is not recommended. New Kubernetes storage features, such as volume snapshots, are supported only with CSI drivers. Also, many of the in-tree plugins do not support [dynamic provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes). When using a driver that does not support dynamic provisioning, you must manually create PersistentVolumes for your workloads.

## What's next?

  * Learn how to [Use StorageClasses with your workloads](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class).
  * [Use a pre-existing EBS volume](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/preexisting-volume).
  * Learn about [Persistent volumes and dynamic provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) in GKE.
  * Learn how to [Snapshot a PersistentVolume](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/snapshot-persistentvolume).
  * Read the Kubernetes [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/) documentation.
  * Read the [Container Storage Interface (CSI) for Kubernetes GA](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/) release announcement.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
