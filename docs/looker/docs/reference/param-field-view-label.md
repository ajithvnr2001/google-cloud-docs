---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-view-label/
title: view_label (for fields) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:39.885768+00:00
---

# view_label (for fields)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-view-label/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  view_label (for fields) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `view_label` parameter that is part of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure), or [filter](https://docs.cloud.google.com/looker/docs/reference/param-field-filter).
> 
> `view_label` can also be used as part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore), described on the [`view_label` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label) parameter documentation page.
> 
> `view_label` can also be used as part of a [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join), described on the [`view_label` (for joins)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-view-label) parameter documentation page.

## Usage
    
    
    view: view_name {
      dimension: field_name {
        view_label: "desired label name"
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `view_label` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, Parameter Accepts A string  
---|---  
  
## Definition

The `view_label` parameter lets you change the name of the view under which the field is listed in the field picker without changing how it is referenced in LookML. If the label matches the name of an existing view, the field will now appear under that view. If you specify a new name, that name will appear in the field picker with the field under it. If not specified, the view label defaults to the name of the view.

Fields with view labels are still referenced with the normal `${view_name.field_name}` syntax in LookML. The view label only impacts the appearance of the field picker. It does not alter an existing view or create a new view.

Also, note the difference between a field's `view_label` and the field's [`label`](https://docs.cloud.google.com/looker/docs/reference/param-field-label). The `view_label` changes only the view name under which the field is listed, not the name that's displayed for the field itself.

## Examples

Make this dimension appear under the **Identifiers** view instead of the **Distribution Centers** view in the field picker.
    
    
    view: distribution_centers {
      dimension: id {
        view_label: "Identifiers"
        type: number
        sql: ${TABLE}.id ;;
      }
    }
    

For examples of using `view_label` with a [Liquid parameter](https://docs.cloud.google.com/looker/docs/templated-filters) to define dynamic labels, see the [Interesting ways to use Liquid in labels](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-liquid-in-labels) Best Practices page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
