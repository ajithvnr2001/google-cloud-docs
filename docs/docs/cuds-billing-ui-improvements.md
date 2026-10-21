---
url: https://docs.cloud.google.com/docs/cuds-billing-ui-improvements/
title: Billing user interface improvements \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:29.103714+00:00
---

# Billing user interface improvements  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/cuds-billing-ui-improvements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Resources ](https://docs.cloud.google.com/billing/docs/resources)



Send feedback 

#  Billing user interface improvements Stay organized with collections  Save and categorize content based on your preferences. 

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrate to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

In the Google Cloud console, the Cloud Billing user interface has the following updates to support the CUDs program:

  * **Cost breakdown report** : The Cost breakdown chart now visually represents the net impact of your spend-based CUDs discount, showing savings in green or any underutilized commitment waste in orange.
  * **Savings filter** : In **Reports** and the **Cost table** report, the **Credits** filter is now named **Savings** and has been restructured with clearer subcategories for easier analysis. The Cost table report incorporates additional columns reflecting these distinct savings categories.
  * **[Improved CUD analysis tool](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds)** : A new and improved analysis page for CUDs is available, offering more powerful filtering, data aggregation, and utilization tracking. For the spend-based CUD model, the analysis tool now provides insights into utilization patterns visualized as equivalent on-demand spend (for savings and usage analysis). The new tool offers new filters by multiple dimensions and aggregates machine commitments. It also has a new graph to track utilization percentages over time.
  * **Committed use discounts (CUDs) display names** : All spend-based CUDs now follow a consistent `[Product] CUD` naming pattern in the Committed use discounts (CUDs) for better clarity.
  * **Budgets** : Budgets track your net cost after savings are applied. You must review your existing budget alert thresholds, as your tracked costs might be lower, depending on the filters that you have configured. The total costs tracked by these budgets can decrease as the uncredited costs now include savings when the new model applies.
  * **Pricing table** : The pricing table has new fields to support [consumption models](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro).
  * **CUD metadata exports to BigQuery** : Added new billing data exports for pricing and CUD metadata to BigQuery.



## View your savings

On the Billing account **Overview** page, the Savings calculation includes all eligible discounts and credits. The _View details_ link now takes you to the **Cost breakdown** report, shown in the following image.

