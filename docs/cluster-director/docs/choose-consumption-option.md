---
url: https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option/
title: Choose a consumption option \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:11.350616+00:00
---

# Choose a consumption option  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Choose a consumption option Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the different ways, called _consumption options_ , to get and use compute resources in Cluster Director. For each partition that you want to create in a cluster, choose the consumption option that best suits your workload, duration, and budget.

Each consumption option defines the following:

  * **Resource access** : how you access compute resources to create Compute Engine instances in your cluster.

  * **Provisioning model** : the underlying [provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models), which determines the availability, lifespan, and pricing of your compute instances.




To get AI-powered assistance when you evaluate which consumption option fits your workload and budget requirements, you can prompt Gemini in the Google Cloud console. For more information, see [Design and optimize clusters with Compute Advisor](https://docs.cloud.google.com/cluster-director/docs/create/design-with-gemini).

## Compare consumption options

The following table compares the supported machine types, lifespans, capacity assurance levels, pricing models, and reservation requirements for each consumption option:

Consumption option | Future reservations for capacity blocks | Future reservations in calendar mode (up to 90 days) | Flex-start | Spot | On-demand  
---|---|---|---|---|---  
**Supported machines** | A4X Max, A4X, A4, A3 Ultra, A3 Mega | A4, A3 Ultra, A3 Mega | A4, A3 Ultra, A3 Mega | A4, A3 Ultra, A3 Mega, N2 | C4A, N2  
**Lifespan** | Unlimited | 90 days maximum | 7 days maximum | Unlimited (but subject to [preemption](https://docs.cloud.google.com/compute/docs/instances/spot#preemption)) | Unlimited  
**Capacity assurance** | Very high | Very high | Best-effort | Best-effort | Best-effort  
**Quota** | Quota increases before delivery | No quota is charged | [Preemptible quota](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) is charged | [Preemptible quota](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) is charged | Standard quota is charged  
**Pricing** | Discounted up to 53% ([accelerator pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#accelerator-optimized)) | Discounted up to 53% ([DWS pricing](https://cloud.google.com/products/dws/pricing)) | Discounted up to 53% ([DWS pricing](https://cloud.google.com/products/dws/pricing)) | Deeply discounted up to 91% ([Spot pricing](https://cloud.google.com/spot-vms/pricing)) | Standard pricing ([general-purpose pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose-machine-type-family))  
**Billing model** | Charged for the reservation period ([reservation billing](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing)) | Charged for the reservation period ([reservation billing](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing)) | Pay-as-you-go (PAYG) | Pay-as-you-go (PAYG) | Pay-as-you-go (PAYG)  
**Resource allocation** | Dense | Dense | Best-effort | Best-effort | Best-effort  
**Provisioning model** | Reservation-bound | Reservation-bound | Flex-start | Spot | Standard  
  
## Choose a consumption option

Use the following flowchart to choose the consumption option that best fits the type of partition for your cluster:

[ ![A flowchart with the consumption options that are available in Cluster Director.](https://docs.cloud.google.com/static/cluster-director/images/consumption-options.png)](https://docs.cloud.google.com/static/cluster-director/images/consumption-options.png)

The questions in the preceding diagram are the following:

  1. Do you want high assurance for GPU instances?

     * **Yes** : go to question 2.

     * **No** : skip to question 4.

  2. Do you need capacity for more than 90 days?

     * **Yes** : see Use future reservations for capacity blocks.

     * **No** : go to question 3.

  3. Do you want reserved capacity?

     * **Yes** : see Use future reservations in calendar mode.

     * **No** : go to question 4.

  4. Is your workload fault-tolerant?

     * **Yes** : see Use Spot.

     * **No** : go to question 5.

  5. Do you want to obtain GPU instances?

     * **Yes** : see Use Flex-start.

     * **No** : see Use On-demand.




### Use future reservations for capacity blocks

To run long-running, large-scale distributed workloads that require densely allocated resources, you can request to reserve vCPUs, memory, GPUs, Local SSD disks, and a [Hyperdisk pool](https://docs.cloud.google.com/compute/docs/disks/pools) for a specific time in the future. If Google approves your request, then you have exclusive access to your reserved resources for that period of time, and you can use the resources to create clusters. At the end of the reservation period, Compute Engine does the following:

  * Compute Engine deletes the reservation and any associated empty Hyperdisk pool.

  * Compute Engine stops or deletes any compute instances that you created from the reservation based on the compute instances' [termination action](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm).




#### Ideal workloads for future reservations for capacity blocks

Future reservations for capacity blocks are ideal for the following workloads:

  * Pre-training foundation models

  * Multi-host foundation model inference




#### Key characteristics of future reservations for capacity blocks

Future reservations for capacity blocks have the following characteristics:

  * You can reserve A4X Max, A4X, A4, A3 Ultra, and A3 Mega machine types, as well as Hyperdisk pools. Google allocates compute nodes in close physical proximity to minimize network latency, and co-locates Hyperdisk pools with those compute nodes to optimize storage performance.

  * You can reserve as many compute instances as you want for as long as you want. For any compute instances that you want to reserve for a year or longer, you need to purchase and attach a [resource-based commitment](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments) to your reserved resources. Then, you can use the reserved resources to create and run compute instances until the end of the reservation period.

  * You use the reservation-bound provisioning model to create compute instances, which has the following benefits:

    * You have a higher chance to obtain GPUs.

    * In addition to the commitment attached to your compute instances, you get a discount up to 53% for vCPUs, memory, GPUs, and any attached Local SSD disks, as well as discounts for Hyperdisk pools if you reserve resources for 365 days or more.




#### How to use future reservations for capacity blocks

To use future reservations for capacity blocks to create clusters, you must complete the following steps:

  1. **Request to reserve capacity**. Contact your account team and specify the compute instances and Hyperdisk pools to reserve. Based on availability, Google creates a draft reservation request for you. If the draft matches your requirements, then accept and submit the request. If you reserve compute and storage capacity together, then you must accept both requests as a bundle to ensure that Google delivers both resources at the same time. Google Cloud approves your reservation request within a few minutes.

For instructions, see [Reserve capacity through your account team](https://docs.cloud.google.com/cluster-director/docs/reserve-capacity).

  2. **Consume reserved resources**. At the start of your reservation period, Google delivers your compute reservation and Hyperdisk pools. You can use the reserved resources to create compute instances and attach storage disks in one or more of your cluster partitions.

For instructions, see one of the following:

     * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

     * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)




### Use future reservations in calendar mode

To run short-running distributed workloads that require densely allocated resources, you can request to reserve compute resources for up to 90 days. If your request is approved, then you have exclusive access to your reserved resources for that time, and you can use the resources to create clusters. At the end of the reservation period, Compute Engine does the following:

  * Compute Engine deletes the reservation.

  * Compute Engine deletes any virtual machine (VM) instances that use the reservation.

**Caution:** Cluster Director deletes a VM after the reservation that you used to create the VM reaches its end time, regardless of the VM's [termination action](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm). To prevent data loss, back up your data by using one of the data protection options. For more information, see [Data protection options for disks and instances](https://docs.cloud.google.com/compute/docs/disks/data-protection).



#### Ideal workloads for future reservations in calendar mode

Future reservations in calendar mode are ideal for the following workloads:

  * Model pre-training

  * Model fine-tuning

  * Simulations

  * Inference




#### Key characteristics of future reservations in calendar mode

Future reservations in calendar mode have the following characteristics:

  * You can reserve A4, A3 Ultra, or A3 Mega machine types. Machines are densely allocated to minimize network latency.

  * You can view the future availability of resources, and then reserve up to 80 VMs for up to 90 days in the future. Then, you can use the reserved resources to create VMs until the end of the reservation period.

  * You use the reservation-bound provisioning model to create compute instances, which has the following benefits:

    * You have a higher chance to obtain GPUs.

    * You get a discount up to 53% for vCPUs, memory, GPUs, and any attached Local SSD disks.




#### How to use future reservations in calendar mode

To use future reservations in calendar mode to clusters, you must complete the following steps:

  1. **View resources availability**. You can view the future availability of the resources that you want to reserve. When you create a reservation request, you can specify the number, type, and reservation duration for the resources that you confirmed as available. This action increases the chances that Google Cloud approves your request.

For instructions, see [View resource future availability](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#view-availability).

  2. **Reserve capacity**. You create a reservation request for a future date and time. Google Cloud approves the reservation request within two minutes. If approved, then Compute Engine reserves the capacity for you. At your chosen delivery date, you can use the reserved resources to create clusters.

For instructions, see [Create a request for GPU VMs, H4D VMs, or TPUs](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#request).

  3. **Consume reserved resources**. At the start of your chosen reservation period, you can use the reservation to create VMs in one or more of your cluster partitions.

For instructions, see one of the following:

     * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

     * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)




### Use Flex-start

To run short-duration workloads that require densely allocated resources, you can request compute resources for up to seven days by using Flex-start. Whenever resources are available, Compute Engine creates your requested number of VMs. The Flex-start VMs run until you delete them, or until Compute Engine deletes the VMs at the end of their run duration.

#### Ideal workloads for Flex-start

Flex-start is ideal for workloads that can start at any time, such as the following:

  * Small model pre-training

  * Model fine-tuning

  * Simulations

  * Batch inference




#### Key characteristics of Flex-start

Flex-start has the following characteristics:

  * You can request A4, A3 Ultra, and A3 Mega VMs. Dense allocation depends on resource availability.

  * You use the flex-start provisioning model to create Flex-start VMs, which has the following benefits:

    * You have a higher chance to obtain GPUs.

    * You get a discount up to 53% for vCPUs, memory, GPUs, and any attached Local SSD disks.

  * You can request resources for up to seven days. When your allocated resources reach the end of their maximum run duration, Cluster Director automatically requests new resources with the same run duration.

**Note:** If resources are unavailable at the end of a maximum run duration, then Cluster Director attempts to obtain resources to restart nodes for up to eight hours. After this time, Slurm sets the node state to `down`. The request remains active until Cluster Director allocates the required resources or you cancel the request. To cancel a pending request, modify a compute resource configuration, modify the number of nodes in a nodeset, or delete your cluster.



#### How to use Flex-start

To use Flex-start to create VMs in one or more of your cluster partitions, use one of the following methods:

  * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

  * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)




### Use Spot

To run fault-tolerant workloads, you can obtain compute resources immediately based on availability. You get resources at the lowest price possible. However, Compute Engine can preempt Spot VMs at any time to reclaim capacity.

#### Ideal workloads for Spot

Spot is ideal for workloads where interruptions are acceptable, such as the following:

  * Batch processing

  * High performance computing (HPC)

  * Continuous integration and continuous deployment (CI/CD)

  * Data analytics

  * Media encoding

  * Online inference




#### Key characteristics of Spot

Spot has the following characteristics:

  * You can create A4, A3 Ultra, A3 Mega, and N2 VMs. Dense allocation depends on resource availability.

  * You can immediately create clusters. The VMs in the cluster run until you stop or delete them, or until Compute Engine preempts the VMs to reclaim capacity.

  * You use the spot provisioning model to create Spot VMs, which has the following benefits:

    * You have a higher chance to obtain GPUs.

    * You get a discount of up to 91% off for vCPUs, memory, and any attached GPUs and Local SSD disks.




#### How to use Spot

To use Spot to create VMs in one or more of your cluster partitions, complete the following steps:

  1. **View resources availability**. You can view resource availability in the region or zone where you want to create Spot VMs. This action helps reduce the time that Cluster Director takes to allocate resources and create Spot VMs.

For instructions, see [View resource availability for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).

  2. **View preemption rate and pricing**. You can view the historical and current preemption rate and pricing across different machine types and zones. This information helps you choose the machine type and location that best fit your workload and budget.

For instructions, see [View the preemption rate and pricing for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-spot-preemption-price).

  3. **Create your cluster**. To create your cluster with one or more partitions that use Spot VMs, select one of the following methods:

     * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

     * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)




### Use On-demand

For cluster components that don't require GPU acceleration, such as login nodes, or for running CPU-bound computational tasks like HPC workloads, you can get resources immediately based on availability. You get resources at the standard pricing.

#### Ideal workloads for On-demand

On-demand is ideal for workloads that don't require GPU-acceleration, such as the following:

  * Login nodes

  * CPU-bound computational tasks

  * General-purpose HPC




#### Key characteristics of On-demand

On-demand has the following characteristics:

  * You can create C4A and N2 VMs. Dense allocation depends on resource availability. You can use C4A VMs only for login nodes.

  * You can immediately create clusters. The VMs in the cluster run until you stop or delete them.

  * You use the standard provisioning model, which is the default model.




#### How to use On-demand

To use On-demand to create VMs in one or more of your cluster partitions, use one of the following methods:

  * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

  * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
