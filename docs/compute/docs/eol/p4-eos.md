---
url: https://docs.cloud.google.com/compute/docs/eol/p4-eos/
title: NVIDIA P4 end of support \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:49.312034+00:00
---

# NVIDIA P4 end of support  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/eol/p4-eos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  NVIDIA P4 end of support Stay organized with collections  Save and categorize content based on your preferences. 

NVIDIA P4 GPUs on Google Cloud will reach end of support (EOS) on **August 1, 2027**.

## What you need to know

As of August 1, 2027, you cannot create, launch, or access any Google Cloud resources that run NVIDIA P4 GPUs. This deprecation affects resources for the following services:

  * Compute Engine: Compute Engine instances
  * Google Kubernetes Engine (GKE): nodes
  * Gemini Enterprise Agent Platform: models, jobs, and endpoints
  * Cloud Workstations: workstations
  * Dataflow: pipeline jobs
  * Managed Service for Apache Spark: clusters and serverless batches
  * Deep Learning VM and Container-Optimized OS VM instances



### Committed use discounts (CUDs)

You can no longer purchase or renew 3-year [committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#resource_based) for NVIDIA P4 GPUs. Your existing active 1-year and 3-year commitments remain valid until their expiration date. If you have active commitments that expire after the platform's End of Life (EOL) date, contact your account team or Technical Account Manager (TAM) to discuss your migration options and develop a transition plan.

## How this EOS impacts your existing resources

Until August 1, 2027, your resources that run NVIDIA P4 GPUs continue to function normally. However, because NVIDIA P4 GPUs are approaching their EOS, you must migrate your workloads to modern GPU alternatives before the decommission date. Google Cloud does not support EOS products or features.

As of the final decommission date on August 1, 2027, Google Cloud will shut down any remaining compute instances and resources running NVIDIA P4 GPUs, and you can no longer create, launch, or access them.

## What you need to do

To transition your workloads to supported GPUs, choose a new GPU model, review its availability in your regions, and migrate your workloads before August 1, 2027.

### Choose a GPU model

We recommend migrating your workloads to modern GPU alternatives, specifically the **G4** or **G2** machine series. To determine the best GPU model for your workload, compare the following options:

Feature | G2 (NVIDIA L4) | G4 (NVIDIA RTX PRO 6000)  
---|---|---  
**Best for** | High-performance AI inference, generative AI, video transcoding and streaming, graphics, and light machine learning (ML) training. L4 GPUs provide a direct, high-efficiency upgrade for P4 inference and transcoding workloads. | High-performance simulation, NVIDIA Omniverse workloads, 3D graphics rendering, local LLM fine-tuning and inference, virtual workstations (vWS), and fractional GPU (vGPU) sharing.  
**Architecture and memory** | Ada Lovelace architecture with 24 GB GDDR6 GPU memory. | Blackwell architecture with 96 GB GPU memory per GPU.  
**Machine series** | [G2 accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) | [G4 accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)  
  
For a comprehensive list and comparison of all GPU models, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus).

### Review available locations

To verify that your selected GPU model is available, review the location details for your service:

  * Gemini Enterprise Agent Platform: review [Gemini Enterprise Agent Platform accelerator locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations#accelerators).
  * Cloud Workstations: review [Cloud Workstations GPU availability by region and zone](https://docs.cloud.google.com/workstations/docs/available-gpus#gpu_availability_by_region_and_zone).
  * For all other services: review the available [GPU regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones).



## Migrate your workloads

Based on the service that you use, select one of the following transition paths:

### Compute Engine workloads

To transition your Compute Engine workloads to the recommended G2 (NVIDIA L4) or G4 (NVIDIA RTX PRO 6000) machine series, you must move to a new compute instance. You cannot modify an existing compute instance in-place from an N1 general-purpose machine type to an accelerator-optimized machine type.

To move to a new compute instance, complete the following steps:

  1. If your existing compute instance uses Local SSD disks that contain data you want to keep, move the contents of those disks to a Persistent Disk volume.
  2. Create a new compute instance. For instructions, see [Create a G2 or G4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series).

**Note:** To reuse most of your configurations from your existing compute instances, you can use the [**Create similar** option](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance). However, remember to update the machine series and GPU type.
  3. Move Persistent Disk volumes by detaching them from the old compute instance and attaching them to the new compute instance. You can alternatively [transfer files](https://docs.cloud.google.com/compute/docs/instances/transfer-files) from one compute instance to the other.

  4. Optional: Move the saved data from Persistent Disk volumes back to a Local SSD disk.

  5. [Reassign any static IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign) associated with the old compute instance to the new compute instance.

  6. [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) on the new compute instance.

  7. Install your applications on the new compute instance.

  8. Delete the old compute instance.




### Other Google Cloud workloads

If your workloads run on services other than Compute Engine such as GKE, Gemini Enterprise Agent Platform, Cloud Workstations, Dataflow, or Managed Service for Apache Spark, then do the following:

  1. Update your configurations to reference a supported GPU model.

     * For GKE, Gemini Enterprise Agent Platform, or Cloud Workstations, update your configuration templates.
     * For Dataflow, update your pipeline specifications.
     * For Managed Service for Apache Spark, update your cluster definitions.

For instructions about configuring GPUs for your service, see the product documentation for that service.

  2. Restart or recreate your resources.




## What's next

  * Learn more [about GPUs](https://docs.cloud.google.com/compute/docs/gpus/about-gpus).
  * Learn about [GPU machines in the accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines).
  * Review [GPU pricing](https://cloud.google.com/compute/gpus-pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
