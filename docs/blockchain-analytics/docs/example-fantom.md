---
url: https://docs.cloud.google.com/blockchain-analytics/docs/example-fantom/
title: Fantom example queries \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:18.955225+00:00
---

# Fantom example queries  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/example-fantom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-analytics/docs/overview)



Send feedback 

#  Fantom example queries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides Blockchain Analytics query examples for Fantom.

See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/introduction) for instructions on using BigQuery.

## View the earliest and most recently indexed block

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:7178314adf344543a494a344e146af5f)

The following query is loaded into the **Editor** field:
    
    
    SELECT
      MIN(block_number) AS `First block`,
      MAX(block_number) AS `Newest block`,
      COUNT(1) AS `Total number of blocks`
    FROM
      bigquery-public-data.goog_blockchain_fantom_opera_us.blocks;
    

**Example result** :

First block | Newest block | Total number of blocks  
---|---|---  
0 | 68125012 | 68125013  
  
## Top 10 wallets by number of transactions

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:2109b22594634ec38dd7be5fa5ec7c81)

The following query is loaded into the **Editor** field:
    
    
    SELECT 
      from_address, 
      COUNT(*) AS num_transactions 
    FROM `bigquery-public-data.goog_blockchain_fantom_opera_us.transactions`
    GROUP BY from_address
    ORDER BY num_transactions DESC
    LIMIT 10;
    

**Example result**

From Address | Num Transactions  
---|---  
0xe93685f3bba03016f02bd1828badd6195988d950 | 2278761  
0xb8ff877ed78ba520ece21b1de7843a8a57ca47cb | 1607685  
0x88888846b627c2405c4b8963e45d731b7cdda406 | 1585298  
0x26cf0b614df78bc4ec744f3703a9337a651acf74 | 1375400  
0xebf4fbb9c81b84dd5cf89bc75588e5d0018501b3 | 1306694  
0x9d945d909ca91937d19563e30bb4dac12c860189 | 847169  
0x70ecc7fecaea8d67e820035ed48c53706e7f2079 | 830320  
0x657439ed989b0ec28a09b592fda8c61ebd434b6a | 806376  
0x9d7593003c0d48014a38be07ca8c312e6d32f17d | 804562  
0xd968665350a0bb7d487aadba94d920d8890ee06f | 804225  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
