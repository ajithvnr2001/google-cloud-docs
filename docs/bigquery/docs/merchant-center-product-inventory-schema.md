---
url: https://docs.cloud.google.com/bigquery/docs/merchant-center-product-inventory-schema/
title: Google Merchant Center product inventory table \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:26.770944+00:00
---

# Google Merchant Center product inventory table  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/merchant-center-product-inventory-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Merchant Center product inventory table

## Overview

**Caution:** BigQuery will no longer support the report that exports the Product Inventory table on September 1, 2025. We recommend that you migrate to use the [new best sellers report](https://docs.cloud.google.com/bigquery/docs/merchant-center-best-sellers-schema) instead.

Best sellers data helps merchants understand the most popular brands and products in Shopping ads and unpaid listings. For more information about best sellers, see the description in [Supported reports](https://docs.cloud.google.com/bigquery/docs/merchant-center-transfer#supported_reports).

The data is written to a table named `BestSellers_TopProducts_Inventory_MERCHANT_ID`.

## Schema

The `BestSellers_TopProducts_Inventory_` table has the following schema:

**Column** | **BigQuery data type** | **Description**  
---|---|---  
`rank_id` | `STRING` | Rank identifier to join against the [Top Products](https://docs.cloud.google.com/bigquery/docs/merchant-center-top-products-schema) table  
`product_id` | `STRING` | Content API's REST ID of the product in the form `channel:content_language:feed_label:offer_id`.  
`merchant_Id` | `INTEGER` | Merchant account ID.  
`aggregator_id` | `INTEGER` | Aggregator account ID for multi-client accounts.  
  
## Example

The example below demonstrates how the `BestSellers_TopProducts_Inventory_` table provides a mapping to your products for all target countries in the `Products_` table.

**Top Products**

**product_title** | **rank_id:** | **ranking_country** | **ranking_category** | **rank**  
---|---|---|---|---  
Example Backpack | 2020-03-14:AU:5181:40:product | AU | 5181 | 40  
  
**Product inventory table**

**rank_id** | **product_id**  
---|---  
2020-03-14:AU:5181:40:product | online:en:AU:666840730  
2020-03-14:AU:5181:40:product | online:en:AU:666840730  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
