---
url: https://docs.cloud.google.com/blockchain-analytics/docs/example-polygon/
title: Polygon Mainnet example queries \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:18.911774+00:00
---

# Polygon Mainnet example queries  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/example-polygon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-analytics/docs/overview)



Send feedback 

#  Polygon Mainnet example queries Stay organized with collections  Save and categorize content based on your preferences. 

This page provides Blockchain Analytics query examples for Polygon Mainnet.

See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/introduction) for instructions on using BigQuery.

## View the earliest and most recently indexed block

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:5893450501c0464faf9e9c511432353a)

The following query is loaded into the **Editor** field:
    
    
    SELECT
      MIN(block_number) AS `First block`,
      MAX(block_number) AS `Newest block`,
      COUNT(1) AS `Total number of blocks`
    FROM
      bigquery-public-data.goog_blockchain_polygon_mainnet_us.blocks;
    

The following shows an example result:

First Block | Newest Block  
---|---  
0 | 54794165  
  
## Calculate TPS (transactions per second) by month on Polygon mainnet

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:c72953cdf4f64699934c8d467de1e718)

The following query is loaded into the **Editor** field:
    
    
    SELECT
      COUNT(*) AS TXN_COUNT_PER_MONTH,
      COUNT(*) / 2592000.0 AS TXN_PER_SECOND, # seconds in a month
      EXTRACT(YEAR
      FROM
        txn.block_timestamp) AS YEAR,
      EXTRACT(MONTH
      FROM
        txn.block_timestamp) AS MONTH,
    FROM
      `bigquery-public-data.goog_blockchain_polygon_mainnet_us.transactions` AS txn
    GROUP BY
      EXTRACT(YEAR
      FROM
        txn.block_timestamp),
      EXTRACT(MONTH
      FROM
        txn.block_timestamp)
    ORDER BY TXN_COUNT_PER_MONTH DESC;
    

The following shows an example result:

TXN_COUNT_PER_MONTH | TXN_PER_SECOND | YEAR | MONTH  
---|---|---|---  
113,037,832 | 43.610274691358022 | 2024 | 2  
103,680,742 | 40.0002862654321 | 2024 | 1  
82,598,612 | 31.866748456790123 | 2024 | 3  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
