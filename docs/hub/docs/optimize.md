---
url: https://docs.cloud.google.com/hub/docs/optimize/
title: View resource costs and utilization \u00a0|\u00a0 Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:26.088974+00:00
---

# View resource costs and utilization  |  Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/optimize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)



Send feedback 

#  View resource costs and utilization Stay organized with collections  Save and categorize content based on your preferences. 

The Optimization page lets you view summary cost data, resource utilization metrics, and recommendations for Google Cloud services. Reviewing this data helps you optimize spending across your projects and [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) applications.

This document is for developers and platform administrators. If you manage billing accounts or budgets in Cloud Billing, see the [Cloud Billing cost optimization documentation](https://docs.cloud.google.com/billing/docs/how-to/finops-hub) for information about using FinOps Hub and Gemini Cloud Assist in Cloud Billing.

To learn about using Gemini for Google Cloud to help with cost optimization, see [Optimize costs with Gemini assistance](https://docs.cloud.google.com/hub/docs/optimize-gemini).

## Before you begin

[Set up Cloud Hub](https://docs.cloud.google.com/hub/docs/setup-cloud-hub).

**Note:** Cloud Hub only supports applications in a folder configured for application management. It doesn't support applications in a [host project or a single-project boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).

### Required roles

The Cloud Hub Operator role contains most of the required permissions to view data on the Optimization page, including permissions to view Monitoring data, App Hub application data, and Active Assist recommendations.

To get the permissions that you need to view data in Cloud Hub, ask your administrator to grant you the following IAM roles on the project or management project (for [app-enabled folders](https://docs.cloud.google.com/hub/docs/app-project-views#app-view)): 

  * View most data in Cloud Hub: [Cloud Hub Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Making changes based on your analysis of costs, such as applying a recommendation from Active Assist or changing the billing option for Cloud Run, requires additional permissions or coordination with a member of your organization who has the required permissions.

## View costs and utilization

The Optimization page displays the following information:

  * The total cost and cost trend for a selected project or application.
  * The top five resources or application workloads with the highest cost along with their cost change.
  * The five most expensive resources or workloads with the lowest utilization.



When you view data for a selected project or application, you can filter the page to display specific products.

To view costs and utilization:

  1. In the Google Cloud console, go to the **Optimization** page:

[Go to Optimization](https://console.cloud.google.com/cloud-hub/optimization)

  2. Select the [project or application](https://docs.cloud.google.com/hub/docs/app-project-views) that you want to view:

     * To view data for applications, choose the folder that is configured for application management. Folders configured for application management have a special icon (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)). The management project for the folder also has a special icon (![ ](https://docs.cloud.google.com/static/hub/images/mgmt-project.png)) and the project name is in the format `FOLDER-NAME-mp`. If you choose the management project instead of the folder, then the project picker automatically changes the selection to the folder.

     * To view data for an individual project, choose the project that contains the resources you want to view.

  3. To filter data for a specific product, location, or historical time range, select an option from the **Product** , **Location** , or time range filters. You can view up to 30 days of data.

The Optimization page shows the following information:

     * **Cost trend** : Total costs for the selected filters.

![ ](https://docs.cloud.google.com/static/hub/images/cho-cost-summary-project.svg)**Figure 1** : Cost summary for a project![ ](https://docs.cloud.google.com/static/hub/images/cho-cost-summary-app.svg)**Figure 2** : Cost summary for an application
       * **Total gross cost** : displays the total cost of usage for the selected filters.
       * **Cost change** : displays the change in gross cost. The change is calculated based on the time period you selected. For example, if you select **7 days** and the current date is April 30, 2025, the change percentage is a comparison between data from April 23 to April 29 and data from April 16 to April 22. The start of the billing day is at midnight in the US and Canadian Pacific Standard Time (UTC-8) time zone when Pacific Standard Time is in effect. When Pacific Daylight Time is in effect, the start of the billing day is at midnight in the US and Canadian Pacific Daylight Time (UTC-7) time zone.
     * **Cost and utilization** : This section lists top resources to consider for further investigation.

       * Costs for Persistent Disk and network data transfers are aggregated separately from resource costs.
       * Costs associated with products that aren't supported are classified as **Other**.

**For a project** : displays the top five resources with the highest cost and cost change and the top five resources with high cost and lowest utilization. Resources for a product that aren't supported are classified as **Other**.

![ ](https://docs.cloud.google.com/static/hub/images/cho-utilization-project.svg)**Figure 3** : Cost summary for a project
       * To further explore costs, click a specific resource name to view details for that resource.
       * To view more detailed cost information, click **View details in Cost Explorer**. The view in Cost Explorer is filtered to show the same project, product, location, and time range as the Optimization page.

**For an application** : displays the top five workloads and services with the highest cost and cost change and the top five workloads and services with high cost and lowest utilization.

![ ](https://docs.cloud.google.com/static/hub/images/cho-utilization-app.svg)**Figure 4** : Cost summary for an application
       * To further explore costs, click a specific workload or service name to view details for that workload or service.
     * **Top talkers** : [(Preview)](https://cloud.google.com/products#product-launch-stages) This section lists resources with the highest data transfer costs, including Cloud Load Balancing data processing fees.




For more information about displayed cost and utilization data, supported resource-level costs, and limitations, see [About cost and utilization data](https://docs.cloud.google.com/hub/docs/optimization-data).

To view more detailed cost information, click **View details in Cost Explorer** in the appropriate section. For more information about using Cost Explorer, see [Optimize costs with Cost Explorer](https://docs.cloud.google.com/stackdriver/docs/costs/optimize-costs).

Since utilization is only one aspect of cost for Google Cloud services, we recommend that you use data on the Optimization page in the context of other cost-optimization features and best practices that are available for the services you use. For example, Compute Engine, Google Kubernetes Engine (GKE), and Cloud Run provide [committed use discounts](https://docs.cloud.google.com/docs/cuds). Cloud Run also lets you choose from different [billing options](https://docs.cloud.google.com/run/docs/configuring/billing-settings) based on how you use your instances.

## View recommendations

Active Assist generates recommendations and insights to help you optimize your Google Cloud resources. The Optimization page in Cloud Hub displays the top 5 cost optimization recommendations for the selected project or application.

For information about cost recommenders and how they work, see the [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders) page. The Optimization page displays cost recommendations from all cost recommenders except for the [committed use discounts recommender](https://docs.cloud.google.com/docs/cuds-recommender).

To view recommendations:

  1. In the Google Cloud console, go to the **Optimization** page:

[Go to Optimization](https://console.cloud.google.com/cloud-hub/optimization)

  2. Select the [project or application](https://docs.cloud.google.com/hub/docs/app-project-views) that you want to view:

     * To view data for applications, choose the folder that is configured for application management. Folders configured for application management have a special icon (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)). The management project for the folder also has a special icon (![ ](https://docs.cloud.google.com/static/hub/images/mgmt-project.png)) and the project name is in the format `FOLDER-NAME-mp`. If you choose the management project instead of the folder, then the project picker automatically changes the selection to the folder.

     * To view data for an individual project, choose the project that contains the resources you want to view.

The **Top 5 optimization recommendations** table displays the following information:

     * **Resource** (for projects) or **Workload** (for applications) - The resource or workload that the recommendation applies to.
     * **Cost** \- The cost for the selected time period in the filter bar. The default is 7 days. Consider choosing 30 days as the time period so that it's easier to compare costs with the **Monthly savings** column.
     * **Monthly savings** : The highest amount of money you can potentially save if you apply the cost savings recommendations. 
       * Cost savings are an estimate that is calculated using data from the last month, regardless of the time period selected in the filter bar.
       * Cost savings are based on your contract prices, before any committed use discounts or other credits are applied.
       * Actual cost savings can vary.
  3. To view additional recommendations, click **View all recommendations in Active Assist Recommendations**.

     * If a project is selected in the project picker, Active Assist displays all recommendations for the project.
     * Active Assist does not support displaying data for a folder or an App Hub application. If you know which project contains the resource that you are interested in optimizing, select the project from the project picker.



## What's next

  * [Optimize costs with Gemini assistance](https://docs.cloud.google.com/hub/docs/optimize-gemini).
  * Use the [App Optimize API](https://docs.cloud.google.com/app-optimize/overview) to get cost and utilization data programmatically and integrate the data into your daily workflows.
  * Explore opportunities for cost savings and optimization in [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub).
  * Perform in-depth cost analysis with [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports).
  * Learn cost optimization best practices in the document [Google Cloud Architecture Framework: Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
