---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/backup-pd-volume-snapshots/
title: Back up Persistent Disk storage using volume snapshots \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:04.281762+00:00
---

# Back up Persistent Disk storage using volume snapshots  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/backup-pd-volume-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Back up Persistent Disk storage using volume snapshots Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Back up and restore your Persistent Disk storage in Google Kubernetes Engine (GKE) by using volume snapshots. A volume snapshot creates a point-in-time copy of your Persistent Disk data, allowing for efficient recovery and testing. This capability helps you safeguard against data loss, revert to previous states, and ensure business continuity for your workloads. To learn more about the fundamental concepts of volume snapshots in Kubernetes, see [About Kubernetes volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots).

## Requirements

To use volume snapshots on GKE, you must meet the following requirements:

  * Use a CSI driver that supports snapshots. The in-tree Persistent Disk driver does not support snapshots. To create and manage snapshots, you must use the same CSI driver as the underlying `PersistentVolumeClaim` (PVC).

    * For Persistent Disk (PD) volume snapshots, use the Compute Engine Persistent Disk CSI driver. The [Compute Engine Persistent Disk CSI driver](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver) is installed by default on new Linux clusters running GKE version 1.18.10-gke.2100 or later, or version 1.19.3-gke.2100 or later. You can also [enable the Compute Engine Persistent Disk CSI driver on an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#enabling_the_on_an_existing_cluster).

    * For a list of all CSI drivers that support snapshots, see the **Other features** column in [Drivers](https://kubernetes-csi.github.io/docs/drivers.html) in the Kubernetes documentation.

  * Use control plane [versions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) 1.17 or later. To use the [Compute Engine Persistent Disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gce-pd-csi-driver) in a `VolumeSnapshot`, use GKE versions 1.17.6-gke.4 or later.



  * Have an existing `PersistentVolumeClaim` to use for a snapshot. The `PersistentVolume` you use for a snapshot source must be managed by a CSI driver. You can verify that you're using a CSI driver by checking that the `PersistentVolume` spec has a `csi` section with `driver: pd.csi.storage.gke.io` or `filestore.csi.storage.gke.io`. If the `PersistentVolume` is [dynamically provisioned](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#dynamic_provisioning) by the CSI driver as described in the following sections, it's managed by the CSI driver.



## Limitations

All [restrictions for creating a disk snapshot](https://docs.cloud.google.com/compute/docs/disks/snapshots#restrictions) on Compute Engine also apply to GKE.

## Best practices

Be sure to follow [best practices for Compute Engine disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices) when using Persistent Disk `Volume` snapshots on GKE.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Creating and using a volume snapshot

The examples in this document show you how to do the following tasks:

  1. Create a `PersistentVolumeClaim` and `Deployment`.
  2. Add a file to the `PersistentVolume` that the `Deployment` uses.
  3. Create a `VolumeSnapshotClass` to configure the snapshot.
  4. Create a volume snapshot of the `PersistentVolume`.
  5. Delete the test file.
  6. Restore the `PersistentVolume` to the snapshot you created.
  7. Verify that the restoration worked.



To use a volume snapshot, you must complete the following steps:

  1. Create a `VolumeSnapshotClass` object to specify the CSI driver and deletion policy for your snapshot.
  2. Create a `VolumeSnapshot` object to request a snapshot of an existing `PersistentVolumeClaim`.
  3. Reference the `VolumeSnapshot` in a `PersistentVolumeClaim` to restore a volume to that snapshot or create a new volume using the snapshot.



### Create a `PersistentVolumeClaim` and a `Deployment`

  1. To create the `PersistentVolumeClaim` object, save the following manifest as `my-pvc.yaml`:

###  Persistent Disk 
         
         apiVersion: v1
          kind: PersistentVolumeClaim
          metadata:
            name: my-pvc
          spec:
            storageClassName: standard-rwo
            accessModes:
            - ReadWriteOnce
            resources:
              requests:
                storage: 1Gi
         

This example uses the `standard-rwo` storage class installed by default with the Compute Engine Persistent Disk CSI driver. To learn more, see [Using the Compute Engine Persistent Disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#enabling_the_on_a_new_cluster).

For `spec.storageClassName`, you can specify any storage class that uses a supported CSI driver.

  2. Apply the manifest:
         
         kubectl apply -f my-pvc.yaml
         

  3. To create a `Deployment`, save the following manifest as `my-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: hello-app
         spec:
           selector:
             matchLabels:
               app: hello-app
           template:
             metadata:
               labels:
                 app: hello-app
             spec:
               containers:
               - name: hello-app
                 image: google/cloud-sdk:slim
                 args: [ "sleep", "3600" ]
                 volumeMounts:
                 - name: sdk-volume
                   mountPath: /usr/share/hello/
               volumes:
               - name: sdk-volume
                 persistentVolumeClaim:
                   claimName: my-pvc
         

  4. Apply the manifest:
         
         kubectl apply -f my-deployment.yaml
         

  5. Check the status of the `Deployment`:
         
         kubectl get deployment hello-app
         

It might take some time for the `Deployment` to become ready. You can run the preceding command until you see an output similar to the following:
         
         NAME        READY   UP-TO-DATE   AVAILABLE   AGE
         hello-app   1/1     1            1           2m55s
         




### Add a test file to the volume

  1. List the `Pods` in the `Deployment`:
         
         kubectl get pods -l app=hello-app
         

The output is similar to the following:
         
         NAME                         READY   STATUS    RESTARTS   AGE
         hello-app-6d7b457c7d-vl4jr   1/1     Running   0          2m56s
         

  2. Create a test file in a `Pod`:
         
         kubectl exec POD_NAME \
             -- sh -c 'echo "Hello World!" > /usr/share/hello/hello.txt'
         

Replace `POD_NAME` with the name of the `Pod`.

  3. Verify that the file exists:
         
         kubectl exec POD_NAME \
             -- sh -c 'cat /usr/share/hello/hello.txt'
         

The output is similar to the following:
         
         Hello World!
         




### Create a `VolumeSnapshotClass` object

Create a `VolumeSnapshotClass` object to specify the CSI driver and `deletionPolicy` for your volume snapshot. You can reference `VolumeSnapshotClass` objects when you create `VolumeSnapshot` objects.

  1. Save the following manifest as `volumesnapshotclass.yaml`.

###  Persistent Disk 

Use the `v1` API version for clusters running versions 1.21 or later.
         
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshotClass
         metadata:
           name: my-snapshotclass
         driver: pd.csi.storage.gke.io
         deletionPolicy: Delete
         

In this example:

     * The `driver` field is used by the CSI driver to provision the snapshot. In this example, `pd.csi.storage.gke.io` uses the [Compute Engine Persistent Disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gce-pd-csi-driver).

     * The`deletionPolicy` field tells GKE what to do with the `VolumeSnapshotContent` object and the underlying snapshot when the bound `VolumeSnapshot` object is deleted. Specify `Delete` to delete the `VolumeSnapshotContent` object and the underlying snapshot. Specify `Retain` if you want to keep the `VolumeSnapshotContent` and the underlying snapshot.

To use a [custom storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#custom_location), add a `storage-locations` parameter to the snapshot class. To use this parameter, your clusters must use version 1.21 or later.
           
           apiVersion: snapshot.storage.k8s.io/v1
           kind: VolumeSnapshotClass
           metadata:
             name: my-snapshotclass
           parameters:
             storage-locations: us-east2
           driver: pd.csi.storage.gke.io
           deletionPolicy: Delete
           

     * To create a [disk image](https://docs.cloud.google.com/compute/docs/images), add the following to the `parameters` field:
           
           parameters:
             snapshot-type: images
             image-family: IMAGE_FAMILY
           

Replace `IMAGE_FAMILY` with the name of your preferred image family, such as `preloaded-data`.

  2. Apply the manifest:
         
         kubectl apply -f volumesnapshotclass.yaml
         




### Create a `VolumeSnapshot`

A `VolumeSnapshot` object is a request for a snapshot of an existing `PersistentVolumeClaim` object. When you create a `VolumeSnapshot` object, GKE automatically creates and binds it with a `VolumeSnapshotContent` object, which is a resource in your cluster like a `PersistentVolume` object.

  1. Save the following manifest as `volumesnapshot.yaml`.
         
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshot
         metadata:
           name: my-snapshot
         spec:
           volumeSnapshotClassName: my-snapshotclass
           source:
             persistentVolumeClaimName: my-pvc
         

  2. Apply the manifest:
         
         kubectl apply -f volumesnapshot.yaml
         

After you create a `Volume` snapshot, GKE creates a corresponding `VolumeSnapshotContent` object in the cluster. This object stores the snapshot and bindings of `VolumeSnapshot` objects. You don't interact with `VolumeSnapshotContents` objects directly.

  3. Confirm that GKE created the `VolumeSnapshotContents` object:
         
         kubectl get volumesnapshotcontents
         

The output is similar to the following:
         
         NAME                                               AGE
         snapcontent-cee5fb1f-5427-11ea-a53c-42010a1000da   55s
         




After the `Volume` snapshot content is created, the CSI driver you specified in the `VolumeSnapshotClass` creates a snapshot on the corresponding storage system. After GKE creates a snapshot on the storage system and binds it to a `VolumeSnapshot` object on the cluster, the snapshot is ready to use. You can check the status by running the following command:
    
    
    kubectl get volumesnapshot \
      -o custom-columns='NAME:.metadata.name,READY:.status.readyToUse'
    

If the snapshot is ready to use, the output is similar to the following:
    
    
    NAME               READY
    my-snapshot        true
    

### Delete the test file

  1. Delete the test file that you created:
         
         kubectl exec POD_NAME \
             -- sh -c 'rm /usr/share/hello/hello.txt'
         

  2. Verify that the file no longer exists:
         
         kubectl exec POD_NAME \
             -- sh -c 'cat /usr/share/hello/hello.txt'
         

The output is similar to the following:
         
         cat: /usr/share/hello/hello.txt: No such file or directory
         




### Restore the volume snapshot

You can reference a `VolumeSnapshot` in a `PersistentVolumeClaim` to provision a new volume with data from an existing volume or restore a volume to a state that you captured in the snapshot.

To reference a `VolumeSnapshot` in a `PersistentVolumeClaim`, add the `dataSource` field to your `PersistentVolumeClaim`. The same process is used whether the `VolumeSnapshotContents` refers to a disk image or a snapshot.

In this example, you reference the `VolumeSnapshot` that you created in a new `PersistentVolumeClaim` and update the `Deployment` to use the new claim.

  1. Verify if you're using a disk or image snapshot, which differ as follows:

     * **Disk snapshots** : Take snapshots frequently and restore infrequently.
     * **Image snapshots** : Take snapshots infrequently and restore frequently. Image snapshots may also be slower to create than disk snapshots.

For details see [Snapshot frequency limits](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#freq_limits). Knowing your snapshot type helps if you need to troubleshoot any issues.

Inspect the `VolumeSnapshot`:
    
    kubectl describe volumesnapshot SNAPSHOT_NAME
    

The `volumeSnapshotClassName` field specifies the snapshot class.
    
    kubectl describe volumesnapshotclass SNAPSHOT_CLASS_NAME
    

The `snapshot-type` parameter will specify `snapshots` or `images`. If it is not given, the default is `snapshots`.

If there is no snapshot class (for instance, if the snapshot was statically created), inspect the `VolumeSnapshotContents`. `sh kubectl describe volumesnapshotcontents SNAPSHOT_CONTENTS_NAME` The format of a snapshot handle in the output tells you the type of snapshot, as follows: * `projects/PROJECT_NAME/global/snapshots/SNAPSHOT_NAME`: disk snapshot

     * `projects/PROJECT_NAME/global/images/IMAGE_NAME`: image snapshot


  1. Save the following manifest as `pvc-restore.yaml`:

###  Persistent Disk 
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: pvc-restore
         spec:
           **dataSource :
             name: my-snapshot
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
         

  3. Update the `my-deployment.yaml` file to use the new `PersistentVolumeClaim`:
         
         ...
         volumes:
         - name: my-volume
           persistentVolumeClaim:
             claimName: pvc-restore
         

  4. Apply the updated manifest:
         
         kubectl apply -f my-deployment.yaml
         




### Check that the snapshot restored successfully

  1. Get the name of the new `Pod` that GKE creates for the updated `Deployment`:
         
         kubectl get pods -l app=hello-app
         




Verify that the test file exists:
    
    
       kubectl exec NEW_POD_NAME \
           -- sh -c 'cat /usr/share/hello/hello.txt'
    

Replace `NEW_POD_NAME` with the name of the new `Pod` that GKE created.

The output is similar to the following:
    
    
       Hello World!
    

## Import a pre-existing snapshot

You can use an existing volume snapshot created outside the current cluster to manually provision the `VolumeSnapshotContents` object. For example, you can populate a volume in GKE with a snapshot of another Google Cloud resource created in a different cluster.

  1. Locate the name of your snapshot.

###  Google Cloud console 

[Go to Snapshots page](https://console.cloud.google.com/compute/snapshots)

###  Google Cloud CLI 

Run the following command:
         
         gcloud compute snapshots list
         

The output is similar to the following:
         
         NAME                                           DISK_SIZE_GB  SRC_DISK                                                     STATUS
         snapshot-5e6af474-cbcc-49ed-b53f-32262959a0a0  1             us-central1-b/disks/pvc-69f80fca-bb06-4519-9e7d-b26f45c1f4aa READY
         

  2. Save the following `VolumeSnapshot` manifest as `restored-snapshot.yaml`.
         
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshot
         metadata:
           name: restored-snapshot
         spec:
           volumeSnapshotClassName: my-snapshotclass
           source:
             volumeSnapshotContentName: restored-snapshot-content
         

  3. Apply the manifest:
         
         kubectl apply -f restored-snapshot.yaml
         

  4. Save the following `VolumeSnapshotContent` manifest as `restored-snapshot-content.yaml`. Replace the `snapshotHandle` field with your project ID and snapshot name. Both `volumeSnapshotRef.name` and `volumeSnapshotRef.namespace` must point to the previously created `VolumeSnapshot` for the bi-directional binding to be valid.
         
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshotContent
         metadata:
           name: restored-snapshot-content
         spec:
           deletionPolicy: Retain
           driver: pd.csi.storage.gke.io
           source:
             snapshotHandle: projects/PROJECT_ID/global/snapshots/SNAPSHOT_NAME
           volumeSnapshotRef:
             kind: VolumeSnapshot
             name: restored-snapshot
             namespace: default
         

  5. Apply the manifest:
         
         kubectl apply -f restored-snapshot-content.yaml
         

  6. Save the following `PersistentVolumeClaim` manifest as `restored-pvc.yaml`. The Kubernetes storage controller will find a `VolumeSnapshot` named `restored-snapshot` and then try to find, or dynamically create, a `PersistentVolume` as the data source. You can then utilize this PVC in a Pod to access the restored data.
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: restored-pvc
         spec:
           dataSource:
             name: restored-snapshot
             kind: VolumeSnapshot
             apiGroup: snapshot.storage.k8s.io
           storageClassName: standard-rwo
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: 1Gi
         

  7. Apply the manifest:
         
         kubectl apply -f restored-pvc.yaml
         

  8. Save the following `Pod` manifest as `restored-pod.yaml` referring to the `PersistentVolumeClaim`. The CSI driver will provision a `PersistentVolume` and populate it from the snapshot.
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: restored-pod
         spec:
           containers:
           - name: busybox
             image: busybox
             args:
             - sleep
             - "3600"
             volumeMounts:
             - name: source-data
               mountPath: /demo/data
           volumes:
           - name: source-data
             persistentVolumeClaim:
               claimName: restored-pvc
               readOnly: false
         

  9. Apply the manifest:
         
         kubectl apply -f restored-pod.yaml
         

  10. Verify that the file has been restored:
         
         kubectl exec restored-pod -- sh -c 'cat /demo/data/hello.txt'
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps.

  1. Delete the `VolumeSnapshot`:
         
         kubectl delete volumesnapshot my-snapshot
         

**Note:** If a volume snapshot's `VolumeSnapshotClass` has `deletionPolicy:Delete`, the corresponding `VolumeSnapshotContent` and the physical snapshot on the storage system are also deleted. If it has a `deletionPolicy:Retain`, GKE retains the underlying snapshot.
  2. Delete the `VolumeSnapshotClass`:
         
         kubectl delete volumesnapshotclass my-snapshotclass
         

  3. Delete the `Deployment`:
         
         kubectl delete deployments hello-app
         

  4. Delete the `PersistentVolumeClaim` objects:
         
         kubectl delete pvc my-pvc pvc-restore
         




## What's next

  * Read the [Kubernetes Volume Snapshot](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-feature-cis-volume-snapshot-beta/) documentation.
  * Learn about [volume expansion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/volume-expansion).
  * Learn how to [manually install a CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/install-csi-driver). 
  * Learn about [block storage (Persistent Disk) for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview#pd). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
