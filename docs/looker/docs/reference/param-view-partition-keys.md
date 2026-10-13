---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-partition-keys/
title: partition_keys \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:31.887651+00:00
---

# partition_keys  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-partition-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  partition_keys Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      derived_table: {
        partition_keys: [ "created_date" ]
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `partition_keys` \- or - [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) [`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) `partition_keys` |  Default Value `None` Accepts One or more partitioned column names Special Rules `partition_keys` is supported only on specific dialects  
---|---  
  
## Definition

The `partition_keys` parameter supports database dialects that have the ability to partition columns. When a query is run that is filtered on a partitioned column, the database will scan only those partitions that include the filtered data, rather than scanning the entire table. Because a smaller subsection of the table is being scanned, this can significantly reduce the time and cost of querying large tables when the appropriate partition and filter are specified.

> The `partition_keys` parameter works only with tables that are [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#adding_persistence), such as PDTs and aggregate tables. `partition_keys` is not supported for [derived tables](https://docs.cloud.google.com/looker/docs/creating-ndts) without a persistence strategy.
> 
> In addition, the `partition_keys` parameter is not supported for derived tables that are defined using [`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) or [`sql_create`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create).

When you create a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) (PDT) or an [aggregate table](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table), if your underlying database table uses partitioning, Looker can use that partitioning.

> See the Dialect support for `partition_keys` section for the list of dialects that support `partition_keys`.

To add a partitioned column to a PDT or an aggregate table, use `partition_keys` and supply the names of the corresponding columns that are partitioned in the database table.

## Examples

Create a `customer_day_facts` PDT on a BigQuery database with a partition key on the `date` column:
    
    
    view: customer_order_facts {
      derived_table: {
        explore_source: order {
          column: customer_id { field: order.customer_id }
          column: date { field: order.order_time }
          derived_column: num_orders {
            sql: COUNT(order.customer_id) ;;
          }
        }
        partition_keys: [ "date" ]
        datagroup_trigger: daily_datagroup
      }
    }
    

Create a `customer_day_facts` SQL-based derived table on a Presto database with partition keys on the `date` and `state` columns:
    
    
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
        partition_keys: [ "date", "state" ]
        datagroup_trigger: daily_datagroup
      }
    }
    

## Dialect support for `partition_keys`

The ability to use `partition_keys` depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support `partition_keys`:

> In BigQuery, partitioning can be used on only one table column, which must be a [date/time column](https://cloud.google.com/bigquery/docs/creating-column-partitions#creating_a_partitioned_table_from_a_query_result) — so a Looker PDT based on a BigQuery table can use partitioning on only one date/time column.

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
