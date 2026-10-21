---
url: https://docs.cloud.google.com/data-studio/add-reference-lines-and-reference-bands-to-charts/
title: Add reference lines and reference bands to charts \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:17:07.711682+00:00
---

# Add reference lines and reference bands to charts  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-reference-lines-and-reference-bands-to-charts/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Add reference lines and reference bands to charts Stay organized with collections  Save and categorize content based on your preferences. 

Reference lines and reference bands display how the data in a chart compares against a preset value. For example, you can use reference lines to visualize how daily sales compare to a target sales figure, or to compare the average sale data for individual stores against a regional sales average.

## Reference lines and reference bands in Data Studio

There are two types of reference lines that can be added to charts:

  * **Reference line** : A reference line is helpful for highlighting a single value to compare data against.

You can also choose to highlight a date along the X-axis in the **Axis** section of the **Style** tab.

  * **Reference band** : A reference band is another type of reference line that is helpful for comparing data against a range of values. For example, you can highlight whether data is in a favorable or unfavorable range with a reference band.

You can also choose to highlight date ranges along the X-axis in the **Axis** section of the **Style** tab.




### Reference line and reference band examples

You can use a reference line to highlight a single value, such as a sales goal, to compare data against. For example, you can use a reference line to highlight a **Weekly sales target** in a time series chart that displays **Sales** by **Date**.

