---
url: https://docs.cloud.google.com/bigtable/docs/asynchronous-secondary-index/
title: Create an asynchronous secondary index \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:58.132000+00:00
---

# Create an asynchronous secondary index  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/asynchronous-secondary-index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an asynchronous secondary index

You can use continuous materialized views as asynchronous secondary indexes for tables.

Before you read this page, familiarize yourself with [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views).

Data in a Bigtable table is typically indexed by [row keys](https://docs.cloud.google.com/bigtable/docs/schema-design#row-keys). However, you can create a continuous materialized view from a source table and use it as an asynchronous secondary index. This lets you retrieve the same data using different query lookup patterns by querying the materialized view.

An _asynchronous secondary index_ is a continuous materialized view that contains a subset of columns from a source table, along with a row key that is different from the row key in the source table. These row keys might be based on the following transformations that allow your application to retrieve the same data based on different query lookup patterns:

  * Attributes within the source table, such as column qualifiers, column values, or parts of the source row key.
  * A reformatting of the row key.
  * A transformation that combines the row key with an attribute.



Bigtable synchronizes asynchronous secondary indexes with the source table automatically in a way that is [eventually consistent](https://docs.cloud.google.com/bigtable/docs/replication-overview#consistency-model).

## When to use an asynchronous secondary index

Applications often need to query the same data using different lookup patterns or attributes. For example, consider an application that retrieves user information by either the email address or a phone number. You might want the same level of performance across both query patterns. If you make the email address your Bigtable row key and store telephone numbers in a column, then the performance of the phone number lookup is slower because it requires a full table scan.

To improve query performance when looking up by a telephone number, you can create a continuous materialized view with a SQL statement. The SQL statement instructs Bigtable how to restructure your data with a different row key. A continuous materialized view acts like a table that you can query. Then you use the view as an asynchronous secondary index. It gives your application another access path to the same data. Each path uses a different row key so you can choose an alternative path for each query. To choose the best path for your query, understand the structure of the row key for each table and the data that each table stores.

Using a continuous materialized view as an asynchronous secondary index can improve query performance in the following use cases:

  * **Rekeying your data** : If you need to query your data by using a different key than the source table's row keys, you can then create a continuous materialized view with the alternative key and query against that view.
  * **Filtering data** : If you want to filter the source table and populate only specific rows of data in the asynchronous secondary index, then provide a `WHERE` clause in the SQL query that defines the view.
  * **Attribute keys** : If you need to query your data based on a non-key attribute, such as a column qualifier or value, you can include it in your `ORDER BY` clause.



## About asynchronous secondary indexes

To use a continuous materialized view in Bigtable as an asynchronous secondary index, consider the following requirements:

  * The row key for a new asynchronous secondary index must include the row key of the source table to help ensure a one-to-one mapping between rows in the source table and rows in the asynchronous secondary index of the continuous materialized view.
  * The asynchronous secondary index doesn't have to have the same schema or attributes as the source table. In the `SELECT` part of the SQL query, you must specify which columns from the table are necessary and any SQL transformations of the data that you want to apply.
  * The asynchronous secondary index only needs to copy data that you need for the query pattern. Providing all the source data in the source table is not required.
  * In Bigtable, the row key that you choose provides the default sort order.



To query asynchronous secondary indexes, consider the following requirements:

  * Every column in the `ORDER BY` clause must also be included in the `SELECT` clause.
  * Once you define the asynchronous secondary index, your application must be able to choose between querying the source table or the materialized view that represents the asynchronous secondary index.
  * Applications don't write directly to the index, which continuously synchronizes with the source table. Always write to the source table.
  * The asynchronous secondary index is eventually consistent; data is written to the source table first and then transformed to the asynchronous secondary index format.
  * We recommend that you create a covering index. For more information, see the Covering indexes section of this document.
  * The `ORDER BY` clause must contain the unmodified row key of the source table, and all data must be sorted in an ascending order. The row key in the source table is always projected to the materialized view; however, it can be combined with other attributes.
  * The columns in the `ORDER BY` clause become part of the [structured row key](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas) of the asynchronous secondary index. All other selected columns become non-key column values in the asynchronous secondary index. If you convert a value in the `ORDER BY` clause to a specific [GoogleSQL for Bigtable](https://docs.cloud.google.com/bigtable/docs/googlesql-overview) data type, it retains its data type in the structured row key of the asynchronous secondary index.



## Covering indexes

A _covering index_ includes all the columns that your queries need. When you query a covering index, Bigtable can retrieve all the required data directly from the index, without having to access the source table. We recommend this approach for optimal performance because it minimizes the number of disk reads. To create a covering index, make sure that your `SELECT` statement specifies all the columns that you need in your queries.

When you want to create a non-covering index, query the index and then use the results to look up the additional columns that you need from the source table.

## Define an asynchronous secondary index

You create an asynchronous secondary index by [creating a continuous materialized view](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views) with a SQL query that defines the asynchronous secondary index.

In the following example, the SQL query creates an asynchronous secondary index that lets you query user interactions data. The `ORDER BY` clause defines the structured row key of the asynchronous secondary index, using a combination of the user's phone number, user ID, and email address. It also assigns the name `interactions` to the `activity` column family:
    
    
    SELECT
      user['phone'] AS phone,
      CAST(user['id'] AS INT64) AS user_id,
      _key AS email,
      activity AS interactions
    FROM CLICKS_TABLE
    ORDER BY 1, 2, 3;
    

The following table explains how the index is created by comparing the view of the same row in the source table with the corresponding asynchronous secondary index:

Source table row | Asynchronous secondary index row  
---|---  
Row key:   
`_key`: `user1@example.com`  
  
  
  
Attributes:   
`user`: `{id: "123", phone: "555-123-4567"}`   
`activity`: `{action: "CLICKED_PRODUCT_A"}` | Structured row key:   
`phone`: `555-123-4567`   
`user_id`: `123`   
`email`: `user1@example.com`   
  
Attribute:   
`interactions`: `{action: "CLICKED_PRODUCT_A"}`  
Row key:   
`_key`: `user2@example.com`  
  
  
  
Attributes:   
`user`: `{id: "456", phone: "555-987-6543"}`   
`activity`: `{action: "VIEWED_PRODUCT_B"}` | Structured row key:   
`phone`: `555-987-6543`   
`user_id`: `456`   
`email`: `user2@example.com`   
  
Attribute:   
`interactions`: `{action: "VIEWED_PRODUCT_B"}`  
Row key:   
`_key`: `user3@example.com`  
  
  
  
Attributes:   
`user`: `{id: "1000", phone: "555-111-2222"}`   
`activity`: `{action: "ADDED_TO_CART_PRODUCT_C"}` | Structured row key:   
`phone`: `555-111-2222`   
`user_id`: `1000`   
`email`: `user3@example.com`   
  
Attribute:   
`interactions`: `{action: "ADDED_TO_CART_PRODUCT_C"}`  
  
## Limitations

  * To read the output key, which is the asynchronous secondary index key, you can only use SQL queries.



## What's next

  * [Asynchronous secondary index queries](https://docs.cloud.google.com/bigtable/docs/asynchronous-secondary-index-queries)
  * [Continuous materialized view queries](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries)
  * [Create and manage continuous materialized views](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views)
  * [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design)
  * [Manage row key schemas](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas)
  * [Distributed counting in Bigtable](https://cloud.google.com/blog/products/databases/distributed-counting-with-bigtable)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
