---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/resource-policy/
title: Create a resource policy \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:15.597849+00:00
---

# Create a resource policy  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/resource-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a resource policy Stay organized with collections  Save and categorize content based on your preferences. 

Use the `resource-policy` module to create a [Compute Engine resource policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview). This module lets you define placement policies, such as specifying that instances should be physically located close together (compact) or spread apart (spread) to meet your workload latency or availability requirements. 

You can apply this policy to other modules, such as the [`gke-node-pool` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-node-pool), to control the placement of the provisioned nodes.

For the complete list of inputs and outputs, see the [`resource-policy` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/compute/resource-policy/README.md#inputs) in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. To view a working example of a blueprint configured for the `resource-policy` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select software or resource** menu, and then select **Compute Engine resource policy**. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * The `resource-policy` module does not create a continuous long-running workload or a full cluster. It creates [Compute Engine resource policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) to define placement constraints for compute instances or GKE nodes.



### Required roles

To get the permissions that you need to create and manage Compute Engine resource policies , ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a placement policy

To create a placement policy, add the `resource-policy` module to your blueprint. You can then reference this policy in other modules by using the `use` keyword.

The following example creates a compact group placement policy with a maximum distance of 2. It then applies this policy to a GKE node pool.
    
    
      - id: group_placement_1
        source: modules/compute/resource-policy
        settings:
          name: gp-np-1
          group_placement_max_distance: 2
    
      - id: node_pool_1
        source: modules/compute/gke-node-pool
        use: [group_placement_1]
        settings:
          machine_type: e2-standard-8
        outputs: [instructions]
    

**Note:** The possible maximum distance value changes depending on your machine type. For details, see [About compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies).

## What's next

  * To learn how to use this policy with a GKE node pool, see [Create a Google Kubernetes node pool](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-node-pool).
  * For a complete list of all available input fields and output values, see the [`resource-policy` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/compute/resource-policy/README.md#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
