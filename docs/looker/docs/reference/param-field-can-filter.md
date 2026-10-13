---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-can-filter/
title: can_filter \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:32.570233+00:00
---

# can_filter  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-can-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  can_filter Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page refers to the `can_filter` parameter that is part of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [dimension group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group), or [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure).

## Usage
    
    
    view: view_name {
      dimension: field_name {
        can_filter: yes 
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `can_filter` |  Possible Field Types Dimension, Dimension Group, Measure Accepts A Boolean (yes or no)  
---|---  
  
## Definition

The `can_filter` parameter lets you prohibit a dimension or measure from being used as a filter. For example:
    
    
    dimension: description {
      can_filter: no
    }
    

The default value of `can_filter` is true, meaning that dimensions and measures can be used as filters as you would expect. However, there may be some cases when a field may be too demanding to search (like a large text description), and in these situations you can prevent that field from being used as a filter. Users won't see a **FILTER** option when they hover over the field.

Note that `can_filter` cannot be used with:

  * Measures of [`type: list`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#list), because they cannot be filtered on anyway
  * [`filter`](https://docs.cloud.google.com/looker/docs/templated-filters) fields, which only exist for the purpose of filtering
  * The [`filters`](https://docs.cloud.google.com/looker/docs/reference/param-field-filters) parameter that is used with measures



Additionally, drilling into a field won't be permitted if the drill requires a filterable dimension and the `can_filter` parameter is set to `no`. This occurs when you:

  * Attempt to drill on a dimension that uses `can_filter: no`
  * Attempt to drill on a measure if a `can_filter: no` dimension is used in the same query as that measure



See the documentation pages for [`drill_fields` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields) and [`drill_fields` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-drill-fields).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
