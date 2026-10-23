---
url: https://docs.cloud.google.com/data-studio/count/
title: COUNT \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:34.912744+00:00
---

# COUNT  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/count/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  COUNT Stay organized with collections  Save and categorize content based on your preferences. 

The `COUNT` function counts the number of items in a field.

## Syntax

`COUNT( X )`

### Parameters

  * `X` \- a field or expression that contains the items to be counted.



## How the `COUNT``` function works

The `COUNT``` function takes one parameter, which can be the name of a metric, dimension, or an expression of any type. `COUNT``` returns the total number of items in that field or expression, including duplicates.

To count only unique items, use `COUNT_DISTINCT` or `APPROX_COUNT_DISTINCT`.

> There are 2 other ways to apply this function:
> 
>   * In a data source, change a field's **Aggregation** type to `Count`.
>   * in a report, [edit the field's aggregation](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) in a chart.
> 


## Examples

`COUNT(Page)``` \- counts the number of non-unique values in the **Page** dimension.

## Limits of `COUNT`

You can't apply this function to a pre-aggregated field ( **Aggregation** type of **Auto** ), or to an expression which is the result of another aggregation function. For example, a formula such as `COUNT(SUM(x))` will produce an error. 

## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
