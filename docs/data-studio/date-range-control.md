---
url: https://docs.cloud.google.com/data-studio/date-range-control/
title: Date range control \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:13:56.503236+00:00
---

# Date range control  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/date-range-control/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Date range control Stay organized with collections  Save and categorize content based on your preferences. 

The date range control is a customizable calendar widget that lets you adjust the timeframe of a report without editing the configuration. This gives you a way to let your viewers to select the dates they want to see.

## Add a date range control to a report

To add a date range control to a report, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the toolbar, select **Add a control** ![Control icon.](https://docs.cloud.google.com/static/data-studio/images/filterlistgrey6002x48dp-2020-09-09.png).
  3. Select the **Date range control** icon ![Date range control icon.](https://docs.cloud.google.com/static/data-studio/images/gmcalendartodaygrey60048dp-2021-10-27.png) and then place the control on the report.
  4. On the right, in the **Date range control Properties** panel, set the default date range or leave it set to **Auto date range**.
  5. Use the **STYLE** tab options to change the look of the control as it appears on the report.



## How date range controls work

The date range control lets you select the dates you want to see in the report. You can define a custom date range by choosing start and end dates, or you can select from a list of predefined ranges, including options such as Yesterday, Last 7 days (including today), Last quarter, and Year to Date.

### Default date range

When you first add a date range control to your report, it uses the default date range provided by the data source (which in turn, depends on the connector used by that data source). For example, the Google Analytics connector defaults to last 28 days, whereas the Google Sheets connector defaults to providing all the data contained in the sheet. You can override this default by changing the control's **Default date range** setting.

Learn more about [setting date ranges](https://docs.cloud.google.com/data-studio/set-report-date-ranges).

### Date range controls and data sources

To add a date range control to a report, at least one of the data sources attached to the report must have a date dimension. Date range controls only affect charts built on data sources that have a date dimension.

#### Multiple date fields in a chart

If a chart's data source contains more than one date or timestamp field (for example, _Order Date_ and _Ship Date_), the date range control affects only the field that you specify as the **Date Range Dimension** for that chart. You can set this value in the chart's **Setup** panel.

#### Multiple tables with different date fields

A single date range control can filter multiple tables or charts even if they use different date fields or come from different data sources. Each table or chart responds to the date range control, which uses each table's own **Date Range Dimension** setting. For example, Table A could use `created_at` as its date range dimension, while Table B could use `timestamp_utc`. The date range control will filter both tables based on the same selected time period, and use each table's respective date field.

To set up multiple date filters on a single report, consider [setting up parameters](https://docs.cloud.google.com/data-studio/use-parameters-in-a-custom-query).

### Date range control scope

A date range control governs all the charts on the page. You can limit the scope of the date range control in one of the following ways:

  1. By setting a date range property for an individual chart to override the date range control
  2. By grouping a date range control with a chart that limits the date range control to that chart. Any non-grouped charts are not affected by the date range control.



## Related resources

  * [About dates and time in Data Studio](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [About controls](https://docs.cloud.google.com/data-studio/about-controls)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
