---
url: https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances/
title: Basic scenarios for creating managed instance groups (MIGs) \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:04.401224+00:00
---

# Basic scenarios for creating managed instance groups (MIGs)  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Basic scenarios for creating managed instance groups (MIGs) Stay organized with collections  Save and categorize content based on your preferences. 

A [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) is a group of virtual machine (VM) instances that you treat as a single entity. Each VM in a MIG is based on an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates).

If you only need to create multiple VMs, but don't want them grouped together in a MIG, see the [bulk instance API](https://docs.cloud.google.com/compute/docs/instances/using-bulk-api).

To learn about other Compute Engine options, see [Choose a Compute Engine deployment strategy for your workload](https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option).

To get started with creating a MIG, read this document to find a basic configuration that works for you.

## Basic scenarios for creating a MIG

MIGs have many configuration options. See the following guides to quickly get a MIG up and running for various scenarios:

Guide | Scenario  
---|---  
[Create a MIG with VMs in a single zone (_zonal MIG_)](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig) | Your VMs can be deployed to a single zone.  
[Create a MIG with VMs in multiple zones in a region (_regional MIG_)](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) | You want to distribute your VMs across multiple zones in a region in order to protect against zonal failure or to automatically find zones with limited resource like [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).  
[Create a MIG with multiple machine types (_instance flexibility_)](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-multiple-machine-types) | Your application is compatible with multiple machine types. You want the MIG to automatically use one of the compatible machine types based on real-time availability.  
[Create a MIG from an existing VM](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-from-vm) | You want to scale out a VM into a group of VMs and deploy them in a single zone or across multiple zones.  
[Create a MIG with autoscaling](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-autoscaling) | You want your MIG to automatically create VMs in the group when demand increases and delete VMs when demand drops.  
[Create a MIG that uses Flex-start VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-flex-start-vms) | Your workload runs for no longer than seven days, and you want to obtain highly demanded resources like GPUs or TPUs at a discounted price.  
[Create a MIG that uses Spot VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-spot-vms) | Your workload can tolerate disruptions and you want to take advantage of the cost-savings associated with Spot VMs.  
[Create a MIG that adds the GPU VMs that you require all at once](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms) | Your workload needs a group of GPU VMs all at once—for example, you want to run batch workloads, such as training machine learning models or high performance computing workloads, on GPU VMs.  
[Create a MIG with stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-stateful-disks) | Your workload needs stateful configuration—for example, you need disks that must retain their data whenever VMs are autohealed, updated, or recreated.  
**Note:** By default, Compute Engine creates–and when necessary recreates–each VM in a MIG based on the configuration that you set in the MIG's instance template. The default behavior for all persistent disks in a MIG is to delete or recreate them when the corresponding VM is deleted or recreated, so you shouldn't rely on attached disks as persistent data. To retain your data in a MIG, you can back up the data in another centralized location, such as Cloud Storage, or add configuration for stateful disks.

## Limitations

