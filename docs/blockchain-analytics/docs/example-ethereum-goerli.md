---
url: https://docs.cloud.google.com/blockchain-analytics/docs/example-ethereum-goerli/
title: Ethereum Goerli example queries \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:18.383906+00:00
---

# Ethereum Goerli example queries  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/example-ethereum-goerli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-analytics/docs/overview)



Send feedback 

#  Ethereum Goerli example queries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides Blockchain Analytics query examples for Ethereum Goerli.

See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/introduction) for instructions on using BigQuery.

**Warning:** Goerli has reached [end-of-life](https://blog.ethereum.org/2023/11/30/goerli-lts-update) status and is no longer maintained by the Ethereum Foundation.

## Average daily transactions count drop since announcement of Goerli deprecation

This query looks at the drop in average daily transactions on Goerli once it was announced on April 1, 2023 that the Goerli testnet would be deprecated in favor of the Sepolia and Holesky testnets.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:4eb0dbcc17194464b963a8cc2d8d4d2f)

The following query is loaded into the **Editor** field:
    
    
     # Average daily transactions count drop since announcement of Goerli
     # deprecation (two weeks around Apr 1st, 2023) In favor of new Sepolia chain
    SELECT
     DATE(block_timestamp) AS date,
     COUNT(*) AS num_transactions
    FROM
     `bigquery-public-data.goog_blockchain_ethereum_goerli_us.transactions`
    WHERE
     block_timestamp >= TIMESTAMP('2023-03-24')
     AND block_timestamp <= TIMESTAMP('2023-04-08')
    GROUP BY
     1
    ORDER BY
     1 DESC;
    

The following shows an example result:

Date | Number of Transactions  
---|---  
2023-04-08 | 80  
2023-04-07 | 633,348  
2023-04-06 | 530,415  
2023-04-05 | 485,717  
2023-04-04 | 478,859  
2023-04-03 | 493,144  
2023-04-02 | 514,925  
2023-04-01 | 460,480  
2023-03-31 | 524,960  
2023-03-30 | 532,627  
2023-03-29 | 596,644  
2023-03-28 | 555,764  
2023-03-27 | 541,082  
2023-03-26 | 550,949  
2023-03-25 | 541,940  
2023-03-24 | 591,707  
  
## Daily transaction count for the last 7 days

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:77288257cada4c52868e3ddd48b61d22)

The following query is loaded into the **Editor** field:
    
    
    SELECT
      DATE(block_timestamp) AS date,
      COUNT(*) AS num_transactions
    FROM
      `bigquery-public-data.goog_blockchain_ethereum_goerli_us.transactions`
    WHERE
      block_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 10 DAY)
    GROUP BY
      1
    ORDER BY
      1 DESC;
    

The following shows an example result:

date | num_transactions  
---|---  
2023-09-08 | 181766  
2023-09-07 | 278809  
2023-09-06 | 209469  
2023-09-05 | 265245  
2023-09-04 | 260391  
2023-09-03 | 240675  
2023-09-02 | 243579  
2023-09-01 | 220796  
2023-08-31 | 216822  
2023-08-30 | 208608  
2023-08-29 | 52474  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
