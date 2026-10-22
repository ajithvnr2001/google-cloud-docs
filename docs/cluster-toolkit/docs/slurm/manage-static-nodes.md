---
url: https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes/
title: Manage static compute nodes \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:08.585502+00:00
---

# Manage static compute nodes  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Manage static compute nodes Stay organized with collections  Save and categorize content based on your preferences. 

You can maintain your high performance computing (HPC) Slurm clusters with static compute nodes by following the procedures in this guide. The steps in this guide are the following:

  1. Understand how Slurm states relate to Compute Engine instance state.
  2. Update VM images.
  3. Restore down nodes.
  4. Remove nodes left behind after destruction.
  5. Review host maintenance.



For more information about different node types, see [About node types](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/node-types).

## How Slurm states relate to compute instance state

The compute instance that is backing your static compute nodes can transition through many states as part of its lifecycle. Changes in your Slurm state impacts the static compute nodes as follows:

  * If the Slurm state changes to `DOWN`, this only affects the Slurm state. The backing compute instance stays in a `RUNNING` state, and all attached state devices are unaffected.
  * If the Slurm state changes to `POWER_DOWN`, the backing compute instance is deleted. This deletion leads to a loss of instance state and loss of attached state devices.
  * When the Slurm state changes to `POWERING_UP`, a new compute instance is created.



For more information about what happens to a compute instance and its attached devices during each phase of its lifecycle, see [Compute Engine instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).

## Update VM images

During the operation of a cluster, you might need to update the OS image used by the compute nodes. Because compute instances backing static compute nodes are always up, this takes some additional consideration.

**Note:** When using `Slurm-GCP` static nodes, powering down a Slurm node (`scontrol update State=POWER_DOWN_ASAP`) is equivalent to deleting the backing compute instance. In this state, all node-local data is lost, including all data on Local SSDs.

To allow for updating images, the compute nodeset should be configured to use a custom image family that you are able to publish to. It is important to specify an image family and not a specific image name because the compute node always tries to use the latest image in a family, allowing the nodes to pick new images without redeploying the cluster. You also need to set the `instance_image_custom` setting to `true` to signify that a custom image is being used.

The following code block shows how to specify a custom image for a static nodeset.
    
    
    ‐ id: static_nodeset
      source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
      use: [network]
      settings:
        node_count_static: 4
        node_count_dynamic_max: 0
        instance_image_custom: true
        instance_image:
          family: custom-family
          project: $(vars.project_id)
        allow_automatic_updates: false
    

**Note:** The [`allow_automatic_updates: false`](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices#disable_automatic_updates) setting is only compatible with images that are built on top of an [HPC VM image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm#disable_automatic_updates) or its derivatives such as Slurm images.

For information about how to build a custom image on top of an existing Slurm image, see the [`examples/image-builder.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/image-builder.yaml) blueprint file.

Use the following steps to update the OS image of static compute nodes on a running cluster:

  1. Build a new OS image and save it to the required image family.

For example, say a nodeset is configured to use `custom-family`, and static compute nodes are running on `image-a` which is the latest image from `custom-family`. You can then build a new image, `image-b`, and publish it to `custom-family`. Once published, `image-b` is the latest image in `custom-family`, but the static compute nodes are still running on `image-a` since the image can't be updated on a running compute instance.

  2. SSH to the Slurm controller and run the following command. Replace `NODES_TO_UPDATE` with the nodes you are updating. We recommend testing updates on a small number of nodes prior to deploying throughout your cluster. For example, `compute-static-[0-1]` updates `compute-static-0` and `compute-static-1`.
         
         sudo -i -u slurm scontrol update NodeName=NODES_TO_UPDATE State=POWER_DOWN_ASAP Reason="image-update"

In the preceding command snippet, the Slurm user account is impersonated as it has permission to update node state. When you run the command, the state of the nodes are set to `POWER_DOWN_ASAP`. This drains the nodes, allowing jobs to finish but not taking on any new jobs. Once drained, Slurm deletes the compute instances that back the nodes. The node's state changes to `idle%` while the instance is being deleted and eventually transitions to `idle~` when deletion has finished.

  3. After some time, normally minutes, Slurm automatically recreates the deleted nodes and returns them to service. Optionally, when the node is in `idle~` state, you can manually initiate this process with the following command:
         
         sudo -i -u slurm scontrol update NodeName=NODES_TO_UPDATE State=POWER_UP

Depending on the timing, manual intervention might clash with the periodic automation and might result in compute instances being deleted and recreated. Once the node has fully booted it has a status of `idle`. At this point it is running on the new image, `image-b`. If you want to confirm the new image is being used, see [View the source OS image or source disk image of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-image#view_the_source_os_image_or_source_disk_image_of_a_vm).

  4. It might be helpful to label nodes to keep track of which nodes have been updated and advertise which nodes have new images. To label nodes, run the following command:
         
         sudo -i -u slurm scontrol update nodename=NODES_TO_UPDATE AvailableFeatures=image=rev3 




## Restore down nodes

When a node is in a `down*` state it is best to power it down which deletes the node and allows for it to be recreated. You can use the following command to restore down nodes. Replace `DOWNED_NODE` with the name of the downed node.
    
    
    sudo -i -u slurm scontrol update NodeName=DOWNED_NODE State=POWER_DOWN Reason="reset-node"

## Remove nodes left behind after destruction

It is common for nodes to be left behind when a cluster is destroyed. If you would like static compute nodes to be destroyed upon destruction of the cluster (when you run the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy)), you can use the `cleanup_compute_nodes` setting on the Slurm controller. Using this setting requires that local python dependencies are installed on the deployment machine. To install local python dependencies, see [controller description](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/develop/community/modules/scheduler/schedmd-slurm-gcp-v6-controller/README.md#description).

Static compute nodes can also be manually deleted after the controller has been destroyed although this might interfere with cleanup of any network resources created for and used by the static compute nodes.

## Review host maintenance

A [maintenance event](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) is when Compute Engine performs a hardware or software update on the host machine running a compute instance. How the instance is affected depends on whether the host maintenance policy is set to `TERMINATE` (default) or `MIGRATE`. When you use compact placement policies, as recommended in the best practices, Slurm overrides the host maintenance policy provided in the blueprint and sets it to TERMINATE. To view the host maintenance policy of a compute instance, see [View host maintenance policy of an instance](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#viewoptions).

If the host maintenance policy is set to `TERMINATE`, a maintenance event causes the compute instance to be stopped. When the instance is stopped, some forms of state are lost such as RAM state, instance state, and Local SSD state. Persistent disks are maintained. While the compute instance is stopped, Slurm state shows the node as `down*`. This shutdown disrupts any job running on that node. The default behavior is to requeue these failed jobs. For instructions on how to bring the node back up, see Restore down nodes.

If the host maintenance policy is set to `MIGRATE`, a maintenance event triggers a live migration where Compute Engine moves the compute instance to a new host, and there is no disruption to your job, although there may be a temporary performance impact while the migration is taking place. Also note that the topology changes due to live migrations.

Using the `MIGRATE` setting is not possible in all cases such as when using GPUs or when you use certain compact placement policies in some scenarios. You can manually trigger a maintenance event to test how it affects operation and performance by using the [Simulate a host maintenance event procedure](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance).

## What's next

  * Review the [Cluster blueprints catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
