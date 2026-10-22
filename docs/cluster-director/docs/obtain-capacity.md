---
url: https://docs.cloud.google.com/cluster-director/docs/obtain-capacity/
title: Capacity overview \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:59.680319+00:00
---

# Capacity overview  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/obtain-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Capacity overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of how you can obtain capacity for each consumption option in Cluster Director.

Cluster Director supports several [consumption options](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option#comparison_of_consumption_options) to help you get and use compute resources.

## How to obtain capacity

The following table describes how you can obtain capacity for each consumption option.

Consumption option | Process for obtaining capacity | Pricing implications  
---|---|---  
Future reservations for more than 90 days (for capacity blocks) |  To get future reservation resources, the process is as follows:

  1. Contact your account team to [reserve capacity](https://docs.cloud.google.com/cluster-director/docs/reserve-capacity). You can request compute instances and, optionally, a Hyperdisk pool.
  2. Google increases your quota, and then provisions your requested resources at your specified start date and for your specified duration.
  3. When you [create a cluster](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template), select the **Use reservation** consumption option and then specify your reservation. Cluster Director creates the cluster from your reserved capacity.

| You pay for the entire reservation period, whether you use the reserved resources or not. For more information, see the pricing for [ reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing) and [Hyperdisk pools](https://docs.cloud.google.com/compute/disks-image-pricing#storage_pools).   
Future reservations for up to 90 days (in calendar mode) |  To get future reservation resources, the process is as follows:

  1. [ Search for available capacity and reserve resources by using the Google Cloud console, gcloud CLI, or Compute Engine API](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode).
  2. No quota is charged and no action is required from you.
  3. When you [create a cluster](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template), select the **Use reservation** consumption option and then specify your reservation. Cluster Director creates the cluster from your reserved capacity.

| You're charged for the entire reservation period, whether or not you use the reserved resources for the entire period. For more information, see [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing).   
Flex-start |  For this consumption option, _no reservation is required_. To get Flex-start resources, the process is as follows:

  1. You must request [preemptible quota for the GPU machine type](https://docs.cloud.google.com/compute/resource-usage#gpu_quota) that you want to use.
  2. When you [create a cluster](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template), select the **Use Flex-start** consumption option. When your requested capacity becomes available, Cluster Director provisions your cluster. You obtain resources for up to seven days.

| You're charged when the resources are in use. Resources provisioned using Flex-start automatically get discounts through [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing).  
Spot |  For this consumption option, _no reservation is required_. To get Spot resources, the process is as follows:

  1. You must request [preemptible quota for the GPU machine type](https://docs.cloud.google.com/compute/resource-usage#gpu_quota) that you want to use.
  2. [View resource availability in the region or zone where you want to create compute instances](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).
  3. When you [create a cluster](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template), select the **Use Spot** consumption option. Cluster Director provisions your cluster, but it can be preempted at any time.

| You're charged when the resources are in use. Spot VMs automatically get discounts through [Spot VMs pricing](https://docs.cloud.google.com/compute/docs/instances/spot#pricing).   
On-demand |  For this consumption option, _no reservation is required_. To get on-demand resources, the process is as follows:

  1. If you don't already have enough [CPU quota](https://docs.cloud.google.com/compute/resource-usage#cpu_quota) for the number of vCPUs you plan to provision, [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).
  2. When you [create a cluster](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template), select the **Use on-demand** consumption option. Cluster Director provisions your cluster.

| You're charged when the resources are in use. For more information, see [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
