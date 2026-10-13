---
url: https://docs.cloud.google.com/compute/docs/instances/provisioning-models/
title: Compute Engine instances provisioning models \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:52.024593+00:00
---

# Compute Engine instances provisioning models  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/provisioning-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Compute Engine instances provisioning models Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

When you create a Compute Engine instance, you must define the method, called _provisioning model_ , that you want to use to obtain your requested resources. Each provisioning model determines the availability, lifespan, and pricing of your compute instances.

This document explains the different provisioning models that you can specify when you create compute instances. By understanding these models, you can choose the best option for your workload.

**Tip:** To get AI-powered assistance when you evaluate which provisioning model best fits your workload and budget requirements, you can prompt Gemini in the Google Cloud console. For more information, see [Design compute infrastructure with Compute Advisor](https://docs.cloud.google.com/compute/docs/design-with-gemini).

## Available provisioning models

When you create a compute instance, you can specify one of the following provisioning models. If you don't specify a provisioning model, then Compute Engine uses the standard provisioning model by default.

  * Standard

  * Spot

  * Flex-start

  * Reservation-bound




The following table helps you compare the use cases and pricing for each provisioning model:

| Standard | Spot | Flex-start | Reservation-bound  
---|---|---|---|---  
Summary | 

  * Based on resource availability, you can immediately create compute instances.
  * You can control when to stop or delete compute instances.

| 

  * Based on resource availability, you can immediately create compute instances.
  * You can control when to stop or delete compute instances. However, you also allow Compute Engine to stop or delete compute instances at any time to reclaim capacity.

| 

  * Based on resource availability, you can create compute instances within a specified waiting time. For a standalone Flex-start VM, you can specify a waiting time of up to two hours. For a MIG, Compute Engine keeps trying to create compute instances until resources become available or you cancel your creation request. 
  * You can control when to stop or delete compute instances. However, you can't suspend or recreate them. Compute instances run for a minimum of 10 minutes and up to a maximum of seven days. When the compute instances reach the end of their run duration, Compute Engine stops or deletes them based on their termination action.

| 

  * You can request to reserve capacity at a future date for creating compute instances. If Google Cloud approves your request, then Compute Engine creates a reservation. At the start of the reservation period, you can consume the reservation by creating compute instances that match the reservation.
  * During the approved reservation period, you can stop, restart, delete, and recreate compute instances to consume the reservation as needed. When the reservation period ends, Compute Engine deletes the reservation, and stops or deletes any compute instances that consume the reservation based on their termination action.

  
Use cases |  Ideal for workloads that require stability and continuous operation, such as the following workloads:

  * Web servers
  * Databases
  * Enterprise applications
  * Development and testing

|  Ideal for workloads that can tolerate interruptions, such as the following workloads:

  * Batch processing
  * High performance computing (HPC)
  * Continuous integration and continuous deployment (CI/CD)
  * Data analytics
  * Media encoding
  * Online inference

|  Workloads that require stability and need to run for no more than seven days, such as the following workloads:

  * Small model pre-training
  * Model fine-tuning
  * HPC simulation
  * Batch inference

|  Ideal for workloads that require stability and a specific run time, such as the following:

  * **For workloads that last up to 90 days** :
    * Model pre-training jobs
    * Model fine-tuning jobs
    * HPC simulation workloads
    * Short-term expected increases in inference workloads
  * **For workloads longer than 90 days** :
    * Training workloads
    * Inference workloads

  
Resource allocation | **Best-effort**. Compute Engine physically places resources close to each other on a best-effort basis. To control placement, you can optionally use [placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).  | **Best-effort**. Compute Engine physically places resources close to each other on a best-effort basis. To control placement, you can optionally use [placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).  | **Dense on a best-effort basis**. Compute Engine makes best-effort attempts to densely place resources close together. To control placement for your Flex-start VMs, you can optionally use one of the following: 

  * **For standalone Flex-start VMs** : [ compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies)
  * **For Flex-start VMs in a MIG** : [workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies)

| **Dense**. Compute Engine physically places resources on tightly coupled hosts connected by a high-speed network fabric to minimize network latency.   
Pricing | 

  * You incur standard pricing for compute instances. See [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing).
  * You incur charges based on the method that you use to create compute instances:
    * If you immediately create compute instances, then you pay for compute resources on a pay-as-you-go (PAYG) basis.
    * If you create compute instances by using an on-demand reservation or an auto-created reservation for a future reservation, then you're charged for as long as the reservation exists. For more information, see [ reservations billing](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing).

| 

  * You get discounts up to 91% off for many machine types, GPUs, TPUs, and Local SSD disks. For more information, see the [pricing page](https://cloud.google.com/spot-vms/pricing). 
  * You pay for compute resources on a pay-as-you-go (PAYG) basis.

| 

  * Based on the machine type that your compute instances use, you can get discounts as follows:
    * For A4, A3, A2, G4, and TPU machine types, you can get a discount up to 53% for vCPUs, memory, and any attached accelerators and Local SSD disks.
    * For H4D machine types, you can get a discount up to 25% for vCPUs, memory, and any attached Local SSD disks.
Other supported machine types aren't eligible for discounts. For more information, see [Dynamic Workload Scheduler (DWS) pricing](https://cloud.google.com/products/dws/pricing).
  * You pay for compute resources on a pay-as-you-go (PAYG) basis.

| 

  * You incur charges based on how you reserve capacity for creating compute instances as follows:
    * If you create a future reservation for capacity blocks, then you incur charges based on [compute instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing). If you reserve resources for a year or longer, then you must purchase and attach a [ resource-based commitment](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) to your reserved resources.
    * If you reserve capacity by using future reservations in calendar mode, then you incur charges based on the [ Dynamic Workload Scheduler (DWS) pricing](https://cloud.google.com/products/dws/pricing). 
  * You're charged for the reservation period. For more information, see [ reservations billing](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing).

  
Quota | When you create a compute instance, standard quota is consumed. |  When you create a Spot VM, [preemptible quota](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) is consumed. If your project lacks preemptible quota, then standard quota is consumed.   
  
[Google Cloud Free Tier credits](https://docs.cloud.google.com/free/docs) don't apply to Spot VMs.  | When you create a Flex-start VM, [preemptible quota ](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) is consumed. If your project lacks preemptible quota, then standard quota is consumed. | Quota consumption varies based on the method that you use to reserve resources:

  * **Future reservations for capacity blocks** : Google manages the quota for your reserved resources. You don't need to manually request quota. At the start time of your approved future reservation, Google automatically increases quota if your project lacks it.
  * **Future reservations in calendar mode** : to reserve H4D machine types, [CPU quota](https://docs.cloud.google.com/compute/resource-usage#cpu_quota) is consumed. To reserve GPU or TPU machine types, quota isn't required.

  
  
## Compute instance availability and lifespan

The following table shows compute instance availability and lifespan for each provisioning model:

| Standard | Spot | Flex-start | Reservation-bound  
---|---|---|---|---  
Creation prerequisites | No creation prerequisites. | No creation prerequisites. | No creation prerequisites. |  To create compute instances, you must first reserve capacity using one of the following methods:

  * To reserve capacity for long-running workloads, use [ future reservations for capacity blocks](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type#reserve-capacity-aihc).
  * To reserve capacity for workloads that run for up to 90 days, use [ future reservations in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

At your chosen delivery date and time, Compute Engine provisions your requested capacity. Then, you can consume the capacity by creating compute instances.  
Supported machine series | You can use any machine series, except A4X Max, A4X, A4, and A3 Ultra.  |  You can use any machine series, except A4X instances and any bare metal instances (machine types with a name that contains `-metal`). To use the TPU7x machine series, you must request access1.  |  You can only use the following machine series:

  * [ A4, A3, A2, G4, and G2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines)
  * [TPU7x1, TPU v6e, and TPU v5p](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines)
  * [N1 virtual machine (VM) instances with GPUs attached](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-general-purpose)
  * [ H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series)

|  Based on how you reserve capacity to create VMs, you can only use the following machine series:

  * If you [create a future reservation for capacity blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity), then you can only use A4X Max, A4X, A4, A3 Ultra, A3 Mega with 8 GPUs, A3 High with 8 GPUs, A3 Edge, H4D, TPU7x1, TPU v6e, and TPU v5p machine series.
  * If you [ create a future reservation in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview), then you can only use the A4, A3 Ultra, A3 Mega, A3 High with 8 GPUs, A3 Edge, H4D, TPU7x1, TPU v6e, and TPU v5p machine series.

  
Compute instance availability | You can create compute instances at any time, as long as your requested resources are available. | You can create compute instances at any time, as long as your requested resources are available. To help reduce your chances of encountering resource availability errors, you can [view the availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability) before you create them. | You can create compute instances as follows:

  * [ Create a standalone compute instance](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms).
  * [ Create a MIG that individually creates compute instances based on availability](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).
  * [ Create a MIG that creates compute instances all at once](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

Compute Engine uses [ DWS](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler) to schedule the provisioning of your requested capacity based on resource availability. DWS helps you obtain high-demand resources like GPUs or TPUs. | You can only create compute instances after reserving capacity for a future date. On your requested date, Compute Engine delivers your requested capacity, which you can then use to create compute instances. If you reserve resources using future reservations in calendar mode, then Compute Engine uses [ DWS](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler) to provision your requested capacity. DWS helps you obtain high-demand resources like GPUs or TPUs.   
Capacity assurance | **Based on the creation method**. Capacity assurance varies based on the method that you use to create compute instances as follows: 

  * If you immediately create compute instances, then Compute Engine makes best-effort attempts to provision your requested capacity. 
  * If you create compute instances by consuming an on-demand reservation or an auto-created reservation for a future reservation, then you have very high assurance that Compute Engine provisions your requested capacity if the reservation has reserved capacity available.

| **Best-effort**. When you create Spot VMs, Compute Engine makes best-effort attempts to provision your requested capacity. | **Best-effort**. When you create a MIG resize request, Compute Engine makes best-effort attempts to schedule the provisioning of your requested capacity. | **Very high**. If Google Cloud approves your reservation request, then you have very high assurance that Compute Engine provisions your reserved capacity at your chosen delivery date and time. You have exclusive access to your reserved capacity for the reservation period.   
Compute instance lifespan | You can control when to stop or delete a compute instance. However, if the machine type that the compute instance uses doesn't support live migration, then Compute Engine stops the compute instance during [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview).  |  You can control when to stop or delete a compute instance, except in the following cases:

  * Compute Engine stops or deletes the compute instance to reclaim capacity. This process is called [_preemption_](https://docs.cloud.google.com/compute/docs/instances/spot#preemption). 
  * If the machine type that the compute instance uses doesn't support live migration, then Compute Engine stops the compute instance during [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview). 

|  Before a compute instance reaches the end of its run duration, you can do the following:

  * **Stop the compute instance** : if you created your Flex-start VM as a standalone compute instance or individually in a MIG as capacity becomes available, then you can stop the compute instances at any time. You can't stop Flex-start VM that were created in a MIG resize request.
  * **Delete the compute instance** : you can delete the compute instance at any time.

When a compute instance reaches the end of its run duration, Compute Engine stops or deletes it based on its termination action. |  You can control when to stop or delete a compute instance, except in the following cases:

  * Compute Engine stops the compute instance during [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview).
  * The automatically created reservation to provision your requested capacity reaches the end of its committed reservation period. At that time, Compute Engine deletes the reservation, and stops or deletes any compute instances that consume the reservation based on the [ termination action](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm) that is specified in their configuration. 

  
  
1 To use the TPU7x machine series with the spot, flex-start, or reservation-bound provisioning models, you must be on an allowlist. To request access, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact). 

## What's next

  * Read an [overview of creating Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview).

  * Learn more about [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).

  * Learn more about [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms).

  * Learn more about [compute instances that use the reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/instances/about-reservation-bound-vms).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
