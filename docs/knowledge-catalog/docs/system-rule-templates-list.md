---
url: https://docs.cloud.google.com/knowledge-catalog/docs/system-rule-templates-list/
title: System rule templates list \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:09.305523+00:00
---

# System rule templates list  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/system-rule-templates-list/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  System rule templates list Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog (formerly Dataplex Universal Catalog) supports a range of rule templates that you can use to define and automate data quality and data validation processes. Implementing these templates is a key part of data governance, ensuring that datasets remain accurate and consistent.

To identify which of these templates to use, you can perform [data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview) on your resources to identify potential quality issues. After identifying the required quality checks, you can select the appropriate templates from this page to define rules for your resources.

This page lists the available system rule templates that you can use in any region.

### Table shape

Name | Description  
---|---  
[Column Count Equality Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/column_count_equality_expectation) | Aggregate rule that evaluates whether the number of columns in the table equals a specified value. This rule requires `bigquery.tables.get`, `bigquery.tables.list`, and `bigquery.datasets.get` permissions on the table and dataset being queried.  
[Column Count Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/column_count_range_expectation) | Aggregate rule that evaluates whether the number of columns in the table lies within a specified range. This rule requires `bigquery.tables.get`, `bigquery.tables.list`, and `bigquery.datasets.get` permissions on the table and dataset being queried.  
[Column Existence Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/column_existence_expectation) | Aggregate rule that evaluates whether a specific column exists in the table. This rule requires `bigquery.tables.get`, `bigquery.tables.list`, and `bigquery.datasets.get` permissions on the table and dataset being queried.  
[Freshness Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/freshness_expectation) | Aggregate rule that evaluates whether the latest data in a column is newer than a specified interval.  
[Grouped Freshness Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/grouped_freshness_expectation) | Aggregate rule that evaluates whether the latest grouped data in a column is newer than a specified interval.  
[Ordered Schema Match Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/ordered_schema_match_expectation) | Aggregate rule that evaluates whether the ordered columns in the table exactly match an ordered, specified list.  
[Row Count Equality Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/row_count_equality_expectation) | Aggregate rule that evaluates whether the number of rows in the table equals a specified value.  
[Row Count Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/row_count_range_expectation) | Aggregate rule that evaluates whether the number of rows in the table lies within a specified range.  
[Schema Containment Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/schema_containment_expectation) | Aggregate rule that evaluates whether the set of columns in the table contain all the columns in a specified set. This rule requires `bigquery.tables.get`, `bigquery.tables.list`, and `bigquery.datasets.get` permissions on the table and dataset being queried.  
[Schema Exclusion Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/schema_exclusion_expectation) | Aggregate rule that evaluates whether the columns in the table aren't in a specified set. This rule requires `bigquery.tables.get`, `bigquery.tables.list`, and `bigquery.datasets.get` permissions on the table and dataset being queried.  
[Schema Match Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/schema_match_expectation) | Aggregate rule that evaluates whether the columns in the table exactly match a specified set. This rule requires `bigquery.tables.get`, `bigquery.tables.list`, and `bigquery.datasets.get` permissions on the table and dataset being queried.  
[Table Comparison Aggregate Equality Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/table_comparison_aggregate_equality_expectation) | Aggregate rule that evaluates whether the result of an aggregate expression is equal between the current table and a specified reference table.  
[Table Comparison Aggregate Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/table_comparison_aggregate_range_expectation) | Aggregate rule that evaluates whether the result of an aggregate expression on the current table deviates from the reference table by more than a specified tolerance.  
[Table Comparison Row Count Equality Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/table_comparison_row_count_equality_expectation) | Aggregate rule that evaluates whether the number of rows in the current table is equal to the number of rows in a specified reference table, with optional row filtering before counting.  
[Table Comparison Row Count Factor Equality Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/table_comparison_row_count_factor_equality_expectation) | Aggregate rule that evaluates whether the number of rows in the current table is equal to a factor of the number of rows in a specified reference table, with optional row filtering before counting.  
  
### Missing values, unique values, and types

