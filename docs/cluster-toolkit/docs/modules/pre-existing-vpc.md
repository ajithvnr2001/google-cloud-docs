---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-vpc/
title: Use a pre-existing VPC network \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:42.660865+00:00
---

# Use a pre-existing VPC network  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Use a pre-existing VPC network Stay organized with collections  Save and categorize content based on your preferences. 

Use the `pre-existing-vpc` module to use an existing VPC network in Google Cloud and retrieve the network attributes.

This module lets you integrate your pre-provisioned network infrastructure into new Cluster Toolkit deployments. By using this module, you securely connect new resources, such as Compute Engine instances, to your established network environments without the need to recreate the networks. The module outputs attributes that uniquely identify the VPC network and subnetwork so that other modules can consume the attributes.

Because the module outputs align with the standard [`vpc` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/vpc), you can use the `pre-existing-vpc` module as a direct substitute.

For the complete list of inputs and outputs for this module, see the [`pre-existing-vpc` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/pre-existing-vpc#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `pre-existing-vpc` module, see the [`examples/hpc-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page.
  * If your target VPC network exists in a different Google Cloud project, then you can use this module to reference the network. However, if you use a network from a different project, then you must first configure a Cloud NAT gateway and configure Identity-Aware Proxy Transmission Control Protocol (TCP) forwarding. For more information about these prerequisites, see the following documentation:

    * [Cloud NAT overview](https://docs.cloud.google.com/nat/docs/overview)
    * [Use IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding)



### Required roles

To get the permissions that you need to discover the pre-existing VPC network and subnetwork, ask your administrator to grant you the [Compute Network Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use an existing VPC

The following example identifies a global network and a regional subnetwork. The `use` keyword instructs the `vm-instance` module to accept the variables that identify the network and subnetwork so that the cluster creates the compute instance inside the correct VPC network.
    
    
    - id: network1
      source: modules/network/pre-existing-vpc
      settings:
        project_id: $(vars.project_id)
        region: us-central1
    
    - id: example_vm
      source: modules/compute/vm-instance
      use:
      - network1
      settings:
        name_prefix: example
        machine_type: c2-standard-4
    

The `project_id` setting and the `region` setting are inferred from deployment variables that share the same name.

## What's next

  * For the complete list of inputs and outputs for this module, see the [`pre-existing-vpc` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/pre-existing-vpc#inputs) page in the Cluster Toolkit GitHub repository.
  * For a complete list of supported modules, see the [compatibility matrix](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/network_storage.md#compatibility-matrix) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
