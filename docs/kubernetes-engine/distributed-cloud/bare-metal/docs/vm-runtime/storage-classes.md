---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/storage-classes/
title: Create and use storage classes in VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:17.652963+00:00
---

# Create and use storage classes in VM Runtime on GDC  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/storage-classes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create and use storage classes in VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for application owners and platform administrators that run Google Distributed Cloud. This document shows you how to create and use storage classes for VMs that use VM Runtime on GDC. A `StorageClass` lets you define different storage configurations to provide for the various needs of your VMs.

## Before you begin

To complete this document, you need access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Google Distributed Cloud on Compute Engine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).

## Storage classes overview

You use a `StorageClass` to define the type of storage you make available to VMs. Different storage classes might map to a different type of storage hardware, file system, or performance. You can create and use storage classes to support your compute workloads in VM Runtime on GDC. For more information, see [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/).

A default `StorageClass` can be defined in the custom resource for VM Runtime on GDC. If you don't define a specific class when you create a `VirtualMachineDisks,` this default `StorageClass` is used. No initial `StorageClass` is configured and set as default. In the following section, you learn how to set or update this default StorageClass.

## Set or update the default StorageClass

Initially, Google Distributed Cloud with VM Runtime on GDC have no default `StorageClass` configured. To create a `VirtualMachineDisk` without specifying a `StorageClass`, you must first [create a `StorageClass`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/default-storage-class#create_storageclass) and then set it as default.

If you want to initially set or update the default `StorageClass` that VM Runtime on GDC uses when you create a `VirtualMachineDisk`, update the `VMRuntime` custom resource.

  1. Edit the `VMRuntime` custom resource:
         
         kubectl edit vmruntime
         

  2. Add or update the `spec.storage` section that specifies the default `StorageClass` to use:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VMRuntime
         metadata:
           name: vmruntime
         spec:
           enabled: true
           storage:
             defaultStorageClass: STORAGE_CLASS_NAME
         ...
         

Edit `STORAGE_CLASS_NAME` with the name of the default `StorageClass` you want to use. If you need to first create a `StorageClass`, see [Create a `StorageClass`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/default-storage-class#create_storageclass).

  3. Save and close the `VMRuntime` custom resource in your editor.

The `StorageClass` you specified is now used when you now create a virtual machine disk and don't specify a `StorageClass`. The following section shows you how to create a disk and use a specific StorageClass.

Existing `VirtualMachineDisk` resources are not updated to use the newly specified `StorageClass`.




## Use a specific StorageClass

If you don't want to use the default `StorageClass` when you create a `VirtualMachineDisk`, use the `storageClassName` field to specify a different `StorageClass`.

To use a specific, already-defined `StorageClass` when you create a `VirtualMachineDisk`, complete the following steps:

  1. Create a `VirtualMachineDisk` manifest, such as `my-disk.yaml`, in the editor of your choice:
         
         nano my-disk.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: DISK_NAME
         spec:
           size: 10Gi
           storageClassName: STORAGE_CLASS_NAME
         

Replace the following values:

     * `DISK_NAME`: the name for your disk.
     * `STORAGE_CLASS_NAME`: the `StorageClass` to use for your disk. This `StorageClass` must already exist. If you need to first create a `StorageClass`, see [Create a StorageClass](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/default-storage-class#create_storageclass).
  3. Save and close the disk manifest in your editor.

  4. Create the disk using `kubectl`:
         
         kubectl apply -f my-disk.yaml
         




## Configure storage profiles

Storage profiles provide extra configuration options associated with each `StorageClass`. These configuration options include which access mode and volume mode to use for `VirtualMachineDisks` that use the `StorageClass`.

Without a configured storage profile, disks default to the `ReadWriteOnce` access mode. This access mode isn't sufficient for production workloads, as features like live migration don't work. The default volume mode without a configured storage profile is `Filesystem`.

VM Runtime on GDC automatically generates one storage profile for each `StorageClass` in a cluster. The storage profile is the same name as the associated `StorageClass`. The following example output shows that the cluster has four storage classes and associated profiles:
    
    
      $ kubectl get storageprofiles
    
      NAME            AGE
      anthos-system   11d
      node-disk       11d
      standard        11d
      nfs             11d
    

To edit a storage profile and change the access mode or volume mode, complete the following steps:

  1. Edit the `StorageProfile` custom resource for editing:
         
         kubectl edit storageprofile STORAGE_PROFILE_NAME
         

Replace `STORAGE_PROFILE_NAME` with the `StorageProfile` you want to edit.

  2. Add a single entry to the `spec.claimPropertySets` list of the `StorageProfile`:
         
         apiVersion: cdi.kubevirt.io/v1beta1
         kind: StorageProfile
         metadata:
           name: nfs
         spec:
           claimPropertySets:
           - accessModes:
             - ACCESS_MODE
             volumeMode: VOLUME_MODE
         

The `accessMode` and `volumeMode` use the underlying Kubernetes components. The values you set depend on the storage driver you use. Replace the following values as appropriate for the storage you use:

     * `ACCESS_MODE`: the access mode that you want to use. If supported by the associated `StorageClass`, the preferred access mode is `ReadWriteMany`. 
       * Acceptable values include `ReadWriteOnce`, `ReadOnlyMany`, `ReadWriteMany`, and `ReadWriteOncePod`. If not specified, `ReadWriteOnce` is used based on the VM Runtime on GDC defaults. For more information, see [Access modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).
     * `VOLUME_MODE`: the volume mode that you want to use. 
       * Acceptable values include `Filesystem` and `Block`. If not specified, `Filesystem` is used based on the Kubernetes defaults. For more information, see [Volume modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#volume-mode).
**Note:** The access mode and volume mode must be supported by the underlying `StorageClass`.
  3. Save and close the `StorageProfile` custom resource in your editor.

The storage profile settings you defined are used when you now create any virtual disks. Existing `VirtualMachineDisk` resources are not updated to use the defined storage profile settings.




## What's next

  * [Create and manage disks in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks).
  * [Create and use credentials to import images from Cloud Storage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-storage-credentials).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
