---
url: https://docs.cloud.google.com/data-studio/pie-chart-reference/
title: Pie chart reference \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:00.205613+00:00
---

# Pie chart reference  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/pie-chart-reference/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Pie chart reference Stay organized with collections  Save and categorize content based on your preferences. 

Pie charts display your data in a circular visualization, with sections (slices of the pie) representing your data series. The sizes of the slices are proportional to the quantity or relative value of the metric you are plotting. In general, pie charts are most useful when comparing a few data points with relatively large differences in proportion between the values. Pie charts that display large numbers of series with minor variations in the data can be confusing to viewers of the chart.

## Pie charts in Data Studio

Pie charts in Data Studio visualize the relative values for a single dimension and metric combination. The dimension determines the number and names of the slices, while the metric determines the proportion of each slice. Pie charts in Data Studio support as few as 1 slice to as many as 10 slices. Data Studio automatically aggregates any superfluous data points into a slice labeled **Others**. The pie can be solid, or it can be donut (ring) shaped.

## Pie chart examples

The following pie charts visualize the same data: the percentage of the **Pageviews** metric by **Source** dimension. Each colored pie slice represents a traffic source, identified in the legend at the right of the chart. The slice colors are assigned according to the metric value. For example: the highest is blue; the second highest is red. (You can change these colors in the **Style** tab in the **Properties** panel.) The percentage of **Pageviews** for each traffic **Source** appears as text labels on the larger slices. (You can see the percentages for the smaller slices by hovering your cursor over them.)

The first chart is configured to show 10 slices. The second chart shows just 2 slices, and is also using the donut style option. In the first chart, Data Studio uses the tenth slice to aggregate any remaining traffic sources into the **Others** category. The second chart compares the largest traffic source ("google" in this case) to all the other sources combined.

![Two pie charts: The first displays Pageviews by Source with each source represented as a slice, and the second displays Pageviews by Source grouped in two slices - google and others.](https://docs.cloud.google.com/static/data-studio/images/pie-chart-reference-example-1-2016-10-24.png)

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

Pie charts can have one dimension.

#### Drill down

This option appears on charts that support it.

Drilling down gives viewers a way to reveal additional levels of detail within a chart. When you turn on the **Drill down** switch, each dimension that you add becomes another level of detail that you can drill into. [Learn more about chart drill down](https://docs.cloud.google.com/data-studio/add-drill-actions-to-charts).

### Metric

Metrics measure the things that are contained in dimensions and provide the numeric scale and data series for the chart.

Metrics are aggregations that come from the underlying dataset or that are the result of implicitly or explicitly applying an aggregation function, such as `COUNT()`, `SUM()`, or `AVG()`. The metric itself has no defined set of values, so you can't group by a metric as you can with a [dimension](https://docs.cloud.google.com/data-studio/dimension).

[Learn more about aggregation](https://docs.cloud.google.com/data-studio/aggregation).

Pie charts can have one metric.

#### Optional metrics

You can add [optional metrics](https://docs.cloud.google.com/data-studio/optional-metrics) by turning on the **Optional metrics** switch and selecting metrics from the **Add metric** field selector. You can also click metrics from the fields list on the **Data** panel and place them in the **Optional metrics** selector.

#### Metric sliders

Turn on the **Metric sliders** switch to add a [metric slider](https://docs.cloud.google.com/data-studio/metric-slider) to your chart.

### Display

The **Display** settings determine the number of slices that are displayed on the chart. You can choose to display the slices from the **Top N** of query results or **Bottom N** of query results. You can click the icon next to this value to increase to the max number of results supported by the visualization.

**Note:** **Top N** is set by default.

When either **Top N** or **Bottom N** is selected, you can specify the number of slices to display in the **Number of slices** setting.

#### Group the rest as "Others"

The **Group the rest as "Others"** setting aggregates the results that are outside of the specified **Slices to display** limit into one slice that will have the label **Others**. When enabled, this setting lets you compare the individual slices against the context of the remaining results.

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

  * **Auto:** Uses the default date range, which is determined by the chart's data source.
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart.



[Learn more about working with dates and time](https://docs.cloud.google.com/data-studio/dates-and-times).

### Sort

The **Sort** option in the chart's setup panel controls the default sorting behavior. You can select any metric in the chart's data source, or any dimension that is displayed in the chart, to use as the primary sorting field.

**Note:** When you specify a metric as a sort field, you can [edit the field's aggregation](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports). For example, you could include a numeric field in the chart as a `SUM`, but sort on that same field's `AVERAGE` value.

### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

The **Change sorting** option lets report viewers change how a chart is sorted.

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



### Pie chart

This section controls the overall appearance and layout of your chart.

**Note:** You may not see all these settings if you're using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

#### Slice padding

Determines the size of the spacing in between the slices of the chart. Slide the control from the left to the right to increase the size of the space in between the slices. Decrease the size of the spaces in between the slices by sliding the control from the right to the left.

**Note:** The padding thickness that can be applied may be limited by the size of the smallest slice in the pie chart.

#### Inner radius

Determines the size of the hole in the center of the chart. Slide the control from the left to the right to increase the size of the hole. Decrease the size of the hole by sliding the control from the right to the left.

#### Border radius

Determines the curve radius of the pie slices. Setting the **Border radius** to 100 creates a petal shape.

### Color by

These options control how your data is colored:

  * **Single color:** When this option is selected, the data series is displayed in shades of a single color. Otherwise, the chart is displayed in multiple colors, according to your [report theme](https://docs.cloud.google.com/data-studio/how-to-color-your-reports). You can set specific colors by using the color picker.
  * **Slice order:** Use the current theme to color the data according to its position in the chart. This option emphasizes the ranking of the data over the identity of the data. You can set specific colors by using the color picker.
  * **Dimension values:** This option colors each dimension value in the chart with the color that is specified in the **Manage dimension values** color map. This option ensures that your data uses color consistently, regardless of the position of that data in the chart.
  * **"Others" color** : This option lets you set a color for the **Others** series when the **Group the rest as "Others"** setting is enabled.



Learn more about [coloring your data](https://docs.cloud.google.com/data-studio/how-to-color-your-reports).

### Label

These options control the appearance of the data labels:

  * **Pie slice font color:** Sets the color of the data labels inside the pie slices.
  * **Font size:** Sets the size of the data labels inside the pie slices.
  * **Pie slice font:** Sets the font family of the data labels inside the pie slices.
  * **Slice label:** Determines the style of the slice labels. The options include the following: 
    * **None:** No label appears.
    * **Percentage (default):** Displays the percentage value of each slice.
    * **Label:** Displays the dimension value. (You may need to increase the chart size to accommodate longer values.)
    * **Value:** Displays the metric value.
  * **Text contrast:** Sets the font color automatically to provide better readability of your data labels. Choose from four levels of contrast: none, low, medium, or high.



### Legend

**Note:** You may not see all these settings if you're using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

These options determine the placement and appearance of the chart legend:

  * **Display legend:** When enabled, displays the chart legend.
  * **Position:** Sets the position of the legend.
  * **Alignment:** Sets the alignment of the legend relative to the selected position.
  * **Max lines:** Sets the number of lines that are used by the legend. If the number of series requires more lines, overflow items can be displayed by clicking the** < **and** > **arrows.

**Note:** This setting applies only when the **Position** is set to **Top**. This setting has no effect if the **Position** is set to **Right** or **Bottom**.
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
  * [Work with dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [About filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
