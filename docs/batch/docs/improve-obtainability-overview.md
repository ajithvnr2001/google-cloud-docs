---
url: https://docs.cloud.google.com/batch/docs/improve-obtainability-overview/
title: Improve resource obtainability for jobs \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:28.834924+00:00
---

# Improve resource obtainability for jobs  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/improve-obtainability-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Improve resource obtainability for jobs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains resource obtainability and recommends how to improve obtainability when you create and run Batch jobs.

## What is obtainability?

**Key Point:** Higher obtainability isn't always better, even when your priority is reliability. The level of obtainability that you want varies based on competing priorities like cost and performance.

_Obtainability_ is the probability that resources are available to run your workload. When resources aren't available, your workload fails due to [resource availability errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability). Obtainability is related to but distinct from _reliability_ , the probability that your workload is available for its users. (_Availability_ might mean either or both.)

The relationship between obtainability and reliability is complex. Your workload needs to obtain resources to be reliable. But, while any flexibility across location, time, and hardware increases obtainability, reliability only increases with flexibility that meets your workload's requirements. For example, note the following complexities:

  * Higher-performance machine types might be less obtainable due to higher demand, but reliability decreases when your workload doesn't have enough performance.
  * Location flexibility increases obtainability, but densely allocated machines improve network performance.
  * Time flexibility increases obtainability, but excessive waiting can cause unnecessary delays.



Consequently, higher obtainability isn't always better. The optimal level of obtainability varies based on your priorities and requirements. For example, you might want lower obtainability to prioritize reducing costs. Even if you want to prioritize reliability, then you might need to balance the benefits of higher obtainability with the risks of lower performance or increased delays.

## Recommendations to improve obtainability for jobs

Review the following sections to improve obtainability for Batch jobs:

  * Recommendations for all consumption options: Review these recommendations for every job.
  * Recommendations based on consumption option: Choose a recommendation based on the consumption option for your job.



### Recommendations for all consumption options

  * **Minimize your needs for large and high-performance machine types by separating your workload.** For example, first separate compute-intensive operations from low-demand operations by using dependent jobs. Then, reduce as much as possible the minimum compute resources that each job requires by maximizing parallel processing and minimizing tightly coupled tasks.

