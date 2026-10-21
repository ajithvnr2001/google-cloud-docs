---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-csi-driver/
title: Install a Container Storage Interface driver \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:21:54.741632+00:00
---

# Install a Container Storage Interface driver  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-csi-driver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Install a Container Storage Interface driver Stay organized with collections  Save and categorize content based on your preferences. 

Installing a Container Storage Interface (CSI) driver lets you provision and manage persistent storage for stateful workloads in Google Distributed Cloud clusters. After you install a driver by following your storage vendor's instructions, you can verify the installation and create a `StorageClass` to dynamically provision volumes for your applications.

## Overview

[Container Storage Interface](https://github.com/container-storage-interface/spec) (CSI) is an open standard API supported by many major storage vendors that enables Kubernetes to expose arbitrary storage systems to containerized workloads.

Kubernetes volumes are managed by vendor-specific storage drivers, which have historically been [compiled into Kubernetes binaries](https://kubernetes.io/docs/concepts/storage/#types-of-volumes). Previously, you couldn't use a storage driver that was not included with Kubernetes. Installing a CSI driver adds support for a storage system that is not natively supported by Kubernetes. Also, CSI enables the use of modern storage features, such as snapshots and resizing.

To use a CSI driver, you need to create a Kubernetes [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/). You set the CSI driver as the provisioner for the StorageClass. Then, you can [set the StorageClass as the cluster's default](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/default-storage-class), or configure your workloads to use the StorageClass (StatefulSet example).

## Install a vendor's CSI driver

Storage vendors develop their own CSI drivers, and they are responsible for providing installation instructions. In simple cases, installation might only involve deploying manifests to your clusters. See the list of [CSI drivers](https://kubernetes-csi.github.io/docs/drivers.html) in the CSI documentation.

For production storage, we recommend installing a CSI driver from an [GDC Ready storage partner](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

**Note:** Google does not provide support for, nor instructions for installing, vendors' drivers.

## Verify a driver installation

After you install a CSI driver, you can verify the installation by running:
    
    
    kubectl get csinodes -o jsonpath='{range .items[*]} \
        {.metadata.name}{": "} {range .spec.drivers[*]} {.name}{"\n"} {end}{end}'
    

## Use a CSI driver

To use a CSI driver:

  1. Create a Kubernetes [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) that references the driver in its `provisioner` field.

  2. To provision storage, you can either:

     * Reference the StorageClass in the `volumeClaimTemplates` specification for a [StatefulSet](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) object.
     * [Set it as the cluster's default StorageClass](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/default-storage-class).



### Considerations for StorageClasses backed by a CSI driver

When you create a StorageClass, consider the following:

  * CSI driver documentation should include the [driver-specific parameters](https://kubernetes.io/docs/concepts/storage/storage-classes/#the-storageclass-resource) that you provide to your StorageClass, including the provisioner name.
  * You should name the StorageClass after its properties, rather than after the name of the specific driver or appliance behind it. Naming the StorageClass after its properties lets you create StorageClasses with the same name across multiple clusters and environments, and allows your applications to get storage with the same properties across clusters.



### Example: Reference StorageClass in a StatefulSet

The following example models how to define a CSI driver in a StorageClass, and then reference the StorageClass in a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) workload. The example assumes the driver has already been installed to the cluster.

The following simple StorageClass, `premium-rwo`, uses a fictional CSI driver, `csi.example.com`, as its provisioner:

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
          storageClassName: premium-rwo # This field references the existing StorageClass

## What's next

  * [Read more about Google Distributed Cloud storage concepts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/storage)
  * [Set a default StorageClass for your cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/default-storage-class)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
