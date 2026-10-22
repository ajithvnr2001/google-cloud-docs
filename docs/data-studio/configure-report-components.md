---
url: https://docs.cloud.google.com/data-studio/configure-report-components/
title: Configure report components \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:34.415447+00:00
---

# Configure report components  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/configure-report-components/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Configure report components Stay organized with collections  Save and categorize content based on your preferences. 

You can configure charts, controls, and other components by using the properties and data panels in Data Studio. The panels let you customize how data is presented, apply interactive filters, and design dashboards that are tailored to your audience.

## Properties panel, data panel, and the panel manager

The properties panel, data panel, and panel manager appear on the right side of the report editor.

  * Use the properties panel to configure the selected component(s).
  * Use the data panel to access all of the data sources and their fields that are added to the report.
  * Use the panel manager to show or hide the properties panel and data panel.



The properties panel is context-dependent: when you select one or more report components, you'll see the properties that you can configure for those components.

For example, you will see the following elements when a table is selected on a report in edit mode:

![The report editor window showing the properties panel, the data panel, the panel manager, the setup tab, and the data sources and fields list.](https://docs.cloud.google.com/static/data-studio/images/data-panel-v2-simple-numbers-2022-06-01.png)

  1. The table that is selected on the report canvas.
  2. The data panel.
  3. The properties panel for the selected table.
  4. The setup tab for the selected table (part of the chart's properties panel).
  5. Data sources and fields list (part of the data panel).
  6. The panel manager.



When you select or add a component that has data properties, such as a chart, control, or image, the properties panel appears with the following tabs:

  1. Use the options in the **SETUP** tab to configure the component's data.
  2. Use the options in the **STYLE** tab to configure the component's appearance.



Static components, such as a text, shape, or line, have only style properties. When you select multiple components, you'll only see the settings those components have in common.

You can stylize the entire report by applying a [theme](https://docs.cloud.google.com/data-studio/themes) and changing the [layout](https://docs.cloud.google.com/data-studio/report-and-page-layout).

### Search for settings

To quickly find specific settings when you're navigating the **SETUP** or **STYLE** tab, use the **Search settings** bar in the properties panel. For example, you can search for the word _color_ in the chart properties panel to display settings such as **Color by** , **Bar border color** , and **Others color**.

![Searching for the word 'color' in the chart properties panel displays settings such as 'Color by', 'Bar border color', and 'Others color'.](https://docs.cloud.google.com/static/data-studio/images/search-settings.png)

## Set up a component's data

Here are the settings you can configure and actions you can perform that are common to all components. For settings and actions that are specific to an individual component, see the related resources section at the end of this document.

### Data source

A data source provides the connection between the component and the underlying dataset.

  * To change the chart's data source, click the current data source name.
  * To view or edit the data source, click ![Edit](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png). (You must have at least [Viewer permission](https://docs.cloud.google.com/data-studio/viewer-user-type) to see this icon.)
  * Click **+BLEND DATA** to see data from multiple data sources in the same chart. [Learn more about data blending](https://docs.cloud.google.com/data-studio/how-blends-work).



### Dimensions and metrics

Dimensions and metrics (collectively referred to as _fields_) contain the data that is displayed in your charts or acted upon by controls in your report.

**Dimensions** contain unaggregated data. Think of dimensions as categories of data, for example, names, descriptions, colors, sizes, or other characteristics of the data. The dimensions you add to a chart determine how the data in that chart is grouped. Dimensions appear as green fields in the properties panel.

**Metrics** measure the data that is contained in dimensions and provide the numeric scale and data series for your charts. Metrics appear as blue fields in the properties panel.

### Add dimensions and metrics

To add data to a component:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a component.
  3. In the component's **SETUP** tab, click **\+ Add a dimension** or **\+ Add a metric** , then select the field from the list. 
     1. To create a calculated field in the chart, click **\+ Add a dimension** or **\+ Add a metric** , then at the bottom of the field list, click **\+ Add a field**. Learn more about [Chart-specific calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields).
  4. From the data panel, drag a field to an available slot in the component's setup panel.
  5. From the data panel, drag a field directly to the component on the report canvas.

**Note:** You can add fields only from that component's current data source.

#### Data type

An icon that indicates a dimension's data type appears to the left of each dimension in the setup panel. The data type tells Data Studio what kind of data to expect when processing that field:

  * ![](https://docs.cloud.google.com/static/data-studio/images/data-type---text-2022-06-02.png): Text
  * ![](https://docs.cloud.google.com/static/data-studio/images/data-type---number-2022-06-02.png): Number or Currency
  * ![](https://docs.cloud.google.com/static/data-studio/images/data-type---date-2022-06-02.png): Date
  * ![](https://docs.cloud.google.com/static/data-studio/images/geo-type-2022-06-02.png): Geo
  * ![](https://docs.cloud.google.com/static/data-studio/images/data-type---image-2022-06-02.png): Image
  * ![](https://docs.cloud.google.com/static/data-studio/images/data-type---link-2022-06-02.png): URL
  * ![](https://docs.cloud.google.com/static/data-studio/images/data-type---boolean-2022-06-02.png): Boolean



[Learn more about data types](https://docs.cloud.google.com/data-studio/data-types).

#### Aggregation methods

Metrics are aggregations that come from the underlying dataset or that are the result of implicitly or explicitly applying an aggregation function, such as `COUNT()`, `SUM()`, or `AVG()`. The metric itself has no defined set of values, so you can't group by a metric as you can with a [dimension](https://docs.cloud.google.com/data-studio/dimension).

An icon that indicates a field's aggregation method appears to left of each metric in the setup panel:

Aggregation Method  |  Abbreviation  |  Description   
---|---|---  
Sum  |  SUM  |  The field values are added together.   
Average  |  AVG  |  The field values are averaged.   
Count  |  CT  |  Each field value is counted.   
Count Distinct  |  CTD  |  Only unique field values are counted.   
Min  |  MIN  |  The field displays the minimum value.   
Max  |  MAX  |  The field displays the maximum value.   
Auto  |  AUT  |  You can't apply this method directly. The aggregation method is supplied by the underlying data set, or as the result of a calculated field.  You can't change the Auto aggregation method.   
None  |  |  No aggregation is applied. The field is treated as a dimension, even if it contains numeric data.  **Note** This method only appears in the data source. The default aggregation for metrics in reports is Sum.   
  
[Learn more about aggregation](https://docs.cloud.google.com/data-studio/aggregation).

#### Edit a field

To change a field's name, data type or aggregation, click the type (for a dimension) or the aggregation (for a metric) icon. (The icon changes to ![Edit](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png) when you hover over it.)

[Learn more about editing fields in your reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).

### Date range dimension

This option appears if your data source has a valid date dimension.

**Note:** This option does not appear for Google Ads or Google Analytics data sources, as these automatically select a dimension of type **Date** from the data source.

The **Date range** dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension that is used if you set a date range property for the chart or if a viewer of the report uses a date range control to limit the time frame.

### Drill down

This option appears on charts that support it.

Drilling down gives viewers a way to reveal additional levels of detail within a chart. When you turn on the **Drill down** option **,** each dimension that you add becomes another level of detail that you can drill into. [Learn more about chart drill down](https://docs.cloud.google.com/data-studio/add-drill-actions-to-charts).

### Optional metrics

Define a list of additional metrics that can be displayed by the chart or table. [Learn more about optional metrics](https://docs.cloud.google.com/data-studio/optional-metrics).

### Metric sliders

Let report users filter the chart or table by metric values. [Learn more about metric sliders](https://docs.cloud.google.com/data-studio/metric-slider).

### Set the default sort

The **Sort** and **Secondary sort** options in the chart's setup panel control the default sorting behavior. You can select any metric in the chart's data source, or any dimension that is displayed in the chart, to use as the primary or secondary sorting field.

**Note:** The **Secondary sort** option only appears when there is an appropriate combination of dimensions and metrics in the chart. 

When you specify a metric as a sort field, you can [edit the field's aggregation](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports). For example, you could include a numeric field in the chart as a SUM, but sort on that same field's AVERAGE value.

### Default date range

The **Default date range** property lets you set a timeframe for an individual chart.

Default date range options:

  * **Auto:** Uses the default date range, which is determined by the chart's data source. 
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart. 
  * **Date compare type:** Displays comparison data for the selected time period. 



[Learn more about working with dates and time.](https://docs.cloud.google.com/data-studio/dates-and-times)

### Filter

Filters restrict the data that is displayed in the component by including or excluding the values that you specify. [Learn more about the filter property.](https://docs.cloud.google.com/data-studio/about-filter-properties)

Filter options:

  * **Filter name:** Click an existing filter to edit it. Mouse over the filter name and click **X** to delete it. 
  * **+Add a filter:** Click this option to create a new filter for the chart. 



### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

## Stylize a component

A chart's style properties control the overall presentation and appearance of the chart. All components share some common style settings, such as background, borders, and chart header options. For settings that are specific to an individual component type, see the [chart references](https://docs.cloud.google.com/data-studio/types-of-charts) and [control references](https://docs.cloud.google.com/data-studio/about-controls).

## Data panel

Use the data panel to quickly access the fields in the data sources that are added to the report.

### Search for a field

To find fields that you can add to the report, use the search bar at the top of the data panel. Searching for a field is contextual:

  * When no components are selected, you can search for fields in any data source that is added to the report.
  * When a component is selected, the search results are restricted to that component's data source.
  * When a group of components is selected, the search results are restricted to the grouped component's data sources.



### Add a field to a component

To add a field to an existing component on the canvas, select a field from that component's data source and then drag the field from the data panel onto the component.

### Create a new chart from a field

As a shortcut to using the toolbar or menus, you can create a new chart by dragging and dropping a field from the data panel to the canvas. Data Studio creates a new chart that is appropriate to the field you're adding:

  * For a metric or numeric dimension, Data Studio creates a new scorecard.
  * For a geo field type, Data Studio creates a new map.
  * For a date field type, Data Studio creates a new time series.
  * For other types of dimensions, Data Studio creates a new table.



The new chart is based on the data source from which you selected the field.

### Add calculated fields and parameters to a data source

At the bottom of the field list for each data source, the **\+ Add a field** and **\+ Add a parameter** buttons give you a convenient shortcut to create calculated fields and parameters in the selected data source.

## Related resources

  * [Add components to the report](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report)
  * [Add text, images, lines, and shapes](https://docs.cloud.google.com/data-studio/add-text-images-lines-and-shapes-to-your-reports)
  * [Chart references](https://docs.cloud.google.com/data-studio/types-of-charts)
  * [Control references](https://docs.cloud.google.com/data-studio/about-controls)
  * [Report settings](https://docs.cloud.google.com/data-studio/report-settings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
