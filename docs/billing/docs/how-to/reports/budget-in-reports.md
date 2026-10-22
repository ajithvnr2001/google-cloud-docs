---
url: https://docs.cloud.google.com/billing/docs/how-to/reports/budget-in-reports/
title: Billing reports: View a budget in your report \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:44.888805+00:00
---

# Billing reports: View a budget in your report  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/reports/budget-in-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Billing reports: View a budget in your report Stay organized with collections  Save and categorize content based on your preferences. 

In Cloud Billing cost reports, when you open the report from an existing budget, the report's filters are configured based on the scope of the budget, and you can view the budget's amount in your report. The budget's target amount appears in the report chart as a red, dashed, horizontal line, helping you to visualize the budget while you're analyzing the specific costs that are tracked by the budget.

You have these options to view a budget amount in a report:

  * View the cost report for the current month, with report filters matching your budget scope.
  * View the cost report for the previous 12 months, with report filters matching your budget scope.

View a budget in your cost report showing costs for the _current month_  
---  
To view a budget in your cost report for the current month, take the following steps:

  1. Go to the [ Budgets and alerts list page](https://docs.cloud.google.com/billing/docs/how-to/budgets#view-budgets).
  2. To navigate to a cost report that's configured using the budget's scope settings, click the **Spend and budget amount** progress bar for the budget you want to analyze.

|  ![Example of the budget list page, showing several budgets and pointing
         to a progress bar in the Spend and budget amount column.](https://docs.cloud.google.com/static/billing/docs/images/budget-list-link-to-reports.png)Example of the budget list page. Click image to view an enlarged version. ![](https://docs.cloud.google.com/static/billing/docs/images/budget-list-link-to-reports.png)  
The cost report opens with the following settings:

  * The [ **Time range**](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range) option is set as **Usage date** , setting a custom range for the current month.
  * The [ **Time aggregation**](https://docs.cloud.google.com/billing/docs/how-to/reports#time_aggregation) setting in the report chart is set to **Daily cumulative**.
  * The [ **Chart style**](https://docs.cloud.google.com/billing/docs/how-to/reports#bar-chart) is set to **bar chart**.
  * The [ **Group by**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) option defaults to **Service**.
  * The rest of the [ **report filters**](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) are configured using the [ budget's scope settings](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope), such as Projects, Services, Labels, and Credit selections.
  * A **Budget amount** line appears in the report chart, representing the target spend amount of the budget.

|  ![Example of a cost report opened from a budget. The report displays a
         budget amount line on the report chart.](https://docs.cloud.google.com/static/billing/docs/images/report-with-budget-line-current-month.png)Example of a cost report opened from a budget. Click image to view an enlarged version. ![](https://docs.cloud.google.com/static/billing/docs/images/report-with-budget-line-current-month.png)  
View a budget in your cost report showing costs for the _previous 12 months_  
---  
To view a budget in your cost report for the previous 12 months, take the following steps:

  1. Go to the [ Budgets and alerts list page](https://docs.cloud.google.com/billing/docs/how-to/budgets#view-budgets).
  2. Access the [ **budget scope**](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope) by [ opening an existing budget](https://docs.cloud.google.com/billing/docs/how-to/budgets#edit-or-delete-budget).
  3. In the [ budget's cost trend chart](https://docs.cloud.google.com/billing/docs/how-to/budgets#cost-trend-chart), click the  arrow_forward**View report** link to navigate to a cost report that's configured using the budget's scope settings.

|  ![Example of a budget's cost trend chart, viewable when creating or
         editing a budget, showing the link to navigate to the cost report
         page.](https://docs.cloud.google.com/static/billing/docs/images/budget-cost-trend-chart-link-to-reports.png)Example of a budget's cost trend chart. Click image to view an enlarged version. ![](https://docs.cloud.google.com/static/billing/docs/images/budget-cost-trend-chart-link-to-reports.png)  
The cost report opens with the following settings:

  * The [ **Time range**](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range) option is set as **Usage date** , selecting **Custom range**. The date range is set for the previous 12 months. 
  * The [ **Time aggregation**](https://docs.cloud.google.com/billing/docs/how-to/reports#time_aggregation) setting in the report chart is set to **Monthly**.
  * The [ **Chart style**](https://docs.cloud.google.com/billing/docs/how-to/reports#bar-chart) is set to **bar chart**.
  * The [ **Group by**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) option defaults to **Service**.
  * The rest of the [ **report filters**](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) are configured using the [ budget's scope settings](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope), such as Projects, Services, Labels, and Credit selections.
  * If you're navigating to the report from an existing budget, a **Budget amount** line appears in the report chart, representing the previously saved target spend amount of the budget. If you navigate to the report while you're creating a budget, the budget amount line doesn't display in the cost report. 

|  ![Example of a cost report opened from the cost trend chart of a budget.
         The report displays a budget amount line on the report chart.](https://docs.cloud.google.com/static/billing/docs/images/report-with-budget-line-12-months.png)Example of a cost report opened from the cost trend chart of a budget. Click image to view an enlarged version. ![](https://docs.cloud.google.com/static/billing/docs/images/report-with-budget-line-12-months.png)  
  
### Analyze the report when the budget amount line is visible

The budget amount line is removed from the report if you adjust most of the report settings. However, you can adjust the following settings in the report and the budget amount line will remain visible.

  * **Group by** setting: You can switch the [Group by](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) setting to use any of the available options.
  * **Chart style** setting: You can switch the [Chart style](https://docs.cloud.google.com/billing/docs/how-to/reports#bar-chart) setting between bar chart and line chart.
  * **Savings** setting: You can select or clear the [Savings filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-credits) to change the view of your cost calculations to include or exclude credits, helping you see how credits impact the cost calculations compared to your budget target amount.



If you change any other report settings, the budget amount line is removed. These settings include the report's [time range](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range) settings, the report chart [time aggregation](https://docs.cloud.google.com/billing/docs/how-to/reports#time_aggregation) settings, and the [report filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filters), including Subaccounts, Projects, Services, SKUs, Locations, and Labels.

To restore the budget amount line, re-open the report from a budget.

### Understand the differences between budget scopes and report filters

[Budget scopes](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope) and [report filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) behave slightly differently. In each of the scopes in a budget, you can select from a list of all possible items available in a given scope. In each of the report filters, you can select from a list of items that incurred usage costs in the Cloud Billing account you're viewing. This means that the items selectable in your budget scopes might not match up exactly to the items selectable in your cost report filters.

Review the following examples for more information:

#### Projects: budget scope versus cost report filter

For the Cloud Billing account, assume the following regarding projects:

  * 20 active projects incurring costs.
  * 10 inactive projects that previously incurred costs.
  * This Cloud Billing account is also incurring charges that aren't specific to a project, such as the cost of a support plan.
  * You have billing-account-level permissions to access the Cloud Billing account.

Budget | Cost Report  
---|---  
On your budget, in your [ **Projects** scope](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope), you can select from the 20 active projects. You can't select inactive projects or select [Charges not specific to a project]. | On the cost report, your [ **Projects** filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) list includes _all_ projects for which you have incurred usage costs, both active projects and inactive projects. Your Projects filter also includes the option to select and view [Charges not specific to a project].  
On your budget, you set the **Project scope** to "All projects (20)" — where "20" indicates 20 active projects. | When you open the cost report from the budget, the value in the report's **Projects filter** displays "All projects (31)" — where "31" indicates that you have 31 projects that have incurred costs in the Cloud Billing account you're viewing, including active and inactive projects, and [Charges not specific to a project].  
When you open the cost report from the budget's cost trend chart, if your budget scope is set for all projects, and your Cloud Billing account is incurring _charges not specific to a project_ , you might notice that your costs appear higher in the cost report than in the budget's cost trend chart.  
  
#### Services: budget scope versus cost report filter

For the Cloud Billing account, assume the following regarding services:

  * There are 200 possible services or products that you could use.
  * The Cloud Billing account has incurred costs for 16 out of the 200 possible services.

Budget | Cost Report  
---|---  
On your budget, in your [ **Services** scope](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope), you can see and select from _all 200_ possible services, even if you haven't incurred any usage or costs for those services. | On the cost report, your [ **Services** filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) list includes only those services or products for which you have incurred usage costs.  
On your budget, you set the **Services scope** to "All services (200)" — where "200" indicates all possible services. | When you open the cost report from the budget, the value in the report's **Services filter** displays "All services (16)" — where "16" indicates that you only have 16 services that have incurred costs in your Cloud Billing account.   
  
## Related topic

  * [Analyze billing data with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
