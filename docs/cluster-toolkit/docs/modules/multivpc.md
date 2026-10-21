---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/multivpc/
title: Create multiple VPC networks \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:42.397053+00:00
---

# Create multiple VPC networks  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/multivpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create multiple VPC networks Stay organized with collections  Save and categorize content based on your preferences. 

Use the `multivpc` module to create up to eight VPC networks, each with a single subnetwork that contains a distinct IP address range.

By using this module, you can quickly deploy multiple isolated network environments for complex cluster configurations, such as high performance computing (HPC) workloads. The module outputs the `additional_networks` parameter, which lets you connect your networks to Slurm modules.

For the complete list of inputs and outputs for this module, see the [`multivpc` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/multivpc#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `multivpc` module, see the [`examples/gke-tpu-v6e/gke-tpu-v6e.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-v6e/gke-tpu-v6e.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page.



### Required roles

To get the permissions that you need to create multiple VPC networks and subnetworks, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure multiple networks

To configure the `multivpc` module, you must define the following variables:

  * **Name prefix:** the name prefix for the VPC networks. The module prepends this string to all networks and subnetworks and appends a unique number. Specify this value by using the `network_name_prefix` field.
  * **Network count:** the number of VPC networks that you want to create. Specify this value by using the `network_count` field.
  * **Global IP range:** the Classless Inter-Domain Routing (CIDR) formatted IP address range that spans the entire set of networks. Specify this value by using the `global_ip_address_range` field.
  * **Subnetwork CIDR suffix:** the CIDR suffix that defines the address space that the individual VPC networks cover. Specify this value by using the `subnetwork_cidr_suffix` field.

**Warning:** You must verify that the `subnetwork_cidr_suffix` value is larger than the CIDR suffix on the `global_ip_address_range` value. The difference between these two suffixes must be large enough to accommodate the number of VPC networks that you deploy. For example, the CIDR suffix bit difference must be less than or equal to the `ceil(log2(network_count))` value.

**Note:** If your deployment requires multiple VPC networks that don't meet this specific structure, we recommend that you deploy multiple individual `vpc` modules instead.

## Example configuration

The following example shows how to use the `multivpc` module to create eight new VPC networks. The module assigns names ranging from the `multivpc-net-0` string to the `multivpc-net-7` string. The module also creates exactly one subnetwork in each VPC network.
    
    
      - id: network
        source: modules/network/vpc
    
      - id: multinetwork
        source: modules/network/multivpc
        settings:
          network_name_prefix: multivpc-net
          network_count: 8
          global_ip_address_range: 172.16.0.0/12
          subnetwork_cidr_suffix: 16
    
      - id: a3_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network, multinetwork]
        settings:
          machine_type: a3-highgpu-8g
    
    

## What's next

  * For the complete list of inputs and outputs for this module, see the [`multivpc` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/multivpc#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
