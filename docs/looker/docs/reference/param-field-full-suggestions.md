---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-full-suggestions/
title: full_suggestions \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:36.207695+00:00
---

# full_suggestions  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-full-suggestions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  full_suggestions Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        full_suggestions: yes 
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `full_suggestions` |  Possible Field Types Dimension, Dimension Group, Filter, Parameter Accepts A Boolean (yes or no)  
---|---  
  
## Definition

When a user [filters an Explore](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) on a [field type that supports suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions#fields_that_support_suggestions), by default Looker will suggest possible values for the field (see the [Changing filter suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions) documentation page for information about how you can affect filter suggestions). To provide suggestions for a filter field, Looker executes a query on your database to retrieve a list of distinct values for the field. Looker typically generates these suggestions by executing a query such as the following on the filter field:
    
    
    SELECT DISTINCT field_name FROM table
    WHERE (field_name LIKE '%' OR field_name LIKE '% %')
    GROUP BY 1 ORDER BY 1 LIMIT 1000
    

The `full_suggestions` parameter controls how Looker queries your database to provide suggestions for the field's values in the filter of an Explore:

  * `full_suggestions: no`: Looker will use its typical filter suggestion query, and will query only the view that contains the filter field.
  * `full_suggestions: yes`: Looker will add the Explore logic to its filter suggestion query, meaning that Looker will include any of the Explore's joins that are required to query the filter's field, and Looker will include the logic from the Explore's parameters, including the following parameters:

    * [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where)
    * [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter)
    * [`always_join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join)
    * [`conditionally_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter)
**Notes:**
    * The suggestions presented to a user for a [`case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) dimension will **not** be restricted when the dimension is defined with `full_suggestions:yes`. Any option that you include in a `case` parameter will be visible to all users.
    * The [`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) parameter is not applied to filter suggestion queries.



## Default behavior

If the `full_suggestions` parameter is not specified for a field, Looker queries for suggestion values with the following behavior:

  * For Explores that use [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) or [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter), or [`always_join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join), Looker defaults to the `full_suggestions: yes` behavior. Because the `access_filter`, `sql_always_where`, and `always_join` parameters apply constraints to Explore queries, these same constraints are applied to the filter suggestion queries. See Considerations for Explores with `sql_always_where` or `access_filter` for additional information about how Looker provides suggestions for Explores with query constraints.
  * Otherwise, Looker defaults to the `full_suggestions: no` behavior, querying just the filter field's view, and without including any of the Explore's logic. The `full_suggestions: no` setting makes filter suggestions more performant, since Looker queries a single table without any joins, without using any of the logic defined in the Explore.



## Example

To prompt Looker to use the Explore's logic to query your database when providing filter suggestions for a dimension, add `full_suggestions: yes` to the dimension's definition:
    
    
    dimension: project_name {
      type: string
      sql: ${TABLE}.project_name ;;
      full_suggestions: yes
    }
    

## Considerations for Explores with `sql_always_where` or `access_filter`

The `sql_always_where` and `access_filter` parameters are often used to control data access. Whenever `sql_always_where` or `access_filter` are used on an Explore, Looker applies those restrictions to the filter suggestions it makes for [field types that support suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions#fields_that_support_suggestions). To prevent users from seeing a filter suggestion that does not apply to them, Looker requires that the Explore logic (`full_suggestions:yes`) is applied to the filter value suggestions in the Explore. Therefore, if an Explore is defined with `sql_always_where` or `access_filter`, Looker won't provide any suggestions for a filter on a field defined with `full_suggestions:no`.

If you have an Explore with `sql_always_where` or `access_filter`, and you have a field that you know does not require the `sql_always_where` or `access_filter` logic, you can override the behavior by adding [`bypass_suggest_restrictions:yes`](https://docs.cloud.google.com/looker/docs/reference/param-field-bypass-suggest-restrictions) to the field's definition. The `bypass_suggest_restrictions:yes` statement prompts Looker to provide the full list of filter value suggestions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
