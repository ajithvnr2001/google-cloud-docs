---
url: https://docs.cloud.google.com/bigtable/docs/query-builder/
title: Build queries in the console \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:08.666671+00:00
---

# Build queries in the console  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/query-builder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build queries in the console

You can query and view your Bigtable data by using the Bigtable Studio _query builder_. The query builder is an interactive form in the Google Cloud console that lets you build a query, run it against a table, and then view the results in the console.

The Bigtable Studio query builder lets you use drop-down selectors to specify a combination of query clauses without needing to write an application or use a CLI. When you run the query, the console makes a call to the Bigtable Data API, which returns data that matches your query.

**Note:** The query builder does not create SQL statements. For information on creating and running SQL statements that you can run in the Bigtable query editor, see [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).

This document describes how to use the query builder and offers tips on optimizing your queries. Before you read this page, you should be familiar with the [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview) .

Queries run in the query builder are subject to the same pricing and quotas as any other query sent to a table.

## When to use the query builder

The ability to query your Bigtable data in the Google Cloud console is helpful when you need to do the following:

  * Quickly get a visual representation of your table's schema.
  * Verify that certain data was successfully written.
  * Validate data integrity during a migration.
  * Debug possible data issues.
  * Preview the results that a specific combination of clauses returns before you use them in your code. This can be especially helpful for new Bigtable users as well as experienced users who don't want to use the `cbt` CLI .



## Before you begin

