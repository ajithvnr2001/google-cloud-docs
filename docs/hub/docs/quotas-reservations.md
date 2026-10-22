---
url: https://docs.cloud.google.com/hub/docs/quotas-reservations/
title: View quotas and reservations \u00a0|\u00a0 Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:54.081195+00:00
---

# View quotas and reservations  |  Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/quotas-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)



Send feedback 

#  View quotas and reservations Stay organized with collections  Save and categorize content based on your preferences. 

On the **Quotas & reservations** page, you can view aggregated data for quotas, system limits, and Compute Engine resource usage.

  * View Google Cloud quotas and system limits with over 90% usage.
  * View historical and forecasted usage of Compute Engine resources.
  * View Compute Engine [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).



Use this data to better understand current quota and Compute Engine usage and plan for future needs.

## Required roles

To get the permissions that you need to view quotas, system limits, and Compute Engine resource usage, ask your administrator to grant you the [Cloud Hub Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To make changes to quotas or reservations, additional permissions are required.

  * For permissions to work with quotas, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/permissions).
  * For requirements and permissions to create future reservation requests, see the documentation for [creating future reservations](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations).



## View quotas and system limits

_Quotas_ restrict how much of a Google Cloud resource your Google Cloud project can use. You can request an increase or decrease to your quota. _System limits_ are fixed constraints and aren't adjustable.

You can view the following information for a selected project:

  * Quotas and system limits that are over 90% used.
  * Pending quota increase requests.



To view quota information:

  1. In the Google Cloud console, go to the **Quotas and Reservations** page,

[Go to Quotas & reservations](https://console.cloud.google.com/cloud-hub/quotas-and-reservations)

  2. In the project selector, select the project that you want to view.




The page displays the following information for the selected project:

  * **Quotas & System Limits at risk**: displays quotas and system limits that are over 90% used.

    * To view more information about a quota or system limit, click its name.
    * To view all quotas with usage over 90%, click **View all at risk**.

If you click one of the links, then the Quotas & System Limits page displays the quota details. If you have the necessary permissions, then you can [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#managing_your_quota_console).

  * **Quotas & System Limits summary**: displays additional information about quotas.

    * **All quotas and system limits** : displays the total number of quotas and system limits. To view a list of quotas and system limits for the selected project, click **View**.
    * **Pending increase requests** : displays the total number of pending quota increase requests. To view pending requests for the selected project, click **View requests**.
    * **Quota adjuster status** : displays whether the [quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster) is enabled or disabled. The quota adjuster is only available for projects with enough historical activity to support accurate predictions for submitting proactive quota adjustment requests on your behalf. To view or change the setting, click **View**.



For more information about viewing and managing quotas on the Quotas & System Limits page, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

## View usage and forecast data

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can view the usage and forecast data of the following Compute Engine resources:

  * Compute Engine instances, including vCPUs, RAM, and Local SSD disks attached to the instances.

  * Persistent Disk volumes, whether they're attached to instances or not.

  * GPUs, whether they're attached to instances or not.




To plan for future usage, you can explore additional details in [Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/overview) and request future reservations to reserve capacity in advance.

**Note:** If the **Quotas and reservations** page doesn't display a section for usage and forecast data, then your project might not be eligible to use this feature. To request access, contact your [Technical Account Manager (TAM)](https://cloud.google.com/tam) or the [Sales team](https://cloud.google.com/contact).

To view usage and forecast data:

  1. In the Google Cloud console, go to the **Quotas and Reservations** page,

[Go to Quotas & reservations](https://console.cloud.google.com/cloud-hub/quotas-and-reservations)

  2. In the project selector, select the project that you want to view.

  3. In the **Usage and Forecast** section, use the selectors to choose the data that you want to view.

     * **Resource type** : Select the resource type you want to view.
     * **Resource name** : If you selected **vCPU** , **RAM** , or **Local SSD** as the resource type, select a machine family. To view all machine families, select **ALL**.
     * **Location** : Select a region or zone that you want to view.

The **Usage and Forecast** graph displays usage, forecast data for the next six months, reservations (if any), and quota for the selected resource type and location.

     * Quota data only appears on the graph if you selected resource and location options that have an associated quota.
     * The **Usage** line shows the history of daily usage aggregated at the 99th percentile. Historical usage data is updated every 24 hours.
     * The **Forecast** line shows an estimate of future usage based on historical usage patterns. It is an upper bound of P50 prediction interval.

For more information about usage and forecast data, see the [Capacity Planner overview](https://docs.cloud.google.com/capacity-planner/docs/overview#how_works).

     * You can view historically reserved capacity for your instances from August 1, 2024.

  4. To change the time range that the graph displays, use one of the following options:

     * **Expand a specific time interval** : drag to select the time range that you want to magnify.
     * **Pan** : press `Control` or `Command`, and then drag horizontally to shift the time range.
     * **Zoom** : press `Control` or `Command`, and then scroll to zoom in or zoom out.
  5. To explore the selected data further in Capacity Planner, click **Plan capacity**. Capacity Planner provides detailed views on usage, forecast, and reservations. It also lets you create future reservations based on historical usage and forecast data at the machine type level. Learn more about [requesting future capacity](https://docs.cloud.google.com/capacity-planner/docs/create-future-reservations).

Capacity Planner displays data for resources you selected on the **Quotas & reservations** page. To learn about using the graphs in Capacity Planner, see [View usage and forecast data in Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/view-data).




## View reservations

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can view current usage for Compute Engine reservations. Comparing current usage with historical or forecast usage can help you better plan for future capacity needs.

**Note:** If the **Quotas & reservations** page doesn't display a section for reservation usage, then your project might not be eligible to use this feature. To request access, contact your [Technical Account Manager (TAM)](https://cloud.google.com/tam) or the [Sales team](https://cloud.google.com/contact).

To view reservation usage:

  1. In the Google Cloud console, go to the **Quotas and Reservations** page,

[Go to Quotas & reservations](https://console.cloud.google.com/cloud-hub/quotas-and-reservations)

  2. In the project selector, select the project that you want to view.




The **Utilization of reservations** section displays usage of your reservations in the last 24 hours. To view and manage reservations, click **Manage reservations**.

For more information about viewing reservation details, see [View reservations or future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view).

## What's next

  * Learn about [setting up alerts and monitoring](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts) for quotas.
  * Learn more about [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).
  * Learn more about [Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/overview). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