![A Weekly sales vs. target time series chart displays a Weekly sales target horizontal reference line.](https://docs.cloud.google.com/static/data-studio/images/ref-line-example-1-2020-06-16.png)

You can use a reference band to highlight a set range against which to compare data. For example, you can highlight a **Mobile subscription sales goal range** in a time series chart that displays **Mobile Subscriptions** by **Year**.

![A time series chart displays mobile subscriptions by year with a reference band that highlights the Mobile subscription sales goal range of 3 billion to 5 billion.](https://docs.cloud.google.com/static/data-studio/images/reference-band-examples.png)

## Reference lines versus trend lines

Reference lines let you show target values and set thresholds and benchmarks so tht you can see how your data matches expectations or goals.

Trend lines reveal the overall direction of the data in a chart. Trend lines can help you see patterns and make predictions from data that would otherwise appear random. In Data Studio, you can add trend lines to [time series](https://docs.cloud.google.com/data-studio/time-series-reference) and [scatter charts](https://docs.cloud.google.com/data-studio/scatter-chart-reference).

## Add a reference line or reference band

You can add reference lines to time series, line and combo charts, bar and column charts, area charts, and scatter charts.

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a chart. You can add reference lines to Cartesian chart types (for example, a line chart, a bar chart, or an area chart).
  3. In the right-hand **Properties** panel, select the **Style** tab.
  4. Click **Add a reference line** or **Add a reference band**.
  5. Configure the reference line or reference band using the options that are outlined in the Reference line style options and Reference band style options sections on this page.



Reference lines and reference bands appear with either a default label or with a custom label that you apply.

You can hover your cursor over a reference line or reference band to access a tooltip that displays more details about the reference values.

## Reference line style options

Configure a reference line using the following options on the **Style** tab of the right-hand **Properties** panel.

### Type

Determines the value upon which the reference line is based.

#### Constant value

Base the reference line on a value that you type in. For example, if your sales target is $10,000 per day, enter 10000. For a percentage value, enter the number as a decimal (.5 equals 50%).

#### Metric

Base the reference line on a metric that appears in the chart.

#### Parameter

Base the reference line on a parameter that you select. Only single-valued numeric parameters are allowed.

#### Calculation

For metric-based reference lines, choose the aggregation to apply to the selected metric. For example, if the chart is visualizing **Users** by **Week** , you can create a reference line showing the average number of weekly users by choosing the **Users** metric and **Average** calculation.

Available calculations:

  * Average
  * Median
  * Percentile - Enter the percentile as a whole number between 0 and 100.
  * Min
  * Max
  * Total



### Axis

Display the reference line on the chart's X, Y, Left-Y, or Right-Y axis. This option applies to constant value and parameter-based reference lines. The available axes depend on the chart type.

If you select x-axis and your x-axis is a date dimension, a date selector will appear that lets you specify a date to highlight as a reference on the chart.

### Label

Display a custom label for the reference line.

If you leave the **Label** field blank, Data Studio supplies a default label. For constant value reference lines, the label is **Reference Line #n**. For metric reference lines, the default label is the type of calculation that is applied. For parameter reference lines, the default label is the parameter name.

Click the **Show label** checkbox to display the label on the chart by default. Clear the **Show label** checkbox to hide the label from the chart.

#### Show reference value in label

When you click the **Show label** checkbox, the option to **Show reference value in label** also becomes available.

Click the **Show reference value in label** checkbox to display the reference line value. The value will be appended to the label.

### Line weight

Select a number from the **Line weight** drop-down menu to change the thickness of the reference line. The higher the number that you select, the thicker the line will appear.

### Line style

Select an option from the **Line style** drop-down to change the appearance of the reference line. Using different line styles can be helpful in distinguishing between multiple lines that appear in a chart.

Line style options include the following:

  * Dashed
  * Dotted
  * Solid
  * Dash-dot
  * Long dash
  * Long dash-dot



### Line color

Use the **Line color** color selector to change the color of the reference line.

## Reference band style options

Configure a reference band using the following options on the **Style** tab of the right-hand **Properties Panel**.

### Beginning value

These settings determine the starting value of the reference band range.

#### Type

Select the type of value to begin the reference band range.

> You can have different **Type** options selected for the **Beginning** **value** and the **Ending value**. For example, you can use an **Average** calculation for the starting value, and a **Metric** value for the ending value, depending on which value is greater.

#### Constant value

Base the reference band beginning value on a number that you type in. For example, if your sales target is $10,000 per day, enter 10000. For a percentage value, enter the number as a decimal (.5 equals 50%).

#### Metric

Base the beginning value of the reference band on a metric that appears in the chart.

#### Parameter

Base the beginning value of the reference band on a parameter that you select. Only single-valued numeric parameters are allowed.

#### Calculation

For metric-based beginning values, choose the aggregation to apply to the selected metric.

The available calculations are as follows:

  * Average
  * Median
  * Percentile - Enter the percentile as a whole number between 0 and 100.
  * Min
  * Max
  * Total



### Label

Display a custom label for the reference band.

If you leave the **Label** field blank, Data Studio supplies a default label. For constant value reference bands, the label displays the range of the band. For metric reference bands, the default label is the type of calculation that is applied. For parameter reference bands, the default label is the parameter name.

Click the **Show label** checkbox to display the label on the chart by default. Clear the **Show label** checkbox to hide the label from the chart.

#### Show reference value in label

When you click the **Show label** checkbox, the option to **Show reference value in label** also becomes available.

Click the **Show reference value in label** checkbox to display the reference band value.

The value will be appended to the label and will be display the band range as the **lowest value to highest value**. For example, for a reference band with a low value of 3,000 and a high value of 5,000, the value will be displayed as **3,000 to 5,000**.

Line weight

Select a number from the **Line weight** drop-down menu to change the thickness of the reference band lines. The higher the number that you select, the thicker the line will appear.

### Line style

Select an option from the **Line style** drop-down to change the appearance of the reference band lines. Using different line styles in distinguishing the line from other lines that appear in a chart.

Line style options include the following:

  * Dashed
  * Dotted
  * Solid
  * Dash-dot
  * Long dash
  * Long dash-dot



### Background color

Use the **Background color** selector to select a fill color for the area between the **Beginning value** and the **Ending value** range.

### Line color

Use the **Line color** color selector to change the color of the reference band lines.

### Opacity

Select a value from the **Opacity** drop-down menu to change the opacity of the fill color. The higher the percentage that you select, the less opaque the fill color will appear.

### Ending value

These settings determine the starting value of the reference band range.

#### Type

Select the type of value to end the reference band range.

> You can have different **Type** options selected for the **Beginning** **value** and the **Ending value**. For example, you can use an **Average** calculation for the starting value, and a **Metric** value for the ending value, depending on which value is greater.

#### Constant value

Base the reference band ending value on a number that you type in. For example, if your sales target is $10,000 per day, enter **10000.** For a percentage value, enter the number as a decimal (.5 equals 50%).

#### Metric

Base the ending value of the reference band on a metric that appears in the chart.

#### Parameter

Base the ending value of the reference band on a parameter that you select. Only single-valued numeric parameters are allowed.

#### Calculation

For metric-based ending values, choose the aggregation to apply to the selected metric.

The available calculations are as follows:

  * Average
  * Median
  * Percentile - Enter the percentile as a whole number between 0 and 100.
  * Min
  * Max
  * Total



### Axis

Display the reference band on the chart's X, Y, Left-Y, or Right-Y axis. This option applies to constant value and parameter-based reference bands. The available axes depend on the chart type.

If you select x-axis and your x-axis is a date dimension, a date selector will appear in the **Beginning value** and **Ending value** sections that lets you specify a date range to highlight on the chart.

## Remove a reference line or reference band

To remove a reference line from a chart:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select the chart.
  3. In the right-hand **Properties** panel, select the **Style** tab.
  4. Locate the reference line or reference band that you want to remove, then click the ![](https://docs.cloud.google.com/static/data-studio/images/highlightoffgrey6001x48dp-2020-06-10.png)**Delete reference line** or ![](https://docs.cloud.google.com/static/data-studio/images/highlightoffgrey6001x48dp-2020-06-10.png)**Delete reference band** icon.



## Edit charts with reference lines or reference bands

If you change the chart type, Data Studio deletes any reference lines or reference bands that are not supported by the new chart type.

If you remove a metric from the chart, Data Studio deletes any reference lines or reference bands that are associated with that metric.

## Limits of reference lines

The following limitations apply while using reference lines in Data Studio:

  * Reference lines and reference bands are supported only for the following chart types: 
    * time series
    * column/bar
    * line/combo
    * area
    * scatter
  * Stacked column/bar charts support only constant-value reference lines.
  * Reference lines and reference bands are not supported on 100% stacked column/bar charts.
  * You can add up to 10 reference lines per supported chart.
  * Reference lines are only available for numeric axes. Reference lines on date axes aren't supported.
  * Metric-based reference lines can only consider values currently displayed in the chart. For example, if you add a reference line to a bar chart with 10 bars, data from any additional bars aren't included in the calculation.
  * Stacked column, stacked bar, and stacked area charts only support constant value and parameter reference lines.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
