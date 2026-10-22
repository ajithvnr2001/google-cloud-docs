---
url: https://docs.cloud.google.com/compute/quotas-limits/
title: Compute Engine quota and limits overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:20.270373+00:00
---

# Compute Engine quota and limits overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/quotas-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Compute Engine quota and limits overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Compute Engine resources. System limits can't be changed. 

There are three categories of Compute Engine quotas and limits:

  * **Resource quotas** : Quotas that restrict usage of Compute Engine resources, such as virtual machine (VM) instances and GPUs. For more information, see [Resource usage quotas and permission management](https://docs.cloud.google.com/compute/resource-usage).
  * **API quotas** : Quotas that restrict how often you can call the Compute Engine API. For more information, see [Compute Engine API quotas](https://docs.cloud.google.com/compute/api-quota).
  * **Concurrent operation quotas** : Limits that restrict the number of in-flight Compute Engine operations. For more information, see [Compute Engine concurrent operation quotas](https://docs.cloud.google.com/compute/operations-quota).



## Permissions for checking and editing usage limits

To _view_ your quotas, you must have the [`serviceusage.quotas.get`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.quotas.get) permission.

To _change_ your quotas, you must have the [`serviceusage.quotas.update`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.quotas.update) permission.

These permissions are included by default in the [basic IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) of Owner and Editor and in the predefined [Quota Administrator role](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement).

## Check your allocation quota

_Regional_ quotas are not a subset of _project_ quotas. Virtual machine (VM) instances are a part of regional quotas.

If you're looking for regional quotas, such as how many VMs you can create in a region, see Check regional quota. To check your _project_ quota, use the Google Cloud console or the Google Cloud CLI.

The following sections describe how to view the limits for allocation quota in your project. To view the limits for API quota and concurrent operations quota, use the `gcloud alpha services quota list` command. For more information, see [View concurrent operation quotas and limits](https://docs.cloud.google.com/compute/operations-quota#view_quota_limits).

For information about quota categories, see [About quotas](https://docs.cloud.google.com/docs/quotas/overview).

### Check regional quota

###  Console 

In the Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

###  gcloud 

List quotas in a region:
    
    
    gcloud compute regions describe REGION

Replace `REGION` with the name of the region for which you want a list of quota information.

### Check project quota

###  Console 

In the Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

###  gcloud 

Check project-wide quotas:
    
    
    gcloud compute project-info describe --project PROJECT_ID

Replace `PROJECT_ID` with your project ID.

## Edit your quota

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

## Quota rollouts

Occasionally, Google Cloud changes the default quota for resources and APIs. These changes take place gradually. During the rollout of a new default quota, the maximum quota that appears in the Google Cloud console might not reflect the actual maximum quota that is available to you.

For example, suppose that Google Cloud changes the default maximum quota for firewall rules from `200` to `300`, and you use the Google Cloud console to view your quota, you might see the new quota of `300`, even though your actual quota is `200` until the rollout completes.

For information about ongoing quota rollouts, see [known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues). If no issues are described, no quota rollouts are ongoing.

If a quota rollout is ongoing and you want to confirm the actual maximum quota that is available to you, use the Google Cloud CLI to check your quota. If you need more quota than you have access to, [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## What's next

  * View Compute Engine [Resource usage quotas and permission management](https://docs.cloud.google.com/compute/resource-usage).
  * View [Compute Engine API quotas](https://docs.cloud.google.com/compute/api-quota).
  * View [Compute Engine concurrent operation limits](https://docs.cloud.google.com/compute/operations-quota).
  * Read about [resource-based pricing](https://docs.cloud.google.com/compute/resource-based-pricing).
  * Read about [VM instances pricing](https://cloud.google.com/compute/vm-instance-pricing).
  * [View and manage quota](https://docs.cloud.google.com/docs/quotas/view-manage).
  * Learn how to [set up quota alerts](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
