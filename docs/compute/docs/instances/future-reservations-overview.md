---
url: https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview/
title: About future reservation requests \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:09:33.436886+00:00
---

# About future reservation requests  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About future reservation requests Stay organized with collections  Save and categorize content based on your preferences. 

This document gives you an overview of future reservation requests. To learn more about the different types of reservations, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).

Use future reservations to request assurance of important or difficult-to-obtain capacity in advance.

## Overview

Compared to [on-demand reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview), future reservations provide you with an even higher level of assurance in obtaining capacity for Compute Engine zonal resources. With future reservations, you can request to reserve capacity starting on a specific date up to 1 year in the future. After you create a future reservation, Google Cloud reviews your request and, if approved, Compute Engine provisions the requested capacity on the date and time you specified. This process reserves the requested capacity exclusively for your project and any projects that you share the reservation with. For example, future reservations can be useful to do the following:

  * Migrate a large number of virtual machine (VM) instances.

  * Obtain highly-demanded resources.

  * Secure capacity for peak scale events.




Each future reservation provides a very high level of assurance for one or more VMs with the same properties in a specific zone. If Google Cloud approves a future reservation request, then, on the date you requested to have the reserved capacity available, Compute Engine subtracts any matching, existing reservations and running VMs, and it automatically creates reservations to reach the requested capacity specified in the future reservation. The new automatically created reservations can then be consumed just like on-demand reservations, and they prevent anyone else from using your reserved resources until they're deleted.

There are no additional costs for creating future reservation requests. You only start to pay when Compute Engine provisions the reserved resources, and you're charged at the same cost as on-demand reservations.

**Important:** If you can't access and use future reservations in the gcloud CLI or Compute Engine API, you might not be eligible to access and use future reservations at this time. In that case, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact).

## How future reservations work

The details of how future reservations work are outlined in the following sections.

### Future reservations properties

When you create a future reservation request, you must define the following properties:

  * **Name prefix**

