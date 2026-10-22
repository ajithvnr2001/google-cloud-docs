---
url: https://docs.cloud.google.com/bigquery/docs/merchant-center-top-brands-schema/
title: Google Merchant Center top brands table \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:04.413899+00:00
---

# Google Merchant Center top brands table  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/merchant-center-top-brands-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Merchant Center top brands table

## Overview

**Caution:** BigQuery will no longer support the report that exports the Top brands table on September 1, 2025. We recommend that you migrate to use the [new best sellers report](https://docs.cloud.google.com/bigquery/docs/merchant-center-best-sellers-schema) instead.

Best sellers data helps merchants understand the most popular brands and products in Shopping ads and unpaid listings. For more information about best sellers, see the description in [Supported reports](https://docs.cloud.google.com/bigquery/docs/merchant-center-transfer#supported_reports).

The data is written to a table named `BestSellers_TopBrands_MERCHANT_ID`.

## Schema

The `BestSellers_TopBrands_` table has the following schema:

**Column** | **BigQuery data type** | **Description** | **Example data**  
---|---|---|---  
`rank_timestamp` | `TIMESTAMP` | Date and time when the rank was published. | 2020-05-30 00:00:00 UTC  
`rank_id` | `STRING` | Unique identifier for the rank. | 2020-05-30:FR:264:120:brand  
`rank` | `INTEGER` | The popularity rank of the brand on Shopping ads and unpaid listings for the `ranking_country` and `ranking_category`. Popularity is based on the estimated number of products sold. The rank updates daily. The data included in metrics might be delayed by up 2 days.  | 120  
`previous_rank` | `INTEGER` | The change in rank over the previous 7 days. | 86  
`ranking_country` | `STRING` | Country code used for ranking. | FR  
`ranking_category` | `INTEGER` | [Google product category ID](https://support.google.com/merchants/answer/1705911) used for ranking. | 264  
`ranking_category_path` | `RECORD, REPEATED` | The full path of the [Google product category](https://support.google.com/merchants/answer/1705911) used for ranking in each locale. |   
`ranking_category_path.locale` | `STRING` | The locale of the category path. | en-US  
`ranking_category_path.name` | `STRING` | A human-readable name for the category path. | Electronics > Communications > Telephony > Mobile Phone Accessories  
`relative_demand` | `RECORD` | A brand's estimated demand in relation to the brand with the highest popularity rank in the same category and country. |   
`relative_demand.bucket` | `STRING` |  | Very high  
`relative_demand.min` | `INTEGER` |  | 51  
`relative_demand.max` | `INTEGER` |  | 100  
`previous_relative_demand` | `RECORD` | A brand's estimated demand in relation to the brand with the highest popularity rank in the same category and country over the previous 7 days.  |   
`previous_relative_demand.bucket` | `STRING` |  | Very high  
`previous_relative_demand.min` | `INTEGER` |  | 51  
`previous_relative_demand.max` | `INTEGER` |  | 100  
`brand` | `STRING` | Brand of the item. | Example Brand Name  
`google_brand_id` | `STRING` | Google brand ID of the item. | 11887454107284768325  
  
## Query examples

### Top brands for a given category and country

The following SQL query returns top brands for the `Smartphones` category in the US.
    
    
    SELECT
      rank,
      previous_rank,
      brand
    FROM
      dataset.BestSellers_TopBrands_merchant_id
    WHERE
      _PARTITIONDATE = 'YYYY-MM-DD' AND
      ranking_category = 267 /*Smartphones*/ AND
      ranking_country = 'US'
    ORDER BY
      rank

**Note:** For more information about product categories, including a full list of category codes, see [Definition: `google_product_category`](https://support.google.com/merchants/answer/6324436).

### Products of top brands in your inventory

The following SQL query returns a list of products in your inventory from top brands, listed by category and country.
    
    
      WITH latest_top_brands AS
      (
        SELECT
          *
        FROM
          dataset.BestSellers_TopBrands_merchant_id
        WHERE
          _PARTITIONDATE = 'YYYY-MM-DD'
      ),
      latest_products AS
      (
        SELECT
          product.*,
          product_category_id
        FROM
          dataset.Products_merchant_id AS product,
          UNNEST(product.google_product_category_ids) AS product_category_id,
          UNNEST(destinations) AS destination,
          UNNEST(destination.approved_countries) AS approved_country
        WHERE
          _PARTITIONDATE = 'YYYY-MM-DD'
      )
      SELECT
        top_brands.brand,
        (SELECT name FROM top_brands.ranking_category_path
        WHERE locale = 'en-US') AS ranking_category,
        top_brands.ranking_country,
        top_brands.rank,
        products.product_id,
        products.title
      FROM
        latest_top_brands AS top_brands
      INNER JOIN
        latest_products AS products
      ON top_brands.google_brand_id = products.google_brand_id AND
         top_brands.ranking_category = product_category_id AND
         top_brands.ranking_country = products.approved_country

**Note:** For more information about product categories, including a full list of category codes, see [Definition: `google_product_category`](https://support.google.com/merchants/answer/6324436).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
