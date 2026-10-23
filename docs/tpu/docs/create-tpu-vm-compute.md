---
url: https://docs.cloud.google.com/tpu/docs/create-tpu-vm-compute/
title: Cloud TPU creation overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:23.295004+00:00
---

# Cloud TPU creation overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/create-tpu-vm-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud TPU creation overview

Compute Engine lets you create and manage TPU virtual machines (VMs) either as individual instances or as part of a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups). MIGs can have multiple single-host TPU VMs or multi-host TPU slices. MIGs with single-host VMs are best for when you have multiple, independent workloads, for example, inference workloads. MIGs with multi-host TPU slices have multiple, interconnected TPU VMs that work together as a unit on a single workload. How you create and manage your TPU VMs depends on your workload requirements.

To learn how to create a single TPU VM, see [Create a single TPU VM instance](https://docs.cloud.google.com/tpu/docs/create-instance-compute). To learn about MIGs and TPUs, see [Create Cloud TPU VMs with MIGs](https://docs.cloud.google.com/tpu/docs/tpus-and-migs)

## What's next

  * Learn how to [Create a MIG with single-host Cloud TPU slices](https://docs.cloud.google.com/tpu/docs/create-single-host-mig).
  * Learn how to [Create a MIG with a multi-host Cloud TPU slice](https://docs.cloud.google.com/tpu/docs/create-multi-host-mig).
  * Learn how to [manage TPU VMs](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute).
  * Learn about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
