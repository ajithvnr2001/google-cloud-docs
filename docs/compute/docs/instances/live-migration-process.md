---
url: https://docs.cloud.google.com/compute/docs/instances/live-migration-process/
title: Live migration process during maintenance events \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:41.969032+00:00
---

# Live migration process during maintenance events  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/live-migration-process/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Live migration process during maintenance events Stay organized with collections  Save and categorize content based on your preferences. 

During a planned maintenance event for the underlying hardware of a virtual machine (VM) instance or bare metal instance, the host server is unavailable. To keep an instance running during a host event, Compute Engine performs a _live migration_ of the instance to another host server in the same zone. For more information about host events, see [About host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview).

Live migration lets Google Cloud perform maintenance without interrupting a workload, rebooting an instance, or modifying any of the instance's properties, such as IP addresses, metadata, block storage data, application state, or network settings.

Live migration keeps instances running during the following situations:

  * **Infrastructure maintenance.** Infrastructure maintenance includes host hardware, network and power grids in data centers, and host operating system (OS) and BIOS.

  * **Security-related updates and system configuration changes.** These include events such as installing security patches and changing the size of the host root partition for storage of the host OS image and packages.

  * **Hardware failures.** This includes failures in memory, CPUs, network interface cards, and disks. If the failure is detected before there is a complete server failure, then Compute Engine performs a preventative live migration of the instance to a new host server. If the hardware fails completely or otherwise prevents live migration, then the instance terminates and restarts automatically.




Compute Engine only performs a live migration of VMs that have the host maintenance policy set to migrate. For information about how to change the host maintenance policy, see [Set VM host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-options).

## Live migration process and Local SSD disks

Compute Engine can live migrate instances with Local SSD disks attached (excluding Z3 instances with more than 18,000 GiB of attached Titanium SSD). Compute Engine moves the compute instances along with their Local SSD data to a new host server in advance of any planned maintenance.

**Important:** Instances with a large amount of Local SSD data can experience a longer period of performance degradation during the migration to the new host server. 

## Limitations

Live migration is not supported for the following VM types: 

  * **H4D instances with Local SSD**.
  * **Instances that have a Cloud RDMA network interface**.
  * **Bare metal instances**. Instances created with a [bare metal machine type](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances) don't support live migration. The maintenance behavior for these instances is set to `TERMINATE` and `RESTART`, respectively.
  * **Most Confidential VM instances**. Live migration for Confidential VM instances is supported on N2D and C3D machine types running AMD SEV. All other Confidential VM instances don't support live migration, and must be set to stop and optionally restart during a host maintenance event. See [Live migration](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-live-migration) for more details.
  * **VMs with GPUs attached**. VM instances with GPUs attached must be set to stop and optionally restart. Compute Engine offers a notice before a VM instance with a GPU attached is stopped, depending on the GPU type:

    * For most GPUs, Compute Engine provides a 60-minute notice.
    * For A4X, A4, or A3 Ultra instances, Compute Engine provides a 10-minute notice.

To learn more about these maintenance event notices, read [Query metadata server for maintenance event notices](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice). 

