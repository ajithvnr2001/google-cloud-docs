---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition/
title: Create a partition for a Slurm controller \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:13.093496+00:00
---

# Create a partition for a Slurm controller  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a partition for a Slurm controller Stay organized with collections  Save and categorize content based on your preferences. 

Use this module to create a compute partition to use as input when you define the [`slurm-controller` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-controller). A compute partition defines a logical group of compute nodes for your Slurm cluster. This module works alongside the [`nodeset` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset) to group resources together in a single partition.

This module lets you configure partition-level settings such as job exclusivity, power management, timeouts, and default status.

For the complete list of inputs and outputs, see the [`schedmd-slurm-gcp-v6-partition` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/compute/schedmd-slurm-gcp-v6-partition/README.md#inputs) in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `slurm-partition` module, see the [`examples/hpc-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `slurm-partition` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **Slurm**.
  * In your blueprint, you must have defined at least one [`slurm-nodeset` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset) to include in the partition.



### Required roles

To get the permissions that you need to deploy the partition, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a compute partition

To create a compute partition, add the `slurm-partition` module to your blueprint and specify the `nodeset` modules that the partition contains.

The following example creates a partition module with the following configuration:

  * Adds two nodesets by using the `use` field:

    * The first nodeset uses the `c2-standard-30` machine type.
    * The second nodeset uses the `c2-standard-60` machine type.
    * Both nodesets specify a maximum of 200 dynamic nodes.
  * Sets the partition name to `compute`.

  * Connects to the `network` module by using the `use` field.

  * Mounts `homefs` by using the `use` field, which connects the partition to the shared file system module that hosts user home directories.



    
    
    - id: nodeset_1
      source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
      use: [network]
      settings:
        name: c30
        node_count_dynamic_max: 200
        machine_type: c2-standard-30
    
    - id: nodeset_2
      source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
      use: [network]
      settings:
        name: c60
        node_count_dynamic_max: 200
        machine_type: c2-standard-60
    
    - id: compute_partition
      source: community/modules/compute/schedmd-slurm-gcp-v6-partition
      use:
      - homefs
      - nodeset_1
      - nodeset_2
      settings:
        partition_name: compute
    

## Set the default partition

You can set a specific partition as the default for jobs that don't explicitly request one. To do this, set the `is_default` setting to `true`.
    
    
      settings:
        partition_name: compute
        is_default: true
    

## Configure job exclusivity

By default, the `slurm-partition` module configures nodes to execute a single job at a time by using the `exclusive: true` setting. When a job completes, the node is automatically deleted to ensure a clean environment for the next job.

To let multiple jobs to share a node, set the `exclusive` setting to `false`:
    
    
      settings:
        partition_name: shared-compute
        exclusive: false
    

## Configure node power management

Slurm on Google Cloud automatically suspends idle nodes to save costs. You can configure this behavior by using the following input settings:

  * `suspend_time`: controls how many seconds a node remains idle before it turns off. The default is 300 seconds (5 minutes). Set this to `-1` to prevent nodes from suspending.
  * `suspend_timeout`: controls the maximum time allowed (in seconds) between when a request to suspend a node is issued and when the node fully shuts down.
  * `resume_timeout`: controls the maximum time allowed (in seconds) between when a request to start a node is issued and when the node is ready for use.


    
    
      settings:
        partition_name: compute
        suspend_time: 600 # Wait 10 minutes before scaling down
        suspend_timeout: 120
        resume_timeout: 300
    

**Note:** If the `exclusive` setting is set to `true` (the default setting), nodes are deleted immediately after a job finishes, ignoring the `suspend_time` setting.

## What's next

  * To learn how to define the nodesets used in this partition, see [Create a nodeset for a Slurm partition](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset).
  * To configure the controller that manages this partition, see [Create a Slurm controller node](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-controller).
  * For a complete list of all available input fields and output values, see the [`schedmd-slurm-gcp-v6-partition` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/compute/schedmd-slurm-gcp-v6-partition/README.md#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