To get the permissions that you need to use the query builder, ask your administrator to grant you the [Bigtable Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigtable#bigtable.reader) (`roles/bigtable.reader`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to use the query builder. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the query builder:

  * `bigtable.tables.get`
  * `bigtable.instances.get`
  * `bigtable.appProfiles.list`
  * `bigtable.tables.list`
  * `bigtable.tables.readRows  
`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you don't have a table to query, you can [create a small test table](https://docs.cloud.google.com/bigtable/docs/creating-test-table) and run your queries against it.

## Open the query builder

When you open the query builder, a default query is run and displayed for the first table alphabetically in the instance. The default query is run using the default app profile, and up to 100 rows are returned.

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the name of the instance that contains the table that you want to query.

  3. In the navigation pane, click **Bigtable Studio**. The **Bigtable Studio** page opens in query builder mode. The **Explorer** pane provides a list of tables in the instance, and the **Query results** pane shows the results of the default query.

  4. Optional: Collapse the **Explorer** pane to make the query builder pane larger.




## Data display format

Query builder results are displayed in a table. The first heading and column is **Row key**. The remaining headings each represent a column in the Bigtable table, expressed as the column family and column qualifier separated by a colon. For example, the heading **cell_plan: data_plan_01gb** indicates that values in that column are from the `data_plan_01gb` column in the `cell_plan` column family.

![drop-down](https://docs.cloud.google.com/static/bigtable/img/query-builder-results-table.png)

Only the most recent value for a column is returned. Timestamps are hidden by default, but you can click the toggle to display them.

## Select a table

Use the **Table** drop-down to select the ID of the table that you want to query.

## Optional: Specify an app profile

You can use an app profile that you create specifically for use with the query builder. This can be helpful, for example, when you want to isolate the query traffic by using a different cluster than the one used by your primary application.

To use a different app profile to run your next query, follow these steps.

  1. Click **Add to query**.
  2. Click **Change app profile (default)**. A new drop-down is displayed.
  3. Use the **App profile** drop-down and choose from the list of the instance's app profiles.



To read more about the advantages of using different app profiles for different workloads, see [About app profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles) . To learn how to create an app profile, see [Create and configure app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles) .

If your table is in an instance that uses replication, configure your app profile to read from the cluster that is geographically closest to you.

**Note:** You can't use a [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) app profile with the query builder.

## Add clauses to the query and then run it

  1. After you've selected the table and app profile, add clauses to the query. See the next section for details on the available clauses.
  2. After you've added all your clauses, click **Run**.
  3. View the results.



## Query clauses

You use the query builder to add clauses to your query. When you run the query, the query builder creates and sends a _read request_ to your table. To learn more about read requests, see [Reads](https://docs.cloud.google.com/bigtable/docs/reads).

The row key, row key range, and row key prefix clauses determine the rows that are fetched from storage. The row key regex, columns, and time range clauses add a _filter_ to the generated read request. Filters that you use in the query builder work the same as when you use them in the client libraries. For details about Bigtable filters and how using them can affect performance, see [Filters](https://docs.cloud.google.com/bigtable/docs/filters) and [Use filters](https://docs.cloud.google.com/bigtable/docs/using-filters) .

### Specify row key

To retrieve a single row from the table, provide a row key value. You can add multiple row key clauses.

  1. Click **Add to query**.
  2. In the drop-down list, select **Row key**.
  3. Enter the exact value of the row key for which you want to view values.



### Specify a row key range

To retrieve a range of rows from the table, specify a start and end row key. Bigtable stores data in lexicographic order by row key.

  1. Click **Add to query**.
  2. In the drop-down list, select **Row key range**.
  3. Enter the complete start row key.
  4. Enter the complete end row key.



### Specify a row key prefix

To retrieve only rows whose row keys begin with a specific set of characters, filter by row key prefix. A row key prefix is the first N characters of a row key. By convention, there is often a hashtag, pipe, or other symbol between the prefix and the rest of the row key.

  1. Click **Add to query**.
  2. In the drop-down list, select **Row key prefix**.
  3. Enter a row key prefix. You don't need to enter any wildcard symbols.



### Filter by row key regex

To get only rows whose row key values match a specified regular expression, use a row key regex filter. For better performance, add a row key range or row key prefix clause to the query before you add the row key regex filter. For guidance on composing your regex, see [Row key regex](https://docs.cloud.google.com/bigtable/docs/using-filters#row-key-regex) .

  1. Click **Add to query**.
  2. In the drop-down list, select **Row key regex**.
  3. Enter a regular expression that uses [re2 syntax](https://github.com/google/re2/wiki/Syntax)



### Filter by column

To specify one or more columns to include in the query, add a **columns** clause, choosing the column family and column qualifier for each column that you want to filter by. The read request that is generated when you add this clause includes the [column family regex filter](https://docs.cloud.google.com/bigtable/docs/using-filters#column-family-regex) and the [column range filter](https://docs.cloud.google.com/bigtable/docs/using-filters#column-range) .

  1. Click **Add to query**.
  2. In the drop-down list, select **Columns**.
  3. Click in the Columns field. A list of column families is displayed.
  4. Click a column family ID. A list of column qualifiers is displayed.
  5. Click a column qualifier.



### Filter by time range

To retrieve only cells with a timestamp within a certain range, add a time range clause, which uses the [timestamp range filter](https://docs.cloud.google.com/bigtable/docs/using-filters#timestamp-range) .

  1. Click **Add to query**.
  2. In the drop-down list, select **Time range**.
  3. Enter a start timestamp.
  4. Enter an end timestamp.



Provide a timestamp in one of the following formats:

  * A Unix timestamp in microseconds, such as `3023483279876000`
  * YYYY-MM-DDThh:mm:ss:ss[z]
  * YYYY/MM/DD-hh:mm:ss.sss[z]
  * MM/DD/YYYY
  * YYYY/MM/DD



The optional `T` is a literal that indicates time, and the optional `z` indicates UTC time rather than local time. For more information about timestamp formats, see [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) .

### Specify a limit

To specify a maximum number of rows returned, add a limit clause.

  1. Click **Add to query**.
  2. In the drop-down list, select **Limit**.
  3. Enter a number from 1 to 1,000.



## Limitations

The following limitations apply to the query builder.

  * **1,000 characters per cell** : Bigtable returns a maximum of 1,000 characters per cell. If a cell contains more than 1,000 characters, a truncated result is displayed, annotated with the number of characters not displayed.
  * **100 column maximum** : Bigtable returns the first 100 columns in each row that match the query. Column families are not stored in any particular order, but columns are sorted lexicographically within their column family.
  * **1,000 row maximum** : the query builder returns a maximum of the first 1,000 rows of data that match your query.
  * **Base64** : Bigtable makes a best effort to accurately display Base64-encoded data, but results are not guaranteed. If Bigtable is unable to display the data in a cell, it displays the cell value's size in bytes instead.
  * **Older data** : you can only retrieve the most recent cell (or version) in the columns that you query. For more information, see [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model) and [General concepts](https://docs.cloud.google.com/bigtable/docs/schema-design#general-concepts).
  * **Serialized data** : data that is stored as protocol buffers isn't displayed correctly in the query results. JSON data is better supported but not guaranteed to look right.
  * **HyperLogLog (HLL) columns** : HLL values represent probabilistic sets. When viewed in the results table, they appear as raw bytes or base64. To estimate the unique cardinalities (counts) for HLL columns, you must read the data using the [Zetasketch library](https://github.com/google/zetasketch), or use the query editor with GoogleSQL [HLL++ functions](https://docs.cloud.google.com/bigtable/docs/reference/sql/hll_functions), such as `HLL_COUNT.EXTRACT`.
  * **Artificial timestamps** : if your application assigns non-timestamp numbers to the timestamp property of cells when it writes data to your table, you can use time range filters in your query to get a range of the values that you use instead of timestamps, as long as you specify them as microseconds. To understand why your table data might use artificial timestamps, see [Timestamps](https://docs.cloud.google.com/bigtable/docs/garbage-collection#timestamps)



## What's next

  * [Learn about write requests.](https://docs.cloud.google.com/bigtable/docs/writes)
  * [Create and manage tables.](https://docs.cloud.google.com/bigtable/docs/managing-tables)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
