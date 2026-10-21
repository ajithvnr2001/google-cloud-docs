---
url: https://docs.cloud.google.com/data-studio/about-controls/
title: About controls \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:40:45.635140+00:00
---

# About controls  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/about-controls/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  About controls Stay organized with collections  Save and categorize content based on your preferences. 

Controls make reports interactive by letting viewers filter data or provide input. You can use controls to do the following:

  * Filter data by dimension values
  * Accept user input for [parameters](https://docs.cloud.google.com/data-studio/parameters)
  * Set the report timeframe
  * Change the dataset used by a data source

**Note:** To filter data _before_ viewers see it, use a [filter property](https://docs.cloud.google.com/data-studio/about-filter-properties) instead of a control.

## Types of controls

Data Studio supports the following types of controls:

  * [Drop-down and fixed-size lists](https://docs.cloud.google.com/data-studio/drop-down-list-and-fixed-size-list-control) let the viewer select from a list of filter values.
  * [Input boxes](https://docs.cloud.google.com/data-studio/input-box-control) let viewers enter a value to use as a filter or to provide input to a parameter.
  * [Advanced filters](https://docs.cloud.google.com/data-studio/advanced-filter-control) let viewers create conditional filters by using comparison operators and regular expressions.
  * [Sliders](https://docs.cloud.google.com/data-studio/slider-control) let viewers filter by a range of values in a numeric dimension.
  * [Checkboxes](https://docs.cloud.google.com/data-studio/checkbox-control) let viewers filter by a Boolean dimension or set the value of a Boolean parameter.
  * [Preset filters](https://docs.cloud.google.com/data-studio/preset-filter-control) can be used in combination with buttons to let viewers apply preconfigured filters to a report.
  * [Date range controls](https://docs.cloud.google.com/data-studio/date-range-control) let viewers adjust the timeframe of a report.
  * [Data controls](https://docs.cloud.google.com/data-studio/data-control) let you select the dataset that is used by a report.
  * [Dimension controls](https://docs.cloud.google.com/data-studio/dimension-control) let report viewers change the dimensions in a chart without needing to edit the report.
  * [Buttons](https://docs.cloud.google.com/data-studio/add-buttons) let viewers filter data, access report actions, and navigate to linked content.



## Controls as filters

Filter controls limit the number of records displayed in a chart or table. Providing interactive filters in your reports helps your viewers focus on the data that's most important to them.

Here are some important considerations to keep in mind when using controls as filters:

  * Filters are applied at the data source level, not the chart level.
  * Filters are based on field ID, not display name.
  * Filtering across multiple data sources may require additional configuration.
  * Filters also apply to other controls, not just charts.
  * Filters are generally case-sensitive, but this can vary by connector.



These considerations are explained in detail in the following sections.

### Filters are applied at the data source level

Filters are applied at the data source level, not the chart level. This means that the field that you are filtering on doesn't have to be in the chart, as long as that field appears in the chart's **Data** panel.

**Note:** Filters aren't applied to fields that are hidden in the data source.

### Filters are based on field ID, not display name

Fields in your data source have both a visible display name and a field ID. Filters are applied based on the field's **Field ID** , not the field's display name.

For example, your data source might have a country dimension. The display name might be **Country** while the field ID is a string assigned by the data source connector (for example `_abcd123`). When you apply a filter control, such as **Country** = "France", Data Studio looks for the country field's _internal ID_ in all the data sources used by charts on the page. If a data source contains a field with the ID `_abcd123`, the control will apply the filter to that field.

The preceding concept is a key to understanding how filters work—or don't work—across multiple charts in your report.

### Filter across multiple data sources

If your report uses only one data source, controls will filter all charts without the need for further configuration. If your report uses multiple data sources, filtering behavior depends on whether the field IDs match across those data sources.

The following table summarizes how filtering across data sources works:

If charts in report use... | Field IDs Match? | Automatic Filtering? | Examples  
---|---|---|---  
**One data source** | Yes | **Yes** | N/A  
Multiple data sources of the **same type** from a **fixed-schema** connector | Yes | **Yes** | Google Analytics, Google Ads  
Multiple data sources of **different types** , or from a **flexible-schema** connector | No | **No** (Requires unifying IDs) | Google Sheets, BigQuery; or mixing Sheets + Analytics  
  
In the preceding table, _fixed schema connectors_ refer to data source connectors such as Google Ads and Google Analytics. Fixed schema connectors have a predefined structure. They create data sources that have the same field IDs for every data source that is based on that connector. _Flexible schema connectors_ , on the other hand, create data sources that have a variable, user-defined structure. Examples of flexible schema connectors include Google Sheets and BigQuery.

When your report includes charts that are based on different flexible schema data sources and you want a control to filter across those data sources, you may have to [manually unify the field IDs](https://docs.cloud.google.com/data-studio/use-controls-across-data-sources).

### Filters also apply to other controls, not just charts

Filters don't just apply to charts; they can also filter other controls. For example, say you have one filter on a Country dimension, and a second filter on a Campaign dimension. Filtering on **Country** = "France" causes the filter on the Campaign dimension to only show the campaigns that ran in France. Similarly, filtering on **Campaign** = "ABC" restricts the filter on the Country dimension to only show the countries where that campaign ran.

### Filters and case-sensitivity

In general, the search operators for text dimensions are case-sensitive. However, this can vary by connector, so it's a good idea to test this on your data and provide guidance to your report viewers. To create a case-insensitive regular expression, you can prepend the expression with `(?i)`. Learn more about [Regular expressions in Data Studio](https://docs.cloud.google.com/data-studio/regular-expressions).

## Controls as input

When a control is based on a parameter, the control provides input to that parameter. Parameters are like variables that get their value from the an interaction with the report (say, by typing in a value directly, or picking a value from a predefined list).

You can use parameters to make calculated fields more dynamic. For example, you could create a _Sales Target_ parameter and use it as the control field for an Input box to let people enter different sales goal numbers to visualize projected performance. You could then apply conditional formatting rules that highlight the results in eye-catching ways.

You can also pass parameters back to the underlying SQL query used to create a BigQuery data source, or to data sources created using community connectors.

[Learn more about parameters](https://docs.cloud.google.com/data-studio/parameters).

## Related resources

  * [Apply controls to specific charts](https://docs.cloud.google.com/data-studio/apply-controls-to-specific-charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
