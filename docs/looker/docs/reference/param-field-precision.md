---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-precision/
title: precision \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:36.820529+00:00
---

# precision  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-precision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  precision Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      measure: field_name {
        precision: 10 
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `precision` |  Possible Field Types Measure Default Value `6` Accepts An integer  
---|---  
  
## Definition

In Explores where fanout joins could cause incorrect results for aggregate functions, Looker applies [symmetric aggregate](https://docs.cloud.google.com/looker/docs/best-practices/understanding-symmetric-aggregates) logic to return correct calculations.

For aggregate fields where [symmetric aggregate](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates) logic is applied, by default Looker returns six digits after the decimal point. Use the `precision` field to change the number of digits after the decimal point:

  * Set the value of `precision` to `7` or higher if you need more digits after the decimal point for your calculations.

  * Set the value of `precision` to `5` or lower when working with very large numbers, to avoid overflowing the decimal limit on your database.

**Important:** Performing symmetric aggregation on measures with large numbers greater than 14 digits can cause errors such as `value overflow or collision when computing sum` when `precision` is set higher than `5`.



For more information about symmetric aggregates, see the [Understanding symmetric aggregates](https://docs.cloud.google.com/looker/docs/best-practices/understanding-symmetric-aggregates) Best Practices page.

**Note:** The `precision` parameter applies only for calculations with Looker's symmetric aggregate functionality. If you want to change the decimal precision of field values in the data table and visualization, use the [value_format](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) parameter instead.

## Examples

This example creates a field called `average_value` by averaging the `value` dimension, and maintaining a precision of 10 digits following the decimal point:
    
    
    measure: average_value {
      type: average
      precision: 10
      sql: ${value} ;;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
