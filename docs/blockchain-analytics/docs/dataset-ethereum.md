---
url: https://docs.cloud.google.com/blockchain-analytics/docs/dataset-ethereum/
title: Blockchain Analytics Ethereum dataset \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:35.860949+00:00
---

# Blockchain Analytics Ethereum dataset  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/dataset-ethereum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)



Send feedback 

#  Blockchain Analytics Ethereum dataset Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Ethereum

There are some notable differences between the datasets which can be used together:

Feature |  [ Blockchain Analytics dataset](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2sblockchain_analytics_ethereum_mainnet_us) |  [ Ethereum public dataset](https://console.cloud.google.com/bigquery?mods=logs_tg_staging&ws=!1m4!1m3!3m2!1sbigquery-public-data!2scrypto_ethereum)  
---|---|---  
**Raw data:** Comprehensive raw data including every object in every block.  |  |   
**Lossless values:** Decimal number represented as a STRING to preserve full numeric precision of UINT256 decimal numbers, e.g. "42.9999999".  |    
In addition to providing the [lossless](https://docs.cloud.google.com/blockchain-analytics/docs/terms#lossless) string values and the [lossy](https://docs.cloud.google.com/blockchain-analytics/docs/terms#lossy) numeric value, we provide functions that allow you to query the lossless values as numbers.  |  |  **ETH balances:** Ether balances for all externally owned addresses that have sent or received ether.  |    
Higher granularity at per-block level.  |  |  **Contract classification:** Labels for contracts that adhere to EIP standards such as [ ERC-20](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/), [ ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/), and [ ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/).  | construction   
Work in progress for GA release  |  |  **Token transfers:** Token transfer transactions are identified for easy computation of current and historical balances. |    
In addition to ERC-20 transfers, we also provide decoded ERC-721 and ERC-1155 transfer events.  |  |  **Token balances:** Token balances for all externally owned addresses. | construction   
Work in progress for GA release |  | **Event Decoding:** Decoded values for popular contract events. |  |  | **Data freshness:** Duration of time that measures when data is seen on-chain to when it is available for query. |  On average 12 minutes, or 64 blocks, behind latest. This is the standard time for [**finalized**](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/#finality) **commitment** and reduces the chance of the data being subject to a chain re-org.  |  On average 4 minutes, or 20 blocks, behind latest. 

## What's next for the Ethereum dataset?

Beyond raw blockchain data, we'll provide derived data that makes querying and understanding the data simple.

  * **Contract classification:** By analyzing transactions for a specific contract, it's possible to determine whether that contract conforms to an ERC standard. Specifically we aim to classify whether a contract is [ERC-20](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/), [ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/), or [ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/). This classification allows users to focus their analysis on tokens.
  * **Token balances:** Once we have classified contracts, we'll then compute balances for each wallet. This will allow you to better understand what kind and how many assets a particular wallet has without doing the manual computation on your own.

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-13 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
