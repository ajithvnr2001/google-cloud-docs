---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields/
title: drill_fields (for fields) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:35.290006+00:00
---

# drill_fields (for fields)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  drill_fields (for fields) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `drill_fields` parameter that is part of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure).
> 
> `drill_fields` can also be used as part of a [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view), as described on the [`drill_fields` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-drill-fields) parameter documentation page.

## Usage
    
    
    view: view_name {
      dimension: field_name {
        drill_fields: [field_or_set, field_or_set, …]
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `drill_fields` |  Possible Field Types Dimension, Dimension within a Dimension Group, Measure Accepts A square-bracketed list of field names or set names  
---|---  
  
## Definition

The `drill_fields` parameter controls what happens when a user clicks the value of a table cell while they're exploring data. When a user does this, they "drill" into the data, allowing them to see the individual records that make up that cell, limit their query to the cell's value, or slice the data in a related way.

The `drill_fields` parameter accepts a list of fields, a list of [sets](https://docs.cloud.google.com/looker/docs/reference/param-view-set), or a combination of both fields and sets.

If a measure uses the `drill_fields` parameter, any drill fields set [at the view level](https://docs.cloud.google.com/looker/docs/reference/param-view-drill-fields) will not be applied to that measure.

Drilling can be disabled in some cases:

  * When using the [`can_filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-can-filter) parameter
  * When using the [`raw` timeframe](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#raw) in a dimension group



Once a user clicks on a drill field, they are taken into a [drill overlay](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#drilling_down_into_the_data). The data in the overlay has a default sort that's based on the following prioritization:

  1. The first date dimension, descending
  2. If no date dimension exists, the first measure, descending
  3. If no measure exists, the first added dimension, ascending



### Drilling into dimensions

When you drill into a dimension, you have the following options:

  * Limit the query to the dimension value that the user selected
  * Limit the query to the dimension value that the user selected and replace the dimension with another dimension



#### Limiting the query to the dimension value that the user selected

When you drill into a dimension, one option is to limit the query to the dimension value that you selected. In this case, when a user selects a dimension value, they can choose to filter on it.

![The Filter on UK option is selected in the drill menu of the value UK for the dimension Country.](https://docs.cloud.google.com/static/looker/docs/images/drill-fields-dimension-limit-2210.png)

In this example, by selecting **Filter on "UK"** in the drill menu, the resulting query will be filtered to show only results where the value of **Country** is **UK**.

This option is a default behavior for dimensions and doesn't require the use of the `drill_fields` parameter.

#### Replacing the dimension that the user selected with another dimension

When you drill into a dimension, another option is to limit the query to the dimension value you selected and to replace the original dimension with a different, related dimension in the query results. For example, suppose you have a field called **Country** , and you want to provide users with the option to drill into it by state and by city. The LookML would look like this:
    
    
    dimension: country {
      sql: ${TABLE}.country ;;
      drill_fields: [state, city]
    }
    

In the Looker UI, the drill menu for the **Country** dimension provides options for drilling into each value **by State** and **by City**.

![](https://docs.cloud.google.com/static/looker/docs/images/drill-fields-dimension-drill-2210.png)

If this example, if the user selects the **by State** option in the drill menu for the value **USA** in the **Country** column, the **Country** column in the resulting query is replaced by **State**. Any measures that were added to the query prior to drilling are also carried into the new query.

![](https://docs.cloud.google.com/static/looker/docs/images/drill-fields-dimension-drill-results-2210.png)

Dimension groups of [`type: time`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#time) have drill fields added to them by default. Each timeframe can drill to the more granular timeframes (e.g. week can drill to date and time, but not month). However, you can limit the timeframes that can be drilled to by using the `drill_fields` parameter:
    
    
    dimension_group: created {
      type: time
      timeframes: [time, date, week, month, year]
      sql: ${TABLE}.created ;;
      drill_fields: [created_month, created_date]
    }
    

### Drilling into measures

Drilling into a measure shows the row-level data about the items that comprise that measure. While the `drill_fields` parameter can be used with any measure type, it generally makes more sense when `drill_fields` is used with a measure of either [`type: count`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count) or [`type: count_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count_distinct). The information that is displayed for each row is defined by the fields or sets that you define in the `drill_fields` parameter.

For example, suppose you have the following LookML:
    
    
    measure: count {
      type: count
      drill_fields: [user_details*]
    }
    set: user_details {
      fields: [id, city, state, country]
    }
    

In this example, as defined in the LookML, because the `fields` subparameter of the [`set`](https://docs.cloud.google.com/looker/docs/reference/param-view-set) parameter lists the fields `id`, `city`, `state`, and `country`, those fields will appear in the query results when you drill into the measure `count`.

![Selecting a value for the Count measure opens a query on the fields ID, City, State, and Country.](https://docs.cloud.google.com/static/looker/docs/images/drill-fields-measure-2210.png)

### Linking to dashboards in drill menus

To specify links to specific dashboards (or other non-Looker URLs), you can use the [`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link) parameter.

Dashboards automatically appear in the drill menu if they have a [filter](https://docs.cloud.google.com/looker/docs/viewing-dashboards#temporarily_changing_filter_values_on_dashboards) on the field you are drilling into. This happens in the following cases:

  * There is a global field type filter on the dashboard that points to the field into which you are drilling.
  * There is a dashboard filter applied to the field in a dashboard tile. For example, there might be a numeric dashboard filter applied to the field `users.age` in a particular dashboard tile. This will cause the dashboard to appear in the drill menu for the `users.age` field.
  * Dashboards are in [**Shared** folders](https://docs.cloud.google.com/looker/docs/finding-content#top-level_folders).



For an example of drilling to a dashboard from the drill menu of a field, see the [Drilling into dashboards](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#drilling_into_dashboards) section of the **Exploring data in Looker** documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
