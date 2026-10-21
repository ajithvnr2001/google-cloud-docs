---
url: https://docs.cloud.google.com/data-studio/approxcountdistinct/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:30.715040+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/approxcountdistinct/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# APPROX_COUNT_DISTINCT

The `APPROX_COUNT_DISTINCT` function counts the approximate number of unique items in a field.

**Note:** `APPROX_COUNT_DISTINCT` is available only when your data comes from a BigQuery data source. For other data source types, use `COUNT_DISTINCT`.

## Syntax

`APPROX_COUNT_DISTINCT(X)`

### Parameters

  * `field_expression` \- a field or expression that contains the items to be counted.



## How the `APPROX_COUNT_DISTINCT` function works

The `APPROX_COUNT_DISTINCT` function takes one parameter, which can be the name of a metric, dimension, or expression of any type. `APPROX_COUNT_DISTINCT` returns the approximate number of unique items in that field or expression.

`APPROX_COUNT_DISTINCT` is more efficient in terms of query processing than `COUNT_DISTINCT`, but returns less exact results. If your dataset is very large, or if the performance of your report is more important than exact counts, consider using `APPROX_COUNT_DISTINCT`. Using `APPROX_COUNT_DISTINCT` instead of `COUNT_DISTINCT` can also help reduce query costs when using BigQuery data sources.

For an in-depth explanation of how approximate aggregation works, see the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/approximate_aggregate_functions).

## Example

> `APPROX_COUNT_DISTINCT(Page)` \- counts the approximate number of unique values in the **Page** dimension.

## Limits of `APPROX_COUNT_DISTINCT`

  * The `APPROX_COUNT_DISTINCT` function is available only when used with BigQuery data sources. 

  * For data sources which don't support `APPROX_COUNT_DISTINCT`, `APPROX_COUNT_DISTINCT` will act like `COUNT_DISTINCT`.

  * You can't apply this function to a pre-aggregated metric ( **Aggregation** type of **Auto** ), or to an expression that is the result of another aggregation function. For example, a formula such as ```APPROX_COUNT_DISTINCT(Sessions)``` in a Google Analytics data source will produce an error.




## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
