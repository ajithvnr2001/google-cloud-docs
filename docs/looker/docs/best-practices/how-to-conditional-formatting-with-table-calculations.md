---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-conditional-formatting-with-table-calculations/
title: Conditional formatting using table calculations \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:15.835694+00:00
---

# Conditional formatting using table calculations  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-conditional-formatting-with-table-calculations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Conditional formatting using table calculations Stay organized with collections  Save and categorize content based on your preferences. 

You can use conditional formatting in Looker visualizations to highlight important data points. Looker provides multiple methods for conditional formatting; table calculations are a way to visually emphasize rows in your query results that meet specific conditions. This technique functions similarly to conditional formatting in spreadsheet applications. In this guide, you learn how to implement conditional formatting using table calculations with emoji, with two examples to illustrate the process. 

It's valuable to call out rows that meet (or don't meet) certain conditions in some query results. This pattern is often referred to as _conditional formatting_ in Google Sheets or other spreadsheet applications. 

Looker supports conditional formatting in visualizations in several different ways: 

  * With the [`html`](https://docs.cloud.google.com/looker/docs/reference/param-field-html#using_liquid_variables_in_the_html_parameter) LookML parameter. This is ideal for formatting values when the conditions that drive the formatting are consistent across analysis for a given field. 
  * With [table calculations.](https://docs.cloud.google.com/looker/docs/table-calculations#creating_table_calculations_in_looker) This approach is ideal when the conditions that determine the formatting need to be assignable from Looker's Explore UI. 
  * Directly in the [visualization settings](https://docs.cloud.google.com/looker/docs/table-options#enable_conditional_formatting) for table charts. 



The second approach, which leverages table calculations to determine conditional formatting, is detailed on this page with two examples that use emoji 

To enable emoji: 

  * For Mac: `CTRL + CMD + SPACE` brings up the emoji keyboard that lets you select emoji to drop into a table calculation. 
  * For Windows: [This Buffer article about emoji keyboard shortcuts](https://blog.bufferapp.com/emojis-keyboard-shortcut-mac-windows) goes over how to enable and use emoji. 



**Note: Not all backend databases support emoji in table calculations.** Emoji may unexpectedly break if your instance is migrated to a MySQL backend. Consider using [conditional formatting for table charts](https://docs.cloud.google.com/looker/docs/table-options#enable_conditional_formatting) from the visualization settings editor in an Explore, or [implementing the conditional formatting using HTML](https://discuss.google.dev/t/how-to-change-colors-and-fonts-using-html/119213) instead. 

##  Example 1 

The following example is based on an Explore query with **Inventory Items Count** grouped by **Inventory Items Created Date**. A user wants to add an emoji to indicate whether a value of **Inventory Items Count** is greater than or less than a specified number. 

The first step is to create a calculation that uses the [`if`](https://docs.cloud.google.com/looker/docs/functions-and-operators#logical_functions,_operators,_and_constants) function to specify a condition for categorizing **Inventory Items Count** values, and the [`concat`](https://docs.cloud.google.com/looker/docs/functions-and-operators#string_functions) function to prepend an emoji character depending on whether or not the values satisfy the condition. 

The user wants to use emoji to indicate whether or not a value meets the condition. A green check mark emoji indicates a value that meets the condition, and a red **x** emoji indicates a value that does not meet the condition. 

The table calculation is: 
    
    
    concat(
      if(${inventory_items.count} > 255, "<emoji>" ,
        if(${inventory_items.count} < 260, "<different_emoji>" , " ")), " "
          ,${inventory_items.count})
    

Here the table calculation is shown with emoji in the **Create table calculation** menu: 

![Create table calculation menu with a table calculation that specifies that a green check mark emoji appears when Inventory Items Count values are greater than 255, and a red x emoji appears when Inventory Items Count values are less than 260.](https://docs.cloud.google.com/static/looker/docs/images/hc-cond-formatting-table-calcs-1-2220.png)

This table calculation produces the following table visualization: 

![Table visualization that displays the Inventory Items Count table calculation results as a red x emoji for values less than 260 and a green check emoji for values greater than 255.](https://docs.cloud.google.com/static/looker/docs/images/hc-cond-formatting-table-calcs-2-2220.png)

The **Inventory Items Count** measure column is [hidden](https://docs.cloud.google.com/looker/docs/creating-visualizations#specifying_lookml_fields_to_include_in_the_visualization) from the visualization, so only the table calculation column with the conditionally prepended emoji is visualized. 

## Example 2

Similarly, the Example 1 conditional formatting pattern can be applied to a percent change table calculation to call attention to rows that may warrant additional attention. The following example has two calculations. This example also uses the Explore with **Inventory Items Count** grouped by **Inventory Items Created Date**. 

The first table calculation returns the percent change (using the [`offset`](https://docs.cloud.google.com/looker/docs/functions-and-operators#row-related_functions_for_table_calculations_only) function to compare values associated with different dates in the same column): 
    
    
      (${inventory_items.count} - offset(${inventory_items.count},
      -1))/offset(${inventory_items.count}, -1)
    

In this example of an Explore, the table calculation is named **Inventory Items Count percentage change** , which is referenced in the second table calculation. 

The second table calculation applies the `if` condition and `concat` function to prepend a red **x** emoji to days where **Inventory Items Count** has negative growth as compared to the day before: 
    
    
      concat(
        if((${inventory_items_count_percentage_change}*100) < 0, "<emoji>", " "), " ",
        round(${inventory_items_count_percentage_change}*100,1),
        if(is_null(${inventory_items_count_percentage_change}), " ", "%"))
    

These two table calculations produce an Explore data table with two new rows for the **Inventory Items Count percentage change** and **Inventory Items Count percent change** conditional value emoji table calculations. The resulting table visualization displays the results for all fields except **Inventory Items Count percentage change**. The **Inventory Items Count percentage change** table calculation is hidden from the table visualization: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-cond-formatting-table-calcs-3-2220.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
