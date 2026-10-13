---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-table-format/
title: table_format \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:33.424889+00:00
---

# table_format  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-table-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  table_format Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: my_view {
      derived_table: {
        table_format: PARQUET
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `table_format` |  Default Value `PARQUET` Accepts `PARQUET`, `ORC`, `AVRO`, `JSON`, or `TEXTFILE` Special Rules `table_format` is supported only on specific dialects  
---|---  
  
## Definition

The `table_format` parameter specifies the format that a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) (PDT) will have in an Athena database, which can be one of the following:

  * Parquet
  * Optimized Row Columnar (ORC)
  * Avro
  * JavaScript Object Notation (JSON)
  * Text file



See the [Amazon Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/considerations-ctas.html) for details.

> See the Dialect support for `table_format` section for the list of dialects that support `table_format`.

> The `table_format` parameter works only with tables that are [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#adding_persistence), such as PDTs and aggregate tables. `table_format` is not supported for [derived tables](https://docs.cloud.google.com/looker/docs/creating-ndts) without a persistence strategy.

## Examples

Create a `customer_order_facts` PDT on an Amazon Athena database using ORC format:
    
    
    view: customer_order_facts {
      derived_table: {
        explore_source: order {
          column: customer_id { field: order.customer_id }
          column: date { field: order.order_time }
          column: city { field: users.city }
          column: age_tier { field: users.age_tier }
          derived_column: num_orders {
            sql: COUNT(order.customer_id) ;;
          }
        }
        table_format: ORC
        table_compression: SNAPPY
        datagroup_trigger: daily_datagroup
      }
    }
    
    

## Dialect support for `table_format`

The ability to use `table_format` depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support `table_format`:

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
