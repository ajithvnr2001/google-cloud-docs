---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/install-csi-driver/
title: Manually install a CSI driver \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:32.414552+00:00
---

# Manually install a CSI driver  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/install-csi-driver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Manually install a CSI driver Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to install a Container Storage Interface (CSI) storage driver on Google Kubernetes Engine (GKE) Standard clusters. This page doesn't apply to GKE Autopilot clusters, which automatically use the [Compute Engine persistent disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#using_the_for_linux_clusters).

If you are using the [Compute Engine persistent disk CSI driver](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver) in your Standard cluster, we recommend [automatically deploying the driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver) to reduce your management overhead.

## Overview

[CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md) is an open standard API that enables Kubernetes to expose arbitrary storage systems to containerized workloads. Kubernetes volumes are managed by vendor-specific storage drivers, which have historically been [compiled into Kubernetes binaries](https://kubernetes.io/docs/concepts/storage/volumes/#types-of-volumes). Previously, you could not use a storage driver that was not included with Kubernetes. Installing a CSI driver adds support for a storage system that is not natively supported by Kubernetes. Also, CSI enables the use of modern storage features, such as snapshots and resizing.

**Note:** Google Distributed Cloud 1.5 does not support Kubernetes CSI snapshots.

## Installing a vendor's CSI driver

Other storage vendors develop their own CSI drivers, and they are responsible for providing installation instructions. In simple cases, installation might only involve deploying manifests to your clusters. See the list of [CSI drivers](https://kubernetes-csi.github.io/docs/drivers.html) in the CSI documentation.

**Note:** Google does not provide support for, nor instructions for installing, other vendors' drivers.

## Verifying a driver installation

After you install a CSI driver, you can verify the installation by running one of the following commands, depending on your cluster's GKE version:

### 1.14+
    
    
    kubectl get csinodes \
    -o jsonpath='{range .items[*]} {.metadata.name}{": "} {range .spec.drivers[*]} {.name}{"\n"} {end}{end}'

### 1.13.x
    
    
    kubectl get nodes \
    -o jsonpath='{.items[*].metadata.annotations.csi\.volume\.kubernetes\.io\/nodeid}'

## Using a CSI driver

To use a CSI driver:

  1. Create a Kubernetes [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) that references the driver in its `provisioner` field, if a StorageClass is not created for you as part of driver installation. Some CSI drivers deploy a StorageClass when you install them.

  2. To provision storage, you can either:

     * Reference the StorageClass in the `volumeClaimTemplates` specification for a [StatefulSet](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) object.
     * [Set it as the cluster's default StorageClass](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/).



### Considerations for StorageClasses backed by a CSI driver

When you create a StorageClass, consider the following:

  * CSI driver documentation should include the [driver-specific parameters](https://kubernetes.io/docs/concepts/storage/storage-classes/#the-storageclass-resource) that you provide to your StorageClass, including the provisioner name.
  * You should name the StorageClass after its properties, rather than after the name of the specific driver or appliance behind it. Naming the StorageClass after its properties allows you to create StorageClasses with the same name across multiple clusters and environments, and allows your applications to get storage with the same properties across clusters.



### Example: Reference StorageClass in a StatefulSet

The following example models how to define a CSI driver in a StorageClass, and then reference the StorageClass in a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) workload. The example assumes the driver has already been installed to the cluster.

The following is a simple StorageClass named `premium-rwo` that uses a fictional CSI driver, `csi.example.com`, as its provisioner:
    
    
    # fast-sc.yaml
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: premium-rwo
    provisioner: csi.example.com # CSI driver
    parameters: # You provide vendor-specific parameters to this specification
      type: example-parameter # Be sure to follow the vendor's instructions
      datastore: my-datastore
    reclaimPolicy: Retain
    allowVolumeExpansion: true
    

You reference the StorageClass in a StatefulSet's `volumeClaimTemplates` specification.

When you reference a StorageClass in a StatefulSet's `volumeClaimTemplates` specification, Kubernetes provides stable storage using PersistentVolumes. Kubernetes calls the provisioner defined in the StorageClass to create a new storage volume. In this case, Kubernetes calls the fictional `csi.example.com` provider, which calls out to the provider's API, to create a volume. After the volume is provisioned, Kubernetes automatically creates a PersistentVolume to represent the storage.

Here is a simple StatefulSet that references the StorageClass:
    
    
    # statefulset.yaml
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: web
    spec:
      replicas: 2
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

  * Learn more about GKE [storage concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
