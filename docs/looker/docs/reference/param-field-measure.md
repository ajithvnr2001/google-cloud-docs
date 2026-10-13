---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-measure/
title: measure \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:27.851528+00:00
---

# measure  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-measure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  measure Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      measure:  field_name { ... }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `measure` |  Accepts [A Looker identifier](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#scoping_and_naming) to name the measure  
---|---  
  
## Definition

The `measure` parameter declares a new measure (aggregation) and specifies a name for that measure.

There are several criteria for a measure's name:

  * It must be unique within any given view.
  * It must consist of characters `a` through `z` (no capital letters), `0` through `9`, or `_`.
  * It must start with a letter.



There are many types of measures, as discussed further on the [Measure types](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) documentation page.

## Subparameters for `measure`

See the [Field parameters](https://docs.cloud.google.com/looker/docs/reference/param-field#example_usage) reference page for a list of subparameters that are available for LookML fields.

**Tip:** You can use the [Quick Help panel](https://docs.cloud.google.com/looker/docs/looker-ide#quick_help_panel) in the Looker IDE to quickly see the available subparameters for a given LookML field. Click a LookML parameter in the IDE editor panel to update the **Quick Help** panel to display the supported options and subparameters for that LookML element. Also, you can click a parameter name in the **Quick Help** panel to open the Looker documentation page for that parameter.

## Examples

Create measures named `product_count` and `total_value` in a view named `products`:
    
    
    view: products {
      measure: product_count {
        type: count
      }
      measure: total_value {
        sql: ${value} ;;
        type: sum
      }
    }
    

## Things to know

### Measures in joined views

To have measures (aggregations) come through joins, you must define primary keys in all the views that are involved in the join.

You can do this by adding the [`primary_key`](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) parameter to the primary key field definition in each view:
    
    
    dimension: id {
      type: number
      primary_key: yes
    }
    

> To correctly handle joined measures, Looker relies on you specifying a primary key where the values are completely unique, non-NULL values. If your data does not contain a primary key, consider whether the [concatenation of several fields](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) would result in a primary key of completely unique, non-NULL values. If your primary key is not unique or contains NULL values and your query includes data that reveals those issues, then Looker returns an error as described in the [Error: Non-Unique value/primary key (or sql_distinct_key), value overflow or collision when computing sum](https://docs.cloud.google.com/looker/docs/best-practices/error-non-unique-primary-key-computing-sum) Best Practices page.

### Measures based on other measures

It is possible to define a measure that is based on another measure. The new measure must be of `type: number` to avoid nested-aggregation errors. See the documentation on [`type: number` for measures](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number) for an example and explanation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
