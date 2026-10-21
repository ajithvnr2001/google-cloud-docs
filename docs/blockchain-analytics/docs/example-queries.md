---
url: https://docs.cloud.google.com/blockchain-analytics/docs/example-queries/
title: Example queries \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:11:35.637158+00:00
---

# Example queries  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/example-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-analytics/docs/overview)



Send feedback 

#  Example queries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides general instructions on how to query Blockchain Analytics.

See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/introduction) for instructions on using BigQuery.

To build your own query:

  1. In the Google Cloud console, go to the **BigQuery** page. 

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Click **Compose a new query**.
  3. Type a query in the **Editor** field.
  4. Click **Run**.



For example, to list the total number of transactions for each day for the last six months:

  1. In the Google Cloud console, go to the **BigQuery** page. 

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Copy the following and paste it into the query box:
         
         SELECT
           TIMESTAMP_TRUNC(block_timestamp, DAY) AS timestamp1, COUNT(1) AS txn_count
         FROM
           bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions
         WHERE
           block_timestamp >= CAST(DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH) AS TIMESTAMP)
         GROUP BY timestamp1
         ORDER BY timestamp1
         

  3. Click **Run**. The following shows an example result:


**Example result**  
---  
timestamp1 | txn_count  
2023-01-10 00:00:00.000000 UTC | 1061055  
2023-01-11 00:00:00.000000 UTC | 1083178  
2023-01-12 00:00:00.000000 UTC | 1085563  
2023-01-13 00:00:00.000000 UTC | 1076328  
2023-01-14 00:00:00.000000 UTC | 1107804  
2023-01-15 00:00:00.000000 UTC | 1000777  
2023-01-16 00:00:00.000000 UTC | 1057284  
2023-01-17 00:00:00.000000 UTC | 1018353  
2023-01-18 00:00:00.000000 UTC | 1118225  
2023-01-19 00:00:00.000000 UTC | 1007125  
2023-01-20 00:00:00.000000 UTC | 1024504  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
