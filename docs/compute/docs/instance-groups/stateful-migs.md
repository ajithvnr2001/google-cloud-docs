---
url: https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs/
title: Stateful managed instance groups \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:29:24.051717+00:00
---

# Stateful managed instance groups  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Stateful managed instance groups Stay organized with collections  Save and categorize content based on your preferences. 

You can build highly available deployments of stateful workloads on VM instances using stateful [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) (stateful MIGs). Stateful workloads include applications with stateful data or configurations such as databases, legacy monolith applications, and long-running batch computations with checkpointing.

With stateful MIGs, you can improve the uptime and resiliency of such stateful applications with autohealing (automatic recovery of failed workloads), multi-zone deployments, and [automated rolling updates](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).

A stateful managed instance group preserves the unique state of each instance (including instance name, attached persistent disks, IP addresses, and metadata) on VM restart, recreation, autohealing, or update.

This page describes when to use stateful MIGs and provides a high-level overview of how they work. For more information, see [How stateful MIGs work](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work).

To learn how to set up a stateful MIG, see [Configuring stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs).

## How stateful workloads are different from stateless workloads

You can use managed instance groups to support both stateful and stateless workloads. The key difference between stateful and stateless workloads is that stateful workloads preserve individual VM state (for example, a database shard, or app configuration) on the VM's disks, while stateless workloads, like a web frontend, don't retain any state on the individual VMs.

You treat VMs with stateful workloads like custom-built machinery: you care about VM identity (name), IP address, metadata, and data on each individual machine. You cannot easily scale stateful workloads horizontally because scaling could require data replication, creation or deletion of data shards, or changing the overall application configuration. When recreating or updating a machine with a stateful workload, you must preserve the VM's unique state. Examples of stateful applications include Cassandra, ElasticSearch, mongoDB, MySQL, PostgreSQL, and Kafka.

You treat VMs with stateless workloads as interchangeable and only care about the number of serving VMs that you have. No one VM is treated any differently than another. You can quickly scale stateless workloads horizontally by adding or removing VMs. When updating your application, you can delete machines and replace them with new ones with different names, IP addresses, metadata, and disks. When a stateless VM is deleted or recreated, all data on the machine is lost: the disks are deleted or recreated from scratch. A web frontend is an example of a stateless application.

| Stateful MIG| Stateless MIG  
---|---|---  
Workload | Stateful workloads where disks, IP addresses, and/or metadata are preserved on VM recreate operations. | Highly available and scalable stateless workloads, where disks and IP addresses are recreated from scratch on horizontal scaling, autohealing, auto-updating, and VM recreation.  
MIG features | 

  * Autohealing
  * Automated rolling updates
  * Multi-zone deployments

| 

  * Autohealing
  * Automated rolling updates
  * Multi-zone deployments
  * Autoscaling

  
Preservable items | 

  * Instance names
  * Persistent disks, including support for disks that are not defined in the instance template
  * Instance-specific metadata
  * IP addresses

| Instance names  
  
All MIGs support custom and preservable instance names.

## When to use stateful MIGs

Consider using stateful managed instance groups (stateful MIGs) whenever you deploy a stateful application or cluster to Compute Engine and would like to improve its availability with [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) and [multi-zone deployments](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups), or you want to simplify updates of stateful instances by [orchestrating update rollouts](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs) and controlling the allowed level of disruption to the instances.

