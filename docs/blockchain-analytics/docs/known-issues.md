---
url: https://docs.cloud.google.com/blockchain-analytics/docs/known-issues/
title: Blockchain Analytics known issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:14.659020+00:00
---

# Blockchain Analytics known issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Resources ](https://docs.cloud.google.com/blockchain-analytics/docs/resources)



Send feedback 

#  Blockchain Analytics known issues Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page lists Blockchain Analytics known issues and workarounds. For a list of bugs, new features, and other release information, see [Release notes](https://docs.cloud.google.com/blockchain-analytics/docs/release-notes).

To filter this page, do one or more of the following: select a category, type a search term, or click a column heading to sort.

Select categoryAvalancheEthereumFantomOptimismTron

Category | Subject | Description  
---|---|---  
Ethereum | Accounts data | 

  * The `accounts_state` table stores data about accounts seen in the `to` or `from` position of transactions initiated by externally owned accounts. Today, Blockchain Analytics does not compute mutations to account state as a result of internal transactions (transactions between smart contracts). 
  * The `accounts_state` table shows a static _snapshot_ of all accounts seen on-chain from the genesis block to block 17,399,999, including block 17,399,999. Starting from block 17,400,00, Blockchain Analytics adds a new row to the `accounts_state` table every time an account is observed participating in a transaction initiated by an externally owned account. 
  * The `accounts_state` table does not hold storage state and storage proofs for smart contracts. 

  
Avalanche  
Ethereum  
Fantom  
Optimism  
Tron | Addresses |  Because Blockchain Analytics indexes addresses as returned by the upstream node's JSON-RPC API, addresses in Blockchain Analytics datasets are indexed in all lowercase.  Use [ `LOWER()`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#lower) when working with mixed case addresses.  For example:
    
    
    SELECT
      *
    FROM
      bigquery-public-data.blockchain_analytics_ethereum_mainnet_us.transactions
    WHERE
      to_address = LOWER("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
    AND
      block_number = 17641663;  
  
Ethereum | Data freshness |  Blockchain Analytics indexes Ethereum upon finalized commitment. The indexer waits for majority two-thirds validation from Ethereum validators before indexing data. Because of this, data is typically two epochs (or 64 slots) behind the latest block. This is roughly 12 - 15 minutes behind latest.   
Polygon | Data freshness |  The Polygon data will remain approximately 24 hours behind the tip-of-chain.   
Ethereum | Traces |  Blockchain Analytics indexes and normalizes Ethereum traces to Parity-style traces.   
Avalanche  
Ethereum  
Fantom  
Optimism  
Tron | UINT256 |  To perform lossless UINT256 computation, usage of UDFs is required. UDFs are subject to quote limit, rate limit and time-outs as described in [ User-defined functions, Limitations](https://docs.cloud.google.com/bigquery/docs/user-defined-functions#limitations).   
Avalanche  
Fantom  
Optimism  
Tron | Missing transaction receipts |  Affected chains may be missing rows from the transaction receipts table. This currently affects < 0.1% of all transactions per chain.   
Avalanche  
Fantom  
Optimism  
Tron |  Table partitioning and clustering  |  Tables for affected chains are not partitioned. Tables are clustered by columns used to form the primary key for the table. Refer to `Table Info` for each table.  ![BigQuery table info. Click to enlarge image.](https://docs.cloud.google.com/static/blockchain-analytics/images/table-info.png)![](https://docs.cloud.google.com/static/blockchain-analytics/images/table-info.png)  
Avalanche  
Ethereum  
Fantom  
Optimism  
Tron | Schema consistency across chains |  Datasets for all chains have the following tables:

  * Blocks
  * Transactions
  * Receipts
  * Logs

Tables in the Avalanche, Fantom, Optimism, and Tron datasets share the same table schemas.  The Ethereum dataset includes additional tables and slight schema differences from Avalanche, Fantom, Optimism, and Tron.  All tables in the Ethereum dataset include the block timestamp column.  Refer to the [ schemas page](https://docs.cloud.google.com/blockchain-analytics/docs/schema) for more information.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


