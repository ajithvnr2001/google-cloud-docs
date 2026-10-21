---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option/
title: About accelerator consumption options for AI/ML workloads in GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:10.045533+00:00
---

# About accelerator consumption options for AI/ML workloads in GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About accelerator consumption options for AI/ML workloads in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the available techniques that you can use to obtain computing accelerators, such as [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) or [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus), based on the requirements of your AI/ML workloads. These techniques are called _accelerator consumption options_ in GKE. Understanding the different consumption options helps you optimize resource utilization to avoid underutilizing resources, increase the likelihood of obtaining resources, and balance cost and performance.

This page is intended for Platform admins and operators that coordinate with Machine learning (ML) engineers to obtain the necessary resources to successfully deploy AI/ML workloads.

To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

## Understand consumption options

You can select from the following options to consume accelerators on GKE:

  * **On-demand:** you consume TPUs or GPUs on GKE without arranging capacity in advance. Before requesting resources, you must have enough on-demand quota for the specific type and quantity of accelerators. On-demand is the most flexible consumption option; however, there is no guarantee that enough on-demand resources will be available to satisfy your request.
  * **Reservations:** you reserve resources for a set period. A reservation can be any of the following: 
    * **Future reservations:** you reserve resources for typically longer durations for a specific time in the future. You have exclusive access to your reserved resources for that period of time. Future reservations require engagement with a Technical Account Manager (TAM). For more information, see [TPU](https://docs.cloud.google.com/tpu/docs/long-term-reservation) and [GPU](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview) guidance.
    * **Future reservations for up to 90 days (in calendar mode):** you request capacity for a specified time period, with a calendar advisor suggesting available dates. Future reservations for up to 90 days (in calendar mode) offers more flexibility for shorter durations and self-service capacity search. For more information, see [Future reservations requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).
    * **On-demand reservations:** you can request an on-demand reservation to be provisioned as soon as the capacity is available, similar to the on-demand option. While the reservation is active, you pay for the resources whether you use them or not.
  * **Flex-start:** you secure densely allocated resources for short-duration workloads without a reservation. You request a specific number of GPUs or TPUs, and Compute Engine provisions them when capacity becomes available. The GPUs or TPUs run uninterrupted for up to seven days. For more information, see [flex-start provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).
  * **Spot:** you provision Spot VMs, which lets you get significant discounts, but Spot VMs can be preempted at any time, with a 30-second warning. For more information, see [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).



To optimize provisioning success under compute resource constraints, you can orchestrate these options using **ComputeClasses**.

## Understand accelerator quota in GKE

Quotas and system limits restrict your use of Google Cloud resources to support resource availability for all Google Cloud users. Quotas have default values, but you can typically request adjustments. System limits are fixed values that can't be changed. By default, projects generally don't come with significant accelerator quota. You must request and receive approval for quota for specific accelerator types and regions.

Consider the following characteristics when managing the quotas that your workloads need:

  * You must request the quota needed for each consumption option. To identify the quota required for each consumption option, see the corresponding "Quota" parameters listed in the choose a consumption option table. If there isn't enough quota, attempts to create clusters, node pools, or deploy workloads requiring accelerators will fail with a `Quota exceeded` error.

  * You must request quota when you use [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) in Autopilot. The nodes provisioned to meet the ComputeClass requirements still consume your project's quota for the specified accelerators.

  * Google Cloud Free Trial accounts have limitations on requesting quota increases for high-value resources like GPUs and TPUs. To have access to accelerator quota, upgrade to a paid account.




To check and request quota, go to the [Quotas page](https://console.cloud.google.com/iam-admin/quotas) in the Google Cloud console. You can filter for accelerator quotas and request increases.

## Identify a consumption option

Use the following considerations to choose the best consumption option for your AI/ML workload:

  * **Workload type:** consider the type of workload that you want to implement. GKE requirements vary if you are running a training or an inference workload: 
    * **Training:** requires high-performance resources with significant memory. Training workloads typically have a well-defined lifespan. These workloads are commonly easier to plan for because they are less prone to sudden spikes in resource consumption.
    * **Inference:** typically requires accelerators that are optimized for scalability and lower cost. Inference workloads can require significant accelerator memory during sudden spikes in resource consumption.
  * **Lifespan based on the implementation phase:** consider your business goal if you are executing a Proof of Concept (POC), platform evaluation, application development or testing, productionalization, or optimization.
  * **Time to provision:** determine if your workload requires _immediate_ execution or if it can be run in the future. If future execution is possible, determine how flexible the start time can be.
  * **Balance between cost and performance:** evaluate your workload performance requirements and budget constraints to select the most cost-effective accelerator. Consider the trade-off between the cost of the accelerators and their performance characteristics. Remember that new accelerators might bring improved cost-performance ratios.



## Choose a consumption option

Use the following table to choose a consumption option:

Consumption option | Provisioning parameters | Supported accelerators | Details | Example workloads  
---|---|---|---|---  
**[On-demand reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview)** | 

  * **Time to provision:** Immediate (with approved reservation)
  * **Lifespan:** Long-term (per reservation)

| 

  * Any GPU (except A4X, A4, or A3 Ultra)
  * Any TPU

| 

  * **Cost:** you are charged for the full reservation period.
  * **Quota:** quota is automatically increased before capacity is delivered.

| 

  * Long-running, large-scale workloads such as pre-training foundation models or multi-host inference.
  * Production workloads.

  
**[Future reservations](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview)** | 

  * **Time to provision:** Immediate (with approved reservation)
  * **Lifespan:** Long-term (per reservation)

| 

  * G2
  * A2
  * A3 High with 8 GPUs
  * A3 Mega
  * A3 Edge

| 

  * **Cost:** you are charged for the full reservation period.
  * **Quota:** quota is automatically increased before capacity is delivered.

| 

  * Long-running, large-scale workloads such as pre-training foundation models or multi-host inference.
  * Production workloads.

  
**[Future reservations for up to 90 days (in calendar mode)](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview)** | 

  * **Time to provision:** Immediate (with approved reservation)
  * **Lifespan:** Up to 90 days

| 

  * A4
  * A3 Ultra
  * A3 Mega
  * A3 High with 8 GPUs
  * A3 Edge
  * Ironwood (TPU7x)
  * TPU v6e
  * TPU v5p
  * TPU v5e

| 

  * **Cost:** discounted (up to 53%). You are charged for the reservation period.
  * **Quota:** no quota is charged.

| 

  * Short-running distributed workloads like model fine-tuning, simulations, or batch inference, where a precise start time is needed.
  * Workloads for platform evaluation, benchmarking, or optimization testing.

  
**[Flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws)** | 

  * **Time to provision:** On-demand (subject to availability)
  * **Lifespan:** Up to 7 days per allocation

| 

  * All GPU families except A4X
  * All TPU versions

| 

  * **Cost:** discounted (up to 53%). You pay as you go.
  * **Quota:** [GPU Preemptible quota](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) or [TPU Preemptible quota](https://docs.cloud.google.com/tpu/docs/quota#preemptible-quotas) is charged.

| 

  * Batch workloads such as small model training, fine-tuning, or scalable inference where start time is flexible.
  * Workloads for POCs or integration testing.

  
**[Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms)** | 

  * **Time to provision:** On-demand (subject to availability)
  * **Lifespan:** Variable, can be preempted with a 30-second warning

| 

  * All GPU families except A4X
  * All TPU versions

| 

  * **Cost:** deeply discounted (up to 91%). You pay as you go.
  * **Quota:** [GPU Preemptible quota](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) or [TPU Preemptible quota](https://docs.cloud.google.com/tpu/docs/quota#preemptible-quotas) is charged.

| 

  * Lower priority, fault-tolerant workloads like CI/CD, data analytics, or high performance computing (HPC).
  * Highly interruptible workloads.

  
**On-demand ([GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus) or [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot))** | 

  * **Time to provision:** Immediate (subject to availability)
  * **Lifespan:** No limit

| 

  * All GPU families except A4X, A4, or A3 Ultra
  * All TPU versions

| 

  * **Cost:** you pay as you go.
  * **Quota:** [GPU](https://docs.cloud.google.com/compute/resource-usage#gpu_quota) or [TPU](https://docs.cloud.google.com/tpu/docs/quota#on-demand-quotas) on-demand quota is charged.

| 

  * General purpose workloads requiring immediate execution.

  
  
## Optimize cost and workload provisioning with ComputeClasses

You can use [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) to dynamically manage and automate your accelerator consumption strategy by defining a priority-based list of fallback configurations. During scale-up operations, GKE attempts to provision nodes according to the hierarchy of priorities you set.

The following list describes the consumption options available with ComputeClasses and how to configure them. For full YAML manifests, see Examples of consumption options with ComputeClasses.

  * **Reservations** : you can define the reservation name in the [`reservations`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#reservations) field in your ComputeClass. This ensures that GKE first attempts to consume your reserved capacity before falling back.
  * **Flex-start provisioning mode** : enable the flex queue using the [`flexStart`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#flexStart) field in your ComputeClass, and configure fallback node replacement durations by using the [`nodeRecycling`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodeRecycling) fields.
  * **Spot VMs** : instruct GKE to use Spot VMs when provisioning nodes for that priority rule by setting the [`spot`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorities) field to `true`.
  * **On-demand capacity combined with a multi-zonal location policy** : Declare the standard machine configurations in the priorities list and configure a fallback location strategy using the [`location`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#location) fields.



ComputeClasses don't support [Future reservations](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview) or [Future reservations for up to 90 days (in calendar mode)](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

### Examples of consumption options with ComputeClasses

The following sections provide configuration examples for these strategies.

#### Reservations with fallback configuration

This configuration works best for workloads that can tolerate disruptions, rather than workloads that depend on persistent data or need to run to completion.

This configuration establishes a resilient fallback strategy using the following steps:

  1. **Consume reservations first:** GKE attempts to provision nodes using your specific, pre-purchased capacity reservation.
  2. **Fall back to Flex-start:** If the reservation capacity is fully utilized, GKE falls back to short-duration, discounted flex-start resources.
  3. **Fall back to On-demand:** As a final fallback, GKE provisions standard, on-demand resources.
  4. **Migrate back to reservations:** Enabling active migration instructs GKE to automatically consolidate and migrate workloads back to the higher-prioritized reservation nodes as soon as capacity becomes available. This migration can be disruptive.
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: ha-gpu-fallback
         spec:
           activeMigration:
             optimizeRulePriority: true # Migrate workloads back to reservation when capacity releases
           priorities:
           # Priority 1: Consume specific corporate reservation first
           - gpu:
               type: nvidia-l4
               count: 1
             reservations:
               affinity: Specific
               specific:
               - name: reserved-l4-pool
                 project: my-project
                 zones: [us-central1-a]
           # Priority 2: Fallback to Flex Start (short-duration allocation)
           - gpu:
               type: nvidia-l4
               count: 1
             flexStart:
               enabled: true
           # Priority 3: Fallback to On-demand resources
           - gpu:
               type: nvidia-l4
               count: 1
         




#### Flex-start provisioning mode with node recycling configuration

This configuration manages short-duration, discounted capacity with continuous uptime using the following steps:

  1. **Request Flex-start VMs:** GKE requests VM instances from the flex-start queue (which run uninterrupted for up to seven days).
  2. **Monitor lease expiration:** GKE tracks the remaining duration of the active flex-start nodes.
  3. **Trigger node recycling:** Twenty minutes (1200 seconds) before the VM lease expires, GKE automatically provisions a replacement node.
  4. **Reschedule workloads:** Workloads migrate onto the new node, resuming execution without service interruption.
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: flex-node-recycling
         spec:
           priorities:
           - gpu:
               type: nvidia-l4
               count: 1
             flexStart:
               enabled: true
               nodeRecycling:
                 leadTimeSeconds: 1200 # Automatically launch replacement node before VM lease expires
         




#### Multi-zone allocation policy configuration

This configuration bypasses single-zone supply restrictions using the following steps:

  1. **Define target zones:** you list multiple backup zones (such as `us-central1-a`, `us-central1-b`, and `us-central1-c`) in the priority rules.
  2. **Broaden target parameters:** you set the [location policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#location_policy) to `ANY`. This setting instructs the cluster autoscaler to search for requested capacity across all specified zones.
  3. **Analyze zonal availability:** during scale-up events, GKE scans the designated zones.
  4. **Provision in available zones:** GKE immediately provisions the requested workload nodes in whichever target zone has matching capacity. This strategy prevents blockages in allocation queues.
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: broad-zonal-serving
         spec:
           priorities:
           - gpu:
               type: nvidia-l4
               count: 1
             location:
               zones: [us-central1-a, us-central1-b, us-central1-c]
               locationPolicy: ANY # Provision accelerator in any target zone with supply
         




## What's next

  * Learn more about [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus).
  * Learn more about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Learn more [about AI/ML inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
