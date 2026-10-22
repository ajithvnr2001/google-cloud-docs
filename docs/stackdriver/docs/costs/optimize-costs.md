---
url: https://docs.cloud.google.com/stackdriver/docs/costs/optimize-costs/
title: Optimize costs with the Cost Explorer \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:39.510066+00:00
---

# Optimize costs with the Cost Explorer  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/costs/optimize-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Optimize costs with the Cost Explorer Stay organized with collections  Save and categorize content based on your preferences. 

The Cost Explorer page lets you monitor and understand the costs and utilization of resources in your Google Cloud project or [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) application. The Cost Explorer provides a current and historical visualization of cost data and utilization metrics, helping you make informed decisions about optimization opportunities.

For example, developers and platform administrators in your organization might use the Cost Explorer when they want to do the following:

  * Determine how costs have increased for the App Hub workload `cymbal` in the last two weeks.

  * Determine which resources in your Google Cloud project have high cost and low utilization.

  * Identify high-cost Compute Engine managed instance groups (MIGs) that have a low utilization within an application.




To retrieve cost and utilization data programmatically for integration with other tools and data, use the [App Optimize API](https://docs.cloud.google.com/app-optimize/overview).

Gemini assistance is also available for optimizing costs and utilization. For more information, see [Optimize costs with Gemini assistance](https://docs.cloud.google.com/hub/docs/optimize-gemini).

This document is for developers and platform administrators. If you manage billing accounts or budgets in Cloud Billing, see the [Cloud Billing cost optimization documentation](https://docs.cloud.google.com/billing/docs/how-to/finops-hub), for information about using FinOps Hub and Gemini Cloud Assist in Cloud Billing.

## Before you begin

The Cost Explorer uses Cloud Billing to retrieve cost data, and Cloud Monitoring for utilization metrics. To use the Cost Explorer, you need access to Monitoring data and configuration information, as well as the ability to view Cloud Billing data.

**Note:** If you can't access the Cost Explorer in the Google Cloud console, then your organization might not be eligible to access and use the Cost Explorer.

  1. If you want to view cost data by App Hub application, then verify that you have [set up App Hub](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub) and created your applications.

  2. If you are only viewing cost data for a project, enable the App Optimize API. in the project.

     1. In the Google Cloud console toolbar, select the project where you want to enable the API.

     2. Enable the App Optimize API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=appoptimize.googleapis.com)




The Cost Explorer only supports applications managed in a folder configured for application management. It doesn't support applications in a [host project or a single-project boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).

### Required roles

Using the Cost Explorer requires different permissions depending on whether you are viewing by project or by application.

#### View by project

To get the permissions that you need to view cost and utilization data for a project, ask your administrator to grant you the following IAM roles on the project: 

  * Enable APIs: [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) 
  * View utilization data: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 
  * View costs: Cloud Hub Operator (`roles/cloudhub.operator`) or a custom role with the `billing.resourceCosts.get` permission 



If your administrator already granted you the [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`) role, then the Monitoring Viewer permissions are included in that role.

#### View by application

To get the permissions that you need to view cost and utilization data for an application, ask your administrator to grant you the following IAM roles on the management project for a folder: 

  * View utilization data: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 
  * View data for applications: [App Hub Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.viewer) (`roles/apphub.viewer`) 
  * View data in a folder: [Folder Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderViewer) (`roles/resourcemanager.folderViewer`) 



## View the Cost Explorer

To view the Cost Explorer, do the following:

  1. In the Google Cloud console, go to the **Cost Explorer** page: 

[Go to **Cost Explorer**](https://console.cloud.google.com/monitoring/cost-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**. 

  2. Select the project or application that you want to view:

     * To view data for a project, select a project from the project picker at the top of the page.

     * To view data for an application, in the toolbar of the Google Cloud console, select the management project for a folder. Then, go to the toolbar of the Cost Explorer, and set the view to **Application**. If you don't know which project to select, ask your administrator.

**Note:** When you select a project to view in the Cost Explorer, cost values are only for resource usage in that project. When you select an application, cost values are only for resources that are fully used by the selected application.



You can also view cost and utilization data from the **Optimization** page in Cloud Hub. The [**Optimization** page](https://docs.cloud.google.com/hub/docs/optimize) displays an overview of the data you see in the Cost Explorer, letting you identify trends at a glance. You can see total cost trends for your selected project or application, the top 5 resources by cost change, and the 5 most underutilized resources. In the **Resources by cost and utilization** section, you can further explore your cost and utilization data by clicking **View details in Cost Explorer**.

## Explore your costs and utilization

The Cost Explorer lets you view only cost data, or cost data in tandem with utilization metrics.

You can filter the data presented by adjusting the time-range selector, where you can select **1 day** , **7 days** , **14 days** , or **30 days**.

Google Cloud products report usage and cost data to Cloud Billing processes at varying intervals. As a result, you might see a delay between your use of Google Cloud services and the usage and costs being available to view in the Cost Explorer. Typically, your costs are available within a day, but can sometimes take more than 24 hours.

### Analyze by cost

The **Cost summary for selected scope** section of the Cost Explorer displays data about the total cost, total cost change, and total cost change by resource.

The total cost is based on usage in the selected project or application based on your contract prices, before any [committed-use discounts (CUDs)](https://docs.cloud.google.com/docs/cuds) or other credits are applied. For an application, the total cost includes all resources that are fully used by the application and excludes resources shared across applications.

The total cost table breaks down costs for supported products and resources.

  * Network data transfer costs and Cloud Load Balancing data processing fees are shown separately from resource costs.
  * Costs for local storage using Persistent Disk are shown under the product Persistent Disk.



Unsupported products are classified as **Other** in the **Product** column and unsupported resources are classified as **Other** in the **Resource Type** column.

For more information about cost and utilization data in the Cost Explorer, see [About cost and utilization data](https://docs.cloud.google.com/stackdriver/docs/costs/optimization-data).

### Analyze by cost and utilization

For supported Google Cloud products, you can further explore costs in relation to resources in the **Explore analyzed resources** section.

This section lets you select a metric that aggregates cost and utilization, presenting a treemap that organizes cost by size, and utilization by color. For example, this section might be helpful in identifying resources that cost the most, while also having low CPU utilization in the last 30 days.

If you select the **Aggregated cost, cost change** metric, the **Resource list** table includes additional information.

## What's next

  * Use the [App Optimize API](https://docs.cloud.google.com/app-optimize/overview) to get cost and utilization data programmatically and integrate the data into your daily workflows.
  * Explore opportunities for cost savings and optimization in [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub).
  * Perform in-depth cost analysis with [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports).
  * Learn cost optimization best practices in the document [Google Cloud Architecture Framework: Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
