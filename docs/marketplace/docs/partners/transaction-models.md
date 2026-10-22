---
url: https://docs.cloud.google.com/marketplace/docs/partners/transaction-models/
title: Transaction models \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:18.333734+00:00
---

# Transaction models  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/transaction-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/partners/transaction-models)



Send feedback 

#  Transaction models Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Marketplace supports the following two transaction models:

  * **The agency model** : Under the agency model, Google acts as an agent for you as you offer your product through Cloud Marketplace. Google facilitates and processes the transaction, but you're the Merchant of Record for the transaction. Your customers receive two invoices: one for their purchases of Cloud Marketplace products offered by independent software vendors (ISVs), and one for their purchases of first-party Google products and usage of Google Cloud services.

  * **The Merchant of Record model** : Under the Merchant of Record model, Google acts as the Merchant of Record for the transaction. This means that Google sells your product to your customers directly.




If a customer makes a transaction through Cloud Marketplace that meets the requirements of the agency model (described below on this page), Cloud Marketplace uses the agency model for that transaction. Otherwise, Cloud Marketplace uses the Merchant of Record model for that transaction.

When your customers make transactions through Cloud Marketplace, Cloud Marketplace notifies them during the purchasing process whether it's using the agency model or the Merchant of Record model for that transaction.

To verify the transaction model for your customers' transactions, [check the `transaction_model` field](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight#agency-fields) in your Customer Insights reports.

## Requirements to transact through the agency model

For a transaction to occur through the agency model, the following requirements must be met:

  * Both you and the customer must be located in a region that Cloud Marketplace supports for the agency model. For a list of supported regions, visit [Agency jurisdictions](https://cloud.google.com/terms/marketplace-agency-jurisdictions).

  * Your organization must have agreed to the [current version](https://cloud.google.com/terms/marketplace-vendor-agreement) of the Marketplace Vendor Agreement.

  * Both you and the customer must have verified your identity to Google, if you were requested to by Google. For more information, visit [Verify your identity](https://docs.cloud.google.com/marketplace/docs/partners/verify-your-identity).




## Split invoicing for some agency model transactions

For transactions that meet the following criteria, Google invoices your customers' purchases of Cloud Marketplace products that you offer separately from their purchases of first-party Google products and usage of Google Cloud services:

  * The transactions occur under the agency transaction model.
  * Your customer's Google Cloud organization's payment profile is located in one of the following countries: 
    * The United Kingdom (starting February 1, 2025)
    * Germany (starting February 1, 2025)
    * France (starting February 1, 2025)
    * Israel (starting June 1, 2025)
    * Belgium (starting September 1, 2025)
    * Italy (starting September 1, 2025)
    * Luxembourg (starting September 1, 2025)
    * Netherlands (starting September 1, 2025)
    * Poland (starting September 1, 2025)
    * Spain (excluding the Canary Islands) (starting September 1, 2025)
    * Sweden (starting September 1, 2025)
    * Switzerland (starting June 1, 2026)
    * Australia (starting August 1, 2026)



For all other transactions, your customers continue to receive a single invoice from Google for their Cloud Marketplace transactions and their usage of Google products and services.

### Split invoicing for agency transactions for organizations located in Switzerland

**Three Invoices:** Starting with charges incurred in June 2026 (invoices likely to be received July 1, 2026), your customers will receive three separate billing documents each month:

  * **Google Cloud Invoice:** This will cover their direct purchases of Google Cloud products and services, including premium operating systems (OS). The payment information for this invoice will remain the same.
  * **Cloud Marketplace "Request for Payment":** This new document will specifically cover their purchases of third-party products from Cloud Marketplace that are governed under the Agency model. This document won't have VAT as part of the Total amount due.
  * **Cloud Marketplace Invoice:** This new document will specifically cover their purchases of third-party products from Cloud Marketplace that are governed under Google as the Reseller model.



### Split invoicing for agency transactions for organizations located in Israel

Starting June 1, 2025, for transactions that meet the following criteria, Google invoices your purchases of Cloud Marketplace products offered by independent software vendors (ISVs) separately from your purchases of first-party Google products and usage of Google Cloud services:

  * The transactions occur under the agency transaction model.
  * Your Google Cloud organization's payment profile is located in Israel.



Starting June 1, 2025, you also receive a **Request for Payment** document containing additional payment information for all of your Cloud Marketplace transactions. For more information, see [Migration to split invoicing for agency model transactions](https://docs.cloud.google.com/marketplace/docs/migrations/split-invoicing-for-agency).

###  Split invoicing for agency transactions for organizations located in Australia 

**Four Documents:** Starting with charges incurred in August 2026 (invoices likely to be received September 1, 2026), your customers will receive up to four separate billing documents each month. Depending on your location (as the seller), they receive different documents for your products:

  * **If you are located in Australia (Domestic):**
    * Your customer receives a **"Request for Payment"** document for your products.
    * This document does not include GST or other Google-assessed taxes.
    * You are responsible for invoicing the customer directly for any applicable taxes (GST).
  * **If you are located outside Australia (Foreign):**
    * Your customer receives a standard **Google Cloud Marketplace Invoice** for your products.
    * This document includes Google-assessed taxes.



For more information on the other documents they receive, see [Transaction models](https://docs.cloud.google.com/marketplace/docs/transaction-models#split-invoicing-australia).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
