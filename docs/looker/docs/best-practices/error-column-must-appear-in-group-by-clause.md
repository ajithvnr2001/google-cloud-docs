---
url: https://docs.cloud.google.com/looker/docs/best-practices/error-column-must-appear-in-group-by-clause/
title: Error: Column < name > must appear in the GROUP BY clause or be used in an aggregate function \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:41.763672+00:00
---

# Error: Column < name > must appear in the GROUP BY clause or be used in an aggregate function  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/error-column-must-appear-in-group-by-clause/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Error: Column < name > must appear in the GROUP BY clause or be used in an aggregate function Stay organized with collections  Save and categorize content based on your preferences. 

This page can help you troubleshoot the `column `name` must appear in the GROUP BY clause or be used in an aggregate function` error in Looker. 

This error commonly occurs when a dimension is used in a measure that does not have an aggregate type. Our [measure type documentation](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#measure_type_categories) contains a list of measure types and whether each is an aggregate type. 

For example, a `type: number` measure is not an aggregate measure, so this LookML would produce an error: 
    
    
    measure: bad_measure {
     type: number
     sql: ${measure} + ${dimension} ;;
    }
    

Typically you fix this problem by first turning the dimension into a measure, and then using that new measure in your calculations. For example: 
    
    
    measure: dimension_total {
     type: sum
     sql: ${dimension} ;;
    }
    
    measure: good_measure {
     type: number
     sql: ${measure} + ${dimension_total} ;;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
