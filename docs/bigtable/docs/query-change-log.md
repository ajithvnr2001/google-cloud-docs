---
url: https://docs.cloud.google.com/bigtable/docs/query-change-log/
title: Query a Bigtable change log in BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:24.040131+00:00
---

# Query a Bigtable change log in BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/query-change-log/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query a Bigtable change log in BigQuery

This page provides guidance and example queries to help you process a Bigtable change log in BigQuery.

This page is intended for users who have completed the following:

  * [Set up a Bigtable change stream-enabled table](https://docs.cloud.google.com/bigtable/docs/change-streams-quickstart).
  * Run the [Dataflow template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-bigquery) that writes a change log to BigQuery. You can follow the quickstart to learn how to set this up.



This guide assumes some knowledge of BigQuery. To learn more, you can follow the [quickstart that shows how to load and query data](https://docs.cloud.google.com/bigquery/docs/quickstarts/load-data-console).

## Open the change log table

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, expand your project.

  3. Expand your dataset.

  4. Click the table with the suffix: `_changelog`.




### Table format

The entire [output schema](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-bigquery#bigquery-output-table-schema) contains several columns. This guide focuses on connecting the rows to their columns and values, and parsing values into analyzable formats.

## Basic queries

The examples in this section use a Bigtable table for tracking credit card sales. The table has one column family (`cf`) and the following columns:

  * Row key with the format `credit card number`#`transaction timestamp`
  * Merchant
  * Amount
  * Category
  * Transaction date



### Query one column

Filter the results to just one column family and one column using a `WHERE` clause.
    
    
    SELECT row_key, column_family, column, value, timestamp,
    FROM your_dataset.your_table
    WHERE
      mod_type="SET_CELL"
      AND column_family="cf"
      AND column="merchant"
    LIMIT 1000
    

### Parse values

All values are stored as strings or byte strings. You can cast a value to its intended type with [conversion functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/conversion_functions).
    
    
    SELECT row_key, column_family, column, value, CAST(value AS NUMERIC) AS amount
    FROM your_dataset.your_table
    WHERE
      mod_type="SET_CELL"
      AND column_family="cf"
      AND column="amount"
    LIMIT 1000
    

### Perform aggregations

You can perform more operations, such as aggregations on numeric values.
    
    
    SELECT SUM(CAST(value AS NUMERIC)) as total_amount
    FROM your_dataset.your_table
    WHERE
      mod_type="SET_CELL"
      AND column_family="cf"
      AND column="amount"
    

## Pivot the data

To perform queries that involve multiple Bigtable columns, you need to pivot the table. Each new BigQuery row includes one data change record returned by the change stream from its corresponding row in your Bigtable table. Depending on your schema, you can use a combination of the row key and timestamp to group the data.
    
    
    SELECT * FROM (
      SELECT row_key, timestamp, column, value
      FROM your_dataset.your_table
    )
    PIVOT (
      MAX(value)
      FOR column in ("merchant", "amount", "category", "transaction_date")
    )
    

**Note:** It is possible for multiple values to appear, so you need to use an [aggregate function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions) on the value.

### Pivoting with a dynamic columnset

If you have a dynamic set of columns, you can do some additional processing to get all the columns and put them into the query programmatically.
    
    
    DECLARE cols STRING;
    SET cols = (
      SELECT CONCAT('("', STRING_AGG(DISTINCT column, '", "'), '")'),
      FROM your_dataset.your_table
    );
    
    EXECUTE IMMEDIATE format("""
    SELECT * FROM (
      SELECT row_key, timestamp, column, value
      FROM your_dataset.your_table
    )
    PIVOT (
      MAX(value)
      FOR column in %s
    )""", cols);
    

## JSON Data

If you are setting all values with JSON, you need to parse them and extract the values based on the keys. You can use parsing functions once you have derived the value from the JSON object. These examples use the credit card sales data introduced earlier, but instead of writing data to multiple columns, the data is written as a single column as a JSON object.
    
    
    SELECT
      row_key,
      JSON_VALUE(value, "$.category") as category,
      CAST(JSON_VALUE(value, "$.amount") AS NUMERIC) as amount
    FROM your_dataset.your_table
    LIMIT 1000
    

### Aggregation queries with JSON

You can perform aggregation queries with JSON values.
    
    
    SELECT
      JSON_VALUE(value, "$.category") as category,
      SUM(CAST(JSON_VALUE(value, "$.amount") AS NUMERIC)) as total_amount
    FROM your_dataset.your_table
    GROUP BY category
    

## What's next

  * Learn more about [Bigtable change streams](https://docs.cloud.google.com/bigtable/docs/change-streams-overview).
  * Refer to [the Bigtable change stream to BigQuery template reference page](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-bigquery).
  * Learn how to [set up the Bigtable change stream to BigQuery template](https://docs.cloud.google.com/bigtable/docs/change-streams-to-bigquery-quickstart).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
