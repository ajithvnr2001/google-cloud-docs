---
url: https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work/
title: How stateful MIGs work \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:53.478253+00:00
---

# How stateful MIGs work  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  How stateful MIGs work Stay organized with collections  Save and categorize content based on your preferences. 

A [stateful managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) (stateful MIG) preserves the unique state of each virtual machine (VM) instance—including VM name, attached persistent disks, IP addresses, and/or metadata—on machine restart, recreation, auto-healing, or update.

This page describes how stateful MIGs work. See [Configuring stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs) to learn how to set up a stateful MIG.

## Overview of how stateful MIGs work

A MIG is considered stateful if you have created a [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration).

You [create a stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs) by setting a non-empty stateful policy and/or one or more non-empty per-instance configurations:

  * A [stateful policy](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_policy) defines items that you want to preserve for all instances in your MIG.
  * A [per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs) defines items to preserve for a specific VM instance.



The configuration is effective after you or the MIG [applies](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_stateful_configuration_to_managed_instances) it:

  * A MIG automatically applies your stateful policy configuration to new and existing instances.
  * When creating or updating per-instance configurations, you can choose whether to apply the new configuration manually or have it applied automatically.



After the stateful configuration (stateful policy and/or per-instance configurations) is applied, you can [verify](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#viewing_the_preserved_states_of_managed_instances) it by inspecting the preserved state of each managed instance.

Subsequent changes to your MIG's stateful configuration or size (for example, decreasing the MIG's size, or deleting or abandoning instances from the MIG) can [affect the preserved states](https://docs.cloud.google.com/compute/docs/instance-groups/preserved-state) of the instances.

## How stateful configuration is applied to managed instances

Your stateful configuration is effective after you or the MIG applies it. Applying stateful configuration to a MIG's instances depends on the configuration:

  * Stateful policy: The MIG automatically applies your stateful policy configuration to new and existing instances.
  * Per-instance configurations: When creating or updating per-instance configurations, you can choose whether to apply the new configuration manually or have it applied automatically.



![Applying stateful configuration to managed instances.](https://docs.cloud.google.com/static/compute/images/mig-stateful-applying-config.png)

### How stateful policy updates are applied to instances

When you create or update a [stateful policy](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_policy), for example add or remove a stateful disk, the MIG applies your stateful policy configuration to all managed instances in the group automatically and asynchronously. A MIG also automatically applies your stateful policy configuration to new instances during their creation, for example, when a MIG's size is increased or when you create instances in the MIG manually.

After the configuration is applied, you can see the effect of the update in each managed instance's [preserved state from policy](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#viewing_the_preserved_states_of_managed_instances).

Updates to a stateful policy do not disrupt running VMs.

When you update a stateful policy to add a stateful disk, the MIG updates each VM [resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances), changing the value of the disk's `autoDelete` flag (`instances.disks[].autoDelete`):

  * The MIG sets `autoDelete` to `FALSE` for disks that you configure as stateful. This prevents deletion of that disk on instance recreation by autohealing, updating, or manual recreation.
  * The MIG sets `autoDelete` to match your instance template [configuration](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates) (`instanceTemplates.disks[].autoDelete`) for all disks that are to be stateless.



Changing the value of the `autoDelete` flag does not disrupt a running VM.

### How per-instance configuration updates are applied to instances

When you create or update a per-instance configuration, you can choose whether to apply the new configuration manually or automatically. For more information, see [Applying stateful configuration from per-instance configurations](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs).

The following table shows the [disruption levels](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig#disruption_levels) that are required to apply different per-instance configuration updates to a VM:

**Per-instance configuration update** | **Disruption to VM required for applying**  
---|---  
Configure a disk, defined by the instance template, to be stateful (added to the per-instance configuration) | REFRESH  
Configure a disk, defined by the instance template, to be stateless (removed from the per-instance configuration) | REFRESH  
Add a disk, not defined by the instance template, and attach it to the VM | REFRESH  
Remove a disk, not defined by the instance template, and detach it from the VM | REFRESH  
Add a metadata key-value pair | REFRESH  
Remove a metadata key-value pair | REFRESH  
Add an external boot disk, not created from the instance template, and attach it to the VM | REPLACE  
Remove an external boot disk, not created from the instance template, detach it from the VM, and create a boot disk from the instance template instead  | REPLACE  
Set an internal IP address | REPLACE  
Remove an internal IP address | REPLACE  
  
When applying an updated per-instance configuration to the corresponding VM, the MIG performs the following actions depending on which stateful items are updated:

  * Adds (or removes) disks, IP addresses, or metadata to the preserved state from configuration in the corresponding managed instance.
  * Attaches (or detaches) disks that are not defined by the instance template to the VM.
  * Sets (or removes) metadata key-value pairs that are specific for the VM.
  * Assigns (or removes) specified IP addresses to the VM instance.



After a per-instance configuration is applied to a corresponding managed VM, you can see the effect of the update in the instance's preserved state from configuration.

## Preserved state of a managed instance

When it is applied, the MIG translates your instance template and [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration) into a "preserved state" for each [managed instance](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance).

You can [view the preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#viewing_the_preserved_states_of_managed_instances) by inspecting a managed instance.

The MIG maintains these preserved states automatically, and the MIG automatically and asynchronously applies this state to each corresponding actual VM instance in the MIG.

![Preserved state of managed VMs that are generated by applying stateful configuration.](https://docs.cloud.google.com/static/compute/images/mig-stateful-preserved-state-overview.png)

The preserved state describes which individual items (persistent disks, IP addresses, metadata) are stateful for a given instance:

![Preserved state generated from applied stateful configuration.](https://docs.cloud.google.com/static/compute/images/mig-stateful-preserved-state-example.png)

The preserved state generated based on a stateful policy is stored separately from the preserved state generated based on a per-instance configuration. The MIG combines both of them when recreating a VM, with the preserved state from a per-instance configuration taking priority.

### Preserved state according to stateful policy

A stateful policy specifies items, present in all instances and defined in the MIG's instance template, to preserve individually for each VM instance in a MIG.

When applied, the MIG translates the stateful policy into instance-specific preserved states (`managedInstances[].preservedStateFromPolicy`). The MIG maintains these preserved states automatically.

The following example shows a MIG with two VM instances that use a stateful disk defined in a stateful policy that applies to every instance. There are no per-instance configurations in this example.

![Preserved state generated from stateful policy only.](https://docs.cloud.google.com/static/compute/images/mig-stateful-preserved-state-from-policy.png)

The preceding figure shows a MIG with two instances:

  * The instance template defines a boot disk with device name, `boot-disk`, and a disk with device name, **`data-disk`** , for all instances in the MIG.
  * The stateful policy declares **`data-disk`** as stateful. The boot disk remains stateless. Note that the disk with device name, **`data-disk`** , must be and is defined by the instance template.
  * After the configuration is applied, the MIG translates the stateful policy into instance-specific preserved states for each managed instance. The preserved states instruct the MIG to preserve the disk **`data-disk-1`** for VM instance `node-1` and the disk **`data-disk-2`** for the instance `node-2`, because both of these disks have device name **`data-disk`** configured in the stateful policy.
  * This example has no per-instance configurations.



### Preserved state according to per-instance configuration

A per-instance configuration specifies items that must be preserved for a particular VM. These items don't have to be defined in the MIG's instance template.

When applied, the MIG translates each per-instance configuration into a preserved state (`preservedStateFromConfig`) for the corresponding instance.

The following example shows a MIG with two VM instances for which stateful metadata and disks are defined in per-instance configurations (PICs) for every instance. There is no stateful policy in this example.

![Preserved state generated from PICs only.](https://docs.cloud.google.com/static/compute/images/mig-stateful-preserved-state-from-pic.png)

In the preceding figure:

  * The instance template defines a boot disk with device name `boot-disk` for all instances in the MIG. The boot disk is stateless for all VMs in the MIG.
  * Per-instance configurations define the states to preserve for two instances in the MIG: `node-1` and `node-2`. 
    * For the `node-1` instance, the per-instance configuration defines a disk **`my-legacy-1`** with device name **`legacy-disk`** and metadata **`node-id:xyz273`**.
    * For the `node-2` instance, the per-instance configuration defines a disk **`my-logs-1`** with device name **`logs-disk`** and metadata **`node-id:pqr851`**.
  * After the configuration is applied, the MIG automatically translates the per-instance configurations into preserved states for each managed instance. The preserved states instruct the MIG to attach and preserve the following: 
    * Persistent disk **`my-legacy-1`** and metadata **`node-id:xyz273`** for VM `node-1`
    * Persistent disk **`my-logs-1`** and metadata **`node-id:pqr851`** for VM `node-2`
  * This example has no stateful policy.



Note that the disks and metadata in the preserved state from per-instance configurations are not defined by the instance template in this example; instead, they are defined by the per-instance configurations only. This is because the configuration that you specify in a per-instance configuration is specific for a particular VM, which means it does not have to be present in the instance template.

### Per-instance configurations have priority over stateful policy and instance template

You can configure both a stateful policy and one or more per-instance configurations in one MIG. For example, in a stateful policy, you can define stateful disks that are present in all instances, and in per-instance configurations, you can define instance-specific metadata.

A managed instance's per-instance configuration takes priority over conflicting configuration in the instance template or in a stateful policy.

If you apply a per-instance configuration to add a disk or a network interface that is already defined in a stateful policy, the MIG stores the stateful configuration for that disk or network interface in the managed instance's preserved state from per-instance configuration (`preservedStateFromConfig`) and removes the conflicting entries from its preserved state from policy (preservedStateFromPolicy). The MIG must [refresh](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig#disruption_levels) the VM if the new preserved state is different from the previous one. The refresh could result in metadata change, external IP address change, or a disk swap to detach the disk from the last preserved state configuration and attach the disk specified in the new preserved state configuration.

In the following example, the per-instance configuration for VM instance `node-1` redefines:

  * The preserved state for the disk with device name **`logs-disk`** , originally defined in the stateful policy
  * The value for metadata key **`logmonth`** , originally defined in the instance template.



![Configuration from per-instance configurations takes priority over stateful policy and instance template.](https://docs.cloud.google.com/static/compute/images/mig-stateful-pic-priority.png)

In the preceding figure:

  * The instance template defines: 
    * Three disks for all instances in the MIG, with device names `boot-disk`, `data-disk`, **`logs-disk`**.
    * Metadata common to all instances: **`logmonth:jan`**.
  * The stateful policy declares that disks with device names `data-disk` and **`logs-disk`** are stateful; the boot disk remains stateless.
  * A per-instance configuration for the instance `node-1` redefines: 
    * Stateful configuration for a disk with device name **`logs-disk`** : This instructs the MIG to attach the disk **`pd-logs-feb`** to `node-1` under the **`logs-disk`** device name.
    * Metadata, defined in the instance template, with key value **`logmonth:jan`** : This instructs the MIG to set value **`logmonth:feb`** to `node-1`.
  * After you [apply](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs), the configuration, the MIG automatically translates the stateful policy and per-instance configuration into an instance-specific preserved state, stored in the managed instance. 
    * The preserved state from policy instructs the MIG to preserve the disk `data-disk-1` for the VM `node-1`. Note that the preserved state from policy does not include stateful configuration for the disk with device name **`logs-disk`** because this configuration is overridden by the configuration for **`logs-disk`** in the per-instance configuration.
    * The preserved state from configuration instructs the MIG to attach and preserve persistent disk **`logs-disk`** and to set and preserve metadata **`logmonth:feb`** for VM instance `node-1`. Note that the preserved state from configuration overrides the configuration for **`logs-disk`** from the stateful policy and overrides metadata **`logmonth:jan`** from the instance template.



## How removing a resource from a stateful policy affects preserved state

If you remove a resource configuration from your stateful policy, the MIG automatically removes the corresponding `preservedStateFromPolicy` for all managed instances. The compute resources remain attached to the instances, but they are no longer stateful.

In the following example, removing a disk from the stateful policy leads to removal of that disk from preserved states from policy in all managed VMs. Those disks remain attached to their VMs, but they are no longer stateful and might be deleted and recreated on next VM recreation.

![Removing a disk from a stateful policy.](https://docs.cloud.google.com/static/compute/images/mig-removing-disk-from-stateful-policy-1.png)

If the same item, for example, a stateful persistent disk, is present both in the stateful policy and a per-instance configuration, and you remove its stateful configuration from the stateful policy only, the MIG doesn't remove it from the per-instance configuration. For the corresponding VM, the configured resource remains stateful.

In the following example, removing the disk from the stateful policy does not lead to removal of the disk from the per instance configuration. The disk remains stateful because it is still a part of preserved state from configuration.

![Removing a disk from a stateful policy when a per-instance configuration also exists.](https://docs.cloud.google.com/static/compute/images/mig-removing-disk-from-stateful-policy-2.png)

## How removing items from per-instance configurations affects preserved state

If you remove the stateful configuration from a per-instance configuration, and apply the change, the MIG automatically removes the stateful configuration from the preserved state from configuration (`preservedStateFromConfig`) in the corresponding managed instance. The compute resources that are no longer part of any preserved state become stateless.

### How removing stateful disks configuration from per-instance configurations affects preserved state

If you remove a stateful disk from a per-instance configuration and apply the change to the associated VM instance, the MIG does the following:

  * The disk configuration is removed from the instance's preserved state from configuration.
  * If a disk with the same device name is defined in the instance template but not configured in a stateful policy, then the disk stays attached to the given VM. However, the disk becomes stateless for the given VM and it might be recreated according to the instance template configuration on the next VM recreation, autohealing, or update event.
  * If a disk with the same device name is not defined in the instance template, then it is automatically detached from the VM immediately upon application of the updated per-instance configuration to the associated VM, regardless of its auto-delete configuration.
  * If a disk with the same device name is configured in a stateful policy, then its stateful policy configuration is translated into the preserved state from policy for the given managed instance, and the disk remains stateful.



In the following example, removing a blue and a green disk from `node-1`'s per-instance configuration leads to removal of both disks from the `node-1` managed instance's preserved state from configuration.

  * The blue disk remains attached to the `node-1` VM instance, but it is now stateless and can be recreated on the next VM recreation according to the instance template configuration.
  * The green disk is detached from the `node-1` VM instance because the instance template does not define a disk with the same device name.



![Removing disks from a per-instance configuration.](https://docs.cloud.google.com/static/compute/images/mig-removing-disks-from-per-instance-config.png)

### How removing stateful metadata from per-instance configurations affects preserved state

Removing stateful metadata from a per-instance configuration and applying the change causes the MIG to immediately remove that stateful metadata from the corresponding managed instance's preserved state:

  * If you defined metadata with the same key in the instance template, the MIG immediately applies the value from the instance template to the instance.
  * If the metadata with the same key is not defined in the instance template, the MIG immediately removes the key value from the instance.



In the following example, removing **`mode:dev`** and **`id:xyz273`** metadata from `node-1`'s per-instance configuration leads to automatic removal of both key-value pairs from the `node-1` managed instance's preserved state from configuration.

  * **`mode:dev`** is replaced by the instance template's **`mode:test`** in the VM.
  * **`id:xyz273`** is removed from the VM immediately because the instance template does not have metadata with the same key **`id`** to replace it with.



![Removing metadata from a per-instance configuration.](https://docs.cloud.google.com/static/compute/images/mig-removing-metadata-from-per-instance-config.png)

### How removing stateful IP configuration from per-instance configurations affects preserved state

Removing the internal IP configuration from per-instance configuration makes the IP address for this VM stateless. No automated changes are performed on this VM, but the IP address can change after the VM is recreated, updated, or autohealed.

### Fallback to stateful policy

If you remove the stateful configuration of a resource from a per-instance configuration, and you configured the same resource in the stateful policy, then the resource remains stateful according to the stateful policy.

The MIG automatically removes the item's stateful configuration from the `preservedStateFromConfig` and adds it to the `preservedStateFromPolicy` for the corresponding managed instance.

In the following example, removing a disk from `node-1`'s per-instance configuration does not lead to removal of the disk from the stateful policy. The disk remains stateful according to the stateful policy:

  * The MIG automatically removes the disk from the `preserveStateFromConfig` for the `node-1` managed instance because the disk is no longer part of its per-instance configuration.
  * The MIG automatically adds the disk to the `preserveStateFromPolicy` for the `node-1` managed instance because the stateful policy configuration is still in place and is no longer in conflict with the `node-1` per-instance configuration.



![Removing a disk from a per-instance configuration but not from stateful policy.](https://docs.cloud.google.com/static/compute/images/mig-removing-disk-from-pic-applies-stateful-policy.png)

## Feedback

We want to learn about your use cases, challenges, and feedback about stateful MIGs. Please share your feedback with our team at [mig-discuss@google.com](mailto:mig-discuss@google.com).

## What's next

  * Learn [how different configurations and MIG actions affect preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/preserved-state).
  * For information about how to support stateful workloads by preserving instance names, persistent disks, and metadata in managed instances, see [Configuring stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs).
  * Learn more about [when to use stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#when_to_use_stateful_migs).
  * Learn how to [Migrate an existing workload to a stateful MIG](https://docs.cloud.google.com/compute/docs/tutorials/migrate-workload-to-stateful-mig).
  * Learn more about [MIGs](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).
  * Work with [managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
