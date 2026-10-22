---
url: https://docs.cloud.google.com/billing/docs/how-to/reports/charges-on-invoices/
title: Billing reports: View the charges on your invoices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:18.333192+00:00
---

# Billing reports: View the charges on your invoices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/reports/charges-on-invoices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Billing reports: View the charges on your invoices Stay organized with collections  Save and categorize content based on your preferences. 

Invoices include charges for _all of the projects_ linked to a billing account, as well as _account-level charges_ not specific to a project, and _invoice-level charges_ that are added at the time an invoice is generated (such as tax). To view all of the costs on your invoice, you must access your Cloud Billing account using [billing-account-level permissions](https://docs.cloud.google.com/billing/docs/how-to/reports#required-permissions).

In [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can change the report view to display charges by billing period (formerly _invoice month_), including invoice-level charges (for example, taxes, contractual credits, adjustments, or surcharges). If you receive more than one invoice for a month, the report view aggregates all invoice costs for the _invoice month_. In Billing Reports, you _can't_ view the report by _individual_ invoice.

If you want to view detailed costs by _individual invoice_ , see the [Cost table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table). Using the Cost table report, you can view invoice costs by invoice number and [download the report to CSV](https://docs.cloud.google.com/billing/docs/how-to/cost-table#download-to-csv) for offline analysis.

To view the cost report for a billing period (formerly invoice month), do the following:

  1. In the **Billing** section of the Google Cloud console, [access the cost report](https://docs.cloud.google.com/billing/docs/how-to/reports#getting_started) for the Cloud Billing account you want to analyze.

  2. In the [**Time range** setting](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range), select **Billing period** (formerly _Invoice month_), then set your **From** and **To** month range.



  * The **Invoice level charges** section (below the Savings section in the **Filters** panel) shows **Tax** and **Adjustments** by default.

**Note:** Adjustments appear on your invoice when Google needs to modify your account balance. Adjustments are rare and are typically in the form of credits, which reduce your account balance.
  * The report summary, above the chart, displays taxes when **Billing period** is selected.


**Note:** The **Billing period** (formerly _Invoice month_) filter shows historical billing data for the selected months. You can only select months that are complete. For example, if you're viewing the report on July 15, the most recent invoice month you can select is June. Data filtered by **Billing period** is available back to May 2019.

![Costs by invoice
 month, including invoice-level charges.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports8.png)

  * The summary footer, below the table, displays the subtotal, the invoice-level charges (adjustments and tax), and the invoice total.

![Footer summarizing your report costs based on your filter selections.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports9.png)

Invoice-level charges (tax and adjustments) are _NOT_ displayed when the **Time range** setting is by **Charge period** (formerly _Usage date_), or when you set other report filters, such as **Projects** , **Services** , or **SKUs**.

![Example of the footer for a report configured to use a charge period time range.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports9a.png)




### View invoice charges for the most recent billing period (formerly _invoice month_)

To view all invoice charges for the most recent billing period (formerly _invoice month_), select the [**preset** report: **Last invoice by service**](https://docs.cloud.google.com/billing/docs/how-to/reports#preset_views). This preset report automatically sets the report filters as follows:

  * In the **Time range** setting, **Billing period** (formerly _Invoice month_) is selected, and the **From** and **To** month range is set for the most recent, complete billing period month (for example, May 2026).
  * The **Group by** filter is set to group costs by **Service**.
  * All other report filters are set to use their default configurations (for example, _ALL_ projects, services, SKUs, and savings options).



Using the **Last invoice by service** preset report, you can quickly view a report with totals that map to your most recent invoice or statement, showing costs for all services and SKUs, grouped by Service, and including discounts, credits, and invoice-level charges (such as taxes, contractual credits, adjustments, or surcharges).

Billing Reports aggregates all invoice costs for the _billing period_ (formerly _invoice month_), and NOT by _individual_ invoice. If you receive more than one invoice in a month, your _billing period_ totals might not map to the totals of an _individual_ invoice issued in the same month. If you want to view the detailed costs per individual invoice, see the [**cost table report**](https://docs.cloud.google.com/billing/docs/how-to/cost-table).

### View invoice charges for a specific billing period

To view all invoice charges for _a specific billing period_ , do the following:

  1. In the **Billing** section of the Google Cloud console, [access the cost report](https://docs.cloud.google.com/billing/docs/how-to/reports#getting_started) for the Cloud Billing account you want to analyze.
  2. In the [**Time range** setting](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range), select **Billing period** (formerly _Invoice month_), then set your **From** and **To** month range for the same month (for example, January 2026).
  3. Select your preferred **Group by** setting (for example, Project, Service, or SKU).
  4. Ensure _no other filters_ are set. That is, you should view the report for _ALL_ filter options (such as projects, services, SKUs, and savings options).

In the summary footer, the cost breakdown displays:

     * **Subtotal** : The sum of the **Group by** costs, after Savings discounts and credits.
     * **Adjustments** : The sum of credit or debit memos and other adjustments applied to your Cloud Billing account due to billing corrections or contractual requirements, as reported from the invoices issued for the _billing period_ month (formerly _invoice month_). Adjustments might be issued in a different month than the billing period month to which they are applied. For more details on adjustments, see [Understand memos and adjustments](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#understand-memos). You won't see this line item if you have no adjustments applied to your invoices.
     * **Tax** : Sum of all taxes reported from all of the invoices for the billing period month.
     * **Invoice total** : Includes all savings, adjustments, taxes, and rounding errors, aggregated for all invoices issued for the _billing period_ month.

**Note:** Rounding errors are included in the **Invoice total** but aren't listed as a separate line item. To view the exact rounding error sum, hold the pointer over the tooltip (help) next to **Invoice total**.



### Invoice total versus Filtered total

In the summary footer of the report, the display of invoice-level costs and the type of report total depends on how your report filters are configured.

  * **Invoice total** : Invoice total includes all costs and savings for the _billing period_ month, as well as invoice-level charges such as taxes, adjustments, and rounding errors, aggregated for all invoices issued during the same _billing period_ month. To view the invoice total, set the **Time range** to **Billing period** (formerly _Invoice month_), and make sure all of the other filters are set to show _all_ options (such as all Projects, Services, SKUs, and Savings).

![Example of a report footer showing an invoice total, which includes
taxes and adjustments.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports8-inv-total.png)

  * **Filtered total** : When your **Time range** is set to **Billing period** , the filtered total summarizes your charges based on the filter selections you have chosen (such as filtering on a subset of Projects, Services, or SKUs), excluding tax, adjustments, and rounding errors. When you see a _Filtered total_ in the report, invoice-level charges aren't displayed in the summary footer and aren't included in the calculation of the filtered total. A filtered total doesn't match the total on your monthly invoice or statement.

![Example of a report footer showing a filtered total. When any report
filter is set, invoice-level charges aren't included in the amount of the
filtered total.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports8-filtered-total.png)




### Related reports

  * [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table): A detailed, tabular view of your monthly costs for a given invoice or statement, which can be filtered and downloaded.
  * [Cost Breakdown report](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown): An at-a-glance waterfall view of your usage costs calculated using the on-demand price for your Google Cloud usage, how discounts and credits saved you money, and any invoice-level charges applied (if you're viewing the cost breakdown for a _billing period_ (formerly _invoice month_) time range).



## Related topic

  * [Analyze billing data with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
