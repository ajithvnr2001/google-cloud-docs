---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/columnar-engine/
title: Troubleshoot the columnar engine \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:25.775483+00:00
---

# Troubleshoot the columnar engine  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/columnar-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot the columnar engine Stay organized with collections  Save and categorize content based on your preferences. 

This page provides recommended fixes and information for common issues and questions regarding the AlloyDB for PostgreSQL columnar engine.

## You added referenced columns to the columnar engine, but your SELECT query doesn't use them

**Description:** To use the columnar engine, all columns referenced in a query fragment—such as joins and scans—must be in the column store. If any referenced column isn't in the columnar engine, then the query fragment defaults to the row-based store.

A _query fragment_ in this context is a query that can have multiple scan nodes. For example, the query fragment can have two scan nodes for a join. One scan node might use non-columnar and another scan node might use columnar. All columns of a scan node—filter columns and projection columns—must be populated in columnar. Similarly, a query can have some partitions in columnar and other partitions in non-columnar.

**Recommended fix:** To verify that all referenced columns are in the columnar engine, follow these steps:

  1. Check supported data types.

Make sure that AlloyDB supports all the data types of the columns that you intend to use with the columnar engine. For more information, see [Supported data types](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about#supported-data-types). If AlloyDB doesn't support a critical data type, consider contacting [Google Cloud Support](https://cloud.google.com/support).

  2. Check supported operators.

Make sure that AlloyDB supports the operators on the data types in the columnar engine. For more information about supported operators, see [Query types that benefit from the columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about#benefits).

  3. Run the `EXPLAIN COLUMNAR_ENGINE` command.

To identify and address issues that prevent specific queries from using the columnar engine, run the following `EXPLAIN COLUMNAR_ENGINE` command:
         
         EXPLAIN (COLUMNAR_ENGINE, ANALYZE) SELECT column1, column2 FROM my_table WHERE column3 > 100;
         




## You're unable to add or drop tables in the columnar engine

**Description:** You want to add or drop tables in the columnar engine.

**Recommended fix:** Verify your user permissions. You can only add or drop tables in the columnar engine if you have read privileges on the table.

## Columnar data size exceeds allocated memory

**Description:** You encounter performance or data handling issues when your columnar data size exceeds the memory allocated for the columnar engine.

**Recommended fix:** For optimal performance, use the recommendation feature in AlloyDB to identify optimal tables and columns to populate the columnar engine.

If the recommended tables and columns exceed the physical memory of the columnar engine, the excess columnar data uses a portion of the ultra-fast cache layer. Queries on the remaining data in the table, which isn't in the columnar engine, transparently use the row store.

You can also adjust the columnar engine memory and storage cache allocation. The columnar engine is provisioned with a default size for memory and storage cache. You can manually configure the memory and storage cache. To change the amount of memory or storage cache allocated to the columnar engine, see [Configure memory for the columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure#configure-memory).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
