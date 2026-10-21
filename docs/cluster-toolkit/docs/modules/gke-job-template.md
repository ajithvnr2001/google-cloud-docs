---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-job-template/
title: Create a Google Kubernetes job template \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:39.955704+00:00
---

# Create a Google Kubernetes job template  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-job-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Google Kubernetes job template Stay organized with collections  Save and categorize content based on your preferences. 

The `gke-job-template` module simplifies the deployment and management of Kubernetes job templates on your Google Kubernetes Engine (GKE) clusters. This module helps you efficiently define and submit batch workloads, such as those common in high performance computing (HPC) and artificial intelligence (AI) and machine learning (ML) environments. 

The module provides a flexible framework for creating job specifications, which you can submit directly or customize further. It integrates with [`gke-node-pool`](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-node-pool) modules to configure jobs to run on specific GKE node pools.

In this document, you learn how to use the `gke-job-template` module. For a complete list of inputs and outputs, see the [`gke-job-template` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/compute/gke-job-template/README.md#inputs) in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `gke-job-template` module, see the [`examples/hpc-gke.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-gke.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `gke-job-template` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select software or resource** menu and then select **Google Kubernetes Engine job template**.
  * In your blueprint, you must have added the [`gke-node-pool` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-node-pool).



### Required roles

To get the permissions that you need to create Google Kubernetes Engine job templates, ask your administrator to grant you the [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a job template

To create a GKE job template, add the `gke-job-template` module to your blueprint. You must specify which node pools the job can use by referencing them in the `use` field.

The following example creates a job template that uses the `gke-node-pool` module. The example also requests the `instructions` output, which provides the `kubectl` commands needed to submit the job.
    
    
      - id: job-template
        source: modules/compute/gke-job-template
        use: [compute_pool]
        settings:
          node_count: 3
        outputs: [instructions]
    

To see a detailed example of how to deploy GKE for high performance computing workloads, see the [`examples/hpc-gke.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-gke.yaml) file in the Cluster Toolkit repository on GitHub.

## Configure storage options

The `gke-job-template` module supports the following storage configuration options:

  * **Filestore:** A shared file system mounted between pods and nodes.
  * **Ephemeral storage:** Pod-level storage options, including the following:

    * **Memory-backed`emptyDir`:** uses the node's RAM (`tmpfs`) to provide high-speed, low-latency storage for temporary data that does not persist across pod restarts.
    * **Local SSD-backed`emptyDir`:** uses physically attached NVMe SSDs to provide high-performance, high-throughput ephemeral storage suitable for demanding scratch space requirements.
    * **SSD persistent disk-backed ephemeral volume:** uses SSD-backed persistent disks (PD-SSD) to provide reliable ephemeral storage with consistent performance for disk-intensive temporary tasks.
    * **Balanced persistent disk-backed ephemeral volume:** uses balanced persistent disks (PD-Balanced) to provide a cost-effective storage option that balances performance and capacity for general-purpose ephemeral needs.



For examples of how to use Filestore and ephemeral storage with this module, see the [`examples/storage-gke.yaml` blueprint](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/storage-gke.yaml) in the GitHub repository.

## Configure resource requests

When you reference one or more `gke-node-pool` modules in the `use` field, the module automatically populates the requested resources to achieve one pod per node, while leaving additional space for required system pods.

To override this behavior and specify a custom CPU requirement, use the `requested_cpu_per_pod` setting.

## What's next

  * To learn how to deploy this blueprint, see [Deploy a cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/deploy-cluster-overview).
  * For a complete list of all available input fields and output values, see the [`gke-job-template` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/compute/gke-job-template/README.md#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
