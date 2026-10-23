---
url: https://docs.cloud.google.com/data-studio/bar-chart-and-column-chart-reference/
title: Bar chart and column chart reference \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:49.204620+00:00
---

# Bar chart and column chart reference  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/bar-chart-and-column-chart-reference/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Bar chart and column chart reference Stay organized with collections  Save and categorize content based on your preferences. 

Use bar charts to compare different categories of information. The categories are represented by the bars, and the length of each bar (or height of each column) represents the value of that category. The longer the bar, the greater the value it represents.

## Bar charts in Data Studio

Bar charts let you visualize your data in two ways:

  * One single dimension with multiple metrics. This method lets you analyze a single category of information using up to 20 metrics.
  * Two dimensions with a single metric. This method lets you apply a breakdown dimension to the primary dimension and measure that breakdown with a single metric.



### Other types of bar charts

You can select from the following preset chart types when you add a chart from the toolbar.

#### Stacked bar chart

Stack the breakdown dimensions horizontally instead of showing them side-by-side.

![](https://docs.cloud.google.com/static/data-studio/images/stacked-bar-chart-reference-splash-image-2023-06-13.png)

#### 100% stacked bar chart

Stack the breakdown dimensions horizontally, with each series in the chart having the same overall length.

![](https://docs.cloud.google.com/static/data-studio/images/100-stacked-column-bar-reference-splash-image-2023-06-13.png)

#### Column chart

Display the data using vertical columns, with breakdown dimensions shown side-by-side.

![](https://docs.cloud.google.com/static/data-studio/images/column-chart-reference-splash-image-2023-06-13.png)

#### Stacked column chart

Stack the breakdown dimensions vertically instead of showing them side-by-side.

![](https://docs.cloud.google.com/static/data-studio/images/stacked-column-chart-reference-splash-image-2023-06-13.png)

#### 100% stacked column chart

Stack the breakdown dimensions vertically, with each series in the chart having the same overall height.

![](https://docs.cloud.google.com/static/data-studio/images/100-stacked-column-chart-reference-splash-image-2023-06-13.png)

**Tip:** Use a stacked bar or stacked column chart to show part-to-whole relationships. 100% stacked bars or columns are useful to show the relationship between individual items and the whole in a single bar, where the cumulative total isn't important.

### Column chart example

The following column charts show Google Analytics web traffic data. The base dimension for both charts is **Medium**. The left hand chart uses stacked columns to show several metrics (**Sessions** , **Users** , and **Exits**) for medium. The right hand chart uses a second dimension, **Country ISO Code** , to break down each medium according to its country of origin. Instead of stacked columns, this chart use grouped columns: Each column is a data series that corresponds to one of the countries. Two-dimensional charts can only plot a single metric (**Sessions** again in this example).

![Two column charts: One displays stacked columns, and the other displays grouped columns.](https://docs.cloud.google.com/static/data-studio/images/bar-chart-reference-example-2016-09-26.png)

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

At least one dimension is required. The first dimension you specify serves as the primary data series in the chart.

#### Drill down

This option appears on charts that support it.

Drilling down gives viewers a way to reveal additional levels of detail within a chart. When you turn on the **Drill down** switch, each dimension that you add becomes another level of detail that you can drill into. [Learn more about chart drill down](https://docs.cloud.google.com/data-studio/add-drill-actions-to-charts).

#### Breakdown dimension

This option displays the metric data broken down according to the selected dimension. For example, a chart that shows annual sales data could be broken down by a **Sales Region** dimension to show sales by region or by an **Employee ID** dimension to show sales by sales associate.

**Note:** If you specify a breakdown dimension, the chart is limited to a single metric.

### Metric

Metrics measure the things that are contained in dimensions and provide the numeric scale and data series for the chart.

Metrics are aggregations that come from the underlying dataset or that are the result of implicitly or explicitly applying an aggregation function, such as `COUNT()`, `SUM()`, or `AVG()`. The metric itself has no defined set of values, so you can't group by a metric as you can with a [dimension](https://docs.cloud.google.com/data-studio/dimension).

[Learn more about aggregation](https://docs.cloud.google.com/data-studio/aggregation).

At least one metric is required. For charts with a single dimension, you can have up to 20 metrics. For charts with two dimensions, you can have only one metric.

#### Optional metrics

You can add [optional metrics](https://docs.cloud.google.com/data-studio/optional-metrics) by turning on the **Optional metrics** switch and selecting metrics from the **Add metric** field selector. You can also click metrics from the fields list on the **Data** panel and place them in the **Optional metrics** selector.

#### Metric sliders

Turn on the **Metric sliders** switch to add a [metric slider](https://docs.cloud.google.com/data-studio/metric-slider) to your chart.

### Display

The **Display** settings determine the number of dimension series or breakdown dimension series that are displayed on the chart. If you have set a value for **Breakdown dimension**, there will be a **Display** section labeled **Dimension** for dimension series display settings, and a **Display** section labeled **Breakdown dimension** for breakdown dimension series display settings.

You can choose to display the series from the **Top N** of query results or **Bottom N** of query results. You can click the icon next to this value to increase to the max number of results supported by the visualization.

**Note:** **Top N** is set by default.

When either **Top N** or **Bottom N** is selected, you can specify the number of bars to display in the **Number of bars** setting.

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



[Learn more about working with dates and time](https://docs.cloud.google.com/data-studio/dates-and-times).

### Sort

The **Sort** and **Secondary sort** settings in the chart's setup panel control the default sorting behavior. You can select any metric in the chart's data source, or any dimension that is displayed in the chart, to use as the primary or secondary sorting field.

**Note:** The **Secondary sort** settings only appear when a breakdown dimension is set.

When you specify a metric as a sort field, you can [edit the field's aggregation](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports). For example, you can include a numeric field in the chart as a `SUM`, but sort on that same field's `AVERAGE` value.

### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

The **Change sorting** option lets report viewers change how a chart is sorted.

The **Zoom** option lets you zoom into a chart and pan on that chart to view all the data that is present. [Learn more about zooming and panning on Cartesian charts](https://docs.cloud.google.com/data-studio/zoom-and-pan-on-charts).

**Important:** The **Zoom** option is not available when the **Cross-filtering** option is enabled.

## Style the chart

The options in the **Style** tab control the overall presentation and appearance of the chart.

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

### Chart title

Turn on the **Show title** switch to add a title to your chart. Data Studio can automatically generate a title, or you can create a custom title for the chart. You can also customize the title's styling and placement.

### Conditional formatting

Click **Add conditional formatting** to apply conditional formatting rules to the chart. [Learn more about conditional formatting in Data Studio charts](https://docs.cloud.google.com/data-studio/use-conditional-formatting-rules-in-looker-studio).

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



### Bar chart

This section controls the overall appearance and layout of your chart. These options apply to both bar and column charts:

  * ![](https://docs.cloud.google.com/static/data-studio/images/vertical-table.png)**Vertical:** Displays the data series as vertical columns.
  * ![](https://docs.cloud.google.com/static/data-studio/images/horizontal-table.png)**Horizontal:** Displays the data series as horizontal bars.

  * **Bar width** : For unstacked bar charts with multiple bars, use the slider to specify a custom width for each individual bar, and use the **Group bar with** slider to specify a custom bar width for each group of bars.

  * **Group bar width:** For stacked bar charts, use the **Group bar width** slider to specify a custom bar width between 0% and 100%.

  * **Stacked bars:** When this option is selected, the chart displays stacked bars or columns. Otherwise, the chart displays grouped bars or columns. This option is available only when you have set a value for **Breakdown dimension**.

  * **100% stacking** : When this option is selected, stacked charts show the contribution of each data series to 100% of the total value. This option is available only when the **Stacked Bars** setting is enabled, and when you have set more than one metric for the chart.

  * **Show total card:** Shows the total value of the metrics for a selected stacked bar. Position your cursor over the bar to display the card. This option is available only when the **Stacked Bars** setting is enabled, and when you have set more than one metric for the chart.

  * **Show data labels:** When this option is selected, the value is displayed for each series in the chart. Selecting this option also reveals the **Data label** section, where you can control the presentation of the labels on the chart.




#### Data label

This section controls the presentation of data labels for bars. Turn on the **Show data labels** switch to see these options:

  * **Bar label type:** This option is available only for stacked bar charts and 100% stacked bar charts. The **Bar label type** drop-down menu includes the following options:

    * **Metric value (default):** Shows a metric value for each segment of the bar.
    * **Stacked:** Shows the total stack value for each bar, along with the running sum from the values for each segment of the bar.
    * **Total:** Shows only the total stack value for all the segments of the bar. The **Total** option is available only for the stacked bar chart type.
  * **Show data labels as:** Sets whether labels are displayed as numbers or percentages. This option is available only for 100% stacked bar charts.

  * **Compact numbers:** Rounds numbers and displays the unit indicator. For example, 553,939 becomes 553.9K.

**Note:** This option is available only if **Show data labels as** is set to **Number** for 100% stacked bar charts.
  * **Decimal precision:** Sets the number of decimal places that are displayed in metric values. This option is available only if **Show data labels as** is set to **Number**. If **Show data labels as** is set to **Percentage** , then the decimal precision will always be 2.

  * **Font family:** Sets the font type of the label text.

  * **Font size:** Sets the font size for the label text.

  * **Font color:** Sets the font color for the label text. This option is available only when the **Bar label position** option is set to **Left** (for bar charts) or to **Below** (for column charts).

  * **Font styling options:** Applies bold or italic styling to the label text.

  * **Bar label position:** Sets the position of labels relative to the bar or column. For stacked charts, you can select **Center** to place the label in the center of the bar segment. If there is not enough space to fit the label in the center, it is moved outside the bar.

  * **Background color:** Sets a background color for the label text.

  * **Labels opacity:** For labels with a custom background color, this setting adjusts the opacity of the background for the label text. 100% opacity makes the background solid, and 0% opacity makes the background fully transparent.

  * **Labels border radius:** For labels with a custom background color, this setting adds rounded borders to the chart background. Choose a value from 0px (90° corners) to 20px (maximum rounding).




### Color by

This section controls how your data is colored. Learn more about [coloring your data](https://docs.cloud.google.com/data-studio/how-to-color-your-reports).

  * **Single color:** When this option is selected, the data series is displayed in shades of a single color. Otherwise, the chart is displayed in multiple colors, according to your [report theme](https://docs.cloud.google.com/data-studio/how-to-color-your-reports). You can set a specific color in the **Bar color** menu.

**Note:** If you don't have a value set for **Breakdown dimension**, the **Bar color** setting is used to color the chart, and the other **Color by** options will not appear.
  * **Bar order:** Use the current theme to color the data according to its position in the chart. This option emphasizes the ranking of the data over the identity of the data. You can set specific colors by using the color picker.

  * **Dimension values:** This option colors each dimension value in the chart with the color that is specified in the **Manage dimension values** color map. This option ensures that your data uses color consistently, regardless of the position of that data in the chart.

  * **Bar border color:** This option lets you change the outline color for the bars in the chart. You can also specify a bar border color for all the bar charts in your report from the **Layout** tab of the [**Themes** menu](https://docs.cloud.google.com/data-studio/themes).

  * **"Others" color** : This option lets you set a color for the **Others** series when the **Group the rest as "Others"** setting is enabled.




### Reference lines

Add a reference line or a reference band to your chart by selecting the **Add a reference line** or **Add a reference band** option, respectively.

For more information about reference lines and reference bands, visit the [Add reference lines and reference bands to charts](https://docs.cloud.google.com/data-studio/add-reference-lines-and-reference-bands-to-charts) page. Reference lines are not available for 100% stacked area charts.

Reference lines are not available for 100% stacked bar charts or 100% stacked column charts.

### Zoom

When you enable the **Zoom** option for a chart on the **Setup** tab of the **Properties** panel, you can select one of the following options:

  * **Click and drag to zoom** : Zoom by clicking and dragging to select a portion of the visualization to magnify.
  * **Scroll to zoom** : Zoom by scrolling with your mouse.



Optionally, turn on the **Pan/Zoom X-axis only** switch to let users zoom and pan only along the X-axis.

### Axes

These options control the display of the chart axes titles and scales. A right Y-axis section appears when you have more than one metric in your chart.

**Note:** You may not see all of these settings if you are using a report that has not been upgraded to **Modern charts.** [Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

These options control the display of the chart axes titles and scales:

  * **Show axes:** Shows or hides the chart axes.
  * **Axis color:** Sets the color of the axes.
  * **Axis text color:** Sets the text color for the axis text.
  * **Font family:** Sets the font type for the axis text.
  * **Axis font size:** Sets the font size for the axis text.
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
