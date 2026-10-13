---
url: https://docs.cloud.google.com/bigquery/docs/merchant-center-price-benchmarks-schema/
title: Google Merchant Center price benchmarks table \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:06.358718+00:00
---

# Google Merchant Center price benchmarks table  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/merchant-center-price-benchmarks-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Merchant Center price benchmarks table

## Overview

**Caution:** BigQuery will no longer support the Price Benchmarks report on September 1, 2025. We recommend that you migrate to use the [Price Competitiveness report](https://docs.cloud.google.com/bigquery/docs/merchant-center-price-competitiveness-schema) instead.

Price Benchmarks data in BigQuery helps merchants understand how other merchants are pricing the same product. When your Google Merchant Center reporting data is transferred to BigQuery, the format of the `Products_PriceBenchmarks_` table provides a daily price benchmark per country and per product.

The data is written to a table named `Products_PriceBenchmarks_MERCHANT_ID` if you are using an individual Merchant ID, or `Products_PriceBenchmarks_AGGREGATOR_ID` if you're using an MCA account.

## Schema

The `Products_PriceBenchmarks` table has the following schema:

Column | BigQuery data type | Description  
---|---|---  
`**product_id**` | `STRING` | Content API's REST ID of the product in the form: `channel:content_language:feed_label:offer_id`, similar to the way it's defined in the [products table schema](https://docs.cloud.google.com/bigquery/docs/merchant-center-products-schema). This field is a primary key.   
`merchant_id` | `INTEGER` | Merchant account ID.  
`aggregator_id` | `INTEGER` | Aggregator account ID for multi-client accounts.  
`country_of_sale` | `STRING` | Country where the user performed the query on Google.  
`price_benchmark_value` | `FLOAT` | The average click-weighted price for a given product across all merchants who advertise that same product on Shopping ads. Products are matched based on their GTIN. For more details, see the [Help Center article](https://support.google.com/merchants/answer/9626903).   
`price_benchmark_currency` | `STRING` | Currency of the benchmark value.  
`price_benchmark_timestamp` | `DATETIME` | Timestamp of the benchmark.  
  
## Example: compare product prices to benchmarks

The following SQL query joins `Products` and `Price Benchmarks` data to return the list of products and associated benchmarks.
    
    
    WITH products AS
    (
      SELECT
        _PARTITIONDATE AS date,
        *
      FROM
        dataset.Products_merchant_id
      WHERE
       _PARTITIONDATE >= 'YYYY-MM-DD'
    ),
    benchmarks AS
    (
      SELECT
        _PARTITIONDATE AS date,
        *
      FROM
        dataset.Products_PriceBenchmarks_merchant_id
      WHERE
        _PARTITIONDATE >= 'YYYY-MM-DD'
    )
    SELECT
      products.date,
      products.product_id,
      products.merchant_id,
      products.aggregator_id,
      products.price,
      products.sale_price,
      benchmarks.price_benchmark_value,
      benchmarks.price_benchmark_currency,
      benchmarks.country_of_sale
    FROM
      products
    INNER JOIN
      benchmarks
    ON products.product_id = benchmarks.product_id AND
       products.merchant_id = benchmarks.merchant_id AND
       products.date = benchmarks.date

Notes on joining the data:   
1\. Not all products have benchmarks, so use INNER JOIN or LEFT JOIN accordingly.   
2\. Each product may have multiple benchmarks (one per country). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
