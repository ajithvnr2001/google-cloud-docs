---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/install-csi-driver/
title: Installing a Container Storage Interface driver \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:00.374348+00:00
---

# Installing a Container Storage Interface driver  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/install-csi-driver/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Installing a Container Storage Interface driver Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/install-csi-driver)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/install-csi-driver)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page explains how to install a Container Storage Interface (CSI) storage driver to Google Distributed Cloud clusters.

## Overview

[CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md) is an open standard API that enables Kubernetes to expose arbitrary storage systems to containerized workloads. When you deploy a CSI-compatible storage driver to a Google Distributed Cloud cluster, the cluster can connect directly to a compatible storage device without having to go through vSphere storage.

Kubernetes volumes are managed by vendor-specific storage drivers, which have historically been [compiled into Kubernetes binaries](https://kubernetes.io/docs/concepts/storage/). Previously, you could not use a storage driver that was not included with Kubernetes. Installing a CSI driver adds support for a storage system that is not natively supported by Kubernetes. Also, CSI enables the use of modern storage features, such as snapshots and resizing.

To use a CSI driver, you need to create a Kubernetes [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/). You set the CSI driver as the provisioner for the StorageClass. Then, you can [set the StorageClass as the cluster's default](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/default-storage-class), or configure your workloads to use the StorageClass (StatefulSet example).

## Before you begin

By default, Google Distributed Cloud uses vSphere datastores via the built-in [vsphereVolume](https://kubernetes.io/docs/concepts/storage/volumes/#vspherevolume) driver. Additionally, the built-in drivers for NFS and iSCSI can attach and mount existing volumes to your workloads.

**Note:** The built-in [NFS](https://kubernetes.io/docs/concepts/storage/volumes/#nfs) and [iSCSI](https://kubernetes.io/docs/concepts/storage/volumes/#iscsi) drivers cannot provision new volumes. For dynamic provisioning, you need a CSI storage driver specific to your storage appliance.

## Installing a vendor's CSI driver

Storage vendors develop their own CSI drivers, and they are responsible for providing installation instructions. In simple cases, installation might only involve deploying manifests to your clusters. See the list of [CSI drivers](https://kubernetes-csi.github.io/docs/drivers.html) in the CSI documentation.

**Note:** Google does not provide support for, nor instructions for installing, vendors' drivers.

## Verifying a driver installation

After you install a CSI driver, you can verify the installation by running one of the following commands, depending on your cluster's Google Distributed Cloud version:

### 1.2.0-gke.5
    
    
    kubectl get csinodes \
    -o jsonpath='{range .items[*]} {.metadata.name}{": "} {range .spec.drivers[*]} {.name}{"\n"} {end}{end}'

### 1.1.0-gke.6
    
    
    kubectl get nodes \
    -o jsonpath='{.items[*].metadata.annotations.csi\.volume\.kubernetes\.io\/nodeid}'

## Using a CSI driver

To use a CSI driver:

  1. Create a Kubernetes [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) that references the driver in its `provisioner` field.

  2. To provision storage, you can either:

     * Reference the StorageClass in the `volumeClaimTemplates` specification for a [StatefulSet](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) object.
     * [Set it as the cluster's default StorageClass](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/default-storage-class).



### Considerations for StorageClasses backed by a CSI driver

When you create a StorageClass, consider the following:

  * CSI driver documentation should include the [driver-specific parameters](https://kubernetes.io/docs/concepts/storage/storage-classes/#the-storageclass-resource) that you provide to your StorageClass, including the provisioner name.
  * You should name the StorageClass after its properties, rather than after the name of the specific driver or appliance behind it. Naming the StorageClass after its properties allows you to create StorageClasses with the same name across multiple clusters and environments, and allows your applications to get storage with the same properties across clusters.



### Example: Reference StorageClass in a StatefulSet

The following example models how to define a CSI driver in a StorageClass, and then reference the StorageClass in a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) workload. The example assumes the driver has already been installed to the cluster.

Below is a simple StorageClass named `premium-rwo` that uses a fictional CSI driver, `csi.example.com`, as its provisioner:

### fast-sc.yaml
    
    
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

When you reference a StorageClass in a StatefulSet's `volumeClaimTemplates` specification, Kubernetes provides stable storage using PersistentVolumes (PVs). Kubernetes calls the provisioner defined in the StorageClass to create a new storage volume. In this case, Kubernetes calls the fictional `csi.example.com` provider, which calls out to the provider's API, to create a volume. After the volume is provisioned, Kubernetes automatically creates a PV to represent the storage.

Here is a simple StatefulSet that references the StorageClass:

### statefulset.yaml
    
    
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
          storageClassName: fast # This field references the existing StorageClass

## What's next

  * [Read more about Google Distributed Cloud storage concepts](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/storage)
  * [Set a default StorageClass for your cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/default-storage-class)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
