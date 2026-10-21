---
url: https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview/
title: About future reservation requests in calendar mode \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:11:37.405693+00:00
---

# About future reservation requests in calendar mode  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About future reservation requests in calendar mode Stay organized with collections  Save and categorize content based on your preferences. 

This document gives an overview of future reservation requests in calendar mode.

Use future reservation requests in calendar mode to obtain high-demand resources, such as for creating virtual machine (VM) instances that have GPUs or TPUs attached. When Google Cloud approves a reservation request, Compute Engine provisions your reserved resources at your specified date and time, and for a duration of up to 90 days. You can then use the reserved resources for creating GPU VMs, H4D VMs, or TPU VMs to run the following workloads:

  * Model pre-training jobs

  * Model fine-tuning jobs

  * High performance computing (HPC) simulation workloads

  * Short-term expected increases in inference workloads




For more information about other ways to reserve resources in Compute Engine, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).

## Create a request in calendar mode

The following sections explain how to view resource availability, as well as what details to specify when you create a future reservation request in calendar mode.

### View resource future availability

Before you create a future reservation request in calendar mode, you can view the future availability in a region of the following resources:

  * For GPU or H4D VMs, up to 60 days in advance

  * For TPUs, up to 120 days in advance




Compute Engine uses the [Dynamic Workload Scheduler (DWS)](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler) to view when your requested resources are available. When you create a request, specify the number, type, and reservation period for the resources that you confirmed as available. Google Cloud is more likely to approve your request if you supply this information.

### Define request properties

