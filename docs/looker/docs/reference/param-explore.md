---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore/
title: Explore parameters \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:19.807115+00:00
---

# Explore parameters  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  Explore parameters Stay organized with collections  Save and categorize content based on your preferences. 

This page links to all the LookML parameters that are children of the `explore` parameter.

An Explore serves as the starting point for a query in the Looker application. Explores reference [views](https://docs.cloud.google.com/looker/docs/reference/param-view) and each Explore can contain [joins](https://docs.cloud.google.com/looker/docs/reference/param-join) to other views. Explores should typically be declared in a [model file](https://docs.cloud.google.com/looker/docs/reference/param-model).

## Example usage

_Hover over a parameter name to see a quick description; click it to jump to that page. When a parameter can be set to one of several specific options, the default value is listed first._
    
    
    ## STRUCTURAL PARAMETERS
    
    [explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore "Exposes a view in the Explore menu"): explore_name {
      [extension](https://docs.cloud.google.com/looker/docs/reference/param-explore-extension "Specifies that the Explore requires extension"): required
      [extends](https://docs.cloud.google.com/looker/docs/reference/param-explore-extends "Specifies Explore\(s\) that will be extended by this view"): [explore_name,  explore_name, ...]
      [fields](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields "Limits the fields available in an Explore from its base view and through the Explore's joins"): [field_or_set, field_or_set, ...]
      [tags](https://docs.cloud.google.com/looker/docs/reference/param-explore-tags "Specifies text that can be passed to other applications"): ["string1", "string2", ...]
    
      # DISPLAY PARAMETERS
      [description](https://docs.cloud.google.com/looker/docs/reference/param-explore-description "Adds a description for an Explore that appears to users in the UI"): "Description I want"
      [group_label](https://docs.cloud.google.com/looker/docs/reference/param-explore-group-label "Creates a group label to display as a heading in the Explore menu"): "Label to use as a heading in the Explore menu"
      [hidden](https://docs.cloud.google.com/looker/docs/reference/param-explore-hidden "Hides an Explore from the Explore menu"): yes | no
      [label](https://docs.cloud.google.com/looker/docs/reference/param-explore-label "Changes the way an Explore appears in the Explore menu"): "desired label"
      [query](https://docs.cloud.google.com/looker/docs/reference/param-explore-query "Defines queries for Explore Quick Start"):  {
          # Desired query parameters (described on the [query](https://docs.cloud.google.com/looker/docs/reference/param-explore-query) page)      }
      [view_label](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label "Specifies how a group of fields from the Explore's base view will be labeled in the field picker"): "Field picker heading I want for the Explore's fields"
    
      # FILTER PARAMETERS
    
      [access_filter](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter "Adds user-specific filters to an Explore"): {
        [field](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter "See access_filter page for more detail"): fully_scoped_field
        [user_attribute](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter "See access_filter page for more detail"): user_attribute_name
      }
    
      # Possibly more access_filter declarations
    
      [always_filter](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter "Adds filters a user can change, but not remove, to an Explore"): {
        [filters](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter "See always_filter page for more detail"): [field_name: "filter expression", field_name: "filter expression", ...]
      }
      [case_sensitive](https://docs.cloud.google.com/looker/docs/reference/param-explore-case-sensitive "Specifies whether filters are case-sensitive for an Explore"): yes | no
      [conditionally_filter](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter "Adds filters to an Explore if a user does not add their own filter from a specific list"): {
        [filters](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter "See conditionally_filter page for more detail"): [field_name: "filter expression", field_name: "filter expression", ...]
        [unless](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter "See conditionally_filter page for more detail"): [field_name, field_name, ...]
      }
      [sql_always_having](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-having "Inserts conditions into the query's HAVING clause that a user cannot change or remove for this Explore"): SQL HAVING condition ;;
      [sql_always_where](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where "Inserts conditions into the query's WHERE clause that a user cannot change or remove for this Explore"): SQL WHERE condition ;;
    
      # JOIN PARAMETERS
    
      [always_join](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join "Specifies which joins must always be applied to an Explore"): [view_name, view_name, ...]
      [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join "Joins an additional view to an Explore"): view_name {
        # Desired join parameters (described on [Join Parameters](https://docs.cloud.google.com/looker/docs/reference/param-join) page)
      }
      # Possibly more join declarations
    
      # QUERY PARAMETERS
    
      [autogenerate_primary_keys](https://docs.cloud.google.com/looker/docs/reference/param-explore-autogenerate-primary-keys "Enables or disables automatic primary key generation"): yes | no
      [cancel_grouping_fields](https://docs.cloud.google.com/looker/docs/reference/param-explore-cancel-grouping-fields " Cancels the GROUP BY clause when certain fields are chosen in an Explore"): [fully_scoped_field, fully_scoped_field, ...]
      [from](https://docs.cloud.google.com/looker/docs/reference/param-explore-from "Specifies the view on which an Explore will be based, and reference the fields of that view by the Explore's name"): view_name
      [persist_for](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-for "Changes the cache settings for an Explore"): "N (seconds | minutes | hours)"
      [persist_with](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-with "Specifies the datagroup to use for the Explore's caching policy"): datagroup_name
      [required_access_grants](https://docs.cloud.google.com/looker/docs/reference/param-explore-required-access-grants "Specifies which access grants are required for a user to access this Explore"): [access_grant_name, access_grant_name, ...]
      [sql_table_name](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-table-name "Specifies the database table on which an Explore will be based"): table_name ;;
      [sql_analytic_model_name](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-analytic-model-name "Specifies the in-database analytic model on which an Explore is based"): analytic_model_name ;;
      [sql_preamble](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-preamble "Specifies a SQL statement that executes before queries in the Explore are run"): SQL STATEMENT  ;;
      [symmetric_aggregates](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates "Specifies whether symmetric aggregates are enabled for an Explore"): yes | no
      [view_name](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-name "Specifies the view on which an Explore will be based, and references the fields of that view by the view's name"): view_name
    
      # AGGREGATE TABLE PARAMETERS
    
      [aggregate_table](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table " Creates an aggregate table in order to use aggregate awareness for queries on the Explore"): table_name {
        [query](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#query "Defines the query for the aggregate table"):  {
          # Desired query parameters (described on the [aggregate_table](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#query) page)
        }
        [materialization](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization "Specifies the persistence strategy for the aggregate table"):  {
          # Desired materialization parameters (described on the [aggregate_table](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) page)
        }
      }
      # Possibly more aggregate_table declarations
    }
    
    ## REFINEMENT PARAMETERS
    
    explore: [+explore_name](https://docs.cloud.google.com/looker/docs/lookml-refinements "Adds a refinement to an existing Explore") {
      [final](https://docs.cloud.google.com/looker/docs/lookml-refinements#final "Indicates that this is the final refinement allowed for the Explore"): yes
    }
    

## Parameter definitions

Parameter Name | Description  
---|---  
Structural Parameters  
[`extends` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-extends) | Specifies Explore(s) that will be extended by this Explore  
[`extension` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-extension) | Specifies that the Explore requires extension and cannot itself be exposed to users  
[`explore` (for model)](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) | Exposes a view in the Explore menu  
[`fields` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields) | Limits the fields available in an Explore from its base view and through the Explore's joins  
[`tags` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-tags) | Specifies text that can be passed to other applications  
Display Parameters  
[`description` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-description) | Adds a description for an Explore that appears to users in the UI  
[`group_label` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-group-label) | Creates a group label to use as a heading in the Explore menu  
[`hidden` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-hidden) | Hides an Explore from the Explore menu  
[`label` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-label) | Changes the way an Explore appears in the Explore menu  
[`query` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-query) | Creates a predefined query for users to select in an Explore's Quick Start menu.  
[`view_label` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label) | Specifies how a group of fields from the Explore's base view will be labeled in the field picker  
Filter Parameters  
[`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter) | Adds user-specific filters to an Explore  
[`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) | Adds filters a user can change, but not remove, to an Explore  
[`case_sensitive` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-case-sensitive) | Specifies whether filters are case-sensitive for an Explore  
[`conditionally_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter) | Adds filters to an Explore if a user does not add their own filter from a specific list  
[`sql_always_having`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-having) | Inserts conditions into the query's `HAVING` clause that a user cannot change or remove for this Explore  
[`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) | Inserts conditions into the query's `WHERE` clause that a user cannot change or remove for this Explore  
Join Parameters  
[`always_join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join) | Specifies which joins must always be applied to an Explore  
[`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) | Joins an additional view to an Explore. For more information about joins and their parameters, see the [Join Parameters](https://docs.cloud.google.com/looker/docs/reference/param-join) reference page.   
Query Parameters  
[`autogenerate_primary_keys` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-autogenerate-primary-keys) | Enables or disables automatic primary key generation  
[`cancel_grouping_fields`](https://docs.cloud.google.com/looker/docs/reference/param-explore-cancel-grouping-fields) | Cancels the `GROUP BY` clause when certain fields are chosen in an Explore  
[`from` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-from) | Specifies the view on which an Explore will be based, and reference the fields of that view by the Explore's name  
[`persist_for` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-for) | Changes the cache settings for an Explore  
[`persist_with` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-with) | Specifies the datagroup to use for the Explore's caching policy  
[`required_access_grants` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-required-access-grants) | Limits access to the Explore to only users whose user attribute values match the access grants  
[`sql_table_name` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-table-name) | Specifies the database table on which an Explore will be based  
[`sql_analytic_model_name` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-analytic-model-name) | Specifies the in-database analytic model on which an Explore will be based  
[`symmetric_aggregates`](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates) |  Specifies whether symmetric aggregates are enabled for an Explore   
[`view_name` (for Explore)](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-name) | Specifies the view on which an Explore will be based, and references the fields of that view by the view's name  
Aggregate Table Parameters  
[`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) | Creates an aggregate table in order to use aggregate awareness for queries on the Explore. For information on the `aggregate_table` parameter, see the [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) parameter page. For an overview of aggregate awareness, see the [Aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness) documentation page.   
[`query`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#query) | Defines the query for the aggregate table. For information on `query` and its subparameters, see the [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#query) parameter page.   
[`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) | Defines the persistence strategy for the aggregate table. For information on `materialization` and its subparameters, see the [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) parameter page.   
Refinement Parameters  
[`explore: +explore_name`](https://docs.cloud.google.com/looker/docs/lookml-refinements) | Adds a plus sign (`+`) in front of an existing Explore name to add a refinement to the existing Explore. See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) documentation page for more information and use cases.  
[`final`](https://docs.cloud.google.com/looker/docs/lookml-refinements#final) | Indicates that the current refinement is the final refinement allowed for the Explore. See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements#final) documentation page for more information and use cases.  
Parameters to Avoid  
`access_filter_fields` |  Removed 6.0  Replaced by [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
