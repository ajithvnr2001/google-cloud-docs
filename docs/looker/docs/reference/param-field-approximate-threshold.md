---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-approximate-threshold/
title: approximate_threshold \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:34.197391+00:00
---

# approximate_threshold  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-approximate-threshold/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  approximate_threshold Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      measure: field_name {
        approximate_threshold: 100000
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `approximate_threshold` |  Possible Field Types Measure Accepts An integer  
---|---  
  
## Definition

Google BigQuery Legacy SQL calculates an exact `count_distinct` if there are fewer than 1,000 distinct values, but performs an approximation for larger numbers of distinct values. The approximate count is faster, but typically has an error of a few percent.

If you want BigQuery Legacy SQL to calculate an exact `count_distinct` for more than 1,000 distinct values, you can set that amount with the `approximate_threshold` parameter.

## Examples

Return an exact `count_distinct` for up to 100,000 distinct values:
    
    
    measure: unique_count {
      type: count_distinct
      approximate_threshold: 100000   # default value is 1000
      sql: ${id} ;;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
