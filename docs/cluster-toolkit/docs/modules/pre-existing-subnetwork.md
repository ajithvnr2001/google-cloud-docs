---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-subnetwork/
title: Use a pre-existing subnetwork \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:17.177767+00:00
---

# Use a pre-existing subnetwork  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-subnetwork/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Use a pre-existing subnetwork Stay organized with collections  Save and categorize content based on your preferences. 

Use the `pre-existing-subnetwork` module to discover an existing subnetwork in Google Cloud and retrieve the subnetwork attributes.

This module lets you integrate your pre-provisioned network infrastructure with new Cluster Toolkit deployments. By using this module, you securely connect new resources, such as Compute Engine instances, to your established network environments without the need to recreate the networks. The module outputs attributes that uniquely identify the subnetwork so that other modules can consume the attributes.

For the complete list of inputs and outputs for this module, see the [`pre-existing-subnetwork` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/pre-existing-subnetwork#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `pre-existing-subnetwork` module, see the [`examples/hpc-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page.



### Required roles

To get the permissions that you need to discover the pre-existing subnetwork, ask your administrator to grant you the [Compute Network Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure the module

To identify the subnetwork, you can provide the self-link for the subnetwork. If you provide the `subnetwork_self_link` variable, then the module ignores the `subnetwork_name` variable, the `region` variable, and the `project` variable.

The following example demonstrates how to discover a subnetwork by using the `subnetwork_self_link` setting and pass the subnetwork attributes to the `vm-instance` module. The `use` keyword instructs the `vm-instance` module to accept the variables that identify the subnetwork so that the cluster creates the compute instance inside the correct subnetwork.
    
    
    - id: network
      source: modules/network/pre-existing-subnetwork
      settings:
        subnetwork_self_link: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK_NAME
    
    - id: example_vm
      source: modules/compute/vm-instance
      use:
      - network
      settings:
        name_prefix: example
        machine_type: c2-standard-4
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that owns the subnetwork.
  * `REGION`: the Google Cloud region where the subnetwork is located.
  * `SUBNETWORK_NAME`: the name of the pre-existing subnetwork.



## What's next

  * For the complete list of inputs and outputs for this module, see the [`pre-existing-subnetwork` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/pre-existing-subnetwork#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
