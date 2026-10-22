---
url: https://docs.cloud.google.com/data-studio/countdistinct/
title: COUNT_DISTINCT \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:29.665578+00:00
---

# COUNT_DISTINCT  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/countdistinct/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  COUNT_DISTINCT Stay organized with collections  Save and categorize content based on your preferences. 

The `COUNT_DISTINCT` function counts the number of unique items in a field.

## Syntax

`COUNT_DISTINCT(X)`

### Parameters

  * `X` \- a field or an expression that contains the items to be counted.



## How the `COUNT_DISTINCT` function works

The `COUNT_DISTINCT` function takes one parameter, which can be the name of a dimension or an expression that doesn't result in an aggregation. `COUNT_DISTINCT` returns the total number of unique items in that field or expression.

To count all items, including duplicates, use `COUNT`. **Tip:** There are 2 other ways to apply this function:

  * In a data source, change a field's **Aggregation** type to `Count Distinct`.
  * in a report, [edit the field's aggregation](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) in a chart. 



## Examples

Example formula  |  Output   
---|---  
` COUNT_DISTINCT(user_id) ` |  22,854,921   
` COUNT_DISTINCT(order_id) ` |  497,091,812   
  
## Limits of `COUNT_DISTINCT`

When using the `COUNT_DISTINCT` function, note the following:

### `COUNT_DISTINCT` works with unaggregated data

You can't apply this function to metrics, including fields with an **Aggregation** type of **Auto** , or to an expression that's the result of another aggregation function. For example, a formula such as `COUNT_DISTINCT(Sessions)` in a Google Analytics data source produces an error because `Sessions` is an **Auto** aggregated field.

### Consider using `APPROX_COUNT_DISTINCT` for BigQuery data

To avoid possibly incurring higher query costs when using BigQuery data sources, consider using `APPROX_COUNT_DISTINCT`.

### Variable results from function pushdown

To optimize performance, Data Studio attempts to delegate (or "push down") the calculation of `COUNT_DISTINCT` to the underlying data source whenever possible. Because the actual count is performed by the connected system rather than by Data Studio, the results can vary depending on how that system implements distinct counting.

For example, factors that can lead to differences in distinct counts include the following:

  * **SQL databases** : Different SQL dialects may handle case-sensitivity, trailing space comparison, or null value counting in unique ways.
  * **File-based sources** : For file connectors (such as CSV files), results depend on target-site parsing behavior and internal engine operations.
  * **SaaS APIs** : Cloud services and SaaS connectors are constrained by their API capabilities, which may return approximate counts or apply specific filtering logic.



## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
