---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-skip-drill-filter/
title: skip_drill_filter \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:37.941035+00:00
---

# skip_drill_filter  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-skip-drill-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  skip_drill_filter Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        skip_drill_filter: yes 
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `skip_drill_filter` |  Possible Field Types Dimension Accepts A Boolean (yes or no)  
---|---  
  
## Definition

When users drill into a measure, the resulting dataset is filtered so that users arrive at the specific records that made up that measure. Looker achieves this by adding filters that match the dimension values in the same row as the measure. For most types of dimensions, this works well.

However, if the value of one of those dimensions changed _during_ the process of drilling, this might cause the dataset to be different than the user was expecting. If a dimension may change often (likely a pre-aggregation that occurs in a frequent ETL process), you can stop it from being included in drill filters by using `skip_drill_filter`. `skip_drill_filter` accepts `true` or `false`.

## Examples

Prevent the `transactions` dimension from being included in drill filters:
    
    
    dimension: transactions {
      sql: ${TABLE}.transactions ;;
      type: number
      skip_drill_filter: yes
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
