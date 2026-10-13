---
url: https://docs.cloud.google.com/billing/docs/how-to/split-invoice/
title: Split invoicing for agency model transactions \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:14.181471+00:00
---

# Split invoicing for agency model transactions  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/split-invoice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Split invoicing for agency model transactions Stay organized with collections  Save and categorize content based on your preferences. 

Google might send you multiple invoices for a set of transactions, also known as split invoices. Split invoices separate the Google services you buy through a Google partner reseller (third-party transactions) from services you buy directly from Google (first-party transactions). Invoices can also split between transactions in different countries.

For all other Google Cloud transactions on invoiced billing, you typically receive a single invoice from Google. You might receive more than one invoice in the same month if Google needs to issue [billing credits or adjustments](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#viewing_credits_and_adjustments).

**Note:** (**Customers in Israel**) Starting on **June 1, 2025** , for agency model transactions involving customers in Israel, you don't receive an invoice. Customers in Israel receive a _Request for payment_ document. For more information, see [Split invoicing for agency transactions for organizations located in Israel](https://docs.cloud.google.com/marketplace/docs/migrations/split-invoicing-for-agency#split-invoicing-israel).**Note:** (**Customers in Switzerland**) Starting on **June 1, 2026** , for agency model transactions involving customers in Switzerland, you don't receive an invoice for the agency model portion. Customers in Switzerland receive a _Request for payment_ document. For more information, see [Split invoicing for agency transactions for organizations located in Switzerland](https://docs.cloud.google.com/marketplace/docs/migrations/split-invoicing-for-agency#split-invoicing-switzerland).**Note:** (**Customers in Australia**) Starting on **August 1, 2026** , for agency model transactions involving customers in Australia, you might receive up to four separate billing documents. For more information, see [Split invoicing for Australia](https://docs.cloud.google.com/marketplace/docs/migrations/split-invoicing-for-agency#split-invoicing-australia).

## Know when split invoices apply

When you buy a third-party product for the first time, Google will send a confirmation email that indicates you might receive two invoices.

## View split invoices

**Starting with the November 2024 invoice** , you can view separate invoices for first-party transactions (Google) and third-party transactions (Partners) in the Cloud Billing console:

  * The [**Cost table**](https://docs.cloud.google.com/billing/docs/how-to/cost-table) report has additional fields and data to support split invoices, including the following: 
    * The [**header**](https://docs.cloud.google.com/billing/docs/how-to/cost-table#table-header) of the **Cost table** report displays a [**Publisher type** field](https://docs.cloud.google.com/billing/docs/how-to/cost-table#publisher-type-in-header) with a value of **Google** (indicating an invoice for first-party transactions) or **Partner** (indicating an invoice for third-party transactions).
    * The [**Invoice month** filter](https://docs.cloud.google.com/billing/docs/how-to/cost-table#time-range) displays the [**Publisher type**](https://docs.cloud.google.com/billing/docs/how-to/cost-table#publisher-type-in-header) (either _Google_ or _Partner_) below the month and invoice number.
    * The report table has additional [columns](https://docs.cloud.google.com/billing/docs/how-to/cost-table#columns_in_the_cost_table) you can view for [**Seller name**](https://docs.cloud.google.com/billing/docs/how-to/cost-table#seller-name-column) and [**Transaction type**](https://docs.cloud.google.com/billing/docs/how-to/cost-table#transaction-type-column).



For more information, see [About split invoices](https://docs.cloud.google.com/billing/docs/how-to/cost-table#split-invoices) in the _View and download the cost details of your invoice or statement_ documentation.

## Pay split invoices

To pay split invoices, you might need to set up multiple vendors in your accounts payable (AP) system, because payments for each invoice go to different entities.

For more information, see [Make a Payment to an Invoiced Cloud Billing Account](https://docs.cloud.google.com/billing/docs/how-to/pay-invoice).

## Export split invoice data

If you enable billing data export to BigQuery, three fields are available to help you identify and analyze transactions on split invoices. These fields are available in both the [_standard usage cost data_ table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#standard-usage-cost-data-schema) and the [_detailed usage cost data_ table](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#detailed-usage-cost-data-schema).

  * `invoice.publisher_type`: The publisher type field indicates when Google splits your invoices between transactions directly with Google (first-party), and transactions with a partner (third-party).
  * `seller_name`: The legal name of the seller.
  * `transaction_type`: The transaction type of the seller, indicating services sold by Google, or third-party services either resold by Google or sold by a partner.



For more information about the exported billing data fields, see [Standard usage cost data schema](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#standard-usage-cost-data-schema) and [Detailed usage cost data schema](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage#detailed-usage-cost-data-schema).

For more information about exporting billing data, see [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

## What's next

  * For more information about the agency model and when it applies to your transactions, see [transaction models](https://docs.cloud.google.com/marketplace/docs/partners/transaction-models).
  * For information about the migrating to the agency model, see [Migration to transacting in the agency model](https://docs.cloud.google.com/marketplace/docs/partners/migrations/agency-model-transactions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
