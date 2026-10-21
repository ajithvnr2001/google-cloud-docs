---
url: https://docs.cloud.google.com/looker/docs/pivot_index/
title: pivot_index function \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:24.575576+00:00
---

# pivot_index function  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/pivot_index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  pivot_index function Stay organized with collections  Save and categorize content based on your preferences. 

The `pivot_index` function can be used in [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to extract and manipulate the value of a pivoted column based on its index (in other words, its position).

## Syntax

**`pivot_index(expression, pivot_index)`**

The `pivot_index` function evaluates `expression` in the context of the pivot column at the position `pivot_index` (1 for first pivot, 2 second pivot, etc.) The function returns null for unpivoted results.

## Examples

The following table shows a query that counts the number of orders made in each season of the year. The query includes a pivoted dimension, **Products Category** , which has the values `Swimwear` and `Coats`. To compute the total number of orders made in each season across all categories, create a **Total Orders Count** table calculation.

Products Category | Swimwear | Coats | Total Orders Count  
---|---|---|---  
Season | Orders Count | Orders Count  
Winter | 3 | 671 | 674  
Spring | 278 | 120 | 398  
Summer | 840 | 21 | 861  
Fall | 30 | 432 | 462  
  
The **Total Orders Count** table calculation adds the value of the first pivot column to the value of the second pivot column. The formula is:
    
    
    pivot_index(${orders.count}, 1) + pivot_index(${orders.count}, 2)
    

## Things to know

`pivot_index` cannot be used in a [custom filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
