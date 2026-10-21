---
url: https://docs.cloud.google.com/spanner/docs/full-text-search/json-indexes/
title: JSON search indexes \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:23.737247+00:00
---

# JSON search indexes  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/full-text-search/json-indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  JSON search indexes Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is available with the Spanner Enterprise edition and Enterprise Plus edition. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview). 

In addition to indexing text, the Spanner [search index](https://docs.cloud.google.com/spanner/docs/full-text-search/search-indexes) provides an efficient way to index and query JSON and JSONB documents. Use search indexes for standalone JSON and JSONB queries, or to augment other [full-text search](https://docs.cloud.google.com/spanner/docs/full-text-search) queries.

For more information, see [Index JSON data](https://docs.cloud.google.com/spanner/docs/working-with-json#index) and [Index JSONB data](https://docs.cloud.google.com/spanner/docs/working-with-jsonb#index).

## Tokenize JSON and JSONB

You can use the `TOKENIZE_JSON` function to create a JSON index in GoogleSQL, or the `TOKENIZE_JSONB` function to create a JSONB index in PostgreSQL. For details, see [`TOKENIZE_JSON`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/search_functions#tokenize_json) and [`TOKENIZE_JSONB`](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#indexing).

## JSON and JSONB queries

You can use a search index to accelerate queries that include _equality comparisons_ , _JSON containment_ , and _key existence_ conditions:

  * **Equality comparisons** determine whether a JSON document or a subpath within a JSON document equals a target value.
  * **JSON containment** determines if one JSON document is contained within another.
  * **Key existence** determines if a key or path exists in a JSON document.



You can express these conditions in each dialect as follows:

  * In GoogleSQL:

    * Construct equality predicates using the `=`, `!=`, `<>`, `IN`, and `NOT IN` operators on an indexed `JSON` column or a subpath extracted with the [field access](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/operators#field_access_operator) and [subscript](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/operators#json_subscript_operator) operators. For example, `doc = JSON '{"a": 1}'`, `doc.sub.path[0].key = "value"`, or `doc.status IN ("active", "pending")`. Other [comparison operators](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#comparison_and_sorting) such as `<`, `<=`, `>`, and `>=` aren't accelerated by JSON search indexes.
    * Express JSON containment in your schema by using the [`JSON_CONTAINS`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/json_functions#json_contains) function.
    * Construct key existence conditions using the field access, array subscript operators, and `IS NOT NULL`. The field access and array subscript operators describe a JSON document path. `IS NOT NULL` checks for the existence of this path (for example, `doc.sub.path[@index].key IS NOT NULL`).
  * In PostgreSQL:

    * Construct equality predicates using the `=`, `!=`, `<>`, `IN`, and `NOT IN` operators on an indexed `JSONB` column or a subpath extracted with the [`->`](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#jsonb_operators) operator. For example, `doc = '{"a": 1}'::jsonb`, `doc->'sub'->0->'key' = '"value"'::jsonb`, or `doc->'status' IN ('"active"'::jsonb, '"pending"'::jsonb)`. Other comparison operators such as `<`, `<=`, `>`, and `>=`, as well as text extraction predicates that use `->>`, aren't accelerated by JSONB search indexes.
    * Express JSONB containment using the `@>` and `<@` operators. For more information, see [JSONB operators](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#jsonb_operators).
    * Construct key existence conditions using the `?`, `?|`, and `?&` operators. For more information, see [JSONB operators](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#jsonb_operators).



In your queries, you can include multiple JSON conditions of any type in the search index. You can also include the JSON conditions in a logical combination using `AND`, `OR`, and `NOT`.

### Check search index usage

To check that that your query uses a search index, look for a _Search index scan_ node in the [query execution plan](https://docs.cloud.google.com/spanner/docs/query-execution-plans).

## Restrictions

  * Search indexes, including JSON and JSONB search indexes, are used only in read-only transactions. Spanner might use relevant secondary indexes in a read-write transaction. If you attempt to force the use of a search index in a read-write transaction, the following error occurs: `ERROR: spanner: code = "InvalidArgument", desc = "The search index AlbumsIndex cannot be used in transactional queries by default."`
  * Attempts to store certain large or very complex JSON documents in a search index might return a `too many search token bytes` error. The output token size from this JSON document must be smaller than 10 MB. If you don't need the entire document to be searchable, consider extracting a smaller subset of the document (for example, by using a generated column) and searching over the column instead.



## What's next

  * Learn about [tokenization and tokenizers](https://docs.cloud.google.com/spanner/docs/full-text-search/tokenization).
  * Learn about [search indexes](https://docs.cloud.google.com/spanner/docs/full-text-search/search-indexes).
  * Learn about [indexing JSON data](https://docs.cloud.google.com/spanner/docs/working-with-json#index).
  * Learn about [indexing JSONB data](https://docs.cloud.google.com/spanner/docs/working-with-jsonb#index).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
