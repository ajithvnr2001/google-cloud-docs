---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/readonlymany-disks/
title: Use persistent disks with multiple readers \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:21.486621+00:00
---

# Use persistent disks with multiple readers  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/readonlymany-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Use persistent disks with multiple readers Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to add a [persistent disk](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) to your cluster using the ReadOnlyMany access mode. This mode allows multiple [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) on different [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) to mount the disk for reading.

For more information on this mode, refer to [persistent volume access modes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#access_modes).

## Requirements

  * Your cluster must run GKE version 1.22 or later.
  * Your cluster must use the [Compute Engine persistent disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver).



## Format and populate a source persistent disk

To use a persistent disk in read-only mode, you must populate a source persistent disk with data, then either clone the volume or use a volume snapshot to move the data into a new ReadOnlyMany PersistentVolume.

  1. Create a PersistentVolume using an [existing persistent disk](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/preexisting-pd) or using [dynamic provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#dynamic_provisioning).

  2. Format the disk and populate it with data. To format the disk, reference the disk as a ReadWriteOnce PersistentVolume in a Pod. GKE automatically formats the underlying disk, and lets the Pod write data to the disk. When the Pod starts, make sure the Pod writes the data you want to the disk.




## Create a `ReadOnlyMany` PersistentVolume

You can create a `ReadOnlyMany` PersistentVolume using one of the following methods:

  * A volume snapshot of a source PersistentVolume that you populate with data.
  * A [volume clone](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-cloning) of a source PersistentVolume that you populate with data.
  * A pre-existing persistent disk that was already populated with data.




###  Volume snapshot 

  1. [Create a volume snapshot of the source PersistentVolume](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots#create-snapshotclass).

  2. Save the following PersistentVolumeClaim manifest as `snapshot-pvc.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           namespace: PVC_NAMESPACE
           name: PVC_NAME
         spec:
           dataSource:
             apiGroup: snapshot.storage.k8s.io
             kind: VolumeSnapshot
             name: SNAPSHOT_NAME
           accessModes:
             **- ReadOnlyMany**
           storageClassName: premium-rwo
           resources:
             requests:
               storage: STORAGE_SIZE
         

Replace the following:

     * `PVC_NAMESPACE`: the namespace of the new PersistentVolumeClaim.
     * `PVC_NAME`: the name of the new PersistentVolumeClaim.
     * `SNAPSHOT_NAME`:the name of your `VolumeSnapshot` object.
     * `STORAGE_SIZE`: the amount of storage to request. This must be the same as the amount requested in the source PersistentVolumeClaim.
  3. Apply the manifest to your cluster:
         
         kubectl apply -f snapshot-pvc.yaml
         




This creates a new PersistentVolumeClaim named `PVC_NAME` in your cluster, which GKE uses to dynamically provision a new PersistentVolume that contains the data from the snapshot of the source persistent disk.

###  Volume cloning 

Before using volume cloning, make sure to familiarize yourself with the [limitations of this approach](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-cloning).

  1. Save the following manifest as `cloning-pvc.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           namespace: PVC_NAMESPACE
           name: PVC_NAME
         spec:
           dataSource:
             name: SOURCE_PVC
             kind: PersistentVolumeClaim
           accessModes:
             **- ReadOnlyMany**
           storageClassName: STORAGE_CLASS_NAME
           resources:
             requests:
               storage: STORAGE_SIZE
         

Replace the following:

     * `PVC_NAMESPACE`: the namespace of the new PersistentVolumeClaim.
     * `PVC_NAME`: the name of the new PersistentVolumeClaim.
     * `SOURCE_PVC`: the name of the source PersistentVolumeClaim populated with data.
     * `STORAGE_CLASS_NAME`: the storage class for the new PersistentVolumeClaim. This must be the same as the storage class of the source PersistentVolumeClaim.
     * `STORAGE_SIZE`: the amount of storage for the new PersistentVolumeClaim. This must be the same amount requested by the source PersistentVolumeClaim.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f cloning-pvc.yaml
         




This creates a PersistentVolumeClaim named `PVC_NAME` that GKE uses to create a new PersistentVolume in ReadOnlyMany mode with the data in the source PersistentVolume.

For more detailed information about Volume Cloning, see [Create clones of persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-cloning).

###  Pre-existing persistent disk 

  1. Save the following manifest as `preexisting-disk-pv-pvc.yaml`:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: PV_NAME
         spec:
           storageClassName: "STORAGE_CLASS_NAME"
           capacity:
             storage: DISK_SIZE
           accessModes:
             **- ReadOnlyMany**
           claimRef:
             namespace: PVC_NAMESPACE
             name: PVC_NAME
           csi:
             driver: pd.csi.storage.gke.io
             volumeHandle: DISK_ID
             fsType: FS_TYPE
             **readOnly : true**
         ---
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           namespace: PVC_NAMESPACE
           name: PVC_NAME
         spec:
           storageClassName: "STORAGE_CLASS_NAME"
           volumeName: PV_NAME
           accessModes:
             **- ReadOnlyMany**
           resources:
             requests:
               storage: DISK_SIZE
         

Replace the following:

     * `PV_NAME`: the name of your new PersistentVolume.
     * `STORAGE_CLASS_NAME`: the name of your new StorageClass.
     * `DISK_SIZE`: the size of your pre-existing persistent disk. For example, `500G`.
     * `PVC_NAMESPACE`: the namespace of the new PersistentVolumeClaim.
     * `PVC_NAME`: the name of your new PersistentVolumeClaim.
     * `DISK_ID`: the identifier of your pre-existing persistent disk. The format is `projects/{project_id}/zones/{zone_name}/disks/{disk_name}` for [Zonal persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#pd-zones), or `projects/{project_id}/regions/{region_name}/disks/{disk_name}` for [Regional persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#regional_persistent_disks).
     * `FS_TYPE`: the filesystem type. You can leave this as the default (`ext4`), or use `xfs`. If your clusters use a Windows Server node pool, you must change this to `NTFS`.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f preexisting-disk-pv-pvc.yaml
         




This creates a PersistentVolumeClaim named `PVC_NAME` and a PersistentVolume named `PV_NAME` in ReadOnlyMany mode.

For more detailed information about using a pre-existing persistent disk, see [existing persistent disk](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/preexisting-pd).

## Use the PersistentVolumeClaim in a Pod

You can now reference the new PersistentVolumeClaim in read-only mode in multiple Pods on multiple nodes at the same time. You cannot attach persistent disks in ReadWriteOnce mode to multiple nodes at the same time. For more information, refer to [Deployments vs. StatefulSets](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#deployments_vs_statefulsets).

In your Pod specification, you must specify `readOnly: true` in the `volumeMounts` section and the `volumes` section, such as in the following example:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: multi-read
      labels:
        app: web-server
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: web-server
      template:
        metadata:
          labels:
            app: web-server
        spec:
          containers:
          - name: web-server
            image: nginx
            volumeMounts:
            - mountPath: /test-mnt
              name: my-volume
              **readOnly : true**
          volumes:
          - name: my-volume
            persistentVolumeClaim:
              claimName: PVC_NAME
              **readOnly : true**
    

**Note:** Read-only ext3 and ext4 filesystems do not support journal playback. If the source persistent disk filesystem is marked as dirty when you clone or snapshot it, the data in your read-only persistent disk might be inconsistent or corrupt. The Compute Engine persistent disk CSI driver attempts to mount the disk normally. If the inability to playback the journal causes the volume mount to fail, the CSI driver automatically retries the mount with the `noload` option, which disables playback attempts on ext3 and ext4 filesystems. If the source filesystem was actually inconsistent at the moment it was cloned or snapshotted, the read-only mount will also be inconsistent.

## What's next

  * Learn more about [GKE persistent volumes and provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).
  * Learn how to [use the Compute Engine persistent disk CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver).
  * Learn how to [use pre-existing persistent disks as PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/preexisting-pd).
  * Learn how to [use volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots).
  * Learn how to [create clones of persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-cloning).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
