---
url: https://docs.cloud.google.com/bigtable/docs/filters/
title: Filters \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:08.242301+00:00
---

# Filters  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Filters

When you read data from Bigtable, you can read specific rows or ranges of rows. However, you don't always need all of the data in all of the rows. You might only need rows that contain a specific value in their row key, or cells within a specific column family.

To limit the results of a read request, include _filters_ in the request. A filter is applied to the data before the response is sent, reducing the amount of data that is returned. As result, using filters can mean lower network costs and faster throughput. This page provides an overview of how Bigtable filters work and a list of available filters.

For details and code samples for each filter, see [Filter examples](https://docs.cloud.google.com/bigtable/docs/using-filters).

**Note:** The HBase client for Java uses HBase's filter APIs instead of the Bigtable Data API. To learn about HBase's filter APIs, see the [HBase documentation](https://hbase.apache.org/book.html#client.filter). 

## How filters work

When your read request includes a filter, Bigtable retrieves a row or a range of rows from your table. For each of the _input rows_ that it retrieves, Bigtable evaluates the row using your filter, then generates an _output row_ based on the filter results.

Bigtable provides several types of filters, as described in the following sections. Basic filters fall under two categories: _limiting_ and _modifying_. You can combine basic filters into _composing_ filters.

In most cases, a filter is applied to _all rows_ unless you specify row key, row range, or number of rows that the filter should be applied to. One exception is the [row key regex](https://docs.cloud.google.com/bigtable/docs/using-filters#row-key-regex) filter, which can restrict the row range in certain cases if the regex is a fixed prefix. In general, to avoid the slowness of a full table scan, always specify the rows for a filter.

### Limiting filters

A _limiting filter_ controls which rows or cells are included in the response, based on whether they match specific criteria. For example, you can say that the response should include only rows in which the row key matches a regular expression, or that you want only cells from a specific column family.

Many limiting filters can exclude cells from an output row. If all of the cells are excluded from an output row, the row is not included in the response.

See the Summary of filters for a complete list of limiting filters.

### Modifying filters

A _modifying filter_ affects the data or metadata for individual cells.

**Note:** Modifying filters affect the data that is returned in the read request, _not_ the data in the table.

Bigtable provides the following modifying filters:

  * The [**strip value filter**](https://docs.cloud.google.com/bigtable/docs/using-filters#strip-value), which replaces each cell's value with an empty string. This filter is useful when you only need the number of rows or the list of row keys that meet your criteria, rather than the data from those rows.

  * The [**apply label filter**](https://docs.cloud.google.com/bigtable/docs/using-filters#apply-label), which applies a label to each cell to identify which filter produced each cell in the response. Your application can use these labels to perform additional filtering on the client side.




### Composing filters

A _composing filter_ allows you to combine multiple basic filters into one, which makes it possible to apply more than one filter to a single read request. For example, to get CPU usage data for your servers, you could use one filter to include only rows where the row key starts with `SERVER`, followed by a second filter to include only cells within the `CPU` column family.

Bigtable provides the following composing filters:

  * A [**chain**](https://docs.cloud.google.com/bigtable/docs/using-filters#chain), which applies a sequence of filters to each input row and returns an output row. A chain filter is like using a logical AND.
  * An [**interleave**](https://docs.cloud.google.com/bigtable/docs/using-filters#interleave), which sends each input row through multiple filters, then combines all of the filter results for the input row into a single output row. An interleave filter is like using a logical OR.
  * A [**condition**](https://docs.cloud.google.com/bigtable/docs/using-filters#condition), which generates an output row by applying one of two possible filters to the input row. The filter is chosen by applying a predicate filter to the input row, then checking to see whether the predicate filter's output row contains any cells.



## Filters and performance

Filters allow you to retrieve only the data you actually need. As a result, filters can improve performance by reducing the amount of data that is sent to your application.

However, filters are not an all-purpose solution to every performance issue. In general, filters should be used to control _throughput efficiency_ , not to reduce the latency between sending a request and receiving a response. Used correctly, filters can be an effective part of a strategy to [improve read performance](https://docs.cloud.google.com/bigtable/docs/reads#performance).

The [conditions](https://docs.cloud.google.com/bigtable/docs/using-filters#condition) filter, in particular, can increase latency, because conditions are much slower than other filters. If your read request is extremely performance-sensitive, do not use conditions in the request.

**Warning:** Using a regex rowkey filter without also specifying a start, end, prefix, or number of rows results in a full table scan, which can be slow.

## Summary of filters

The following tables list the filters that Bigtable provides, including links to details and code samples for each filter.

Limiting filters  
---  
[Block all](https://docs.cloud.google.com/bigtable/docs/using-filters#block-all) |  Don't emit any cells. Mostly useful for debugging.   
[Cells per column limit](https://docs.cloud.google.com/bigtable/docs/using-filters#cells-per-column-limit) |  Include only the _N_ most recent versions of a column in a row.   
[Cells per row limit](https://docs.cloud.google.com/bigtable/docs/using-filters#cells-per-row-limit) |  Include only the first _N_ cells from a row.   
[Cells per row offset](https://docs.cloud.google.com/bigtable/docs/using-filters#cells-per-row-offset) |  Omit the first _N_ cells from a row.   
[Column family regex](https://docs.cloud.google.com/bigtable/docs/using-filters#column-family-regex) |  Include only cells whose column family matches an [RE2](https://github.com/google/re2/blob/master/doc/syntax.txt) regular expression.   
[Column qualifier regex](https://docs.cloud.google.com/bigtable/docs/using-filters#column-qualifier-regex) |  Include only cells whose column qualifier matches a regular expression.   
[Column range](https://docs.cloud.google.com/bigtable/docs/using-filters#column-range) |  Include only cells in a specific column family whose column qualifier is within a specific range.   
[Pass all](https://docs.cloud.google.com/bigtable/docs/using-filters#pass-all) |  Emit all input cells. Mostly useful for debugging.   
[Row key regex](https://docs.cloud.google.com/bigtable/docs/using-filters#row-key-regex) |  Include only cells whose row key matches a regular expression.   
[Row sample](https://docs.cloud.google.com/bigtable/docs/using-filters#row-sample) |  Retrieve a random sample of rows.   
[Sink](https://docs.cloud.google.com/bigtable/docs/using-filters#sink) |  Include cells in the final output row, and prevent them from being modified or removed by a subsequent filter.   
[Timestamp range](https://docs.cloud.google.com/bigtable/docs/using-filters#timestamp-range) |  Include only cells whose timestamp falls within a specific range.   
[Value range](https://docs.cloud.google.com/bigtable/docs/using-filters#value-range) |  Include only cells whose value falls within a specific range.   
[Value regex](https://docs.cloud.google.com/bigtable/docs/using-filters#value-regex) |  Include only cells whose value matches a regular expression.   
Modifying filters  
---  
[Apply label](https://docs.cloud.google.com/bigtable/docs/using-filters#apply-label) |  Add a label to all cells.   
[Strip value](https://docs.cloud.google.com/bigtable/docs/using-filters#strip-value) |  Return an empty string for each cell value.   
Composing filters  
---  
[Chain](https://docs.cloud.google.com/bigtable/docs/using-filters#chain) |  Apply multiple filters in order.   
[Condition](https://docs.cloud.google.com/bigtable/docs/using-filters#condition) |  Apply one of two possible filters to a row.   
[Interleave](https://docs.cloud.google.com/bigtable/docs/using-filters#interleave) |  Combine output rows from multiple filters into a single output row.   
  
## What's next

  * [See samples of read requests.](https://docs.cloud.google.com/bigtable/docs/reads)
  * [Explore samples of write requests.](https://docs.cloud.google.com/bigtable/docs/writes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
