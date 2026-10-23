---
url: https://docs.cloud.google.com/spanner/docs/concepts/function-volatility/
title: Function volatility \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:58.543562+00:00
---

# Function volatility  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/concepts/function-volatility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Function volatility Stay organized with collections  Save and categorize content based on your preferences. 

In Spanner, functions, including built-in SQL and user-defined functions, are classified by their volatility. The volatility category indicates whether a function returns the same result when you call it with the same arguments. This classification affects how the query optimizer handles the function and where you can use the function, such as in generated column expressions or index definitions. Understanding function volatility helps you write more predictable and performant queries and schemas in Spanner.

There are three volatility categories, which are similar to concepts in systems such as [PostgreSQL](https://www.postgresql.org/docs/13/xfunc-volatility.html):

  * **Immutable** : A function is _immutable_ if it returns the same results when you call it with the same argument values. This behavior means the function's result depends only on its input arguments and not on database state, session settings, or external factors. Most mathematical functions are immutable. The following functions are examples:

    * [`ABS`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/mathematical_functions#abs)

    * [`LENGTH`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/string_functions#length)

    * String manipulation functions, such as [`CONCAT`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/string_functions#concat) and [`LOWER`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/string_functions#lower)

    * Date and time formatting functions with explicit inputs

Functions that depend on runtime-configurable settings, such as [time zone](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/timestamp_functions#timezone_definitions), aren't immutable because their results can vary across different database or session configurations.

  * **Stable** : A function is _stable_ if it returns the same results for the same argument values within a single statement execution. However, its result can change across different SQL statements. Functions such as [`CURRENT_TIMESTAMP`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/timestamp_functions#current_timestamp), [`CURRENT_DATE`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/date_functions#current_date), and similar time-based functions are stable. For example, multiple calls to `CURRENT_TIMESTAMP` within the same `SELECT` statement yield the same timestamp, but subsequent statements might produce a different timestamp.

  * **Volatile** : A function is _volatile_ if its value can change even within a single statement execution with the same arguments. For example, the [`GENERATE_UUID`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/utility-functions#generate_uuid) function, which generates a unique ID, is volatile.




## Volatility implications

A function's volatility category dictates where it can be used in your database schema and how queries containing the function are optimized:

  * **Generated columns:** Expressions that define [generated columns](https://docs.cloud.google.com/spanner/docs/generated-column/how-to) must be immutable. This ensures that the stored value is deterministic based on the other columns in the row. Spanner produces an error if you try to define a generated column with an expression that's not immutable.

  * **Indexing:** You can't create indexes on expressions that involve volatile functions. Spanner produces an error if you try to create an index on an expression that involves volatile functions.

  * **Query optimization:** The query optimizer uses volatility information to perform optimizations. For example, the [query optimizer](https://docs.cloud.google.com/spanner/docs/query-optimizer/overview) precalculates calls to immutable functions with constant arguments. The optimizer often caches results of stable functions within the scope of a single statement's execution.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
