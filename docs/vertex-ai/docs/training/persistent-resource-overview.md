---
url: https://docs.cloud.google.com/vertex-ai/docs/training/persistent-resource-overview/
title: Overview of persistent resources \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:52.044910+00:00
---

# Overview of persistent resources  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/training/persistent-resource-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Overview of persistent resources Stay organized with collections  Save and categorize content based on your preferences. 

A Gemini Enterprise Agent Platform persistent resource is a long-running cluster that you can create to run serverless training jobs. After a training job completes, the persistent resource remains available to run other training jobs until you delete it. You can use a persistent resource to ensure compute resource availability and to reduce the job startup time that's otherwise needed for compute resource creation. Persistent resources support all VMs and GPUs that are supported by serverless training jobs. This page explains when to use a persistent resource and gives you information about billing and quota.

## When to use a persistent resource

We recommend using persistent resources in the following scenarios:

  * You want to ensure capacity availability for critical ML workloads or during peak seasons. Unlike custom jobs, where the training service releases the resource after job completion, persistent resource remains available until it's deleted.
  * You're submitting the same job multiple times and can benefit from data and image caching by running the jobs on the same persistent resource.
  * You run many short-lived training jobs where the actual training time is shorter than the job startup time.



For more context on when to and why use a persistent resource, see the blog post [Bringing capacity assurance and faster startup times to Gemini Enterprise Agent Platform Training](https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-persistent-resources-and-capacity-assurance).

## Billing details

You are billed for the entire duration that a persistent resource is in a running state, regardless of whether there is a job running on the persistent resource. For each instance in the persistent resource pool, you are billed by core hour. All jobs running on a persistent resource are not separately charged. You are billed only for the persistent resource.

If you set up auto scaling for your persistent resource, you only pay for the provisioned instances. For example, if `min-replica-count` is set to `4`, `4` instances are always provisioned and this is the minimum amount you're billed for. When your workload increases, the resource pool might scale up to `6` to accommodate the increased demand. Then, you're billed for the `6` provisioned instances until your resource pool scales down again. To avoid paying for idle nodes, use auto scaling for your persistent resource, or delete it when you no longer need it. To learn more about pricing, see the [Custom-trained models](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing#custom-trained_models) section in the Gemini Enterprise Agent Platform pricing page.

## Quotas

Persistent resources use your training quota, so verify you have sufficient quota for persistent resource creation. To learn more about quotas, see [Training quotas and limits](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/quotas#training).

## What's next

  * [Create and use a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-create).
  * [Run training jobs on a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-train).
  * [Get information about a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-get).
  * [Reboot a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot).
  * [Delete a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-delete).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
