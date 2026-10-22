---
url: https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker/
title: Track the status of your conditional incentives \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:44.516908+00:00
---

# Track the status of your conditional incentives  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Track the status of your conditional incentives Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the Incentives page, where you can track the status of your spend-based milestone and incremental workload credit programs, and the Rapid Migration and Modernization Program (RaMP) incentives. These are all promotional credits that you might earn as part of a custom Google Cloud pricing contract.

## Overview of incentives tracking

The **Incentives** program tracking page serves as the single source of truth for understanding and monitoring the conditional incentives built into your Google Cloud contracts.

Conditional incentives require you to meet specific spend or usage milestones within a defined timeframe to unlock rewards. These rewards can be:

  * **Spend-based credits** : Credit amounts issued to your account after meeting spend thresholds. Examples of spend-based milestone programs include the following:

    * A program that gives you 25% in credit for every dollar you spend, after you reach the milestone of spending $100 on BigQuery in a month.

    * A program that gives you $30 in credit every time you spend $200 on Compute Engine resources.

  * **Rapid Migration and Modernization Program (RaMP)** : View and track credits related to your [RaMP agreement](https://cloud.google.com/solutions/cloud-migration-program).

    * [RaMP tracking and incentive guide](https://docs.cloud.google.com/migration-center/docs/ramp-user-guide). Learn more about the steps and rules for RaMP incentive qualification, reward calculation, and incentive usage.

    * [RaMP workload tagging guide](https://docs.cloud.google.com/migration-center/docs/ramp-workload-tagging). To unlock your outcome-based incentives, map your workloads to the RaMP program through "tagging" to track your actual consumption.




For information on custom Google Cloud contracts, [contact Google Cloud sales](https://cloud.google.com/contact/), or your Google Cloud Technical Account Manager.

The incentive programs that you achieve act as a payment method, and are automatically applied to your costs. Credits are typically applied to your Cloud Billing account within 45 days of achieving the applicable RaMP or spend-based milestone, or for monthly milestones, on a rolling monthly basis (typically within 45 days of month-end).

In reports and Cloud Billing data export to BigQuery, the incentive program credits that you earn appear as `PROMOTION` type credits.

## Permissions required to access the Incentives page

To access the **Incentives** page for your Cloud Billing account, you need a role on your Cloud Billing account that includes the following [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing):

  * `billing.credits.list`



To gain this permissions using a [predefined role](https://docs.cloud.google.com/iam/docs/roles-overview#predefined), you need to be assigned to one of the following [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access) roles on your Cloud Billing account:

  * [Billing Account User](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.user)
  * [Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.viewer)
  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)



For more information about billing permissions, see:

  * [Overview of access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)



## Access the Incentives page in the Google Cloud console

If you have a contract that includes RaMP incentives or spend-based milestone credits, access the Incentives page to view a summary of each program and the status of the credit milestones associated with each program.

  1. In the Google Cloud console, go to your Cloud Billing account.

[Go to your Cloud Billing account](https://console.cloud.google.com/billing/overview)

  2. At the prompt, **choose the Cloud Billing account** for which you'd like to view the Incentives page.

The Billing Overview page opens.

  3. From the **Billing navigation menu** , click **Incentives**.




## Navigate the Incentives dashboard

The Incentives program tracker dashboard is designed to give you both a high-level summary and a detailed tabular view of your active and historical incentive programs.

**Note:** The incentives program tracker doesn't update in real time. There might be a delay of up to three days before the tracker reflects your spend.

### Summary scorecard

![Example of the Incentives page, showing the summary scorecard and the
   milestone status panel.](https://docs.cloud.google.com/static/billing/docs/images/incentives-iwc-all-status.png)Example of the Incentives page, showing the summary scorecard and the milestone status panel. Click image to view an enlarged version. 

![](https://docs.cloud.google.com/static/billing/docs/images/incentives-iwc-all-status.png)

At the top of the page, the Summary Scorecard displays key aggregate metrics for your active programs, such as active milestone counts and progress.

### Program tracker table and statuses

The Program tracker table lists your incentive programs, showing the program name, milestone index, milestone end date, spend target, progress, and reward.

Select a program to view its details in the milestone status panel. The milestone status panel uses visual indicators to show the status of each milestone in the program:

  * cached **Active** : The milestone is open for earning.
  * check_circle_outline **Achieved** : The conditions to earn the reward have been met.
  * arrow_forward **Upcoming** : The milestone period hasn't started yet.
  * error_outline **Missed** : The milestone period ended without meeting the conditions to earn the reward.
  * cached **X/Y achieved** : For multi-tier programs, indicates progress (for example, "1/2 achieved" means 1 of 2 milestones achieved).



## Program types and milestone details

On the Incentives page, you can view the conditions, scope, targets, progress, and issued rewards for all of your RaMP and spend-based milestone credit programs (including incremental workloads) on one page.

Program types include the following:

  * **Conditional credits** : Programs that consist of a single condition that unlocks a single reward.
  * **Incremental Workload Credits (IWC)** : Programs that track your spend incrementally over time, typically with multiple milestones.
  * **Rapid Migration and Modernization Program (RaMP) incentives** : RaMP workloads that are [tagged and qualify for RaMP incentives](https://docs.cloud.google.com/migration-center/docs/ramp-workload-tagging).



### View the details of a current program milestone

  1. In the **Program tracker** table, select a program to view its details in the milestone status panel.

  2. Select the **Current milestone** tab to view the details of the current milestone in the selected program.


Conditional spend-based milestone program | Incremental Workload Credits (IWC) program  
---|---  
![Example of a conditional spend-based milestone credit program, showing the
       program name, and details about the reward.](https://docs.cloud.google.com/static/billing/docs/images/incentives-spend-milestone-credit.png)Shows the details in the milestone status panel for a conditional credit program with a single milestone. Click image to view an enlarged version. ![](https://docs.cloud.google.com/static/billing/docs/images/incentives-spend-milestone-credit.png) |  ![Example of an Incremental Workload Credits \(IWC\) program, showing the
     program name, and details about the reward.](https://docs.cloud.google.com/static/billing/docs/images/incentives-iwc-current.png)Shows the details in the milestone status panel for the current milestone in an active IWC program. Click image to view an enlarged version. ![](https://docs.cloud.google.com/static/billing/docs/images/incentives-iwc-current.png)  
  
### View all milestones in a program, including program history

![Milestone status panel for all milestones in an IWC program,
     including past, current, and future milestones.](https://docs.cloud.google.com/static/billing/docs/images/incentives-iwc-all.png)Shows the details in the milestone status panel for all milestones in an IWC program, including past, current, and future milestones. Click image to view an enlarged version. 

![](https://docs.cloud.google.com/static/billing/docs/images/incentives-iwc-all.png)

  1. In the **Program tracker** table, select a program to view its details in the milestone status panel.

  2. Select the **All milestones** tab to view a list of milestones in the selected program.

  3. To view the history of a milestone, expand the milestone to see past achievements and rewards earned.




## Analyze your costs and credits in reports

When you earn incentive rewards, they are applied as `PROMOTION` type credits, and are automatically applied to your eligible costs. You can use the cost table report or the Cloud Billing export to BigQuery to analyze your usage costs, and see the detailed breakdown of how your incentive program credits are applied to reduce your costs.

**Note:** Credits are typically applied to your Cloud Billing account within 45 days of achieving the applicable RaMP or spend-based milestone, or for monthly milestones, on a rolling monthly basis (typically within 45 days of month-end).

### View credits for a specific invoice in the cost table report

The cost table report helps you reconcile the costs and credits on a specific invoice or statement. To view your incentive program credits in the cost table, use the following configuration:

  1. Open the cost table in the Google Cloud console.

[Go to Cost table](https://console.cloud.google.com/billing/reports/tabular)

  2. Click **Table configuration** , and from the **Group by** menu, select **No grouping**.

  3. Click view_column **Column display options** , and enable the **Credit type** , **Credit name** , and **Credit ID** columns.

  4. In the **Filters** section, select the following options:

     * Select an **Invoice month**.
     * Optionally, if you know the services that your credits are applied to, select them from the **Services** menu.
     * Under **Savings** , in the **Other savings** section, select **Promotional credits** , and clear all of the other **Savings** options.
  5. In the cost table, click the **Credit type** column header to sort the rows by the type of credit.

Your incentive program credits are shown with the credit type `PROMOTION`, broken down by each SKU they apply to. Use the **Credit name** column to identify the credits that are part of the same milestone.

**Tip:** Use the **Rows per page** setting at the bottom of the cost table to view more rows.
  6. To download your report as a comma-separated value (CSV) file, click get_app **Download to CSV**.




[Learn more about using the cost table report to analyze your costs](https://docs.cloud.google.com/billing/docs/how-to/cost-table).

### View credits in the billing export to BigQuery

You can use the Cloud Billing export to BigQuery to export detailed billing data to a BigQuery dataset, and use the data for detailed analysis of your costs.

In your exported data, the name of the credit is in the `credits.full_name` column. The following queries show examples of data that you can get about credits from your BigQuery export.

#### Example: get all promotional credits for usage before a specific date

This example gets all the line items for credits that were applied before March 1, 2024:
    
    
    SELECT
    c.full_name AS CreditName, c.type AS CreditType,
     usage_start_time AS UsageStart, cost AS Cost
    FROM `project_name.dataset_name.gcp_billing_export_resource_v1_XXXXXX_XXXXXX_XXXXXX`,
     UNNEST(credits) AS c
    WHERE
     c.type = "PROMOTION"
    AND
     DATE(TIMESTAMP_TRUNC(usage_start_time, DAY, 'US/Pacific')) < '2024-03-01';
    

#### Example: get information about specific promotional credits

This example uses the name of the credit to get all the usage that the credit was applied to.
    
    
    SELECT
    c.full_name AS CreditName, c.type AS CreditType,
     usage_start_time AS UsageStart, cost AS Cost
    FROM `project_name.dataset_name.gcp_billing_export_resource_v1_XXXXXX_XXXXXX_XXXXXX`,
     UNNEST(credits) AS c
    WHERE
     c.full_name LIKE "%example%";
    

[Learn more about the Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

## Frequently Asked Questions (FAQ)

  * Why was the "Spend-based Milestones" page replaced?
  * How often is the progress data updated?
  * What is the difference between "Earn Scope" and "Reward Scope"?



Why was the "Spend-based Milestones" page replaced?
    

The new "Incentives program tracker" page expands support to cover both spend-based milestones and RaMP in a unified view, improving clarity and auditability of your contract benefits.

Back to FAQ

How often is the progress data updated?
    

Progress calculations are refreshed daily, but can be delayed up to three days based on the latest cost data. This delay means that the data might lag spend reflected on cost reports and BigQuery exports.

Back to FAQ

What is the difference between "Earn Scope" and "Reward Scope"?
    

  * **Earn Scope** : Defines the spend and accounts that count towards meeting the milestone.
  * **Reward Scope** : Defines _where_ the credit is applied after the milestone is earned.



Back to FAQ

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