When you create a future reservation request in calendar mode, you must specify the following properties:

  * **Auto-delete**. This property determines if Compute Engine deletes the automatically created (_auto-created_) reservation for your request at the end time, even if the reservation isn't fully consumed. To create a request in calendar mode, you must enable the auto-delete option.

  * **Consumption type**. This property defines how VMs consume the auto-created reservation. When you create a request in calendar mode, you must specify that you want to create [_specifically-targeted reservations_](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type#consumption-type). This setting means that only VMs that target the reservation can consume it.

  * **Deployment type**. This property defines the collocation of your reserved resources. Compute Engine reserves resources based on the resource type:

    * For GPU or H4D VMs, you must specify the dense (`DENSE`) deployment type when you create a request. This configuration specifies to densely reserve resources for minimal network latency.

**Important:** Compute Engine densely allocates resources only within the auto-created reservation for a single request. Reservations from multiple requests might be allocated in different clusters. In such a case, you can't use the same RDMA network for your reservations. Each reservation must use its own separate RDMA network.
    * For TPUs, Compute Engine uses the flexible (`FLEXIBLE`) deployment type by default. This configuration specifies to reserve resources as close as possible on a best-effort basis.

  * **Name**. The name of your request, which must be unique within your project.

  * **Number of resources**. The number of GPU VMs, H4D VMs, or TPUs to reserve at your requested start time.

  * **Planning status**. This property defines if you immediately submit your request to Google Cloud for review, or save it as a draft and submit it later. When you create a request in calendar mode, you must specify to immediately submit the request for review.

  * **Reservation mode**. This property defines the method to reserve resources, which you must set to `CALENDAR` for a request in calendar mode.

  * **Reservation name**. The name for the reservation that Compute Engine automatically creates if Google Cloud approves your request.

  * **Share type**. This property defines if other projects in your organization can consume the auto-created reservation for your approved request. You can specify one of the following options:

    * **Single-project**. Only your project can consume the reserved capacity.

    * **Shared**. You can share the reserved capacity with up to 100 other projects in your organization. If you specify this option, then you must specify the projects to share the auto-created reservation with. For more information, see the [best practices for shared reservations](https://docs.cloud.google.com/compute/docs/instances/best-practices-shared-reservations).

  * **Reservation period**. The date and time when Compute Engine provisions your requested capacity, and you can consume it. The reservation period includes the following:

    * **Start time**. When you want to start consuming your reserved capacity. Based on the resources that you reserve, the start time must be at least one of the following values from when you create and submit a request:

      * For GPU and H4D VMs, 87 hours (three days and 15 hours)

      * For TPUs, six hours

    * **End time**. When your requested capacity is no longer reserved for you. At this time, Compute Engine deletes the auto-created reservation, and stops or deletes any VMs that consume the reservation based on the [termination action](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm) that you specified for the VMs.

  * **Resource properties**. The hardware requirements of the GPU VMs, H4D VMs, or TPUs that you want to reserve. VMs can only use a reservation if their properties match the reservation's properties. For more information, see the [requirements to consume reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type#requirements).

  * **Zone**. The zone where you want to reserve capacity.




## Request review process

To reserve capacity by using a future reservation request in calendar mode, you must create and submit the request to Google Cloud for review. After you create and submit a request, Google Cloud reviews it within a minute, and then one of the following occurs:

  * **Google Cloud approves your request** : Compute Engine reserves your requested resources and, within a minute after approval, automatically creates an empty reservation. Unless you [cancel your request](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations-calendar-mode#cancel), Compute Engine provisions your requested capacity by increasing the number of GPU VMs, H4D VMs, or TPUs in the reservation at the request's start time.

  * **You encounter an error**. The request fails because the request's zone lacks sufficient resources. We recommend that you view future resource availability again, and then create and submit a new request for review.




## Request lifecycle

The following diagram shows the different states that Compute Engine can set a future reservation request in calendar mode to:

[ ![A flowchart that shows the different states that a future reservation request in calendar mode can go through.](https://docs.cloud.google.com/static/compute/images/reservations/request-calendar-mode-states.png)](https://docs.cloud.google.com/static/compute/images/reservations/request-calendar-mode-states.png)

The states and flow of events shown in the preceding diagram are as follows:

  * **`PENDING_APPROVAL`** : you created and submitted a request for review. Within a minute, Google Cloud approves the request.

  * **`APPROVED`** : Google Cloud has approved your request. Then, within a minute, Compute Engine creates an empty reservation and changes the request state to `PROCURING`.

  * **`PROCURING`** : Compute Engine schedules the provisioning of your reserved resources. To prevent this provisioning, you can [cancel your request](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations-calendar-mode#cancel) if it meets one of the following conditions:

    * The start time is more than 30 days away.

    * You cancel the request within 24 hours after approval, and the start time is at least four days away.

Before the request reaches its start time, the request state changes to `PROVISIONING`.

  * **`CANCELLED`** : you canceled your request while it was in the `PROCURING` state. This action releases your reserved capacity and you don't incur charges for it. You can retain your request for future reference, or delete it if you no longer need it.

  * **`PROVISIONING`** : Compute Engine is provisioning your reserved resources by increasing the number of reserved GPU VMs, H4D VMs, or TPUs in the auto-created reservation. When the request reaches its start time, the request state changes to `FULFILLED`.

  * **`FULFILLED`** : Compute Engine has provisioned your reserved resources, and you're charged for them. You can consume the auto-created reservation by creating VMs until the request end time.




When the request reaches its end time, Compute Engine deletes the auto-created reservation, and it stops or deletes any VMs that consume the reservation based on the [termination action](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm) that is configured in the VMs. You can retain the request in calendar mode for record, or delete the request if you no longer need it.

## Consume provisioned capacity

After Google Cloud approves a future reservation request in calendar mode, Compute Engine automatically creates a reservation with the following characteristics:

  * The auto-created reservation has no reserved GPU VMs, H4D VMs, or TPUs; you can't consume it yet.

  * The auto-created reservation inherits the VM or TPU properties specified in your request.




At the request start time, Compute Engine provisions your requested capacity by increasing the number of GPU VMs, H4D VMs, or TPUs in the auto-created reservation. You can then consume the reservation by creating GPU VMs, H4D VMs, or TPU VMs that meet all of the following conditions:

  * The VMs and the reservation have [matching properties](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements).

  * The VMs [specifically target the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

  * The VMs use the [reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

  * The VMs must be [stopped or deleted at the reservation end time](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm).




You can create VMs until the reservation is fully consumed or until the request end time. At the request end time, Compute Engine deletes the auto-created reservation, and stops or deletes any VMs that consume the reservation.

## Quota

Quota requirements for future reservation requests in calendar mode depend on the machine type as follows:

  * **GPU and TPU machine types** : no quota is required to reserve capacity.

  * **H4D machine types** : [CPU quota](https://docs.cloud.google.com/compute/resource-usage#cpu_quota) is consumed.




When you create VMs by consuming reserved capacity, you must have sufficient quota for any resources that aren't part of your reservation, such as disks or IP addresses. Otherwise, creating VMs fails.

## Pricing

When you create and submit a future reservation request in calendar mode, and Google Cloud approves your request, you don't immediately incur charges. Instead, you incur charges when the following occurs:

  * **Compute Engine provisions your requested capacity**. When your request reaches the `FULFILLED` state at the request's start time, you incur charges for the provisioned resources according to [DWS pricing](https://cloud.google.com/products/dws/pricing). This pricing model offers vCPUs, memory, GPUs, and TPUs at a discounted price compared to standard pricing.

  * **You use resources outside of the reservation**. When you create VMs that consume an auto-created reservation, you don't incur additional charges for the consumed resources. You only incur charges for resources that aren't part of the reservation, such as disks or IP addresses.




You stop incurring charges for the reserved resources at the request end time. At this time, Compute Engine deletes the auto-created reservation, and stops or deletes any VMs that consume the reservation based on their termination action.

**Caution:** If you configure a VM's termination action to stop the VM, then Compute Engine stops the VM at the end of the reservation period. You continue to incur charges for any resources that are attached to the VM, such as disks or IP addresses. To avoid unnecessary charges, detach and delete resources that you no longer need.

## Limitations

The following sections explain the limitations for future reservation requests in calendar mode.

### Limitations for all requests

All future reservation requests in calendar mode have the following limitations:

  * You can reserve resources for a period between 1 and 90 days.

  * After you submit a request and Google Cloud approves it, the following limitations apply:

    * You can cancel the request if it meets one of the following conditions:

      * The start time is more than 30 days away.

      * You cancel the request within 24 hours after approval, and the start time is at least four days away.

    * You can delete the request after you cancel it or after it reaches its end time.

    * You can't modify the request.




### Limitations for requests for GPU or H4D VMs

You can only reserve GPU VMs or H4D VMs as follows:

  * You can reserve the following number of VMs per request:

    * For GPU VMs, between 1 and 80 VMs

    * For H4D VMs, between 1 and 256 VMs

  * You can reserve the following machine series:

    * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms)

    * [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms)

    * [A3 Mega](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms)

    * [A3 High with 8 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms)

    * [A3 Edge](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms)

    * [H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series)

  * You can reserve GPU or H4D VMs only in specific regions and zones:

    * For GPU VMs, see [GPU locations](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones).

    * For H4D VMs, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

**Important:** If GPU or H4D VMs aren't available in any region after you [ view future availability](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#view-availability), then contact your account team or the sales team. 
  * You can't use an instance template to create requests for GPU or H4D VMs.




### Limitations for requests for TPU VMs

You can only reserve TPU VMs as follows:

  * You can reserve 1, 4, 8, 16, 32, 64, 128, 256, 512, or 1,024 TPU chips per request.

  * You can reserve the following TPU versions:

    * [TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x)

    * [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e)

    * [TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p)

  * You can reserve TPUs only in specific regions and zones. For more information, see [TPU locations](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones).

**Important:** If TPU chips aren't available in any region after you [ view future availability](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#view-availability), then contact your account team or the sales team. 



### Limitations for all auto-created reservations

An auto-created reservation for a request has the following limitations:

  * You can modify the reservation only after it reaches its start time. After this point, you can make the following changes:

    * Allow or disallow jobs in Vertex AI from consuming the reservation.

    * Convert a single-project reservation into a shared reservation, or a shared reservation into a single-project reservation.

  * You can't apply committed use discounts (CUDs) or sustained use discounts (SUDs) to the reservation.

  * You can't delete the reservation; Compute Engine deletes it when the reservation reaches its end time.




## What's next

  * [Create a future reservation request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode)

  * [Delete a future reservation request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations-calendar-mode)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
