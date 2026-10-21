---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-optimize-looker-server-performance/
title: Optimize Looker performance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:39.410921+00:00
---

# Optimize Looker performance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-optimize-looker-server-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Optimize Looker performance Stay organized with collections  Save and categorize content based on your preferences. 

> _These best practices reflect recommendations that have been shared by a cross-functional team of seasoned Lookers. These insights come from years of experience working with Looker customers from implementation to long-term success. The practices are written to work for most users and situations, but you should use your best judgment when implementing._

## Optimize query performance

You can ensure that queries are built and executed optimally against your database with the following frontend and backend tips: 

  * Build Explores using [`many_to_one`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship#many_to_one_\(the_default_value\)) joins whenever possible. Joining views from the most granular level to the highest level of detail (`many_to_one`) typically provides the best query performance. 
  * Maximize caching to sync with your ETL policies wherever possible to reduce database query traffic. By default, Looker caches queries for one hour. You can control the caching policy and sync Looker data refreshes with your ETL process by applying [datagroups](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) within Explores, using the [`persist_with`](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-with) parameter. This enables Looker to integrate more closely with the backend data pipeline, so cache usage can be maximized without the risk of analyzing stale data. Named caching policies can be applied to an entire model and/or to individual Explores and [persistent derived tables](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#how_looker_uses_pdts_and_rebuilds_them) (PDTs). 
  * Use Looker's [aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness) functionality to create roll-ups or summary tables that Looker can use for queries whenever possible, especially for common queries of large databases. You can also take advantage of aggregate awareness to drastically [improve the performance of entire dashboards](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#get_lookml_dashboard). See the [Aggregate awareness tutorial](https://docs.cloud.google.com/looker/docs/best-practices/aggregate-awareness-tutorial) for additional information. 
  * Use [PDTs](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) for faster queries. Convert Explores with many complex or unperformant joins, or dimensions with subqueries or subselects, into PDTs so that the views are pre-joined and ready prior to runtime. 
  * If your [database dialect supports incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts#supported_database_dialects_for_incremental_pdts), configure [incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts) to reduce the time Looker spends rebuilding PDTs. 
  * Avoid joining views into Explores on concatenated [primary keys](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) that are defined in Looker. Instead, join on the base fields that make up the concatenated primary key from the view. Alternatively, recreate the view as a PDT with the concatenated primary key predefined in the table's SQL definition, rather than in a view's LookML. 
  * Use the [Explain in SQL Runner tool](https://docs.cloud.google.com/looker/docs/sql-runner-manage-db#examining_an_execution_plan_using_explain) for benchmarking. `EXPLAIN` produces an overview of your database's query execution plan for a given SQL query, letting you detect query components that can be optimized. Learn more in the [How to optimize SQL with `EXPLAIN`](https://discuss.google.dev/t/how-to-optimize-sql-with-explain/119243) Community post. 
  * Declare indexes. You can look at the indexes of each table directly in Looker from [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics) by clicking the gear icon in a table and then selecting [**Show Indexes**](https://docs.cloud.google.com/looker/docs/sql-runner-manage-db#getting_table_information).

The most common columns that can benefit from indexes are important dates and foreign keys. Adding indexes to these columns will increase performance for almost all queries. This also applies for PDTs. LookML parameters, such as [`indexes`](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes), [`sort keys`](https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys), and [`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution), can be applied appropriately. 
  * Increase memory, cores, and I/O (input/output) of databases with insufficient hardware or necessary provisioned resources (such as AWS) for processing large datasets, to increase query performance. 



## Optimize Looker server performance

You can also take measures to ensure that the Looker server and application are performing optimally: 

  * Limit the number of elements within an individual dashboard. There is no precise rule for defining the number, because the design of each element impacts memory consumption based on a variety of factors; however, dashboards with 25 or more tiles tend to be problematic when it comes to performance. 
  * Use the [dashboard auto refresh](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#autorefresh) feature strategically. If a dashboard uses auto refresh, make sure it refreshes no faster than the ETL processes running behind the scenes. 
  * Use pivots strategically, and avoid over-using pivots within dashboard tiles and Looks. Queries with pivoted dimensions will consume more memory. The more dimensions that are pivoted, the more memory is consumed when content (an Explore, a Look, or a dashboard) is loaded. 
  * Use features such as [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations), sparingly. These features are intended to be used as proofs of concept to help design your model. It is best practice to hardcode any frequently used calculations and functions in LookML, which will generate SQL to be processed on your database. Excessive calculations can compete for Java memory on the Looker instance, causing the Looker instance to respond more slowly. 
  * For [merged results queries](https://docs.cloud.google.com/looker/docs/merged-results), use [in-database merge queries](https://docs.cloud.google.com/looker/docs/merged-results#in-database-merge-queries) whenever possible. In-database merge queries are processed in your database, instead of in Looker memory. 
  * Limit the number of views included within a model when a large number of view files are present. Including all views in a single model can slow performance. When a large number of views are present within a project, consider including only the view files that are needed within each model. Consider using strategic naming conventions for view filenames, to enable inclusion of groups of views within a model. An example is outlined in the [`includes`](https://docs.cloud.google.com/looker/docs/reference/param-model-include#things_to_know) parameter documentation. 
  * Avoid returning a large number of data points by default within dashboard tiles and Looks. Queries that return thousands of data points will consume more memory. Ensure that data is limited wherever possible by applying frontend [ filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#adding_dashboard_filters) to dashboards, Looks and Explores, and on the LookML level with [`required filters`](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#requiring_a_filter_value), [`conditionally_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter) and [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) parameters. 
  * Download or deliver queries using the [**All Results**](https://docs.cloud.google.com/looker/docs/downloading#all_results) option sparingly, as some queries can be very large and overwhelm the Looker server when processed. 
  * Understand the impact of connection performance on the entire Looker instance. Looker uses shared resources to process queries from all database connections. These resources include Kubernetes pods, query queues, and thread pools. Because of this shared infrastructure, a single slow or overloaded database connection can negatively impact the performance of queries on all other connections. If you notice widespread performance degradation, investigate the health of all your database connections, not just the ones that are directly related to related to the slow dashboards or Explores. 



For more help identifying the source of performance issues, check out the [Performance overview](https://docs.cloud.google.com/looker/docs/best-practices/how-to-optimize-looker-performance) Best Practices page. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
