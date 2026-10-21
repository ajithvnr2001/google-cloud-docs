---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/release-notes/
title: AI Hypercomputer release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:51.506332+00:00
---

# AI Hypercomputer release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Resources ](https://docs.cloud.google.com/ai-hypercomputer/docs/release-notes)



Send feedback 

#  AI Hypercomputer release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to AI Hypercomputer. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## October 06, 2026

Feature

**Generally available** : When you reserve compute resources for creating GPU instances through your account team, you can include a Hyperdisk pool in the same request or in a subsequent request. This option helps ensure that your artificial intelligence (AI) and machine learning (ML) workloads have the storage resources that they require close to your GPU instances. For more information, see [Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).

## September 07, 2026

Security

Google addressed a security vulnerability (CVE-2026-65107) that affects Slurm clusters. Based on the Google Cloud product that you used to create your Slurm cluster, see one of the following to mitigate the vulnerability:

  * [Security bulletin for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/security-bulletins#gcp-2026-060)

  * [Security bulletin for Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/security-bulletins#gcp-2026-060)




## August 21, 2026

Change

AI Hypercomputer has expanded to cover all GPU machine series. Specifically, the documentation for AI Hypercomputer has been significantly updated as follows:

  * Documentation has been added for the A3 Edge, A2, G4, G2, N1+T4, and N1+V100 GPU machine series.
  * Pages are labeled based on whether they are relevant to the newly documented machine series for [general GPU](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus), the pre-existing machine series for [clustered GPU](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus), or both.



To learn more about the differences between general GPUs and clustered GPUs, see [Choose your accelerator infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-infrastructure). To view workload recommendations, see [Choose between general GPUs and clustered GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy).

## June 23, 2026

Feature

**Preview** : You can use Gemini in the Google Cloud console as an AI-powered interface to evaluate hardware options, estimate deployment costs, and view recommended configurations for your clusters. Prompting Gemini helps you reach an optimal configuration for your cluster before you create or modify the cluster. For more information, see [Design and optimize your cluster with Gemini](https://docs.cloud.google.com/ai-hypercomputer/docs/design-with-gemini).

## June 22, 2026

Feature

**Preview** : RoCE VPC networks for VM instances support assigning alias IP ranges to `MRDMA` vNICs. For more information about these features, see the following:

  * [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles)
  * [Alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip)



## June 15, 2026

Feature

**Preview** : Before you create Spot VMs, you can view the real-time availability, estimated uptime, historical preemption rate, and pricing for a specific machine type and location. This information helps you maximize the chances of successfully creating Spot VMs and choose the configuration that best fits your workload needs and budget. For more information, see [Use Spot](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#spot).

## April 16, 2026

Feature

**Generally available** : The AI Hypercomputer documentation includes support for the A3 Mega and A3 High machine types. The addition of A3 Mega and A3 High expand the available compute options for training and serving large-scale AI models on Google Kubernetes Engine (GKE) and Compute Engine.

To support this effort, several new pages have been added and existing pages updated in the AI Hypercomputer documentation where relevant. These updates provide comprehensive guidance for deploying, managing, and optimizing the A3 Mega and A3 High machine types within the AI Hypercomputer stack.

New documentation pages include the following:

  * [Create an AI-optimized instance with A3 High or A3 Mega](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a3-high-mega)
  * [Create AI-optimized instances in bulk with A3 High or A3 Mega](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a3-high-mega)
  * [Create GKE Autopilot clusters that use A3 Mega or A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-autopilot-a3-high-mega)
  * [Create GKE Standard clusters that use A3 Mega or A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-standard-a3-high-mega)
  * [Run NCCL on custom GKE clusters that use A3 Mega and A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a3-mega-high)

**Note:** [Cluster management capabilities](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities) aren't supported for A3 Mega or A3 High VMs that you created before October 1, 2025\. To check if your A3 Mega or A3 High VMs have cluster management capabilities, verify that the `deploymentType` field in the reservation that you used to create the VMs is set to [DENSE](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation). For more information about using A3 Mega or A3 High VMs in a cluster, contact your account team.

## March 02, 2026

Feature

**Generally available** : Pathways on Cloud version 0.1.0 is now generally available. Updates include the following:

  * **JAX versions** : supported versions include 0.9.0, 0.8.2, 0.8.1, 0.8.0, 0.7.2, and 0.7.1.
  * **TPU versions** : supported versions include v5e, v5p, v6e, and 7x.
  * **Colocated Python sidecar containers** : client-side support, including shared memory on sidecars.
  * **Elastic Training** : client-side support.



For more information, see [Introduction to Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro).

Feature

**Generally available** : You can apply compact placement policies to standalone Flex-start VMs. These policies let you colocate your standalone Flex-start VMs in adjacent blocks or in the same block. Applying a compact placement policy gives you more control over VM placement and helps minimize network latency for AI/ML workloads. For more information, see [Use Flex-start](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#flex-start).

## December 12, 2025

Issue

Workloads on A4 VMs might experience interruptions due to a firmware issue for NVIDIA B200 GPUs. To help prevent the issue, we recommend resetting the GPUs on A4 VMs at least once every 60 days. For more information, see the [known issue](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/known-issues#a4-firmware).

## December 09, 2025

Feature

**Generally available** : You can enable node health prediction in an AI-optimized GKE cluster to help the cluster avoid scheduling workloads on nodes that are likely to degrade within the next five hours. This approach helps minimize interruptions for critical and interruption-sensitive workloads, such as large-scale training. For more information, see [Enable node health prediction in a GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/enable-node-health-prediction).

## October 21, 2025

Feature

**Generally available** : You can use future reservations in AI Hypercomputer to request to reserve capacity starting on a specific date up to one year in the future. For more information, see [Reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).

## September 10, 2025

Feature

**Generally available** : When you reserve capacity for creating VMs, you can specify the reservation operational mode for your reserved capacity. A reservation operational mode defines how your VMs behave after a host error or faulty host report, and it determines your level of visibility and control over the reservation's infrastructure. For more information, see [Reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode).

Feature

**Generally available** : You can receive a notification when maintenance for an A4X reservation sub-block is scheduled, starts, or is completed. Additionally, you can now view and trigger maintenance for an A4X reservation sub-block. These features give you more control over maintenance for your A4X reservations, helping you minimize downtimes for your workloads. For more information, see [Manage host events across reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations).

Feature

**Generally available** : You can view and manage the topology of your A4X reservations, including sub-blocks. This feature helps you better understand the topology of the VMs in your workload to further minimize network latency, as well as understand the health of your reservation blocks or sub-blocks. For more information, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity).

Feature

**Generally available** : When you reserve capacity for creating VMs, you can specify a maintenance scheduling type for your reservations. This feature helps you minimize downtimes by letting you specify whether you want to group VMs and have synchronized maintenance scheduling (_grouped_), or loosely coupled VMs have independent maintenance scheduling (_independent_). For more information, see [Maintenance scheduling types](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#maintenance-scheduling-types).

Feature

**Generally available** : You can use the following Cloud Monitoring metrics to monitor your A4X VMs, and help you identify and troubleshoot issues with your GPUs:

  * NVLink runtime error
  * Uncorrectable DRAM ECC errors
  * Uncorrectable DRAM row remapping count
  * Uncorrectable DRAM row remapping failed
  * Uncorrectable PCIe errors
  * Uncorrectable cache ECC errors



For more information, see [Monitor VMs and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor).

Feature

**Generally available** : The [accelerator-optimized A4X machine type](https://docs.cloud.google.com/ai-hypercomputer/docs/gpu#a4x), the first GPU VM to run on Arm, is available on AI Hypercomputer. The A4X machine series has the NVIDIA GB200 Grace Blackwell Superchips attached and runs on the NVIDIA GB200 NVL72 platform. Use this machine type to run your large artificial intelligence (AI) models and machine learning (ML) workloads. The A4X machine type is currently available in the `us-central1-a` zone.

Feature

You can receive at least seven days of advance notice for unplanned hardware maintenance for a reservation. This feature helps you more proactively control disruptions to your workloads when unplanned maintenance is scheduled after a host error or faulty host report. For more information, see [Manage hardware emergency maintenance notifications](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#emergency-notifications).

## July 18, 2025

Feature

**Generally available** : You can troubleshoot workloads with slow performance by using straggler detection metrics and logs.

_Stragglers_ are single-point, non-crashing failures that eventually slow down your entire workload. Large-scale ML workloads are very susceptible to stragglers, and VMs with stragglers are often very difficult to notice and pinpoint without straggler detection.

For more information, see [Monitor VMs and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor) and [Troubleshoot slow performance](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance).

## July 10, 2025

Feature

**Generally available** : You can now manage the [Collective Communication Analyzer (CoMMA)](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma), a library that uses the NVIDIA Collective Communication Library (NCCL) profiler plugin to collect detailed NCCL telemetry for GPU machine types. The collected performance metrics and operational events are used for analyzing and optimizing large-scale AI and ML training workloads.

CoMMA is automatically installed and enabled on A4X, A4 High, and A3 Ultra machine types when using specific images. You can manage this data collection by disabling the plugin, adjusting its data granularity levels, or manually installing it on other GPU machine types. For more information, see [Enable, disable, and configure CoMMA](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/configure-comma).

## July 07, 2025

Feature

**Preview** : You can use future reservations in calendar mode to obtain resources for up to 90 days. By creating a request in calendar mode, you can reserve up to 80 GPU VMs for a future date and time. Then, you can use that capacity to run the following workloads:

  * Model pre-training

  * Model fine-tuning

  * Simulations

  * Inference




For more information, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

## June 11, 2025

Feature

**Generally available** : You can apply a workload policy in a managed instance group (MIG) to specify the type of the workload to run on the MIG. Workload policies help improve the workload performance by optimizing the underlying infrastructure. The supported type, `high-throughput`, is ideal for workloads that require high networking performance. For more information, see [Workload policy for MIGs](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy#workload-policy).

## May 22, 2025

Feature

**Generally available** : You can proactively manage upcoming maintenance host events on your reserved blocks of capacity, whether VMs are running on them or not. This approach helps you minimize disruptions and maintain optimal performance. For more information, see [Manage host events across reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations).

## May 15, 2025

Feature

**Preview:** You can use the Flex-start consumption option to obtain resources for up to seven days. Flex-start provisions capacity from a secured resource pool. Using this feature increases your chance to obtain high-demand resources like GPUs. For more information, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

## March 18, 2025

Feature

**Generally available** : The [A4 accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) is now generally available. A4 VMs are powered by NVIDIA B200 GPUs and provide up to 3x performance of previous GPU machine types for most GPU accelerated workloads. A4 is especially recommended for ML training workloads at large scales. A4 is available in the following region and zone:

  * Council Bluffs, Iowa: `us-central1-b`



When provisioning A4 machine types, you can use [Hypercompute Cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/hypercompute-cluster) to request capacity and create VMs or clusters. To get started see [Overview of creating VMs and clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

**Software stack updates**

The following new Docker images are also released to support workloads running on your [A4 GKE clusters that are deployed using Hypercompute Cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute).

  * NeMo docker image: `nemo25.02-gib1.0.5-A4`
  * MaxText docker image: `jax-maxtext-gpu:jax0.5.1-cuda_dl25.02-rev1-maxtext-20150317`



For more information, see [AI Hypercomputer images](https://docs.cloud.google.com/ai-hypercomputer/docs/software-stack).

## December 31, 2024

Feature

**Preview** : [Hypercompute Cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/hypercompute-cluster) is now available in preview. With Hypercompute Cluster, you can streamline the provisioning of up to tens of thousands of A3 Ultra accelerator-optimized machines. 

With features such as dense co-location of resources, ultra-low latency networking, targeted workload placement, and advanced maintenance controls to minimize workload disruptions, Hypercompute Cluster is built to deliver exceptional performance and resilience, so you can run your most demanding AI, ML, and HPC workloads with confidence. 

To get started, review the overview for [VM and cluster creation](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

Feature

**Generally available** : The [A3 Ultra accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) is now generally available. A3 Ultra VMs are powered by NVIDIA H200 Tensor Core GPUs and support the new Titanium ML network adapter, which delivers non-blocking 3.2 Tbps of GPU-to-GPU traffic with RDMA over Converged Ethernet (RoCE). A3 Ultra VMs are ideal for foundation ML model training and serving. The A3 Ultra machine type is available in the following region and zone:

  * St. Ghislain, Belgium, Europe - `europe-west1-b`



When provisioning A3 Ultra machine types, you must use [Hypercompute Cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/hypercompute-cluster) to request capacity and create VMs or clusters. To get started see [Overview of creating VMs and clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) in the AI Hypercomputer documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
