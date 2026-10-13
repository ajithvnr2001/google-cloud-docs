---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-suggestable/
title: suggestable \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:38.898768+00:00
---

# suggestable  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-suggestable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  suggestable Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        suggestable: yes 
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `suggestable` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, Parameter Accepts A Boolean (yes or no)  
---|---  
  
## Definition

When a user [filters an Explore](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) on a [field that supports suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions#fields_that_support_suggestions), by default Looker will suggest possible values for the field (see [Changing filter suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions) for information about how you can affect filter suggestions).

The `suggestable` parameter lets you disable suggestions for a field when a user filters on that field in a Look or an Explore. The default value of `suggestable` is `yes`, and suggestions are provided when possible. If you set `suggestable` to `no`, Looker won't suggest values for the field.

**Note:** If the field's view is defined with [`suggestions:no`](https://docs.cloud.google.com/looker/docs/reference/param-view-suggestions), Looker won't provide suggestions for any field in the view, even if the field is defined with `suggestable:yes`.

## Examples

Prevent Looker from providing filter value suggestions for the `name` dimension:
    
    
    dimension: name {
      type: string
      sql: ${TABLE}.name ;;
      suggestable: no
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
