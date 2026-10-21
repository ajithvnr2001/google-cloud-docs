---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-vertical-reference-lines/
title: How to create vertical reference lines \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:13:22.407848+00:00
---

# How to create vertical reference lines  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-vertical-reference-lines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  How to create vertical reference lines Stay organized with collections  Save and categorize content based on your preferences. 

**Tip:** Starting in Looker 24.0, you can use the [Chart Config Editor](https://docs.cloud.google.com/looker/docs/chart-config-editor#add_vertical_reference_bands) to create more robust vertical reference lines and bands.

Looker visualization options let you customize your visualization, including [adding reference lines](https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-reference-lines-with-visualization-editor). The reference line options are static value, median, average (mean), maximum, minimum, and range, which can be selected in the **Edit Visualization** settings. 

But what if you want to use vertical reference lines in a graph? For example, what if you want to visualize the various stages of a product launch on specific dates against the orders that were placed during that period? 

## The solution

Using [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations), you can create vertical bars that you can reference in graphs. The vertical lines will appear like those in the following example. 

The following example is based on an Explore with **Orders Count** grouped by **Orders Created Date**. 

To create a vertical reference line: 

  1. [Create a table calculation](https://docs.cloud.google.com/looker/docs/table-calculations#creating_table_calculations) that references the data points in the visualization that you want to highlight with vertical reference lines. This example of a use case uses the following expression to create vertical reference lines to mark stages in the product launch dates using the **Orders Created Date** : 
         
         if(
               to_string(${orders.created_date}) = "2019-12-21" OR
               to_string(${orders.created_date}) = "2019-12-14" OR
               to_string(${orders.created_date}) = "2019-12-07"
               ,
               max(${orders.count})+1, null
               )
             

  2. Next, apply the following sections in the visualization **Edit** menu: 
     * In the [**Series** menu](https://docs.cloud.google.com/looker/docs/line-options#series_menu_options), set the visualization **Type** for the table calculation to **Column**. 
     * In the [**X** menu](https://docs.cloud.google.com/looker/docs/line-options#x_menu_options), change **Scale Type** to **Ordinal**. 
     * In the [**Plot** menu](https://docs.cloud.google.com/looker/docs/line-options#plot_menu_options), make sure **Series Positioning** is _not_ set to **Stacked Percentage**. 



The resulting visualization displays the line representing the number of orders placed over time, and the vertical bars produced by the **Vertical reference line** table calculation mark the launch stages of the product over time — beginning, middle, and end: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-vertical-reference-line-result-2210.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
