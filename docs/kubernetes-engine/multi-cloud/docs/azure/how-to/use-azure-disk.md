---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/use-azure-disk/
title: Use an Azure Disk volume \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:58.042333+00:00
---

# Use an Azure Disk volume  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/use-azure-disk/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use an Azure Disk volume

GKE on Azure automatically deploys the [`azuredisk-csi-driver`](https://github.com/kubernetes-sigs/azuredisk-csi-driver) to provision and manage Azure Disk volumes in your clusters.

The GKE on Azure Azure Disk CSI Driver version is tied to a Kubernetes cluster version. The driver version is typically the latest available when the GKE version is released. When the cluster is upgraded, the drivers update automatically.

For more information on how GKE on Azure provides persistent storage, see [Storage overview](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/storage).

## Default storage classes

GKE on Azure provides the following StorageClass options by default:

  * `standard-rwo` (default): Provisions standard SSD Azure disks with [LRS](https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy#redundancy-in-the-primary-region)
  * `premium-rwo`: Provisions premium SSD Azure disks with LRS



## Before you begin

  * [Connect to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster)



## Use the default StorageClass

When you create a PersistentVolumeClaim without setting the field `spec.storageClassName`, GKE on Azure provisions an Azure [Standard SSD volume](https://azure.microsoft.com/en-us/blog/preview-standard-ssd-disks-for-azure-virtual-machine-workloads/) using the default GKE on Azure Azure Disk CSI Driver StorageClass.

The following YAML creates a PersistentVolumeClaim (PVC) named `mypvc` with a size of 30 gibibytes.
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: mypvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 30Gi
    

## Use the premium storage class

When you create a PersistentVolumeClaim and sed the field `spec.storageClassName` to `premium-rwo`, GKE on Azure provisions an Azure [premium SSD volume](https://azure.microsoft.com/en-us/blog/preview-standard-ssd-disks-for-azure-virtual-machine-workloads/).

The following YAML creates a PersistentVolumeClaim (PVC) named `mypvc` with a size of 30 gibibytes.
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: mypvc
    spec:
      storageClassName: premium-rwo
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 30Gi
    

## Reference the StorageClass in a StatefulSet

To use your new StorageClass, you can reference it in a StatefulSet's `volumeClaimTemplates`.

When you reference a StorageClass in a StatefulSet's `volumeClaimTemplates` specification, Kubernetes provides stable storage using PersistentVolumes (PVs). Kubernetes calls the provisioner defined in the StorageClass to create a new storage volume. After the volume is provisioned, Kubernetes automatically creates a PV.

The following StatefulSet references the `premium-rwo` StorageClass and provisions a 1 gibibyte volume:
    
    
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
          storageClassName: premium-rwo # This field references the existing StorageClass
    

## What's next

  * Read the documentation for the [Azure Disk CSI driver](https://github.com/kubernetes-sigs/azuredisk-csi-driver/tree/v1.8.0/docs).

  * [Create a custom storage class](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-class) with specific parameters.

  * Learn about [Persistent volumes in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).

  * Install [Storage drivers](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/storage-drivers) on your GKE on Azure cluster.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
