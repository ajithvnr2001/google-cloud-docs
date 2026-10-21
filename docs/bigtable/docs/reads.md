---
url: https://docs.cloud.google.com/bigtable/docs/reads/
title: Reads \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:16.014146+00:00
---

# Reads  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Reads

**Note:** This page includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

This page describes the types of read requests you can send to Bigtable, discusses performance implications, and presents a few recommendations for specific types of queries. Before you read this page, you should be familiar with [the overview of Bigtable](https://docs.cloud.google.com/bigtable/docs/overview).

## Overview

Read requests to Bigtable stream back the contents of the requested rows in key order, meaning they are returned in the order in which they are stored. You are able to read any writes that have returned a response.

The queries that your table supports should help determine the type of read that is best for your use case. Bigtable read requests fall into two general categories:

  * Reading a single row
  * Scans, or reading multiple rows



Reads are atomic at the row level. This means that when you send a read request for a row, Bigtable returns either the entire row or, in the event the request fails, none of the row. A partial row is never returned unless you specifically request one.

We strongly recommend that you use our Cloud Bigtable [client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries) to read data from a table instead of calling the API directly. [Code samples](https://docs.cloud.google.com/bigtable/docs/reading-data) showing how to send read requests are available in multiple languages. All read requests make the `ReadRows` API call.

## Reading data with Data Boost serverless compute

Bigtable Data Boost lets you run high-throughput read jobs without affecting serving path application traffic. Data Boost is a serverless compute service that you can use to read your Bigtable data while your core application uses your cluster's nodes for compute. Enterprise Plus extends Data Boost query capability with SQL support and access to HDD and tiered storage data.

Data Boost is ideal for scans and is not recommended for single-row reads. You can't use Data Boost for reverse scans. For more information and eligibility criteria, see [Data Boost overview](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).

## Single-row reads

You can request a single row based on the row key. Single-row reads, also known as _point reads_ , are not compatible with [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview). Code samples are available for the following variations:

  * [Reading a single row](https://docs.cloud.google.com/bigtable/docs/reading-data#single-row)
  * [Reading a partial row by specifying columns](https://docs.cloud.google.com/bigtable/docs/reading-data#partial-row)
  * [Reading multiple rows](https://docs.cloud.google.com/bigtable/docs/reading-data#multiple-rows)



## Scans

Scans are the most common way to read Bigtable data. You can read a range of contiguous rows or multiple ranges of rows from Bigtable, by specifying a row key prefix or specifying beginning and ending row keys. Code samples are available for the following variations:

  * [Reading a range of rows](https://docs.cloud.google.com/bigtable/docs/reading-data#row-range)
  * [Reading multiple ranges of rows](https://docs.cloud.google.com/bigtable/docs/reading-data#multi-row-range)
  * [Reading multiple rows using a key prefix](https://docs.cloud.google.com/bigtable/docs/reading-data#prefix)



## Reverse scans

Reverse scans let you read a range of rows backwards either by specifying a row key prefix or a range of rows. The row key prefix is used as the initiating point of scan to read backwards. If you specify a range of rows, the end row key is used as the initiating point of scan.

**Note:** If you are using the HBase client libraries and scanning a range of rows in reverse, specify the start row key as the initiating point of scan.

Scanning in reverse order can be useful for the following scenarios:

  * You want to find an event (row) and then read the previous N number of events.
  * You want to find the highest value prior to a given value. This can be helpful when you store time series data [using a timestamp as a row key suffix](https://docs.cloud.google.com/bigtable/docs/schema-design#time-based).



Reverse scans are less efficient than forward scans. In general, design your row keys so that most scans are forward. Use reverse scans for short scans, such as 50 rows or less, to maintain low-latency response time.

To scan in reverse, you set the value for the `ReadRowsRequest` field `reversed` to true. The default is false.

Reverse scans are available when you use the following client libraries:

  * Bigtable client library for C++ version 2.18.0 or later
  * Bigtable client library for Go version 1.21.0 or later
  * Bigtable client library for Java version 2.24.1 or later
  * Bigtable HBase client for Java version 2.10.0 or later



For code samples demonstrating how to use reverse scans, see [Scan in reverse](https://docs.cloud.google.com/bigtable/docs/reading-data#reverse-scan).

### Use case examples

The following examples show how reverse scans can be used to find the last time a customer changed their password and price fluctuations for a product around a particular day.

#### Password resets

Consider an assumption that your row keys each contain a customer ID and a date, in the format `123ABC#2022-05-02`, and one of the columns is `password_reset`, which stores the hour when the password was reset. Bigtable automatically stores the data lexicographically, like the following. Note that the column does not exist for rows (days) when the password was not reset.
    
    
    `123ABC#2022-02-12,password_reset:03`
    `123ABC#2022-04-02,password_reset:11`
    `123ABC#2022-04-14`
    `123ABC#2022-05-02`
    `223ABC#2022-05-22`
    

If you want to find the last time that customer `123ABC` reset their password, you can scan in reverse a range of `123ABC#` to `123ABC#<DATE>`, using today's date or a date in the future, for all rows that contain the column `password_reset` with a row limit of 1.

#### Price changes

In this example, your row keys contain values for product, model, and timestamp, and one of the columns contains the price for the product and model at a given time.
    
    
    `productA#model2#1675604471,price:82.63`
    `productA#model2#1676219411,price:82.97`
    `productA#model2#1677681011,price:83.15`
    `productA#model2#1680786011,price:83.99`
    `productA#model2#1682452238,price:83.12`
    

If you want to find price fluctuations surrounding the price on February 14, 2023, even though a row key for that particular date doesn't exist in the table, you can do a forward scan starting from row key `productA#model2#1676376000` for N number of rows, and then do a reverse scan for the same number of rows from the same starting row. The two scans give you the prices before and after the given time.

## Filtered reads

If you only need rows that contain specific values, or partial rows, you can use a filter with your read request. Filters allow you to be highly selective in the data that you want.

Filters also let you make sure that reads match the [garbage collection policies](https://docs.cloud.google.com/bigtable/docs/garbage-collection) that your table is using. This is particularly useful if you frequently write new timestamped cells to existing columns. Because garbage collection can take up to a week to remove expired data, using a timestamp range filter to read data can ensure you don't read more data than you need.

The [overview of filters](https://docs.cloud.google.com/bigtable/docs/filters) provides detailed explanations of the types of filters that you can use. [Using filters](https://docs.cloud.google.com/bigtable/docs/using-filters) shows examples in multiple languages.

## Read data from an authorized view

To read data from an authorized view, you must use one of the following:

  * gcloud CLI
  * Bigtable client for Java



The other Bigtable client libraries don't yet support view access.

Any method that calls the `ReadRows` or `SampleRowKeys` method of the Bigtable Data API is supported. You provide the authorized view ID in addition to the table ID when you create your client.

## Read data from a continuous materialized view

You can read data from a [continuous materialized view](https://docs.cloud.google.com/bigtable/docs/materialized-views) using SQL or the `ReadRows` Data API call. Continuous materialized views are read-only. Data in a materialized view is typed based on the [query that defines it](https://docs.cloud.google.com/bigtable/docs/\(/bigtable/docs/continuous-materialized-view-queries\)).

### SQL

To read data from a continuous materialized view using SQL, you can use either the Bigtable Studio query editor or one of the [client libraries that support SQL queries](https://docs.cloud.google.com/bigtable/docs/googlesql-overview#client-libraries).

SQL automatically exposes query results as typed columns, so there's no need to handle encoding in your query.

When you create a continuous materialized view, Bigtable automatically creates a [row key schema](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas) for the table that defines the structured row keys for the view. For more information about querying structured row keys with SQL, see [Structured row key queries](https://docs.cloud.google.com/bigtable/docs/structured-row-keys).

#### Read data during initial population

When you create a continuous materialized view on an existing table, Bigtable starts an initial population process that copies existing table data into the view.

By default, to help ensure data correctness, Bigtable rejects read requests that attempt to read from a continuous materialized view while the view is being created. If you query a view that's still populating, then Bigtable returns the `Materialized view is still creating.` error. The error has a `FAILED_PRECONDITION` status code.

If your application can tolerate incomplete data, then you can opt in to read from the view before the initial population finishes. To read from a continuous materialized view during the initial population, add the `allow_incomplete_view=true` statement-level query hint to your SQL query:
    
    
    SELECT key_part FROM `VIEW_ID` @{allow_incomplete_view=true}
    

Replace `VIEW_ID` with the unique identifier of your continuous materialized view.

**Caution:** When you use the `allow_incomplete_view=true` query hint, Bigtable returns only the data that has been processed so far. Query results might be incomplete and are subject to change as the initial population progresses. If the view performs aggregation, then the returned aggregates might reflect only some of the data.

For more information, see [Creating continuous materialized views on existing tables](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views#cmv-on-table).

### Data API

If you plan to read from a continuous materialized view with a `ReadRows` call from one of the client libraries for Bigtable, you should review the SQL query used to define the view. Take note of whether the view has a defined `_key` column, which is recommended for views that are meant to be read using `ReadRows`, and if it has a `_timestamp` column.

You also must know each column's type and decode the column data in your application code.

Aggregated values in a continuous materialized view are stored using encoding described in the following table, based on the output type of the column from the view definition. 

**Type** | **Encoding**  
---|---  
BOOL | 1 byte value, 1 = true, 0 = false  
BYTES | No encoding  
INT64 (or INT, SMALLINT, INTEGER, BIGINT, TINYINT, BYTEINT) | 64-bit big-endian  
FLOAT64 | 64-bit IEEE 754, excluding NaN and +/-inf  
STRING | UTF-8  
TIME/TIMESTAMP | 64-bit integer representing the number of microseconds since the Unix epoch (consistent with GoogleSQL)  
For more information, see [ Encoding](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#encoding_1) in the Data API reference. 

In addition to knowing the type for each column in the view, you need to know the column family and column qualifier. The default column family is called `default`, and the column qualifier is the alias specified in the defining query. For example, consider a continuous materialized view defined with this query:
    
    
    SELECT
      _key,
      SUM(clicks) AS sum_clicks
    FROM
      mytable
    GROUP BY
      sum_clicks
    

When you query the view with `ReadRows` you provide the column family `default` and the column qualifier `sum_clicks`.

## Reads and performance

Reads that use filters are slower than reads without filters, and they increase CPU utilization. On the other hand, they can significantly reduce the amount of network bandwidth that you use, by limiting the amount of data that is returned. In general, filters should be used to control _throughput efficiency_ , not latency.

If you want to optimize your read performance, consider the following strategies:

  1. **Restrict the rowset as much as possible.** Limiting the number of rows that your nodes have to scan is the first step toward improving time to first byte and overall query latency. If you don't restrict the rowset, Bigtable will almost certainly have to scan your entire table. This is why we recommend that you [design your schema](https://docs.cloud.google.com/bigtable/docs/schema-design) in a way that allows your most common queries to work this way.

  2. For additional performance tuning after you've restricted the rowset, try adding a **basic filter**. Restricting the set of columns or the number of versions returned generally doesn't increase latency and can sometimes help Bigtable seek more efficiently past irrelevant data in each row.

  3. If you want to fine-tune your read performance even more after the first two strategies, consider using a more **complicated filter**. You might try this for a few reasons:

     * You're still getting back a lot of data you don't want.
     * You want to simplify your application code by pushing the query down into Bigtable.

Be aware, however, that filters requiring conditions, interleaves, or regular expression matching on large values tend to do more harm than good if they allow most of the scanned data through. This harm comes in the form of increased CPU utilization in your cluster without large savings client-side.




In addition to these strategies, **avoid reading a large number of non-contiguous row keys or row ranges in a single read request.** When you request hundreds of row keys or row ranges in a single request, Bigtable scans the table and reads the requested rows sequentially. This lack of parallelism affects the _overall_ latency, and any reads that hit a [hot node](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cpu) can increase the _tail_ latency. The more row ranges requested, the longer the read takes to complete. If this latency is unacceptable, you should instead send multiple concurrent requests that each retrieve fewer row ranges.

**Tip:** We recommend that a `ReadRows` read request should contain up to 100 row keys.

In general, reading more row ranges in a single request optimizes throughput, but not latency. Reading fewer row ranges in multiple concurrent requests optimizes latency, but not throughput. Finding the right balance between latency and throughput will depend on your application's requirements, and can be arrived at by adjusting the concurrent read request count and the number of row ranges in one request.

## Large rows

Bigtable enforces the following limits that apply to large rows:

  * 256 MB is the maximum size of a row. If you need to read a row that has grown larger than the limit, you can paginate your request and use a [`cells per row limit` filter](https://docs.cloud.google.com/bigtable/docs/using-filters#cells-per-row-limit) and a [`cells per row offset` filter](https://docs.cloud.google.com/bigtable/docs/using-filters#cells-per-row-offset). Be aware that if a write arrives for the row between the paginated read requests, the read might not be atomic.

  * 512 KB is the maximum size of a `ReadRows` API call. If you exceed the limit, Bigtable returns an `INVALID_ARGUMENT` error.




## What's next

  * [Implement counters by using aggregate cells.](https://docs.cloud.google.com/bigtable/docs/aggregates)
  * [Read an overview of filters.](https://docs.cloud.google.com/bigtable/docs/filters)
  * [Look at code samples showing how to use filters.](https://docs.cloud.google.com/bigtable/docs/using-filters)
  * [Read about the types of write requests you can send to Bigtable.](https://docs.cloud.google.com/bigtable/docs/writes)
  * [Use the Bigtable emulator.](https://docs.cloud.google.com/bigtable/docs/emulator)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
