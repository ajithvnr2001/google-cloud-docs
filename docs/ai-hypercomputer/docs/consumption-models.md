---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models/
title: Consumption options for AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:23.281617+00:00
---

# Consumption options for AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Consumption options for AI Hypercomputer Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

AI Hypercomputer has several consumption options for acquiring compute resources. These options address needs such as workload duration, fault tolerance, and infrastructure model. Learn about these options and choose the best one for your use case.

As an alternative to manual evaluation, you can prompt Gemini in the Google Cloud console to compare consumption options for your workload and budget. For more information, see [Design AI infrastructure with Compute Advisor](https://docs.cloud.google.com/ai-hypercomputer/docs/design-with-gemini).

## Overview of consumption options

To compare consumption options across key characteristics, use the following table:

Consumption option | Provisioning model | Best for | Capacity assurance | Lifespan | Preemptible | Quota | Discounts | Allocation model  
---|---|---|---|---|---|---|---|---  
Flex-start | Flex-start | Short-duration workloads up to seven days that can wait for capacity. | Best-effort | Up to seven days | No | Preemptible quota | Discounted (up to 53%) on supported series | Dense for MIG resize requests; best-effort for standalone VMs.  
Spot VMs | Spot |  Fault-tolerant, short-duration general GPU workloads.  | Best-effort | Preemptible | Yes | Preemptible quota | Deeply discounted (up to 91%) | Standard  
Standard reservations | Standard | Critical general GPU workloads that require a very high level of assurance for capacity. | Very high | Very high | User-defined | No | No quota consumed | Discounted rates with committed use discounts (CUDs)  
Future reservations for capacity blocks | Reservation-bound | Large-scale, long-running training on clustered GPU. | Very high | Unlimited within the reservation period. | No | Quota is increased before delivery | Discounted (up to 53%) with CUDs | Dense  
Future reservations in calendar mode | Reservation-bound | clustered GPU workloads up to 90 days that require reserved capacity. | Very high | Up to 90 days | No | No quota consumed | Discounted (up to 53%) | Dense  
On-demand VMs | Standard |  general GPU workloads with no specific duration.  | Best-effort | Unlimited | No | On-demand quota | None (pay-as-you-go) | Standard  
  
The consumption option that you use to deploy your infrastructure depends on whether you use General GPU or Clustered GPU.

  * **General GPU** : designed for small-scale inference, development, and smaller-scale training workloads. This type of GPU offers operational flexibility through asynchronous maintenance. To view the available options, see Consumption options for general GPU.

  * **Clustered GPU** : designed for large-scale, tightly coupled training workloads and large-scale inference, RL, and reasoning model workloads that require high capacity assurance and dense resource allocation to minimize network latency. To view the available options, see Consumption options for clustered GPU.




## Consumption options for general GPUs

Use the following consumption options to acquire capacity for general GPU.

### Use Flex-start

To run short-duration workloads that require densely allocated resources, you can request compute resources for up to seven days by using Flex-start. Whenever resources are available, Compute Engine creates your requested number of VMs. You can stop standalone Flex-start VMs, but you can't stop Flex-start VMs that a managed instance group (MIG) creates through resize requests. Flex-start VMs exist until you delete them, or until Compute Engine deletes the VMs at the end of their run duration. 

#### Ideal workloads

  * Small model pre-training
  * Model fine-tuning
  * High performance computing (HPC) simulation
  * Batch inference



#### Key characteristics

  * **Provisioning model** : Flex-start.
  * **Broad hardware support** : request any clustered GPU machine type, except A4X Max and A4X.
  * **Latency optimization** : apply a compact placement policy to standalone VMs to minimize network latency.
  * **Cost efficiency** : receive a discount of up to 53% on vCPUs, memory, GPUs, and Local SSD disks for A4, A3, A2, and G4 machine series. Standard on-demand rates apply to other supported series. For more information, see [Flex-start pricing](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#pricing).



### Use Spot

To run fault-tolerant workloads, you can obtain compute resources immediately based on availability. You get resources at the lowest price possible. However, Compute Engine can preempt VMs at any time to reclaim capacity.

#### Ideal workloads

  * Batch processing and data analytics
  * High performance computing (HPC) and media encoding



#### Key characteristics

  * **Provisioning model** : Spot.
  * **Broad hardware support** : request any clustered GPU machine type, except A4X Max and A4X.
  * **Latency optimization** : apply a compact placement policy to standalone VMs to minimize network latency.
  * **Cost efficiency** : receive a discount of up to 91% on vCPUs, memory, GPUs, and Local SSD disks.



### Use on-demand

Tip: To increase your chances of obtaining general GPU capacity, use Flex-start or Spot. These consumption options offer GPUs at a discounted price compared to on-demand pricing, and they were designed to help increase your chances of obtaining high-demand resources like GPUs.

To run workloads with no specific duration, you can obtain compute resources immediately based on availability. VMs run until you stop or delete them.

#### Ideal workloads

  * Inference and model serving
  * Prototyping and experimentation



#### Key characteristics

  * **Provisioning model** : Standard.
  * **Immediate availability** : create VM instances immediately without waiting for capacity scheduling or approval.
  * **Standard pricing** : pay for resources at standard on-demand rates without long-term commitments.
  * **Broad hardware support** : use with any supported GPU machine series in the general GPU path.



### Use standard reservations

To run critical general GPU workloads that require a very high level of assurance for capacity, you can use standard reservations.

#### Ideal workloads

  * Critical production workloads
  * Workloads requiring assured capacity



#### Key characteristics

  * **Provisioning model** : Standard.
  * **Capacity assurance** : provides very high assurance that resources are available.
  * **Pricing** : standard rates apply, but you can attach CUDs for savings.



## Consumption options for clustered GPU

Use the following consumption options to acquire capacity for clustered GPU.

### Use future reservations for capacity blocks

To run long-running, large-scale distributed workloads that require densely allocated resources, you can request densely allocated compute resources for a future date and time. You have exclusive access to your reserved resources for that period of time, and you can use the resources to create VMs or clusters. At the end of the reservation period, Compute Engine performs the following actions:

  * Compute Engine deletes the reservation and any associated empty storage pool.
  * Based on the [termination action](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm) that you specify for the VMs, Compute Engine stops or deletes any VMs that use the reservation.



#### Ideal workloads

  * Pre-training foundation models
  * Inference for foundation models across multiple hosts



#### Key characteristics

  * **Provisioning model** : Reservation-bound.
  * **Premium machine support** : reserve A4X Max, A4X, A4, A3 Ultra, A3 Mega, or A3 High (8 GPUs) machine types.
  * **Hyperdisk reservations** : you can reserve a Hyperdisk Storage Pool or Hyperdisk Exapool together with compute capacity to help ensure that your workloads have sufficient storage resources. Google co-locates Hyperdisk pools with your compute nodes to optimize storage performance.
  * **Commitment requirements** : attach a resource-based commitment for reservations of one year or longer to receive discounts on compute resources and Hyperdisk pools.
  * **Dynamic modifications** : enable hardware emergency maintenance notifications for Vertex AI jobs usage after the period starts.



### Use future reservations in calendar mode

To run short-running distributed workloads that require densely allocated resources, you can request compute resources for up to 90 days. You have exclusive access to your reserved resources for that time, and you can use the resources to create VMs or clusters. At the end of the reservation period, Compute Engine does the following:

  * Compute Engine deletes the reservation.
  * Based on the [termination action](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm) that you specify for the VMs, Compute Engine stops or deletes any VMs that use the reservation.



#### Ideal workloads

  * Pre-training and fine-tuning
  * Large-scale simulations and inference



#### Key characteristics

  * **Provisioning model** : Reservation-bound.
  * **Machine series support** : reserve A4, A3 Ultra, A3 Mega, or A3 High (8 GPUs) machine types.
  * **Scalability limits** : reserve up to 80 VMs for a maximum of 90 days.
  * **Optimized provisioning** : use a reservation-bound model to increase your chances of obtaining GPUs.



### Use Flex-start

Use Flex-start for clustered managed instance group (MIG) resize requests when you need densely allocated resources for up to seven days.

#### Ideal workloads

Flex-start VMs are ideal for running workloads that can start at any time, such as the following:

  * Small model pre-training
  * Model fine-tuning
  * High performance computing (HPC) simulation
  * Batch inference



#### Key characteristics

  * **Provisioning model** : Flex-start.
  * **Resource allocation** : densely allocated for MIG resize requests.
  * **Cost efficiency** : you receive a discount of up to 53% on vCPUs, memory, GPUs, and any attached Local SSD disks for A4, A3, A2, and G4 machine series. Standard on-demand rates apply to other supported machine series.



### Use Spot

You can use Spot VMs for densely allocated fault-tolerant workloads to achieve deep discounts, with the understanding that Compute Engine can preempt VMs to reclaim capacity.

#### Ideal workloads

  * Fault-tolerant distributed training
  * Batch processing



#### Key characteristics

  * **Provisioning model** : Spot.
  * **Preemption** : Compute Engine can preempt instances at any time.
  * **Cost efficiency** : receive a discount of up to 91% on vCPUs, memory, GPUs, and any attached Local SSD disks



## What's next

  * To review the process and choices to make when you start a cluster, see [Plan and create your AI infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/process-overview).
  * To create and use reservations, see [Create and use reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).
  * To learn more about Spot VMs, see [Learn more about Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).
  * To create an on-demand VM instance, see [Create an on-demand VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
