---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-calculate-percent-change-percent-previous/
title: Calculating percent of previous and percent change with table calculations \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:37.148466+00:00
---

# Calculating percent of previous and percent change with table calculations  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-calculate-percent-change-percent-previous/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Calculating percent of previous and percent change with table calculations Stay organized with collections  Save and categorize content based on your preferences. 

> As an alternative to the methods that this page describes, you can use [shortcut calculations](https://docs.cloud.google.com/looker/docs/table-calculations#quick_calculations) to perform common calculations on numeric fields that are in an Explore's data table without using Looker [functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators) when you have the [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) to create table calculations. 

[Table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) let you create ad hoc metrics and perform calculations on the data that is returned by an Explore query. This is convenient for calculating metrics like **percent of previous** and **percent change**. 

This page shows you how to calculate these metrics — both down columns and across pivoted rows. 

##  Calculating percent of previous and percent change down columns using `offset()`

The [`offset()`](https://docs.cloud.google.com/looker/docs/functions-and-operators#positional) table calculation function lets you reference values from other rows in the same column. This is perfect for calculating percent of previous and percent change down columns. 

The following examples use the data from the following table, which includes **Orders Count** grouped by **Orders Created Date** : 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-percent-previous-down-column-example-table-2310.png)

###  Calculating percent of previous down columns using `offset()`

To calculate the percent of previous of `orders.count`, you can make a table calculation such as the following: 
    
    
    ${orders.count} / offset(${orders.count}, -1)

This calculation divides each value in the column by the value in the row that precedes it. 

###  Calculating percent change down columns using `offset()`

You can calculate percent change similarly to percent of previous, and then subtract the entire calculation by 1: 
    
    
    ${orders.count} / offset(${orders.count}, -1) -1 

### The results

The percent of previous and percent change table calculations yield the following results: 

![Explore data table showing two new columns for the Orders Count percent of previous and Orders Count percent change table calculations.](https://docs.cloud.google.com/static/looker/docs/images/hc-percent-previous-down-column-result-table-2310.png)

You can [customize the format](https://docs.cloud.google.com/looker/docs/table-calculations#creating_table_calculations) of table calculation values by selecting a format from the **Format** drop-down menu in the **Create table calculation** or **Edit table calculation** pop-up. Alternatively, you can use custom formatting as explained on the [Adding custom formatting to numeric fields documentation page](https://docs.cloud.google.com/looker/docs/custom-formatting) (if you want something other than the available default formats). 

##  Calculating percent change and percent of previous across rows using `pivot_offset()`

With [pivoted results](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions), the [`pivot_offset()`](https://docs.cloud.google.com/looker/docs/functions-and-operators#positional) table calculation function lets you reference values that are on the same row in different columns. In the following examples, using `pivot_offset(), -1` references the previous column (rather than the previous row). 

The following examples use the data from the following table, which includes **Orders Count** grouped by **Orders Created Date** and pivoted by **Users Age Tier** : 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-percent-previous-across-rows-example-table-2406.png)

###  Calculating percent of previous across pivoted rows using `pivot_offset()`

To calculate percent of previous across rows, you can use `pivot_offset()` in the same way that `offset()` was used in the examples that showed how to calculate the percent of previous and the percent change down columns: 
    
    
    ${orders.count} / pivot_offset(${orders.count}, -1)

This expression divides each value in the table by the value in the same row, located one column to the left. This results in the following table: 

![Explore data table showing a new pivot column for the Orders Count percent of previous - across rows table calculation.](https://docs.cloud.google.com/static/looker/docs/images/hc-percent-previous-across-rows-results-table-2406.png)

###  Calculating percent change across pivoted rows using `pivot_offset()`

Again, you can use `pivot_offset()` to make calculations across pivoted rows the same way you use `offset()` when calculating down columns: 
    
    
    (${orders.count} / pivot_offset(${orders.count}, -1)) - 1

This is the same expression as percent of previous, just subtracted by 1. This results in the following table: 

![Explore data table showing a new pivot column for the Orders Count percent change - across rows table calculation.](https://docs.cloud.google.com/static/looker/docs/images/hc-percent-change-across-rows-results-table-2406.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-06 UTC."],[],[]] 
