---
url: https://docs.cloud.google.com/bigtable/docs/query-stats/
title: Get query stats \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:23.207996+00:00
---

# Get query stats  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/query-stats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get query stats

This page describes how to get _query stats_ using the `cbt` CLI . You can also get query stats using the Go client library for Cloud Bigtable.

The content provided here is intended for application developers. Before you read this page, you should understand the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/com/bigtable/docs/overview#storage-model). You should also be familiar with [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design) and [understand performance](https://docs.cloud.google.com/bigtable/docs/schema-design).

The ability to get information about a Bigtable query can be useful when you are developing an application. It lets you get data on a query's performance and then adjust the query or change your schema design to fine-tune the performance of your query.

Although in general a _query_ is any data request sent to a table, Bigtable returns query statistics only for read requests.

## Before you begin

  1. If you haven't already installed the `cbt` CLI , follow the instructions on the [ `cbt` CLI overview](https://docs.cloud.google.com/bigtable/docs/cbt-overview) including the steps to create a `.cbtrc` file.
  2. Review the [Read rows](https://docs.cloud.google.com/bigtable/docs/cbt-reference#read_rows) section of the `cbt` CLI reference to familiarize yourself with the command-line syntax and options available for sending a `cbt read` request to your table. Note that the `cbt` CLI does not support filters.
  3. Ensure that you have `bigtable.tables.readRows` permission for the table or that you are a principal of the `bigtable.reader` role.



## Run your query

  1. Create a query using the syntax for [Read rows](https://docs.cloud.google.com/bigtable/docs/cbt-reference#read_rows).

  2. Run the following command. The `include-stats=full` parameter tells Bigtable to return the query stats.
         
         cbt read TABLE_ID QUERY include-stats=full
         

Replace the following:

     * `TABLE_ID`: the unique ID for the table that you are querying
     * `QUERY`: a `cbt` CLI -formatted query

The terminal displays the data that was read and a list containing the following stats:

     * `rows_seen_count`: the number of rows that Bigtable processed for the request
     * `rows_returned_count`: the number of rows returned after applying filters
     * `cells_seen_count`: the number of cells processed for the request
     * `cells_returned_count`: the number of cells returned after applying filters
     * `frontend_server_latency`: request latency measured from the Bigtable front-end server pool, expressed in milliseconds



## Interpret the results

  * Look at the ratio of cells seen to cells returned. If the quotient for `cells_seen_count` / `cells_returned_count` is 1 or close to 1, that's an indication that your query didn't cause Bigtable to process data that was ultimately filtered out.

  * Consider the number of rows returned. The higher that number is, the more work that Bigtable is doing. The optimal number here is dependent on your use case and latency requirements, but in general, a query that returns fewer rows will have lower latency.




## Example

If you want to get query stats when you read all rows that match the regular expression `orange:*.*` in a table called `my-table`, you can run the following:
    
    
    cbt read my-table regex='.*orange' columns='.*:.*' include-stats=full
    

The output is similar to the following:
    
    
      ----------------------------------------
      orange
        Details:Color                            @ 2022/09/26-14:48:01.286000
          "orange"
        Details:Size                             @ 2022/09/26-14:48:01.286000
          "medium"
    
      Request Stats
      ====================
      rows_seen_count: 10
      rows_returned_count : 1
      cells_seen_count: 2
      cells_returned_count: 2
      frontend_server_latency: 13ms
    

## What's next

  * [Identify a cluster's hot tablets.](https://docs.cloud.google.com/bigtable/docs/hot-tablets)
  * [Review schema design best practices.](https://docs.cloud.google.com/bigtable/docs/schema-design)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
