---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-calculate-percent-of-total/
title: How to calculate percent of total \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:37.574826+00:00
---

# How to calculate percent of total  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-calculate-percent-of-total/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  How to calculate percent of total Stay organized with collections  Save and categorize content based on your preferences. 

> You can use [shortcut calculations](https://docs.cloud.google.com/looker/docs/table-calculations#quick_calculations) to perform common calculations on numeric fields that are in an Explore's data table without using Looker [functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators) when you have the [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) to create table calculations. 

Calculating a percentage of the total for a given row in a table can help analysts see how one piece of data contributes to the whole. This page provides an overview of how to calculate percent of total calculations in Looker — for queries with and _without_ [pivoted dimensions](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions). 

## Calculating percent of total for queries without pivoted dimensions

There are a few ways to calculate percent of total for query results that do not include [pivoted dimensions](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions): 

  * Using table calculations
  * Using a pie chart visualization



### Using table calculations

You can use [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to calculate a percent of total by dividing a row's value by the sum of its column: `${measure}/sum(${measure})`

For example, the following Explore displays the **Order Items Count** grouped by **Users State** : 

![](https://docs.cloud.google.com/static/looker/docs/images/percent-of-total-unpivot-explore-2210.png)

You can calculate the percent of total for each **Order Items Count** value by dividing by the [sum](https://docs.cloud.google.com/looker/docs/functions-and-operators#math) of that column: 
    
    
    ${order_items.count}/sum(${order_items.count})

The resulting percent of total table calculation will display percentages as a new column in the data table:

![](https://docs.cloud.google.com/static/looker/docs/images/percent-of-total-unpivot-explore-calc-results-2210.png)

### Using a pie chart visualization

You can also use a [pie chart](https://docs.cloud.google.com/looker/docs/pie-options) to display the percent of total without creating a table calculation. The percentages are listed in the legend alongside the fields to which they belong.

For example, the results of the preceding Explore example — **Order Items Count** grouped by **Users City** — are visualized in the following pie chart that displays the percent of total for each city's **Order Items Count** value in the legend: 

![](https://docs.cloud.google.com/static/looker/docs/images/percent-of-total-unpivot-explore-image-results-2210.png)

This method is valid if you are only using the visualization. A percent of total calculation will not be included in the Explore data table, and any downloaded results will not contain the percent of total. 

## Calculating percent of total for queries with pivots

There are also a few ways to calculate a percent of total across columns for Explores that do include [pivoted dimensions](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions): 

  * Using table calculations
  * Using the **Stacked Percentage** visualization setting



### Using table calculations

You can use table calculations to calculate a percent of total across pivoted columns by dividing a row's value by the sum of its row: `sum(pivot_row(${measure}))/sum(sum(pivot_row(${measure}))) `

This calculation performs the following functions: 

  * [`pivot_row`](https://docs.cloud.google.com/looker/docs/functions-and-operators#pivot-related_functions_for_table_calculations_only) returns the pivoted values of a row as a list. 
  * `sum(pivot_row(${measure}))` sums the list of pivoted values across a row to produce a row total. The row total is essentially its own column value. 
  * `sum(sum(pivot_row(${measure})))` produces the grand total of row values. 
  * `sum(pivot_row(${measure}))/sum(sum(pivot_row(${measure})))` is the final expression, dividing the row total by the grand row total to get the percent of total for that row. 



The following Explore — **Order Items Count** grouped by **Users Created Date** and pivoted by **Users State** — displays calculations for each part of the percent of total table calculation: 

  * **Order Items Row Total** : `sum(pivot_row(${order_items.count}))`
  * **Order Items Grand Total** : `sum(sum(pivot_row(${order_items.count})))`
  * **Order Items Percent of Total** : `sum(pivot_row(${order_items.count}))/sum(sum(pivot_row(${order_items.count})))`



![](https://docs.cloud.google.com/static/looker/docs/images/percent-of-total-pivot-explore-2210.png)

### Using the Stacked Percentage visualization setting

If you only need the percent of total to be displayed in a visualization, you can use the **Stacked Percentage** [**Plot**](https://docs.cloud.google.com/looker/docs/column-options#plot_menu_options) menu option to automatically display the percent of total for the following visualization types: 

  * Column 
  * Bar 
  * Scatterplot 
  * Line 
  * Area 



Select the **Stacked Percentage** option in the **Plot** tab of the **Edit** menu on an Explore's **Visualization** bar: 

![](https://docs.cloud.google.com/static/looker/docs/images/percent-of-total-vis-edit-plot-2210.png)

Using the **Stacked Percentage** method for an Explore that displays values for **Order Items Count** grouped by **Orders Created Year** and pivoted by **Users State** results in the following [column chart](https://docs.cloud.google.com/looker/docs/column-options) visualization. You can hover your cursor over each section of the column to see the percent of total for each order created date and age tier combination in the tooltip: 

![Stacked Percentage column chart displaying percent of total values in the cursor tooltip.](https://docs.cloud.google.com/static/looker/docs/images/percent-of-total-vis-1-2210.png)

The information displayed in the tooltip will not be included in any static images or downloads of the chart. If you need to export the data or a static image of the chart, you can use the table calculation method or enable the **Value Labels** setting on the [**Values**](https://docs.cloud.google.com/looker/docs/column-options#values_menu_options) tab of the visualization **Edit** menu to display the percentages in the visualization: 

![Stacked Percentage column chart displaying percent of total values.](https://docs.cloud.google.com/static/looker/docs/images/percent-of-total-vis-2-2210.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
