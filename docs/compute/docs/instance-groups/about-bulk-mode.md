---
url: https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode/
title: About bulk mode \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:56.101939+00:00
---

# About bulk mode  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About bulk mode Stay organized with collections  Save and categorize content based on your preferences. 

Managed instance groups (MIGs) can create virtual machine (VM) instances in bulk, achieving your target size all at once, instead of creating each instance individually. Bulk creation of instances helps to ensure that the requested resources are ready before the MIG begins to create its instances. Bulk creation is useful for batch jobs that can only start after all instances are available, for example, High Performance Computing (HPC) or distributed training.

If you need to make multiple requests in a MIG to create instances all at once, then use _resize requests_. For more information, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

## Bulk mode

In a MIG, the mode in the _target size policy_ determines whether the MIG creates the instances independently or all at once. By default, the MIG creates its instances independently.

The following are the two modes in the target size policy:

  * **Individual** (default): In the _individual mode_ , the MIG creates instances independently. If there is not enough capacity to create all the instances specified in the target size, then the MIG creates as many instances as possible with the available capacity and attempts to create the remaining instances as capacity becomes available.

  * **Bulk** : In the _bulk mode_ , the MIG creates the instances all at once. If there is not enough resource capacity to create all the instances specified in the target size, then the MIG waits for the full capacity to become available. The MIG doesn't create any instance until Compute Engine has the capacity for the specified target size. By using bulk mode, you ensure that your workload receives all its required resources before the MIG begins to create the instances.




## How bulk mode in a MIG works

To enable bulk mode in a MIG, you must set the target size policy mode to `BULK` and specify a target size. After you specify a target size, the MIG starts the bulk creation operation and waits for full capacity to become available.

During this waiting period, the MIG creates [managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance). These managed instances represent the actual instances that the MIG will create when the bulk creation is successfully completed. The MIG doesn't create any VM instances until Compute Engine has the capacity for all the instances specified in the target size. When the full capacity becomes available, the MIG creates your requested instances all at once.

To monitor the bulk creation operation, see [View the status of bulk creation of instances](https://docs.cloud.google.com/compute/docs/instance-groups/view-cancel-vm-bulk-creation-in-migs#view-bulk-instance-operation).

## Limitations

The following sections describe the limitations that apply when you use bulk mode in a MIG.

### Instance provisioning and distribution

The following limitations apply to instance provisioning and distribution when using bulk mode:

  * Bulk mode supports only [TPU machine types](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines).

  * In a regional MIG, you can only use the [`ANY_SINGLE_ZONE` target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).




### Configuration changes and resizing

The following limitations apply to configuration changes and resizing when using bulk mode:

  * You can't change the target size policy mode in an existing MIG.

  * If your MIG's instance template specifies flex-start provisioning model, then you must turn off repairs in the MIG by setting the `defaultActionOnFailure` field to `DO_NOTHING`.

  * When adding or removing instances from the MIG, the following conditions apply:

    * You can add instances by increasing the target size or by using the `createInstances` method only when there is no instance (`targetSize = 0`) in the MIG.

    * You can remove instances by decreasing the target size to `0`. To decrease to a non-zero size, the MIG must not have a bulk instance operation in progress (`bulkInstanceOperation.inProgress` must be `false`). 

  * When resizing the MIG by using the `resizeAdvanced` method, you cannot [disable creation retries](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#disabling_creation_retries_mode_during_resize).




### Unsupported features for MIG

Bulk mode doesn't support the following MIG features:

  * [Resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig) that create instances all at once
  * [Instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility)
  * [Autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler)
  * [Canary updates](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#canary_updates)
  * [Standby pool](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig#target_sizes_of_suspended_and_stopped_pools)



## Pricing

Bulk instance operation in a MIG incurs no additional charges. Instead, based on the provisioning model that you use, you incur charges as follows:

  * If you use MIG to create Flex-start VMs, then you incur charges as follows:

    * Charges begin when the MIG creates the Flex-start VMs. Google Cloud charges you for the Flex-start VMs based on [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing).

    * Charges end when the MIG deletes the Flex-start VMs at the end of their run duration, or when you delete the Flex-start VMs.

**Important:** If a MIG creates only some requested Flex-start VMs and fails to create the rest, then you might still incur charges for any created Flex-start VMs. These charges apply until the MIG automatically deletes the Flex-start VMs.
  * If you use MIG to create VMs by consuming a reservation, then you incur charges as follows:

    * When the MIG creates the VMs, you don't incur charges again for the consumed reservation resources. You only incur charges for resources that the VMs use and that aren't part of the reservation, such as disks or IP addresses.

    * Charges end at the reservation end time. At this time, Compute Engine deletes the reservation and any VMs that consume it. For more information, see the [billing for reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing).




## What's next

  * Learn how to [create a MIG that uses bulk mode](https://docs.cloud.google.com/compute/docs/instance-groups/bulk-create-instances-in-mig).
  * [View the target size policy in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#getting_a_migs_properties).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
