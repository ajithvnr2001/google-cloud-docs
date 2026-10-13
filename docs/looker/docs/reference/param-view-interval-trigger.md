---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-interval-trigger/
title: interval_trigger \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:31.037377+00:00
---

# interval_trigger  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-interval-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  interval_trigger Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `interval_trigger` parameter that is part of a [derived_table](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table).
> 
> `interval_trigger` can also be used as part of a datagroup, described on the [`datagroup`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup#interval_trigger) parameter documentation page.

## Usage
    
    
    view: my_view {
      derived_table: {
        interval_trigger: "N (seconds | minutes | hours)"
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `interval_trigger` |  Default Value none Accepts A string containing an integer followed by a timeframe (seconds, minutes, or hours)   
---|---  
  
## Definition

`interval_trigger` lets you trigger the regeneration of a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_\(pdts\)) based on a time interval. In the `interval_trigger` parameter you pass a string containing an integer followed by "seconds", "minutes", or "hours".

## Example

This persistent derived table has an `interval_trigger` of `"3 hours"`, so every three hours it will be triggered to rebuild:
    
    
    derived_table: {
      interval_trigger: "3 hours"
      ...
       }
     }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
