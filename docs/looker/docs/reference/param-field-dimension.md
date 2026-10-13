---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-dimension/
title: dimension \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:26.963405+00:00
---

# dimension  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-dimension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  dimension Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name { ... }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `dimension` |  Accepts A [Looker identifier](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#scoping_and_naming) to name the dimension  
---|---  
  
## Definition

The `dimension` parameter declares a new dimension and specifies a name for that dimension.

The name must meet the following requirements:

  * It must be unique within any given view.
  * It must consist of characters `a` through `z`, `0` through `9`, or `_`. The dimension name is case-sensitive. Because of this, we recommend using a consistent lowercase name for all LookML objects, including dimensions.
  * It must start with a letter.



There are many types of dimensions, as discussed further on the [Dimension, filter, and parameter types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types) documentation page.

## Subparameters for `dimension`

See the [Field parameters](https://docs.cloud.google.com/looker/docs/reference/param-field#example_usage) reference page for a list of subparameters that are available for LookML fields.

**Tip:** You can use the [Quick Help panel](https://docs.cloud.google.com/looker/docs/looker-ide#quick_help_panel) in the Looker IDE to quickly see the available subparameters for a given LookML field. Click a LookML parameter in the IDE editor panel to update the **Quick Help** panel to display the supported options and subparameters for that LookML element. Also, you can click a parameter name in the **Quick Help** panel to open the Looker documentation page for that parameter.

## Examples

Create an `id` and a `supplier_name` dimension in a view named `products`:
    
    
    view: products {
      dimension: id {
        primary_key: yes
        sql: ${TABLE}.id ;;
      }
      dimension: supplier_name {
        sql: ${TABLE}.supplier_name ;;
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
