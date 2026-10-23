---
url: https://docs.cloud.google.com/tpu/docs/plan-tpus/
title: Plan your Cloud TPU resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:18.960555+00:00
---

# Plan your Cloud TPU resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/plan-tpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Plan your Cloud TPU resources 

This page describes how to plan your Tensor Processing Unit (TPU) usage.

## Choose a consumption option

Consumption options refers to the ways to get and use compute resources. You can request Cloud TPU VM capacity based on your needs for speed, duration, cost, and preemption tolerance. Options include:

  * **On-demand:** Standard pay-as-you-go instances.
  * **Spot VMs:** Lower-cost, preemptible instances. Uses preemptible quota.
  * **Flex-start VMs:** Reserve capacity as needed, for up to 7 days, without long-term reservations or complex quota management.
  * **Reservations:** Reserve capacity for a specific duration (up to 90 days or 1 year+), guaranteeing availability. Uses on-demand quota.



The following table compares TPU consumption options based on how they work, their ideal use cases, and supported TPU versions.

Consumption option | How it works | Best used for | Supported TPU versions  
---|---|---|---  
Future reservations for one year or longer |  You request TPU resources for one year or longer in advance. These resources are reserved for your exclusive use during that time. Reservations provide the highest level of assurance for capacity and provide a lower price than on-demand resources. Future TPU reservations include a committed use discount (CUD) CUDs provide discounted prices when you purchase a committed use contract. For more information, see [ Future reservations for one year or longer](https://docs.cloud.google.com/tpu/docs/long-term-reservation) | Future reservations for one year or longer are ideal for long-running training jobs and inference workloads. | All TPU versions  
Future reservations for up to 90 days (calendar mode) |  You request TPU resources for a specific start time and duration, between one and 90 days. These resources are reserved for your exclusive use during that time. For more information, see [Future reservations for up to 90 days (in calendar mode)](https://docs.cloud.google.com/tpu/docs/calendar-mode-reservation) Reservations provide the highest level of assurance for capacity and provide a lower price than on-demand resources. | Future reservations in calendar mode are a good fit for training and experimentation workloads that require precise start times and have a defined duration. | TPU7x, TPU v6e, and TPU v5p  
On-demand |  You request TPU resources for immediate use, for as long as you need them. On-demand provides significant flexibility. On-demand resources aren't preempted, but there's no guarantee that there are enough available TPU resources to satisfy your request. On-demand is the default option when you create TPU resources. For more information about creating and using on-demand TPUs, see [Create TPU VMs](https://docs.cloud.google.com/tpu/docs/create-instance-compute). | On-demand is a good fit for urgent jobs and workloads that require a flexible end time. | All TPU versions  
Flex-start ([Preview](https://cloud.google.com/products#product-launch-stages)) |  You request TPU resources for a specific amount of time, up to seven days, without reserving capacity in advance. TPU Flex-start VMs are delivered from a dedicated pool of capacity, so the availability of these resources is higher than on-demand. For more information, see [Request TPU Flex-start VMs](https://docs.cloud.google.com/tpu/docs/create-flex-start-compute).  For more information about using TPU Flex-start VMs with Google Kubernetes Engine (GKE), see [ About GPU and TPU provisioning with flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws). | Flex-start is ideal for experimentation, small-scale testing, dynamic provisioning of TPUs for inference workloads, model fine-tuning, and workload runs that take less than seven days. | TPU7x, TPU v6e, and TPU v5p  
Spot |  You request TPU resources that can be preempted. Spot VMs are available at a significantly lower price than on-demand resources. Spot VMs are often easier to obtain than on-demand resources but can be preempted (shut down) at any time. There is no limit on runtime duration. For more information about TPU Spot VMs, see [ Manage TPU Spot VMs](https://docs.cloud.google.com/tpu/docs/spot-compute). | Spot is a good fit for scheduling lower priority workloads like model pre-training, model fine-tuning, and simulation jobs that are tolerant to availability disruptions. | All TPU versions  
  
## Choose a TPU capacity mode

By default, TPU capacity operates on Google-managed infrastructure. If you have a reservation, you can choose to use All Capacity mode for TPU v6e (Trillium) and TPU7x (Ironwood). All Capacity mode gives you access to 100% of your reserved capacity and provides full topology visibility. However, you are responsible for managing hardware maintenance and failure recovery.

For a detailed comparison between default Google-managed infrastructure and All Capacity mode, see [TPU capacity modes](https://docs.cloud.google.com/tpu/docs/capacity-modes).

## Choose TPU version

Select the TPU version, for example, v5p, v6e, or TPU7x (Ironwood) based on your model's training or inference needs. For more information, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

## Request TPU quota

To use TPU VMs, regardless of the consumption option, you need either on-demand or preemptible quota for Cloud TPU resources. Make sure you have enough quota for your chosen option, TPU version, size, and zone. Quotas are specific to each TPU version and differ for on-demand versus preemptible use. Some TPU versions have default quotas; for others, you must request quota. For more information, see [Compute Engine quotas](https://docs.cloud.google.com/compute/quotas-limits).

## What's next

  * Learn how to [create TPU VMs](https://docs.cloud.google.com/tpu/docs/create-tpu-vm-compute)
  * Learn how to [manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
