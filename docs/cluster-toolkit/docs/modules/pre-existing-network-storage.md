---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-network-storage/
title: Use pre-existing network storage \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:17.318520+00:00
---

# Use pre-existing network storage  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-network-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Use pre-existing network storage Stay organized with collections  Save and categorize content based on your preferences. 

Use the `pre-existing-network-storage` module to define and mount file systems that already exist outside of your current deployment group. This module connects your Compute Engine instances to storage that was created previously or is managed independently.

This module supports the following file system types:

  * [NFS](https://en.wikipedia.org/wiki/Network_File_System)
  * [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview)
  * [Lustre](https://www.lustre.org/)
  * [Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview)



For a complete list of inputs and outputs, see the [`pre-existing-network-storage` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/pre-existing-network-storage/README.md#inputs) in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `pre-existing-network-storage` module, see the [`examples/machine-learning/a4x-maxgpu-4g-metal/a4xmax-bm-slurm-blueprint.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a4x-maxgpu-4g-metal/a4xmax-bm-slurm-blueprint.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page.
  * The storage system must already be provisioned and accessible.
  * You must know the `server_ip` (or equivalent identifier such as a host name) and the `remote_mount` path (export or bucket name) before deployment.



### Required roles

To get the permissions that you need to mount pre-existing network storage, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * If using Cloud Storage: Storage Object Viewer (`roles/storage.objectViewer`) - the source bucket 
  * If using Google Cloud Managed Lustre: Managed Lustre Viewer (`roles/lustre.viewer`) - the Managed Lustre instance 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Mount an NFS share

To mount a standard NFS share, provide the server IP address and the remote export path.
    
    
    - id: homefs
      source: modules/file-system/pre-existing-network-storage
      settings:
        server_ip: SERVER_IP
        remote_mount: REMOTE_MOUNT
        local_mount: /home
        fs_type: nfs
    
    

Replace the following:

  * `SERVER_IP`: the IP address of your NFS server, such as `10.1.2.3`.
  * `REMOTE_MOUNT`: the exported path or directory on the NFS server, such as `nfsshare`.



## Mount a Cloud Storage bucket

To mount a Cloud Storage bucket, set the `fs_type` field to a value of `gcsfuse`. The `remote_mount` setting must be the bucket name, without the `gs://` string.

We recommend that you use the `implicit_dirs` mount option to treat object paths as directories, which is useful for files that are created by other sources.
    
    
    - id: data-bucket
      source: modules/file-system/pre-existing-network-storage
      settings:
        remote_mount: my-bucket-name
        local_mount: /data
        fs_type: gcsfuse
        mount_options: defaults,_netdev,implicit_dirs
    
    

## Mount a Lustre file system

You can mount both generic self-managed Lustre and Google Managed Lustre instances.

### Self-managed Lustre

For self-managed Lustre, provide the Metadata Server Network ID (MGS NID) in the `server_ip` field, including the `@tcp` suffix.
    
    
    - id: lustrefs
      source: modules/file-system/pre-existing-network-storage
      settings:
        fs_type: lustre
        server_ip: 192.168.227.11@tcp
        local_mount: /scratch
        remote_mount: /exacloud
    
    

### Managed Lustre configuration

For Managed Lustre, set the `fs_type` field to a value of `managed_lustre`. Supported operating systems include Rocky Linux 9 (the default OS image in Cluster Toolkit), Rocky Linux 8, and Ubuntu 22.04.
    
    
    - id: lustrefs
      source: modules/file-system/pre-existing-network-storage
      settings:
        fs_type: managed_lustre
        server_ip: 192.168.227.11@tcp
        local_mount: /scratch
        remote_mount: /mg_lustre
    
    

## Mount the storage

The Cluster Toolkit offers two methods for mounting network storage: automatic mounting with module relationships or manual mounting with output runners.

### Automatic mounting

When you connect the `pre-existing-network-storage` module to a compatible compute module (such as a Slurm partition or compute instance group) by using the `use` keyword, Cluster Toolkit automatically handles client installation and mounting.

For a complete list of supported modules, see the [compatibility matrix](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/network_storage.md#compatibility-matrix) section on GitHub.

### Manual mounting

If you need to mount the storage manually, such as in a custom startup script, then you can use the module's `client_install_runner` and `mount_runner` outputs.

The module provides these runners for the following `fs_type` values:

  * `nfs`: Mounts standard [Network File System (NFS)](https://en.wikipedia.org/wiki/Network_File_System) shares.
  * `lustre`: Mounts self-managed [Lustre](https://www.lustre.org/) file systems.
  * `managed_lustre`: Mounts [Managed Service for Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) instances.
  * `gcsfuse`: Mounts Cloud Storage buckets by using [Cloud Storage FUSE](https://cloud.google.com/storage/docs/gcs-fuse).

**Warning:** The `mount_runner` output executes the `scripts/mount.sh` script. This script updates the `/etc/fstab` file and mounts the network storage. The script fails if the path specified in `local_mount` is already defined in `/etc/fstab`.

## What's next

  * For a complete list of input fields and output values, see the [`pre-existing-network-storage` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/pre-existing-network-storage/README.md#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
