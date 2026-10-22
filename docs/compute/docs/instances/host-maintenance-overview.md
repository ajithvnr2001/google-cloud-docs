---
url: https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview/
title: About host events \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:35.272641+00:00
---

# About host events  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About host events Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

During the lifespan of a virtual machine (VM) instance or bare metal instance, the host machine that your instance runs on can experience multiple host events. A host event can include the regular maintenance of Compute Engine infrastructure, or, in rare cases a host error. You can choose how your compute instances respond during or after a host event by configuring the host maintenance policy.

By default, most instances are set to live migrate during host events. For all machine series except Z3, you can override this behavior and explicitly set the instances to terminate and optionally restart. Instances created using certain machine types or configurations don't support live migration, such as the following:

  * H4D instances
  * Z3 instances with more than 18,000 GiB of attached Titanium SSD
  * Z4D and Z4M instances with more than 42,000 GiB of attached Titanium SSD
  * Instances that have a Cloud RDMA network interface
  * [Bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances)
  * Instances with attached GPUs



These instances terminate during host events. For more information, see [Maintenance and restart behaviors](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors).

## Types of host events

There are three types of host events, which are described in more detail in the following sections:

  * Maintenance events
  * Emergent maintenance
  * Host errors



If your instance becomes unresponsive, then this can also trigger a restart or termination of the instance.

### Maintenance events

