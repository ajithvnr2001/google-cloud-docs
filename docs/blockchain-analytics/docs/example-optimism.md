---
url: https://docs.cloud.google.com/blockchain-analytics/docs/example-optimism/
title: Optimism example queries \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:19.024382+00:00
---

# Optimism example queries  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/example-optimism/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-analytics/docs/overview)



Send feedback 

#  Optimism example queries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides Blockchain Analytics query examples for Optimism.

See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/introduction) for instructions on using BigQuery.

## View the earliest and most recently indexed block

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:bb161caf40844b0cb9a23129783496b0)

The following query is loaded into the **Editor** field:
    
    
    SELECT
      MIN(block_number) AS `First block`,
      MAX(block_number) AS `Newest block`,
      COUNT(1) AS `Total number of blocks`
    FROM
      bigquery-public-data.goog_blockchain_optimism_mainnet_us.blocks;
    

**Example result** :

First block | Newest block | Total number of blocks  
---|---|---  
0 | 109516624 | 109516625  
  
## View L1 assets bridged to Optimism via the Optimism Standard Bridge

This query shows how to find finalized deposit events logs for L1 assets that were bridged to Optimism using the official [Optimism Standard Bridge](https://community.optimism.io/docs/developers/bridge/standard-bridge/). The Optimism Standard Bridge supports bridging native Ether and [certain ERC-20 tokens](https://static.optimism.io/optimism.tokenlist.json) from Ethereum to Optimism.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:92d97fa52d3a4752b414332e2cb3bdeb)

The following query is loaded into the **Editor** field:
    
    
    -- UDF for easier string manipulation.
    CREATE TEMP FUNCTION ParseSubStr(hexStr STRING, startIndex INT64, endIndex INT64)
    RETURNS STRING
    LANGUAGE js
    AS r"""
      if (hexStr.length < 1) {
        return hexStr;
      }
      return hexStr.substring(startIndex, endIndex);
    """;
    
    -- UDF to translate hex numbers into decimal representation.
    CREATE TEMP FUNCTION HexToDec(hexStr STRING)
    RETURNS BIGNUMERIC
    LANGUAGE js
    AS r"""
       return parseInt(hexStr, 16)
    """;
    
    -- UDF to strip leading zeroes from 66 character addresses.
    -- Optimism addresses as returned from the OP node are 66 characters long.
    -- Format: "0x" prefix + 64 character (32-byte) address.
    -- Strip the leading zeroes so that it's easier to look up addresses in block explorer.
    CREATE TEMP FUNCTION StripLeadingZeroes(hex STRING, numZeroes INT64)
    RETURNS STRING
    LANGUAGE js
    AS r"""
      function _stripLeadingZeroes(addr, numZeroes) {
        if (addr.length != 66) {
          return addr;
        }
        return '0x'.concat(addr.substring(numZeroes));
      }
      return _stripLeadingZeroes(hex, numZeroes);
    """;
    
    -- Find finalized deposits into Optimism (L2) where assets were transferred
    -- from the L1 (Ethereum) to the L2 (Optimism) via the Optimism Standard Bridge
    -- at block X.
    SELECT
      block_number,
      transaction_hash,
      CONCAT("https://optimistic.etherscan.io/tx/", transaction_hash) AS txn_optimistic_etherscan,
      StripLeadingZeroes(topics[OFFSET(1)], 26) AS L1Token,
      StripLeadingZeroes(topics[OFFSET(2)], 26) AS L2Token,
      StripLeadingZeroes(topics[OFFSET(3)], 26) AS from_address,
      StripLeadingZeroes(ParseSubStr(l.data, 0, 66), 26) AS to_address,
      HexToDec(ParseSubStr(l.data, 66, 130)) AS amount_deposited,
    FROM
      `bigquery-public-data.goog_blockchain_optimism_mainnet_us.logs` as l
    WHERE
      ARRAY_LENGTH(l.topics) > 0 -- Check for non-empty topics first to short-circuit boolean evaluation.
    AND
      -- DepositFinalized:
      -- https://github.com/ethereum-optimism/optimism/blob/e24d77204ede3635d57253f5b6306be261e109b5/packages/contracts-ts/abis.json#L10319
      l.topics[OFFSET(0)] = "0xb0444523268717a02698be47d0803aa7468c00acbed2f8bd93a0459cde61dd89"
    AND
      block_number = 109223310;
    

**Example result** :

Block Number | Txn Hash | Txn Optimistic Etherscan | L1 Token | L2 Token | From Address | To Address | Amount Deposited  
---|---|---|---|---|---|---|---  
109223310 | 0xec5885cdfe06809206d3898206e855b7fdac7c95792974f33462b90c7a91f126 | https://optimistic.etherscan.io/tx/0xec5885cdfe06809206d3898206e855b7fdac7c95792974f33462b90c7a91f126 | 0x0000000000000000000000000000000000000000 | 0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000 | 0x777a89166b1265ec9d2cab2df5db59d1f50621d1 | 0x777a89166b1265ec9d2cab2df5db59d1f50621d1 | 1000000000000000  
109223310 | 0xa04d89f7a8cbbafd81fc315d3f76ca8d8dda4e0177225ff62d266b34b2530454 | https://optimistic.etherscan.io/tx/0xa04d89f7a8cbbafd81fc315d3f76ca8d8dda4e0177225ff62d266b34b2530454 | 0xd533a949740bb3306d119cc777fa900ba034cd52 | 0x0994206dfe8de6ec6920ff4d779b0d950605fb53 | 0x9e7f8d6e87ec1c783d01fcc90ebf6ec766b0036c | 0xcea806562b757aeffa9fe9d0a03c909b4a204254 | 1022823927640195072000  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
