---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-order-by-field/
title: order_by_field \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:37.530755+00:00
---

# order_by_field  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-order-by-field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  order_by_field Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        order_by_field: field_name
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [](https://docs.cloud.google.com/looker/docs/reference/param-field)[Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `order_by_field` |  Possible Field Types Dimension, Dimension Group, Measure Accepts A field name  
---|---  
  
> Using `order_by_field` incorrectly can cause inconsistent, confusing behavior for users.

## Definition

The `order_by_field` parameter lets you use the sort order from a dimension, dimension group, or measure on another field of the same type, rather than using the [default sort order](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#sorting_data). Fields that are referenced by the `order_by_field` parameter must match the field type of the parent field. A dimension cannot reference a field of `type: measure`, and vice versa.

For example, you have a table that contains both a `status_id` and a `status_name` column. When a user sorts by **Status Name** in the UI, you want the names to appear in the order of the status ID, and not the alphabetical order of the names.

> There should be a 1:1 relationship between a dimension or dimension group and the field referenced by the `order_by_field` parameter, so that the grouping characteristics of both fields are exactly the same. If you do not ensure this, sorting can appear to be random to users.

If there is one and only one `status_id` for each `status_name`, you could write:
    
    
    dimension: status_name {
      sql: ${TABLE}.status_name ;;
      order_by_field: status_id
    }
    

With measures, `order_by_field` lets you use the sort order from a measure on another measure.

This can be helpful in cases where you want to sort a non-numeric measure type, such as a [`string`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#string), by a numeric measure type.

In this example, a string of cities is ordered by a [`count`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count) measure:
    
    
    measure: user_cities {
      type: string
      order_by_field: count
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
