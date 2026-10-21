---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/preexisting-volume/
title: Import a preexisting Azure Disk volume \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:56.300343+00:00
---

# Import a preexisting Azure Disk volume  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/preexisting-volume/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Import a preexisting Azure Disk volume

If you already have an Azure Disk volume to use with GKE on Azure, you can create a PersistentVolume (PV) object and reserve it for a specific PersistentVolumeClaim (PVC).

This page explains how to create a PV by using an existing volume populated with data, and how to use the PV in a Pod.

## Before you begin

  * [Connect to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster)



## Create a PersistentVolume for a pre-existing volume

You can import an existing volume by specifying a new PV.

  1. Copy the following YAML into a file named `existing-volume.yaml`.:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: VOLUME_NAME
           annotations:
             pv.kubernetes.io/provisioned-by: disk.csi.azure.com
         spec:
           capacity:
             storage: VOLUME_CAPACITY
           accessModes:
             - ReadWriteOnce
           persistentVolumeReclaimPolicy: Retain
           storageClassName: STORAGE_CLASS_NAME
           claimRef:
             name: my-pvc
             namespace: default
           csi:
             driver: disk.csi.azure.com
             volumeHandle: /subscriptions/SUBSCRIPTION_ID/resourcegroups/RESOURCE_GROUP_NAME/providers/microsoft.compute/disks/DISK_NAME
             fsType: FILE_SYSTEM_TYPE
         

Replace the following:

     * VOLUME_NAME: a name for the volume
     * VOLUME_CAPACITY: size of the volume. For example, `30Gi`. For more information on specifying volume capacity in Kubernetes, see the [Meaning of memory](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/#meaning-of-memory).
     * STORAGE_CLASS_NAME: the name of the StorageClass that provisions the volume. For example, you can use the default `standard-rwo`.

**Note:** A StorageClass is required to reference other attributes like `allowVolumeExpansion`, even if a volume is not dynamically provisioned.
     * SUBSCRIPTION_ID: the Azure subscription ID that contains the volume.

     * RESOURCE_GROUP_NAME: the Azure resource group that contains the volume.

     * DISK_NAME: the Azure Disk name of the volume.

     * FS_TYPE: the [file system type](https://github.com/kubernetes-sigs/azuredisk-csi-driver/blob/master/docs/driver-parameters.md#dynamic-provisioning) of the volume. For example, `ext4`.

  2. Apply the YAML to your cluster
         
         kubectl apply -f existing-volume.yaml
         

  3. Confirm the creation of your PV
         
         kubectl describe pv VOLUME_NAME
         

The output of this command contains the status of the PV.




## Use the volume with a PersistentVolumeClaim and Pod

After you have imported your volume, you can create a PVC and a Pod that mounts the PVC.

  1. The following YAML creates a PVC and attaches it to a Pod running the Nginx web server. Copy it into a file named `nginx.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: my-pvc
         spec:
           storageClassName: STORAGE_CLASS_NAME
           volumeName: VOLUME_NAME
           accessModes:
             - ACCESS_MODE
           resources:
             requests:
               storage: VOLUME_CAPACITY
         ---
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: web-server
         spec:
           containers:
            - name: web-server
              image: nginx
              volumeMounts:
                - mountPath: /var/lib/www/html
                  name: data
           volumes:
            - name: data
              persistentVolumeClaim:
                claimName: my-pvc
         

Replace the following:

     * STORAGE_CLASS: the name of the StorageClass from the PersistentVolume you created previously. For example, `standard-rwo`.
     * ACCESS_MODE: the access mode of the volume. For Azure Disk, use `ReadWriteOnce`. For Azure File, use `ReadWriteMany`.
     * VOLUME_CAPACITY: size of the volume. For example, `30Gi`.
  2. Apply the YAML to your cluster
         
         kubectl apply -f nginx.yaml
         

  3. Check the status of your Nginx instance with `kubectl describe`. The output should have a `STATUS` of `Running`.
         
         kubectl describe pod web-server
         




## What's next

  * Use additional [storage drivers](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-drivers) with GKE on Azure.
  * Read the documentation for the [Azure Disk CSI driver](https://github.com/kubernetes-sigs/azuredisk-csi-driver/tree/v1.8.0/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
