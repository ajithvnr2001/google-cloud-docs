---
url: https://docs.cloud.google.com/looker/docs/reference/param-join/
title: Join parameters \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:24.631802+00:00
---

# Join parameters  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-join/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  Join parameters Stay organized with collections  Save and categorize content based on your preferences. 

This page links to all the LookML parameters that are children of the `join` parameter. You can learn more about using joins on the [Working with joins in LookML](https://docs.cloud.google.com/looker/docs/working-with-joins) documentation page.

A join is what allows multiple [views](https://docs.cloud.google.com/looker/docs/reference/param-view) to be added to a single [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore), allowing users to access and compare fields from various views at the same time. You declare the Explore and any desired `join` parameters in a [model file](https://docs.cloud.google.com/looker/docs/reference/param-model).

## Example usage

Hover over a parameter name to see a quick description; click it to jump to that page. When a parameter can be set to one of several specific options, the default value is listed first.
    
    
    ## STRUCTURAL PARAMETERS
    [explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore "Exposes a view in the Explore menu"): explore_name {
      # Desired Explore parameters (described on [Explore Parameters](https://docs.cloud.google.com/looker/docs/reference/param-explore) page)
    
      [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join "Joins an additional view to an Explore"): join_name  {
    
        # DISPLAY PARAMETERS
        [view_label](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-view-label "Changes the way the join's view name appears in the field picker"): "desired label for the view"
    
        # JOIN PARAMETERS
        [fields](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-fields "Determines which fields from a join are brought into an explore"): [field_or_set, field_or_set, ...]
        [foreign_key](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key "Specifies a relationship between an explore and a join using the joined view's primary key"): dimension_name
        [from](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-from "Specifies the view on which a join will be based"): view_name
        [outer_only](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-outer-only "Specifies whether all queries must use an outer join"): no | yes
        [relationship](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship "Declares a join as having a one-to-one, many-to-one, one-to-many, or many-to-many relationship"): many_to_one | many_to_many | one_to_many | one_to_one 
        [required_joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-joins "Specifies which joins should be applied to an explore when fields from a certain join are chosen"): [view_name, view_name, ...]
        [sql_on](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on "Specifies a relationship between an explore and a join by writing a SQL ON clause"): SQL ON clause ;;
        [sql_table_name](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name "Specifies the database table on which a join will be based"): table_name ;;
        [type](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type "Declares a join as being a left, full, inner, or cross type"): left_outer | cross | full_outer | inner 
    
        # QUERY PARAMETERS
        [required_access_grants](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-access-grants "Specifies which access grants are required for a user to access this join"): [access_grant_name, access_grant_name, ...]
        [sql_where](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-where "If this join is included, inserts conditions into the query's WHERE clause that a user cannot change or remove for this explore \(BigQuery only\)"): SQL WHERE condition ;;
      }
      # Possibly more join declarations
    }
    

## Parameter definitions

Parameter Name | Description  
---|---  
Structural Parameters  
[`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) | Joins an additional view to an Explore  
Display Parameters  
[`view_label` (for join)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-view-label) | Changes the way the join's view name appears in the field picker  
Join Parameters  
[`fields` (for join)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-fields) | Determines which fields from a join are brought into an Explore  
[`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) | Specifies a relationship between an Explore and a join using the joined view's primary key  
[`from` (for join)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-from) | Specifies the view on which a join will be based  
[`outer_only`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-outer-only) | Specifies whether all queries must use an outer join  
[`relationship`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship) | Declares a join as having a one-to-one, many-to-one, one-to-many, or many-to-many relationship  
[`required_joins`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-joins) | Specifies which joins should be applied to an Explore when fields from a certain join are chosen  
[`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on) | Specifies a relationship between an Explore and a join by writing a SQL `ON` clause  
[`sql_table_name` (for join)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name) | Specifies the database table on which a join will be based  
[`type` (for join)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type) | Declares a join as being a left, a full, an inner, or a cross type  
Query Parameters  
[`required_access_grants` (for join)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-access-grants) | Limits access to the join to only users whose user attribute values match the access grants  
[`sql_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-where) | If this join is included in the query, inserts conditions into the query's `WHERE` clause that a user cannot change or remove for this Explore. (For BigQuery only)  
Parameters to Avoid  
[`sql` (for join)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql) |  Avoid 3.10  Replaced by a combination of [`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on), [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key), [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type), and/or [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name), as described [here](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql#definition)  
[`sql_foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-foreign-key) |  Avoid 3.16  Replaced by [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key)  
  
> **Note:** The [`always_join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join) parameter specifies any joins that must always be applied to an Explore. That parameter is defined in an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore), so it is listed on the [`explore` parameter](https://docs.cloud.google.com/looker/docs/reference/param-explore) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
