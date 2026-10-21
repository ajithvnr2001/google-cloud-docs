---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset-dynamic/
title: Create a dynamic nodeset for a Slurm partition \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:40.551291+00:00
---

# Create a dynamic nodeset for a Slurm partition  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset-dynamic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a dynamic nodeset for a Slurm partition Stay organized with collections  Save and categorize content based on your preferences. 

Use the `schedmd-slurm-gcp-v6-nodeset-dynamic` module to create an instance template and a nodeset data structure for dynamic compute nodes. This module works in conjunction with the [`schedmd-slurm-gcp-v6-partition` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition) to let your Slurm cluster provision resources on demand. 

For the complete list of inputs and outputs, see the [`slurm-nodeset-dynamic` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/compute/schedmd-slurm-gcp-v6-nodeset-dynamic/README.md#inputs) in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `slurm-nodeset-dynamic` module, see the [`examples/hpc-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `slurm-nodeset-dynamic` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **Slurm**.



### Required roles

To get the permissions that you need to deploy the dynamic nodeset, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a dynamic nodeset

To create a dynamic nodeset, add the `schedmd-slurm-gcp-v6-nodeset-dynamic` module to your blueprint. You must specify the machine type and connect it to a partition and controller.

The following example creates a dynamic nodeset and uses it to configure a partition. It also defines a managed instance group (MIG) that uses the instance template created by the dynamic nodeset module:
    
    
      - id: dynamic_ns
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset-dynamic
        use: [network, controller]
        settings:
          machine_type: n2-standard-2
    
      - id: dynamic_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use: [dynamic_ns]
        settings:
          partition_name: mp
          is_default: true
    
      - id: controller
        source: community/modules/scheduler/schedmd-slurm-gcp-v6-controller
        use: [network, dynamic_partition]
    
      - id: mig
        source: community/modules/compute/mig
        settings:
          versions:
          - name: v1
            instance_template: $(dynamic_ns.instance_template_self_link)
          base_instance_name: $(dynamic_ns.node_name_prefix)
    

## Configure custom images

For information about how to create valid custom images for the node group Compute Engine instances or for custom instance templates, see the documentation on [Slurm on Google Cloud custom images](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/vm-images.md#slurm-on-gcp-custom-images) on GitHub.

## Configure GPU support

To learn more about GPU support in `slurm-nodeset-dynamic` and other Cluster Toolkit modules, see the documentation on [GPU support](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gpu-support.md) on GitHub.

## What's next

  * To add this nodeset to a partition, see [Create a partition for a Slurm controller](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition).
  * For a complete list of all available input fields and output values, see the [`schedmd-slurm-gcp-v6-nodeset-dynamic` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/compute/schedmd-slurm-gcp-v6-nodeset-dynamic/README.md#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
