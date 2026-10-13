---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions/
title: suggestions (for fields) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:39.113478+00:00
---

# suggestions (for fields)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  suggestions (for fields) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `suggestions` parameter that is part of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [filter field](https://docs.cloud.google.com/looker/docs/reference/param-field-filter), or [parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter).
> 
> You can also use `suggestions` as part of a [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view), as described on the [`suggestions` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-suggestions) parameter documentation page.

## Usage
    
    
    view: view_name {
      dimension: field_name {
        suggestions: ["suggestion string", "suggestion string", "…"]
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `suggestions` |  Possible Field Types Dimension, Filter, Parameter Accepts A string or a list of strings  
---|---  
  
## Definition

When a user [filters an Explore](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) on a [field type that supports suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions#fields_that_support_suggestions), by default Looker will suggest possible values for the field (see [Changing filter suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions) for information about how you can affect filter suggestions). To provide suggestions for a filter field, Looker executes a query on your database to retrieve a list of distinct values for the field. Looker typically generates these suggestions by executing a query such as the following on the filter field:
    
    
    SELECT DISTINCT field_name FROM table
    WHERE (field_name LIKE '%' OR field_name LIKE '% %')
    GROUP BY 1 ORDER BY 1 LIMIT 1000
    

The `suggestions` parameter lets you hard-code the list of suggested values for a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [filter field](https://docs.cloud.google.com/looker/docs/reference/param-field-filter), or [parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) that will appear when someone uses that field to filter a query.

**Note:** Although Looker caches up to 1,000 results for this query, only the first 100 results appear to the user as filter suggestions.

If the field is in a large table, this query can be too slow or create too large a database load. By using `suggestions` you can hard-code a list of possible values instead and improve performance.

The `suggestions` parameter is also useful because it lets you specify a more limited list if you don't want certain values from a field to appear as suggestions.

**Caution:** The `label` values from the [`case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) parameter will take precedence over suggestions presented to users from the `suggestions` parameter.

## Examples

Replace the default suggestions for the `colors` dimension with a hard-coded list:
    
    
    dimension: colors {
      type: string
      sql: ${TABLE}.colors ;;
      suggestions: ["red", "yellow", "blue"]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
