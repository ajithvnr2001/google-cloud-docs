---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-display-confusing-table-calculation-totals-as-nulls/
title: Display potentially confusing table calculation totals as nulls \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:16:26.905482+00:00
---

# Display potentially confusing table calculation totals as nulls  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-display-confusing-table-calculation-totals-as-nulls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Display potentially confusing table calculation totals as nulls Stay organized with collections  Save and categorize content based on your preferences. 

> When you have the appropriate [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) to create table calculations, you can use [shortcut calculations](https://docs.cloud.google.com/looker/docs/table-calculations#quick_calculations), which let you perform common calculations on numeric fields that are in an Explore's data table without the need to use Looker [functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators). 

> You can also apply table calculations directly to the values in the **Total** row. 

## Why calculations in the Total row may be confusing

The examples and discussions on this page are based on an example of an Explore query: **Order Items Count** , **Users Count** , **Order Items per User** , and **Mean Order Items** grouped by **Orders Created Date** with the [**Totals**](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals) option applied: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-potentially-confusing-table-calc-null-2110.png)

The total for the **Order Items per User** is 4.5, which is the expected rounded total of 54,767 (**Order Items Total**) divided by 12,290 (**Users Count Total**). 

The total for the **Mean Order Items** is 54,767, which is the total **Order Items Count** — 54,767 — divided by 1, which may not make sense to display to users. 

As discussed in the [Considerations for using table calculations](https://docs.cloud.google.com/looker/docs/table-calculations#considerations_when_using_table_calculations) section of the [Using table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) documentation page, table calculations calculate totals based on the single **Total** row, not on the values in the data column. The results are clearly understandable for some calculations, like the **Order Items per User** table calculation total. 

However, table calculations that perform aggregations — for example, calculations that use `percentile` and `median` — may calculate totals in confusing ways, such as in the **Mean Order Items** total in the example of the Explore. 

## Replacing a calculation total with a null symbol in the Total row

If you have a potentially confusing result in a table calculation total, you can replace one of your totals with a null symbol using the following table calculation expression. You can replace `my_grouping_dim` with your grouping dimension, and `table_calc` with the table calculation for which you wish to display a null in the **Total** row: 
    
    
    if(is_null(my_grouping_dim), null, <table_calc>)

If the previous expression is applied to the **Mean Order Items** table calculation, the table calculation will display a null symbol for the **Mean Order Items** total in the data table **Total** row: 
    
    
      if(is_null(${orders.created_date}), null, mean(${order_items.count}))
    

This result looks like the following in the data table: 

![Explore data table displaying a null instead of 54,767 in the Mean Order Items Total row column.](https://docs.cloud.google.com/static/looker/docs/images/hc-potentially-confusing-table-calc-null-3-2110.png)

## Additional resources

For additional information regarding troubleshooting totals for measures, see the [Why don't my totals match the values in my table?](https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-looker-totals) Best Practices page. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
