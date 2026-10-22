---
url: https://docs.cloud.google.com/blockchain-analytics/docs/uint256/
title: UINT256 Handling \u00a0|\u00a0 Blockchain Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:15.682375+00:00
---

# UINT256 Handling  |  Blockchain Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-analytics/docs/uint256/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Blockchain Analytics ](https://docs.cloud.google.com/blockchain-analytics/docs)
  * [ Resources ](https://docs.cloud.google.com/blockchain-analytics/docs/resources)



Send feedback 

#  UINT256 Handling Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides information on how to handle blockchain UINT256 data types in Blockchain Analytics.

## Lossless columns

Blockchain Analytics does not support UINT256 NUMERIC columns, but some blockchain data types have numerical precision up to UINT256.

In order to preserve the numerical precision, Blockchain Analytics datasets presents UINT256 values in two separate columns:

  * An UINT128 NUMERIC column with potential loss of precision.
  * A STRING column containing the full decimal value in string form. The string columns are marked with the `_lossless` prefix.



## BigQuery User-Defined Functions (UDF)

Google Cloud hosts a Blockchain Analytics utility library that contains UDF for handling UINT256 computations and aggregations. The following UDFs are relevant for UINT256 computation.

  * `bqutil.fn.bignumber_add`
  * `bqutil.fn.bignumber_sub`
  * `bqutil.fn.bignumber_mul`
  * `bqutil.fn.bignumber_div`
  * `bqutil.fn.bignumber_sum`
  * `bqutil.fn.bignumber_avg`



See the [BigQuery UDF GitHub repository](https://github.com/GoogleCloudPlatform/bigquery-utils/tree/master/udfs) for details on community managed BigQuery UDFs.

See the [BigQuery UDF documentation](https://docs.cloud.google.com/bigquery/docs/user-defined-functions) for instructions on using BigQuery UDFs.

## Lossless example with UDF workaround for UINT256

In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery?sq=650023896125:fc20b24c8f8b4bb9aa2e3f02c8085e14)

The following query is loaded into the **Editor** field:
    
    
    WITH withdrawals AS (
      SELECT
        w.amount_lossless AS amount,
        DATE(b.block_timestamp) AS block_date
      FROM
        bigquery-public-data.blockchain_analytics_ethereum_mainnet_us.blocks AS b
        CROSS JOIN UNNEST(withdrawals) AS w
    )
    SELECT
      block_date,
      bqutil.fn.bignumber_div(bqutil.fn.bignumber_sum(ARRAY_AGG(amount)), "1000000000") AS eth_withdrawn
    FROM
      withdrawals
    GROUP BY 1 ORDER BY 1 DESC
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
