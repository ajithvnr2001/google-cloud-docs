---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/filestore-instance/
title: Create a Filestore instance \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:24.790658+00:00
---

# Create a Filestore instance  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/filestore-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Filestore instance Stay organized with collections  Save and categorize content based on your preferences. 

Use the `filestore` module to create a [Filestore instance](https://docs.cloud.google.com/filestore/docs/overview).

This module creates high-performance network file systems that you can mount to one or more Compute Engine instances.

You can mount this storage to other modules, such as the [`slurm-partition` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition) or the [`gke-node-pool` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-node-pool), by using the `use` keyword. This keyword method handles the client installation and mounting processes for you.

For the complete list of inputs and outputs for this module, see the [`filestore` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/modules/file-system/filestore/README.md#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `filestore` module, see the [`examples/hpc-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `filestore` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select storage type** menu and then select **Filestore**.
  * Verify that your project has enough quota for Cloud Filestore in the region where you want to provision the storage. Because high scale SSD starts with no quota, you must request a [quota increase](https://docs.cloud.google.com/filestore/docs/service-tiers#quota) before you can use it.



### Required roles

To get the permissions that you need to create and mount Filestore instances, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Filestore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Filestore tiers

Filestore supports the following [tiers of service](https://docs.cloud.google.com/filestore/docs/service-tiers). In Cluster Toolkit, you can specify these tiers of service, by using the following values:

  * Basic HDD: `BASIC_HDD`
  * Basic SSD: `BASIC_SSD`
  * High scale (legacy): `HIGH_SCALE_SSD`. For more information, see [Legacy Filestore service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers-legacy).
  * Zonal: `ZONAL`
  * Enterprise: `ENTERPRISE`
  * Regional: `REGIONAL`

**Warning:** You must review the minimum storage requirements for each tier. The Terraform module can only enforce the minimum value of the `size_gb` parameter for the lowest tier of service. If you supply a value that is too low, Cluster Toolkit fails to create a Filestore instance when you run the `terraform apply` command.

## Request Filestore quota

Your project must have the required quota for Filestore in the region you provision the storage. There are separate quota limits for HDD and SSD storage. All projects begin with zero available quota for the high scale SSD tier. To use this tier, [make a request](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases) and wait for it to be approved. For more information, see [Quotas and limits](https://docs.cloud.google.com/filestore/docs/limits).

## Create a Filestore instance

To create a Filestore instance, add the `filestore` module to your blueprint and specify the `filestore_tier` setting. This section provides examples for creating instances for the basic SSD and high scale SSD tiers.

### Create a Filestore instance for the basic SSD tier

The following example creates a standard instance that has the following settings:

  * Uses the `BASIC_SSD` tier, which is the default value.
  * Requests 2.5 TiB (2,560 GiB) capacity, which is the default value.
  * Uses a value of `homefs` for the module ID.
  * Mounts the Filestore instance to the home file system connected to the network defined in the `network1` module.


    
    
      - id: homefs
        source: modules/file-system/filestore
        use: [network1]
        settings:
          local_mount: /home
    

### Create a Filestore instance for the high scale SSD tier

**Note:** The high scale SSD tier is a [legacy tier](https://docs.cloud.google.com/filestore/docs/service-tiers-legacy).

The following example creates a high scale SSD instance that has the following settings:

  * Uses the `HIGH_SCALE_SSD` tier.
  * Requests 10 TiB (10,240 GiB) capacity.
  * Uses a value of `highscale` for the module ID.
  * Mounts the Filestore instance to the `/projects` directory connected to the network defined in the `network1` module.


    
    
      - id: highscale
        source: modules/file-system/filestore
        use: [network1]
        settings:
          filestore_tier: HIGH_SCALE_SSD
          size_gb: 10240
          local_mount: /projects
    

### Enable deletion protection

You can enable Filestore deletion protection in Cluster Toolkit. Deletion protection prevents unintentional deletion of an entire Filestore instance. However, deletion protection doesn't stop the deletion of files within the Filestore instance when that instance is mounted by a compute instance. For more information, see [Prevent deletion of an instance](https://docs.cloud.google.com/filestore/docs/deletion-protection).

To prevent the unintentional deletion of an entire Filestore instance, enable deletion protection in the `settings` block:
    
    
      - id: homefs
        source: modules/file-system/filestore
        use: [network1]
        settings:
          deletion_protection:
            enabled: true
            reason: Avoid data loss
          local_mount: /home
    

## Mount the instance

When you apply the `filestore` module to a compatible module, such as Slurm, by using the `use` keyword, the module handles client installation and mounting automatically.

If you need to mount the instance manually or on a custom module, then you can use the output runners of the `filestore` module with the `startup-script` module:
    
    
      - id: filestore
        source: modules/file-system/filestore
        use: [network1]
        settings: {local_mount: /scratch}
    
      - id: mount-at-startup
        source: modules/scripts/startup-script
        settings:
          runners:
          - $(filestore.install_nfs_client_runner)
          - $(filestore.mount_runner)
    
    

## Configure Filestore protocols and mount options

When mounting a Filestore instance, you can customize the underlying protocols and mount options to optimize performance for your workloads.

### Mount options

Cluster Toolkit uses [default mount options](https://linux.die.net/man/8/mount) for all service tiers. To improve performance, we recommend that you use the [specific mount option](https://docs.cloud.google.com/filestore/docs/mounting-fileshares) that applies to your service tier.

To override the default options, use the `mount_options` setting in the `filestore` module.
    
    
    - id: homefs
      source: modules/file-system/filestore
      use: [network1]
      settings:
        local_mount: /homefs
        mount_options: defaults,hard,timeo=600,retrans=3,_netdev
    
    

### Protocols

Filestore supports the `NFS_V3` (default) and `NFS_V4_1` NFS protocols. Protocol support depends on your selected tier:

  * **`NFS_V3`** : Supported on all tiers: `BASIC_HDD`, `BASIC_SSD`, `HIGH_SCALE_SSD`, `ZONAL`, and `ENTERPRISE`.
  * **`NFS_V4_1`** : Supported only on `HIGH_SCALE_SSD`, `ZONAL`, `REGIONAL`, and `ENTERPRISE` tiers.



To specify the protocol, use the `protocol` setting. By default, the module uses `NFS_V3` for compatibility.

The following example creates a zonal instance that uses the `NFS_V4_1` protocol.
    
    
    - id: homefs
      source: modules/file-system/filestore
      use: [network1]
      settings:
        local_mount: /homefs
        protocol: NFS_V4_1
        filestore_tier: ZONAL
    
    

## What's next

  * For a complete list of all available input fields and output values, see the [`filestore` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/filestore#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
