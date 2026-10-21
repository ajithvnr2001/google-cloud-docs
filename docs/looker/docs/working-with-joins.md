---
url: https://docs.cloud.google.com/looker/docs/working-with-joins/
title: Working with joins in LookML \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:45.184583+00:00
---

# Working with joins in LookML  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/working-with-joins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Working with joins in LookML Stay organized with collections  Save and categorize content based on your preferences. 

Joins let you connect different [views](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#view) so that you can explore data from more than one view at the same time and see how different parts of your data relate to each other.

For example, your database might include the tables `order_items`, `orders`, and `users`. You can use joins to explore data from all tables at the same time. This page explains joins in LookML, including specific join parameters and joining patterns.

## Joins start with an Explore

Joins are defined in the [model file](https://docs.cloud.google.com/looker/docs/lookml-project-files#model-file) to establish the relationship between an [Explore](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#explore) and a [view](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#view). Joins connect one or more views to a single Explore, either directly or through another joined view.

Consider two database tables: `order_items` and `orders`. After you generate views for both tables, declare one or more of them under the `explore` parameter in the model file:
    
    
    explore: order_items { ... }
    

When you run a query from the `order_items` Explore, `order_items` appears in the `FROM` clause of the generated SQL:
    
    
    SELECT ...
    FROM order_items
    

You can join additional information to the `order_items` Explore. For example, you can use the following sample LookML to join the `orders` view to the `order_items` Explore:
    
    
    explore: order_items {
      join: orders {
        type: left_outer
        relationship: many_to_one
        sql_on: ${order_items.order_id} = ${orders.id} ;;
      }
    }
    

The LookML shown previously accomplishes two things. First, you can see fields from both `orders` and `order_items` in the [Explore field picker](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#field_picker):

![The Order Items Explore includes the fields from the Order Items view and the fields from the joined Orders view.](https://docs.cloud.google.com/static/looker/docs/images/develop-order-items-explore-v44-or-v48-v2-2206.png)

Second, the LookML describes how to join `orders` and `order_items` together. That LookML would translate to the following SQL:
    
    
    SELECT ...
    FROM order_items
    LEFT JOIN orders
    ON order_items.order_id = orders.id
    

These LookML parameters are described in greater detail in the following sections.

**Chat Team Tip:** Users ask most about the validation error, "Unknown or inaccessible field," which can be caused by a missing join. See [Error: Unknown or inaccessible field](https://docs.cloud.google.com/looker/docs/best-practices/error-unknown-or-inaccessible-field) for more information.

## Join parameters

Four main parameters are used to join: [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join), [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type), [`relationship`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship), and [`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on).

### Step 1: Starting the Explore

First, create the `order_items` Explore:
    
    
    explore: order_items { ... }
    

### Step 2: `join`

To join a table, you must first [declare the table in a view](https://docs.cloud.google.com/looker/docs/lookml-project-files#view_files). In this example, assume that the `orders` is an existing view in your model.

Then, use the `join` parameter to declare that you want to join the `orders` view to the `order_items` Explore:
    
    
    explore: order_items {
      join: orders { ... }
    }
    

### Step 3: `type`

Consider which type of join to perform. Looker supports `LEFT JOIN`, `INNER JOIN`, `FULL OUTER JOIN`, and `CROSS JOIN`. These correspond to the `type` parameter values of `left_outer`, `inner`, `full_outer`, and `cross`.
    
    
    explore: order_items {
      join: orders {
        type: left_outer
      }
    }
    

The default value of `type` is `left_outer`.

### Step 4: `relationship`

Define a join relationship between the `order_items` Explore and the `orders` view. Properly declaring the relationship of a join is important for Looker to calculate accurate measures. The relationship is defined _from_ the `order_items` Explore _to_ the `orders` view. The possible options are `one_to_one`, `many_to_one`, `one_to_many`, and `many_to_many`.

In this example, there can be many order items for a single order. The relationship from the `order_items` Explore to the `orders` view is `many_to_one`:
    
    
    explore: order_items {
      join: orders {
        type: left_outer
        relationship: many_to_one
      }
    }
    

If you don't include a `relationship` parameter in your join, Looker defaults to `many_to_one`.

For additional tips on defining the `relationship` parameter correctly for a join, see [Getting the `relationship` parameter right](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-relationship-parameter-correctly).

### Step 5: `sql_on`

Declare how to join the `order_items` table and the `orders` table together with either the `sql_on` parameter or the [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) parameter.

**Tip:** We usually suggest using the `sql_on` parameter since it can do everything that the `foreign_key` parameter can do, but the `sql_on` parameter is typically easier to understand.

The `sql_on` parameter is equivalent to the `ON` clause in the generated SQL for a query. With this parameter, you can declare which fields should be matched up to perform the join:
    
    
    explore: order_items {
      join: orders {
        type: left_outer
        relationship: many_to_one
        sql_on: ${order_items.order_id} = ${orders.id} ;;
      }
    }
    

You can also write more complex joins. For example, you may want to join only orders with `id` greater than 1000:
    
    
    explore: order_items {
      join: orders {
        type: left_outer
        relationship: many_to_one
        sql_on: ${order_items.order_id} = ${orders.id} AND ${orders.id} > 1000 ;;
      }
    }
    

See the [substitution operators documentation](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#substitution_operator_\($\)) to learn more about the `${ ... }` syntax in these examples.

### Step 6: Testing

Test that this join is functioning as expected by going to the **Order Items** Explore. You should see fields from both `order_items` and `orders`.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-order-items-menu-item-2412.png)

See [Testing the fields in the Explore](https://docs.cloud.google.com/looker/docs/looker-ide#testing_the_fields_in_the_explore) to learn more about testing LookML changes in an Explore.

## Joining through another view

You can join a view to an Explore through another view. In the join parameters example, you joined `orders` to `order_items` using the `order_id` field. We might also want to join the data from a view called `users` to the `order_items` Explore, even though they don't share a common field. This can be done by joining _through_ the `orders` view.

Use the [`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on) parameter or the [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) parameter to join the `users` view to to the `orders` view, instead of to the `order_items` Explore. Do this by correctly scoping the field from `orders` as `orders.user_id`.

Here is an example using the `sql_on` parameter:
    
    
    explore: order_items {
      join: orders {
        type: left_outer
        relationship: many_to_one
        sql_on: ${order_items.order_id} = ${orders.id} ;;
      }
      join: users {
        type: left_outer
        relationship: many_to_one
        sql_on: ${orders.user_id} = ${users.id} ;;
      }
    }
    

## Joining a view more than once

A `users` view contains data for both **buyers** and **sellers**. To join data from this view into `order_items`, but do so separately for buyers and sellers, you can join `users` twice, with different names, using the [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-from) parameter.

The `from` parameter lets you specify which view to use in a join, while giving the join a unique name. For example:
    
    
    explore: order_items {
      join: orders {
        type: left_outer
        relationship: many_to_one
        sql_on: ${order_items.order_id} = ${orders.id} ;;
      }
      join: buyers {
        from: users
        type: left_outer
        relationship: many_to_one
        sql_on: ${orders.buyer_id} = ${buyers.id} ;;
      }
      join: sellers {
        from: users
        type: left_outer
        relationship: many_to_one
        sql_on: ${orders.seller_id} = ${sellers.id} ;;
      }
    }
    

In this case, only **buyer** data is joined as `buyers`, while only **seller** data is joined in as `sellers`.

**Note** : The `users` view must now be referred to by its aliased names `buyers` and `sellers` in the join.

## Limiting fields from a join

The [`fields`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-fields) parameter lets you specify which fields are brought from a join into an Explore. By default, all fields from a view are brought in when joined. However, you might want to bring through only a subset of fields.

For example, when `orders` is joined to `order_items`, you may want to bring only the `shipping` and `tax` fields through the join:
    
    
    explore: order_items {
      join: orders {
        type: left_outer
        relationship: many_to_one
        sql_on: ${order_items.order_id} = ${orders.id} ;;
        fields: [shipping, tax]
      }
    }
    

You can also reference a **set** of fields, such as `[set_a*]`. Each set is defined within a view using the [`set`](https://docs.cloud.google.com/looker/docs/reference/param-view-set) parameter. Suppose you have the following set defined in the `orders` view:
    
    
    set: orders_set {
      fields: [created_date, shipping, tax]
    }
    

You can choose to bring only these three fields through when you join `orders` to `order_items`:
    
    
    explore: order_items {
      join: orders {
        type: left_outer
        relationship: many_to_one
        sql_on: ${order_items.order_id} = ${orders.id} ;;
        fields: [orders_set*]
      }
    }
    

## Symmetric aggregates

Looker uses a feature called "symmetric aggregates" to calculate aggregations (like sums and averages) correctly, even when joins result in a fanout. Symmetric aggregates are described in more detail in [Understanding symmetric aggregates](https://docs.cloud.google.com/looker/docs/best-practices/understanding-symmetric-aggregates). The fanout problem that symmetrid aggregates solve is explained in the [The problem of SQL fanouts](https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220) Community post.

### Primary keys required

To have measures (aggregations) come through joins, you must define primary keys in all views that are involved in the join.

Do this by adding the [`primary_key`](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) parameter to the primary key field definition in each view:
    
    
    dimension: id {
      type: number
      primary_key: yes
    }
    

**Note:** To correctly handle joined measures, Looker relies on you specifying a primary key where the values are completely unique, non-NULL values. If your data does not contain a primary key, consider whether the concatenation of several fields would result in a primary key of completely unique, non-NULL values. If your primary key is not unique or contains NULL values and your query includes data that reveal those issues, then Looker returns an error as described on the [Error: Non-Unique value/primary key (or sql_distinct_key), value overflow or collision when computing sum](https://docs.cloud.google.com/looker/docs/best-practices/error-non-unique-primary-key-computing-sum) Best Practices page.

### Supported SQL dialects

For Looker to support symmetric aggregates in your Looker project, your database dialect must also support them. The following table shows which dialects support symmetric aggregates in the latest release of Looker:

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
If your dialect does not support symmetric aggregates, be careful when executing joins in Looker, as some types of joins can result in inaccurate aggregations (like sums and averages). This problem and the workarounds for it are described in great detail in [The problem of SQL fanouts](https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220) Community post.

## Learn more about joins

To learn more about join parameters in LookML, see the [Join reference](https://docs.cloud.google.com/looker/docs/reference/param-join) documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
