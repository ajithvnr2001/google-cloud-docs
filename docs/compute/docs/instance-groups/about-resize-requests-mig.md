---
url: https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig/
title: About resize requests in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:26.967380+00:00
---

# About resize requests in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About resize requests in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document gives an overview of resize requests in a managed instance group (MIG). To learn more about other ways to add virtual machine (VM) instances to a MIG, see [Add instances to a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#adding_instances_to_a_mig).

Use MIG resize requests for the following benefits:

  * **Create VMs in the MIG all at once**. When resources are available, the MIG creates VMs all at once. This approach helps you avoid charges for partial capacity until all resources become available.

  * **Obtain high-demand resources**. You can use MIG resize requests with the flex-start or reservation-bound provisioning models. These provisioning models give you the following benefits:

    * You have higher chances of obtaining high-demand resources like GPUs.

    * Based on the machine type that your requested VMs use, you get a discount up to 53% for memory, vCPUs, and any attached GPUs and Local SSD disks.




## Use cases

You can use resize requests in a MIG for the following:

  * **Create Flex-start VMs**. You can request to create [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms) for obtaining resources as soon as they are available. These VMs are suitable for workloads that need to run for up to seven days, but can start at any time. When you use resize requests to create Flex-start VMs, the following occurs:

    * The MIG schedules Flex-start VM creation as soon as resources are available.

    * After the MIG creates the requested Flex-start VMs, the VMs run until one of the following occurs:

      * Compute Engine deletes the Flex-start VMs at the end of their run duration.

      * You delete the Flex-start VMs.

  * **Create VMs by consuming a reservation**. You can request to create [VMs that use the reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/instances/about-reservation-bound-vms) to consume a reservation. When you use resize requests to consume a reservation, the following occurs:

    * The MIG creates VMs at or after the reservation start time.

    * After the MIG creates the requested VMs, the VMs run until one of the following occurs:

      * Compute Engine deletes the reservation at its end time.

      * You stop or delete the VMs.




## How resize requests work

The following sections explain how MIG resize requests work.

### On creation

