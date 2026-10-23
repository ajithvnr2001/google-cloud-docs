---
url: https://docs.cloud.google.com/alloydb/docs/index-advisor-overview/
title: Index advisor overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:24.850689+00:00
---

# Index advisor overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/index-advisor-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Index advisor overview Stay organized with collections  Save and categorize content based on your preferences. 

To detect potential query performance bottlenecks and optimize index creation, you can use the fully managed index advisor in AlloyDB for PostgreSQL. The index advisor tracks the queries that your database regularly handles and periodically analyzes those queries to recommend indexes that can improve query performance.

## How does the index advisor work?

The AlloyDB index advisor helps you improve query processing by doing the following:

  * Helping you identify a set of indexes.
  * Providing details to help you create recommended indexes, for example, estimated storage size and impact of indexes on a query.



You can also use the index advisor with [query insights](https://docs.cloud.google.com/alloydb/docs/query-insights-overview). The index advisor stores and displays the `CREATE INDEX` command that contains the database name, schema name, table name, and column names. The tracked queries are all normalized queries with all literals removed.

Index recommendations are encrypted at rest.

For more information about how to use the index advisor, see [Use index advisor](https://docs.cloud.google.com/alloydb/docs/use-index-advisor). For more information how to use it with query insights, see [Use index advisor with query insights](https://docs.cloud.google.com/alloydb/docs/use-index-advisor-with-query-insights).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
