---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-label-from-parameter/
title: label_from_parameter \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:36.761133+00:00
---

# label_from_parameter  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-label-from-parameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  label_from_parameter Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        label_from_parameter: parameter_name
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `label_from_parameter` |  Possible Field Types Dimension, Measure Accepts A [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) name  
---|---  
  
## Definition

The `label_from_parameter` parameter lets you change how a field name appears in a visualization, based on the value of a [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter).

The field name remains unchanged in the data table and the field picker.

In the following example we create a parameter called `item_to_add_up` that lets a user choose the database column to sum. A corresponding measure called `dynamic_sum` performs the calculation, and it takes on the name of the parameter value because we've used `label_from_parameter: item_to_add_up`.
    
    
    parameter: item_to_add_up {
      type: unquoted
      allowed_value: {
        label: "Total Sale Price"
        value: "sale_price"
      }
      allowed_value: {
        label: "Total Cost"
        value: "cost"
      }
      allowed_value: {
        label: "Total Profit"
        value: "profit"
      }
    }
    
    measure: dynamic_sum {
      type: sum
      sql: ${TABLE}.{% parameter item_to_add_up %} ;;
      label_from_parameter: item_to_add_up
      value_format_name: "usd"
    }
    

When the parameter value `Total Sale Price` is selected, the `dynamic_sum` field will appear as `Total Sale Price` in the visualization. The field will still appear as `Dynamic Sum` in the data table and the field picker.

![](https://docs.cloud.google.com/static/looker/docs/images/label_from_parameter_422.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
