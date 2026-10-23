---
url: https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports/
title: Edit fields in your reports \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:17.389344+00:00
---

# Edit fields in your reports  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Edit fields in your reports Stay organized with collections  Save and categorize content based on your preferences. 

By default, the definitions of the fields in your reports match how those fields are defined in the underlying data source. Specifically, fields in the report have the same name, data type, and aggregation as in the data source.

The **Field Editing in Reports** data source option allows report editors to change field definitions at the chart level. Editing field definitions in the report makes customizing your reports faster and easier. It reduces or even eliminates the need to duplicate fields in the data source in order to apply different aggregations or functions to the same data. It also lets you have canonical field definitions in the data source, while tailoring the fields to fit different report requirements.

## Enable or disable field editing in reports

**Note:** The **Field Editing in Reports** option—which allows this capability to be turned off at the data source level—is available only for **reusable** data sources. For charts that are based on **embedded** data sources, report editors can always modify the field definitions. [Learn more about the differences between embedded and reusable data sources](https://docs.cloud.google.com/data-studio/embedded-data-sources#embedded_versus_reusable_data_sources).

You enable or disable field editing in reports at the data source level. New data sources have this option turned on by default. You must be able to edit the data source to change this.

**To turn this off or on (for older data sources)** , follow these steps:

  1. Edit the data source(s) used in your report
  2. In the data source header, click **Field Editing in Reports.**



## How editing fields in reports works

When you create a report that's based on a data source that has the **Field Editing in Reports** setting turned on, all the fields in the report that use the data source become editable. This option applies to all reports that use that data source. To edit a field definition in a report, follow these steps:

  1. Create or [edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. [Add a new chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report) or select an existing chart.
  3. In the **Setup** tab of the **Properties** panel, click a field's data type icon to open the field's edit menu.



![A user hovers a cursor over a dimension Type icon on the Setup tab of the chart Properties panel to edit the field type.](https://docs.cloud.google.com/static/data-studio/images/editable-fields-2017-08-23.png)

### What you can edit

Editing a field lets you change the following:

  * The field's **name**. For example, you can rename _Order Value_ to _Average Order Value_.

  * A metric's **aggregation**. For example, you can recalculate _Order Value_ from **Sum** to **Average**.

This option isn't available if the field is a metric with Auto aggregation type.

  * The field's **data type**. For example, you can convert a **Number** to a **Percent** , or **Text** to a **URL** , or a full **Date** to a date part.

  * A metric's **comparison calculation**. For example, you can apply a **Percentage of Total** function to your orders.

  * A metric's **running calculation**. For example, you can show running sums of your data, record by record.

  * A [**calculated field**](https://docs.cloud.google.com/data-studio/about-calculated-fields) formula, a [**custom bin**](https://docs.cloud.google.com/data-studio/create-a-custom-bin) definition, or a [**custom group**](https://docs.cloud.google.com/data-studio/create-a-custom-group) definition.

  * A dimension's [drill actions](https://docs.cloud.google.com/data-studio/add-drill-actions-to-charts) (for table charts only).

  * A [custom value format](https://docs.cloud.google.com/data-studio/format-fields-in-reports) for a **Numeric** or **Date & Time** type dimension, metric, or calculated field.




Learn more about [comparison and running calculations](https://docs.cloud.google.com/data-studio/add-comparison-metrics-and-running-totals).

Any changes that you make to a given field apply only to that instance of that field in that chart. For example, if the **Average Order** field appears in a table and a bar chart in the same report, changing any of the attributes of that field in the table has no effect on the **Average Order** field in the bar chart.

## Rename a field

You can change a field's display name in the selected chart. This lets you have multiple instances of the same field in a chart. For example, you can add two instances of the **Order Value** field to a table and change the name of the second instance to **Average Order Value**. Use the aggregation options that are described next on this page to change how the field is calculated.

## Change the field aggregation

A field's aggregation determines how its data is calculated in the chart. You can select from the following aggregations:

  * Average
  * Count Distinct
  * Count
  * Max
  * Median
  * Min
  * Standard deviation
  * Sum
  * Variance



Metrics with an aggregation of Auto [can't be changed](https://docs.cloud.google.com/data-studio/what-does-the-unable-to-aggregate-ratio-metrics-error-mean).

## Change the field data type

A field's data type tells Data Studio what kind of data to expect as input. For example, Data Studio displays Text fields "as is," with no other processing. Even if the field contains numbers, Data Studio won't apply any numeric aggregation to it. A field defined as a URL, on the other hand, is displayed as a hyperlink.

When the specified data type and actual data don't match, unexpected results can occur. You can adjust a field's data type in circumstances when the data source hasn't been correctly configured and you don't have edit access to it. For example, converting a dimension containing valid data but defined as **Text** to a **Date** type can let you use it as date range dimension.

You can also further customize how **Numeric** and **Date & Time** field type values are displayed by applying [custom value formatting](https://docs.cloud.google.com/data-studio/format-fields-in-reports) to dimensions, metrics, and custom fields in charts.

## Change the date granularity

Changing a **Date & Time** field type aggregates the data by the new type. For example, instead of grouping your data by year, month, and day, you can group by year and month.

For example, if the date field contains the complete year, month, and day, you can group by year quarter.

### Example

The following tables show the same data. The first table groups **Qty Sold** by **Date** and **Item** , listing each item and **Qty Sold** more than once; the second table groups **Qty Sold** by **Item** with the time granularity set to **Year Quarter** , which results in each item listed once with their quarterly **Qty Sold** for Q4.

Date  |  Item  |  Qty Sold   
---|---|---  
Oct 1, 2016  |  Healthy Dog Dog Food  |  3   
Oct 1, 2016  |  Hungry Kitty Cat Food  |  1   
Oct 1, 2016  |  Pretty Bird Bird Seed  |  5   
Oct 1, 2016  |  Happy Cat Catnip  |  1   
Oct 2, 2016  |  Pretty Bird Bird Seed  |  3   
Oct 2, 2016  |  Happy Cat Catnip  |  2   
Oct 2, 2016  |  Parrot Perch  |  4   
Oct 3, 2016  |  Playful Puppy Toy  |  9   
Oct 3, 2016  |  Hungry Kitty Cat Food  |  2   
Oct 4, 2016  |  Pretty Bird Bird Seed  |  5   
|  **Grand Total** |  **62**  
Date  |  Item  |  Qty Sold   
---|---|---  
Q4, 2016  |  Pretty Bird Bird Seed  |  20   
Q4, 2016  |  Healthy Dog Dog Food  |  16   
Q4, 2016  |  Playful Puppy Toy  |  11   
Q4, 2016  |  Parrot Perch  |  8   
Q4, 2016  |  Happy Cat Catnip  |  4   
Q4, 2016  |  Hungry Kitty Cat Food  |  3   
|  **Grand Total** |  **62**  
**Important:** To change how compatibility mode dates group the data, use the **Granularity** option, _not_ the **Type** option.

You can also further customize how **Numeric** and **Date & Time** field type values are displayed by applying [custom value formatting](https://docs.cloud.google.com/data-studio/format-fields-in-reports) to dimensions, metrics, and custom fields in charts.

## Related resources

  * [About data sources](https://docs.cloud.google.com/data-studio/about-data-sources)
  * [Dates and Times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Model your data](https://docs.cloud.google.com/data-studio/model-your-data)
  * [Format fields in reports](https://docs.cloud.google.com/data-studio/format-fields-in-reports)
  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
