---
url: https://docs.cloud.google.com/bigquery/docs/merchant-center-top-products-schema/
title: Google Merchant Center top products \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:52:37.630450+00:00
---

# Google Merchant Center top products  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/merchant-center-top-products-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Merchant Center top products

## Overview

**Caution:** BigQuery will no longer support this version of the Top products table on September 1, 2025. We recommend that you migrate to use the [new best sellers report](https://docs.cloud.google.com/bigquery/docs/merchant-center-best-sellers-schema) instead.

Best sellers data helps merchants understand the most popular brands and products in Shopping ads. For more information about best sellers, see the description in [Supported Reports](https://docs.cloud.google.com/bigquery/docs/merchant-center-transfer#supported_reports).

The data is written to a table named `BestSellers_TopProducts_MERCHANT_ID`.

## Schema

The `BestSellers_TopProducts_` table has the following schema:

**Column** | **BigQuery data type** | **Description** | **Sample field**  
---|---|---|---  
`rank_timestamp` | `TIMESTAMP` | Date and time when the rank was published. | 2020-03-14 00:00:00 UTC  
`rank_id` | `STRING` | Rank identifier to join against the [Product Inventory](https://docs.cloud.google.com/bigquery/docs/merchant-center-product-inventory-schema) table. | 2020-03-14:AU:100:2:product  
`rank` | `INTEGER` | The popularity rank of the product on Shopping ads for the `ranking_country` and `ranking_category`. Popularity is based on the estimated number of products sold. The rank updates daily. The data included in metrics might be delayed by up 2 days. | 2  
`previous_rank` | `INTEGER` | The change in rank over the previous 7 days. | 4  
`ranking_country` | `STRING` | Country code used for ranking. | AU  
`ranking_category` | `INTEGER` | [Google product category](https://support.google.com/merchants/answer/1705911) ID used for ranking. | 5181  
`ranking_category_path` | `RECORD,  
REPEATED` | [Google product category](https://support.google.com/merchants/answer/1705911) full path for each locale used for ranking. |   
`ranking_category_path.locale` | `STRING` |  | en-AU  
`ranking_category_path.name` | `STRING` |  | Luggage & Bags  
`relative_demand` | `RECORD` | A product's estimated demand in relation to the product with the highest popularity rank in the same category and country. |   
`relative_demand.bucket` | `STRING` |  | Very high  
`relative_demand.min` | `INTEGER` |  | 51  
`relative_demand.max` | `INTEGER` |  | 100  
`previous_relative_demand` | `RECORD` | A product's estimated demand in relation to the product with the highest popularity rank in the same category and country over the previous 7 days. |   
`previous_relative_demand.bucket` | `STRING` |  | Very high  
`previous_relative_demand.min` | `INTEGER` |  | 51  
`previous_relative_demand.max` | `INTEGER` |  | 100  
`product_title` | `RECORD,  
REPEATED` | Product title. |   
`product_title.locale` | `STRING` |  | en-AU  
`product_title.name` | `STRING` |  | ExampleBrand Backpack  
`gtins` | `STRING,  
REPEATED` | [Global Trade Item Number](https://support.google.com/merchants/answer/188494#gtin) (GTIN). | 07392158680955  
`brand` | `STRING` | Brand of the item. | ExampleBrand  
`google_brand_id` | `STRING` | Google brand ID of the item. | 11887454107284768328  
`google_product_category` | `INTEGER` | [Google product category](https://support.google.com/merchants/answer/1705911) ID of the item. | 100  
`google_product_category_path` | `RECORD,  
REPEATED` | [Google product category](https://support.google.com/merchants/answer/1705911) full path of the item. |   
`google_product_category_path.locale` | `STRING` |  | en-US  
`google_product_category_path.name` | `STRING` |  | Luggage & Bags > Backpacks  
`price_range` | `RECORD` | Price range: lower and upper (with no decimals) and currency. The price does not include shipping costs. | n/a  
`price_range.min` | `NUMERIC` |  | 115  
`price_range.max` | `NUMERIC` |  | 147  
`price_range.currency` | `STRING` |  | AUD  
  
## Understanding the data

  * Ranking categories are subject to change over time.
  * The [Google product category](https://support.google.com/merchants/answer/6324436) in the `BestSellers_TopProducts_Inventory_` table might be different from the Google Product Category in the [`Products_`](https://docs.cloud.google.com/bigquery/docs/merchant-center-products-schema) table. The `Products_` table surfaces a retailer provided value of Google product category.
  * For products in your inventory, the price range in `BestSellers_TopProducts_` might differ from the `Products_PriceBenchmarks_` table. Price benchmarks metrics are calculated over a different time period. The price ranges in `BestSellers_TopProducts_` reflect prices of different variants of the product, whereas the price ranges in `Products_PriceBenchmarks_` only refer to a single variant.
  * Some products in your inventory might not have a rank for each category in the path. We limit the number of products per category to 10,000, and in some sub-categories we don't publish any ranking.



## Example

Products might have a rank for each category within the product category path. For example, a Google Pixel 4 phone is classified as `Electronics > Communications > Telephony > Mobile Phones`. The Pixel 4 will have a separate ranking for Electronics, Communications, Telephony, and Mobile Phones. Use `ranking_category_path` in addition to `ranking_country` to determine the depth of category that you want to see a ranking for.

In the example below, an ExampleBrand Backpack contains a separate ranking for both the Luggage & Bags and Backpacks categories. Select "Backpacks" and "AU" to see what its ranking is in Australia in the Backpacks category.

### Ranking for Luggage & Bags

**product_title** | **ExampleBrand Backpack**  
---|---  
**ranking_country** | AU  
**ranking_category** | 5181  
**ranking_category_path** | Luggage & Bags  
**Rank** | 40  
**google_product_category** | 100  
**google_product_category_path** | Luggage & Bags > Backpacks  
  
### Ranking for Luggage & Bags > Backpacks

**product_title** | **ExampleBrand Backpack**  
---|---  
**ranking_country** | AU  
**ranking_category** | 100  
**ranking_category_path** | Luggage & Bags > Backpacks  
**rank** | 4  
**google_product_category** | 100  
**google_product_category_path** | Luggage & Bags > Backpacks  
  
## Query examples

### Top products for a given category and country

The following SQL query returns top products for the `Smartphones` category in the US.
    
    
    SELECT
      rank,
      previous_rank,
      relative_demand.bucket,
      (SELECT name FROM top_products.product_title WHERE locale = 'en-US') AS product_title,
      brand,
      price_range
    FROM
      dataset.BestSellers_TopProducts_merchant_id AS top_products
    WHERE
      _PARTITIONDATE = 'YYYY-MM-DD' AND
      ranking_category = 267 /*Smartphones*/ AND
      ranking_country = 'US'
    ORDER BY
      rank

**Note:** For more information about product categories, including a full list of category codes, see [Definition: `google_product_category`](https://support.google.com/merchants/answer/6324436).

### Top products in your inventory

The following SQL query joins `BestSellers_TopProducts_Inventory_` and `BestSellers_TopProducts_` data to return a list of top products you have in your inventory.
    
    
    WITH latest_top_products AS
    (
      SELECT
        *
      FROM
        dataset.BestSellers_TopProducts_merchant_id
      WHERE
        _PARTITIONDATE = 'YYYY-MM-DD'
    ),
    latest_top_products_inventory AS
    (
      SELECT
        *
      FROM
        dataset.BestSellers_TopProducts_Inventory_merchant_id
      WHERE
        _PARTITIONDATE = 'YYYY-MM-DD'
    )
    SELECT
      top_products.rank,
      inventory.product_id,
      (SELECT ANY_VALUE(name) FROM top_products.product_title) AS product_title,
      top_products.brand,
      top_products.gtins
    FROM
      latest_top_products AS top_products
    INNER JOIN
      latest_top_products_inventory AS inventory
    USING (rank_id)

**Note:** For more information about product categories, including a full list of category codes, see [Definition: `google_product_category`](https://support.google.com/merchants/answer/6324436).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
