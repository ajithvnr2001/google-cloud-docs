---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-controller/
title: Create a Slurm controller node \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:15.360335+00:00
---

# Create a Slurm controller node  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-controller/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Slurm controller node Stay organized with collections  Save and categorize content based on your preferences. 

The `schedmd-slurm-gcp-v6-controller` module lets you create a Slurm controller node. By using this module, you establish the central management node for your Slurm cluster. The controller node manages job queues, schedules workloads, and monitors compute resources.

For the complete list of inputs and outputs for this module, see the [`schedmd-slurm-gcp-v6-controller` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/scheduler/schedmd-slurm-gcp-v6-controller#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for Slurm, see the [`examples/hpc-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support Slurm, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **Slurm**.
  * The `schedmd-slurm-gcp-v6-controller` module does not execute your individual jobs or provide direct user login capability. It establishes the central management plane to monitor compute resources and orchestrate the scheduling of your workloads.



### Required roles

To get the permissions that you need to deploy the Slurm controller node, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Slurm controller

The following example creates a controller node that has the following attributes:

  * Connects to the primary subnetwork of the `network` module.
  * Mounts the file system that has the `homefs` identifier.
  * Configures one partition that has the `compute_partition` identifier.
  * Upgrades the machine type from the default `c2-standard-4` type to the `c2-standard-8` type.


    
    
      - id: slurm_controller
        source: community/modules/scheduler/schedmd-slurm-gcp-v6-controller
        use:
        - network
        - homefs
        - compute_partition
        settings:
          machine_type: c2-standard-8
    

## Update your live Slurm cluster

The `schedmd-slurm-gcp-v6-controller` module supports the reconfiguration of partitions and the Slurm configuration in a running, active cluster. To reconfigure a running cluster, do the following:

  1. Edit the blueprint with the configuration changes that you want.
  2. To overwrite the deployment directory, execute the [`gcluster create` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-create) and append the `-w` flag.
  3. Deploy the changes by following the terminal instructions.



The following list provides examples of updates that you can apply to a running cluster:

  * Add or remove a partition.
  * Resize an existing partition.
  * Attach new network storage to an existing partition.

**Note:** Changing the machine type of a Compute Engine instance within a partition might fail. We recommend that you create a new partition and delete the old partition instead.

## Configure custom images

For more information about how to create valid custom images for the controller compute instance or for custom instance templates, see the [Slurm on Google Cloud custom images](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/vm-images.md#slurm-on-gcp) documentation on GitHub.

## Turn on scheduled maintenance reservations

A [maintenance event](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) occurs when Google Cloud stops a compute instance to perform a hardware update or a software update. The host maintenance policy determines these events. Maintenance events can disrupt your running jobs.

To protect jobs from termination during maintenance, you can turn on the scheduled maintenance reservation feature for your compute nodeset. When you turn on this feature, Slurm reserves your node for maintenance during the maintenance window. Slurm does not schedule any jobs that overlap with the maintenance reservation.

To turn on the maintenance reservation feature, configure your blueprint to resemble the following example:
    
    
      - id: compute_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network]
        settings:
          enable_maintenance_reservation: true
    

When you execute a job on the Slurm cluster, you can specify the total run time of the job in minutes by using the [`-t` flag](https://slurm.schedmd.com/srun.html#OPT_time). This flag helps ensure that the job executes only outside of the maintenance window. The following command sets the total run time to 10 minutes:
    
    
    srun -n1 -pcompute -t 10:00 JOB_FILE.sh
    

Only the Compute Engine API `alpha` version supports the maintenance notification feature. To update the API version in your blueprint, configure the `endpoint_versions` setting to resemble the following example:
    
    
      - id: slurm_controller
        source: community/modules/scheduler/schedmd-slurm-gcp-v6-controller
        settings:
          endpoint_versions:
            compute: "alpha"
    

## Opportunistic Compute Engine API maintenance in Slurm

You can turn on opportunistic Compute Engine API maintenance to perform early maintenance as a Slurm job. If the system detects a node for maintenance, then Slurm creates a maintenance job and places the job in the queue.

If you use the [backfill](https://slurm.schedmd.com/sched_config.html#backfill) scheduler, Slurm backfills the maintenance job if a time window is available. You can also use the built-in scheduler. If you use the built-in scheduler, then Slurm executes the maintenance job in strict priority order. If the maintenance job does not execute, then forced maintenance occurs at the scheduled window.

To turn on this feature at the nodeset level, configure your blueprint to look like the following:
    
    
      - id: debug_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network]
        settings:
          enable_opportunistic_maintenance: true
    

## Use placement policies

When you turn on the [`enable_placement`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/compute/schedmd-slurm-gcp-v6-nodeset/README.md#input_enable_placement) setting with Slurm, Google Cloud attempts to place the compute instances as physically close together as possible. Capacity constraints at the time of instance creation might still force the system to spread the compute instances across multiple racks.

Google provides the `max-distance` flag to control the maximum allowed spreading. For more information about the `max-distance` flag, see [Reduce latency by using compact placement policies](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies).

You can use the `placement_max_distance` setting on the `schedmd-slurm-gcp-v6-nodeset` module to control the `max-distance` behavior. The following example demonstrates how to configure this setting:
    
    
      - id: nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [ network ]
        settings:
          machine_type: c2-standard-4
          node_count_dynamic_max: 30
          enable_placement: true
          placement_max_distance: 1
    

You must set the `enable_placement` variable to `true` for the `placement_max_distance` setting to take effect.

In the preceding example, a value of `1` restricts the compute instances to the same rack. To confirm that the system applied the `max-distance` value, execute the following command while jobs are running:
    
    
    gcloud beta compute resource-policies list \
      --format='yaml(name,groupPlacementPolicy.maxDistance)'
    

**Warning:** If a zone lacks capacity, a lower `max-distance` value, such as `1`, increases the probability that the compute instance creation fails.

## Configure tree width and node communication

Slurm uses a fan-out mechanism to communicate with large groups of nodes. The [`TreeWidth`](https://slurm.schedmd.com/slurm.conf.html#OPT_TreeWidth) configuration variable determines the shape of this fan-out tree.

In the cloud, this fan-out mechanism can become unstable when nodes restart with new IP addresses. You can enforce that all nodes communicate directly with the controller by setting the `tree_width` value to a number greater than or equal to the largest partition.

If the largest partition contains 200 nodes, then configure the blueprint to resemble the following example:
    
    
      - id: slurm_controller
        source: community/modules/scheduler/schedmd-slurm-gcp-v6-controller
        settings:
          cloud_parameters:
            tree_width: 200
    

The default value is `128`. Values greater than `128` might cause congestion on the controller.

## Configure resume rate and node resumption

The `ResumeRate` parameter in the `slurm.conf` file controls the maximum number of nodes that Slurm attempts to resume per minute. This parameter is important in cloud environments because autoscaling can cause a large number of nodes to start concurrently.

When many nodes start simultaneously, they place a heavy load on shared resources, such as shared file systems. To reduce the peak load on these shared resources and improve overall cluster stability during scaling events, you can limit the `ResumeRate` parameter to stagger the node startup process.

The following example demonstrates how to limit the node resumption rate to 100 nodes per minute by using the `cloud_parameters` setting:
    
    
      - id: slurm_controller
        source: community/modules/scheduler/schedmd-slurm-gcp-v6-controller
        settings:
          cloud_parameters:
            resume_rate: 100
    

Adjust this value based on the capabilities of your shared file system and the expected scaling behavior of your cluster.

## What's next

  * For the complete list of inputs and outputs for this module, see the [`schedmd-slurm-gcp-v6-controller` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/scheduler/schedmd-slurm-gcp-v6-controller#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
