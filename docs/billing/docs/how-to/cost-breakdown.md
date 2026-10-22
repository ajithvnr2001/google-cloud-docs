---
url: https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown/
title: Understand your savings with cost breakdown reports \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:40.046318+00:00
---

# Understand your savings with cost breakdown reports  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Understand your savings with cost breakdown reports Stay organized with collections  Save and categorize content based on your preferences. 

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrate to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

## Overview

![Example of a cost breakdown report.](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-list.png)

![](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-list.png)

For the selected date range and filters, the **Cost breakdown** report shows your base usage cost (calculated from on-demand prices) and how discounts, credits, adjustments, and taxes affect this cost to arrive at your total.

The [_waterfall chart_](https://wikipedia.org/wiki/Waterfall_chart) displays **Charges** in orange, **Credits** in green, and **Subtotals** and **Totals** in blue.

### Permissions required to access the cost breakdown report

To view the cost breakdown report for your Cloud Billing account, you need a role that includes the following [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on your Cloud Billing account:

  * [`billing.accounts.getSpendingInformation`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information) to view costs and usage for a billing account.



To gain this permission using a predefined role, ask your administrator to grant you one of the following [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access) roles on your Cloud Billing account:

  * Billing Account Administrator
  * Billing Account Costs Manager
  * Billing Account Viewer



For more information about billing permissions, see the following:

  * [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations)
  * [Understanding predefined IAM roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)



## Access the report

To view the **Cost breakdown** report for your Cloud Billing account:

  1. In the Google Cloud console, go to your Cloud Billing account.

[Go to your Cloud Billing account](https://console.cloud.google.com/billing/overview)

  2. At the prompt, **choose the Cloud Billing account** for which you'd like to view reports. The Billing **Overview** page opens for the selected billing account.

On the billing account **Overview** page, the **Savings** calculation includes all eligible discounts and credits. The _View details_ link takes you to the **Cost breakdown** report:

![Example of the Total cost summary widget on the billing account overview page](https://docs.cloud.google.com/static/billing/docs/images/cuds-savings.png)

  3. Alternatively, in the **Cost management** section of the **Billing navigation menu** , select **Cost breakdown**.




## How to read the cost breakdown chart

From left to right, the chart displays bars for charges, then credits, then subtotal, then any invoice-level charges, and then total, aggregated for all costs incurred during the selected time range.

The first bar on the chart is the gross cost of your usage, which represents the amount that you would've paid during the selected _time range_ if you were charged only at the _on-demand rate_ for your Google Cloud usage. Then, the report shows you how much you saved, broken out by savings types (for example, committed use discounts and sustained use discounts). Finally, if your _time range_ is configured for a _Billing period_ (formerly _Invoice month_), the report shows your invoice-level charges such as tax and adjustments (if any) applied for the selected invoice months.

If your Cloud Billing account is associated with a _custom pricing contract_ , the _on-demand rate_ used to calculate the gross cost of your usage depends on the _time range_ of the costs you're analyzing:

  * For costs incurred _before_ May 1, 2021, your _on-demand rate_ is based on your contract prices, and includes the savings you earned compared to list prices.
  * For costs incurred _after_ May 1, 2021, your _on-demand rate_ is based on the publicly available list prices. The savings you earn with your custom contract prices (compared to list prices) is displayed on the report as a _negotiated savings_ credit.



Below the chart is a summary table of the information in the report. The summary table includes a row for each bar on the chart, displays the effective % rates of costs and savings, and provides links to open related report pages where you can view the details behind specific cost breakdown report values.

Examples  
---  
For a Cloud Billing account associated with _standard list prices_ (and for any billing account viewing costs incurred prior to May 1, 2021), the cost breakdown report displays a **Usage cost** column, along with any applicable credits and invoice-level charges:  ![Example of a cost breakdown report, showing the base usage cost](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-list.png)**Figure 1** : Example of a cost breakdown report, showing the base usage cost and how that cost was affected by any credits, adjustments, and taxes. Click the image to view an enlarged version.  ![](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-list.png) |  For a Cloud Billing account associated with a _custom pricing contract_ , when viewing the report using a time range that starts on _May 1, 2021_ , or later, the cost breakdown report displays a **Usage cost** column, and a  **Negotiated savings** column, as well as any other applicable credits and invoice-level charges:  ![Example of a cost breakdown report, showing negotiated savings](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-contract.png)**Figure 2** : Example of the cost breakdown report for a Cloud Billing account associated with a custom pricing contract. Click the image to view an enlarged version. ![](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-contract.png)  
  
### About on-demand rates

Each Cloud Billing account is associated with a _price list_ , which provides the prices per SKU for your usage of Google Cloud Platform services, Google Maps Platform, and Google Workspace.

  * If your Cloud Billing account is using standard list prices, your on-demand rates are based on the publicly available price list.
  * If your Cloud Billing account is associated with a custom pricing contract, your on-demand rates are based on your custom price list.

    * On the cost breakdown report, when viewing the report using a time range that starts _before_ May 1, 2021, the gross cost of your usage is calculated using your custom contract prices.
    * When viewing the report using a time range that starts _after_ May 1, 2021, the gross cost of your usage is calculated using [list prices](https://docs.cloud.google.com/billing/docs/how-to/pricing-table).



To view your prices per SKU for your Cloud Billing account, see the [Pricing table report](https://docs.cloud.google.com/billing/docs/how-to/pricing-table) or [export your Cloud Billing prices to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). If you have questions regarding pricing, contact your Account Representative for more details.

## Configure your report settings

You can select the costs you want to analyze and configure the display of your cost breakdown report using the **Time range** and other **filters**. As you configure the report, your page URL updates to include your selections; use link **Share** to copy the URL to share the report. Click the get_app **Download CSV** selector located above the summary table to download the filtered cost breakdown data.

![Example of a cost breakdown report emphasizing the available report
          settings and filters, including time range, projects, services, and
          SKUs.](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-ucv-filters.png)**Figure 3** : Example of the cost breakdown report for a Cloud Billing emphasizing the available report settings and filters, including time range, projects, services, and SKUs.

### Time range

Set the range of time for the usage costs you want to analyze. You can select **Charge period** (formerly _Usage date_) or **Billing period** (formerly _Invoice month_). By default, when you first access the report, the **Time range** is set to **Billing period** , with the most recent completed invoice month selected.

![Shows the report's time range setting in the filters panel, with options
     to select charge period or billing period.](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-time-range.png)

  * **Charge period** (formerly _Usage date_) returns actual usage and cost data incurred during the date range selected. When you select **Charge period** , you can choose a preset or custom time range for charting your cost data (available back to January 2017).

When you set a _charge period_ time range, the cost breakdown report _doesn't display_ invoice-level charges, such as tax, contractual credits, surcharges, or adjustments.

  * **Billing period** (formerly _Invoice month_) returns usage and charges on the invoices issued for the months selected. When you select **Billing period** , you can set a range based on complete billing period months (available back to May 2019).

When you set a _Billing period_ time range, the cost breakdown report _includes_ invoice-level charges, such as tax, contractual credits, surcharges, or adjustments.




If your Cloud Billing account is associated with a _custom pricing contract_ , the _on-demand rate_ used to calculate the gross cost of your usage depends on the **Time range** of the costs you are analyzing:

  * When viewing the report using a time range that starts _before_ May 1, 2021, the gross cost of your usage is calculated using your custom contract prices, and includes the savings you earned compared to list prices. On the report, these charges are displayed in the **Usage cost** bar.
  * When viewing the report using a time range that starts _after_ May 1, 2021, the gross cost of your usage is calculated using publicly available [list prices](https://docs.cloud.google.com/billing/docs/how-to/pricing-table). On the report, these charges are displayed in the **Usage cost** bar. Additionally, the savings you earn with your custom contract prices (compared to list prices) is displayed on the report as a _Negotiated savings_ credit.



### Filters

The **Cost breakdown** report can show all charges and credits for the entire Cloud Billing account, or you can filter it to focus on a specific set of resources. By default, when you first access the report, the filters are configured to include all values. As you set your filters, the amounts displayed in the report adjust to represent the aggregated charges and credits based on the filters selected.

![Various filter selectors in the filters panel.](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-filters.png)

  * **Subaccounts** : If you're viewing a primary billing account with [subaccounts](https://docs.cloud.google.com/billing/docs/concepts#subaccounts), you can select all subaccounts (default) or select a subset of subaccounts by clicking them in the list.

  * **Folders & Organizations**: Folders and organizations are components of a [project hierarchy](https://docs.cloud.google.com/billing/docs/how-to/reports-project-hierarchy#about-project-hierarchy), the resource hierarchy mapping of a project. If the **Time range** is configured to _start on or after January 1, 2022_ , you can select all folders and organizations (default) that are associated with the [projects that are linked to the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked), or select a subset of folders and organizations.

The values in the selector are listed in alphabetical order by resource name. To determine if a value is an organization or a folder, look at the [ID number following each name](https://docs.cloud.google.com/billing/docs/release-notes#March_08_2022). ID numbers are prefaced with _folders/_ or _organizations/_ to indicate the type of resource.

For the Cloud Billing account you're viewing, if none of the [linked projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked) are associated with any folders or organizations, then this filter option isn't displayed. To learn more about organizations, folders, and project hierarchy, see [Billing reports: Analyzing your costs by project hierarchy](https://docs.cloud.google.com/billing/docs/how-to/reports-project-hierarchy).

  * **Projects** : You can select all Google Cloud projects under the Cloud Billing account (default) or select a subset of projects by clicking them in the list.

  * **Services** : You can select all services (default) or select a subset of services by clicking them in the list.

  * **SKUs** : You can select all SKUs (default) or select a subset of SKUs by clicking them in the list. To learn more about SKUs, see the [pricing table report](https://docs.cloud.google.com/billing/docs/how-to/pricing-table).

  * **Applications** : You can select all [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) applications (default) or select a subset of applications by clicking them in the list.

App Hub applications might incur usage and costs in more than one billing account and associated projects. Cost data filtered by application might be based on partial data, limited to projects and costs for the Cloud Billing account you are actively viewing.

To filter on costs that are not part of an App Hub application, select _[Charges not specific to an application]_.




![Setting the Locations filters in the filters panel.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-filters-locations.png)

  * **Locations** : By default, all locations are enabled. By clicking the location tiles, you can filter on a subset of locations by **geography** (such as Europe), **multi-region** (such as Global), or **region** (such as us-east1). Specifically, the report is filtered by the **regions** and **multi-regions** selected.

Use the tiles in **geography** to quickly select (or deselect) all regions and multi-regions in that geography. Multi-region tiles are marked with an asterisk (for example, `us*`).

Learn more about [geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).




![Setting the Labels filters in the filters panel.](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-labels-filters.png)

  * **Labels** : Labels are key and value pairs you attach to resource usage (for example, Compute Engine or Cloud Storage). To filter usage by label:

    1. Expand the **Labels** section.
    2. Select the label **Key**.
    3. Select the **Value** under that key you want to filter on (the default is all values under the selected key).

To **add another** label with a different key, click **\+ Add Label** , and then select the **key** and **values** for the label filter.

To **remove** a label filter, click delete (delete) for each _label key-value_ pair that you want to remove.

If you want to view costs for Google Kubernetes Engine, you can filter your resources using the following label keys:

    * `goog-fleet-project`: Filter cluster resources by [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project), if the cluster is registered to a fleet.
    * `goog-k8s-cluster-location`: Filter GKE resources by location.
    * `goog-k8s-cluster-name`: Filter GKE resources by cluster.
    * `goog-k8s-node-pool-name`: Filter cluster resources by node pool.

To filter GKE resources using the following label keys, you must [enable cost allocation for your GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations):

    * `k8s-namespace`: Filter GKE resources by namespace.
    * `k8s-namespace-labels`: Filter GKE resources by [fleet namespace label](https://docs.cloud.google.com/anthos/fleet-management/docs/setup-teams#manage_fleet_namespace_labels).

When filtering by label keys, you can't select labels applied to a project. You can select other _user-created_ labels that you set up and applied to Google Cloud services. For more information about labels, see [common uses of labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#common-uses) and [creating and managing resource labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).




### Chart unit

![Setting the Labels filters in the filters panel.](https://docs.cloud.google.com/static/billing/docs/images/cost-breakdown-chart-unit.png)

The **chart unit** setting is located above the bar chart and controls the value unit for the amounts displayed in the bar chart. By default, when you first access the report, the chart unit is configured to display the values in currency. You can toggle the chart units between [**currency**](https://docs.cloud.google.com/billing/docs/resources/currency) ($) and **percent** (%) by selecting the preferred option.

The **$** icon represents the _currency_ setting for the _chart unit_ option. The actual type of currency that's used to calculate your costs matches the [currency of your Cloud Billing account](https://docs.cloud.google.com/billing/docs/resources/currency). When viewing the values in the bar chart using **currency** , the amounts of charges, credits, and subtotals and totals are prefaced with the symbol for the currency of your Cloud Billing account (for example, USD: $, GBP: £, EUR: €, or JPY: ¥).

## Understand the values in the chart and report summary

The cost breakdown chart shows the following, if applicable to your Cloud Billing account. If you don't incur these types of charges or credits, you won't see these items on your report.

### Charges

  * **Usage cost** : The monthly cost of your cloud usage calculated using the on-demand rates in effect for your Cloud Billing account.

**CUD fees in Usage costs** :

    * For previously purchased _Legacy spend-based CUDs_ and _Resource-based CUDs_ , the Usage cost amount _includes the fees_ for any [committed use discounts](https://docs.cloud.google.com/docs/cuds) (CUDs) that you purchased, before any credits are applied.
    * For the new [_Spend-based CUDs program_](https://docs.cloud.google.com/docs/cuds-multiprice), the fee to purchase spend-based CUD discounts is _excluded_ from the Usage cost amount. Instead, the spend-based CUD discounts fee is included in the _net_ calculation of the _Spend-based CUD discounts_ savings amount.



### Savings and credits

The following savings, discounts, and credits appear on the report if applicable to your Cloud Billing account and selected _Time range_ :

  * **Negotiated savings** : A credit that displays for Cloud Billing accounts _associated with a_ [_custom pricing contract_](https://docs.cloud.google.com/billing/docs/how-to/pricing-table). The **Negotiated savings** amount represents your cost savings computed using this equation:

`Negotiated savings = Costs at Contract price - Costs at List price`

**Negotiated savings** is available when using a starting **Time range** set to May 1, 2021, or later.

Note that for Cloud Billing accounts associated with a _custom pricing contract_ , when you configure the report using a starting **Time range** set _prior to_ May 1, 2021, the **Negotiated savings** bar isn't displayed. In these instances, the **Usage cost** bar is displayed, which shows the gross cost of your cloud usage calculated using your [contract prices](https://docs.cloud.google.com/billing/docs/how-to/pricing-table).

  * **Spend-based CUD _discounts_** : This is the _net_ impact of the new [spend-based commitments](https://cloud.google.com/docs/cuds-multiprice), which includes the fees paid for your spend-based CUDs as well as the discounts earned based on your [consumption model](https://docs.cloud.google.com/docs/cuds-multiprice#consumption-model-intro). When your commitments are fully utilized, this bar appears as a green credits bar. If your commitments are underutilized, this bar can appear as an orange charge bar, representing [wasted usage](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights).

  * **Legacy spend-based CUD _credits_** : For spend-based committed use discounts [(CUDs) that aren't part of the new pricing model](https://docs.cloud.google.com/docs/cuds-multiprice#affected-cuds), this is the gross credit earned in exchange for your commitment to spend a minimum amount for a service in a particular region. This credit offsets your costs calculated at list (on-demand) prices. [Learn more about spend-based committed use discounts](https://docs.cloud.google.com/docs/cuds-multiprice).

    * Learn how to [analyze the granular details of your CUDs purchase costs and credits](https://docs.cloud.google.com/billing/docs/how-to/reports#analyze-cud-credits).
    * To analyze the effectiveness of the CUDs that you purchased, [view the CUD analysis page](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).
  * **Resource-based CUD _credits_** : For eligible Compute Engine virtual machine (VM) resources where you've purchased committed use contracts in return for deeply discounted prices, this is the gross credit earned on the VM usage covered by the purchased commitments. CUD credits offset your eligible Compute Engine VM usage costs calculated at list (on-demand) prices. [Learn more about resource-based committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

    * Learn how to [analyze the granular details of your CUDs purchase costs and credits](https://docs.cloud.google.com/billing/docs/how-to/reports#analyze-cud-credits).
    * To analyze the effectiveness of the CUDs that you purchased, [view the CUD analysis page](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).
  * **Free tier usage** : Some products offer free resource usage up to specified limits. For some services, credits are applied to implement the free tier usage. [Learn more about free tiers](https://docs.cloud.google.com/free/docs/gcp-free-tier).

  * **Promotional credits** : The total savings you received from promotional credits, such as [spend-based milestone credits](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker), [Google Cloud Free Trial](https://docs.cloud.google.com/free/docs/free-cloud-features#free-trial), and marketing campaign credits, or other grants to use Google Cloud.

  * **Sustained use discounts** (Compute Engine): This credit represents the automatic savings you receive for running eligible Compute Engine instances for a significant portion of the month, with no commitment required. [Learn more about sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts).

  * **Reseller margin** : For resellers only, this is the _Reseller Program Discount_ credit you receive for selling eligible Google Cloud products.

  * **Spending-based discounts** : The total savings you earned for the time period you're viewing. Spending-based discounts offer progressively larger discounts based on your total spend over a defined period, or discounts that are applied after a contractual spending threshold is reached.

  * **Subscription credits** : The total savings you earned from long-term subscriptions to services that are purchased in exchange for discounts. These credits are typically applied to Base + Overage subscriptions, also known as Non-Unified Commitment Service (Non-UCS) subscriptions.

  * **Others** : Other credits or discounts that aren't associated with the current categories.




See Cloud Billing Reports to [learn more about savings and credits](https://docs.cloud.google.com/billing/docs/how-to/reports#credits).

### Invoice-level charges

Invoice-level charges are generated when an invoice is issued and are only displayed in the report when you're viewing your costs by **Invoice month**. When you set a **Charge period** (formerly _Usage date_) time range, the cost breakdown report doesn't display invoice-level charges. When you set a **Billing period** (formerly _Invoice month_) time range, the **Cost breakdown** report includes invoice-level charges, if applicable to your Cloud Billing account.

  * **Adjustments** : The total of any adjustments that were applied to your invoices (if applicable), for the selected billing period months. Adjustments are credits or surcharges applied to your Cloud Billing account due to billing corrections and contractual requirements. An adjustment might be issued in a different month than it's applied. For guidance on analyzing adjustments, see [Understand memos and adjustments](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#understand-memos).
  * **Tax** : The taxes that applied to your usage for the selected billing period months, for each tax type.



#### Learn more about invoice-level charges:

  * See the [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) for a detailed, tabular view of your monthly costs for a given invoice or statement (by invoice month and document number).
  * See [Cloud Billing Reports](https://docs.cloud.google.com/billing/docs/how-to/reports#invoice-charges) for an at-a-glance report view of charges by billing period month, including invoice-level charges.
  * View your [Cloud Billing documents](https://docs.cloud.google.com/billing/docs/how-to/get-invoice#get-statement-or-invoice) to see all your invoices and other documents issued to your account. Open the document to see account balance details and where credit or debit memos are applied.



### Report summary

Below the chart is a summary table of the information in the chart. The summary table includes a row for each bar on the chart, and displays the effective percentage (%) rates of charges and credits.

  * When you hold your pointer over a row in the summary table, the corresponding bar in the preceding chart is emphasized.
  * Click the **View report** links to open the corresponding report pages where you can view the details behind specific cost breakdown report values.

Links to the **Reports** page open the report with the same filters you set here.

    * The **Usage cost** row shows gross costs. The **View report** link in the **Usage cost** row opens a report _excluding all**Savings**_ options in the Report's filter settings.
    * The **View report** link in the **Cost** row opens a report _including all**Savings**_ options in the Report's filter settings.



### Not on the chart

The following is _not_ shown on the cost breakdown chart:

  * **Cost breakdown by individual invoice** : Typically, one invoice is issued per month, per Cloud Billing account, but it's possible to receive more than one invoice in a month. The cost breakdown chart aggregates the costs and credits for all invoices issued during the selected invoice months. You can't view the breakdown report for an individual invoice.
  * **BigQuery flat rate savings** : The cost of BigQuery flat rate is included in the **Usage cost** bar; we don't separate the savings you achieved from purchasing BigQuery flat rate.
  * **Cloud Storage Growth plan** : The cost of Cloud Storage is included in the **Usage cost** bar; we don't separate the savings you achieved from purchasing the Cloud Storage Growth plan.
  * **Promotional or custom pricing** : For Cloud Billing accounts associated with a custom pricing contract, when viewing cost incurred using a starting time range _before_ May 1, 2021, the cost of resources in the **Usage cost** bar is calculated using your contract prices. To view your prices per SKU, see the [Pricing table report](https://docs.cloud.google.com/billing/docs/how-to/pricing-table) or [export your Cloud Billing prices to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). If you have questions regarding pricing, contact your Account Representative for more details.
  * **Project hierarchy filter options** : When viewing cost incurred using a starting time range _before_ January 1, 2022, the **Folders & Organizations** filter selector is inactive. For the Cloud Billing account you're viewing, if none of the [linked projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked) are associated with any folders or organizations, then the **Folders & Organizations** filter isn't shown. To learn more about organizations, folders, and project hierarchy, see [Billing reports: Analyzing your costs by project hierarchy](https://docs.cloud.google.com/billing/docs/how-to/reports-project-hierarchy).



## Share or bookmark the URL of a customized report

You can bookmark or share the URL of a **Cost breakdown** report you've customized. As you configure your cost breakdown report by setting the time range and filters, your page URL updates to include your selections.

  * You can share the report by copying the **URL**. Click link **Share** to copy the URL to your clipboard.
  * Optionally, in your browser, you can **bookmark the URL** to save the URL with your report settings.

**Note:** As you configure your report by setting filters and groupings, your page URL updates to include your selections. It's possible that the URL length limit might be reached if you select many settings (for example, selecting 374 SKUs out of 375). In these instances, the link **Share** button is disabled and you see a notification on the reports page: _The URL may no longer reflect your selected filters, due to length limitations_.



## Download cost breakdown data to a CSV file

You can download the cost breakdown data to a comma-separated values (CSV) file using the get_app **Download CSV** selector located above the summary table. The CSV file includes a column for each of the items in the summary table of the report, such as cost, credits, subtotal, taxes, adjustments, and total; and a single row that shows the amount for each item. The CSV file doesn't include the _Effective rate_ data that's shown in the summary table.

### CSV filename

For the cost breakdown data, the CSV filename follows this pattern:

`[Billing Account name]_Cost Breakdown, [YYYY-MM-DD] - [YYYY-MM-DD].csv`

For example, a CSV file of the cost breakdown data downloaded for a Cloud Billing account named _My Billing Account_ , for a date range of _October 1 to December 31, 2022_ , is named:

`My Billing Account_Cost Breakdown, 2022-10-01 - 2022-12-31.csv`

**Note:** If you download a report with the same date range multiple times, then the default report name will be the same. If you configured your report with a specific set of parameters, you might want to rename the CSV file to something that'll help you differentiate between reports run using the same date range but using different report settings or filters.

## Related topics

  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [View Gemini Enterprise costs in Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs)
  * [Analyze the effectiveness of your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)
  * [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
