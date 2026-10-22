---
url: https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs/
title: View Gemini Enterprise costs in Cloud Billing reports \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:44.197227+00:00
---

# View Gemini Enterprise costs in Cloud Billing reports  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  View Gemini Enterprise costs in Cloud Billing reports Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to track and analyze your Gemini Enterprise subscription and consumption costs using Cloud Billing Reports. Using these methods, you can get SKU-level visibility into your base subscription fees and overages, or view your Gemini Enterprise costs summarized by the Gemini product.

## Overview of Gemini Enterprise billing

Gemini Enterprise is billed on a subscription-seat basis, including potential consumption-based charges for usage that exceeds your subscription limits (quotas). Understanding how these costs flow into your billing reports is essential for accurate budgeting and chargeback mapping.

## Reporting capabilities for Gemini Enterprise

Costs for Gemini Enterprise subscriptions are categorized under the `Vertex AI Search` [Service](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-services), (service ID: 74B1-77CF-C302) which can lead Gemini Enterprise costs to be grouped with other related service costs. To help you better distinguish the specific Gemini Enterprise costs, use the following billing Report settings and filters to view your Gemini Enterprise subscription and overage costs:

### _Originating products_ filter for logical product suites and families

**What it does** : The [**Originating products** filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-orig-products) groups related SKUs and services into product suites and _logical_ product families, independent of the underlying technical [Google Cloud Service](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-services).

**How to use it** : Filter the report for the **Gemini Enterprise** _Originating products_ to cleanly isolate your AI subscription costs and AI overage spend, regardless of the underlying Google Cloud Service.

### SKU-level granularity for overages

If you incur additional Gemini Enterprise charges (such as consumption-based overages or add-ons), set the report [Group by setting](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) to [`SKU`](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-sku) to view a detailed breakdown of the costs.

**What it does** : [Grouping by SKU](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-sku) breaks down costs into the most granular components. For Gemini Enterprise charges, you can separate the base _Gemini Enterprise Subscription_ SKUs from any _Gemini Enterprise Overage_ SKUs.

**Benefit** : Grouping by SKU gives you transparency into the exact drivers of your Gemini Enterprise spend.

## Configure your cost report for Gemini Enterprise spend

