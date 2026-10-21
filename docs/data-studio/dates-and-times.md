---
url: https://docs.cloud.google.com/data-studio/dates-and-times/
title: Dates and times \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:27.682945+00:00
---

# Dates and times  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/dates-and-times/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Dates and times Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page describes how to work with date and time data types in Data Studio. To learn how to change the way those dates and times are displayed in a report, see [Format fields in reports](https://docs.cloud.google.com/data-studio/format-fields-in-reports).

You can use Data Studio to visualize and compare dates and times in charts and graphs, and let users adjust the report's date range. You can also use date functions in calculated fields to manipulate and transform date and time data.

## Date and time data types

Data Studio supports the following calendar date and time data types:

**Type** |  **Example data**  
---|---  
Date  |  Sep 15, 2020   
Date & Time  |  Sep 15, 2020, 6:10:59:59 PM   
Year  |  2020   
Year Quarter  |  Q3 2020   
Year Month  |  Sep 2020   
ISO Year Week  |  Sep 14, 2020 to Sep 20, 2020 (Week 38)   
Date Hour  |  Sep 15, 2020, 6 PM   
Date Hour Minute  |  Sep 15, 2020, 6:10 PM   
Quarter  |  Q3   
Month  |  September   
ISO Week  |  Week 35   
Month Day  |  Sep 15   
Day of Week  |  Tuesday   
Day of Month  |  23   
Hour  |  6 PM   
Minute  |  52   
  
**Note** : Data Studio doesn't support an explicit `TIME` data type. If your underlying dataset contains a `TIME` field, Data Studio converts that field to a `TEXT` field. For possible workarounds, [see the BigQuery connector documentation](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery#time_data_type).

### Date & Time (compatibility mode)

Date and time dimensions in data sources created before September 15, 2020 use a Date & Time (compatibility mode) data type. Compatibility mode dates include the format or an example in the name.

#### Learn how to upgrade a compatibility mode date

![Options for the compatibility mode Date & Time Type option on the Edit Connection panel include timeframes such as Year \(YYYY\), Year Quarter \(YYYYQ\), and Year Month \(YYYYM\), among others.](https://docs.cloud.google.com/static/data-studio/images/compatibility-mode-dates-2020-09-10.png) Compatibility mode dates have both a [**Format Type**](/data-studio/format-fields-in-reports) and a **Granularity** option when editing the field in charts. To adjust a chart's date grouping, use the **Granularity** option.  #### Upgrade a compatibility mode date field Compatibility mode dates continue to work in your existing components and calculated fields. However, you can't use compatibility mode dates with all of the available date and time functions. To use those functions, you can upgrade your date fields to new Date or Date & Time data types. 

**Warning:** When you upgrade a compatibility mode date to a new Date or Date & Time type:

  * You can use the upgraded field with functions such as `DATETIME_ADD`, `DATETIME_DIFF`, `EXTRACT`, and more.
  * Calculated fields and filters that expect a specific data format might fail, due to the new data type's formatting. You can fix any broken components by adjusting the formulas or filters to use the upgraded field's new format.
  * You can't change a Date or Date & Time field to compatibility mode. The compatibility mode type is turned off for upgraded fields.
  * If you decide you want to undo the change, use [version history](https://docs.cloud.google.com/data-studio/see-whats-changed-in-reports-and-data-sources) in the data source to restore an earlier version.

**To upgrade:** 1\. [Sign into Data Studio](https://datastudio.google.com). 2\. [Edit your data source](/data-studio/edit-a-data-source). 3\. Locate the compatibility mode date field you want to convert. 4\. Click the field's **Type** menu, then select **Date & Time**. 5\. Select the date type. 6\. In the dialog that appears, click **UPGRADE**. > Because upgrading might impact your reports, you must upgrade date and time fields individually. Reconnecting your data source won't upgrade the fields. > > The following connectors don't support the new Date and Date & Time data types, so you can't upgrade to or create those types in data sources using these connectors: > > \- Cloud Spanner > \- YouTube Analytics > \- BigQuery using Legacy SQL 

## Use dates and times in charts

You can group (aggregate) the data in your charts at different levels of date granularity to correspond to the data type in your data fields.

For example, adding a **Date** field to your chart will group the data by year, month, and day. To then group the data by month, you could change the data type to **Month** , or use a field from your data source with a data type of **Month**.

![Two time series charts: One chart displays a metric grouped by date, and the other chart displays a metric grouped by month.](https://docs.cloud.google.com/static/data-studio/images/charts-w-different-dates-2020-09-10.png)

  1. Chart showing Metric by full date.
  2. Chart showing Metric by month.



## Change a field's data type

You can change a field's data type in a chart or from the data source itself:

  * If you change a field's data type from the data source, the new data type is applied to the field everywhere the field is used. This may limit how you can use that field in charts.
  * If you change a field's data type from a chart, the new data type is applied to the field only in that one chart.



To change a field's data source everywhere the field is used, select the field's **Type** menu in the data source:

![A user selects the Date dimension Type drop-down menu on the Edit connection panel to display the available Date & Time timeframe options for the Date dimension.](https://docs.cloud.google.com/static/data-studio/images/new-dates-2020-09-10.png)

To change a field's data source in a single chart only, click the field's **Edit** icon in the **SETUP** tab of a report:

![A user selects a Date dimension field type icon on a table chart Setup tab to display the available Date & Time timeframe options for the Date dimension.](https://docs.cloud.google.com/static/data-studio/images/new-dates-in-charts-2020-09-10.png)

**Best practice:** Always have a full Date or Date & Time field in your data source. Use that field in your charts and adjust the field's type in the chart:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report)
  2. Select the chart.
  3. Place your cursor over the date field, then click the **Edit** icon ![](https://docs.cloud.google.com/static/data-studio/images/gmcreategrey60048dp-2020-03-12.png).
  4. Select the new field type.



## Use dates and times in calculated fields

You can use functions in calculated fields to create new columns of date and time data in your data source or directly in components on the report.

For example, you can construct a complete date from separate numeric day, month, and year fields using the `DATE` function. You can extract date and time parts from a date with functions like `YEAR`, `DAY`, and `HOUR`. You can calculate the difference between 2 dates using `DATETIME_DIFF`, or add a certain number of time parts using `DATETIME_ADD`.

[Learn more about date and time functions](https://docs.cloud.google.com/data-studio/currentdate).

### Date and Date & Time literals

To use literal date and time values in a calculated field, you can precede the value with the appropriate marker:

Literal  |  Canonical data format   
---|---  
` DATE ` |  ` 'YYYY-\[M\]M-\[D\]D' `  
` DATETIME ` |  ` 'YYYY-\[M\]M-\[D\]D \[\[H\]H:\[M\]M:\[S\]S\]' `  
  
### Examples:

Calculate the difference between a date from data and a specific fixed date:

`DATETIME_DIFF(date_field, DATE "2008-12-25", DAY)`

Format a date as text:

`FORMAT_DATETIME("%x", DATE "2008-12-25")`

## Related resources

  * [Set report date ranges](https://docs.cloud.google.com/data-studio/set-report-date-ranges)
  * [Date range control](https://docs.cloud.google.com/data-studio/date-range-control)
  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studiofunction list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
