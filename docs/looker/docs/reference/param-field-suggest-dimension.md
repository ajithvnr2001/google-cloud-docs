---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-dimension/
title: suggest_dimension \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:38.271682+00:00
---

# suggest_dimension  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-dimension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  suggest_dimension Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        suggest_dimension: dimension_name
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `suggest_dimension` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, Parameter Accepts A fieldname in the current view or viewname.fieldname  Special Rules To refer to a field in another view, use viewname.fieldname where viewname is a view joined in the Explore  
---|---  
  
## Definition

This parameter changes how Looker generates suggestions for a [`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) field or a [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) of `type: string` when someone uses that field to filter a query.

Looker typically generates these suggestions by executing the following query on the filter field:

`SELECT DISTINCT <field name> FROM <table> LIMIT 1000`

If the field is in a large table, this query can be too slow or create too large a database load.

By using `suggest_dimension`, you can make Looker query an alternative dimension for the suggestion values. If that dimension is defined in a different Explore, [`suggest_explore`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-explore) tells Looker where to find it. In this case, include both the view name where the dimension is defined and the dimension name in the format `view_name.field_name`. In addition, ensure that the view is [joined](https://docs.cloud.google.com/looker/docs/working-with-joins) to the Explore that is specified in the `suggest_explore` parameter.

If the dimension is defined in the current view, `suggest_explore` is not required.

## Examples

In this example, instead of looking through a huge list of user names from the `event` Explore, we've told Looker to query the names from a `user` Explore instead:
    
    
    dimension: event_user_name {
      type: string
      sql: ${TABLE}.event_user_name ;;
      suggest_explore: user
      suggest_dimension: user.name
    }
    

In this example, rather than a different Explore, the suggestion uses a dimension in another view joined to the same Explore:
    
    
    dimension: event_company_name {
      type: string
      sql: ${TABLE}.event_company_name ;;
      suggest_dimension: company.name
    }
    

## Things to know

Fields with `suggest_dimension` will not be affected by [linked filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#setting_up_linked_filters) in dashboards.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