The _name prefix_ specifies a string that Compute Engine adds to the start of the name of each auto-created reservation for your request. You can filter by one or more name prefixes to identify the auto-created reservations when you [view a list of reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view#list-reservations).

  * **Reservation affinity**

The _reservation affinity_ specifies how VMs consume the auto-created reservations that Compute Engine provisions for your future reservation after Google Cloud approves it and the future reservation reaches its start time. You can specify one of the following reservation affinities:

    * **Automatically consumed (`ANY_RESERVATION`)**: if the properties of a VM match the properties of an auto-created reservation, then the VM automatically consumes the reservation. This behavior applies to VMs in your project and in any project that you share the reservation with, as well as to new and existing VMs. If you delete the auto-created reservations after they reach their end time, then the VMs continue to run until you stop, suspend, or delete them. For more information, see [Consume an automatically consumed reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_any_matching_reservation).

    * **Specifically targeted (`SPECIFIC_RESERVATION`)**: to consume an auto-created reservation, a VM must target the reservation by name and the VM must have properties that match the reservation's properties. Otherwise, creating the VM fails. Before you can delete the auto-created reservations, you must stop, suspend, or delete all of the VMs that consume them. For more information, see [Consume a specifically targeted reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

**Caution:** If you delete a specifically targeted reservation after stopping or suspending the VMs that consume it, then you can't restart or resume those VMs. You can only restart or resume the VMs if you create a new specifically targeted reservation with the same name, owner project, zone, and properties as the deleted reservation.
  * **Reservation period**

The _reservation period_ defines the time period that Compute Engine holds your reserved capacity for. You must specify both of the following values:

    * **Start time** : the date and time when Compute Engine completes the creation of the auto-created reservations. At the start time, you can create VMs to consume the reservations. Choose a start time that gives you enough time to create the VMs before your workload needs them. The start time must be within one year of the date and time when you submit the future reservation request for review.

    * **End time** : the date and time when your reservation period ends. After this time, you can delete the future reservation request and its auto-created reservations. The end time must be at least 24 hours after the start time and has no upper limit. To increase the likelihood that Google Cloud approves your request, specify a recommended minimum reservation period.

  * **Share type**

The _share type_ specifies which projects can consume the auto-created reservations for your future reservation request. You can specify one of the following share types:

    * **Single-project** : VMs can consume the reserved capacity from the project where you create the future reservation request, and not from any other project. For more information, see [single-project reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project).

    * **Shared** : VMs can consume the reserved capacity from the _owner_ project, where you create the future reservation request, and from _consumer_ project(s), which can be any project that you share the request with. You can share a future reservation request with up to 100 consumer projects that are in the same Google Cloud organization as the owner project. For more information, see [shared reservations](https://docs.cloud.google.com/compute/docs/instances/best-practices-shared-reservations).

  * **Total count**

The _total count_ specifies the total number of VMs with the specified properties that you want to reserve in the zone at the start time. Based on the reservation affinity that you specify, Compute Engine provisions capacity as follows:

    * **Automatically consumed reservations** : Compute Engine treats this value as a total capacity target. Compute Engine subtracts existing, matching VMs and reservations in your project and any projects that you share the reservation with, and provisions capacity for the remaining count.

    * **Specifically targeted reservations** : Compute Engine treats this value as incremental capacity. Compute Engine provisions the full count of VMs and doesn't subtract existing, matching reservations or VMs.

For more information, see how Compute Engine counts and provisions reserved resources in this document.

**Note:** Each auto-created reservation supports up to 1,000 VMs. If you request a total count greater than 1,000, then Compute Engine creates multiple auto-created reservations to fulfill your request.
  * **VM properties**

The _VM properties_ define the hardware requirements, such as memory and CPUs, and optional resources, such as Local SSD disks and GPUs, for the VMs that you want to reserve. When you create a future reservation request, you can specify these properties, copy them from an existing VM, or use an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates). To consume an auto-created reservation, a VM must have properties that [match all properties of the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements).

  * **Zone**

The _zone_ specifies the location where you want to reserve capacity. The combination of zone and machine type that you specify affects the likelihood that Google Cloud approves your future reservation request. For more information, see Future reservations review process in this document.




In addition, you can define the following optional properties:

  * **Auto-delete**

The _auto-delete_ option specifies whether Compute Engine deletes the auto-created reservations for your request after the end time, even if VMs consume them. If you enable this option, then Compute Engine deletes the auto-created reservations after the specified deletion time, within two hours. This option helps you avoid charges for unconsumed reservations.

  * **Description**

The _description_ specifies optional text that describes your future reservation request.

  * **Planning status**

The _planning status_ specifies whether you want to save your future reservation request as a draft or submit it to Google Cloud for review. For more information, see Future reservations status in this document.




### Future reservations status

This section specifies the possible states that a future reservation request can be set to. A future reservation request contains the following status fields:

  * Planning status

This section explains the planning status, which you specify when creating a future reservation request. The planning status specifies if a future reservation request is in a draft state or was submitted to Google Cloud for review.

  * Procurement status

This section explains the procurement status, which is set by Compute Engine after you create a future reservation request. At first, the procurement status field displays the approval status of a future reservation request. After Google Cloud approves a future reservation request and the request enters its lock time, this field displays the procurement status of the requested resources.




#### Future reservations planning status

When creating a future reservation request, you can set its planning status (`planningStatus`) to one of the following values:

  * **Draft** (`DRAFT`): By default, you create a draft future reservation request. You can modify the draft of a future reservation request as needed and, when you're satisfied with your changes, you can submit it to Google Cloud for review. Google recommends creating a draft request first as this lets you determine the number of VMs that Compute Engine will provision for the request instead of manually estimating this number, and optionally modify the number of reserved VMs in the request before submitting it for review.

  * **Submitted** (`SUBMITTED`): The future reservation request was submitted for review to Google Cloud. After you submit a future reservation request for review, you can't change its planning status back to `DRAFT`. Optionally, you can immediately submit a future reservation request for review when creating it.




#### Future reservations procurement status

After creating a future reservation request, Compute Engine sets its procurement status (`procurementStatus`) to one of the following values:

  * **Drafting** (`DRAFTING`): The future reservation request is in its draft state.

  * **Pending approval** (`PENDING_APPROVAL`): The future reservation request is submitted for approval to Google Cloud. While the request is in review, the procurement status of a future reservation request can be set to one of the following:

    * **Declined** (`DECLINED`): Google Cloud has declined the future reservation request. You can still modify the future reservation request and, after you've finalized your changes, submit it again for approval.

    * **Approved** (`APPROVED`): Google Cloud has approved the future reservation request and Compute Engine plans to provision the auto-created reservations with the requested capacity at the start time of the reservation period. If Google Cloud approves the future reservation request within 56 days (8 weeks) from its start time, then the future reservation enters its lock time within a few minutes.

    * **Canceled** (`CANCELED`): A user canceled the future reservation request during review, or after Google Cloud approved or declined it.

After a future reservation request is approved or declined, you can modify one or more properties of the future reservation request and submit it again to Google Cloud for review. This action sets the status of the future reservation back to pending approval.

  * **Procuring** (`PROCURING`): 56 days (8 weeks) from the start time of its reservation period, a future reservation enters its lock time. After the future reservation enters this state:

    * You can't cancel the future reservation anymore.

    * You can only delete the future reservation after its end time.

    * If you want to modify the reservation period, the share settings, the total count, or the VM properties of the future reservation, you must request approval from Google Cloud. After then, Google Cloud approves or declines your request by changing its update status. If Google Cloud declines a request and you don't submit new ones, Compute Engine provisions the reserved resources using the previously-specified properties.

If a future reservation specifies a reservation period that is less than 56 days from the date and time you submit a future reservation request, then the future reservation enters its lock time within a few minutes after approval.

  * **Provisioning** (`PROVISIONING`): 24 hours before the start time specified in a future reservation, Compute Engine starts to provision the requested resources by automatically creating reservations. Then, Compute Engine sets the procurement status of the future reservation to one of the following:

    * **Fulfilled** (`FULFILLED`): Compute Engine has provisioned all the resources required to reach the total count specified in the future reservation.

    * **Partially fulfilled** (`FAILED_PARTIALLY_FULFILLED`): Compute Engine has only provisioned part of the resources required to reach the total count specified in the future reservation because of insufficient quota.

    * **Failed** (`FAILED`): Compute Engine has failed to provision the reserved resources.

**Important:** If Compute Engine can only partially provision or fails to provision the reserved resources, then contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact).