![Example of the billing account overview page](https://docs.cloud.google.com/static/docs/images/cuds-savings.png)

For more information, see [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).

### Filter your savings

In **Reports** , the **Credits** filter is now named **Savings** , and the subcategories have been restructured as _Savings programs_ and _Other savings_ for easier analysis. The filters let you see your costs before and after various discounts are applied. By toggling these options, you can analyze how much money you are saving with each type of discount, shown in the following image.

![Example of the savings filter in cost Reports](https://docs.cloud.google.com/static/docs/images/cuds-savings-filter.png)

In Reports, the **Savings** filter displays only the specific credit types that you incurred in your Google Cloud costs. If a particular type of credit doesn't apply to your Cloud Billing account, you won't see that credit option in the list.

The _Savings programs_ subcategory includes the Committed Use Discount (CUD) options:

  * **Spend-based CUD discounts** : Discounts earned with the spend-based pricing model, showing you the cost savings you have from your commitments.
  * **Legacy spend-based CUD credits** : Spend-based committed use discounts (CUDs) credits for SKUs that are not part of the spend-based pricing model, or for CUDs credits earned before the spend-based pricing model went into effect.
  * **Resource-based CUD credits** : Credits on Compute Engine resource costs when you commit to using eligible resources during a specified term.



The _Other savings_ subcategory includes Free tier credits, Promotional credits, and other discounts and credits such as the following:

  * **Sustained Use Discounts (SUDs)** : Discounts automatically earned when you run eligible Compute Engine resources throughout the billing month.
  * **Spending-based discounts** : Discounts applied after a contractual spending threshold is reached, typically earning progressively larger discounts based on your total spend over a defined period.
  * **Subscription credits** These credits are typically applied to Base + Overage subscriptions, also known as Non-Unified Commitment Service (Non-UCS) subscriptions.



See Cloud Billing Reports to [learn more about savings](https://docs.cloud.google.com/billing/docs/how-to/reports#credits).

## New columns and filters in the Cost table report

In the Cost table report, new columns and filters show you how the consumption model affects your costs and let you filter the savings data for more flexibility, shown in the following image.

![View of the savings filter](https://docs.cloud.google.com/static/docs/images/cuds-consumption-model-filters.png)

## Use labels and group data in the Cost table report

In the Cost table report, you can use the **Table configuration** settings to organize, aggregate, and add business context to your tabular view of your costs for a given invoice or statement. These settings let you select a label to categorize your data, use labels as a grouping dimension, and select a grouping option, shown in the following image.

![Table configuration settings in the cost
 table report.](https://docs.cloud.google.com/static/docs/images/cuds-label-and-group-data.png)

The table configuration dialog has the following options:

  * **Label data** : This lets you select one of your custom label keys. It adds a new column to the table, showing the specific label value for each cost item. This is the best way to overlay your own business context (like teams, environments, or cost centers) onto your report.
  * **Group by** : The grouping options control how the rows in the table are aggregated and nested. You can view a flat list, or you can create a hierarchical, nested view of your costs. The Group by options include:

    * **No grouping** : Shows each cost item as a separate, individual row.
    * **Project > Service > SKU > Consumption model**: Creates a nested hierarchy starting with the project at the highest level, allowing you to see costs roll up from the most granular level (the consumption model) to the highest level.
    * **Service > SKU > Consumption model**: Creates a nested hierarchy starting with the service at the highest level.
    * **Custom grouping** : Select grouping dimensions to break out totals of the different types of savings or credits that apply.



[Learn more about the Cost table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table).

## Analyze your savings with the Cost Breakdown report

For the report date range, the Cost breakdown report shows your base usage cost and how that cost is affected by any credits, adjustments, and taxes, to arrive at your total cost. The waterfall chart displays charges in orange, savings in green, and subtotals and totals in blue. For services covered by the new spend-based CUDs, the _Spend-based CUD discounts_ bar shows the net impact of your spend-based commitments, shown in the following image.

![The cost breakdown report.](https://docs.cloud.google.com/static/docs/images/cuds-cost-breakdown.png)

The Cost breakdown report includes a savings bar for each _applicable_ type of credit. If a particular type of credit doesn't apply to your Cloud Billing account, you won't see that savings type in the chart. In the example image, the Cost breakdown chart and table are showing the following items:

  * **Usage cost** : This is the starting point—the gross cost of all services you used during the time period, before any discounts or credits are applied.
  * **Negotiated savings** : This green bar represents a credit for any special pricing or custom discounts negotiated in your contract.
  * **Spend-based CUD discounts** : This shows the net impact of your spend-based commitments. It appears as a green credit bar representing your savings, but can appear as an orange charge bar in the rare case of underutilized commitments (waste).
  * **Sustained use discounts (SUDs)** : This credit represents the automatic savings you receive for running eligible resources for a significant portion of the month, with no commitment required.
  * **Spending-based discounts** : This credit is for any automatic volume-based discounts you receive for high usage of certain services.
  * **Subtotal / Total** : The final blue bars show your subtotal after all credits are applied, and the final total represents the net costs after taxes are added.



[Learn more about the Cost breakdown report](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).

## Review your budgets after cost-saving updates

With recent updates to how spend-based CUDs cost savings are calculated, the total costs tracked by your budgets might now be lower. Commitment savings are more consistently included in the budget's calculation, giving you a more accurate view of your actual net spend.

Due to this change, you should ask the following questions:

  * Should I lower my budget alert thresholds to avoid missing important spending changes?
  * Which of my existing budgets are affected and need review?
  * How can I create a new budget that accurately reflects my net costs?



We recommend that you visit your budgets dashboard to review any existing budgets. Since they now track a lower total cost that includes commitment savings, your original alert thresholds might be too high and might not trigger when expected. Adjusting your thresholds downward ensures you continue to receive timely spending alerts based on your actual costs.

When creating or reviewing a budget, the **Savings** scope is the key section to understand, shown in the following image.

  * This section controls which credits and discounts are subtracted from your gross costs to determine the final "total cost" that your budget tracks.
  * Because your budget tracks the cost _after_ these savings are applied, the tracked amount is your net cost. This is why your total tracked cost might be lower than it was previously, requiring you to review and potentially lower your alert thresholds to match this more accurate, post-savings number.



[Learn more about managing budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets).

![The savings options in the budget scope.](https://docs.cloud.google.com/static/docs/images/cuds-create-budget.png)

## Committed use discounts (CUDs) display names

To simplify how commitments are displayed, all spend-based CUDs use a consistent naming convention. This helps you identify which product a specific commitment applies to directly from the list view.

The display names for all CUD offerings in the spend-based model use the following naming pattern:

  * **Naming Pattern** : `[Product] CUD` \- The name of the product is listed first, followed by "CUD".
  * **Examples shown in the screenshot** : 
    * `AlloyDB for PostgreSQL CUD`
    * `Cloud Run CUD`
    * `Compute Flexible CUD`
    * `Kubernetes Engine CUD`



## Pricing table fields for consumption models

The Pricing page provides a comprehensive list of all available SKUs and their associated prices for your account. There are new fields in this view, for example **Consumption model description** , shown in the following image.

![The pricing view for a project with negotiated pricing.](https://docs.cloud.google.com/static/docs/images/cuds-pricing-field-tables.png)

By using the column chooser on the right side of the table, you have granular control over your pricing report. This lets you create a view tailored to your specific needs, whether that's a high-level overview focusing on product names or a detailed deep-dive that includes specific IDs and taxonomy.

You can choose the data points to show, for example:

  * **Identifiers** : `SKU ID` for technical analysis.
  * **Descriptions** : `SKU description` and `Consumption model description` for better readability.
  * **Classification** : `Product taxonomy` to understand how a SKU is categorized within the Google Cloud ecosystem.
  * **Pricing Details** : `Price reason` to understand why a certain price is being applied (e.g., `DEFAULT_PRICE`).



## Pricing and CUD metadata exports to BigQuery

For customizable analysis of your pricing and savings, enable Billing data exports to BigQuery:

  * **Pricing** (updated): This export contains all of your account's SKUs and their prices. You can join this data with the detailed usage export to perform custom pricing calculations or analysis. [Learn more](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data)
  * **Committed Use Discounts Export** (new): This export provides all the metadata related to your _spend-based_ CUDs. It lets you analyze your commitment portfolio, track utilization over time, and identify opportunities for optimization beyond what is available in the standard console reports. [Learn more](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export)



In addition, there are new fields added to the **Pricing data export**. For more information, see [Price export changes](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel#price-export-changes).

## Related topics

  * [Spend-based CUD program improvements](https://docs.cloud.google.com/docs/cuds-multiprice)
  * [Spend-based CUD data model changes](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel)
  * [Verify your discounts after migration](https://docs.cloud.google.com/docs/cuds-verify-discounts)
  * [Choose the correct amount of CUD to buy](https://docs.cloud.google.com/docs/cuds-choose-correctly)
  * [Sample queries for the CUDs data model](https://docs.cloud.google.com/docs/cuds-example-queries)
  * [Migrated CUD SKUs, offers, and consumption model IDs](https://docs.cloud.google.com/docs/cuds-migration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
