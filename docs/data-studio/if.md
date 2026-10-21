---
url: https://docs.cloud.google.com/data-studio/if/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:34.883452+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/if/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IF

`IF` defines a condition and returns a result when that condition is met, or returns a different result if that condition is not met.

**Note:** `IF` is similar to `CASE` but acts only on a single condition, and can return only one true result or one false result.

## Sample usage

Calculate a bonus rate if actual sales exceed forecast sales:

`IF(Actual > Forecast, Bonus *1.2, Bonus)`

## Syntax

`IF( condition, true_result, false_result )`

### Parameters

  * `condition` \- The expression to evaluate. `condition` can be any valid Boolean expression.
  * `true_result` \- the value to return if `condition` is true. `true_result` can be any valid expression.
  * `false_result` \- the value to return if `condition` is false. `false_result` can be any valid expression.



## Examples

Return a dimension based on a parameter selection.

For example, you can create a **Boolean** parameter, **Forecast Parameter** , and use it to return a column of forecasted data. Otherwise, use the actual data:

`IF(Forecast Parameter, Forecast Data, Actual Data)`

Identify records that are older than a certain number of days before today:

`IF(DATETIME_DIFF(TODAY(),Date,DAY) > 60, "old","new")`

A more complex condition with logical `AND`, and regular expression matching:

`IF(Event name = "purchase" AND (REGEXP_MATCH(Page path, ".*footwear.*") OR REGEXP_MATCH(Page path, ".*shoes.*")), "Shoe Sales", Page title)`

**Note:** `IF` is limited to returning only one of two possible results: the `true_result` or the `false_result`. To create a function that can return more possible results, use [`CASE`](https://docs.cloud.google.com/data-studio/case-searched) or [simple `CASE`](https://docs.cloud.google.com/data-studio/case-simple) instead.

## Related resources

  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)
  * [google/RE2 GitHub documentation](https://github.com/google/re2/wiki/Syntax)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
