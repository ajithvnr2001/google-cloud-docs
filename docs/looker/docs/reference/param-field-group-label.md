---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-group-label/
title: group_label (for fields) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:35.965116+00:00
---

# group_label (for fields)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-group-label/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  group_label (for fields) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `group_label` parameter that is part of a field.
> 
> `group_label` can also be used as part of an Explore, as described on the [`group_label` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-group-label) parameter documentation page.

## Usage
    
    
    view: view_name {
      dimension: field_name {
        group_label: "desired label name"
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `group_label` |  Possible Field Types Dimension, Dimension Group, Filter, Measure Accepts A string  
---|---  
  
## Definition

The `group_label` parameter lets you combine fields into custom groups, within a given view, in the field picker. For example:
    
    
    view: accounts {
      dimension: shipping_city {
        sql: ${TABLE}.shipping_city ;;
        group_label: "Shipping Info"
      }
      dimension: shipping_state {
        sql: ${TABLE}.shipping_state ;;
        group_label: "Shipping Info"
      }
      dimension: shipping_street {
        sql: ${TABLE}.shipping_street ;;
        group_label: "Shipping Info"
      }
    }
    

In this case, instead of the fields appearing ungrouped, they are combined into an expandable **Shipping Info** section.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-group-label-66.png)

You can also use the `group_item_label` parameter to specify how fields appear in the field picker under a group label. See the [**`group_item_label`**](https://docs.cloud.google.com/looker/docs/reference/param-field-group-item-label) parameter documentation page for details.

`group_label` also interacts with dimension groups in useful ways, since a dimension group automatically places its fields together in the field picker. By using `group_label`, you can add additional fields into the dimension group. For example:
    
    
    view: accounts {
      dimension_group: created {
        type: time
        timeframes: [date, week, month]
        sql: ${TABLE}.created_date ;;
      }
      dimension: special_date_calculation {
        sql: QUARTER(${TABLE}.created_date)
        group_label: "Created Date" ;;
      }
    }
    

In the field picker, the `Special Date Calculation` field would appear in the `Created Date` dimension group.

![](https://docs.cloud.google.com/static/looker/docs/images/group_label-dimension-group.png)

You must have at least one field with the group label to create a group in the field picker. In addition, you can't group dimensions and measures together under the same group label, because all dimensions always appear separately from all measures within any given view.

For example, the following code creates a field named `Engine Type` inside a group label named `Engine Details`:
    
    
    dimension: engine_type {
        group_label: "Engine Details"
        type: string
        sql: ${TABLE}.engine_type ;;
      }
    

![](https://docs.cloud.google.com/static/looker/docs/images/group-label-single-field-70.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