To learn more about handling host maintenance with GPUs, read [Handling host maintenance](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance) in the GPUs documentation.

  * **Cloud TPUs**. [Cloud TPUs](https://docs.cloud.google.com/tpu/docs/tpus) don't support live migration.
  * **Storage-optimized VMs**. For the following machine types, the maintenance behavior for these VMs is set to `TERMINATE` and `RESTART`. Compute Engine preserves the data on Titanium SSD during the maintenance event, as described in [Disk persistence following instance termination](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#disk-persistence). 

    * Z4D or Z4M VMs with more than 42,000 GiB of attached Titanium SSD
    * Z4M VMs that have a Cloud RDMA network interface
    * Z3 VMs with more than 18,000 GiB of attached Titanium SSD 
  * **Compute-optimized VMs** H4D VMs don't support live migration, because live migration isn't supported for RDMA-enabled VMs. From an HPC application perspective, performing live migration of an instance would severely impact application performance, and it's better for applications to start from a checkpoint. Maintenance behavior for these VMs is set to `TERMINATE` and `RESTART`. Compute Engine preserves the data on Titanium SSD during the maintenance event, as described in [Disk persistence following instance termination](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#disk-persistence). 



## How does the live migration process work?

When a VM is scheduled to live migrate, Compute Engine provides a [notification](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice) so that you can prepare your workloads and applications for this live migration disruption. During live migration, Google Cloud observes a minimum disruption time, which is typically much less than 1 second. If a VM is not set to live migrate, Compute Engine terminates the VM during host maintenance. VMs that are set to terminate during a host event [stop and (optionally) restart](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#terminate_and_optionally_restart).

When Google Cloud migrates a running VM from one host to another, it moves the complete state of the VM from the source to the destination in a way that is transparent to the guest OS and anything communicating with it. There are many components involved in making this work seamlessly, but the high-level steps are shown in the following illustration:

[ ![Migrating a VM and each of its resources to a new host system
            without requiring the guest operating system to restart.](https://docs.cloud.google.com/static/compute/images/live-migration.svg)](https://docs.cloud.google.com/static/compute/images/live-migration.svg) _Live migration components_

The process begins with a notification that a VM needs to be moved from its current host machine. The notification might start with a file change indicating that a new BIOS version is available, a hardware operation scheduling maintenance, or an automatic signal from an impending hardware failure.

Google Cloud's cluster management software constantly watches for these events and schedules them based on policies that control the data centers, such as capacity utilization rates and the number of VMs that a single customer can migrate at once.

After a VM is selected for migration, Google Cloud provides a notification to the guest that a migration is happening soon. After a waiting period, a target host is selected and the host is asked to set up a new, empty "target" VM to receive the migrating "source" VM. Authentication is used to establish a connection between the source and the target.

There are three stages involved in the VM's migration:

  1. **Source brownout.** The VM is still executing on the source host, while most state is sent from the source VM to the target VM. For example, Google Cloud copies all the guest memory to the target VM, while tracking the pages that have been changed on the source VM. The time spent in source brownout is a function of the size of the guest memory and the rate at which pages are being changed.

  2. **Blackout.** A very brief moment when the VM is not running anywhere. The source VM is paused and all the remaining state required to begin running the VM on the target host is sent. The VM enters the blackout stage when sending state changes during the source brownout stage reaches a point of diminishing returns. An algorithm is used that balances numbers of bytes of memory being sent against the rate at which the guest is making changes.

During blackout events, the system clock appears to jump forward, up to 5 seconds. If a blackout event exceeds 5 seconds, Google Cloud stops and synchronizes the clock using a daemon that is included as part of the VM guest packages.

  3. **Target brownout.** The VM executes on the target host. The source VM is present and might provide support for the target VM. For example, until the network fabric has caught up with the new location of the target VM, the source VM provides forwarding services for packets to and from the target VM.




Finally, the migration is complete and the system deletes the source VM. You can see that the migration took place in the [Cloud Logging logs](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#check-logs-for-maintenance) for your VM.

**Note:** During live migration, VMs might experience a decrease in performance in disk, CPU, memory, and network utilization for a short period of time.

## Live migration of sole-tenant VMs

As your workload runs, you might want to move VMs to a different sole-tenant node or node group. If you move a VM to a group of nodes, Compute Engine determines which node to place it on. For information about sole-tenancy, see [Sole-tenancy overview](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

To move sole-tenant VMs to a different node or node group, you can manually initiate a live migration. You can also manually initiate a live migration to move a VM on a multi-tenant host into a sole-tenant node. For more information, see [Manually live migrate VMs](https://docs.cloud.google.com/compute/docs/nodes/about-manual-live-migration).

## What's next

  * Set [VM host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) options to configure your instances to live migrate.

  * Learn how to [get live migration notices](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice#maintenanceevents) so you can trigger tasks that you want to perform prior to a maintenance event.

  * Read tips for [designing a robust system](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems) that can handle service disruptions.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