The auto-created reservations can be consumed at the start time. To make sure you have the total capacity requested, identify any unconsumed auto-created reservations and create VMs to consume them. You can only modify or delete an auto-created reservation after the end time specified in the future reservation. For more information, see How Compute Engine provisions resources in this document.




### Future reservations updates

After creating a future reservation request, you can optionally update it—cancel it, delete it, modify it, or request to modify it. However, you can only update future reservation requests during certain time frames, as explained in the following sections.

#### Future reservation lock time

After you submit a future reservation request, you can cancel or delete it any time before Google Cloud starts procuring (`PROCURING`) its resources, at which point the future reservation enters its lock time. During the lock time for a future reservation, you can no longer cancel it and can't delete it until after its end time.

Additionally, the lock time affects when you can request modifications. The lock time for a future reservation request begins at one of the following times:

  * If the future reservation request specifies a start time that is less than 56 days (8 weeks) away from when it's submitted, the future reservation request enters the lock time shortly after it's approved.

  * Otherwise, the lock time for the future reservation request begins 56 days from its start time.




#### Future reservation modification

If a future reservation request isn't canceled or pending approval, then you can modify the request at any time before it reaches a procurement status of Provisioning (`PROVISIONING`).

After a future reservation request is approved, you can modify the following properties only if you request a modification from Google Cloud:

  * GPUs and GPU type

  * Local SSD disks and the disk interface type

  * Machine series and machine type

  * Minimum CPU platform

  * Share settings

  * Start and end time of the reservation period

  * Total count (Number of VMs)

**Note:** You can only modify GPUs, Local SSD disks, machine series and type, and minimum CPU platform in a future reservation request if you didn't create the request using an instance template. Otherwise, you must create a new future reservation request.



You can only request one modification (of one or more properties) for an approved future reservation at a time. Additionally, if you submit the following types of modification requests, Google Cloud is likely to decline them:

  * Any requests made within 72 hours of the start time.

  * Any requests to modify VM properties made within 14 days of the start time.

  * Any requests to significantly increase or decrease the total count made within 14 days of the start time.




Submitting a modification request creates the update status (`AmendmentStatus`) field in the future reservation. After Google Cloud reviews the request, Compute Engine sets the update status to one of the following values:

  * **Update pending approval** (`AMENDMENT_PENDING_APPROVAL`): Google Cloud is reviewing your request.

  * **Update approved** (`AMENDMENT_APPROVED`): Google Cloud has approved your request. Compute Engine will provision the reserved resources using the approved properties.

  * **Update declined** (`AMENDMENT_DECLINED`): Google Cloud has declined your request. Unless you submit a new request and the request is approved, Compute Engine provisions the reserved resources using previously-approved properties.




To learn more about how to modify future reservation requests and the properties that you can modify, see [Modify future reservation requests](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations).

### Future reservations review process

To provision the requested capacity, you must submit any future reservation requests to Google Cloud for review. Google Cloud typically takes five days to review your request. If Google Cloud needs more time or has questions, then your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact) will contact you.

