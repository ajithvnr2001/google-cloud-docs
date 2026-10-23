---
url: https://docs.cloud.google.com/data-studio/color-your-data/
title: Color your data \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:57.209429+00:00
---

# Color your data  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/color-your-data/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Color your data Stay organized with collections  Save and categorize content based on your preferences. 

You can customize chart colors in Data Studio to distinguish categories and highlight key data trends. Applying consistent coloring techniques helps viewers interpret complex visual data quickly and navigate multi-page reports with clarity. You can select single colors, color by dimension values, or color by series order in the **Color by** section of the **STYLE** tab.

To apply a color option, follow these steps:

  1. Select a chart and then on the right, open the **STYLE** tab.
  2. Select an option in the **Color by** section.



![The Color By section for a bar chart displays the color options Single Color, Bar order, and Dimension values.](https://docs.cloud.google.com/static/data-studio/images/color-by-options-2019-10-25.png)

## Color by dimension values

Coloring by dimension values applies consistent colors to the data series in your charts by mapping specific colors to specific dimension values.

The default dimension value colors are based on the current report theme, however can choose different colors by [editing the dimension value color map](https://docs.cloud.google.com/data-studio/the-dimension-value-color-map).

### Example

In the following charts, the colors used for each dimension stay constant, even if their position in the chart changes: France is always blue, Germany is always red, and India is always green.

![Two pie charts, one labeled Yesterday and the other labeled Today, display values in assigned colors: Values for Germany are in red, India in green, and France in dark blue.](https://docs.cloud.google.com/static/data-studio/images/coord-colors-compare-4-2017-09-21.png)Example of coloring by dimension value.

## Color by series order

The series order option colors the data according to its order in the chart. This option emphasizes the ranking of the data over the identity of the data. For example, suppose you want the highest valued dimension to always appear in green. Using the color by series order option, you can assign that color to the first color swatch in the current theme.

### Example

These charts use the color by series order (called _slice order_ in the Pie Chart properties panel) option. Here, dark blue represents the highest valued dimension, rather than a specific country.

![Two pie charts, one labeled Yesterday and the other labeled Today, display the highest value in dark blue: The Yesterday highest value is France, and the Today highest value is Germany.](https://docs.cloud.google.com/static/data-studio/images/coord-colors-compare-3-2017-09-21.png)Example of coloring by series order.

## Set series colors

To change the colors assigned to data series in a specific chart:

  1. Select that chart, then on the right, open the **STYLE** tab.
  2. In the **Color by** section, select **Series order, Bar order,** or **Slice order** , depending on the type of chart.
  3. Click a color box to set the color for each series. The color boxes appear in rank order: the first color box corresponds to the first series, the second box to the second series, and so on.



![A user assigns colors to bars in a bar chart with the Bar order option selected in the Color By section of the Style tab.](https://docs.cloud.google.com/static/data-studio/images/color-swatch-2019-10-25.png)

## Single color

Bar charts and pie charts have a single color option that displays the data in shades of the selected color, as shown in the following example.

![A pie chart with a donut center displays data slices in shades of gray.](https://docs.cloud.google.com/static/data-studio/images/single-color-2017-09-21.png)Example of coloring with a single color.

## Color metrics

Metrics get their default colors from the current report theme. You can customize metric colors in selected charts by editing the **STYLE** properties for those charts.

Learn how to [create custom colors](https://docs.cloud.google.com/data-studio/how-to-color-your-reports).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
