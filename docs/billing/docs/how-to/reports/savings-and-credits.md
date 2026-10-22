---
url: https://docs.cloud.google.com/billing/docs/how-to/reports/savings-and-credits/
title: Billing reports: View and analyze your savings \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:16.364269+00:00
---

# Billing reports: View and analyze your savings  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/reports/savings-and-credits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Billing reports: View and analyze your savings Stay organized with collections  Save and categorize content based on your preferences. 

In [Cloud Billing Reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can use the **Savings** filters to change the view of your cost calculations. You can select all applicable savings options (default) to be included in the cost calculations, or you can clear some or all of the discounts and credit options to exclude those savings from the cost calculations.

![Illustrating the savings filter options in the reports page.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports2.png)

Usage-specific savings are listed in separate columns in the table, and impact the **Subtotal** value. There are two categories of usage-specific savings: **Savings programs** and **Other savings**.

For Cloud Billing accounts associated with a custom pricing contract, you also see a **Negotiated savings** column.

### Savings programs

Savings programs include the various committed use discounts (CUDs) options, which lower the cost of your Google Cloud usage by offering discounts and credits tied to your resource usage or spending.

  * [**Spend-based CUD discounts**](https://docs.cloud.google.com/docs/cuds-multiprice): Spend-based committed use discounts (CUDs) provide _discounted prices_ on certain Google Cloud services when you commit to spending a minimum amount during a specified term. The discounted price is determined by the [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) that applies to the SKU usage.
  * [**Legacy spend-based CUD credits**](https://docs.cloud.google.com/docs/cuds-spend-based): For spend-based committed use discounts (CUDs) that aren't part of the new pricing model, this is the credit earned in exchange for your commitment to spend a minimum amount for a service in a particular region.
  * [**Resource-based CUD credits**](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts): Resource-based committed use discounts (CUDs) provide credits on Compute Engine virtual machines (VMs) when you commit to using eligible resources during a specified term.

**Note:** If you have any savings programs connected to your Google Cloud costs, you see the corresponding checkboxes for the different types of committed use discounts that you're using. Your **Savings** filter doesn't display all of the possible savings options, only those specific to the savings types incurred in your Google Cloud costs.

#### View the details of your committed use discounts (CUDs)

[CUDs](https://docs.cloud.google.com/docs/cuds) reduce the usage costs of Compute Engine and certain other Google Cloud services. The fees and credits from your purchased commitments are applied to your _Cloud Billing account_ using attribution, which describes how they're spread across the account's projects that consumed the eligible discounts. To understand how your commitment fees and credits are applied to your Cloud Billing account and projects, see [Attribution of committed use discount fees and credits](https://docs.cloud.google.com/docs/cuds-attribution).

To comprehensively view the details of your CUDs, you should access your Cloud Billing account report using [billing-account-level permissions](https://docs.cloud.google.com/billing/docs/how-to/reports#required-permissions). If you try to analyze your CUDs while your Cloud Billing access is limited to viewing costs for one project at a time, you won't be able to view charges or credits that aren't in the project you're viewing.

#### Analyze Spend-based CUD discounts

_Spend-based CUD discounts_ provide discounted prices on [certain Google Cloud services](https://docs.cloud.google.com/docs/cuds-multiprice#affected-cuds) when you commit to spending a minimum amount during a specified term.

_Spend-based CUD discounts_ are a new CUD model that became available starting July 15, 2025. All customers who have purchased _Legacy spend-based CUD credits_ for [affected products](https://docs.cloud.google.com/docs/cuds-multiprice#affected-cuds) will be migrated to the new _Spend-based CUD discounts_ model. A notification in the **Billing Overview** page shows the date when we will begin the automatic migration from the legacy spend-based CUD model using credits, to the new spend-based CUD model using discounts.

_Spend-based CUD discounts_ use [consumption models](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro) to help track your cloud spending, promotional offers and discounts. To analyze your _Spend-based CUD discounts_ in reports, you can group by or filter by **Spend-based CUDs** in the [Billing Reports](https://docs.cloud.google.com/billing/docs/how-to/reports), or view the [Cost table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) or the [Cost breakdown report](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).

#### Analyze Resource-based CUD credits and Legacy spend-based CUD credits

When analyzing your Google Cloud costs, it's useful to understand how your purchased commitments are impacting your costs. For example, to understand your ongoing Compute Engine costs, you need to know your VM core and RAM usage costs _as well as_ the sustained use discounts and committed use discounts generated by your core and RAM usage.

_Resource-based_ and _Legacy spend-based_ CUDs consist of three components using a balance sheet format on your bill:

  1. **Commitment fee** is the discounted cost of your covered usage.
  2. **On-demand costs** are the usage costs for the resources that you consume, billed at the standard list price.
  3. **Committed use discount credits** are negative costs that offset the eligible on-demand charges covered by the commitment.



The net impact of these three components is that you receive a discount on the usage covered by your commitment. The sum of your **commitment fee (1)** and **committed use discount credits (3)** equals the savings from your CUDs. For more information, see [Understanding your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds#credits-display-change).

  * To configure the report to display the individual components that contain your CUDs, [group your costs by SKU](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-sku). The default report view (not grouped by SKU) doesn't break out the CUD components but instead includes the net of the three components.

  * To view only your ongoing commitment fees, limit the report results to the relevant commitment fee SKUs using the [SKUs filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-sku). For example, select the SKUs filter and type `Commitment [YOUR COMMITMENT TYPE]`.


**Note:** If you have a _custom pricing contract_ , you might have received _promotional_ credits that apply to your costs calculated using _list prices_. If you use these promotional credits to pay your _commitment fees_ , your report includes a service called `Invoice`, with a SKU called `Contract billing adjustment`. This SKU adjusts your promotional credits so that they apply to the costs calculated using _list prices_. To see the details of how these _promotional_ credits are applied and to which specific commitment fee SKUs, use the Cloud Billing data export to BigQuery to export your data and then query your data to see which adjustments applied to specific commitment fees. [Learn about `contract billing adjustments` in the Cloud Billing data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#credits-contracts).

Depending on the SKU for which you purchased commitments, the fees and credits are applied to your Cloud Billing account using either [proportional attribution](https://docs.cloud.google.com/docs/cuds-attribution#type-proportional) or [prioritized attribution](https://docs.cloud.google.com/docs/cuds-attribution#type-prioritized). To understand how your commitment fees and credits are attributed to your Cloud Billing account and projects, see [Attribution of committed use discounts](https://docs.cloud.google.com/docs/cuds-attribution).

### Other savings

Other savings offer additional discounts and credits on your Google Cloud usage. Other savings might be recurring or one-time use and reduce the cost of your Google Cloud usage. If applicable to your Cloud Billing account, there are various types of other savings you might earn, such as the following:

  * [**Free tier credits**](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-tier): Some services offer [free resource usage up to specified limits](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits). For these services, credits are applied to implement the free tier usage.
  * **Promotional credits** : Promotional credits are things like [spend-based milestone credits](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker), [Google Cloud Free Trial](https://docs.cloud.google.com/free/docs/free-cloud-features#free-trial), and marketing campaign credits, or other grants to use Google Cloud. Promotional credits are typically considered a form of payment. When available, promotional credits are automatically applied to reduce your total bill.

    * **Promotional credits for custom pricing contracts** : If you have a [_custom pricing contract_](https://docs.cloud.google.com/billing/docs/how-to/pricing-table) with Google Cloud, and received promotional credits that apply to costs at _list prices_ , your report includes a service called `Invoice`, with a SKU called `Contract billing adjustment`. This SKU adjusts your promotional credits so that they apply to the costs at list price. [View details about contract billing adjustments in the Cloud Billing data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#credits-contracts).

To check if your promotional credits apply at list prices, refer to the terms of your contract.

**Note:** To understand your ongoing Google Cloud costs after your [Google Cloud free trial](https://docs.cloud.google.com/free/docs/free-cloud-features#free-trial) expires, clear the **Promotional credits** checkbox.
  * [**Sustained use discounts**](https://docs.cloud.google.com/compute/docs/sustained-use-discounts): When you run eligible Compute Engine resources throughout the billing month, you automatically earn sustained use discounts (SUDs) credits.

  * **Reseller margin** : For resellers only, this is the _Reseller Program Discount_ credit you receive for selling eligible Google Cloud products.

  * **Spending-based discounts** : Spending-based discounts offer progressively larger discounts based on your total spend over a defined period, or discounts that are applied after a contractual spending threshold is reached.

  * **Subscription credits** : Long-term subscriptions to services that are purchased in exchange for discounts. These credits are typically applied to Base + Overage subscriptions, also known as Non-Unified Commitment Service (Non-UCS) subscriptions.

  * **Others** : Other credits or discounts that aren't associated with the current categories.


**Note:** Your **Savings** filter doesn't display all of the possible discounts and credit options, only those specific to the savings types incurred in your Google Cloud costs. You won't see all of the different types of Savings options in your **Savings** filter. Rather, you can see and filter on only the discounts or credits connected to your Google Cloud costs.

### Negotiated savings

**Negotiated savings** is a credit type that displays for Cloud Billing accounts that are associated with a [_custom pricing contract_](https://docs.cloud.google.com/billing/docs/how-to/pricing-table). You receive these savings from custom pricing you've negotiated with Google. The **Negotiated savings** amount represents your cost savings computed using this equation:

`Negotiated savings = Costs at Contract price - Costs at List price`

  * For usage costs incurred _before_ May 1, 2021, your _on-demand rate_ is based on your contract prices, and includes the savings you earned compared to list prices. When you configure the report using a starting [**Time range**](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range) set _prior to_ May 1, 2021, the **Negotiated savings** column isn't displayed. In these instances, the **Usage cost** column shows the gross cost of your cloud usage calculated using your [contract prices](https://docs.cloud.google.com/billing/docs/how-to/pricing-table).
  * For usage costs incurred _after_ May 1, 2021, your _on-demand rate_ is based on the publicly available list prices, and the **Usage cost** column shows the gross cost of your cloud usage calculated using list prices. The savings you earn with your custom contract prices (compared to list prices) is displayed on the report as a _negotiated savings_ credit.

![Example of a billing report for a Cloud Billing account
that's associated with a custom pricing contract, showing Negotiated
savings as a credit column, separate from the Usage cost column that displays
base usage cost calculated using list prices.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports2-contract.png)Example of a billing report for a Cloud Billing account that's associated with a custom pricing contract, configured with a **Time range** starting _after_ May 1, 2021.

**Note:** The first full month of data with _Negotiated savings_ is May 2021.

### Related report

To see an overview of how much your usage-based credits and discounts are saving you, view the [Cost Breakdown report](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).

## Related topic

  * [Analyze billing data with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
