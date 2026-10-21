---
url: https://docs.cloud.google.com/compute/docs/tpus/tpus-and-migs/
title: TPU instances in MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:06.205008+00:00
---

# TPU instances in MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tpus/tpus-and-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  TPU instances in MIGs Stay organized with collections  Save and categorize content based on your preferences. 

Managed instance groups (MIGs) automate the creation, configuration, and lifecycle management of a collection of VMs. MIGs provide benefits such as high availability through autohealing and regional (multi-zone) deployments, automatic scaling to handle variable loads, and simplified rolling updates for applications. For more information, see [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).

You can use MIGs to create and manage TPU VMs for TPU versions v5p, v6e, and TPU7x. You can create MIGs with a single TPU VM, independent TPU VMs (also called single-host slices) and MIGs with interconnected TPU VMs (also called multi-host slices).

Each slice in a single-host MIG has at most one TPU VM. The TPU VMs within the MIG are not connected with inter-chip interconnect (ICI) links.

A multi-host slice contains multiple TPU VMs that are interconnected with ICI links.

## MIGs with a single TPU VM instance

You can create and manage an individual TPU VM using a MIG by setting the MIG's target size to one. This approach is useful if you want to use MIG features like automatic repair for a single instance. For more information, see [Create a MIG with single-host TPU slices](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-mig-single-host-slice).

## MIGs with single-host TPU slices

Creating a managed instance group (MIG) with multiple, independent TPU instances is beneficial for workloads that require several individual TPU VMs but don't need them to be interconnected with ICI links for distributed workloads. For example:

  * **Inference serving** : Each VM in the MIG can independently handle inference requests. A MIG lets you scale the number of serving instances based on demand and manage them as a group.
  * **Parallel independent tasks** : A MIG provides a way to manage many small, independent training jobs or other computations that can run in parallel on single TPU VMs.
  * **Management** : MIGs provide the following features: 
    * **Deployment** : Define an instance template once and use the MIG to create multiple identical TPU VMs.
    * **Scalability** : Adjust the number of TPU VMs by resizing the MIG.
    * **Rolling updates** : Update the software or machine type across all VMs in a controlled manner.
  * **Cost-effectiveness** : For tasks that don't require the full power or interconnectivity of a large TPU slice, using multiple smaller, independent TPU slices can be more cost-effective.



For more information, see [Create a MIG with single-host TPU slices](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-mig-single-host-slice).

## MIGs with a multi-host slice

Unlike groups of independent TPU slices, a MIG configured for a multi-host slice manages a set of TPU VMs that are tightly coupled through ICI links. This creates a single, logical TPU slice.

### Benefits and performance

MIGs for multi-host TPU slices provide the scale and performance required for intensive machine learning workloads.

  * **Distributed training** : Training machine learning models often requires more TPU power than a single TPU VM can provide. Larger TPU slices distribute computation across many TPU chips and VMs, with the ICI links enabling fast communication between them. This is crucial for training performance.
  * **High interconnect bandwidth** : The ICI network provides higher bandwidth and lower latency between TPU chips in the slice than the standard data center network (DCN). This is essential for the synchronous operations common in large model training.



### Atomic lifecycle operations

To ensure the integrity of the interconnected topology, the MIG manages the entire slice as a single, indivisible unit throughout its lifecycle.

  * **Creation** : All VMs in the slice are provisioned together. If enough healthy, interconnected capacity aren't available for the entire requested topology, the slice isn't created.
  * **Deletion** : The MIG deletes the entire slice as a unit.
  * **Resizing** : Resizing is restricted to scaling from 0 to the full slice size, or from the full slice size back down to 0. You can't partially resize a multi-VM slice.



### Configuration requirements

Configuring a multi-host MIG requires defining both the physical interconnection topology and the individual instance properties.

  * **Workload policy** : You must specify a workload policy with the `accelerator-topology` parameter (for example, 4x4, 8x8, or 4x4x4). This configures the MIG to treat the instances as a single, interconnected slice. For information about topology, see [TPU topology](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_topology).
  * **Instance template** : Defines properties like machine type, disk image, and other settings for each VM within the slice.



### Slice availability and failure recovery

