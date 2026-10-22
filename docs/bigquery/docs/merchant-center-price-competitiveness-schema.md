---
url: https://docs.cloud.google.com/bigquery/docs/merchant-center-price-competitiveness-schema/
title: Google Merchant Center price competitiveness table \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:46.203358+00:00
---

# Google Merchant Center price competitiveness table  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/merchant-center-price-competitiveness-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Merchant Center price competitiveness table

## Overview

Price competitiveness data in BigQuery helps merchants understand how other merchants are pricing the same product. When your Google Merchant Center reporting data is transferred to BigQuery, the format of the `PriceCompetitiveness_` table provides a daily price benchmark per country and per product. The price competitiveness table also contains several other attributes of the product to help you to understand the competitiveness of your pricing within a category or brand for example.

The data is written to a table named `PriceCompetitiveness_MERCHANT_ID` if you are using an individual Merchant ID, or `PriceCompetitiveness_AGGREGATOR_ID` if you're using an MCA account.

**Note:** To access price competitiveness data, you must meet the [eligibility requirements for market insights](https://support.google.com/merchants/answer/9712881).

## Schema

The `PriceCompetitiveness_` tables have the following schema:

Column | BigQuery data type | Description | Example data  
---|---|---|---  
`aggregator_id` | `INTEGER` | ID of the [Multi Client Account (MCA)](https://support.google.com/merchants/answer/188487) if the merchant is part of an MCA. Null otherwise. | 12345  
`**merchant_id**` | `INTEGER` | Google Merchant Center account ID. This field is a primary key. | 1234  
`**id**` | `STRING` | [Content API REST ID](https://developers.google.com/shopping-content/guides/products/product-id) of the product in the form: `channel:content_language:feed_label:offer_id`, similar to the way it's defined in the [products table schema](https://docs.cloud.google.com/bigquery/docs/merchant-center-products-schema). This field is a primary key.  | online:en:AU:666840730  
`title` | `STRING` | Title of the product. | TN2351 black USB  
`brand` | `STRING` | Brand of the product. | Brand Name  
`offer_id` | `STRING` | Merchant provided [id of the product](https://support.google.com/merchants/answer/6324405). | tddy123uk  
`benchmark_price` | `RECORD` | Average click-weighted price for a given product across all merchants who advertise that same product on Shopping ads. Products are matched based on their [GTIN](https://support.google.com/merchants/answer/6324461). For more details, see [Help Center article about the price competitiveness report](https://support.google.com/merchants/answer/9626903).  |   
`benchmark_price.amount_micros` | `INTEGER` | Price of the item, in micros (1 is represented as 1000000). | 1000000  
`benchmark_price.currency_code` | `STRING` | Currency of the price of the item. | USD  
`price` | `RECORD` | Price of this product. |   
`price.amount_micros` | `STRING` | Price of the item, in micros (1 is represented as 1000000). | 1000000  
`price.currency_code` | `INTEGER` | Currency of the price of the item. | USD  
`report_country_code` | `STRING` | Country code where the user performed the query on Google. | CH, US  
`product_type_l1` | `STRING` | [Product type attribute](https://support.google.com/merchants/answer/6324406) of the product. |   
`product_type_l2` | `STRING` | [Product type attribute](https://support.google.com/merchants/answer/6324406) of the product. |   
`product_type_l3` | `STRING` | [Product type attribute](https://support.google.com/merchants/answer/6324406) of the product. |   
`product_type_l4` | `STRING` | [Product type attribute](https://support.google.com/merchants/answer/6324406) of the product. |   
`product_type_l5` | `STRING` | [Product type attribute](https://support.google.com/merchants/answer/6324406) of the product. |   
`category_l1` | `STRING` | [Google product category](https://support.google.com/merchants/answer/6324436) of the product. | Animals & Pet Supplies  
`category_l2` | `STRING` | [Google product category](https://support.google.com/merchants/answer/6324436) of the product. | Pet Supplies  
`category_l3` | `STRING` | [Google product category](https://support.google.com/merchants/answer/6324436) of the product. | Dog Supplies  
`category_l4` | `STRING` | [Google product category](https://support.google.com/merchants/answer/6324436) of the product. | Dog Beds  
`category_l5` | `STRING` | [Google product category](https://support.google.com/merchants/answer/6324436) of the product. |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
