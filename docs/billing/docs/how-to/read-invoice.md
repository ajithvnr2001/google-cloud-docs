---
url: https://docs.cloud.google.com/billing/docs/how-to/read-invoice/
title: Understand Your monthly invoice \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:56.393045+00:00
---

# Understand Your monthly invoice  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/read-invoice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Understand Your monthly invoice Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

When you [request invoiced billing](https://docs.cloud.google.com/billing/docs/how-to/invoiced-billing), Google extends a line of credit to you for your computing costs, and you receive an invoice each month. Typically, invoiced billing is used by large businesses.

An invoice for a particular month should be available by the fifth business day of the following month. For example, your September invoice will be ready no later than the fifth business day of October. Invoices aren't generated on weekends or bank holidays, so you should expect invoices to be delayed during those periods.

You might receive multiple invoices that are split across a set of transactions, when they involve resellers or multiple countries. For more information, see [Split invoicing for agency model transactions](https://docs.cloud.google.com/billing/docs/how-to/split-invoice).

### Cost data available in an invoice

The invoice total generally includes all costs incurred during a given calendar month. Sometimes, at the end of a calendar month, there is a delay in usage reporting. The costs of late-reported usage might not be included on that month's invoice and instead might roll over to the next month's invoice. As a result, your invoice might include costs for more than one calendar month.

When you [view your invoice details](https://docs.cloud.google.com/billing/docs/how-to/cost-table) or [online reports](https://docs.cloud.google.com/billing/docs/how-to/reports#invoice-charges), the usage is shown with the actual usage date.

Other data specific to an invoice includes the totals of any taxes and adjustments.

  * For a detailed breakdown of the taxes on an invoice, [view the cost table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table), or [view the details of your invoice](https://docs.cloud.google.com/billing/docs/how-to/get-invoice#invoiced-account).
  * For guidance on understanding and analyzing any adjustments, see [Understand memos and adjustments](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#understand-memos).



## Download your invoice

If your account is configured for monthly invoicing, you can [download your invoice](https://docs.cloud.google.com/billing/docs/how-to/get-invoice#invoiced-account) in the following two formats:

  * PDF: The PDF format is intended for your Accounts Payable department to review your monthly Google Cloud cost totals and to learn how and when to pay Google. Your PDF invoice is summarized and doesn't provide details for every resource cost or cost per subaccount (for resellers).

  * CSV: Prior to your January 2021 invoice, the CSV format provided more details than those included in the PDF. Starting with your January 2021 invoice, these details have been removed and now the CSV invoice mirrors the PDF and includes the invoice header information and cost totals. You can view the invoice cost details in the downloadable [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table), including project-level costs and additional details you might need, such as service IDs, credit IDs, labels, and total costs by subaccount (for resellers). You can access this report from the Google Cloud console.

**Note:** If you want to review and analyze detailed month-to-month costs for projects, SKUs, and subaccounts (for resellers) view your [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) and download it to CSV for analysis. If you want to collect and analyze more granular data on how you are billed, we recommend you enable [Cloud Billing Export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). For more information, review [key concepts for Cloud Billing data export, online reports, and invoices](https://docs.cloud.google.com/billing/docs/onboarding-checklist#key-concepts).



## Columns in the CSV invoice

**Caution:** Starting with your January 2021 invoice (available in February 2021), we removed the detailed usage cost line items from your invoices. This means the columns described here no longer appear on your CSV invoice. The content provided here is maintained for _historical purposes only_. If your organization previously processed the invoice CSV and you need the invoice cost details, download the CSV from the [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) and process it in place of the invoice CSV.

For invoices _prior to January 2021_ , the following columns appear in the CSV invoice:

Field | Description | Account Name | The name of the Cloud Billing Account that the usage is associated with.  
---|---  
Account ID | The Cloud Billing Account ID that the usage is associated with.  
Source*  
* As of November 2019, this field is removed from the invoice CSV. | The name of the project that generated the Cloud Billing data. **Caution** : Starting with your **November 2019 invoice** (available in December 2019), we removed the project-level cost detail from your invoices and statements. This means that the `Source` field no longer appears in the invoice CSV.  
Product | The Google Cloud service that reported the Cloud Billing data.  
Resource Type | A description of the resource used by the service. For example, a resource type for Cloud Storage is _Standard Storage US_.  
SKU ID | The ID of the resource used by the service. For the full list of SKUs, see the [ Pricing table report](https://docs.cloud.google.com/billing/docs/how-to/pricing-table).  
Description | A description of the type of cost for the line item.  
Start Date | The date when the invoice period began.  
End Date | The date when the invoice period ended.  
Quantity | The quantity of units used.  
Unit | The billing unit of the usage (such as hour or gibibyte month).  
Amount | The calculated cost of the usage.  
**Note:** Invoice usage details don't include a column for the SKU price. If you have negotiated pricing, the invoice amount has that pricing applied to it. To view your prices per SKU, see the [Pricing table report](https://docs.cloud.google.com/billing/docs/how-to/pricing-table) or [export your Cloud Billing prices to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). If you have questions regarding pricing per SKU, contact your Account Representative for more details.

## Related topics

  * [Cost table report: View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [Get a Cloud Billing document such as an invoice, statement, or receipt](https://docs.cloud.google.com/billing/docs/how-to/get-invoice)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)
  * [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [Key concepts for Cloud Billing data export, online reports, and invoices](https://docs.cloud.google.com/billing/docs/onboarding-checklist#key-concepts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
