---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/vm-instances/
title: Create VM instances \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:05:03.785225+00:00
---

# Create VM instances  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/vm-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create VM instances Stay organized with collections  Save and categorize content based on your preferences. 

The `vm-instance` module helps you provision and configure [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances) within your Cluster Toolkit blueprints. With this module, you streamline the deployment of high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads. You can consistently define settings such as machine type, image, networking, and placement policies. This approach helps ensure efficient and standardized resource provisioning. 

For the complete list of inputs and outputs that you can use with this module, see the [vm-instance module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/compute/vm-instance/README.md#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `vm-instance` module, see the [`examples/hpc-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `vm-instance` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select machine type** menu and then select a machine family, such as **N2**.



### Required roles

To get the permissions that you need to deploy the compute instances, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a basic compute instance group

To create a group of compute instances, add the `vm-instance` module to the `deployment_groups` section of your blueprint. You must specify the number of instances and the machine type.

The following example creates a cluster of 8 C2 instances that uses the `c2-standard-60` machine type and connects the instances to a VPC network that a separate network module defines.
    
    
    - id: compute
      source: modules/compute/vm-instance
      use: [network]
      settings:
        instance_count: 8
        name_prefix: compute
        machine_type: c2-standard-60
    

## Configure network connectivity

The `vm-instance` module requires you to configure network connectivity for your compute instances. You can configure network connectivity in one of the following ways:

  * **Reference a network module** Connect your compute instances by using a [`vpc` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/vpc) or a [`pre-existing-vpc` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-vpc). Specify the module ID in the `use` field. The `vm-instance` module automatically configures the network interface using the outputs from the referenced network. We recommend this method as this configuration is less manual.

  * **Define network interfaces manually.** If you need to connect to multiple networks or require advanced customization, then use the `network_interfaces` setting. This setting lets you manually configure specific network interfaces on the compute instance.

The format for this setting matches the `network_interface` block in the Terraform `google_compute_instance` resource. For more information, see the [Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance#nested_network_interface).

**Note:** If you provide the `network_interfaces` variable, then the module ignores any networks associated through the `use` field. Additionally, the `bandwidth_tier` and `disable_public_ips` settings don't apply to networks that you define in `network_interfaces` input. You can find more information about this [input on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/modules/compute/vm-instance/README.md#inputs).



## Configure compute instance placement

Use the `placement_policy` setting to control where your compute instances are physically located relative to each other within a zone. This configuration is critical for high performance computing (HPC) workloads that require low latency (compact placement) or high availability (spread placement). For more information about placement policies, see the [Placement policies overview](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).

### Compact placement

Compact placement creates compute instances close to each other to minimize network latency. By default, the policy results in the most compact set of instances available.
    
    
    - id: compute
      source: modules/compute/vm-instance
      use: [network]
        settings:
          ...
          placement_policy:
            collocation: "COLLOCATED"
    

To enforce strict compactness and fail the deployment if the specified level of compactness is not available, use the `max_distance` setting:
    
    
    placement_policy:
      collocation: "COLLOCATED"
      max_distance: 1
    

### Spread placement

Spread placement ensures that compute instances are placed in different availability domains to improve fault tolerance.
    
    
    - id: compute
      source: modules/compute/vm-instance
      use: [network]
        settings:
          ...
          placement_policy:
            availability_domain_count: 2
    

## Configure simultaneous multithreading (SMT)

Simultaneous multithreading (SMT) is disabled by default (`threads_per_core=1`) in this module. This configuration results in only physical cores being visible on the compute instance. This default is often preferred for HPC workloads to improve performance.

When the `threads_per_core` field is set to a value of `2`, the total number of virtual cores for the `c2-standard-60` machine type is extended to 60 virtual cores. With the `threads_per_core` field set to `1` (SMT turned off), 30 physical cores are available on the compute instance.

To enable SMT and expose virtual cores, set the `threads_per_core` field to a value of `2`:
    
    
    settings:
      instance_count: 8
      machine_type: c2-standard-60
      threads_per_core: 2
    

## Configure GPU support

To learn more about GPU support in `vm-instance` and other Cluster Toolkit modules, see [GPU support](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gpu-support.md) in the GitHub repository.

## Replace specific compute instances

The `vm-instance` module automatically replaces your compute instances when you change the `instance_image` variable and run `terraform apply` or the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) on the deployment group folder. However, creating a new image in an image family does not automatically trigger a replacement.

To selectively replace specific compute instances without changing the configuration, use the `terraform apply -replace` command:
    
    
    terraform state list
    # Search for the module ID and resource address
    terraform apply -replace="address"
    

For more information on the syntax for this command, see the [Terraform documentation](https://developer.hashicorp.com/terraform/cli/commands/apply#replace-resource).

## What's next

  * To deploy this blueprint, see [Deploy a cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/deploy-cluster-overview).
  * For a complete list of all available input fields and output values, see the [vm-instance module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/compute/vm-instance/README.md#inputs) in the GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
