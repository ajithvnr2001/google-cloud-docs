---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name/
title: sql_table_name (for joins) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:25.780410+00:00
---

# sql_table_name (for joins)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_table_name (for joins) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `sql_table_name` parameter that is part of a [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join).
> 
> `sql_table_name` can also be used as part of a view, described on the [`sql_table_name` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) parameter documentation page.
> 
> `sql_table_name` can also be used as part of an Explore, described on the [`sql_table_name` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-table-name) parameter documentation page.

## Usage
    
    
    explore: view_name {
      join: view_name {
        sql_table_name: table_name ;;
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) `sql_table_name` |  Default Value None Accepts A table name in your database Special Rules

  * The table referenced by `sql_table_name` must be accessible within the database connection of its model.
  * If the table is in a different database, schema, project, or dataset than the default path you defined in your database connection, you must scope the table name.

  
---|---  
  
## Definition

Typically the view on which a [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) is based defines the table to be queried.

You can use `sql_table_name` to set the table in your database to be queried by a [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join). This is unusual, but it can be useful when multiple tables have the same schema; it allows the same view to be used to describe all of them. `sql_table_name` lets you specify which tables should be used by the view that you are joining. In such situations, consider using [`extends`](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends) or [refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements).

### Scoping table names

When you reference a table using the table name alone, Looker will use the default search path (the database and schema) that your Looker admin has configured in the settings for the database connection. See the Things to consider section of this page for more information.

If you need to reference a table in a different database and schema that is not in the database user's default search path, you can scope the table name using the `<database_name>.<schema_name>.<table_name>` format to point to another database or schema:

  * To reference a table from a different schema, use `<schema_name>.<table_name>`, as shown in the example on this page.
  * To reference a table from a different database, use the full `<database_name>.<schema_name>.<table_name>`.



For a Google BigQuery connection, you can reference a table in a different project and dataset by scoping the table name using the format `<project_name>.<dataset_name>.<table_name>`. See the Google [BigQuery connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) documentation page for additional information.

**Notes:**

  * Joins across databases require that the two databases be in the same SQL dialect and that the two databases both be accessible from the same connection in Looker (see the Things to consider section on this page).
  * Depending on your database configuration and dialect, the tables joined across databases may also need to reside on the same physical machine. See the [Federated joins](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name#federated_joins) section on the [`sql_table_name` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) documentation page.



## Examples

This example makes the `customers` join rely on the `customer_1` table from the default schema:
    
    
    explore: orders {
      join: customers {
        sql_table_name: customer_1 ;;
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

This example makes the `customers` join rely on the `customer_1` table from the `analytics` schema by scoping the table name to include the schema name (using the format `<schema_name>.<table_name>`):
    
    
    explore: orders {
      join: customers {
        sql_table_name: analytics.customer_1 ;;
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

## Things to consider

### Tables referenced by `sql_table_name` must be accessible from the current connection

When the `sql_table_name` parameter is used within a [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) object, that `join` object is defined within an [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) object, which is in turn included in a [model](https://docs.cloud.google.com/looker/docs/reference/param-model) object. (The Hierarchy on this page shows this relationship chain.) The model object has a database [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) defined in it. When you reference a database table in the `sql_table_name` parameter, the table needs to be accessible within the associated connection specified in the model file.

The default [database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#database) and [schema](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#schema) (or, for Google BigQuery, the [billing project](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) and [dataset](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#dataset)) are defined by your Looker admin when they [create the Looker connection to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db).

### To name a `join` differently than the underlying table, apply `sql_table_name` at the view level

Using `sql_table_name` at the [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) level, as described on this page, is uncommon. It should only be used when the same [view](https://docs.cloud.google.com/looker/docs/reference/param-view) can describe multiple tables.

The more typical method is to use [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) at the [view](https://docs.cloud.google.com/looker/docs/reference/param-view) level to name a view differently than the underlying table name.

Instead of this:

_Model File_
    
    
    explore: orders {
      join: customers {
        sql_table_name: customer_1 ;;
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }}
    

do this:

_Model File_
    
    
    explore: orders {
      join: customers {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

_View File_
    
    
    view: customers {
      sql_table_name: customer_1 ;;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
