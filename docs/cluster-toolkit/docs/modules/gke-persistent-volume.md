---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-persistent-volume/
title: Create a Google Kubernetes Engine persistent volume \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:18.131334+00:00
---

# Create a Google Kubernetes Engine persistent volume  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-persistent-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Google Kubernetes Engine persistent volume Stay organized with collections  Save and categorize content based on your preferences. 

Use the `gke-persistent-volume` module to create Kubernetes [`PersistentVolume` (PV) and `PersistentVolumeClaim` (PVC)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) resources.

This module connects Cluster Toolkit storage modules to the [`gke-job-template`](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-job-template).

This module supports the following storage backends:

  * [Filestore](https://docs.cloud.google.com/filestore/docs/overview)
  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction)
  * [Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview)



For the complete list of inputs and outputs, see the [`gke-persistent-volume` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/gke-persistent-volume/README.md#inputs) in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `gke-persistent-volume` module, see the [`examples/storage-gke.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/storage-gke.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `gke-persistent-volume` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **GKE**.
  * The `gke-persistent-volume` module does not create a continuous long-running workload or a full cluster. It defines Kubernetes [`PersistentVolume` (PV) and `PersistentVolumeClaim` (PVC)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) resources that connect pre-provisioned storage volumes to your GKE cluster.
  * The `gke-persistent-volume` module calls the Kubernetes API to create resources. You must authorize the deployment machine to connect to the Kubernetes API. To authorize the deployment machine, add the `master_authorized_networks` setting to your [`gke-cluster` module configuration](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-cluster). You must include the IP address of the deployment machine in this block. This configuration lets the deployment machine connect to the cluster.
  * Each `gke-persistent-volume` module defines a single file system. If you need multiple shared file systems, then you must include multiple instances of this module.



### Required roles

To get the permissions that you need to create GKE persistent volumes and storage backends, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * If using Filestore: [Cloud Filestore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`) 
  * If using Cloud Storage: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
  * If using Google Cloud Managed Lustre: [Managed Lustre Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use with Filestore

The following example creates a Filestore instance and uses the `gke-persistent-volume` module to expose the instance as shared storage (mounted at `/data`) to a GKE job.
    
    
      - id: gke_cluster
        source: modules/scheduler/gke-cluster
        use: [network1]
        settings:
          master_authorized_networks:
          - display_name: deployment-machine
            cidr_block: IP_ADDRESS/32
    
      - id: datafs
        source: modules/file-system/filestore
        use: [network1]
        settings:
          local_mount: /data
    
      - id: datafs-pv
        source: modules/file-system/gke-persistent-volume
        use: [datafs, gke_cluster]
    
      - id: job-template
        source: modules/compute/gke-job-template
        use: [datafs-pv, compute_pool, gke_cluster]
    
    

Replace `IP_ADDRESS` with the IP address of your deployment machine.

## Use with Cloud Storage

The following example creates a Cloud Storage bucket and uses the `gke-persistent-volume` module to expose the bucket to the job template.
    
    
      - id: gke_cluster
        source: modules/scheduler/gke-cluster
        use: [network1]
        settings:
          master_authorized_networks:
          - display_name: deployment-machine
            cidr_block: IP_ADDRESS/32
    
      - id: data-bucket
        source: modules/file-system/cloud-storage-bucket
        settings:
          local_mount: /data
    
      - id: datagcs-pv
        source: modules/file-system/gke-persistent-volume
        use: [data-bucket, gke_cluster]
    
      - id: job-template
        source: modules/compute/gke-job-template
        use: [datagcs-pv, compute_pool, gke_cluster]
    
    

## Use with Google Cloud Managed Lustre

The following example creates a Google Cloud Managed Lustre instance and uses the `gke-persistent-volume` module to expose the instance to the job template.
    
    
      - id: gke_cluster
        source: modules/scheduler/gke-cluster
        use: [network1]
        settings:
          master_authorized_networks:
          - display_name: deployment-machine
            cidr_block: IP_ADDRESS/32
    
      - id: data-managedlustre
        source: modules/file-system/managed-lustre
        settings:
          local_mount: /data
    
      - id: datalustre-pv
        source: modules/file-system/gke-persistent-volume
        use: [data-managedlustre, gke_cluster]
    
      - id: job-template
        source: modules/compute/gke-job-template
        use: [datalustre-pv, compute_pool, gke_cluster]
    
    

## What's next

  * To learn how to use these volumes in a job, see the [`gke-job-template` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-job-template).
  * For a complete list of input fields and output values, see the [`gke-persistent-volume` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/modules/file-system/gke-persistent-volume/README.md#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
