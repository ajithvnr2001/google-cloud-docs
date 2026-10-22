---
url: https://docs.cloud.google.com/compute/docs/instance-groups/about-repair/
title: About repairing VMs for high availability \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:03.774208+00:00
---

# About repairing VMs for high availability  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/about-repair/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About repairing VMs for high availability Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how a managed instance group (MIG) provides high availability of your application by repairing failed and unhealthy VMs in the group.

A MIG keeps your application up and available by proactively maintaining the number of running VMs in the group. If a VM in the group goes down, the MIG _repairs_ the VM by recreating it in the following ways to bring the VM back to service:

  * **Automatically repair a failed VM** : If a VM fails or is deleted by an action not initiated by the MIG, then the MIG automatically repairs the failed VM. In this document, see Automatically repair a failed VM.
  * **Repair a VM based on an application health check** : An optional way to further improve high availability by repairing _unhealthy_ VMs. If you configure an application-based health check and your application fails the health check, then the MIG marks that VM as unhealthy and repairs it. Repairing a VM based on an application health check is also called _autohealing_. In this document, see Repair a VM based on an application health check.



## Automatically repair a failed VM

If a VM in a MIG fails, the MIG automatically repairs the failed VM by recreating it. A VM can fail due to the following reasons:

  * Unexpected reasons like a hardware failure.
  * Actions not initiated by the MIG, such as the following: 
    * Preemption of a [Spot VM](https://docs.cloud.google.com/compute/docs/instances/spot#spot-with-instance-groups).
    * Infrastructure [maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) when the VM instance is not set to live migrate.
    * Actions performed directly on a VM using the [VM instances console page](https://console.cloud.google.com/compute/instances), [`instances` gcloud CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/compute), or [`instances` API resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances). For example, stopping a VM in the group using the `instances.stop` method or the `gcloud compute instances stop` command triggers repairing.



If the MIG intentionally stops a VM—for example, when an [autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler) deletes a VM—then the MIG doesn't repair that VM.

**Note:** To make sure that the MIG doesn't revert your configuration changes, you must manage the MIG by using the [instance groups console page](https://console.cloud.google.com/compute/instanceGroups), the [`instance-groups managed` gcloud CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed), and the [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers) instance group manager API resources.

## Repair a VM based on an application health check

In addition to the automatic repair of failed VMs, you might want to repair a VM if an application that you're running on the VM freezes, crashes, or runs out of memory. To make sure that the application is responding as expected, you can configure an application-based health check.

An application-based health check periodically verifies that the applications that you're running on each VM in a MIG are responding as expected. If the application on a VM doesn't respond, then the MIG marks that VM as unhealthy. The MIG then repairs the unhealthy VM. Repairing a VM based on an application health check is called autohealing.

To make sure that the MIG keeps running a subset of its VMs, the group never concurrently autoheals all of its VMs. This approach helps to prevent issues such as an incorrect health check triggering unnecessary repairs, a misconfigured firewall rule preventing a health check from probing the VM, or network connectivity or infrastructure issues that cause a healthy VM to be wrongly identified as unhealthy. However, if a zonal MIG has only one VM, or a regional MIG has only one VM per zone, a MIG autoheals these VMs when they become unhealthy.

### Autohealing policy

Each MIG has an autohealing policy in which you can configure a health check and also set an initial delay. The initial delay is the time that a new VM takes to initialize and run its startup script. The initial delay timer starts when the MIG changes the VM's [`currentAction`](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#current_actions_on_instances) field to `VERIFYING`. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This approach prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready.

For more information about configuring an autohealing policy, see [Set up an application health check and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).

### Monitor application health state changes

If you've configured an application-based health check in your MIG, you can check the health state of each VM in the MIG. For more information, see [Check whether VMs are healthy](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#checking_whether_instances_are_healthy).

You can also monitor the changes in the health state of a VM. For more information, see [Monitor health state changes](https://docs.cloud.google.com/compute/docs/instance-groups/monitoring-managed-instance-health-state-changes).

### Pricing

When you set up an application-based health check, by default Compute Engine writes a log entry whenever a managed instance's health state changes. Cloud Logging provides a [free allotment per month](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary) after which logging is priced by data volume. To avoid costs, you can [disable](https://docs.cloud.google.com/compute/docs/instance-groups/disabling-and-enabling-health-state-change-logs#disabling_health_state_change_logs) the health state change logs. 

## Behavior during a repair

The following sections explain the behavior during automatic repairs and repairs based on application health check.

### Update on repair

By default, during a repair, a MIG recreates a VM using the original instance template that was used to create the VM. For example, if a VM was created using `instance-template-a` and then you update the MIG to use `instance-template-b` in [`OPPORTUNISTIC`](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#choosing_between_automated_and_selective_updates) mode, the MIG still uses `instance-template-a` to recreate the VM.

If you want your MIG to use the latest instance template and [per-instance configurations](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs) during VM repair, you can configure the group to [apply configuration updates during repairs](https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair) by enabling _update on repair_.

If your MIG uses [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility), enabling update on repair lets the MIG check availability across your alternative machine types while it continues attempting to repair a failed VM using its original machine type. During this repair process, if the original machine type is unavailable, Compute Engine logs a `ZONE_RESOURCE_POOL_EXHAUSTED` stockout error in Cloud Logging. For more information, see [Instance flexibility and VM repairs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility#instance_flexibility_and_vm_repairs).

### Repair a VM in an alternate zone

By default, a regional MIG repairs a failed or an unhealthy VM by recreating the VM in its original zone. You can configure a regional MIG to repair VMs in any of the MIG's [selected zones](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones). When the MIG cannot repair the VM in the original zone, then the MIG selects an alternate zone based on available capacity and quota, and recreates the VM in that zone.

When a MIG repairs a VM in a zone different from its original zone, then the URL of the VM changes because the URL contains the zone—for example, `projects/example-project/zones/us-central1-b/instances/example-mig-0289gx`.

Repairing a VM in an alternate zone has the following benefits:

  * Makes your application more resilient to zonal failures.

  * Improves resource obtainability, particularly for high-demand hardware like GPUs, VMs with large number of cores or memory, or Spot VMs.




For more information, see [Repair a VM in an alternate zone](https://docs.cloud.google.com/compute/docs/instance-groups/repair-vm-in-alternate-zone).

### Disk handling

During a repair, when recreating a VM based on its template, the MIG handles different types of disks differently. Some disk configurations can cause a repair to fail when attempting to recreate a VM.

Disk type | `autodelete` | Behavior during a repair  
---|---|---  
New persistent disk | `true` | Disk is recreated as specified in the instance template. Any data that was written to that disk is lost when the disk and its VM are recreated.  
New persistent disk | `false` | Disk is preserved and reattached when MIG recreates the VM.  
Existing persistent disk | `true` | Old disk is deleted. VM recreate operation fails because Compute Engine cannot reattach a deleted disk to the VM. However, for existing read/write disks, a MIG can have only up to one VM because a single persistent disk cannot be attached to multiple VMs in read/write mode.  
Existing persistent disk | `false` | Old disk is reattached as specified in the instance template. The data on the disk is preserved. However, for existing read/write disks, a MIG can have only up to one VM because a single persistent disk cannot be attached to multiple VMs in read/write mode.  
New local SSD | N/A | Disk is recreated as specified in the instance template. The data on a local SSD is lost when a VM is recreated or deleted.  
  
The MIG does not reattach disks that are not specified in the instance template or per-instance configurations, such as disks that you attached to a VM manually after the VM was created.

To preserve important data that was written to disk, take precautions, such as the following:

  * Take regular persistent disk [snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).
  * Export data to another source, such as Cloud Storage.
  * Configure [stateful persistent disks](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs).



If your VMs have important settings that you want to preserve, Google also recommends that you use a [custom image](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#use_custom_or_public_images_in_your_instance_templates) in your instance template. A custom image contains any custom settings that you need. When you specify a custom image in your instance template, the MIG recreates VMs using the custom image that contains the custom settings you need.

## Turn off repairs

You can turn off repairs that are automatically done by a MIG. When you turn off repairs in a MIG, repairing of failed VMs and repairing based on an application health check are turned off. You can also separately turn off repairs based on an application health check.

You might want to turn off repairs in a MIG in scenarios such as the following:

  * To investigate or debug a failed VM without interruption from automatic repair.
  * To repair VMs manually or implement your own repair logic.
  * To prevent recreating VMs while a batch job is in progress.
  * To observe application health states without repairing an unhealthy VM.
  * To fine-tune health check configuration without inadvertently triggering repairs.



When you turn off repairs, the MIG doesn't take any action if a VM in the group fails or becomes unhealthy. Failed and unhealthy VMs continue to be in the group and the target number of running VMs in the MIG (`targetSize`) remains the same. However, if you've set a [time limit for the VMs](https://docs.cloud.google.com/compute/docs/instance-groups/limit-vm-runtime-in-migs#limit_the_run_time_of_vms_in_a_mig), then when the failed and unhealthy VMs reach that time limit, the MIG automatically deletes those VMs and the `targetSize` decreases.

If the MIG's [update type](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#type) is set to `proactive` and a new instance template is available, then the MIG updates the failed and unhealthy VMs by recreating those VMs using the new template. If you don't want to update the failed and unhealthy VMs, you must set the update type to `opportunistic`.

If you've configured an application-based health check, turning off repairs doesn't affect the functioning of the health check. The health check continues to probe the application and provide the VM health states. This setting lets you monitor application health states while preventing the MIG from repairing unhealthy VMs.

If the MIG is part of a backend service of a load balancer and you turn off repairs in the MIG, any unrepaired failed and unhealthy VMs don't respond to the load balancer health check. If the number of these failed or unhealthy VMs in the MIG increases, the load balancer might reduce traffic to that MIG or switch to another backend, if configured. When the failed VMs become available again, the load balancer resumes the traffic to the MIG.

For more information, see [Turn off repairs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig).

## What's next

  * [Configure a regional MIG to allow VM repair in alternate zone](https://docs.cloud.google.com/compute/docs/instance-groups/repair-vm-in-alternate-zone).
  * [Set up an application-based health check and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).
  * [Check the repair configuration in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#check_vm_repairs_turned_off).
  * [Apply configuration updates during repairs](https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
