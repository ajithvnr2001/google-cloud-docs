---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset/
title: Create a nodeset for a Slurm partition \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:13.309299+00:00
---

# Create a nodeset for a Slurm partition  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a nodeset for a Slurm partition Stay organized with collections  Save and categorize content based on your preferences. 

Use the `schedmd-slurm-gcp-v6-nodeset` module to define a group of compute nodes, known as a nodeset. This module creates the data structure required by the [`schedmd-slurm-gcp-v6-partition` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition) to build a partition. 

Nodesets let you add different types of nodes to a partition. This configuration lets you run jobs that use a mix of hardware specifications.

For a complete list of inputs and outputs, see the [`schedmd-slurm-gcp-v6-nodeset` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/compute/schedmd-slurm-gcp-v6-nodeset/README.md#inputs) in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `slurm-nodeset` module, see the [`examples/hpc-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `slurm-nodeset` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** list, and then select **Slurm**.



### Required roles

To get the permissions that you need to deploy the nodeset, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a nodeset

To create a nodeset, add the `schedmd-slurm-gcp-v6-nodeset` module to your blueprint. You must specify the machine type and the maximum number of dynamic nodes.

The following example uses the `schedmd-slurm-gcp-v6-nodeset` module as input to create a partition module that does the following:

  * Uses the `c2-standard-30` machine type.
  * Sets a maximum count of 200 dynamically created nodes for the nodeset.
  * Uses a nodeset name of `ghpc`.
  * Connects to the module with the `network` ID by using the `use` field.
  * Mounts nodes to the `homefs` network file system by using the `use` field.


    
    
    - id: nodeset
      source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
      use:
      - network
      settings:
        node_count_dynamic_max: 200
        machine_type: c2-standard-30
    
    - id: compute_partition
      source: community/modules/compute/schedmd-slurm-gcp-v6-partition
      use:
      - homefs
      - nodeset
      settings:
        partition_name: compute
    

## Target specific nodesets

To specify nodes from a specific nodeset in a partition, use the `--nodelist` or `-w` flag. This example selects three nodes from `cluster-compute-group-[0-2]` in the compute partition:
    
    
    srun -N 3 -p compute --nodelist cluster-compute-group-[0-2] hostname
    

Depending on how the nodes differ, you can also use the `--constraint` or `-C` flag or other flags, such as `--mincpus`, to specify nodes with the selected characteristics.

## Configure reservations

The `schedmd-slurm-gcp-v6-nodeset` module lets you use Compute Engine [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) to get capacity for your Slurm nodes. You can configure both local and shared reservations by using the `reservation_name` setting. The reservation you use with this module must be a [specifically targeted reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation) of type `SPECIFIC_RESERVATION`.

### Reservation types

You can configure the following types of specific reservations:

  * **Local reservation:** a reservation located within the same project as the cluster (`var.project_id`).
  * **Shared reservation:** a [shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared) from a different host project. Shared reservations let you manage reservations centrally across multiple projects.



### Reservation name formats

The format that you specify for the `reservation_name` setting determines the type of reservation that is used:

  * **Local reservation format:** for a reservation in the same project as the cluster (`var.project_id`), specify the reservation name:
        
        reservation_name: RESERVATION_NAME
        

  * **Shared reservation format:** for a reservation shared from a different project, specify the full resource path:
        
        reservation_name: projects/HOST_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_ID/reservationSubBlocks/SUBBLOCK_ID
        




Replace the following:

  * `HOST_PROJECT_ID`: the project ID of the host project where the shared reservation was created.
  * `RESERVATION_NAME`: the name assigned to the specific reservation.
  * `BLOCK_ID`: the identifier for a specific reservation block, if the reservation contains multiple blocks. This field is optional.
  * `SUBBLOCK_ID`: the identifier for a specific reservation subblock within a block. This field is optional.

**Note:** To retrieve full reservation details when you use a shared reservation, the node service account requires the `compute.reservations.get` permission in the host project (`HOST_PROJECT_ID`). If this permission is missing, then the system falls back to minimal reservation settings and continues the deployment.

### Deploy without a reservation

To deploy nodes without a specific reservation, or to use [automatically consumed reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_any_matching_reservation), set the `reservation_name` setting to an empty string (`""`).

## Configure zone policies

You can specify additional zones for your nodeset to create compute instances by using bulk creation. Configuring partitions with popular machine families lets you access more compute resources across zones.

**Warning:** Zone policies that allow compute instances to be created across multiple zones can lead to additional egress costs when you move large amounts of data between zones in the same region. For example, egress charges apply to traffic between compute instances and shared file systems. To avoid egress charges, make sure that you create compute nodes in a single zone by setting the `var.zone` variable and by leaving the `var.zones` variable to its default value of the empty list.

If Google Cloud adds a new zone to the region while the cluster is active, then nodes in the partition might be created in that zone. In this case, you might need to redeploy the partition to help ensure that the partition denies the zone that was newly added.
    
    
    vars:
      zone: us-central1-f
    
    -   id: zonal-nodeset
      source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
    

The following example configuration lets you create compute instances in additional zones:
    
    
    vars:
      zone: us-central1-f
    
    -   id: multi-zonal-nodeset
      source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
      settings:
        zones:
        -   us-central1-a
        -   us-central1-b
    

## Configure compute instance placement in the nodeset

Use the `enable_placement` setting to decide how Google Cloud places your compute instances in the nodeset.

By default, the `enable_placement` setting is set to a value of `true`. With this setting enabled, the module groups your compute instances close together to help them communicate faster by reducing network latency.

In certain cases, it might be helpful to disable the `enable_placement` setting, such as when you want to do any of the following:

  * **Avoid resource shortages.** When placement is enabled, Google Cloud tries to create all requested compute instances in the same hardware group. If there isn't enough space in that group, the request might fail completely. Disabling placement lets Google Cloud create your instances wherever space is available.
  * **Improve reliability.** To help ensure that a single hardware failure doesn't affect all of your compute instances at once, spread your instances across different hardware.
  * **Avoid extra costs.** If you use specific types of reservations, such as non-dense reservations, then you can avoid the extra cost of placement policies.



To control the maximum distance between nodes in a placement group, use the `placement_max_distance` setting. Lower maximum distance values help ensure closer instance placement, but can result in fewer available machines for compute instance placement. Cluster Toolkit restricts which values are available for the `placement_max_distance` setting based on your chosen machine type.

For more information about supported machine types and maximum distance values, see [About compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) in the Compute Engine documentation.

## Configure custom images

To create valid custom images for the node group compute instances or for custom instance templates, see [Slurm on Google Cloud custom images](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/vm-images.md#slurm-on-gcp-custom-images) on GitHub.

## Configure GPU support

For more information about configuring GPUs in Slurm on Google Cloud v6 and other Cluster Toolkit modules, see [GPU support](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gpu-support.md) on GitHub.

## Get support

The Cluster Toolkit team maintains the wrapper around the `slurm-on-gcp` Terraform modules. For support with the underlying modules, see the instructions in the [Slurm on Google Cloud README](https://github.com/GoogleCloudPlatform/slurm-gcp#overview) on GitHub.

## What's next

  * To add this nodeset to a partition, see [Create a partition for a Slurm controller](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition).
  * To learn about creating nodesets specifically for TPUs, see [Create a TPU nodeset for a Slurm partition](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-nodeset-tpu).
  * For a complete list of all available input fields and output values, see the [`schedmd-slurm-gcp-v6-nodeset` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/compute/schedmd-slurm-gcp-v6-nodeset/README.md#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