To create a MIG resize request, specify the following properties:

  * To define the number of VMs to create, use one of the following properties:

    * **`resizeBy`** : the number of VMs to create. The MIG automatically generates VM names.

    * **`instanceNames`** : a list of VM names. The MIG creates one VM for each name that you specify. This property is in [Preview](https://cloud.google.com/products#product-launch-stages). Use it if your workload requires specific VM names.

  * **`requestedRunDuration`** : how long the VMs must run for. The run duration must be between 10 minutes and seven days. This property is optional. If you use MIG resize requests to create VMs as soon as resources are available, then this property overrides the run duration that is specified in the MIG's instance template.




### After creation

After you create a MIG resize request, the request goes through different states. The following diagram shows these states:

![A diagram of each state that Compute Engine can set a resize request to.](https://docs.cloud.google.com/static/compute/images/instance-groups/resize-requests/resize-requests-states.png)

The states shown in the preceding diagram are as follows:

  * **`CREATING`** : Compute Engine received the resize request, the MIG's target size increases by the number of VMs that are specified in the request, and the MIG creates managed instances that are in a `CREATING` state. These managed instances represent the VMs that the MIG creates when the resize request succeeds.

  * **`ACCEPTED`** : Compute Engine created and accepted the request. Based on your use case for MIG resize requests, Compute Engine does one of the following:

    * **Create Flex-start VMs**. On a best-effort basis, the [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler) schedules Flex-start VM creation based on availability and the run duration that is specified in the request. If you lack [standard or preemptible allocation quota](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#preemptible-quotas), or if resources are temporarily unavailable, then the Dynamic Workload Scheduler maintains the request until you have sufficient quota and resources become available.

**Note:** Even though a MIG creates Flex-start VMs for a resize request only when all the requested capacity is available, in rare cases, the MIG might create only some of the requested number of VMs but fail to create the remaining ones. If this failure occurs, then the MIG automatically deletes these VMs as soon as possible to minimize unwanted charges. The state of the request remains `ACCEPTED` and the MIG retries creating the VMs all at once.
    * **Create VMs by consuming a reservation**. If the auto-created reservation that you're targeting for consumption has reached its start time, then the request transitions to `SUCCEEDED`. Otherwise, the request persists until the reservation reaches its start time.

  * **`SUCCEEDED`** : the MIG created the requested number of VMs all at once. The VMs are allocated as close to each other as possible, based on availability. Based on your use case for MIG resize requests, the following occurs:

    * When the MIG creates Flex-start VMs, the VMs run until the MIG deletes them at the end of their run duration, or until you delete the VMs. You can't recreate, stop, or suspend the VMs.

    * When the MIG creates VMs by consuming an auto-created reservation, the VMs run until the reservation period ends, or until you stop, suspend, or delete the VMs.

  * **`FAILED`** : the resize request failed due to a technical error. As a result, Compute Engine decreases the target size of the MIG by the number of requested VMs.

  * **`CANCELLED`** : a user [canceled the resize request](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig#cancel-request). When you cancel a resize request, Compute Engine stops the MIG from creating the requested resources. After you cancel a resize request, Compute Engine decreases the MIG's target size by the number of requested VMs and deletes the request after 14 days. Optionally, you can [delete the resize request](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig#delete-request) before Compute Engine deletes it.




If you delete a MIG that contains resize requests, then this deletion also removes any resize requests and VMs in the MIG. However, if you delete a MIG when the MIG creates VMs to fulfill a resize request, Compute Engine waits until the MIG has finished creating the requested number of VMs and the state of the resize request transitions to `SUCCEEDED` before deleting the MIG.

## Quota

Based on your use case for MIG resize requests, you need quota as follows:

  * **Create Flex-start VMs**. Quota requirements vary based on the machine type that your requested number of Flex-start VMs use. If you lack quota for your requested resources, then a resize request remains pending until you have sufficient quota. For more information about quotas that apply to Compute Engine resources, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage).

  * **Create VMs by consuming a reservation**. You don't need quota in this use case. This requirement is because you use the [reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) to consume an auto-created reservation for a future reservation in calendar mode.




## Pricing

You don't incur charges when you create, cancel, or delete resize requests in a MIG. Instead, based on your use case for MIG resize requests, you incur charges as follows:

  * If you use MIG resize Flex-start VMs, then you incur charges as follows:

    * Charges begin when the MIG creates the Flex-start VMs. Google Cloud charges you for the Flex-start VMs based on [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing).

    * Charges end when the MIG deletes the Flex-start VMs at the end of their run duration, or when you delete the Flex-start VMs.

**Important:** If a MIG creates only some requested Flex-start VMs and fails to create the rest, then you might still incur charges for any created Flex-start VMs. These charges apply until the MIG automatically deletes the Flex-start VMs.
  * If you use MIG resize requests to create VMs by consuming a reservation, then you incur charges as follows:

    * When the MIG creates the VMs, you don't incur charges again for the consumed reservation resources. You only incur charges for resources that the VMs use and that aren't part of the reservation, such as disks or IP addresses.

    * Charges end at the reservation end time. At this time, Compute Engine deletes the reservation and any VMs that consume it. For more information, see the [billing for reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing).




## Limitations

The following sections explain the limitations for MIG resize requests.

### Limitations for resize requests

MIG resize requests have the following limitations:

  * You can use MIG resize requests to obtain different machine types depending on the provisioning model that you use:

    * **Flex-start** : you can obtain any GPU machine type (except A4X Max and A4X), and H4D machine types. Use this model to create Flex-start VMs as soon as resources are available.

    * **Reservation-bound** : you can only obtain A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), or H4D machine types. Use this model to create VMs by consuming a reservation. 

  * You can only cancel resize requests that are in the `ACCEPTED` state.

  * You can only delete a resize request after it succeeds (`SUCCEEDED`), fails (`FAILED`), or is canceled (`CANCELLED`).




### Limitations for the instance template

For the MIG's instance template, the following limitations apply:

  * You must specify to stop VMs during [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties).

  * You can't specify [placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).

  * Based on your use case for MIG resize requests, you must specify the following configurations when you create the instance template:

    * To create Flex-start VMs, you must specify the following:

      * To delete VMs at the end of their run duration by using the [`maxRunDuration` and `instanceTerminationAction` fields](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#set-duration).

      * To use the [flex-start provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

    * To create VMs by consuming an auto-created reservation for a future reservation in calendar mode, you must specify the following:

      * To delete VMs at the end of the reservation period by using the [`instanceTerminationAction` field](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#set-duration).

      * To [target the reservation for consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

      * To use the [reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).




### Limitations for the MIG

For the MIG, the following limitations apply:

  * In a regional MIG, you can only use the [`ANY_SINGLE_ZONE` target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).

  * You must [turn off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig) in the MIG.

  * You must [delete the autoscaling configuration](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#delete_an_autoscaler).

  * You can't apply VM configuration updates to the VMs created through resize requests. To prevent automatic updates, [set the MIG's update type to opportunistic](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#set_up_a_proactive_or_an_opportunistic_update).

  * You can't apply the [all-instances configuration](https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic) to VMs created through resize requests.

  * You can't define [per-instance configurations](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs) in VMs created through resize requests.

  * You can only set the [standby pool mode](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig#standby_policy) of the MIG to `manual` (default).

  * If a MIG contains accepted resize requests, then you can't do the following:

    * You can't add a second instance template to initiate a [canary update in the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#canary_updates).

    * You can't change the [target size of the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#set_the_groups_target_size).

  * You can't delete or abandon the managed instances in a `CREATING` status that the MIG creates for a resize request. To delete those managed instances, you must [cancel the resize request](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig#cancel-request).

  * If you use MIG resize requests to create Flex-start VMs, then you can't [stop](https://docs.cloud.google.com/compute/docs/instance-groups/manually-suspend-or-stop-vms-in-mig#stop_selected_vms_in_a_mig) or [recreate VMs](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#recreate_instances).




## What's next

  * Learn how to [create resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/create-resize-requests-mig).

  * Learn how to [view, cancel, or delete resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
