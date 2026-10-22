---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-statefulset-csi-migration-tool/
title: Using the StatefulSet CSI Migration Tool \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:29.887626+00:00
---

# Using the StatefulSet CSI Migration Tool  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-statefulset-csi-migration-tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Using the StatefulSet CSI Migration Tool Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use the StatefulSet CSI Migration Tool to migrate stateful workloads from an in-tree vSphere volume plugin to the vSphere CSI Driver in Google Distributed Cloud.

The following list shows the launch stage for this tool per version:

  * v1.0: GA
  * v0.1: [Preview](https://cloud.google.com/products/#product-launch-stages)



Supported Google Distributed Cloud versions: 1.30 - 1.28.

## Overview

Google Distributed Cloud integrates with external block or file storage systems through VMware vSphere storage, Kubernetes in-tree volume plugins (or "drivers"), and Container Storage Interface (CSI) drivers.

With the Kubernetes CSI migration feature enabled by default in 1.15, a PersistentVolume backed by the in-tree vSphere volume plugin continues functioning in a CSI-only environment. The CSI migration feature redirects in-tree plugin operation calls to the CSI driver. Because the PersistentVolume spec is immutable, it is still backed by the in-tree plugin. The set of available features is the same as for the in-tree volume plugin.

The full set of CSI features, like Volume Expansion and Volume Snapshot, isn't available for such volumes. To take advantage of these features, stateful workloads must be completely migrated to CSI by recreating the PersistentVolumes backed by the vSphere CSI Driver. You can use the CSI migration tool to migrate stateful workloads to CSI and use the full set of CSI features.

This tool provides a way to rolling migrate a StatefulSet's PersistentVolume and PersistentVolumeClaim to CSI and does not involve application downtime. This tooling takes the backup of Kubernetes resources in a local directory and sets `ReclaimPolicy` to `Retain` before migration. So there will be no data loss.

## Limitation

  * The automated tooling is only supported on Google Distributed Cloud versions that are [fully supported](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history).

  * It only works with StatefulSets. You can run preflight checks using the tool to run a few safety checks before using the tools.



    
    
    ./statefulset-csi-migration-tool preflight \
          --kubeconfig ADMIN_KUBECONFIG \
          --cluster-name USER_CLUSTER_NAME \
          --sts-name STS_NAME \
          --sts-namespace STS_NAMESPACE \
          --intree-storageclass INTREE_STORAGECLASS \
          --csi-storageclass CSI_STORAGECLASS
    

Replace the following:

  * `ADMIN_KUBECONFIG`: the path of your admin cluster kubeconfig file.

  * `USER_CLUSTER_NAME`: If the StatefulSet is running on the user cluster, then provide the user cluster name. Skip this flag if the workload is running on the admin cluster.

  * `STS_NAME`: name of the StatefulSet.

  * `STS_NAMESPACE`: namespace of the StatefulSet.

  * `INTREE_STORAGECLASS`: the in-tree StorageClass name backing the StatefulSet's PersistentVolume.

  * `CSI_STORAGECLASS`: the CSI StorageClass name backing the StatefulSet's PersistentVolume after migration.




## Download

Download the tool at `gs://gke-on-prem-release/statefulset-csi-migration-tool/v1.0/statefulset-csi-migration-tool`. Note this tool is in preview.

## Procedure

This section provides the steps needed for migrating StatefulSet from vSphere in-tree **vCP** internal provisioner (`kubernetes.io/vsphere-volume`) to vSphere **CSI** provisioner (`csi.vsphere.vmware.com`).
    
    
    ./statefulset-csi-migration-tool rolling-migration all \
          --kubeconfig ADMIN_KUBECONFIG \
          --cluster-name USER_CLUSTER_NAME \
          --sts-name STS_NAME \
          --sts-namespace STS_NAMESPACE \
          --intree-storageclass INTREE_STORAGECLASS \
          --csi-storageclass CSI_STORAGECLASS \
          --working-directory WORKING_DIRECTORY
    

Replace the following:

  * ADMIN_KUBECONFIG: the path of your admin cluster kubeconfig file.

  * USER_CLUSTER_NAME: If the StatefulSet is running on the user cluster, then provide the user cluster name. Skip this flag if the workload is running on the admin cluster.

  * STS_NAME: name of the StatefulSet.

  * STS_NAMESPACE: namespace of the StatefulSet.

  * INTREE_STORAGECLASS: the in-tree StorageClass name backing the StatefulSet's PersistentVolume.

  * CSI_STORAGECLASS: the CSI StorageClass name backing the StatefulSet's PersistentVolume after migration.

  * WORKING_DIRECTORY: the local directory to save the Kubernetes resource spec of StatefulSet and its Pod, PersistentVolumeClaim and PersistentVolume. The directory name must be unique for each StatefulSet. This directory should be empty or not exist. It is ideal to not create this directory so that the tooling can create one for you.




This command performs the following tasks:

  1. Takes a backup of the StatefulSet and its dependencies like PersistentVolume, PersistentVolumeClaim and Pod replica specs in the local working directory.

  2. Deletes the StatefulSet with orphan deletion policy. This step only deletes the StatefulSet but does not delete its dependencies like the Pod replicas, PersistentVolume and PersistentVolumeClaim.

  3. Migrates each Pod to CSI drivers (similar to Option 1), and does the following:

a. Sets the PersistentVolume's ReclaimPolicy field as Retain.

b. Deletes the Pod, PersistentVolume and PersistentVolumeClaim.

c. Converts the existing VMDK to FCD.

d. Creates the PersistentVolume, PersistentVolumeClaim and Pod again.

  4. Recreates the StatefulSet, but the PVCTemplate field in its spec points to the CSI StorageClass. The StatefulSet controller should map to the orphaned replicas again.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
