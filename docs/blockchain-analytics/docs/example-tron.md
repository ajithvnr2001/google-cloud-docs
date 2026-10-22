---
url: https://docs.cloud.google.com/blockchain-analytics/docs/example-tron/
title: Tron example queries \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:11.233007+00:00
---

# Tron example queries  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/example-tron/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-analytics/docs/overview)



Send feedback 

#  Tron example queries Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides Blockchain Analytics query examples for Tron.

See the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/introduction) for instructions on using BigQuery.

## Tether transfers with the largest amounts in a month

This query returns the three largest USDT transfers in March 2023.

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:d7d7ca8368dc4346b8618d3ea3d11128)

The following query is loaded into the **Editor** field:
    
    
    CREATE TEMP FUNCTION hexToTron(address STRING)
    RETURNS STRING
    LANGUAGE js
    OPTIONS (library=["gs://blockchain-etl-bigquery/ethers.js"])
    AS r"""
      function encode58(buffer) {
        const ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz';
        const digits = [0];
        for (let i = 0; i < buffer.length; i++) {
          for (let j = 0; j < digits.length; j++) digits[j] <<= 8;
          digits[0] += buffer[i];
          let carry = 0;
          for (let j = 0; j < digits.length; ++j) {
            digits[j] += carry;
            carry = (digits[j] / 58) | 0;
            digits[j] %= 58;
          }
          while (carry) {
            digits.push(carry % 58);
            carry = (carry / 58) | 0;
          }
        }
        for (let i = 0; buffer[i] === 0 && i < buffer.length - 1; i++) digits.push(0);
        return digits.reverse().map((digit) => ALPHABET[digit]).join("");
      }
    
      function sha256(msgBytes) {
        const msgHex = ethers.utils.hexlify(msgBytes);
        const hashHex = ethers.utils.sha256(msgHex);
        return ethers.utils.arrayify(hashHex);
      }
    
      addressBytes = ethers.utils.arrayify('0x' + address.replace(/^0x/, '41'))
      checkSum = sha256(sha256(addressBytes)).slice(0, 4);
      return encode58(new Uint8Array([...addressBytes, ...checkSum]));
    """;
    
    WITH transfers AS (
      SELECT
        block_number,
        hexToTron(CONCAT('0x', SUBSTR(topics[1], 27))) AS from_address,
        hexToTron(CONCAT('0x', SUBSTR(topics[2], 27))) AS to_address,
        CAST(data AS INT64) / 1000000 AS amount
      FROM
        `bigquery-public-data.goog_blockchain_tron_mainnet_us.logs` l
      WHERE
        address = '0xa614f803b6fd780986a42c78ec9c7f77e6ded13c' -- USDT contract
        AND ARRAY_LENGTH(topics) = 3
        AND topics[0] = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef' -- Transfer events
        AND DATE(block_timestamp) BETWEEN "2023-03-01" AND "2023-03-31"
    )
    SELECT * FROM transfers ORDER BY amount DESC LIMIT 3;
    

The following shows an example result:

**Example result**  
---  
block_number | from_address | to_address | amount  
49606052 | TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi | TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb | 2173544428.073  
49076870 | TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb | TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi | 2005126503.6518  
49665517 | T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb | TBPxhVAsuzoFnKyXtc1o2UySEydPHgATto | 1000000000.0  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