Name | Description  
---|---  
[Column Type Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/column_type_expectation) | Aggregate rule that evaluates whether the column data type matches a specified type. This rule requires `bigquery.tables.get`, `bigquery.tables.list`, and `bigquery.datasets.get` permissions on the table and dataset being queried.  
[Column Type List Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/column_type_list_expectation) | Aggregate rule that evaluates whether the column data type is in a specified set. This rule requires `bigquery.tables.get`, `bigquery.tables.list`, and `bigquery.datasets.get` permissions on the table and dataset being queried.  
[Non Null Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/non_null_expectation) | Row-level rule that evaluates whether each column value is not null.  
[Null Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/null_expectation) | Row-level rule that evaluates whether each column value is null.  
[String Case Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/string_case_expectation) | Row-level rule that evaluates whether each column value string matches a specified casing.  
[Uniqueness Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/uniqueness_expectation) | Row-level rule that evaluates whether each column value is unique.  
  
### Sets and ranges

Name | Description  
---|---  
[Decreasing Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/decreasing_expectation) | Aggregate rule that evaluates whether the values in a column are decreasing. `NULL` values are ignored. Returns the first row where the expectation isn't met.  
[Increasing Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/increasing_expectation) | Aggregate rule that evaluates whether the values in a column are increasing. `NULL` values are ignored. Returns the first row where the expectation isn't met.  
[Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/range_expectation) | Row-level rule that evaluates whether each column value lies within a specified range.  
[Reference Set Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/reference_set_expectation) | Row-level rule that evaluates whether each column value is contained by a specified reference set.  
[Set Exclusion Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/set_exclusion_expectation) | Row-level rule that evaluates whether each column value isn't contained by a specified set.  
[Set Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/set_expectation) | Row-level rule that evaluates whether each column value is contained by a specified set.  
  
### String matching

Name | Description  
---|---  
[Pattern Exclusion Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/pattern_exclusion_expectation) | Row-level rule that evaluates whether each column value doesn't match a specified SQL `LIKE` pattern.  
[Pattern Exclusion Expectation List](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/pattern_exclusion_expectation_list) | Row-level rule that evaluates whether each column value doesn't match any of the specified SQL `LIKE` patterns.  
[Pattern Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/pattern_expectation) | Row-level rule that evaluates whether each column value matches a specified SQL `LIKE` pattern.  
[Pattern Expectation List](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/pattern_expectation_list) | Row-level rule that evaluates whether each column value matches at least one of the specified SQL `LIKE` patterns.  
[Regex Exclusion Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/regex_exclusion_expectation) | Row-level rule that evaluates whether each column value doesn't match a specified regular expression.  
[Regex Exclusion Expectation List](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/regex_exclusion_expectation_list) | Row-level rule that evaluates whether each column value doesn't match any of the specified regular expressions.  
[Regex Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/regex_expectation) | Row-level rule that evaluates whether each column value matches a specified regular expression.  
[Regex Expectation List](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/regex_expectation_list) | Row-level rule that evaluates whether each column value matches at least one of the specified regular expressions.  
[String Length Equality Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/string_length_equality_expectation) | Row-level rule that evaluates whether each column value string length equals a specified value.  
[String Length Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/string_length_range_expectation) | Row-level rule that evaluates whether each column value string length lies within a specified range.  
  
### Aggregate functions

