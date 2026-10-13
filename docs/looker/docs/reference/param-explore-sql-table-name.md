---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-table-name/
title: sql_table_name (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:23.812735+00:00
---

# sql_table_name (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-table-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_table_name (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `sql_table_name` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `sql_table_name` can also be used as part of a view, described on the [`sql_table_name` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) parameter documentation page.
> 
> `sql_table_name` can also be used as part of a join, described on the [`sql_table_name` (for joins)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      sql_table_name: table_name ;;
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `sql_table_name` |  Default Value The database table on which the Explore's view is based Accepts The name of a database table Special Rules

  * `sql_table_name` for Explores should be used only when the same view can describe multiple tables on your database. 
  * The table referenced by `sql_table_name` must be accessible within the database connection of its model.
  * If the table is in a different database, schema, project, or dataset than the default path you defined in your database connection, you must scope the table name.

  
---|---  
  
## Definition

The `sql_table_name` parameter specifies the table in your database that will be queried by the [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore). Typically the view for which an Explore is named defines the table that will be queried. However, in cases where multiple tables have the same structure, you can use the `sql_table_name` parameter under the `explore` parameter to override the base table that is specified in the view file. In this way you can take the dimensions and measures that you have defined in the view file and apply them to database tables other than the table that is specified in the view file.

### Scoping table names

When you reference a table by using the table name alone, Looker will use the default search path (the database and schema) that your Looker admin has configured in the settings for the database connection. See the Things to consider section of this page for more information.

If you need to reference a table in a different database and schema that is not in the database user's default search path, you can scope the table name by using the `<database_name>.<schema_name>.<table_name>` format to point to another database or schema:

  * To reference a table from a different schema, use `<schema_name>.<table_name>`, as shown in the example on this page.
  * To reference a table from a different database, use the full `<database_name>.<schema_name>.<table_name>`.



For a Google BigQuery connection, you can reference a table in a different project and dataset by scoping the table name with the format `<project_name>.<dataset_name>.<table_name>`. See the [Google BigQuery connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) documentation page for additional information.

## Examples

This example makes the `customers` Explore rely on the `customer_1` table from the default database/schema:
    
    
    explore: customers {
      sql_table_name: customer_1 ;;
    }
    

This example makes the `customers` Explore rely on the `customer_1` table from the `analytics` schema by scoping the table name to include the schema name (using the format `<schema_name>.<table_name>`):
    
    
    explore: customers {
      sql_table_name: analytics.customer_1 ;;
    }
    

**Note:** For a Google BigQuery connection, you can fully scope the table name with the format `<project_name>.<dataset_name>.<table_name>`. See the [Google BigQuery connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) documentation page for more information.

## Things to consider

### Tables referenced by `sql_table_name` must be accessible from the current connection

When the `sql_table_name` parameter is used within an [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) object, that `explore` object is in turn included in a [model](https://docs.cloud.google.com/looker/docs/reference/param-model) object. (The Hierarchy on this page shows this relationship chain.) The model object has a database [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) defined in it. When you reference a database table in the `sql_table_name` parameter, the table needs to be accessible within the associated connection specified in the model file.

The default [database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#database) and [schema](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#schema) (or, for Google BigQuery, the [billing project](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) and [dataset](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#dataset)) are defined by your Looker admin when they [create the Looker connection to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db).

### To name a `view` differently than the underlying table, apply `sql_table_name` at the `view` level

Using `sql_table_name` at the [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) level, as described on this page, is not very common. It should only be used when the same [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view) can describe multiple tables.

The more typical method is to use [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) at the [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view) level when you want to name a view differently than the underlying table name.

In other words, instead of this:

_Model File_
    
    
    explore: customers {
      sql_table_name: customer_1 ;;
    }
    

Do this:

_Model File_
    
    
    explore: customers { ... }
    

_View File_
    
    
    view: customers {
      sql_table_name: customer_1 ;;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