When you use MIGs to create a multi-host TPU slice, the failure recovery behavior depends on the provisioning model and reservation mode that you use:

  * **When a MIG uses on-demand, flex-start, or reservations (excluding All Capacity mode reservations).** In this scenario, Compute Engine automatically manages the slice recovery process. If a host or ICI failure occurs, then the slice transitions to the `REACTIVATING` state. All VMs in the slice transition into the `REPAIRING` state, though not necessarily all at the same time. Compute Engine then automatically recovers the slice by restarting the VMs together on healthy capacity.

  * **When a MIG uses the spot provisioning model.** In this scenario, you are responsible for managing the slice recovery process. If Spot VMs preemption occurs, then Compute Engine terminates all instances in the slice. The slice transitions to the `FAILED` state and the VMs transition to the `TERMINATED` state. To recover from the failed state, you need to manually recreate the slice.

  * **When a MIG uses reservations in All Capacity mode.** In this scenario, you are responsible for managing the slice recovery process. If a failure occurs, then the slice transitions to the `FAILED` state and you need to manually recreate the slice.

The behavior in All Capacity mode further depends on the following:

    * **Host failure or reported faulty VM.** The affected VM transitions to the `REPAIRING` state. Once the underlying hardware is fixed, the VM transitions back to the `RUNNING` state.
    * **Upcoming emergent maintenance.** When you [manually start a maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event#start-maintenance-event), the VMs transition from the `RUNNING` to the `REPAIRING` state. After the maintenance finishes, the VM returns to the `RUNNING` state.
    * **ICI failure.** The VMs remain in the `RUNNING` state, but the slice state transitions to the `FAILED` state.



To recreate a slice after Spot VMs preemption or a failure in All Capacity mode, you must do one of the following:

  * Delete and recreate the MIG.
  * Resize the MIG to `0`, and then increase it to the required size. 



#### Failure recovery from an instance interruption

If you delete or stop a TPU instance, or stop an instance from within the operating system, then the slice transitions to the `FAILED` state. In this scenario, the slice remains in the `FAILED` state until you recreate the slice. To recreate the slice, you must either delete and recreate the MIG, or resize the MIG to `0` and then increase its size.

For more information about the slice states, see [View the status of a TPU slice](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#view_the_status_of_a_tpu_slice).

## Limitations

The following sections explain the limitations for creating a MIG with TPU VMs.

### Limitations for instance templates

Instance templates that specify a TPU machine type have the following limitations:

  * When using the reservation-bound provisioning model, you must set the instance termination action to delete.

  * TPUs can only consume [specifically targeted reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type).

  * You can't specify a [placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).

  * You must not disable [automatic restart](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#autorestart) in the following cases:

    * Multi-host slices using standard, flex-start, or reservation-bound provisioning models (including All Capacity mode).

    * Single-host using reservation-bound provisioning model in All Capacity mode.

  * You must not enable automatic restart when using spot provisioning model.




### Limitations for MIGs

MIGs with TPUs have the following limitations:

  * **Lifecycle operations** : You can't stop, start, resume, or suspend TPU instances. To change configurations that require a restart or to stop incurring charges, you must delete the instances. 

  * **Regional MIG zone distribution** : You must set the [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape) to `ANY_SINGLE_ZONE`.

  * **Configuration updates in a MIG** :

    * You can't [update](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs) a MIG that forms a multi-host TPU slice due to the defined accelerator topology.
    * You can update a MIG that forms single-host TPU slices by using the [automatic or selective methods](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#choosing_between_automated_and_selective_updates). However, the updates for single-host TPU slice don't support the restart (`RESTART`) action. If a restart is necessary and the most disruptive action allowed is replace (`REPLACE`), then the updater will replace the instance; otherwise, the update attempt fails with an error.
  * For a MIG that forms a multi-host TPU slice, the following limitations also apply: 

  * **Target size policy** : You must set the target size policy mode to [`BULK`](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode). After you set this mode, you can't change it.

  * **Target size** : In bulk mode, you can set the target size to either `0` or the number of instances that are required to form the accelerator topology.

  * **Workload policy** : You must specify a workload policy in which the accelerator topology is defined. After you set the workload policy, you can't change or remove the policy from the MIG.

  * **MIG initiated repairs** : You must [turn off MIG initiated repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig) by setting the `defaultActionOnFailure` field to `DO_NOTHING`. In this configuration, the MIG doesn't take any action on a failed instance. Compute Engine automatically recovers the failed instance by restarting all instances in the same slice on healthy capacity. 



* **Unsupported features** : MIGs with TPUs don't support the following features:

  * [Instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility)
  * [Resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig) to obtain resources all at once
  * [Stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration)
  * For a MIG that forms a multi-host TPU slice, the following are also not supported: 
    * [Autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler)
    * [Abandon instances](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances)
    * [Delete instances](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group)



## What's next

  * Learn how to [Create a MIG with single-host TPU slices](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-mig-single-host-slice)
  * Learn how to [Create a MIG with a multi-host TPU slice](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-mig-multi-host-slice)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
