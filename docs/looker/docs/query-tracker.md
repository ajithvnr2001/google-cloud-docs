---
url: https://docs.cloud.google.com/looker/docs/query-tracker/
title: Using the Explore query tracker and Performance panel to monitor query performance \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:23.038629+00:00
---

# Using the Explore query tracker and Performance panel to monitor query performance  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/query-tracker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using the Explore query tracker and Performance panel to monitor query performance Stay organized with collections  Save and categorize content based on your preferences. 

The Explore query tracker and the Explore **Performance** panel provide step-by-step performance data for an Explore query. This data can help identify key entry points for troubleshooting and resolving performance issues with queries and provide recommendations for improvements.

## Explore query tracker

The Explore query tracker displays the progress of an Explore query through the three phases of the query while the query is running.

![](https://docs.cloud.google.com/static/looker/docs/images/query-tracker-2414.png)

If a query is taking a long time to execute, the query tracker can indicate which phase of the query is causing the performance issue. This is useful for identifying where performance problems may occur, and where optimization efforts can be the most effective.

The query tracker is displayed when an Explore is running, as long as either the [Explore **Visualization** panel or the Explore **Data** panel](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_page) is open.

## Explore **Performance** panel

To see the Explore **Performance** panel, click the **See performance details** link, which is available on any Explore query that has been run.

![](https://docs.cloud.google.com/static/looker/docs/images/see-performance-details-2418.png)

The **Performance** panel shows the time that the query spent in each of the three query phases and includes links to performance documentation and the [**Query History** System Activity dashboard](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#query_history), which shows current and historical performance data for the query and the Explore that was used to create the query.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-performance-panel-2418.png)

## Query phases

When a Looker [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) runs a database query, the query is executed in three phases, as follows:

  * The [query initialization phase](https://docs.cloud.google.com/looker/docs/query-tracker#query_initialization_phase)
  * The [running query phase](https://docs.cloud.google.com/looker/docs/query-tracker#running_query_phase)
  * The [processing results phase](https://docs.cloud.google.com/looker/docs/query-tracker#processing_results_phase)



### Query Initialization phase

During the **Query Initialization** phase, Looker is performing all of the tasks that are required before the query is sent to your database. The **Query Initialization** phase includes the following tasks:

  * Compiling the [LookML model](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#model)
  * Checking to see if any [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables) will need to be built
  * [Generating the query SQL](https://docs.cloud.google.com/looker/docs/how-looker-generates-sql)
  * Acquiring the [database connection](https://docs.cloud.google.com/looker/docs/connecting-to-your-db)



The [Understanding query performance metrics](https://docs.cloud.google.com/looker/docs/query-performance-metrics) documentation page describes how to use the **Query Performance Metrics** Explore in [System Activity](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) to view detailed breakdowns of a query. The **Query initialization** phase of the query tracker includes the events that are described in the **[Asynchronous worker phase](https://docs.cloud.google.com/looker/docs/query-performance-metrics#asynchronous_worker_phase_metrics)** , **[Initialization phase](https://docs.cloud.google.com/looker/docs/query-performance-metrics#initialization_phase_metrics)** , and **[Connection handling phase](https://docs.cloud.google.com/looker/docs/query-performance-metrics#connection_handling_phase_metrics)** of the **Query Performance Metrics** Explore.

### Running Query phase

The **Running Query** phase is when Looker contacts and queries your database and returns the results of the query. Performance issues during this phase could indicate issue with the external database, such as PDTs that take a long time to rebuild and may need to be optimized, or external database tables that may need optimization. The **Running Query** phase includes the following tasks:

  * Building any PDTs in the database that are required for the Explore query
  * Running the requested query on the database



The [Understanding query performance metrics](https://docs.cloud.google.com/looker/docs/query-performance-metrics) documentation page describes how to use the **Query Performance Metrics** Explore in [System Activity](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) to view detailed breakdowns of a query. The **Running query** phase of the query tracker includes the events that are described in the **[Main queries phase](https://docs.cloud.google.com/looker/docs/query-performance-metrics#main_queries_phase_metrics)** of the **Query Performance Metrics** Explore.

Possible steps to take if you experience performance issues during this phase include the following:

  * Build Explores using [`many_to_one`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship#many_to_one_default_value) joins whenever possible. Joining views from the most granular level to the highest level of detail (`many_to_one`) typically provides the best query performance.
  * Maximize caching to sync with your ETL policies wherever possible to reduce database query traffic. By default, Looker caches queries for one hour. You can control the caching policy and sync Looker data refreshes with your ETL process by applying [datagroups](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) within Explores using the [`persist_with`](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-with) parameter. Maximizing caching enables Looker to integrate more closely with the backend data pipeline, so cache usage can be maximized without the risk of analyzing stale data. Named caching policies can be applied to an entire model or to individual Explores and [persistent derived tables](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#how_looker_uses_pdts_and_rebuilds_them) (PDTs).
  * Use Looker's [aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness) feature to create roll-ups or summary tables that Looker can use for queries whenever possible, especially for common queries of large databases. You can also use aggregate awareness to drastically [improve the performance of entire dashboards](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#get_lookml_dashboard). See the [Aggregate awareness tutorial](https://docs.cloud.google.com/looker/docs/best-practices/aggregate-awareness-tutorial) for additional information.
  * Use [PDTs](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) for faster queries. Convert Explores with many complex or unperformant joins, or dimensions with subqueries or subselects, into PDTs so that the views are pre-joined and ready prior to runtime.
  * If your [database dialect supports incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts#supported_database_dialects_for_incremental_pdts), configure [incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts) to reduce the time Looker spends rebuilding PDT tables.
  * Avoid joining views into Explores on concatenated [primary keys](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) that are defined in Looker. Instead, join on the base fields that make up the concatenated primary key from the view. Alternatively, recreate the view as a PDT with the concatenated primary key predefined in the table's SQL definition, rather than in a view's LookML.
  * Use the [Explain in SQL Runner tool](https://docs.cloud.google.com/looker/docs/sql-runner-manage-db#examining_an_execution_plan_using_explain) for benchmarking. `EXPLAIN` produces an overview of your database's query execution plan for a given SQL query, letting you detect query components that can be optimized. Learn more in the [How to optimize SQL with `EXPLAIN`](https://discuss.google.dev/t/how-to-optimize-sql-with-explain/119243) Community post.
  * Declare indexes. You can look at the indexes of each table directly in Looker from [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics) by clicking the gear icon in a table and then selecting [**Show Indexes**](https://docs.cloud.google.com/looker/docs/sql-runner-manage-db#getting_table_information).

The most common columns that can benefit from indexes are important dates and foreign keys. Adding indexes to these columns will increase performance for almost all queries. This also applies for PDTs. LookML parameters, such as [`indexes`](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes), [`sort keys`](https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys), and [`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution), can be applied appropriately.



### Processing Results phase

During the **Processing Results** phase, Looker processes and renders the results of the query. The **Processing Results** phase includes the following tasks:

  * Streaming query results to the [cache](https://docs.cloud.google.com/looker/docs/caching-and-datagroups)
  * Resolving [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations)
  * Formatting the results of the [Liquid templating language](https://docs.cloud.google.com/looker/docs/liquid-variable-reference)
  * [Merging queries together](https://docs.cloud.google.com/looker/docs/merged-results)
  * [Calculating totals and subtotals](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals)



The [Understanding query performance metrics](https://docs.cloud.google.com/looker/docs/query-performance-metrics) documentation page describes how to use the **Query Performance Metrics** Explore in [System Activity](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) to view detailed breakdowns of a query. The **Processing Results** phase of the query tracker includes the events that are described in the **[Post-query phase](https://docs.cloud.google.com/looker/docs/query-performance-metrics#post-query_phase_metrics)** of the **Query Performance Metrics** Explore.

Possible steps to take if you experience performance issues during this phase include:

  * Use features such as [merge results](https://docs.cloud.google.com/looker/docs/merged-results), [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields), and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) sparingly. These features are intended to be used as proofs of concept to help design your model. It is best practice to hardcode any frequently used calculations and functions in LookML, which will generate SQL to be processed on your database. Excessive calculations can compete for Java memory on the Looker instance, causing the Looker instance to respond more slowly.
  * Limit the number of views that you include within a model when a large number of view files are present. Including all views in a single model can slow performance. When a large number of views are present within a project, consider including only the view files that are needed within each model. Consider using strategic naming conventions for view file names to enable inclusion of groups of views within a model. An example is outlined in the [`includes`](https://docs.cloud.google.com/looker/docs/reference/param-model-include#things_to_know) parameter documentation.
  * Avoid returning a large number of data points by default within dashboard tiles and Looks. Queries that return thousands of data points will consume more memory. Ensure that data is limited wherever possible by applying frontend [ filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#adding_dashboard_filters) to dashboards, Looks, and Explores, and on the LookML level with [`required filters`](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#requiring_a_filter_value), [`conditionally_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter) and [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) parameters.
  * Download or deliver queries using the [**All Results**](https://docs.cloud.google.com/looker/docs/downloading#all_results) option sparingly, as some queries can be very large and overwhelm the Looker server when they're processed.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
