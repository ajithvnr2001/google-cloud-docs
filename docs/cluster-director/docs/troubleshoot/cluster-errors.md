---
url: https://docs.cloud.google.com/cluster-director/docs/troubleshoot/cluster-errors/
title: Troubleshoot errors in Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:09.610283+00:00
---

# Troubleshoot errors in Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/troubleshoot/cluster-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Troubleshoot errors in Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to resolve common issues and errors that you might encounter when creating or modifying a cluster in Cluster Director. If your error isn't listed in this document, then see the following troubleshooting documentation for Compute Engine resources, Cloud Storage resources, or Google Cloud networking services:

  * [Troubleshoot creating, updating, and deleting Compute Engine instances](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation)

  * [Troubleshoot Compute Engine reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)

  * [Troubleshoot Filestore instance mounting issues](https://docs.cloud.google.com/filestore/docs/mount-issues)

  * [Troubleshoot Managed Lustre instances](https://docs.cloud.google.com/managed-lustre/docs/troubleshooting)

  * [Troubleshoot Cloud Storage bucket issues](https://docs.cloud.google.com/storage/docs/troubleshooting)

  * [Troubleshoot common networking issues](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-networking)

  * [Troubleshoot VPC policy and access problems](https://docs.cloud.google.com/vpc/docs/troubleshooting-policy-and-access-problems)




## Resolve general cluster errors

This section describes common errors related to resource capacity, quotas, or location during cluster creation or modification.

### Resolve duplicate resource name errors

This error occurs when Cluster Director attempts to create a resource with a name that already exists in your project.

**Error messages** :
    
    
    Resource RESOURCE_NAME already exists
    

**Resolution** : Cluster Director names resources with the cluster name as a prefix. For example, if you name a cluster `cluster123`, then the names of the resources that are associated with that cluster start with `cluster123-`. To resolve a naming conflict, complete the following steps:

  1. Identify the resource from the error message or the [audit logs](https://docs.cloud.google.com/cluster-director/docs/monitor/view-audit-logs).

  2. Check the timestamp for when the resource was created, and then do one of the following:

     * If the resource was created during your cluster creation attempt, then delete the resource and try again to create the cluster. If the error persists, then use a different name for your cluster.

     * If the resource existed before you attempted to create your cluster, then do one of the following:

       * If you no longer need the existing resource, then delete the resource and retry creating the cluster.

       * If you must keep the existing resource, then use a different name for your cluster.




### Resolve insufficient quota errors

This error occurs when you attempt to create virtual machine (VM) instances by using the Flex-start, Spot, or On-demand consumption options, but your project lacks sufficient quota for the requested resources.

**Error messages** :
    
    
    RESOURCE_NAME creation failed: Quota QUOTA_NAME exceeded. Limit QUOTA_LIMIT in region REGION
    
    
    
    RESOURCE_NAME creation failed: Quota QUOTA_NAME exceeded. Limit QUOTA_LIMIT in zone ZONE
    
    
    
    Resource exhausted (HTTP 429): QUOTA_EXCEEDED
    

**Resolution** : Check that your project has sufficient quota for the resources that you want to request, and then retry your cluster creation or modification request. For more information about managing quota, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

### Resolve region or zone availability errors

This error occurs when your requested compute resource isn't available in the specified region or zone.

**Error messages** :
    
    
    notFound
    
    
    
    does not exist in zone
    

**Resolution** : Select a region or zone that supports your requested compute resources. To review available regions and zones in Compute Engine, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

### Resolve resource unavailability errors

This error occurs when a specified compute resource isn't available in the region or zone where you are attempting to create your cluster.

**Error messages** :
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED
    
    
    
    The zone 'projects/PROJECT_ID/zones/ZONE' does not have enough resources available to fulfill the request. Try a different zone, or try again later.
    
    
    
    A MACHINE_TYPE VM instance with RESOURCE_ATTACHMENT is currently unavailable in the ZONE zone.
    

**Resolution** : All compute resources that you specify when creating a cluster must be available. To resolve this issue, do the following:

  * If you want to use the Flex-start, Spot, or On-demand consumption option, then try one of the following:

    * Create the cluster in a different region or zone.

    * Create the cluster at a later time when resources become available.

    * Create the cluster by using different compute or storage configuration.

  * Otherwise, for a higher guarantee of capacity, reserve capacity by using one of the following methods. Then, if your reservation request is approved, try creating your cluster again at the request's start time.

    * [Use future reservations for capacity blocks](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option#future-reservations)

    * [Use future reservations in calendar mode](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option#calendar-mode)




## Resolve A4X resource pool exhaustion

This error occurs when your cluster attempts to use more A4X subblocks than you have reserved, which happens when the number of VMs in your nodeset isn't a multiple of 18. Because Compute Engine provisions A4X capacity in indivisible sub-blocks to create 18 VMs, any remaining capacity in a sub-block can't be used by other nodesets in your cluster.

**Error messages** :
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED
    
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS
    

**Resolution** : Modify your cluster so that the total number of VMs for each nodeset with A4X VMs is a multiple of 18. This total is the sum of the static node count and the dynamic node count. For instructions, see [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster).

## Resolve errors for incompatible machine types

This error occurs when you specify a C4A machine type for a login node in a cluster with compute nodes that aren't Arm-based. It also occurs when you specify an unsupported `-lssd` or `-metal` variant of a C4A machine type for a login node.

**Error messages** :
    
    
    INCOMPATIBLE_LOGIN_NODE_MACHINE_TYPE
    
    
    
    The machine type "LOGIN_NODE_MACHINE_TYPE" for the Slurm login node is not supported with compute resource "COMPUTE_RESOURCE_NAME" of machine type "COMPUTE_MACHINE_TYPE". C4A login nodes are only supported with ARM-based compute nodes (such as A4X).
    
    
    
    The machine type "LOGIN_NODE_MACHINE_TYPE" is not supported for the Slurm login node. The lssd and metal variants of C4A machine types are not supported for the login node.
    

**Resolution** : Select a machine type for your login nodes that matches the architecture of your compute nodes:

  * If your compute nodes use the A4X Max or A4X machine series, then specify a [C4A machine type](https://docs.cloud.google.com/cluster-director/docs/compute#c4a-series).

  * If your compute nodes use the A4, A3 Ultra, A3 Mega, or N2 machine series, then specify an [N2 machine type](https://docs.cloud.google.com/cluster-director/docs/compute#n2-series).




## Resolve Slurm controller version errors

This section describes common errors related to when you create or modify a cluster and attempt to specify the Slurm version for the controller node. For more information about Slurm controller versions, see [Slurm controller versions in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/slurm-controller-versions).

### Resolve incompatible OS image errors

This error occurs when you create a nodeset with an OS image that requires a newer Slurm version than the version that the controller node runs.

**Error message** :
    
    
    The cluster is running Slurm CONTROLLER_VERSION. Please select a compatible compute image (Slurm CONTROLLER_VERSION or older).
    

**Resolution** : Compute nodes can't run a newer Slurm version than the controller node. To resolve this error, do one of the following:

  * If your workload requires the newer OS image, then create a new cluster with the required Slurm controller version. For instructions, see [Create a custom cluster from scratch](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster).

  * If you want to keep the current controller version, then modify the nodeset to use an OS image that supports the controller version of your cluster. For instructions, see [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster).




### Resolve unsupported version errors

This error occurs when you specify an invalid version format or an unsupported Slurm controller version when you create a cluster.

**Error messages** :
    
    
    Unsupported controller version.
    
    
    
    Controller version must be in the format 'ab.cd' (e.g., '25.05'), found 'VERSION'.
    

**Resolution** : Specify a supported Slurm controller version in `ab.cd` format; specifically, specify `26.05` or `25.05`.

### Resolve errors when updating the controller version

This error occurs when you modify the Slurm controller version of an existing cluster.

**Error message** :
    
    
    Updating the Slurm controller version is not currently supported.
    

**Resolution** : The Slurm controller version is immutable after you create the cluster. If your workload requires a different Slurm controller version, then create a new cluster with the required version.

## Resolve storage pool errors

This section describes errors that you might encounter when you use [Hyperdisk pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools) or [Hyperdisk Exapools](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools) for node boot disks in your cluster.

### Storage pool zone mismatch

This error occurs when the storage pool that you specify resides in a different zone than the zone of the compute node or login node that uses it.

**Error messages** :
    
    
    The storage pool "STORAGE_POOL" is located in zone "STORAGE_ZONE", but the boot disk is located in zone "COMPUTE_ZONE". The storage pool must be located in the same zone as the boot disk.
    

**Resolution** : Verify that your storage pool and your compute resources reside in the same zone. If your compute resources reside in a different zone, then specify a storage pool in that zone or recreate the storage pool in the correct zone.

### Boot disk type or storage pool type mismatch

This error occurs when you specify a storage pool for a boot disk, but you attempt to specify a boot disk type other than Hyperdisk Balanced, or specify an unsupported storage pool type.

**Error messages** :
    
    
    Boot disk type must be hyperdisk-balanced when a storage pool is specified.
    

**Resolution** : Verify that the boot disk is Hyperdisk Balanced, or that the storage pool is a Hyperdisk storage pool or a Hyperdisk Exapool.

### Storage pool capacity or IOPS exhaustion

This error occurs when the boot disks in your cluster nodesets exceed the provisioned capacity, provisioned input/output operations per second (IOPS), or maximum overprovisioning ratio of the storage pool. When this error occurs, compute instance creation fails.

**Error messages** :
    
    
    HttpError 400: Storage pool provisioned IOPS limit exceeded.
    
    
    
    UNSUPPORTED_OPERATION: Cannot allocate disk from storage pool.
    

**Resolution** : To resolve this error, complete the following steps:

  1. Verify the provisioned capacity and IOPS for your storage pool. For instructions, see [Analyze the provisioned IOPS and throughput for Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk).

  2. Verify that the combined boot disk requirements (minimum 40 GB per node) for all static and dynamic nodes stay within your storage pool limits.

  3. If necessary, then increase the provisioned capacity or IOPS for your storage pool. You can update capacity once every 12 hours. For instructions, see [Modify a storage pool](https://docs.cloud.google.com/compute/docs/disks/manage-storage-pools#modify-sp).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
