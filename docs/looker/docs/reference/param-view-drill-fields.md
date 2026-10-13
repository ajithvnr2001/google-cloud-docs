---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-drill-fields/
title: drill_fields (for views) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:28.083154+00:00
---

# drill_fields (for views)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-drill-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  drill_fields (for views) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `drill_fields` parameter that is part of a [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view).
> 
> `drill_fields` can also be used as part of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure), described on the [`drill_fields` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields) parameter documentation page.

## Usage
    
    
    view: view_name {
      drill_fields: [field_or_set, field_or_set, …]
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `drill_fields` |  Possible Field Types Dimension, Dimension within a Dimension Group, Measure Accepts A square-bracketed list of field names or set names  
---|---  
  
## Definition

The `drill_fields` parameter controls what happens when a user clicks on the value of a table cell while exploring data. When a user does this, they "drill" into the data, allowing them to see the individual records that make up that cell, limit their query to the cell's value, or slice the data in a related way.

The `drill_fields` parameter accepts a list of fields, [sets](https://docs.cloud.google.com/looker/docs/reference/param-view-set), or a combination of both fields and sets.

At the view level, `drill_fields` applies the declared drill fields to all measures in the view that do not have `drill_fields` defined [at the measure level](https://docs.cloud.google.com/looker/docs/reference/param-field-measure).

Drilling can be disabled by including in the query a dimension with the [`can_filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-can-filter) parameter set to `no`.

## Example

Suppose you have the following LookML:
    
    
    view: orders {
      drill_fields: [source*, age]
      measure: count {
        type: count
      }
      measure: average_age {
        type: average
        sql: ${age} ;;
        drill_fields: [id, name, city, state]
      }
      set: source {
        fields: [traffic_source, country]
      }
    }
    

Drilling into the **Average Age** field displays the **ID** , **Name** , **City** , and **State** fields. Drilling into the **Count** field displays the default **Traffic Source** , **Country** , and **Age** fields.

![](https://docs.cloud.google.com/static/looker/docs/images/view-drill-fields-example-2214.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
