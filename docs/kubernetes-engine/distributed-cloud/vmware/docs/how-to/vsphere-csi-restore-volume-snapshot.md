---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-csi-restore-volume-snapshot/
title: Restore a volume from a snapshot \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:47.544034+00:00
---

# Restore a volume from a snapshot  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-csi-restore-volume-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Restore a volume from a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to create a volume snapshot and then use the snapshot to restore the volume. The instructions here apply to clusters that use the [vSphere CSI driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-vsphere-csi-driver).

## Before you begin

Read [Using the vSphere Container Storage Interface driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-vsphere-csi-driver).

[Verify](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-vsphere-csi-driver#confirm_driver_availability) that your cluster has a StorageClass named `standard-rwo` and that the vSphere CSI driver is installed.

Your [vSphere version](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements), ESXi and vCenter Server, must be 7.0 Update 3 or later. For more information, see [Troubleshooting storage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/storage#vsphere-csi-volumesnapshot-not-ready-version).

## Overview of steps

These are the primary steps of the exercise given in this document:

  1. Create a PersistentVolumeClaim.
    Create a [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) that requests the `standard-rwo` storage class. The cluster then [dynamically provisions](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#dynamic) a PersistentVolume and associates it with your PersistentVolumeClaim.
  2. Create a Deployment.
    Create a Deployment that has one Pod. The Pod specifies a volume based on your PersistentVolumeClaim. The one container in the Pod mounts the volume at `/hello/`.
  3. Write a file to the Pod volume.
    Create a file named `hello.txt` in the Pod volume. The content of the file is "Hello World!".
  4. Create a VolumeSnapshot.
    Create a VolumeSnapshot that captures the state of the Pod volume.
  5. Corrupt the file.
    Alter the `hello.txt` file so that it looks like a corrupted file. The content of the file is now "Hello W-corrupted-file-orld!"
  6. Use the snapshot to restore the volume.
    Create a second PersistentVolumeClaim that uses your VolumeSnapshot as its data source. Edit your Deployment so that its volume is associated with the new PersistentVolumeClaim. Then verify that the `hello.txt` file has been restored.



## Create a PersistentVolumeClaim

Here is a manifest for a PersistentVolumeClaim:
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: my-pvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 5Gi
      storageClassName: standard-rwo
    

In the preceding manifest, you can see that `storageClassName` is set to `standard-rwo`. This is the storage class associated with the vSphere CSI driver.

Save the manifest in a file named `my-pvc.yaml`. Create and view the PersistentVolumeClaim:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f my-pvc.yaml
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get pvc my-pvc
    

In the output, you can see that the PersistentVolumeClaim is bound to a dynamically provisioned PersistentVolume. For example, the following output shows that the PersistentVolumeClaim named `my-pvc` is bound to a PersistentVolume named `pvc-467d211c-26e4-4d69-aaa5-42219aee6fd5`:
    
    
    my-pvc   Bound    pvc-467d211c-26e4-4d69-aaa5-42219aee6fd5  …  standard-rwo   100s
    

## Create a Deployment

Here is a manifest for a Deployment:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-deployment
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
            - name: my-volume
              mountPath: /hello/
          volumes:
          - name: my-volume
            persistentVolumeClaim:
              claimName: my-pvc
    

In the context of this exercise, these are the important points to understand about the preceding Deployment manifest:

  * The Pod requests storage by specifying the PersistentVolumeClaim, `my-pvc`, that you created earlier.

  * The Pod has one container, and the container mounts the volume at `/hello/`.




Save the manifest in a file named `my-deployment.yaml`, and create the Deployment:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f my-deployment.yaml
    

The Deployment has one Pod. Get the name of the Pod:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get pods
    

Make a note of the Pod name. For example, in the following output, the Pod name is `my-deployment-7575c4f5bf-r59nt`:
    
    
    my-deployment-7575c4f5bf-r59nt   1/1     Running   0          65s
    

Create a file in the Pod volume, and view the file.
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
        exec POD_NAME \
        -- sh -c 'echo "Hello World!" > /hello/hello.txt'
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
        exec POD_NAME \
        -- sh -c 'cat /hello/hello.txt'
    

The output shows the content of the file `/hello/hello.txt`:
    
    
    Hello World!
    

## Create a snapshot

Here is a manifest for a VolumeSnapshot:
    
    
    apiVersion: snapshot.storage.k8s.io/v1
    kind: VolumeSnapshot
    metadata:
      name: my-snapshot
    spec:
      volumeSnapshotClassName: csi-vsphere-snapshot-class
      source:
        persistentVolumeClaimName: my-pvc
    

Save the manifest in a file named `my-snapshot.yaml`, and create the VolumeSnapshot:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f my-snapshot.yaml
    

## Corrupt the file in the volume

Change the content of the `hello.txt` so that it looks like it has been corrupted:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
        exec POD_NAME \
        -- sh -c 'echo "Hello W-corrupted-file-orld!" > /hello/hello.txt'
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
        exec POD_NAME \
        -- sh -c 'cat /hello/hello.txt'
    

In the output, you can see that the file has been changed:
    
    
    Hello W-corrupted-file-orld!
    

## Restore

Here is a manifest for a second PersistentVolumeClaim:
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: my-pvc-2
    spec:
      storageClassName: standard-rwo
      dataSource:
        name: my-snapshot
        kind: VolumeSnapshot
        apiGroup: snapshot.storage.k8s.io
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 5Gi
    

In the preceding manifest, you can see that the data source for the new PersistentVolume claim is the VolumeSnapshot that you created previously.

Save the manifest in a file named `my-pvc-2.yaml`. Create and view the PersistentVolumeClaim:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f my-pvc-2.yaml
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get pvc my-pvc-2
    

Open the Deployment for editing:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG edit deployment my-deployment
    

Change `my-pvc` to `my-pvc-2`, and close the editor:
    
    
    …
      volumes:
      - name: my-volume
        persistentVolumeClaim:
        claimName: my-pvc-2
    

The Deployment deletes the Pod, and creates a new Pod that uses the new PersistentVolumeClaim.

Wait a few minutes, and then get the new Pod name:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get pods
    

Verify that the Pod volume has been restored:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
       exec NEW_POD_NAME \
       -- sh -c 'cat /hello/hello.txt'
    

The output shows that the volume has been restored:
    
    
    Hello World!
    

## Troubleshooting

For troubleshooting guidance, see [Troubleshooting storage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/storage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
