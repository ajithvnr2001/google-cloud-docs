---
url: https://docs.cloud.google.com/bigtable/docs/asynchronous-secondary-index-queries/
title: Asynchronous secondary index queries \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:05.710628+00:00
---

# Asynchronous secondary index queries  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/asynchronous-secondary-index-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Asynchronous secondary index queries

This document provides examples of common query patterns for building asynchronous secondary indexes in Bigtable. The examples use IDs and values that are similar to those in [Data for examples](https://docs.cloud.google.com/bigtable/docs/using-filters#data) and you can [create a test table](https://docs.cloud.google.com/bigtable/docs/creating-test-table#create-test_table) to test the queries.

Before you read this page, familiarize yourself with [Create an asynchronous secondary index](https://docs.cloud.google.com/bigtable/docs/asynchronous-secondary-index) and [GoogleSQL for Bigtable](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).

## Example queries

The following examples show how to create asynchronous secondary indexes using different GoogleSQL queries.

### Create an inverted index based on a column qualifier and values

The following query creates an inverted index by extracting all key-value pairs from a column family that has a flexible schema. It uses `MAP_ENTRIES` to get an array of all data that the `stats_summary` column family stores, and then `UNNEST` to transform each key-value pair into a separate row. The resulting index allows for fast lookups based on `stat_description` and `stat_value`. If you add new types of statistics to the source table, then Bigtable includes them in the asynchronous index automatically.
    
    
    SELECT
     stats.key as stat_description,
     stats.value as stat_value,
     _key as original_key,
     cell_plan as cell_plan
    FROM test_table
    CROSS JOIN UNNEST(MAP_ENTRIES(stats_summary)) stats
    ORDER BY stat_description, stat_value, original_key
    

As a result, each key-value pair from the original `stats_summary` column family has its own row in the continuous materialized view:

stat_description (key) | stat_value (key) | original_key (key) | cell_plan  
---|---|---|---  
connected_cell | "2" | phone#4c410523#20190501 | { "data_plan_01gb": "true", "data_plan_05gb": "false" }  
os_build | PQ2A.190401.002 | phone#5c10102#20190501 | { "data_plan_10gb": "false" }  
  
To get fast lookups on data that Bigtable captured as values, use the new row keys to query the data, as shown in the following example:
    
    
    SELECT cell_plan, original_key
    FROM `mv_inverted_index`
    WHERE stat_description = "connected_cell"
    AND stat_value = "2"
    

### Create a new row key based on existing data

The following example creates a new index key, `total_plan_capacity`, by categorizing data plans that the `cell_plan` column family stores. The query uses `MAP_KEYS` to get all keys in `cell_plan` and `ARRAY_INCLUDES_ANY` to filter for specific data plan keys. A `CASE` statement then defines the logic to assign a `total_plan_capacity` category that's based on the presence and values of these data plans. This allows for efficient lookups based on the combined data plan capacity.
    
    
    SELECT
     CASE
        WHEN
         cell_plan['data_plan_01gb'] = "true"
         AND (cell_plan['data_plan_05gb'] = "false" OR cell_plan['data_plan_05gb'] IS NULL)
         AND (cell_plan['data_plan_10gb'] = "false" OR cell_plan['data_plan_10gb'] IS NULL)
       THEN 'x-small'
    
       WHEN
         cell_plan['data_plan_01gb'] = "true"
         AND (cell_plan['data_plan_05gb'] = "true")
         AND (cell_plan['data_plan_10gb'] = "false" OR cell_plan['data_plan_10gb'] IS NULL)
       THEN 'small'
    
       WHEN
         cell_plan['data_plan_01gb'] = "true"
         AND (cell_plan['data_plan_05gb'] = "false" OR cell_plan['data_plan_05gb'] IS NULL)
         AND (cell_plan['data_plan_10gb'] = "true")
       THEN 'medium'
    
       WHEN
         (cell_plan['data_plan_01gb'] = "false" OR cell_plan['data_plan_01gb'] IS NULL)
         AND (cell_plan['data_plan_05gb'] = "true")
         AND (cell_plan['data_plan_10gb'] = "true")
       THEN 'large'
    
       WHEN
         cell_plan['data_plan_01gb'] = "true"
         AND (cell_plan['data_plan_05gb'] = "true")
         AND (cell_plan['data_plan_10gb'] = "true")
       THEN 'x-large'
     END as total_plan_capacity,
     _key as original_key,
     stats_summary
    FROM test_table
    WHERE ARRAY_INCLUDES_ANY(MAP_KEYS(cell_plan), ["data_plan_01gb", "data_plan_05gb","data_plan_10gb"])
    ORDER BY total_plan_capacity, original_key
    

### Create a time-series-based index

Bigtable stores each cell value and its associated timestamp. By using the `WITH_HISTORY=>TRUE` flag in the `FROM` clause, you can retrieve all versions of data and their timestamps. The `UNPACK` table function then expands the query results so that each timestamped value appears on its own row with a separate `_timestamp` column. This lets you create an asynchronous secondary index where the new row key is based on these timestamp values, enabling quick lookups that are based on time ranges.
    
    
    SELECT
     _timestamp as stats_timestamp,
     _key as original_key,
     stats_summary
    FROM UNPACK((
     select
       _key,
       stats_summary
      FROM
     test_table (WITH_HISTORY=>TRUE)
    ))
    ORDER BY stats_timestamp, original_key
    

### Create an index entry for items and values in a JSON cell

Bigtable is often used as a key-value store for large-scale workloads, including data in formats such as JSON. The following example shows how to create an asynchronous secondary index for fast lookups of data that JSON stores. The query uses `JSON_EXTRACT` to extract the `store_id` from a JSON string within the `transaction_information` column family in a table named `sales`. This index allows for quick retrieval of sales transactions by specific store IDs.
    
    
    SELECT
    JSON_EXTRACT(transaction_information["json"], "$.store_id") as store_id,
    _key as original_key,
    transaction_information
    from sales
    ORDER BY store_id, original_key;
    

## What's next

  * [Continuous materialized view queries](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries)
  * [Create and manage continuous materialized views](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
