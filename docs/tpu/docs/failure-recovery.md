---
url: https://docs.cloud.google.com/tpu/docs/failure-recovery/
title: Failure recovery of TPU instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:22.164103+00:00
---

# Failure recovery of TPU instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/failure-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Failure recovery of TPU instances

To keep your workloads running, Compute Engine recovers TPU instances and slices from hardware and application failures.

Failure recovery behavior depends on your capacity mode:

  * **Managed capacity mode** (on-demand, flex-start, and standard reservations): Compute Engine automatically recovers TPU instances and slices by restarting them on healthy hardware.
  * **All Capacity mode** (reservations in All Capacity mode): You manage TPU slice recovery. Hardware failures are repaired on the existing host without automatically relocating instances to new hardware.



## Multi-host slice recovery requirements

Multi-host TPU slices require all instances in the slice to be recovered or rescheduled together. Whether Compute Engine automatically handles recovery in managed capacity mode or you recover slices manually in All Capacity mode, you can't reschedule individual instances within a slice.

Instances in a multi-host slice are connected by inter-chip interconnect (ICI) and, in some cases, by an Optical Circuit Switch (OCS). When you provision a multi-host slice, Compute Engine creates TPU instances and activates the ICI network. You specify the network topology of the slice by setting the accelerator topology in your workload policy. When a workload starts, LibTPU, the foundational TPU software layer, initializes the network topology. By default, the XLA compiler then statically maps the model's operations to this topology.

If an instance or network link fails, then the physical hardware no longer matches the mapped topology. As a result, the XLA compiler can't execute the workload until the system reconfigures the network topology by recreating or rescheduling all instances in the slice.

## Failure recovery in managed capacity mode

In managed capacity mode (including on-demand, flex-start, and standard reservations), Compute Engine automatically recovers TPU instances and slices from hardware and host failures by restarting them on healthy hardware.

### Automatic recovery of a single-host TPU slice

Single-host slices are independent TPU instances. By default, Compute Engine automatically recovers failed instances by restarting the instances on healthy hardware. This behavior is controlled by the automatic restart setting, which is enabled by default when creating instances, except for Spot VMs. If you disable automatic restart, then an instance failure causes the instance to enter the `TERMINATED` state. For more information, see [Automatic restart](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#autorestart).

Compute Engine automatically recovers a failed instance in scenarios such as:

  * A host timeout or error caused by the physical machine not responding, host shutdown, host reboot, or host power outage
  * [Physical host maintenance events](https://docs.cloud.google.com/tpu/docs/prepare-for-maintenance) initiated by you or Google
  * Inter-chip interconnect (ICI) failure within a host
  * VM crash



Compute Engine doesn't automatically recover instances in scenarios of planned termination, including:

  * Instance deletion
  * Reservation deletion or expiration
  * Spot VMs preemption



#### MIG-initiated repair in single-host slices

In a MIG with single-host slices, if a TPU instance in a single-host slice enters a `TERMINATED` state due to hardware failures or external events like Spot VMs preemption, then the MIG repairs the instance by default. During a repair, the MIG recreates the instance with the same name. You can disable this repair mechanism if you [turn off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig).

You can also set up an application-based health check in a MIG with single-host slices. If the health check detects that your application is unresponsive, then the MIG marks the instance as unhealthy and autoheals the instance by recreating it.

For more information, see [About repairing VMs for high availability](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair) and [Set up an application health check and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).

### Automatic recovery of a multi-host slice

For TPUs in managed mode using the on-demand, flex-start, or reservation consumption models, Compute Engine automatically recovers failed instances in a multi-host slice.

During recovery, Compute Engine identifies a set of TPU machines that can form the network topology, restarts all instances in the slice together on those machines, and reconfigures the network. This process minimizes downtime by recreating the topology on available healthy hardware, rather than waiting for hardware repairs.

**Important:** You must not disable [automatic restart](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#autorestart) for a multi-host TPU slice in managed capacity mode.

#### Recovery process and slice states

During automatic recovery, the slice transitions through the following states:

  1. The slice transitions to the `REACTIVATING` state.
  2. All instances in the slice transition to the `REPAIRING` state, though not necessarily at the same time.
  3. Compute Engine restarts all instances in the slice together on healthy hardware.



For more information about TPU slice states, see [Accelerator topology states](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#accelerator_topology_states).

### Scenarios requiring manual slice recovery in managed capacity mode

Compute Engine can't automatically recover a multi-host slice in the following scenarios:

  * **Spot VMs preemption** : If any instance in the slice is preempted, Compute Engine terminates all instances in the slice, and the slice enters the `FAILED` state.
  * **User-initiated interruptions** : If you stop or delete a TPU instance, or stop an instance from within the operating system, then the slice enters the `FAILED` state. The slice remains in the `FAILED` state until you recreate it.



In these scenarios, you must manually recover the slice.

## Failure recovery in All Capacity mode

In All Capacity mode, you are responsible for managing the TPU slice recovery process. Unlike managed capacity mode, Compute Engine doesn't automatically relocate failed TPU instances or multi-host slices to new physical hardware. Google repairs the underlying failed hardware on the existing host, and you're responsible for rescheduling unhealthy slices to healthy spare hardware that you set aside in your reservation.

**Important:** For TPUs in All Capacity mode, you must not disable automatic restarts (`scheduling.automaticRestart` must remain set to `true`).

### Host failure and faulty host repair

If a host failure occurs or if you report a VM host as faulty, the host repair process works as follows:

  * The affected VM transitions to the `REPAIRING` state while the physical hardware is repaired.
  * Once the underlying hardware is fixed, the VM transitions back to the `RUNNING` state on the same host. However, if the VM belongs to a multi-host slice, then the slice remains in the 'FAILED' state. You must manually recover the slice.



For more information, see [Report and repair faulty TPU hosts in All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-report-faulty-hosts).

### Emergent maintenance

During emergent maintenance events or when you manually initiate a maintenance event:

  * The VMs transition from the `RUNNING` state to the `REPAIRING` state.
  * After maintenance finishes, the VMs return to the `RUNNING` state on the same host.



For more information, see [Manage maintenance events in All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-maintenance-events).

### Multi-host slice failure scenarios

In All Capacity mode, Compute Engine doesn't automatically recover a multi-host slice. A slice transitions to the `FAILED` state in the following scenarios:

  * **ICI failure** : The VMs remain in the `RUNNING` state, but the slice state transitions to the `FAILED` state.
  * **Spot VMs preemption** : If any instance in the slice is preempted, Compute Engine terminates all instances in the slice, and the slice enters the `FAILED` state.
  * **User-initiated interruptions** : If you stop or delete a TPU instance, or stop an instance from within the operating system, then the slice enters the `FAILED` state.



When a slice enters the `FAILED` state, you must manually recover the slice by rescheduling all instances in the slice.

## Manually recover a TPU slice

When a TPU slice in managed capacity mode or All Capacity mode is in the `FAILED` state, you must manually recover it by rescheduling all instances in the slice using one of the following methods:

  * [Resize the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group) to target size `0`, and then increase it to the required size.
  * [Delete the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig#delete_a_mig) and [recreate the slice](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-mig-multi-host-slice).



## What's next

To verify failure recovery of TPUs, check the following statuses:

  * [View the status of a TPU slice](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#view_the_status_of_a_tpu_slice)
  * [View the status of instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
