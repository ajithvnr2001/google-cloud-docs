---
url: https://docs.cloud.google.com/spanner/docs/full-text-search/search-vs-secondary-index/
title: Search versus secondary indexes \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:37.719284+00:00
---

# Search versus secondary indexes  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/full-text-search/search-vs-secondary-index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Search versus secondary indexes Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is available with the Spanner Enterprise edition and Enterprise Plus edition. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview). 

This page describes the features for search and secondary indexes.

When deciding between search indexes and secondary indexes, keep in mind that search indexes should be the default choice for full-text use cases and secondary indexes should be the default option for everything else. The following table describes when to use each type of index.

Feature | Secondary index | Search index  
---|---|---  
Sort order | The index is sorted by all index key columns | Search index can only be sorted by at most two user-controlled INT64 columns  
Arrays | You can't use arrays data type values as keys in secondary indexes. | Search indexes support array indexing. All tokens of a document are colocated in the same split. As a result, transactions that change 1 row only write to one index split.  
JSON/JSONB | You can't use JSON values as keys in secondary indexes. | Search indexes support indexing JSON values.  
Lookups | Lookup by index key only needs to access one split | Queries that use search index generally need to read from all splits of a given partition. The only exception is top-k pattern matching.  
Multi-column indexing | Secondary indexes can include multiple key columns. Queries need to look up data by prefix of index key columns for efficient execution. | Search indexes can index multiple columns. Queries can specify complex logical expressions (conjunctions, disjunctions, negations) on any subset of the indexed columns, and still execute efficiently  
Index intersection | Users can rewrite their query to join multiple secondary indexes. | Intersection of multiple indexed columns is implemented as an efficient local zig-zag join, followed by a distributed merge union (that combines results from all relevant splits).  
Reading data | SQL Query or Read API | SQL Query  
  
Besides semantics, the syntax of the DDL statement to create a search index is different from the DDL syntax to create a secondary index:

  * Indexed columns are defined separately from the sort order in the search index.
  * The order of `TOKENLIST` columns in the `ON` clause of the `CREATE SEARCH INDEX` statement is immaterial.



## What's next

  * Learn about [search indexes](https://docs.cloud.google.com/spanner/docs/full-text-search/search-indexes).
  * Learn about [secondary indexes](https://docs.cloud.google.com/spanner/docs/secondary-indexes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
