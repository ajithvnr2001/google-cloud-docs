---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-plot-dimensions-on-the-y-axis/
title: How to plot dimensions on a Y-axis \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:45.172716+00:00
---

# How to plot dimensions on a Y-axis  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-plot-dimensions-on-the-y-axis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  How to plot dimensions on a Y-axis Stay organized with collections  Save and categorize content based on your preferences. 

> _All user data presented on this page is made up for example purposes._

Looker visualizations automatically determine which values to plot on a y-axis based on what field types are present in a query. For example, if an Explore that breaks down **Users First Name** and **Users Age** for the top 10 highest **Orders Count** is visualized as a column chart, the 10 dimension values for **Users First Name** and **Users Age** are automatically concatenated and separated by a dash (–) on the x-axis. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-plot-dimension-y-axis-opening-screenshot-2220.png)

What if you want to separate **Users Age** and **Users First Name** so that **Users Age** is plotted on the y-axis, and **Users First Name** and **Orders Count** appear on the x-axis? 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-plot-dimension-y-axis-result-example-2220.png)

The two following solutions outline how to transform a dimension, such as **Users Age** , into a measure so that it can be visualized on the y-axis: 

  * Using a table calculation — Create a one-off solution directly from an Explore without developing LookML. 
  * Creating a measure — Develop LookML to be able to reuse an expression in future Explores without needing to create a table calculation. 



## Using a table calculation

A [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations) is the fastest and easiest way to plot a dimension on the y-axis. A calculation is typically plotted as a dimension if no measures are involved in the expression. You can make a table calculation behave as a measure by including a measure in the calculation's expression. The key is making sure the measure won't affect the value of the original dimension. 

To use a table calculation to plot a measure on the y-axis, perform the following steps:

  1. If there is no measure in your Explore query, add any measure (such as a count), and then [hide](https://docs.cloud.google.com/looker/docs/creating-visualizations#specifying_lookml_fields_to_include_in_the_visualization) it from the visualization. If there is already a measure in your query that you want to include in the visualization, there's no need to hide it. 
  2. Next, create a table calculation: 
     * For a **numerical field** , the calculation will be as follows:
           
           ${mydimension} + (0 * ${mymeasure})

_The calculation preserves the original dimension value by multiplying the measure by 0._
     * For a **string field** , the calculation will involve two [logical functions,](https://docs.cloud.google.com/looker/docs/functions-and-operators#logical_functions,_operators,_and_constants) `if()` and `is_null()`, instead: 
           
           if(is_null(${mymeasure}),${string_dimension},${string_dimension})

This expression tells Looker to _always_ display the value of the string dimension in place of the measure values. 
  3. Hide the original dimension — **Users Age** in this case — from the visualization, since the table calculation — **Age** measure — now represents the dimension's values in the visualization. 



![](https://docs.cloud.google.com/static/looker/docs/images/hc-plot-dimension-y-axis-table-calc-data-table-2220.png)

To distinguish between values in a visualization — in this example, the **Age** measure table calculation and **Orders Count** measures — you can use [multiple vis types](https://docs.cloud.google.com/looker/docs/creating-visualizations#including_multiple_visualization_types_on_a_single_chart) in a single chart. 

For example, you can visualize **Orders Count** values as a line and **Users Age** values as a column to distinguish them once **Users Age** is plotted on the y-axis. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-plot-dimension-y-axis-result-example-2220.png)

## Creating a measure in LookML

If you plan to plot a specific dimension on a y-axis again in the future, a more sustainable option is to create a [`sum` measure](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum) or [`number` measure](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum) in LookML that makes the dimension you want to plot into a measure. Instead of recreating the same table calculation in an Explore multiple times, you can add the field to a query from the field picker. 

The measure will look similar to this:
    
    
        measure: measure_for_age { ## replace with a new name
            description: "Use this age field for displaying age on the y-axis"
            type: number ## or sum
            sql: ${age} ;; ## replace with your dimension
        }
    

> _Adding a[`description`](https://docs.cloud.google.com/looker/docs/reference/param-field-description) to the measure can help users understand the intended use of a field._

In this case, `measure_for_age` is a `number` type measure, since `number` type measures do not perform any actual aggregation. This means **Measure for Age** will display the same values as **Users Age** because it is a `number` type measure that does not perform any aggregation. 

Once you create the measure, include both the dimension _and_ the new measure in the Explore query. For this example, include the dimensions **Users First Name** and **Users Age** , and include the measures **Orders Count** and **Users Measure for Age**. Finally, hide the dimension that the measure is based on. 

With the **Users Age** dimension hidden from the Explore visualization and custom visualization settings applied, the resulting Explore visualization displays the **Users Measure for Age** on the y-axis and **Users First Name** on the x-axis, and the **Orders Count** values as a line. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-plot-dimension-y-axis-table-calc-measure-explore-2220.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
