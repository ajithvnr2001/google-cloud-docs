---
url: https://docs.cloud.google.com/blockchain-analytics/docs/example-ethereum/
title: Ethereum Mainnet example queries \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:00.682376+00:00
---

# Ethereum Mainnet example queries  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/example-ethereum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-analytics/docs/overview)



Send feedback 

#  Ethereum Mainnet example queries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides Blockchain Analytics query examples for Ethereum Mainnet.

See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/introduction) for instructions on using BigQuery.

## View the first and last block indexed

This query tells you how fresh the data is.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:f570aa8f5aae40dda3478b2c971944a5)

The following query is loaded into the **Editor** field:
    
    
    SELECT
      MIN(block_number) AS `First block`,
      MAX(block_number) AS `Newest block`,
      COUNT(1) AS `Total number of blocks`
    FROM
      bigquery-public-data.goog_blockchain_ethereum_mainnet_us.blocks;
    

The following shows an example result:

**Example result**  
---  
First block | Newest block | Total number of blocks  
0 | 17665654 | 17665655  
  
## Visualize the number of transactions by day over the last 6 months

This query lists the total number of transactions for each day for the last six months.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:7c79d9334707477689af2e3847a505e7)

The following query is loaded into the **Editor** field:
    
    
    SELECT
      TIMESTAMP_TRUNC(block_timestamp, DAY) AS timestamp1, COUNT(1) AS txn_count
    FROM
      bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions
    WHERE
      block_timestamp >= CAST(DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH) AS TIMESTAMP)
    GROUP BY timestamp1
    ORDER BY timestamp1
    

The following shows an example result:

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
  
## Daily slot utilization

Count the number of blocks added each calendar day since [The Merge](https://ethereum.org/en/roadmap/merge/). Since then, there are 7200 slots available for blocks, but not every slot is used.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:8290aee6f4d24ebf88a725b4307789b6)

The following query is loaded into the **Editor** field:
    
    
    SELECT
      DATE(block_timestamp) AS block_date,
      COUNT(block_number) AS daily_blocks,
      7200 - COUNT(block_number) AS skipped_slots
    FROM
      bigquery-public-data.goog_blockchain_ethereum_mainnet_us.blocks
    WHERE
      DATE(block_timestamp) BETWEEN DATE("2022-09-16") AND CURRENT_DATE("UTC") - 1 /* Only count complete days after The Merge */
    GROUP BY block_date
    

The following shows an example result:

**Example result**  
---  
block_date | daily_blocks | skipped_slots  
2023-06-26 | 7105 | 95  
2023-06-25 | 7109 | 91  
2023-06-24 | 7110 | 90  
2023-06-23 | 7111 | 89  
2023-06-22 | 7114 | 86  
2023-06-21 | 7135 | 65  
2023-06-20 | 7120 | 80  
2023-06-19 | 7121 | 79  
2023-06-18 | 7126 | 74  
2023-06-17 | 7142 | 58  
  
## Total Staked ETH withdrawal

### Lossless example with UDF workaround for UINT256

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:fc20b24c8f8b4bb9aa2e3f02c8085e14)

The following query is loaded into the **Editor** field:
    
    
    WITH withdrawals AS (
      SELECT
        w.amount_lossless AS amount,
        DATE(b.block_timestamp) AS block_date
      FROM
        bigquery-public-data.goog_blockchain_ethereum_mainnet_us.blocks AS b
        CROSS JOIN UNNEST(withdrawals) AS w
    )
    SELECT
      block_date,
      bqutil.fn.bignumber_div(bqutil.fn.bignumber_sum(ARRAY_AGG(amount)), "1000000000") AS eth_withdrawn
    FROM
      withdrawals
    GROUP BY 1 ORDER BY 1 DESC
    

### Lossy example

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:eaa5836626f04cbeb1111d3cca8348d3)

The following query is loaded into the **Editor** field:
    
    
    WITH withdrawals AS (
      SELECT
        u.amount AS amount
      FROM
        bigquery-public-data.goog_blockchain_ethereum_mainnet_us.blocks
        CROSS JOIN UNNEST(withdrawals) AS u
    )
    SELECT
      SUM(withdrawals.amount) / POW(10,9) AS total_eth_withdrawn
    FROM
      withdrawals
    

