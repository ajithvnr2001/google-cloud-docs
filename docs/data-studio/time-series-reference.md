---
url: https://docs.cloud.google.com/data-studio/time-series-reference/
title: Time series reference \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:54.162326+00:00
---

# Time series reference  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/time-series-reference/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Time series reference Stay organized with collections  Save and categorize content based on your preferences. 

A time series chart shows how your data changes over a period of time. For example, you can display the count of website sessions daily over the course of a week, or your company's profit margin quarter by quarter for the last 4 years.

## Time series in Data Studio

A time series chart displays the time dimension as the X-axis (horizontal axis), with the Y-axis (vertical axis) representing the measurement scale. Individual metrics are plotted as a series of data points (also called _markers_) between the two axes. You can have separate left and right Y-axes in a Data Studio time series chart.

You can show up to five metrics in your time series chart. Each series can be shown as a line or a bar in the chart.

## Time series example

The following example chart shows the distribution of website **Users** metric broken down by the **Region** dimension from a Google Analytics data source. The chart is filtered to show US states and has a date range of "Last Month."

![A time series chart compares the number of users in California and New York as two lines during the month of October.](https://docs.cloud.google.com/static/data-studio/images/time-series-example-2-optimized-2016-08-02.png)

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

#### Breakdown Dimension

This option displays the metric data broken down according to the selected dimension. For example, a chart that shows annual sales data could be broken down by a **Sales Region** dimension to show sales by region or by an **Employee ID** dimension to show sales by sales associate.

### Metric

Metrics measure the things that are contained in dimensions and provide the numeric scale and data series for the chart.

Metrics are aggregations that come from the underlying dataset or that are the result of implicitly or explicitly applying an aggregation function, such as `COUNT()`, `SUM()`, or `AVG()`. The metric itself has no defined set of values, so you can't group by a metric as you can with a [dimension](https://docs.cloud.google.com/data-studio/dimension).

[Learn more about aggregation](https://docs.cloud.google.com/data-studio/aggregation).

You can display up to five metrics in a time series.

#### Optional metrics

You can add [optional metrics](https://docs.cloud.google.com/data-studio/optional-metrics) by turning on the **Optional metrics** switch and selecting metrics from the **Add metric** field selector. You can also click metrics from the fields list on the **Data** panel and place them in the **Optional metrics** selector.

#### Metric sliders

Turn on the **Metric sliders** switch to add a [metric slider](https://docs.cloud.google.com/data-studio/metric-slider) to your chart.

### Display

**Note:** The **Display** options are available only when you have set a value for **Breakdown dimension**.

The **Display** settings determine the number of breakdown dimension series that are displayed on the chart. You can choose to display the series from the **Top N** of query results or **Bottom N** of query results. You can click the icon next to this value to increase to the max number of results supported by the visualization.

**Note:** **Top N** is set by default.

When either **Top N** or **Bottom N** is selected, you can specify the number of series to display in the **Number of series** setting.

The series that are displayed are based on the **Breakdown dimension sort** specifications.

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

  * **Auto:** Uses the default date range, which is determined by the chart's data source.
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart.
  * **Comparison date range:** Displays comparison data for the selected time period.



[Learn more about working with dates and time](https://docs.cloud.google.com/data-studio/dates-and-times).

### Breakdown dimension sort

The **Breakdown dimension sort** setting controls the default sorting behavior of the breakdown dimension.

You can select any metric in the chart's data source, or any dimension that is displayed in the chart, to use as the sorting field.

**Important:** The **Breakdown dimension sort** setting is available only when you have set a **Breakdown dimension**. When you specify a metric as a sort field, you can [edit the field's aggregation](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports). For example, you could include a numeric field in the chart as a SUM, but sort on that same field's AVERAGE value.

### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

The **Zoom** option lets you zoom into a chart and pan on that chart to view all the data that is present. [Learn more about zooming and panning on Cartesian charts](https://docs.cloud.google.com/data-studio/zoom-and-pan-on-charts).

**Important:** The **Zoom** option is not available when the **Cross-filtering** option is enabled.

## Style the chart

The options in the **Style** tab control the overall presentation and appearance of the chart.

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts**. [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

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



### Color by

This section controls how your data is colored. Learn more about [coloring your data](https://docs.cloud.google.com/data-studio/how-to-color-your-reports).

These options appear when you have a secondary (breakdown) dimension in your chart:

  * **Series order:** Use the current theme to color the data according to its position in the chart. This option emphasizes the ranking of the data over the identity of the data. You can set specific colors by using the color picker.
  * **Dimension values:** This option colors each dimension value in the chart with the color that is specified in the **Manage dimension color values** color map. This option ensures that your data uses color consistently, regardless of the position of that data in the chart.
  * **"Others" color** : This option lets you set a color for the **Others** series when the **Group the rest as "Others"** setting is enabled.



### Series

Use the **Select series** drop-down menu to select a specific series to customize, or select **All series** to apply changes to all series at once.

Styles set for an individual series will override styles set for **All series**.

Some settings appear at both the individual series and the **All series** level (for example, adding points on line charts). If a setting has different values for different series, then selecting **All series** will indicate that there are multiple values for that setting. The style panel will either display a mixed toggle state, or the word **Mixed** for settings with a text value.

These options control the appearance of each series:

  * **Series type:** Displays the data points for this series in **Line** or **Bars**.
  * **Color:** Sets the color for the series line or bar. This setting appears when you select **Series order** in the **Color by** setting.
  * **Line weight:** Determines the thickness of line series. This option appears when you select **Line**.
  * **Line style:** Determines the style and appearance of the series line. This option appears when you select **Line**.
  * **Gradient:** Highlights the series line with a color gradient shadow. This option appears when you select **Line**.
  * **Cumulative:** When enabled, data for this series is summed over time. Otherwise, the data is shown with no additional aggregation.
  * **Show points:** Displays individual data points on a line series. Viewers can put their cursor over a data point to display its value. This option appears when you select **Line**.
  * **Stepped lines:** Displays a line with a series of steps between data points instead of a smooth line that connects the data points. This option appears when you select **Line**.
  * **Show data labels:** Displays individual values for the data points in the series. Selecting this option also reveals the **Data label** section, where you can control the presentation of the labels on the chart.



#### Data label

If you enable the **Show data labels** setting in the **Series** section, you can configure the following options:

  * **Compact numbers:** Rounds numbers and displays the unit indicator. For example, 553,939 becomes 553.9K.
  * **Decimal precision:** Sets the number of decimal places in metric values.
  * **Font family:** Sets the font type of the label text.
  * **Font color:** Sets the font color for the label text.
  * **Font size:** Sets the font size for the label text.
  * **Font styling options:** Applies bold or italic styling to the label text.
  * **Background color:** Sets a background color for the label text.
  * **Labels opacity:** For labels with a custom background color, this setting adjusts the opacity of the background for the label text. 100% opacity makes the background solid, and 0% opacity makes the background fully transparent.
  * **Labels border radius:** For labels with a custom background color, this setting adds rounded borders to the chart background. Choose a value from 0px (90° corners) to 20px (maximum rounding).



#### Trendline

A trendline is a line that is superimposed on a chart to reveal the overall direction of the data. Data Studio supports several types of trendlines, which are available in the **Trendline** drop-down menu:

  * **Linear:** Displays a straight line that most closely approximates the data in the chart. (To be precise, it's the line that minimizes the sum of squared distances from every point to it.)
  * **Polynomial:** Displays data directionality as a curved line. It can be useful for analyzing large, highly variable data series.
  * **Exponential:** Displays the direction of data that is best represented as an exponential of the form `eax+b`.
  * **Moving average:** Displays a moving average calculation of the chart data. When you select a **Moving average** trendline, you must specify the time period for the calculation.



The **Moving average** trend line type is available only for time series charts.

Trendlines are available only for [time series charts](https://docs.cloud.google.com/data-studio/time-series-reference) and [scatter charts](https://docs.cloud.google.com/data-studio/scatter-chart-reference).

Options for setting the trendline **Weight** , **Style,** and **Color** appear when an option is selected from the **Trendline** drop-down menu.

### Intervals

Click **Add an interval** to add an interval to your time series chart.

For more information about intervals in Data Studio, visit the [Add intervals to charts](https://docs.cloud.google.com/data-studio/add-intervals-to-charts) page.

### Reference lines

Add a reference line or a reference band to your chart by selecting the **Add a reference line** or **Add a reference band** option, respectively.

For more information about reference lines and reference bands, visit the [Add reference lines and reference bands to charts](https://docs.cloud.google.com/data-studio/add-reference-lines-and-reference-bands-to-charts) page. Reference lines are not available for 100% stacked area charts.

### Missing data

This option appears when your time dimension is missing data. You can select one of the following options when Data Studio determines that your time dimension is missing data:

  * **Line To Zero:** When you select this option, a line series will drop to zero for the missing dates. This is the default option.
  * **Line Breaks:** When this option is selected, missing data appears as breaks in the data series.
  * **Linear Interpolation:** When this option is selected, Data Studio will continue the series by connecting the data points on either side of the missing data.



### General

  * **Smooth:** Display series lines as curves. This option appears for line charts, or when at least one series in a combo chart is a **Line**.



### Zoom

When you enable the **Zoom** option for a chart on the **Setup** tab of the **Properties** panel, you can select one of the following options:

  * **Click and drag to zoom** : Zoom by clicking and dragging to select a portion of the visualization to magnify.
  * **Scroll to zoom** : Zoom by scrolling with your mouse.



Optionally, turn on the **Pan/Zoom X-axis only** switch to allow zooming and panning only along the X-axis.

### Axes

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

These options control the display of the chart axes titles and scales:

  * **Show axes:** Shows or hides the chart axes.
  * **Axis color:** Sets the color of the axes.
  * **Axis text color:** Sets the text color for the axis text.
  * **Font family:** Sets the font type for the axis text.
  * **Axis font size:** Sets the font size for the axis text.
  * **Range:** Sets the range for the axis.
  * **Reverse Y-axis direction:** Controls the vertical display of the Y-axis.
  * **Reverse X-axis direction:** Controls the horizontal display of the X-axis.
  * **Align both axes to 0:** Makes both left and right axes start at 0. Available for Cartesian line, bar, and combo charts that have left and right Y-axes.



#### Left Y-Axis

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

These options appear when you enable **Show axes** in the **Axes** section. A **Right Y-Axis** section with the same options appears when you have more than one metric in your chart.

These options control the display of the Y-axis:

  * **Show axis title:** Shows or hides the axis title.
  * **Show axis labels:** Shows or hides the axis labels.
  * **Rotation (0° to 90°):** Sets the rotation of the axis labels for ease of readability. This option appears when you enable **Show axis labels**.
  * **Show axis line:** Shows or hides the axis line.
  * **Axis min:** Sets the minimum value for the axis.
  * **Axis max:** Sets the maximum value for the axis.
  * **Custom tick interval:** Controls the interval between axis ticks.
  * **Log scale:** Makes the axis scale logarithmic.



#### X-Axis

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

These options control the display of the chart's X-axis. These options appear when you enable **Show axes** in the **Axes** section:

  * **Show axis title:** Shows or hides the axis title.
  * **Show axis labels:** Shows or hides the axis labels.
  * **Rotation (0° to 90°):** Sets the rotation of the axis labels for ease of readability. This option appears when you enable **Show axis labels**.
  * **Show axis line:** Shows or hides the axis line.
  * **Custom tick interval:** Controls the interval between axis ticks.



### Grid

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

These options control the look of the chart grid:

  * **Grid background:** Sets the color of the chart background.
  * **Grid border color:** Sets the color of the inner chart border.
  * **Show X-axis grid lines:** Displays the X-axis grid line.
  * **Grid line style:** Sets the line style of the X-axis grid. This option is available only when **Show X-axis grid lines** is enabled.
  * **Grid line color:** Sets the color of the X-axis grid line. This option is available only when **Show X-axis grid lines** is enabled.
  * **Show Y-axis grid lines:** Displays the Y-axis grid line.
  * **Grid line style:** Sets the line style of the Y-axis grid. This option is available only when **Show Y-axis grid lines** is enabled.
  * **Grid line color:** Sets the color of the Y-axis grid line. This option is available only when **Show Y-axis grid lines** is enabled.



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

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