MIGs have different limitations depending on which features you use. The following lists show general MIG limitations as well as additional limitations if you use regional or stateful features.

  * By default, you can create up to 1,000 VMs in a zonal MIG. If you need more, use one of the following options:

    * [Increase the size limit](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#increase_the_groups_size_limit) of your MIG.
    * [Create a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups), which allows twice as many VMs as a zonal MIG.
    * Create multiple MIGs and split your workload across them.
    * [Contact support](https://cloud.google.com/support-hub/) to make a request.
  * When updating a MIG, you can specify up to 1,000 VMs in a single request.

  * Once the MIG is created, you cannot change its networks or subnetworks. All VMs in the MIG are assigned to the same subnetworks.

  * Shared VPC on interfaces other than `nic0` for managed instance groups is supported in gcloud CLI and the API, but not in Google Cloud console.




A MIG that is spread across multiple zones—a _regional MIG_ —has the following limitations:

  * By default, you can create up to 2,000 VMs. If you need more, [increase the size limit of your MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#increase_the_groups_size_limit) or [contact support](https://cloud.google.com/support-hub/).
  * You must select which [zones](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) are associated with a regional MIG when you create the MIG. After you choose specific zones during creation, you cannot change or update the zones later. But you can set the MIG's [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape) to specify how the group distributes its managed instances across the zones that you selected.
  * If you set the group's target distribution shape to `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`, review the [target distribution shape limitations](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape#limitations).


  * [Load balancing](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a regional MIG doesn't support the `max-rate` target capacity in `RATE` and `UTILIZATION` balancing modes. To learn more about the usage guidelines for each load balancer, see [Balancing modes and target capacity settings](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode-combos). 



A MIG with [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#what_makes_a_mig_stateful)—a _stateful MIG_ —has the following limitations:

  * You cannot use autoscaling if your MIG has stateful configuration.
  * If you want to use automated rolling updates, you must set the [replacement method](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#replacement_method) to `RECREATE`.
  * For stateful regional MIGs, you must [disable proactive redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution) (set the redistribution type to `NONE`) to prevent deletion of stateful instances by automatic cross-zone redistribution.
  * If you use an [all-instances configuration](https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic) to override instance template properties, you cannot specify those properties in any per-instance configuration and at the same time in the group's all-instances configuration.



If you want to configure an autoscaler for your MIG, review the [autoscaler specifications](https://docs.cloud.google.com/compute/docs/autoscaler#specifications), too.

## IPv6 support

If you want your MIG to include VM instances that use IPv6 addressing, you must use either the IPv6-only or the dual-stack setting when you create your instance template

Including instances with IPv6 addresses in a MIG has the following limitations:

  * While you can use [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair) with dual-stack instances in a MIG, the [health checking endpoint](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) supports only IPv4.
  * When using IPv6-only instances in a MIG, the following features aren't supported: 
    * [Health checking and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair)
    * [Stateful IP addresses](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs)
    * [Target pools](https://docs.cloud.google.com/load-balancing/docs/target-pools)



For more information, see [Create an instance template with IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#template-ipv6).

## Additional MIG tasks

After you've created a MIG, you might want to do the following:

### Learn about the group and its VMs

  * [View info](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs) about your MIG and its managed VM instances
  * [Learn what a managed instance is](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances) and how to work with managed instances



### Resize the group

  * [Add or remove VMs](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig) from the group

    * [Automatically resize a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#autoscaling) based on increases or decreases in load by configuring an autoscaler
    * [Create a resize request in the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_request)
    * [Manually set the size of a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group)
    * [Disable creation retries mode during resize](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#disabling_creation_retries_mode_during_resize)
    * [Create instances with specific names in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs)
    * [Delete specific instances from a group](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group)
    * [Abandon instances from a group](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances)
  * [Increase the group's size limit](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#increase_the_groups_size_limit)

  * [Delete the group](https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig)




### Change the group's VM configuration

  * [Change the instance template for the group](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs)

  * [Apply configuration updates to the VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs)

    * [Automatically apply configuration updates to VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)
    * [Selectively apply configuration updates to specific VMs](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig)
    * [Understand the `instanceTemplate` and `versions` fields](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#relationship_between_versions_and_instancetemplate_fields)

    * [Recreate instances in the group](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#recreate_instances)

    * [Canary test a new instance template in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#canary_updates)

  * [Learn how to add stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) in order to preserve disks, IP addresses, and metadata when VMs are recreated




### Add MIG features

  * [Set up an application-based health check](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) to automatically recreate VMs if your application does not respond as expected
  * [Set up a load balancer](https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer) to distribute user traffic across multiple instances of your application



## Tutorials

Try a tutorial:

  * [Use autohealing for highly available applications](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-autohealing)
  * [Use load balancing for highly available applications](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-load-balancing)
  * [Use autoscaling for highly scalable applications](https://docs.cloud.google.com/compute/docs/tutorials/high-scalability-autoscaling)
  * [Migrate an existing workload to a stateful managed instance group](https://docs.cloud.google.com/compute/docs/tutorials/migrate-workload-to-stateful-mig)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
