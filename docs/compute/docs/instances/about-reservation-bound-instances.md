---
url: https://docs.cloud.google.com/compute/docs/instances/about-reservation-bound-instances/
title: About instances that use the reservation-bound model \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:09:31.046926+00:00
---

# About instances that use the reservation-bound model  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/about-reservation-bound-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About instances that use the reservation-bound model Stay organized with collections  Save and categorize content based on your preferences. 

This document describes Compute Engine instances that use the reservation-bound provisioning model, including their benefits and creation requirements.

When you create a compute instance, you must specify the underlying [provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models), which defines the availability, pricing, and lifespan for the resources that your compute instance uses. The reservation-bound provisioning model lets you create compute instances by using reserved capacity from a [future reservation in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview) or a [future reservation for capacity blocks](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type#reserve-capacity-aihc).

The reservation-bound provisioning model offers the following benefits:

  * **Cost control** : you don't incur additional charges when you create compute instances by using reserved capacity. You only incur charges for resources that aren't part of your reservation, such as disks or IP addresses.

  * **Lifecycle management** : based on the termination action that you specify when you create compute instances, Compute Engine stops or deletes the compute instances at the end of the reservation period.




## Understand instances that use the reservation-bound provisioning model

The following sections describe the requirements that you apply when you create compute instances by using the reservation-bound provisioning model.

### Compute instance creation prerequisites

To use the reservation-bound provisioning model to create compute instances, you must first reserve resources. You can reserve resources as follows:

  * To reserve up to 80 A4, A3 Ultra, A3 Mega, A3 High with 8 GPUs, or A3 Edge instances, up to 256 H4D instances, or up to 1,024 TPU7x, TPU v6e, or TPU v5p chips for up to 90 days, use [future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

  * To reserve A4X Max, A4X, A4, A3 Ultra, A3 Mega, A3 High with 8 GPUs, A3 Edge, H4D, TPU7x, TPU v6e, or TPU v5p instances for any duration or quantity, use [future reservations for capacity blocks](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type#reserve-capacity-aihc).




If Google Cloud approves your future reservation request, then Compute Engine automatically creates (_auto-creates_) a reservation at the start of your reservation period. You can then use the reservation to create compute instances.

### Compute instance creation requirements

To create a compute instance by using the reservation-bound provisioning model, you must specify the following configurations:

  * **The compute instance and the reservation must have matching properties**. You can only use your reserved capacity to create instances if the instance and auto-created reservation properties _exactly_ match. For more information, see the [requirements for consuming reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements).

  * **The compute instance must specifically target the reservation for consumption**. When you create a compute instance, you must specify the name of the auto-created reservation to target for consumption, as well as set the `reservationAffinity` field to `SPECIFIC_RESERVATION`. For more information, see [Consume a specifically targeted reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

  * **The compute instance must use the reservation-bound provisioning model**. When you create a compute instance, you must specify the reservation-bound provisioning model as follows:

    * If you use the Google Cloud console, then, in the **Provisioning model** list, select **Reservation-bound**.

    * If you use the Google Cloud CLI, then include the `--provisioning-model=RESERVATION_BOUND` flag in the command.

    * If you use the Compute Engine API, then include the `"provisioningModel": "RESERVATION_BOUND"` field in the request body.

  * **The compute instance must be stopped or deleted at the reservation end time**. When you create a compute instance, you must specify whether to stop or delete the compute instance at the reservation's end time by using the `instanceTerminationAction` field. For more information, see how to [limit the run time of a compute instance](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm).




After you create a compute instance by using the reservation-bound provisioning model, the compute instance starts running and keeps running until you stop or delete it, or until the Compute Engine stops or deletes the compute instance at the reservation's end time.

## Quota

When you create a compute instance by using the reservation-bound provisioning model, you don't need quota for the reserved resources that you use to create the compute instance. You only need quota for the resources that aren't part of your reserved capacity, such as disks and IP addresses. For more information about the different types of quota, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage).

## Pricing

When you create a compute instance by using the reservation-bound provisioning model, you incur charges as follows:

  * **Charges start when you create the compute instance**. You don't incur additional charges for the reserved resources that you use to create your compute instance. You only incur charges for the resources that aren't part of the reservation, such as disks or IP addresses. For more information, see the [billing for reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing).

  * **Charges stop at the reservation's end time**. At that time, Compute Engine deletes the reservation, and stops or deletes your compute instance based on the termination action that is specified in the compute instance.

**Important:** After Compute Engine stops a compute instance and changes its state to `STOPPING`, you continue to incur charges for any resources that are attached to the compute instance, such as disks. To avoid unnecessary costs, detach and delete any resources that you no longer need, or delete the compute instance altogether. For more information, see the [pricing for a compute instance's uptime](https://docs.cloud.google.com/compute/vm-instance-pricing#instanceuptime).



## Limitations

To create compute instances by using the reservation-bound provisioning model, you must use one of the following machine series or TPU versions:

  * GPUs:

    * A4X Max

    * A4X

    * A4

    * A3 Ultra

    * A3 Mega

    * A3 High with 8 GPUs

    * A3 Edge

To inquire about using other GPU machine series with the reservation-bound provisioning model, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact).

  * TPU versions:

    * TPU7x

    * v6e

    * v5p

  * H4D




## What's next

  * [Create an instance with the reservation-bound model](https://docs.cloud.google.com/compute/docs/instances/create-reservation-bound-instance)



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
