---
url: https://docs.cloud.google.com/capacity-planner/docs/enable-quota-adjuster/
title: Enable the quota adjuster \u00a0|\u00a0 Capacity Planner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:34.458022+00:00
---

# Enable the quota adjuster  |  Capacity Planner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/capacity-planner/docs/enable-quota-adjuster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Capacity Planner ](https://docs.cloud.google.com/capacity-planner/docs)
  * [ Guides ](https://docs.cloud.google.com/capacity-planner/docs/overview)



Send feedback 

#  Enable the quota adjuster Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to set up automatic request submissions for quota increase for your project in Capacity Planner. To learn more about Capacity Planner, see [Capacity Planner overview](https://docs.cloud.google.com/capacity-planner/docs/overview).

Capacity Planner lets you enable the [quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster) in your project. This setting allows Google Cloud to automatically submit quota increase requests on your behalf when your quota nears a limit.

You can enable the quota adjuster to do the following:

  * Proactively respond to planned or unplanned increases in usage.

  * Help prevent outages when reaching a quota.

  * Reduce the need to submit manual quota increase requests.




To disable the quota adjuster in your project, see instead [Disable the quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster#disable).

## Limitations

Before you enable the quota adjuster in your project, consider the following limitations:

  * You can enable the quota adjuster in your project only if your project has sufficient usage data.

  * You can enable the quota adjuster only for specific resources. For a complete list of supported resources, see [Availability](https://docs.cloud.google.com/docs/quotas/quota-adjuster#availability).




## Before you begin

  * If you can't access Capacity Planner in the Google Cloud console, then your organization might not be eligible to access and use Capacity Planner. To request access, contact your [Technical Account Manager (TAM)](https://cloud.google.com/tam) or the [Sales team](https://cloud.google.com/contact).



### Required roles

To get the permissions that you need to manage the quota adjuster in Capacity Planner, ask your administrator to grant you the following IAM roles on your project: 

  * To access and view Capacity Planner: [Capacity Planner Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`) 
  * To access and manage the quota adjuster in your project: [Quota Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.quotaAdmin) (`roles/servicemanagement.quotaAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage the quota adjuster in Capacity Planner. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage the quota adjuster in Capacity Planner:

  * To view the forecasted usage of your Compute Engine resources: `capacityplanner.forecasts.list` on the project 
  * To view the usage of your Compute Engine resources: `capacityplanner.usageHistories.list` on the project 
  * To summarize the usage of your Compute Engine resources: `capacityplanner.usageHistories.summarize` on the project 
  * To view the quota adjuster settings: `cloudquotas.quotas.get` on the project 
  * To enable or disable the quota adjuster: `cloudquotas.quotas.update` on the project 
  * To access your project's quota usage: `monitoring.timeseries.list` on the project 
  * To view your project's quota: 
    * `serviceusage.quotas.get` on the project
    * `serviceusage.services.get` on the project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable the quota adjuster

To enable the quota adjuster in your project, do the following:

  1. In the Google Cloud console, go to the **Capacity Planner** page.

[Go to Capacity Planner](https://console.cloud.google.com/capacity/usage)

  2. Optional: To change project, in the project picker at the top of the page, select another project.

  3. In the navigation menu, click the **Virtual machine** tab.

  4. In the **Usage and forecast by machine family** graph, click **Enable quota adjuster**. The **Quotas** page appears and the **Configurations** tab is selected.

![The Enable quota adjuster button on the Capacity Planner page.](https://docs.cloud.google.com/capacity-planner/images/enable-quota-adjuster-button.png)

  5. To enable the quota adjuster, click **Enable**.




After you enable the quota adjuster, you can [create alert policies to monitor it](https://docs.cloud.google.com/docs/quotas/quota-adjuster#alerts).

## What's next

  * [Quotas and limits for Compute Engine](https://docs.cloud.google.com/compute/quotas-limits)

  * [Audit logging information for Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/audit-logging)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
