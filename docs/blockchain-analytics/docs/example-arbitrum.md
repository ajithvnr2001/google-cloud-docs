---
url: https://docs.cloud.google.com/blockchain-analytics/docs/example-arbitrum/
title: Arbitrum example queries \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:01.699182+00:00
---

# Arbitrum example queries  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/example-arbitrum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-analytics/docs/overview)



Send feedback 

#  Arbitrum example queries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides Blockchain Analytics query examples for Arbitrum.

See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/introduction) for instructions on using BigQuery.

## Number of L1 to L2 tickets created in last 30 days

This query shows the number of [retryable messages](https://docs.arbitrum.io/arbos/l1-to-l2-messaging) successfully created between Ethereum and Arbitrum in the last 30 days.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:ce5c0aec918b46ab9f588659b7c6cae8)
    
    
    SELECT
      DISTINCT COUNT(topics[OFFSET(1)]) AS num_l1_to_l2_tickets_created
    FROM
      bigquery-public-data.goog_blockchain_arbitrum_one_us.logs
    WHERE
      ARRAY_LENGTH(topics) > 0
    AND
      -- "TicketCreated" event emitted via Arbitrum's canonical method for creating L1 to L2 messages.
      topics[OFFSET(0)] = LOWER("0x7c793cced5743dc5f531bbe2bfb5a9fa3f40adef29231e6ab165c08a29e3dd89")
    AND block_timestamp > (CURRENT_TIMESTAMP() - INTERVAL 30 DAY)
    ;
    

The following shows an example result:

num_l1_to_l2_tickets_created  
---  
7779  
  
## Show withdrawals to L1 (Ethereum), with remaining dispute period

This query shows withdrawals of Eth from Arbitrum to Ethereum using the [official Arbitrum bridge](https://docs.arbitrum.io/for-users/troubleshooting-users#how-long-does-it-take-before-i-receive-my-funds-when-i-initiate-withdrawal-from-arbitrum-chains-one-and-nova), and the remaining estimated dispute period.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:8143dfca31144a87b80db06ed03b8584)
    
    
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
    
    SELECT
      b.block_timestamp as block_timestamp,
      CONCAT("https://arbiscan.io/tx/", transaction_hash) AS arbiscan_txn,
      (t.value.bignumeric_value / 1000000000000000000) AS eth_withdrawn,
      CONCAT("0x", ParseSubStr(t.input, 34, LENGTH(t.input))) AS l1_destination_address,
      CASE WHEN DATETIME_DIFF(CURRENT_TIMESTAMP(), b.block_timestamp, DAY) >= 7 THEN 'True' ELSE 'False' END AS wait_period_over,
      CASE WHEN 7 - DATETIME_DIFF(CURRENT_TIMESTAMP(), b.block_timestamp, DAY) > 0 THEN 7 - DATETIME_DIFF(CURRENT_TIMESTAMP(), b.block_timestamp, DAY) ELSE 0 END AS wait_period_days_left,
    FROM
      bigquery-public-data.goog_blockchain_arbitrum_one_us.transactions AS t
    INNER JOIN
      bigquery-public-data.goog_blockchain_arbitrum_one_us.blocks AS b
    ON
      b.block_hash = t.block_hash
    WHERE
      t.to_address = LOWER("0x0000000000000000000000000000000000000064") -- ArbSys contract.
    AND
      t.input LIKE "%0x25e16063%" -- withdrawEth
    ORDER BY
      b.block_timestamp
    DESC;
    

block_timestamp | arbiscan_txn | eth_withdrawn | l1_destination_address | wait_period_over | wait_period_days_left  
---|---|---|---|---|---  
2023-10-02 23:05:26.000000 UTC | <https://arbiscan.io/tx/0xe6800b17c1b8161fbdf68ea2c0a913c7cc78305da4fbb1b397aa80d524550c95> | 0.013858051475204934 | 0x3a0ab56fb888159eae27f1021a0aa3bd9a73b2be | False | 1  
2023-10-02 22:55:46.000000 UTC | <https://arbiscan.io/tx/0x4b1695e72b80a9e0a6051f5536af56379da4ed0118364f3089ef554c4e0b2108> | 1.8593161561369025 | 0x8c35933c469406c8899882f5c2119649cd5b617f | False | 1  
2023-10-02 19:51:32.000000 UTC | <https://arbiscan.io/tx/0x68503fbe4aa013c09e653efaf01586957b9b07a6b3479713c083283eba12b0ac> | 0.31 | 0x641763fb275dd3418012ee26591a9898360e9d69 | False | 1  
2023-10-02 17:32:50.000000 UTC | <https://arbiscan.io/tx/0x683da04b6b4a81c05176128cccbef71ae5d65122d5a52abb65a70107f8101c6c> | 0.13967551424971486 | 0x38e69da3f8003c41a7b5e9e5f0a060c6f18215a1 | True | 0  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
