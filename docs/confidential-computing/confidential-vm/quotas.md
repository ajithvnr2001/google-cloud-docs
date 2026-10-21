---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/quotas/
title: Quotas and limits \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:17.089951+00:00
---

# Quotas and limits  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Resources ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/get-support)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

Confidential VM is subject to the [Compute Engine resource quotas](https://docs.cloud.google.com/compute/quotas) because it is a type of Compute Engine VM.

## What is a quota?

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

## View quota values

Not all projects have the same quota values. As you use Google Cloud, your quotas may increase accordingly. Learn how to [view your quota values](https://docs.cloud.google.com/docs/quotas/view-manage).

## Increase your quota

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

For NVIDIA RTX PRO 6000 quota requests, see NVIDIA RTX PRO 6000.

For NVIDIA H100 quota requests, see NVIDIA H100.

## GPU quotas

To create Confidential VM instances with attached NVIDIA GPUs, you must have sufficient [GPU quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota) in your Google Cloud project for the specific GPU type, region, and instance provisioning model that you want to use.

### NVIDIA RTX PRO 6000

Confidential VM instances that are based on the G4 machine type use NVIDIA RTX PRO 6000 GPUs and consume GPU quotas based on the instance provisioning model:

  * **Standard (on-demand) VM instances** : Consume the `GPU_FAMILY:NVIDIA_RTX_PRO_6000` quota.

  * **Spot VM and Flex-start VM instances** : Consume the `PREEMPTIBLE_NVIDIA_RTX_PRO_6000_GPUS` quota.




Quota requests for NVIDIA RTX PRO 6000 GPUs follow the Google Cloud process. For more information, see [View and manage quotas](https://docs.cloud.google.com/docs/quota/view-manage#requesting_higher_quota).

**Note:** If you want to use committed use discounts with G4 instances, you must have committed GPU quota (`COMMITTED_NVIDIA_RTX_PRO_6000_GPUS`) in your project. This quota is required when purchasing the commitment, not when creating the instance. For more information, see [Commitment quotas](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#quota).

### NVIDIA H100

Confidential VM instances that are based on the A3 High machine type use NVIDIA H100 GPUs. You need sufficient quota in the following quota types to create a Confidential VM instance with GPU successfully:

  * Preemptible quota for the GPU models that you want to create in each region.

  * Global quota for the total number of GPUs of all types in all regions.




To request a quota increase, complete the following instructions based on the type of quota you need.

###  Preemptible quota 

To request a regional preemptible NVIDIA H100 GPUs quota increase, do the following:

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the **Filter** box, enter `PREEMPTIBLE_NVIDIA_H100_GPUS`, and then press the `Enter` or `Return` key.

  3. In the **Dimensions** column of the table, find the row with the region whose quota you want to increase.

  4. In that row, click more_vert **More actions** , and then click **Edit quota**.

  5. In the **Quota changes** pane, enter the number of GPUs you want in the **New value** box.

  6. Click **Submit request**.




###  Global quota 

To request a global quota increase, do the following:

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the **Filter** box, enter `GPUS_ALL_REGIONS`, and then press the `Enter` or `Return` key.

  3. In the resulting row, click more_vert **More actions** , and then click **Edit quota**.

  4. In the **Quota changes** pane, enter the number of GPUs you want in the **New value** box.

  5. Click **Submit request**.




#### What happens after a quota request

If your quota request is successful, you're sent an approval email. Wait about 15 minutes after you receive the email, and then refresh the [**Quotas** page](https://console.cloud.google.com/iam-admin/quotas) to check for the updated quota. If the quota still hasn't been updated after 15 minutes, contact [Cloud Customer Care](https://docs.cloud.google.com/support).

If your quota request is denied, you might receive an email explaining the next steps you can take. To reapply for more quota, follow the instructions in the email. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
