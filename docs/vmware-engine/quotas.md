---
url: https://docs.cloud.google.com/vmware-engine/quotas/
title: Quotas and limits \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:57.732996+00:00
---

# Quotas and limits  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/vmware-engine/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This document lists the quotas and system limits that apply to Google Cloud VMware Engine.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on VMware Engine resources. System limits can't be changed. 

Before you can deploy a Google Cloud VMware Engine private cloud to a Google Cloud project, that Google Cloud project must have a quota of nodes. A VMware Engine node quota describes the maximum number of nodes you can use, assuming nodes are available.

## Regional and global quotas

You assign VMware Engine node quota per Google Cloud project, per region. Additionally, your Google Cloud project has a global node quota that represents the total quota across all regions. To increase your quota and assign more nodes, you must submit a quota increase request and receive approval.

For example, you have a global quota of 12 nodes and the same regional quota of 8 nodes for each region. To create 16 nodes in `us-central1` and 8 nodes in `europe-west2`, you must increase your global quota by 12 and your `us-central1` regional quota by 8. These increases result in a global quota of 24 nodes, a regional quota of 16 nodes in `us-central1`, and regional quota of 8 nodes in all other regions.

## Quotas and resource availability

Quotas don't ensure node availability. If no resources are available, you won't be able to create private clouds or add nodes to an existing private cloud. This is the case even if you have remaining quota in your region or Google Cloud project.

**Note:** If you have a business-critical workload or plan to deploy a large number of nodes, contact your Google Cloud sales representative, account team, or Google Cloud Support to discuss capacity planning and reservations to ensure capacity availability.

## Viewing quota

To view your regional or global quota, do the following:

  1. In the Google Cloud console, go to **IAM & Admin > Quotas**.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. On the **Quotas** page, filter by service for **VMware Engine API**.

  3. Click the quota entry for the node type and quota type (regional or global) that you want information about.

  4. The **Current usage** column shows the number of nodes used in the selected quota type.

  5. A panel appears and describes your quota as the **Limit** globally or for each region.




## Requesting quota

When you need additional resources, you can submit a quota increase request. As a convenience, you can request only a regional quota increase if you plan to exceed both your global and regional quota at the same time. If approved, your global quota updates as needed to match your requested regional quota increase.

To request a regional quota increase of nodes for the Google Cloud project containing your private cloud, do the following:

  1. In the Google Cloud console, go to **IAM & Admin > Quotas**.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. On the **Quotas** page, filter by service for **VMware Engine API**.

  3. Select the quota entry for the node type you want quota for. For example, the entry with limit name "VMware Engine standard 72 vCPUs nodes per region" in the region "australia-southeast1".

  4. Click **Edit Quotas**.

  5. Enter the new limit you want to request, and click **Done**. You must request at least three nodes if you are requesting quota for this Google Cloud project for the first time.

  6. Click **Submit Request**.




If you want to request an increase in global quota, perform the previous steps using the _VMware Engine standard 72 vCPUs nodes across regions_ quota entry instead. The most common situation for a global quota increase request is when you already have sufficient regional quota. If this applies to you, use the **Request description** field to describe your situation before submitting your request.

**Note:** A request to decrease quota is rejected by default. If you must reduce your quota, reply to the support email with an explanation of your requirements. A support representative from the Compute Engine team will respond to your request within 24 to 48 hours.

## What's next

  * Review private cloud [limitations](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#limitations).
  * [Create a VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud).
  * [Manage your private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
