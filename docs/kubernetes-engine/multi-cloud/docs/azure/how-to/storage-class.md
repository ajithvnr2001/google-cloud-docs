---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-class/
title: Use a custom StorageClass with your workloads \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:41.026753+00:00
---

# Use a custom StorageClass with your workloads  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-class/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use a custom StorageClass with your workloads

To define specific storage behaviors for your containerized workloads on Google Kubernetes Engine (GKE) on Azure, create and use custom StorageClasses. By customizing StorageClasses, you can optimize storage performance and cost for your applications by selecting different Azure disk types, file system types, and other parameters for your PersistentVolumes. This capability helps you run efficient services by tailoring storage to your workload's exact needs.

GKE on Azure automatically deploys and manages the Azure Disk CSI Driver and Azure File CSI Driver, which are essential for handling storage provisioning. The versions of these drivers are tied to your GKE on Azure Kubernetes version and update automatically with cluster upgrades, ensuring seamless compatibility for your custom StorageClasses.

## Use a custom StorageClass

You can create additional StorageClasses for volumes or use Container Storage Interface (CSI) Drivers.

  1. Choose if you are using an Azure disk volume or another CSI driver.

### Azure Disk Volume

You can create your own custom StorageClass that specifies an Azure Disk volume type, file system type, and other parameters. You can find additional StorageClass parameters on the GKE on Azure Azure Disk CSI Driver [GitHub page](https://github.com/kubernetes-sigs/azuredisk-csi-driver/blob/v1.8.0/docs/driver-parameters.md).

To configure a custom StorageClass, copy the following YAML manifest into a file named `my-custom-class.yaml`.
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
          name: CLASS_NAME
         provisioner: disk.csi.azure.com
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true
         

Replace CLASS_NAME with the name of your new StorageClass.

For example, the following YAML creates a new StorageClass that provisions volumes in a [specific storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview) and applies a [tag](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources) of `group=dev` to each new volume.
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
          name: my-custom-class
         provisioner: disk.csi.azure.com
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true
         parameters:
          storageAccount: my-storage-account
          tags: group=dev
         

**Note:** GKE on Azure doesn't support the UltraSSD_LRS account type.

### CSI Driver

You can specify a different CSI driver in the `provisioner` field.

To create a StorageClass with another CSI driver, you can use the following example YAML.
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
          name: CLASS_NAME
         provisioner: CSI_DRIVER_NAME
         volumeBindingMode: WaitForFirstConsumer
         parameters:
          ...
         

Replace the following values:

     * CLASS_NAME: the name of the StorageClass (for example, `my-custom-class`).
     * CSI_DRIVER_NAME: the name of the CSI driver (for example, `csi.example.com`).

Next, configure subfields under `parameters` according to your CSI driver's documentation.

  2. Apply the YAML to your cluster.
         
         kubectl apply -f my-custom-class.yaml
         

  3. Create a PersistentVolumeClaim with a custom StorageClass.

After you create a custom StorageClass, you can specify it in a PVC. The following example creates a PVC named `my-pvc` that references the StorageClass `my-custom-class`.
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
          name: my-pvc
         spec:
          accessModes:
           - ReadWriteOnce
          resources:
           requests:
            storage: 30Gi
          storageclassName: my-custom-class
         




## Set the default StorageClass

GKE on Azure uses a default StorageClass called `standard-rwo` that provisions standard SSD Azure disks with [LRS](https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy#redundancy-in-the-primary-region). You can change the default to another StorageClass.

To change the default StorageClass:

  1. Update the `is-default-class` annotation for the `standard-rwo` StorageClass with `kubectl patch`.
         
         kubectl patch storageclass standard-rwo -p \
          '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
         

  2. Create a new StorageClass that has the annotation `storageclass.kubernetes.io/is-default-class: true`.

The following example StorageClass uses the `disk.csi.azure.com` driver. To install another storage driver, see [Installing a CSI driver](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-drivers).

Copy the following YAML into a file named `my-custom-class.yaml`.
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
          name: CLASS_NAME
          annotations:
           storageclass.kubernetes.io/is-default-class: true
         provisioner: disk.csi.azure.com
         volumeBindingMode: WaitForFirstConsumer
         parameters:
          skuName: VOLUME_TYPE
         

Replace the following:

     * CLASS_NAME: the name of your new StorageClass.
     * VOLUME_TYPE: the Azure Disk [volume type](https://docs.microsoft.com/en-us/azure/virtual-machines/disks-types) that the StorageClass creates.

For example, the following YAML creates a new default StorageClass that provisions [Premium SSD](https://docs.microsoft.com/en-us/azure/virtual-machines/disks-types#premium-ssds) Azure Disk volumes.
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
     name: my-custom-default-class
     annotations:
      storageclass.kubernetes.io/is-default-class: "true"
    provisioner: disk.csi.azure.com
    volumeBindingMode: WaitForFirstConsumer
    parameters:
     skuName: Premium_LRS
    

  3. Apply the new custom class to your cluster.
         
         kubectl apply -f my-custom-class.yaml
         




After applying this manifest, GKE on Azure uses the `my-custom-default-class` StorageClass for new storage requests.

## Reference the StorageClass in a StatefulSet

To use your new StorageClass, you can reference it in a StatefulSet's `volumeClaimTemplates`.

When you reference a StorageClass in a StatefulSet's `volumeClaimTemplates` specification, Kubernetes provides stable storage using PersistentVolumes (PVs). Kubernetes calls the provisioner defined in the StorageClass to create a new storage volume. After the volume is provisioned, Kubernetes automatically creates a PV.

The following StatefulSet references the `my-custom-class` StorageClass and provisions a 1 gibibyte volume:
    
    
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: web
    spec:
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: registry.k8s.io/nginx-slim:0.8
            volumeMounts:
            - name: www
              mountPath: /usr/share/nginx/html
      volumeClaimTemplates: # This is the specification in which you reference the StorageClass
      - metadata:
          name: www
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: 1Gi
          storageClassName: my-custom-class # This field references the existing StorageClass
    

## What's next

  * Read the documentation for the [Azure Disk CSI driver](https://github.com/kubernetes-sigs/azuredisk-csi-driver/tree/v1.8.0/docs) or the [Azure File CSI driver](https://github.com/kubernetes-sigs/azurefile-csi-driver/tree/v1.7.0/docs).

  * Learn about [Persistent volumes in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).

  * Install [Storage drivers](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-drivers) on your GKE on Azure cluster.

  * Deploy your first workload with the [Quickstart](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deploy-app).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