A _maintenance event_ is when Compute Engine has to perform a maintenance or repair activity that requires VMs to be moved out of the host server. If you enable the **live migration** [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#schedulingoptions) for a supported instance type, then Compute Engine moves the instance to a new host, and there is minimal disruption to your application.

Compute Engine also applies some lightweight hypervisor and network upgrades in the background non-disruptively by retaining the instance on the same host.

Instance behavior during a maintenance event can vary depending on the [tenancy of the instance](https://docs.cloud.google.com/compute/docs/instances/about-vm-tenancy) and the machine type.

For sole-tenant VMs, the approximate frequency of planned host maintenance events is every 4 to 6 weeks. Whether or not live migration is supported depends on the [host maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#host_maintenance_policy) for the sole-tenant VM.

You can find information about the maintenance behavior for each machine type on the respective machine family page, as follows:

  * C series: 
    * C2 and C2D: [Compute-optimized machine family](https://docs.cloud.google.com/compute/docs/compute-optimized-machines)
    * C4N: [Network-optimized machine family](https://docs.cloud.google.com/compute/docs/network-optimized-machines)
    * All other C series: [General-purpose machine family](https://docs.cloud.google.com/compute/docs/general-purpose-machines)
  * E, N, and T series: [General-purpose machine family](https://docs.cloud.google.com/compute/docs/general-purpose-machines)
  * H series: [Compute-optimized machine family](https://docs.cloud.google.com/compute/docs/compute-optimized-machines)
  * M and X series: [Memory-optimized machine family](https://docs.cloud.google.com/compute/docs/memory-optimized-machines)
  * Z series: [Storage-optimized machine family](https://docs.cloud.google.com/compute/docs/storage-optimized-machines)



For accelerator-optimized machine families, see the following pages:

  * GPUs: [Handle GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).
  * TPUs: [Prepare for maintenance events](https://docs.cloud.google.com/tpu/docs/prepare-for-maintenance) in the Cloud TPU documentation.



### Emergent maintenance

An _emergent maintenance_ event occurs when Compute Engine detects an impending host failure or other hardware issue that requires urgent maintenance. For these events, Compute Engine schedules the maintenance event and creates a notification. Emergent maintenance events usually have a shorter notification window than standard maintenance events.

An emergent maintenance event typically provides 7 to 14 days advance notice. Depending on the severity of the issue, the notification window can be shorter. Review the maintenance notification for supported functionality, such as starting the maintenance at a time of your choosing. If no action is taken or if manually starting the maintenance isn't possible, then Compute Engine starts the maintenance automatically when the notification window ends.

**Warning:** If the emergent maintenance event is related to hardware errors, then your instance can't restart on the same host because the host needs to be repaired. Compute Engine restarts the instance on a different, healthy host. Before you start the maintenance, back up any data on Local SSD disks and your instance configuration before you start the maintenance.

If a planned maintenance event is pending when Compute Engine issues an emergent maintenance notification, then the emergent maintenance event replaces the planned maintenance event.

You can check the reason for the emergent maintenance in the `maintenanceReasons` field of the instance metadata. This field contains a value that represents the failure category.

### Host errors

A host error (`compute.instances.hostError`) means that there was a hardware or software issue on the physical machine or the data center infrastructure hosting your compute instance that caused your instance to crash. A host error involving a total hardware failure or other hardware issues might prevent the [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) of your instance. If your instance is set to automatically restart, which is the default setting, Compute Engine restarts your instance, typically within three minutes from the time the error was detected. Depending on the issue, the restart might take up to 5.5 minutes.

After a compute instance encounters a host error, or you report its host as faulty, the instance's host requires emergency, unplanned maintenance. By default, Compute Engine provides a few hours of advance notice when it schedules this type of maintenance.

Occasionally, a compute instance might become unresponsive before a host error is signaled. You can reduce the amount of time Compute Engine waits to restart or terminate the instance by setting the host error recovery timeout. For more information, see [Set the policy for an existing instance](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#updatingoption). 

Physical hardware and software failures can happen occasionally but are rare occurrences. To protect your applications and services from these potentially disruptive system events, review the following resources:

  * [Designing robust systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems)
  * [Patterns for scalable and resilient apps](https://docs.cloud.google.com/solutions/scalable-and-resilient-apps)
  * [ Creating managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances)



Google also offers managed services such as [App Engine](https://docs.cloud.google.com/appengine) and the [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible).

## Host maintenance policy overview

An instance's host maintenance policy determines how it behaves during the following host events:

  * Maintenance event
  * Emergent maintenance event
  * Host error event or instance not responding



You can configure instances to continue running during host maintenance, while Compute Engine live migrates them to another host or you can choose to stop your instance instead.

You can change an instance's [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties) by configuring the following settings:

  * **Maintenance behavior:** whether the instance is live migrated or stopped when there is a maintenance event.
  * **Restart behavior:** whether Compute Engine restarts or terminates the instance if the instance crashes, experiences a host error, or becomes unresponsive.
  * **Host error detection time:** the maximum amount of time that Compute Engine waits to restart or terminate an instance after detecting that the instance is unresponsive. 
  * **Local SSD recovery time:** the maximum amount of time that Compute Engine spends in the `REPAIRING` state recovering the data on Local SSD disks after detecting a host error or during a maintenance event that requires instance termination. The Local SSD data is lost if the specified time elapses without a successful recovery.



You can update an instance's host maintenance policy at any time to control how you want your instances to behave.

## Maintenance and restart behaviors

When a host event occurs, the compute instance can either use live migration, or the instance can be terminated. If an instance is terminated, then you can choose to restart the instance yourself or have Compute Engine automatically restart it.

The following machine series might not support live migration, and instead require termination during host events:

  * Instances based on the following machine types terminate and restart in place: 
    * [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines) with more than 18,000 GiB of Titanium SSD
    * [Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines) or [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series) with more than 42,000 GiB of Titanium SSD
    * [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series) that have a Cloud RDMA network interface
    * [X5](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_series),
    * [X4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series)
    * [H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series)
  * [Bare metal](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#machine_series_with_bare_metal_machine_types) instances terminate and restart, meaning they might restart on a different host. For more details, see the "Maintenance experience" documentation for the machine series. For example, for C3 bare metal machine types, see [Maintenance experience for C3 instances](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_maintenance).
  * [Confidential VM instances](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#limitations) except for N2D machine types with AMD EPYC Milan CPU platforms running AMD SEV.
  * [Instances with GPUs](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance)
  * [Instances with TPUs](https://docs.cloud.google.com/tpu/docs/prepare-for-maintenance)



### Live migrate

By default, most instance types are set to [live migrate](https://docs.cloud.google.com/compute/docs/instances/live-migration-process), excluding the instance types mentioned in the previous section.

During live migration, Compute Engine automatically migrates your instance away from an infrastructure maintenance event, and your instance remains running during the migration. Your instance might experience a short period of decreased performance, but in general, most instances shouldn't perform noticeably different. This is ideal for instances that require constant uptime and can tolerate a short period of decreased performance.

When Compute Engine migrates your instance, it reports a system event that is published to the list of zone operations and to the System Events logs. You can review this event by [viewing the Compute Engine operations](https://docs.cloud.google.com/compute/docs/instances/viewing-compute-operations) for a specific zone. Live migration events have the following operation type:
    
    
    compute.instances.migrateOnHostMaintenance
    

### Terminate and restart

If you don't want your instance to live migrate, or if your instance type doesn't support live migration, then you can instead choose to allow Google Cloud to stop the instance when a host event occurs. With this configuration, if a host event occurs, then Compute Engine sends a soft power-off signal to shut down the instance. It then waits 60 seconds for the instance to shut down cleanly, and sets the instance status to `TERMINATED`. If the instance doesn't shut down cleanly in 60 seconds, then it is forcibly terminated.

This option is ideal if your instances demand constant, maximum performance, and if your overall application is built to handle instance failures or reboots.

When Compute Engine stops an instance because of a host event, it reports a system event that is published to the list of zone operations and to the System Events logs. You can review this event by [viewing the Compute Engine operations](https://docs.cloud.google.com/compute/docs/instances/viewing-compute-operations) for a specific zone. Instance termination events have the following operation type:
    
    
    compute.instances.terminateOnHostMaintenance
    

### Automatic restart

If your instance is configured to stop when there is a maintenance event, or if your instance crashes because of an underlying hardware issue, then Compute Engine can automatically restart the instance. The instance is either restarted on the same host server, or moved to another server in the same zone that isn't participating in the maintenance event.

By default, Compute Engine tries to recover instances with attached Local SSD disks for one hour. If the time limit is reached, then Compute Engine attempts to restart the instance on a different host server in the same zone. Z4D, Z4M, Z3, X4, and H4D instances have different default wait times. These instance types restart on the same host server after instance termination. 

To configure automatic restart, set the host maintenance policy field `automaticRestart` to `true`. This setting does not apply if the instance is taken offline due to a zonal outage or through manual operation, such as calling `sudo shutdown` within the guest OS.

When Compute Engine automatically restarts your instance, it reports a system event that is published to the list of zone operations. You can review this event by [viewing the Compute Engine operations](https://docs.cloud.google.com/compute/docs/instances/viewing-compute-operations) for a specific zone. Automatic restart events have the following operation type:
    
    
    compute.instances.automaticRestart
    

## Disk persistence following instance termination

Because Persistent Disk and Hyperdisk are network-attached storage, when your instance restarts, Compute Engine reattaches the boot disk and any secondary disks to the instance. The data on those disks persists through live migration and instance restarts.

Compute Engine preserves the data on Local SSD disks following a host event when possible. However, Compute Engine doesn't guarantee Local SSD data persistence. 

  * Local SSD disks are preserved in the following scenarios:

    * You reboot the guest operating system (OS).
    * You configure your instance for live migration and the instance goes through a host maintenance event.
    * A host error occurs and Compute Engine reconnects the instance to the Local SSD disks within the timeout limit.
    * You opt to [preserve the Local SSD data](https://docs.cloud.google.com/compute/docs/disks/local-ssd#stop_instance) when you stop or suspend the instance ([Preview](https://cloud.google.com/products/#product-launch-stages)).
    * A compute instance with attached Local SSD disks that supports only termination and automatic restart undergoes a maintenance event. The instance restarts in place, preserving the Local SSD data, instead of migrating to a new host.
  * Local SSD disks aren't preserved in the following scenarios:

    * You shutdown the guest operating system and force the instance to stop.
    * You create a [Spot VM](https://docs.cloud.google.com/compute/docs/instances/spot) or [preemptible VM](https://docs.cloud.google.com/compute/docs/instances/preemptible) and the VM goes through the preemption process.
    * You configure the instance to stop on host maintenance events instead of using live migration, and the instance goes through a host maintenance event.
    * You misconfigure a Local SSD disk and it becomes unreachable.
    * You disable project billing, causing the instance to stop.
    * If `automaticRestart` isn't configured on your instance.
    * A host error occurs and Compute Engine can't reconnect the disks to the instance before the timeout expires. In this case, the instance is restarted without recovering the Local SSD disks. When the instance restarts, Compute Engine attaches blank Local SSD disks to the restarted instance. You must [format and mount](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#formatandmount) these disks before the instance can use them. The data on the original Local SSD disks is unrecoverable.



Google Cloud uses a best-effort approach to keep your Local SSD data intact. However, there are cases where data can't be recovered, such as a timeout. For more information about when Local SSD disks are preserved, see [Local SSD data persistence](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence).

### Local SSD recovery timeout

When an instance with attached Local SSD disks enters the [`REPAIRING`](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle#repairing-state) state, Compute Engine tries to recover or preserve the Local SSD data. The instance and Local SSD disks are unavailable during this time.

An instance enters the `REPAIRING` state and starts the Local SSD recovery timeout countdown in the following scenarios:

  * A host error occurs.
  * Scheduled maintenance occurs on an instance that supports Local SSD data persistence after termination, and the instance is configured to both stop on host maintenance (`onHostMaintenance` set to `TERMINATE`) and automatically restart (`automaticRestart` set to `true`). During maintenance, Compute Engine preserves the data by either restarting the instance in place on the same host or migrating the instance and its Local SSD data to another host while stopped.



You can control how much time Compute Engine spends trying to recover or preserve the data with the host policy `localSsdRecoveryTimeout` setting. By default, Compute Engine spends 1 hour recovering the data, but valid values for this setting are between 0 and 168, in increments of 1 hour. The following machine types have different default values:

  * Z4D, Z4M, and Z3 VM machine types: the default value is 6, which means these instances try to recover the Local SSD data for 6 hours in the `REPAIRING` state before reaching the timeout limit.
  * Z4M bare metal and Z3 bare metal: the default value is 168 hours (7 days).



If you set the Local SSD recovery timeout to 0, then Compute Engine doesn't attempt to recover any attached Local SSD disks. The instance is restarted as soon as possible and the Local SSD data is unrecoverable. Use this configuration if resuming the workload is more important than recovering the Local SSD data.

If the recovery timeout isn't set to 0, but the time limit is reached before the Local SSD data is recovered, then Compute Engine restarts the instance without the Local SSD disk. Compute Engine attaches new, blank Local SSD disks to the restarted instance. You must [format and mount](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#formatandmount) these disks before the instance can use them.

**Caution:** If you set the Local SSD recovery timeout to less than four hours, then you risk losing data during scheduled maintenance.

If you set the Local SSD recovery timeout to the maximum value of 168, then the instance remains in the `REPAIRING` state for up to 7 days while Compute Engine attempts to recover the Local SSD disks.

You're not charged for the instance while it is in the `REPAIRING` state, as described in [VM instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle).

**Important:** The time spent attempting to recover Local SSD data doesn't count towards instance availability SLA downtime. While the instance is in this recovery phase, the [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't cover the instance.

### Stop Local SSD disk recovery

You can interrupt the Local SSD disk recovery process before Compute Engine reaches the recovery timeout limit. To do so, use the `gcloud compute instances stop` command with the `--discard-local-ssd=True` flag.

This command stops the recovery process, stops the compute instance, and **discards the Local SSD data**. You can then restart the instance. See [Stop an instance with Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#stop_instance) for more information.

**Note:** You can't preserve Local SSD data on suspend with Titanium SSD disks. For Titanium instances, the only supported option is `--discard-local-ssd=True`.

To set the Local SSD recovery timeout, see [Set instance host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#settingoptions). 

## Maintenance scheduling

Google Cloud provides features that allow tighter control around maintenance. By using [certain machine families](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event#limitations), you can specify maintenance preferences and get notifications of upcoming maintenance events through Cloud Logging, the instance's metadata server, the gcloud CLI `compute instances describe` command or the REST `instances.describe` method. Upon receipt of a [notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event), you have a period of time in which you can start the scheduled maintenance at a time you choose. If you don't trigger the scheduled maintenance, then the maintenance event occurs at the end of the notification time period, which is the scheduled time listed in the notification.

You can use these features in combination with your host maintenance policy to customize a maintenance schedule that fits your workload.

## What's next

  * Learn more about [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).
  * Learn more about [setting instance host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-options).
  * Learn more about [getting live migration notices](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice).
  * Learn more about [simulating host maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance). 
  * Learn more about [handling GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance). 
  * Learn more about [manually live migrating sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/manually-live-migrate).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
