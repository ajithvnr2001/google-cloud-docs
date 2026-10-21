---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/default-storage-class/
title: Set the default StorageClass \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:27.790059+00:00
---

# Set the default StorageClass  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/default-storage-class/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Set the default StorageClass Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/default-storage-class)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/default-storage-class)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page shows how to set the default StorageClass for an Distributed Cloud cluster.

## Overview

Google Distributed Cloud can integrate with block or file storage by using any of the following mechanisms:

  * [Kubernetes in-tree volume plugins](https://kubernetes.io/docs/concepts/storage/volumes/#types-of-volumes)
  * [Container Storage Interface (CSI)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-csi-driver)



## Default StorageClass

When you request storage with a [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PVC), you can specify a StorageClass. If you do not specify a StorageClass, the default StorageClass is used if one is configured in the cluster. Google Distributed Cloud does not configure a default StorageClass. For example, suppose you create a PVC that does not specify a StorageClass. The volume controller will fulfill the claim according to the default StorageClass.

## Change the default StorageClass

As a cluster administrator, you might want to change the default storage class. Then all requests for storage that do not specify a StorageClass will be fulfilled according to the StorageClass of your choice. This section gives the steps for changing the default.

### Deploy a new storage system

Deploy a new storage system and any software components for integrating the new storage mechanism with a Kubernetes cluster. For example, you might need to [install a CSI driver](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-csi-driver) in the cluster.

### Mark any existing default StorageClass as non-default

Search your cluster for any existing default StorageClass if one already exists and mark it as non-default. For details, see [Change the default StorageClass](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/).

### Create a new StorageClass

[Create a manifest for a new StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/). Include the `storageclass.kubernetes.io/is-default-class: "true"` annotation. For example:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      annotations:
        storageclass.kubernetes.io/is-default-class: "true"
      ...
      name: my-storage-class
      ...
    parameters:
      ...
    provisioner: [MY_PROVISIONER]
    ...
    

Save your manifest as a YAML file, and create the new StorageClass:
    
    
    kubectl --kubeconfig [CLUSTER_KUBECONFIG] apply -f [MANIFEST_FILE]
    

where [MANIFEST_FILE] is the path to your new StorageClass manifest file.

## What's next

  * [Read about Google Distributed Cloud's storage concepts](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/storage)

  * [Install a CSI driver](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-csi-driver)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
