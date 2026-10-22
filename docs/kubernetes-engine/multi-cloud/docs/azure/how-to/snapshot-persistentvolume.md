---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/snapshot-persistentvolume/
title: Snapshot a PersistentVolume \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:40.473549+00:00
---

# Snapshot a PersistentVolume  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/snapshot-persistentvolume/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Snapshot a PersistentVolume

You can use the Kubernetes volume snapshot feature for [Persistent volumes and dynamic provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) in your GKE clusters.

Volume snapshots let you create a copy of your volume at a specific point in time. You can use this copy to bring a volume back to a prior state or to provision a replacement volume.

You can provision and attach volume snapshots with the following components:

  * [VolumeSnapshotClass](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/)
  * [VolumeSnapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)
  * [VolumeSnapshotContent](https://kubernetes.io/docs/concepts/storage/volume-snapshots/#volume-snapshot-contents)



## Requirements

To use volume snapshots on GKE on Azure, you must have the following:

  * A volume using a Container Storage Interface (CSI) driver that supports snapshots. The Azure Disk and Azure File drivers that GKE on Azure uses by default support snapshots.

**Note:** The Azure File CSI driver doesn't support restoring from a snapshot. For more information, see [Overview of share snapshots for Azure Files](https://docs.microsoft.com/en-us/azure/storage/files/storage-snapshots-files). 

For a list of all CSI drivers that support snapshots, see the "Other features" column in [Drivers](https://kubernetes-csi.github.io/docs/drivers.html) in the Kubernetes documentation.

  * Have an existing `PersistentVolumeClaim` to use for a snapshot. The `PersistentVolume` you use for a snapshot source must be managed by a CSI driver. You can verify that you're using a CSI driver by checking that the `PersistentVolume` spec has a `csi` section with `driver: disk.csi.azure.com` or `file.csi.azure.com`. If your cluster [Dynamically provisions PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#dynamic_provisioning) by the CSI driver as described in the following sections, it's managed by the CSI driver.




## Before you begin

  * [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster)
  * [Connect to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster)



## Create and use a volume snapshot

The examples in this document show you how to do the following tasks:

  1. Create an example `PersistentVolumeClaim` and `Pod`.
  2. Create a VolumeSnapshot.
  3. Restore the volume snapshot.
  4. Verify that the restoration worked.



To use a volume snapshot, you must complete the following steps:

  1. Create a `VolumeSnapshot` object to request a snapshot of an existing PersistentVolumeClaim.
  2. Reference the `VolumeSnapshot` in a `PersistentVolumeClaim` to restore a volume to that snapshot or create a new volume using the snapshot.



### Create an example `PersistentVolumeClaim` and `Pod`

  1. To create the `PersistentVolumeClaim` object, save the following manifest as `example-pvc.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: example-pvc
         spec:
           storageClassName: standard-rwo
           accessModes:
           - ReadWriteOnce
           resources:
             requests:
               storage: 1Gi
         

For `spec.storageClassName`, you can specify any storage class that uses a supported CSI driver. This example uses the default `standard-rwo` storage class.

  2. Apply the manifest:
         
         kubectl apply -f example-pvc.yaml
         

  3. Create a Pod that writes the current date and time to the volume. To create a Pod, save the following manifest as `snapshot-shell.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: snapshot-shell
         spec:
           terminationGracePeriodSeconds: 10
           containers:
           - name: linux
             image: ubuntu:bionic
             command: ["/bin/sh"]
             args: ["-c", "echo $(date -u) >> /data/out.txt"]
             volumeMounts:
             - name: snapshot-volume
               mountPath: /data
           restartPolicy: Never
           volumes:
           - name: snapshot-volume
             persistentVolumeClaim:
               claimName: example-pvc
         

  4. Apply the manifest:
         
         kubectl apply -f snapshot-shell.yaml
         

  5. Check the status of the Pod:
         
         kubectl get pod snapshot-shell
         

It might take some time for the Pod to run and complete. You can run the preceding command until you see an output similar to the following:
         
         NAME             READY   STATUS      RESTARTS   AGE
         snapshot-shell   0/1     Completed   0          24s
         




### Create a VolumeSnapshot

A `VolumeSnapshot` object is a request for a snapshot of an existing `PersistentVolumeClaim` object. When you create a `VolumeSnapshot` object, your cluster automatically creates and binds it with a `VolumeSnapshotContent` object, which is a resource in your cluster like a `PersistentVolume` object.

  1. Save the following manifest as `volumesnapshot.yaml`.
         
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshot
         metadata:
           name: example-snapshot
         spec:
           source:
             persistentVolumeClaimName: example-pvc
         

  2. Apply the manifest:
         
         kubectl apply -f volumesnapshot.yaml
         

After you create a volume snapshot, your cluster creates a corresponding `VolumeSnapshotContent` object. This object stores the snapshot and bindings of `VolumeSnapshot` objects. You do not interact with `VolumeSnapshotContents` objects directly.

  3. Confirm that your cluster created the `VolumeSnapshotContents` object:
         
         kubectl get volumesnapshotcontents
         

The output is similar to the following:
         
         NAME                                               AGE
         snapcontent-cee5fb1f-5427-11ea-a53c-42010a1000da   55s
         




#### Confirm the volume snapshot is ready

After the volume snapshot content is created, the CSI driver you specified in the `VolumeSnapshotClass` creates a snapshot on the corresponding storage system. After your cluster creates a snapshot on the storage system and binds it to a `VolumeSnapshot` object, the snapshot is ready to use. You can check the status by running the following command:
    
    
    kubectl get volumesnapshot \
      -o custom-columns='NAME:.metadata.name,READY:.status.readyToUse'
    

If the snapshot is ready to use, the output is similar to the following:
    
    
    NAME                    READY
    example-snapshot        true
    

### Restore the volume snapshot

You can reference a `VolumeSnapshot` in a `PersistentVolumeClaim` to provision a new volume with data from an existing volume or restore a volume to a state that you captured in the snapshot.

To reference a `VolumeSnapshot` in a `PersistentVolumeClaim`, add the `dataSource` field to your `PersistentVolumeClaim`.

In this example, you reference the `VolumeSnapshot` that you created in a new `PersistentVolumeClaim` and create a Pod that mounts the `PersistentVolumeClaim`.

  1. Save the following manifest as `pvc-restore.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
          name: pvc-restore
         spec:
          **dataSource :
            name: example-snapshot
            kind: VolumeSnapshot
            apiGroup: snapshot.storage.k8s.io**
          storageClassName: standard-rwo
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 1Gi
         

**Note:** The namespace of the `PersistentVolumeClaim` must be the same as the namespace of the `VolumeSnapshot`.
  2. Apply the manifest:
         
         kubectl apply -f pvc-restore.yaml
         

  3. Launch a temporary Pod that mounts the PVC to the Pod and prints the contents of `out.txt` to logs.

Save the following manifest as `restore-log.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: restore-verify
         spec:
           volumes:
             - name: restore-data
               persistentVolumeClaim:
                 claimName: pvc-restore
           containers:
             - name: shell-container
               image: ubuntu:bionic
               volumeMounts:
                 - mountPath: "/data"
                   name: restore-data
               command: [ "/bin/sh" ]
               args: ["-c", "cat /data/out.txt", "exit", "1"]
           restartPolicy: Never
         

  4. Apply the manifest:
         
         kubectl apply -f restore-log.yaml
         




### Check that the snapshot restored successfully

The Pod you created in the previous step reads from the snapshot. To view the data from the snapshot, use the `kubectl logs` command.
    
    
    kubectl logs restore-verify
    

The output should include a timestamp from the snapshot.

## Clean up

To avoid incurring charges for the resources used on this page, follow these steps.

  1. Delete the `VolumeSnapshot`:
         
         kubectl delete volumesnapshot example-snapshot
         

**Note:** If a volume snapshot's `VolumeSnapshotClass` has `deletionPolicy:Delete`, the corresponding `VolumeSnapshotContent` and the physical snapshot on the storage system are also deleted. If it has a `deletionPolicy:Retain` the underlying snapshot is retained.
  2. Delete the temporary Pod:
         
         kubectl delete -f restore-log.yaml
         

  3. Delete the Pod:
         
         kubectl delete -f snapshot-shell.yaml
         

  4. Delete the `PersistentVolumeClaim` objects:
         
         kubectl delete pvc example-pvc pvc-restore
         




## What's next

  * Read the Kubernetes [Volume Snapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) documentation.
  * [Install additional CSI drivers](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-drivers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
