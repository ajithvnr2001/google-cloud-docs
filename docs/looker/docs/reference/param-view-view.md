---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-view/
title: view \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:29.675072+00:00
---

# view  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  view Stay organized with collections  Save and categorize content based on your preferences. 

## Usage

view: view_name { ... }

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) |  Default Value None Accepts [A Looker identifier](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#scoping_and_naming) Special Rules

  * To be usable, the view must be referenced by an `explore` or `join` parameter
  * View names must be unique within any given model

  
---|---  
  
## Definition

> If there is a plus sign (`+`) in front of the view name, such as `view: +orders`, that is a _refinement_ of a view. See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) documentation page for more information.

The `view` parameter, along with its underlying parameters, describes a table of data that will be used in a Looker model. That table can already exist in your database or you can create a new table using Looker's [derived table](https://docs.cloud.google.com/looker/docs/derived-tables) functionality.

In the case of an existing database table, the name of the view generally matches the name of the table that you want to work with. If you want the view name to be different than the underlying table or if you need to reference a table from a different database or schema, you can add the [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) parameter.

In the case of a derived table, the name of the view can be any [identifier](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#scoping_and_naming). Then references to the derived table use that identifier name.

After you create a view, you must reference that view in an [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) or [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) parameter to make the view available to users.

> When you use a [measure](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count) of `type: count` in an Explore, the visualization labels the resulting values with the view name rather than the word "Count." To avoid confusion, we recommend pluralizing your view name, selecting **Show Full Field Name** under **Series** in the visualization settings, or using a `view_label` with a pluralized version of your view name.

## Examples

Make the `orders` table in your database available for modeling:
    
    
    view: orders {}
    

Create a [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) named `user_facts`:
    
    
    view: user_facts {
      derived_table: {
        sql: … ;;
      }
    }
    

Make the `order_1` table in your database available for modeling, but use the [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) parameter to call it `orders`:
    
    
    view: orders {
      sql_table_name: order_1 ;;
    }
    

Use the [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) parameter to make the `users` table from your `analytics` schema available for modeling:
    
    
    view: users {
      sql_table_name: analytics.user ;;
    }
    

## Common challenges

### A view is not accessible by users until added using `explore` or `join`

Creating a view will not do anything in and of itself. In order for users to be able to interact with it the view must be referenced by an [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) or [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) parameter.

### Two views must be referred to by different names within an Explore

Within any given Explore, a view can be used more than once, but each view must have a unique reference. If you need to join a view to an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) more than once, you need to use the [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-from) parameter in your join.

### Tables referenced by `view` must be accessible from the current connection

Views are referenced by an [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) or [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) parameter, which in turn is referenced by a [model](https://docs.cloud.google.com/looker/docs/reference/param-model). The model determines which database connection is used (see the [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) parameter). Database connections themselves are defined in the **Admin** section of Looker, and they have a default schema associated with them.

When you reference a table in the `view` parameter, the table needs to be accessible within the associated connection. Additionally, if you need to reference a table from the non-default schema, you'll need to make use of the [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) parameter to provide the non-default schema name.

## Things to know

### `view` usually contains dimensions and measures

Although `view` could theoretically be used all by itself, in practice, it almost always has dimensions and measures nested underneath it. Dimensions provide access to the columns of the database table, while measures allow aggregation of columns.

Dimensions are described on the [Dimension, filter, and parameter types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types) documentation page, while measures are described on the [Measure types](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) documentation page. In addition, you can define [filter fields](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) and groups of date-based dimension fields using [dimension groups](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
