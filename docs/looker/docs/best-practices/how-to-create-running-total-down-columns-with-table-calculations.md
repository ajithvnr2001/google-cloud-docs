---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-running-total-down-columns-with-table-calculations/
title: Creating a running total down columns with table calculations \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:37.327455+00:00
---

# Creating a running total down columns with table calculations  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-running-total-down-columns-with-table-calculations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Creating a running total down columns with table calculations Stay organized with collections  Save and categorize content based on your preferences. 

> As an alternative to the methods described on this page, when you have the appropriate [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) to create table calculations, you can use [shortcut calculations](https://docs.cloud.google.com/looker/docs/table-calculations#quick_calculations). Shortcut calculations let you perform common calculations on numeric fields that are in an Explore's data table without the need to use Looker [functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators). 

[Table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) let you create ad hoc metrics and perform calculations on the data that is returned by an Explore query. This is convenient for calculating metrics like running totals. 

This page shows you how to calculate a running total down columns in an Explore's **Data** table. You can also create a running total across rows using table calculations, which you can read more about in the [Aggregating across rows (row totals) in table calculations](https://docs.cloud.google.com/looker/docs/best-practices/how-to-aggregate-values-across-rows) Best Practices page. 

## Using the `running_total()` function

To create a running total down a column using table calculations, you can use the [`running_total()`](https://docs.cloud.google.com/looker/docs/functions-and-operators#functions_for_table_calculations_only) function, which returns the running total of the values in a specified column. 

For example, to create a running total of the column **Inventory Items Count** in the following Explore **Data** table that shows **Inventory Items Count** grouped by **Inventory Items Created Date** , you can create this table calculation: 
    
    
    running_total(${inventory_items.count})

This expression yields the following results: 

![Explore data table showing a new column for the Inventory Items Count running total table calculation.](https://docs.cloud.google.com/static/looker/docs/images/hc-running-total-down-column-result-2308.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