Stateful MIGs are intended for applications with stateful data or configuration, such as:

  * **Databases**. For example: Cassandra, ElasticSearch, mongoDB, and ZooKeeper. Before deciding on stateful MIGs, consider using fully managed services, for example, MySQL and PostgreSQL are available in [Cloud SQL](https://docs.cloud.google.com/sql), to focus on your applications and not have to deal with VMs.
  * **Data processing** applications. For example: Kafka and Flink. Before deciding on stateful MIGs, consider using fully managed services, for example, [Dataflow](https://docs.cloud.google.com/dataflow) or [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc), to focus on your data processing tasks and not have to deal with VMs.
  * **Other stateful** applications. For example: TeamCity, Jenkins, Bamboo, DNS servers with stateful IP address, and custom stateful workloads.
  * **Legacy monolith** applications. These applications store application state on a boot disk or additional persistent disks, or they rely on stateful configuration, such as specific VM instance names, IP addresses, or metadata key values.
  * **Batch workloads with checkpointing**. With this configuration, you can preserve checkpointed results of long-running computation in anticipation of workload or VM failure or instance preemption. Stateful MIGs can recreate a failed machine, while preserving its data disk, so that your computation can continue from the last checkpoint.



To achieve resilience against zonal failure, your application must replicate data across multiple instances at the application level. For example, ElasticSearch and Cassandra support such functionality. You can use a regional MIG to make such an application resilient to zonal failure by deploying redundant replicas to multiple zones and relying on your application's data replication functionality. In the event of a zonal failure, your data is served from available replicas in the remaining zones.

Review the [limitations](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs#limitations) to verify if a stateful MIG fully meets your requirements.

**Note:** Your workload must start automatically on VM boot so that it can continue serving or computing after autohealing, auto-updating, and instance recreation events.

## What makes a MIG stateful

A MIG is considered stateful if you have created a stateful configuration.

You can create a stateful configuration when you create your MIG, or you can convert a group from stateless to stateful after its creation by adding a configuration.

You create a stateful configuration by setting a non-empty stateful policy or one or more non-empty per-instance configurations:

  * A _stateful policy_ defines items that you want to preserve for all instances in your MIG.
  * A _per-instance configuration_ defines items to preserve for a specific VM instance.



The configuration is effective after you or the MIG applies it:

  * A MIG automatically applies your stateful policy configuration to new and existing instances.
  * When creating or updating per-instance configurations, you can choose whether to apply the new configuration manually or have it applied automatically.



After the stateful configuration (stateful policy or per-instance configurations) is applied, you can verify it by inspecting the preserved state of each managed instance.

Subsequent changes to your MIG's stateful configuration or size (for example, decreasing the MIG's size, or deleting or abandoning instances from the MIG) can [affect the preserved states](https://docs.cloud.google.com/compute/docs/instance-groups/preserved-state) of the instances.

## Stateful configuration

A stateful managed instance group (MIG) takes its instance configuration from a combination of the [instance template](https://docs.cloud.google.com/compute/docs/instance-templates), optional [all-instances configuration](https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic), optional stateful policy, and optional per-instance configurations that you set. After you set the configuration for your group, the MIG uses that configuration when creating VMs. To apply an updated configuration to existing VMs, see [Apply new VM configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).

**Note:** If you only need to preserve VM instance names, you don't need to configure a stateful policy or per-instance configurations: 

  * MIGs preserve instance names on recreation and on autohealing by default.
  * For proactive rolling updates to preserve instance names, you must set the Updater [ replacement method](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#replacement_method) to `RECREATE`. 



### Stateful policy

A stateful policy defines common stateful items for all instances in a managed instance group. Each item that you include in the stateful policy must be defined in the MIG's instance template.

You can make the following changes to a stateful policy:

  * Configure disks to become stateful by [adding them](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs#configuring_stateful_persistent_disks_for_all_vms_in_a_mig) to the stateful policy.
  * Configure disks to become stateless by [removing them](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs#removing_stateful_persistent_disks_from_a_mig) from the stateful policy.
  * Specify that IP addresses must be stateful by [adding](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs#configuring_stateful_ip_addresses_for_all_vms_in_a_group) network interface configuration to the stateful policy.
  * Specify that IP addresses must be treated as stateless by [removing](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs#declaring_previously_stateful_ip_addresses_as_stateless) the configuration from stateful policy.



### Per-instance configurations

A per-instance configuration defines stateful items that are unique for a specific [managed instance](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance), such as instance-specific disks, metadata key-value pairs, and IP addresses. Instance-specific metadata and disks don't need to be defined in the MIG's instance template; however, network interfaces for stateful IPs must be defined in the MIG's instance template.

You can make the following changes to a per-instance configuration for a specific instance in a MIG:

  * [Configure disks](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs#configuring_stateful_persistent_disks_individually_for_a_vm_in_a_mig) that are defined in the instance template to become stateful for the instance (by adding those disks to the per-instance configuration) or to become stateless (by removing those disks from the per-instance configuration).
  * [Configure existing disks](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs#adding_existing_stateful_disks_to_new_vms_in_a_mig), not defined in the instance template, to be attached and become stateful for the instance (by adding those disks to the per-instance configuration) or to be detached from the instance (removing disks from the per-instance configuration).
  * [Add or remove](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-metadata-in-migs#setting_modifying_and_removing_stateful_metadata_individually_for_existing_vm_instances) stateful metadata key-value pairs that are specific to the instance.
  * [Configuring IP addresses](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs#configuring_stateful_ip_addresses_individually_for_vms_in_a_mig) individually for instances in a MIG to become stateful or stateless. Per-instance configurations for IP addresses are not supported for Dynamic Network Interfaces.



### Example of stateful configuration

Here is an example of a stateful configuration:

![Instance template + stateful policy + per-instance configuration = managed instance config.](https://docs.cloud.google.com/static/compute/images/mig-stateful-config-example.png)

In this chart:

  * The instance template defines a common configuration for all VM instances in a MIG
  * The stateful policy defines a common stateful configuration for disks with device name, `data-disk`, which are defined by the instance template, and which are created and attached individually to each VM instance in the MIG.
  * The per-instance configuration defines a stateful configuration for a specific VM instance named, `node-1`. It specifies to attach an existing disk, `my-legacy-1`, to the `node-1` instance and treat it as stateful. It also specifies one metadata key value to preserve individuality for the `node-1` instance: `node-id:xyz273`.



When creating the `node-1` VM, the MIG does the following:

  1. Uses the `n2-standard-2` machine type, according to the instance template.
  2. Creates and attaches a boot disk with an auto-generated disk name, `boot-node-1`, and device name `boot-disk`, using a Debian GNU/Linux image, according to the instance template. The MIG treats the `boot-node-1` boot disk as stateless because it isn't configured in the stateful policy or in the per-instance configuration.
  3. Creates and attaches an additional disk with an auto-generated disk name, `data-disk-1`, and device name, `data-disk`, using a custom image, according to the instance template. The MIG treats the `data-disk-1` additional disk as stateful because its device name is specified in the stateful policy.
  4. Attaches an existing disk with the disk name, `my-legacy-1`, and uses device name, `legacy-disk`, according to the per-instance configuration. The MIG treats the `my-legacy-1` additional disk as stateful because its device name is specified in the per-instance configuration.
  5. Sets three metadata key-value pairs: two from the instance template (`app:example-stateful-app`, `version:1.0`) and one from the per-instance config (`node-id:xyz273`). The MIG treats the `node-id:xyz273` key-value pair as stateful because it is specified in the per-instance configuration.



When recreating the `node-1` VM, assuming the same config is still effective, the MIG recreates the stateless items and preserves the stateful items:

  1. Recreates the boot disk from the original image:

First, it deletes the `boot-node-1` boot disk, and then it recreates it from the Debian GNU/Linux image, as specified in the instance template.

  2. Preserves additional disks, `data-disk-1` and `my-legacy-1`:

Detaches the additional disks before deleting the VM, and then attaches them to the VM after it has been recreated.

  3. Preserves the individual metadata key-value pair, `node-id:xyz273`:

Sets the metadata after the VM has been recreated. Also sets the common key-value pairs from the instance template (`app:example-stateful-app` and `version:1.0`).




## Feedback

We want to learn about your use cases, challenges, and feedback about stateful MIGs. We invite you to share your feedback with our team at [mig-discuss@google.com](mailto:mig-discuss@google.com).

## What's next

  * Read [Configuring stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs) to learn how to support stateful workloads by preserving instance names, persistent disks, and metadata in managed instances.
  * Learn how to [Migrate an existing workload to a stateful MIG](https://docs.cloud.google.com/compute/docs/tutorials/migrate-workload-to-stateful-mig).
  * Learn more about [How stateful MIGs work](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work).
  * Learn more about [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).
  * Read about [Working with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
