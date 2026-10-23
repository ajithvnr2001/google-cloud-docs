---
url: https://docs.cloud.google.com/spanner/docs/optimize-schema-performance/
title: Test and tune your schema and application performance \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:57.776386+00:00
---

# Test and tune your schema and application performance  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/optimize-schema-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Test and tune your schema and application performance Stay organized with collections  Save and categorize content based on your preferences. 

Performance tuning is an iterative process in which you evaluate metrics like CPU utilization and latency, adjust your schema and application to improve performance, and test again.

For example, in your schema, you might add or change an index, or change a primary key. In your application, you might batch writes, or you might merge or modify your queries.

For production traffic in particular, performance tuning is important to help avoid surprises. Performance tuning is more effective the closer the setup is to live production traffic throughput and data sizes.

To test and tune your schema and application performance, follow these steps:

  1. Upload a subset of your data into a Spanner database. You can use the [BigQuery reverse ETL workflow](https://docs.cloud.google.com/bigquery/docs/export-to-spanner) to load the sample data. For more information, see [Load sample data](https://docs.cloud.google.com/spanner/docs/load-sample-data).
  2. Point the application to Spanner.
  3. Verify the database consistency by checking for basic flows.
  4. Verify that performance meets your expectations by performing load tests on your application. For help identifying and optimizing your most expensive queries, see [Detect query performance issues with query insights](https://docs.cloud.google.com/spanner/docs/using-query-insights). In particular, the following factors can contribute to suboptimal query performance: 
     1. **Inefficient queries** : For information about writing efficient SQL queries, see [SQL best practices](https://docs.cloud.google.com/spanner/docs/sql-best-practices).
     2. **High CPU utilization** : For more information, see [Investigate high CPU utilization](https://docs.cloud.google.com/spanner/docs/introspection/investigate-cpu-utilization).
     3. **Locking** : To reduce bottlenecks caused by transaction locking, see [Identify transactions that might cause high latencies](https://docs.cloud.google.com/spanner/docs/use-lock-and-transaction-insights).
     4. **Inefficient schema design** : If the schema isn't designed well, query optimization isn't very useful. For more information about designing good schemas, see [Schema design best practices](https://docs.cloud.google.com/spanner/docs/schema-design).
     5. **Hotspots** : Hotspots in Spanner limit write throughput, especially for high-QPS applications. To identify hotspots or schema design issues, check the [Key Visualizer](https://docs.cloud.google.com/spanner/docs/key-visualizer) statistics from the Google Cloud console. For more information about avoiding hotspots, see [Choose a primary key to prevent hotspots](https://docs.cloud.google.com/spanner/docs/schema-design#primary-key-prevent-hotspots).
  5. If you modify schema or indexes, repeat database consistency and performance testing until you achieve satisfactory results.



For more information about fine-tuning your database performance, contact [Spanner support](https://docs.cloud.google.com/spanner/docs/getting-support).

[ Previous arrow_back  Migrate your application  ](https://docs.cloud.google.com/spanner/docs/application-migration)

[ Next Migrate your data  arrow_forward  ](https://docs.cloud.google.com/spanner/docs/data-migration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
