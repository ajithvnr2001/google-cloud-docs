---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-hidden/
title: hidden (for fields) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:37.458711+00:00
---

# hidden (for fields)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-hidden/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  hidden (for fields) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `hidden` parameter that is part of a field.
> 
> `hidden` can also be used as part of an Explore, described on the [`hidden` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-hidden) parameter documentation page.

## Usage
    
    
    view: view_name {
      dimension: field_name {
        hidden: yes 
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [](https://docs.cloud.google.com/looker/docs/reference/param-field)[Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `hidden` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, Parameter Accepts A Boolean (yes or no)  
---|---  
  
## Definition

If you want a field to be available for modeling, but not shown to users, you can hide it from the field picker by using the `hidden` parameter.

Hidden fields can still be accessed in the UI if they are [manually added to the URL](https://discuss.google.dev/t/using-urls-and-query-parameters/115290). The `hidden` value is a way to keep the field picker clean; it is not a security feature.

The default value of `hidden` is `no`, unless the field is defined in a view that has the [`fields_hidden_by_default: yes`](https://docs.cloud.google.com/looker/docs/reference/param-view-fields-hidden-by-default) parameter.

You can use the `fields_hidden_by_default: yes` view parameter to set the default for all the view's fields to `hidden:yes`. This is helpful if you want to hide the majority of fields in a view, since you won't have to add `hidden:yes` to each of the view's fields. To display a field in a view that has the `fields_hidden_by_default: yes` parameter, add the `hidden:no` parameter to the field.

## Examples

Prevent the `raw_event_stream` dimension from appearing in the field picker:
    
    
    dimension: raw_event_stream {
      sql: ${TABLE}.event_stream ;;
      hidden: yes
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
