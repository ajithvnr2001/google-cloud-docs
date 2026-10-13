---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-indexes/
title: indexes \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:30.906307+00:00
---

# indexes  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  indexes Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: my_view {
      derived_table: {
        indexes: ["order_id"]
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `indexes` \- or - [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) [`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) `indexes` |  Default Value None Accepts The names of one or more columns in a PDT or an aggregate table Special Rules `indexes` is supported only on specific dialects  
---|---  
  
## Definition

The `indexes` parameter lets you apply indexes to the columns of a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) (PDT) or an [aggregate table](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table). When you add more than one column, Looker will create one index for each column that you specify; it does not create a single, multi-column index. If the `indexes` parameter is missing from the query, Looker will warn you to add an `indexes` parameter to improve query performance. Learn more about indexing persistent derived tables on the [Derived tables in Looker](https://docs.cloud.google.com/looker/docs/derived-tables#query-performance-and-persistence) documentation page.

> See the Dialect support for `indexes` section on this page for the list of dialects that support `indexes`.
> 
> The `indexes` parameter works only with tables that are [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#adding_persistence), such as PDTs and aggregate tables. `indexes` is not supported for [derived tables](https://docs.cloud.google.com/looker/docs/creating-ndts) without a persistence strategy.
> 
> In addition, the `indexes` parameter is not supported for derived tables that are defined using [`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) or [`sql_create`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create).

If you use `indexes` with Redshift, you will create an interleaved sort key. You can also create regular sort keys using [`sortkeys`](https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys), but you cannot use both at the same time. Distribution keys can be created with [`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution).

Generally speaking, indexes should be applied to primary keys and date or time columns.

## Examples

For a traditional database (for example, MySQL or Postgres), create a `customer_order_facts` persistent derived table. The PDT should rebuild when the `order_datagroup` [datagroup](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#using_a_datagroup_for_a_pdt) is triggered and will have an index on `customer_id`:
    
    
    view: customer_order_facts {
      derived_table: {
        explore_source: order {
          column: customer_id { field: order.customer_id }
          column: lifetime_orders { field: order.lifetime_orders }
        }
        datagroup_trigger: order_datagroup
        indexes: ["customer_id"]
      }
    }
    

For a traditional database, create a `customer_order_facts` persistent derived table that is based on a SQL query and applies an index on `customer_id`:
    
    
    view: customer_order_facts {
      derived_table: {
        sql:
          SELECT
            customer_id,
            COUNT(*) AS lifetime_orders
          FROM
            order
          GROUP BY
            customer_id ;;
        persist_for: "24 hours"
        indexes: ["customer_id"]
      }
    }
    

For a traditional database, create a `customer_day_facts` derived table with indexes on both `customer_id` and `date`:
    
    
    view: customer_day_facts {
      derived_table: {
        sql:
          SELECT
            customer_id,
            DATE(order_time) AS date,
            COUNT(*) AS num_orders
          FROM
            order
          GROUP BY
            customer_id ;;
        persist_for: "24 hours"
        indexes: ["customer_id", "date"]
      }
    }
    

For a Redshift database, create a `customer_day_facts` derived table with an interleaved sort key built from `customer_id` and `date`:
    
    
    view: customer_day_facts {
      derived_table: {
        sql:
          SELECT
            customer_id,
            DATE(order_time) AS date,
            COUNT(*) AS num_orders
          FROM
            order
          GROUP BY
            customer_id ;;
        persist_for: "24 hours"
        indexes: ["customer_id", "date"]
      }
    }
    

## Dialect support for `indexes`

The ability to use `indexes` depends on the database dialect your Looker connection is using. If you are working with something other than a traditional database (for example, MySQL or Postgres), your database may not support the `indexes` parameter. Looker will warn you if this is the case. You can swap out the `indexes` parameter for one that is appropriate for your database connection. Learn more about such parameters on the [View parameters](https://docs.cloud.google.com/looker/docs/reference/param-view) documentation page.

In the latest release of Looker, the following dialects support `indexes`:

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
