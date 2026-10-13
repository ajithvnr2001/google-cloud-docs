---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-bypass-suggest-restrictions/
title: bypass_suggest_restrictions \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:34.493707+00:00
---

# bypass_suggest_restrictions  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-bypass-suggest-restrictions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  bypass_suggest_restrictions Stay organized with collections  Save and categorize content based on your preferences. 

> Use caution when using this parameter, as it can reveal sensitive data if used incorrectly.

## Usage
    
    
    view: view_name {
      dimension: field_name {
        bypass_suggest_restrictions: yes
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `bypass_suggest_restrictions` |  Possible Field Types Dimension, Dimension Group, Filter, Parameter Accepts A Boolean (yes or no)  
---|---  
  
## Definition

Typically, when [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) or [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter) is used, filter suggestions are restricted for that Explore. This prevents users from seeing a filter suggestion that does not apply to them.

For example, you might be using [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter) to limit users to their company's data. If one of those users added a **Project Name** filter, you might not want them to see the names of projects from other companies.

If you are certain that there are no possible values in a particular [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or [`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) field that would reveal sensitive information, you can re-enable filter suggestions like this:
    
    
    dimension: project_name {
      sql: ${TABLE}.project ;;
      bypass_suggest_restrictions: yes
    }
    

-

If there _are_ values in a field that would reveal sensitive information, the [`full_suggestions`](https://docs.cloud.google.com/looker/docs/reference/param-field-full-suggestions) parameter can enable you to get properly filtered suggestions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