If a future reservation request or modification request is approved, then Google Cloud uses commercially reasonable efforts to make your requested capacity available at the start time of the future reservation's reservation period. Google Cloud prioritizes the delivery of your reserved capacity over other customers without approved future reservations with the same properties. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms).

To increase the likelihood that Google Cloud approves a future reservation request, make sure to specify the following when creating or modifying a future reservation request:

  * A recommended start time

  * A recommended minimum reservation period




#### Recommended start time

56 days (8 weeks) from the start time of its reservation period, any approved future reservation request enters a lock time. If the start time specified in an approved future reservation is less than 56 days from the date and time you submit a future reservation request for review, then the future reservation request enters its lock time within a few minutes from approval.

To have enough time to cancel or delete a future reservation request, as well as submit a modification request, specifying a start time that is more than 56 days from the date and time you submit a future reservation request for review is recommended.

#### Recommended minimum reservation period

When you create or modify a future reservation request, you must specify a reservation period of at least 24 hours. However, to increase your chances that Google Cloud approves your future reservation request, we recommend that you specify a reservation period of 365 days or longer.

## How Compute Engine provisions reserved resources

This section explains how Compute Engine provisions the reserved resources:

  * Count and provision reserved resources

This section explains how Compute Engine accounts for existing future reservations, reservations, and VMs that match your request when provisioning the total count of resources for an approved future reservation.

  * Auto-created reservations

This section explains the type of reservations that Compute Engine creates for an approved future reservation at its start time.




### Count and provision reserved resources

How Compute Engine provisions capacity for an approved future reservation depends on the reservation affinity that you specify in your request:

  * Total count for automatically consumed reservations

  * Total count for specifically targeted reservations




#### Total count for automatically consumed reservations

If your future reservation request specifies to automatically create automatically consumed reservations, then Compute Engine treats the total count as a capacity target across your specified projects. To reach the total count of an approved future reservation, Compute Engine does the following:

  1. Compute Engine subtracts any matching existing (consumed and unconsumed) reservations that are only shared with (some or all of) the projects specified in the future reservation.

  2. Compute Engine automatically creates reservations for the remaining amount. This means the following:

     * Any existing matching VMs start consuming the auto-created reservations.

     * You'll need to create matching VMs for any auto-created reservation that wasn't consumed.




For example, suppose that you create a shared future reservation request in zone `us-central1-a`. This future reservation request specifies a total count of 10 VMs with `n2-standard-2` machine type, project A as the owner project, and projects B and C as the consumer projects. After this future reservation request is approved and Compute Engine starts creating reservations at the start time of the reservation period, suppose that these projects contain the following resources with VM properties that match the future reservation:

  * In project A, 1 running VM that is _not_ consuming a reservation.

  * In project B, 1 unconsumed shared reservation with project C for 2 VMs.

  * In project C, 1 unconsumed single-project reservation for 1 VM.




In this scenario, Compute Engine automatically creates a shared reservation for 7 VMs to reach a total count of 10 VMs at the start time.

**Caution:** 24 hours before the start time of a future reservation's reservation period, Google doesn't recommend deleting or modifying existing, matching reservations for the projects specified in your future reservations. Otherwise, Compute Engine might not have enough notice to account for your requested capacity.

