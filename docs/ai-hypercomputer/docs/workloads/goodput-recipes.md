---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/goodput-recipes/
title: Goodput optimization recipes \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:53.712033+00:00
---

# Goodput optimization recipes  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/goodput-recipes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Goodput optimization recipes Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document helps you optimize the _goodput_ , the rate of useful data transferred, for your workloads. To achieve this optimization, we have curated reproducible goodput recipes that use common machine learning (ML) frameworks and models. To review these recipes, see the [AI Hypercomputer GitHub organization](https://github.com/orgs/AI-Hypercomputer/repositories). The goodput recipes were tested on clusters that were created by using Cluster Toolkit.

**Important:** Only A4X, A4, and A3 Ultra virtual machine (VM) instances that you created by using reserved capacity support goodput recipes.

To help ensure optimal workload reliability and maximize your goodput, you can also proactively identify nodes in a Google Kubernetes Engine (GKE) cluster that are likely to degrade in the next five hours. This early warning helps you avoid scheduling new workloads on at-risk VMs, thereby reducing the risk of interruptions to your jobs. For more information, see [Enable node health prediction](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/enable-node-health-prediction).

## Before you begin

Before you use the goodput recipes in this document, complete the following steps if you haven't already:

  1. [Choose an accelerator that best suits your workload](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy)

  2. [Choose a consumption method based on your accelerator of choice](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models)

  3. [Create your cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#accelerators-pre-train)




## Recipes

The following reproducible goodput recipes are available for pre-training on GKE clusters:

**Recipe name** | **Accelerator** | **Model** | **Framework** | **Workload type**  
---|---|---|---|---  
[Llama3.1 70B - A3 Mega](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/training/a3mega/llama3-1-70b/nemo-pretraining-gke-resiliency/README.md) | A3 Mega | Llama3.1 70B | NeMo | Pre-training on GKE  
  
## What's next

  * Learn how to [optimize cluster networking by using NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
