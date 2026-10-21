---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-login-node/
title: Create a Slurm login node \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:41.030531+00:00
---

# Create a Slurm login node  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-login-node/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Slurm login node Stay organized with collections  Save and categorize content based on your preferences. 

The `schedmd-slurm-gcp-v6-login` module lets you create a login node for a Slurm cluster. By using this module, you can provide a more secure entry point so that users can do the following:

  * Interact with the cluster
  * Submit jobs
  * Manage workloads



This module operates alongside the [`schedmd-slurm-gcp-v6-controller` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-controller) to establish a complete Slurm environment.

For the complete list of inputs and outputs for this module, see the [`schedmd-slurm-gcp-v6-login` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/scheduler/schedmd-slurm-gcp-v6-login#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for Slurm, see the [`examples/hpc-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support Slurm, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **Slurm**.
  * The `schedmd-slurm-gcp-v6-login` module does not create a full active cluster. Instead, it provisions a Compute Engine instance that functions as a login node for interacting with the cluster and managing workloads.



### Required roles

To get the permissions that you need to deploy the Slurm login node, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Slurm login node

The following example demonstrates how to configure a Slurm login node that connects to a specific subnetwork and associates with a Slurm controller. The example in this section uses the following configuration:

  * Connects to the primary subnetwork of the `network` module.
  * Associates with the [`slurm_controller` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-controller) to establish the controller relationship.
  * Provisions a compute instance that uses the `n2-standard-4` machine type.


    
    
    - id: slurm_login
      source: community/modules/scheduler/schedmd-slurm-gcp-v6-login
      use:
      - network
      settings:
        group_name: login
        machine_type: n2-standard-4
    
    - id: slurm_controller
      source: community/modules/scheduler/schedmd-slurm-gcp-v6-controller
      use:
      - network
      - slurm_login
    

## What's next

  * For the complete list of inputs and outputs for this module, see the [`schedmd-slurm-gcp-v6-login` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/scheduler/schedmd-slurm-gcp-v6-login#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
