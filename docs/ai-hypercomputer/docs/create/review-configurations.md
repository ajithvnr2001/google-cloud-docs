---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations/
title: Review compute instance and cluster configurations \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:00.760447+00:00
---

# Review compute instance and cluster configurations  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Review compute instance and cluster configurations Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes the configurations in AI Hypercomputer to consider before you create Compute Engine instances and clusters. Reviewing the available configurations helps optimize performance for your workloads, as well as minimize downtimes and performance issues.

## Configuration factors for compute instance and cluster creation

Before you create compute instances and clusters to run your workloads, consider which configuration to use:

  1. The provisioning model

  2. The cluster deployment tools

  3. If you use the reservation-bound provisioning model, then you must also consider the following factors:

     * The reservation block deployment type

     * The reservation operational mode

     * The maintenance scheduling type




## Provisioning models

Based on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you choose for creating compute instances or clusters, you can use one of the following provisioning models to obtain the necessary resources for creating instances:

  * **Reservation-bound** : you can reserve resources at a discounted price for a future date and duration. At the start of your reservation period, you can use the reserved resources to create instances or clusters. You have exclusive access to your reserved resources for the reservation period.

  * **Flex-start** : you can request discounted resources for up to seven days. Compute Engine makes best-effort attempts to schedule the provisioning of your requested resources as soon as they're available. You have exclusive access to your obtained resources for your requested period.

  * **Spot** : based on availability, you can immediately obtain deeply discounted resources. However, Compute Engine might stop or delete instances at any time to reclaim capacity.




### Reservation-bound provisioning model

The reservation-bound provisioning model links your created compute instances to the capacity that you previously reserved. When you reserve capacity, Compute Engine creates an empty reservation. Then, at the reservation start time, the following occurs:

  * Compute Engine adds your reserved number of instances to the reservation. You have exclusive access to the reserved capacity until the reservation end time.

  * Google Cloud charges you for the reserved capacity until the end of your reservation period, whether you use the capacity or not.




You can then use the reserved resources to create instances without additional charges. You only pay for resources that aren't included in the reservation, such as disks or IP addresses.

To specify the reservation-bound provisioning model when you create compute instances or MIGs, do the following:

  * In the Google Cloud console, in the **Provisioning model** list, select **Reservation-bound**.

  * In the Google Cloud CLI, include the `--provisioning-model=RESERVATION_BOUND` flag in the command.

  * In the Compute Engine API, include the `"provisioningModel": "RESERVATION_BOUND"` field in the request body.




For more information about setting these parameters when you create instances or MIGs after you reserve capacity, see [Compute instance and cluster creation overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview). If you use Cluster Toolkit to deploy your clusters, then the cluster blueprint sets the provisioning model for you.

### Flex-start provisioning model

The flex-start provisioning model lets you create standalone Flex-start VMs or add Flex-start VMs to a managed instance group (MIG) when your requested capacity is available. When you add Flex-start VMs to a MIG by using resize requests, the MIG creates the instances all at once. This approach helps you avoid unnecessary charges for partial capacity that Compute Engine might deliver while you wait for the full capacity needed to start your workload. The flex-start provisioning model provisions resources from a secure capacity pool, which helps to increase your chances of obtaining high-demand resources like GPUs.

To specify the flex-start provisioning model when creating a standalone instance or an instance template for a MIG, do the following:

  * In the Google Cloud console, in the **Provisioning model** list, select **Flex-start**.

  * In the gcloud CLI, include the `--provisioning-model=FLEX_START` flag in the command.

  * In the Compute Engine API, include the `"provisioningModel": "FLEX_START"` field in the request body.




