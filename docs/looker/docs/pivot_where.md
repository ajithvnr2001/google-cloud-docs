---
url: https://docs.cloud.google.com/looker/docs/pivot_where/
title: pivot_where Function \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:24.910728+00:00
---

# pivot_where Function  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/pivot_where/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  pivot_where Function Stay organized with collections  Save and categorize content based on your preferences. 

The `pivot_where` function can be used in a [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations) to select a pivot column by a condition.

## Syntax

**`pivot_where(select_expression, expression)`**

The `pivot_where` function returns the value of `expression` for the pivot column which uniquely satisfies `select_expression` or `null` if such a column does not exist or is not unique.

## Examples

In the following example we look for the pivot column that is based on "Order Status", and has a value of "pending". If we find it, return the "Order Count" in that cell:
    
    
    pivot_where(${orders.status} = "pending", ${orders.count})
    

## Things to know

  1. If there is _exactly_ one pivot column where `select_expression` is true, the `expression` is returned. Otherwise the `expression` returns NULL.

  2. `pivot_where` cannot be used in a [custom filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
