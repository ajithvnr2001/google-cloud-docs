---
url: https://docs.cloud.google.com/blockchain-analytics/docs/schema/
title: Dataset schemas \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:03.360944+00:00
---

# Dataset schemas  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Reference ](https://docs.cloud.google.com/blockchain-analytics/docs/schema)



Send feedback 

#  Dataset schemas Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes Blockchain Analytics table schemas. 

**Note:** All tables for Blockchain Analytics datasets use [`MONTHLY`](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#select_daily_hourly_monthly_or_yearly_partitioning) time partition on the `block_timestamp` field.

## Arbitrum One

**Deprecated:** The Arbitrum One BigQuery sharing (formerly Analytics Hub) listings in the `EU` and `US` multi-regions, including the `goog-blockchain.arbitrum_one_us` dataset, are deprecated and stop receiving updates after October 31, 2026. Use the `bigquery-public-data.goog_blockchain_arbitrum_one_us` tables listed on this page instead. For more information, see [Blockchain Analytics locations](https://docs.cloud.google.com/blockchain-analytics/docs/locations).

### Tables available for analysis

  * **[blocks](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_arbitrum_one_us!3sblocks)** : Table holding Arbitrum block data.
  * **[decoded_events](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_arbitrum_one_us!3sdecoded_events)** : Table holding decoded event data for a variety of popular Arbitrum event types.
  * **[logs](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_arbitrum_one_us!3slogs)** : Table holding Arbitrum event logs emitted during on-chain activity.
  * **[receipts](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_arbitrum_one_us!3sreceipts)** : Table holding transaction receipts, data about outcomes of transactions.
  * **[transactions](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_arbitrum_one_us!3stransactions)** : Table holding transactions which are actions initiated by externally owned accounts.

**Caution:** Addresses in the Blockchain Analytics Arbitrum dataset are indexed in all lowercase. Use [`LOWER()`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#lower) when working with mixed case addresses.

## Avalanche Contract Chain

**Deprecated:** The Avalanche Contract Chain BigQuery sharing (formerly Analytics Hub) listings in the `EU` and `US` multi-regions, including the `goog-blockchain.avalanche_contract_chain_us` dataset, are deprecated and stop receiving updates after October 31, 2026. Use the `bigquery-public-data.goog_blockchain_avalanche_contract_chain_us` tables listed on this page instead. For more information, see [Blockchain Analytics locations](https://docs.cloud.google.com/blockchain-analytics/docs/locations).

### Tables available for analysis

  * **[blocks](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_avalanche_contract_chain_us!3sblocks)** : Table holding Avalanche block data.
  * **[decoded_events](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_avalanche_contract_chain_us!3sdecoded_events)** : Table holding decoded event data for a variety of popular Avalanche event types.
  * **[logs](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_avalanche_contract_chain_us!3slogs)** : Table holding Avalanche event logs emitted during on-chain activity.
  * **[receipts](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_avalanche_contract_chain_us!3sreceipts)** : Table holding transaction receipts, data about outcomes of transactions.
  * **[transactions](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_avalanche_contract_chain_us!3stransactions)** : Table holding transactions which are actions initiated by externally owned accounts.

**Caution:** Addresses in the Blockchain Analytics Avalanche dataset are indexed in all lowercase. Use [`LOWER()`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#lower) when working with mixed case addresses.

## Cronos Mainnet

**Deprecated:** The Cronos mainnet BigQuery sharing (formerly Analytics Hub) listings in the `EU` and `US` multi-regions, including the `goog-blockchain.cronos_mainnet_us` dataset, are deprecated and stop receiving updates after October 31, 2026. Use the `bigquery-public-data.goog_blockchain_cronos_mainnet_us` tables listed on this page instead. For more information, see [Blockchain Analytics locations](https://docs.cloud.google.com/blockchain-analytics/docs/locations).

### Tables available for analysis

  * **[blocks](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_cronos_mainnet_us!3sblocks)** : Table holding Cronos block data.
  * **[decoded_events](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_cronos_mainnet_us!3sdecoded_events)** : Table holding decoded event data for a variety of popular Cronos event types.
  * **[logs](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_cronos_mainnet_us!3slogs)** : Table holding Cronos event logs emitted during on-chain activity.
  * **[receipts](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_cronos_mainnet_us!3sreceipts)** : Table holding transaction receipts, data about outcomes of transactions.
  * **[transactions](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_cronos_mainnet_us!3stransactions)** : Table holding transactions which are actions initiated by externally owned accounts.

**Caution:** Addresses in the Blockchain Analytics Cronos dataset are indexed in all lowercase. Use [`LOWER()`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#lower) when working with mixed case addresses.

## Ethereum Goerli

**Deprecated:** Goerli has reached [end-of-life](https://blog.ethereum.org/2023/11/30/goerli-lts-update) status and is no longer maintained by the Ethereum Foundation. The Ethereum Goerli BigQuery sharing (formerly Analytics Hub) listings in the `EU` and `US` multi-regions and the `goog-blockchain.ethereum_goerli_us` and `bigquery-public-data.goog_blockchain_ethereum_goerli_us` datasets are deprecated without a replacement.

### Tables available for analysis

  * **[blocks](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_goerli_us!3sblocks)** : Table holding Ethereum Goerli block data.
  * **[decoded_events](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_goerli_us!3sdecoded_events)** : Table holding decoded event data for a variety of popular Ethereum Goerli event types.
  * **[logs](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_goerli_us!3slogs)** : Table holding Ethereum Goerli event logs emitted during on-chain activity.
  * **[receipts](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_goerli_us!3sreceipts)** : Table holding transaction receipts, data about outcomes of transactions.
  * **[transactions](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_goerli_us!3stransactions)** : Table holding transactions which are actions initiated by externally owned accounts.

**Caution:** Addresses in the Blockchain Analytics Ethereum Goerli dataset are indexed in all lowercase. Use [`LOWER()`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#lower) when working with mixed case addresses.

## Ethereum Mainnet

**Deprecated:** The Ethereum mainnet BigQuery sharing (formerly Analytics Hub) listings in the `EU` and `US` multi-regions, including the `goog-blockchain.ethereum_mainnet_us` dataset, are deprecated and stop receiving updates after October 31, 2026. Use the `bigquery-public-data.goog_blockchain_ethereum_mainnet_us` tables listed on this page instead. For more information, see [Blockchain Analytics locations](https://docs.cloud.google.com/blockchain-analytics/docs/locations).

### Tables available for analysis

  * **[accounts_state](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3saccounts_state)** : Table holding account state at block heights where the account was seen transacting on-chain (excludes internal transactions).
  * **[blocks](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3sblocks)** : Table holding Ethereum block data.
  * **[decoded_events](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3sdecoded_events)** : Table holding decoded event data for a variety of popular Ethereum event types.
  * **[logs](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3slogs)** : Table holding Ethereum event logs emitted during on-chain activity.
  * **[receipts](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3sreceipts)** : Table holding transaction receipts, data about outcomes of transactions.
  * **[token_transfers](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3stoken_transfers)** : Table holding ERC-20, ERC-721, and ERC-1155 token transfers.
  * **[traces](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3straces)** : Table holding Parity-style traces which show actions executed by the EVM for some specific transaction or block reward.
  * **[transactions](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3stransactions)** : Table holding transactions which are actions initiated by externally owned accounts.

**Caution:** Addresses in the Blockchain Analytics Ethereum dataset are indexed in all lowercase. Use [`LOWER()`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#lower) when working with mixed case addresses.

### Clustered materialized views

**Important:** The following materialized views leverage [**clustering**](https://docs.cloud.google.com/bigquery/docs/clustered-tables) to improve query performance and reduce bytes scanned. We recommend issuing queries against these materialized views if your queries heavily filter on account addresses.

  * **[accounts](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3saccounts)** : Identifies accounts as externally owned accounts or smart contracts with the following schema, clustered on `address`.

Field name | BigQuery type | Description  
---|---|---  
`address` | STRING | Address identifying the account.  
`code` | STRING |  Compiled runtime bytecode of this account, given the account is a smart contract.   
`code_hash` | STRING |  Hash of the code of the account. For all externally-owned accounts this will be `0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470`. This is the hash when there is no code present.   
`is_contract` | BOOLEAN |  Whether or not this address is a smart contract. True, if the address identifies a smart contract.   
  * **[accounts_state_by_address](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3saccounts_state_by_address)** : Materialized view that has the same schema as the [**`accounts_state`**](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3saccounts_state) table and clusters the data on the **`address`** column.

  * **[transactions_by_from_address](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3stransactions_by_from_address)** : Materialized view that has the same schema as the [**`transactions`**](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3stransactions) table and clusters the data on the **`from_address`** column.

  * **[transactions_by_to_address](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3stransactions_by_to_address)** : Materialized view that has the same schema as the [**`transactions`**](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_ethereum_mainnet_us!3stransactions) table and clusters the data on the **`to_address`** column.




## Optimism Mainnet

**Deprecated:** The Optimism mainnet BigQuery sharing (formerly Analytics Hub) listings in the `EU` and `US` multi-regions, including the `goog-blockchain.optimism_mainnet_us` dataset, are deprecated and stop receiving updates after October 31, 2026. Use the `bigquery-public-data.goog_blockchain_optimism_mainnet_us` tables listed on this page instead. For more information, see [Blockchain Analytics locations](https://docs.cloud.google.com/blockchain-analytics/docs/locations).

### Tables available for analysis

  * **[blocks](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_optimism_mainnet_us!3sblocks)** : Table holding Optimism block data.
  * **[decoded_events](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_optimism_mainnet_us!3sdecoded_events)** : Table holding decoded event data for a variety of popular Optimism event types.
  * **[logs](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_optimism_mainnet_us!3slogs)** : Table holding Optimism event logs emitted during on-chain activity.
  * **[receipts](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_optimism_mainnet_us!3sreceipts)** : Table holding transaction receipts, data about outcomes of transactions.
  * **[transactions](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_optimism_mainnet_us!3stransactions)** : Table holding transactions which are actions initiated by externally owned accounts.

**Caution:** Addresses in the Blockchain Analytics Optimism dataset are indexed in all lowercase. Use [`LOWER()`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#lower) when working with mixed case addresses.

## Polygon Mainnet

**Deprecated:** The Polygon mainnet BigQuery sharing (formerly Analytics Hub) listings in the `EU` and `US` multi-regions, including the `goog-blockchain.polygon_mainnet_us` dataset, are deprecated and stop receiving updates after October 31, 2026. Use the `bigquery-public-data.goog_blockchain_polygon_mainnet_us` tables listed on this page instead. For more information, see [Blockchain Analytics locations](https://docs.cloud.google.com/blockchain-analytics/docs/locations).

### Tables available for analysis

  * **[blocks](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_polygon_mainnet_us!3sblocks)** : Table holding Polygon block data.
  * **[decoded_events](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_polygon_mainnet_us!3sdecoded_events)** : Table holding decoded event data for a variety of popular Polygon event types.
  * **[logs](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_polygon_mainnet_us!3slogs)** : Table holding Polygon event logs emitted during on-chain activity.
  * **[receipts](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_polygon_mainnet_us!3sreceipts)** : Table holding transaction receipts, data about outcomes of transactions.
  * **[transactions](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_polygon_mainnet_us!3stransactions)** : Table holding transactions which are actions initiated by externally owned accounts.

**Caution:** Addresses in the Blockchain Analytics Polygon dataset are indexed in all lowercase. Use [`LOWER()`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#lower) when working with mixed case addresses.

## Tron Mainnet

**Deprecated:** The Tron mainnet BigQuery sharing (formerly Analytics Hub) listings in the `EU` and `US` multi-regions, including the `goog-blockchain.tron_mainnet_us` dataset, are deprecated and stop receiving updates after October 31, 2026. Use the `bigquery-public-data.goog_blockchain_tron_mainnet_us` tables listed on this page instead. For more information, see [Blockchain Analytics locations](https://docs.cloud.google.com/blockchain-analytics/docs/locations).

  * **[blocks](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_tron_mainnet_us!3sblocks)** : Table holding Tron block data.
  * **[decoded_events](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_tron_mainnet_us!3sdecoded_events)** : Table holding decoded event data for a variety of popular Tron event types.
  * **[logs](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_tron_mainnet_us!3slogs)** : Table holding Tron event logs emitted during on-chain activity.
  * **[receipts](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_tron_mainnet_us!3sreceipts)** : Table holding transaction receipts, data about outcomes of transactions.
  * **[transactions](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sgoog_blockchain_tron_mainnet_us!3stransactions)** : Table holding transactions which are actions initiated by externally owned accounts.

**Caution:** Addresses in the Blockchain Analytics Tron dataset are indexed in all lowercase. Use [`LOWER()`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#lower) when working with mixed case addresses.

## BigQuery schemas

Reference the **Schema** tab of each table in BigQuery:

[![Schema tab, BigQuery](https://docs.cloud.google.com/static/blockchain-analytics/images/schema-tab.png)](https://docs.cloud.google.com/static/blockchain-analytics/images/schema-tab.png)

[![Column description,
BigQuery](https://docs.cloud.google.com/static/blockchain-analytics/images/schema-descriptions.png)](https://docs.cloud.google.com/blockchain-analytics/images/schema-descriptions.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
