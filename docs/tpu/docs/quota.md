---
url: https://docs.cloud.google.com/tpu/docs/quota/
title: Cloud TPU quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:14.120755+00:00
---

# Cloud TPU quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Resources ](https://docs.cloud.google.com/tpu/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud TPU quotas

**Important:** This document describes Cloud TPU API quota. If you are using Google Kubernetes Engine or Compute Engine to manage TPUs, you use Compute Engine API quota, which is a different quota. For more information about quota for TPUs in GKE, see [Ensure sufficient quota](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota). For more information about quota for TPUs in Compute Engine, see [TPU quota](https://docs.cloud.google.com/compute/resource-usage#tpu_quota).

This document lists the quotas that apply to Cloud TPU. For information about Cloud TPU pricing, see [Cloud TPU pricing](https://cloud.google.com/tpu/pricing).

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

## TPU quota

TPU quotas are limits on the number of Cloud TPU cores you can use with a Google Cloud project. Each version of TPU is associated with its own quota. In addition, each Cloud TPU version quota is divided into on-demand quota and [preemptible](https://docs.cloud.google.com/tpu/docs/preemptible) (or spot) quota.

**Note:** For more information about TPU chips and TensorCores, see [TPU System architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm).

When you create Cloud TPU resources, by default you are creating on-demand resources. You can create preemptible resources using the `--spot` parameter when creating resources with the `gcloud` command. For more information, see [Manage TPU resources](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm).

## Default Cloud TPU quotas

The following tables show default values for on-demand and preemptible quota for each [available zone](https://docs.cloud.google.com/tpu/docs/regions-zones). These values specify the maximum number of TPU cores you can use within your project.

### Preemptible quotas

TPU version | Default quota (number of cores) | Quota name  
---|---|---  
v6e | 1536 cores | Preemptible TPU v6e cores per project per zone  
v5p | 768 cores | Preemptible TPU v5p cores per project per zone  
v5e | 1536 cores | Preemptible TPU v5 lite pod cores per project per zone  
v4 | 0 cores | Preemptible TPU v4 pod cores per project per zone  
v3 pod | 32 cores | Preemptible TPU v3 pod cores per project per zone  
v3 | 120 cores | Preemptible TPU v3 cores per project per zone  
v2 pod | 32 cores | Preemptible TPU v2 pod cores per project per zone  
v2 | 120 cores | Preemptible TPU v2 cores per project per zone  
  
### On-demand quotas

TPU version | Default quota (number of cores) | Quota name  
---|---|---  
v6e | 512 cores | TPU v6e cores per project per zone  
v5p | 128 cores | TPU v5p cores per project per zone  
v5e | 512 cores | TPU v5 lite pod cores per project per zone  
v4 | 0 cores | TPU v4 pod cores per project per zone  
v3 pod | 32 cores | TPU v3 pod cores per project per zone  
v3 | 40 cores | TPU v3 cores per project per zone  
v2 pod | 32 cores | TPU v2 pod cores per project per zone  
v2 | 40 cores | TPU v2 cores per project per zone  
  
**Note:** All requests for quota in us-central2-b (currently, only TPU v4) need to be manually approved by Google. No default quota is granted. If you require quota in us-central2-b, request quota for v4 using the same process as described in the following section.

## View and request additional quota

You can view the quota allocated for your Google Cloud project on the [Quotas page in the Google Cloud console](https://console.cloud.google.com/apis/api/tpu.googleapis.com/quotas).

You can request additional Cloud TPU quota, from the [Quotas page](https://console.cloud.google.com/iam-admin/quotas). To find the quota you want to increase, click the three vertical dots and choose **Edit quota**. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota). If you request quota below the auto-approve threshold, your request will be automatically approved.

### Preemptible quotas

TPU version | Auto-approve threshold | Quota name  
---|---|---  
v6e | All zones: 0 cores | Preemptible TPU v6e cores per project per zone  
v5p | All zones: 0 cores | Preemptible TPU v5p cores per project per zone  
v5e | 

  * us-east5-b: 800 cores
  * us-west4-a: 1600 cores
  * us-west4-b: 3968 cores
  * us-west1-c: 576 cores
  * us-central1-a: 3264 cores
  * europe-west4-a: 4032 cores

| Preemptible TPU v5 lite pod cores per project per zone  
v4 | All zones: 0 cores | Preemptible TPU v4 pod cores per project per zone  
v3 pod | 

  * europe-west4-a: 512 cores
  * us-east1-d: 320 cores

| Preemptible TPU v3 pod cores per project per zone  
v3 | 

  * us-central1-a: 64 cores
  * europe-west4-a: 128 cores

| Preemptible TPU v3 cores per project per zone  
v2 pod | 

  * us-central1-a: 64 cores
  * europe-west4-a: 64 cores

| Preemptible TPU v2 pod cores per project per zone  
v2 | 

  * us-central1-b: 128 cores
  * us-central1-c: 64 cores
  * us-central1-f: 128 cores
  * europe-west4-a: 32 cores

| Preemptible TPU v2 cores per project per zone  
  
### On-demand quotas

TPU version | Auto-approve threshold | Quota name  
---|---|---  
v6e | All zones: 0 cores | TPU v6e cores per project per zone  
v5p | us-east5-a: 64 core | TPU v5p cores per project per zone  
v5e | All zones: 64 cores | TPU v5 lite pod cores per project per zone  
v4 | All zones: 0 cores | TPU v4 pod cores per project per zone  
v3 pod | 

  * europe-west4-a: 128 cores
  * us-east1-d: 64 cores

| TPU v3 pod cores per project per zone  
v3 | 

  * us-central1-a: 64 cores
  * europe-west4-a: 128 cores

| TPU v3 cores per project per zone  
v2 pod | 

  * us-central1-a: 64 cores
  * europe-west4-a: 64 cores

| TPU v2 pod cores per project per zone  
v2 | 

  * us-central1-b: 128 cores
  * us-central1-c: 64 cores
  * us-central1-f: 128 cores
  * europe-west4-a: 32 cores

| TPU v2 cores per project per zone  
  
You will receive an email stating if your quota request is approved or denied. Google Cloud service quota increases take place gradually. This might result in ongoing rollouts across different regions or resources. During the rollout, the quota value that appears in the Google Cloud console or Cloud Quotas API won't reflect the new, increased quota value until the rollout completes. For more information, see [View ongoing rollouts](https://docs.cloud.google.com/docs/quotas/view-ongoing-rollouts).

## What's next

  * Learn how to [create TPU VMs](https://docs.cloud.google.com/tpu/docs/create-tpu-vm)
  * Learn how to [manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
