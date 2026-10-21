---
url: https://docs.cloud.google.com/bigquery/docs/merchant-center-query-your-data/
title: Query your Google Merchant Center Transfers data \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:09:47.860971+00:00
---

# Query your Google Merchant Center Transfers data  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/merchant-center-query-your-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query your Google Merchant Center Transfers data

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When your data is transferred to BigQuery, the data is written to ingestion-time partitioned tables. For more information, see [Introduction to partitioned tables](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).

When you query your Google Merchant Center table, you must use the `_PARTITIONTIME` or `_PARTITIONDATE` pseudocolumn in your query. For more information, see [Querying partitioned tables](https://docs.cloud.google.com/bigquery/docs/querying-partitioned-tables).

The `Products_` table contains nested and repeated fields. For information on handling nested and repeated data, see [Differences in repeated field handling](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/migrating-from-legacy-sql#differences_in_repeated_field_handling) in the GoogleSQL documentation.

## Google Merchant Center sample queries

You can use the following Google Merchant Center sample queries to analyze your transferred data. You can also use the queries in a visualization tool such as [Data Studio](https://www.google.com/analytics/data-studio/).

In each of the following queries, replace dataset with your dataset name. Replace merchant_id with your Merchant ID. If you're using an MCA, replace merchant_id with your MCA ID.

### Products and product issues statistics

The following SQL sample query provides the number of products, products with issues, and issues by day.
    
    
    SELECT
      _PARTITIONDATE AS date,
      COUNT(*) AS num_products,
      COUNTIF(ARRAY_LENGTH(issues) > 0) AS num_products_with_issues,
      SUM(ARRAY_LENGTH(issues)) AS num_issues
    FROM
      dataset.Products_merchant_id
    WHERE
      _PARTITIONDATE >= 'YYYY-MM-DD'
    GROUP BY
      date
    ORDER BY
      date DESC

### Products disapproved for Shopping Ads

The following SQL sample query provides the number of products that are not approved for display in Shopping Ads, separated by country. Disapproval can result from the destination being [excluded](https://support.google.com/merchants/answer/6324486) or because of an issue with the product.
    
    
    SELECT
      _PARTITIONDATE AS date,
      disapproved_country,
      COUNT(*) AS num_products
    FROM
      dataset.Products_merchant_id,
      UNNEST(destinations) AS destination,
      UNNEST(disapproved_countries) AS disapproved_country
    WHERE
      _PARTITIONDATE >= 'YYYY-MM-DD'
    GROUP BY
      date, disapproved_country
    ORDER BY
      date DESC

### Products with disapproved issues

The following SQL sample query retrieves the number of products with disapproved issues, separated by country.
    
    
    SELECT
      _PARTITIONDATE AS date,
      applicable_country,
      COUNT(DISTINCT CONCAT(CAST(merchant_id AS STRING), ':', product_id))
          AS num_distinct_products
    FROM
      dataset.Products_merchant_id,
      UNNEST(issues) AS issue,
      UNNEST(issue.applicable_countries) as applicable_country
    WHERE
      _PARTITIONDATE >= 'YYYY-MM-DD' AND
      issue.servability = 'disapproved'
    GROUP BY
      date, applicable_country
    ORDER BY
      date DESC

**Note:** This query constructs a unique key by using `merchant_id` and `product_id`. This is only required if you have an MCA account. When you use an MCA account, there is the potential for `product_id` collisions across multiple sub-accounts.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
