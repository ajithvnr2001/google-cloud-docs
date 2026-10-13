---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-persist-for/
title: suggest_persist_for \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:38.759163+00:00
---

# suggest_persist_for  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-persist-for/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  suggest_persist_for Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        suggest_persist_for: "5 hours"
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `suggest_persist_for` |  Possible Field Types Dimension, Filter, Parameter Accepts A string specifying the length of time in seconds, minutes, or hours as follows: "N (seconds | minutes | hours)"  
---|---  
  
## Definition

When Looker determines the values that it will suggest to users when they filter on a [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or [`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) field, it runs a query to find the unique values of that field. By default this list of suggestions is cached for 6 hours. However, you can change the amount of time that suggestions are cached using `suggest_persist_for`.

Looker typically generates suggestions for a dimension by executing a `SELECT DISTINCT` query on that dimension. For some large tables this query can be too slow, or create too large of a database load. Caching suggestion values for a longer period reduces the number of `SELECT DISTINCT` queries. Alternatively, if your database is updated frequently, a shorter cache time results in fresher suggestion lists.

## Examples

Set the suggestion cache for the `name` dimension to 30 minutes:
    
    
    dimension: name {
      sql: ${TABLE}.name ;;
      suggest_persist_for: "30 minutes"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
