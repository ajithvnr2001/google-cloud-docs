---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-reference-lines-with-visualization-editor/
title: Creating reference lines for visualizations with visualization menu settings \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:44.746587+00:00
---

# Creating reference lines for visualizations with visualization menu settings  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-reference-lines-with-visualization-editor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Creating reference lines for visualizations with visualization menu settings Stay organized with collections  Save and categorize content based on your preferences. 

You can add a reference line to several available Looker visualization types: 

  * [Column charts](https://docs.cloud.google.com/looker/docs/column-options#add_reference_line)
  * [Bar charts](https://docs.cloud.google.com/looker/docs/bar-options#add_reference_line)
  * [Line charts](https://docs.cloud.google.com/looker/docs/line-options#add_reference_line)
  * [Area charts](https://docs.cloud.google.com/looker/docs/area-options#add_reference_line)
  * [Scatterplot charts](https://docs.cloud.google.com/looker/docs/scatter-options#add_reference_line)



Default reference line options include static value, median, average (mean), maximum, minimum, and range, which can be selected from the visualization option settings [**Edit**](https://docs.cloud.google.com/looker/docs/line-options#value,_start_value,_and_end_value_\(for_a_reference_line\)) menu. 

However, you may want to represent a more specific metric — such as a weighted average — with a reference line, instead of the default reference line options. You can make custom reference lines by creating [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations#creating_table_calculations_in_looker) and then plotting them in visualizations. 

Continuing with the weighted average example shown previously, let's say you wanted to weight average user age by the count of users and had measures for each of these in an Explore. To create a weighted average vertical reference line, you would perform the following steps: 

  1. [Add](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#adding_more_dimensions_for_more_detail) the **Users Count** measure and **Users Average Age** measures to an Explore query. 
  2. Create a table calculation like the following to calculate the weighted average with the two measures: 
         
         mean(sum(${users.count}*${users.average_age})/sum(${users.count}))

The table calculation will return a single value — the weighted average — for every row of the query. 

  3. If the selected visualization type is not a line chart, such as a column chart or bar chart, you can visualize the table calculation as a line by selecting the **Line** visualization type for the table calculation series on the [**Series**](https://docs.cloud.google.com/looker/docs/creating-visualizations#including_multiple_visualization_types_on_a_single_chart) tab of the **Edit** menu. Since the table calculation only returns one value, the line will appear as a horizontal reference line. 

If you do not want **Users Average Age** to appear in your visualization, you can also hide that field using the [**Hide from Visualization**](https://docs.cloud.google.com/looker/docs/creating-visualizations#specifying_lookml_fields_to_include_in_the_visualization) option.




Visualized as a column chart, the **Users Count** and **Users Average Age** grouped by **Users Age** Explore data looks like the following with the **Weighted Average Age** reference line: 

![Column chart with the Weighted Average Age calculation visualized as a horizontal reference line.](https://docs.cloud.google.com/static/looker/docs/images/hc-reference-lines-for-charts-result-2210.png)

If you want to be able to reuse the table calculation in future Explores, you can re-create the calculation between numeric fields with a [`number`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number) type measure. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
