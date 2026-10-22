---
url: https://docs.cloud.google.com/bigtable/docs/schema-design-time-series/
title: Schema design for time series data \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:42.244781+00:00
---

# Schema design for time series data  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/schema-design-time-series/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Schema design for time series data

This page describes schema design patterns for storing time series data in Bigtable. This page builds on [Designing your schema](https://docs.cloud.google.com/bigtable/docs/schema-design) and assumes you are familiar with the concepts and recommendations described on that page.

A time series is a collection of data that consists of measurements and the times when the measurements are recorded. Examples of time series include the following:

  * The plot of memory usage on your computer
  * Temperature over time on a news report
  * Stock market prices over a period of time



A good schema results in excellent performance and scalability, and a bad schema can lead to a poorly performing system. However, no single schema design provides the best fit for all use cases.

The patterns described on this page provide a starting point. Your unique dataset and the queries you plan to use are the most important things to consider as you design a schema for your time-series data.

The basic design patterns for storing time-series data in Bigtable are as follows:

  * Rows are time buckets

    * New columns for new events
    * New cells for new events
  * Rows represent single timestamps

    * Serialized column data
    * Unserialized column data



## Data for examples

To illustrate the differences between patterns, the examples on this page assume that you are storing data for an app that records the measurements that weather balloons take once every minute. We use _event_ to mean a single request that writes one or multiple cells at the same time. Location IDs correspond with Google Cloud regions.

Measurement | Example  
---|---  
  
  1. Timestamps on this page are formatted like `tYYYY-MM-DD-HHMM` for human readability. In a production table, timestamps are usually expressed as the number of microseconds since 1970-01-0100:00:00 UTC, like `1616264288050807`. 

  
Pressure (pascals) | 94587  
Temperature (Celsius) | 9.5  
Humidity (percentage) | 65  
Altitude (meters) | 601  
Related data | Example  
Balloon ID | 3698  
Location | asia-southeast1  
Timestamp1 | t2021-03-05-1204  
  
## Time buckets

In a time bucket pattern, each row in your table represents a "bucket" of time, such as an hour, day, or month. A row key includes a non-timestamp identifier, such as `week49`, for the time period recorded in the row, along with other identifying data.

The size of the bucket that you use — such as minute, hour, or day — depends on the queries that you plan to use and on [Bigtable data size limits](https://docs.cloud.google.com/bigtable/quotas#limits-data-size). For example, if rows that contain an hour of data are bigger the recommended maximum size per row of 100 MB, then rows that represent a half hour or a minute are probably a better choice.

**Advantages** of time bucket patterns include the following:

  * You'll see better [performance](https://docs.cloud.google.com/bigtable/docs/performance). For example, if you store 100 measurements, Bigtable writes and reads those measurements faster if they are in one row than if they are in 100 rows.

  * Data stored in this way is compressed more efficiently than data in tall, narrow tables.




**Disadvantages** include the following:

  * Time-bucket schema design patterns are more complicated than single-timestamp patterns and can take more time and effort to develop.



### Adding new columns for new events

In this time bucket pattern, you write a new column to a row for each event, storing the _data in the column qualifier rather than as a cell value_. This means that for each cell, you send the column family, column qualifier, and timestamp, but no value.

Using this pattern for the sample weather balloon data, each row contains all the measurements for a single metric, such as `pressure`, for a single weather balloon, over the course of a week. Each row key contains the location, balloon ID, metric that you are recording in the row, and a week number. Every time a balloon reports its data for a metric, you add a new column to the row. The column qualifier contains the measurement, the pressure in Pascals, for the minute identified by the cell timestamp.

In this example, after three minutes a row might look like this:

Row key | 94558 | 94122 | 95992  
---|---|---|---  
us-west2#3698#pressure#week1 | "" (t2021-03-05-1200) | "" (t2021-03-05-1201) | "" (t2021-03-05-1202)  
  
**Use cases** for this pattern include the following:

  * You don't need to measure changes in your time series data.

  * You want to save storage space by [using column qualifiers as data](https://docs.cloud.google.com/bigtable/docs/schema-design#columns).




### Adding new cells for new events

In this time bucket pattern, you add new cells to existing columns when you write a new event. This pattern lets you take advantage of Bigtable's ability to let you store multiple timestamped cells in a given row and column. It's important to specify garbage collection rules when you use this pattern.

Using the weather balloon data as an example, each row contains all the measurements for a single weather balloon over the course of a week. The row key prefix is an identifier for the week, so you can read an entire week's worth of data for multiple balloons with a single query. The other row key segments are the location where the balloon operates and the ID number for the balloon. The table has one column family, `measurements`, and that column family has one column for each type of measurement: `pressure`, `temperature`, `humidity`, and `altitude`.

Every time a balloon sends its measurements, the application writes new values to the row that holds the current week's data for the balloon, writing additional timestamped cells to each column. At the end of the week, each column in each row has one measurement for each minute of the week, or 10,080 cells (if your garbage collection policy allows it).

Each column in each row holds a measurement for each minute of the week. In this case, after three minutes, the first two columns in a row might look like this:

Row key | pressure | temp  
---|---|---  
asia-south2#3698#week1 | 94558 (t2021-03-05-1200) | 9.5 (t2021-03-05-1200)  
94122 (t2021-03-05-1201) | 9.4 (t2021-03-05-1201)  
95992 (t2021-03-05-1202) | 9.2 (t2021-03-05-1202)  
  
**Use cases** for this pattern include the following:

  * You want to be able to measure changes in measurements over time.



## Single-timestamp rows

In this pattern, you create a row for each new event or measurement instead of adding cells to columns in existing rows. The row key suffix is the timestamp value. Tables that follow this pattern tend to be _tall and narrow_ , and each column in a row contains only one cell.

**Important:** To avoid hotspots, _never_ use a timestamp value as a row key prefix.

### Single-timestamp serialized

In this pattern, you store all the data for a row in a single column in a serialized format such as JSON or a protocol buffer (protobuf). This approach is described in more detail on [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design#protobuf-data).

For example, if you use this pattern to store the weather balloon data, your table might look like this after four minutes:

Row key | measurements_blob  
---|---  
us-west2#3698#2021-03-05-1200 | _protobuf_1_  
us-west2#3698#2021-03-05-1201 | _protobuf_2_  
us-west2#3698#2021-03-05-1202 | _protobuf_3_  
us-west2#3698#2021-03-05-1203 | _protobuf_4_  
  
**Advantages** of this pattern include the following:

  * Storage efficiency

  * Speed




**Disadvantages** include the following:

  * If you don't use the SQL querying features of Bigtable for JSON or protocol buffers, you are unable to retrieve only specific fields when you read the data and must instead read all data for a given cell.

  * The need to deserialize the data after it's read




**Use cases** for this pattern include the following:

  * You almost always need to retrieve all measurements for a given event at the same time.

  * You prioritize storage efficiency because you almost always retrieve all measurements for a given event at the same time. While you can use Bigtable's SQL capabilities to filter data server-side, this pattern is most beneficial when you don't need to filter frequently.

  * Each event contains so many measurements that you might exceed the 100 MB per-row limit if you store the data in multiple columns.




### Single-timestamp unserialized

In this pattern, you store each event in its own row, even if you are recording only one measurement. The data in the columns is not serialized.

**Advantages** of this pattern include the following:

  * It is generally easier to implement than a time-bucket pattern.

  * You might spend less time [refining your schema](https://docs.cloud.google.com/bigtable/docs/schema-design-steps#refine) before using it.




**Disadvantages** of this pattern often outweigh the advantages:

  * Bigtable is less performant with this pattern.

  * Data stored this way is not as efficiently compressed as data in wider columns.

  * Even when the timestamp is at the end of the row key, this pattern can result in hotspots.




**Use cases** for this pattern include the following:

  * You want to always retrieve all columns but only a specified range of timestamps, but you have a reason not to store the data in a serialized structure.

  * You want to store an unbounded number of events.




Using the weather balloon example data, the column family and column qualifiers are the same as the example using time buckets and new cells. In this pattern, however, every set of reported measurements for each weather balloon is written to a _new row_. The following table shows five rows that are written using this pattern:

Row key | pressure | temperature | humidity | altitude  
---|---|---|---|---  
us-west2#3698#2021-03-05-1200 | 94558 | 9.6 | 61 | 612  
us-west2#3698#2021-03-05-1201 | 94122 | 9.7 | 62 | 611  
us-west2#3698#2021-03-05-1202 | 95992 | 9.5 | 58 | 602  
us-west2#3698#2021-03-05-1203 | 96025 | 9.5 | 66 | 598  
us-west2#3698#2021-03-05-1204 | 96021 | 9.6 | 63 | 624  
  
## Additional strategies

If you need to send multiple different queries for the same dataset, consider storing your data in multiple tables, each with a row key designed for one of the queries.

You can also combine patterns in some cases. For example, you can store serialized data in rows that represent time buckets, as long as you don't let the rows become too big.

## What's next

  * Review the steps involved in [planning a schema](https://docs.cloud.google.com/bigtable/docs/schema-design-steps).
  * Understand the [best practices for designing a schema](https://docs.cloud.google.com/bigtable/docs/schema-design).
  * Read about [the performance you can expect from Bigtable](https://docs.cloud.google.com/bigtable/docs/performance).
  * Explore the diagnostic capabilities of [Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
