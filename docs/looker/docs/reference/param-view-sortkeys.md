---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys/
title: sortkeys \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:31.760045+00:00
---

# sortkeys  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sortkeys Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: my_view {
      derived_table: {
        sortkeys: ["date"]
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `sortkeys` \- or - [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) [`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) `sortkeys` |  Default Value None Accepts The names of one or more columns in a PDT or an aggregate table Special Rules `sortkeys` is supported only on specific dialects  
---|---  
  
## Definition

The `sortkeys` parameter lets you specify one or more columns of a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) (PDT) or an [aggregate table](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) on which to apply a regular sort key. Use a sort key to specify the columns of a PDT that will be most frequently sorted by to make querying the data faster.

> See the Dialect support for `sortkeys` section for the list of dialects that support `sortkeys`.

You can also create an interleaved sort key by using [`indexes`](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes) instead. You cannot use both at the same time, but at least one is required.

> The `sortkeys` parameter works only with tables that are [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#adding_persistence), such as PDTs and aggregate tables. `sortkeys` is not supported for [derived tables](https://docs.cloud.google.com/looker/docs/creating-ndts) without a persistence strategy.
> 
> In addition, the `sortkeys` parameter is not supported for derived tables that are defined using [`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) or [`sql_create`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create).

Generally speaking, a sort key should be applied to date or time columns in the table, and possibly to columns that will be used frequently as filters. More information can be found in the [Amazon Redshift documentation](http://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key.html).

## Examples

These examples assume that you are working with a Redshift database so that you can use the `sortkeys` parameter.

Create a `customer_day_facts` persistent [native derived table](https://docs.cloud.google.com/looker/docs/creating-ndts) that has a sortkey on `date` and rebuilds when the [datagroup](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#using_a_datagroup_for_a_pdt) `order_datagroup` is triggered:
    
    
    view: customer_day_facts {
      derived_table: {
        explore_source: order {
          column: customer_id { field: order.customer_id }
          column: date { field: order.order_date }
          column: num_orders { field: order.customer_order_count }
        }
        datagroup_trigger: order_datagroup
        sortkeys: ["date"]
      }
    }
    

Create a `customer_day_facts` derived table that is based on a SQL query and has a sortkey on `date`:
    
    
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
        sortkeys: ["date"]
      }
    }
    

Create a `customer_day_facts` derived table that is based on a SQL query with a sortkey on `date` and `customer_id`:
    
    
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
        sortkeys: ["date", "customer_id"]
      }
    }
    

## Dialect support for `sortkeys`

The ability to use `sortkeys` depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support `sortkeys`:

> Traditional SQL dialects (such as MySQL and Postgres) should use [`indexes`](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes); `sortkeys` will not work with these databases.

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
