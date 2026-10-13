---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-allow-fill/
title: allow_fill \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:33.554059+00:00
---

# allow_fill  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-allow-fill/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  allow_fill Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        allow_fill: yes 
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [](https://docs.cloud.google.com/looker/docs/reference/param-field)[Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `allow_fill` |  Possible Field Types Dimension, Dimension Group Default Value `yes` Accepts A Boolean (yes or no)  
---|---  
  
## Definition

Some datasets have values, such as dates, that follow a predictable pattern. A user might pull data by a time frame and find that some dates, weeks, months, or other date types don't have any corresponding value. By default, the data table and the visualization will display the dates that the query returns and skip any missing dates.

For these cases, Looker's **dimension fill** option lets the user [fill in missing dates and values](https://docs.cloud.google.com/looker/docs/creating-visualizations#filling_in_missing_dates_and_values) in the data table and in the axis of the query's visualization. This option is found in the dimension's gear menu in the **Data** section of an Explore.

![](https://docs.cloud.google.com/static/looker/docs/images/dimension-fill-menu-2320.png)

The `allow_fill` parameter for a dimension is used to enable or disable the option to fill in the missing values in the data table and in the axis of the visualization. By default, if the dimension type supports filling in missing values, the option is shown in the dimension's gear menu. To disable the option to fill in missing values for a dimension, set `allow_fill` to `no`.

The `allow_fill` option is available for dimension groups and dimensions that have a fixed number of values, such as yes/no and tiered values, as well as date types such as [`day_of_week` or `hour_of_day`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframe_options).

You can also use the [`case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) or [`tier`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#tier) parameter to apply the `allow_fill` option to any dimension option that is based on a list of values. Missing values are filled in automatically for queries that run with a single dimension and/or a single [pivot](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions), as long as the user has not applied filters to any measures.

Dimension fill can be applied to multiple dimensions at once in a query — including pivoted dimensions — however, Looker may automatically disable dimension fill to optimize query performance if it detects that too many fields will be generated with filled values.

## Examples

Prevent a user from being able to fill in missing values for the **Created Date** dimension:
    
    
    dimension: created_date {
      type: date
      sql: ${TABLE}.created_date ;;
      allow_fill: no
    }
    

## Things to consider

There are a few other cases when the user will not be able to dimension fill:

  * When dimensions make use of the [`order_by_field`](https://docs.cloud.google.com/looker/docs/reference/param-field-order-by-field) parameter.

  * When dimensions have a filter applied to them and also have a fixed number of values, such as yes/no, days of the week, days of the month, and so on. Filtering against these field types eliminates the fixed number of values that Looker needs to accurately fill in missing values.

  * When the user is [drilling](https://docs.cloud.google.com/looker/docs/creating-visualizations#drilling_into_visualizations) into a [pivoted](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions) dimension.

  * When Looker detects that too many rows or columns will be generated with filled values and automatically disables dimension fill to optimize query performance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