## Earned mining transaction fees since EIP-1559

Since [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559#eth-burn-precludes-fixed-supply), the base fees of transactions are burned and the miners only earn the priority fees. The following query computes the total amount of fees earned by the miners since the London hard fork.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:a684332f3abb459ebfa1ed84ba09d65d)

The following query is loaded into the **Editor** field:
    
    
    WITH tgas AS (
      SELECT t.block_number, gas_used, effective_gas_price FROM
        bigquery-public-data.goog_blockchain_ethereum_mainnet_us.receipts AS r
        JOIN bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions AS t
        ON t.block_number = r.block_number AND t.transaction_hash = r.transaction_hash
    )
    SELECT
      /* Cast needed to avoid INT64 overflow when doing multiplication. */
      SUM(CAST(tgas.effective_gas_price - b.base_fee_per_gas AS BIGNUMERIC) * tgas.gas_used)
    FROM
      bigquery-public-data.goog_blockchain_ethereum_mainnet_us.blocks b JOIN tgas
      ON b.block_number = tgas.block_number
    WHERE
      b.block_number >= 12965000 /* The London hard fork. */
    

The following shows an example result:

**Example results**  
---  
f0_  
645681358899882340722378  
  
## Skipped Beacon Chain slots

Find the epoch and slot numbers for missing, forked, or otherwise skipped slots since the [Beacon Chain](https://ethereum.org/en/roadmap/beacon-chain/) upgrade.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:510ef69c7a6e40a6893e2573985a695e)

The following query is loaded into the **Editor** field:
    
    
    CREATE TEMP FUNCTION SlotNumber(slot_time TIMESTAMP) AS (
      (SELECT DIV(TIMESTAMP_DIFF(slot_time, "2020-12-01 12:00:23 UTC", SECOND), 12))
    );
    
    CREATE TEMP FUNCTION EpochNumber(slot_time TIMESTAMP) AS (
      (SELECT DIV(SlotNumber(slot_time), 32))
    );
    
    /* Beacon Chain slot timestamps. */
    WITH slots AS (
      /* Directly generate the first day's slots. */
      SELECT * FROM UNNEST(GENERATE_TIMESTAMP_ARRAY("2020-12-01 12:00:23 UTC", "2020-12-01 23:59:59 UTC", INTERVAL 12 SECOND)) AS slot_time
      UNION ALL
      /* Join dates and times to generate up to yesterday's slots. Attempting this directly overflows the generator functions. */
      SELECT TIMESTAMP(DATETIME(date_part, TIME(time_part))) AS slot_time
      FROM UNNEST(GENERATE_DATE_ARRAY("2020-12-02", CURRENT_DATE("UTC") - 1)) AS date_part
      CROSS JOIN
      UNNEST(GENERATE_TIMESTAMP_ARRAY("1970-01-01 00:00:11 UTC", "1970-01-01 23:59:59 UTC", INTERVAL 12 SECOND)) AS time_part
    )
    SELECT
      EpochNumber(slot_time) AS epoch,
      SlotNumber(slot_time) AS slot,
      slot_time,
      FORMAT("https://beaconcha.in/slot/%d", SlotNumber(slot_time)) AS beaconchain_url,
    FROM
      slots LEFT JOIN bigquery-public-data.goog_blockchain_ethereum_mainnet_us.blocks
      ON slot_time = block_timestamp
    WHERE
      block_number IS NULL AND slot_time BETWEEN "2022-09-15 06:42:59 UTC" AND CURRENT_TIMESTAMP()
    ORDER BY slot_time DESC;
    

The following shows an example result:

**Example result**  
---  
epoch | slot | slot_time | beaconchain_url  
211159 | 6757113 | 2023-06-27 23:42:59 UTC | <https://beaconcha.in/slot/6757113>  
211159 | 6757088 | 2023-06-27 23:37:59 UTC | <https://beaconcha.in/slot/6757088>  
211158 | 6757061 | 2023-06-27 23:32:35 UTC | <https://beaconcha.in/slot/6757061>  
211145 | 6756660 | 2023-06-27 22:12:23 UTC | <https://beaconcha.in/slot/6756660>  
211145 | 6756642 | 2023-06-27 22:08:47 UTC | <https://beaconcha.in/slot/6756642>  
211142 | 6756564 | 2023-06-27 21:53:11 UTC | <https://beaconcha.in/slot/6756564>  
211136 | 6756379 | 2023-06-27 21:16:11 UTC | <https://beaconcha.in/slot/6756379>  
211136 | 6756374 | 2023-06-27 21:15:11 UTC | <https://beaconcha.in/slot/6756374>  
211135 | 6756320 | 2023-06-27 21:04:23 UTC | <https://beaconcha.in/slot/6756320>  
211132 | 6756225 | 2023-06-27 20:45:23 UTC | <https://beaconcha.in/slot/6756225>  
  
## USDC token issuance

Analyze the net issuance of USDC over the first week of March 2023.

**Note:** To include internal transactions, this query should be modified to use the logs table.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:c932e3fd3a3c4a51acbd0a3f875a49b3)

The following query is loaded into the **Editor** field:
    
    
    CREATE TEMP FUNCTION IFMINT(input STRING, ifTrue ANY TYPE, ifFalse ANY TYPE) AS (
      CASE
        WHEN input LIKE "0x40c10f19%" THEN ifTrue
        ELSE ifFalse
      END
    );
    
    CREATE TEMP FUNCTION USD(input FLOAT64) AS (
      CAST(input AS STRING FORMAT "$999,999,999,999")
    );
    
    SELECT
      DATE(block_timestamp) AS `Date`,
      USD(SUM(IFMINT(input, 1, -1) * CAST(CONCAT("0x", LTRIM(SUBSTRING(input, IFMINT(input, 75, 11), 64), "0")) AS FLOAT64) / 1000000)) AS `Total Supply Change`,
    FROM
      bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions
    WHERE
      DATE(block_timestamp) BETWEEN "2023-03-01" AND "2023-03-07"
      AND to_address = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48" -- USDC Coin Token
      AND (
        input LIKE "0x42966c68%" -- Burn
        OR input LIKE "0x40c10f19%" -- Mint
      )
    GROUP BY `Date`
    ORDER BY `Date` DESC;
    

The following shows an example result:

**Example result**  
---  
Date | Total Supply Change  
2023-03-07 | -$257,914,457  
2023-03-06 | -$223,014,422  
2023-03-05 | $200,060,388  
2023-03-04 | $234,929,175  
2023-03-03 | $463,882,301  
2023-03-02 | $631,198,459  
2023-03-01 | $172,338,818  
  
## Top 10 USDC Account Balances

Analyze the current top holders of USDC tokens.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:b3f62ad89e63447c904c0ca83f15123a)

