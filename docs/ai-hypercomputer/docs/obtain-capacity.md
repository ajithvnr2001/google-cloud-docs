---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity/
title: Capacity overview \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:01.419526+00:00
---

# Capacity overview  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Capacity overview Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

AI Hypercomputer supports several [consumption options](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#comparison_of_consumption_options) to help you get and use compute resources. This document provides an overview of how you can obtain capacity for each consumption option.

## How to obtain capacity

The following table describes how you can obtain capacity for each consumption option.

Consumption option | Process for obtaining capacity | Pricing implications  
---|---|---  
Future reservations for more than 90 days (for capacity blocks) |  To get future reservation resources, the process is as follows:

  1. Contact your account team to [reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity). You can request compute instances alone. If your workloads require storage, then you can also request a Hyperdisk pool with your compute instances.
  2. Google increases your quota, and then provisions your requested resources at your specified date and time.
  3. When you [create a Compute Engine instance or cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview), specify the reservation-bound provisioning model and properties that match your reserved resources. Compute Engine provisions compute instances and clusters by using your reserved capacity.

| You pay for the entire reservation period, whether you use the reserved resources or not. For more information, see the pricing for [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing) and [storage pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools#pricing).   
Future reservations for up to 90 days (in calendar mode) |  To get future reservation resources, the process is as follows:

  1. [ Search for available capacity and reserve resources](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode).
  2. No quota is charged and no action is required from you.
  3. When you [create a compute instance or cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview), you must specify the reservation-bound provisioning model. Compute instances and clusters are provisioned from your reserved capacity.

| You're charged for the entire reservation period, whether or not you use the reserved resources for the entire period. For more information, see [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing).   
Flex-start |  For this consumption option, _no reservation is required_. To get Flex-start resources, the process is as follows:

  1. You must request [preemptible quota for the GPU machine type](https://docs.cloud.google.com/compute/resource-usage#gpu_quota) that you want to use.
  2. When you create compute instances or clusters by using one of the following options, specify the flex-start provisioning model: 
     * [Create a standalone virtual machine (VM) instance](https://docs.cloud.google.com/compute/docs/instances/create-flex-start-vm)
     * [ Create MIGs with resize requests](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra)
     * Create Slurm clusters:
       * [ Create a fully managed cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster)
       * [ Create a self-managed cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster)
     * Create GKE clusters:
       * [ Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)
       * [ Create an AI-optimized GKE cluster that uses A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra)
When your requested resources become available, Compute Engine provisions your VMs. Your VMs run for up to seven days.

| You're charged when the resources are in use. Resources provisioned by using Flex-start automatically get discounts through [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing).  
On-demand |  For this consumption option, reserving capacity is optional. On-demand resources are only available for general GPUs (such as N1, G2, G4, A2, or A3 Edge). To get these on-demand resources, the process is as follows:

  1. Request standard GPU quota for the machine type that you want to use. For more information, see [Request a quota increase](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).
  2. Verify availability by checking the preferred regions for your hardware in the Compute Engine [GPU availability by region and zone](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones) list.
  3. Create a compute instance or cluster and specify the standard provisioning model. Resources are provisioned immediately based on available capacity.

**Note:** To help improve your chances of obtaining general GPU capacity, we recommend that you use Flex-start. The Flex-start consumption option was specifically designed to help you obtain highly demanded resources, such as GPUs, at a discounted price.  | Standard on-demand rates apply while the resources are in use.   
On-demand reservations |  On-demand reservations (sometimes referred to as _reservations_) are only available for general GPUs (such as G2, G4, A2, or A3 Edge). To reserve capacity, the process is as follows:

  1. Request standard GPU quota for your machine type. For details, see [Request a quota increase](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).
  2. Create an on-demand reservation for your specific VM and GPU type by using the Google Cloud console, the gcloud CLI, or other methods. For details about all methods to create reservations, see [Create a reservation for a single project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-vm-properties).
  3. **Provision your resources** by creating an instance or cluster and targeting your specific reservation.

| Standard rates apply for the entire reservation period. Apply [CUDs](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) for significant savings.  
Standard future reservations |  For this consumption option, you reserve capacity for a future date. Standard future reservations use the standard provisioning model and are only available for general GPUs.

  1. Request standard GPU quota for your machine type. For details, see [Request a quota increase](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).
  2. Create a future reservation request for your specific VM and GPU type.
  3. When the reservation reaches its start time, create compute instances by using your reserved capacity.

**Caution:** You must have sufficient quota for your requested resources _both_ when you submit your reservation request to Google Cloud for review, and when your request reaches its start time after approval. If you lack quota, then Google Cloud might decline your request or provision only part of your requested resources at the start time.  | Standard rates apply for the entire reservation period. Apply [CUDs](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) for significant savings.  
Spot |  For this consumption option, _no reservation is required_. To get Spot resources, the process is as follows:

  1. You must request [preemptible quota for the GPU machine type](https://docs.cloud.google.com/compute/resource-usage#gpu_quota) that you want to use.
  2. [View resource availability in the region or zone where you want to create compute instances](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).
  3. When you [create a compute instance or cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview), specify the spot provisioning model. Resources are provisioned for you as capacity becomes available, but can be preempted at any time.

| You're charged when the resources are in use. Spot VMs automatically get discounts through [Spot VMs pricing](https://docs.cloud.google.com/compute/docs/instances/spot#pricing).   
  
## What's next

  * To review the available options for consuming resources, see [Consumption models](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  * To deploy your infrastructure, see [Create a Compute Engine instance or cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).
  * To reserve resources for your workloads, see [Reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).
  * To check where specific GPUs are available, see [GPU availability by region and zone](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
