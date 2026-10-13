---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join/
title: join \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:22.916751+00:00
---

# join  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  join Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    
    explore: explore_name {
      join: view_name { ... }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `join` |  Default Value None Accepts The name of an existing view Special Rules

  * This parameter accepts a view name, not the name of the view's underlying table (although they are often identical) 
  * If your dialect does not support [`symmetric_aggregates`](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates) most measure types are excluded from joined views 
  * You can join the same view more than once using [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-from)

  
---|---  
  
## Definition

`join` lets you define the join relationship between an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) and a [view](https://docs.cloud.google.com/looker/docs/reference/param-view), so that you can combine data from multiple views. You can join in as many views as you like for any given Explore.

Recall that each view is associated with a table in your database, or a derived table that you have defined in Looker. Similarly, since an Explore is associated with a view, it is also connected to a table of some kind.

The table associated with the Explore is placed into the `FROM` clause of the SQL that Looker generates. Tables that are associated with joined views are placed into the `JOIN` clause of the SQL that Looker generates.

## Major join parameters

To define the join relationship (the SQL `ON` clause) between an Explore and a view, you'll need use `join` in combination with other parameters.

It is required that you use _either_ the [`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on) _or_ the [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) parameter in order to establish the SQL `ON` clause.

You'll also need to make sure that you are using appropriate join types and relationships, although the [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type) and [`relationship`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship) parameters are not always explicitly required. If their default values of `type: left_outer` and `relationship: many_to_one` are appropriate for your use case, then these parameters can be excluded.

These key parameters, and their relation to the SQL that Looker generates, can be summarized as follows: 

![](https://docs.cloud.google.com/static/looker/docs/images/concept-join-to-sql-diagram-for-new-lookml-40b.png)

  * The `explore` parameter determines the table in the `FROM` clause of the generated SQL query.
  * Each `join` parameter determines a `JOIN` clause of the generated SQL query. 
    * The `type` parameter determines the type of SQL join.
    * The `sql_on` parameter and `foreign_key` parameter determine the `ON` clause of the generated SQL query.



### `sql_on`

[`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on) lets you establish a join relationship by writing the SQL `ON` clause directly. It can accomplish the same joins that [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) can, but it is easier to read and understand.

See the [`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on) parameter documentation page for more information.

### `foreign_key`

[`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) lets you establish a join relationship using the primary key of the joined view, and connecting it with a dimension in the Explore. This pattern is very common in database design, and [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) is an elegant way to express the join in these cases.

For a complete understanding, see the [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) parameter documentation page.

### `type`

Most joins in Looker are `LEFT JOIN` for the reasons discussed in the Don't apply business logic in joins if possible section on this page. Therefore, if you don't explicitly add a [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type), Looker will assume you want a `LEFT JOIN`. However, if you do need another type of join for some reason, you can do so with [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type).

For a complete explanation, see the [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type) parameter documentation page.

### `relationship`

[`relationship`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship) doesn't have a straightforward impact on the SQL that Looker generates, but it is **critical** to the proper functioning of Looker. If you don't explicitly add a [`relationship`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship), Looker will interpret the relationship as `many-to-one`, which means that many rows in the Explore can have one row in the joined view. Not all joins have this type of relationship, and joins with other relationships need to be declared properly.

For a complete understanding, see the [`relationship`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship) parameter documentation page.

## Examples

Join the view named `customer` to the Explore named `order` where the join relationship is

`FROM order LEFT JOIN customer ON order.customer_id = customer.id`:
    
    
    explore: order {
      join: customer {
        foreign_key: customer_id
        relationship: many_to_one # Could be excluded since many_to_one is the default
        type: left_outer          # Could be excluded since left_outer is the default
      }
    }
    

Join the view named `address` to the Explore named `person` where the join relationship is

`FROM person LEFT JOIN address ON person.id = address.person_id` `AND address.type = 'permanent'`:
    
    
    explore: person {
      join: address {
        sql_on: ${person.id} = ${address.person_id} AND ${address.type} = 'permanent' ;;
        relationship: one_to_many
        type: left_outer # Could be excluded since left_outer is the default
      }
    }
    

Join the view named `member` to the Explore named `event` where the join relationship is

`FROM event INNER JOIN member ON member.id = event.member_id`:
    
    
    explore: event {
      join: member {
        sql_on: ${event.member_id} = ${member.id} ;;
        relationship: many_to_one # Could be excluded since many_to_one is the default
        type: inner
      }
    }
    

## Common challenges

### `join` must use view names and not underlying table names

The `join` parameter only takes a view name, not the table name associated with that view. Often the view name and table name are identical, which may lead to the false conclusion that table names can be used.

### Some types of measures require symmetric aggregates

If you are not using symmetric aggregates, most measure types are excluded from joined views. For Looker to support [symmetric aggregates](https://docs.cloud.google.com/looker/docs/working-with-joins#symmetric-aggregates) in your Looker project, your database dialect must also support them. The following table shows which dialects support symmetric aggregates in the latest release of Looker:

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
  
Without symmetric aggregates, join relationships that are not one-to-one can create inaccurate results in aggregate functions. Since Looker measures are aggregate functions, only measures of `type: count` (as `COUNT DISTINCT`) are brought from joined views into the Explore. If you do have a one-to-one join relationship, you can use the [`relationship`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship) parameter to force the other measure types to be included, like this:
    
    
    explore: person {
      join: dna {
        sql_on: ${person.dna_id} = ${dna.id} ;;
        relationship: one_to_one
      }
    }
    

The reasons that Looker works this way (for dialects that don't support symmetric aggregates) are discussed in more detail in [The problem of SQL fanouts](https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220) Community post.

## Things to know

### You can join the same table more than once using `from`

In cases where a single table contains different types of entities, it is possible to join a view to an Explore more than once. To do so you'll need to use the [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-from) parameter. Suppose you had an `order` Explore and needed to join a `person` view to it twice: once for the customer and once for the customer service representative. You might do something like this:
    
    
    explore: order {
      join: customer {
        from: person
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
      join: representative {
        from: person
        sql_on: ${order.representative_id} = ${representative.id} ;;
      }
    }
    

### Don't apply business logic in joins if possible

The standard Looker approach to joining is to use a `LEFT JOIN` whenever possible. Consider a different approach if you find yourself doing something along these lines:
    
    
    explore: member_event {
      from: event
      always_join: [member]
      join: member {
        sql_on: ${member_event.member_id} = ${member.id} ;;
        type: inner
      }
    }
    

In this example we've created an Explore that _only_ looks at events associated with known members. However, the preferred way to execute this in Looker would be to use a `LEFT JOIN` to get event data and member data stuck together, like this:
    
    
    explore: event {
      join: member {
        sql_on: ${event.member_id} = ${member.id} ;;
      }
    }
    

Then you would create a dimension that you could set to `yes` or `no`, if you only wanted to look at member events, like this:
    
    
    dimension: is_member_event {
      type: yesno
      sql: ${member.id} IS NOT NULL ;;
    }
    

This approach is preferable because it gives users the flexibility to look either at all events, or at only member events, as they desire. You have not forced them to look only at member events via the join.

### If not using symmetric aggregates, avoid joins that cause fanouts

> This section only applies to database dialects that don't support [symmetric aggregates](https://docs.cloud.google.com/looker/docs/working-with-joins#symmetric-aggregates). See the discussion of symmetric aggregates in the Common challenges section on this page to determine if your dialect supports symmetric aggregates.

If your database dialect doesn't support [symmetric aggregates](https://docs.cloud.google.com/looker/docs/working-with-joins#symmetric-aggregates), you should avoid joins that result in a fanout. In other words, joins that have a one-to-many relationship between the Explore and view should generally be avoided. Instead, aggregate the data from the view in a [derived table](https://docs.cloud.google.com/looker/docs/derived-tables) in order to establish a one-to-one relationship with the Explore, then join that derived table into the Explore.

This important concept is further explained in the Community post [The problem of SQL fanouts](https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
