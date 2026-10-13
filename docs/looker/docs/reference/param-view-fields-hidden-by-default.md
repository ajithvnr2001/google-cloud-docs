---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-fields-hidden-by-default/
title: fields_hidden_by_default \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:27.487594+00:00
---

# fields_hidden_by_default  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-fields-hidden-by-default/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  fields_hidden_by_default Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      fields_hidden_by_default: yes 
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `fields_hidden_by_default` |  Accepts A Boolean (yes or no)  
---|---  
  
## Definition

By default, all fields in a view are displayed in the view's Explores. If you want a field to be available for modeling but not shown to users, you can hide the field from the Explore field picker by adding the [`hidden: yes`](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden) parameter to the field.

If you want to hide most of the fields in a view, you can instead add the `fields_hidden_by_default: yes` parameter to the view. This sets the default for all the view's fields to `hidden:yes`. Then, if you want to display a field in the view, you can add the `hidden:no` parameter to the field.

> Hidden fields can still be accessed in the UI if they are [manually added to the URL](https://discuss.google.dev/t/using-urls-and-query-parameters/115290). Therefore, the `hidden` value is a way to keep the field picker clean; it is not a security feature.

## Examples

This example `airports` view has the `fields_hidden_by_default: yes` parameter, so all fields are hidden in the view's Explores by default. The `country` dimension is defined with `hidden:no`, so it will be displayed in the view's Explores. The `id` dimension has no `hidden` parameter, so it will take the default value and will be hidden in the view's Explores.
    
    
    view: airports {
      sql_table_name: flightstats.airports ;;
      fields_hidden_by_default: yes
    
      dimension: id {
        primary_key: yes
        type: number
        sql: ${TABLE}.id ;;
      }
      dimension: county {
        type: string
        sql: ${TABLE}.county ;;
        hidden: no
      }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
