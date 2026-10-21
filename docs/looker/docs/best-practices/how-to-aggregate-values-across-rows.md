---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-aggregate-values-across-rows/
title: Aggregating across rows (row totals) in table calculations \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:36.910837+00:00
---

# Aggregating across rows (row totals) in table calculations  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-aggregate-values-across-rows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Aggregating across rows (row totals) in table calculations Stay organized with collections  Save and categorize content based on your preferences. 

> You can use [shortcut calculations](https://docs.cloud.google.com/looker/docs/table-calculations#quick_calculations) to perform common calculations on numeric fields that are in an Explore's data table without using Looker [functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators) when you have the [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) to create table calculations. 

There may be situations where you or other users want to analyze [pivoted data in Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions). This page discusses how you can use the [`pivot_row()` table calculation function](https://docs.cloud.google.com/looker/docs/functions-and-operators#pivot-related_functions_for_table_calculations_only) to create row totals and other aggregations that can help users gain further insight into Explore data. 

##  How does `pivot_row()` work? 

The `pivot_row()` table calculation function groups all the values of a pivoted row into a list. 

This example uses the following Explore data table with **Products Count** grouped by **Orders Created Date** and pivoted by **Users Age** : ![](https://docs.cloud.google.com/static/looker/docs/images/hc-agg-across-rows-1-2208.png)

You can use `pivot_row()` to write a table calculation that will group all of the **Products Count** row values into one column: 
    
    
    pivot_row(${products.count})

The table calculation then outputs a new column that displays a list of all the values of **Products Count** in each pivoted row: ![](https://docs.cloud.google.com/static/looker/docs/images/hc-agg-across-rows-2-2208.png)

##  Calculating the row total using `pivot_row()`

You can also perform calculations on the lists that you create with the `pivot_row()` function to make further analyses. For example, you can calculate row totals by using the `sum()` function on the listed values that are returned by `pivot_row()`. 

Using the same Explore data table with **Products Count** grouped by **Orders Created Date** and pivoted by **Users Age** , you can write the following table calculation to output the row totals for **Products Count** : 
    
    
    sum(pivot_row(${products.count}))

The table calculation sums the list of **Products Count** values that are calculated with the `pivot_row()` function and outputs a new column that displays the total of each pivoted row: ![](https://docs.cloud.google.com/static/looker/docs/images/hc-agg-across-rows-3-2208.png)

##  Calculating other aggregations using `pivot_row()`

You can use the `pivot_row()` function to aggregate across any pivoted row. For example, rather than a `sum()`, you can also calculate the `mean()` of the values in the list, the `max()`, the `min()`, and so on. This section of the [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators#functions_for_table_calculations_only) documentation page lists all the available table calculation functions and operators. 

You can also perform more complex calculations across pivot rows with the `pivot_row()` function, including a percent of total. Read about how to use `pivot_row()` to calculate a percent of total across rows in the [How to calculate percent-of-total](https://docs.cloud.google.com/looker/docs/best-practices/how-to-calculate-percent-of-total) Best Practices page. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
