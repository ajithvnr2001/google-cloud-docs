---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-storage/
title: Create a Google Kubernetes Engine storage class \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:17.979063+00:00
---

# Create a Google Kubernetes Engine storage class  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Google Kubernetes Engine storage class Stay organized with collections  Save and categorize content based on your preferences. 

You can use the `gke-storage` module to create a Kubernetes `StorageClass` resource. This resource helps you dynamically provision Google Cloud storage resources, such as [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced), for your GKE workloads within Cluster Toolkit blueprints. By dynamically provisioning storage, you help ensure your applications have the necessary storage without manual intervention, simplifying infrastructure management for high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) deployments.

For the complete list of inputs and outputs for this module, see the [`gke-storage` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/gke-storage#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `gke-storage` module, see the [`examples/gke-managed-hyperdisk.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-managed-hyperdisk.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `gke-storage` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **GKE**.



### Required roles

To get the permissions that you need to create GKE storage classes and provision storage, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Add storage to blueprint

To dynamically provision storage, add the `gke-storage` module to your blueprint.

The following example uses the `gke-storage` module to create a Google Cloud Managed Lustre `StorageClass` resource and a Kubernetes `PersistentVolumeClaim` resource. The example then uses the `gke-job-template` module to dynamically provision the storage volume by using the PVC.
    
    
      - id: gke_cluster
        source: modules/scheduler/gke-cluster
        use: [network]
        settings:
          enable_managed_lustre_csi: true
    
      - id: private_service_access
        source: modules/network/private-service-access
        use: [network]
        settings:
          prefix_length: 24
    
      - id: gke_storage
        source: modules/file-system/gke-storage
        use: [gke_cluster, private_service_access]
        settings:
          storage_type: ManagedLustre
          access_mode: ReadWriteMany
          sc_volume_binding_mode: Immediate
          sc_reclaim_policy: Delete
          sc_topology_zones: [$(vars.zone)]
          pvc_count: 2
          capacity_gb: 12000
    
      - id: job_template
        source: modules/compute/gke-job-template
        use: [gke_storage, compute_pool]
    

## Configure authorized networks

The `gke-storage` module calls the Kubernetes API to create Kubernetes entities. Therefore, you must authorize the deployment machine to connect to the Kubernetes API.

To authorize the deployment machine, add the `master_authorized_networks` setting to your `gke-cluster` module configuration. You must include the IP address of the deployment machine in this block. This configuration lets the deployment machine connect to the cluster.

## What's next

  * For the complete list of inputs and outputs for this module, see the [`gke-storage` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/modules/file-system/gke-storage/README.md#inputs) page in the Cluster Toolkit GitHub repository.
  * For a complete list of supported modules, see the [compatibility matrix](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/network_storage.md#compatibility-matrix) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