[Cost reports](https://docs.cloud.google.com/billing/docs/how-to/reports) are accessible in the Billing section of the Google Cloud console.

### Use preset report for quick configuration

Take the following steps to access Billing Reports and select a _preset_ cost report to focus on your granular Gemini Enterprise costs:

  1. Make sure that you have the [**permissions required to access and view billing reports**](https://docs.cloud.google.com/billing/docs/how-to/reports#required-permissions). You'll need _Full billing account permissions_.

  2. **Access the Cloud Billing Reports page**

Follow these steps to **access the Reports page** for your Cloud Billing account:

     1. In the **Google Cloud console** , go to the **Reports** page for your **Cloud Billing** account.

[Go to the Reports page](https://console.cloud.google.com/billing/reports)

     2. At the prompt, select the Cloud Billing account that is linked to your Gemini Enterprise subscriptions.

The **Reports** page opens for the selected Cloud Billing account.

  3. Select the preset report **Gemini Enterprise costs by SKU**.

[Preset reports](https://docs.cloud.google.com/billing/docs/how-to/reports#preset_views) are accessible in the saved reports carousel, and in the **All reports** page.

![Preset and saved reports carousel, use to quick-configure the Gemini Enterprise report filters and settings.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-presets-and-saved-views-ge.png)

When you select the **Gemini Enterprise costs by SKU** preset report, your Billing Report is configured as follows:

     * [Time range](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range): By charge period for the current month.
     * [Group by](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by): SKU - shows granular costs for each SKU.
     * [Filter by](https://docs.cloud.google.com/billing/docs/how-to/reports#filters): All _Gemini Enterprise_ **Originating products**.



### Manually configure your cost report for detailed Gemini Enterprise spend

Take the following steps to access Billing Reports and configure a cost report to focus on your Gemini Enterprise costs:

  1. Make sure that you have the [**permissions required to access and view billing reports**](https://docs.cloud.google.com/billing/docs/how-to/reports#required-permissions). You'll need _Full billing account permissions_.

  2. **Access the Cloud Billing Reports page**

Follow these steps to **access the Reports page** for your Cloud Billing account:

     1. In the **Google Cloud console** , go to the **Reports** page for your **Cloud Billing** account.

[Go to the Reports page](https://console.cloud.google.com/billing/reports)

     2. At the prompt, select the Cloud Billing account that is linked to your Gemini Enterprise subscriptions.

The **Reports** page opens for the selected Cloud Billing account.

  3. **Configure the report to focus on Gemini Enterprise costs**

![Configuring the Originating products filter.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-orig-prod-filter.png)![](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-orig-prod-filter.png)

     1. In the [**Report filters**](https://docs.cloud.google.com/billing/docs/how-to/reports#filters), open the [**Originating products** filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-products), search for and select all **Gemini Enterprise** originating products, such as _Gemini Enterprise_ and _Gemini Enterprise Agent Platform_ , then click **Apply**.

     2. In the [**Report filters**](https://docs.cloud.google.com/billing/docs/how-to/reports#filters), set the [**Group by**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) setting to [group by **SKU**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-sku), then click **Apply**.

**Tip** : For daily or monthly cost granularity, you can group by _Date > SKU_ or _Month > SKU_.

When you group by SKU, the report table and chart displays costs by individual SKUs. Your report shows:

        * **Subscription SKU(s)** : Shows the daily prorated subscription costs.
        * **Overage SKU(s)** : Shows any usage-based charges incurred beyond your subscription seat limit.
     3. Adjust the **Time range** options and **chart settings** :

        * By default, when you first access the Reports page, the [Time range](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range) setting is set as _Charge period_ (formerly _Usage date_), for the current calendar month. Use the **Time range** filter to adjust the time period for the report data, to view trends of your daily or monthly costs.
        * Adjust [chart settings](https://docs.cloud.google.com/billing/docs/how-to/reports#changing_chart_settings) to change the display of data in the report chart and table.

![Example of the reports page, configured to show the
    Gemini Enterprise costs.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-gemini-enterprise.png)Example of the reports page, configured to show the Gemini Enterprise costs grouped by SKU. 

![](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-gemini-enterprise.png)

### Configure your cost report for summarized Gemini Enterprise spend

Take the following steps to access Billing Reports and configure a cost report to focus on your Gemini Enterprise costs, grouped by Originating product. Using this configuration, your report can show costs similar to the [cost view available in the Billing tab](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs) on the _Usage & Spending_ page accessible in the _Gemini Enterprise console_.

In the Gemini Enterprise console, the Billing tab on the Usage & Spending page displays a summary of your overage and Pay-as-you-go usage costs over the last 30 days across your enabled features and tools, broken out by Gemini Enterprise app, Gemini Enterprise Agent Platform, and AI developer tools (such as Antigravity).

  1. Make sure that you have the [**permissions required to access and view billing reports**](https://docs.cloud.google.com/billing/docs/how-to/reports#required-permissions). You'll need _Full billing account permissions_.

  2. **Access the Cloud Billing Reports page**

Follow these steps to **access the Reports page** for your Cloud Billing account:

     1. In the **Google Cloud console** , go to the **Reports** page for your **Cloud Billing** account.

[Go to the Reports page](https://console.cloud.google.com/billing/reports)

     2. At the prompt, select the Cloud Billing account that is linked to your Gemini Enterprise subscriptions.

The **Reports** page opens for the selected Cloud Billing account.

  3. **Configure the report to focus on your summarized Gemini Enterprise costs**

![Configuring the Originating products filter.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-orig-prod-filter.png)![](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-orig-prod-filter.png)

     1. In the [**Report filters**](https://docs.cloud.google.com/billing/docs/how-to/reports#filters), open the [**Originating products** filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-products), search for and select all **Gemini Enterprise** originating products, such as _Gemini Enterprise_ and _Gemini Enterprise Agent Platform_ , then click **Apply**.

     2. In the [**Report filters**](https://docs.cloud.google.com/billing/docs/how-to/reports#filters), set the [**Group by**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) setting to [group by **Originating Product**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-orig-prod), then click **Apply**.

When you group by **Originating Product** , the resulting report shows your costs in the **report chart** summarized by date (or month) and each _Originating Product_ \+ _Product suite_ combination, and each row in the **report table** shows your actual costs and savings summarized by each _Originating Product_ \+ _Product suite_ combination.

        * **Gemini Enterprise app** : Look for the row with the **Originating product** _Gemini Enterprise app_.
        * **Gemini Enterprise Agent Platform** : Look for all of the rows for the **Product suite** _Gemini Enterprise Agent Platform_ , then sum up all of the costs for each of the different **Originating products** under the Gemini Enterprise Agent Platform _Product suite_.
        * **AI developer tools** : Look for the rows for the _Product suite_ Gemini Enterprise + an _Originating product_ that is an AI developer tool, such as _Antigravity_.
     3. Adjust the **Time range** options:

        * By default, when you first access the Reports page, the [Time range](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range) setting is set as _Charge period_ (formerly _Usage date_), for the current calendar month. To match the settings in the Gemini Enterprise console billing page, set the **Time range** filter to _Charge period_ , **Last 30 days**.

![Example of the reports page, configured to show the
    Gemini Enterprise costs.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-ge-costs-by-orig-prod.png)Example of the reports page, configured to show the Gemini Enterprise costs grouped by Originating product. 

![](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-ge-costs-by-orig-prod.png)

## Limitations

When using the _Originating products_ filter or the _Originating Product_ Group-by setting, the [existing cost report features](https://docs.cloud.google.com/billing/docs/how-to/reports) work as expected, with the following exceptions:

  * The [cost forecast feature](https://docs.cloud.google.com/billing/docs/how-to/reports/forecasted-costs) is disabled when using the _Originating products_ dimensions.
  * The _Originating products_ field hasn't been added to the [BigQuery export schemas](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables), so the [Generate query](https://docs.cloud.google.com/billing/docs/how-to/reports#generate-query) button is disabled when using the _Originating products_ dimensions.
  * You can't use [Gemini Cloud Assist](https://docs.cloud.google.com/billing/docs/how-to/reports#ask-gemini) to create a report using the _Originating products_ filter or Group-by setting. Instead, use the _preset report_ Gemini Enterprise costs by SKU to quickly configure a report using the _Originating products_ filter, then manually adjust the other [report filters and settings](https://docs.cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping) as needed.
  * The _Originating products_ filter is NOT available in the [Cost table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) or the [Cost breakdown report](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).



## Frequently Asked Questions (FAQ)

Gemini Enterprise is billed on a subscription-seat basis, including potential consumption-based charges for usage that exceeds your subscription limits.

### Why do I see small charges every day instead of a single monthly fee?

Cloud Billing uses daily proration for subscriptions. A monthly seat fee of $30 is billed at approximately $1 per day.

### How do I identify Gemini Enterprise overage charges?

![Configuring the Originating products filter.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-orig-prod-filter.png)![](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-orig-prod-filter.png)

![Configuring the Group by setting to use SKU.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-group-by-sku.png)![](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-group-by-sku.png)

Configure your report to:

  * Group by **SKU** and
  * Filter by **Originating products** for all **Gemini Enterprise** _product suites_ and _logical_ products.



Any overage charges appear as separate SKU line items in the report table, letting you differentiate overage costs from your fixed subscription seat costs.

## What's next

  * [Learn more about how to analyze billing data with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [Learn more about how to manage Gemini Enterprise costs](https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview)
  * [Learn how to view Gemini Enterprise costs in the Gemini Enterprise console](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
