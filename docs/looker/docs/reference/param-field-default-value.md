---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-default-value/
title: default_value \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:34.726368+00:00
---

# default_value  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-default-value/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  default_value Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      filter: field_name {
        default_value: "chosen default value"
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `default_value` |  Possible Field Types Filter, Parameter Accepts Static, literal strings Special Rules If an Explore specifies a value for this field in an [`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) parameter, then that setting overrides the `default_value` setting for the field.   
---|---  
  
## Basics

The `default_value` parameter is used to specify a default value for [`filter` fields](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) and [`parameter` fields](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter).

**Caution:** Avoid using `default_value` with `parameter` if your data has values that include underscores.

See the following example of this parameter's usage:
    
    
    filter: order_region {
      default_value: "Northeast"
    }
    

-

## Common challenges

If an `explore` parameter has a value specified by an [`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) parameter, then that setting overrides the `default_value` setting for the field.

This parameter doesn't accept [Liquid variables](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) or [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
