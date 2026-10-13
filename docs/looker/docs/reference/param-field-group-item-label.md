---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-group-item-label/
title: group_item_label \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:36.153889+00:00
---

# group_item_label  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-group-item-label/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  group_item_label Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        group_item_label: "desired label"
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `group_item_label` |  Possible Field Types Dimension, Dimension Group, Filter, Measure Accepts A string  
---|---  
  
## Definition

In cases where you've used the [`group_label`](https://docs.cloud.google.com/looker/docs/reference/param-field-group-label) parameter to combine fields into custom groups in a view's field picker, you can also use the `group_item_label` parameter for each of the grouped fields to customize how the individual fields are shown in the field picker.

For example, you can add the `group_label` to a set of fields like this:
    
    
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
    

These fields will now be combined into an expandable **Shipping Info** section in the field picker.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-group-label-66.png)

But since these fields are shown under the expandable **Shipping Info** section, they don't need to have "Shipping" in their individual labels as well. So you can add the `group_item_label` parameter to each of the grouped fields:
    
    
    view: accounts {
      dimension: shipping_city {
        sql: ${TABLE}.shipping_city ;;
        group_label: "Shipping Info"
        group_item_label: "City"
      }
      dimension: shipping_state {
        sql: ${TABLE}.shipping_state ;;
        group_label: "Shipping Info"
        group_item_label: "State"
      }
      dimension: shipping_street {
        sql: ${TABLE}.shipping_street ;;
        group_label: "Shipping Info"
        group_item_label: "Street"
      }
    }
    

![](https://docs.cloud.google.com/static/looker/docs/images/dev-group-item-label-66.png)

The `group_item_label` displays only in the field picker. In the Data section of an Explore and in any visualizations, Looker displays the field's name or label as normal.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
