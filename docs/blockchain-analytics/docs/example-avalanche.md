---
url: https://docs.cloud.google.com/blockchain-analytics/docs/example-avalanche/
title: Avalanche example queries \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:34.355799+00:00
---

# Avalanche example queries  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/example-avalanche/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-analytics/docs/overview)



Send feedback 

#  Avalanche example queries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides Blockchain Analytics query examples for Avalanche.

See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/introduction) for instructions on using BigQuery.

## View the first and last block indexed

This query tells you how fresh the data is.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:f135e42cd4a041d9a272b935436c474f)

The following query is loaded into the **Editor** field:
    
    
    SELECT
      MIN(block_number) AS `First block`,
      MAX(block_number) AS `Newest block`,
      COUNT(1) AS `Total number of blocks`
    FROM
      bigquery-public-data.goog_blockchain_avalanche_contract_chain_us.blocks;
    

The following shows an example result:

**Example result**  
---  
First block | Newest block | Total number of blocks  
0 | 35145353 | 35144883  
  
## View the blocks with largest AVAX value transfer

This query shows you which blocks had the largest total value of AVAX transferred between accounts. It only counts successful transactions.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:97243666e96b4504bdb3c9ae4085c782)

The following query is loaded into the **Editor** field:
    
    
    SELECT block_hash, SUM(value.bignumeric_value / 1000000000000000000) value_total
    FROM `bigquery-public-data.goog_blockchain_avalanche_contract_chain_us.transactions`
      JOIN `bigquery-public-data.goog_blockchain_avalanche_contract_chain_us.receipts` USING (block_hash, transaction_hash)
    WHERE status = 1
    GROUP BY block_hash
    ORDER BY value_total DESC
    LIMIT 5
    

The following shows an example result:

**Example result**  
---  
block_hash | value_total  
0xb7fd57885ff93e1bfdb1976a09a8a24a6dd51720ede2a89ec7d4730753a6dd7b | 3000000.436603689536241393  
0x1c5cc5e1a5eb9d154e3f2e034d7eab21255ea0025a36c8efaac2c3c8ccd0825f | 2918908.4828071  
0xf39246ef10fa86e30c9e31b7213384548bed7709bd3648d419bae9368d35cd43 | 2858755.74711697255864143  
0xd840777af617fd998dfb576bd334eb19f4d5f93a7e470e65fb064fa5ed047565 | 2463896.227593705442089976  
0x5e5fd196b53b5aa9f027bb5bb2804d6940892a5b09017a779c06542f17a38475 | 2213537.345616222964672662  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