The following query is loaded into the **Editor** field:
    
    
    WITH Transfers AS (
      SELECT address token, to_address account, 0 _out, CAST(quantity AS BIGNUMERIC) _in
      FROM `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.token_transfers`
    
      UNION ALL
    
      SELECT address token, from_address account, CAST(quantity AS BIGNUMERIC) _out, 0 _in
      FROM `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.token_transfers`
    )
    
    /* Top 10 Holders of USDC */
    SELECT account, (SUM(_in) - SUM(_out)) / 1000000 balance
    FROM Transfers
    WHERE token = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
    GROUP BY account
    ORDER BY balance DESC
    LIMIT 10;
    

The following shows an example result:

**Example result**  
---  
account | balance  
0xcee284f754e854890e311e3280b767f80797180d | 934249404.099105  
0x40ec5b33f54e0e8a33a975908c5ba1c14e5bbbdf | 608860969.753471  
0x47ac0fb4f2d84898e4d9e7b4dab3c24507a6d503 | 422999999.84  
0x0a59649758aa4d66e25f08dd01271e891fe52199 | 382469988.743467  
0xd54f502e184b6b739d7d27a6410a67dc462d69c8 | 335866305.446392  
0x99c9fc46f92e8a1c0dec1b1747d010903e884be1 | 300569267.063296  
0xda9ce944a37d218c3302f6b82a094844c6eceb17 | 231000000  
0x51edf02152ebfb338e03e30d65c15fbf06cc9ecc | 230000000.000002  
0x7713974908be4bed47172370115e8b1219f4a5f0 | 218307714.860457  
0x78605df79524164911c144801f41e9811b7db73d | 211737271.4  
  
