---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption/
title: Troubleshoot reservation consumption \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:27.548738+00:00
---

# Troubleshoot reservation consumption  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot reservation consumption Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to resolve issues with consuming [reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

## Fewer compute instances available for consumption

**Issue** : The number of physically reserved Compute Engine instances (the `assuredCount` field) is less than the number of compute instances that are specified in the reservation (the `count` field). This discrepancy means that you have fewer compute instances available than expected for your project, and for any project with which a reservation is shared.

This issue can occur for one or more of the following reasons:

  * **Google Cloud suspended a consumer project or a user migrated it**. Google Cloud has [suspended](https://docs.cloud.google.com/resource-manager/docs/project-suspension-guidelines) a project with which the reservation is shared, a _consumer project_ , or a user [migrated the consumer project to another organization](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#how-shared-reservations-work). In these cases, Compute Engine decreases the `assuredCount` field in the reservation by the number of compute instances that the consumer project was consuming before the migration or suspension.

  * **Google Cloud suspended the owner project**. Google Cloud has suspended the project in which the reservation exists, the _owner project_. In this case, Compute Engine sets the `assuredCount` field in the reservation to `0`.

  * **A hardware or host error impacted the reservation**. In this case, Compute Engine does both of the following in the reservation:

    * Compute Engine sets the `status` field to `DEGRADED`.

    * Compute Engine decreases the `assuredCount` field by the number of impacted hosts.




**Resolution** : Unless the owner project for your reservation is suspended, Compute Engine makes best-effort attempts to resolve the discrepancy between the `assuredCount` and `count` fields within 24 hours. During this time, Google Cloud bills you only for the physically reserved capacity that's shown in the `assuredCount` field. If this issue isn't resolved within 48 hours, then contact your [account team](https://cloud.google.com/tam) or [support](https://docs.cloud.google.com/support).

## Issues for compute instances not consuming reservations

If a compute instance can't consume a reservation, then it might be due to one or more of the following issues:

  * The reservation is degraded

  * The reservation and compute instance's properties don't match

  * The compute instance's reservation affinity is incorrect

  * The reservation is already fully consumed

  * The quota for the shared reservations is exceeded




This section describes how to identify and resolve each of these issues, and how to verify reservation consumption.

### Degraded reservation

**Issue** : You attempt to create a compute instance by consuming a reservation, but creating the compute instance fails with one of the following errors:
    
    
    BACKEND_ERROR
    
    
    
    GCE_STOCKOUT
    
    
    
    INFEASIBLE
    
    
    
    QUOTA_ERROR
    
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED
    

Additionally, when you [view the details of the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-reservations), the value of the `status` field is set to `DEGRADED`. This value indicates that some of the physically reserved machines in your reservation have encountered a hardware or host error. In this state, you can use the reservation to create compute instances only up to the number that is specified in the `assuredCount` field. Until the issue is resolved, Google Cloud bills you only for the number of reserved compute instances that's indicated in the `assuredCount` field.

**Resolution** : Compute Engine makes best-effort attempts to resolve the issue within 24 hours. If the `status` field in your reservation is still set to `DEGRADED` after 48 hours, then contact your [account team](https://cloud.google.com/tam) or [support](https://docs.cloud.google.com/support) for guidance.

### Mismatched compute instance properties

**Issue** : A compute instance can't consume a reservation with different [compute instance properties](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements).

To identify which properties aren't matching between the compute instance and reservation, view the properties of the reservation and the compute instance by doing the following:

  1. [View the details of the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#describe-reservations)

  2. [View the details of the compute instance](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)




Then, compare the two outputs to verify that the following properties _exactly_ match:

  * `project`

    * If the reservation is shared with multiple projects (specifically, if the reservation has the`shareType` field set to `SPECIFIC_PROJECTS`), then the compute instances can be located in the project where the reservation was created (the owner project), or in any projects that the reservation is shared with (consumer projects).
  * `zone`

  * `machineType`

  * `guestAccelerators.acceleratorType` (if any)

  * `guestAccelerators.acceleratorCount` (if any)

  * `minCpuPlatform`

    * The compute instance and reservation must have the exact same `minCpuPlatform` configuration. For example, setting `minCpuPlatform` to `Intel Broadwell` when creating a compute instance won't match the `minCpuPlatform` value of `Automatic` within a reservation.
  * `localSsds.interface` (if any)

    * The reservation and compute instance must have the same number of Local SSD disks with a matching `localSsds.interface` property for each Local SSD disk.
  * `resourcePolicies` (if any)

    * Only if a reservation specifies a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies).
  * `locationHint` (if any)

    * Only if a reservation specifies the `locationHint` field. You can specify the `locationHint` field only when creating compute instances by using the REST API.



**Resolution** : After identifying the properties that don't match, try one of the following:

  * If the compute instance properties don't match the reservation, then do one of the following:

    * [Delete the compute instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) and create a new compute instance with properties that match the reservation's properties.

    * [Update the compute instance](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties) to match the reservation's properties.

  * If the reservation's properties are supposed to match the compute instance's properties, then [delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-delete#deleting_a_reservation) and [create a new reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project) that matches the compute instance's properties. Optionally, you can create a [specific reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation). When creating compute instances to consume a specific reservation, you encounter errors if the compute instance's properties don't match the reservation's properties.




After updating the compute instance or creating a new reservation, check if the compute instance is consuming the reservation by [verifying the reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption).

### Reservation affinity is incorrect

**Issue** : The [reservation affinity](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_reserved_instances) of the compute instance is misconfigured. The reservation affinity of a compute instance controls the reservations that a compute instance can consume. To check your compute instance's reservation affinity, do the following:

  1. [View the details of a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#describe-reservations) and verify if the reservation is an automatically consumed or specific reservation. For more information, see [Consumption type](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type).

  2. [View the details of the compute instance](https://docs.cloud.google.com/compute/docs/instances/view-vm-details) and verify the reservation affinity.




**Resolution** : If the reservation affinity of the compute instance and the reservation don't match, then do one of the following:

  * Create a new compute instance with a reservation affinity property that matches the reservation's type.

  * [Update the `reservationAffinity` property in the compute instance](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties) to specify whether the compute instance can consume any matching reservation or a specific reservation. To finalize the compute instance's update, you must restart the compute instance.




To check if the compute instance is consuming the reservation, see [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption).

### Reservation is already fully consumed

**Issue** : The number of compute instances consuming this reservation matches the reservation's total number of reserved compute instances. This indicates that the reservation is fully consumed.

**Resolution** : To verify if the reservation is fully consumed, [view the details of the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#listing_and_describing_reservations), and then verify that the number of compute instances consuming the reservation matches the total number of reserved compute instances in the reservation.

If the reservation is fully consumed, then try one of the following:

  * Increase the number of reserved compute instances by [modifying the number of reserved compute instances in a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#resizing_a_reservation).

  * If the reservation already reserves the [maximum number of compute instances](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#max-vm-count-exceeded), then create a new reservation.

  * Reduce the number of compute instances that are consuming the reservation. For more information, see Compute instances unintentionally consuming reservations.




If the reservation isn't fully consumed but the compute instance isn't consuming the reservation, then you can further troubleshoot the issue by doing the following:

  1. [Create a specific reservation with matching properties](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

  2. Create a compute instance to consume the reservation. If the compute instance and the reservation properties don't match, then creating the compute instance fails.




### Resource quota exceeded for shared reservations

**Issue** : A compute instance isn't consuming a shared reservation because your project doesn't have sufficient quota for the resources that you're trying to consume.

**Resolution** : Shared reservations have [additional quota requirements](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements-shared-reservations). If you need to increase quota in your project to consume the reserved resources, then see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase) in the Cloud Quotas documentation.

## Compute instance count not restored after stopping or deleting a compute instance

**Issue** : If you stop, suspend, or delete a compute instance that is consuming a reservation, then the operation must complete before the compute instance no longer counts against the reservation, and the previously consumed resources are again available for consumption.

**Resolution** : Wait for a few minutes for the stop, suspend, or delete operation on the compute instances to complete. Then, to verify that the stopped, suspended, or deleted compute instances no longer count against the reservation, check the total number of consumed compute instances in the reservation by using one of the following methods:

  * Recommended: [Monitor the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-monitor) and look for a change in the measurements of the reservation.

  * [View the details of the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#describe-reservations) and check if the value of the `inUseCount` field decreased. If its value didn't decrease, then one or more compute instances have started consuming the reservation while the stop, suspend, or delete operation was completing.




## Compute instance unintentionally consuming reservations

**Issue** : When you create [reservations that are automatically consumed](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_any_matching_reservation) (default), a compute instance might unintentionally consume these reservations.

**Resolution** : To avoid that one or more compute instances unintentionally consume a reservation, do one of the following:

  * [Create compute instances that can't consume any reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-prevent-consumption)

  * [Create reservations that can be consumed only when specifically targeted](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
