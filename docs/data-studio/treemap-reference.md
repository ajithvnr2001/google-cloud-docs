---
url: https://docs.cloud.google.com/data-studio/treemap-reference/
title: Treemap reference \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:17:31.654522+00:00
---

# Treemap reference  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/treemap-reference/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Treemap reference Stay organized with collections  Save and categorize content based on your preferences. 

A treemap shows your data organized into dimension hierarchies. For example, you can use a treemap to show the average annual sales of each item in a product category, broken down by its subcategory and its place in the product hierarchy.

![A Data Studio treemap visualization with blue, orange, and purple branches and no value labels.](https://docs.cloud.google.com/static/data-studio/images/presettreemap-2019-06-25-svg-rge.svg)

## Treemaps in Data Studio

Data in a treemap is displayed in "branches" (also called "nodes"). Each branch can have zero or more sub-branches, and one parent branch (except for the root, which has no parents). Each branch is displayed as a rectangle, sized and colored according to the values in your data. Sizes and colors are valued relative to all other branches in the graph.

Treemaps are a good hypothesis-generation tool because they can help expose the relative importance of, and the relationship between, different entities.

## Treemap examples

The following treemap displays the number of items sold by an online pet store. The branch labels come from the **Department** and **Item** dimensions.

![A treemap displays Avian, Canine, and Feline Department dimension categories and related Item dimension values.](https://docs.cloud.google.com/static/data-studio/images/treemap-show-levels-2-2019-06-26.png)

Here's how the underlying data for this chart is organized:

![A Google Sheet with data organized in columns labeled Date, Department, Item, Qty sold, and Price.](https://docs.cloud.google.com/static/data-studio/images/treemap-sheets-data-2019-06-26.png)

## Add the chart

[Add a new chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report) or select an existing chart. Then, use the **Properties** panel to configure the chart's **Setup** tab and **Style** tab properties to set up the chart data and style the chart, respectively.

## Set up the chart data

The options in the **Setup** tab of the **Properties** panel determine how the chart's data is organized and displayed.

### Data source

A data source provides the connection between the component and the underlying dataset.

  * To change the chart's data source, click the current data source name.
  * To view or edit the data source, click the ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png)**Edit data source** icon. (You must have at least [Viewer permission](https://docs.cloud.google.com/data-studio/viewer-user-type) to see this icon.)
  * Click **Blend data** to see data from multiple data sources in the same chart. [Learn more about data blending](https://docs.cloud.google.com/data-studio/how-blends-work).



### Dimension

Dimensions are data categories. Dimension values (the data that is contained by the dimension) are names, descriptions, or other characteristics of a category.

#### Drill down

This option appears on charts that support it.

Drilling down gives viewers a way to reveal additional levels of detail within a chart. When you turn on the **Drill down** switch, each dimension that you add becomes another level of detail that you can drill into. [Learn more about chart drill down](https://docs.cloud.google.com/data-studio/add-drill-actions-to-charts).

#### Levels to show

The **Levels to show** option determines the granularity of the chart. For example, the sample chart in the Treemap examples section on this page has **Levels to show** set to **2** , causing it to show two levels of detail (**Department** and **Item**).

Setting **Levels to show** to **1** causes the chart to display only one level of detail (**Department**):

![A treemap with the Levels to show option set to 1 displays only Department-level details.](https://docs.cloud.google.com/static/data-studio/images/treemap-show-levels-1-2019-06-26.png)

> **What's the difference between drill down and levels to show?**
> 
> **Drill down** lets you focus on a specific level of detail, while **Levels to show** controls how many levels of detail appear in the treemap. For example, here's the result of drilling down into a chart. Note that it now displays only one level of detail, but that level is now the **Item** dimension level.
> 
> ![A treemap displays item details when a user drills into the Item dimension.](https://docs.cloud.google.com/static/data-studio/images/treemap-show-levels-1-dd-2019-06-26.png)
> 
> [See an example of a treemap with drill down turned on](https://datastudio.google.com/reporting/1LOEYnYhJXrfAQpUAHDLH-9484eE93uZG/page/CLmn) (the report is in English only).

### Metric

This option displays the metric data broken down according to the selected dimension. For example, a chart that shows annual sales data could be broken down by a **Sales Region** dimension to show sales by region or by an **Employee ID** dimension to show sales by sales associate.

#### Optional metrics

You can add [optional metrics](https://docs.cloud.google.com/data-studio/optional-metrics) by turning on the **Optional metrics** switch and selecting metrics from the **Add metric** field selector. You can also click metrics from the fields list on the **Data** panel and place them in the **Optional metrics** selector.

#### Metric sliders

Turn on the **Metric sliders** switch to add a [metric slider](https://docs.cloud.google.com/data-studio/metric-slider) to your chart.

### Fields

The **Fields** options let you choose how to color the treemap.

#### Color

Select **Metric** or **Dimension** to color the treemap by either the metric or the dimension fields that are set. By default, treemap charts are colored by **Metric**. The **Fields** setting determines the available options in the **Color by** setting in the **Style** tab.

#### Secondary label

You can optionally choose another dimension or metric for the **Secondary label** setting to display that field's corresponding values in the treemap chart.

### Display

The **Display** settings determine the number of breakdown dimension series that are displayed on the chart. You can choose to display the series from the **Top N** of query results or **Bottom N** of query results. You can click the icon next to this value to increase to the max number of results supported by the visualization.

**Note:** **Top N** is set by default.

When either the **Top N** or **Bottom N** are selected, you can specify the number of rows to display in the **Number of rows** setting.

#### Group the rest as "Others"

When enabled, the **Group the rest as "Others"** setting aggregates the results that are outside of the specified numeric limit into a series that will have the label **Others**. When enabled, **Group the rest as "Others"** lets you compare other series against the context of the remaining results.

**Group the rest as "Others"** is enabled by default.

**Important:** When **Group the rest as "Others"** is not enabled, depending on the chart's configuration, the chart may not display all the data.**Warning:** The **Group the rest as "Others"** option is not compatible with [comparison metrics](https://docs.cloud.google.com/data-studio/add-comparison-metrics-and-running-totals#differences_between_running_calculations_and_calculated_fields). To use comparison metrics, disable the **Group the rest as "Others"** option.

### Filter

Filters restrict the data that is displayed in the component by including or excluding the values that you specify. [Learn more about the filter property](https://docs.cloud.google.com/data-studio/about-filter-properties).

Filter options include the following:

  * **Filter name:** Click an existing filter to edit it. Mouse over the filter name and click **X** to delete it.
  * **Add filter:** Click this option to create a new filter for the chart.



### Date range dimension

This option appears if your data source has a valid date dimension.

**Important:** This option does not appear for Google Ads or Google Analytics data sources, as these automatically select a dimension of type **Date** from the data source.

The date range dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension that is used if you set a date range property for the chart or if a viewer of the report uses a date range control to limit the timeframe.

### Default date range filter

The default date range filter lets you set a timeframe for an individual chart.

Default date range filter options include the following:

  * **Auto** : Uses the default date range, which is determined by the chart's data source.
  * **Custom** : Lets you use the calendar widget to select a custom date range for the chart.



[Learn more about working with dates and time](https://docs.cloud.google.com/data-studio/dates-and-times).

### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

## Style the chart

The options in the **Style** tab control the overall presentation and appearance of the chart.

**Note:** You may not see all these settings if you're using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

### Chart title

Turn on the **Show title** switch to add a title to your chart. Data Studio can automatically generate a title, or you can create a custom title for the chart. You can also customize the title's styling and placement.

#### Autogenerate

This option is enabled by default. When **Autogenerate** is enabled, Data Studio generates a title that is based on the chart type and the fields that are used in the chart. The autogenerated title will be updated if you change the chart type or make changes to the fields that are used in the chart.

To add a custom title to your chart, enter it into the **Title** field. This will turn off the **Autogenerate** setting.

#### Title options

When the **Show title** setting is enabled, you can use the following title options:

  * **Title:** Provides a text field where report editors can enter a custom title for the chart.
  * **Font family:** Sets the font type for the title text.
  * **Font size:** Sets the font size for the title text.
  * **Font color:** Sets the font color for the title text.
  * **Font styling options:** Applies bold, italic, or underline styling to the title text.
  * **Top:** Positions the chart title at the top of the chart.
  * **Bottom:** Positions the chart title at the bottom of the chart.
  * **Left:** Aligns the chart title to the left side of the chart.
  * **Center:** Centers the chart title horizontally.
  * **Right:** Aligns the chart title to the right side of the chart.



### Treemap

**Note:** You may not see all these settings if you're using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

These options control the appearance of the treemap:

  * **Show branch header** : Shows or hides the parent branches.
  * **Branch header color** : Sets the color of the branch header. This setting appears when **Show branch header** is enabled.
  * **Show scale** : When enabled, displays the value scale for branch color colors. This setting appears when **Gradient** is the selected **Color by** option.
  * **Border radius** : Sets the border radius of the branches. The higher the value, the more rounded the edges of the branches will appear.



### Color By

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

These options control how your data is colored:

  * **Single color** : When this option is selected, the data series is displayed in shades of a single color. Otherwise, the chart is displayed in multiple colors, according to your [report theme](https://docs.cloud.google.com/data-studio/how-to-color-your-reports). You can set a specific color in the **Branch color** menu.
  * **Gradient:** This option colors each branch in multiple shades of the **Max color value** setting, with the option to display the coordinating value scale. Additionally, you can customize the colors that are set for **Mid color value** and **Min color value**. The **Gradient** option appears only when **Metric** is selected in the **Fields** setting of the **Setup** tab.
  * **Dimension values** : This option colors each dimension value in the chart with the color that is specified in the **Manage dimension value** color map. The **Dimension values** setting ensures that your data uses color consistently, regardless of the position of that data in the chart. This option appears only when **Dimension** is selected in the **Fields** setting of the **Setup** tab. 
    * **Enable multi-tone** : When this setting is enabled, branches are displayed in varying shades of the colors that are set in the **Manage dimension value colors** map, according to the branch dimension value. This option appears when **Dimension values** is selected.
  * **"Others" color** : This option lets you set a color for the **Others** series when the **Group the rest as "Others"** setting is enabled.



### Label

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

These options set the font style, font size, font color, and value format for the text in the chart:

  * **Font family** : Sets the font type of the legend font.
  * **Font size** : Sets the size of the legend font.
  * **Font color** : Sets the color of the legend font.
  * **Show data labels as** : Sets the data that is displayed in the branch labels. The options that are selectable depend on the type of field, if any, that is set for the **Secondary label** setting in the **Setup** tab. The data label options include the following: 
    * **None** : Displays branches with no data labels.
    * **Dimension only** : Displays the dimension values in each branch.
    * **Dimension and metric (value)** : Displays the dimension and metric values in each branch.
    * **Dimension and metric (percent)** : Displays the dimension value and the percentage of the metric value against the total of the metric values in the chart.



### Legend

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

These options determine the placement and appearance of the chart legend:

  * **Display legend:** When enabled, displays the chart legend.
  * **Position:** Sets the position of the legend.
  * **Alignment:** Sets the alignment of the legend relative to the selected position.
  * **Align legend with grid:** Sets the alignment of the legend with the position of the grid, instead of aligning with the title.

**Note:** This setting does _not_ appear if **Display legend** is off, if the legend **Position** is set to **Right** , or when there is no chart title.
  * **Max lines:** Sets the number of lines that are used by the legend. If the number of series requires more lines, overflow items can be displayed by clicking the** < **and** > **arrows.

**Note:** This setting only applies when the **Position** is set to **Top**. This setting has no effect if the **Position** is set to **Right** or **Bottom**.
  * **Font family:** Sets the font type of the legend font.

  * **Font size:** Sets the size of the legend font.

  * **Font color:** Sets the color of the legend font.




### Background and border

These options control the appearance of the chart background container:

  * **Background:** Sets the chart background color.
  * **Opacity:** Sets the chart opacity. 100% opacity completely hides objects behind the chart. 0% opacity makes the chart invisible.
  * **Border color:** Sets the chart border color.
  * **Border radius:** Adds rounded borders to the chart background. When the radius is 0, the background shape has 90° corners. A border radius of 100° produces a circular shape.
  * **Border weight:** Sets the chart border line thickness.
  * **Border style:** Sets the chart border line style.
  * **Add border shadow:** Adds a shadow to the chart's lower and right borders.



### Chart header

The chart header lets viewers perform various actions on the chart, such as exporting the data, drilling up or down, or sorting the chart. Chart header options include the following:

  * **Chart header:** Controls where the chart header appears on the chart. The **Chart header** options include the following: 
    * **Do not show:** The header options never appear. Note that report viewers can always access the options by right-clicking the chart.
    * **Always show:** The header options always appear.
    * **Show on hover (default):** Three vertical dots appear when you hold the pointer over the chart header. Click these to access the header options.
  * **Header font color:** Sets the color of the chart header options.



### Reset to report theme

Click **Reset to report theme** to reset the chart settings to the report theme settings.

## Related resources

  * [Types of charts in Data Studio](https://docs.cloud.google.com/data-studio/types-of-charts)
  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [About filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
