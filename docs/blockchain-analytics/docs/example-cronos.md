---
url: https://docs.cloud.google.com/blockchain-analytics/docs/example-cronos/
title: Cronos example queries \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:43:45.166134+00:00
---

# Cronos example queries  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/example-cronos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-analytics/docs/overview)



Send feedback 

#  Cronos example queries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides Blockchain Analytics query examples for Cronos.

See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/introduction) for instructions on using BigQuery.

## Show all USDT transfers

This query shows transfers of the USDT token on Cronos since genesis.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:5c3ab9f971ee4302b8dddaaf06d30232)

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
    
    -- UDF to convert hex to decimal.
    CREATE TEMP FUNCTION HexToDecimal(hexStr STRING)
    RETURNS INT64
    LANGUAGE js
    AS r"""
      return parseInt(hexStr, 16);
    """;
    
    SELECT
      t.transaction_hash,
      t.from_address AS from_address,
      CONCAT("0x", ParseSubStr(l.topics[OFFSET(2)], 26, LENGTH(l.topics[OFFSET(2)]))) AS to_address,
      (HexToDecimal(l.data) / 1000000) AS usdt_transfer_amount
    FROM
      `bigquery-public-data.goog_blockchain_cronos_mainnet_us.transactions` AS t
    INNER JOIN
      `bigquery-public-data.goog_blockchain_cronos_mainnet_us.logs` AS l
    ON
      l.transaction_hash = t.transaction_hash
    WHERE
      t.to_address = LOWER("0x66e428c3f67a68878562e79a0234c1f83c208770") -- USDT
    AND
      ARRAY_LENGTH(l.topics) > 0
    AND
      -- Transfer(address indexed src, address indexed dst, uint wad)
      l.topics[OFFSET(0)] = LOWER("0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef")
    ;
    

The following shows an example result:

Transaction Hash | From Address | To Address | USDT Transfer Amount  
---|---|---|---  
0x6688fbfff00aee60811c150e3f5fcd08a6c9c50b9e028ff4bed3138918cd6b16 | 0x792f3570cf9a552952b7f80703d1b4e773397e33 | 0xe6e2d743e057024e033fde3e16077de3302e0cd1 | 1500.0  
0x84f0b00a5ddc882134fab138097a582500097eb7051fed499c403368ab622b31 | 0xf6d7dd84382cd532eb68cc2711509058936e890d | 0x03363e4bbc35f01bec95a33b3b391894f4ca7244 | 1001.08402  
0xc353e823bfa7c582956154194bccfabef6a4f7e71efb9211ae64b9ccc1b21cc7 | 0x9e199307660706e0ed1ed4d56684aad67ca97bde | 0x43d615be1714913fc1850e5a77cd01fa9b75e90c | 5000.0  
0x98321418e4fdc29d84a2d49bfc2d6ce1b4d0b37b93b84051aea75b19fb2a6e44 | 0x340a27ea8874177c894c365183d2283b5fcaa697 | 0xa0b5564550345414b619821c8dcbf7e0a20a195a | 7.0  
0x095a3a3453b27d003ac299fbdbcff53f78c32e748f79064e8a74bc6e20fe8e48 | 0x3a956433edae040b41f1767b24009d08bf73fd6e | 0x8995909dc0960fc9c75b6031d683124a4016825b | 30000.0  
  
## Wrapped Cronos activity

This query shows the wallets with the most interactions with Wrapped Cronos in the last 30 days.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:ed059681c252444886f759cbc3d7bda9)

The following query is loaded into the **Editor** field:
    
    
    SELECT
      from_address AS address,
      CONCAT("https://cronoscan.com/address/", from_address) AS croniscan_link,
      COUNT(from_address) AS num_transactions
    FROM
      `bigquery-public-data.goog_blockchain_cronos_mainnet_us.transactions` AS t
    WHERE
      to_address = LOWER("0x5C7F8A570d578ED84E63fdFA7b1eE72dEae1AE23") -- Wrapped CRO
    AND
      block_timestamp > (CURRENT_TIMESTAMP() - INTERVAL 30 DAY)
    GROUP BY
      from_address
    ORDER BY
      COUNT(from_address) DESC
    ;
    

The following shows an example result:

address | croniscan_link | num_transactions  
---|---|---  
0x07195f6dbac033152904747ca22d4debad682ad7 | <https://cronoscan.com/address/0x07195f6dbac033152904747ca22d4debad682ad7> | 167  
0x70f1378570328c42782e9023c048d1357071082b | <https://cronoscan.com/address/0x70f1378570328c42782e9023c048d1357071082b> | 148  
0xce6aeeb31f00a5783c115a669e516f34d56512e4 | <https://cronoscan.com/address/0xce6aeeb31f00a5783c115a669e516f34d56512e4> | 120  
0xc7b0ff7bd56618645737ad1f5623568c1fc65449 | <https://cronoscan.com/address/0xc7b0ff7bd56618645737ad1f5623568c1fc65449> | 95  
0x8194ed39b510a07425b49752ce489cbaa972fbf0 | <https://cronoscan.com/address/0x8194ed39b510a07425b49752ce489cbaa972fbf0> | 77  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