For more information about creating instances or clusters that use flex-start provisioning model, see the following documents:

  * [Create a standalone instance](https://docs.cloud.google.com/compute/docs/instances/create-flex-start-vm)

  * [Create MIGs with resize requests](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-prereqs)

  * Create Slurm clusters:

    * [Create a fully managed Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster)

    * [Create a self-managed Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster)

  * Create GKE clusters:

    * [Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)

    * [Create an AI-optimized GKE cluster that uses A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra)




### Spot provisioning model

The spot provisioning model lets you create deeply-discounted compute instances based on availability. However, Compute Engine might stop or delete the created instances at any time to reclaim capacity. This process is called [_preemption_](https://docs.cloud.google.com/compute/docs/instances/spot#preemption).

To specify the spot provisioning model when you create instances or MIGs, do the following:

  * In the Google Cloud console, in the **Provisioning model** list, select **Spot**.

  * In the gcloud CLI, include the `--provisioning-model=SPOT` flag in the command.

  * In the Compute Engine API, include the `"provisioningModel": "SPOT"` field in the request body.




For more information about setting these parameters when you create instances or MIGs, see [Compute instance and cluster creation overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

## Cluster deployment tools

[Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) is an open source deployment tool that is recommended for creating GPU-accelerated clusters. Cluster Toolkit can deploy both Google Kubernetes Engine (GKE) or Slurm clusters.

Alternatively, you can choose to provision your groups of compute instances by using one of the following methods, and then incorporate your own workload scheduler as needed:

  * [Create standalone instances](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm)

  * [Create instances in bulk](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk)

  * [Create a managed instance group (MIG)](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig)




## Reservation block deployment types

If you use the reservation-bound provisioning model when creating clustered GPU compute instances or clusters, the machines you receive are automatically deployed within blocks of densely allocated hosts. This deployment offers the following benefits:

  * Non-blocking networking for consistent high-bandwidth, low-latency instance connectivity by using dynamic machine learning (ML) network fabric from Google.

  * Access to network topology that provides a hierarchical view of the relative proximity among instances. This capability is useful for advanced job scheduling use cases.

  * Fine-grained, topology-aware placement when you use orchestrators.

  * Fine-grained user control over maintenance schedules to maximize job scheduling and uptime, and minimize downtimes.




## Reservation operational mode

**Important:** A4X Max, A4X, A4, and A3 Ultra are the only GPU machine series that support reservation operational mode.

If you use the reservation-bound provisioning model, then the machine type that you reserve determines the _reservation operational mode_ for your reserved capacity. Each mode defines how to respond to host errors or faulty host reports, as well as your level of visibility and control over the reservation's infrastructure.

Each reservation operational mode defines the following:

  * **Who manages recovery** : you or Google Cloud.

  * **What capacity you use for recovery** : only your reserved capacity, or capacity within or outside your reservations.

  * **Your level of placement control** : whether you can view and start maintenance before the planned time for specific reservation sub-blocks for fine-grained control.




When you reserve capacity to create compute instances or clusters, you must choose between one of the following reservation operational modes: _managed mode_ or _all capacity mode_.

### Managed mode

**Important:** A4 and A3 Ultra are the only GPU machine series that support managed mode.

In managed mode, Google Cloud automatically manages the maintenance and recovery process of your compute instances after host errors or faulty host reports. This approach is ideal when your workload requires high stability, and you prefer an automated process to minimize downtimes.

The managed mode has the following characteristics:

  * **Only use reserved capacity for recovery** : Compute Engine only uses your reserved capacity to restart instances. If there's no available capacity in your reservations, then Compute Engine only restarts instances after you obtain more capacity.

  * **Automated instance restarts** : Google Cloud handles the entire recovery process for an instance. When host maintenance is required, Compute Engine automatically migrates your instances on other available machines within your reservation and restarts the instances.

  * **Block management and visibility** : you can view the topology, health, and maintenance status of individual reservations and reservation blocks. You can also receive maintenance notifications, and optionally start maintenance before the scheduled maintenance time, for these resources.

  * **Potential API rate limits** : calls to the report faulty host API might be rate-limited per reservation.




### All capacity mode

**Important:** A4X Max and A4X are the only GPU machine series that support all capacity mode.

In all capacity mode, you are responsible for managing a compute instance recovery process. You must manually start maintenance after host errors or faulty host reports. Unlike the managed mode, you can also view and start maintenance for your reservation sub-blocks. These features give you full, granular control over the maintenance and recovery process for your instances.

The all capacity mode has the following characteristics:

  * **Use reserved and unreserved capacity for recovery** : you can use your reserved resources, as well as any resources that are available outside of your reservation, to help you migrate and restart an instance when its host fails.

  * **Manual instance restarts** : you're responsible for the recovery process of an instance. When host maintenance is required because of a host error or faulty host report, Compute Engine stops your instance. You can only restart the instance after maintenance completes.

  * **Block and sub-block management and visibility** : you can view the topology, health, and maintenance status of individual reservations, reservation blocks, and reservation sub-blocks. You can also receive maintenance notifications, and optionally start maintenance before the scheduled maintenance time, for these resources.

  * **No API rate limits** : there are no rate limits when you make calls to the report faulty host API.




## Maintenance scheduling types

**Important:** A4X Max, A4X, A4, and A3 Ultra are the only GPU machine series that support maintenance scheduling.

If you use the reservation-bound provisioning model, then Cluster Director provides options for scheduling host maintenance for the running compute instances in your cluster. When you reserve capacity, you can specify whether to group instances and have synchronized maintenance scheduling (_grouped_), or the instances can be loosely coupled and have independent maintenance scheduling (_independent_).

### Grouped maintenance scheduling

The grouped maintenance scheduling type helps align all instances running the same workload to the same planned maintenance frequency, no matter when Compute Engine provisions a compute instance. This tightly-coupled maintenance lets you optimize your job's performance by giving you complete control over your used and unused capacity.

A group maintenance scheduling type is useful in the following cases:

  * Your environment uses a job scheduler, such as Slurm or GKE.

  * You want to run training or other highly parallelized-computing workloads.




### Independent maintenance scheduling

**Important:** A4 and A3 Ultra are the only GPU machine series that support independent maintenance scheduling.

This independent maintenance scheduling type gives instances different maintenance schedules. This configuration is ideal if you want to run inference or limited-scale training where workloads run more efficiently when they have separate maintenance schedules.

## What's next?

  * [Reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
