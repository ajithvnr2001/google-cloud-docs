---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-string-datatype/
title: string_datatype \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:38.592486+00:00
---

# string_datatype  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-string-datatype/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  string_datatype Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        string_datatype: unicode
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `string_datatype` |  Possible Field Types Dimension Accepts The value `unicode` Special Rules Applies only to dimensions of `type: string` (which is the default if no `type` is specified)   
---|---  
  
## Definition

The `string_datatype` parameter lets you specify that the dimension's string values are unicode characters, which is helpful for dialects requiring special filter handling. Specifically, you can specify `string_datatype: unicode` for Microsoft SQL Server and MySQL for fields that have filters with unicode characters. This applies to:

  * Microsoft SQL Server (MSSQL) for non-Latin collations types
  * MySQL for variable character (NVARCHAR) and fixed-number character (NCHAR) types



The `string_datatype: unicode` parameter applies only to dimensions of [`type: string`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#string) (which is the default value for the `type` parameter).

## Examples
    
    
    dimension: comments {
      string_datatype: unicode
      sql: ${TABLE}.comments ;;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