## Top 5 most active traders of BAYC tokens

Analyze which EOAs have transferred the most Bored Ape NFTs.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:e4e3a72d5d1144fbaa98d40172a0790c)

The following query is loaded into the **Editor** field:
    
    
    WITH Transfers AS (
      SELECT address AS token, to_address AS account, COUNT(*) transfer_count
      FROM `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.token_transfers`
      GROUP BY token, account
    
      UNION ALL
    
      SELECT address AS token, from_address AS account, COUNT(*) transfer_count
      FROM `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.token_transfers`
      WHERE from_address != '0x0000000000000000000000000000000000000000'
      GROUP BY token, account
    )
    
    SELECT account, SUM(transfer_count) quantity
    FROM Transfers LEFT JOIN `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.accounts` ON account = address
    WHERE NOT is_contract AND token = '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d' /* BAYC */
    GROUP BY account
    ORDER BY quantity DESC
    LIMIT 5;
    

The following shows an example result:

**Example result**  
---  
account | quantity  
0xed2ab4948ba6a909a7751dec4f34f303eb8c7236 | 6036  
0x020ca66c30bec2c4fe3861a94e4db4a498a35872 | 2536  
0xd387a6e4e84a6c86bd90c158c6028a58cc8ac459 | 2506  
0x8ae57a027c63fca8070d1bf38622321de8004c67 | 2162  
0x721931508df2764fd4f70c53da646cb8aed16ace | 968  
  
## Average daily price of WETH in USDC on Uniswap

View the average daily swap price in the Uniswap USDC/WETH 0.05% fee pool.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:6acc11191f65431a9a1d0722d23e6ee3)

The following query is loaded into the **Editor** field:
    
    
    With Swaps AS (
      SELECT block_timestamp, transaction_hash,
        STRING(args[0]) sender,
        STRING(args[1]) recipient,
        SAFE_CAST(STRING(args[2]) AS BIGNUMERIC) amount0, /* USDC amount */
        SAFE_CAST(STRING(args[3]) AS BIGNUMERIC) amount1, /* WETH amount */
        SAFE_CAST(STRING(args[4]) AS BIGNUMERIC) sqrtPriceX96,
        CAST(STRING(args[5]) AS BIGNUMERIC) liquidity,
        CAST(STRING(args[6]) AS INT64) tick
      FROM `bigquery-public-data.blockchain_analytics_ethereum_mainnet_us.decoded_events`
      WHERE event_signature = 'Swap(address,address,int256,int256,uint160,uint128,int24)' /* Uniswap v3 Swaps */
      AND address = '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640' /* USDC/ETH 0.05% Pool */
    ),
    EtherUSDC AS (
      SELECT block_timestamp,
        ABS(amount0) / 1000000 usdc_amount, /* USDC uses 6 decimals */
        ABS(amount1) / 1000000000000000000 eth_amount, /* WETH uses 18 decimals */
        ABS(SAFE_DIVIDE(amount0, amount1)) * 1000000000000 usd_eth /* USDC/ETH has 12 decimal difference */
      FROM Swaps
    )
    
    SELECT EXTRACT(DATE FROM block_timestamp) `date`, CAST(AVG(usd_eth) AS STRING FORMAT '$9,999.00') `avg_price`, COUNT(*) `swap_count`
    FROM EtherUSDC
    WHERE usdc_amount >= 1.00 /* Ignore miniscule swaps */
    GROUP BY `date`
    ORDER BY `date` DESC
    

The following shows an example result:

**Example result**  
---  
date | avg_price | swap_count  
2023-10-03 | $1,658.24 | 3819  
2023-10-02 | $1,704.98 | 5136  
2023-10-01 | $1,689.63 | 3723  
2023-09-30 | $1,675.90 | 2988  
2023-09-29 | $1,665.99 | 4173  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