Name | Description  
---|---  
[Distinct Values Containment Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/distinct_values_containment_expectation) | Aggregate rule that evaluates whether the set of distinct column values contains all the values in a specified set.  
[Distinct Values Count Equality Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/distinct_values_count_equality_expectation) | Aggregate rule that evaluates whether the number of distinct values in the column equals a specified value.  
[Distinct Values Count Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/distinct_values_count_range_expectation) | Aggregate rule that evaluates whether the number of distinct values in the column lies within a specified range.  
[Distinct Values Match Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/distinct_values_match_expectation) | Aggregate rule that evaluates whether the set of distinct column values exactly matches a specified set.  
[Distinct Values Proportion Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/distinct_values_proportion_expectation) | Aggregate rule that evaluates whether the proportion of distinct values in the column (that is, distinct values count / total rows count) is within a specified range.  
[Distinct Values Set Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/distinct_values_set_expectation) | Aggregate rule that evaluates whether each distinct column value is contained by a specified set.  
[Max Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/max_range_expectation) | Aggregate rule that evaluates whether the column maximum lies within a specified range.  
[Mean Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/mean_range_expectation) | Aggregate rule that evaluates whether the column average lies within a specified range. If a floating-point type is returned, the [`AVG()` function's result is non-deterministic](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions#avg).  
[Median Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/median_range_expectation) | Aggregate rule that evaluates whether the column median lies within a specified range.  
[Min Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/min_range_expectation) | Aggregate rule that evaluates whether the column minimum lies within a specified range.  
[Mode Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/mode_range_expectation) | Aggregate rule that evaluates whether all column modes (most frequent values) lie within a specified range. If there are multiple modes, each will be checked against the range and any failing modes will be returned.  
[Mode Set Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/mode_set_expectation) | Aggregate rule that evaluates whether all column modes (most frequent values) are within the specified set. `NULL` values are ignored when calculating modes. If there are multiple modes with the same highest frequency, each will be checked against the set and any failing modes will be returned in an array.  
[Quantile Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/quantile_range_expectation) | Aggregate rule that evaluates whether the value at the specified quantile for the column lies within a specified range.  
[Standard Deviation Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/standard_deviation_range_expectation) | Aggregate rule that evaluates whether the column standard deviation lies within a specified range.  
[Sum Range Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/sum_range_expectation) | Aggregate rule that evaluates whether the column sum lies within a specified range. If a floating-point type is returned, the [`SUM()` function's result is non-deterministic](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions#sum).  
[Table Comparison Unique Values Count Equality Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/table_comparison_unique_values_count_equality_expectation) | Aggregate rule that evaluates whether the number of unique values in a specified column is equal between the current table and a reference table.  
  
### Multi-column

Name | Description  
---|---  
[Column Comparison Equality Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/column_comparison_equality_expectation) | Row-level rule that evaluates whether the value in column A is equal to the value in column B for each row.  
[Column Comparison Greater Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/column_comparison_greater_expectation) | Row-level rule that evaluates whether the value in column A is greater than the value in column B for each row.  
[Column Pairs Set Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/column_pairs_set_expectation) | Aggregate rule that evaluates whether the paired values from column A and column B are contained by a specified set.  
[Multi Column Sum Equality Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/multi_column_sum_equality_expectation) | Aggregate rule that evaluates whether the sum of all rows across a specified list of columns equals a specified value. If a floating-point type is returned, the [`SUM()` function's result is non-deterministic](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions#sum).  
[Multi Column Uniqueness Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/multi_column_uniqueness_expectation) | Row-level rule that evaluates whether the combination of values across a specified list of columns is unique for each row (for example, a multi-column primary key).  
[Record Column Uniqueness Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/record_column_uniqueness_expectation) | Row-level rule that evaluates whether the values across a specified list of columns are unique within each record (row). Note that records can be duplicated.  
  
### Distributional functions

Name | Description  
---|---  
[Date Part Completeness Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/date_part_completeness_expectation) | Aggregate rule that evaluates whether a table has data for every interval (for example, every day) within a date range.  
[Standard Deviation Values Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/standard_deviation_values_expectation) | Row-level rule that evaluates whether each column value lies within a specified number of standard deviations from the column average.  
  
### Generic conditions

Name | Description  
---|---  
[Row Condition Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/row_condition_expectation) | Row-level rule that evaluates whether each row in a table passes the specified condition.  
[SQL Assertion](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/sql_assertion) | Aggregate rule that evaluates the number of rows returned for the provided statement. If any rows are returned, this rule fails.  
[Table Condition Expectation](https://console.cloud.google.com/dataplex/projects/dataplex-templates/locations/global/ruleLibraries/rule-library/ruleTemplates/table_condition_expectation) | Aggregate rule that evaluates whether the provided expression is true for a table.  
  
## What's next

  * Learn how to [use auto data quality](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality) for data validation.
  * Learn about metadata management in the [Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).
  * Learn about [data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview).
  * Learn how to [reuse data quality rules](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
