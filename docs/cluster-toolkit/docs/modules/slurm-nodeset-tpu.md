---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset-tpu/
title: Create a TPU nodeset for a Slurm partition \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:40.081708+00:00
---

# Create a TPU nodeset for a Slurm partition  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a TPU nodeset for a Slurm partition Stay organized with collections  Save and categorize content based on your preferences. 

Use the `schedmd-slurm-gcp-v6-nodeset-tpu` module to define a group of Tensor Processing Unit (TPU) nodes. This module creates the data structure that's required by the [`schedmd-slurm-gcp-v6-partition` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition) to build a partition that supports machine learning workloads. 

TPUs are Google's custom-developed Application-Specific Integrated Circuits (ASICs) designed to accelerate machine learning workloads.

For the complete list of inputs and outputs, see the [`schedmd-slurm-gcp-v6-nodeset-tpu` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/compute/schedmd-slurm-gcp-v6-nodeset-tpu/README.md#inputs) on GitHub.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. To view a working example of a blueprint configured for the `slurm-nodeset-tpu` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **Slurm**. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `slurm-nodeset-tpu` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page.



### Required roles

To get the permissions that you need to deploy the TPU nodeset, ask your administrator to grant you the following IAM roles on your project: 

  * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a TPU nodeset

To create a TPU nodeset, add the `schedmd-slurm-gcp-v6-nodeset-tpu` module to your blueprint. You must specify the node type and TensorFlow version.

The following example creates a TPU partition by using the `tpu_nodeset` module as input. It configures the nodeset with the following settings:

  * Connects to a network defined by a separate module.
  * Uses the `v2-8` node type.
  * Uses TensorFlow version `2.10.0`.
  * Enables preemptibility for the TPU VMs.
  * Disables the `preserve_tpu` setting. If this setting is disabled, then the system deletes suspended VMs.


    
    
    -   id: tpu_nodeset
      source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset-tpu
      use: [network]
      settings:
        node_type: v2-8
        tf_version: 2.10.0
        disable_public_ips: false
        preemptible: true
        preserve_tpu: false
    
    -   id: tpu_partition
      source: community/modules/compute/schedmd-slurm-gcp-v6-partition
      use: [tpu_nodeset]
      settings:
        partition_name: tpu
    

## Configure preemptibility

To reduce costs, you can configure your TPU nodes to be preemptible by enabling the `preemptible` setting.

Additionally, you can control the behavior of suspended VMs by using the `preserve_tpu` setting:

  * **`false`:** suspended VMs are deleted. This value is the default value for this setting.
  * **`true`:** suspended VMs are stopped but not deleted, preserving their state.


    
    
      settings:
        preemptible: true
        preserve_tpu: false
    

## What's next

  * To add this nodeset to a partition, see [Create a partition for a Slurm controller](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition).
  * For a complete list of inputs and outputs, see the [`slurm-nodeset-tpu` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/compute/schedmd-slurm-gcp-v6-nodeset-tpu/README.md#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
