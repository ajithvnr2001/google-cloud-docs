---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-alias/
title: alias \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:33.078726+00:00
---

# alias  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-alias/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  alias Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        alias: [old_field_name, old_field_name, ...]
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [](https://docs.cloud.google.com/looker/docs/reference/param-field)[Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `alias` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, Parameter Accepts A square-bracketed list of field names  
---|---  
  
## Definition

The `alias` parameter provides alternative names for a field that might appear in the URL for a query. It can be useful in cases when field names in a model change, but you have pre-existing URLs to queries that you want to keep functioning.

The following example shows how you could change a field named `count` to the new name `number_of_items`, without breaking any existing queries that refer to `count`.
    
    
    measure: number_of_items {  # the new name
      alias: [count]            # the old name
      type: count
    }
    

You can also provide multiple aliases, in case you rename a field multiple times. For example, if you renamed the `number_of_items` field from the previous example to `number_of_order_items`, you could use the following:
    
    
    measure: number_of_order_items {   # the new name
      alias: [count, number_of_items]  # the old names
      type: count
    }
    

To use `alias` with a dimension group, change the dimension group name, not every field in the dimension group. For example, to rename the dimension group `created_date` to `order_date`:
    
    
    dimension_group: order_date {  # the new name
      alias: [created_date]        # the old name
      type: time
      timeframes: [time, hour, date, week, month, year, hour_of_day, day_of_week, month_num, raw]
      sql: ${TABLE}.created_at ;;
    }
    

Note that `alias` is used only to keep URLs functioning. It should not be used when referencing fields in LookML. For example:
    
    
    measure: number_of_items {
      alias: [count]
      type: count
    }
    measure: percent_items_sold {
      sql: ${sold_items} / ${number_of_items} ;; # will work because there
      type: number                               # is a measure named number_of_items
    }
    measure: percent_items_sold {
      sql: ${sold_items} / ${count} ;; # will NOT work because you
      type: number                     # should not use alias names in LookML
    }
    

## Things to know

If you `alias` a field as a name already taken by another field, the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_changes) will return an error.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
