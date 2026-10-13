---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/use-azure-file/
title: Use an Azure File share \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:28.424252+00:00
---

# Use an Azure File share  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/use-azure-file/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use an Azure File share

GKE on Azure supports mounting [Azure Files](https://azure.microsoft.com/en-us/services/storage/files/#documentation) shares. If you already have an Azure File share to use with GKE on Azure, you can create a PersistentVolume (PV) object and reserve it for a specific PersistentVolumeClaim (PVC).

This page explains how to create a PV by using an existing share populated with data, and how to use the PV in a Pod.

## Before you begin

  * [Connect to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster)
  * Have access to or create an Azure File share. For more information, see [Create an Azure file share](https://docs.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share?tabs=azure-portal).



## Store your Azure storage account information

GKE on Azure stores information to access your Azure storage account in a Secret. If you haven't created a Secret in your cluster, you must add one. If you have this Secret in you cluster, skip to Create a PersistentVolume for a pre-existing share.

  1. To create the Secret, copy the following manifest into a file named 'azure-service-account-key.yaml'.
         
         ---
         apiVersion: v1
         kind: Secret
         metadata:
           name: azure-secret-account-key
         type: Opaque
         stringData:
           accountname: STORAGE_ACCOUNT_NAME
           accountkey: STORAGE_ACCOUNT_KEY
         

Replace the following:

     * STORAGE_ACCOUNT_NAME: your Azure storage account name
     * STORAGE_ACCOUNT_KEY: your Azure storage account key
  2. Apply the file to your cluster with the `kubectl` tool:
         
         kubectl apply -f azure-service-account-key.yaml
         




## Create a PersistentVolume for a pre-existing share

You import an existing Azure File share by specifying a new PV in your cluster. To create the PV, do the following:

  1. Copy the following YAML into a file named `existing-volume.yaml`:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: VOLUME_NAME
         spec:
           capacity:
             storage: VOLUME_CAPACITY
           storageClassName: standard-rwx
           accessModes:
             - ReadWriteMany
           persistentVolumeReclaimPolicy: Retain
           csi:
             driver: file.csi.azure.com
             readOnly: false
             volumeHandle: VOLUME_ID
         

Replace the following:

     * VOLUME_NAME: a name for the volume
     * VOLUME_CAPACITY: size of the volume. For example, `30Gi`. For more information on specifying volume capacity in Kubernetes, see the [Meaning of memory](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/#meaning-of-memory).
     * VOLUME_ID: a unique ID for the volume, formatted as a string of `RESOURCE_GROUP_NAME#STORAGE_ACCOUNT_NAME#FILESHARE_NAME#` where
     * FILE_SHARE_NAME: the Azure File share name

If your storage account is in a different resource group than your cluster, you need to add a reference to a Secret that contains your storage account key. To add the reference, insert the following in the `spec.csi` section:
    
    # Optional. Only required if your storageAccount is in a different resource group than the cluster.
        nodeStageSecretRef:
          name: NODE_STAGE_SECRET_NAME
          namespace: NODE_STAGE_SECRET_NAMESPACE
    

Replace the following:

     * NODE_STAGE_SECRET_NAME: the name of the Secret
     * NODE_STAGE_SECRET_NAMESPACE the Namespace that contains the Secret
  2. Apply the YAML to your cluster.
         
         kubectl apply -f existing-volume.yaml
         

  3. Confirm the creation of your PV with `kubectl describe pv`.
         
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
  2. Apply the YAML to your cluster.
         
         kubectl apply -f nginx.yaml
         

  3. Check the status of your Nginx instance with `kubectl describe`. The output should have a `STATUS` of `Running`.
         
         kubectl describe pod web-server
         

  4. To delete the Pod, use the `kubectl delete` command.
         
         kubectl delete -f nginx.yaml
         




## What's next

  * Use additional [storage drivers](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-drivers) with GKE on Azure.
  * Read the documentation for the [Azure File CSI driver](https://github.com/kubernetes-sigs/azurefile-csi-driver/tree/v1.7.0/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
