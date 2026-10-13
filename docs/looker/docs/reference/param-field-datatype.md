---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-datatype/
title: datatype \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:34.446885+00:00
---

# datatype  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-datatype/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  datatype Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: order_date {
        datatype: date
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `datatype` |  Possible Field Types Dimension, Dimension Group, Filter, Measure Default Value `timestamp` Accepts One of several possible values  
---|---  
  
## Definition

The `datatype` parameter lets you specify the type of time or date data in your database table that you are supplying to your [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [dimension_group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group), [filter](https://docs.cloud.google.com/looker/docs/reference/param-field-filter), or [measure](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) field. Matching the data type to your field can increase query performance.

For dimensions, filters, and measures that contain date or time data, and for dimension groups with [`type: time`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_time), the `datatype` parameter applies to the [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter of the dimension group.

For dimension groups with [`type: duration`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_duration), the `datatype` parameter applies to both the [`sql_start`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#sql_start) and [`sql_end`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#sql_end) parameters, so be sure the `sql_start` and `sql_end` are both of the specified data type.

The `datatype` parameter accepts the following values:

  * `epoch` \- a SQL epoch field (i.e., an integer representing the number of seconds from the Unix epoch)
  * `date` \- a SQL date field (i.e., one that does not contain time of day information)
  * `datetime` \- a SQL datetime field
  * `timestamp` \- a SQL timestamp field
  * `yyyymmdd` \- a SQL field that contains an integer that represents a date of the form **YYYYMMDD**



The default value for `datatype` is `timestamp`.

## Example

Create a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) for a date field. Set the `datatype:` to `date` to increase query performance.
    
    
    dimension_group: order_date
      type: time
      timeframes: [date, week, month, year]
      datatype: date
      sql: ${TABLE}.order_date
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
