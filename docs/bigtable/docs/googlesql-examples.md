---
url: https://docs.cloud.google.com/bigtable/docs/googlesql-examples/
title: GoogleSQL for Bigtable query examples \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:16.875529+00:00
---

# GoogleSQL for Bigtable query examples  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/googlesql-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GoogleSQL for Bigtable query examples

**Note:** This page includes features available only in the Enterprise Plus edition, such as Data Boost for SQL. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

The examples on this page demonstrate SQL query patterns for common and advanced Bigtable queries. You can run GoogleSQL queries in the [ Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console) query editor. You can also run queries using the [Bigtable client library for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview).

Before you read this page, read the [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).

**Note:** A _version_ refers to a timestamped value for a given column and row. Each version is stored in a cell. For more information, see [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model).

The examples on this page use IDs and values similar to those in [Data for examples](https://docs.cloud.google.com/bigtable/docs/using-filters#data).

## Common Bigtable SQL query patterns

The following are examples of common queries for Bigtable data. To see examples of similar queries that call the Bigtable Data API, see [Read examples](https://docs.cloud.google.com/bigtable/docs/reading-data) and [Use filters](https://docs.cloud.google.com/bigtable/docs/using-filters). For examples of queries on structured row keys, see [Structured row key queries](https://docs.cloud.google.com/bigtable/docs/structured-row-key-queries).

Retrieve the latest version of all columns for a given row key.
    
    
      SELECT * FROM myTable WHERE _key = 'r1'
    

Retrieve all versions of all columns for a given row key.
    
    
      SELECT * FROM myTable(with_history => TRUE) WHERE _key = 'r1'
    

Retrieve the latest version of a particular column from a particular column family for a given row key.
    
    
      SELECT stats_summary['os_build'] AS os
      FROM analytics
      WHERE _key = 'phone#4c410523#20190501'
    

Retrieve the row keys and the latest version of multiple columns for a given row key range.
    
    
      SELECT
        _key,
        stats_summary['os_build'] AS os,
        stats_summary['user_agent'] AS agent
      FROM analytics
      WHERE _key >= 'phone#4c410523#20190501' AND _key < 'phone#4c410523#201906201'
    

Retrieve all versions of all columns for multiple row key ranges, up to 10 rows.
    
    
      SELECT *
      FROM analytics(with_history => TRUE)
      WHERE
        (_key >= 'phone#4c410523#20190501' AND _key < 'phone#4c410523#201906201')
        OR (_key >= 'phone#5c10102#20190501' AND _key < 'phone#5c10102#20190601')
      LIMIT 10
    

Retrieve all versions of all columns for multiple row keys.
    
    
      SELECT *
      FROM analytics(with_history => TRUE)
      WHERE _key = 'phone#4c410523#20190501' OR _key = 'phone#4c410523#20190502'
    

Retrieve all versions of all columns for multiple row keys using a different approach.
    
    
      SELECT *
      FROM analytics(with_history => TRUE)
      WHERE _key IS IN ('phone#4c410523#20190501', 'phone#4c410523#20190502')
    

Retrieve the latest version of all columns within a column family for a row key prefix.
    
    
      SELECT stats_summary
      FROM analytics
      WHERE _key LIKE 'phone#%'
    

Retrieve the row keys and three latest versions of all columns within a column family for all rows in the table. This query requires a full table scan, so it's not recommended for low-latency, high-throughput access patterns.
    
    
      SELECT _key, cell_plan FROM analytics(with_history => TRUE, latest_n => 3)
    

Retrieve the latest version of all columns with row keys matching a specified regular expression. This query requires a full table scan, so it's not recommended for low-latency, high-throughput access patterns, unless you also provide a row key prefix or row key range predicate in the `WHERE` clause.
    
    
      SELECT *
      FROM myTable(with_history => TRUE)
      WHERE REGEXP_CONTAINS(_key, '.*#20190501$')
    

Retrieve the latest version of all columns with the matching row key prefix and counter value more than `123`. You don't need to cast for this comparison, because [Bigtable aggregates](https://docs.cloud.google.com/bigtable/docs/aggregates#aggregate-column-families) are numeric.
    
    
      SELECT *
      FROM myTable
      WHERE _key LIKE 'user12%' AND counterFamily['counter'] > 123
    

Retrieve the latest version of all columns for a row key prefix if the referrer matches a specific value.
    
    
      SELECT *
      FROM analytics
      WHERE _key LIKE 'com.mysite%' AND session['referrer'] = './home'
    

Categorize a given row based on the value of a given column. This query is similar to using a [composing conditional filter](https://docs.cloud.google.com/bigtable/docs/using-filters#condition) in the Bigtable Data API.
    
    
      SELECT
        *,
        CASE cell_plan['data_plan']
          WHEN '10gb' THEN 'passed-filter'
          ELSE 'filtered-out'
          END
          AS label
      FROM analytics
    

Retrieve the row key and the column qualifiers in a specific column family for a specified row key range. In SQL, column families are represented by the map data type, where each column qualifier and value is mapped as a key-value pair. This SQL query is similar to using a [strip value filter](https://docs.cloud.google.com/bigtable/docs/using-filters#strip-value) in the Bigtable Data API.
    
    
      SELECT _key, MAP_KEYS(cell_plan) AS keys
      FROM analytics
      WHERE _key >= 'phone#4c410523#20190501' AND _key < 'phone#4c410523#201906201'
    

The `UNPACK` function lets you transform Bigtable data into a tabular time series format, which is useful when performing time series analysis. Consider an example where you have a `clicks` column in an `engagement` column family. The following query uses `UNPACK` to see how certain campaigns are performing by aggregating the clicks over a minute from the last hour.
    
    
      SELECT
        FORMAT_TIMESTAMP('%M', _timestamp) AS minute,
        COUNT(clicks) AS total_clicks
      FROM
        UNPACK((
          SELECT engagement['clicks'] as clicks
          FROM metrics(with_history => true, after => TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR))
          WHERE _key = @campaign_id
        ))
      GROUP BY
        minute;
    

## Advanced Bigtable SQL query patterns

The following samples demonstrate more advanced patterns.

With the following query, you can retrieve the row key and most recent value of the JSON attribute `abc` in the `session` column family. For more information, see [`JSON` functions](https://docs.cloud.google.com/bigtable/docs/reference/sql/json_functions#json_functions).
    
    
      SELECT _key, JSON_VALUE(session['payload'], '$.abc') AS abc FROM analytics
    

With the following query, you can retrieve the row key and calculate the average session length using the latest value of two [Bigtable aggregate cells](https://docs.cloud.google.com/bigtable/docs/aggregates) , which are numeric, for each row in the table.
    
    
      SELECT
        _key AS userid,
        session['total_minutes'] / session['count'] AS avg_session_length
      FROM analytics
    

With the following query, you can retrieve the latest version of all columns for a given row key prefix if the `session` column family contains `referrer`, `origin`, or `server` as a column qualifier. Alternatively, this query can also be written as a series of individual comparisons such as `session['referrer'] IS NOT NULL OR session['origin'] IS NOT NULL`. However, for queries involving a large number of comparisons, the following approach is recommended.
    
    
      SELECT *
      FROM analytics
      WHERE
        _key LIKE 'com.abc%'
        AND ARRAY_INCLUDES_ANY(MAP_KEYS(session), ['referrer', 'origin', 'server'])
    

With the following query, you can retrieve the latest version of all columns for a given row key prefix if the `session` column family contains`referrer`, `origin`, and `server` as column qualifiers. Alternatively, this query can be written as a series of individual comparisons such as `session['referrer'] IS NOT NULL AND session ['origin'] IS NOT NULL`.
    
    
      SELECT *
      FROM analytics
      WHERE
        _key LIKE 'com.abc%'
        AND ARRAY_INCLUDES_ALL(MAP_KEYS(session), ['referrer', 'origin', 'server'])
    

With the following query, you can retrieve the latest version of all columns for a given row key prefix if the `session` column family contains `com.google.search`, `com.google.maps`, or `com.google.shopping` as values.
    
    
      SELECT *
      FROM analytics
      WHERE
        _key LIKE 'com.abc%'
        AND ARRAY_INCLUDES_ANY(
          MAP_VALUES(session),
          ['com.google.search', 'com.google.maps', 'com.google.shopping'])
    

With the following query, you can retrieve the latest version of all columns if key-value pairs in the `cell_plan` column family include both `data_plan:unlimited` and `roaming:North America`.
    
    
      SELECT *
      FROM analytics
      WHERE
        ARRAY_INCLUDES_ALL(
          CAST(
            MAP_ENTRIES(cell_plan)
            AS ARRAY<STRUCT<key STRING, value STRING>>),
          [('data_plan', 'unlimited'), ('roaming', 'North America')])
    

With the following query, you can retrieve the `row key` and `temperature` readings for weather sensors for cases where the temperature exceeded 70 degrees during the last seven measurements.
    
    
      SELECT
        _key AS sensorid,
        ARRAY_FILTER(
          CAST(
            sensor['temperature']
            AS ARRAY<STRUCT<timestamp TIMESTAMP, value STRING>>),
          e -> CAST(e.value AS FLOAT32) > 70) AS high_temperature
      FROM weather(with_history => TRUE, latest_n => 7)
    

In temporal filtering order, `latest_n` comes last, so a query like `after => X, before => y, latest_n => 3` returns the latest three values that satisfy the after and before conditions. If your use case requires `latest_n` to take precedence, you can provide `latest_n` as the only temporal filter, and then apply the rest of the temporal filters using query operators in your `SELECT` statement, as shown in the example. For more information, see [Temporal filters](https://docs.cloud.google.com/bigtable/docs/googlesql-overview#temporal-filters).
    
    
      SELECT
        ARRAY_FILTER(
          CAST(
            address['street']
            AS ARRAY<STRUCT<timestamp TIMESTAMP, value STRING>>),
          e -> e.timestamp > TIMESTAMP('2021-01-04T23:51:00.000Z'))
          AS street_address
      FROM locations(with_history => TRUE, latest_n => 3)
    

Similar to the previous example, you can apply a different temporal filter to each column family in your query. For example, the following query returns the three most recent versions of the `street` column and the two least recent versions of the `state` column.
    
    
      SELECT
        ARRAY_FILTER(
          CAST(
            address['street']
            AS ARRAY<STRUCT<timestamp TIMESTAMP, value STRING>>),
          (e, i) -> i <= 2)
          AS street_address,
        ARRAY_FILTER(
          ARRAY_REVERSE(
            CAST(
              address['state']
              AS ARRAY<STRUCT<timestamp TIMESTAMP, value STRING>>)),
          (e, i) -> i <= 1)
          AS state
      FROM locations(with_history => TRUE)
    

With the following query, you can retrieve all versions of all columns if key-value pairs in the address column family include both `city:Savannah` or `city:Nashville` at any point in time.
    
    
      SELECT *
      FROM locations(with_history => TRUE)
      WHERE
        ARRAY_LENGTH(
          ARRAY_FILTER(
            CAST(
              MAP_ENTRIES(address)
              AS ARRAY<
                STRUCT<
                  key STRING,
                  value ARRAY<STRUCT<timestamp TIMESTAMP, value STRING>>>>),
            e ->
              e.key = 'city'
              AND ARRAY_INCLUDES_ANY(
                ARRAY_TRANSFORM(e.value, k -> k.value), ['Savannah', 'Nashville'])))
        > 0
    

In this particular example, casting is not required, so this can also be written in the following shorter form.
    
    
      SELECT *
      FROM locations(with_history => TRUE)
      WHERE
        ARRAY_LENGTH(
          ARRAY_FILTER(
            MAP_ENTRIES(address),
            e ->
              e.key = 'city'
              AND ARRAY_INCLUDES_ANY(
                ARRAY_TRANSFORM(e.value, k -> k.value), ['Savannah', 'Nashville'])))
        > 0
    

## High-throughput SQL analysis with Data Boost

In the Enterprise Plus edition, for high-throughput, analytical workloads, you can use Data Boost to run queries that scan large amounts of data without impacting the performance of your production clusters. These queries are optimal for real-time analysis and generating insights from historical or time-series data. To run these queries, you must use an [application profile configured for Data Boost](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#create-data-boost-app-profile).

The following examples demonstrate SQL patterns for high-throughput analysis using serverless compute.

### Analyze historical time-series data

With Data Boost, you can retrieve the row keys and all versions of metrics for all rows in a table from the last 24 hours. The following query performs a full table scan, which is handled by an isolated serverless compute.
    
    
    SELECT _key, metrics
    FROM myTable(with_history => TRUE, after => TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR))
    

### Aggregate large datasets

The following query shows you how to calculate the total number of events for each device over a specific time range across the entire table.
    
    
    SELECT
      _key AS device_id,
      COUNT(events['event_type']) AS total_events
    FROM
      UNPACK((
        SELECT events['event_type']
        FROM sensor_data(with_history => TRUE, after => TIMESTAMP('2026-01-01T00:00:00Z'))
      ))
    GROUP BY
      Device_id;
    

### Large range scans

The following query shows you how to retrieve all columns for a large range of row keys. Using Data Boost ensures that this high-throughput request doesn't consume CPU resources on your cluster nodes.
    
    
    SELECT *
    FROM analytics
    WHERE _key >= 'user#000000' AND _key < 'user#999999'
    

## What's next

  * [Browse the GoogleSQL for Bigtable reference documentation.](https://docs.cloud.google.com/bigtable/docs/reference/sql/googlesql-reference-overview)
  * [Use the Bigtable Spark connector.](https://docs.cloud.google.com/bigtable/docs/use-bigtable-spark-connector)
  * [Manage row key schemas](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