To learn how to determine the number of VMs that Compute Engine plans to provision for an existing future reservation request, see [Consumable instances in a future reservation request](https://docs.cloud.google.com/compute/docs/instances/reservations-view#number-instances-future-reservation).

#### Total count for specifically targeted reservations

If your future reservation request specifies to automatically create reservations as specifically targeted reservations, then Compute Engine provisions all of the VMs that you requested as additional capacity. For this reservation type, Compute Engine doesn't subtract existing, matching reservations or running VMs from your requested count. In addition, existing VMs don't automatically consume the auto-created reservation at the start time. To consume the reserved capacity, you must create VMs to target the auto-created reservations by name.

### Auto-created reservations

24 hours before the start time specified in a future reservation, Compute Engine starts provisioning the requested capacity in an approved future reservation by automatically creating reservations, but you're only charged for the auto-created reservations at the start time. Each auto-created reservation has the following properties:

  * The reservation can be consumed by creating VMs with [matching properties](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements).

  * The reservation has matching VM properties as the ones specified in its future reservation request.

  * The reservation matches the share settings of its future reservation request. Specifically:

    * If you created a single-project future reservation request, each auto-created reservation is a single-project reservation.

    * If you created a shared future reservation request, each auto-created reservation is a shared reservation that specifies the same owner project and consumer projects.

  * The reservation name starts with the name prefix specified in its future reservation request.

  * If you enabled the auto-delete option when creating or modifying a future reservation request, each auto-created reservation specifies a `deleteAtTime` field set to the time when Compute Engine automatically deletes the auto-created reservation.




When an auto-created reservation reaches its start time, you can consume it the same way as an on-demand reservation. You can modify the reservation if your workload needs change. However, you can't modify the number of VMs in the reservation or its end time. For more information, see [Modify reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify).

**Caution:** 14 days before the start time of a future reservation, make sure that your project has sufficient quota for the resources that you reserved. Otherwise, Compute Engine might only provision part of the requested capacity at the start time. To verify that you have sufficient quota for your reserved capacity, [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).

## Restrictions

The restrictions for reservations are outlined in the following sections.

### Restrictions on creation

When creating a future reservation request, the following restrictions apply:

  * If you have existing reservations with matching properties, read the following:

    * If your project already contains auto-created or on-demand reservations, or these reservations are shared with your project, you can only create future reservation requests shared across all the projects specified in the existing reservations.

    * If your project already contains a single-project future reservation request, you can create single-project future reservation requests only.

    * If your project already contains a shared future reservation request, or a future reservation request is shared with your project, you can only create shared future reservation requests across the same projects. For example, a shared future reservation request in project A (the owner project) that is shared with projects B and C (the consumer projects), means that you can do the following:

      * Create another shared future reservation request in project A and share it with projects B and C.

      * Create a shared future reservation request in project B and share it with projects A and C.

      * Create a shared future reservation request in project C and share it with projects A and B.

  * You can create and submit future reservation requests only for the following machine series:

    * **Accelerator-optimized** : A3 Mega, A3 High (with 8 GPUs), A3 Edge, and G4

    * **Compute-optimized** : H3 and H4D

    * **General-purpose** : C3, C3D, C4, C4A, C4D, C4N, N4, N4A, and N4D

    * **Memory-optimized** : M3, M4, M4N, and X4

    * **Storage-optimized** : Z3 and Z4M

**Important:** Before you submit a future reservation request for GPU, H4D, or Z4M instances, you must contact your account team or the sales team to discuss your request. Otherwise, Google Cloud might decline your request.
  * You can't specify a reservation period that is shorter than 24 hours.

  * If you set the reservation affinity to automatically consumed (`ANY_RESERVATION`), then the reservation period can't overlap with another future reservation request that has matching VM properties and zone. This restriction applies whether the future reservation request exists in your project or is shared with your project.

  * You can't specify a start time that is after 1 year from the date and time you submit a future reservation request for review.

  * You can't specify placement policies.




### Restrictions after creation

After creating a future reservation request, the following restrictions apply:

  * If you move a project that created a future reservation request to a different organization and the future reservation hasn't entered its lock time yet, the future reservation request is deleted.

  * After a future reservation request is approved and enters its lock time, the following restrictions apply:

    * You can't cancel the future reservation anymore.

    * If you want to [attach auto-created reservations to a commitment](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds), the following restrictions apply:

      * You can purchase the commitment only during the last 24 hours before the start time of the reservation period.

      * You can attach only the auto-created reservations that have the auto-delete option disabled. If you enabled the auto-delete option when creating or modifying a future reservation request, you must disable the option.

    * You can only delete the future reservation after its end time.

  * After a future reservation enters its start time, you can only modify or delete the auto-created reservations provisioned for the future reservation after the end time.




## Billing

There are no additional costs for creating future reservation requests.

After a future reservation request is approved and enters its lock time, you commit to pay for the total provisioned capacity for the entire reservation period, unless you request Google Cloud to modify the number or the VM properties of the resources you're reserving before the start time of the reservation period. If Google Cloud approves the request, you then commit to pay for the updated requested capacity.

At the start time of a future reservation's reservation period, Google Cloud charges you _only_ for the auto-created reservations to reach the total count specified in the future reservation. If Compute Engine can only partially deliver the requested capacity, you're only charged for the provisioned resources.

Any auto-created reservation incurs charges as follows:

  * At the same rate as [on-demand reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing).

  * While the reservation exists, regardless of whether you use the reserved resources or not.

**Important:** You can't delete an auto-created reservation until the end time of a future reservation. Thus, you must commit to pay for an auto-created reservation at least until the end time.



## What's next

  * Learn how to create future reservation requests:

    * [Create future reservation requests for a single project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations).

    * [Create shared future reservation requests](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations).



  * Learn how to [reserve capacity from the actual or forecasted usage of your VMs](https://docs.cloud.google.com/capacity-planner/docs/create-future-reservations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
