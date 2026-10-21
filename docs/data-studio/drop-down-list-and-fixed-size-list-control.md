---
url: https://docs.cloud.google.com/data-studio/drop-down-list-and-fixed-size-list-control/
title: Drop-down list and Fixed-size list control \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:56:11.644694+00:00
---

# Drop-down list and Fixed-size list control  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/drop-down-list-and-fixed-size-list-control/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Drop-down list and Fixed-size list control Stay organized with collections  Save and categorize content based on your preferences. 

Drop-down list and Fixed-size list controls show a list of options from which you can select. The list can come from the values in a dimension, or from a list of acceptable values defined for a parameter.

## Drop-down list and Fixed-size list control DATA options

Most of the DATA options only apply to controls as filters. To configure parameter data options, edit the parameter in the data source.

### Data Source

Provides the dimensions and parameters you can use in the control.

### Date range dimension

This option appears if your data source has a valid date dimension. For Google Ads and Analytics data sources, this option is automatically set to the Date dimension.

The Date Range Dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension used if you set a date range property for the chart, or if you use a date range control to limit the timeframe.

### Dimension

Provides the list of values that appear in the control.

### Control field

The dimension to filter by or the parameter whose value is set by this control.

### Default selection

Specify a default value or parameter.

To specify multiple values for a dimension, enter a comma-separated list. Be sure to enter the values exactly as they appear in your data. Parameter controls only support selecting a single default value.

**Note:** Parameter values will be interpreted as strings, even if the parameter type is another data type.

### Metric

This option displays a reference metric in the control. You can use this to sort the list, however, you can't filter based on the metric value. To hide the metric, clear the Show values option.

### Decimal precision

Specify the number of digits in the metric value to show.

### Order

This option controls the sort order and number of values listed in the control. You can sort the values list in either ascending or descending order by the dimension values, or by any metric.

### Show top

This option limits the number of items displayed in the control. If the number of items available exceeds this limit, remaining items are grouped into "All others."

### Default Date Range

This option limits the values displayed in the control to the range you specify.

### Filter

Restrict the data displayed in the control by including or excluding the values you specify.

## Drop-down list and Fixed-size list control STYLE options

### Drop-down

Displays the control in a drop-down box.

### Fixed-size

Displays the control as a fixed-size box.

### Single-select

Requires you to choose only one option from the list. Note that parameter controls only support selecting single values.

### Allow Select all

Lets you run the report without any options selected, which returns data from all values in the list. This option is only displayed if the Single-select option is enabled. If this option is disabled, you must define a default selected value.

### Enable search box

Lets you search for values in the list.

## Related resources

[About parameters](https://docs.cloud.google.com/data-studio/parameters)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