Learn more about [dependent jobs](https://docs.cloud.google.com/batch/docs/create-run-dependent-job) and [compute resources and parallelism](https://docs.cloud.google.com/batch/docs/create-run-job#execution).

  * **Maximize the number of locations that are allowed for your job's Compute Engine resources.** This is true by default; unless you specify the `allowedLocations[]` field for a job, the job's Compute Engine resources are allowed to run in every zone in the job's location.

Learn more about [locations](https://docs.cloud.google.com/batch/docs/locations).

  * **Consider using fail-fast strategies before waiting for better obtainability.** To try avoiding delays, consider fail-fast strategies like the following:

    * Although you can troubleshoot resource availability errors by trying your request at another time, it's often faster to try different locations or hardware first.
    * If you're open to using multiple consumption options, it's often faster to first try the consumption options without delays: on-demand reservations, on-demand, and Spot VMs.
    * For new workloads that you plan to repeat, you might prefer to expedite initial testing and troubleshooting by temporarily using options that are faster to obtain.



### Recommendations based on consumption option

The consumption option that you select is a primary factor for a job's obtainability. This section briefly summarizes each consumption option and recommends how to optimize obtainability for each consumption option.

**Important:** Obtainability isn't the only factor to consider when choosing a consumption option. For example, a consumption option also needs to be compatible with your requirements for pricing, run time, and machine type support. For additional information about how to choose a consumption option for a job, see [Select the consumption option](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#select-provisioning-method).

The following consumption options are listed from highest to lowest obtainability:

  * **For workloads with high obtainability requirements, use _reservations_.** Reservations provide a higher level of assurance in obtaining capacity than all other consumption options. To use reserved capacity, first create or identify existing reservations that you can use. Then, configure instances to consume that reserved capacity. Unlike other consumption options, reserved instances incur costs even when they aren't being used until you delete them, due to their capacity assurance. When considering obtainability, choose between the following types of reservations:

    * **To require reserved capacity, consume a _specifically targeted_ reservation.** These reservations make it easiest to verify that reserved capacity is available and consumable by your workload. Whenever reserved capacity isn't available and compatible, your workload fails and returns an error. A specifically targeted reservation includes all reservations for the `RESERVATION_BOUND` provisioning model and some reservations for the `STANDARD` provisioning model.

Learn how to create a job that uses [reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation).

    * **For optional reserved capacity, consume an _automatically consumed_ reservation and use instance flexibility ([Preview](https://cloud.google.com/products#product-launch-stages)).** These reservation options provide high levels of assurance in obtaining capacity but only when reserved capacity that your workload can consume is available. For automatically consumed reservations, you must specify the `STANDARD` provisioning model and manually verify that reserved capacity is available and matches the instance configuration of your workload. Whenever reserved capacity isn't available or doesn't match, your workload attempts to use on-demand capacity instead. But, unlike specifically targeted reservations, you can use instance flexibility with automatically consumed reservations to let your workload attempt to consume multiple automatically consumed reservations.

Learn how to create a job that uses [reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation) and [instance flexibility](https://docs.cloud.google.com/batch/docs/create-run-job-instance-flexibility) ([Preview](https://cloud.google.com/products#product-launch-stages)).

  * **For workloads with medium obtainability requirements, either use on-demand capacity with instance flexibility ([Preview](https://cloud.google.com/products#product-launch-stages)) or Flex-start VMs.** Choose between these options as follows:

    * **Unless your machine type is in the A3 machine series or unsupported, consider using _on-demand_ capacity with instance flexibility ([Preview](https://cloud.google.com/products#product-launch-stages)).** The on-demand consumption option requires the `STANDARD` (default) provisioning model. Unless you explicitly block reservation consumption, your workload also attempts to consume automatically consumed reservations by default. Notably, [we don't recommend on-demand for the A3 machine series](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#a3-exception).

Learn how to create a job that uses the [standard provisioning model](https://docs.cloud.google.com/batch/docs/create-run-basic-job) and [instance flexibility](https://docs.cloud.google.com/batch/docs/create-run-job-instance-flexibility) ([Preview](https://cloud.google.com/products#product-launch-stages)).

    * **Otherwise or if on-demand capacity is repeatedly unavailable, consider using _Flex-start VMs_.** To use the Flex-start VMs consumption option, specify the `FLEX_START` provisioning model. Flex-start VMs require your workload to withstand a wait time and limited run duration, but also provide discounts through Dynamic Workload Scheduler pricing.

Learn how to create a job that uses [Flex-start VMs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#use-gpu-vms-dws).

  * **For workloads with low obtainability requirements, use _Spot VMs_ with multiple obtainability features.** To use the Spot VMs consumption option, specify the `SPOT` provisioning model. Spot VMs might not always be available and can be preempted at any time, so they are only recommended for fault tolerant workloads, but might provide the largest discounts through Spot VMs pricing.

We generally recommend that you view the availability of Spot VMs before creation and verify that your workload can handle preemption. Then, to improve obtainability of Spot VMs in Batch jobs specifically, we recommend that you use instance flexibility with multiple machine types in the same rank ([Preview](https://cloud.google.com/products#product-launch-stages)) and use automatic retries to automatically attempt to recreate Spot VMs after preemption.

Learn how to [view the availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability) and [manage preemption of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#manage-preemption) in the Compute Engine documentation. Then, learn how to create a job that uses the [Spot VMs provisioning model](https://docs.cloud.google.com/batch/docs/create-run-basic-job), [instance flexibility](https://docs.cloud.google.com/batch/docs/create-run-job-instance-flexibility) ([Preview](https://cloud.google.com/products#product-launch-stages)), and [automatic retries for preemption](https://docs.cloud.google.com/batch/docs/automate-task-retries).




## What's next

  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
