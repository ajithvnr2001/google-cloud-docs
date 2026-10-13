---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name/
title: sql_table_name (for views) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:28.567641+00:00
---

# sql_table_name (for views)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_table_name (for views) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `sql_table_name` parameter that is part of a [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view).
> 
> `sql_table_name` can also be used as part of a join, described on the [`sql_table_name` (for joins)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name) parameter documentation page.
> 
> `sql_table_name` can also be used as part of an Explore, described on the [`sql_table_name` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-table-name) parameter documentation page.

## Usage
    
    
    view: view_name {
      sql_table_name: table_name ;;
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `sql_table_name` |  Default Value The name of the view Accepts A table name in your database Special Rules

  * The table referenced by `sql_table_name` must be accessible within the database connection of its model.
  * If the table is in a different database, schema, project, or dataset than the default path you defined in your database connection, you must scope the table name.

  
---|---  
  
## Definition

The `sql_table_name` parameter specifies the table in your database that will be queried by a [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view).

> If you want to create a view based on a derived table, don't use the `sql_table_name` parameter. Instead use the `derived table` parameter, described on the [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) documentation page. The Looker IDE will return an error if you have both `sql_table_name` and `derived_table` in a view file.

If a view does not contain either the `sql_table_name` or the `derived_table` parameter, Looker assumes that the view is based on a database table, and that the name of the database table matches the name of the [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view). In other words, this:
    
    
    view: my_name { ... }
    

is logically equivalent to this:
    
    
    view: my_name {
      sql_table_name: my_name ;;
    }
    

It is quite common to fall back on this default behavior, and not use `sql_table_name`. However, there are some major situations where it can be useful. First, in some cases you'll want the view to have a different name than the underlying table, such as to clean up a messy table name:
    
    
    view: orders {
      sql_table_name: prod_orders_2 ;;
    }
    

Additionally, there are cases when a view needs to be based on a database or schema that is not in the database user's default search path. You can then scope the table name, using the format `<schema_name>.<table_name>`, like this:
    
    
    view: desired_view_name {
      sql_table_name: database_name.schema_name.table_name ;;
    }
    

### Scoping table names

When you reference a table using the table name alone, Looker will use the default search path (the database and schema) that your Looker admin has configured in the connection settings for the database connection. See the Things to consider section on this page for more information.

If you need to reference a table in a different database and schema that is not in the database user's default search path, you can scope the table name using the `<database_name>.<schema_name>.<table_name>` format to point to another database or schema:

  * To reference a table from a different schema, use `<schema_name>.<table_name>`, as shown in the example on this page.
  * To reference a table from a different database, use the full `<database_name>.<schema_name>.<table_name>`.



For a Google BigQuery connection, you can reference a table in a different project and dataset by scoping the table name using the format `<project_name>.<dataset_name>.<table_name>`. See the [Google BigQuery connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) documentation page for additional information.

### Federated joins

Joining two tables from different databases is called a federated join. Federated joins can be performed using Looker if the two databases are on the same SQL dialect, the dialect supports federated joins, and the two databases are both accessible from the same connection in Looker. Depending on your database configuration, the tables may also need to reside on the same physical machine.

Under those conditions, you can create a federated join by specifying the database name of each table in the `sql_table_name` parameter for that view:
    
    
    view: view_1 {
      sql_table_name: database_name.table_1 ;;
    }
    
    view: view_2 {
      sql_table_name: another_database_name.table_2 ;;
    }
    

Then join these views using the `sql_on` parameter:
    
    
    explore: view_1 {
      join: view_2 {
        sql_on: ${view_1.view_1_ID} = ${view_2.view_2_ID} ;;
      }
    }
    

If you want to join databases that are in different SQL dialects, we recommend replicating one database into the other so that you can pull all data from a single source.

**Note:** If you want to join across two MySQL databases on separate machines, you can perform a federated join across both database connections by creating a `FEDERATED` table using `CONNECTION`. Essentially, you establish a connection to tables on a different server entirely in your MySQL database. See this [MySQL documentation](http://dev.mysql.com/doc/refman/5.5/en/federated-create-connection.html) to learn more.

## Examples

This example makes the `customers` view rely on the `customer_1` table from the default schema:
    
    
    view: customers {
      sql_table_name: customer_1 ;;
    }
    

This example makes the `customers` view rely on the `customer_1` table from the `analytics` by scoping the table name to include the schema name (using the format `<schema_name>.<table_name>`):
    
    
    view: customers {
      sql_table_name: analytics.customer_1 ;;
    }
    

## Things to consider

### Tables referenced by `view` must be accessible from the current connection

When the `sql_table_name` parameter is used within a [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) object, that `view` object can be referenced in an [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) object, which is in turn referenced in a [model](https://docs.cloud.google.com/looker/docs/reference/param-model) object. The model object has a database [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) defined in it. When you reference a database table in the `sql_table_name` parameter, the table needs to be accessible within the associated connection specified in the model file.

The default [database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#database) and [schema](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#schema) (or, for Google BigQuery, the [billing project](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) and [dataset](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#dataset)) are defined by your Looker admin when they [create the Looker connection to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db).

### Unfriendly table names may require additional formatting

Some dialects require that table names that have unsupported characters, also known as "unfriendly" table names, be enclosed in square brackets, double quotes, or single quotes. For example, the table name `Customers.PaymentInfo` includes a period in the table name, which could be interpreted as a table called `PaymentInfo` in the schema `Customers`. To correct this, if your dialect requires square brackets, you can enclose the table name in square brackets, as follows:
    
    
    sql_table_name: [Customers.PaymentInfo] ;;
    

If your dialect requires double quotes or single quotes, you would replace the square brackets for those characters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
