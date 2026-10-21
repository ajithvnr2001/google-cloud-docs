---
url: https://docs.cloud.google.com/compute/docs/instance-groups/preserved-state/
title: How some operations affect preserved state of managed instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:06.293133+00:00
---

# How some operations affect preserved state of managed instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/preserved-state/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  How some operations affect preserved state of managed instances Stay organized with collections  Save and categorize content based on your preferences. 

Read the following sections to learn how various configurations, [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) actions, or instance lifecycle events affect the [preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) of a [managed instance](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance), in a [stateful MIG](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs):

  * Autohealing
  * Updating instances
  * Group resizing
  * Deleting an instance
  * Abandoning an instance
  * Regional groups



## How autohealing handles preserved state

When a virtual machine (VM) instance stops running or becomes [unhealthy](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#health_states), [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) recreates the VM and keeps the preserved state for items that you have configured:

  * The MIG preserves stateful disks and IP addresses and reattaches them on VM recreation.
  * The MIG preserves stateful metadata, configured in per-instance configurations, and sets it on VM recreation.

**Note:** Autohealing might not help if a VM becomes unhealthy due to a corrupt stateful disk. The root cause might remain unresolved because the MIG preserves and reattaches the corrupt stateful disk on instance recreation.

To avoid VM instance recreation failures due to a corrupt stateful boot disk, keep the boot disk stateless so that autohealing can recreate that disk from scratch by using the original image.

## How updating instances handles preserved state

When you update an instance, the MIG maintains the instance's preserved state (disks, IP addresses, metadata):

  * The MIG preserves stateful disks and IP addresses and reattaches them, if the VM instance is recreated or restarted during the update.
  * The MIG preserves stateful metadata, configured in a per-instance configuration, and sets it on the instance during the update.



When setting a new instance template, you must define all disks that you specified in your stateful policy. Setting a new instance template that omits a disk that is defined in a stateful policy is not allowed. This helps prevent accidental deletion of stateful disks.

To remove stateful disks from a MIG when those disks are defined in a stateful policy, use the following procedure:

  1. Remove the disk configuration from your stateful policy.
  2. (Optional.) Detach the disks from the VM instances if you still want to keep them.
  3. Rollout a new instance template that no longer defines the disks.



You cannot update stateful disks to a new image because these disks must be preserved during the update, and updating to a new image requires recreation of a disk.

Google recommends that you keep boot disks and any disks with binaries or temporary files stateless, while keeping your data on stateful disks. Such a configuration supports the following behavior:

  * You can easily and automatically update the boot disk and the disks with binaries to newer images that contain new versions and security patches. You can use auto-updating, or you can manually update the instances to recreate such stateless disks, while keeping your data intact on separate stateful disks.
  * You can preserve the data on stateful disks when rolling out other updates to your instances.



You can configure a boot disk to be stateful, for example, to host a legacy application that keeps binaries and data on the same disk. This lets you move an application to a MIG to benefit from autohealing. But, in this scenario, you must perform software and operating system updates yourself, for example, by updating individual packages using a package manager such as apt on Debian systems, or by using configuration management tools.

If you only configured custom instance names and did not configure stateful disks or metadata, then you can use automated rolling updates. For automated rolling updates, you must set the Updater's replacement policy to `RECREATE`. You cannot use the `SUBSTITUTE` replacement method for auto-updating instances in stateful MIGs because this method substitutes each existing VM with a new one that has a different name and preserved state.

## How group resizing affects preserved state

**Decreasing group size**

Google does not recommend [decreasing the size](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig) of a stateful MIG because the MIG picks the VM instances for deletion and might pick VMs that you need to preserve. You can remove MIG VM instances in a controlled way by [deleting specific instances](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) that you no longer need.

If you do decrease MIG size, the MIG deletes all extra VM instances, together with their associated preserved states. To prevent this, you can configure the MIG to detach and preserve stateful disks and IP addresses on permanent VM instance deletion. Stateful metadata is deleted together with preserved state. For more information, see how deleting an instance affects preserved state.

**Increasing group size**

When you increase the size of a stateful MIG, the group creates VMs from the current instance template with auto-generated names ([base instance name](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--base-instance-name) \+ suffix). You can see the applied stateful configuration in the corresponding managed instance's `preservedStateFromPolicy`. After the MIG creates the instances, you can define stateful metadata and additional stateful disks or IP addresses in the per-instance configurations for these instances.

You can pick custom instance names and increase group size by [creating instances](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs) manually, with the option to bootstrap their state by providing per-instance configurations with stateful metadata, IP addresses, and disks for each instance.

**Note:** You cannot use autoscaling with stateful MIGs.

## How deleting an instance affects preserved state

A VM in a MIG is permanently deleted when:

  * You reduce the size of the group, and the MIG picks this VM instance for deletion, or
  * You delete the whole group, or
  * You specifically [delete the instance](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from the MIG.



When a VM is permanently deleted, the MIG also deletes the corresponding per-instance configuration and managed instance, including its preserved state configuration.

Permanent VM deletion results in the loss of all stateful metadata key-value pairs.

You can configure whether to keep or delete stateful disks and IP addresses on permanent instance deletion by setting the `autoDelete` flag for each resource either in the stateful policy or in a per-instance configuration. The flag supports two options:

  * `NEVER`: (Default.) The MIG never deletes the disk.
  * `ON_PERMANENT_INSTANCE_DELETION`: The MIG deletes the disk when the instance is permanently deleted.



The MIG does not delete stateful resources when autohealing, updating, or recreating instances.

**Note:** You can also disable disk [auto-deletion](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--disk) in the instance template. Although this configuration preserves disk on permanent instance deletion, it is intended for configuring standalone instances either created directly or [created from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template) but outside of a MIG. We do not recommend disabling disk auto-deletion in an instance template for use with MIGs because a MIG might fail to reattach the detached disk on instance recreation, autohealing, or auto-update. Instead, you can configure whether to preserve disks on permanent instance deletion in a stateful policy or in per-instance configurations.  
  
The `autoDelete` flag for a disk set in a stateful policy or in a per-instance configuration has priority over an equivalent `autoDelete` flag in the instance template.

In the following example, the MIG has a single VM `node-1` with a preserved state defined by a per-instance configuration. The preserved state includes two disks (blue & green) and `id:xyz273` metadata. If you resize the MIG to zero, the MIG triggers permanent deletion of the instance, `node-1`, which causes the following effects:

  * The MIG deletes the managed instance and its preserved state configuration.
  * The MIG deletes the per-instance configuration for the instance.
  * The MIG deletes the actual VM instance resource.
  * Metadata `id:xyz273` is lost because the VM instance and its preserved state configuration are deleted.
  * The stateful blue disk is deleted because, for this disk, the per-instance configuration has `autoDelete: ON_PERMANENT_INSTANCE_DELETION`.
  * The stateful green disk is detached because, for this disk, the per-instance configuration has `autoDelete:NEVER`.



![Deleting an instance from a stateful MIG.](https://docs.cloud.google.com/static/compute/images/mig-stateful-deleting-an-instance.png)

## How abandoning an instance affects preserved state

When you [abandon](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances) a VM instance from a MIG, the state of the VM, including stateful metadata, IP addresses, and disks, remains on the instance outside of the MIG. Because the VM is no longer managed by the MIG, the MIG deletes the corresponding per-instance configuration and [managed instance](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance), including the instance's preserved state configuration.

**Note:** If you set stateful configuration for a disk (either in a stateful policy or in a per-instance configuration), the disk is kept even if you delete the standalone VM instance after abandoning the instance from the MIG. This is because the VM instance preserves its `autoDelete` [setting](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances) for the disk (`instances.disks[].autoDelete = FALSE`) through the abandon operation.

In the following example, the VM `node-1` has preserved state, defined by a stateful policy (blue disk) and a per-instance configuration (green disk and metadata `id:xyz273`). If you abandon the instance, `node-1`, from the MIG, here is what happens to its preserved state:

  * The standalone VM instance, `node-1`, preserves its state: all its disks remain attached and metadata, `id:xyz273`, remains set on the VM.
  * The MIG deletes the managed instance and its preserved state configuration.
  * The MIG deletes the per-instance configuration for the instance.
  * The stateful policy remains unchanged because it is applicable to all instances in the MIG.



![Abandoning an instance from a stateful MIG.](https://docs.cloud.google.com/static/compute/images/mig-stateful-abandoning-an-instance.png)

## How regional groups handle preserved state

Stateful regional MIGs handle the preserved states of their instances in the same way as zonal MIGs except that regional MIGs create VM instances in multiple zones:

  * When creating instances, a regional MIG evenly distributes VMs across zones in the region to maximize the availability of your app in the event of a zone-level failure.
  * For existing instances, a stateful regional MIG cannot redistribute or move existing VMs across zones automatically because the preserved state is stored in a specific zone and cannot be moved. For that reason, stateful regional MIGs only support an [instance redistribution type](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution) setting of `NONE`.



## Feedback

We want to learn about your use cases, challenges, and feedback about stateful MIGs. Please share your feedback with our team at [mig-discuss@google.com](mailto:mig-discuss@google.com).

## What's next

  * Read [How stateful MIGs work](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work).
  * Read [Configuring stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs) to learn how to support stateful workloads by preserving instance names, persistent disks, and metadata in managed instances.
  * Learn more about [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).
  * Work with [managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
