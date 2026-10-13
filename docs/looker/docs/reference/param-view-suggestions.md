---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-suggestions/
title: suggestions (for views) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:28.668596+00:00
---

# suggestions (for views)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-suggestions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  suggestions (for views) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `suggestions` parameter that is part of a [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view).
> 
> `suggestions` can also be used as part of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or [filter field](https://docs.cloud.google.com/looker/docs/reference/param-field-filter), described on the [`suggestions` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions) parameter documentation page.

## Usage
    
    
    view: view_name {
      suggestions: yes
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `suggestions` |  Default Value `yes` Accepts A Boolean (`yes` or `no`)  
---|---  
  
## Definition

When a user [filters an Explore](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) on a [field that supports suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions#fields_that_support_suggestions), by default Looker will suggest possible values for the field (see [Changing filter suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions) for information about how you can affect filter suggestions).

Looker provides the dimension's possible values from the database and suggests the possible values based on what the user has typed in the filter field. Suggestions are on by default for most dialects. You can add the `suggestions: no` statement to a [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) definition to disable filter value suggestions for all the dimensions in the view that support suggestions.

> For some dialects, such as Amazon Athena, Qubole Presto, Trino, Cloudera Impala, Apache Hive, and Apache Spark, providing suggestions requires querying the database, which may be expensive. Because of this, if you use Looker to [automatically generate a project from your database](https://docs.cloud.google.com/looker/docs/generating-a-model) for these dialects, Looker will create the views with the `suggestions: no` declaration.

## Example

Here is an example view where suggestions are disabled for all dimensions:
    
    
    view: aircraft_types {
      sql_table_name: flightstats.aircraft_types ;;
      suggestions: no
      ...
    }
    

## Things to know

### `suggestions` at the view level works differently than `suggestions` at the dimension level

The `suggestions` parameter described on this page is applied to a view and works differently than the [`suggestions`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions) parameter applied to a dimension. When applied at the dimension level, [`suggestions`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions) lets you hard-code a list of suggestions for that dimension.

If you want to disable suggestions for an individual dimension, you can use the `suggestable: no` statement for the dimension.

### You can disable suggestions for individual dimensions

If you want to disable suggestions for an individual dimension, you can add the [`suggestable: no`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestable) statement to the dimension's definition instead of using `suggestions: no` for the entire view. The inverse doesn't work, however: you cannot define a view with `suggestions: no` and then use the `suggestable: yes` statement to _enable_ suggestions for individual dimensions in the view. The behavior is set up this way because, if a developer is specifying `suggestions: no` at the view level, the developer wants to prevent expensive queries on the database for that view, so suggestions should be kept off for all dimensions in the view.

As an alternative, for a view with `suggestions: no`, you can use the [`suggestions`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions) parameter for individual dimensions to hard-code possible values for a filter even if the dimension's view has the `suggestions: no` statement, since hard-coded values don't require a query on the database.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
