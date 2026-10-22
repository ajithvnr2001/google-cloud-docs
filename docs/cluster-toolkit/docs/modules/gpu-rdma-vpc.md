---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gpu-rdma-vpc/
title: Create a GPU RDMA VPC network \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:24.243366+00:00
---

# Create a GPU RDMA VPC network  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gpu-rdma-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a GPU RDMA VPC network Stay organized with collections  Save and categorize content based on your preferences. 

Use the `gpu-rdma-vpc` module to create a VPC network that is optimized for GPU Remote Direct Memory Access (RDMA) traffic.

This module is a simplified version of the standard [`vpc` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/vpc). This module lets you automatically create a variable number of subnetworks within a single VPC network. Each generated subnetwork contains its own distinct IP address range. By using this module, you can provision the complex network topologies that you need for high-performance GPU clusters.

The module outputs the following unique parameters:

  * The `subnetwork_interfaces` parameter, which is compatible with Slurm modules and `vm-instance` modules.
  * The `subnetwork_interfaces_gke` parameter, which is compatible with Google Kubernetes Engine modules.



For the complete list of inputs and outputs for this module, see the [`gpu-rdma-vpc` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/gpu-rdma-vpc#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `gpu-rdma-vpc` module, see the [`examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-blueprint.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-blueprint.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `gpu-rdma-vpc` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select machine type** menu and then select **a3-ultragpu-8g**.
  * The `gpu-rdma-vpc` module does not create a continuous long-running workload or a full cluster. It provisions a VPC network with multiple subnetworks optimized for GPU RDMA traffic.



### Required roles

To get the permissions that you need to create the VPC network and subnetworks, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure the subnetworks template

The main difference between this module and the standard `vpc` module is the `subnetworks_template` variable. This variable serves as the template for all subnetworks that the module creates within the network.

The template contains the following values:

  * **Count:** the number of subnetworks to create. Specify this value by using the `count` field.
  * **Name prefix:** the prefix for the subnetwork names. Specify this value by using the `name_prefix` field.
  * **IP range:** the Classless Inter-Domain Routing (CIDR) formatted IP address range. Specify this value by using the `ip_range` field.
  * **Region:** the Google Cloud region where the module deploys the subnetwork. Specify this value by using the `region` field.

**Warning:** You must verify that the `ip_range` value is always large enough to split into the number of subnetworks that you define in the `count` field, while also accommodating the number of required connections within each subnetwork.

The following example demonstrates how to use the `gpu-rdma-vpc` module to create a new VPC network named `test-rdma-net`. The module creates eight subnetworks with names ranging from the `test-mrdma-sub-0` string to the `test-mrdma-sub-7` string.

The subnetworks split the IP address range evenly, starting from bit 16 (0-indexed). The Slurm nodeset then ingests the networks within the `additional_networks` setting.
    
    
      - id: rdma-net
        source: modules/network/gpu-rdma-vpc
        settings:
          network_name: test-rdma-net
          network_profile: https://www.googleapis.com/compute/beta/projects/$(vars.project_id)/global/networkProfiles/$(vars.zone)-vpc-roce
          network_routing_mode: REGIONAL
          subnetworks_template:
            name_prefix: test-mrdma-sub
            count: 8
            ip_range: 192.168.0.0/16
            region: $(vars.region)
    
      - id: a3_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network0]
        settings:
          machine_type: a3-ultragpu-8g
          additional_networks:
            $(concat(
              [{
                network=null,
                subnetwork=network1.subnetwork_self_link,
                subnetwork_project=vars.project_id,
                nic_type="GVNIC",
                queue_count=null,
                network_ip="",
                stack_type=null,
                access_config=[],
                ipv6_access_config=[],
                alias_ip_range=[]
              }],
              rdma-net.subnetwork_interfaces
            ))
          ...
    

## What's next

  * For the complete list of inputs and outputs for this module, see the [`gpu-rdma-vpc` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/gpu-rdma-vpc#inputs) page in the Cluster Toolkit GitHub repository.
  * For a complete list of supported modules, see the [compatibility matrix](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/network_storage.md#compatibility-matrix) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
