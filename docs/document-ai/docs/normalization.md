---
url: https://docs.cloud.google.com/document-ai/docs/normalization/
title: Normalization \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:09.369951+00:00
---

# Normalization  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/normalization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Normalization Stay organized with collections  Save and categorize content based on your preferences. 

For many specific supported fields, Document AI also returns an [`entity.normalizedValue`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#normalizedvalue) in addition to the raw extracted field obtained through the `textAnchor` of each entity. It normalize the literal text. Normalization often breaks the text value up into sub-fields.

This contain the data in a standardized format to reduce post processing, and enable conversion to whatever format is selected. The `mentionText`, representing what is literally on the document, is never changed by normalization.

Normalized fields belong to one of the following categories.

## Normalized values in the console

In the Google Cloud console, the normalized fields are annotated with **G**. For example:

![enrichment](https://docs.cloud.google.com/static/document-ai/docs/images/get_started/normalization-1.png)Sample normalized field shown in the web application. 

## Supported processors

Here are the processors and fields that support entity enrichment and normalization:

Processors | Normalized fields  
---|---  
  
### Bank Statement Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Lending  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_bank-statement-parser)  
  
  * `ending_balance`
  * `starting_balance`
  * `statement_date`
  * `statement_end_date`
  * `statement_start_date`
  * `table_item/transaction_deposit`
  * `table_item/transaction_deposit_date`
  * `table_item/transaction_withdrawal`
  * `table_item/transaction_withdrawal_date`

  
  
### Identity Document Proofing Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Identity  
**Functions** | OCR, Quality Analysis  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_id-proofing-parser)  
  
  * `fraud_signals_image_manipulation`
  * `fraud_signals_online_duplicate (US only)`
  * `fraud_signals_is_identity_document`
  * `fraud_signals_suspicious_words`

  
  
### Pay Slip Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Lending  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_pay-slip-parser)  
  
  * `bonus`
  * `bonus_ytd`
  * `commissions`
  * `commissions_ytd`
  * `direct_deposit`
  * `end_date`
  * `gross_earnings`
  * `gross_earnings_ytd`
  * `holiday`
  * `holiday_ytd`
  * `net_pay`
  * `net_pay_ytd`
  * `overtime`
  * `overtime_ytd`
  * `pay_date`
  * `regular_pay`
  * `regular_pay_ytd`
  * `start_date`
  * `vacation`
  * `vacation_ytd`

  
  
### US Driver License Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Identity  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_us-driver-license-parser)  
  
  * `Date Of Birth`
  * `Expiration Date`
  * `Issue Date`

  
  
### Expense Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Procurement  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_expense-parser)  
  
  * `currency`
  * `total_amount`
  * `total_tax_amount`
  * `net_amount`
  * `receipt_date`
  * `purchase_time`
  * `start_date`
  * `end_date`
  * `line_item/amount`
  * `line_item/payment_date`
  * `line_item/payment_amount`

  
  
### Invoice Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Procurement  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor)  
  
  * `amount_paid_since_last_invoice`
  * `currency`
  * `currency_exchange_rate`
  * `delivery_date`
  * `due_date`
  * `freight_amount`
  * `invoice_date`
  * `net_amount`
  * `total_amount`
  * `total_tax_amount`
  * `line_item/amount`
  * `line_item/quantity`
  * `line_item/unit_price`
  * `vat/amount`
  * `vat/tax_amount`
  * `vat/tax_rate`

  
  
### Extraction processors

Custom extractor supports normalization of all entities with the following Google Cloud common data types: [`dateTime`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Type-DateTime), `currency`, [`money`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Type-Money), and `number`.

Processors | Normalized data types  
---|---  
  
### Custom Extractor

| **Category** | Extract  
---|---  
**Solution type** | Custom  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde)  
  
  * `dateTime as `STRING``
  * `currency as `STRING``
  * `money as `google.type.Money``
  * `number as `FLOAT` or `INTEGER``

  
  
[ Previous arrow_back  Enrichment  ](https://docs.cloud.google.com/document-ai/docs/enrichment)

[ Next BigQuery integration  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/big-query-integration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
